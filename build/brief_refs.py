# -*- coding: utf-8 -*-
"""References of the 96 technology briefs, on the report's canon (build/sources.py, report §9).

Each brief keeps its own list: IEEE entries numbered in order of first citation in the English brief text (all text outside
the Sources list, the sections after it included); the Russian brief uses the same numbers and the same entries (a
bibliography is not translated). One work = one entry (a preprint and its published version, a work listed twice); an
entry never cited is dropped. A work already in the report's bibliography (data/sources.json) is referenced there
("report:CODE#i"), never copied; every other work has its record in data/brief-sources.json:

    {"works":  {key: record},                         # same schema as data/sources.json
     "briefs": {bid: [{"work": key | "report:S2#0", "grade": "D"}, ...]}}   # in number order: entry n = item n-1

The md Sources section is derived from those records: plain-text IEEE lines "[n] … [grade]" (the text form of
sources.ieee(): journal names in *italics*, DOI and arXiv ids as links, URLs bare). Lines of a Sources section that are not
numbered entries (research notes such as "[G] …", "General facts cited above: …") are kept as they are, after the list.

    python3 build/brief_refs.py --migrate           # one-time: works, renumbering of EN+RU text, data file, md lists
    python3 build/brief_refs.py --merge-verified [DIR]   # fold verified records (DIR/out_*.json) into the data file
    python3 build/brief_refs.py --write             # regenerate every md Sources list from the data file
    python3 build/brief_refs.py --check             # lists == data, citations == entries, numbering, RU == EN
"""
import glob, json, os, re, sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S

ROOT = S.ROOT
DATA = os.path.join(ROOT, 'data', 'brief-sources.json')
HEAD = {'en': '## Sources', 'ru': '## Источники'}
# editor's decisions on wrong or split works (24 Sep 2026, triage of the verification notes)
FR = 'https://www.federalregister.gov/documents/2024/09/06/2024-19633/'
SAME_WORK = {FR + 'commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent':
             FR + 'implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and',
             FR + 'commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies':
             FR + 'implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and'}   # one rule, FR Doc 2024-19633
SPLIT = {('ro_fluor', '14'): 'doi:10.1364/optica.400751'}   # Reddy et al. (Optica 2020) carried Wu et al.'s DOI (ro_spd [1])
QW_B = 'https://quantware.com/news/quantware-raises-178-million'
FIX_TO = {'doi:10.1038/s41377-025-02031-5': 'doi:10.1364/optica.400751',
          'https://quantware.com/product/peripherals': QW_B}   # the fix record of a split key belongs to the split-off work
AS_CITED = 'https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape'   # PatSnap "as cited in the main report"
KINDS = {'article': 'journal', 'press': 'web', 'software': 'web'}
CITE_SPLIT = {('ro_disp', '6'): (re.compile(r'Series B|\$178'), '6s', QW_B)}   # the Series B row cites the release, the TWPA sentence the product page
RECORD_FIX = {   # values the independent re-check read from OpenAlex (24 Sep 2026); None removes the field
    'doi:10.1038/s41534-024-00944-4': {'date': '2025-01-07', 'pubdate': None},   # de Graaf, npj Quantum Inf. 11 (1): Jan. 2025
    'doi:10.1109/tqe.2025.3580377': {'date': '2025'},                           # van Staveren, IEEE TQE 6, 1-18: 2025
    # the product page read by the web pass (out_web_8: Crescendo TWPA confirmed); its one unconfirmed claim, the Series B,
    # now cites the QuantWare release (CITE_SPLIT), so the page record stands for the TWPA sentence
    'https://quantware.com/product/peripherals': {'title': 'Peripherals | Crescendo TWPA', 'site': 'QuantWare', 'verified': True},
}
RENAME = {'arxiv:2408.13687': 'arxiv:2402.15644'}   # the key named a different paper (McEwen et al. is arXiv:2402.15644)
FIELDS = ('authors', 'etal', 'n_authors', 'org', 'title', 'journal', 'volume', 'issue', 'pages', 'article', 'date', 'pubdate', 'doi', 'arxiv',
          'kind', 'site', 'publisher', 'edition', 'section', 'url', 'also', 'retraction', 'verified')
ENTRY = re.compile(r'^(?:\[(\d{1,3}[a-z]?)\]|(\d{1,3})\.)\s+(.*)$')
CITE = re.compile(r'(?<![\[\w:])\[(\d{1,3}[a-z]?)\](?![\](])')   # a bare [n]: not [[4,2,2]], not [G:…], not a md link
MAP = OrderedDict([('authors', ['R. Neeman']), ('title', 'Quantum Technology Map'), ('kind', 'report'), ('edition', '2026.09 (beta)'),
                   ('publisher', 'Qodeh'), ('date', '2026-09')])


# ---------- md
def read(p):
    with open(p, encoding='utf-8', newline='') as f: return f.read()


def write(p, s):
    with open(p, 'w', encoding='utf-8', newline='\n') as f: f.write(s)


