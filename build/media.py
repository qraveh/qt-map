# -*- coding: utf-8 -*-
"""The Atlas's use of the media register (SP08, 27 Sep 2026): a snapshot of the licensed pictures and of what each one
illustrates (data/media/media.json), and the helpers the page builders call to place them.

    python3 build/media.py --import [--dir DIR]     read the register's CSVs, write data/media/media.json
    python3 build/media.py --check [--thumbs DIR]   counts and problems; with DIR, the hosted thumbnails missing from it
    python3 build/media.py --files                  the thumbnail files the deploy copies to <atlas base>/media/

DIR defaults to $QT_MEDIA_DIR, else /home/claude/work/QT-Map/media-register/data. Assets whose verdict is QUARANTINE or REJECT
are dropped with their illustrates rows; LINK-OUT assets are kept and linked, never hosted; EMBED / EMBED-ASIS assets are
hosted as <asset_id>.jpg (the register's assets/thumbs/; the build never copies pictures into the repository).

A target's list is ranked (hosted before link-out; for a technology, the register's best real capture, then its best drawing
or figure; role; real captures before renders and drawings; confidence, high first; asset id), so a consumer takes the
first n and the register's chosen real capture is always among them:

    import media
    media.gallery_html('node:ion', lang, base)      # up to 3 <figure class="media">, '' when the target has none
    media.pick('machine:google-willow', n=1, kinds=('photo',))

A hosted picture's credit line is verdicts.attribution printed once, its web addresses as links; the licence follows only
when the attribution does not already name it.
"""
import csv, datetime, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, 'data', 'media', 'media.json')
REG = os.environ.get('QT_MEDIA_DIR') or '/home/claude/work/QT-Map/media-register/data'
FILES = ('media.csv', 'verdicts.csv', 'stories.csv', 'illustrates.csv', 'coverage-nodes.csv')
HOSTED = ('EMBED', 'EMBED-ASIS'); KEPT = HOSTED + ('LINK-OUT',); DROPPED = ('QUARANTINE', 'REJECT')
ROLE_RANK = {'shown-primary': 0, 'shown-machine': 1, 'shown-secondary': 2, 'shown-generation': 3, 'shown-background': 4,
             'also': 5, 'implied': 6}
LINKOUT = {'en': 'external image — opens at the source', 'ru': 'внешнее изображение — откроется у источника'}


def _lpick(lang, texts):
    """the language's text, English where the language has none (langs.pick; named apart from media.pick, 29 Sep 2026)"""
    from langs import pick as lp
    return lp(lang, texts)


# ---- import: the register's CSVs -> the snapshot ----

def _rows(d, name):
    with open(os.path.join(d, name), newline='', encoding='utf-8-sig') as fh:
        return [{k: (v or '').strip() for k, v in r.items() if k is not None} for r in csv.DictReader(fh)]


def _note(notes, label, items):
    items = sorted(set(items))
    if items: notes.append('%s: %d (%s%s)' % (label, len(items), ', '.join(items[:8]), ', ...' if len(items) > 8 else ''))


def _index(rows, label, notes):
    out, dup = {}, []
    for r in rows:
        if r['asset_id'] in out: dup.append(r['asset_id'])
        out[r['asset_id']] = r
    _note(notes, '%s: asset ids listed twice (the last row counts)' % label, dup)
    return out


def _int(s):
    try: v = int(float(s))
    except (ValueError, OverflowError): return None
    return v if v > 0 else None


def _conf(s):
    try: v = float(s)
    except ValueError: return None
    return v if 0.0 <= v <= 1.0 else None


def _href(u):
    u = (u or '').strip()
    return u if u.lower().startswith(('http://', 'https://')) else ''


