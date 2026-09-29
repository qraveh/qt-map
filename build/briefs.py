# -*- coding: utf-8 -*-
"""Technology briefs: parsing, ordering and HTML rendering.

Shared by build_html.py (page integration) and briefs_bundle.py (MD bundles).
Nothing here reads the report markdown or the D3 bundle, so it is safe to import.
"""
import os, re, json, html, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langs import LANGS, pick, has, fb_attrs, direction   # the languages (29 Sep 2026: en, ru, he); a missing translation reads English
BDIR = os.path.join(ROOT, 'briefs')
DIRS = {L: os.path.join(BDIR, L) for L in LANGS}   # briefs/<lang>/<id>.md
EN_DIR = DIRS['en']; RU_DIR = DIRS['ru']           # the old names, kept for callers that set them
MODE = 'internal'          # 'internal' | 'public'
REGMAP = {}                # public mode: registry key → {text,date,url} for linked [G:KEY] chips
TABLE_NUM = '8.2'          # section number of the node table (7.2 in the public edition)
ID_SECTIONS = ('8.2', '8.5', '8.6', '8.7')


def configure(mode='internal', en_dir=None, ru_dir=None, regmap=None, table_num=None, id_sections=None, dirs=None):
    global MODE, EN_DIR, RU_DIR, REGMAP, TABLE_NUM, ID_SECTIONS
    MODE = mode
    if dirs: DIRS.update(dirs)
    if en_dir: DIRS['en'] = en_dir
    if ru_dir: DIRS['ru'] = ru_dir
    EN_DIR, RU_DIR = DIRS['en'], DIRS['ru']
    if regmap is not None: REGMAP = regmap
    if table_num: TABLE_NUM = table_num
    if id_sections: ID_SECTIONS = tuple(id_sections)
    if mode == 'public':
        TAGS['G'] = ('established / general fact — a linked chip opens the dated primary source', 'установленный / общий факт — чип-ссылка открывает датированный первоисточник')
        for k, v in NAV.items():
            v['row'] = v['row'].replace('8.2', TABLE_NUM)

RANKING = json.load(open(os.path.join(ROOT, 'data', 'ranking.json'), encoding='utf-8'))

FM_ORDER = ('id', 'name', 'layer', 'tier', 'status', 'since', 'one_line', 'verdict', 'updated')

# ---------- status / layer vocabulary (mirrors graph.json vocab)
STATUS = {
    'demonstrated': ('demonstrated', 'продемонстрировано'),
    'emerging': ('emerging', 'формируется'),
    'theory': ('theory / design only', 'только теория / дизайн'),
    'theory / design only': ('theory / design only', 'только теория / дизайн'),
    'empty slot': ('empty slot — no technology yet', 'пустой слот — технологии ещё нет'),
    'empty slot — no technology yet': ('empty slot — no technology yet', 'пустой слот — технологии ещё нет'),
}
LAYER_RU = {1: 'Носитель', 2: 'Кодирование', 3: 'Механизм гейта', 4: 'Связность / транспорт',
            5: 'Управление', 6: 'Считывание', 7: 'Код', 8: 'Декодер', 9: 'Интерконнект', 10: 'Производство'}

# ---------- evidence tags
TAGS = {
    'D': ('measured / peer-reviewed', 'измерено / рецензировано'),
    'C': ('company claim', 'заявление компании'),
    'R': ('roadmap / target', 'дорожная карта / цель'),
    'S': ('simulation / estimate', 'симуляция / оценка'),
    'G': ('established / general fact', 'установленный / общий факт'),
    'P': ('preprint / trade press', 'препринт / отраслевая пресса'),
}
REG_TITLE = ('registry key — dated primary source in the verification registry',
             'ключ реестра — датированный первичный источник в реестре верификации')

# ---------- folded body sections
# the brief's section skeleton in each language (the nine body sections, then References and Open verification items); the Hebrew
# names are the binding terms of data/i18n/he-terms.md (29 Sep 2026)
SKELETON = {
    'en': ('Identity & lineage', 'Physics & limits', 'Engineering state of the art', 'Manufacturing, materials & supply chain',
           'Control, readout & I/O burden', 'Role in the stack', 'Evidence — how the numbers were measured', 'Actors & economics',
           'Outlook & open questions', 'References', 'Open verification items'),
    'ru': ('Идентичность и происхождение', 'Физика и пределы', 'Инженерное состояние (state of the art)', 'Производство, материалы и цепочка поставок',
           'Управление, считывание и нагрузка на ввод-вывод', 'Роль в стеке', 'Свидетельства — как измерены числа', 'Акторы и экономика',
           'Прогноз и открытые вопросы', 'Литература', 'Открытые пункты верификации'),
    'he': ('זהות ומוצא', 'פיזיקה וגבולות', 'מצב ההנדסה העדכני', 'ייצור, חומרים ושרשרת האספקה', 'בקרה, קריאה ועומס הקלט-פלט',
           'תפקיד במחסנית', 'ראיות — כיצד נמדדו המספרים', 'שחקנים וכלכלה', 'תחזית ושאלות פתוחות', 'מקורות', 'פריטי אימות פתוחים'),
}
SK_REFS, SK_OVI = 9, 10
# the folded body sections: References (the brief's Sources list) and Open verification items, under their name in any language
FOLD_HEADS = {}
for _L, _sk in SKELETON.items():
    FOLD_HEADS[_sk[SK_REFS]] = (_sk[SK_REFS], 'src'); FOLD_HEADS[_sk[SK_OVI]] = (_sk[SK_OVI], 'ovi')

