# -*- coding: utf-8 -*-
import re, json, sys, html
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'build')); sys.path.insert(0,os.path.join(ROOT,'data'))
import markdown
from page_css import CSS
from map_js import JS
from brief_js import BRIEF_JS
from labels import SHORT
from editions import EDITIONS, editions_html, CONCEPT_DOI, REPO, SITE, STATUS
import briefs as BR
G=json.load(open(os.path.join(ROOT,'data','graph.json'),encoding='utf-8'))

# ---------- math: $...$ → HTML
GREEK={'Lambda':'Λ','lambda':'λ','mu':'µ','varepsilon':'ε','epsilon':'ε','kappa':'κ','alpha':'α','beta':'β','gamma':'γ','delta':'δ','Delta':'Δ','eta':'η','theta':'θ','sigma':'σ','pi':'π','tau':'τ','omega':'ω','Omega':'Ω','rho':'ρ','phi':'φ','chi':'χ','psi':'ψ','nu':'ν'}
SYM={'times':'×','sim':'∼','approx':'≈','le':'≤','ge':'≥','leq':'≤','geq':'≥','ll':'≪','gg':'≫','pm':'±','to':'→','rightarrow':'→','infty':'∞','propto':'∝','cdot':'·','diamond':'◇','rangle':'⟩','langle':'⟨','lvert':'|','rvert':'|','ast':'∗','circ':'∘','neq':'≠','ne':'≠','sqrt':'√','in':'∈','cup':'∪','cap':'∩','dots':'…','ldots':'…'}
def tex(s):
    s=s.replace('\\,',' ').replace('\\ ',' ').replace('\;',' ')
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
    plain=re.sub('<[^>]+>','',s)
    cls='m long' if len(plain)>50 else 'm'
    return '<span class="'+cls+'">'+s+'</span>'
def premath(md):
    md=re.sub(r'\$\$(.+?)\$\$',lambda m:'<div class="m">'+tex(m.group(1))+'</div>',md,flags=re.S)
    return re.sub(r'(?<!\\)\$([^$\n]+?)\$',lambda m:tex(m.group(1)),md)

# ---------- markdown → html + structure
def convert(md,lang):
    P=lang+'-'
    md=premath(md)
    h=markdown.markdown(md,extensions=['tables','sane_lists'])
    # wrap tables
    h=re.sub(r'<table>',r'<div class="tbl"><table>',h); h=h.replace('</table>','</table></div>')
    # headings: ids and numbering
    toc=[]; k=0; j=0
    def h2(m):
        nonlocal k,j; k+=1; j=0; txt=m.group(1); mm=re.match(r'(\d+)\.\s+(.*)',txt)
        num,title=(mm.group(1),mm.group(2)) if mm else ('',txt)
        toc.append((f'{P}s{k}',num,re.sub('<[^>]+>','',title),2))
        return f'<h2 id="{P}s{k}">'+(f'<span class="num">{num}</span>' if num else '')+f'{title}</h2>'
    def h3(m):
        nonlocal k,j; j+=1; txt=m.group(1); mm=re.match(r'(\d+\.\d+)\s+(.*)',txt); num,title=(mm.group(1),mm.group(2)) if mm else ('',txt)
        toc.append((f'{P}s{k}-{j}',num,re.sub('<[^>]+>','',title),3))
        return f'<h3 id="{P}s{k}-{j}">{txt}</h3>'
    h=re.sub(r'<h2>(.*?)</h2>',h2,h); h=re.sub(r'<h3>(.*?)</h3>',h3,h)
    # the first h2 (subtitle line) is actually the subtitle: strip the first h1/h2 pair
    h=re.sub(r'<h1>.*?</h1>\s*','',h,count=1,flags=re.S)
    h=re.sub(r'<h2 id="'+P+r's1">.*?</h2>\s*','',h,count=1,flags=re.S); toc=[t for t in toc if t[0]!=P+'s1']
    # fold big tables in §8 (node table, edge lists) and §9 sources
    def fold(h,heading_regex,label):
        m=re.search(heading_regex,h)
        if not m: return h
        start=m.end(); t=h.find('<div class="tbl">',start); e=h.find('</div>',t)+6
        return h[:t]+f'<details class="fold big-table"><summary>{label}</summary>'+h[t:e]+'</details>'+h[e:]
    h=fold(h,r'<h3 id="[a-z]+-s\d+-2">[^<]*</h3>','Show table · Показать таблицу' if lang=='en' else 'Показать таблицу · Show table')
    h=fold(h,r'<h3 id="[a-z]+-s\d+-11">[^<]*</h3>','Show records · Показать рекорды' if lang=='en' else 'Показать рекорды · Show records')
    for lbl in (['<strong>requires / provides</strong>','<strong>alternatives (within layer)</strong>','<strong>conflicts</strong>','<strong>transfers (node → additional platform paths)</strong>','<strong>defines (node → output; every row carries a source, a date and a number)</strong>'] if lang=='en' else
                ['<strong>требует / обеспечивает</strong>','<strong>альтернативы (внутри слоя)</strong>','<strong>конфликтует</strong>','<strong>переносится (узел → дополнительные платформенные пути)</strong>','<strong>определяет (узел → выход; каждая строка несёт источник, дату и число)</strong>']):
        h=fold(h,re.escape(lbl),re.sub('<[^>]+>','',lbl))
    # split off sources section into a fold
    return h,toc

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