def split(s, lang):
    """→ (pre, body_lines, post): pre ends with the heading line and its newline; post starts at the next '## ' heading."""
    h = '\n' + HEAD[lang] + '\n'; i = s.find(h)
    if i < 0: return None
    a = i + len(h); j = s.find('\n## ', a)
    body = s[a:] if j < 0 else s[a:j + 1]
    return s[:a], body.split('\n')[:-1] if body.endswith('\n') else body.split('\n'), ('' if j < 0 else s[j + 1:])


def entries(body):
    """→ ([(label, text)], extra lines (non-blank, not entries), trailing blank-line count)"""
    ents, extra = [], []
    for l in body:
        m = ENTRY.match(l)
        if m: ents.append((m.group(1) or m.group(2), m.group(3).strip()))
        elif l.strip(): extra.append(l)
    trail = 0
    for l in reversed(body):
        if l.strip(): break
        trail += 1
    return ents, extra, trail


def cites(text):
    """in-text citations in order → [label…]; a range [a]–[b] of the IEEE form stands for a..b"""
    out, prev = [], None
    for m in CITE.finditer(text):
        lab = m.group(1)
        if prev is not None and text[prev.end():m.start()] == '–' and lab.isdigit() and prev.group(1).isdigit():
            out += [str(k) for k in range(int(prev.group(1)) + 1, int(lab))]
        out.append(lab); prev = m
    return out


def runs(text):
    """maximal runs of adjacent bare citations → [(start, end, [label…])]"""
    ms = list(CITE.finditer(text)); out = []
    for m in ms:
        if out and out[-1][1] == m.start(): out[-1][1] = m.end(); out[-1][2].append(m.group(1))
        else: out.append([m.start(), m.end(), [m.group(1)]])
    return out


def run_text(nums):
    ns = sorted(set(nums)); rs = []
    for n in ns:
        if rs and n == rs[-1][1] + 1: rs[-1][1] = n
        else: rs.append([n, n])
    return ', '.join('[%d]' % a if a == b else ('[%d], [%d]' % (a, b) if b == a + 1 else '[%d]–[%d]' % (a, b)) for a, b in rs)


# ---------- records
def ids_of_line(rec):
    ids = []
    if rec.get('doi'): ids.append('doi:' + rec['doi'].lower().rstrip('.'))
    if rec.get('arxiv'): ids.append('arxiv:' + rec['arxiv'])
    for u in rec.get('urls', []) or ([rec['url']] if rec.get('url') else []):
        ids.append('u:' + S.norm(u))
        if S.arxiv_of(u): ids.append('arxiv:' + S.arxiv_of(u))
        if S.doi_of(u): ids.append('doi:' + S.doi_of(u).lower())
    return ids


def ids_of_record(r):
    ids = []
    if r.get('doi'): ids.append('doi:' + r['doi'].lower().rstrip('.'))
    if r.get('arxiv'): ids.append('arxiv:' + r['arxiv'])
    for u in [r.get('url', '')] + list(r.get('also', [])):
        if not u: continue
        ids.append('u:' + S.norm(u))
        if S.arxiv_of(u): ids.append('arxiv:' + S.arxiv_of(u))
        if S.doi_of(u): ids.append('doi:' + S.doi_of(u).lower())
    return ids


def report_index():
    idx = {}
    for c, rs in S.load_json().items():
        for i, r in enumerate(rs):
            for k in ids_of_record(r): idx.setdefault(k, 'report:%s#%d' % (c, i))
    return idx


SAME = re.compile(r'^Same work\b[,:;]?\s*', re.I)
PH = '\x00'


def parse(line):
    """sources.parse_line, and a 'Same work, <venue> …' line read as a venue line (no author, no title of its own)"""
    if SAME.match(line): return S.parse_line('%s · "%s" · %s' % (PH, PH, SAME.sub('', line)))
    return S.parse_line(line)


def record_from_lines(lines):
    """best-effort record (verified: false) from a work's source lines, the published version first"""
    recs = [parse(l) for l in lines]
    def rank(x): return (x.get('kind') == 'journal', bool(x.get('volume')), not S.arxiv_of(x.get('url', '')), bool(x.get('title')))
    recs.sort(key=rank, reverse=True)
    b = dict(recs[0]); r = OrderedDict()
    if b.get('title') == PH:
        o = next((x for x in recs[1:] if x.get('title') != PH), {})
        for k in ('authors', 'etal', 'org', 'title'): b.pop(k, None)
        b.update({k: o[k] for k in ('authors', 'etal', 'org', 'title') if o.get(k)})
    for k in ('authors', 'etal', 'org', 'title', 'journal', 'volume', 'issue', 'pages', 'date', 'doi', 'arxiv', 'kind'):
        if b.get(k): r[k] = b[k]
    for o in recs[1:]:
        for k in ('doi', 'arxiv', 'date'):
            if o.get(k) and not r.get(k): r[k] = o[k]
    if r.get('kind') == 'web': r['site'] = b.get('venue') or S.host(b.get('url', ''))
    urls = []
    for o in recs:
        for u in o.get('urls', []):
            if u not in urls: urls.append(u)
    if urls:
        r['url'] = urls[0]
        also = [u for u in urls[1:] if not S.arxiv_of(u) and not (r.get('doi') and 'doi.org' in u)]
        if also: r['also'] = also
    r['kind'] = r.get('kind') or ('journal' if r.get('doi') else 'preprint' if r.get('arxiv') else 'web')
    if r.get('journal'): r['journal'] = S.JOURNALS.get(r['journal'], r['journal'])
    r['verified'] = False
    return OrderedDict((k, r[k]) for k in FIELDS if k in r)


