"""Every sortable column of the Atlas's main page sorts, in every language (QM-028, 24 Nov 2026).

    <Playwright python> build/audit/sort_check.py [--out report.json] [--only en,ru]

For each language's main page (dist/manifest.json) and, on each page, for every language the page can show (its own inline,
the others as the fragments LANG_JS fills in): every div.tbl[data-sort] of that language must carry sort buttons; every
sortable column is clicked three times — ascending (descending first where the table asks for it), descending, back to the
build order — and the ↺ button and a platform table's first header must restore the build order. After each click the
column's cells are read in Python by a reader written apart from the page's (map_js.py `val()`): the first number not glued
to a letter, a power of ten after it (2.2×10³, a bare 10⁻⁴), a unit of time or frequency after that (a frequency in a
time-dominated column sorts by its period), dates as YYYY[-MM[-DD]] or «Mon YYYY»; the keys must be monotonic with the empty
cells last in both directions. The map's Table view is switched on and each column button is checked the same way (aria-sort
cycle; monotonic years for `since`, the default order back on the third click). Exit 1 on any failure.
"""
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIST = ROOT / 'dist'
LET = 'A-Za-zА-Яа-яЁёא-ת'
NUMBER = re.compile(r'(?<![%s\d.,])[-−+]?\d+(?:(?:,|[    ])\d{3})*(?:\.\d+)?(?![%s])' % (LET, LET))
SUPS = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺', '0123456789-+')
POWER = re.compile(r'\s*[×x]\s*10([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)')
BARE = re.compile(r'([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)')
UNIT = re.compile(r'(?:\s*[–-]\s*\d[\d.]*)?\s*(ps|ns|µs|μs|us|ms|s|min|h|Hz|kHz|MHz|GHz)(?![%s])' % LET)
TIME = {'ps': 1e-12, 'ns': 1e-9, 'µs': 1e-6, 'μs': 1e-6, 'us': 1e-6, 'ms': 1e-3, 's': 1.0, 'min': 60.0, 'h': 3600.0}
FREQ = {'Hz': 1.0, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9}
NULL = re.compile(r'^(?:—|–|-|∅|n/a|na|not published|не опубликовано|לא פורסם)(?:$|[\s—–:;,.(])', re.I)
MONTHS = {k: i + 1 for i, ks in enumerate(zip(
    'jan feb mar apr may jun jul aug sep oct nov dec'.split(),
    'янв фев мар апр май июн июл авг сен окт ноя дек'.split(),
    'ינו פבר מרץ אפר מאי יונ יול אוג ספט אוק נוב דצמ'.split())) for k in ks}
MONTHS['мая'] = 5


def reading(s):
    """(value, dim) of a cell's text — dim 't' seconds, 'f' hertz, '' a plain number — or None for an empty or wordy cell."""
    s = re.sub(r'\s+', ' ', s or '').strip()
    if not s or NULL.match(s):
        return None
    for m in NUMBER.finditer(s):
        tok = m.group(0)
        if m.start() > 0 and s[m.start() - 1] in '-−' and m.start() > 1 and re.match('[%s]' % LET, s[m.start() - 2]):
            continue   # Gen-1: a hyphen glued to a word is not a minus
        v = float(re.sub(r'[,    ]', '', tok).replace('−', '-'))
        rest = s[m.end():]
        p = POWER.match(rest)
        if p:
            v *= 10.0 ** int(p.group(1).translate(SUPS))
            rest = rest[p.end():]
        elif tok == '10':
            b = BARE.match(rest)
            if b:
                v = 10.0 ** int(b.group(1).translate(SUPS))
                rest = rest[b.end():]
        u = UNIT.match(rest)
        if u:
            return (v * TIME[u.group(1)], 't') if u.group(1) in TIME else (v * FREQ[u.group(1)], 'f')
        return v, ''
    return None


def date_key(s):
    s = s or ''
    m = re.search(r'(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?', s)
    if m:
        return int(m.group(1)) * 10000 + int(m.group(2) or 0) * 100 + int(m.group(3) or 0)
    m = re.search(r'([%s]{3})[%s.]*\s+(\d{4})' % (LET, LET), s)
    if m and m.group(1).lower() in MONTHS:
        return int(m.group(2)) * 10000 + MONTHS[m.group(1).lower()] * 100
    return None


def keys(texts, kind):
    if kind == 'date':
        return [date_key(t) for t in texts]
    rs = [reading(t) for t in texts]
    nt = sum(1 for r in rs if r and r[1] == 't')
    nf = sum(1 for r in rs if r and r[1] == 'f')
    dom = 't' if nt > nf else ('f' if nf > nt else '')
    return [None if r is None else (1.0 / r[0] if dom and r[1] and r[1] != dom and r[0] else r[0]) for r in rs]


def monotonic(ks, direction):
    """None when the keys are in order (empty last), else the first offending position."""
    seen_null = False
    prev = None
    for i, k in enumerate(ks):
        if k is None:
            seen_null = True
            continue
        if seen_null:
            return i
        if prev is not None and (k < prev if direction > 0 else k > prev) and abs(k - prev) > 1e-12 * max(abs(k), abs(prev)):
            return i
        prev = k
    return None