# a language whose brief is not written yet shows the English brief under this note (29 Sep 2026: one note per language)
FALLBACK_NOTE = {'ru': '*Перевод готовится — ниже английский текст брифа.*',
                 'he': '*התרגום בהכנה — להלן נוסח התקציר באנגלית.*'}
RU_FALLBACK_NOTE = FALLBACK_NOTE['ru']

# ---------- preface (deliverable 2c; reused verbatim by the MD bundles)
PREFACE_PUBLIC = {
    'en': [
        'Every technology on the map has a brief, and the depth of each one follows the technology\'s '
        'centrality in the graph — how many platform families and architectures depend on it and how recently it '
        'reached hardware — so a node a dozen architectures run through gets about 2,000 words and a single-platform '
        'node about 800. Centrality is a statement about the graph, not a verdict on the technology; it is '
        'shown in each brief\'s header and in the index below.',
    ],
    'ru': [
        'У каждой технологии на карте есть бриф, а его глубина следует центральности технологии в графе — '
        'сколько семейств платформ и архитектур от неё зависят и насколько недавно она дошла до железа, — так что '
        'узел, через который идёт дюжина архитектур, получает около 2 000 слов, а узел одной платформы — около 800. '
        'Центральность — утверждение о графе, а не вердикт о технологии; она показана в шапке каждого брифа '
        'и в индексе ниже.',
    ],
}
PREFACE = {
    'en': [
        'Every technology on the map has a brief, and the depth of each one follows an importance score '
        'derived from the graph itself — how far a node reaches across platform families, how '
        'many architectures run through it, and how recent it is. Tier 1 is the 27 most important '
        'technologies at roughly 1,600–2,400 words; Tier 2 is 33 technologies at roughly 1,300 words; '
        'Tier 3 is 50 technologies at roughly 800–1,100 words. The tier is a statement about the graph, not a '
        'judgement of the technology.',
        'Every brief carries the same section skeleton — identity and lineage, physics and limits, '
        'engineering state of the art, manufacturing and supply chain, role in the stack, actors and '
        'economics, outlook and open questions, sources, and open verification items — so any two briefs '
        'can be read against each other. The Actors & economics section is verified against dated '
        'primary sources. Evidence tags mark the standing of every claim: '
        '[D] measured or peer-reviewed, [C] company claim, [R] roadmap or target, [S] simulation or '
        'estimate, [G] established or general fact (where the chip is a link it opens the dated primary source), '
        '[P] preprint or trade press.',
    ],
    'ru': [
        'У каждой технологии на карте есть бриф, а его глубина определяется оценкой важности, выведенной '
        'из самого графа: насколько узел дотягивается до разных семейств платформ, сколько '
        'архитектур через него проходит и насколько он свеж. Tier 1 — 27 самых важных технологий, '
        'примерно 1 600–2 400 слов; Tier 2 — 33 технологии, примерно 1 300 слов; Tier 3 — 50 технологий, '
        'примерно 800 слов. Tier — утверждение о графе, а не оценка технологии.',
        'Все брифы построены по одному скелету разделов — идентичность и происхождение, физика и пределы, '
        'инженерное состояние, производство и цепочка поставок, роль в стеке, акторы и экономика, прогноз '
        'и открытые вопросы, источники, открытые пункты верификации, — поэтому любые два брифа читаются '
        'друг против друга. Раздел «Акторы и экономика» верифицирован по датированным первичным '
        'источникам. Теги свидетельств показывают статус каждого утверждения: '
        '[D] измерено или рецензировано, [C] заявление компании, [R] дорожная карта или цель, '
        '[S] симуляция или оценка, [G] установленный или общий факт (чип-ссылка открывает датированный первоисточник), '
        '[P] препринт или отраслевая пресса.',
    ],
}
REFNOTE = {'en': 'Numbers are the Atlas’s: a work has the same number here, in §9 and in every other brief; online sources were accessed in September 2026.',
           'ru': 'Номера общие для всего Атласа: у работы один и тот же номер здесь, в §9 и в любом другом брифе; онлайн-источники просмотрены в сентябре 2026 г.'}
SECTION_TITLE = {'en': 'Technology briefs', 'ru': 'Брифы по технологиям', 'he': 'תקצירי הטכנולוגיות'}


# ---------- front matter
def _unq(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1]
    return v


def parse_brief(path):
    t = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    meta, body = {}, t
    if m:
        for line in m.group(1).split('\n'):
            if ': ' in line:
                k, v = line.split(': ', 1)
                meta[k.strip()] = _unq(v)
        body = t[m.end():]
    return meta, body.strip('\n')


def layer_num(meta):
    m = re.match(r'\s*(\d+)', meta.get('layer', ''))
    return int(m.group(1)) if m else 0


def status_label(meta, lang):
    s = meta.get('status', '').strip()
    return pick(lang, STATUS.get(s, (s, s)))