def map_record(section):
    r = OrderedDict(MAP); r['section'] = section; r['verified'] = True
    return r


# ---------- rendering (text form of sources.ieee())
def _a(m):
    href, text = m.group(1), m.group(2)
    return text if text == href else '[%s](%s)' % (text, href)


def html_to_md(h):
    h = re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', _a, h)
    h = re.sub(r'</?i>', '*', h)
    h = re.sub(r'<[^>]+>', '', h)
    return h.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')


def entry_html(r):
    """IEEE entry (HTML) of a record; the Map's self-reference carries its edition and section."""
    if r.get('kind') == 'report' and r.get('section'):
        sec = r['section']
        return '%s, “%s,” ed. %s, %s, %s, §%s.' % (S.author_text(r), S.title_text(r), S.esc(r.get('edition', '')), S.esc(r.get('publisher', '')),
                                                  S.fmt_date(r.get('date', ''), day=False), S.esc(sec))
    if r.get('kind') == 'regulation':    # a rule in the Federal Register: organisation, title, register, volume, page, date, URL
        seg = [x for x in ('<i>%s</i>' % S.esc(r['journal']) if r.get('journal') else '', ('vol. ' + S.esc(r['volume'])) if r.get('volume') else '',
                           ('p. ' + S.esc(r['pages'])) if r.get('pages') else '', S.fmt_date(r.get('date', ''))) if x]
        h = '%s, “%s,” %s.' % (S.author_text(r), S.title_text(r), ', '.join(seg))
        if r.get('url'): h += ' [Online]. Available: ' + S._link(r['url'])
        return h
    h = S.ieee(r)
    if S.journal_name(r) == 'Optica' and re.fullmatch(r'\d+', r.get('pages') or ''):   # page-numbered; only the first page confirmed
        h = h.replace('Art. no. ' + r['pages'], 'p. ' + r['pages'], 1)
    x = r.get('retraction')
    if x:     # IEEE: the retraction notice follows the retracted work
        h += ' Retracted: <i>%s</i>, vol. %s, p. %s, %s, doi: %s.' % (S.esc(x['journal']), S.esc(x['volume']), S.esc(x['pages']), S.fmt_date(x['date'], day=False),
                                                                    S._link('https://doi.org/' + x['doi'], x['doi']))
    return h


_REPORT = {}


def report_record(ref):
    """'report:C#i' → the §9 work (the published version with its preprint merged in, as sources.build() renders it)"""
    if not _REPORT:
        data = S.load_json(); order, works, alias, num, unv = S.build()
        _REPORT['data'], _REPORT['works'] = data, works
    c, i = ref[len('report:'):].split('#'); rec = _REPORT['data'][c][int(i)]
    mine = set(S._ids(rec))
    for w in _REPORT['works'].get(c, []):
        if mine & set(S._ids(w)) or w.get('url') == rec.get('url'): return w
    return rec


def record_of(work, db):
    return report_record(work) if work.startswith('report:') else db['works'][work]


def md_lines(bid, db):
    out = []
    for n, e in enumerate(db['briefs'][bid], 1):
        out.append('[%d] %s%s' % (n, html_to_md(entry_html(record_of(e['work'], db))), (' [%s]' % e['grade']) if e.get('grade') else ''))
    return out


def load():
    with open(DATA, encoding='utf-8') as f: return json.load(f, object_pairs_hook=OrderedDict)


def save(db):
    out = OrderedDict([('works', OrderedDict(sorted(db['works'].items()))), ('briefs', OrderedDict(sorted(db['briefs'].items())))])
    write(DATA, json.dumps(out, ensure_ascii=False, indent=1) + '\n')


def brief_ids():
    return sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT, 'briefs', 'en', '*.md')))


def path(bid, lang): return os.path.join(ROOT, 'briefs', lang, bid + '.md')


def rewrite_section(s, lang, lines):
    pre, body, post = split(s, lang)
    ents, extra, trail = entries(body)
    lead = []
    for l in body:          # blank lines between the heading and the first entry are kept
        if l.strip(): break
        lead.append(l)
    new = lead + lines + extra + [''] * trail
    return pre + '\n'.join(new) + ('\n' if new else '') + post


