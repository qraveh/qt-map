# -*- coding: utf-8 -*-
"""Apply update proposals to the report (26 Sep 2026 data update): edits to report_EN.md lines, new §9 sources (register line +
data/sources.json record, codes assigned per family prefix), standard records (data/records.json), register field changes
(quantum-machines/data/machines.csv); a job file for the Russian mirror (line, old EN, new EN, current RU line).

    python3 build/report_import.py PROPOSALS.json [PROPOSALS2.json …] [--ru-job OUT.json] [--dry]

A proposals file: {"edits":[{"line","old","new","why"}], "sources":[{"key","prefix","label","record"}], "records":[…],
"machines":[{"machine_id","field","old","new","evidence_url","why"}], "new_machines":[…]}. In `new`, a new source is cited as
[@KEY]; the importer registers the work once (an existing record with the same DOI / arXiv id / URL keeps its code) and writes
[CODE]. Edits whose `old` is not found exactly once on the line are reported and skipped.
"""
import csv, io, json, os, re, sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
import sources as S

EN = os.path.join(ROOT, 'report', 'report_EN.md'); RU = os.path.join(ROOT, 'report', 'report_RU.md'); HE = os.path.join(ROOT, 'report', 'report_HE.md')   # HE optional (29 Sep 2026)
SRC = os.path.join(ROOT, 'data', 'sources.json'); REC = os.path.join(ROOT, 'data', 'records.json')
REG = os.environ.get('QT_MACHINES_DIR') or '/home/claude/work/QT-Map/quantum-machines/data'
FIELDS = ('authors', 'etal', 'n_authors', 'org', 'title', 'journal', 'volume', 'issue', 'pages', 'article', 'date', 'pubdate', 'doi', 'arxiv',
          'kind', 'site', 'publisher', 'url', 'also', 'hint', 'verified')
PH = re.compile(r'\[@([^\]\s]+)\]')


def read_lines(p): return open(p, encoding='utf-8').read().split('\n')
def write_lines(p, ls): open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(ls))


def canon(key):
    if key.startswith('arxiv:'): return ('arxiv', key[6:].strip())
    if key.startswith('doi:'): return ('doi', key[4:].strip().lower().rstrip('.'))
    if key.startswith('u:'):
        u = key[2:].strip()
        if S.arxiv_of(u): return ('arxiv', S.arxiv_of(u))
        if S.doi_of(u): return ('doi', S.doi_of(u).lower().rstrip('.'))
        return ('url', S.norm(u))
    raise SystemExit('unknown key form ' + key)


def existing_code(kind, val, data):
    for c, rs in data.items():
        for r in rs:
            if kind == 'arxiv' and (r.get('arxiv') == val or S.arxiv_of(r.get('url', '') or '') == val): return c
            if kind == 'doi' and ((r.get('doi') or '').lower().rstrip('.') == val or (S.doi_of(r.get('url', '') or '') or '').lower() == val): return c
            if kind == 'url' and S.norm(r.get('url', '') or '') == val: return c
    return None


def next_code(prefix, data, en):
    ns = [int(m.group(1)) for c in data for m in [re.match(prefix + r'(\d+)$', c)] if m]
    ns += [int(x) for x in re.findall(r'\[' + prefix + r'(\d+)\]', '\n'.join(en))]
    return '%s%d' % (prefix, (max(ns) if ns else 0) + 1)


def register_line(lines, prefix):
    """index of the §9 register line that opens with [<prefix>1] (the group's single line)"""
    for i, l in enumerate(lines):
        if l.startswith('[%s1] ' % prefix): return i
    raise SystemExit('no §9 register line for prefix ' + prefix)


BRIEF_WORKS = None
def brief_work(key):
    """the brief-sources record of the same work (by canonical id), so that one work keeps one entry form across §9 and the briefs"""
    global BRIEF_WORKS
    if BRIEF_WORKS is None:
        try: BRIEF_WORKS = json.load(open(os.path.join(ROOT, 'data', 'brief-sources.json'), encoding='utf-8'))['works']
        except Exception: BRIEF_WORKS = {}
    kind, val = canon(key)
    for k, w in BRIEF_WORKS.items():
        if kind == 'arxiv' and (w.get('arxiv') == val or S.arxiv_of(w.get('url', '') or '') == val): return w
        if kind == 'doi' and (w.get('doi') or '').lower().rstrip('.') == val: return w
        if kind == 'url' and S.norm(w.get('url', '') or '') == val: return w
    return None


def make_record(rec, key):
    bw = brief_work(key)
    if bw:
        r = OrderedDict((k, v) for k, v in bw.items() if k in FIELDS)
        for k in ('org', 'site', 'also', 'hint'):
            if rec.get(k) and not r.get(k): r[k] = rec[k]
        r.setdefault('verified', bool(bw.get('verified')))
        return r
    r = OrderedDict()
    for k in FIELDS:
        v = rec.get(k)
        if v in (None, '', [], False) and k != 'verified': continue
        r[k] = v
    kind, val = canon(key)
    if kind == 'arxiv': r.setdefault('arxiv', val); r.setdefault('url', 'https://arxiv.org/abs/' + val)
    if kind == 'doi': r.setdefault('doi', val)
    r.setdefault('kind', 'journal' if r.get('doi') and r.get('journal') else 'preprint' if r.get('arxiv') else 'web')
    if r['kind'] == 'web' and not r.get('site'): r['site'] = S.host(r.get('url', ''))
    if r.get('journal'): r['journal'] = S.JOURNALS.get(r['journal'], r['journal'])
    r['verified'] = bool(rec.get('verified'))
    if not r.get('url'): raise SystemExit('source without url: ' + key)
    return r