def _meta_from_en(en_meta, L):
    """Front matter for a brief of language L whose file does not exist yet (the layer's name in L when the graph has it)."""
    m = dict(en_meta)
    n = layer_num(en_meta)
    if n:
        m['layer'] = '%d %s' % (n, _LAYER_NAME.get(L, {}).get(n) or (LAYER_RU.get(n, '') if L == 'ru' else _LAYER_NAME['en'].get(n, '')))
    return m


_NODES = None
_LAYER_NAME = {L: {} for L in LANGS}
def _load_layers():
    try:
        for l in json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))['layers']:
            for L in LANGS: _LAYER_NAME[L][l['n']] = pick(L, l)
    except (OSError, ValueError, KeyError): pass
_load_layers()
def _node(bid):
    """the graph's record of a technology (data/graph.json, written by make_sections before the briefs are rendered)"""
    global _NODES
    if _NODES is None:
        try: _NODES = {n['id']: n for n in json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))['nodes']}
        except (OSError, ValueError): _NODES = {}
    return _NODES.get(bid)


def load_briefs():
    """All briefs (one per node of data/ranking.json) ordered by rank, each in every language of langs.LANGS: a language whose file is
    missing shows the English body under its FALLBACK_NOTE (b['fallback'][lang] is then True)."""
    out = []
    for bid, r in sorted(RANKING.items(), key=lambda kv: kv[1]['rank']):
        if not os.path.exists(os.path.join(DIRS['en'], bid + '.md')):
            sys.stderr.write('briefs: no English brief for %s yet — skipped\n' % bid); continue   # release_check counts briefs against nodes
        en_meta, en_body = parse_brief(os.path.join(DIRS['en'], bid + '.md'))
        rec = {'id': bid, 'rank': r['rank'], 'tier': r['tier'], 'score': r['score'], 'layer': layer_num(en_meta),
               'fallback': {'en': False}, 'en': {'meta': en_meta, 'body': en_body}}
        for L in LANGS[1:]:
            path = os.path.join(DIRS.get(L) or os.path.join(BDIR, L), bid + '.md')
            if os.path.exists(path):
                m, body = parse_brief(path); rec['fallback'][L] = False
            else:
                m, body = _meta_from_en(en_meta, L), pick(L, FALLBACK_NOTE) + '\n\n' + en_body; rec['fallback'][L] = True
            rec[L] = {'meta': m, 'body': body}
        rec['ru_fallback'] = rec['fallback'].get('ru', False)   # the old key
        # one name per technology: the brief's title and its "since" are the graph's (the front matter keeps the author's wording
        # for the record; build/audit/briefs_meta_check.py lists the divergences — 97 of 222 names differed on 27 Sep 2026)
        node = _node(bid)
        if node:
            for lang in LANGS:
                meta = rec[lang]['meta']
                meta['brief_name'] = meta.get('name', ''); meta['name'] = pick(lang, node)
                meta['since'] = str(node['since']) if node.get('since') is not None and node['since'] < 2030 else ''
                meta['layer'] = '%d %s' % (node['layer'], _LAYER_NAME[lang].get(node['layer'], ''))   # the layer's name is the graph's too (layer 1 "Qubit carrier", 28 Sep 2026)
        out.append(rec)
    if MODE == 'public':
        out.sort(key=lambda b: (b['layer'], -b['score'], b['id']))
    return out


# ---------- family colours (same rule as map_js.py: first architecture a node belongs to)
FAMVAR = {'SC': 'var(--sc)', 'ION': 'var(--ion)', 'ATOM': 'var(--atom)', 'PHOTON': 'var(--photon)',
          'SPIN': 'var(--spin)', 'DEFECT': 'var(--defect)', 'TOPO': 'var(--topo)', 'ANNEAL': 'var(--anneal)'}


def family_colours(G):
    prim, alt = {}, {}
    for p in G['paths']:
        for _L, ids in p['slots'].items():
            for i, nid in enumerate(ids):
                (prim if i == 0 else alt).setdefault(nid, []).append(p['id'])
    byid = {p['id']: p for p in G['paths']}
    col = {}
    for n in G['nodes']:
        ps = prim.get(n['id'], []) + alt.get(n['id'], [])
        col[n['id']] = FAMVAR.get(byid[ps[0]]['family'], 'var(--mid)') if ps else 'var(--mid)'
    return col


# ---------- tag chips
_TAG_RE = re.compile(r'\[(D|C|R|S|G|P)\](?![\(\w])')
_REG_RE = re.compile(r'\[REG:([A-Za-z0-9._\-]+)\]')
_GKEY_RE = re.compile(r'\[G:([A-Za-z0-9._\-]+)\]')


GTIPS = {}   # [G:CODE] chip tooltips, one per code (window.__GTIPS): brief_js sets the title at load — the same 200-byte tip
             # would otherwise stand once per chip, in both languages (0.3 MB over the briefs)


def gkey_tip(code):
    r = REGMAP.get(code)
    return '%s · %s' % (r['text'][:220], r['date']) if r and r.get('url') else None


FACT_CHIP = ('fact', 'факт')   # a [G:KEY] chip links a dated entry of the shared fact ledger (data/facts.json); until 27 Sep 2026 it was drawn as
                                # the [G] "established fact" grade, which 548 of 816 ledger links to company pages and trade press did not deserve


