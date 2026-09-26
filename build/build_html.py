# -*- coding: utf-8 -*-
import re, json, sys, html
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'build')); sys.path.insert(0,os.path.join(ROOT,'data'))
import markdown
import html as html_mod
import json, os
from page_css import CSS
from map_js import JS
from brief_js import BRIEF_JS
from labels import SHORT
# shared tooltip for .tt terms: hover, keyboard focus or a tap shows the explanation below the term, kept inside the viewport
GTIP_JS=r"""(function(){var tip=document.createElement('div');tip.id='gtip';tip.hidden=true;tip.setAttribute('role','tooltip');document.body.appendChild(tip);var cur=null,pinned=false,timer=null;
function textOf(el){var t=el.getAttribute('data-tip');if(t)return t;var L=(document.getElementById('app')||{getAttribute:function(){return 'en';}}).getAttribute('data-lang')||'en';var D=(window.__TIPS||{});return (D[L]||{})[el.getAttribute('data-t')]||(D.en||{})[el.getAttribute('data-t')]||'';}
function place(el){var r=el.getBoundingClientRect(),sx=window.scrollX,sy=window.scrollY,vw=document.documentElement.clientWidth;tip.style.left='0px';tip.style.top='0px';var w=tip.offsetWidth,h=tip.offsetHeight;var x=r.left+sx,y=r.bottom+sy+6;if(x+w>sx+vw-12)x=Math.max(sx+12,sx+vw-12-w);if(r.bottom+6+h>window.innerHeight&&r.top-6-h>0)y=r.top+sy-6-h;tip.style.left=x+'px';tip.style.top=y+'px';}
function show(el,pin){var t=textOf(el);if(!t)return;if(timer){clearTimeout(timer);timer=null;}cur=el;tip.textContent=t;tip.hidden=false;tip.classList.toggle('pinned',!!pin);place(el);}
function hide(){if(timer){clearTimeout(timer);timer=null;}tip.hidden=true;tip.classList.remove('pinned');cur=null;pinned=false;}
function later(){if(pinned)return;if(timer)clearTimeout(timer);timer=setTimeout(function(){if(!pinned)hide();},220);}   /* a short grace so the pointer can travel into the tip and select its text */
document.addEventListener('mouseover',function(ev){var el=ev.target.closest&&ev.target.closest('.tt');if(el){if(el!==cur&&!pinned)show(el,false);else if(el===cur&&timer){clearTimeout(timer);timer=null;}return;}if(tip.contains(ev.target)&&timer){clearTimeout(timer);timer=null;}});
document.addEventListener('mouseout',function(ev){var to=ev.relatedTarget;var el=ev.target.closest&&ev.target.closest('.tt');if((el&&el===cur)||tip.contains(ev.target)){if(to&&(tip.contains(to)||(cur&&cur.contains(to))))return;later();}});
document.addEventListener('click',function(ev){if(tip.contains(ev.target))return;var el=ev.target.closest&&ev.target.closest('.tt');if(!el){if(cur)hide();return;}if(cur===el&&pinned){hide();}else{pinned=true;show(el,true);}});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')hide();});
window.addEventListener('scroll',function(){if(cur&&!tip.hidden)place(cur);},{passive:true});})();"""
from editions import EDITIONS, editions_html, CONCEPT_DOI, REPO, SITE, STATUS
import briefs as BR
G=json.load(open(os.path.join(ROOT,'data','graph.json'),encoding='utf-8'))
# ---------- machines on the Map (C2): a slim, deterministic copy of data/machines.json for the page (window.__MACH)
MACH_PATH=os.path.join(ROOT,'data','machines.json')
MACH_URLS={'register':'https://claude.ai/artifact/Bfj8NrxCsx8PMdxUCBMBhV#m-','tech':'https://claude.ai/artifact/2EcsTbo9kjAHseEnBxzawp#node-'}
MACH_FAMILIES=['SC','ION','ATOM','PHOTON','SPIN','DEFECT','TOPO','ANNEAL']
def mach_slim():
    """Per machine: id, name, org, family, path, status, status_date, q, layers {L:[[node,role,summary,ev_type,ev_url,ev_locator,verified],…]}
    (gap cells — node ids starting with ∅, not graph nodes — are left out of `layers`, listed by id in `gaps` {L:[id,…]} and counted in `ev`),
    ev [verified,total]; plus by_node restricted to graph nodes. Field order fixed, so the same input gives identical bytes."""
    if not os.path.exists(MACH_PATH): return {'machines':[],'by_node':{},'families':MACH_FAMILIES,'urls':MACH_URLS}
    M=json.load(open(MACH_PATH,encoding='utf-8'))
    out=[]
    for m in M['machines']:
        layers={}; gaps={}
        for L in [str(i) for i in range(1,11)]:
            cells=[]
            for c in m.get('layers',{}).get(L,[]):
                if str(c['node']).startswith('∅'): gaps.setdefault(L,[]).append(c['node']); continue
                e=c.get('evidence') or {}
                cells.append([c['node'],c.get('role',''),c.get('summary',''),e.get('type',''),e.get('url',''),e.get('locator',''),bool(e.get('verified'))])
            if cells: layers[L]=cells
        ec=m.get('evidence_counts') or {}
        out.append({'id':m['id'],'name':m['name'],'org':m['org'],'family':m['family'],'path':m['map_path'],'status':m['status'],'status_date':m['status_date'],
                    'q':m.get('physical_qubits_num'),'layers':layers,'gaps':gaps,'ev':[ec.get('verified',0),ec.get('total',0)],
                    'refs':[[r['kind'],r['url'],r['title']] for r in (m.get('refs') or [])[:3]]})   # up to three attribution-verified links per machine
    by_node={k:{'primary':list(v.get('primary',[])),'alternate':list(v.get('alternate',[]))} for k,v in M['by_node'].items() if not str(k).startswith('∅')}
    return {'machines':out,'by_node':by_node,'families':MACH_FAMILIES,'urls':MACH_URLS}

# ---------- math: $...$ → HTML
GREEK={'Lambda':'Λ','lambda':'λ','mu':'µ','varepsilon':'ε','epsilon':'ε','kappa':'κ','alpha':'α','beta':'β','gamma':'γ','delta':'δ','Delta':'Δ','eta':'η','theta':'θ','sigma':'σ','pi':'π','tau':'τ','omega':'ω','Omega':'Ω','rho':'ρ','phi':'φ','chi':'χ','psi':'ψ','nu':'ν'}
SYM={'times':'×','sim':'∼','approx':'≈','le':'≤','ge':'≥','leq':'≤','geq':'≥','ll':'≪','gg':'≫','pm':'±','to':'→','rightarrow':'→','infty':'∞','propto':'∝','cdot':'·','diamond':'◇','rangle':'⟩','langle':'⟨','lvert':'|','rvert':'|','ast':'∗','circ':'∘','neq':'≠','ne':'≠','sqrt':'√','in':'∈','cup':'∪','cap':'∩','dots':'…','ldots':'…'}
def tex(s):
    s=s.replace('\\,',' ').replace('\\ ',' ').replace('\\;',' ')
    s=s.replace('\\%','%').replace('\\$','$').replace('\\_','_').replace('\\&','&amp;').replace('\\hbar','ℏ')   # escaped literals and ℏ
    s=re.sub(r'\\bar\s*([a-zA-Z])',lambda m:m.group(1)+'\u0304',s)
    s=re.sub(r'\\sqrt\{([^}]*)\}',lambda m:'√<span style="text-decoration:overline">'+m.group(1)+'</span>',s)
    s=re.sub(r'\\(text|mathrm)\{([^}]*)\}',lambda m:m.group(2),s)
    # sub/sup with braces or single char
    for _ in range(3):
        s=re.sub(r'\^\{([^{}]*)\}',lambda m:'<sup>'+m.group(1)+'</sup>',s)
        s=re.sub(r'_\{([^{}]*)\}',lambda m:'<sub>'+m.group(1)+'</sub>',s)
    s=re.sub(r'\^([A-Za-z0-9\-+])',lambda m:'<sup>'+m.group(1)+'</sup>',s)
    s=re.sub(r'_([A-Za-z0-9])',lambda m:'<sub>'+m.group(1)+'</sub>',s)
    s=re.sub(r'\\([A-Za-z]+)',lambda m:GREEK.get(m.group(1),SYM.get(m.group(1),m.group(0))),s)
    s=s.replace('{','').replace('}','')
    # `.m` is white-space:nowrap so a short formula never breaks. A few `$…$` runs in the reports are
    # long prose (currency amounts pair up into a false math span), and a nowrap span of that length
    # pushes the whole document sideways — mark those `long` so the stylesheet lets them wrap.
    s=s.replace('|','&#124;')   # a bar from \lvert inside a markdown table cell would split the cell
    plain=re.sub('<[^>]+>','',s)
    cls='m long' if len(plain)>50 else 'm'
    return '<span class="'+cls+'">'+s+'</span>'
# a math span opens at a `$` that is not a currency sign ("$10 B", "$1/qubit", "$14–17.6 B", "$/qubit") and closes at the next `$`;
# before 21 Sep 2026 a currency sign on the same line paired with the next formula's opener and swallowed the prose between
MATH=re.compile(r'(?<!\\)\$(?!\d[\d,.]*(?:\s|[BMk]\b|/|–|-|\)|$))(?!/)([^$\n]+?)(?<!\\)\$')
def premath(md):
    md=re.sub(r'\$\$(.+?)\$\$',lambda m:'<div class="m">'+tex(m.group(1))+'</div>',md,flags=re.S)
    md=MATH.sub(lambda m:tex(m.group(1)),md)
    return md.replace('\\$','$').replace('\\%','%')     # literal dollars and percents outside math