# ---------- migrate
def migrate(raw_path, vdir=None):
    """Two passes over the untouched briefs: the first assigns keys and applies the verified records in memory, so that
    works sharing an identifier across all briefs and §9 are known; the second numbers, renumbers and writes with them."""
    st, db = _migrate(raw_path, vdir, {}, {}, dry=True)
    alias = unify(db)
    enrich = {c: db['works'][c]['arxiv'] for c in set(alias.values()) if c in db['works'] and db['works'][c].get('arxiv')}
    return _migrate(raw_path, vdir, alias, enrich, dry=False)


def _migrate(raw_path, vdir, alias, enrich, dry):
    raw = json.load(open(raw_path, encoding='utf-8'))
    use = {(b, str(n)): w for w in raw for b, n in w['uses']}
    ridx = {}
    for w in raw:
        for k in ids_of_record({'doi': w.get('doi'), 'arxiv': w.get('arxiv'), 'url': (w.get('urls') or [''])[0], 'also': (w.get('urls') or [])[1:]}):
            ridx.setdefault(k, w['key'])
    rep = report_index()
    db = {'works': OrderedDict(), 'briefs': OrderedDict()}
    lines_of = OrderedDict()                     # new work key → its source lines (all briefs)
    nourl = {}
    st = {'merged': [], 'dropped': [], 'missing': [], 'self': [], 'as_cited': [], 'unparsed': [], 'ru_mismatch': [], 'extra': [],
          'reused': set(), 'new': set(), 'notraw': [], 'split': [], 'same': []}
    for bid in brief_ids():
        s_en, s_ru = read(path(bid, 'en')), read(path(bid, 'ru'))
        sp_en, sp_ru = split(s_en, 'en'), split(s_ru, 'ru')
        if not sp_en or not sp_ru: st['unparsed'].append(bid); continue
        e_en, x_en, _ = entries(sp_en[1]); e_ru, x_ru, _ = entries(sp_ru[1])
        split_cites = {}
        for (b_, lab_), (rx, new_lab, new_key) in CITE_SPLIT.items():
            if b_ != bid: continue
            def sub(t):
                return '\n'.join(re.sub(r'(?<![\[\w:])\[%s\](?![\](])' % lab_, '[%s]' % new_lab, l) if rx.search(l) else l for l in t.split('\n'))
            sp_en = (sub(sp_en[0]), sp_en[1], sub(sp_en[2])); sp_ru = (sub(sp_ru[0]), sp_ru[1], sub(sp_ru[2]))
            split_cites[new_lab] = (lab_, new_key); st['split'].append((bid, lab_ + '→' + new_lab, new_key))
        if x_en: st['extra'].append((bid, len(x_en)))
        if [l for l, _ in e_en] != [l for l, _ in e_ru] or any(set(map(S.norm, re.findall(r'https?://\S+', a))) != set(map(S.norm, re.findall(r'https?://\S+', b)))
                                                              for (_, a), (_, b) in zip(e_en, e_ru)):
            st['ru_mismatch'].append(bid)
        key, grade = {}, {}
        for lab, line in e_en:
            g = S.GRADE_RE.search(line); grade[lab] = g.group(1) if g else ''
            if re.match(r'This report\b', line):
                m = re.search(r'§\s*([\d.]+\d)', line); sec = m.group(1) if m else ''
                k = 'map:§' + sec; st['self'].append((bid, lab, sec))
                db['works'][k] = map_record(sec); key[lab] = k; continue
            if 'as cited in the main report' in line:
                st['as_cited'].append((bid, lab)); key[lab] = AS_CITED; lines_of.setdefault(AS_CITED, []); continue
            if (bid, lab) in SPLIT:
                k = SPLIT[(bid, lab)]; key[lab] = k; lines_of.setdefault(k, [line]); st['split'].append((bid, lab, k)); continue
            w = use.get((bid, lab))
            rec = S.parse_line(line)
            ids = ids_of_line(rec)
            if w is None:
                st['notraw'].append((bid, lab))
                k = next((ridx[i] for i in ids if i in ridx), None)
                if k is None and not rec.get('urls'):     # a line without a URL (e.g. a report cited second-hand): same text, same work
                    k = nourl.setdefault(S.GRADE_RE.sub(' ', line).strip(), 'nourl:%s:%s' % (bid, lab))
                if k is None:
                    k = ('doi:' + rec['doi'].lower()) if rec.get('doi') else ('arxiv:' + rec['arxiv']) if rec.get('arxiv') else (rec['urls'][0] if rec.get('urls') else 'nourl:%s:%s' % (bid, lab))
                    ridx.update({i: k for i in ids})
            else:
                k = w['key']
                if k in SAME_WORK: st['same'].append((bid, lab))
                k = SAME_WORK.get(k, k); k = RENAME.get(k, k)
                if k.startswith('nourl:'): k = nourl.setdefault(S.GRADE_RE.sub(' ', line).strip(), k)
            r = (w or {}).get('report')
            ref = ('report:%s#%d' % (r[0], r[1])) if r else next((rep[i] for i in ids if i in rep), None)
            if ref:
                key[lab] = ref; st['reused'].add(ref); continue
            key[lab] = k; lines_of.setdefault(k, [])
            for l in ((w or {}).get('lines') or []) + [line]:
                if l not in lines_of[k]: lines_of[k].append(l)
        for lab in key: key[lab] = alias.get(key[lab], key[lab])
        for new_lab, (lab_, new_key) in split_cites.items():
            key[new_lab] = new_key; grade[new_lab] = grade.get(lab_, ''); txt_ = dict(e_en)[lab_]
            lines_of.setdefault(new_key, [txt_])
        # one work = one entry within the brief: a 'Same work, …' line joins the line above it; lines sharing a DOI, an
        # arXiv id or a URL are one work (the §9 record wins, else the first line's key)
        labs = [l for l, _ in e_en]; txt = dict(e_en)
        idl = {l: set(ids_of_line(parse(txt[l]))) for l in labs if not key[l].startswith('map:')}
        for i, l in enumerate(labs):
            grp = [m for m in labs[:i] if key[m] != key[l] and (idl.get(l, set()) & idl.get(m, set()))]
            if SAME.match(txt[l]) and i and key[labs[i - 1]] != key[l]: grp.append(labs[i - 1])
            if not grp: continue
            ks = [key[m] for m in grp] + [key[l]]
            k = next((x for x in ks if x.startswith('report:')), ks[0])
            for x in ks:
                if x != k and not x.startswith(('report:', 'map:')):
                    for ln in lines_of.get(x, []):
                        if not k.startswith('report:') and ln not in lines_of[k]: lines_of[k].append(ln)
            for m in labs:
                if key[m] in ks: key[m] = k
        # numbering by first citation in the English text
        text_en = sp_en[0] + sp_en[2]
        new, order = {}, []
        for lab in cites(text_en):
            if lab not in key: st['missing'].append((bid, 'en', lab)); continue
            k = key[lab]
            if k not in new: new[k] = len(order) + 1; order.append((k, lab))
        for lab in cites(sp_ru[0] + sp_ru[2]):
            if lab not in key: st['missing'].append((bid, 'ru', lab))
            elif key[lab] not in new: st['missing'].append((bid, 'ru-only', lab))
        byk = {}
        for lab, _ in e_en: byk.setdefault(key[lab], []).append(lab)
        for new_lab in split_cites: byk.setdefault(key[new_lab], []).append(new_lab)
        for k, labs in byk.items():
            if len(labs) > 1: st['merged'].append((bid, labs))
            if k not in new: st['dropped'].append((bid, labs))
        db['briefs'][bid] = [{'work': k, 'grade': next((grade[l] for l in byk[k] if grade[l]), '')} for k, _ in order]
        for k, _ in order:
            if not k.startswith(('report:', 'map:')): st['new'].add(k)
        # renumber the text, EN and RU
        for lang, s, sp in (('en', s_en, sp_en), ('ru', s_ru, sp_ru)):
            def renum(t):
                out, last = [], 0
                for a, b, labs in runs(t):
                    if any(l not in key or key[l] not in new for l in labs): continue
                    out.append(t[last:a]); out.append(run_text([new[key[l]] for l in labs])); last = b
                out.append(t[last:]); return ''.join(out)
            s2 = renum(sp[0]) + '\n'.join(sp[1]) + ('\n' if sp[1] else '') + renum(sp[2])
            if not dry: write(path(bid, lang), s2)
    for w in raw:
        k = RENAME.get(w['key'], w['key'])
        if k in lines_of and not lines_of[k]: lines_of[k] = list(w['lines'])
    for k, ls in lines_of.items():
        if k in st['new']: db['works'][k] = record_from_lines(ls)
    for k in list(db['works']):
        if not any(e['work'] == k for es in db['briefs'].values() for e in es): del db['works'][k]
    if vdir: apply_verified(db, vdir)
    for c, ax in enrich.items():     # the arXiv id a merged-away record held
        if c in db['works'] and not db['works'][c].get('arxiv'):
            w = db['works'][c]; w['arxiv'] = ax; db['works'][c] = OrderedDict((f, w[f]) for f in FIELDS if f in w)
    if dry: return st, db
    left = unify(db); s9_arxiv()
    if left: raise SystemExit('works still to unify after the second pass: %s' % sorted(left.items())[:5])
    save(db)
    write_all(db)
    return st, db