def _gkey_chip(m, lang='en'):
    r = REGMAP.get(m.group(1))
    lab = pick(lang, FACT_CHIP)
    if r and r.get('url'):
        GTIPS[m.group(1)] = gkey_tip(m.group(1))
        return '<a class="tag tag-fact tag-link" href="%s" target="_blank" rel="noopener" data-g="%s">%s</a>' % (html.escape(r['url']), html.escape(m.group(1)), lab)
    return '<span class="tag tag-fact" title="%s">%s</span>' % (html.escape(pick(lang, TAGS['G'])), lab)


def expand_gtips(h, gtips=None):
    """the page as the browser shows it: the [G] chips' tooltips set from window.__GTIPS (for the static checkers)"""
    T = gtips if gtips is not None else GTIPS
    return re.sub(r'(<a class="tag tag-fact tag-link" href="[^"]*" target="_blank" rel="noopener") data-g="([^"]+)">([^<]*)</a>',
                  lambda m: '%s title="%s">%s</a>' % (m.group(1), html.escape(T.get(html.unescape(m.group(2))) or ''), m.group(3)), h)


def expand_ulinks(h):
    """self-labelled links carry no href in the file (sources._link): the page sets href = text at load; the checkers see the same"""
    return re.sub(r'<a class="u"( target="_blank" rel="noopener")>((?:[^<]|<wbr>)+)</a>', lambda m: '<a href="%s" class="u"%s>%s</a>' % (m.group(2).replace('<wbr>', ''), m.group(1), m.group(2)), h)


def expand_langs(h, page_path=None):
    """One page per language (27 Sep 2026): the other languages' prose and brief halves are placeholders (data-lang-slot) that
    the page fills at load from dist/lang/<lang>.js. The static checkers see the whole document: the fragments are read from
    beside the page (or from dist/lang when no path is given) and put into their slots the way the browser does."""
    import json as _json
    slots = re.findall(r'<div class="(?:prose|bl) lang-(\w+)"[^>]*data-lang-slot="([^"]+)"><p class="langwait">[^<]*</p></div>', h)
    if not slots: return h
    base = os.path.join(ROOT, 'dist', 'lang')
    if page_path:
        d = os.path.dirname(os.path.abspath(page_path))
        for cand in (os.path.join(d, 'lang'), os.path.join(os.path.dirname(d), 'lang')):
            if os.path.isdir(cand): base = cand; break
    frags = {}
    for lang in sorted({l for l, _ in slots}):
        fp = os.path.join(base, lang + '.js')
        if not os.path.exists(fp): continue
        t = open(fp, encoding='utf-8').read()
        i = t.index('=', t.index('window.__LANGFRAG[')); frags[lang] = _json.loads(t[i + 1:].rstrip().rstrip(';'))
    def sub(m):
        lang, key = m.group(1), m.group(2)
        F = frags.get(lang, {})
        return F.get(key[len(lang) + 1:], m.group(0))
    return re.sub(r'<div class="(?:prose|bl) lang-(\w+)"[^>]*data-lang-slot="([^"]+)"><p class="langwait">[^<]*</p></div>', sub, h)


# ---------- the Sources lists of the other languages (29 Sep 2026): a brief's list is the same works in the same numbers in every language
# (a bibliography is not translated), so a non-English half carries a placeholder cloned from the English list at load (brief_js), its
# ids and §-links switched to that language — the same entries would otherwise stand once per language in the file
_CLONE = re.compile(r'<ol class="refs" data-nohint="1" data-clone="([^"]+)"(?: data-clone-lang="(\w+)")?></ol>')


def clone_list(bid, lang):
    return '<ol class="refs" data-nohint="1" data-clone="brief-%s-en-refs" data-clone-lang="%s"></ol>' % (bid, lang)


def expand_clones(h):
    """the page as the browser shows it: every placeholder list filled from the English list (a placeholder without its language —
    the form of brief_refs.list_html — is Russian)"""
    lists = {m.group(1): m.group(2) for m in re.finditer(r'<ol class="refs" data-nohint="1" id="([^"]+)">(.*?)</ol>', h, flags=re.S)}
    def sub(m):
        src = lists.get(m.group(1)); L = m.group(2) or 'ru'
        if src is None: return m.group(0)
        return '<ol class="refs" data-nohint="1">' + src.replace('-en-src-', '-%s-src-' % L).replace('href="#en-s', 'href="#%s-s' % L) + '</ol>'
    return _CLONE.sub(sub, h)


def expand_page(h, page_path=None):
    """every load-time expansion the static checkers must see: the other language's blocks, RU Sources lists, key-reference
    chips, [G] chip tooltips"""
    import brief_refs, json as _json
    h = expand_langs(h, page_path)
    h = expand_clones(h)
    h = expand_ulinks(h)
    k = h.find('window.__KEYREFS='); k2 = h.find('</script>', k)
    if k > 0: h = expand_keys(h, fill_key_labels(h, _json.loads(h[k + len('window.__KEYREFS='):k2].rstrip(';'))))
    g = h.find('window.__GTIPS='); g2 = h.find('</script>', g)
    if g > 0: h = expand_gtips(h, _json.loads(h[g + len('window.__GTIPS='):g2].rstrip(';')))
    return h