# ---------- markdown → html + structure
def convert(md,lang):
    P=lang+'-'
    md=premath(md)
    h=markdown.markdown(md,extensions=['tables','sane_lists'])
    # wrap tables
    h=re.sub(r'<table>',r'<div class="tbl"><table>',h); h=h.replace('</table>','</table></div>')
    # headings: ids and numbering
    # heading ids follow the printed section number (en-s7, en-s7-2), so they survive an inserted chapter and can be linked to;
    # the two unnumbered h2 are the subtitle (stripped below) and "About the map" (id en-s-about). Before 20 Sep 2026 the ids
    # carried a running counter that shifted whenever a heading was added, which broke every hard-coded anchor.
    toc=[]; k=0; j=0
    def h2(m):
        nonlocal k,j; k+=1; j=0; txt=m.group(1); mm=re.match(r'(\d+)\.\s+(.*)',txt)
        num,title=(mm.group(1),mm.group(2)) if mm else ('',txt)
        hid=f'{P}s{num}' if num else (f'{P}s-subtitle' if k==1 else f'{P}s-about')
        toc.append((hid,num,re.sub('<[^>]+>','',title),2))
        return f'<h2 id="{hid}">'+(f'<span class="num">{num}</span>' if num else '')+f'{title}</h2>'
    def h3(m):
        nonlocal k,j; j+=1; txt=m.group(1); mm=re.match(r'(\d+)\.(\d+)\s+(.*)',txt)
        num,title=(mm.group(1)+'.'+mm.group(2),mm.group(3)) if mm else ('',txt)
        hid=f'{P}s{mm.group(1)}-{mm.group(2)}' if mm else f'{P}s-x{j}'
        toc.append((hid,num,re.sub('<[^>]+>','',title),3))
        return f'<h3 id="{hid}">{txt}</h3>'
    h=re.sub(r'<h2>(.*?)</h2>',h2,h); h=re.sub(r'<h3>(.*?)</h3>',h3,h)
    # the first h2 (subtitle line) is actually the subtitle: strip the first h1/h2 pair
    h=re.sub(r'<h1>.*?</h1>\s*','',h,count=1,flags=re.S)
    h=re.sub(r'<h2 id="'+P+r's-subtitle">.*?</h2>\s*','',h,count=1,flags=re.S); toc=[t for t in toc if t[0]!=P+'s-subtitle']
    # fold big tables in §8 (node table, edge lists) and §9 sources
    def fold(h,heading_regex,label):
        m=re.search(heading_regex,h)
        if not m: return h
        start=m.end(); t=h.find('<div class="tbl">',start); e=h.find('</div>',t)+6
        return h[:t]+f'<details class="fold big-table"><summary>{label}</summary>'+h[t:e]+'</details>'+h[e:]
    # target the headings by their printed number: the h3 ids carry a running counter, so id-based matching folded §1.2 and §3.1 instead of §7.2 and §7.11 (found 17 Sep 2026)
    h=fold(h,r'<h3 id="[^"]+">7\.2 [^<]*</h3>','Show table · Показать таблицу' if lang=='en' else 'Показать таблицу · Show table')
    h=fold(h,r'<h3 id="[^"]+">7\.11 [^<]*</h3>','Show records · Показать рекорды' if lang=='en' else 'Показать рекорды · Show records')
    for lbl in (['<strong>requires / provides</strong>','<strong>alternatives (within layer)</strong>','<strong>conflicts</strong>','<strong>transfers (node → additional platform paths)</strong>','<strong>defines (node → output; every row carries a source, a date and a number)</strong>'] if lang=='en' else
                ['<strong>требует / обеспечивает</strong>','<strong>альтернативы (внутри слоя)</strong>','<strong>конфликтует</strong>','<strong>переносится (узел → дополнительные платформенные пути)</strong>','<strong>определяет (узел → выход; каждая строка несёт источник, дату и число)</strong>']):
        h=fold(h,re.escape(lbl),re.sub('<[^>]+>','',lbl))
    h=polish(h,lang)
    h=re.sub(r'(<h2 id="'+P+r's0">.*?</h2>\s*(?:<p>.*?</p>\s*)*)<ol>',lambda m:m.group(1)+'<ol class="es">',h,count=1,flags=re.S)   # the executive summary's list is justified
    return h,toc

# ---------- reader-facing polish (21 Sep 2026, the editor's review): labelled lists, definition-style items, and every
# reference made clickable — source codes [S1] to their entry in §9, §x.y to the heading, Figure/Table x.y to the figure or the
# section, hypotheses H1–H8 and forecast rows F1a–F6 to their anchors in §8. Text nodes only: never inside links, code, headings,
# scripts or SVG.
SKIP_TAGS={'a','code','pre','script','style','h1','h2','h3','nav','svg','title','summary'}
def map_text(h,fn):
    """apply fn to the text nodes of h that lie outside SKIP_TAGS elements and outside any element carrying data-nohint"""
    out=[]; stack=[]   # (tag name, skipping?)
    for tok in re.split(r'(<[^>]+>)',h):
        if tok.startswith('<'):
            out.append(tok); m=re.match(r'<(/?)([a-zA-Z0-9]+)',tok)
            if m and not tok.endswith('/>'):
                closing,name=m.group(1),m.group(2).lower()
                if closing:
                    for k in range(len(stack)-1,-1,-1):
                        if stack[k][0]==name: del stack[k]; break
                else: stack.append((name,name in SKIP_TAGS or 'data-nohint' in tok))
        else: out.append(tok if any(f for _,f in stack) else fn(tok))
    return ''.join(out)
# paragraphs that themselves define terms carry no hints (the definition is the text); the "Why" paragraph of About is narrative
NOHINT_OPENERS=['Terms used in this chapter','Термины этой главы','Two scores are given where they differ','Там, где оценки расходятся',
                'Legend:','Легенда:','Nodes are technologies, not platforms','Узлы — технологии, а не платформы','Seven attributes per node','Семь атрибутов узла','Five edge types','Пять типов рёбер',
                'Clock is not an attribute','Такт — не атрибут','Off-diagonal test','Тест на off-diagonal','Validity criterion','Критерий валидности']
def mark_nohint(h):
    def rep(m):
        plain=html_mod.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()
        return m.group(0) if not any(plain.startswith(o) for o in NOHINT_OPENERS) else '<p data-nohint="1"'+m.group(1)+'>'+m.group(2)+'</p>'
    return re.sub(r'<p((?: [^>]*)?)>(.*?)</p>',rep,h,flags=re.S)
CITE=re.compile(r'\[([A-Z]{1,2}\d{1,3})\]')
CITE_RUN=re.compile(r'\[[A-Z]{1,2}\d{1,3}\](?:(?:,?\s?|\s?[–-]\s?)\[[A-Z]{1,2}\d{1,3}\])*')   # [S3][S4], [S3], [S4], [X1]–[X4]
REFS=None
def refs():
    """The canonical bibliography (build/sources.py): codes → works, IEEE numbers by first citation in the English text."""
    global REFS
    if REFS is None:
        import sources
        REFS=sources.build()
    return REFS
def expand_codes(run):
    """the codes of a citation run; a range of codes [X1]–[X4] expands to X1, X2, X3, X4"""
    out=[]
    for m in re.finditer(r'\[([A-Z]{1,2})(\d{1,3})\](\s?[–-]\s?\[([A-Z]{1,2})(\d{1,3})\])?',run):
        if m.group(3) and m.group(4)==m.group(1) and int(m.group(5))>int(m.group(2)):
            out+=[m.group(1)+str(k) for k in range(int(m.group(2)),int(m.group(5))+1)]
        else:
            out.append(m.group(1)+m.group(2))
            if m.group(3): out.append(m.group(4)+m.group(5))
    return out
def polish(h,lang):
    P=lang+'-'
    h=mark_nohint(h)
    # 1. lists: "(a) …"/"(i) …" items carry their label as a hanging tag; "**Term** — text" items put the term on its own line
    h=re.sub(r'<li>\(([a-z]|[ivx]+)\)\s',lambda m:'<li class="lbl"><span class="lb">('+m.group(1)+')</span> ',h)
    h=re.sub(r'<li>(<p>)?<strong>([^<]{3,120})</strong>\s?—\s(\S)',lambda m:'<li class="def">'+(m.group(1) or '')+'<strong>'+m.group(2)+'</strong>'+m.group(3).upper(),h)
    # 2. §9 is generated (23 Sep 2026, the editor's review): the markdown's register (code → URLs) is replaced by the IEEE list of
    #    build/sources.py — one numbered entry per work, numbered by first citation in the English text, ids by code — followed by
    #    the register's closing note(s); anchors for hypotheses and forecast rows in §8, Figure 8.1
    i9=h.find(f'<h2 id="{P}s9">'); i8=h.find(f'<h2 id="{P}s8">')
    srcs=set()
    if i9>0:
        import sources
        order,works,alias,num,_=refs()
        e=h.find('</h2>',i9)+5; body=h[e:]
        keep=[p for p in re.findall(r'<p>.*?</p>',body,flags=re.S) if not CITE.search(p) and not re.search(r'End of (?:the )?\w+ edition|Конец \w+ издания',p)]
        note=('<p class="refnote">A number stands for one work throughout the Map — here, in every technology brief and in later editions. Online sources were accessed in September 2026.</p>' if lang=='en' else
              '<p class="refnote">Номер обозначает одну работу во всей Карте — здесь, в каждом брифе по технологии и в последующих изданиях. Онлайн-источники просмотрены в сентябре 2026 г.</p>')
        h=h[:e]+'\n'+note+'\n'+sources.render_list(lang,order,works,num)+'\n'+'\n'.join(keep)+'\n'
        srcs=set(num)
    h=re.sub(r'<p><strong>(H[1-8]) — ',lambda m:f'<p id="{P}{m.group(1).lower()}"><strong>{m.group(1)} — ',h)
    h=re.sub(r'<td>(F[1-6][abc]?)</td>',lambda m:f'<td><a class="src" id="{P}{m.group(1).lower()}">{m.group(1)}</a></td>',h)   # an anchor, not a link (never self-linked)
    h=h.replace('<figure class="fig81">',f'<figure class="fig81" id="{P}fig8-1">')
    ids=set(re.findall(r' id="([^"]+)"',h))
    # 3. links in the text
    def link(t,in_ch8):
        def cite(m):
            codes=expand_codes(m.group(0))
            if not codes or not all(c in srcs for c in codes): return m.group(0)
            import sources
            order,works,alias,num,_=refs()
            return sources.cite_html(codes,lang,works,num,order)
        t=CITE_RUN.sub(cite,t)
        def sec(m):
            a,b=m.group(1),m.group(2); tid=f'{P}s{a}'+(f'-{b}' if b else '')
            return f'<a class="xref" href="#{tid}">{m.group(0)}</a>' if tid in ids else m.group(0)
        t=re.sub(r'(?<!CFR )§(\d+)(?:\.(\d+))?',sec,t)
        def figtab(m):
            word,a,b=m.group(1),m.group(2),m.group(3); low=word.lower()
            tid=f'{P}fig{a}-{b}' if low in ('figure','рисунок','рис.','fig.') else f'{P}s{a}-{b}'
            return f'<a class="xref" href="#{tid}">{m.group(0)}</a>' if tid in ids else m.group(0)
        t=re.sub(r'\b(Figure|Fig\.|Table|Рисунок|Рис\.|Таблица|табл\.)\s(\d)\.(\d+)\b',figtab,t)
        # hypotheses and forecast rows: after a §8.x reference anywhere; bare tokens only inside the chapter itself
        # (outside it, H1/H2 are half-years and Quantinuum machines)
        def hf(m):
            c=m.group(0); tid=f'{P}{c.lower()}'; return f'<a class="xref" href="#{tid}">{c}</a>' if tid in ids else c
        t=re.sub(r'(§8\.\d</a>,\s*)((?:[HF]\d[abc]?(?:,\s*|\s*(?:and|и)\s*)?)+)',lambda m:m.group(1)+re.sub(r'\b[HF]\d[abc]?\b',hf,m.group(2)),t)
        if in_ch8:
            t=re.sub(r'(?<![\w/\-–])(?<!Quantinuum )(?<!Model )([HF][1-8][abc]?)(?![\w/\-–])(?! — )',lambda m:hf(m),t)   # not the label itself ("H1 — …")
        return t
    if i8>0 and i9>i8:
        h=map_text(h[:i8],lambda t:link(t,False))+map_text(h[i8:i9],lambda t:link(t,True))+map_text(h[i9:],lambda t:link(t,False))
    else:
        h=map_text(h,lambda t:link(t,False))
    h=score_tips(h,lang)
    h=tooltips(h,lang)
    return h