def write_all(db):
    for bid, es in db['briefs'].items():
        ls = md_lines(bid, db)
        for lang in ('en', 'ru'):
            p = path(bid, lang); s = read(p); s2 = rewrite_section(s, lang, ls)
            if s2 != s: write(p, s2)


def merge_verified(d):
    """Fold the verified records into the data file; idempotent. out_id_*/out_web_* first, then out_redo_* (a second pass
    overrides the first), then out_fix.json ({key, record, reason}: the brief cited the wrong paper or DOI, the record
    replaces the work), then out_final.json. A record with verified:false never replaces anything: the brief-line record stays the fallback."""
    db = load(); before = {k: json.dumps(v, sort_keys=True) for k, v in db['works'].items()}; apply_verified(db, d)
    alias = unify(db); s9_arxiv()
    if alias:     # re-point entries; two entries of one brief becoming one work needs the text renumbered: --migrate
        for bid, es in db['briefs'].items():
            ws = [alias.get(e['work'], e['work']) for e in es]
            if len(set(ws)) != len(ws): raise SystemExit('%s: two entries become one work; re-run --migrate from the original briefs' % bid)
            for e, w in zip(es, ws): e['work'] = w
        for k in list(db['works']):
            if not any(e['work'] == k for es in db['briefs'].values() for e in es): del db['works'][k]
    save(db); write_all(db)
    return sum(1 for k, v in db['works'].items() if before.get(k) != json.dumps(v, sort_keys=True))   # a no-op run reports 0


