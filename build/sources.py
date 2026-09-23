# -*- coding: utf-8 -*-
"""References of the Quantum Technology Map, canonised in IEEE style (editor's review of 23 Sep 2026).

Two files describe the sources:
  - the report's §9 (report/report_EN.md, mirrored in report_RU.md) is the REGISTER: stable codes ([S2], [X11] …) with the
    URLs they stand for — the codes are what the text cites and what the ids of the rendered entries keep;
  - data/sources.json is the BIBLIOGRAPHY: one record per URL of the register (author list or organisation, title, venue,
    volume/issue/pages, date, DOI, arXiv id), verified against arXiv, Crossref or the page itself.
The page renders §9 as one IEEE-numbered list, numbered in order of first citation in the English text (the Russian edition
uses the same numbers: a bibliography is not translated), and every in-text [CODE] becomes its number(s), linked.
A code whose URLs are different works spans consecutive numbers; a preprint and its published version are one work; a work
cited under two codes keeps its first number.

Forms (IEEE Reference Guide, 2024):
  journal   A. B. Author, C. Author, and D. Author, “Title,” Journal, vol. v, no. n, pp. x–y, Mon. year, doi: …
  preprint  A. B. Author et al., “Title,” arXiv:id, Mon. year.
  online    Organisation, “Title,” Site, Mon. day, year. [Online]. Available: URL
  report    A. Author, “Title,” Publisher, year, doi: …
Seven or more authors → first author et al.  Online sources: the access date is stated once at the head of the list.

    python3 build/sources.py            # summary and a sample
    python3 build/sources.py --skeleton # add records for register URLs that data/sources.json does not hold yet
    python3 build/sources.py --check    # anomalies (unverified records, missing fields, register/bibliography drift)
"""
import glob, json, os, re, sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON = os.path.join(ROOT, 'data', 'sources.json')
EXTRA = os.path.join(ROOT, 'data', 'sources-extra.json')
ACCESSED = 'September 2026'
MON = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
SITES = {'quantumcomputingreport.com': 'Quantum Computing Report', 'thequantuminsider.com': 'The Quantum Insider', 'hpcwire.com': 'HPCwire',
         'nature.com': 'Nature', 'arxiv.org': 'arXiv', 'prnewswire.com': 'PR Newswire', 'businesswire.com': 'Business Wire', 'globenewswire.com': 'GlobeNewswire',
         'postquantum.com': 'PostQuantum', 'quantumzeitgeist.com': 'Quantum Zeitgeist', 'darpa.mil': 'DARPA', 'ibm.com': 'IBM', 'blog.google': 'Google',
         'quantinuum.com': 'Quantinuum', 'ionq.com': 'IonQ', 'quera.com': 'QuEra', 'psiquantum.com': 'PsiQuantum', 'dwavequantum.com': 'D-Wave', 'rigetti.com': 'Rigetti Computing',
         'alice-bob.com': 'Alice & Bob', 'atom-computing.com': 'Atom Computing', 'pasqal.com': 'Pasqal', 'iqm.tech': 'IQM', 'xanadu.ai': 'Xanadu', 'quandela.com': 'Quandela',
         'caltech.edu': 'Caltech', 'seeqc.com': 'SEEQC', 'hrl.com': 'HRL Laboratories', 'fujitsu.com': 'Fujitsu', 'global.fujitsu': 'Fujitsu', 'honeywell.com': 'Honeywell',
         'novonordiskfonden.dk': 'Novo Nordisk Foundation', 'nqcc.ac.uk': 'NQCC', 'journals.aps.org': 'APS', 'science.org': 'Science', 'pubs.acs.org': 'ACS',
         'infleqtion.com': 'Infleqtion', 'quantummotion.com': 'Quantum Motion', 'unsw.edu.au': 'UNSW', 'diraq.com': 'Diraq', 'physics.aps.org': 'APS Physics',
         'quantum.microsoft.com': 'Microsoft', 'oqc.tech': 'OQC', 'aqt.eu': 'AQT', 'eleqtron.com': 'eleQtron', 'nordquantique.com': 'Nord Quantique',
         'quantumcircuits.com': 'Quantum Circuits', 'quixquantum.com': 'QuiX Quantum', 'forbes.com.au': 'Forbes Australia', 'anl.gov': 'Argonne National Laboratory',
         'planqc.eu': 'planqc', 'newsroom.ibm.com': 'IBM Newsroom', 'investors.rigetti.com': 'Rigetti Computing'}