# ---------- tooltips (21 Sep 2026): the map's own terms and codes, and the field's abbreviations, explained where they stand.
# data/glossary-own.json (the report's own definitions) and data/glossary-field.json (standard expansions). Codes, marks and
# goal ids get a tooltip at every occurrence; words at their first occurrence in each section (h2/h3), so a reader who lands
# anywhere finds the term explained within the section. Text nodes only; never inside links, code, headings, SVG or math.
GLOSSARY=None
def glossary():
    global GLOSSARY
    if GLOSSARY is None:
        GLOSSARY=[]
        for fn in ('glossary-own.json','glossary-field.json'):
            part=json.load(open(os.path.join(ROOT,'data',fn),encoding='utf-8'))
            for e in part: e['own']=(fn=='glossary-own.json')   # the map's own terms are hinted in the report, not in the briefs
            GLOSSARY+=part
        for e in GLOSSARY:
            if e['id'] in ('notation-lambda','notation-code-distance'): e['scope']='first'   # notation: once per section is enough
    return GLOSSARY
def tips_dict():
    d={'en':{},'ru':{}}
    for e in glossary():
        for L in ('en','ru'):
            d[L][e['id']]=e[L]
            for k,v in enumerate(e.get('variants') or []): d[L][e['id']+'@'+str(k)]=v[L]
    return d
def variant_key(e,secnum):
    # a variant applies to sections before its "until" (About and §0 count as 0): the reader has not yet met the definition
    for k,v in enumerate(e.get('variants') or []):
        try:
            if secnum<float(v.get('until','0')): return e['id']+'@'+str(k)
        except ValueError: pass
    return e['id']
def _term_re(forms):
    alts=[]
    for f in forms:
        f=f.strip()
        if not f: continue
        esc=re.escape(f)
        if f[0].isalpha() and f[0].islower(): esc='['+f[0]+f[0].upper()+']'+re.escape(f[1:])   # sentence-initial capital
        left=r'(?<![\w\-])' if f[0].isalnum() else ''; right=r'(?![\w\-])' if f[-1].isalnum() else ''
        alts.append(left+esc+right)
    return '|'.join(alts)
def tooltips(h,lang,briefs=False):
    G_=glossary(); items=[]   # (entry, own regex, alternatives)
    for e in G_:
        if briefs and e.get('own') and not e.get('briefs'): continue   # a brief is a stand-alone article: field terms and the evidence codes only
        forms=e.get('match_ru' if lang=='ru' else 'match') or []
        rx=e.get('re') if lang=='en' else e.get('re_ru')
        body=rx if rx else _term_re(forms)   # a regex replaces the plain forms (it carries the context rules)
        if not body: continue
        items.append((e,re.compile(body),body))
    # one combined regex, longer forms first so "path instance" beats "path"; the entry is identified by a full match afterwards
    items.sort(key=lambda x:-max(len(f) for f in (x[0].get('match_ru' if lang=='ru' else 'match') or ['']) ) )
    comb=re.compile('|'.join('(?:'+b+')' for _,_,b in items))
    def entry_of(txt):
        for e,rx,_ in items:
            if rx.fullmatch(txt): return e
        return None
    def process(segment):
        seen=set(); mh=re.match(r'<h[23] id="(?:en|ru)-s(\d+)(?:-(\d+))?"',segment)
        secnum=float(mh.group(1)+'.'+(mh.group(2) or '0')) if mh else 0.0
        major=str(int(secnum))
        for e,_,_ in items:                       # entries confined to some sections ("only") are marked seen elsewhere
            if e.get('only') and major not in e['only']: seen.add(e['id'])
        def wrap(e,txt): return '<span class="tt" data-t="'+variant_key(e,secnum)+'">'+txt+'</span>'   # the text comes from window.__TIPS[lang][key]
        def fn(t):
            if not t.strip(): return t
            out=[]; pos=0
            while True:
                m=comb.search(t,pos)
                while m:
                    e=entry_of(m.group(0))
                    if e and not (e['id'] in seen and (e['scope']=='first' or e.get('only'))): break
                    m=comb.search(t,m.start()+1)
                if not m: out.append(t[pos:]); break
                out.append(t[pos:m.start()]); out.append(wrap(e,m.group(0))); pos=m.end()
                if e['scope']=='first': seen.add(e['id'])
            return ''.join(out)
        return map_text(segment,fn)
    parts=re.split(r'(?=<h[23] id=")',h)
    return ''.join(process(pt) for pt in parts)
