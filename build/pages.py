# -*- coding: utf-8 -*-
"""Every record of the Atlas at its own address (27 Sep 2026, the editor's item 16).

Built by build_html.build() after the main pages, from the same data and renderers:
  dist/technology/<id>.html      the station card + the technology brief (111 × 2 languages)
  dist/machine/<id>.html         the machine card (the register's profile, cells, records) + its pictures
  dist/architecture/<pid>.html   the architecture card + the §8.3 narrative and register block + machines
  dist/organisation/<slug>.html  the organisation's profile: machines, technologies, architectures, mentions
  dist/<kind>/index.html         one index per kind; dist/sitemap.xml; dist/assets/atlas.css, cards.css
Russian pages under dist/ru/<kind>/…; every page names its twin in the other language (hreflang) and the main page
("Open on the map": #station-<id>, #machine-<id>, #architecture-<pid>, which map_js handles). Pictures come from the media
register through build/media.py (hosted thumbnails at <atlas>/media/<asset>.jpg — the deploy copies them; the build lists them
in dist/media-files.txt). Links inside a record page that point at an anchor of the main page are rewritten to go there.
"""
import html, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build')); sys.path.insert(0, os.path.join(ROOT, 'data'))
import cards, media, orgs
from editions import EDITIONS, CONCEPT_DOI, SITE, REPO