def chip_tags(h, lang):
    """Turn [D]/[C]/… and [REG:KEY] into chips, skipping anything inside an HTML tag."""
    reg_title = pick(lang, REG_TITLE)
    out = []
    for part in re.split(r'(<[^>]*>)', h):
        if part.startswith('<'):
            out.append(part)
            continue
        part = _REG_RE.sub(
            lambda m: '<span class="tag tag-reg" title="%s">REG:%s</span>' % (html.escape(reg_title), m.group(1)),
            part)
        part = _GKEY_RE.sub(lambda m: _gkey_chip(m, lang), part)
        part = _TAG_RE.sub(lambda m: '<span class="tag tag-%s">%s</span>' % (m.group(1), m.group(1)), part)   # the title comes on hover (TAG_JS): 10,000 chips, one table
        out.append(part)
    return ''.join(out)


# ---------- body → HTML
_H2_SPLIT = re.compile(r'<h2>(.*?)</h2>', re.S)


_BARE_URL = re.compile(r'(?<!["\'=>/])(https?://[^\s<>"\']+?)(?=[\s<]|[.,;:)\]]*(?:\s|<|$))')
_SRC_START = re.compile(r'(^|<p>|<br />\s*|<li>)\s*\[(\d+)\]', re.M)
_CITE = re.compile(r'\[(\d+)\]')


def autolink(h):
    """Wrap bare URLs (outside tags and existing anchors) in <a>."""
    out = []
    for part in re.split(r'(<a\b[^>]*>.*?</a>|<[^>]*>)', h, flags=re.S):
        if part.startswith('<'):
            out.append(part); continue
        out.append(_BARE_URL.sub(lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(1), m.group(1)), part))
    return ''.join(out)


def _anchor_sources(content, bid, lang):
    """Give every source entry an id so in-text citations can jump to it."""
    pre = 'brief-%s-%s-src-' % (bid, lang)
    # "[n] …" entries (paragraph / <br /> separated)
    content = _SRC_START.sub(lambda m: '%s<span class="srcn" id="%s%s">[%s]</span>' % (m.group(1), pre, m.group(2), m.group(2)), content)
    # "1. …" entries rendered as <ol><li>
    if '<ol>' in content and 'class="srcn"' not in content:
        k = [0]
        def li(m):
            k[0] += 1
            return '<li id="%s%d"><span class="srcn">[%d]</span> ' % (pre, k[0], k[0])
        content = re.sub(r'<li>', li, content)
    return content


def _ref_list(body, bid, lang, md2html, content):
    """The Sources fold: the brief's IEEE list (build/brief_refs.py, the §9 form), then the section's lines that are not entries
    (research notes such as "[G] …") as they are; a brief without a list in the data file keeps its markdown list."""
    import brief_refs
    lst = brief_refs.list_html(bid, 'en')
    if lst is None: return _anchor_sources(content, bid, lang)
    if lang != 'en': lst = clone_list(bid, lang)
    txt = _section_any(body, SK_REFS)
    ents, extra, _ = brief_refs.entries(txt.split('\n'))
    return lst + (md2html('\n'.join(extra)) if extra else '')


def _link_cites(h, bid, lang):
    """[n] in the body → link to the source entry; skips tags and the sources fold itself."""
    pre = 'brief-%s-%s-src-' % (bid, lang)
    out = []
    for part in re.split(r'(<[^>]*>)', h):
        if part.startswith('<'):
            out.append(part); continue
        out.append(_CITE.sub(lambda m: '<a class="cite" href="#%s%s">[%s]</a>' % (pre, m.group(1), m.group(1)), part))
    return ''.join(out)


TOOLTIPS = None   # build_html.tooltips, injected at build time
FOLD = None       # build_html.foldable (sections and tables fold), injected at build time


_PATENT_RE = re.compile(r'\b(US|EP|WO|CN|JP|KR)\s?\d{1,2}(?:,\d{3}){2}\b')


def ru_numbers(text):
    """Russian number style for a brief body (27 Sep 2026): the English thousands comma becomes a no-break space (1,121 → 1 121;
    387 places), except in code parameters [[144,12,12]] and patent numbers (US 11,748,652 B1), which keep their commas. Decimal
    points are left alone: a global point→comma rule would also hit DOIs, arXiv ids, versions and URLs."""
    keep = []
    def hold(m): keep.append(m.group(0)); return '\x00%d\x00' % (len(keep) - 1)
    t = _PATENT_RE.sub(hold, text)
    t = re.sub(r'\[\[[^\]]*\]\]', hold, t)
    t = re.sub(r'(?<=\d),(?=\d{3}\b)', '\u00a0', t)
    return re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], t)


def body_html(body, lang, md2html, bid=''):
    if lang == 'ru': body = ru_numbers(body)
    h = md2html(body)
    h = h.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    parts = _H2_SPLIT.split(h)
    out = [_link_cites(parts[0], bid, lang) if bid else parts[0]]
    for k in range(1, len(parts), 2):
        head_raw = parts[k]
        content = parts[k + 1] if k + 1 < len(parts) else ''
        plain = re.sub('<[^>]+>', '', head_raw).strip()
        if plain in FOLD_HEADS:
            kind = FOLD_HEADS[plain][1]
            if kind == 'src' and bid:
                content = _ref_list(body, bid, lang, md2html, content)
            elif bid:
                content = _link_cites(content, bid, lang)
            out.append('<details class="fold bfold fold-%s"><summary>%s</summary><div class="bfoldin">%s</div></details>'
                       % (kind, head_raw, content))
        else:
            out.append('<h3 class="bh3">%s</h3>%s' % (head_raw, _link_cites(content, bid, lang) if bid else content))
    h = chip_tags(autolink(''.join(out)), lang)
    h = TOOLTIPS(h, lang) if TOOLTIPS else h   # the glossary tooltips of build_html (set by the caller), once per term per brief
    return FOLD(h, lang, bid or 'x') if FOLD else h