# insert map section after §0 (before <h2 id="s3"> which is "1. Criteria") — s2 is exec summary (s1 stripped)
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

# ---------- map section block
def map_block(lang,gsec='8'):
    en=lang=='en'
    return f'''<section class="mapsec">
<h2><span class="num">{'MAP' if en else 'КАРТА'}</span>{'Technology map — ten layers, seven coordinates, fourteen platform paths' if en else 'Карта технологий — десять слоёв, семь координат, четырнадцать путей платформ'}<button type="button" class="chip mapcol" data-mapcollapse="1" aria-expanded="true"><span class="when-open">{'▾ collapse' if en else '▾ свернуть'}</span><span class="when-closed" hidden>{'▸ expand map' if en else '▸ развернуть карту'}</span></button></h2>
<p class="lead">{'Columns are the layers of the stack; the vertical position is carrier-nature affinity (natural at the top, fabricated at the bottom), so the natural/fabricated diagonal is visible and every hatched station is a place where a platform breaks it. Coloured lines are platform paths through one station per layer; a station on several lines is a transfer hub (◎); dashed hollow stations are empty slots. Click a station for its three spaces; pick a lens to recolour every station by one coordinate; the strip below shows the full seven-coordinate vector of every technology. Construction rules and derived tables are in §'+gsec+'.' if en else 'Колонки — слои стека; вертикальная позиция — сродство носителя (естественные сверху, изготовленные снизу), так что диагональ естественный/изготовленный видна, а каждая заштрихованная станция — место, где платформа её ломает. Цветные линии — пути платформ через одну станцию на слой; станция на нескольких линиях — хаб переноса (◎); пунктирные полые станции — пустые слоты. Кликните станцию, чтобы увидеть её три пространства; выберите линзу, чтобы перекрасить станции по одной координате; лента ниже показывает полный семикоординатный вектор каждой технологии. Правила построения и выведенные таблицы — в §'+gsec+'.'}</p>
</section>'''
MAPUI='''<div class="mapbar" id="mapbar">
 <div class="grp chipsrow"><span class="lbl lang-en">paths</span><span class="lbl lang-ru">пути</span><span id="pathchips" class="grp"></span></div>
 <div class="grp"><span class="lbl lang-en">lens</span><span class="lbl lang-ru">линза</span><select id="lens" class="sel" aria-label="colour lens"></select></div>
 <div class="grp"><span class="lbl lang-en">edges</span><span class="lbl lang-ru">рёбра</span>
  <button class="chip tog" id="tg-req" aria-pressed="false"><span class="lang-en">all requires</span><span class="lang-ru">все «требует»</span></button>
  <button class="chip tog" id="tg-rep" aria-pressed="false"><span class="lang-en">all alternatives</span><span class="lang-ru">все «альтернативы»</span></button>
  <button class="chip tog" id="tg-conf" aria-pressed="false"><span class="lang-en">all conflicts</span><span class="lang-ru">все «конфликтует»</span></button>
  <button class="chip" id="tg-reset"><span class="lang-en">reset</span><span class="lang-ru">сброс</span></button></div>
 <details class="glyphs" id="glyphlegend" open><summary><span class="lbl lang-en">legend</span><span class="lbl lang-ru">легенда</span></summary>
  <div class="glyphlist">
  <span class="gl"><i class="lg hub">◎</i><span class="lang-en">hub</span><span class="lang-ru">хаб</span></span>
  <span class="gl"><i class="lg off">⤢</i><span class="lang-en">off-diagonal</span><span class="lang-ru">внедиагональный</span></span>
  <span class="gl"><i class="lg emp">∅</i><span class="lang-en">empty slot</span><span class="lang-ru">пустой слот</span></span>
  <span class="gl"><i class="lg ed req"></i><span class="lang-en">requires</span><span class="lang-ru">требует</span></span>
  <span class="gl"><i class="lg ed rep"></i><span class="lang-en">alternatives</span><span class="lang-ru">альтернативы</span></span>
  <span class="gl"><i class="lg ed con"></i><span class="lang-en">conflicts — hover for the reason</span><span class="lang-ru">конфликтует — причина по наведению</span></span>
  <span class="gl"><i class="lg band"></i><span class="lang-en">outline colour = platform family; with a lens on, tint + left band = the lens value (legend below)</span><span class="lang-ru">цвет рамки = семейство платформ; при включённой линзе оттенок + полоса слева = значение линзы (легенда ниже)</span></span>
  <span class="gl"><i class="lg badges"><b></b><b></b></i><span class="lang-en">small squares = the platform lines through the station (■ primary, □ alternate)</span><span class="lang-ru">маленькие квадраты = линии платформ через станцию (■ основная, □ альтернатива)</span></span>
  <span class="gl"><i class="lg ax">↕</i><span class="lang-en">rows natural → fabricated · columns = layers · click a station</span><span class="lang-ru">строки естественное → изготовленное · колонки — слои · клик по станции</span></span>
  <span class="gl try"><span class="lang-en">try:</span><span class="lang-ru">попробуйте:</span> <a href="#" data-goto="transmon">Transmon</a> · <a href="#" data-goto="ct_sfq">SFQ</a> · <a href="#" data-goto="ro_erasure"><span class="lang-en">Erasure check</span><span class="lang-ru">Проверка стирания</span></a></span>
  </div>
 </details>
 <div class="grp lenslegend" id="lenslegend"></div>
</div>
<div class="mapgrid"><div class="mapwrap" id="mapwrap"><div class="zoombar"><div class="zoomctl" role="group" aria-label="map zoom"><span class="zhint lang-en">zoom</span><span class="zhint lang-ru">масштаб</span><button type="button" class="zb" id="zoom-out" aria-label="zoom out" title="zoom out (−)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><input class="zlvl" id="zoomlvl" type="text" inputmode="numeric" pattern="[0-9]*" value="100%" aria-label="zoom percent — type a number and press Enter" title="type a percentage and press Enter; ↑/↓ = ±5"><button type="button" class="zb" id="zoom-in" aria-label="zoom in" title="zoom in (+)"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h10M8 3v10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><i class="zsep"></i><button type="button" class="zb zt" id="zoom-fit" title="fit width"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2 8h12M2 8l3-3M2 8l3 3M14 8l-3-3M14 8l-3 3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lang-en">fit</span><span class="lang-ru">вписать</span></button><button type="button" class="zb zt" id="zoom-100" title="actual size">1:1</button></div></div><div class="tip" id="maptip"></div></div><aside class="insp" id="insp" hidden></aside></div>
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
<div class="pcwrap" id="pcwrap"><h3 class="lang-en">Seven coordinates at once — parallel coordinates</h3><h3 class="lang-ru">Семь координат сразу — параллельные координаты</h3>
<p class="lang-en">Each polyline is one technology; axes are the seven design coordinates. Hover to name a line, click to select it on the map. Bundles reveal the diagonal (natural carriers run through optical control and transport; fabricated ones through microwave/electrical control and static wiring); lines that cross the bundles are the off-diagonal technologies.</p>
<p class="lang-ru">Каждая ломаная — одна технология; оси — семь координат проектирования. Наведите, чтобы назвать линию; кликните, чтобы выбрать её на карте. Пучки показывают диагональ (естественные носители идут через оптическое управление и транспорт; изготовленные — через СВЧ/электрическое управление и статическую разводку); линии, пересекающие пучки, — off-diagonal технологии.</p>
<div id="pc"></div></div>'''
# assemble content with both languages
def toc_html(toc,lang,gsec='8'):
    def li(i,num,t,lvl):
        sty=' style="padding-left:14px;font-size:12.5px"' if lvl==3 else ''
        return '<li'+sty+'><a href="#'+i+'"><span class="n">'+num+'</span><span>'+html.escape(t)+'</span></a></li>'
    items=''.join(li(i,num,t,lvl) for i,num,t,lvl in toc if lvl==2 or num.startswith(gsec+'.'))
    return f'<ol><li class="mapl"><a href="#map"><span class="n">◎</span><span>{"Technology map" if lang=="en" else "Карта технологий"}</span></a></li>{items}</ol>'