KINDS = ('technology', 'machine', 'architecture', 'organisation')
T = {
 'en': dict(atlas='Quantum Technology Atlas', back='← Quantum Technology Atlas', map='Open on the map', tech='Technologies', mach='Machines',
            arch='Architectures', org='Organisations', brief='Brief', pictures='Pictures', cite='Cite as', lang='Русский', twin='ru',
            index='Index', edition='Edition', part='part of the', licence='CC BY 4.0', prev='← previous', next='next →',
            tech_one='technology', mach_one='machine', arch_one='architecture', org_one='organisation',
            narrative='The architecture in the report (§8.3)', machines_of='Machines of this architecture', by_layer='by layer',
            no_pictures='No picture in the media register yet.', story_note='Every picture carries the story of what it shows and its credit line.'),
 'ru': dict(atlas='Quantum Technology Atlas', back='← Quantum Technology Atlas', map='Открыть на карте', tech='Технологии', mach='Машины',
            arch='Архитектуры', org='Организации', brief='Бриф', pictures='Иллюстрации', cite='Как цитировать', lang='English', twin='en',
            index='Указатель', edition='Издание', part='часть издания', licence='CC BY 4.0', prev='← предыдущая', next='следующая →',
            tech_one='технология', mach_one='машина', arch_one='архитектура', org_one='организация',
            narrative='Архитектура в отчёте (§8.3)', machines_of='Машины этой архитектуры', by_layer='по слоям',
            no_pictures='В медиа-реестре пока нет иллюстрации.', story_note='У каждой иллюстрации — рассказ о том, что на ней, и строка авторства.'),
}
KIND_T = {'technology': 'tech', 'machine': 'mach', 'architecture': 'arch', 'organisation': 'org'}


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
        self.written = 0

    # ---------- addresses
    def rel(self, lang): return '../' if lang == 'en' else '../../'          # from dist/<kind>/x.html or dist/ru/<kind>/x.html to dist/
    def href(self, kind, ident, lang, from_lang=None):
        """address of a record page relative to another record page of `from_lang` (default: the same language)"""
        return '%s%s%s/%s.html' % (self.rel(from_lang or lang), '' if lang == 'en' else 'ru/', kind, ident)
    def abs_url(self, kind, ident, lang): return '%s%s%s/%s.html' % (self.site, '' if lang == 'en' else 'ru/', kind, ident)
    def out_path(self, kind, ident, lang): return os.path.join(self.dist, '' if lang == 'en' else 'ru', kind, ident + '.html')

    # ---------- shell
    def shell(self, kind, ident, lang, title, desc, body, image=None, twin=True, jsonld_extra=None):
        t = T[lang]; base = self.rel(lang); other = 'ru' if lang == 'en' else 'en'
        canonical = self.abs_url(kind, ident, lang)
        alts = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (L, self.abs_url(kind, ident, L)) for L in ('en', 'ru')) + \
               '<link rel="alternate" hreflang="x-default" href="%s">' % self.abs_url(kind, ident, 'en')
        og_image = image or (self.cfg.get('og_image') or '')
        ld = {"@context": "https://schema.org", "@type": "TechArticle", "headline": title, "inLanguage": lang, "url": canonical,
              "isPartOf": {"@type": "ScholarlyArticle", "name": "Quantum Technology Atlas", "url": self.site, "identifier": "https://doi.org/" + CONCEPT_DOI},
              "author": {"@type": "Person", "name": self.cfg['author']}, "publisher": {"@type": "Organization", "name": self.cfg['publisher']},
              "license": "https://creativecommons.org/licenses/by/4.0/", "datePublished": self.cfg['date'], "description": desc}
        if og_image: ld["image"] = og_image
        if jsonld_extra: ld.update(jsonld_extra)
        nav_kinds = ' · '.join('<a href="%s%s%s/index.html">%s</a>' % (base, '' if lang == 'en' else 'ru/', k, t[KIND_T[k]]) for k in KINDS)
        head = (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{html.escape(title)} — Quantum Technology Atlas</title>\n<meta name="description" content="{html.escape(desc)}">\n'
                f'<meta name="author" content="{html.escape(self.cfg["author"])}"><meta name="citation_title" content="{html.escape(title)} — Quantum Technology Atlas"><meta name="citation_author" content="{html.escape(self.cfg["author"])}">'
                f'<meta name="citation_publication_date" content="{self.cfg["date"].replace("-", "/")}"><meta name="citation_publisher" content="{html.escape(self.cfg["publisher"])}"><meta name="citation_doi" content="{CONCEPT_DOI}"><meta name="citation_language" content="{lang}">\n'
                f'<meta property="og:type" content="article"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canonical}">'
                + (f'<meta property="og:image" content="{html.escape(og_image)}">' if og_image else '') +
                f'<meta name="twitter:card" content="summary_large_image">\n<link rel="canonical" href="{canonical}">{alts}<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">\n'
                f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Golos+Text:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">'
                f'<link rel="stylesheet" href="{base}assets/atlas.css"><link rel="stylesheet" href="{base}assets/cards.css"><link rel="stylesheet" href="{base}assets/record.css">'
                f'<meta name="color-scheme" content="light dark"><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head>\n')
        twin_link = f'<a class="rb-lang" href="{self.href(kind, ident, other, lang)}" hreflang="{other}">{t["lang"]}</a>' if twin else ''
        bar = (f'<div class="recbar"><a class="rb-home" href="{base}{"" if lang == "en" else "ru/"}{os.path.basename(self.cfg["out_full"])}">{t["back"]}</a>'
               f'<span class="rb-kinds">{nav_kinds}</span><span class="rb-sp"></span>{twin_link}</div>')
        foot = (f'<footer class="recfoot"><p><b>{t["cite"]}.</b> {html.escape(self.cfg["author"])} (2026). <i>Quantum Technology Atlas</i>. {html.escape(self.cfg["publisher"])}. '
                f'<a href="https://doi.org/{CONCEPT_DOI}">https://doi.org/{CONCEPT_DOI}</a> — {t["edition"]} {self.edition} · <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">{t["licence"]}</a> · '
                f'<a href="{REPO}">GitHub</a></p></footer>')
        page = head + f'<body class="record record-{kind}"><div id="app" data-lang="{lang}" data-page-lang="{lang}" data-edition="{self.edition}">{bar}<main class="recmain">{body}</main>{foot}</div>' \
               f'<script src="{base}assets/tips.js"></script><script>{self.gtip_js}</script><script>{self.tag_js}</script></body></html>'
        return self.fix_links(page, lang)

    def fix_links(self, page, lang):
        """a fragment link whose target is not on this page goes to the main page's anchor; buttons of the brief become links"""
        base = self.rel(lang); main = base + ('' if lang == 'en' else 'ru/') + os.path.basename(self.cfg['out_full'])
        ids = set(re.findall(r'\sid="([^"]+)"', page))
        def sub(m):
            frag = m.group(1)
            if frag in ids or frag == '': return m.group(0)
            return 'href="%s#%s"' % (main, frag)
        page = re.sub(r'href="#([^"]*)"', sub, page)
        return page

    # ---------- pieces
    def gallery(self, key, lang, n=3):
        base = self.rel(lang); g = media.gallery_html(key, lang, base, n=n)
        t = T[lang]
        if not g: return ''
        return f'<section class="pictures"><h3>{t["pictures"]}</h3><p class="empty">{t["story_note"]}</p>{g}</section>'

    def first_image(self, key):
        for a in media.pick(key, n=1):
            if a.get('thumb'): return self.site + 'media/' + a['thumb']
        return None

    # ---------- technology pages
    def technology(self, lang):
        t = T[lang]; base = self.rel(lang)
        order = [b['id'] for b in self.B]
        for i, b in enumerate(self.B):
            nid = b['id']; n = self.node[nid]
            prev_id = order[i - 1] if i else ''; next_id = order[i + 1] if i + 1 < len(order) else ''
            card = cards.station_card_html(nid, lang, base)
            brief = self.BR._one_lang(b, lang, self.md2html, prev_id, next_id, self.colours.get(nid, 'var(--mid)'))
            # the brief's own controls become links: prev/next → the neighbouring technology pages, close → the index, "station on the map" → the map
            brief = re.sub(r'<button type="button" class="chip" data-brief="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s">%s</a>' % (self.href('technology', m.group(1), lang), m.group(2)), brief)
            brief = re.sub(r'<button type="button" class="chip bclose" data-briefclose="1">[^<]*</button>', '', brief)
            brief = re.sub(r'<button type="button" class="chip" data-briefclose="1">[^<]*</button>', '', brief)
            mainp = base + ('' if lang == 'en' else 'ru/') + os.path.basename(self.cfg['out_full'])
            brief = re.sub(r'<button type="button" class="chip" data-mapstation="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s#station-%s">%s</a>' % (mainp, m.group(1), m.group(2)), brief)
            brief = re.sub(r'<button type="button" class="chip" data-tablerow="(\w+)">([^<]*)</button>', lambda m: '<a class="chip" href="%s#%s-s7-2">%s</a>' % (mainp, lang, m.group(2)), brief)
            brief = re.sub(r'<a class="chip" href="#" data-goto="(\w+)"([^>]*)>', lambda m: '<a class="chip" href="%s#station-%s"%s>' % (mainp, m.group(1), m.group(2)), brief)
            brief = brief.replace('<div class="bl lang-%s">' % lang, '<div class="bl lang-%s" id="brief">' % lang, 1)
            pics = self.gallery('node:' + nid, lang)
            name = n[lang]; one = self.BR.inline_html(b[lang]['meta'].get('one_line', ''), self.md2html)
            desc = re.sub(r'<[^>]+>', '', one) or n['desc'][lang]
            body = f'<h1 class="rectitle">{html.escape(name)} <span class="recid">{nid}</span></h1><p class="reclead">{one}</p>{card}{pics}<section class="recbrief">{brief}</section>'
            self.write('technology', nid, lang, name, desc, body, image=self.first_image('node:' + nid))

    # ---------- machine pages
    def machine(self, lang):
        t = T[lang]; base = self.rel(lang)
        for mid, m in sorted(self.mach.items()):
            card = cards.machine_card_html(mid, lang, base)
            oslug = self.org_of.get(mid)
            orgline = (f'<p class="recorg"><a href="{self.href("organisation", oslug, lang)}">{html.escape(m["org"])}</a></p>' if oslug else f'<p class="recorg">{html.escape(m["org"])}</p>')
            pics = self.gallery('machine:' + mid, lang)
            name = m['name']; p = self.path.get(m['map_path'])
            q = m.get('physical_qubits_num')
            desc = '%s — %s; %s; %s' % (m['org'], (p.get('short') or {}).get(lang, p[lang]) if p else m['map_path'], m['status'].lower(), ('%s %s' % (q, 'qubits' if lang == 'en' else 'кубитов')) if q else '')
            body = f'<h1 class="rectitle">{html.escape(name)}</h1>{orgline}{card}{pics}'
            self.write('machine', mid, lang, name, desc.strip('; '), body, image=self.first_image('machine:' + mid))

    # ---------- architecture pages
    def architecture(self, lang):
        t = T[lang]; base = self.rel(lang); H = self.page_html[lang]; P = 'en' if lang == 'en' else 'ru'
        for k, p in enumerate(self.G['paths'], 1):
            pid = p['id']
            card = cards.architecture_card_html(pid, lang, base)
            # the §8.3.k block of the main page: from its h4 to the next h4/h3/h2
            m = re.search(r'<h4 id="%s-s8-3-%d"[^>]*>.*?</h4>' % (P, k), H, flags=re.S)
            narr = ''
            if m:
                j = re.search(r'<h[234] id="%s-s8' % P, H[m.end():])
                block = H[m.start():(m.end() + j.start()) if j else m.end() + 200000]
                block = re.sub(r'<button type="button" class="foldbtn"[^>]*></button>', '', block)
                narr = f'<section class="recnarr"><h2>{t["narrative"]}</h2>{block}</section>'
            name = (p.get('short') or {}).get(lang) or p[lang]
            desc = '%s — %s' % (p[lang], p.get('actors', ''))
            body = f'<h1 class="rectitle">{html.escape(name)} <span class="recid">{html.escape(p[lang])}</span></h1>{card}{narr}'
            self.write('architecture', pid, lang, name, desc[:300], body)

    # ---------- organisation pages
    def organisation(self, lang):
        t = T[lang]; base = self.rel(lang)
        for o in self.orgs:
            prof = re.sub(r'<h2>.*?</h2>', '', orgs.profile_html(o, lang, base, self.mach, self.node, self.path), count=1)   # the page's h1 carries the name
            pics = ''.join(media.gallery_html('machine:' + mid, lang, base, n=1) for mid in o.get('machines', [])[:6])
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
        t = T[lang]; base = self.rel(lang)
        # technologies by layer
        rows = []
        for l in self.G['layers']:
            items = [n for n in self.G['nodes'] if n['layer'] == l['n']]
            rows.append('<h3>%d · %s</h3><ul>%s</ul>' % (l['n'], html.escape(l[lang]), ''.join('<li><a href="%s">%s</a> <code>%s</code> — %s</li>' % (self.href('technology', n['id'], lang), html.escape(n[lang]), n['id'], html.escape(n['desc'][lang][:160])) for n in items)))
        self.write('technology', 'index', lang, t['tech'], t['tech'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["tech"]} · {len(self.G["nodes"])}</h1>' + ''.join(rows), twin=True)
        # machines by family then name
        fams = {}
        for m in self.mach.values(): fams.setdefault(m['family'], []).append(m)
        rows = []
        for f, ms in sorted(fams.items(), key=lambda kv: -len(kv[1])):
            rows.append('<h3>%s · %d</h3><ul>%s</ul>' % (html.escape(f), len(ms), ''.join('<li><a href="%s">%s</a> — %s; %s%s</li>' % (self.href('machine', m['id'], lang), html.escape(m['name']), html.escape(m['org']), html.escape(m['status'].lower()), (', %s q' % m['physical_qubits_num']) if m.get('physical_qubits_num') else '') for m in sorted(ms, key=lambda m: m['name']))))
        self.write('machine', 'index', lang, t['mach'], t['mach'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["mach"]} · {len(self.mach)}</h1>' + ''.join(rows))
        rows = ''.join('<li><a href="%s">%s</a> — %s</li>' % (self.href('architecture', p['id'], lang), html.escape((p.get('short') or {}).get(lang) or p[lang]), html.escape(p[lang])) for p in self.G['paths'])
        self.write('architecture', 'index', lang, t['arch'], t['arch'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["arch"]} · {len(self.G["paths"])}</h1><ul>{rows}</ul>')
        rows = ''.join('<li><a href="%s">%s</a> — %s%s</li>' % (self.href('organisation', o['slug'], lang), html.escape(o['name']), html.escape(o.get('country', '') or ''), (' · %d %s' % (len(o['machines']), t['mach'].lower())) if o.get('machines') else '') for o in self.orgs)
        self.write('organisation', 'index', lang, t['org'], t['org'] + ' — Quantum Technology Atlas', f'<h1 class="rectitle">{t["org"]} · {len(self.orgs)}</h1><ul>{rows}</ul>')

    def sitemap(self):
        main = [(self.site, 'en'), (self.site + 'ru/', 'ru')]
        urls = []
        def entry(loc, alts):
            a = ''.join('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (L, u) for L, u in alts)
            return '<url><loc>%s</loc>%s<lastmod>%s</lastmod></url>' % (loc, a, self.cfg['date'])
        urls.append(entry(self.site, [('en', self.site), ('ru', self.site + 'ru/'), ('x-default', self.site)]))
        urls.append(entry(self.site + 'ru/', [('en', self.site), ('ru', self.site + 'ru/'), ('x-default', self.site)]))
        seen = set()
        for lang, kind, ident in self.urls:
            loc = self.abs_url(kind, ident, lang)
            urls.append(entry(loc, [('en', self.abs_url(kind, ident, 'en')), ('ru', self.abs_url(kind, ident, 'ru')), ('x-default', self.abs_url(kind, ident, 'en'))]))
        sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n'
        open(os.path.join(self.dist, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(sm)

    # ---------- write
    def write(self, kind, ident, lang, title, desc, body, image=None, twin=True):
        page = self.shell(kind, ident, lang, title, desc, body, image=image, twin=twin)
        p = self.out_path(kind, ident, lang); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8', newline='\n').write(page); self.written += 1
        self.urls.append((lang, kind, ident))

    def assets(self):
        d = os.path.join(self.dist, 'assets'); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'atlas.css'), 'w', encoding='utf-8', newline='\n').write(self.CSS)
        open(os.path.join(d, 'cards.css'), 'w', encoding='utf-8', newline='\n').write(cards_css(self.CSS))
        open(os.path.join(d, 'record.css'), 'w', encoding='utf-8', newline='\n').write(RECORD_CSS)
        open(os.path.join(d, 'tips.js'), 'w', encoding='utf-8', newline='\n').write('window.__TIPS=%s;\n' % self.tips)   # the hints' texts, one shared file
        open(os.path.join(self.dist, 'media-files.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(media.hosted_files()) + '\n')

    def build(self, langs=('en', 'ru')):
        self.assets()
        for lang in langs:
            self.technology(lang); self.machine(lang); self.architecture(lang); self.organisation(lang); self.indexes(lang)
        self.sitemap()
        return self.written


RECORD_CSS = """
/* record pages (27 Sep 2026): one record per page, the map's card rendered statically, the brief or the narrative below */
body.record{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "Golos Text",system-ui,sans-serif}
.recbar{display:flex;gap:14px;align-items:center;flex-wrap:wrap;padding:10px 20px;border-bottom:1px solid var(--line);font-size:14px;position:sticky;top:0;background:var(--bg);z-index:5}
.recbar .rb-home{font-weight:600;text-decoration:none;color:var(--ink)} .recbar .rb-kinds a{margin-right:2px} .recbar .rb-sp{flex:1} .recbar .rb-lang{text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:2px 10px}
.recmain{max-width:1080px;margin:0 auto;padding:18px 20px 60px}
.rectitle{font:700 30px/1.15 "Unbounded","Golos Text",sans-serif;margin:14px 0 6px} .rectitle .recid{font:500 13px "JetBrains Mono",monospace;color:var(--ink2);margin-left:10px;vertical-align:middle}
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