JOURNALS = {'PRL': 'Phys. Rev. Lett.', 'PRX': 'Phys. Rev. X', 'PRA': 'Phys. Rev. A', 'PRB': 'Phys. Rev. B', 'PR Applied': 'Phys. Rev. Appl.', 'PRApplied': 'Phys. Rev. Appl.',
            'PRX Quantum': 'PRX Quantum', 'Nature Communications': 'Nat. Commun.', 'Nat. Commun.': 'Nat. Commun.', 'Nature Physics': 'Nat. Phys.', 'Nature Electronics': 'Nat. Electron.',
            'Nature Nanotechnology': 'Nat. Nanotechnol.', 'Nature Photonics': 'Nat. Photon.', 'Nature Materials': 'Nat. Mater.', 'Science Advances': 'Sci. Adv.',
            'npj Quantum Information': 'npj Quantum Inf.', 'PNAS': 'Proc. Natl. Acad. Sci. USA', 'Physical Review Letters': 'Phys. Rev. Lett.', 'Physical Review X': 'Phys. Rev. X',
            'Physical Review Applied': 'Phys. Rev. Appl.', 'Physical Review A': 'Phys. Rev. A', 'Physical Review B': 'Phys. Rev. B', 'Quantum': 'Quantum', 'Nature': 'Nature', 'Science': 'Science',
            'Proceedings of the National Academy of Sciences': 'Proc. Natl. Acad. Sci. USA', 'Proceedings of the National Academy of Sciences of the United States of America': 'Proc. Natl. Acad. Sci. USA',
            'Nano Letters': 'Nano Lett.', 'Physics': 'Physics', 'Nature Reviews Physics': 'Nat. Rev. Phys.', 'Reviews of Modern Physics': 'Rev. Mod. Phys.',
            'Applied Physics Letters': 'Appl. Phys. Lett.', 'Physical Review Research': 'Phys. Rev. Res.', 'Nature Chemistry': 'Nat. Chem.', 'Science Robotics': 'Sci. Robot.',
            'Journal of Applied Physics': 'J. Appl. Phys.', 'Optica': 'Optica', 'Communications Physics': 'Commun. Phys.', 'IEEE Transactions on Quantum Engineering': 'IEEE Trans. Quantum Eng.'}
DOI_JOURNAL = [('10.1038/s41586', 'Nature'), ('10.1038/s41467', 'Nat. Commun.'), ('10.1038/s41567', 'Nat. Phys.'), ('10.1038/s41565', 'Nat. Nanotechnol.'), ('10.1038/s41928', 'Nat. Electron.'),
               ('10.1038/s41566', 'Nat. Photon.'), ('10.1038/s41534', 'npj Quantum Inf.'), ('10.1103/PhysRevLett', 'Phys. Rev. Lett.'), ('10.1103/PhysRevX', 'Phys. Rev. X'), ('10.1103/PRXQuantum', 'PRX Quantum'),
               ('10.1103/PhysRevApplied', 'Phys. Rev. Appl.'), ('10.1103/PhysRevA', 'Phys. Rev. A'), ('10.1103/PhysRevB', 'Phys. Rev. B'), ('10.1126/science', 'Science'), ('10.1126/sciadv', 'Sci. Adv.'),
               ('10.22331/q-', 'Quantum'), ('10.1073/pnas', 'Proc. Natl. Acad. Sci. USA'), ('10.1021/acs.nanolett', 'Nano Lett.')]


