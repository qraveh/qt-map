# -*- coding: utf-8 -*-
"""Find in the Atlas — one search over everything the page holds, walked hit by hit the way a browser's find walks a page
(the editor, 28 Sep 2026; redesigned on his word of 29 Sep: the window opens where it was called, is a little transparent,
searches as one types, speaks full regular expressions, and lists the hits in context).

What it searches. Every text node of the page — the report, the briefs (closed ones too), the glossary, the tables — plus
the tooltips, aria-labels and alt texts (metadata), in the page's languages (the other language's fragment once it has
loaded), and the map's cards *as they render*: every technology, machine and architecture card is rendered off-screen by
the map's own card builders and indexed as text, so "DEPLOYED · 256 q" or "8 technologies" are found where the reader
would see them. Not searched: the record pages (technology/, machine/, organisation/), which are separate documents.

How. The index is built from the live DOM at the first search (and rebuilt when the page's text changes): the page is
walked into "runs" — the text of one block-level element (or of one language span inside it) as one string with a map
back to its text nodes — so a phrase spanning <b>, <a> or <em> still matches. The query is a regular expression in the
ECMAScript dialect (the one browsers, Python's `re` in its common subset, VS Code and grep -E share): `[bg]ui`, `\d+ q`,
`erasure|stirania`, `heron.*flux`; an expression that does not parse yet (a lone "[" while typing) is taken literally
until it does. Options: case-insensitive / case-sensitive, substring / whole word (Unicode word boundaries — any
non-letter, not only a space, delimits a word), and the language: this page's, another implemented language, or all.
Typing searches at once, in slices between keystrokes, and updates only the count while the search runs; Enter / ▼ /
Shift+Enter / ▲ walk the hits, the list under the box shows every hit in its sentence with where it sits, and a click
on a row jumps there. Each step reveals what hides the hit — a folded section, a closed brief, the map's collapsed bar,
the other language, a card — scrolls it into view and highlights it (the CSS Custom Highlight API; a <mark> where the API
is missing).
"""

FIND_HTML = r'''<div class="findbar" id="findbar" hidden role="search" aria-label="find in the Atlas">
 <div class="findrow">
  <input type="search" id="findq" class="findq" autocomplete="off" spellcheck="false" placeholder="find…  regex: [bg]ui  \d+ q  a|b" aria-label="find in the Atlas — a regular expression; Enter next hit, Shift+Enter previous">
  <span class="findcount" id="findcount" aria-live="polite"></span>
  <button type="button" class="fb" id="findprev" aria-label="previous hit (Shift+Enter)" title="previous (Shift+Enter)">▲</button>
  <button type="button" class="fb" id="findnext" aria-label="next hit (Enter)" title="next (Enter)">▼</button>
  <button type="button" class="fb findclose" id="findclose" aria-label="close (Escape)" title="close (Escape)">✕</button>
 </div>
 <div class="findopts">
  <button type="button" class="fo" id="findcase" title="click to toggle"><span class="lang-en">case-insensitive</span><span class="lang-ru">без учёта регистра</span></button>
  <button type="button" class="fo" id="findword" title="click to toggle"><span class="lang-en">substring</span><span class="lang-ru">подстрока</span></button>
  <span class="folang"><button type="button" class="fo" id="findlang" aria-haspopup="menu" aria-expanded="false" title="the language searched"><span id="findlangname">English</span> ▾</button><div class="fomenu" id="findlangmenu" hidden role="menu"></div></span>
  <span class="findmode" id="findmode" title="the query is read as a regular expression; an expression that does not parse is taken literally"></span>
  <span class="findwhere" id="findwhere"></span>
 </div>
 <ol class="findlist" id="findlist" hidden></ol>
</div>'''