UNCHECKED = re.compile(r'UNRESOLVED|recollection|from memory|not checked|not re-read', re.I)
CONFIRMABLE = ('title', 'authors', 'journal', 'volume', 'issue', 'pages', 'article', 'date', 'pubdate', 'doi')


def s9_arxiv():
    """write the arXiv ids unify() found for §9 records into data/sources.json (nothing else of a §9 record changes)"""
    if not S9_ARXIV: return
    data = S.load_json(); n = 0
    for ref, ax in sorted(S9_ARXIV.items()):
        c, i = ref[len('report:'):].split('#'); r = data[c][int(i)]
        if not r.get('arxiv'):
            items = list(r.items()); j = next((q + 1 for q, (f, _) in enumerate(items) if f == 'doi'), len(items))
            data[c][int(i)] = OrderedDict(items[:j] + [('arxiv', ax)] + items[j:]); n += 1
    if n:
        write(S.JSON, json.dumps(data, ensure_ascii=False, indent=1)); _REPORT.clear()
    print('§9 records given an arXiv id:', sorted(S9_ARXIV.items()))


def apply_verified(db, d):
    """Fold the verified records into db (in memory) → number of works whose record changed. A record is applied only when it
    was read from a primary record: never when its note says a detail is a recollection, from memory or not checked; a
    PARTIAL record gives only the fields its note says were confirmed; a pubdate inferred from an issue is not applied."""
    start = {k: json.dumps(v, sort_keys=True) for k, v in db['works'].items()}
    batches = [(p, json.load(open(p, encoding='utf-8'))) for p in sorted(glob.glob(os.path.join(d, 'out_id_*.json'))) + sorted(glob.glob(os.path.join(d, 'out_web_*.json')))
               + sorted(glob.glob(os.path.join(d, 'out_redo_*.json')))]
    fx = os.path.join(d, 'out_fix.json')
    if os.path.exists(fx):
        batches.append((fx, [dict(f['record'], key=FIX_TO.get(f['key'], f['key'])) for f in json.load(open(fx, encoding='utf-8'))]))
    fx2 = os.path.join(d, 'out_fix2.json')      # re-pointings of the web triage (a homepage or listing → the release it meant)
    if os.path.exists(fx2):
        batches.append((fx2, [dict(f['record'], key=FIX_TO.get(f['key'], f['key'])) for f in json.load(open(fx2, encoding='utf-8'))]))
    fn = os.path.join(d, 'out_final.json')     # the last pass of the verification
    if os.path.exists(fn): batches.append((fn, json.load(open(fn, encoding='utf-8'))))
    for p in sorted(glob.glob(os.path.join(d, 'out_enrich_*.json'))):     # enrichment of incomplete records
        batches.append((p, json.load(open(p, encoding='utf-8'))))
    for p, rs in batches:
        fix = os.path.basename(p).startswith('out_fix')
        for r in rs:
            k = RENAME.get(r.get('key'), r.get('key'))
            if k not in db['works'] or not r.get('verified'): continue
            note = r.get('note', '') or ''
            enr = os.path.basename(p).startswith('out_enrich_')
            if enr and UNCHECKED.search(note): continue          # an enrichment the note does not vouch for
            if enr and note.startswith('PARTIAL'):
                ok = [f for f in CONFIRMABLE if re.search(r'\b%s\b' % f, note.split('confirmed')[0])]
                w = OrderedDict(db['works'][k]); w.update((f, r[f]) for f in ok if r.get(f))
                if w.get('journal'): w['journal'] = S.JOURNALS.get(w['journal'], w['journal'])
                db['works'][k] = OrderedDict((f, w[f]) for f in FIELDS if f in w); continue
            r = dict(r)
            if enr and re.search(r'pubdate inferred', note): r.pop('pubdate', None)
            r['kind'] = KINDS.get(r.get('kind'), r.get('kind'))
            m = re.search(r'retraction note doi (10\.\S+?) \((.+?) (\d+), (E?\d+), (\d{4}-\d{2}-\d{2})\)', r.get('note', ''))
            if m and re.search(r'\bRETRACTED\b', r.get('note', '')):
                r['retraction'] = OrderedDict([('journal', m.group(2)), ('volume', m.group(3)), ('pages', m.group(4)), ('date', m.group(5)), ('doi', m.group(1))])
            if r.get('journal'): r['journal'] = S.JOURNALS.get(r['journal'], r['journal'])
            if not r.get('arxiv'):     # an old-style arXiv id (quant-ph/0601173) the URL carries
                m = re.search(r'arxiv\.org/(?:abs|pdf)/([a-z\-]+(?:\.[A-Z]{2})?/\d{7})', r.get('url', '') or '')
                if m: r['arxiv'] = m.group(1)
            if r.get('moved_to'): r['url'] = r['moved_to']     # a moved page: its new URL (verified records only reach here)
            if not fix and not r.get('arxiv') and db['works'][k].get('arxiv') and db['works'][k].get('verified'): r['arxiv'] = db['works'][k]['arxiv']
            rec = OrderedDict((f, r[f]) for f in FIELDS if f in r and r[f] not in ('', None, []))
            db['works'][k] = rec
    for k, fx in RECORD_FIX.items():
        if k in db['works']:
            w = OrderedDict(db['works'][k])
            for f, v in fx.items():
                if v is None: w.pop(f, None)
                else: w[f] = v
            db['works'][k] = OrderedDict((f, w[f]) for f in FIELDS if f in w)
    return sum(1 for k, v in db['works'].items() if start.get(k) != json.dumps(v, sort_keys=True))