PAGED = {'Nature', 'Science', 'Nat. Phys.', 'Nat. Nanotechnol.', 'Nat. Electron.', 'Nat. Photon.', 'Nat. Mater.', 'Nano Lett.', 'Physics'}   # page-numbered journals
APS_YEAR = {'PhysRevLett': lambda v: str(2023 + (int(v) - 130) // 2) if int(v) >= 130 else '', 'PhysRevX': lambda v: str(2010 + int(v)), 'PRXQuantum': lambda v: str(2019 + int(v))}


def journal_name(r):
    j = (r.get('journal') or '').strip()
    if j: return JOURNALS.get(j, j)
    for pre, name in DOI_JOURNAL:
        if (r.get('doi') or '').startswith(pre): return name
    return ''
JOURNAL_WORDS = ('Nature', 'Science', 'Phys', 'PRX', 'PRL', 'PRA', 'PRB', 'Quantum', 'Commun', 'Lett', 'Rev', 'npj', 'IEEE', 'Proc', 'Optica', 'Electron', 'ISCA', 'ACM', 'Nanotechnol', 'Photon')
DROP = {'X10'}   # register codes never cited in the text: not rendered
CODE = r'[A-Z]{1,2}\d{1,3}'


# ---------- identifiers
def norm(u):
    u = u.rstrip('.;,)')
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', u)
    if m: return 'arxiv:' + m.group(1)
    m = re.search(r'nature\.com/articles/([a-z0-9\-]+)', u)
    if m: return 'nature:' + m.group(1)
    return u.lower().rstrip('/')


def host(u):
    m = re.match(r'https?://([^/]+)', u); h = (m.group(1) if m else '').lower()
    for k, v in sorted(SITES.items(), key=lambda kv: -len(kv[0])):
        if h == k or h.endswith('.' + k): return v
    return h.replace('www.', '')


def doi_of(u):
    m = re.search(r'doi\.org/(10\.\S+)', u)
    if m: return m.group(1).rstrip('.;,)')
    m = re.search(r'nature\.com/articles/([a-z0-9\-]+)', u)
    if m: return '10.1038/' + m.group(1)
    m = re.search(r'journals\.aps\.org/[^/]+/abstract/(10\.\d+/\S+)', u)
    if m: return m.group(1).rstrip('.;,)')
    m = re.search(r'/(10\.\d{4,9}/[^\s?#]+)', u)
    if m and 'science.org' in u: return m.group(1)
    return ''


def arxiv_of(u):
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', u or ''); return m.group(1) if m else ''


# ---------- dates
DATE_FULL = re.compile(r'(?<![\d.])((?:19|20)\d{2})-(\d{2})-(\d{2})(?!\d)')
DATE_YM = re.compile(r'(?<![\d.])((?:19|20)\d{2})-(\d{2})(?![\d-])')
DATE_Y = re.compile(r'(?<![\d:.\-])((?:19|20)\d{2})(?![\d]|\.\d)')
MONTHS = {m.lower().rstrip('.'): i + 1 for i, m in enumerate(MON)}
MONTHS.update({'january': 1, 'february': 2, 'march': 3, 'april': 4, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'sept': 9, 'october': 10, 'november': 11, 'december': 12})
DATE_MY = re.compile(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+(?:(\d{1,2}),?\s+)?((?:19|20)\d{2})\b')


def find_date(s):
    """The most specific ISO date in s (YYYY-MM-DD, YYYY-MM, Mon YYYY, YYYY), preferring text outside parentheses."""
    for t in (re.sub(r'\([^)]*\)', ' ', s), s):
        m = DATE_FULL.search(t)
        if m: return '%s-%s-%s' % m.groups()
        m = DATE_YM.search(t)
        if m: return '%s-%s' % m.groups()
        m = DATE_MY.search(t)
        if m: return '%s-%02d%s' % (m.group(3), MONTHS[m.group(1).lower()], ('-%02d' % int(m.group(2))) if m.group(2) else '')
        m = DATE_Y.search(t)
        if m: return m.group(1)
    return ''


def fmt_date(d, day=True):
    d = (d or '').strip()
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', d)
    if m: return ('%s %d, %s' % (MON[int(m.group(2)) - 1], int(m.group(3)), m.group(1))) if day else ('%s %s' % (MON[int(m.group(2)) - 1], m.group(1)))
    m = re.match(r'(\d{4})-(\d{2})$', d)
    if m: return '%s %s' % (MON[int(m.group(2)) - 1], m.group(1))
    m = re.match(r'(\d{4})', d)
    return m.group(1) if m else d


# ---------- a source line of a brief → record (tolerant: the lines use " · ", " — " or prose separators, a grade tag anywhere)
GRADE_RE = re.compile(r'\s*\[([A-Z])(?::[^\]]*)?\]\s*')


def split_venue(v):
    """'Nature 646 (8087)' → Nature, 646, 8087; 'PRX Quantum 4, 030336' → PRX Quantum, 4, pages 030336; 'PRL 134, 090601'."""
    v = v.strip(' ,;·')
    m = re.match(r'^([A-Za-z][A-Za-z .&]*?)\s*(\d+)\s*(?:\((\d+)\))?(?:,\s*([\w\d–-]+))?\s*$', v)
    if not m: return {'journal': JOURNALS.get(v, v)}
    j = m.group(1).strip(' ,'); r = {'journal': JOURNALS.get(j, j), 'volume': m.group(2)}
    if m.group(3): r['issue'] = m.group(3)
    if m.group(4): r['pages'] = m.group(4)
    return r


def parse_line(line):
    """→ {'authors' or 'org', 'title', 'venue', 'date', 'arxiv', 'doi', 'url', 'urls', 'grade', 'kind'} — best effort."""
    grade = ''
    g = GRADE_RE.search(line)
    if g: grade = g.group(1)
    core = GRADE_RE.sub(' ', line).strip()
    urls = [u.rstrip('.;,)') for u in re.findall(r'https?://\S+', core)]
    text = re.sub(r'\s*[·—–-]?\s*https?://\S+', '', core).strip(' ·—–-;,')
    text = re.sub(r'\s+', ' ', text)
    m = re.search(r'["“](.+?)["”]', text) or re.search(r'\*([^*]+)\*', text)
    if m:
        author = text[:m.start()].strip(' ·—–,:;'); title = m.group(1).strip(' ,.'); rest = text[m.end():]
    else:
        parts = [x.strip() for x in re.split(r'\s[·—]\s', text) if x.strip()]
        if len(parts) >= 3: author, title, rest = parts[0], parts[1], ' · '.join(parts[2:])
        elif len(parts) == 2: author, title, rest = parts[0], parts[1], ''
        else: author, title, rest = '', text, ''
    rest = rest.strip(' ·—–,:;')
    ax = re.search(r'arXiv:\s*(\d{4}\.\d{4,5})', rest) or re.search(r'arXiv:\s*(\d{4}\.\d{4,5})', text)
    arxiv = ax.group(1) if ax else (arxiv_of(urls[0]) if urls else '')
    dm = re.search(r'doi:?\s*(10\.\d{4,9}/[^\s,;)]+)', rest, flags=re.I)
    doi = dm.group(1) if dm else (doi_of(urls[0]) if urls else '')
    date = find_date(rest)
    venue = re.sub(r'\((?:[^)]*(?:arXiv|v\d|\d{4}-\d{2}|accessed)[^)]*)\)', ' ', rest)   # versions, ids, dates in parentheses are not the venue
    venue = re.sub(r'doi:?\s*10\.\d{4,9}/[^\s,;)]+', ' ', venue, flags=re.I)
    venue = re.sub(r'arXiv:\s*\d{4}\.\d{4,5}(?:v\d+)?', ' ', venue)
    for pat in (DATE_FULL, DATE_YM, DATE_MY, DATE_Y): venue = pat.sub(' ', venue)
    venue = re.sub(r'^(?:published(?:\s+in)?|publ\.)\s*', '', venue.strip(' ·—–,:;()'), flags=re.I)
    venue = re.sub(r'\s*[·—–,;]\s*(?=[·—–,;]|$)', '', venue); venue = re.sub(r'\s+', ' ', venue).strip(' ·—–,:;()')
    rec = {'title': title, 'venue': venue, 'date': date, 'arxiv': arxiv, 'doi': doi, 'url': urls[0] if urls else '', 'urls': urls, 'grade': grade}
    author = re.sub(r'\s*\([^)]*\)\s*$', '', author).strip(' ,')   # a trailing affiliation in parentheses is not an author
    if author and (re.search(r',| et al| and |&', author) or re.match(r'^[A-Z][a-zä-ÿ\-]+$', author)) and not any(w in author for w in ('Inc', 'Ltd', 'University', 'Lab', 'Quantum', 'Google', 'IBM', 'Microsoft', 'Report', 'Insider', 'Team')):
        rec['authors'] = [a.strip() for a in re.split(r',\s*|\s+and\s+|\s*&\s*', re.sub(r'\s*et al\.?', '', author)) if a.strip()]
        if 'et al' in author: rec['etal'] = True
    else:
        rec['org'] = author
    if arxiv and not any(w in venue for w in JOURNAL_WORDS): rec['kind'] = 'preprint'
    elif doi or any(w in venue for w in JOURNAL_WORDS): rec['kind'] = 'journal'; rec.update(split_venue(venue) if venue else {})
    else: rec['kind'] = 'web'
    return rec


def brief_records():
    """URL → record, from every brief's source list (English briefs)."""
    recs = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'briefs', 'en', '*.md'))):
        for m in re.finditer(r'^\[(\d+)\]\s+(.*)$', open(f, encoding='utf-8').read(), flags=re.M):
            rec = parse_line(m.group(2).strip())
            for u in rec['urls']: recs.setdefault(norm(u), rec)
    return recs


