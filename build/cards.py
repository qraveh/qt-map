# -*- coding: utf-8 -*-
"""The map's three cards — technology, machine, architecture — rendered in Python for the Atlas's record pages (27 Sep 2026).

A port of inspect(), inspectMachine() and inspectPath() of build/map_js.py with their helpers (T, vt, fmtT, esc, lk, evGlyph,
evHTML, machCell, usedByHTML, placeText, isOffd / isEmpty, the machines' slim form of build_html.mach_slim): the same
texts in both languages, the same blocks in the same order, the same class names, the same numbers and times (JavaScript's
String(), toFixed, toPrecision and toExponential are reproduced exactly). No JavaScript in the output; every link is a real href:
    a technology       → {base}technology/{id}.html       "Open on the map" → {base}index.html#station-{id}
    a machine       → {base}machine/{id}.html          "Open on the map" → {base}index.html#machine-{id}
    an architecture → {base}architecture/{pid}.html    "Open on the map" → {base}index.html#architecture-{pid}
    (base: from the page to its language's root — '../' on an English record page, '../../ru/' on a Russian one, '../../he/' on a Hebrew
    one — so that every link stays in the page's language; before 29 Sep 2026 the non-English cards linked the English pages)
    "Brief →"       → #brief (the brief is on the technology's own page); a machine → its own page machine/<id>.html
What only the live map can do is left out: the drag grip and dock buttons, "clear machine", the lens-row highlight and the hints
that describe clicks on the map (the "Used by" hint keeps its other clauses). EXTRAS (default True) adds what the spec lists
beyond the map's cards: the machine's access, codes, flags and standard records, and the summary and evidence of its gap / none /
undisclosed cells; the architecture's machines. cards.EXTRAS = False renders the map's cards alone.

    import cards
    cards.load()                                     # data/graph.json, data/machines.json, build/labels.py, the briefs' key references
    cards.station_card_html(node_id, lang, base)     # lang: any of langs.LANGS; base = prefix to the language's root
    cards.machine_card_html(machine_id, lang, base)
    cards.architecture_card_html(path_id, lang, base)
"""
import html, json, math, os, re, sys
import regvocab
from langs import LANGS, pick   # 29 Sep 2026: every text is a (en, ru[, he]) tuple; a missing language reads English

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
EXTRAS = True

# ---------- the constants of map_js.py
FAMC = {'SC': 'var(--sc)', 'ION': 'var(--ion)', 'ATOM': 'var(--atom)', 'PHOTON': 'var(--photon)', 'SPIN': 'var(--spin)',
        'DEFECT': 'var(--defect)', 'TOPO': 'var(--topo)', 'ANNEAL': 'var(--anneal)'}
FAMN = {'SC': ('superconducting circuits', 'сверхпроводниковые схемы', 'מעגלים מוליכי-על'), 'ION': ('trapped ions', 'ионы в ловушках', 'יונים לכודים'),
        'ATOM': ('neutral atoms', 'нейтральные атомы', 'אטומים ניטרליים'), 'PHOTON': ('photonics', 'фотоника', 'פוטוניקה'),
        'SPIN': ('semiconductor spins', 'полупроводниковые спины', 'ספינים במוליכים למחצה'), 'DEFECT': ('defect spins', 'спины дефектов', 'ספיני פגם'),
        'TOPO': ('topological', 'топологические', 'טופולוגי'), 'ANNEAL': ('quantum annealers', 'квантовый отжиг', 'מחשבי הרפיה קוונטית')}
MACH_FAMILIES = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']
OFFDEF = ('a crossing technology: it takes a trait from the other side of the natural/fabricated divide — hatched on the map (see §7.5)',
          'сквозная технология: берёт свойство с другой стороны раздела естественное/искусственное — на карте заштрихована (см. §7.5)',
          'טכנולוגיה חוצה: היא נוטלת מאפיין מהצד השני של החלוקה טבעי–מיוצר — מקווקוות במפה (ראו §7.5)')
EMPTYDEF = ('a technology with no demonstrated technology yet', 'технология, для которой технологии ещё нет', 'טכנולוגיה שעדיין אין לה מימוש שהודגם')
PLACES = ['RT', '4K', 'mK', 'none']   # CATS.place
EVG = (('figure', '▣'), ('whitepaper', '▥'), ('paper', '▤'), ('vendor', '▦'), ('datasheet', '▧'), ('press', '▨'))
NA_T = {'none': ('none — nothing in this layer', 'none — в этом слое ничего нет', 'none — אין דבר בשכבה זו'),
        'undisclosed': ('undisclosed — exists, nothing published', 'undisclosed — есть, но не опубликовано', 'undisclosed — קיים, אך דבר לא פורסם')}
PROF_KEYS = ('qubit_type', 'gate_mechanism', 'connectivity', 'control', 'control_placement', 'readout', 'role', 'gate_evidence', 'decoder_mode')
PROF_T = (('qubit type', 'тип кубита', 'סוג הקיוביט'), ('gate mechanism', 'механизм вентиля', 'מנגנון השער'), ('connectivity', 'связность', 'קישוריות'),
          ('control', 'управление', 'בקרה'), ('control placement', 'размещение управления', 'מיקום הבקרה'), ('readout', 'считывание', 'קריאה'),
          ('role', 'роль', 'תפקיד'), ('gate evidence', 'свидетельство вентиля', 'ראיה לשער'), ('decoder mode', 'режим декодера', 'מצב המפענח'))