def inline_html(s, md2html):
    h = md2html(s).strip()
    h = re.sub(r'^<p>', '', h)
    h = re.sub(r'</p>$', '', h)
    return h.replace('</p>\n<p>', ' ')


# ---------- one brief section
NAV = {
    'en': {'map': '← Technology on the map', 'row': '↑ Table 8.2 row', 'prev': '← Previous brief',
           'next': 'Next brief →', 'close': 'Close ✕', 'verdict': 'Verdict',
           'layer': 'layer', 'tier': 'Tier', 'rank': 'rank', 'centrality': 'centrality', 'since': 'since', 'updated': 'updated'},
    'ru': {'map': '← Технология на карте', 'row': '↑ Строка таблицы 8.2', 'prev': '← Предыдущий бриф',
           'next': 'Следующий бриф →', 'close': 'Закрыть ✕', 'verdict': 'Вердикт',
           'layer': 'слой', 'tier': 'Tier', 'rank': 'ранг', 'centrality': 'центральность', 'since': 'с', 'updated': 'обновлено'},
}


def _one_lang(b, lang, md2html, prev_id, next_id, colour):
    m = b[lang]['meta']
    t = pick(lang, NAV)
    fb = b.get('fallback', {}).get(lang, False)   # the English brief in place of the language's own: marked, its note in the language
    name = inline_html(m.get('name', b['id']), md2html)
    one = inline_html(ru_numbers(m.get('one_line', '')) if lang == 'ru' else m.get('one_line', ''), md2html)
    verdict = inline_html(ru_numbers(m.get('verdict', '')) if lang == 'ru' else m.get('verdict', ''), md2html)
    meta_line = ' · '.join(x for x in [
        '<span class="bid">%s</span>' % html.escape(b['id']),
        '%s %s' % (t['layer'], html.escape(m.get('layer', ''))),
        ('%s %s' % (t['tier'], b['tier'])) if MODE != 'public' else '',
        ('%s %d/%d' % (t['rank'], b['rank'], len(RANKING))) if MODE != 'public' else ('%s %s' % (t['centrality'], ('%g' % b['score']))),
        html.escape(status_label(m, lang)),
        ('%s %s' % (t['since'], html.escape(m.get('since', '')))) if m.get('since') else '',
        '%s %s' % (t['updated'], html.escape(m.get('updated', ''))),
    ] if x)
    nav = ('<nav class="bnav">'
           '<button type="button" class="chip" data-mapstation="%s">%s</button>'
           '<button type="button" class="chip" data-tablerow="%s">%s</button>'
           '%s%s'
           '<button type="button" class="chip" data-briefclose="1">%s</button></nav>') % (
        b['id'], t['map'], b['id'], t['row'],
        ('<button type="button" class="chip" data-brief="%s">%s</button>' % (prev_id, t['prev'])) if prev_id else '',
        ('<button type="button" class="chip" data-brief="%s">%s</button>' % (next_id, t['next'])) if next_id else '',
        t['close'])
    body = body_html(b[lang]['body'], lang, md2html, b['id'])
    if fb and lang in FALLBACK_NOTE: body = body.replace('<p><em>', '<p lang="%s" dir="%s"><em>' % (lang, direction(lang)), 1)
    return ('<div class="bl lang-%s"%s>'
            '<div class="brief-head" style="--fam:%s">'
            '<button type="button" class="chip bclose" data-briefclose="1">%s</button>'
            '<div class="bmeta">%s</div><h2 class="btitle">%s</h2>'
            '<p class="bone">%s</p>'
            '<p class="bverdict"><b>%s.</b> %s</p>%s</div>'
            '<div class="bbody">%s</div>%s</div>') % (
        lang, fb_attrs(lang, fb), colour, t['close'], meta_line, name, one, t['verdict'], verdict,
        key_refs_html(key_refs(b['en']['body'], bid=b['id']), lang, b['id']),
        body, nav)


def brief_section(b, md2html, prev_id, next_id, colour):
    return '<section class="brief" id="brief-%s" hidden>%s</section>' % (
        b['id'], ''.join(_one_lang(b, L, md2html, prev_id, next_id, colour) for L in LANGS))


# ---------- index table
IDX_HEAD = {'en': ('rank', 'id', 'technology', 'layer', 'tier', 'one line'),
            'ru': ('ранг', 'id', 'технология', 'слой', 'tier', 'одной строкой')}
IDX_HEAD_PUBLIC = {'en': ('layer', 'id', 'technology', 'centrality', 'one line'),
                   'ru': ('слой', 'id', 'технология', 'центральность', 'одной строкой')}


