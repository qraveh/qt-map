# -*- coding: utf-8 -*-
"""Find in the Atlas (the editor's request of 28 Sep 2026): one search over everything the page holds, including what is
folded, closed or in the other language, walked hit by hit the way a browser's find walks a page.

What it searches. Every text node of the page — the report, the briefs (closed ones too), the glossary, the tables, the
map's own labels — plus the tooltips, aria-labels and alt texts (metadata), in both languages (the other language's
fragment is in the page once it has loaded), and the map's cards, which are built from data: technology names and
descriptions, machine names and organisations, architecture names. Not searched: the record pages (technology/, machine/,
organisation/), which are separate documents — a site search reaches them.

How. The index is built at query time from the live DOM: the page is walked into "runs" — the text of one block-level
element (or of one language span inside it) as one string with a map back to its text nodes — so a phrase spanning
<b>, <a> or <em> still matches. The query is literal except * (any run of characters) and ? (one character); a space
matches any whitespace; options: match case, whole word, language scope (this / the other / both). Hits are listed in
document order; Enter / ▼ and Shift+Enter / ▲ walk them, "k of N"; each step reveals what hides the hit — a folded
section, a closed brief, a collapsed map bar, the other language — scrolls it into view and highlights it (the CSS
Custom Highlight API; a <mark> where the API is missing). A hit in a card opens the card on the map.
"""

FIND_HTML = r'''<div class="findbar" id="findbar" hidden role="search" aria-label="find in the Atlas">
 <div class="findrow">
  <input type="search" id="findq" class="findq" autocomplete="off" spellcheck="false" placeholder="find… (* any run, ? one character)" aria-label="find in the Atlas — * any run of characters, ? one character, Enter next, Shift+Enter previous">
  <span class="findcount" id="findcount" aria-live="polite"></span>
  <button type="button" class="fb" id="findprev" aria-label="previous hit (Shift+Enter)" title="previous (Shift+Enter)">▲</button>
  <button type="button" class="fb" id="findnext" aria-label="next hit (Enter)" title="next (Enter)">▼</button>
  <button type="button" class="fb findclose" id="findclose" aria-label="close (Escape)" title="close (Escape)">✕</button>
 </div>
 <div class="findopts">
  <button type="button" class="fo" id="findcase" aria-pressed="false" title="match case">Aa</button>
  <button type="button" class="fo" id="findword" aria-pressed="false" title="whole word"><span class="lang-en">word</span><span class="lang-ru">слово</span></button>
  <span class="fosep"></span>
  <span class="folbl"><span class="lang-en">in</span><span class="lang-ru">где</span></span>
  <button type="button" class="fo" data-findscope="this" aria-pressed="true"><span class="lang-en">this language</span><span class="lang-ru">этот язык</span></button>
  <button type="button" class="fo" data-findscope="other" aria-pressed="false"><span class="lang-en">the other</span><span class="lang-ru">другой</span></button>
  <button type="button" class="fo" data-findscope="all" aria-pressed="false"><span class="lang-en">both</span><span class="lang-ru">оба</span></button>
  <span class="findwhere" id="findwhere"></span>
 </div>
</div>'''

