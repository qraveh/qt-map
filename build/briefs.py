# -*- coding: utf-8 -*-
"""Technology briefs: parsing, ordering and HTML rendering.

Shared by build_html.py (page integration) and briefs_bundle.py (MD bundles).
Nothing here reads the report markdown or the D3 bundle, so it is safe to import.
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BDIR = os.path.join(ROOT, 'briefs')
EN_DIR = os.path.join(BDIR, 'en')
RU_DIR = os.path.join(BDIR, 'ru')
MODE = 'internal'          # 'internal' | 'public'
REGMAP = {}                # public mode: registry key → {text,date,url} for linked [G:KEY] chips
TABLE_NUM = '8.2'          # section number of the node table (7.2 in the public edition)
ID_SECTIONS = ('8.2', '8.5', '8.6', '8.7')


def configure(mode='internal', en_dir=None, ru_dir=None, regmap=None, table_num=None, id_sections=None):
    global MODE, EN_DIR, RU_DIR, REGMAP, TABLE_NUM, ID_SECTIONS
    MODE = mode
    if en_dir: EN_DIR = en_dir
    if ru_dir: RU_DIR = ru_dir
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
FOLD_HEADS = {
    'Sources': ('Sources', 'src'), 'Источники': ('Источники', 'src'),
    'Open verification items': ('Open verification items', 'ovi'),
    'Открытые пункты верификации': ('Открытые пункты верификации', 'ovi'),
}

RU_FALLBACK_NOTE = '*Перевод готовится — ниже английский текст брифа.*'

# ---------- preface (deliverable 2c; reused verbatim by the MD bundles)
PREFACE = {
    'en': [
        'Every technology on the map has a brief, and the depth of each one follows an importance score '
        'derived from the graph itself — how far a node reaches across platform families (hub reach), how '
        'many platform paths run through it, and how recent it is. Tier 1 is the 27 most important '
        'technologies at roughly 1,600–2,400 words; Tier 2 is 33 technologies at roughly 1,300 words; '
        'Tier 3 is 36 technologies at roughly 800 words. The tier is a statement about the graph, not a '
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
        'из самого графа: насколько узел дотягивается до разных семейств платформ (охват хаба), сколько '
        'путей платформ через него проходит и насколько он свеж. Tier 1 — 27 самых важных технологий, '
        'примерно 1 600–2 400 слов; Tier 2 — 33 технологии, примерно 1 300 слов; Tier 3 — 36 технологий, '
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
SECTION_TITLE = {'en': 'Technology briefs', 'ru': 'Брифы по технологиям'}


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
    return STATUS.get(s, (s, s))[0 if lang == 'en' else 1]


def _ru_from_en(en_meta):
    """Front matter for a RU brief whose file does not exist yet."""
    ru = dict(en_meta)
    n = layer_num(en_meta)
    if n:
        ru['layer'] = '%d %s' % (n, LAYER_RU.get(n, ''))
    return ru


def load_briefs():
    """All 96 briefs ordered by rank. RU falls back to the EN body when the file is missing."""
    out = []
    for bid, r in sorted(RANKING.items(), key=lambda kv: kv[1]['rank']):
        en_meta, en_body = parse_brief(os.path.join(EN_DIR, bid + '.md'))
        ru_path = os.path.join(RU_DIR, bid + '.md')
        if os.path.exists(ru_path):
            ru_meta, ru_body = parse_brief(ru_path)
            fallback = False
        else:
            ru_meta, ru_body = _ru_from_en(en_meta), RU_FALLBACK_NOTE + '\n\n' + en_body
            fallback = True
        out.append({
            'id': bid, 'rank': r['rank'], 'tier': r['tier'], 'score': r['score'],
            'layer': layer_num(en_meta), 'ru_fallback': fallback,
            'en': {'meta': en_meta, 'body': en_body},
            'ru': {'meta': ru_meta, 'body': ru_body},
        })
    return out


# ---------- family colours (same rule as map_js.py: first path a node belongs to)
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


def _gkey_chip(m):
    r = REGMAP.get(m.group(1))
    lab = TAGS['G'][0 if MODE == 'internal' else 0]
    if r and r.get('url'):
        tip = '%s · %s' % (r['text'][:220], r['date'])
        return '<a class="tag tag-G tag-link" href="%s" target="_blank" rel="noopener" title="%s">G</a>' % (html.escape(r['url']), html.escape(tip))
    return '<span class="tag tag-G" title="[G] %s">G</span>' % html.escape(lab)


def chip_tags(h, lang):
    """Turn [D]/[C]/… and [REG:KEY] into chips, skipping anything inside an HTML tag."""
    i = 0 if lang == 'en' else 1
    out = []
    for part in re.split(r'(<[^>]*>)', h):
        if part.startswith('<'):
            out.append(part)
            continue
        part = _REG_RE.sub(
            lambda m: '<span class="tag tag-reg" title="%s">REG:%s</span>' % (html.escape(REG_TITLE[i]), m.group(1)),
            part)
        part = _GKEY_RE.sub(_gkey_chip, part)
        part = _TAG_RE.sub(
            lambda m: '<span class="tag tag-%s" title="[%s] %s">%s</span>'
                      % (m.group(1), m.group(1), html.escape(TAGS[m.group(1)][i]), m.group(1)),
            part)
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


def _link_cites(h, bid, lang):
    """[n] in the body → link to the source entry; skips tags and the sources fold itself."""
    pre = 'brief-%s-%s-src-' % (bid, lang)
    out = []
    for part in re.split(r'(<[^>]*>)', h):
        if part.startswith('<'):
            out.append(part); continue
        out.append(_CITE.sub(lambda m: '<a class="cite" href="#%s%s">[%s]</a>' % (pre, m.group(1), m.group(1)), part))
    return ''.join(out)


def body_html(body, lang, md2html, bid=''):
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
                content = _anchor_sources(content, bid, lang)
            elif bid:
                content = _link_cites(content, bid, lang)
            out.append('<details class="fold bfold fold-%s"><summary>%s</summary><div class="bfoldin">%s</div></details>'
                       % (kind, head_raw, content))
        else:
            out.append('<h3 class="bh3">%s</h3>%s' % (head_raw, _link_cites(content, bid, lang) if bid else content))
    return chip_tags(autolink(''.join(out)), lang)


def inline_html(s, md2html):
    h = md2html(s).strip()
    h = re.sub(r'^<p>', '', h)
    h = re.sub(r'</p>$', '', h)
    return h.replace('</p>\n<p>', ' ')


# ---------- one brief section
NAV = {
    'en': {'map': '← Map station', 'row': '↑ Table 8.2 row', 'prev': '← Previous brief',
           'next': 'Next brief →', 'close': 'Close ✕', 'verdict': 'Verdict',
           'layer': 'layer', 'tier': 'Tier', 'rank': 'rank', 'since': 'since', 'updated': 'updated'},
    'ru': {'map': '← Станция на карте', 'row': '↑ Строка таблицы 8.2', 'prev': '← Предыдущий бриф',
           'next': 'Следующий бриф →', 'close': 'Закрыть ✕', 'verdict': 'Вердикт',
           'layer': 'слой', 'tier': 'Tier', 'rank': 'ранг', 'since': 'с', 'updated': 'обновлено'},
}


def _one_lang(b, lang, md2html, prev_id, next_id, colour):
    m = b[lang]['meta']
    t = NAV[lang]
    name = inline_html(m.get('name', b['id']), md2html)
    one = inline_html(m.get('one_line', ''), md2html)
    verdict = inline_html(m.get('verdict', ''), md2html)
    meta_line = ' · '.join(x for x in [
        '<span class="bid">%s</span>' % html.escape(b['id']),
        '%s %s' % (t['layer'], html.escape(m.get('layer', ''))),
        '%s %s' % (t['tier'], b['tier']),
        '%s %d/96' % (t['rank'], b['rank']),
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
    return ('<div class="bl lang-%s">'
            '<div class="brief-head" style="--fam:%s">'
            '<button type="button" class="chip bclose" data-briefclose="1">%s</button>'
            '<div class="bmeta">%s</div><h2 class="btitle">%s</h2>'
            '<p class="bone">%s</p>'
            '<p class="bverdict"><b>%s.</b> %s</p>%s</div>'
            '<div class="bbody">%s</div>%s</div>') % (
        lang, colour, t['close'], meta_line, name, one, t['verdict'], verdict,
        key_refs_html(key_refs(b['en']['body']), lang),
        body_html(b[lang]['body'], lang, md2html, b['id']), nav)


def brief_section(b, md2html, prev_id, next_id, colour):
    return ('<section class="brief" id="brief-%s" hidden>%s%s</section>' % (
        b['id'],
        _one_lang(b, 'en', md2html, prev_id, next_id, colour),
        _one_lang(b, 'ru', md2html, prev_id, next_id, colour)))


# ---------- index table
IDX_HEAD = {'en': ('rank', 'id', 'technology', 'layer', 'tier', 'one line'),
            'ru': ('ранг', 'id', 'технология', 'слой', 'tier', 'одной строкой')}


def index_table(briefs, lang, md2html):
    th = ''.join('<th>%s</th>' % h for h in IDX_HEAD[lang])
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
    """The whole '§ Technology briefs' block: heading, preface, index, and 96 hidden sections."""
    langs = []
    for lang in ('en', 'ru'):
        pref = ''.join('<p>%s</p>' % chip_tags(html.escape(p, quote=False), lang) for p in PREFACE[lang])
        langs.append('<div class="lang-%s"><h2><span class="num">%s</span>%s</h2>'
                     '<div class="blede">%s</div>%s</div>' % (
                         lang, 'BR' if lang == 'en' else 'БР', SECTION_TITLE[lang],
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


def _sources(body):
    txt = _section_text(body, 'Sources') or _section_text(body, 'Источники')
    out = {}
    for m in _SRC_LINE.finditer(txt):
        n = int(m.group(1) or m.group(2)); rest = m.group(3)
        u = _URL.search(rest)
        url = u.group(0).rstrip('.,;)') if u else ''
        label = rest[:u.start()].strip() if u else rest.strip()
        label = re.sub(r'\s*[—·-]\s*$', '', label)
        label = re.sub(r'\s*\[(?:REG:[^\]]+|[DCRSGP])\]\s*', ' ', label).strip()
        ys = [y for y in re.findall(r'(?<!\d)((?:19|20)\d\d)(?!\d)', label) if int(y) <= 2026]
        year = ys[-1] if ys else None
        short = re.split(r' et al\.?| · |, |\(|"|«|—', label, 1)[0].strip(' .:;')
        if len(short) > 26: short = short[:24].rstrip() + '…'
        out[n] = {'n': n, 'label': label, 'url': url, 'year': year, 'short': short}
    return out


def key_refs(body, limit=5):
    """Ordered, de-duplicated source numbers cited in Identity & lineage, then in the records-timeline table."""
    srcs = _sources(body)
    order = []
    lineage = _section_text(body, 'Identity & lineage')
    eng = _section_text(body, 'Engineering state of the art')
    table = '\n'.join(l for l in eng.split('\n') if l.startswith('|'))
    for chunk in (lineage, table, eng):
        for m in _CITE.finditer(chunk):
            n = int(m.group(1))
            if n in srcs and n not in order and srcs[n]['url']:
                order.append(n)
            if len(order) >= limit: break
        if len(order) >= limit: break
    return [srcs[n] for n in order]


def key_refs_all(briefs, limit=5):
    return {b['id']: key_refs(b['en']['body'], limit) for b in briefs}


def key_refs_html(refs, lang):
    if not refs: return ''
    t = 'Key references' if lang == 'en' else 'Ключевые источники'
    items = ''.join('<a href="%s" target="_blank" rel="noopener" title="%s">[%d] %s%s</a>' % (
        html.escape(r['url']), html.escape(r['label']), r['n'], html.escape(r.get('short') or ''), (' ' + r['year']) if r['year'] else '') for r in refs)
    return '<div class="bkeys"><span class="tk">%s</span> %s</div>' % (t, items)