# the three register fields of 2 Oct 2026, in the reader's words (the register's codes stay out of the page: the editor's rule on own codes)
PROF_WORDS = {
    'role': {'scale-demonstrator': ('scale demonstrator — built to prove scale, performance not published, not operated for users', 'демонстратор масштаба — построен, чтобы доказать масштаб; производительность не опубликована; пользователям не предоставлялся', 'מדגים קנה מידה — נבנה להוכחת קנה מידה, הביצועים לא פורסמו, לא הופעל עבור משתמשים'),
             'exploratory': ('exploratory — operated for users as a technical demonstration', 'пробная — работала для пользователей как техническая демонстрация', 'ניסיונית — הופעלה עבור משתמשים כהדגמה טכנית')},
    'gate_evidence': {'device-benchmark': ('a benchmark paper with its protocol', 'статья с бенчмарком и протоколом', 'מאמר מדידה עם הפרוטוקול שלו'),
                      'platform-calibration': ('calibration data shown on a cloud platform', 'калибровочные данные на облачной платформе', 'נתוני כיול שהוצגו בפלטפורמת ענן'),
                      'vendor-dashboard': ("the vendor's datasheet or dashboard", 'спецификация или дашборд производителя', 'גיליון הנתונים או לוח המחוונים של היצרן'),
                      'vendor-figure': ('a number stated by the vendor, protocol unstated', 'число, названное производителем, без протокола', 'מספר שהיצרן נקב בו, ללא פרוטוקול'),
                      'figure': ('a published figure (source class not yet tagged)', 'опубликованная цифра (класс источника ещё не помечен)', 'נתון שפורסם (סוג המקור טרם סומן)'),
                      'vendor-statement': ('words only, no figure ("comparable to…")', 'только слова, без цифры («сопоставим с…»)', 'מילים בלבד, ללא נתון ("דומה ל…")'),
                      'none': ('no published figure', 'опубликованной цифры нет', 'אין נתון שפורסם')},
    'decoder_mode': {'none': ('none', 'нет', 'אין'), 'planned': ('planned — named in a roadmap only', 'планируется — назван только в дорожной карте', 'מתוכנן — נזכר רק במפת הדרכים'),
                     'offline': ('offline — syndromes decoded after the run', 'офлайн — синдромы декодируются после прогона', 'לא מקוון — הסינדרומים מפוענחים אחרי הריצה'),
                     'real-time-throughput': ('real-time throughput — keeps up with the syndrome stream, no feedback into the circuit', 'в реальном времени без обратной связи — успевает за потоком синдромов, в схему не возвращает', 'תפוקה בזמן אמת — עומד בקצב זרם הסינדרומים, ללא משוב למעגל'),
                     'feed-forward': ('feed-forward — the decoder\'s result acts inside the run (closed loop)', 'с обратной связью — результат декодера действует внутри прогона (замкнутый цикл)', 'משוב קדימה — תוצאת המפענח פועלת בתוך הריצה (לולאה סגורה)')}}
KIND = {'paper': ('paper', 'статья', 'מאמר'), 'whitepaper': ('whitepaper', 'whitepaper', 'מסמך טכני'), 'product': ('product page', 'страница продукта', 'דף מוצר'),
        'docs': ('docs', 'документация', 'תיעוד'), 'blog': ('blog', 'блог', 'בלוג'), 'press': ('press', 'пресса', 'עיתונות'), 'other': ('link', 'ссылка', 'קישור')}
PN = (('gates', ('gates', 'вентили', 'שערים')), ('transport', ('transport', 'транспорт', 'הובלה')), ('1q', ('1Q', '1Q', '1Q')), ('readout', ('readout', 'считывание', 'קריאה')),
      ('reset', ('reset', 'сброс', 'איפוס')))
USEBY_HINT = ('↗ its register card · paper / product / press: links that name the machine (attribution checked on 20 Sep 2026)',
              '↗ карточка реестра · статья / продукт / пресса: ссылки, где машина названа (атрибуция проверена 20 сентября 2026)',
              '↗ כרטיס המרשם שלה · מאמר / מוצר / עיתונות: קישורים שבהם המכונה נזכרת בשמה (הייחוס נבדק ב-20 בספטמבר 2026)')
MAP_LINK = ('Open on the map', 'Открыть на карте', 'פתח במפה')
ACTORS_GOALS = ('Actors & goals', 'Участники и цели', 'שחקנים ויעדים')   # the architecture card's block title; build/pages.py finds the block by it
PLAIN_UNITS = {'s', 'Hz', 'count', '1', 'fraction', 'dimensionless', 'ratio', 'relative', 'population'}   # machine records: other units are printed

G = None
NODE, PATH, PRIM, ALT, V, MACH, BY_NODE, SHORT, KEYREFS, URLS, _LISTS = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}


# ---------- loading
def _okeys(d):
    """a JS object's key order: integer keys ascending, then the others in insertion order"""
    ints = sorted((k for k in d if re.fullmatch(r'0|[1-9][0-9]*', k)), key=int)
    return ints + [k for k in d if k not in ints]


def _mach_urls():
    """the register's URLs as build_html.py sets them (MACH_URLS; machines.json carries none)"""
    try:
        s = open(os.path.join(BUILD, 'build_html.py'), encoding='utf-8').read()
        d = dict(re.findall(r"'(register|tech)'\s*:\s*'([^']*)'", re.search(r'MACH_URLS\s*=\s*\{[^}]*\}', s).group(0)))
        if d.get('register'): return d
    except Exception: pass
    return {'register': 'machine/', 'tech': 'technology/'}


def _keyrefs():
    """KEYREFS as the build computes them (briefs.key_refs_all), read only: a work number the table lacks is assigned in memory,
    never written (worknum.flush is the build's job)"""
    try:
        import briefs, worknum
        fl = worknum.flush; worknum.flush = lambda: None
        try: return briefs.key_refs_all(briefs.load_briefs())
        finally: worknum.flush = fl
    except Exception as e:
        sys.stderr.write('cards: no key references (%s)\n' % e); return {}


def load(keyrefs=None):
    """keyrefs: {station: [{n, url, year, short[, label]}]} — the build's BR.key_refs_all(B) or its slim form; computed when omitted"""
    global G, V, URLS, KEYREFS, SHORT
    if BUILD not in sys.path: sys.path.insert(0, BUILD)
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8')); V = G['vocab']
    NODE.clear(); NODE.update((n['id'], n) for n in G['nodes'])
    PATH.clear(); PATH.update((p['id'], p) for p in G['paths'])
    PRIM.clear(); ALT.clear()
    for p in G['paths']:
        for k in _okeys(p['slots']):
            for i, nid in enumerate(p['slots'][k]): (ALT if i else PRIM).setdefault(nid, []).append(p['id'])
    mp = os.path.join(ROOT, 'data', 'machines.json')
    M = json.load(open(mp, encoding='utf-8')) if os.path.exists(mp) else {'machines': [], 'by_node': {}}
    MACH.clear(); MACH.update((m['id'], m) for m in M['machines'])
    BY_NODE.clear(); BY_NODE.update((k, v) for k, v in M['by_node'].items() if not str(k).startswith('∅'))
    try:
        from labels import SHORT as S
    except Exception: S = {}
    SHORT = S; URLS = _mach_urls(); _LISTS.clear()
    KEYREFS = keyrefs if keyrefs is not None else _keyrefs()