def main():
    a = sys.argv[1:]; dry = '--dry' in a
    job_out = a[a.index('--ru-job') + 1] if '--ru-job' in a else None
    files = [x for x in a if x.endswith('.json') and not (job_out and x == job_out)]
    en = read_lines(EN); ru = read_lines(RU)
    data = json.load(open(SRC, encoding='utf-8'), object_pairs_hook=OrderedDict)
    recs = json.load(open(REC, encoding='utf-8'))
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8')); nodes = {n['id'] for n in G['nodes']}; reckeys = set(G['vocab']['RECKEYS'])
    mrows = list(csv.reader(open(os.path.join(REG, 'machines.csv'), encoding='utf-8', newline=''))); mh = mrows[0]; mix = {h: i for i, h in enumerate(mh)}
    codes = {}; job = []; new_machines = []; log = []
    for f in files:
        P = json.load(open(f, encoding='utf-8'))
        # sources first: keys → codes
        for s in P.get('sources', []):
            kind, val = canon(s['key'])
            c = existing_code(kind, val, data)
            if c:
                codes[s['key']] = c; log.append('source %s → existing [%s]' % (s['key'], c)); continue
            c = next_code(s['prefix'], data, en); codes[s['key']] = c
            r = make_record(s.get('record') or {}, s['key'])
            data[c] = [r]
            label = s.get('label') or r.get('title', '')[:90]
            entry = ' · [%s] %s — %s' % (c, label, r['url'])
            for ls in (en, ru):
                i = register_line(ls, s['prefix']); ls[i] = ls[i].rstrip() + entry
            log.append('source %s → new [%s]' % (s['key'], c))
        for e in P.get('edits', []):
            i = e['line'] - 1; line = en[i]
            if line.count(e['old']) != 1:
                log.append('SKIP edit line %d (old found %d×): %s' % (e['line'], line.count(e['old']), e['old'][:60])); continue
            new = PH.sub(lambda m: '[%s]' % codes[m.group(1)] if m.group(1) in codes else m.group(0), e['new'])
            left = PH.findall(new)
            if left: log.append('SKIP edit line %d: unregistered keys %s' % (e['line'], left)); continue
            en[i] = line.replace(e['old'], new)
            job.append({'line': e['line'], 'en_old': e['old'], 'en_new': new, 'ru_line': ru[i], 'why': e.get('why', '')})
            log.append('edit line %d ok' % e['line'])
        for r in P.get('records', []):
            if r.get('node') not in nodes or r.get('key') not in reckeys: log.append('SKIP record %s/%s' % (r.get('node'), r.get('key'))); continue
            recs.append({k: r.get(k, '') for k in ('node', 'key', 'num', 'unit', 'text', 'scope', 'date', 'url', 'tag', 'note')}); log.append('record %s/%s' % (r['node'], r['key']))
        for m in P.get('machines', []):
            row = next((x for x in mrows[1:] if x[mix['machine_id']] == m['machine_id']), None)
            if row is None or m['field'] not in mix: log.append('SKIP machine %s.%s' % (m.get('machine_id'), m.get('field'))); continue
            cur = row[mix[m['field']]]
            if str(m.get('old', '')).strip() and cur.strip() != str(m['old']).strip() and str(m['old']).strip() not in cur:
                log.append('WARN machine %s.%s: current %r ≠ old %r — applied anyway' % (m['machine_id'], m['field'], cur[:60], str(m['old'])[:60]))
            new = m['new']
            if m['field'] == 'flags':
                if isinstance(new, str) and new.strip().startswith('['):
                    import ast; new = ast.literal_eval(new)
                if isinstance(new, list): new = ';'.join(str(x) for x in new)
            row[mix[m['field']]] = str(new); log.append('machine %s.%s ← %s' % (m['machine_id'], m['field'], str(new)[:60]))
        new_machines += P.get('new_machines', [])
    for l in log: print(l)
    if dry: print('dry run — nothing written'); return
    write_lines(EN, en); write_lines(RU, ru)
    with open(SRC, 'w', encoding='utf-8', newline='\n') as fh: json.dump(data, fh, ensure_ascii=False, indent=1); fh.write('\n')
    with open(REC, 'w', encoding='utf-8', newline='\n') as fh: json.dump(recs, fh, ensure_ascii=False, indent=1); fh.write('\n')
    out = io.StringIO(); csv.writer(out, lineterminator='\n').writerows(mrows)
    open(os.path.join(REG, 'machines.csv'), 'w', encoding='utf-8', newline='').write(out.getvalue())
    if job_out:
        json.dump({'edits': job, 'new_machines': new_machines}, open(job_out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('written: %d edits, %d new sources, %d new machines pending' % (len(job), sum(1 for v in log if '→ new [' in v), len(new_machines)))


if __name__ == '__main__':
    main()