S9_ARXIV = {}       # §9 record → the arXiv id a verified brief record of the same work holds
POORER_S9 = set()   # §9 records a brief holds in a richer (e.g. published) form: candidates for updating data/sources.json
DISTINCT = {frozenset(('doi:10.1364/optica.400751', 'doi:10.1038/s41377-025-02031-5'))}   # a split is never undone


def _rich(r):
    return (bool(r.get('verified')), r.get('kind') == 'journal', bool(r.get('volume')), bool(r.get('pages') or r.get('article')), bool(r.get('arxiv')))


def unify(db):
    """One work, one key, across all briefs and §9 (the richest record carries it — verified, journal form, volume, pages;
    a §9 record on a tie): works sharing a DOI, an arXiv id, a normalised URL or an also[] URL, or
    the same title by the same first author, are one work. A §9 record wins (it is reused as it is); otherwise the richest record (verified, journal form, volume,
    pages) carries the work and takes the arXiv id another holds. → {key: canonical key} for the keys that change."""
    used = []
    for es in db['briefs'].values():
        for e in es:
            if e['work'] not in used: used.append(e['work'])
    rec = {k: (report_record(k) if k.startswith('report:') else db['works'][k]) for k in used}
    par = {k: k for k in used}
    def find(k):
        while par[k] != k: par[k] = par[par[k]]; k = par[k]
        return k
    owner = {}
    for k in used:
        if k.startswith('map:'): continue
        r = rec[k]; t = S._title_key(r.get('title'))
        who = S._first_author(r) or re.sub(r'\W+', ' ', (r.get('org') or '').lower()).strip()
        tid = ['t:%s|%s' % (t, who)] if len(t) > 20 and who else []     # the same title by the same first author: one work
        for i in ids_of_record(r) + tid:
            if i in owner:
                a, b = find(owner[i]), find(k)
                if a != b and frozenset((a, b)) not in DISTINCT and frozenset((owner[i], k)) not in DISTINCT: par[b] = a
            else: owner[i] = k
    groups = {}
    for k in used: groups.setdefault(find(k), []).append(k)
    alias = {}
    for g in groups.values():
        if len(g) < 2: continue
        canon = max(g, key=lambda k: (_rich(rec[k]), k.startswith('report:')))   # a §9 record wins a tie
        POORER_S9.update((k, canon) for k in g if k.startswith('report:') and k != canon)
        ax = next((rec[k].get('arxiv') for k in g if rec[k].get('arxiv') and rec[k].get('verified')), '')
        if not canon.startswith('report:'):
            c = db['works'][canon]
            if ax and not c.get('arxiv'):
                c['arxiv'] = ax; db['works'][canon] = OrderedDict((f, c[f]) for f in FIELDS if f in c)
        elif ax and not rec[canon].get('arxiv'):     # the §9 record takes the arXiv id too (data/sources.json, the id only)
            S9_ARXIV[canon] = ax
        for k in g:
            if k != canon: alias[k] = canon
    return alias


# ---------- page (build/briefs.py)
_DB = {}


def db_cached():
    if 'db' not in _DB: _DB['db'] = load() if os.path.exists(DATA) else {'works': {}, 'briefs': {}}
    return _DB['db']


def list_html(bid, lang, chip=lambda g: ' [%s]' % g):
    """A brief's list as the page renders it: the §9 IEEE entries, ids brief-<bid>-<lang>-src-<n>, the grade tag after the entry."""
    db = db_cached()
    if bid not in db['briefs']: return None
    out = ['<ol class="refs" data-nohint="1">']
    for n, e in enumerate(db['briefs'][bid], 1):
        out.append('<li id="brief-%s-%s-src-%d" value="%d"><span class="src">[%d]</span> <span class="ref">%s</span>%s</li>'
                   % (bid, lang, n, n, n, entry_html(record_of(e['work'], db)), chip(e['grade']) if e.get('grade') else ''))
    out.append('</ol>')
    return '\n'.join(out)