JS_TABLES = r"""(L) => {
  const LANGS = window.__LANGS.list;
  function langOf(w){ const f = w.closest('details.tblfold'); if (f && f.id) return f.id.split('-')[0];
    for (let e = w; e; e = e.parentElement) { if (e.classList) for (const x of LANGS) if (e.classList.contains('lang-'+x)) return x; }
    return '?'; }
  const txt = el => (el ? el.textContent : '').replace(/\s+/g,' ').trim();
  const out = [];
  [...document.querySelectorAll('div.tbl[data-sort]')].forEach((w, wi) => {
    if (langOf(w) !== L) return;
    const t = w.querySelector('table'), head = t && t.tHead && t.tHead.rows[0];
    const id = (w.closest('details.tblfold') || {}).id || ('wrap-' + wi);
    const kind = w.getAttribute('data-sort'), first = w.getAttribute('data-sort-first') === 'desc' ? -1 : 1;
    const rows = () => [...t.tBodies].flatMap(b => [...b.rows]);
    rows().forEach((r, k) => { if (!r.hasAttribute('data-sk')) r.setAttribute('data-sk', String(k)); });
    const order = () => rows().map(r => r.getAttribute('data-sk')).join(',');
    const build = order();
    const ths = head ? [...head.cells] : [];
    const rec = {id, kind, first, heads: ths.map(txt), buttons: 0, cols: [], restores: []};
    ths.forEach((th, i) => {
      const b = th.querySelector('button.sortbtn'); if (!b) return; rec.buttons++;
      if (b.classList.contains('sortreset')) { rec.resetCol = i; return; }
      const col = {i, head: txt(th), clicks: []};
      for (let c = 0; c < 3; c++) {
        b.click();
        col.clicks.push({aria: th.getAttribute('aria-sort'), order: order(), texts: rows().map(r => txt(r.cells[i]))});
      }
      col.restored = (order() === build);
      rec.cols.push(col);
    });
    // the ↺ button and a platform table's first header restore the build order after a sort
    const any = ths.map(th => th.querySelector('button.sortbtn:not(.sortreset)')).find(Boolean);
    if (any) {
      any.click(); const r = w.querySelector('button.tsreset'); if (r) r.click();
      rec.restores.push({how: '↺', ok: order() === build, present: !!r});
      if (rec.resetCol != null) { any.click(); ths[rec.resetCol].querySelector('button.sortbtn').click(); rec.restores.push({how: 'first header', ok: order() === build, present: true}); }
    }
    out.push(rec);
  });
  return out;
}"""

JS_TABLEVIEW = r"""() => {
  if (!window.__setView) return {missing: 'window.__setView'};
  window.__setView('table');
  const tab = () => document.querySelector('table.ttab');
  if (!tab()) return {missing: 'table.ttab'};
  const txt = el => (el ? el.textContent : '').replace(/\s+/g,' ').trim();
  const ids = () => [...tab().querySelectorAll('tbody tr')].map(r => r.getAttribute('data-id') || txt(r.cells[1]));
  const base = ids().join('|');
  const cols = [...tab().querySelectorAll('thead th')].map((th, i) => ({i, cls: th.className, head: txt(th), btn: !!th.querySelector('.tsort')}));
  const res = [];
  cols.filter(c => c.btn).forEach(c => {
    const k = (c.cls.match(/tc-(\w+)/) || [])[1]; const seq = [];
    for (let n = 0; n < 3; n++) {
      const b = tab().querySelector('th.tc-' + k + ' .tsort'); b.click();
      const th = tab().querySelector('th.tc-' + k);
      seq.push({aria: th.getAttribute('aria-sort'), order: ids().join('|'), texts: [...tab().querySelectorAll('tbody tr')].map(r => txt(r.cells[c.i]))});
    }
    res.push({k, head: c.head, seq, restored: ids().join('|') === base});
  });
  window.__setView('map');
  const key = c => (c.cls.match(/tc-(\w+)/) || [])[1];
  return {cols: cols.length, buttons: cols.filter(c => c.btn).length, keys: cols.map(key).filter(Boolean), sortable: cols.filter(c => c.btn).map(key), res};
}"""