# ---------- the register: report §9 → codes → [(sublabel, url)]
def parse_register(lang='en'):
    p = os.path.join(ROOT, 'report', 'report_%s.md' % lang.upper()); s = open(p, encoding='utf-8').read()
    head = '## 9. Sources' if lang == 'en' else '## 9. Источники'
    i = s.find(head); body, src = s[:i], s[i:]
    ent = OrderedDict()
    for l in src.split('\n'):
        if not l.strip() or l.startswith('#') or l.startswith('**') or l.startswith('*'): continue
        for part in re.split(r'\s·\s(?=\[' + CODE + r'\])', l):
            m = re.match(r'\[(' + CODE + r')\]\s*(.*)', part.strip())
            if not m: continue
            label = m.group(2).strip(); items = []
            for sub in re.split(r'\s;\s', label):
                us = [u.rstrip('.;,)') for u in re.findall(r'https?://\S+', sub)]
                txt = re.sub(r'\s*[—–-]?\s*https?://\S+', '', sub).strip(' ;—–-')
                if not us and items: items[-1] = (items[-1][0] + '; ' + txt, items[-1][1]); continue
                for k, u in enumerate(us): items.append((txt if k == 0 else '', u))
            ent[m.group(1)] = {'label': label, 'items': items, 'urls': [u for _, u in items]}
    return body, ent