FIND_JS = r'''(function(){
var bar=document.getElementById('findbar'), q=document.getElementById('findq'), cnt=document.getElementById('findcount'), where=document.getElementById('findwhere'), list=document.getElementById('findlist'), mode=document.getElementById('findmode');
if(!bar||!q) return;
var app=document.getElementById('app');
function lang(){ return (app&&app.getAttribute('data-lang'))||'en'; }
var T=function(en,ru){ return lang()==='ru'?ru:en; };
var NATIVE={en:'English',ru:'Русский',de:'Deutsch',fr:'Français',es:'Español',zh:'中文',ja:'日本語',he:'עברית',ar:'العربية',pt:'Português',it:'Italiano',ko:'한국어'};
var LANGS=[app.getAttribute('data-page-lang')||'en']; try{ JSON.parse(app.getAttribute('data-other-langs')||'[]').forEach(function(l){ if(LANGS.indexOf(l)<0) LANGS.push(l); }); }catch(e){}
var opts={cs:false, whole:false, scope:'this'};   // scope: 'this' | 'all' | a language code
var hits=[], cur=-1, lastKey='', running=null, index=null, indexKey='', cards={};
var HL=!!(window.CSS&&CSS.highlights&&window.Highlight);
// ---------- the walk: runs of text with a map back to the nodes
var SKIP={SCRIPT:1,STYLE:1,TEMPLATE:1,NOSCRIPT:1,CANVAS:1,SELECT:1,OPTION:1,TEXTAREA:1,INPUT:1,IFRAME:1,OBJECT:1};
var BLOCK={P:1,DIV:1,LI:1,UL:1,OL:1,TABLE:1,THEAD:1,TBODY:1,TFOOT:1,TR:1,TD:1,TH:1,H1:1,H2:1,H3:1,H4:1,H5:1,H6:1,SECTION:1,ARTICLE:1,ASIDE:1,DL:1,DT:1,DD:1,DETAILS:1,SUMMARY:1,FIGURE:1,FIGCAPTION:1,BLOCKQUOTE:1,PRE:1,NAV:1,HEADER:1,FOOTER:1,MAIN:1,FORM:1,FIELDSET:1,LABEL:1,BUTTON:1,HR:1,BR:1,svg:1,SVG:1,text:1,g:1,tspan:1};
var EXCL='#findbar,#insp,#maptip,nav.toc,#tocdrawer,#tocbackdrop,.fbkpop,.langwait,#gtip,.tip,.floatlang';
function langOf(el){ var c=el.classList; if(!c) return null; if(c.contains('lang-en')) return 'en'; if(c.contains('lang-ru')) return 'ru'; return null; }
function walkInto(root,lg,runs,metas,card){
  function textNodesOf(el,out){ var c=el.childNodes; for(var i=0;i<c.length;i++){ var n=c[i]; if(n.nodeType===3) out.push(n); else if(n.nodeType===1&&!SKIP[n.tagName]&&!(n.matches&&n.matches(EXCL))) textNodesOf(n,out); } }
  function flush(run,lgx){ if(!run.length) return; var nodes=[]; for(var i=0;i<run.length;i++){ var n=run[i]; if(n.nodeType===3) nodes.push(n); else textNodesOf(n,nodes); }
    if(!nodes.length) return; var segs=[], text='', pos=0;
    for(var k=0;k<nodes.length;k++){ var t=nodes[k].nodeValue; if(!t) continue; segs.push({node:nodes[k],start:pos,end:pos+t.length}); text+=t; pos+=t.length; }
    if(text.trim()) runs.push({text:text,segs:segs,lang:lgx,card:card||null}); }
  function meta(el,lgx){ if(card) return; var a=['title','aria-label','alt']; for(var i=0;i<a.length;i++){ var v=el.getAttribute&&el.getAttribute(a[i]); if(v&&v.trim()) metas.push({el:el,attr:a[i],text:v,lang:lgx}); } }
  function walk(el,lgx){
    if(el.nodeType!==1||SKIP[el.tagName]||(el.matches&&el.matches(EXCL))) return;
    var l=langOf(el)||lgx; meta(el,l);
    var run=[], c=el.childNodes;
    for(var i=0;i<c.length;i++){ var n=c[i];
      if(n.nodeType===3){ run.push(n); continue; }
      if(n.nodeType!==1) continue;
      if(SKIP[n.tagName]||(n.matches&&n.matches(EXCL))){ flush(run,l); run=[]; continue; }
      if(BLOCK[n.tagName]||langOf(n)||n.querySelector('p,div,li,table,h1,h2,h3,h4,dl,details,figure,section,.lang-en,.lang-ru')){ flush(run,l); run=[]; walk(n,l); }
      else { run.push(n); meta(n,l); var inl=n.querySelectorAll('[title],[aria-label],[alt]'); for(var j=0;j<inl.length;j++) meta(inl[j],l); }
    }
    flush(run,l);
  }
  if(root.nodeType===11){ var ch=root.childNodes; var top=[]; for(var i=0;i<ch.length;i++){ if(ch[i].nodeType===1) walk(ch[i],lg); } }
  else walk(root,lg);
}
function buildDom(){ var runs=[], metas=[]; walkInto(document.body,null,runs,metas,null); return {runs:runs,metas:metas}; }
// the cards as they render (the map's own builders), per language: technology, machine, architecture
function cardRuns(L){
  if(cards[L]) return cards[L];
  var out=[]; var R=window.__cardHTML, G=window.__GRAPH, M=window.__MACH; if(!R||!G) return (cards[L]=out);
  var was=app.getAttribute('data-lang'); if(was!==L) app.setAttribute('data-lang',L);   // the builders read the page language; restored before the browser paints
  try{
    var items=[]; G.nodes.forEach(function(n){ items.push(['node',n.id,n[L]||n.en||n.id]); }); (G.paths||[]).forEach(function(p){ items.push(['path',p.id,p[L]||p.en||p.id]); }); if(M&&M.machines) M.machines.forEach(function(m){ items.push(['machine',m.id,m.name]); });
    items.forEach(function(it){ var html=''; try{ html=R[it[0]](it[1]); }catch(e){ html=''; } if(!html) return;
      var tpl=document.createElement('template'); tpl.innerHTML=html; walkInto(tpl.content,L,out,[],{kind:it[0],id:it[1],name:it[2]}); });
  } finally { if(was!==L) app.setAttribute('data-lang',was); }
  return (cards[L]=out);
}
window.__findInvalidate=function(){ index=null; cards={}; lastKey=''; };
(window.__hydrators=window.__hydrators||[]).push(function(){ index=null; lastKey=''; });
// ---------- the query: a regular expression; a literal fallback while it does not parse
function esc(s){ return s.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&'); }
function makeRe(query){ var flags='gu'+(opts.cs?'':'i'), src=query, lit=false;
  try{ new RegExp(src,flags); }catch(e){ src=esc(query); lit=true; }
  if(opts.whole) src='(?<![\\p{L}\\p{N}_])(?:'+src+')(?![\\p{L}\\p{N}_])';
  var re=null; try{ re=new RegExp(src,flags); }catch(e){ try{ re=new RegExp(src,'g'+(opts.cs?'':'i')); }catch(e2){ re=null; } }
  if(mode) mode.textContent=lit?T('literal','буквально'):'regex';
  return re; }
function scopeLangs(){ if(opts.scope==='all') return null; if(opts.scope==='this') return [lang()]; return [opts.scope]; }
function inScope(lg){ var s=scopeLangs(); if(!s||!lg) return true; return s.indexOf(lg)>=0; }
// ---------- search, in slices between keystrokes: only the count moves while it runs
var MAXH=3000;
function search(query,done){
  if(running){ running.stop=true; }
  clearHL(); hits=[]; cur=-1; list.hidden=true; list.innerHTML='';
  var re=makeRe(query); if(!re){ show(); return; }
  var key=lang(); if(!index||indexKey!==key){ index=buildDom(); indexKey=key; }
  var langs=scopeLangs()||LANGS.slice(); var cardSets=[]; langs.forEach(function(L){ if(L===lang()||LANGS.indexOf(L)>=0) cardSets.push(cardRuns(L)); });
  var run={stop:false}; running=run; var n=0, i=0, phase=0, pos=0, cardK={};
  var pools=[index.runs].concat(cardSets);
  function step(){ if(run.stop) return; var t0=Date.now();
    while(Date.now()-t0<12){
      if(phase<pools.length){ var pool=pools[phase]; if(pos>=pool.length){ phase++; pos=0; continue; }
        var r=pool[pos++]; if(n>=MAXH||!inScope(r.lang)) continue; re.lastIndex=0; var m;
        while((m=re.exec(r.text))){ if(!m[0].length){ re.lastIndex++; continue; } var h={kind:'text',run:r,start:m.index,end:m.index+m[0].length,lang:r.lang};
          if(r.card){ h.kind='card'; h.card=r.card; var ck=r.card.kind+':'+r.card.id; cardK[ck]=(cardK[ck]||0); h.k=cardK[ck]++; }
          hits.push(h); if(++n>=MAXH) break; } }
      else if(phase===pools.length){ if(pos>=index.metas.length){ phase++; pos=0; continue; } var x=index.metas[pos++]; if(n>=MAXH||!inScope(x.lang)) continue; re.lastIndex=0; var mm=re.exec(x.text); if(mm){ hits.push({kind:'meta',el:x.el,attr:x.attr,text:x.text,lang:x.lang}); n++; } }
      else break;
    }
    cnt.textContent=(cur>=0?(cur+1):'—')+' / '+n+(n>=MAXH?'+':'');
    if(phase>pools.length){ running=null; paintAll(); renderList(); show(); if(done) done(); return; }
    setTimeout(step,0); }
  step();
}
// ---------- highlight
function rangeOf(h){ var r=document.createRange(), s=null, e=null;
  for(var i=0;i<h.run.segs.length;i++){ var g=h.run.segs[i]; if(!g.node.isConnected) return null; if(s===null&&h.start<g.end){ s=g; r.setStart(g.node,h.start-g.start); } if(h.end<=g.end){ e=g; r.setEnd(g.node,h.end-g.start); break; } }
  if(s===null||e===null) return null; return r; }
function unmark(){ var ms=document.querySelectorAll('mark.findmark'); for(var i=0;i<ms.length;i++){ var m=ms[i]; var p=m.parentNode; while(m.firstChild) p.insertBefore(m.firstChild,m); p.removeChild(m); }
  var os=document.querySelectorAll('.findout'); for(var j=0;j<os.length;j++) os[j].classList.remove('findout'); }
function clearHL(){ if(HL){ CSS.highlights.delete('findall'); CSS.highlights.delete('findcur'); } unmark(); }
function paintAll(){ if(!HL) return; try{ var H=new Highlight(); hits.forEach(function(h){ if(h.kind==='text'){ var r=rangeOf(h); if(r) H.add(r); } }); CSS.highlights.set('findall',H); }catch(e){} }
function paintRange(r,el){ if(HL){ try{ var H=new Highlight(); H.add(r); CSS.highlights.set('findcur',H); return; }catch(e){} }
  try{ var m=document.createElement('mark'); m.className='findmark'; r.surroundContents(m); }catch(e){ if(el) el.classList.add('findout'); } }
// ---------- reveal what hides a hit
function revealEl(el){
  var lgEl=el.closest&&el.closest('.lang-en,.lang-ru'); var lg=lgEl?(lgEl.classList.contains('lang-ru')?'ru':'en'):null;
  if(lg&&lg!==lang()&&window.__setLang) window.__setLang(lg);
  for(var p=el;p;p=p.parentElement){
    if(p.tagName==='DETAILS'&&!p.open) p.open=true;
    if(p.hidden){ if(p.classList.contains('secbody')&&window.__setFold) window.__setFold(p.dataset.sec,true,false);
      else if(p.classList.contains('brief')&&window.__openBrief){ window.__openBrief(p.id.replace(/^brief-/,''),true); }
      else if(p.id==='barsum'){ }
      else p.hidden=false; }
    if(p.id==='mapbar'&&p.classList.contains('collapsed')&&window.__setBarCollapsed) window.__setBarCollapsed(false);
    if(p.id==='mapbody'&&window.__expandMap) window.__expandMap();
  }
}
function visible(el){ var r=el.getBoundingClientRect?el.getBoundingClientRect():null; return !!(r&&(r.width||r.height)); }
function scrollTo(el){ try{ el.scrollIntoView({block:'center',inline:'nearest'}); }catch(e){ el.scrollIntoView(); } }
function openCard(c){ if(window.__expandMap) window.__expandMap(); var ok=false;
  if(c.kind==='node'&&window.__selectNode) ok=window.__selectNode(c.id); else if(c.kind==='machine'&&window.__showMachine) ok=window.__showMachine(c.id); else if(c.kind==='path'&&window.__isolatePath) ok=window.__isolatePath(c.id);
  return ok; }
function go(i){ if(!hits.length){ show(); return; } i=((i%hits.length)+hits.length)%hits.length; cur=i; var h=hits[i];
  if(HL) CSS.highlights.delete('findcur'); unmark();
  if(h.kind==='text'){ var el=h.run.segs[0].node.parentElement; if(!el){ show(); return; } revealEl(el);
    var r=rangeOf(h); var host=r?(r.startContainer.parentElement||el):el; if(!r||!visible(host)){ show(T('hidden here','скрыто здесь')); markRow(); return; }
    scrollTo(host); paintRange(r,host); show(); }
  else if(h.kind==='meta'){ revealEl(h.el); if(visible(h.el)){ scrollTo(h.el); h.el.classList.add('findout'); } show((h.attr==='title'?T('tooltip: ','подсказка: '):h.attr+': ')+h.text.slice(0,140)); }
  else if(h.kind==='card'){ var L=h.lang; if(L&&L!==lang()&&window.__setLang) window.__setLang(L);
    openCard(h.card); var insp=document.getElementById('insp'); var w=document.getElementById('mapwrap');
    if(insp&&!insp.hidden){ var runs=[]; walkInto(insp,L,runs,[],h.card); var re=makeRe(q.value.trim()); var k=0, found=null;
      if(re) for(var a=0;a<runs.length&&!found;a++){ re.lastIndex=0; var m; while((m=re.exec(runs[a].text))){ if(!m[0].length){ re.lastIndex++; continue; } if(k===h.k){ found={run:runs[a],start:m.index,end:m.index+m[0].length}; break; } k++; } }
      if(found){ var rr=rangeOf(found); if(rr){ var hostEl=rr.startContainer.parentElement; try{ hostEl.scrollIntoView({block:'nearest'}); }catch(e){} paintRange(rr,hostEl); } }
      else if(w) scrollTo(w); }
    else if(w) scrollTo(w);
    show(T('card: ','карточка: ')+h.card.name); }
  markRow();
}
// ---------- the list of hits in context
var RENDERED=0, ROWS=200;
function whereOf(h){ if(h.kind==='card') return (h.card.kind==='node'?T('technology card','карточка технологии'):h.card.kind==='machine'?T('machine card','карточка машины'):T('architecture card','карточка архитектуры'))+' · '+h.card.name;
  if(h.kind==='meta') return T('tooltip','подсказка');
  var el=h.run.segs[0].node.parentElement; if(!el) return '';
  var b=el.closest('section.brief'); if(b){ var t=b.querySelector('h2,h3,.btitle'); return T('brief','бриф')+(t?' · '+t.textContent.trim().slice(0,60):''); }
  if(el.closest('#mapbar')) return T('map controls','панель карты'); if(el.closest('#mapbody')) return T('map','карта'); if(el.closest('.mast')) return T('masthead','шапка'); if(el.closest('#pcwrap')) return T('strip','лента');
  var sb=el.closest('.secbody[data-sec]'); if(sb){ var hd=sb.previousElementSibling; if(hd&&/^H[23]$/.test(hd.tagName)){ var c=hd.cloneNode(true); var fb=c.querySelector('.foldbtn'); if(fb) fb.remove(); return c.textContent.replace(/\s+/g,' ').trim().slice(0,70); } }
  var g=el.closest('dl.glossary,details.glossary-fold'); if(g) return T('glossary','глоссарий');
  return ''; }
function rowHTML(h,i){ var ctx='', wh=whereOf(h);
  if(h.kind==='text'||h.kind==='card'){ var t=h.run.text, a=Math.max(0,h.start-26), b=Math.min(t.length,h.end+80); ctx=(a>0?'…':'')+E(t.slice(a,h.start))+'<b>'+E(t.slice(h.start,h.end))+'</b>'+E(t.slice(h.end,b))+(b<t.length?'…':''); }
  else ctx=E(h.text.slice(0,120));
  return '<li data-i="'+i+'"'+(i===cur?' class="cur"':'')+'><span class="fx">'+ctx.replace(/\s+/g,' ')+'</span>'+(wh?'<span class="fw">'+E(wh)+'</span>':'')+'</li>'; }
function E(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function renderList(){ list.innerHTML=''; RENDERED=0; if(!hits.length){ list.hidden=true; return; } list.hidden=false; more(); }
function more(){ var end=Math.min(hits.length,RENDERED+ROWS); var html=''; for(var i=RENDERED;i<end;i++) html+=rowHTML(hits[i],i); list.insertAdjacentHTML('beforeend',html); RENDERED=end;
  if(RENDERED<hits.length){ var li=document.createElement('li'); li.className='more'; li.textContent=T('… more','… ещё')+' ('+(hits.length-RENDERED)+')'; li.addEventListener('click',function(){ li.remove(); more(); }); list.appendChild(li); } }
function markRow(){ var rows=list.querySelectorAll('li.cur'); for(var i=0;i<rows.length;i++) rows[i].classList.remove('cur'); if(cur<0) return; var r=list.querySelector('li[data-i="'+cur+'"]'); if(r){ r.classList.add('cur'); try{ r.scrollIntoView({block:'nearest'}); }catch(e){} } }
list.addEventListener('click',function(ev){ var li=ev.target.closest('li[data-i]'); if(!li) return; go(parseInt(li.dataset.i,10)); });
function show(note){ if(!q.value.trim()){ cnt.textContent=''; where.textContent=''; if(mode) mode.textContent=''; return; }
  cnt.textContent=hits.length?((cur>=0?(cur+1):'—')+' / '+hits.length+(hits.length>=MAXH?'+':'')):(running?'…':T('no hits','нет совпадений'));
  var loading=document.documentElement.classList.contains('lang-loading')&&opts.scope!=='this';
  where.textContent=(note||'')+(loading?(' · '+T('the other language is still loading','другой язык ещё загружается')):''); }
// ---------- options: each button names its current state
function paintOpts(){ var c=document.getElementById('findcase'), w=document.getElementById('findword'), ln=document.getElementById('findlangname');
  c.innerHTML=opts.cs?'<span class="lang-en">case-sensitive</span><span class="lang-ru">с учётом регистра</span>':'<span class="lang-en">case-insensitive</span><span class="lang-ru">без учёта регистра</span>';
  w.innerHTML=opts.whole?'<span class="lang-en">whole word</span><span class="lang-ru">целое слово</span>':'<span class="lang-en">substring</span><span class="lang-ru">подстрока</span>';
  ln.textContent=opts.scope==='all'?T('all languages','все языки'):(opts.scope==='this'?(NATIVE[lang()]||lang()):(NATIVE[opts.scope]||opts.scope)); }
function langMenu(){ var m=document.getElementById('findlangmenu'); m.innerHTML=''; var items=[];
  LANGS.forEach(function(l){ items.push([l,NATIVE[l]||l]); }); items.push(['all',T('all languages','все языки')]);
  items.forEach(function(it){ var b=document.createElement('button'); b.type='button'; b.setAttribute('role','menuitem'); b.textContent=it[1]; var on=(it[0]==='all'&&opts.scope==='all')||(it[0]!=='all'&&(opts.scope===it[0]||(opts.scope==='this'&&it[0]===lang()))); if(on) b.className='on';
    b.addEventListener('click',function(){ opts.scope=(it[0]==='all')?'all':(it[0]===lang()?'this':it[0]); m.hidden=true; document.getElementById('findlang').setAttribute('aria-expanded','false'); paintOpts(); lastKey=''; if(q.value.trim()) run(false); }); m.appendChild(b); }); }
document.getElementById('findlang').addEventListener('click',function(){ var m=document.getElementById('findlangmenu'); if(m.hidden){ langMenu(); m.hidden=false; this.setAttribute('aria-expanded','true'); } else { m.hidden=true; this.setAttribute('aria-expanded','false'); } });
document.addEventListener('click',function(ev){ var m=document.getElementById('findlangmenu'); if(!m.hidden&&!ev.target.closest('.folang')){ m.hidden=true; document.getElementById('findlang').setAttribute('aria-expanded','false'); } });
function tog(id,key){ var b=document.getElementById(id); b.addEventListener('click',function(){ opts[key]=!opts[key]; paintOpts(); lastKey=''; if(q.value.trim()) run(false); }); }
tog('findcase','cs'); tog('findword','whole');
// ---------- open (where it was called), close, keys
var lastPos=null;
function place(ev){ var vw=window.innerWidth, vh=window.innerHeight; if(vw<=700){ bar.style.left=''; bar.style.top=''; bar.style.right=''; return; }
  var w=Math.min(560,vw-32), x, y; if(ev&&typeof ev.clientX==='number'&&(ev.clientX||ev.clientY)){ x=ev.clientX-24; y=ev.clientY+14; lastPos={x:x,y:y}; } else if(lastPos){ x=lastPos.x; y=lastPos.y; } else { x=vw-w-16; y=10; }
  x=Math.max(8,Math.min(vw-w-8,x)); y=Math.max(8,Math.min(vh-160,y)); bar.style.left=x+'px'; bar.style.top=y+'px'; bar.style.right='auto'; bar.style.width=w+'px'; }
function open(ev){ place(ev); bar.hidden=false; document.body.classList.add('has-find'); paintOpts(); q.focus(); try{ q.select(); }catch(e){} if(q.value.trim()&&!hits.length) run(false); }
function close(){ bar.hidden=true; document.body.classList.remove('has-find'); if(running) running.stop=true; running=null; clearHL(); hits=[]; cur=-1; lastKey=''; list.hidden=true; list.innerHTML=''; }
function run(jump){ var v=q.value.trim(); var key=v+'|'+opts.cs+'|'+opts.whole+'|'+opts.scope+'|'+lang();
  if(!v){ if(running) running.stop=true; running=null; clearHL(); hits=[]; cur=-1; lastKey=''; list.hidden=true; list.innerHTML=''; show(); return; }
  if(key===lastKey&&!running){ if(jump) go(cur+1); return; }
  lastKey=key; search(v,function(){ if(jump&&hits.length) go(0); }); }
var typing=null;
q.addEventListener('input',function(){ clearTimeout(typing); typing=setTimeout(function(){ run(false); },220); });
q.addEventListener('keydown',function(ev){ if(ev.key==='Enter'){ ev.preventDefault(); clearTimeout(typing); if(running){ running.then=true; } if(ev.shiftKey&&hits.length) go(cur-1); else if(hits.length&&lastKey===q.value.trim()+'|'+opts.cs+'|'+opts.whole+'|'+opts.scope+'|'+lang()) go(cur+1); else run(true); } else if(ev.key==='Escape'){ ev.preventDefault(); close(); } });
q.addEventListener('search',function(){ if(!q.value){ run(false); } });
document.querySelectorAll('[data-findopen]').forEach(function(b){ b.addEventListener('click',function(ev){ if(bar.hidden) open(ev); else close(); }); });
document.getElementById('findclose').addEventListener('click',close);
document.getElementById('findnext').addEventListener('click',function(){ if(!hits.length) run(true); else go(cur+1); });
document.getElementById('findprev').addEventListener('click',function(){ if(!hits.length) run(true); else go(cur-1); });
document.addEventListener('keydown',function(ev){ var t=ev.target; var typing=t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.tagName==='SELECT'||t.isContentEditable);
  if(!typing&&ev.key==='/'&&!ev.ctrlKey&&!ev.metaKey&&!ev.altKey){ ev.preventDefault(); open(null); }
  else if((ev.ctrlKey||ev.metaKey)&&!ev.shiftKey&&!ev.altKey&&(ev.key==='k'||ev.key==='K')){ ev.preventDefault(); open(null); }
  else if(ev.key==='Escape'&&!bar.hidden&&t!==q){ close(); } });
document.querySelectorAll('[data-setlang]').forEach(function(b){ b.addEventListener('click',function(){ setTimeout(function(){ paintOpts(); index=null; lastKey=''; if(!bar.hidden&&q.value.trim()) run(false); },0); }); });
window.__find={open:open,close:close,search:function(v,o,cb){ if(o) Object.assign(opts,o); paintOpts(); q.value=v; lastKey=''; return new Promise(function(res){ search(v,function(){ res(hits.length); }); }); },go:go,hits:function(){ return hits; },cur:function(){ return cur; },opts:opts,running:function(){ return !!running; }};
})();'''