FIND_JS = r'''(function(){
var bar=document.getElementById('findbar'), q=document.getElementById('findq'), cnt=document.getElementById('findcount'), where=document.getElementById('findwhere');
if(!bar||!q) return;
var app=document.getElementById('app');
function lang(){ return (app&&app.getAttribute('data-lang'))||'en'; }
function otherLang(){ return lang()==='en'?'ru':'en'; }
var T=function(en,ru){ return lang()==='ru'?ru:en; };
var opts={caseSens:false, word:false, scope:'this'};
var hits=[], cur=-1, lastKey='', built=null;
var HL=!!(window.CSS&&CSS.highlights&&window.Highlight);
// ---------- the walk: runs of text with a map back to the nodes
var SKIP={SCRIPT:1,STYLE:1,TEMPLATE:1,NOSCRIPT:1,CANVAS:1,SELECT:1,OPTION:1,TEXTAREA:1,INPUT:1,IFRAME:1,OBJECT:1};
var BLOCK={P:1,DIV:1,LI:1,UL:1,OL:1,TABLE:1,THEAD:1,TBODY:1,TFOOT:1,TR:1,TD:1,TH:1,H1:1,H2:1,H3:1,H4:1,H5:1,H6:1,SECTION:1,ARTICLE:1,ASIDE:1,DL:1,DT:1,DD:1,DETAILS:1,SUMMARY:1,FIGURE:1,FIGCAPTION:1,BLOCKQUOTE:1,PRE:1,NAV:1,HEADER:1,FOOTER:1,MAIN:1,FORM:1,FIELDSET:1,LABEL:1,BUTTON:1,HR:1,BR:1,svg:1,SVG:1,text:1,g:1,tspan:1};
var EXCL='#findbar,#insp,#maptip,nav.toc,#tocdrawer,#tocbackdrop,.fbkpop,.langwait,#gtip,.tip';
function langOf(el){ var c=el.classList; if(!c) return null; if(c.contains('lang-en')) return 'en'; if(c.contains('lang-ru')) return 'ru'; return null; }
function build(){
  var runs=[], metas=[];
  function textNodesOf(el,out){ var c=el.childNodes; for(var i=0;i<c.length;i++){ var n=c[i]; if(n.nodeType===3) out.push(n); else if(n.nodeType===1&&!SKIP[n.tagName]&&!n.matches(EXCL)) textNodesOf(n,out); } }
  function flush(run,lg){ if(!run.length) return; var nodes=[]; for(var i=0;i<run.length;i++){ var n=run[i]; if(n.nodeType===3) nodes.push(n); else textNodesOf(n,nodes); }
    if(!nodes.length) return; var segs=[], text='', pos=0;
    for(var k=0;k<nodes.length;k++){ var t=nodes[k].nodeValue; if(!t) continue; segs.push({node:nodes[k],start:pos,end:pos+t.length}); text+=t; pos+=t.length; }
    if(text.trim()) runs.push({text:text,segs:segs,lang:lg}); }
  function meta(el,lg){ var a=['title','aria-label','alt']; for(var i=0;i<a.length;i++){ var v=el.getAttribute&&el.getAttribute(a[i]); if(v&&v.trim()) metas.push({el:el,attr:a[i],text:v,lang:lg}); } }
  function walk(el,lg){
    if(el.nodeType!==1||SKIP[el.tagName]||el.matches(EXCL)) return;
    var l=langOf(el)||lg; meta(el,l);
    var run=[], c=el.childNodes;
    for(var i=0;i<c.length;i++){ var n=c[i];
      if(n.nodeType===3){ run.push(n); continue; }
      if(n.nodeType!==1) continue;
      if(SKIP[n.tagName]||n.matches(EXCL)){ flush(run,l); run=[]; continue; }
      if(BLOCK[n.tagName]||langOf(n)||n.querySelector('p,div,li,table,h1,h2,h3,h4,dl,details,figure,section,.lang-en,.lang-ru')){ flush(run,l); run=[]; walk(n,l); }
      else { run.push(n); meta(n,l); var inl=n.querySelectorAll('[title],[aria-label],[alt]'); for(var j=0;j<inl.length;j++) meta(inl[j],l); }
    }
    flush(run,l);
  }
  walk(document.body,null);
  // the map's cards are built from data: names and descriptions of technologies, machines and architectures
  var cards=[]; try{
    var G=window.__GRAPH, M=window.__MACH;
    if(G){ G.nodes.forEach(function(n){ ['en','ru'].forEach(function(L){ cards.push({kind:'node',id:n.id,lang:L,text:(n[L]||'')+' — '+((n.desc&&n.desc[L])||'')+' ('+n.id+')'}); }); });
      (G.paths||[]).forEach(function(p){ ['en','ru'].forEach(function(L){ cards.push({kind:'path',id:p.id,lang:L,text:(p[L]||'')+' ('+p.id+')'}); }); }); }
    if(M&&M.machines) M.machines.forEach(function(m){ cards.push({kind:'machine',id:m.id,lang:null,text:(m.name||'')+' · '+(m.org||'')+' ('+m.id+')'}); });
  }catch(e){}
  return {runs:runs,metas:metas,cards:cards};
}
// ---------- the query
function esc(s){ return s.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&'); }
function makeRe(query){ var parts=query.split(/(\*|\?|\s+)/).filter(function(x){return x!=='';}).map(function(x){ if(x==='*') return '[^\\n]*?'; if(x==='?') return '.'; if(/^\s+$/.test(x)) return '\\s+'; return esc(x); });
  var src=parts.join(''); if(!src) return null;
  if(opts.word) src='(?<![\\p{L}\\p{N}_])(?:'+src+')(?![\\p{L}\\p{N}_])';
  try{ return new RegExp(src,'gu'+(opts.caseSens?'':'i')); }catch(e){ try{ return new RegExp(src,'g'+(opts.caseSens?'':'i')); }catch(e2){ return null; } } }
function inScope(lg){ if(!lg) return true; if(opts.scope==='all') return true; if(opts.scope==='this') return lg===lang(); return lg===otherLang(); }
function search(query){
  clearHL(); hits=[]; cur=-1;
  var re=makeRe(query); if(!re){ show(); return; }
  built=build();
  var MAXH=3000, n=0;
  built.runs.forEach(function(r){ if(n>=MAXH||!inScope(r.lang)) return; re.lastIndex=0; var m; while((m=re.exec(r.text))){ if(!m[0].length){ re.lastIndex++; continue; } hits.push({kind:'text',run:r,start:m.index,end:m.index+m[0].length,lang:r.lang}); if(++n>=MAXH) break; } });
  built.metas.forEach(function(x){ if(n>=MAXH||!inScope(x.lang)) return; re.lastIndex=0; var m=re.exec(x.text); if(m){ hits.push({kind:'meta',el:x.el,attr:x.attr,text:x.text,lang:x.lang}); n++; } });
  built.cards.forEach(function(c){ if(n>=MAXH||!inScope(c.lang)) return; re.lastIndex=0; var m=re.exec(c.text); if(m){ hits.push({kind:c.kind,id:c.id,text:c.text,lang:c.lang}); n++; } });
  paintAll(); if(hits.length){ go(0); } else show();
}
// ---------- highlight
function rangeOf(h){ var r=document.createRange(), s=null, e=null;
  for(var i=0;i<h.run.segs.length;i++){ var g=h.run.segs[i]; if(s===null&&h.start<g.end){ s=g; r.setStart(g.node,h.start-g.start); } if(h.end<=g.end){ e=g; r.setEnd(g.node,h.end-g.start); break; } }
  if(s===null||e===null) return null; return r; }
function clearHL(){ if(HL){ CSS.highlights.delete('findall'); CSS.highlights.delete('findcur'); } var ms=document.querySelectorAll('mark.findmark'); for(var i=0;i<ms.length;i++){ var m=ms[i]; var p=m.parentNode; while(m.firstChild) p.insertBefore(m.firstChild,m); p.removeChild(m); }
  var os=document.querySelectorAll('.findout'); for(var j=0;j<os.length;j++) os[j].classList.remove('findout'); }
function paintAll(){ if(!HL) return; try{ var H=new Highlight(); hits.forEach(function(h){ if(h.kind==='text'){ var r=rangeOf(h); if(r) H.add(r); } }); CSS.highlights.set('findall',H); }catch(e){} }
function paintCur(h){ if(h.kind!=='text') return; var r=rangeOf(h); if(!r) return;
  if(HL){ try{ var H=new Highlight(); H.add(r); CSS.highlights.set('findcur',H); return; }catch(e){} }
  try{ var m=document.createElement('mark'); m.className='findmark'; r.surroundContents(m); }catch(e){ var el=r.startContainer.parentElement; if(el) el.classList.add('findout'); } }
// ---------- reveal what hides a hit
function revealEl(el){
  var lgEl=el.closest&&el.closest('.lang-en,.lang-ru'); var lg=lgEl?(lgEl.classList.contains('lang-ru')?'ru':'en'):null;
  if(lg&&lg!==lang()&&window.__setLang) window.__setLang(lg);
  for(var p=el;p;p=p.parentElement){
    if(p.tagName==='DETAILS'&&!p.open) p.open=true;
    if(p.hidden){ if(p.classList.contains('secbody')&&window.__setFold) window.__setFold(p.dataset.sec,true,false);
      else if(p.classList.contains('brief')&&window.__openBrief){ window.__openBrief(p.id.replace(/^brief-/,''),true); }
      else if(p.id==='barsum'){ /* the bar's summary line: shown only when collapsed */ }
      else p.hidden=false; }
    if(p.id==='mapbar'&&p.classList.contains('collapsed')&&window.__setBarCollapsed) window.__setBarCollapsed(false);
    if(p.id==='mapbody'&&window.__expandMap) window.__expandMap();
  }
}
function visible(el){ var r=el.getBoundingClientRect ? el.getBoundingClientRect() : null; return !!(r&&(r.width||r.height)); }
function scrollTo(el,rect){ try{ el.scrollIntoView({block:'center',inline:'nearest'}); }catch(e){ el.scrollIntoView(); } }
function go(i){ if(!hits.length){ show(); return; } i=((i%hits.length)+hits.length)%hits.length; cur=i; var h=hits[i];
  if(HL) CSS.highlights.delete('findcur'); var ms=document.querySelectorAll('mark.findmark'); for(var k=0;k<ms.length;k++){ var m=ms[k]; var p=m.parentNode; while(m.firstChild) p.insertBefore(m.firstChild,m); p.removeChild(m); }
  var os=document.querySelectorAll('.findout'); for(var j=0;j<os.length;j++) os[j].classList.remove('findout');
  if(h.kind==='text'){ var el=h.run.segs[0].node.parentElement; if(!el){ show(); return; } revealEl(el);
    var r=rangeOf(h); var host=r?(r.startContainer.parentElement||el):el; if(!visible(host)){ /* hidden by something the page does not expose: say so and move on */ show(T('hidden here','скрыто здесь')); return; }
    scrollTo(host); paintCur(h); show(); }
  else if(h.kind==='meta'){ revealEl(h.el); if(visible(h.el)){ scrollTo(h.el); h.el.classList.add('findout'); } show((h.attr==='title'?T('tooltip: ','подсказка: '):h.attr+': ')+h.text.slice(0,140)); }
  else if(h.kind==='node'){ if(window.__expandMap) window.__expandMap(); if(window.__selectNode) window.__selectNode(h.id); var w=document.getElementById('mapwrap'); if(w) scrollTo(w); show(T('technology card: ','карточка технологии: ')+h.text.slice(0,120)); }
  else if(h.kind==='machine'){ if(window.__expandMap) window.__expandMap(); if(window.__showMachine) window.__showMachine(h.id); var w2=document.getElementById('mapwrap'); if(w2) scrollTo(w2); show(T('machine card: ','карточка машины: ')+h.text.slice(0,120)); }
  else if(h.kind==='path'){ if(window.__expandMap) window.__expandMap(); if(window.__isolatePath) window.__isolatePath(h.id); var w3=document.getElementById('mapwrap'); if(w3) scrollTo(w3); show(T('architecture card: ','карточка архитектуры: ')+h.text.slice(0,120)); }
}
function show(note){ if(!q.value){ cnt.textContent=''; where.textContent=''; return; }
  cnt.textContent=hits.length?((cur+1)+' / '+hits.length+(hits.length>=3000?'+':'')):T('no hits','нет совпадений');
  var loading=document.documentElement.classList.contains('lang-loading')&&opts.scope!=='this';
  where.textContent=(note||'')+(loading?(' · '+T('the other language is still loading','другой язык ещё загружается')):''); }
// ---------- open / close / keys
function open(){ bar.hidden=false; document.body.classList.add('has-find'); q.focus(); try{ q.select(); }catch(e){} }
function close(){ bar.hidden=true; document.body.classList.remove('has-find'); clearHL(); hits=[]; cur=-1; lastKey=''; }
function run(){ var v=q.value.trim(); var key=v+'|'+opts.caseSens+'|'+opts.word+'|'+opts.scope+'|'+lang(); if(!v){ clearHL(); hits=[]; cur=-1; show(); return; } if(key===lastKey&&hits.length){ go(cur+1); return; } lastKey=key; search(v); }
document.querySelectorAll('[data-findopen]').forEach(function(b){ b.addEventListener('click',function(){ if(bar.hidden) open(); else close(); }); });
document.getElementById('findclose').addEventListener('click',close);
document.getElementById('findnext').addEventListener('click',function(){ if(!hits.length) run(); else go(cur+1); });
document.getElementById('findprev').addEventListener('click',function(){ if(!hits.length) run(); else go(cur-1); });
q.addEventListener('keydown',function(ev){ if(ev.key==='Enter'){ ev.preventDefault(); if(ev.shiftKey&&hits.length) go(cur-1); else run(); } else if(ev.key==='Escape'){ ev.preventDefault(); close(); } });
q.addEventListener('input',function(){ if(!q.value){ clearHL(); hits=[]; cur=-1; lastKey=''; show(); } });
q.addEventListener('search',function(){ if(!q.value){ clearHL(); hits=[]; cur=-1; lastKey=''; show(); } });
function tog(id,key){ var b=document.getElementById(id); b.addEventListener('click',function(){ opts[key]=!opts[key]; b.setAttribute('aria-pressed',String(opts[key])); lastKey=''; if(q.value.trim()) run(); }); }
tog('findcase','caseSens'); tog('findword','word');
document.querySelectorAll('[data-findscope]').forEach(function(b){ b.addEventListener('click',function(){ opts.scope=b.dataset.findscope; document.querySelectorAll('[data-findscope]').forEach(function(x){ x.setAttribute('aria-pressed',String(x===b)); }); lastKey=''; if(q.value.trim()) run(); }); });
document.addEventListener('keydown',function(ev){ var t=ev.target; var typing=t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.tagName==='SELECT'||t.isContentEditable);
  if(!typing&&ev.key==='/'&&!ev.ctrlKey&&!ev.metaKey&&!ev.altKey){ ev.preventDefault(); open(); }
  else if((ev.ctrlKey||ev.metaKey)&&!ev.shiftKey&&!ev.altKey&&(ev.key==='k'||ev.key==='K')){ ev.preventDefault(); open(); }
  else if(ev.key==='Escape'&&!bar.hidden&&t!==q){ close(); } });
window.__find={open:open,close:close,search:function(v,o){ if(o) Object.assign(opts,o); q.value=v; lastKey=''; run(); return hits.length; },go:go,hits:function(){ return hits; },cur:function(){ return cur; }};
})();'''