def build_snapshot(d=REG):
    """Read the register's CSVs in d; return (snapshot, notes). The notes are the inconsistencies seen, reported as data."""
    for f in FILES:
        if not os.path.isfile(os.path.join(d, f)): raise SystemExit('media register file not found: ' + os.path.join(d, f))
    notes = []
    media = _index(_rows(d, 'media.csv'), 'media.csv', notes)
    verdicts = _index(_rows(d, 'verdicts.csv'), 'verdicts.csv', notes)
    stories = {a: r['story'] for a, r in _index(_rows(d, 'stories.csv'), 'stories.csv', notes).items()}
    ill = _rows(d, 'illustrates.csv')
    cover = {r['node']: r for r in _rows(d, 'coverage-nodes.csv')}

    first_kind = {}
    for r in ill: first_kind.setdefault(r['asset_id'], r['content_kind'])
    assets, bad_size, bad_url = {}, [], []
    for a, m in media.items():
        v = verdicts.get(a)
        if not v or v['verdict'] not in KEPT: continue
        e = {'title': m['title'], 'creator': m['creator'], 'rights_holder': m['rights_holder'], 'date': m['date_created'],
             'kind': first_kind.get(a) or m['media_type'], 'verdict': v['verdict'], 'attribution': v['attribution'],
             'cite_as': v['cite_as'], 'license': m['license_spdx'], 'license_url': m['license_url'],
             'source_page_url': m['source_page_url'], 'width': _int(m['width']), 'height': _int(m['height']),
             'story': stories.get(a, ''), 'thumb': a + '.jpg' if v['verdict'] in HOSTED else None}
        if v['verdict'] == 'LINK-OUT': e['file_url'] = m['file_url']
        if (m['width'] and e['width'] is None) or (m['height'] and e['height'] is None): bad_size.append(a)
        for f in ('source_page_url', 'file_url'):
            if e.get(f) and not _href(e[f]): bad_url.append('%s.%s' % (a, f))
        assets[a] = e
    _note(notes, 'media.csv assets without a verdicts.csv row (dropped)', [a for a in media if a not in verdicts])
    _note(notes, 'verdicts.csv assets missing in media.csv (dropped)', [a for a in verdicts if a not in media])
    _note(notes, 'unknown verdicts (asset dropped)', ['%s=%s' % (a, v['verdict']) for a, v in verdicts.items()
                                                     if v['verdict'] not in KEPT + DROPPED])
    _note(notes, 'kept assets without a story (the title stands in)', [a for a, e in assets.items() if not e['story']])
    _note(notes, 'kept assets with an unreadable width/height (null)', bad_size)
    _note(notes, 'kept assets with a link that is not http(s) (not linked)', bad_url)

    targets, seen = {}, {}
    miss_media, miss_verdict, mismatch, roles, bad_conf, blank = [], [], [], [], [], []
    for i, r in enumerate(ill, 2):
        a, kind, tid = r['asset_id'], r['target_kind'], r['target']
        if a not in assets:
            if a not in media: miss_media.append(a)
            elif a not in verdicts: miss_verdict.append(a)
            continue                                   # QUARANTINE / REJECT: dropped with the asset
        if not kind or not tid: blank.append('line %d' % i); continue
        e = assets[a]
        if r['licence_verdict'] and r['licence_verdict'] != e['verdict']:
            mismatch.append('%s %s/%s' % (a, r['licence_verdict'], e['verdict']))
        if r['role'] not in ROLE_RANK: roles.append('%s=%s' % (a, r['role']))
        conf = _conf(r['confidence'])
        if r['confidence'] and conf is None: bad_conf.append(a)
        key = kind + ':' + tid
        t = {'asset': a, 'role': r['role'], 'how': r['how'], 'confidence': conf, 'kind': r['content_kind'] or e['kind'],
             'real': r['real_capture'] == 'real'}
        best = 2
        if kind == 'node':
            c = cover.get(tid) or {}
            best = 0 if a == c.get('best_real_capture') else 1 if a == c.get('best_drawing_or_figure') else 2
        rank = (0 if e['verdict'] in HOSTED else 1, best, ROLE_RANK.get(r['role'], len(ROLE_RANK)), 0 if t['real'] else 1,
                -(conf or 0.0), a, r['role'], r['how'])
        targets.setdefault(key, []).append((rank, t))
        seen[(key, a)] = seen.get((key, a), 0) + 1
    targets = {k: [t for _, t in sorted(v, key=lambda x: x[0])] for k, v in targets.items()}
    _note(notes, 'illustrates rows whose asset is missing in media.csv (skipped)', miss_media)
    _note(notes, 'illustrates rows whose asset is missing in verdicts.csv (skipped)', miss_verdict)
    _note(notes, 'illustrates rows without a target (skipped)', blank)
    _note(notes, 'illustrates rows whose licence_verdict differs from verdicts.csv (verdicts.csv counts)', mismatch)
    _note(notes, 'illustrates rows with an unknown role (ranked last)', roles)
    _note(notes, 'illustrates rows with an unreadable confidence (null)', bad_conf)
    _note(notes, 'target/asset pairs listed more than once', ['%s <- %s x%d' % (k, a, n) for (k, a), n in seen.items() if n > 1])
    used = {a for _, a in seen}
    _note(notes, 'kept assets that illustrate no target', [a for a in assets if a not in used])
    _note(notes, 'coverage-nodes best picks that are not a kept row of their node',
          ['%s.%s=%s' % (n, f, c[f]) for n, c in cover.items() for f in ('best_real_capture', 'best_drawing_or_figure')
           if c.get(f) and ('node:' + n, c[f]) not in seen])

    mtime = os.path.getmtime(os.path.join(d, 'illustrates.csv'))
    source = {'register': 'media-register (SP08)', 'assets': len(assets), 'targets': len(targets),
              'imported': datetime.datetime.fromtimestamp(mtime, datetime.timezone.utc).strftime('%Y-%m-%d')}
    return {'source': source, 'assets': assets, 'targets': targets}, notes


