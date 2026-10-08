# -*- coding: utf-8 -*-
"""Every record of the Atlas at its own address (27 Sep 2026, the editor's item 16).

Built by build_html.build() after the main pages, from the same data and renderers:
  dist/technology/<id>.html      the technology card + the technology brief (111 × 2 languages)
  dist/machine/<id>.html         the machine card (the register's profile, cells, records) + its pictures
  dist/architecture/<pid>.html   the architecture card + the §8.3 narrative and register block + machines
  dist/organisation/<slug>.html  the organisation's profile: machines, technologies, architectures, mentions
  dist/<kind>/index.html         one index per kind; dist/sitemap.xml; dist/assets/atlas.css, cards.css
Every language of build/langs.py has its pages in its folder (dist/ru/<kind>/…, dist/he/<kind>/… since 29 Sep 2026); every page names
its twins in the other languages (hreflang, and links by the languages' own names) and the main page
("Open on the map": #station-<id>, #machine-<id>, #architecture-<pid>, which map_js handles). Pictures come from the media
register through build/media.py (hosted thumbnails at <atlas>/media/<asset>.jpg — the deploy copies them; the build lists them
in dist/media-files.txt). Links inside a record page that point at an anchor of the main page are rewritten to go there.
"""
import datetime, hashlib, html, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build')); sys.path.insert(0, os.path.join(ROOT, 'data'))
import cards, media, orgs, regvocab
from editions import EDITIONS, CONCEPT_DOI, SITE, REPO
from langs import LANGS, NATIVE, FOLDER, pick, direction, others, up

KINDS = ('technology', 'machine', 'architecture', 'organisation')
# the sitemap's <lastmod> per page (8 Oct 2026: every URL carried the edition date, so a later change looked like none to a search engine)
LASTMOD = os.path.join(ROOT, 'data', 'vv', 'page-lastmod.json')
LASTMOD_DOC = ("Ledger of the sitemap's <lastmod>, one entry per sitemap page, keyed by the page's path under dist/ (the language roots by their "
               "index.html). sha256 = the hash of the page's bytes as the build wrote them, all of them: the pages embed no build date or time "
               "(their only date is the edition's, editions.EDITIONS[0]['date'], which is data) and the sitemap's lastmod is not fed back into any "
               "page. lastmod = the day the page's bytes last changed: a build keeps the ledger's lastmod for a page whose hash is unchanged and "
               "gives a new or changed page the build's own date (datetime.date.today()); a page no longer built is dropped. Written by "
               "build/pages.py at every build and committed with the change that moved it. Seeded 8 Oct 2026: 2026-09-30 (the edition) for a "
               "page whose bytes were equal in the builds of tag 2026.09 and of c7-2026-10-08; for a page that differed, the date of the last "
               "commit that changed it in dist/ (the three main pages: 2026-10-07), else 2026-10-04 (the record pages, which are not committed).")
