# -*- coding: utf-8 -*-
"""Propagation of newly acquired facts to every corner of the Atlas (the editor, 29 Sep 2026: "check completeness of
propagation of the newly acquired information to all corners of the Atlas … design this process for effectiveness").

The process. A research pass ends in a change ledger, data/changes/<date>.json — one item per fact: a machine renamed, its
status changed, a row added or removed, a cell corrected, a builder's statement recorded, a doubt resolved. The facts land
first in the data (the register, the graph); the build then carries them into every GENERATED corner by itself (machines.json,
§8's tables, hypotheses and forecasts, the cards, the record and organisation pages, the Find index). What the build cannot
carry are the HAND-WRITTEN corners: the report's own sections (§0–§6, §9's notes), the architecture narratives of §8.3
(report/paths), the technology briefs, the glossaries, the editions text, the checks that assert names and numbers, README.
This tool walks those corners for every subject of the ledger and prints the checklist — every place the subject is named,
with the line — and flags what contradicts the new fact:

    OLD-NAME    a renamed machine's old name stands alone (without the new name in the same sentence / bracket)
    REMOVED     a row that left the register is still named as a machine
    STATUS      a machine whose register status is now DEPLOYED/DEMONSTRATED/RETIRED is called planned/announced/expected/
                "not yet"/"never delivered" in the same sentence (or the reverse: a planned one called deployed/delivered)
    QUBITS      a number followed by "qubits"/"кубит…" in the same sentence disagrees with the register's physical_qubits_num

    python3 build/audit/propagate.py [data/changes/2026-09-29.json …] [--check] [--all]

--check exits 1 when a flag is raised outside data/changes/allow.json (a list of "file:subject" strings the editor accepted);
--all lists every mention, not only the flagged ones. Without a file argument every ledger in data/changes/ is read.
"""
import csv, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORNERS = (['report/report_EN.md', 'report/report_RU.md', 'report/report_HE.md', 'README.md', 'build/editions.py', 'build/machines_chapter.py',
            'build/make_sections.py', 'build/build_html.py', 'build/cards.py', 'build/map_js.py', 'build/audit/c2_smoke.py', 'build/audit/mobile_check.py',
            'build/audit/vv/test_oracle.py', 'data/glossary-own.json', 'data/glossary-field.json', 'data/graph_data.py', 'data/orgs/organisations.json']
           + sorted(glob.glob(os.path.join(ROOT, 'report', 'paths', '*.md'))) + sorted(glob.glob(os.path.join(ROOT, 'briefs', '*', '*.md'))))
PLANNED_WORDS = re.compile(r'\b(planned|announced|expected|target|not (?:yet )?delivered|never delivered|undelivered|due in|will ship|запланирован\w*|анонсирован\w*|ожидает\w*|не поставлен\w*)\b', re.I)
DELIVERED_WORDS = re.compile(r'\b(deployed|delivered|installed|inaugurated|shipped|in operation|введ[её]н\w*|поставлен\w*|установлен\w*)\b', re.I)


def register():
    p = os.path.join(ROOT, 'data', 'register', 'machines.csv')
    with open(p, encoding='utf-8', newline='') as f: rows = list(csv.DictReader(f))
    return {r['machine_id']: r for r in rows}


def load_ledgers(files):
    items = []
    for f in files:
        d = json.load(open(f, encoding='utf-8'))
        for it in d.get('items', []): it['_ledger'] = os.path.basename(f); items.append(it)
    return items


def terms_of(item, reg):
    """the strings by which the subject is named: current name, old names, aliases, the parenthesised parts of the name"""
    s = item.get('subject', {}); out = set()
    for k in ('name', 'old_name'):
        v = item.get(k)
        if v: out.add(v)
    for v in item.get('aliases', []) or []: out.add(v)
    if s.get('type') == 'machine' and s.get('id') in reg:
        nm = reg[s['id']]['name']; out.add(nm)
        for part in re.findall(r'\(([^)]+)\)', nm):
            for x in re.split(r'\s*/\s*', part):
                if len(x) >= 4: out.add(x.strip())
        out.add(re.sub(r'\s*\([^)]*\)', '', nm).strip())
    v = (item.get('old') or {}).get('name')
    if isinstance(v, str) and 4 <= len(v) <= 80 and item.get('kind') in ('rename', 'remove'): out.add(v)
    return sorted({t for t in out if len(t) >= 4 and not t.lower().startswith('unknown')}, key=len, reverse=True)


def sentences(line):
    return re.split(r'(?<=[.;!?])\s+', line)