def write_snapshot(d=REG):
    """--import: build the snapshot from the register in d and write data/media/media.json (same inputs, same bytes)."""
    global _CACHE
    snap, notes = build_snapshot(d)
    txt = json.dumps(snap, sort_keys=True, ensure_ascii=False, indent=1) + '\n'
    os.makedirs(os.path.dirname(SNAP), exist_ok=True)
    with open(SNAP, 'w', encoding='utf-8', newline='\n') as fh: fh.write(txt)
    _CACHE = None
    for n in notes: print('note:', n)
    print('%s written from %s: %d assets, %d targets, %d bytes' % (os.path.relpath(SNAP, ROOT), d, snap['source']['assets'],
                                                                   snap['source']['targets'], len(txt.encode('utf-8'))))
    return snap


# ---- the API the page builders use ----

_CACHE = None


def load():
    """The snapshot dict, read once per process."""
    global _CACHE
    if _CACHE is None:
        with open(SNAP, encoding='utf-8') as fh: _CACHE = json.load(fh)
    return _CACHE


def pick(target_key, n=3, kinds=None):
    """Up to n pictures for a target ('node:ion', 'machine:google-willow', 'gap:G-cryo', 'adjacent:adj_aom'), best first.
    Each is the asset's entry merged with how it shows this target: asset (the id), role, how, confidence, real.
    kinds, when given, keeps only those content kinds, e.g. ('photo',). An asset listed twice for one target comes once;
    n=None returns all."""
    if n is not None and n <= 0: return []
    S = load(); A = S['assets']
    if isinstance(kinds, str): kinds = (kinds,)
    out, seen = [], set()
    for t in S['targets'].get(target_key, ()):
        a = t['asset']
        if a in seen or a not in A or (kinds and t['kind'] not in kinds): continue
        if A[a].get('verdict') == 'LINK-OUT' and A[a].get('kind') == 'document-page': continue   # a pointer to where pictures may be found (a media-kit folder, a press page), not an illustration (27 Sep 2026)
        seen.add(a)
        d = dict(A[a], asset=a)
        d.update((k, t[k]) for k in ('role', 'how', 'confidence', 'real'))
        out.append(d)
        if n is not None and len(out) >= n: break
    return out


def _e(s): return html.escape('' if s is None else str(s), quote=True)


def _a(url, text):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (_e(url), text)


URL_RE = re.compile(r'https?://[^\s<>"“”‘’«»]+', re.I)
# a credit text names its licence when it says CC… (CC BY, CC-BY-SA, CC0), public domain or PD, as words, not inside one
NAMES_LICENCE = re.compile(r'(?<![a-z])cc(?:0|(?![a-z]))|public[\s-]domain|(?<![a-z0-9])pd(?![a-z])', re.I)
_OPENER = {')': '(', ']': '[', '}': '{'}