def index_table(briefs, lang, md2html):
    if MODE == 'public':
        th = ''.join('<th>%s</th>' % h for h in pick(lang, IDX_HEAD_PUBLIC))
        rows = []
        for b in briefs:
            m = b[lang]['meta']
            rows.append(
                '<tr data-brief="%s" class="brow"><td>%s</td>'
                '<td><a class="bref" href="#brief-%s" data-brief="%s"><code>%s</code></a></td>'
                '<td><b>%s</b></td><td class="r">%g</td><td class="ol"%s>%s</td></tr>' % (
                    b['id'], html.escape(m.get('layer', '')), b['id'], b['id'], b['id'],
                    inline_html(m.get('name', b['id']), md2html), b['score'], fb_attrs(lang, b.get('fallback', {}).get(lang, False)),
                    inline_html(m.get('one_line', ''), md2html)))
        return '<div class="tbl bidx" data-sort="centrality" data-sort-first="desc" data-default="build"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
            th, ''.join(rows))
    th = ''.join('<th>%s</th>' % h for h in pick(lang, IDX_HEAD))
    rows = []
    for b in briefs:
        m = b[lang]['meta']
        rows.append(
            '<tr data-brief="%s" class="brow"><td class="r">%d</td>'
            '<td><a class="bref" href="#brief-%s" data-brief="%s"><code>%s</code></a></td>'
            '<td><b>%s</b></td><td>%s</td><td class="r">%d</td><td class="ol">%s</td></tr>' % (
                b['id'], b['rank'], b['id'], b['id'], b['id'],
                inline_html(m.get('name', b['id']), md2html), html.escape(m.get('layer', '')),
                b['tier'], inline_html(m.get('one_line', ''), md2html)))
    return '<div class="tbl bidx"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        th, ''.join(rows))


def briefs_section_html(briefs, md2html, colours):
    """The whole '§ Technology briefs' block: heading, preface, index, and one hidden section per brief."""
    langs = []
    for lang in LANGS:   # a language without its own preface shows the English one, marked
        paras = (pick(lang, PREFACE_PUBLIC) + pick(lang, PREFACE)[1:]) if MODE == 'public' else pick(lang, PREFACE)
        fa, fr = fb_attrs(lang, not has(lang, PREFACE_PUBLIC if MODE == 'public' else PREFACE)), fb_attrs(lang, not has(lang, REFNOTE))
        pref = ''.join('<p%s>%s</p>' % (fa, chip_tags(html.escape(p, quote=False), lang)) for p in paras) + '<p class="refnote"%s>%s</p>' % (fr, pick(lang, REFNOTE))
        langs.append('<div class="lang-%s"><h2><span class="num">%s</span>%s</h2>'
                     '<div class="blede">%s</div>%s</div>' % (
                         lang, pick(lang, ('BR', 'БР')), pick(lang, SECTION_TITLE),
                         pref, index_table(briefs, lang, md2html)))
    secs = []
    for i, b in enumerate(briefs):
        prev_id = briefs[i - 1]['id'] if i else ''
        next_id = briefs[i + 1]['id'] if i + 1 < len(briefs) else ''
        secs.append(brief_section(b, md2html, prev_id, next_id, colours.get(b['id'], 'var(--mid)')))
    return '<section class="briefs" id="briefs">%s<div class="briefbodies">%s</div></section>' % (
        ''.join(langs), ''.join(secs))


# ---------- entry points in the §8 tables
def _region(h, num):
    m = re.search(r'<h3 id="[^"]*">' + re.escape(num) + r'[\s<]', h)
    if not m:
        return None
    nxt = re.search(r'<h[23][ >]', h[m.end():])
    return m.start(), (m.end() + nxt.start()) if nxt else len(h)


def link_node_ids(h, ids, row_sections=None, sections=None):
    row_sections = row_sections or (TABLE_NUM,)
    sections = sections or ID_SECTIONS
    """Make `<code>node_id</code>` in the §8 tables open the brief; tag 8.2 rows with data-row."""
    for num in sections:
        r = _region(h, num)
        if not r:
            continue
        a, b = r
        seg = h[a:b]
        if num in row_sections:
            def rowrep(m):
                inner = m.group(1)
                f = re.search(r'<code>([a-z0-9_]+)</code>', inner)
                if f and f.group(1) in ids:
                    return '<tr data-row="%s">%s</tr>' % (f.group(1), inner)
                return m.group(0)
            seg = re.sub(r'<tr>(.*?)</tr>', rowrep, seg, flags=re.S)

        def coderep(m):
            i = m.group(1)
            if i not in ids:
                return m.group(0)
            return '<a class="bref" href="#brief-%s" data-brief="%s"><code>%s</code></a>' % (i, i, i)
        seg = re.sub(r'<code>([a-z0-9_]+)</code>', coderep, seg)
        h = h[:a] + seg + h[b:]
    return h


# ---------- key references: the sources cited in "Identity & lineage" and in the records timeline
_SRC_LINE = re.compile(r'^\s*(?:\[(\d+)\]|(\d+)\.)\s+(.*?)\s*$', re.M)
_URL = re.compile(r'https?://\S+')
_CITE = re.compile(r'\[(\d+)\]')


def _section_text(body, heading):
    m = re.search(r'^## ' + re.escape(heading) + r'\s*$(.*?)(?=^## |\Z)', body, re.M | re.S)
    return m.group(1) if m else ''