def check_tables(recs, L, page_lang, fails, stats):
    if not recs:
        fails.append('%s page / %s: no sortable table found' % (page_lang, L))
    for r in recs:
        where = '%s page / %s / %s' % (page_lang, L, r['id'])
        stats['tables'] += 1
        if not r['buttons']:
            fails.append('%s: no sort buttons (the QM-028 failure)' % where)
            continue
        for c in r['cols']:
            stats['columns'] += 1
            first = r['first']
            want = ['ascending' if first > 0 else 'descending', 'descending' if first > 0 else 'ascending', 'none']
            got = [k['aria'] for k in c['clicks']]
            if got != want:
                fails.append('%s col %d «%s»: aria-sort %s, expected %s' % (where, c['i'], c['head'][:30], got, want))
            kind = 'date' if r['kind'] == 'date' else 'num'
            for k, d in ((0, first), (1, -first)):
                ks = keys(c['clicks'][k]['texts'], kind)
                bad = monotonic(ks, d)
                if bad is not None:
                    fails.append('%s col %d «%s»: %s order breaks at row %d (%r after %r)' % (
                        where, c['i'], c['head'][:30], 'ascending' if d > 0 else 'descending', bad,
                        c['clicks'][k]['texts'][bad][:40], [t for t, x in zip(c['clicks'][k]['texts'][:bad], ks[:bad]) if x is not None][-1:]))
            if not c['restored']:
                fails.append('%s col %d «%s»: the third click did not restore the build order' % (where, c['i'], c['head'][:30]))
        for x in r['restores']:
            if not x['present'] or not x['ok']:
                fails.append('%s: %s did not restore the build order (present %s)' % (where, x['how'], x['present']))


def check_tableview(tv, L, page_lang, fails, stats):
    where = '%s page / %s / Table view' % (page_lang, L)
    if tv.get('missing'):
        fails.append('%s: %s missing' % (where, tv['missing']))
        return
    data_cols = [k for k in tv['keys'] if k != 'layer']   # the data columns (th.tc-<key>) but the layer, which keeps the map's order
    if sorted(tv['sortable']) != sorted(data_cols):
        fails.append('%s: sort buttons on %s, expected on every data column but the layer: %s' % (where, tv['sortable'], data_cols))
    for c in tv['res']:
        stats['tv_columns'] += 1
        got = [s['aria'] for s in c['seq']]
        if got != ['ascending', 'descending', 'none']:
            fails.append('%s «%s»: aria-sort %s' % (where, c['k'], got))
        if not c['restored']:
            fails.append('%s «%s»: the third click did not restore the layer order' % (where, c['k']))
        if c['seq'][0]['order'] == c['seq'][1]['order'] and len(set(c['seq'][0]['texts'])) > 1:
            fails.append('%s «%s»: ascending and descending give the same order' % (where, c['k']))
        if c['k'] == 'since':
            for n, d in ((0, 1), (1, -1)):
                ks = [None if not re.match(r'^\d{4}$', t) else int(t) for t in c['seq'][n]['texts']]
                if monotonic(ks, d) is not None:
                    fails.append('%s «since»: %s order of the years broken' % (where, 'ascending' if d > 0 else 'descending'))


def main():
    a = sys.argv[1:]
    out = a[a.index('--out') + 1] if '--out' in a else None
    man = json.loads((DIST / 'manifest.json').read_text(encoding='utf-8'))
    langs = list(man['languages'])
    only = a[a.index('--only') + 1].split(',') if '--only' in a else langs
    fails, stats, report = [], {'tables': 0, 'columns': 0, 'tv_columns': 0, 'views': 0}, []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for PL in only:
            page = DIST / man['languages'][PL]['path']
            p = br.new_page(viewport={'width': 1280, 'height': 900})
            errors = []
            p.on('pageerror', lambda e, x=errors: x.append(str(e)[:200]))
            p.goto(page.as_uri(), wait_until='load', timeout=180000)
            p.evaluate("() => (window.__langReady ? Promise.all((JSON.parse(document.getElementById('app').getAttribute('data-other-langs')||'[]')).map(l => window.__langReady(l))) : true)")
            p.wait_for_timeout(300)
            for L in [PL] + [x for x in langs if x != PL]:
                p.evaluate('(l) => window.__setLang(l)', L)
                p.wait_for_timeout(200)
                recs = p.evaluate(JS_TABLES, L)
                check_tables(recs, L, PL, fails, stats)
                tv = p.evaluate(JS_TABLEVIEW)
                check_tableview(tv, L, PL, fails, stats)
                stats['views'] += 1
                report.append({'page': PL, 'lang': L, 'tables': [{'id': r['id'], 'kind': r['kind'], 'buttons': r['buttons'],
                                                                  'sortable': [c['head'] for c in r['cols']]} for r in recs],
                               'tableview_buttons': tv.get('buttons')})
                print('%s page, %s shown: %d sortable tables, %d sortable columns; Table view %s buttons' % (
                    PL, L, len(recs), sum(len(r['cols']) for r in recs), tv.get('buttons')))
            for e in errors:
                fails.append('%s page: page error %s' % (PL, e))
            p.close()
        br.close()
    if out:
        pathlib.Path(out).write_text(json.dumps({'stats': stats, 'fails': fails, 'views': report}, ensure_ascii=False, indent=1), encoding='utf-8')
    print('\nsort_check: %d views, %d tables, %d sortable columns, %d Table-view columns — %s' % (
        stats['views'], stats['tables'], stats['columns'], stats['tv_columns'], 'PASS' if not fails else 'FAIL (%d)' % len(fails)))
    for f in fails[:60]:
        print('  FAIL', f)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