T = {
 'en': dict(atlas='Quantum Technology Atlas', back='← Quantum Technology Atlas', map='Open on the map', tech='Technologies', mach='Machines',
            arch='Architectures', org='Organisations', brief='Brief', pictures='Pictures', cite='Cite as',
            index='Index', edition='Edition', part='part of the', licence='CC BY 4.0', prev='← previous', next='next →',
            tech_one='technology', mach_one='machine', arch_one='architecture', org_one='organisation',
            narrative='The architecture in the report (§8.3)', machines_of='Machines of this architecture', by_layer='by layer',
            no_pictures='No picture in the media register yet.', story_note='Every picture carries the story of what it shows and its credit line.',
            chip='on the map bar: %s'),
 'ru': dict(atlas='Quantum Technology Atlas', back='← Quantum Technology Atlas', map='Открыть на карте', tech='Технологии', mach='Машины',
            arch='Архитектуры', org='Организации', brief='Обзор', pictures='Иллюстрации', cite='Как цитировать',
            index='Указатель', edition='Издание', part='часть издания', licence='CC BY 4.0', prev='← предыдущая', next='следующая →',
            tech_one='технология', mach_one='машина', arch_one='архитектура', org_one='организация',
            narrative='Архитектура в отчёте (§8.3)', machines_of='Машины этой архитектуры', by_layer='по слоям', chip='на панели карты: %s',
            no_pictures='В медиа-реестре пока нет иллюстрации.', story_note='У каждой иллюстрации — рассказ о том, что на ней, и строка авторства.'),
 # Hebrew (29 Sep 2026; the terms of data/i18n/he-terms.md): the arrows point the reader's way in a right-to-left line
 'he': dict(atlas='Quantum Technology Atlas', back='→ Quantum Technology Atlas', map='פתח במפה', tech='טכנולוגיות', mach='מכונות',
            arch='ארכיטקטורות', org='ארגונים', brief='תקציר', pictures='תמונות', cite='כיצד לצטט',
            index='מפתח', edition='מהדורה', part='חלק מן', licence='CC BY 4.0', prev='→ הקודמת', next='הבאה ←',
            tech_one='טכנולוגיה', mach_one='מכונה', arch_one='ארכיטקטורה', org_one='ארגון',
            narrative='הארכיטקטורה בדוח (§8.3)', machines_of='מכונות בארכיטקטורה זו', by_layer='לפי שכבה', chip='בסרגל המפה: %s',
            no_pictures='במרשם המדיה אין עדיין תמונה.', story_note='כל תמונה מלווה בתיאור של מה שהיא מראה ובשורת הקרדיט שלה.'),
}
KIND_T = {'technology': 'tech', 'machine': 'mach', 'architecture': 'arch', 'organisation': 'org'}
ORG_LINKS = None   # build_html.link_org_blocks, injected at build time: organisation names link to their pages, block by block (29 Sep 2026)
def AG(L): return '<h4>%s</h4><div>' % cards.esc(cards.T(L, *cards.ACTORS_GOALS))   # the architecture card's actors line (a block for ORG_LINKS), in the card's own words


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').lower()
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')


def cards_css(css):
    """The map's card rules (.insp …) re-scoped to .card for the record pages; the panel's own geometry rules are left out."""
    out = []
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel, body = m.group(1).strip(), m.group(2)
        if '.insp' not in sel: continue
        parts = []
        for s in sel.split(','):
            s = s.strip()
            if re.search(r'\.insp\b(?![ >])', s): continue   # .insp itself, .insp.sheet-max, .insp:… — panel geometry
            if re.search(r'\.insp\s*[ >]', s): parts.append(re.sub(r'\.insp\b', '.card', s, count=1))
        if parts: out.append('%s{%s}' % (','.join(parts), body))
    return '\n'.join(out)