def _bare(u): return re.sub(r'^(https?://)?(www\.)?', '', (u or '').strip().lower()).rstrip('/')


def names_licence(text, spdx='', url=''):
    """True when the credit text already names its licence: CC…, public domain, PD, the SPDX code or the licence URL."""
    t = (text or '').lower()
    return bool(NAMES_LICENCE.search(t) or (spdx and spdx.lower() in t) or (_bare(url) and _bare(url) in t))


def licence_name(spdx):
    """The licence's short, human-readable name: CC-BY-4.0 -> CC BY 4.0, CC-BY-SA-4.0 -> CC BY-SA 4.0, CC0-1.0 -> CC0,
    LicenseRef-PD-USGov -> public domain (US government work), other LicenseRef-x-y -> x y; anything else as it is."""
    s = (spdx or '').strip()
    if s == 'LicenseRef-PD-USGov': return 'public domain (US government work)'
    if s.startswith('LicenseRef-'): return s[len('LicenseRef-'):].replace('-', ' ')
    if s.upper() == 'CC0-1.0': return 'CC0'
    p = s.split('-')
    if len(p) >= 3 and p[0].upper() == 'CC' and p[-1][:1].isdigit(): return 'CC %s %s' % ('-'.join(p[1:-1]), p[-1])
    return s


_SCRAPE_RE = re.compile(r'<!--.*?(?:-->|$)|<[^>]+>|You must enable JavaScript[^.]*\.|\(\d+ additional authors not shown\)', re.S)
MAX_AUTHORS = 6


def clean_text(text):
    """A register text field as the page may print it: cut at an HTML comment, drop tags and the scraped arXiv boilerplate
    (two credits of 26 Sep 2026 carried a toggleAuthorList() script after 200 author names), collapse whitespace."""
    t = _SCRAPE_RE.sub(' ', text or '')
    for _ in range(3):   # LaTeX source doubled next to its rendering in scraped captions: "|0⟩\\ket{0}" → "|0⟩"
        t2 = re.sub(r'\\[A-Za-z]+(?:\{[^{}]*\})*(?:[_^](?:\{[^{}]*\}|\w))*', '', t)
        if t2 == t: break
        t = t2
    t = re.sub(r'[_^]\{[^{}]*\}|\{\}', '', t)
    t = re.sub(r'“([^”]{100,})”', lambda m: '“' + (m.group(1) if m.group(1).rstrip()[-1:] in '.!?)' else m.group(1)[:m.group(1).rfind(' ')].rstrip(' ,;:') + '…') + '”', t)   # a title cut mid-word by the register ends at a word
    return re.sub(r'\s+', ' ', t).strip(' ,;')


def shorten_authors(text):
    """An author run of more than MAX_AUTHORS comma-separated names — after ' by ' in an attribution, or a bare creator list —
    becomes 'first author et al.'; the linked source names them all. Runs of six or fewer print in full."""
    def cut(run):
        names = [n.strip() for n in run.split(',') if n.strip()]
        return run if len(names) <= MAX_AUTHORS else names[0] + ' et al.'
    m = re.search(r'(?<=\bby )([^\n]*?)(?=,? ?https?://|$)', text)
    if m: return text[:m.start()] + cut(m.group(1)) + text[m.end():]
    return cut(text) if text.count(',') >= MAX_AUTHORS and not re.search(r'https?://', text) else text


def _credit_parts(a):
    who = clean_text(a.get('attribution')) or ' · '.join(dict.fromkeys(x for x in (clean_text(a.get('creator')), clean_text(a.get('rights_holder'))) if x))
    who = shorten_authors(who)
    spdx, url = a.get('license') or '', a.get('license_url') or ''
    return who, ('' if names_licence(who, spdx, url) else licence_name(spdx)), _href(url)


def credit(a):
    """The credit line of a hosted picture, as text: verdicts.attribution once (when it is empty, the creator and rights
    holder stand in), then ' · ' and the licence's short name only when the attribution does not already name it."""
    who, lic, _ = _credit_parts(a)
    return ' · '.join(x for x in (who, lic) if x)