def _section_any(body, k):
    """the text of skeleton section k (SKELETON's index) under its name in whichever language the body is written"""
    for L in LANGS:
        t = _section_text(body, SKELETON[L][k]) if L in SKELETON else ''
        if t: return t
    return ''


def _sources(body):
    txt = _section_any(body, SK_REFS)
    out = {}
    for m in _SRC_LINE.finditer(txt):
        n = int(m.group(1) or m.group(2)); rest = m.group(3)
        u = _URL.search(rest)
        url = u.group(0).rstrip('.,;)') if u else ''
        flat = re.sub(r'\[([^\]]+)\]\(https?://[^)\s]*\)', r'\1', rest)   # a markdown link in the line (e.g. a linked DOI) reads as its text
        u2 = _URL.search(flat)
        label = flat[:u2.start()].strip() if u2 else flat.strip()
        label = re.sub(r'\s*[—·-]\s*$', '', label)
        label = re.sub(r'\s*\[(?:REG:[^\]]+|[DCRSGP])\]\s*', ' ', label).strip()
        ys = [y for y in re.findall(r'(?<!\d)((?:19|20)\d\d)(?!\d)', label) if int(y) <= 2026]
        year = ys[-1] if ys else None
        short = re.split(r' et al\.?| · |, |\(|"|«|—', label, 1)[0].strip(' .:;')
        if len(short) > 26: short = short[:24].rstrip() + '…'
        out[n] = {'n': n, 'label': label, 'url': url, 'year': year, 'short': short}
    return out


def key_refs(body, limit=5, bid=None):
    """Ordered, de-duplicated source numbers cited in Identity & lineage, then in the records-timeline table; entries from
    the brief's records (build/brief_refs.py) when it has a list there."""
    import brief_refs
    srcs = (brief_refs.key_info(bid) if bid else {}) or _sources(body)
    order = []
    lineage = _section_any(body, 0)
    eng = _section_any(body, 2)
    table = '\n'.join(l for l in eng.split('\n') if l.startswith('|'))
    for chunk in (lineage, table, eng):
        for n in _cite_nums(chunk):
            if n in srcs and n not in order and srcs[n]['url']:
                order.append(n)
            if len(order) >= limit: break
        if len(order) >= limit: break
    return [srcs[n] for n in order]


def _cite_nums(t):
    """cited numbers in order; an IEEE range [a]–[b] stands for a..b"""
    out, prev = [], None
    for m in _CITE.finditer(t):
        n = int(m.group(1))
        if prev is not None and t[prev.end():m.start()] == '–': out += list(range(int(prev.group(1)) + 1, n))
        out.append(n); prev = m
    return out


def key_refs_all(briefs, limit=5):
    return {b['id']: key_refs(b['en']['body'], limit, b['id']) for b in briefs}


def key_refs_html(refs, lang, bid=None):
    """The key-references chips of a brief header. With a brief id the block is a placeholder that brief_js fills at load from
    window.__KEYREFS (the same records the technology cards use) — the chips and their IEEE tooltips would otherwise stand in the
    file twice per brief (0.27 MB over the briefs); the static form is kept for the md bundles and for expand_keys()."""
    if not refs: return ''
    t = pick(lang, ('Key references', 'Ключевые источники'))
    if bid: return '<div class="bkeys" data-keys="%s"><span class="tk">%s</span></div>' % (bid, t)
    return '<div class="bkeys"><span class="tk">%s</span> %s</div>' % (t, key_refs_items(refs))


def key_refs_slim(keyrefs):
    """the page's embedded form (27 Sep 2026): no label — the IEEE text of work n stands in the brief's own Sources list
    (li#brief-<sid>-en-src-<n> span.ref); brief_js and the technology card read it from there (90 KB saved, one text per work)"""
    return {sid: [{k: v for k, v in r.items() if k != 'label'} for r in refs] for sid, refs in keyrefs.items()}


def fill_key_labels(h, keyrefs):
    """the labels the slim form left out, read back from the page's brief Sources lists (for the static checkers)"""
    out = {}
    for sid, refs in keyrefs.items():
        rs = []
        for r in refs:
            r = dict(r)
            if not r.get('label'):
                m = re.search(r'<li id="brief-%s-en-src-%d"[^>]*>.*?<span class="ref">(.*?)</span>' % (re.escape(sid), int(r['n'])), h, flags=re.S)
                r['label'] = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''
            rs.append(r)
        out[sid] = rs
    return out


def key_refs_items(refs):
    return ''.join('<a href="%s" target="_blank" rel="noopener" title="%s">[%d] %s%s</a>' % (
        html.escape(r['url']), html.escape(r['label']), r['n'], html.escape(r.get('short') or ''), (' ' + r['year']) if r['year'] else '') for r in refs)


def expand_keys(h, keyrefs):
    """the page as the browser shows it: the key-reference placeholders filled (for the static checkers)"""
    return re.sub(r'<div class="bkeys" data-keys="([^"]+)"><span class="tk">([^<]*)</span></div>',
                  lambda m: '<div class="bkeys"><span class="tk">%s</span> %s</div>' % (m.group(2), key_refs_items(keyrefs.get(m.group(1), []))), h)