def load_json():
    return json.load(open(JSON, encoding='utf-8'), object_pairs_hook=OrderedDict) if os.path.exists(JSON) else OrderedDict()


def skeleton(write=True):
    """Add a best-effort record for every register URL that data/sources.json does not hold; existing records are kept."""
    body, ent = parse_register('en')
    data = load_json(); briefs = brief_records()
    extra = json.load(open(EXTRA, encoding='utf-8')) if os.path.exists(EXTRA) else {}
    added = 0
    for c, e in ent.items():
        if e['label'].startswith('see [') or c in DROP: continue
        have = {r['url']: r for r in data.get(c, [])}
        out = []
        for sub, u in e['items']:
            if u in have: out.append(have[u]); continue
            ex = next((r for r in extra.get(c, []) if r.get('url') == u), None)
            b = briefs.get(norm(u))
            r = OrderedDict()
            if ex:
                r.update({k: v for k, v in ex.items() if v not in ('', None)})
                if r.get('author') and not r.get('org') and not r.get('authors'): r['org'] = r.pop('author')
            elif b:
                for k in ('authors', 'org', 'title', 'journal', 'volume', 'issue', 'pages', 'date', 'doi', 'arxiv', 'kind'):
                    if b.get(k): r[k] = b[k]
                if b.get('kind') == 'web': r['site'] = b.get('venue') or host(u)
                if b.get('kind') == 'preprint' and b.get('venue') and 'arXiv' not in b['venue']: r['note'] = b['venue']
            else:
                r['org'] = host(u); r['title'] = sub or e['label']; r['kind'] = 'preprint' if arxiv_of(u) else 'web'
                if r['kind'] == 'web': r['site'] = host(u)
            r['url'] = u
            r.setdefault('doi', doi_of(u)); r.setdefault('arxiv', arxiv_of(u))
            if not r.get('doi'): r.pop('doi')
            if not r.get('arxiv'): r.pop('arxiv')
            r.setdefault('kind', 'journal' if r.get('doi') else ('preprint' if r.get('arxiv') else 'web'))
            r['hint'] = sub or e['label']   # the register's descriptive label — what the URL is cited for
            r['verified'] = False
            out.append(r); added += 1
        data[c] = out
    if write:
        json.dump(data, open(JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return data, added


# ---------- works, numbering
def _title_key(t):
    return re.sub(r'\W+', ' ', (t or '').lower()).strip()[:60]


def _first_author(r):
    a = (r.get('authors') or [''])[0]
    return re.sub(r'\W+', ' ', initials(a).split()[-1].lower()) if a else ''


def _preprint_of(a, b):
    """the register lists a preprint next to its published version: one journal record, one preprint, the same first author"""
    kinds = {a.get('kind'), b.get('kind')}
    return kinds == {'journal', 'preprint'} and _first_author(a) and _first_author(a) == _first_author(b)


def _ids(r):
    ids = []
    if r.get('doi'): ids.append('doi:' + r['doi'].lower().rstrip('.'))
    if r.get('arxiv'): ids.append('arxiv:' + r['arxiv'])
    t = _title_key(r.get('title'))
    if t and len(t) > 12: ids.append('t:' + t)
    if not ids: ids.append('u:' + (r.get('url') or '').lower().rstrip('/'))
    return ids


def build():
    """→ (order, works, alias, num, unverified): order = codes by first citation in the EN text; works[code] = [record…]
    (a preprint merged with its published version); num[code] = [number…] (one per work, dedupe across codes)."""
    body, ent = parse_register('en')
    data = load_json()
    alias = {c: re.search(r'see \[(' + CODE + r')\]', e['label']).group(1) for c, e in ent.items() if e['label'].startswith('see [')}
    works = OrderedDict()
    for c, e in ent.items():
        if c in alias or c in DROP: continue
        recs = [dict(r) for r in data.get(c, [])]
        if not recs: recs = [{'org': host(u) if u else '', 'title': sub or e['label'], 'url': u, 'kind': 'web', 'site': host(u)} for sub, u in e['items']] or [{'title': e['label'], 'kind': 'web'}]
        merged = []
        for r in recs:
            m = next((w for w in merged if set(_ids(w)) & set(_ids(r)) or _preprint_of(w, r)), None)
            if m is None: merged.append(r); continue
            # one work: the published version is the entry (the record whose url is the publisher's, when both are journal
            # records), the other record fills what it lacks; the preprint's id stays with it
            def rank(x): return (x.get('kind') == 'journal', not arxiv_of(x.get('url', '')), len([k for k in ('volume', 'pages', 'issue') if x.get(k)]))
            j, p = (r, m) if rank(r) > rank(m) else (m, r)
            for k, v in p.items():
                if k in ('url', 'hint', 'note', 'verified', 'kind') or v in ('', None, []): continue
                j.setdefault(k, v)
            j['arxiv'] = j.get('arxiv') or p.get('arxiv') or arxiv_of(p.get('url', ''))
            if p.get('url') and p['url'] != j.get('url') and not arxiv_of(p['url']) and not (j.get('doi') and 'doi.org' in p['url']): j.setdefault('also', []).append(p['url'])
            if j is not m: merged[merged.index(m)] = j
        works[c] = merged
    order = []
    for c in re.findall(r'\[(' + CODE + r')\]', body):
        c = alias.get(c, c)
        if c in works and c not in order: order.append(c)
    order += sorted(c for c in works if c not in order)
    num, seen, k = {}, {}, 1
    for c in order:
        nums = []
        for r in works[c]:
            hit = next((seen[i] for i in _ids(r) if i in seen), None)
            if hit: nums.append(hit); r['dup'] = True
            else:
                for i in _ids(r): seen[i] = k
                nums.append(k); k += 1
        num[c] = nums
    for a, t in alias.items(): num[a] = num.get(t, [0])
    unverified = [(c, r.get('url')) for c in works for r in works[c] if not r.get('verified')]
    return order, works, alias, num, unverified


# ---------- rendering
def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def initials(name):
    """'Rémi Rousseau' → 'R. Rousseau'; 'S. Harvey Moseley Jr' → 'S. H. Moseley Jr'; 'Rousseau' → 'Rousseau'; 'J. W. Lis' stays."""
    name = name.strip(' ,')
    if not name: return ''
    m = re.match(r'^(.+?)((?:,?\s+(?:Jr|Sr|II|III)\.?)?)$', name); core, suffix = m.group(1), m.group(2)
    parts = core.split()
    if len(parts) == 1: return name
    # 'Family, Given' → 'Given Family'
    if ',' in core:
        fam, giv = [x.strip() for x in core.split(',', 1)]; parts = giv.split() + fam.split()
    last = parts[-1]; given = parts[:-1]
    # particles stay with the family name
    while len(given) > 1 and given[-1].lower() in ('de', 'van', 'von', 'der', 'den', 'da', 'di', 'del', 'la', 'le', 'du', "d'"):
        last = given.pop() + ' ' + last
    ini = ' '.join((g if re.match(r'^[A-ZÀ-Ý]\.(-[A-ZÀ-Ý]\.)?$', g) else re.sub(r'^([A-ZÀ-Ýa-zà-ÿ])[^-]*(?:-([A-ZÀ-Ýa-zà-ÿ])[^-]*)?$', lambda mm: mm.group(1).upper() + '.' + ('-' + mm.group(2).upper() + '.' if mm.group(2) else ''), g)) for g in given)
    return (ini + ' ' + last + suffix).strip()


def author_text(r):
    """IEEE: up to six authors in full, 'A. First et al.' beyond; an organisation as printed."""
    au = [initials(a) for a in r.get('authors', []) if a.strip()]
    org = (r.get('org') or '').strip()
    if not au: return esc(org)
    n = r.get('n_authors') or (7 if len(au) >= 6 else len(au))   # six names and no count: the first six of a longer list
    if n > 6 or r.get('etal'): txt = esc(au[0]) + ' <i>et al.</i>'
    elif len(au) == 1: txt = esc(au[0])
    elif len(au) == 2: txt = esc(au[0]) + ' and ' + esc(au[1])
    else: txt = ', '.join(esc(a) for a in au[:-1]) + ', and ' + esc(au[-1])
    return txt


def _same_name(a, b):
    a = re.sub(r'\b(inc|ltd|llc|corp|co|gmbh|sa|ag|plc)\b\.?', '', (a or '').lower()); b = re.sub(r'\b(inc|ltd|llc|corp|co|gmbh|sa|ag|plc)\b\.?', '', (b or '').lower())
    a = re.sub(r'\W+', ' ', a).strip(); b = re.sub(r'\W+', ' ', b).strip()
    return bool(a) and bool(b) and (a == b or a.startswith(b) or b.startswith(a))


def title_text(r):
    t = (r.get('title') or '').strip().strip('"“”.,').replace('--', '–').replace(' | ', ' — ')
    t = re.sub(r'\s+', ' ', t)
    # quotation marks inside a quoted title become single quotation marks
    t = t.replace('“', '‘').replace('”', '’')
    t = re.sub(r'"([^"]*)"', r'‘\1’', t)
    return esc(t)


def _link(u, text=None):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(u), esc(text or u))


def ieee(r):
    """One work as an IEEE-style entry (HTML, without the number)."""
    kind = r.get('kind', 'web'); parts = []
    au = author_text(r); ti = title_text(r)
    if au: parts.append(au + ',')
    if ti: parts.append('“' + ti + ',”')
    doi = (r.get('doi') or '').rstrip('.'); url = r.get('url', ''); ax = r.get('arxiv', '') or arxiv_of(url)
    if kind == 'journal':
        jn = journal_name(r); j = esc(jn); v = r.get('volume'); n = r.get('issue'); pg = r.get('pages') or r.get('article')
        m = re.match(r'10\.1103/(PhysRevLett|PhysRevX|PRXQuantum|PhysRevApplied|PhysRevA|PhysRevB|PhysRevResearch)\.(\d+)\.(\w+)', doi)
        if m: v = v or m.group(2); pg = pg or m.group(3)
        seg = []
        if j: seg.append('<i>' + j + '</i>')
        if v: seg.append('vol. ' + esc(v))
        if n: seg.append('no. ' + esc(n))
        if pg:
            if re.search(r'[–-]', pg): seg.append('pp. ' + esc(pg).replace('-', '–'))
            elif jn in PAGED: seg.append('p. ' + esc(pg))
            else: seg.append('Art. no. ' + esc(pg))
        d = r.get('pubdate') or r.get('date')
        if not d and m and m.group(1) in APS_YEAR: d = APS_YEAR[m.group(1)](m.group(2))
        if d: seg.append(fmt_date(d, day=False))
        if seg: parts.append(', '.join(seg) + ('.' if not doi else ','))
        if doi: parts.append('doi: ' + _link('https://doi.org/' + doi, doi) + '.')
        elif url and not ax: parts.append('[Online]. Available: ' + _link(url))
        if ax: parts.append(_link('https://arxiv.org/abs/' + ax, 'arXiv:' + ax) + '.')
    elif kind == 'preprint':
        seg = []
        if ax: seg.append(_link('https://arxiv.org/abs/' + ax, 'arXiv:' + ax))
        elif url: seg.append(_link(url))
        if r.get('date'): seg.append(fmt_date(r['date'], day=False))
        parts.append(', '.join(seg) + '.')
    elif kind == 'report':
        seg = []
        if r.get('publisher'): seg.append(esc(r['publisher']))
        if r.get('date'): seg.append(fmt_date(r['date'], day=False))
        parts.append(', '.join(seg) + ('.' if not doi else ','))
        if doi: parts.append('doi: ' + _link('https://doi.org/' + doi, doi) + '.')
        elif url: parts.append('[Online]. Available: ' + _link(url))
    else:
        site = (r.get('site') or r.get('venue') or host(url)).strip(); seg = []
        if site and (r.get('authors') or not _same_name(site, r.get('org') or '')): seg.append(esc(site))
        if r.get('date'): seg.append(fmt_date(r['date']))
        if seg: parts.append(', '.join(seg) + '.')
        elif parts: parts[-1] = re.sub(r',”$', '.”', parts[-1].rstrip(',')) if parts[-1].endswith('”') else parts[-1].rstrip(',') + '.'
        if url: parts.append('[Online]. Available: ' + _link(url))
    for a in r.get('also', []):
        parts.append('Also ' + _link(a) + '.')
    return ' '.join(p for p in parts if p)


def render_list(lang, order, works, num):
    """§9 as one numbered list; ids keep the register codes (en-src-S2, en-src-S7-2 …) so in-text links and the release check
    address entries by code."""
    P = lang + '-'; out = ['<ol class="refs" data-nohint="1">']; done = set()
    for c in order:
        for i, r in enumerate(works[c]):
            n = num[c][i]
            if n in done: continue
            done.add(n); rid = P + 'src-' + c + ('' if i == 0 else '-%d' % (i + 1))
            out.append('<li id="%s" value="%d"><span class="src">[%d]</span> <span class="ref">%s</span></li>' % (rid, n, n, ieee(r)))
    out.append('</ol>')
    return '\n'.join(out)


def anchor_for(code, works, num, order):
    """The id of the entry a code points at (the entry that carries its first number)."""
    n = num.get(code, [0])[0]
    for c in order:
        for i, nn in enumerate(num[c]):
            if nn == n: return c + ('' if i == 0 else '-%d' % (i + 1))
    return code


def cite_html(codes, lang, works, num, order):
    """A run of adjacent in-text codes → IEEE numbers: [3], [5]–[7], each number linked to its entry."""
    P = lang + '-'; nums = []
    for c in codes:
        for n in num.get(c, [0]):
            if n and n not in nums: nums.append(n)
    if not nums: return ''.join('[%s]' % c for c in codes)
    where = {}
    for c in order:
        for i, nn in enumerate(num[c]): where.setdefault(nn, c + ('' if i == 0 else '-%d' % (i + 1)))
    link = lambda n: '<a class="cite" href="#%ssrc-%s">[%d]</a>' % (P, where.get(n, ''), n)
    ns = sorted(nums); runs = []
    for n in ns:
        if runs and n == runs[-1][1] + 1: runs[-1][1] = n
        else: runs.append([n, n])
    return ', '.join(link(a) if a == b else (link(a) + ', ' + link(b) if b == a + 1 else link(a) + '–' + link(b)) for a, b in runs)


def brief_line_ieee(line):
    """A brief's source line → IEEE-style HTML (grade tag kept at the end); a line the parser cannot read is returned as is."""
    rec = parse_line(line)
    if not rec.get('title') or not rec.get('url'): return line
    g = (' [' + rec['grade'] + ']') if rec.get('grade') else ''
    r = dict(rec)
    if r['kind'] == 'web': r['site'] = r.get('venue') or host(r['url'])
    return ieee(r) + g


def check():
    body, ent = parse_register('en'); data = load_json()
    reg = {(c, u) for c, e in ent.items() for u in e['urls'] if not e['label'].startswith('see [') and c not in DROP}
    bib = {(c, r.get('url')) for c, rs in data.items() for r in rs}
    probs = []
    for c, u in sorted(reg - bib): probs.append('register URL without a record: [%s] %s' % (c, u))
    for c, u in sorted(bib - reg): probs.append('record without a register URL: [%s] %s' % (c, u))
    for c, rs in data.items():
        for r in rs:
            if not r.get('verified'): probs.append('unverified: [%s] %s' % (c, r.get('url')))
            if not r.get('title'): probs.append('no title: [%s] %s' % (c, r.get('url')))
            if not (r.get('authors') or r.get('org')): probs.append('no author/organisation: [%s] %s' % (c, r.get('url')))
            if not r.get('date'): probs.append('no date: [%s] %s' % (c, r.get('url')))
    return probs


if __name__ == '__main__':
    if '--skeleton' in sys.argv:
        data, added = skeleton(); print('records added', added, 'codes', len(data))
    elif '--check' in sys.argv:
        for p in check(): print(p)
    else:
        order, works, alias, num, unverified = build()
        print('codes', len(works), 'numbers', max(max(v) for v in num.values()), 'aliases', alias, 'unverified', len(unverified))
        for c in order[:8]: print(c, num[c], '|', re.sub('<[^>]+>', '', ieee(works[c][0]))[:170])