# find split point: before <h2 id="s3"> in each
def split_after_s2(h,lang):
    i=h.find(f'<h2 id="{lang}-s3">'); return h[:i],h[i:]
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
    title='Quantum Technology Map', default_lang='en', graph_sec='7', sources_num='8', table_num='7.2', id_sections=('7.2','7.5','7.6','7.7'),
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
  <div class="eyebrow"><span class="lang-en">Edition {cfg['edition']}{' · <b class="beta">beta</b>' if beta else ''} · {cfg['date']} · English / Russian</span><span class="lang-ru">Издание {cfg['edition']}{' · <b class="beta">бета</b>' if beta else ''} · {cfg['date']} · English / Русский</span></div>
  <h1 class="title">Quantum Technology Map <span class="yr">{cfg['edition']}</span></h1>
  <p class="subtitle"><span class="lang-en">Every quantum-computing platform compared by the goal it serves — achievements, justified intentions, the most promising directions — a 96-technology graph across ten stack layers that reproduces those directions on its own, and a brief on each technology.</span><span class="lang-ru">Все платформы квантовых компьютеров, сравнённые по целям, которым они служат, — достижения, обоснованные намерения, наиболее перспективные направления, — граф 96 технологий в десяти слоях стека, который воспроизводит эти направления сам, и бриф по каждой технологии.</span></p>
  <p class="author"><span class="lang-en">Author</span><span class="lang-ru">Автор</span> · <b>{cfg['author']}</b></p>
 </div>
 <div class="controls">
  <div class="seg" role="group" aria-label="language"><button type="button" data-setlang="en" aria-pressed="true">English</button><button type="button" data-setlang="ru" aria-pressed="false">Русский</button></div>
  <a class="jump" href="#map"><span class="lang-en">Jump to the map ↓</span><span class="lang-ru">К карте ↓</span></a>
  <div class="pubmeta">
   <div><span class="lang-en">Published by</span><span class="lang-ru">Издатель</span> <a href="https://qodeh.com" target="_blank" rel="noopener">{cfg['publisher']}</a> · <span class="lang-en">data cut-off 4 September 2026</span><span class="lang-ru">данные по состоянию на 4 сентября 2026</span></div>
   <div>DOI {doi_html} · <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="license noopener">CC BY 4.0</a> · <a href="{cfg['repo']}" target="_blank" rel="noopener"><span class="lang-en">data &amp; source</span><span class="lang-ru">данные и исходники</span></a></div>
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
  <p><b>License.</b> This work is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">Creative Commons Attribution 4.0 International License</a>: you may share and adapt it for any purpose, including commercially, provided you give appropriate credit, link to the license and indicate any changes. The interactive document, its technology graph (96 nodes, edges and coordinates) and the 96 technology briefs are all covered. Quoted figures remain the property of their cited sources.</p>
  <p><b>Data and source.</b> The graph (nodes, coordinates, edges, dated records), the briefs and the build that renders this page are maintained at <a href="{cfg['repo']}">{cfg['repo'].replace('https://','')}</a>; corrections and new records are welcome as issues or pull requests; each edition is a tagged release archived on Zenodo.</p>
  {editions_html('en')}
  <p><b>Provenance.</b> Research and drafting with Claude (Anthropic); every figure traces to a dated, linked primary source, and every claim carries an evidence tag ([D] measured / peer-reviewed, [C] company claim, [R] roadmap, [S] simulation or estimate, [G] established fact, [P] preprint or trade press). Known conflicts between sources are stated, not averaged. Open verification items are listed at the end of each brief. Data cut-off: 4 September 2026.</p>
 </div>
 <div class="lang-ru">
  <p><b>Как цитировать.</b> {cite_ru}</p>
  <p><b>Лицензия.</b> Работа распространяется по лицензии <a href="https://creativecommons.org/licenses/by/4.0/deed.ru" rel="license">Creative Commons Attribution 4.0 International</a>: её можно распространять и перерабатывать в любых целях, включая коммерческие, при условии указания авторства, ссылки на лицензию и обозначения внесённых изменений. Лицензия покрывает интерактивный документ, граф технологий (96 узлов, рёбра и координаты) и 96 брифов. Цитируемые цифры остаются собственностью указанных источников.</p>
  <p><b>Данные и исходники.</b> Граф (узлы, координаты, рёбра, датированные рекорды), брифы и сборка, порождающая эту страницу, ведутся в <a href="{cfg['repo']}">{cfg['repo'].replace('https://','')}</a>; исправления и новые рекорды принимаются как issue или pull request; каждое издание — тегированный релиз, архивируемый на Zenodo.</p>
  {editions_html('ru')}
  <p><b>Происхождение.</b> Исследование и написание — совместно с Claude (Anthropic); каждая цифра прослеживается к датированному первоисточнику по ссылке, каждое утверждение несёт тег свидетельства ([D] измерено / рецензировано, [C] заявление компании, [R] дорожная карта, [S] симуляция или оценка, [G] установленный факт, [P] препринт или отраслевая пресса). Расхождения между источниками названы, а не усреднены. Открытые пункты верификации перечислены в конце каждого брифа. Данные по состоянию на 4 сентября 2026.</p>
 </div>