def linkify(text):
    """Escaped text in which every http(s) URL is a link, shown without its scheme and cut with … after 60 characters."""
    out, pos = [], 0
    for m in URL_RE.finditer(text or ''):
        u = m.group(0)
        while u and u[-1] in '.,;:!?\'")]}':          # trailing punctuation is the sentence's, unless it closes a bracket
            if u[-1] in _OPENER and u.count(_OPENER[u[-1]]) >= u.count(u[-1]): break    # of the URL's own
            u = u[:-1]
        shown = re.sub(r'^https?://', '', u, flags=re.I)
        if not shown: continue
        out += [_e(text[pos:m.start()]), _a(u, _e(shown[:60] + '…' if len(shown) > 60 else shown))]
        pos = m.start() + len(u)
    return ''.join(out) + _e((text or '')[pos:])


def credit_html(a):
    """The credit line of a hosted picture as HTML: the attribution's web addresses and the appended licence are links."""
    who, lic, lic_url = _credit_parts(a)
    parts = ([linkify(who)] if who else []) + ([_a(lic_url, _e(lic)) if lic_url else _e(lic)] if lic else [])
    return ' · '.join(parts)


def _alt(title):
    t = title or ''
    return t if len(t) <= 160 else t[:157].rstrip() + '…'


def figure_html(a, lang, base):
    """One <figure class="media"> for an asset dict (from pick()), with data-asset="<asset_id>" and the class real or
    drawing (from the register's real_capture). base is the relative prefix from the page to the Atlas root ('' at the
    root, '../' one level down). A hosted picture links to its source page; a LINK-OUT one is a titled link to the source
    ('' when it has no http(s) link)."""
    thumb = a.get('thumb') or ''
    aid = a.get('asset') or (thumb[:-4] if thumb.endswith('.jpg') else '')
    cls = ' '.join(['media'] + ([] if thumb else ['linkout']) + ([('real' if a['real'] else 'drawing')] if 'real' in a else []))
    head = '<figure class="%s"%s>' % (cls, ' data-asset="%s"' % _e(aid) if aid else '')
    story = clean_text(a.get('story') or a.get('title') or '')
    if thumb:
        wh = ' width="%d" height="%d"' % (a['width'], a['height']) if a.get('width') and a.get('height') else ''
        pic = '<img src="%smedia/%s" alt="%s" loading="lazy"%s>' % (_e(base), _e(thumb), _e(_alt(clean_text(a.get('title')))), wh)
        url = _href(a.get('source_page_url'))
        if url: pic = _a(url, pic)
        return head + ('%s<figcaption><span class="story">%s</span> <span class="credit">%s</span></figcaption></figure>'
                       % (pic, _e(story), credit_html(a)))
    url = _href(a.get('file_url')) or _href(a.get('source_page_url'))
    if not url: return ''
    return head + ('%s <span class="credit">%s</span><figcaption>%s</figcaption></figure>'
                   % (_a(url, _e(clean_text(a.get('title')))), _e(_lpick(lang, LINKOUT)), _e(story)))


def gallery_html(target_key, lang, base, n=3, kinds=None):
    """The figures of pick() joined; '' when the target has none."""
    return ''.join(figure_html(a, lang, base) for a in pick(target_key, n, kinds))


def hosted_files():
    """Sorted thumbnail file names the site must serve at <atlas base>/media/: every asset with a thumb that illustrates at
    least one target in the snapshot (a hosted asset no target shows is not served)."""
    S = load(); used = {t['asset'] for ts in S['targets'].values() for t in ts}
    return sorted(e['thumb'] for a, e in S['assets'].items() if e.get('thumb') and a in used)