# ---------- JavaScript numbers (ECMA-262): String(x), toFixed, toPrecision, toExponential — exact, a tie goes to the larger n
def js_str(x):
    if isinstance(x, bool): return 'true' if x else 'false'
    if isinstance(x, int): return str(x)
    if x != x: return 'NaN'
    if x in (math.inf, -math.inf): return ('-' if x < 0 else '') + 'Infinity'
    if x == 0: return '0'
    if x < 0: return '-' + js_str(-x)
    mant, _, ex = repr(float(x)).partition('e'); ip, _, fp = mant.partition('.'); ds = ip + fp
    n = len(ip) + int(ex or 0) - (len(ds) - len(ds.lstrip('0'))); ds = ds.strip('0'); k = len(ds)
    if k <= n <= 21: return ds + '0' * (n - k)
    if 0 < n <= 21: return ds[:n] + '.' + ds[n:]
    if -6 < n <= 0: return '0.' + '0' * -n + ds
    return ds[0] + ('.' + ds[1:] if k > 1 else '') + 'e' + ('+' if n > 0 else '-') + str(abs(n - 1))


def _sig(x, p):
    """x > 0 → (n, e): 10^(p-1) <= n < 10^p and n·10^(e-p+1) nearest to x"""
    a, b = x.as_integer_ratio()
    ge = lambda k: a >= b * 10 ** k if k >= 0 else a * 10 ** -k >= b   # x >= 10^k
    e = len(str(a)) - len(str(b))
    while not ge(e): e -= 1
    while ge(e + 1): e += 1
    while True:
        k = e - p + 1
        n = (2 * a + b * 10 ** k) // (2 * b * 10 ** k) if k >= 0 else (2 * a * 10 ** -k + b) // (2 * b)
        if n < 10 ** p: return n, e
        e += 1


def _special(x):
    if x != x: return '', 'NaN'
    s = '-' if x < 0 else ''
    return s, ('Infinity' if abs(x) == math.inf else None)