class Site:
    def __init__(self, cfg, G, MACH, B, briefs_mod, md2html, colours, page_html, CSS, tips, gtip_js, tag_js, keyrefs):
        self.cfg, self.G, self.MACH, self.B, self.BR, self.md2html, self.colours = cfg, G, MACH, B, briefs_mod, md2html, colours
        self.page_html = page_html      # {'en': the built English main page, 'ru': the Russian one} — for the §8.3 blocks
        self.CSS, self.tips, self.gtip_js, self.tag_js = CSS, tips, gtip_js, tag_js
        self.node = {n['id']: n for n in G['nodes']}; self.path = {p['id']: p for p in G['paths']}
        self.mach = {m['id']: m for m in MACH['machines']}
        self.bmap = {b['id']: b for b in B}
        cards.load(keyrefs); media.load(); orgs.load()
        self.orgs = orgs.load()['organisations']; self.org_of = {}
        for o in self.orgs:
            for mid in o.get('machines', []): self.org_of[mid] = o['slug']
        self.edition = cfg['edition']; self.site = cfg.get('site', SITE)
        self.dist = os.path.join(ROOT, 'dist'); self.urls = []   # (lang, path) for the sitemap
        self.written = 0; self.org_links = 0; self.written_by = {}; self.sha = {}   # sitemap path → sha256 of the bytes written

    # ---------- addresses
    def rel(self, lang): return '../' + up(lang)                            # from dist/[<lang>/]<kind>/x.html to dist/
    def base(self, lang): return self.rel(lang) + FOLDER[lang]              # … to the language's root (its index.html and record folders)
    def href(self, kind, ident, lang, from_lang=None):
        """address of a record page relative to another record page of `from_lang` (default: the same language)"""
        return '%s%s%s/%s.html' % (self.rel(from_lang or lang), FOLDER[lang], kind, ident)
    def abs_url(self, kind, ident, lang): return '%s%s%s/%s.html' % (self.site, FOLDER[lang], kind, ident)
    def out_path(self, kind, ident, lang): return os.path.join(self.dist, FOLDER[lang], kind, ident + '.html')

    # ---------- shell
    @staticmethod
    def meta_desc(desc, limit=160):
        """the description search engines show: at most `limit` characters, cut at the last clause boundary (3 Oct 2026 — Bing's rule
        is 25–160; 51 English, 97 Russian and 26 Hebrew technology pages had carried their brief's whole first sentence)"""
        if len(desc) <= limit: return desc
        cut = desc[:limit - 1]
        pos = max(cut.rfind(sep) for sep in ('; ', ' — ', ', ', ': ', ' – '))
        if pos < limit // 2: pos = cut.rfind(' ')
        return cut[:pos].rstrip(' ,;:—–') + '…'
    def shell(self, kind, ident, lang, title, desc, body, image=None, twin=True, jsonld_extra=None):
        t = pick(lang, T); base = self.rel(lang)
        canonical = self.abs_url(kind, ident, lang)
        alts = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (L, self.abs_url(kind, ident, L)) for L in LANGS) + \
               '<link rel="alternate" hreflang="x-default" href="%s">' % self.abs_url(kind, ident, 'en')
        og_image = image or (self.cfg.get('og_image') or '')
        ld = {"@context": "https://schema.org", "@type": "TechArticle", "headline": title, "inLanguage": lang, "url": canonical,
              "isPartOf": {"@type": "ScholarlyArticle", "name": "Quantum Technology Atlas", "url": self.site, "identifier": "https://doi.org/" + CONCEPT_DOI},
              "author": {"@type": "Person", "name": self.cfg['author']}, "publisher": {"@type": "Organization", "name": self.cfg['publisher']},
              "license": "https://creativecommons.org/licenses/by/4.0/", "datePublished": self.cfg['date'], "description": desc}
        if og_image: ld["image"] = og_image
        if jsonld_extra: ld.update(jsonld_extra)
        nav_kinds = ' · '.join('<a href="%s%s/index.html">%s</a>' % (self.base(lang), k, t[KIND_T[k]]) for k in KINDS)
        head = (f'<!doctype html>\n<html lang="{lang}" dir="{direction(lang)}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{html.escape(title)} — Quantum Technology Atlas</title>\n<meta name="description" content="{html.escape(self.meta_desc(desc))}">\n'
                f'<meta name="author" content="{html.escape(self.cfg["author"])}"><meta name="citation_title" content="{html.escape(title)} — Quantum Technology Atlas"><meta name="citation_author" content="{html.escape(self.cfg["author"])}">'
                f'<meta name="citation_publication_date" content="{self.cfg["date"].replace("-", "/")}"><meta name="citation_publisher" content="{html.escape(self.cfg["publisher"])}"><meta name="citation_doi" content="{CONCEPT_DOI}"><meta name="citation_language" content="{lang}">\n'
                f'<meta property="og:type" content="article"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canonical}">'
                + (f'<meta property="og:image" content="{html.escape(og_image)}">' if og_image else '') +
                f'<meta name="twitter:card" content="summary_large_image">\n<link rel="canonical" href="{canonical}">{alts}<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">\n'
                f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Golos+Text:wght@400;500;600&family=Heebo:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">'
                f'<link rel="stylesheet" href="{base}assets/atlas.css"><link rel="stylesheet" href="{base}assets/cards.css"><link rel="stylesheet" href="{base}assets/record.css">'
                f'<meta name="color-scheme" content="light dark"><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head>\n')
        # the page in the other languages, each by its own name (29 Sep 2026: every language of langs.LANGS)
        twin_link = ''.join(f'<a class="rb-lang" href="{self.href(kind, ident, L, lang)}" hreflang="{L}" lang="{L}" dir="{direction(L)}">{NATIVE[L]}</a>' for L in others(lang)) if twin else ''
        bar = (f'<div class="recbar"><a class="rb-home" href="{self.base(lang)}index.html">{t["back"]}</a>'
               f'<span class="rb-kinds">{nav_kinds}</span><span class="rb-sp"></span>{twin_link}</div>')
        foot = (f'<footer class="recfoot"><p><b>{t["cite"]}.</b> {html.escape(self.cfg["author"])} (2026). <i>Quantum Technology Atlas</i>. {html.escape(self.cfg["publisher"])}. '
                f'<a href="https://doi.org/{CONCEPT_DOI}">https://doi.org/{CONCEPT_DOI}</a> — {t["edition"]} {self.edition} · <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">{t["licence"]}</a> · '
                f'<a href="{REPO}">GitHub</a></p></footer>')
        page = head + f'<body class="record record-{kind}"><div id="app" data-lang="{lang}" data-page-lang="{lang}" data-edition="{self.edition}">{bar}<main class="recmain">{body}</main>{foot}</div>' \
               f'<script src="{base}assets/tips.js"></script><script>{self.gtip_js}</script><script>{self.tag_js}</script></body></html>'
        return self.fix_links(page, lang)

    def fix_links(self, page, lang):
        """a fragment link whose target is not on this page goes to the main page's anchor; buttons of the brief become links"""
        main = self.base(lang) + 'index.html'
        ids = set(re.findall(r'\sid="([^"]+)"', page))
        def sub(m):
            frag = m.group(1)
            if frag in ids or frag == '': return m.group(0)
            return 'href="%s#%s"' % (main, frag)
        page = re.sub(r'href="#([^"]*)"', sub, page)
        return page

    # ---------- pieces
    def gallery(self, key, lang, n=3):
        base = self.rel(lang); g = media.gallery_html(key, lang, base, n=n)   # pictures live at the root's media/
        t = pick(lang, T)
        if not g: return ''
        return f'<section class="pictures"><h3>{t["pictures"]}</h3><p class="empty">{t["story_note"]}</p>{g}</section>'

    def first_image(self, key):
        for a in media.pick(key, n=1):
            if a.get('thumb'): return self.site + 'media/' + a['thumb']
        return None

    # ---------- technology pages
    def technology(self, lang):
        t = pick(lang, T); base = self.base(lang)   # the cards link the records of the page's own language
        order = [b['id'] for b in self.B]
        for i, b in enumerate(self.B):
            nid = b['id']; n = self.node[nid]
            prev_id = order[i - 1] if i else ''; next_id = order[i + 1] if i + 1 < len(order) else ''
            card = cards.station_card_html(nid, lang, base)
            brief = self.BR._one_lang(b, lang, self.md2html, prev_id, next_id, self.colours.get(nid, 'var(--mid)'))
            # the brief's own controls become links: prev/next → the neighbouring technology pages, close → the index, "technology on the map" → the map
            brief = re.sub(r'<button type="button" class="chip" data-brief="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s">%s</a>' % (self.href('technology', m.group(1), lang), m.group(2)), brief)
            brief = re.sub(r'<button type="button" class="chip bclose" data-briefclose="1">[^<]*</button>', '', brief)
            brief = re.sub(r'<button type="button" class="chip" data-briefclose="1">[^<]*</button>', '', brief)
            mainp = base + 'index.html'
            brief = re.sub(r'<button type="button" class="chip" data-mapstation="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s#station-%s">%s</a>' % (mainp, m.group(1), m.group(2)), brief)
            brief = re.sub(r'<button type="button" class="chip" data-tablerow="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s#%s-s7-2">%s</a>' % (mainp, lang, m.group(2)), brief)
            brief = re.sub(r'<a class="chip" href="#" data-goto="(\w+)"([^>]*)>', lambda m: '<a class="chip" href="%s#station-%s"%s>' % (mainp, m.group(1), m.group(2)), brief)
            brief = re.sub(r'<div class="bl lang-%s"' % lang, lambda m: m.group(0) + ' id="brief"', brief, count=1)
            if lang != 'en':   # a non-English Sources list is a clone of the English one, filled on the main page by its script; a record page
                import brief_refs   # runs none: it carries the list itself (29 Sep 2026 — the Russian record pages had shown an empty list)
                lst = (brief_refs.list_html(nid, 'en') or '').replace(' id="brief-%s-en-refs"' % nid, '').replace('-en-src-', '-%s-src-' % lang).replace('href="#en-s', 'href="#%s-s' % lang)
                if lst: brief = re.sub(r'<ol class="refs" data-nohint="1" data-clone="brief-%s-en-refs"[^>]*></ol>' % re.escape(nid), lambda m: lst, brief)
            pics = self.gallery('node:' + nid, lang)
            name = pick(lang, n); one = self.BR.inline_html(b[lang]['meta'].get('one_line', ''), self.md2html)
            desc = re.sub(r'<[^>]+>', '', one) or pick(lang, n['desc'])
            body = f'<h1 class="rectitle">{html.escape(name)} <span class="recid">{nid}</span></h1><p class="reclead">{one}</p>{card}{pics}<section class="recbrief">{brief}</section>'
            self.write('technology', nid, lang, name, desc, body, image=self.first_image('node:' + nid))

    # ---------- machine pages
    def machine(self, lang):
        t = pick(lang, T); base = self.base(lang)
        for mid, m in sorted(self.mach.items()):
            card = cards.machine_card_html(mid, lang, base)
            oslug = self.org_of.get(mid)
            orgline = (f'<p class="recorg"><a href="{self.href("organisation", oslug, lang)}">{html.escape(m["org"])}</a></p>' if oslug else f'<p class="recorg">{html.escape(m["org"])}</p>')
            pics = self.gallery('machine:' + mid, lang)
            name = m['name']; p = self.path.get(m['map_path'])
            q = m.get('physical_qubits_num')
            desc = '%s — %s; %s; %s' % (m['org'], (pick(lang, p.get('short') or {}) or pick(lang, p)) if p else m['map_path'], m['status'].lower(), ('%s %s' % (q, pick(lang, ('qubits', 'кубитов', 'קיוביטים')))) if q else '')
            body = f'<h1 class="rectitle">{html.escape(name)}</h1>{orgline}{card}{pics}'
            self.write('machine', mid, lang, name, desc.strip('; '), body, image=self.first_image('machine:' + mid))

    # ---------- architecture pages
    def architecture(self, lang):
        t = pick(lang, T); base = self.base(lang); H = self.page_html[lang]; P = lang   # the main page's ids carry its language (he-s8-3-1 …)
        for k, p in enumerate(self.G['paths'], 1):
            pid = p['id']
            card = cards.architecture_card_html(pid, lang, base).replace(AG(lang), AG(lang)[:-1] + ' class="actors">', 1)
            # the §8.3.k block of the main page: from its h4 to the next h4/h3/h2
            m = re.search(r'<h4 id="%s-s8-3-%d"[^>]*>.*?</h4>' % (P, k), H, flags=re.S)
            narr = ''
            if m:
                j = re.search(r'<h[234] id="%s-s8' % P, H[m.end():])
                block = H[m.start():(m.end() + j.start()) if j else m.end() + 200000]
                block = re.sub(r'<button type="button" class="foldbtn"[^>]*></button>', '', block)
                # the main page's record links are relative to its folder: from here they go through the language's root (29 Sep 2026 —
                # the organisation links of §8.3 pointed at architecture/organisation/… until then)
                block = re.sub(r'href="(?=(?:organisation|technology|machine|architecture)/)', 'href="' + base, block)
                narr = f'<section class="recnarr"><h2>{t["narrative"]}</h2>{block}</section>'
            name = pick(lang, p); short = pick(lang, p.get('short') or {}) or ''      # one name per architecture: the full one; the map bar's short label is a note
            desc = '%s — %s' % (name, p.get('actors', ''))
            body = f'<h1 class="rectitle">{html.escape(name)}' + (f' <span class="recid">{html.escape(t["chip"] % short)}</span>' if short and short != name else '') + f'</h1>{card}{narr}'
            self.write('architecture', pid, lang, name, desc[:300], body)

    # ---------- organisation pages
    def organisation(self, lang):
        t = pick(lang, T); base = self.base(lang)
        for o in self.orgs:
            prof = re.sub(r'<h2>.*?</h2>', '', orgs.profile_html(o, lang, base, self.mach, self.node, self.path), count=1)   # the page's h1 carries the name
            pics = ''.join(media.gallery_html('machine:' + mid, lang, self.rel(lang), n=1) for mid in o.get('machines', [])[:6])
            if pics: pics = f'<section class="pictures"><h3>{t["pictures"]}</h3>{pics}</section>'
            desc = ' · '.join(x for x in [o.get('tier', ''), o.get('segment', ''), o.get('country', '')] if x) + (' — %d %s' % (len(o.get('machines', [])), t['mach'].lower()) if o.get('machines') else '')
            body = f'<h1 class="rectitle">{html.escape(o["name"])}</h1>{prof}{pics}'
            img = None
            for mid in o.get('machines', []):
                img = self.first_image('machine:' + mid)
                if img: break
            self.write('organisation', o['slug'], lang, o['name'], desc, body, image=img)

    # ---------- indexes and the sitemap
    def indexes(self, lang):
        t = pick(lang, T); base = self.rel(lang)
        # technologies by layer
        rows = []
        for l in self.G['layers']:
            items = [n for n in self.G['nodes'] if n['layer'] == l['n']]
            rows.append('<h3>%d · %s</h3><ul>%s</ul>' % (l['n'], html.escape(pick(lang, l)), ''.join('<li><a href="%s">%s</a> <code>%s</code> — %s</li>' % (self.href('technology', n['id'], lang), html.escape(pick(lang, n)), n['id'], html.escape(pick(lang, n['desc'])[:160])) for n in items)))
        self.write('technology', 'index', lang, t['tech'], t['tech'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["tech"]} · {len(self.G["nodes"])}</h1>' + ''.join(rows), twin=True)
        # machines by family then name
        fams = {}
        for m in self.mach.values(): fams.setdefault(m['family'], []).append(m)
        rows = []
        for f, ms in sorted(fams.items(), key=lambda kv: -len(kv[1])):
            def mrow(m):   # name — org; status, qubits; access · ✅ verified/total cells (27 Sep 2026: the index showed no access and no evidence grade)
                ec = m.get('evidence_counts') or {}
                st = regvocab.status_l(m['status'], lang)
                acc = regvocab.access_l(m.get('access') or '', lang)
                return '<li><a href="%s">%s</a> — %s; %s%s%s <span class="recid">✅ %s/%s</span></li>' % (
                    self.href('machine', m['id'], lang), html.escape(m['name']), html.escape(m['org']), html.escape(st.lower()),
                    (', %s q' % m['physical_qubits_num']) if m.get('physical_qubits_num') else '', ('; %s' % html.escape(acc)) if acc and acc != 'n/a' else '',
                    ec.get('verified', 0), ec.get('total', 0))
            rows.append('<h3>%s · %d</h3><ul>%s</ul>' % (html.escape(f), len(ms), ''.join(mrow(m) for m in sorted(ms, key=lambda m: m['name']))))
        self.write('machine', 'index', lang, t['mach'], t['mach'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["mach"]} · {len(self.mach)}</h1>' + ''.join(rows))
        rows = ''.join('<li><a href="%s">%s</a>%s</li>' % (self.href('architecture', p['id'], lang), html.escape(pick(lang, p)), (' — %s' % html.escape(t['chip'] % pick(lang, p.get('short') or {}))) if pick(lang, p.get('short') or {}) else '') for p in self.G['paths'])
        self.write('architecture', 'index', lang, t['arch'], t['arch'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["arch"]} · {len(self.G["paths"])}</h1><ul>{rows}</ul>')
        rows = ''.join('<li><a href="%s">%s</a> — %s%s</li>' % (self.href('organisation', o['slug'], lang), html.escape(o['name']), html.escape(o.get('country', '') or ''), (' · %d %s' % (len(o['machines']), t['mach'].lower())) if o.get('machines') else '') for o in self.orgs)
        self.write('organisation', 'index', lang, t['org'], t['org'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["org"]} · {len(self.orgs)}</h1><ul>{rows}</ul>')

    def sitemap(self):
        """every page with its alternates in every language of langs.LANGS (hreflang) and x-default = English"""
        urls = []
        def entry(loc, alts):
            a = ''.join('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (L, u) for L, u in alts)
            return '<url><loc>%s</loc>%s<lastmod>%s</lastmod></url>' % (loc, a, lastmod[key(loc)])
        def key(loc): k = loc[len(self.site):]; return k + 'index.html' if k == '' or k.endswith('/') else k   # the page's path under dist/
        locs = [self.site + FOLDER[L0] for L0 in LANGS] + [self.abs_url(kind, ident, lang) for lang, kind, ident in self.urls]
        for L0 in LANGS:   # the main pages (build_html wrote them before the record pages; index.html is the directory's default document)
            self.sha[FOLDER[L0] + 'index.html'] = hashlib.sha256(open(os.path.join(self.dist, FOLDER[L0], 'index.html'), 'rb').read()).hexdigest()
        lastmod = self.lastmod([key(l) for l in locs])
        for L0 in LANGS:
            urls.append(entry(self.site + FOLDER[L0], [(L, self.site + FOLDER[L]) for L in LANGS] + [('x-default', self.site)]))
        for lang, kind, ident in self.urls:
            loc = self.abs_url(kind, ident, lang)
            urls.append(entry(loc, [(L, self.abs_url(kind, ident, L)) for L in LANGS] + [('x-default', self.abs_url(kind, ident, 'en'))]))
        sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n'
        open(os.path.join(self.dist, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(sm)

    def lastmod(self, keys):
        """the ledger data/vv/page-lastmod.json (its _doc defines it): an unchanged page keeps its lastmod, a new or changed page takes
        the build's date, a vanished page is dropped; the ledger is rewritten only when an entry moved"""
        try: old = json.load(open(LASTMOD, encoding='utf-8')).get('pages', {})
        except (OSError, ValueError): old = {}
        today = datetime.date.today().isoformat(); new = {}; moved = 0
        for k in keys:
            e = old.get(k)
            if e and e.get('sha256') == self.sha[k]: new[k] = e
            else: new[k] = {'sha256': self.sha[k], 'lastmod': today}; moved += 1
        dropped = len(set(old) - set(new))
        if moved or dropped or list(old) != sorted(new):
            body = ',\n'.join('  %s: %s' % (json.dumps(k), json.dumps(new[k], sort_keys=True)) for k in sorted(new))
            os.makedirs(os.path.dirname(LASTMOD), exist_ok=True)
            open(LASTMOD, 'w', encoding='utf-8', newline='\n').write('{\n "_doc": %s,\n "pages": {\n%s\n }\n}\n' % (json.dumps(LASTMOD_DOC, ensure_ascii=False), body))
        print('sitemap lastmod: %d page(s), %d new or changed (lastmod %s), %d dropped' % (len(new), moved, today, dropped))
        return {k: v['lastmod'] for k, v in new.items()}

    # ---------- write
    def write(self, kind, ident, lang, title, desc, body, image=None, twin=True):
        if ORG_LINKS:   # to the organisation pages of the page's own language; an organisation's page does not link itself
            n0 = body.count('<a class="org" href="')
            body = ORG_LINKS(body, self.base(lang), own=(ident,) if kind == 'organisation' else ())
            self.org_links += body.count('<a class="org" href="') - n0
        page = self.shell(kind, ident, lang, title, desc, body, image=image, twin=twin)
        p = self.out_path(kind, ident, lang); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8', newline='\n').write(page); self.sha[os.path.relpath(p, self.dist).replace(os.sep, '/')] = hashlib.sha256(page.encode('utf-8')).hexdigest(); self.written += 1; self.written_by[lang] = self.written_by.get(lang, 0) + 1
        self.urls.append((lang, kind, ident))
        self.media_used.update(re.findall(r'media/([A-Za-z0-9_.\-]+\.jpg)', page))   # the pictures this page shows (src and og:image)

    def assets(self):
        d = os.path.join(self.dist, 'assets'); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'atlas.css'), 'w', encoding='utf-8', newline='\n').write(self.CSS)
        open(os.path.join(d, 'cards.css'), 'w', encoding='utf-8', newline='\n').write(cards_css(self.CSS))
        open(os.path.join(d, 'record.css'), 'w', encoding='utf-8', newline='\n').write(RECORD_CSS)
        open(os.path.join(d, 'tips.js'), 'w', encoding='utf-8', newline='\n').write('window.__TIPS=%s;\n' % self.tips)   # the hints' texts, one shared file

    def build(self, langs=tuple(LANGS)):
        self.assets(); self.media_used = set()
        for lang in langs:
            self.technology(lang); self.machine(lang); self.architecture(lang); self.organisation(lang); self.indexes(lang)
        # a row that left the data (merged, removed) must not leave its page behind in dist/: a clean clone never had it, a reused
        # working tree kept it and would deploy it (equal1-bell-1 and google-fluxonium were still there on 30 Sep 2026)
        written = set(self.urls); stale = []
        for lang in langs:
            for kind in ('technology', 'machine', 'architecture', 'organisation'):
                d = os.path.join(self.dist, FOLDER[lang], kind)
                if not os.path.isdir(d): continue
                for f in sorted(os.listdir(d)):
                    if f.endswith('.html') and (lang, kind, f[:-5]) not in written:
                        os.remove(os.path.join(d, f)); stale.append('%s%s/%s' % (FOLDER[lang], kind, f))
        if stale: print('record pages: %d stale page(s) removed — %s' % (len(stale), ', '.join(stale)))
        self.sitemap()
        # the pictures the deploy must copy from the media register's thumbs: only those a page shows (289 of 706 hosted on 27 Sep 2026)
        for key in ['node:' + n['id'] for n in self.G['nodes']] + ['machine:' + mid for mid in self.mach]:   # the map's cards show each target's first picture (build_html.pics_slim, 28 Sep 2026)
            for a in media.pick(key, n=1):
                if a.get('thumb'): self.media_used.add(a['thumb'])
        hosted = set(media.hosted_files()); used = sorted(self.media_used & hosted)
        unknown = sorted(self.media_used - hosted)
        if unknown: raise SystemExit('pages: pictures referenced but not hosted by the media register: %s' % ', '.join(unknown[:10]))
        open(os.path.join(self.dist, 'media-files.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(used) + '\n')
        return self.written


RECORD_CSS = """
/* record pages (27 Sep 2026): one record per page, the map's card rendered statically, the brief or the narrative below */
body.record{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "Golos Text",system-ui,sans-serif}
.recbar{display:flex;gap:14px;align-items:center;flex-wrap:wrap;padding:10px 20px;border-bottom:1px solid var(--line);font-size:14px;position:sticky;top:0;background:var(--bg);z-index:5}
.recbar .rb-home{font-weight:600;text-decoration:none;color:var(--ink)} .recbar .rb-kinds a{margin-inline-end:2px} .recbar .rb-sp{flex:1} .recbar .rb-lang{text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:2px 10px}
.recmain{max-width:1080px;margin:0 auto;padding:18px 20px 60px}
.rectitle{font:700 30px/1.15 "Unbounded","Golos Text",sans-serif;margin:14px 0 6px} .rectitle .recid{font:500 13px "JetBrains Mono",monospace;color:var(--ink2);margin-inline-start:10px;vertical-align:middle}
.reclead{font-size:17px;color:var(--ink2);margin:0 0 18px} .recorg{margin:0 0 14px;font-size:15px}
.card{border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:14px 0;background:var(--surface)}
.card h3{margin:0 0 4px;font-size:20px} .card .meta{font-size:13px;color:var(--ink2)} .card .mlinks{margin:6px 0 10px;font-size:14px} .card .maplink{font-weight:600}
.pictures{margin:18px 0} .pictures h3{margin:0 0 6px} .pictures .empty{margin:0 0 8px}
figure.media{margin:0 0 18px;padding:0;max-width:820px} figure.media img{max-width:100%;height:auto;border-radius:8px;border:1px solid var(--line)} figure.media figcaption{font-size:13.5px;color:var(--ink2);line-height:1.45;margin-top:6px} figure.media .credit{display:block;margin-top:4px;font-size:12.5px;color:var(--muted)}
figure.media.linkout{padding:10px 14px;border:1px dashed var(--line);border-radius:8px}
.recbrief .bl{display:block} .recbrief .brief-head{margin-top:26px} .recnarr h2{margin-top:30px}
.recfoot{max-width:1080px;margin:0 auto;padding:18px 20px 40px;border-top:1px solid var(--line);font-size:13.5px;color:var(--ink2)}
.orgcard h2{margin:6px 0} .orgcard .meta{color:var(--ink2);font-size:14px}
@media (max-width:700px){.rectitle{font-size:24px}.recmain{padding:12px 14px 50px}}
"""