</footer>'''

def head_meta(cfg):
    if cfg['mode']=='internal': return '<meta name="color-scheme" content="light dark">'
    doi=cfg['doi_concept']; cite_doi=('' if STATUS=='beta' else '<meta name="citation_doi" content="'+doi+'">'); ident=(cfg['url'] if STATUS=='beta' else 'https://doi.org/'+doi); desc='Quantum computing technologies compared by goal: achievements, justified intentions and the most promising directions; a 96-technology graph across ten stack layers with seven design coordinates and five edge types; 96 technology briefs. Bilingual EN/RU, CC BY 4.0.'
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
    D3=open('/tmp/d3get/node_modules/d3/dist/d3.min.js',encoding='utf-8').read()
    EN=open(cfg['report_en'],encoding='utf-8').read()
    RU=open(cfg['report_ru'],encoding='utf-8').read()
    regmap=json.load(open(cfg['regmap'],encoding='utf-8')) if cfg.get('regmap') else None
    BR.configure(cfg['mode'],en_dir=cfg.get('briefs_en'),ru_dir=cfg.get('briefs_ru'),regmap=regmap,table_num=cfg['table_num'],id_sections=cfg['id_sections'])
    B=BR.load_briefs()
    ids={b['id'] for b in B}
    colours=BR.family_colours(G)
    briefs_block=BR.briefs_section_html(B,brief_md2html,colours)
    en_html,en_toc=convert(EN,'en'); ru_html,ru_toc=convert(RU,'ru')
    en_html=insert_after_h3_table(en_html,'3.1',radars_block('en')); ru_html=insert_after_h3_table(ru_html,'3.1',radars_block('ru'))
    en_html=BR.link_node_ids(en_html,ids); ru_html=BR.link_node_ids(ru_html,ids)
    en_html=BR.autolink(en_html); ru_html=BR.autolink(ru_html)
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
  <div class="prose lang-en">{en_a}</div><div class="prose lang-ru">{ru_a}</div>
  <div id="map"><div class="lang-en">{mapsec_en}</div><div class="lang-ru">{mapsec_ru}</div></div>
  <div id="mapbody"><div class="mapfull">{MAPUI}</div></div>
  <div class="prose lang-en">{en_b1}</div><div class="prose lang-ru">{ru_b1}</div>
  {briefs_block}
  <div class="prose lang-en">{en_b2}</div><div class="prose lang-ru">{ru_b2}</div>
  {footer(cfg)}
 </main>
</div>
</div>
<script>window.__GRAPH={json.dumps(G,ensure_ascii=False)};window.__SHORT={json.dumps(SHORT,ensure_ascii=False)};window.__KEYREFS={json.dumps(BR.key_refs_all(B),ensure_ascii=False)};</script>
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
<script>if(window.__relabelMap)window.__relabelMap();</script>
'''
    open(cfg['out_body'],'w',encoding='utf-8').write(body)
    full=f'<!doctype html>\n<html lang="{dl}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{head_meta(cfg)}<style>img{{max-width:100%}}[hidden]{{display:none!important}}</style></head><body>'+body+'</body></html>'
    open(cfg['out_full'],'w',encoding='utf-8').write(full)
    nofb=sum(1 for b in B if b['ru_fallback'])
    print('built', cfg['mode'], len(body)//1024,'KB body;', len(full)//1024,'KB full;',len(B),'briefs;',nofb,'RU fallbacks')

if __name__=='__main__':
    build(PUBLIC)