def to_fixed(x, f=0):
    s, sp = _special(x); x = abs(x)
    if sp or x >= 1e21: return s + (sp or js_str(x))
    a, b = x.as_integer_ratio(); n = str((2 * a * 10 ** f + b) // (2 * b))
    if f: n = n.rjust(f + 1, '0'); n = n[:-f] + '.' + n[-f:]
    return s + n


def to_precision(x, p):
    s, sp = _special(x); x = abs(x)
    if sp: return s + sp
    n, e = _sig(x, p) if x else (0, 0); m = str(n).rjust(p, '0')
    if e < -6 or e >= p: return s + m[0] + ('.' + m[1:] if p > 1 else '') + 'e' + ('+' if e >= 0 else '-') + str(abs(e))
    if e == p - 1: return s + m
    return s + (m[:e + 1] + '.' + m[e + 1:] if e >= 0 else '0.' + '0' * (-e - 1) + m)


def to_exponential(x, f):
    s, sp = _special(x); x = abs(x)
    if sp: return s + sp
    n, e = _sig(x, f + 1) if x else (0, 0); m = str(n).rjust(f + 1, '0')
    return s + m[0] + ('.' + m[1:] if f else '') + 'e' + ('+' if e >= 0 else '-') + str(abs(e))


def js_log10(x): return -math.inf if x == 0 else (math.nan if x < 0 else math.log10(x))


def fmt_n(v): return to_fixed(v, 0) if v >= 10 else to_precision(v, 2)


def fmt_t(x):
    """fmtT: log10 seconds → ns / µs / ms / s"""
    if x is None: return '—'
    try: v = math.pow(10, x)
    except OverflowError: v = math.inf
    if v >= 1: return fmt_n(v) + ' s'
    if v >= 1e-3: return fmt_n(v * 1e3) + ' ms'
    if v >= 1e-6: return fmt_n(v * 1e6) + ' µs'
    return fmt_n(v * 1e9) + ' ns'


# ---------- text
def _s(x): return '' if x is None else (x if isinstance(x, str) else js_str(x))
def esc(x): return html.escape(_s(x), False)   # text: & < > (the JS esc)
def ea(x): return html.escape(_s(x))           # attribute values
def T(L, *texts): return pick(L, texts)   # T(L, en, ru[, he])


def vt(L, tab, key):
    e = V[tab].get(_s(key)); return T(L, *e) if e else _s(key)


_AX = re.compile(r'arXiv:\s?((?:[0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]{7})(?:v[0-9]+)?)')
_DOI = re.compile(r'(?<![A-Za-z0-9_])(10\.[0-9]{4,9}/[^\s,;)]+)')
_URL = re.compile(r'href="https?://[^"]*"|https?://[^\s<)]+')
_A = '<a href="%s" target="_blank" rel="noopener">%s</a>'


def lk(s):
    """esc, then arXiv ids, DOIs and bare URLs as links (the JS lk, same regexes in the same order)"""
    s = _AX.sub(lambda m: _A % ('https://arxiv.org/abs/' + m.group(1), m.group(0)), esc(s))
    s = _DOI.sub(lambda m: _A % ('https://doi.org/' + m.group(1), m.group(0)), s)
    return _URL.sub(lambda m: m.group(0) if m.group(0).startswith('href="') else _A % (m.group(0), m.group(0)), s)


def _u16(s): return len(s.encode('utf-16-le')) // 2   # JS .length


# ---------- links
def _st(base, nid, L, cls=None, title=None, text=None):
    return '<a href="%stechnology/%s.html"%s%s>%s</a>' % (ea(base), ea(nid), (' class="%s"' % cls) if cls else '',
                                                          (' title="%s"' % ea(title)) if title is not None else '', esc(pick(L, NODE[nid])) if text is None else text)


def _arch(base, pid, L): return '<a href="%sarchitecture/%s.html">%s</a>' % (ea(base), ea(pid), esc(pick(L, PATH[pid])))


def _orglink(base, m, L):
    """the machine's organisation as a link to its page (organisation/<slug>.html) when the organisations register has one"""
    try:
        import orgs; sl = orgs.slug_for_machine(m.get('id') if isinstance(m, dict) else m)
    except Exception: sl = None
    name = esc(m['org'])
    return '<a class="org" href="%sorganisation/%s.html" title="%s">%s</a>' % (ea(base), ea(sl), ea(T(L, "the organisation's page", 'страница организации', 'דף הארגון')), name) if sl else name
def _maplink(base, kind, i, L):
    # the main page of the record's own language (base is that language's root), by its default document (index.html), so that the link
    # also works from a folder on disk
    return '<a class="maplink" href="%sindex.html#%s-%s">%s</a>' % (ea(base), kind, ea(i), esc(T(L, *MAP_LINK)))


def _mrefs(L, m):
    return ' '.join('<a class="mref" href="%s" target="_blank" rel="noreferrer" title="%s">%s</a>' % (ea(r['url']), ea(r.get('title') or r['url']), esc(T(L, *KIND.get(r['kind'], KIND['other']))))
                    for r in (m.get('refs') or [])[:3])


def _mli(L, mid, base, role, tail=''):
    m = MACH[mid]
    return '<li%s><a href="%smachine/%s.html" title="%s">%s</a> <span class="empty">%s</span> %s%s</li>' % (
        (' class="%s"' % role) if role else '', ea(base), ea(mid), ea(m['name'] + ' · ' + m['org']), esc(m['name']), _orglink(base, m, L), _mrefs(L, m), tail)


# ---------- machines: the cells of machines.json as mach_slim reads them
def _cells(m, k):
    """(technologies, gaps, nones) of layer k: full cells; a gap's node starts with ∅, none / undisclosed are cell values"""
    st, gp, na = [], [], []
    for c in (m.get('layers') or {}).get(k, []):
        node = str(c['node'])
        (gp if node.startswith('∅') else na if c.get('state') in ('none', 'undisclosed') or node in ('none', 'undisclosed') else st).append(c)
    return st, gp, na


def _tup(c):
    e = c.get('evidence') or {}
    return [c['node'], c.get('role', ''), c.get('summary', ''), e.get('type', ''), e.get('url', ''), e.get('locator', ''), bool(e.get('verified'))]


def _mcell(m, nid):
    """machCell: the machine's technology cell on that technology's layer"""
    n = NODE.get(nid)
    if not n: return None
    return next((_tup(c) for c in _cells(m, str(n['layer']))[0] if c['node'] == nid), None)


def _ev_glyph(t): return next((g for k, g in EVG if k in _s(t)), '◌')


def _ev_html(L, c):
    g, tl = _ev_glyph(c[3]), ea(c[3] or '')
    a = ('<a class="ev" href="%s" target="_blank" rel="noreferrer" title="%s">%s</a>' % (ea(c[4]), tl, g)) if c[4] else '<span class="ev" title="%s">%s</span>' % (tl, g)
    return a + ((' <span class="loc">%s</span>' % esc(c[5])) if c[5] else '') + ' <span class="vf" title="%s">%s</span>' % (
        ea(T(L, 'verified', 'проверено', 'מאומת') if c[6] else T(L, 'not verified', 'не проверено', 'לא מאומת')), '✅' if c[6] else '🔎')


def _used_by(L, n, base):
    t = lambda *x: esc(T(L, *x))
    ub = BY_NODE.get(n['id']) or {}
    P = [i for i in ub.get('primary') or [] if i in MACH]; A = [i for i in ub.get('alternate') or [] if i in MACH and i not in P]
    N = len(P) + len(A)
    if not N: return '<div class="space useby"><h4>%s</h4></div>' % t('Used by no registered machine', 'Не используется ни одной зарегистрированной машиной', 'אינה בשימוש באף מכונה במרשם')
    head = '%s %d %s (%d %s · %d %s)' % (t('Used by', 'Используют', 'בשימוש:'), N, t('machine' if N == 1 else 'machines', 'машин', 'מכונה' if N == 1 else 'מכונות'), len(P), t('primary', 'основная', 'ראשית'),
                                        len(A), t('alternate', 'альтернатива', 'חלופית'))
    def li(i, role):
        c = _mcell(MACH[i], n['id'])
        return _mli(L, i, base, role, ((' ' + _ev_html(L, c)) if c else '') + ((' <span class="empty">(%s)</span>' % t('alternate', 'альтернатива', 'חלופית')) if role == 'alternate' else ''))
    groups = ''
    for f in MACH_FAMILIES:
        ps, as_ = [i for i in P if MACH[i]['family'] == f], [i for i in A if MACH[i]['family'] == f]
        if ps or as_:
            groups += '<li class="fam"><i class="sw" style="--c:%s"></i>%s <span class="empty">%d</span></li>' % (FAMC.get(f, 'var(--mid)'), t(*FAMN.get(f, (f, f))), len(ps) + len(as_))
            groups += ''.join(li(i, 'primary') for i in ps) + ''.join(li(i, 'alternate') for i in as_)
    return '<div class="space useby"><h4>%s</h4><ul class="useby">%s</ul><div class="empty" style="margin-top:4px">%s</div></div>' % (head, groups, t(*USEBY_HINT))


# ---------- standard records (the technology card's form; a machine's records have no grade tag and often no text)
def _rec_val(L, r, machine):
    num, unit = r.get('num'), r.get('unit')
    if num is None: return '<span class="empty">%s</span>' % esc(T(L, 'not published', 'не опубликовано', 'לא פורסם'))
    if unit == 's': return fmt_t(js_log10(num))
    if unit == 'Hz': return to_exponential(num, 1) + ' Hz'
    if unit == 'count': return js_str(num)
    v = to_exponential(num, 2) if (num < 0.01 or num > 1e4) else js_str(float(to_precision(num, 3)))
    return v + (' ' + esc(unit) if machine and unit and unit not in PLAIN_UNITS else '')


def _records(L, recs, machine=False):
    rk, out = V.get('RECKEYS') or {}, []
    for r in recs:
        d = [esc(r.get('text')), esc(r.get('date')), '<a href="%s" target="_blank" rel="noopener">%s</a>' % (ea(r.get('url')), esc(T(L, 'source', 'источник', 'מקור')))]
        out.append('<div class="def"><div><span class="k">%s</span> → <b>%s</b> <span class="empty">· %s</span></div><div class="d">%s%s%s</div></div>' % (
            esc(T(L, *(rk.get(r['key']) or (r['key'],)))), _rec_val(L, r, machine), esc(T(L, *regvocab.SCOPE.get(r.get('scope') or '', (r.get('scope') or '',) * 2))),
            ' · '.join(x for x in d if x or not machine), (' [%s]' % esc(r.get('tag'))) if r.get('tag') or not machine else '',
            (' <span class="empty" title="%s">ⓘ</span>' % ea(r['note'])) if r.get('note') else ''))
    return '<div class="space"><h4>%s</h4>%s</div>' % (esc(T(L, 'Standard records', 'Стандартные рекорды', 'רשומות סטנדרטיות')), ''.join(out))


# ---------- helpers of the technology card
def _fam(nid):
    ps = PRIM.get(nid, []) + ALT.get(nid, [])
    return PATH[ps[0]]['family'] if ps else None


def _place_text(L, n):
    ps = (n['e'].get('place') or []) or ['none']
    return ' / '.join(vt(L, 'PLACE', p) for p in [p for p in PLACES if p in ps] + [p for p in ps if p not in PLACES])


def _key_label(sid, num):
    """the IEEE text of work num as the brief's English Sources list prints it (li#brief-<sid>-en-src-<n> span.ref)"""
    if sid not in _LISTS:
        try:
            import brief_refs; _LISTS[sid] = brief_refs.list_html(sid, 'en') or ''
        except Exception: _LISTS[sid] = ''
    h = _LISTS[sid]; i = h.find('<li id="brief-%s-en-src-%s"' % (sid, num))
    j = h.find('<span class="ref">', i, h.find('</li>', i)) if i >= 0 else -1
    if j < 0: return ''
    depth, k = 1, j + 18
    for m in re.finditer(r'<span\b|</span>', h[k:]):   # the span's own end (textContent of span.ref)
        depth += 1 if m.group(0) == '<span' else -1
        if not depth: return html.unescape(re.sub(r'<[^>]+>', '', h[k:k + m.start()])).strip()
    return ''


def _wrap(kind, parts): return '<section class="card card-%s">%s</section>' % (kind, '\n'.join(p for p in parts if p))


# ---------- the technology card (inspect)
def station_card_html(nid, lang, base=''):
    L, n = lang, NODE[nid]; t = lambda *x: esc(T(L, *x)); c = n.get('c'); b = n.get('b') or {}; e = n.get('e') or {}
    rows = [(T(L, '(a) carrier affinity', '(a) сродство носителя', '(a) זיקת הנושא'), vt(L, 'AFF', n['aff'])),
            (T(L, '(b) time · entangling', '(b) время · запутывание', '(b) זמן · שזירה'), fmt_t(b.get('t')) + ((' · ' + vt(L, 'DET', b.get('det'))) if b.get('det') != 'na' else '')),
            (T(L, '(c) readout', '(c) считывание', '(c) קריאה'), '%s · %s · %s · %s' % (vt(L, 'MECH', c.get('mech')), fmt_t(c.get('t')),
                                                                         T(L, 'destructive', 'разрушающее', 'הרסנית') if c.get('destr') else T(L, 'non-destructive', 'неразрушающее', 'לא הרסנית'),
                                                                         T(L, 'mid-circuit', 'внутрисхемное', 'mid-circuit') if c.get('mid') else T(L, 'no mid-circuit', 'не внутрисхемное', 'ללא mid-circuit')) if c is not None else '—'),
            (T(L, '(d) mobility', '(d) подвижность', '(d) ניידות'), vt(L, 'MOB', n['d'])),
            (T(L, '(e) control', '(e) управление', '(e) בקרה'), '—' if e.get('mod') == 'none' else '%s @ %s' % (vt(L, 'MOD', e.get('mod')), _place_text(L, n))),
            (T(L, '(f) error structure', '(f) структура ошибки', '(f) מבנה השגיאה'), ', '.join(vt(L, 'ERR', x) for x in n['f'])),
            (T(L, '(g) manufacturing', '(g) производство', '(g) ייצור'), vt(L, 'FAB', n['g']))]
    marks = []
    if n.get('offdiag'):
        marks.append('<div><span class="flag off" title="%s">%s</span> — %s</div>' % (ea(T(L, *OFFDEF)), t('crossing technology', 'сквозная технология', 'טכנולוגיה חוצה'),
                                                                                     esc('; '.join(vt(L, 'OFFDIAG', o) for o in n['offdiag']))))
    if n.get('status') == 'X': marks.append('<div><span class="flag empty" title="%s">∅ %s</span></div>' % (ea(T(L, *EMPTYDEF)), t('empty slot', 'пустой слот', 'משבצת ריקה')))
    flags = ('<div class="marks"><span class="tk">%s</span>%s</div>' % (t('Reading marks', 'Метки чтения', 'סימוני המפה'), ''.join(marks))) if marks else ''
    keys = ''
    if KEYREFS.get(nid):
        kr = []
        for r in KEYREFS[nid]:
            lab = _key_label(nid, r['n']) or r.get('label') or r.get('short') or ''
            if _u16(lab) > 92: lab = lab.encode('utf-16-le')[:180].decode('utf-16-le', 'ignore') + '…'
            kr.append('<div class="kr"><a href="%s" target="_blank" rel="noopener">[%s]</a> %s%s</div>' % (
                ea(r.get('url')), esc(r['n']), esc(lab), (' <span class="empty">· %s</span>' % esc(r['year'])) if r.get('year') else ''))
        keys = '<div class="space keys"><h4>%s</h4>%s</div>' % (t('Key references', 'Ключевые источники', 'מקורות מרכזיים'), ''.join(kr))
    defs = ''.join('<div class="def"><div><span class="k">%s</span> → <b>%s</b></div><div class="d">%s: %s · %s · <a href="%s" target="_blank" rel="noopener">%s</a></div></div>' % (
        esc(d['metric']), esc(d['value']), t('defines', 'определяет', 'מגדירה'), esc(vt(L, 'OUT', d['out'])), esc(d['date']), ea(d['url']), t('source', 'источник', 'מקור'))
        for d in n.get('defines') or []) or '<p class="empty">%s</p>' % t('no dated attribute', 'нет датированных атрибутов', 'אין תכונות מתוארכות')
    attrs = ('<p style="margin:6px 0 0">%s</p>' % lk(pick(L, n['attrs']))) if pick(L, n.get('attrs') or {}) else ''
    al = ALT.get(nid, [])
    tags = ''.join('<div class="pathtag"><i class="sw" style="--c:%s"></i>%s%s<span class="empty"> — %s · %s</span></div>' % (
        FAMC.get(PATH[p]['family']), _arch(base, p, L), (' <span class="empty">(%s)</span>' % t('alternate', 'альтернатива', 'חלופית')) if p in al else '',
        esc(PATH[p]['actors']), esc(PATH[p]['goals'])) for p in PRIM.get(nid, []) + al) or '<p class="empty">%s</p>' % t('on no architecture', 'не входит ни в одну архитектуру', 'אינה חלק מאף ארכיטקטורה')
    E = G['edges']
    req_out = [x for x in E if x['type'] == 'requires' and x['src'] == nid]; req_in = [x for x in E if x['type'] == 'requires' and x['dst'] == nid]
    rep = [x for x in E if x['type'] == 'replaces' and nid in (x['src'], x['dst'])]; con = [x for x in E if x['type'] == 'conflicts' and nid in (x['src'], x['dst'])]
    other = lambda x: x['dst'] if x['src'] == nid else x['src']
    mk = lambda x: ('<span class="empty">°</span>' if x.get('any') else '') + ('<span class="empty">·</span>' if x.get('strength') == 'soft' else '')
    edges = ''
    if req_out: edges += '<div><b>%s:</b> %s</div>' % (t('needs', 'нужно', 'דורשת'), ', '.join(_st(base, x['dst'], L) + mk(x) for x in req_out))
    if req_in: edges += '<div><b>%s:</b> %s</div>' % (t('needed by', 'нужен для', 'נחוצה עבור'), ', '.join(_st(base, x['src'], L) + mk(x) for x in req_in))
    if rep: edges += '<div><b>%s:</b> %s</div>' % (t('alternatives', 'альтернативы', 'חלופות'), ', '.join(_st(base, other(x), L) for x in rep))
    if con:
        edges += '<div><b style="color:var(--crit)">%s:</b></div>' % t('conflicts with', 'конфликтует с', 'מתנגשת עם') + ''.join(
            '<div class="conf"><div>%s <span class="cst %s">%s</span></div><div class="cm">%s</div><div class="cm"><span class="tk">%s</span> %s</div><div class="cm"><span class="tk">%s</span> %s%s</div></div>' % (
                _st(base, other(x), L), ea(x.get('status')), esc(vt(L, 'CONSTAT', x.get('status'))), lk(pick(L, x)), t('price', 'цена', 'מחיר'),
                lk(pick(L, x.get('price') or {}) or ''), t('mitigation', 'смягчение', 'הפחתה'), lk(pick(L, x.get('mitig') or {}) or ''),
                (' · <a href="%s" target="_blank" rel="noopener">%s</a>' % (ea(x['url']), esc(x.get('date')))) if x.get('url') else '') for x in con)
    edges += ('<div class="empty" style="margin-top:4px">° %s · %s</div>' % (t('one of several that would do', 'одно из нескольких, что подошли бы', 'אחת מכמה שהיו מתאימות'),
                                                                            t('the usual route, not a strict need', 'обычный маршрут, не строгая необходимость', 'הדרך המקובלת, לא דרישה מחייבת'))
              if (req_out or req_in or rep or con) else '<p class="empty">—</p>')
    return _wrap('station', [
        '<h3>%s</h3>' % esc(pick(L, n)),
        '<div class="meta">%s · %s %s %s · %s%s</div>' % (esc(nid), t('layer', 'слой', 'שכבה'), n['layer'], esc(pick(L, G['layers'][n['layer'] - 1])), esc(vt(L, 'STATUS', n['status'])),
                                                        (' · %s %s' % (t('since', 'с', 'מאז'), n['since'])) if n.get('since') is not None and n['since'] < 2030 else ''),
        '<div class="mlinks">%s</div>' % _maplink(base, 'station', nid, L),
        '<p>%s</p><div>%s</div>' % (lk(pick(L, n['desc'])), flags),
        '<a class="briefbtn" href="#brief">%s</a>' % t('Brief →', 'Обзор →', 'תקציר ←'),
        keys,
        '<div class="space"><h4>%s</h4><dl>%s</dl></div>' % (t('Design space — attributes', 'Пространство проектирования — атрибуты', 'מרחב התכן — תכונות'),
                                                            ''.join('<dt>%s</dt><dd>%s</dd>' % (esc(k), esc(v)) for k, v in rows)),
        '<div class="space"><h4>%s</h4>%s%s</div>' % (t('Evaluation space — dated attributes', 'Пространство оценки — датированные атрибуты', 'מרחב ההערכה — תכונות מתוארכות'), defs, attrs),
        _records(L, n['records']) if n.get('records') else '',
        '<div class="space"><h4>%s</h4>%s</div>' % (t('Actors & goals — annotations', 'Участники и цели — аннотации', 'שחקנים ויעדים — ביאורים'), tags),
        '<div class="space"><h4>%s</h4>%s</div>' % (t('Edges', 'Рёбра', 'קשתות'), edges),
        _used_by(L, n, base)])


# ---------- the machine card (inspectMachine)
def machine_card_html(mid, lang, base=''):
    L, m = lang, MACH[mid]; t = lambda *x: esc(T(L, *x))
    role = lambda c: t('alternate', 'альтернатива', 'חלופית') if c.get('role') == 'alternate' else t('primary', 'основная', 'ראשית')
    more = lambda c: ' ' + _ev_html(L, _tup(c)) + (('<div class="ms">%s</div>' % lk(c['summary'])) if c.get('summary') else '')
    rows = ''
    for l in G['layers']:
        st, gp, na = _cells(m, str(l['n'])); h = ''
        for c in st:
            nm = _st(base, c['node'], L, 'alt' if c.get('role') == 'alternate' else 'prim') if c['node'] in NODE else esc(c['node'])
            h += '<div class="mc">%s <span class="empty">· %s</span>%s</div>' % (nm, role(c), more(c))
        for c in gp:
            h += ('<div class="mc"><span class="empty">— (%s: %s) · %s</span>%s</div>' % (t('Atlas gap', 'пробел Атласа', 'פער אטלס'), esc(c['node']), role(c), more(c)) if EXTRAS
                  else '<div class="mc empty">— (%s: %s)</div>' % (t('Atlas gap', 'пробел Атласа', 'פער אטלס'), esc(c['node'])))
        for c in na:
            v = esc(T(L, *NA_T.get(str(c['node']), (str(c['node']),) * 2)))
            h += ('<div class="mc"><span class="empty">— %s</span>%s</div>' % (v, more(c))) if EXTRAS else '<div class="mc empty">— %s</div>' % v
        rows += '<tr><td class="ln">%s %s</td><td>%s</td></tr>' % (l['n'], esc(pick(L, l)), h or '<span class="empty">—</span>')
    pf = m.get('profile') or {}
    def pword(k, v):
        w = PROF_WORDS.get(k, {}).get(str(v))
        return T(L, *w) if w else str(v)
    prof = ''.join('<div class="mc"><span class="empty">%s:</span> %s</div>' % (t(*PROF_T[i]), esc(pword(k, pf.get(k)))) for i, k in enumerate(PROF_KEYS)
                   if pf.get(k) and not (k == 'decoder_mode' and pf.get(k) == 'none') and not (k == 'gate_evidence' and pf.get(k) == 'none' and not pf.get('err_2q_median')))
    if EXTRAS:
        for lab, tip, vals in ((('codes', 'коды', 'קודים'), ('error-correcting codes the codes register links to this machine', 'коды коррекции ошибок, которые реестр кодов связывает с этой машиной',
                                                        'קודים לתיקון שגיאות שמרשם הקודים מקשר למכונה זו'), m.get('codes')),
                               (('flags', 'флаги', 'דגלים'), ("the register's caveats on this machine's data", 'оговорки реестра к данным этой машины', 'ההסתייגויות של המרשם לגבי נתוני מכונה זו'), pf.get('flags'))):
            if vals: prof += '<div class="mc"><span class="empty" title="%s">%s:</span> %s</div>' % (ea(T(L, *tip)), t(*lab), esc(', '.join((regvocab.flag_words(v, L) if lab[0] == 'flags' else v) for v in vals)))
    fam, q, sd, ec = m['family'], m.get('physical_qubits_num'), m.get('status_date'), m.get('evidence_counts') or {}
    meta = '%s · %s · %s%s · %s' % (_orglink(base, m, L), t(*FAMN.get(fam, (fam, fam))), esc(regvocab.status_l(m['status'], L)), (' (%s)' % esc(sd)) if sd else '',
                                    T(L, '%s physical qubits' % js_str(q), '%s %s' % (js_str(q), regvocab.ru_plural(q, regvocab.PLURAL['qubits'])),
                                      regvocab.he_count(js_str(q), regvocab.PLURAL_HE['qubits'])) if q is not None and q != '' else t('qubits not published', 'число кубитов не опубликовано', 'מספר הקיוביטים לא פורסם'))
    qa = pf.get('qubits_accessible')
    if qa and q and qa != q: meta += ' · ' + T(L, '%s of them made usable' % js_str(qa), '%s из них доступны пользователям' % js_str(qa), '%s מהם שמישים למשתמשים' % js_str(qa))
    if EXTRAS and m.get('access'): meta += ' · %s: %s' % (t('access', 'доступ', 'גישה'), esc(regvocab.access_l(m['access'], L)))
    pid = m['map_path']
    return _wrap('machine', [
        '<h3><i class="sw" style="--c:%s"></i> %s</h3>' % (FAMC.get(fam, 'var(--mid)'), esc(m['name'])),
        '<div class="meta">%s</div>' % meta,
        '<div class="mlinks"><span class="empty">%s:</span> %s <span class="empty">·</span> %s</div>' % (
            t('architecture', 'архитектура', 'ארכיטקטורה'), _arch(base, pid, L) if pid in PATH else esc(pid),
            _maplink(base, 'machine', mid, L)),
        ('<div class="space"><h4>%s</h4>%s</div>' % (t("Register profile — the machine's variant of its architecture", 'Профиль реестра — вариант архитектуры у этой машины (поля реестра — на английском)', 'פרופיל המרשם — הגרסה של המכונה לארכיטקטורה שלה (שדות המרשם באנגלית)'), prof)) if prof else '',
        '<div class="space"><h4>%s</h4><table class="ptab mtab">%s</table></div>' % (t("Technologies by layer — the machine's cell per layer", 'Технологии по слоям — ячейка машины на каждом слое', 'טכנולוגיות לפי שכבה — התא של המכונה בכל שכבה'), rows),
        _records(L, m['records'], True) if EXTRAS and m.get('records') else '',
        '<div class="mfoot"><span>%s: ✅ %s / %s</span></div>' % (t('evidence', 'источники', 'ראיות'), js_str(ec.get('verified', 0)), js_str(ec.get('total', 0)))])


# ---------- the architecture card (inspectPath)
def architecture_card_html(pid, lang, base=''):
    L, p = lang, PATH[pid]; t = lambda *x: esc(T(L, *x)); sl = p.get('slots') or {}
    members = list(dict.fromkeys(i for k in _okeys(sl) for i in sl[k])); mset = set(members)
    rows = ''.join('<tr><td class="ln">%s %s</td><td>%s</td></tr>' % (l['n'], esc(pick(L, l)), '<span class="empty"> · </span>'.join(
        _st(base, i, L, 'alt' if j else 'prim') for j, i in enumerate(sl.get(str(l['n'])) or [])) or (('<span class="empty">— %s</span>' % esc(T(L, *p['na'][str(l['n'])]))) if str(l['n']) in (p.get('na') or {}) else '<span class="empty">∅ %s</span>' % t('empty slot', 'пустой слот', 'משבצת ריקה')))
        for l in G['layers'])
    R = p.get('round') or {}; RP = R.get('parts') or {}; RX = p.get('react') or {}; CO = p.get('coh') or {}; pn = dict(PN)
    fS = lambda x: '—' if x is None else ('0' if x == 0 else fmt_t(js_log10(x)))
    fE = lambda x: '—' if x is None else to_exponential(x, 1).replace('e+', 'e', 1).replace('e-', 'e−', 1)
    rel = [e for e in G['edges'] if e['src'] in mset and e['dst'] in mset and e['type'] in ('requires', 'replaces', 'conflicts')]
    nm = lambda i: _st(base, i, L, title=pick(L, NODE[i]), text=esc(pick(L, SHORT[i]) if i in SHORT else pick(L, NODE[i])))
    def rel_rows(typ, head, glyph):
        xs = [e for e in rel if e['type'] == typ]
        if not xs: return ''
        return '<div><span class="tk">%s %s · %d</span></div>' % (glyph, head, len(xs)) + ''.join(
            '<div class="rel requires">%s <span class="empty">%s</span> %s%s</div>' % (
                nm(e['dst']), t('is the usual route for', 'обычно служит технологии', 'היא הדרך המקובלת עבור') if e.get('strength') == 'soft' else t('is needed by', 'требуется технологии', 'נחוצה עבור'), nm(e['src']),
                (' <span class="empty">(%s)</span>' % t('or an alternative', 'или альтернатива', 'או חלופה')) if e.get('any') else '') if typ == 'requires' else
            '<div class="rel %s">%s <span class="empty">%s</span> %s%s</div>' % (
                ea(e['type']), nm(e['src']), t('alternative to', 'альтернатива для', 'חלופה עבור') if typ == 'replaces' else t('conflicts with', 'конфликтует с', 'מתנגשת עם'), nm(e['dst']),
                (' <span class="empty">· %s</span>' % esc(vt(L, 'CONSTAT', e['status']))) if typ == 'conflicts' and e.get('status') else '') for e in xs)
    rel_html = (rel_rows('requires', t('dependencies', 'зависимости', 'תלויות'), '→') + rel_rows('conflicts', t('conflicts', 'конфликты', 'התנגשויות'), '✕') +
                rel_rows('replaces', t('alternatives', 'альтернативы', 'חלופות'), '⇄')) if rel else '<div class="empty">%s</div>' % t('no recorded relations among these technologies', 'между этими технологиями связей не записано', 'לא נרשמו קשרים בין הטכנולוגיות האלה')
    lim = R.get('limiter')
    clocks = ('<dt>%s</dt><dd><b>%s</b>%s</dd>' % (t('syndrome round', 'раунд синдрома', 'סבב סינדרום'), fS(R.get('total')), (' · %s: %s · %s %s%s' % (
        t('limiter', 'ограничитель', 'גורם מגביל'), esc(T(L, *pn.get(lim, (_s(lim), _s(lim))))), t('round of', 'раунд кода', 'סבב של הקוד'), esc(R.get('code') or ''),
        (' (d₂ = %s%s)' % (js_str(R['d2']), (', d₁ = ' + js_str(R['d1'])) if R.get('d1') else '')) if R.get('d2') else '')) if R.get('total') else '') +
        (('<dt>%s</dt><dd>%s</dd>' % (t('parts', 'части', 'חלקים'), ' · '.join('%s %s' % (esc(T(L, *v)), fS(RP.get(k))) for k, v in PN))) if R.get('total') else '') +
        '<dt>%s</dt><dd>%s</dd>' % (t('measured cycle', 'измеренный цикл', 'מחזור נמדד'), esc(p.get('cycle') or '—')) +
        '<dt>%s</dt><dd>%s%s %s %s</dd>' % (t('reaction time', 'время реакции', 'זמן תגובה'), ('<b>%s</b> %s · ' % (fS(RX['loop']), t('(published loop)', '(опубликованный контур)', '(לולאה שפורסמה)'))) if RX.get('loop') is not None else '',
                                           t('floor', 'нижняя граница', 'חסם תחתון'), fS(RX.get('floor')),
                                           ('<span class="empty">· %s</span>' % t('no published measurement→operation loop', 'нет опубликованного контура измерение→операция', 'לא פורסמה לולאת מדידה→פעולה')) if RX.get('loop') is None else '') +
        '<dt>%s</dt><dd>T1 %s · T2 %s%s · %s <b>%s</b></dd>' % (t('coherence', 'когерентность', 'קוהרנטיות'), fS(CO.get('t1')), fS(CO.get('t2')),
                                                             (' (%s)' % esc(CO['t2_scope'])) if CO.get('t2_scope') and CO['t2_scope'] != 'typical' else '',
                                                             t('ops per coherence', 'операций на когерентность', 'פעולות לזמן קוהרנטיות'), fE(CO.get('ops_per_coh'))) +
        '<dt>%s</dt><dd>t_round/T2 = %s · %s %s</dd>' % (t('idle exposure per round', 'экспозиция простоя за раунд', 'חשיפת סרק לסבב'), fE(CO.get('idle_exposure')),
                                                        t('measured idle error', 'измеренная ошибка простоя', 'שגיאת סרק נמדדת'), fE(CO.get('idle_measured'))) +
        (('<dt>%s</dt><dd class="empty">%s</dd>' % (t('notes', 'примечания', 'הערות'), esc('; '.join(R['notes'])))) if R.get('notes') else ''))
    rd = lambda ids: ', '.join(_st(base, i, L) for i in ids) or '—'
    ms = ''
    if EXTRAS:
        mids = [i for i, m in MACH.items() if m.get('map_path') == pid]
        ms = '<div class="space useby"><h4>%s · %d</h4>%s</div>' % (t('Machines of this architecture', 'Машины этой архитектуры', 'מכונות בארכיטקטורה זו'), len(mids), (
            '<ul class="useby">%s</ul><div class="empty" style="margin-top:4px">%s</div>' % (''.join(_mli(L, i, base, '') for i in mids), t(*USEBY_HINT))) if mids else '')
    return _wrap('architecture', [
        '<h3><i class="sw" style="--c:%s"></i> %s</h3>' % (FAMC.get(p['family']), esc(pick(L, p))),
        '<div class="meta">%s · %s · %s</div>' % (t('architecture', 'архитектура', 'ארכיטקטורה'), esc(pid), T(L, '10 layers · %d technologies counting alternates' % len(members), '10 слоёв · %d %s с учётом альтернатив' % (len(members), regvocab.ru_plural(len(members), regvocab.PLURAL['stations'])),
                                                                         '10 שכבות · %s כולל החלופיות' % regvocab.he_count(len(members), regvocab.PLURAL_HE['stations']))),
        '<div class="mlinks">%s</div>' % _maplink(base, 'architecture', pid, L),
        '<div class="space"><h4>%s</h4><div>%s</div><div class="empty">%s: %s</div></div>' % (t(*ACTORS_GOALS), esc(p.get('actors')), t('goals', 'цели', 'יעדים'), esc(p.get('goals'))),
        '<div class="space"><h4>%s</h4><dl>%s</dl><div class="empty" style="margin-top:4px">%s</div></div>' % (t('Derived clocks', 'Выведенные такты', 'שעונים נגזרים'), clocks, t(
            "t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset — a sum of the round's phases, from the code node, the attributes and the standard records; the measured cycle is the check.",
            't_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset — сумма фаз раунда из узла кода, атрибутов и стандартных рекордов; измеренный цикл — проверка.',
            't_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset — סכום שלבי הסבב, מצומת הקוד, מהתכונות ומהרשומות הסטנדרטיות; המחזור הנמדד הוא הבדיקה.')),
        '<div class="space"><h4>%s</h4><table class="ptab">%s</table></div>' % (t('Technologies by layer — primary, then alternates', 'Технологии по слоям — основная, затем альтернативы', 'טכנולוגיות לפי שכבה — הראשית, ואחריה החלופיות'), rows),
        '<div class="space"><h4>%s</h4>%s</div>' % (t('Relations within the architecture', 'Связи внутри архитектуры', 'קשרים בתוך הארכיטקטורה'), rel_html),
        '<div class="space"><h4>%s</h4><div>%s: %s</div><div>∅ %s: %s</div></div>' % (
            t('Reading', 'Чтение', 'סימוני המפה'), t('hatched (crossing)', 'штрихованные (сквозные)', 'מקווקוות (חוצות)'),
            rd([i for i in members if NODE[i].get('offdiag')]), t('empty slots', 'пустые слоты', 'משבצות ריקות'), rd([i for i in members if NODE[i].get('status') == 'X'])),
        ms])


if __name__ == '__main__':
    load()
    for fn, i, title in ((station_card_html, 'ion', NODE['ion']), (machine_card_html, 'google-willow', {'en': MACH['google-willow']['name']}),
                         (architecture_card_html, 'sc', PATH['sc'])):
        for lang in LANGS:
            h = fn(i, lang, '../')
            assert re.search(r'<h3>(?:<i class="sw"[^>]*></i> )?%s</h3>' % re.escape(esc(pick(lang, title))), h), (fn.__name__, i, lang)
            assert '<script' not in h and 'href="#"' not in h and 'data-goto' not in h
            print('%-24s %-14s %s %7d bytes' % (fn.__name__, i, lang, len(h.encode('utf-8'))))