def key_info(bid):
    """n → {'n', 'label', 'url', 'year', 'short'} for the brief's key references (from the records, not the md line)."""
    db = db_cached(); out = {}
    for n, e in enumerate(db['briefs'].get(bid, []), 1):
        r = record_of(e['work'], db)
        url = r.get('url') or (('https://doi.org/' + r['doi']) if r.get('doi') else ('https://arxiv.org/abs/' + r['arxiv']) if r.get('arxiv') else '')
        au = r.get('authors') or []
        short = (S.initials(au[0]).split()[-1] if au else (r.get('org') or '')).strip()
        if len(short) > 26: short = short[:24].rstrip() + '…'
        m = re.match(r'(\d{4})', r.get('pubdate') or r.get('date') or '')
        out[n] = {'n': n, 'label': re.sub(r'\s+', ' ', html_to_md(entry_html(r)).replace('*', '')), 'url': url, 'year': m.group(1) if m else None, 'short': short}
    return out


# ---------- check
def check():
    db = load(); probs = []
    for bid in brief_ids():
        if bid not in db['briefs']: probs.append('%s: no list in the data file' % bid); continue
        want = md_lines(bid, db); n = len(want)
        for e in db['briefs'][bid]:
            w = e['work']
            if w.startswith('report:'):
                c, i = w[7:].split('#')
                if c not in S.load_json() or int(i) >= len(S.load_json()[c]): probs.append('%s: %s not in data/sources.json' % (bid, w))
            elif w not in db['works']: probs.append('%s: work %s has no record' % (bid, w))
        works = [e['work'] for e in db['briefs'][bid]]
        if len(set(works)) != len(works): probs.append('%s: a work listed twice' % bid)
        for lang in ('en', 'ru'):
            sp = split(read(path(bid, lang)), lang)
            if not sp: probs.append('%s/%s: no Sources section' % (bid, lang)); continue
            ents, extra, _ = entries(sp[1])
            have = ['[%s] %s' % (l, t) for l, t in ents]
            if have != want: probs.append('%s/%s: Sources list differs from the data file' % (bid, lang))
            cs = cites(sp[0] + sp[2])
            for l in cs:
                if not l.isdigit() or not 1 <= int(l) <= n: probs.append('%s/%s: cites [%s], not in the list' % (bid, lang, l))
            for k in range(1, n + 1):
                if str(k) not in cs: probs.append('%s/%s: entry [%d] never cited' % (bid, lang, k))
            if lang == 'en':
                first = []
                for l in cs:
                    if l not in first: first.append(l)
                if [x for x in first if x.isdigit()] != [str(k) for k in range(1, len(first) + 1)]:
                    probs.append('%s: numbers do not ascend by first citation' % bid)
            for a, b, labs in runs(sp[0] + sp[2]):
                if len(labs) > 1: probs.append('%s/%s: adjacent citations not in IEEE run form: %s' % (bid, lang, ''.join('[%s]' % l for l in labs)))
    unv = sorted({e['work'] for es in db['briefs'].values() for e in es if not e['work'].startswith('report:') and not db['works'].get(e['work'], {}).get('verified')})
    return probs, unv


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--migrate' in a:
        raw = a[a.index('--migrate') + 1] if len(a) > a.index('--migrate') + 1 else os.path.join(ROOT, '..', 'refwork', 'works_raw.json')
        vd = os.path.join(ROOT, '..', 'refwork')
        st, db = migrate(raw, vd if os.path.isdir(vd) else None)
        ws = {e['work'] for v in db['briefs'].values() for e in v}
        print('entries', sum(len(v) for v in db['briefs'].values()), 'works', len(ws), 'reused §9', len({w for w in ws if w.startswith('report:')}),
              'new', len({w for w in ws if not w.startswith(('report:', 'map:'))}), 'map self-refs', len({w for w in ws if w.startswith('map:')}))
        print('poorer §9 records (a brief holds the richer form):', sorted(POORER_S9))
        for k in ('split', 'same', 'merged', 'dropped', 'missing', 'self', 'as_cited', 'unparsed', 'ru_mismatch', 'extra', 'notraw'):
            v = st[k]; print(k, len(v), v if k != 'notraw' else sorted({b for b, _ in v}))
    elif '--merge-verified' in a:
        i = a.index('--merge-verified'); d = a[i + 1] if len(a) > i + 1 else os.path.join(ROOT, '..', 'refwork')
        print('records updated', merge_verified(d))
    elif '--write' in a:
        write_all(load())
    elif '--check' in a:
        ps, unv = check()
        for p in ps: print(p)
        print('unverified works (brief-line records, not a failure):', len(unv))
        print('brief references:', 'OK' if not ps else '%d problem(s)' % len(ps))
        sys.exit(1 if ps else 0)
    else:
        print(__doc__)