# §3.1: the axis letters and the scores explained from the §1.2 table itself (what the axis measures and its 5/3/1 anchors)
def score_tips(h,lang):
    P=lang+'-'; i12=h.find(f'<h3 id="{P}s1-2">'); i31=h.find(f'<h3 id="{P}s3-1">')
    if i12<0 or i31<0: return h
    seg=h[i12:]; tbl=seg[seg.find('<table>'):seg.find('</table>')]
    axes={}
    for row in re.findall(r'<tr>(.*?)</tr>',tbl,flags=re.S):
        cells=[html_mod.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>',row,flags=re.S)]
        if len(cells)==5 and re.match(r'[A-F]\.',cells[0]): axes[cells[0][0]]=cells
    if len(axes)!=6: return h
    en=lang=='en'
    def desc(L):
        a=axes[L]; return (f'{a[0]} — {a[1]}. Anchors: 5 = {a[2]}; 3 = {a[3]}; 1 = {a[4]}' if en else f'{a[0]} — {a[1]}. Опорные значения: 5 = {a[2]}; 3 = {a[3]}; 1 = {a[4]}')
    j=h.find('</table>',i31); t31=h[i31:j]
    def th(m):
        L=m.group(2); return m.group(1)+'<span class="tt" data-tip="'+html_mod.escape(desc(L),quote=True)+'">'+L+m.group(3)+'</span></th>'
    t31=re.sub(r'(<th[^>]*>)([A-F])( [^<]+)</th>',th,t31)
    mi=('Maturity index — the sum of the six axis scores (30 at most): how much of the fault-tolerance stack has been shown to work, not how useful the platform is' if en else
        'Индекс зрелости — сумма баллов по шести осям (не более 30): какая часть стека отказоустойчивости показана в работе, а не полезность платформы')
    t31=re.sub(r'<th([^>]*)><strong>([^<]+)</strong></th>',lambda m:'<th'+m.group(1)+'><strong><span class="tt" data-tip="'+html_mod.escape(mi,quote=True)+'">'+m.group(2)+'</span></strong></th>',t31)
    letters='ABCDEF'
    def row(m):
        cells=re.findall(r'<td[^>]*>.*?</td>',m.group(0),flags=re.S)
        if len(cells)!=8: return m.group(0)
        out=[cells[0]]
        for k,c in enumerate(cells[1:7]):
            L=letters[k]; inner=re.sub(r'^<td[^>]*>|</td>$','',c); txt=html_mod.unescape(re.sub(r'<[^>]+>','',inner)).strip()
            if re.fullmatch(r'\d',txt): tip=(f'{axes[L][0]} — {txt} of 5. Measures: ' if en else f'{axes[L][0]} — {txt} из 5. Измеряет: ')+desc(L).split(' — ',1)[1]
            elif txt.startswith('('): tip=(f'{axes[L][0]}: {txt[1:-1]} — the architecture\'s value by design, not a demonstrated one' if en else f'{axes[L][0]}: {txt[1:-1]} — значение по замыслу архитектуры, не продемонстрированное')
            elif txt=='n/a': tip=(f'{axes[L][0]}: not applicable — annealers run no gate-model error correction, so the axis has no meaning for them' if en else f'{axes[L][0]}: неприменимо — отжигатели не выполняют коррекцию ошибок гейтовой модели, ось для них не имеет смысла')
            elif txt in ('—','-'): tip=(f'{axes[L][0]}: nothing to score yet' if en else f'{axes[L][0]}: оценивать пока нечего')
            else: out.append(c); continue
            out.append(c[:c.find('>')+1]+'<span class="tt" data-tip="'+html_mod.escape(tip,quote=True)+'">'+inner+'</span></td>')
        out.append(cells[7])
        return '<tr>\n'+'\n'.join(out)+'\n</tr>'
    t31=re.sub(r'<tr>\s*<td>.*?</tr>',row,t31,flags=re.S)
    return h[:i31]+t31+h[j:]

# ---------- brief markdown (same TeX + markdown machinery, line breaks kept)
def brief_md2html(md):
    # ensure a blank line before a list that directly follows a paragraph line (CommonMark needs it)
    lines=md.split('\n'); out=[]
    for i,l in enumerate(lines):
        if re.match(r'^\s*[-*] ',l) and i>0 and lines[i-1].strip() and not re.match(r'^\s*[-*] |^\s*\d+\. |^\|',lines[i-1]):
            out.append('')
        out.append(l)
    md='\n'.join(out)
    # bare E_J / E_C style subscripts outside math → HTML subscripts
    md=re.sub(r'(?<![\w$\\`/])([A-ZΦΩ])_([A-Za-z0-9]{1,2})(?![\w{_])',lambda m:m.group(1)+'<sub>'+m.group(2)+'</sub>',md)
    return markdown.markdown(premath(md),extensions=['tables','sane_lists','nl2br'])

# insert map section after §0 (before <h2 id="en-s1">, section 1)
def insert_after_section(h,sec_id,block):
    i=h.find(f'<h2 id="{sec_id}">'); return h[:i]+block+h[i:]

# ---------- radars for §3.1
SCORES=[('Superconducting','Сверхпроводники','SC',[3,5,4,4,4,4]),('Neutral atoms','Нейтральные атомы','ATOM',[4,2,4,4,4,3]),('Trapped ions','Ионы','ION',[5,2,3,4,3,3]),('Bosonic SC','Бозонные SC','SC',[2,5,1,2,3,2]),('Spin qubits','Спиновые кубиты','SPIN',[2,3,2,2,3,3]),('Photonic','Фотоника','PHOTON',[2,4,1,1,3,2]),('Topological','Топологические','TOPO',[1,0,1,1,1,1])]
AXL=['A','B','C','D','E','F']
import math
def radar(name,fam,vals):
    cx=cy=70; R=52; pts=[]
    for i,v in enumerate(vals):
        a=-math.pi/2+i*2*math.pi/6; r=R*v/5; pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    grid=''.join(f'<polygon points="{" ".join(f"{cx+R*g/5*math.cos(-math.pi/2+i*2*math.pi/6):.1f},{cy+R*g/5*math.sin(-math.pi/2+i*2*math.pi/6):.1f}" for i in range(6))}" fill="none" stroke="var(--rule)" stroke-width="1"/>' for g in (1,2,3,4,5))
    spokes=''.join(f'<line x1="{cx}" y1="{cy}" x2="{cx+R*math.cos(-math.pi/2+i*2*math.pi/6):.1f}" y2="{cy+R*math.sin(-math.pi/2+i*2*math.pi/6):.1f}" stroke="var(--rule)"/>' for i in range(6))
    labels=''.join(f'<text x="{cx+(R+11)*math.cos(-math.pi/2+i*2*math.pi/6):.1f}" y="{cy+(R+11)*math.sin(-math.pi/2+i*2*math.pi/6)+3.5:.1f}" text-anchor="middle" font-size="10" fill="var(--muted)" font-family="JetBrains Mono,monospace">{AXL[i]}</text>' for i in range(6))
    poly=f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="var(--{fam.lower()})" fill-opacity=".28" stroke="var(--{fam.lower()})" stroke-width="2"/>'
    dots=''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4" fill="var(--{fam.lower()})"/>' for x,y in pts)
    return f'<svg viewBox="0 0 140 140" role="img" aria-label="{name} profile A–F">{grid}{spokes}{labels}{poly}{dots}</svg>'
def radars_block(lang):
    cap={'en':'Profiles by axis (A channel · B clock · C scale · D FT progress · E scaling path · F roadmap credibility). The shape is the information: superconducting is round, ions are tall on A and short on B, atoms mirror ions on C/D, bosonic and photonic are B-only spikes.','ru':'Профили по осям (A канал · B такт · C масштаб · D прогресс FT · E путь масштабирования · F правдоподобие карты). Информация — в форме: сверхпроводники круглые, ионы высокие по A и низкие по B, атомы зеркалят ионы по C/D, бозонные и фотоника — пики только по B.'}[lang]
    cards=''.join(f'<div class="radar">{radar(n if lang=="en" else r,f,v)}<div class="cap"><b>{n if lang=="en" else r}</b> · {sum(v)}</div></div>' for n,r,f,v in SCORES)
    return f'<div class="radars">{cards}</div><p class="figcap">{cap}</p>'
def insert_after_h3_table(h,h3_num,block):
    m=re.search(r'<h3 id="[^"]+">'+re.escape(h3_num)+r' ',h); t=h.find('</div>',h.find('<div class="tbl">',m.end()))+6
    return h[:t]+block+h[t:]
# sortable tables (editor's review of 17 Sep 2026, second batch, brief D): tag the nth div.tbl after the h3 numbered h3_num;
# the JS block `tblsort` in map_js.py reads data-sort (platform-default · numeric · date · centrality) and data-default="build"
SORT_TABLES=[('3.1','platform-default',1),('7.4','numeric',1),('7.5','numeric',1),('7.6','numeric',2),('7.11','date',1),('7.12','numeric',2),('8.1','numeric',1),('8.2','numeric',1),('8.3','numeric',1),('8.4','numeric',1)]
def tag_sortable(h,h3_num,kind,nth=1):
    m=re.search(r'<h3 id="[^"]+">'+re.escape(h3_num)+r' ',h)
    if not m: return h
    t=m.end()
    for _ in range(nth):
        t=h.find('<div class="tbl">',t)
        if t<0: return h
        t+=1
    t-=1
    return h[:t]+f'<div class="tbl" data-sort="{kind}" data-default="build">'+h[t+len('<div class="tbl">'):]
def tag_sortables(h):
    for num,kind,nth in SORT_TABLES: h=tag_sortable(h,num,kind,nth)
    return h

# ---------- folding (23 Sep 2026, the editor's request): every titled section and every table folds; defaults as before (open,
# except the two big tables), the reader's choices remembered per browser; a link into a folded section opens it (FOLD_JS)
FOLD_BTN=''   # the chevron buttons are made at load (FOLD_JS) from the section bodies: 1,700 buttons of markup would cost 200 KB
def fold_tables(h,lang,idprefix=''):
    """each div.tbl becomes details.tblfold (open); a bold caption paragraph just before it becomes the summary; a table the
    build already put behind a big-table fold is left alone"""
    out=[]; pos=0; k=0; pre_id=idprefix or lang
    for m in re.finditer(r'<div class="tbl"[^>]*>',h):
        s=m.start()
        if s<pos: continue
        e=h.find('</table></div>',s)
        if e<0: continue
        e+=len('</table></div>')
        pre=h[pos:s]
        if re.search(r'<details class="fold big-table">\s*<summary>(?:(?!</summary>).)*</summary>\s*$',pre,re.S):
            out.append(pre+h[s:e]); pos=e; continue
        cap=re.search(r'<p>(<strong>(?:(?!</strong>).)*</strong>)</p>\s*$',pre,re.S)
        if cap: summary=cap.group(1); pre=pre[:cap.start()]
        else: summary='<span class="tlbl">'+('table' if lang=='en' else 'таблица')+'</span>'
        tid=f'{pre_id}-tbl-{k}'; k+=1
        out.append(pre+f'<details class="tblfold" id="{tid}" data-def="1" open><summary>{summary}</summary>'+h[s:e]+'</details>'); pos=e
    out.append(h[pos:]); return ''.join(out)
def foldable(h,lang,levels=('h2','h3'),idprefix=''):
    """headings of the given levels get a chevron button; the content up to the next heading of the same or a higher level (or a
    top-level brief fold) is wrapped in div.secbody[data-sec=id]; headings without an id get one from idprefix"""
    h=fold_tables(h,lang,idprefix)
    pat=re.compile(r'<(h2|h3)((?: [^>]*)?)>(.*?)</\1>|<details class="fold bfold[^>]*>',re.S)
    out=[]; pos=0; open_lv=[]; k=0
    for m in pat.finditer(h):
        lv=m.group(1)
        if lv is None:   # a brief's own fold (sources, open items): a boundary — no section body swallows it
            out.append(h[pos:m.start()]); pos=m.start()
            while open_lv: out.append('</div>'); open_lv.pop()
            continue
        if lv not in levels: continue
        attrs=m.group(2) or ''; inner=m.group(3)
        out.append(h[pos:m.start()]); pos=m.end()
        while open_lv and open_lv[-1]>=lv: out.append('</div>'); open_lv.pop()
        idm=re.search(r' id="([^"]+)"',attrs)
        if idm: sid=idm.group(1)
        else: sid=f'{idprefix}-sec-{k}'; attrs+=f' id="{sid}"'
        k+=1
        out.append(f'<{lv}{attrs}>{inner}{FOLD_BTN.replace("{sid}",sid)}</{lv}><div class="secbody" data-sec="{sid}">'); open_lv.append(lv)
    out.append(h[pos:])
    while open_lv: out.append('</div>'); open_lv.pop()
    return ''.join(out)
TAG_JS=r"""(function(){ var T={en:{D:"[D] measured / peer-reviewed",C:"[C] company claim",R:"[R] roadmap / target",S:"[S] simulation / estimate",G:"[G] established / general fact",P:"[P] preprint / trade press"},ru:{D:"[D] измерено / рецензировано",C:"[C] заявление компании",R:"[R] дорожная карта / цель",S:"[S] симуляция / оценка",G:"[G] установленный / общий факт",P:"[P] препринт / отраслевая пресса"}};
document.addEventListener('mouseover',function(e){ var t=e.target&&e.target.closest&&e.target.closest('span.tag'); if(!t||t.title)return; var m=/(?:^|\s)tag-([DCRSGP])(?:\s|$)/.exec(t.className); if(!m)return; var L=(document.documentElement.lang||'en').slice(0,2)==='ru'?'ru':'en'; t.title=T[L][m[1]]; },true);
})();"""
FOLD_JS=r"""(function(){ var KEY='qmap.folds', closed={}; try{ closed=JSON.parse(localStorage.getItem(KEY)||'{}')||{}; }catch(e){}
document.querySelectorAll('.secbody[data-sec]').forEach(function(b){ var hd=b.previousElementSibling; if(!hd||!/^H[23]$/.test(hd.tagName)||hd.querySelector('.foldbtn'))return; var btn=document.createElement('button'); btn.type='button'; btn.className='foldbtn'; btn.dataset.sec=b.dataset.sec; btn.setAttribute('aria-expanded','true'); btn.title='collapse / expand'; hd.appendChild(btn); });
function q(sel,id){ return document.querySelector(sel+'[data-sec="'+(window.CSS&&CSS.escape?CSS.escape(id):id)+'"]'); }
function set(id,open,save){ var b=q('.secbody',id), btn=q('.foldbtn',id); if(!b)return; b.hidden=!open; if(btn){ btn.setAttribute('aria-expanded',String(open)); var hd=btn.closest('h2,h3'); if(hd)hd.classList.toggle('folded',!open); }
  if(save){ if(open)delete closed[id]; else closed[id]=1; try{ localStorage.setItem(KEY,JSON.stringify(closed)); }catch(e){} } }
document.querySelectorAll('.foldbtn[data-sec]').forEach(function(btn){ var id=btn.dataset.sec; if(closed[id])set(id,false,false);
  var hd=btn.closest('h2,h3'); if(!hd)return; hd.classList.add('foldable');
  hd.addEventListener('click',function(ev){ if(ev.target.closest('a'))return; ev.preventDefault(); var b=q('.secbody',id); if(b)set(id,b.hidden,true); }); });
function reveal(hash){ if(!hash||hash.length<2)return; var el=null; try{ el=document.getElementById(decodeURIComponent(hash.slice(1))); }catch(e){} if(!el)return;
  for(var p=el.parentElement;p;p=p.parentElement){ if(p.classList&&p.classList.contains('secbody')&&p.hidden)set(p.dataset.sec,true,false); if(p.tagName==='DETAILS'&&!p.open)p.open=true; }
  if(el.matches&&el.matches('.secbody[hidden]'))set(el.dataset.sec,true,false); }
document.addEventListener('click',function(ev){ var a=ev.target.closest&&ev.target.closest('a[href^="#"]'); if(a)reveal(a.getAttribute('href')); },true);
window.addEventListener('hashchange',function(){ reveal(location.hash); }); reveal(location.hash);
window.__revealSection=reveal; window.__setFold=set;
var TK='qmap.tfolds', tf={}; try{ tf=JSON.parse(localStorage.getItem(TK)||'{}')||{}; }catch(e){}
document.querySelectorAll('details.tblfold[id]').forEach(function(d){ var def=d.getAttribute('data-def')==='1'; if(tf[d.id]==='c')d.open=false; else if(tf[d.id]==='o')d.open=true;
  d.addEventListener('toggle',function(){ if(d.open===def)delete tf[d.id]; else tf[d.id]=d.open?'o':'c'; try{ localStorage.setItem(TK,JSON.stringify(tf)); }catch(e){} }); });
})();"""
# ---------- map section block
def map_block(lang,gsec='8'):
    en=lang=='en'
    return f'''<section class="mapsec">
<div class="maphead"><h2 class="sr-only">{'Quantum Technology Map' if en else 'Карта квантовых технологий'}</h2><button type="button" class="chip mapcol" data-mapcollapse="1" aria-expanded="true"><span class="when-open">{'▾ collapse the map' if en else '▾ свернуть карту'}</span><span class="when-closed" hidden>{'▸ expand the map' if en else '▸ развернуть карту'}</span></button></div>
</section>'''
def map_lead(gsec='7'):
    """The map's caption (23 Sep 2026, the editor's review): below the map, in both languages, with its section references linked."""
    en='Columns are the ten layers of a quantum-computing stack, from the qubit’s carrier on the left to manufacturing on the right; each column holds the technologies that fill that layer. Within a column a technology sits higher the more natural its carrier is (atoms, ions and photons at the top) and lower the more fabricated (circuits, dots and cavities at the bottom). The order is not decoration: it predicts behaviour — natural carriers are identical and long-lived but slow and optically driven, fabricated ones are fast and wired but differ from unit to unit — and most technologies of a layer follow it. A hatched station breaks the order: a platform borrowing a trait from the other side, which is the map’s test of a genuine move (§7.6). Coloured lines are the fourteen platform paths, one station per layer; a station marked ◎ is a hub — three or more qubit families depend on it (two, if the technology is young) — so a fix or a stall there reaches several platforms at once; dashed hollow stations are slots nobody has filled. Click a station for its brief, pick a lens to recolour the map by one attribute, or choose a machine to light the stations it uses; the strip below shows the seven-attribute vector of every technology. Construction rules and derived tables: §7.'
    ru='Колонки — десять слоёв стека квантового компьютера, от носителя кубита слева до производства справа; в каждой колонке — технологии, заполняющие этот слой. Внутри колонки технология стоит тем выше, чем естественнее её носитель (атомы, ионы и фотоны — вверху), и тем ниже, чем больше он изготовлен (схемы, квантовые точки и резонаторы — внизу). Этот порядок не украшение: он предсказывает поведение — естественные носители одинаковы и долгоживущи, но медленны и управляются оптически, изготовленные быстры и подключены проводами, но различаются от экземпляра к экземпляру, — и большинство технологий слоя ему следует. Заштрихованная станция порядок нарушает: платформа заимствует свойство с другой стороны — это и есть тест карты на настоящий ход (§7.6). Цветные линии — четырнадцать путей платформ, по одной станции на слой; станция со знаком ◎ — хаб: от неё зависят три семейства кубитов и более (два — если технология молода), так что исправление или заминка в ней достигает сразу нескольких платформ; пунктирные полые станции — слоты, которые никто не заполнил. Кликните станцию, чтобы открыть её бриф; выберите линзу, чтобы перекрасить карту по одному атрибуту, или машину, чтобы подсветить станции, которые она использует; лента ниже показывает вектор из семи атрибутов каждой технологии. Правила построения и выведенные таблицы — в §7.'
    def link(t,lang):
        return re.sub(r'§(\d+)(?:\.(\d+))?',lambda m:'<a class="xref" href="#%s-s%s%s">%s</a>'%(lang,m.group(1),('-'+m.group(2)) if m.group(2) else '',m.group(0)),t.replace('§7',"§"+gsec))
    return ('<div class="maplead"><details id="maplead"><summary><span class="lang-en">How to read the map</span><span class="lang-ru">Как читать карту</span></summary>'
            '<p class="lead lang-en">'+link(en,'en')+'</p><p class="lead lang-ru">'+link(ru,'ru')+'</p></details></div>')
MAPUI='''<div class="mapbar" id="mapbar">
 <div class="grp chipsrow"><button type="button" class="bartog" id="bartog" aria-expanded="true" aria-controls="mapbar" title="show or hide the map controls: paths, lens, machine, edges, zoom, legend"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="6" cy="4" r="1.9" fill="var(--surface)" stroke="currentColor" stroke-width="1.4"/><circle cx="11" cy="8" r="1.9" fill="var(--surface)" stroke="currentColor" stroke-width="1.4"/><circle cx="5" cy="12" r="1.9" fill="var(--surface)" stroke="currentColor" stroke-width="1.4"/></svg><span class="lang-en">Controls</span><span class="lang-ru">Управление</span><span class="when-open">▾</span><span class="when-closed" hidden>▸</span></button><span class="lbl lang-en">paths</span><span class="lbl lang-ru">пути</span><span class="barsum" id="barsum" hidden></span><span id="pathchips" class="grp"></span></div>
 <div class="grp"><span class="lbl lang-en">lens</span><span class="lbl lang-ru">линза</span><select id="lens" class="sel" aria-label="colour lens"></select></div>
 <div class="grp machgrp"><span class="lbl lang-en">machine</span><span class="lbl lang-ru">машина</span><select id="machine" class="sel" aria-label="machine — one more term of the lit set" title="light only the stations this machine uses (its register cell per layer); intersects with the isolated path, the focused station and the lens value"><option value="">—</option></select></div>
 <div class="grp"><span class="lbl lang-en">edges</span><span class="lbl lang-ru">рёбра</span>
  <button class="chip tog" id="tg-req" aria-pressed="false"><span class="lang-en">all requires</span><span class="lang-ru">все «требует»</span></button>
  <button class="chip tog" id="tg-rep" aria-pressed="false"><span class="lang-en">all alternatives</span><span class="lang-ru">все «альтернативы»</span></button>
  <button class="chip tog" id="tg-conf" aria-pressed="false"><span class="lang-en">all conflicts</span><span class="lang-ru">все «конфликтует»</span></button>
</div>
 <div class="grp"><button type="button" class="resetbtn" id="tg-reset" title="back to the default view: all paths, no lens value, no edges, nothing selected"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M3.5 8a4.5 4.5 0 1 0 1.3-3.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M4.2 1.9v3.2h3.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">reset map</span><span class="lang-ru">сброс карты</span></button></div>
 <div class="zoomwin"><div class="zoomctl" role="group" aria-label="map zoom"><span class="zhint lang-en">zoom</span><span class="zhint lang-ru">масштаб</span><button type="button" class="zb" id="zoom-out" aria-label="zoom out" title="zoom out (−)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><input class="zlvl" id="zoomlvl" type="text" inputmode="numeric" pattern="[0-9]*" value="100%" aria-label="zoom percent — type a number and press Enter" title="100 % = the map fitted to the width of its frame; type a percentage and press Enter; ↑/↓ = ±5"><button type="button" class="zb" id="zoom-in" aria-label="zoom in" title="zoom in (+)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h10M8 3v10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><i class="zsep"></i><button type="button" class="zb zt" id="zoom-fit" title="fit width (= 100 %)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2 8h12M2 8l3-3M2 8l3 3M14 8l-3-3M14 8l-3 3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">fit</span><span class="lang-ru">вписать</span></button><button type="button" class="zb zt" id="zoom-fith" title="fit height"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M8 2v12M8 2L5 5M8 2l3 3M8 14l-3-3M8 14l3-3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">fit</span><span class="lang-ru">вписать</span></button><i class="zsep"></i><button type="button" class="zb zt" id="zoom-top" title="align the map to the top of the window (maximum height)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 3h10M8 6v8M8 6L5 9M8 6l3 3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">top</span><span class="lang-ru">вверх</span></button><button type="button" class="zb zt" id="zoom-100" title="native size — the drawing at its designed 1,490 px width, labels at their designed size">1:1</button><i class="zsep"></i><button type="button" class="zb zt zfs" id="zoom-fs" data-mapfs="1" aria-pressed="false" title="full screen — Esc or this button to leave"><i class="fs-on"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2 6V2h4M10 2h4v4M14 10v4h-4M6 14H2v-4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">full screen</span><span class="lang-ru">весь экран</span></i><i class="fs-off" hidden><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 2v4H2M14 6h-4V2M10 14v-4h4M2 10h4v4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">leave</span><span class="lang-ru">выйти</span></i></button></div></div>
 <details class="glyphs" id="glyphlegend" open><summary><span class="lbl lang-en">legend</span><span class="lbl lang-ru">легенда</span></summary>
  <div class="glyphlist">
  <span class="gl mark" data-glyph="hub" title="a station that stations of at least two families (or one family, recently) require — where a fix or a stall propagates across platforms"><i class="lg hub">◎</i><span class="lang-en">hub</span><span class="lang-ru">хаб</span> <span class="cnt"></span></span>
  <span class="gl mark" data-glyph="offd" title="a station that takes a trait from the other side of the natural/fabricated divide (see §7.6)"><i class="lg off">⤢</i><span class="lang-en">off-diagonal</span><span class="lang-ru">внедиагональный</span> <span class="cnt"></span></span>
  <span class="gl mark" data-glyph="empty" title="a station with no demonstrated technology yet"><i class="lg emp">∅</i><span class="lang-en">empty slot</span><span class="lang-ru">пустой слот</span> <span class="cnt"></span></span>
  <span class="gl"><i class="lg ed req"></i><span class="lang-en">requires</span><span class="lang-ru">требует</span></span>
  <span class="gl"><i class="lg ed rep"></i><span class="lang-en">alternatives</span><span class="lang-ru">альтернативы</span></span>
  <span class="gl"><i class="lg ed con"></i><span class="lang-en">conflicts — hover for the reason</span><span class="lang-ru">конфликтует — причина по наведению</span></span>
  <span class="gl long"><i class="lg stn" aria-hidden="true"><svg viewBox="0 0 50 16" width="50" height="16"><rect x="0.6" y="0.6" width="21" height="14.8" rx="3.5" fill="var(--surface)" stroke="var(--ink2)" stroke-width="1.2"/><rect x="3.2" y="3.6" width="11" height="1.6" rx="0.8" fill="var(--ink)" opacity="0.8"/><rect x="3.2" y="10.8" width="4" height="2.2" rx="0.6" fill="var(--sc)"/><path d="M23.4 8H27M25.6 6.4L27.2 8L25.6 9.6" fill="none" stroke="var(--muted)" stroke-width="1"/><rect x="28.400000000000002" y="0.6" width="21" height="14.8" rx="3.5" fill="rgba(27,175,122,0.22)" stroke="var(--atom)" stroke-width="1.2"/><rect x="31.0" y="3.6" width="11" height="1.6" rx="0.8" fill="var(--ink)" opacity="0.8"/><rect x="31.0" y="10.8" width="4" height="2.2" rx="0.6" fill="var(--sc)"/><rect x="28.4" y="0.6" width="3.2" height="14.8" rx="1.4" fill="var(--atom)"/></svg></i><span class="lang-en">outline = family colour (dark: several families); with an attribute lens on (any but “Platform family”): tint + left band = the lens value (legend below)</span><span class="lang-ru">рамка = цвет семейства (тёмная: несколько семейств); при линзе по атрибуту (любой, кроме «семейства платформ»): оттенок + полоса слева = значение линзы (легенда ниже)</span></span>
  <span class="gl"><i class="lg stn" aria-hidden="true"><svg viewBox="0 0 50 16" width="50" height="16"><rect x="0.6" y="0.6" width="21" height="14.8" rx="3.5" fill="var(--surface)" stroke="var(--ink2)" stroke-width="1.2"/><rect x="3.2" y="3.6" width="11" height="1.6" rx="0.8" fill="var(--ink)" opacity="0.8"/><rect x="3.2" y="10.8" width="4" height="2.2" rx="0.6" fill="var(--sc)"/><path d="M23.4 8H27M25.6 6.4L27.2 8L25.6 9.6" fill="none" stroke="var(--muted)" stroke-width="1"/><rect x="28.400000000000002" y="0.6" width="21" height="14.8" rx="3.5" fill="var(--surface)" stroke="var(--ink)" stroke-width="2.5"/><rect x="31.0" y="3.6" width="11" height="1.6" rx="0.8" fill="var(--ink)" opacity="0.8"/><rect x="31.0" y="10.8" width="4" height="2.2" rx="0.6" fill="var(--sc)"/></svg></i><span class="lang-en">thick outline = the clicked station</span><span class="lang-ru">толстая рамка = выбранная станция</span></span>
  <span class="gl"><i class="lg badges"><b></b><b></b></i><span class="lang-en">small squares = the platform lines through the station (■ primary, □ alternate)</span><span class="lang-ru">маленькие квадраты = линии платформ через станцию (■ основная, □ альтернатива)</span></span>
  <span class="gl"><i class="lg ax">↕</i><span class="lang-en">rows natural → fabricated · columns = layers · click a station</span><span class="lang-ru">строки естественное → изготовленное · колонки — слои · клик по станции</span></span>
  <span class="gl try"><span class="lang-en">try:</span><span class="lang-ru">попробуйте:</span> <a href="#" data-goto="transmon">Transmon</a> · <a href="#" data-goto="ct_sfq">SFQ</a> · <a href="#" data-goto="ro_erasure"><span class="lang-en">Erasure check</span><span class="lang-ru">Проверка стирания</span></a></span>
  </div>
 </details>
 <div class="grp lenslegend" id="lenslegend"></div>
</div>
<div class="mapgrid"><div class="mapwrap" id="mapwrap"><div class="zoombar"></div><div class="tip" id="maptip"></div></div><aside class="insp" id="insp" hidden></aside></div>
<div class="legend">
 <span class="k"><svg viewBox="0 0 26 16"><rect x="1" y="2" width="24" height="12" rx="4" fill="var(--surface)" stroke="var(--sc)" stroke-width="1.5"/></svg><span class="lang-en">demonstrated</span><span class="lang-ru">продемонстрировано</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><rect x="1" y="2" width="24" height="12" rx="4" fill="var(--surface)" stroke="var(--mid)" stroke-width="1.5" stroke-dasharray="3 2"/></svg><span class="lang-en">emerging</span><span class="lang-ru">формируется</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><rect x="1" y="2" width="24" height="12" rx="4" fill="none" stroke="var(--mid)" stroke-width="1.5" stroke-dasharray="5 3"/></svg><span class="lang-en">empty slot ∅</span><span class="lang-ru">пустой слот ∅</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><defs><pattern id="hl" patternUnits="userSpaceOnUse" width="5" height="5" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="var(--nat)" stroke-width="1"/></pattern></defs><rect x="1" y="2" width="24" height="12" rx="4" fill="url(#hl)" stroke="var(--mid)"/></svg><span class="lang-en">off-diagonal ⤢</span><span class="lang-ru">off-diagonal ⤢</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><rect x="1" y="2" width="24" height="12" rx="4" fill="var(--surface)" stroke="var(--fab)" stroke-width="2"/><circle cx="20" cy="6" r="2.5" fill="none" stroke="var(--fab)" stroke-width="1.4"/></svg><span class="lang-en" title="A station is a hub when the platform paths that pass through it, or through the technologies that require it, belong to at least three carrier families — or to two families if the technology only reached hardware in 2023 or later (a young technology has had less time to spread).">hub ◎ — reaches ≥ 3 carrier families (≥ 2 if demonstrated since 2023)</span><span class="lang-ru" title="Станция — хаб, если пути платформ, проходящие через неё или через технологии, которым она нужна, принадлежат не менее чем трём семействам носителей — или двум, если технология дошла до железа лишь в 2023 г. или позже (молодая технология ещё не успела распространиться).">хаб ◎ — охват ≥ 3 семейств носителей (≥ 2, если показана с 2023 г.)</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><line x1="2" y1="8" x2="24" y2="8" stroke="var(--sc)" stroke-width="3" stroke-linecap="round"/></svg><span class="lang-en">platform path (primary node per layer)</span><span class="lang-ru">путь платформы (основной узел на слой)</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><line x1="2" y1="8" x2="24" y2="8" stroke="var(--sc)" stroke-width="1.2" stroke-dasharray="2 3"/></svg><span class="lang-en">alternate node in the same slot</span><span class="lang-ru">альтернативный узел в том же слоте</span></span>
 <span class="k"><svg viewBox="0 0 26 16"><rect x="4" y="6" width="7" height="4" rx="1" fill="var(--ion)"/><rect x="14" y="6" width="7" height="4" rx="1" fill="none" stroke="var(--atom)"/></svg><span class="lang-en">line badges: primary ■ / alternate □</span><span class="lang-ru">метки линий: основной ■ / альтернатива □</span></span>
</div>
{MAPLEAD}
<div class="pcwrap" id="pcwrap"><div class="pchead"><h3><span class="lang-en">Technologies across the seven attributes — a parallel-coordinates view</span><span class="lang-ru">Технологии по семи атрибутам — вид в параллельных координатах</span><button type="button" class="foldbtn" data-sec="pcwrap" aria-expanded="true" title="collapse / expand"></button></h3><div class="zoomctl pctools" role="group" aria-label="map and strip together"><button type="button" class="zb zt" id="pc-fith" aria-pressed="false" title="fit height: the map and this view together in the window; again to leave"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M8 2v12M8 2L5 5M8 2l3 3M8 14l-3-3M8 14l3-3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">fit height</span><span class="lang-ru">по высоте</span></button><button type="button" class="zb zt zfs" id="pc-fs" aria-pressed="false" title="full screen: the map and this view together — Esc or this button to leave"><i class="fs-on"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2 6V2h4M10 2h4v4M14 10v4h-4M6 14H2v-4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">full screen</span><span class="lang-ru">весь экран</span></i><i class="fs-off" hidden><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 2v4H2M14 6h-4V2M10 14v-4h4M2 10h4v4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">leave</span><span class="lang-ru">выйти</span></i></button></div></div>
<div class="secbody" data-sec="pcwrap">
<details class="pclead" id="pclead" open><summary><span class="lang-en">How to read this view</span><span class="lang-ru">Как читать этот вид</span></summary>
<p class="lang-en">Each polyline is one technology (a station of the map, a node of the graph — the three words name the same thing in its three homes: the field, the map, the data); the vertical axes are its seven design attributes (a)–(g) of §7.1. Hover to name a line — its station lights on the map, and a hovered station lights its line; click a line to select the station. The axes are the map's lenses: click an axis title to colour the map by that attribute (a second click clears the chosen values), click a value on an axis to keep only the technologies with it (Ctrl-click adds a value); the lit, dimmed and dashed lines follow the map's selection. Bundles reveal the diagonal (natural carriers run through optical control and transport; fabricated ones through microwave/electrical control and static wiring); lines that cross the bundles are the off-diagonal technologies.</p>
<p class="lang-ru">Каждая ломаная — одна технология (станция карты, узел графа — три слова называют одно и то же в трёх его домах: отрасли, карте, данных); вертикальные оси — её семь атрибутов проектирования (a)–(g) из §7.1. Наведите на линию, чтобы назвать её — её станция подсветится на карте, а наведение на станцию подсвечивает её линию; клик по линии выбирает станцию. Оси — это линзы карты: клик по заголовку оси раскрашивает карту по этому атрибуту (повторный клик снимает выбранные значения), клик по значению на оси оставляет только технологии с этим значением (Ctrl-клик добавляет значение); подсвеченные, приглушённые и пунктирные линии следуют выбору на карте. Пучки показывают диагональ (естественные носители идут через оптическое управление и транспорт; изготовленные — через СВЧ/электрическое управление и статическую разводку); линии, пересекающие пучки, — off-diagonal технологии.</p>
</details>
<div id="pc"></div></div></div>'''
# assemble content with both languages
def toc_html(toc,lang,gsec='8'):
    def li(i,num,t,lvl):
        sty=' style="padding-left:14px;font-size:12.5px"' if lvl==3 else ''
        return '<li'+sty+'><a href="#'+i+'"><span class="n">'+num+'</span><span>'+html.escape(t)+'</span></a></li>'
    subs=(gsec+'.',str(int(gsec)+1)+'.')   # level-3 entries for the graph section and the machines chapter that follows it
    items=''.join(li(i,num,t,lvl) for i,num,t,lvl in toc if lvl==2 or num.startswith(subs))
    return f'<ol><li class="mapl"><a href="#map"><span class="n">◎</span><span>{"Technology map" if lang=="en" else "Карта технологий"}</span></a></li>{items}</ol>'
# find split point: before <h2 id="s3"> in each
def split_after_s2(h,lang):
    i=h.find(f'<h2 id="{lang}-s1">'); return h[:i],h[i:]   # the map block goes in before section 1
def split_before_num(h,toc,num):
    """Split a body just before the level-2 heading numbered <num> (e.g. '9. Sources')."""
    sid=next((t[0] for t in toc if t[3]==2 and t[1]==num),None)
    if sid is None: return h,''
    i=h.find(f'<h2 id="{sid}">')
    return (h,'') if i<0 else (h[:i],h[i:])
def toc_with_briefs(toc,lang,snum='9'):
    """Insert the Technology-briefs entry before the sources section."""
    out=list(toc); entry=('briefs','◈',BR.SECTION_TITLE[lang],2)
    for k,t in enumerate(out):
        if t[3]==2 and t[1]==snum:
            out.insert(k,entry); return out
    out.append(entry); return out

PUBLIC=dict(mode='public',
    report_en=os.path.join(ROOT,'report','report_EN.md'), report_ru=os.path.join(ROOT,'report','report_RU.md'),
    out_body=os.path.join(ROOT,'dist','body.html'), out_full=os.path.join(ROOT,'dist','Quantum-Technology-Map-%s.html'%EDITIONS[0]['edition']),
    title='Quantum Technology Map', default_lang='en', graph_sec='7', sources_num='9', table_num='7.2', id_sections=('7.2','7.5','7.6','7.7'),
    briefs_en=os.path.join(ROOT,'briefs','en'), briefs_ru=os.path.join(ROOT,'briefs','ru'), regmap=os.path.join(ROOT,'data','facts.json'),
    doi_concept=CONCEPT_DOI, doi_version=EDITIONS[0]['doi'], author='Raveh Neeman', publisher='Qodeh', url=SITE, repo=REPO, date=EDITIONS[0]['date'], edition=EDITIONS[0]['edition'])

def navchrome(cfg):
    dl=cfg['default_lang']
    en='true' if dl=='en' else 'false'; ru='true' if dl=='ru' else 'false'
    return f'''<div class="mobilebar" id="mobilebar">
 <button type="button" class="mb-btn" id="tocopen" aria-expanded="false" aria-controls="tocdrawer"><span class="lang-en">Contents ☰</span><span class="lang-ru">Содержание ☰</span></button>
 <a class="mb-btn" href="#map"><span class="lang-en">Map</span><span class="lang-ru">Карта</span></a>
 <span class="mb-sp"></span>
 <div class="seg mb-seg" role="group" aria-label="language"><button type="button" data-setlang="en" aria-pressed="{en}">EN</button><button type="button" data-setlang="ru" aria-pressed="{ru}">RU</button></div>
</div>
<div class="tocbackdrop" id="tocbackdrop" hidden></div>
<aside class="tocdrawer" id="tocdrawer" hidden role="dialog" aria-modal="true" aria-label="contents">
 <div class="td-head"><span><span class="lang-en">Contents</span><span class="lang-ru">Содержание</span></span><button type="button" class="td-close" id="tocclose" aria-label="close">✕</button></div>
 <div class="td-body" id="tocdrawerbody"></div>
</aside>'''

NAVJS = r"""
/* ≤1024: the sidebar TOC is hidden, so the same markup is cloned into a drawer opened from the
   sticky bar. Closes on link tap, on ✕, on Escape, on backdrop tap; body scroll is locked while open.
   This listener is registered before the map/brief scripts, so its Escape can stop them from also
   firing (closing the drawer must not close an open brief or deselect a station). */
(function(){
  var drawer=document.getElementById('tocdrawer'), back=document.getElementById('tocbackdrop'),
      btn=document.getElementById('tocopen'), closeBtn=document.getElementById('tocclose'),
      host=document.getElementById('tocdrawerbody'), toc=document.querySelector('nav.toc');
  if(!drawer||!back||!btn||!host||!toc) return;
  host.innerHTML=toc.innerHTML;
  var mq=window.matchMedia('(max-width:1024px)');
  function setOpen(o){
    drawer.hidden=!o; back.hidden=!o;
    btn.setAttribute('aria-expanded',String(!!o));
    if(o){ document.body.classList.add('drawer-open'); if(closeBtn&&closeBtn.focus)closeBtn.focus(); }
    else { document.body.classList.remove('drawer-open'); }
  }
  btn.addEventListener('click',function(){ setOpen(drawer.hidden); });
  if(closeBtn) closeBtn.addEventListener('click',function(){ setOpen(false); btn.focus(); });
  back.addEventListener('click',function(){ setOpen(false); });
  host.addEventListener('click',function(ev){ var t=ev.target; if(t&&t.closest&&t.closest('a')) setOpen(false); });
  document.addEventListener('keydown',function(ev){
    if(ev.key==='Escape'&&!drawer.hidden){ ev.stopImmediatePropagation(); setOpen(false); btn.focus(); }
  });
  function sync(){ if(!mq.matches&&!drawer.hidden) setOpen(false); }
  if(mq.addEventListener) mq.addEventListener('change',sync); else if(mq.addListener) mq.addListener(sync);
  window.addEventListener('resize',sync);
})();
/* ≤1024: the glyph legend collapses (it is nine long lines); above 1024 it stays open as before. */
(function(){
  var d=document.getElementById('glyphlegend'); if(!d||!window.matchMedia) return;
  var mq=window.matchMedia('(max-width:1024px)');
  function sync(){ d.open=!mq.matches; }
  sync();
  if(mq.addEventListener) mq.addEventListener('change',sync); else if(mq.addListener) mq.addListener(sync);
})();
"""

def masthead(cfg):
    doi=cfg['doi_concept']; doiurl='https://doi.org/'+doi; beta=(STATUS=='beta')
    doi_html=(f'<span class="doi" title="reserved on Zenodo; resolves when the edition is released">{doi}</span> · <span class="beta lang-en">DOI reserved</span><span class="beta lang-ru">DOI зарезервирован</span>' if beta
              else f'<a href="{doiurl}" target="_blank" rel="noopener">{doi}</a>')
    return f'''<header class="mast">
 <div>
  <div class="eyebrow"><span class="lang-en">Edition {cfg['edition']}{' · <b class="beta">beta</b>' if beta else ''} · English / Russian</span><span class="lang-ru">Издание {cfg['edition']}{' · <b class="beta">бета</b>' if beta else ''} · English / Русский</span></div>
  <h1 class="title">Quantum Technology Map</h1>
  <p class="author"><span class="lang-en">Author</span><span class="lang-ru">Автор</span> · <b>{cfg['author']}</b> <a class="orcid" href="https://orcid.org/0000-0001-7362-9529" target="_blank" rel="noopener author" title="ORCID iD: https://orcid.org/0000-0001-7362-9529" aria-label="ORCID iD 0000-0001-7362-9529"><svg class="orcid-id" viewBox="0 0 256 256" width="16" height="16" aria-hidden="true"><path fill="#A6CE39" d="M256 128c0 70.7-57.3 128-128 128S0 198.7 0 128 57.3 0 128 0s128 57.3 128 128z"/><path fill="#FFF" d="M86.3 186.2H70.9V79.1h15.4v107.1zM108.9 79.1h41.6c39.6 0 57 28.3 57 53.6 0 27.5-21.5 53.6-56.8 53.6h-41.8V79.1zm15.4 93.3h24.5c34.9 0 42.9-26.5 42.9-39.7 0-21.5-13.7-39.7-43.7-39.7h-23.7v79.4zM88.7 56.8c0 5.5-4.5 10.1-10.1 10.1s-10.1-4.6-10.1-10.1c0-5.6 4.5-10.1 10.1-10.1s10.1 4.6 10.1 10.1z"/></svg></a></p>
  <p class="subtitle"><span class="lang-en">Every quantum-computing technology (96) and every quantum machine built, announced or planned (136): analysed and summarised, partitioned by seven invariant design attributes, compared and combined in dozens of ways — with a brief on every technology and a card on every machine.</span><span class="lang-ru">Все технологии квантовых вычислений (96) и все построенные, объявленные или запланированные квантовые машины (136): проанализированы и сведены, разбиты по семи неизменным атрибутам конструкции, сопоставлены и скомбинированы десятками способов — с брифом на каждую технологию и карточкой на каждую машину.</span></p>
 </div>
 <div class="controls">
  <div class="seg" role="group" aria-label="language"><button type="button" data-setlang="en" aria-pressed="true">English</button><button type="button" data-setlang="ru" aria-pressed="false">Русский</button></div>
  <div class="pubmeta">
   <div><span class="lang-en">Published by</span><span class="lang-ru">Издатель</span> <a href="https://qodeh.com" target="_blank" rel="noopener">{cfg['publisher']}</a> · <span class="lang-en">data cut-off 4 September 2026</span><span class="lang-ru">данные по состоянию на 4 сентября 2026</span></div>
   <div>DOI {doi_html} · <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="license noopener">CC BY 4.0</a> · <a class="ghlink" href="{cfg['repo']}" target="_blank" rel="noopener" title="github.com/qraveh/qt-map"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg> <span class="lang-en">GitHub — data &amp; source</span><span class="lang-ru">GitHub — данные и исходники</span></a></div>
  </div>
 </div>
</header>'''

def footer(cfg):
    if cfg['mode']=='internal': return ''
    doi=cfg['doi_concept']; doiurl='https://doi.org/'+doi
    if STATUS=='beta':
        cite_en=f"{cfg['author']} (2026). <i>Quantum Technology Map</i> (Edition {cfg['edition']}, beta). {cfg['publisher']}. <a href=\"{cfg['url']}\">{cfg['url']}</a> — DOI {doi} is reserved on Zenodo and will resolve when the edition is released; until then cite the site."
        cite_ru=f"{cfg['author']} (2026). <i>Quantum Technology Map</i> (издание {cfg['edition']}, бета). {cfg['publisher']}. <a href=\"{cfg['url']}\">{cfg['url']}</a> — DOI {doi} зарезервирован на Zenodo и заработает при выпуске издания; до тех пор ссылайтесь на сайт."
    else:
        cite_en=f"{cfg['author']} (2026). <i>Quantum Technology Map</i> (Edition {cfg['edition']}). {cfg['publisher']}. <a href=\"{doiurl}\">{doiurl}</a> — the concept DOI resolves to the newest edition; cite the edition you read."
        cite_ru=f"{cfg['author']} (2026). <i>Quantum Technology Map</i> (издание {cfg['edition']}). {cfg['publisher']}. <a href=\"{doiurl}\">{doiurl}</a> — DOI концепции разрешается в последнее издание; указывайте издание, которое читали."
    return f'''<footer class="colophon">
 <div class="lang-en">
  <p><b>Cite as.</b> {cite_en}</p>
  <p><b>License.</b> This work is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">Creative Commons Attribution 4.0 International License</a>: you may share and adapt it for any purpose, including commercially, provided you give appropriate credit, link to the license and indicate any changes. The interactive document, its technology graph (96 nodes, edges and attributes) and the 96 technology briefs are all covered. Quoted figures remain the property of their cited sources.</p>
  <p><b>Data and source.</b> The graph (nodes, attributes, edges, dated records), the briefs and the build that renders this page are maintained at <a href="{cfg['repo']}">{cfg['repo'].replace('https://','')}</a>; corrections and new records are welcome as issues or pull requests; each edition is a tagged release archived on Zenodo.</p>
  {editions_html('en')}
  <p><b>Disclosures.</b> This is a single-author publication, produced independently — no funding, sponsorship, affiliation, or solicitation. Factual corrections are welcome.</p>
  <p><b>Provenance.</b> Research and drafting with Claude (Anthropic); every figure traces to a dated, linked primary source, and every claim carries an evidence tag ([D] measured / peer-reviewed, [C] company claim, [R] roadmap, [S] simulation or estimate, [G] established fact, [P] preprint or trade press). Known conflicts between sources are stated, not averaged. Open verification items are listed at the end of each brief. Data cut-off: 4 September 2026.</p>
 </div>
 <div class="lang-ru">
  <p><b>Как цитировать.</b> {cite_ru}</p>
  <p><b>Лицензия.</b> Работа распространяется по лицензии <a href="https://creativecommons.org/licenses/by/4.0/deed.ru" rel="license">Creative Commons Attribution 4.0 International</a>: её можно распространять и перерабатывать в любых целях, включая коммерческие, при условии указания авторства, ссылки на лицензию и обозначения внесённых изменений. Лицензия покрывает интерактивный документ, граф технологий (96 узлов, рёбра и атрибуты) и 96 брифов. Цитируемые цифры остаются собственностью указанных источников.</p>
  <p><b>Данные и исходники.</b> Граф (узлы, атрибуты, рёбра, датированные рекорды), брифы и сборка, порождающая эту страницу, ведутся в <a href="{cfg['repo']}">{cfg['repo'].replace('https://','')}</a>; исправления и новые рекорды принимаются как issue или pull request; каждое издание — тегированный релиз, архивируемый на Zenodo.</p>
  {editions_html('ru')}
  <p><b>Раскрытие.</b> Это публикация одного автора, подготовленная независимо — без финансирования, спонсорства, аффилиации и заказа. Фактические поправки приветствуются.</p>
  <p><b>Происхождение.</b> Исследование и написание — совместно с Claude (Anthropic); каждая цифра прослеживается к датированному первоисточнику по ссылке, каждое утверждение несёт тег свидетельства ([D] измерено / рецензировано, [C] заявление компании, [R] дорожная карта, [S] симуляция или оценка, [G] установленный факт, [P] препринт или отраслевая пресса). Расхождения между источниками названы, а не усреднены. Открытые пункты верификации перечислены в конце каждого брифа. Данные по состоянию на 4 сентября 2026.</p>
 </div>
</footer>'''

def head_meta(cfg):
    if cfg['mode']=='internal': return '<meta name="color-scheme" content="light dark">'
    doi=cfg['doi_concept']; cite_doi=('' if STATUS=='beta' else '<meta name="citation_doi" content="'+doi+'">'); ident=(cfg['url'] if STATUS=='beta' else 'https://doi.org/'+doi); desc='Every quantum-computing technology (96) and every quantum machine built, announced or planned (136): analysed and summarised, partitioned by seven invariant design attributes, compared and combined in dozens of ways — with a brief on every technology and a card on every machine. Bilingual EN/RU, CC BY 4.0.'
    ld={"@context":"https://schema.org","@type":"ScholarlyArticle","name":"Quantum Technology Map","headline":"Quantum Technology Map","version":cfg['edition'],"datePublished":cfg['date'],"codeRepository":cfg.get('repo'),"inLanguage":["en","ru"],
        "author":{"@type":"Person","name":cfg['author']},"publisher":{"@type":"Organization","name":cfg['publisher'],"url":"https://qodeh.com"},
        "license":"https://creativecommons.org/licenses/by/4.0/","isAccessibleForFree":True,"identifier":ident,"sameAs":ident,"url":cfg['url'],"description":desc,
        "keywords":["quantum computing","quantum error correction","superconducting qubits","trapped ions","neutral atoms","photonic quantum computing","spin qubits","technology landscape","technology graph"]}
    return ('<meta name="color-scheme" content="light dark">\n<meta name="description" content="'+html.escape(desc)+'">\n'
            f'<meta name="author" content="{cfg["author"]}">\n<meta name="citation_title" content="Quantum Technology Map">\n<meta name="citation_author" content="{cfg["author"]}">\n'
            f'<meta name="citation_publication_date" content="{cfg["date"].replace("-","/")}">\n<meta name="citation_publisher" content="{cfg["publisher"]}">\n{cite_doi}\n<meta name="citation_language" content="en">\n'
            f'<meta name="DC.title" content="Quantum Technology Map"><meta name="DC.creator" content="{cfg["author"]}"><meta name="DC.publisher" content="{cfg["publisher"]}"><meta name="DC.date" content="{cfg["date"]}"><meta name="DC.identifier" content="{ident}"><meta name="DC.rights" content="CC BY 4.0"><meta name="DC.language" content="en, ru">\n'
            f'<meta property="og:type" content="article"><meta property="og:title" content="Quantum Technology Map"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{cfg["url"]}">\n'
            f'<link rel="license" href="https://creativecommons.org/licenses/by/4.0/"><link rel="canonical" href="{cfg["url"]}">\n'
            '<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>')

def build(cfg=PUBLIC):
    D3=open(os.path.join(ROOT,'build','vendor','d3.v7.min.js'),encoding='utf-8').read()
    EN=open(cfg['report_en'],encoding='utf-8').read()
    RU=open(cfg['report_ru'],encoding='utf-8').read()
    regmap=json.load(open(cfg['regmap'],encoding='utf-8')) if cfg.get('regmap') else None
    BR.configure(cfg['mode'],en_dir=cfg.get('briefs_en'),ru_dir=cfg.get('briefs_ru'),regmap=regmap,table_num=cfg['table_num'],id_sections=cfg['id_sections'])
    B=BR.load_briefs()
    ids={b['id'] for b in B}
    colours=BR.family_colours(G)
    BR.TOOLTIPS=lambda h,lang:tooltips(h,lang,briefs=True)
    BR.FOLD=lambda h,lang,bid:foldable(h,lang,levels=('h3',),idprefix='brief-'+bid+'-'+lang)
    briefs_block=BR.briefs_section_html(B,brief_md2html,colours)
    en_html,en_toc=convert(EN,'en'); ru_html,ru_toc=convert(RU,'ru')
    en_html=insert_after_h3_table(en_html,'3.1',radars_block('en')); ru_html=insert_after_h3_table(ru_html,'3.1',radars_block('ru'))
    en_html=tag_sortables(en_html); ru_html=tag_sortables(ru_html)
    en_html=BR.link_node_ids(en_html,ids); ru_html=BR.link_node_ids(ru_html,ids)
    en_html=BR.autolink(en_html); ru_html=BR.autolink(ru_html)
    en_html=foldable(en_html,'en'); ru_html=foldable(ru_html,'ru')
    mapsec_en=map_block('en',cfg['graph_sec']); mapsec_ru=map_block('ru',cfg['graph_sec'])
    en_a,en_b=split_after_s2(en_html,'en'); ru_a,ru_b=split_after_s2(ru_html,'ru')
    en_b1,en_b2=split_before_num(en_b,en_toc,cfg['sources_num']); ru_b1,ru_b2=split_before_num(ru_b,ru_toc,cfg['sources_num'])
    en_toc=toc_with_briefs(en_toc,'en',cfg['sources_num']); ru_toc=toc_with_briefs(ru_toc,'ru',cfg['sources_num'])
    dl=cfg['default_lang']
    body=f'''<title>{cfg['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Golos+Text:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<div id="app" data-lang="{dl}">
{navchrome(cfg)}
{masthead(cfg)}
<div class="page">
 <nav class="toc" aria-label="contents"><div class="lang-en">{toc_html(en_toc,'en',cfg['graph_sec'])}</div><div class="lang-ru">{toc_html(ru_toc,'ru',cfg['graph_sec'])}</div></nav>
 <main>
  <div id="map"><div class="lang-en">{mapsec_en}</div><div class="lang-ru">{mapsec_ru}</div></div>
  <div id="mapbody"><div class="mapfull">{MAPUI.replace("{MAPLEAD}",map_lead(cfg["graph_sec"]))}</div></div>
  <div class="prose lang-en" lang="en">{en_a}</div><div class="prose lang-ru" lang="ru">{ru_a}</div>
  <div class="prose lang-en" lang="en">{en_b1}</div><div class="prose lang-ru" lang="ru">{ru_b1}</div>
  {briefs_block}
  <div class="prose lang-en" lang="en">{en_b2}</div><div class="prose lang-ru" lang="ru">{ru_b2}</div>
  {footer(cfg)}
 </main>
</div>
</div>
<script>window.__GRAPH={json.dumps(G,ensure_ascii=False,separators=(',',':'))};window.__MACH={json.dumps(mach_slim(),ensure_ascii=False,separators=(',',':'))};window.__SHORT={json.dumps(SHORT,ensure_ascii=False,separators=(',',':'))};window.__KEYREFS={json.dumps(BR.key_refs_all(B),ensure_ascii=False)};</script>
<script>{D3}</script>
<script>
(function(){{const app=document.getElementById('app');
 function setLang(l){{app.setAttribute('data-lang',l); document.querySelectorAll('[data-setlang]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.setlang===l))); document.documentElement.lang=l; try{{localStorage.setItem('qtech-lang',l);}}catch(e){{}} if(window.__relabelMap)window.__relabelMap();}}
 let l='{dl}'; try{{l=localStorage.getItem('qtech-lang')||((navigator.language||'').toLowerCase().startsWith('ru')?'ru':'{dl}');}}catch(e){{}}
 document.querySelectorAll('[data-setlang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.setlang)));
 window.__setLang=setLang; setLang(l);
}})();
</script>
<script>{NAVJS}</script>
<script>{JS}</script>
<script>{BRIEF_JS}</script>
<script>window.__TIPS={json.dumps(tips_dict(),ensure_ascii=False,separators=(',',':'))};</script>
<script>{GTIP_JS}</script><script>{FOLD_JS}</script><script>{TAG_JS}</script>
<script>if(window.__relabelMap)window.__relabelMap();</script>
'''
    open(cfg['out_body'],'w',encoding='utf-8',newline='\n').write(body)
    full=f'<!doctype html>\n<html lang="{dl}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{head_meta(cfg)}<style>img{{max-width:100%}}[hidden]{{display:none!important}}</style></head><body>'+body+'</body></html>'
    open(cfg['out_full'],'w',encoding='utf-8',newline='\n').write(full)
    nofb=sum(1 for b in B if b['ru_fallback'])
    print('built', cfg['mode'], len(body)//1024,'KB body;', len(full)//1024,'KB full;',len(B),'briefs;',nofb,'RU fallbacks')

if __name__=='__main__':
    build(PUBLIC)