def scan(items, reg, show_all=False):
    findings = []   # (flag or '', file, lineno, subject, term, snippet)
    texts = {}
    for c in CORNERS:
        p = c if os.path.isabs(c) else os.path.join(ROOT, c)
        if not os.path.exists(p): continue
        lines = open(p, encoding='utf-8').read().split('\n')
        if re.search(r'report_[A-Z]{2}\.md$', p):   # §7 and §8 of the report are generated from the data by the build: not a hand-written corner
            i = next((k for k, l in enumerate(lines) if re.match(r'## 7\. ', l)), None); j = next((k for k, l in enumerate(lines) if re.match(r'## 9\. ', l)), None)
            if i is not None and j is not None: lines = lines[:i] + [''] * (j - i) + lines[j:]
        texts[os.path.relpath(p, ROOT)] = lines
    for it in items:
        s = it.get('subject', {}); sid = s.get('id', s.get('name', '?')); kind = it.get('kind')
        row = reg.get(sid) if s.get('type') == 'machine' else None
        status = (row or {}).get('status', ''); delivered = bool(re.match(r'(DEPLOYED|DEMONSTRATED|RETIRED)', status)); planned = bool(re.match(r'(PLANNED|ANNOUNCED)', status))
        qn = (row or {}).get('physical_qubits_num', '')
        new_name = (it.get('new') or {}).get('name') or (row or {}).get('name', '')
        old_names = [v for v in [(it.get('old') or {}).get('name'), it.get('old_name')] if v]
        for term in terms_of(it, reg):
            rx = re.compile(r'(?<![\w-])' + re.escape(term) + r'(?![\w-])')
            for f, lines in texts.items():
                for n, line in enumerate(lines, 1):
                    if not rx.search(line): continue
                    for sent in sentences(line):
                        if not rx.search(sent): continue
                        flag = ''
                        mm = rx.search(sent); near = sent[max(0, mm.start() - 90):mm.end() + 90]   # the words around the name, not the whole sentence
                        if kind == 'rename' and term in old_names and new_name and new_name.split(' (')[0] not in sent: flag = 'OLD-NAME'
                        elif kind == 'remove' and it.get('subject', {}).get('type') == 'machine': flag = 'REMOVED'
                        elif row and delivered and PLANNED_WORDS.search(near) and not DELIVERED_WORDS.search(near) and len(sent) < 400: flag = 'STATUS'
                        elif row and planned and DELIVERED_WORDS.search(near) and not PLANNED_WORDS.search(near) and len(sent) < 400: flag = 'STATUS'
                        if row and qn and not flag:
                            m = re.search(re.escape(term) + r'[^.;:]{0,40}?(\d[\d,]*)\s*(?:physical\s+)?(?:qubits?|кубит\w*|q\b)', sent) or re.search(r'(\d[\d,]*)-(?:qubit|кубитн\w*)\s+' + re.escape(term), sent)
                            if m and m.group(1).replace(',', '').isdigit() and int(m.group(1).replace(',', '')) != int(qn): flag = 'QUBITS'
                        if flag or show_all:
                            findings.append((flag, f, n, sid, term, sent.strip()[:160]))
    return findings


def main():
    a = sys.argv[1:]; check = '--check' in a; show_all = '--all' in a
    files = [x for x in a if x.endswith('.json')] or sorted(glob.glob(os.path.join(ROOT, 'data', 'changes', '*.json')))
    files = [f for f in files if not f.endswith('allow.json')]
    items = load_ledgers(files); reg = register()
    allow = set()
    ap = os.path.join(ROOT, 'data', 'changes', 'allow.json')
    if os.path.exists(ap): allow = set(json.load(open(ap, encoding='utf-8')))
    fs = scan(items, reg, show_all)
    HARD = ('OLD-NAME', 'REMOVED')   # the gate: names that must not stand; STATUS and QUBITS are advisory (a reader's glance decides)
    flagged = [x for x in fs if x[0] in HARD and ('%s:%s' % (x[1], x[3])) not in allow]
    print('propagate: %d ledger item(s), %d corner file(s); %d mention(s) listed, %d flagged (%d allowed)' % (
        len(items), len([c for c in CORNERS if os.path.exists(c if os.path.isabs(c) else os.path.join(ROOT, c))]), len(fs), len(flagged), len(fs) - len(flagged) - len([x for x in fs if not x[0]])))
    last = None
    for flag, f, n, sid, term, snip in sorted(fs, key=lambda x: (x[3], x[1], x[2])):
        if (sid, f) != last: print('  %s — %s' % (sid, f)); last = (sid, f)
        print('    %s%s:%d  [%s]  %s' % (('%-9s' % flag) if flag else ' ' * 9, os.path.basename(f), n, term, snip))
    if check and flagged: print('propagate: FAIL — %d flagged mention(s)' % len(flagged)); return 1
    print('propagate: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