def check(thumbs_dir=None):
    """Print the snapshot's counts and problems (with thumbs_dir, when it exists: the hosted files missing from it); return
    the number of problems."""
    S = load(); A = S['assets']; T = S['targets']; src = S.get('source') or {}
    by_verdict, by_kind = {}, {}
    for e in A.values(): by_verdict[e['verdict']] = by_verdict.get(e['verdict'], 0) + 1
    for k in T: by_kind[k.split(':', 1)[0]] = by_kind.get(k.split(':', 1)[0], 0) + 1
    used = {t['asset'] for ts in T.values() for t in ts}
    hosted = [a for a, e in A.items() if e.get('thumb')]
    files = hosted_files()
    print('%s: %s, imported %s' % (os.path.relpath(SNAP, ROOT), src.get('register'), src.get('imported')))
    print('assets %d: hosted %d (%s), link-out %d' % (len(A), len(hosted), ', '.join('%s %d' % (v, by_verdict.get(v, 0))
                                                                                     for v in HOSTED), by_verdict.get('LINK-OUT', 0)))
    print('targets %d: %s' % (len(T), ', '.join('%s %d' % kv for kv in sorted(by_kind.items()))))
    print('illustrates rows %d; assets illustrating no target %d' % (sum(len(ts) for ts in T.values()), len(set(A) - used)))
    print('hosted files to serve %d (hosted assets illustrating no target, not served: %d)' % (len(files), len(hosted) - len(files)))

    problems = []
    if src.get('assets') != len(A) or src.get('targets') != len(T):
        problems.append('source counts %s/%s differ from the snapshot %d/%d' % (src.get('assets'), src.get('targets'), len(A), len(T)))
    for a, e in sorted(A.items()):
        if e['verdict'] not in KEPT: problems.append('%s: verdict %s must not be in the snapshot' % (a, e['verdict']))
        elif (e['verdict'] in HOSTED) != bool(e.get('thumb')):
            problems.append('%s: %s %s a thumb name' % (a, e['verdict'], 'without' if e['verdict'] in HOSTED else 'with'))
        if e.get('thumb') and not credit(e): problems.append('%s: hosted without a credit line' % a)
        if e['verdict'] == 'LINK-OUT' and not (_href(e.get('file_url')) or _href(e.get('source_page_url'))):
            problems.append('%s: link-out without an http(s) link' % a)
    for k, ts in sorted(T.items()):
        problems += ['%s: asset %s is not in the snapshot' % (k, t['asset']) for t in ts if t['asset'] not in A]
    # register data notes (not problems: the renderer cleans them — clean_text): scraped markup or LaTeX source in a text field
    notes = [(a, f) for a, e in sorted(A.items()) for f in ('title', 'creator', 'attribution', 'story') if re.search(r'<|\\[A-Za-z]', e.get(f) or '')]
    print('register text fields with markup or LaTeX source (cleaned at render time): %d — %s' % (len(notes), ', '.join('%s.%s' % n for n in notes[:12]) + (' …' if len(notes) > 12 else '')))
    if thumbs_dir is None:
        print('thumbnails: not checked (no --thumbs DIR)')
    elif not os.path.isdir(thumbs_dir):
        problems.append('thumbs dir not found: %s' % thumbs_dir)
    else:
        have = set(os.listdir(thumbs_dir)); miss = [f for f in files if f not in have]
        print('thumbnails in %s: %d of %d hosted files present' % (thumbs_dir, len(files) - len(miss), len(files)))
        for f in miss: print('missing:', f)
        problems += ['missing thumbnail %s' % f for f in miss]
    for p in problems:
        if not p.startswith('missing thumbnail '): print('problem:', p)
    print('problems: %d' % len(problems))
    return len(problems)


# ---- CLI ----

def main(argv):
    flags, vals, it = set(), {}, iter(argv)
    for x in it:
        if x in ('--dir', '--thumbs'):
            v = next(it, None)
            if v is None or v.startswith('--'): raise SystemExit('%s needs a directory' % x)
            vals[x] = v
        elif x in ('--import', '--check', '--files'): flags.add(x)
        else: raise SystemExit('unknown argument %r\n%s' % (x, __doc__))
    if not flags: print(__doc__); return 2
    rc = 0
    if '--import' in flags: write_snapshot(vals.get('--dir', REG))
    if '--check' in flags: rc = 1 if check(vals.get('--thumbs')) else 0
    if '--files' in flags: print('\n'.join(hosted_files()))
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
