JS = r"""
(function(){
'use strict';
const KEYREFS=window.__KEYREFS||{}; const G=window.__GRAPH, SHORT=window.__SHORT;
const app=document.getElementById('app');
const lang=()=>app.getAttribute('data-lang')||'en';
const T=(en,ru)=>lang()==='en'?en:ru;
const FAMC={SC:'var(--sc)',ION:'var(--ion)',ATOM:'var(--atom)',PHOTON:'var(--photon)',SPIN:'var(--spin)',DEFECT:'var(--defect)',TOPO:'var(--topo)',ANNEAL:'var(--anneal)'};
const FAMN={SC:['superconducting','сверхпроводники'],ION:['ions','ионы'],ATOM:['atoms','атомы'],PHOTON:['photonics','фотоника'],SPIN:['spins','спины'],DEFECT:['defects','дефекты'],TOPO:['topological','топологические'],ANNEAL:['annealing','отжиг']};
const NEUTRAL=new Set(['TOPO','ANNEAL']);
const NODE=Object.fromEntries(G.nodes.map(n=>[n.id,n]));
const PATH=Object.fromEntries(G.paths.map(p=>[p.id,p]));
const V=G.vocab;
const vt=(tab,key)=>{const e=V[tab][String(key)]; return e?(lang()==='en'?e[0]:e[1]):String(key);};
const fmtN=v=>v>=100?v.toFixed(0):(v>=10?v.toFixed(0):v.toPrecision(2)); const fmtT=x=>{if(x==null)return '—';const v=Math.pow(10,x);if(v>=1)return fmtN(v)+' s';if(v>=1e-3)return fmtN(v*1e3)+' ms';if(v>=1e-6)return fmtN(v*1e6)+' µs';return fmtN(v*1e9)+' ns';};
// ---------- primary path membership
const prim={}, alt={};
G.paths.forEach(p=>{Object.entries(p.slots).forEach(([L,ids])=>{ids.forEach((id,i)=>{(i===0?prim:alt)[id]=(i===0?prim:alt)[id]||[]; (i===0?prim:alt)[id].push(p.id);});});});
const famOf=id=>{const ps=(prim[id]||[]).concat(alt[id]||[]); return ps.length?PATH[ps[0]].family:null;};
const famsOf=id=>[...new Set((prim[id]||[]).concat(alt[id]||[]).map(p=>PATH[p].family))];
// ---------- layout
const COLW=141, NW=124, NH=40, ROWH=48, X0=64, Y0=64, BANDGAP=26;
const BANDS=[0,0.25,0.5,0.75,1];
const bandIdx=a=>BANDS.indexOf(a);
const byLayer={}; G.nodes.forEach(n=>{(byLayer[n.layer]=byLayer[n.layer]||[]).push(n);});
const maxc=BANDS.map((b,bi)=>Math.max(...Object.values(byLayer).map(ns=>ns.filter(n=>bandIdx(n.aff)===bi).length)));
const bandTop=[]; let yy=Y0; BANDS.forEach((b,bi)=>{bandTop.push(yy); yy+= (maxc[bi]||0)*ROWH + (maxc[bi]?BANDGAP:0);});
const H=yy+10, W=X0+10*COLW+16;
const statusRank={D:0,E:1,T:2,X:3};
G.nodes.forEach(n=>{n._fam=famOf(n.id); n._fams=famsOf(n.id);});
Object.values(byLayer).forEach(ns=>{
  BANDS.forEach((b,bi)=>{ns.filter(n=>bandIdx(n.aff)===bi).sort((a,c)=>(statusRank[a.status]-statusRank[c.status])||a.id.localeCompare(c.id)).forEach((n,i)=>{n.x=X0+(n.layer-1)*COLW; n.y=bandTop[bi]+i*ROWH; n.cx=n.x+NW/2; n.cy=n.y+NH/2;});});
});
// ---------- svg
const wrap=document.getElementById('mapwrap');
const svg=d3.select(wrap).append('svg').attr('viewBox',`0 0 ${W} ${H}`).attr('width',W).attr('height',H).attr('role','img').attr('aria-label','Technology map: ten stack layers as columns, carrier-nature affinity as rows, platform paths as coloured lines');
const defs=svg.append('defs');
defs.append('pattern').attr('id','hatch').attr('patternUnits','userSpaceOnUse').attr('width',6).attr('height',6).attr('patternTransform','rotate(45)').append('line').attr('x1',0).attr('y1',0).attr('x2',0).attr('y2',6).attr('stroke','var(--nat)').attr('stroke-width',1.2).attr('opacity',.55);
defs.append('marker').attr('id','arr').attr('viewBox','0 0 10 10').attr('refX',9).attr('refY',5).attr('markerWidth',7).attr('markerHeight',7).attr('orient','auto-start-reverse').append('path').attr('d','M0,0 L10,5 L0,10 z').attr('fill','var(--ink)');
const gBands=svg.append('g').attr('class','bandl'), gLanes=svg.append('g').attr('class','laneh'), gPaths=svg.append('g'), gAlt=svg.append('g'), gEdges=svg.append('g'), gNodes=svg.append('g');
// band labels + separators
BANDS.forEach((b,bi)=>{ if(!maxc[bi])return; const y0=bandTop[bi]-8;
  gBands.append('line').attr('class','bandline').attr('x1',X0-40).attr('x2',W-8).attr('y1',y0).attr('y2',y0);
  gBands.append('text').attr('x',X0-44).attr('y',y0+14).attr('text-anchor','end').attr('transform',`rotate(-90 ${X0-44} ${y0+14})`).text(''); });
const bandLabel=gBands.append('g');
// lane headers
const laneHead=gLanes.selectAll('g').data(G.layers).join('g').attr('transform',d=>`translate(${X0+(d.n-1)*COLW},0)`);
laneHead.append('text').attr('x',0).attr('y',18).attr('class','t');
laneHead.append('text').attr('x',0).attr('y',31).attr('class','t t2');
laneHead.append('text').attr('x',0).attr('y',44).attr('class','sub').text(d=>String(d.n).padStart(2,'0'));
// path offsets at shared primary nodes
const offsetAt={}; G.nodes.forEach(n=>{const ps=prim[n.id]||[]; ps.forEach((p,k)=>{offsetAt[p+'|'+n.id]=(k-(ps.length-1)/2)*4;});});
const line=d3.line().x(d=>d.x).y(d=>d.y).curve(d3.curveMonotoneX);
function pathPoints(p){const pts=[]; for(let L=1;L<=10;L++){const ids=p.slots[L]||[]; if(!ids.length)continue; const n=NODE[ids[0]]; pts.push({x:n.cx,y:n.cy+(offsetAt[p.id+'|'+n.id]||0),L});} return pts;}
const pathSel=gPaths.selectAll('path').data(G.paths).join('path').attr('class',d=>'pathline'+(NEUTRAL.has(d.family)?' neutral':'')).attr('d',d=>line(pathPoints(d))).attr('stroke',d=>FAMC[d.family]).attr('data-path',d=>d.id);
// empty-slot markers on paths
const emptyMarks=[]; G.paths.forEach(p=>{const pts=pathPoints(p); for(let L=1;L<=10;L++){const ids=p.slots[L]||[]; if(ids.length)continue; const prev=[...pts].reverse().find(q=>q.L<L)||pts[0]; emptyMarks.push({p,L,x:X0+(L-1)*COLW+NW/2,y:prev.y});}});
gPaths.selectAll('circle.empty').data(emptyMarks).join('circle').attr('class','emptyslot').attr('cx',d=>d.x).attr('cy',d=>d.y).attr('r',5).attr('fill','var(--surface)').attr('stroke',d=>FAMC[d.p.family]).attr('stroke-dasharray','2 2').attr('stroke-width',1.5).attr('data-path',d=>d.p.id).append('title');
// alternates stubs
const stubs=[]; G.paths.forEach(p=>{Object.entries(p.slots).forEach(([L,ids])=>{if(ids.length<2)return; const a=NODE[ids[0]]; ids.slice(1).forEach(id=>{const b=NODE[id]; stubs.push({p,a,b});});});});
gAlt.selectAll('path').data(stubs).join('path').attr('class','altstub').attr('stroke',d=>FAMC[d.p.family]).attr('data-path',d=>d.p.id).attr('d',d=>{const x=d.a.cx+NW/2-8; return `M${x},${d.a.cy} C${x+14},${d.a.cy} ${x+14},${d.b.cy} ${x},${d.b.cy}`;});
// nodes
function wrapLabel(s){ if(s.length<=17) return [s]; const w=s.split(' '); let a='',b=''; for(const x of w){ if((a+' '+x).trim().length<=17 && !b) a=(a+' '+x).trim(); else b=(b+' '+x).trim(); } if(b.length>19) b=b.slice(0,18)+'…'; return [a,b]; }
const st=gNodes.selectAll('g.station').data(G.nodes,d=>d.id).join('g').attr('class',d=>'station'+(d.status==='E'?' emerging':'')+(d.status==='X'?' empty':'')+(d.status==='T'?' theory':'')+(d.offdiag.length?' offd':'')+(d.hub?' hub':'')).attr('transform',d=>`translate(${d.x},${d.y})`).attr('tabindex',0).attr('role','button');
st.append('rect').attr('class','box').attr('width',NW).attr('height',NH).attr('rx',7);
st.append('rect').attr('class','lensbar').attr('x',0).attr('y',0).attr('width',4).attr('height',NH).attr('rx',2).attr('fill','transparent');
st.append('rect').attr('class','hatchov').attr('width',NW).attr('height',NH).attr('rx',7).attr('fill','url(#hatch)').attr('opacity',d=>d.offdiag.length?1:0).attr('pointer-events','none');
st.append('text').attr('class','l1').attr('x',9).attr('y',15);
st.append('text').attr('class','l2').attr('x',9).attr('y',27);
st.append('text').attr('class','id').attr('x',NW-6).attr('y',NH-5).attr('text-anchor','end').text(d=>d.id);
st.filter(d=>d.hub).append('circle').attr('cx',NW-8).attr('cy',8).attr('r',3.2).attr('fill','none').attr('stroke','var(--fab)').attr('stroke-width',1.6).append('title').text('hub');
st.filter(d=>d.offdiag.length).append('text').attr('x',NW-14).attr('y',12).attr('font-size',11).attr('fill','var(--nat)').attr('text-anchor','end').text('⤢');
// family badges
st.each(function(d){const g=d3.select(this); const fp=[...new Set((prim[d.id]||[]).map(p=>PATH[p].family))], fa=[...new Set((alt[d.id]||[]).map(p=>PATH[p].family))].filter(f=>!fp.includes(f)); let x=9;
  fp.forEach(f=>{g.append('rect').attr('class','badge').attr('x',x).attr('y',NH-9).attr('width',7).attr('height',4).attr('rx',1).attr('fill',FAMC[f]); x+=9;});
  fa.forEach(f=>{g.append('rect').attr('class','badge').attr('x',x+.5).attr('y',NH-8.5).attr('width',6).attr('height',3).attr('rx',1).attr('fill','none').attr('stroke',FAMC[f]).attr('stroke-width',1); x+=9;}); });
// tooltip
const tip=document.getElementById('maptip');
function placeTip(ev){ const r=wrap.getBoundingClientRect(); let x=ev.clientX-r.left+wrap.scrollLeft+14, y=ev.clientY-r.top+wrap.scrollTop+14; const tw=tip.offsetWidth, th=tip.offsetHeight; if(ev.clientX-r.left+14+tw>wrap.clientWidth) x=ev.clientX-r.left+wrap.scrollLeft-tw-14; if(ev.clientY-r.top+14+th>wrap.clientHeight) y=ev.clientY-r.top+wrap.scrollTop-th-14; tip.style.left=Math.max(wrap.scrollLeft,x)+'px'; tip.style.top=Math.max(wrap.scrollTop,y)+'px'; }
function stationTip(d){ const L=lang(); const k=state.lens; let h=`<b>${esc(d[L])}</b> <span style="opacity:.7">${d.id}</span><br>${vt('STATUS',d.status)} · ${d.since<2030?d.since:'—'} · ${T('layer','слой')} ${d.layer}`;
  const ps=(prim[d.id]||[]), as=(alt[d.id]||[]);
  if(ps.length||as.length) h+=`<br><span class="tk">${T('lines','линии')}</span> `+ps.map(p=>`<i class="sw" style="background:${FAMC[PATH[p].family]}"></i>${esc(PATH[p][L])}`).concat(as.map(p=>`<i class="sw hollow" style="border-color:${FAMC[PATH[p].family]}"></i>${esc(PATH[p][L])} <span style="opacity:.7">(${T('alternate','альтернатива')})</span>`)).join(' · ');
  if(k==='family'){ const f=d._fams; h+=`<br><span class="tk">${T('outline','рамка')}</span> ${f.length?f.map(x=>T(...FAMN[x])).join(' + '):'—'}`; }
  else { const c=lensColor(d,k); const v=lensValue(d,k); const lab=k==='aff'?vt('AFF',d.aff):(k==='time'?(v==='none'?T('no time','нет времени'):TBINS[+v][1]):catLabel(k,v)); h+=`<br><span class="tk">${T('lens','линза')}</span> ${esc(LENSES[k][L])}: <i class="sw" style="background:${c||'transparent'};border:1px solid ${c||'var(--bg)'}"></i>${esc(lab)}`; }
  const fl=[]; if(d.hub)fl.push('◎ '+T('hub','хаб')); if(d.offdiag&&d.offdiag.length)fl.push('⤢ '+T('off-diagonal','внедиагональный')); if(d.status==='X')fl.push('∅ '+T('empty slot','пустой слот')); if(fl.length)h+=`<br>${fl.join(' · ')}`;
  h+=`<br><span style="opacity:.6">${T('click for the card','клик — карточка')}</span>`; return h; }
st.on('mousemove',(ev,d)=>{tip.style.display='block'; tip.classList.add('wide'); tip.innerHTML=stationTip(d); placeTip(ev);}).on('mouseleave',()=>{tip.style.display='none'; tip.classList.remove('wide');});
st.on('click',(ev,d)=>{ev.stopPropagation(); tip.style.display='none'; select(d.id===state.focus?null:d.id);}).on('keydown',(ev,d)=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault(); select(d.id===state.focus?null:d.id);}});
svg.on('click',()=>select(null));
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')select(null);});
// ---------- state & rendering
const state={focus:null,isolate:null,lens:'family',lensFilter:null,showConf:false,showRep:false,showReq:false};
const LENSES={
 family:{en:'Platform family (paths)',ru:'Семейство платформ (пути)'},
 aff:{en:'(a) carrier affinity: natural ↔ fabricated',ru:'(a) сродство носителя: естественный ↔ изготовленный'},
 time:{en:'(b)/(c) characteristic time (gate or readout)',ru:'(b)/(c) характерное время (гейт или считывание)'},
 det:{en:'(b) entangling: deterministic / heralded',ru:'(b) перепутывание: детерминированное / heralded'},
 mech:{en:'(c) readout mechanism',ru:'(c) механизм считывания'},
 destr:{en:'(c) readout destructive?',ru:'(c) считывание разрушающее?'},
 mid:{en:'(c) mid-circuit readout?',ru:'(c) внутрисхемное считывание?'},
 d:{en:'(d) mobility / connectivity',ru:'(d) подвижность / связность'},
 mod:{en:'(e) control modality',ru:'(e) модальность управления'},
 place:{en:'(e) control placement (temperature stage)',ru:'(e) размещение управления (температурная ступень)'},
 f:{en:'(f) dominant error structure',ru:'(f) доминирующая структура ошибки'},
 g:{en:'(g) manufacturing technology',ru:'(g) технология производства'},
 status:{en:'— status (evaluation space)',ru:'— статус (пространство оценки)'}};
// categorical lens palette (deliberately not the family palette: while a lens is active, path lines turn neutral so colour means the lens value only)
const LENSPAL=['#3B6FD4','#E0862B','#2FA66A','#C94C6B','#7C5CC4','#C7A22B','#2AA5B8','#8B6A45','#D07AB5','#6E7F91'];
const CATS={
 mech:['disp','s2c','qcap','erasure','fluor','img','spd','none'], d:['static','longrange','shared','bus','transport','flying','none'],
 mod:['mw','lf','eo','opt','none'], place:['RT','4K','mK','vac','none'], f:['pauli','coherent','leak','burst','bias','gauss','erasure','loss','unknown','none'],
 g:['sclitho','3d','cmos','mbe','mems','pic','optics','stm','diamond','none'], status:['D','E','T','X'],
 det:['det','her','na'], destr:['yes','no','none'], mid:['yes','no','none']};
const VTAB={mech:'MECH',d:'MOB',mod:'MOD',place:'PLACE',f:'ERR',g:'FAB',status:'STATUS',det:'DET'};
const YESNO={yes:['yes','да'],no:['no','нет'],none:['no readout','без считывания']};
function catLabel(k,v){ if(k==='destr'||k==='mid')return T(...YESNO[v]); return vt(VTAB[k],v); }
function lensValue(n,k){ if(k==='mech')return n.c?n.c.mech:'none'; if(k==='d')return n.d; if(k==='mod')return n.e.mod; if(k==='place')return n.e.place; if(k==='f')return n.f[0]||'none'; if(k==='g')return n.g; if(k==='status')return n.status;
  if(k==='det')return n.b.det||'na'; if(k==='destr')return n.c?(n.c.destr?'yes':'no'):'none'; if(k==='mid')return n.c?(n.c.mid?'yes':'no'):'none'; if(k==='aff')return String(n.aff); if(k==='time'){const t=timeOf(n); return t==null?'none':timeBin(t);} return null;}
function timeOf(n){ if(n.b.t!=null)return n.b.t; if(n.c&&n.c.t!=null)return n.c.t; return null; }
const TBINS=[[-8.5,'≤ 3 ns'],[-7.5,'~30 ns'],[-6.5,'~300 ns'],[-5.5,'~3 µs'],[-4.5,'~30 µs'],[-3.5,'~300 µs'],[-2.5,'≥ 3 ms']];
function timeBin(t){ let best=0; TBINS.forEach((b,i)=>{ if(Math.abs(b[0]-t)<Math.abs(TBINS[best][0]-t))best=i; }); return String(best); }
// resolve CSS colour tokens at runtime (d3 cannot interpolate var(--x) strings); re-resolved on theme change
function css(v){ return getComputedStyle(document.documentElement).getPropertyValue(v).trim()||'#888'; }
let affScale=null, timeScale=null;
function buildScales(){ affScale=d3.scaleLinear().domain([0,0.5,1]).range([css('--nat'),css('--mid'),css('--fab')]).interpolate(d3.interpolateRgb); timeScale=d3.scaleLinear().domain([-8.5,-6.5,-4.5,-2.5]).range([css('--lens1'),css('--lens2'),css('--lens3'),css('--lens4')]).interpolate(d3.interpolateRgb).clamp(true); }
buildScales();
function lensColor(n,k){ if(k==='family')return null; if(k==='aff')return affScale(n.aff); if(k==='time'){const t=timeOf(n); return t==null?null:timeScale(t);} const v=lensValue(n,k); if(v==null||v==='none')return null; const i=CATS[k].indexOf(v); return i<0?null:LENSPAL[i%LENSPAL.length]; }
function tint(c){ const x=d3.color(c); if(!x)return 'var(--surface)'; x.opacity=0.22; return x.formatRgb(); }
function lensItems(k){ const count=v=>G.nodes.filter(n=>lensValue(n,k)===v).length;
  if(k==='family') return Object.keys(FAMC).map(f=>({c:FAMC[f],t:T(...FAMN[f]),v:f,n:G.nodes.filter(n=>n._fams.includes(f)).length}));
  if(k==='aff') return [0,0.25,0.5,0.75,1].map(a=>({c:affScale(a),t:vt('AFF',a),v:String(a),n:count(String(a))}));
  if(k==='time') return TBINS.map((b,i)=>({c:timeScale(b[0]),t:b[1],v:String(i),n:count(String(i))})).concat([{c:null,t:T('no time (code, decoder, fab)','нет времени (код, декодер, производство)'),v:'none',n:count('none')}]);
  return CATS[k].map(v=>({c:v==='none'?null:LENSPAL[CATS[k].indexOf(v)%LENSPAL.length],t:catLabel(k,v),v,n:count(v)})); }
function nodeMatchesFilter(n){ const k=state.lens, v=state.lensFilter; if(v==null)return true; if(k==='family')return n._fams.includes(v); return lensValue(n,k)===v; }
function applyLens(){ const k=state.lens; const leg=document.getElementById('lenslegend'); const lensed=k!=='family';
  svg.classed('lensed',lensed);
  st.select('rect.box').attr('stroke',d=>{ if(!lensed){ const f=d._fams; return f.length===1?FAMC[f[0]]:(f.length>1?'var(--ink)':'var(--mid)'); } const c=lensColor(d,k); return c||'var(--mid)'; })
    .attr('fill',d=>{ if(!lensed)return 'var(--surface)'; const c=lensColor(d,k); return c?tint(c):'var(--surface)'; });
  st.select('rect.lensbar').attr('fill',d=>{ if(!lensed)return 'transparent'; return lensColor(d,k)||'transparent'; });
  pcLines.selectAll('path').attr('stroke',d=>lensed?(lensColor(d,k)||'var(--mid)'):(d._fam?FAMC[d._fam]:'var(--mid)'));
  const items=lensItems(k).filter(it=>it.n>0);
  leg.innerHTML='<span class="lbl">'+T('lens legend · click a value to keep only those stations','легенда линзы · клик по значению оставляет только эти станции')+'</span>'+items.map(it=>`<button type="button" class="k lk" data-lv="${it.v}" aria-pressed="${String(state.lensFilter===it.v)}"><i class="sw" style="background:${it.c||'transparent'};border:1px solid ${it.c?it.c:'var(--mid)'}"></i>${esc(it.t)} <span class="cnt">${it.n}</span></button>`).join('')+(state.lensFilter!=null?`<button type="button" class="k lk clear" data-lv="">${T('clear filter','сбросить фильтр')} ✕</button>`:'');
  leg.querySelectorAll('[data-lv]').forEach(b=>{ b.addEventListener('click',()=>{ const v=b.dataset.lv; state.lensFilter=(v===''||state.lensFilter===v)?null:v; applyLens(); dimming(); pcHighlight(state.focus); });
    b.addEventListener('mouseenter',()=>{ const v=b.dataset.lv; if(v==='')return; st.classed('peek',d=>k==='family'?d._fams.includes(v):lensValue(d,k)===v); });
    b.addEventListener('mouseleave',()=>{ st.classed('peek',false); }); });
  if(state.focus) inspect(NODE[state.focus]);
}
const LENSROWS={aff:['aff'],time:['b','c'],det:['b'],mech:['c'],destr:['c'],mid:['c'],d:['d'],mod:['e'],place:['e'],f:['f'],g:['g']};
function relabel(){ st.select('text.l1').text(d=>wrapLabel(SHORT[d.id]?SHORT[d.id][lang()==='en'?0:1]:d.id)[0]); st.select('text.l2').text(d=>wrapLabel(SHORT[d.id]?SHORT[d.id][lang()==='en'?0:1]:d.id)[1]||'');
  laneHead.each(function(d){const s=lang()==='en'?d.en:d.ru; let a=s,b=''; if(s.length>16){ const i=s.indexOf(' / ')>0?s.indexOf(' / '):s.lastIndexOf(' '); a=s.slice(0,i); b=s.slice(i).replace(/^ \/ /,'/ ').trim(); } d3.select(this).select('text.t:not(.t2)').text(a); d3.select(this).select('text.t2').text(b);});
  bandLabel.selectAll('*').remove(); BANDS.forEach((b,bi)=>{ if(!maxc[bi])return; const y=bandTop[bi]+(maxc[bi]*ROWH)/2; bandLabel.append('text').attr('x',X0-30).attr('y',y).attr('text-anchor','middle').attr('transform',`rotate(-90 ${X0-30} ${y})`).text(vt('AFF',b).split(' ')[0].toUpperCase()); });
  gPaths.selectAll('circle.emptyslot').select('title').text(d=>T('empty slot: ','пустой слот: ')+d.p[lang()]+' — '+G.layers[d.L-1][lang()]);
  document.querySelectorAll('[data-chip-path]').forEach(b=>{b.querySelector('span.t').textContent=PATH[b.dataset.chipPath][lang()];});
  document.querySelectorAll('#lens option').forEach(o=>{o.textContent=LENSES[o.value][lang()];});
  applyLens(); if(state.focus)inspect(NODE[state.focus]); else if(state.isolate)inspectPath(PATH[state.isolate]); else inspectEmpty(); renderPC();
}
function select(id){ state.focus=id; st.classed('sel',d=>d.id===id); drawEdges(); dimming(); if(id){insp.hidden=false; inspect(NODE[id]);} else {insp.hidden=true; insp.innerHTML='';} pcHighlight(id); }
function neighbours(id){ const s=new Set([id]); G.edges.forEach(e=>{ if(e.type==='defines'||e.type==='transfers')return; if(e.src===id)s.add(e.dst); if(e.dst===id)s.add(e.src); }); return s; }
function dimming(){ const f=state.focus, iso=state.isolate;
  let keepN=null, keepP=null;
  if(iso){ keepP=new Set([iso]); keepN=new Set(Object.values(PATH[iso].slots).flat()); }
  if(f){ const ps=new Set((prim[f]||[]).concat(alt[f]||[])); keepP=keepP?new Set([...keepP].filter(p=>ps.has(p))):ps; const nb=neighbours(f); keepN=keepN?new Set([...keepN].filter(n=>nb.has(n)||n===f)):nb; keepN.add(f); }
  if(state.lensFilter!=null){ const lf=new Set(G.nodes.filter(nodeMatchesFilter).map(n=>n.id)); keepN=keepN?new Set([...keepN].filter(x=>lf.has(x))):lf; }
  st.classed('dim',d=>keepN?!keepN.has(d.id):false); st.classed('member',d=>iso?!!(PATH[iso].slots&&Object.values(PATH[iso].slots).flat().includes(d.id)):false);
  pathSel.classed('dim',d=>keepP?!keepP.has(d.id):false);
  gAlt.selectAll('path').classed('dim',d=>keepP?!keepP.has(d.p.id):false);
  gPaths.selectAll('circle.emptyslot').attr('opacity',d=>keepP?(keepP.has(d.p.id)?1:.08):1);
}
function edgePath(a,b){ const dx=b.cx-a.cx; if(Math.abs(dx)<1){ const x=a.cx+NW/2; return `M${a.cx+NW/2-2},${a.cy} C${x+22},${a.cy} ${x+22},${b.cy} ${b.cx+NW/2-2},${b.cy}`; }
  const sx=dx>0?a.cx+NW/2:a.cx-NW/2, tx=dx>0?b.cx-NW/2:b.cx+NW/2; const mx=(sx+tx)/2; return `M${sx},${a.cy} C${mx},${a.cy} ${mx},${b.cy} ${tx},${b.cy}`; }
function drawEdges(){ gEdges.selectAll('*').remove(); const f=state.focus; const es=G.edges.filter(e=>{ if(e.type==='defines'||e.type==='transfers')return false; if(e.type==='conflicts'&&state.showConf)return true; if(e.type==='replaces'&&state.showRep)return true; if(e.type==='requires'&&state.showReq)return true; return f&&(e.src===f||e.dst===f); });
  const ETYPE={requires:['requires','требует'],replaces:['is an alternative to','— альтернатива для'],conflicts:['conflicts with','конфликтует с']};
  const edgeTip=e=>{const L=lang(); const a=NODE[e.src][L], b=NODE[e.dst][L]; let h=`<b>${esc(a)}</b> ${T(...ETYPE[e.type])} <b>${esc(b)}</b>${e.any?' <span style="opacity:.7">('+T('one-of','одно из')+')</span>':''}`;
    if(e[L]) h+=`<br>${esc(e[L])}`;
    if(e.type==='conflicts'&&e.price){ h+=`<br><span class="tk">${T('price','цена')}</span> ${esc(e.price[L])}<br><span class="tk">${T('mitigation','снятие')}</span> ${esc(e.mitig[L])}<br><span class="tk">${T('status','статус')}</span> ${esc(vt('CONSTAT',e.status))} · ${e.date}`; }
    return h; };
  const g=gEdges.selectAll('g').data(es).join('g').attr('class',e=>'edge '+e.type);
  g.append('path').attr('class','hit').attr('d',e=>edgePath(NODE[e.src],NODE[e.dst]));
  g.append('path').attr('class','vis').attr('d',e=>edgePath(NODE[e.src],NODE[e.dst])).attr('marker-end',e=>e.type==='requires'?'url(#arr)':null);
  g.on('mousemove',(ev,e)=>{tip.style.display='block'; tip.classList.add('wide'); tip.innerHTML=edgeTip(e); placeTip(ev);}).on('mouseleave',()=>{tip.style.display='none'; tip.classList.remove('wide');})
   .on('click',(ev,e)=>{ev.stopPropagation(); if(e.type==='conflicts'){ select(state.focus===e.src?e.dst:e.src); }}); }
// ---------- inspector
const insp=document.getElementById('insp');
function esc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function lk(s){ return esc(s).replace(/arXiv:\s?((?:\d{4}\.\d{4,5}|[a-z\-]+\/\d{7})(?:v\d+)?)/g,(m,id)=>`<a href="https://arxiv.org/abs/${id}" target="_blank" rel="noopener">${m}</a>`).replace(/\b(10\.\d{4,9}\/[^\s,;)]+)/g,(m,d)=>`<a href="https://doi.org/${d}" target="_blank" rel="noopener">${m}</a>`).replace(/(?<!href=")(https?:\/\/[^\s<)]+)/g,u=>`<a href="${u}" target="_blank" rel="noopener">${u}</a>`); }
function inspectPath(p){ const L=lang(); insp.hidden=false;
  const members=new Set(Object.values(p.slots).flat());
  const rows=G.layers.map(l=>{const ids=p.slots[String(l.n)]||[]; return `<tr><td class="ln">${l.n} ${esc(l[L])}</td><td>${ids.length?ids.map((id,i)=>`<a href="#" data-goto="${id}" class="${i?'alt':'prim'}">${esc(NODE[id][L])}</a>`).join('<span class="empty"> · </span>'):`<span class="empty">∅ ${T('empty slot','пустой слот')}</span>`}</td></tr>`;}).join('');
  const R=p.round||{}, RP=R.parts||{}, RX=p.react||{}, CO=p.coh||{}; const PN={gates:['gates','гейты'],transport:['transport','транспорт'],'1q':['1Q','1Q'],readout:['readout','считывание'],reset:['reset','сброс']};
  const fS=x=>{if(x==null)return '—'; if(x===0)return '0'; return fmtT(Math.log10(x));}; const fE=x=>x==null?'—':x.toExponential(1).replace('e+','e').replace('e-','e−');
  const hubs=[...members].filter(id=>NODE[id].hub), offs=[...members].filter(id=>NODE[id].offdiag&&NODE[id].offdiag.length), empties=[...members].filter(id=>NODE[id].status==='X');
  insp.innerHTML=`<div class="grip" data-grip="1">⠿ <span class="sp"></span><button type="button" data-dock="left" title="dock left">⇤</button><button type="button" data-dock="right" title="dock right">⇥</button><button type="button" data-close="1" aria-label="close">✕</button></div><h3><i class="sw" style="--c:${FAMC[p.family]}"></i> ${esc(p[L])}</h3><div class="meta">${T('platform path','путь платформы')} · ${p.id} · ${members.size} ${T('stations','станций')}</div>
  <div class="space"><h4>${T('Actors & goals','Акторы и цели')}</h4><div>${esc(p.actors)}</div><div class="empty">${T('goals','цели')}: ${esc(p.goals)}</div></div>
  <div class="space"><h4>${T('Derived clocks','Выведенные такты')}</h4><dl>
   <dt>${T('syndrome round','раунд синдрома')}</dt><dd><b>${fS(R.total)}</b>${R.total?` · ${T('limiter','ограничитель')}: ${T(...(PN[R.limiter]||[R.limiter,R.limiter]))} · ${T('round of','раунд кода')} ${esc(R.code||'')}${R.d2?' (d₂ = '+R.d2+(R.d1?', d₁ = '+R.d1:'')+')':''}`:''}</dd>
   ${R.total?`<dt>${T('parts','части')}</dt><dd>${Object.keys(PN).map(k=>`${T(...PN[k])} ${fS(RP[k])}`).join(' · ')}</dd>`:''}
   <dt>${T('measured cycle','измеренный цикл')}</dt><dd>${esc(p.cycle||'—')}</dd>
   <dt>${T('reaction time','время реакции')}</dt><dd>${RX.loop!=null?`<b>${fS(RX.loop)}</b> ${T('(published loop)','(опубликованный контур)')} · `:''}${T('floor','нижняя граница')} ${fS(RX.floor)} ${RX.loop==null?`<span class="empty">· ${T('no published measurement→operation loop','нет опубликованного контура измерение→операция')}</span>`:''}</dd>
   <dt>${T('coherence','когерентность')}</dt><dd>T₁ ${fS(CO.t1)} · T₂ ${fS(CO.t2)}${CO.t2_scope&&CO.t2_scope!=='typical'?' ('+CO.t2_scope+')':''} · ${T('ops per coherence','операций на когерентность')} <b>${fE(CO.ops_per_coh)}</b></dd>
   <dt>${T('idle exposure per round','экспозиция простоя за раунд')}</dt><dd>t_round/T₂ = ${fE(CO.idle_exposure)} · ${T('measured idle error','измеренная ошибка простоя')} ${fE(CO.idle_measured)}</dd>
   ${(R.notes||[]).length?`<dt>${T('notes','примечания')}</dt><dd class="empty">${esc((R.notes||[]).join('; '))}</dd>`:''}
  </dl><div class="empty" style="margin-top:4px">${T('t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset — a sum of the round\'s phases, from the code node, the coordinates and the standard records; the measured cycle is the check.','t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset — сумма фаз раунда из узла кода, координат и стандартных рекордов; измеренный цикл — проверка.')}</div></div>
  <div class="space"><h4>${T('Stations by layer — primary, then alternates','Станции по слоям — основная, затем альтернативы')}</h4><table class="ptab">${rows}</table></div>
  <div class="space"><h4>${T('Reading','Чтение')}</h4><div>◎ ${T('hubs','хабы')}: ${hubs.length?hubs.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div><div>⤢ ${T('off-diagonal','внедиагональные')}: ${offs.length?offs.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div><div>∅ ${T('empty slots','пустые слоты')}: ${empties.length?empties.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div></div>`;
  insp.querySelectorAll('[data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; wrap.scrollTo({left:Math.max(0,m.x-200),top:Math.max(0,m.y-200),behavior:'smooth'});}));
  insp.querySelector('[data-close]').addEventListener('click',()=>{state.isolate=null; chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false')); inspectEmpty(); dimming();}); wireCard();
}
function inspectEmpty(){ insp.hidden=true; insp.innerHTML=''; }
function inspect(n){ const L=lang(); const c=n.c; const rows=[[T('(a) carrier affinity','(a) сродство носителя'),vt('AFF',n.aff),'aff'],
  [T('(b) time · entangling','(b) время · перепутывание'),(n.b.t!=null?fmtT(n.b.t):'—')+(n.b.det!=='na'?' · '+vt('DET',n.b.det):''),'b'],
  [T('(c) readout','(c) считывание'),c?`${vt('MECH',c.mech)} · ${fmtT(c.t)} · ${c.destr?T('destructive','разрушающее'):T('non-destructive','неразрушающее')} · ${c.mid?'mid-circuit':T('no mid-circuit','без mid-circuit')}`:'—','c'],
  [T('(d) mobility','(d) подвижность'),vt('MOB',n.d),'d'],[T('(e) control','(e) управление'),n.e.mod==='none'?'—':`${vt('MOD',n.e.mod)} @ ${vt('PLACE',n.e.place)}`,'e'],
  [T('(f) error structure','(f) структура ошибки'),n.f.map(x=>vt('ERR',x)).join(', '),'f'],[T('(g) manufacturing','(g) производство'),vt('FAB',n.g),'g']];
  const lr=LENSROWS[state.lens]||[];
  const flags=[]; n.offdiag.forEach(o=>flags.push(`<span class="flag off">⤢ ${vt('OFFDIAG',o)}</span>`)); if(n.hub)flags.push(`<span class="flag hub">◎ ${T('hub','хаб')} · ${n.reach.map(f=>T(...FAMN[f])).join(', ')}</span>`); if(n.status==='X')flags.push(`<span class="flag empty">∅ ${vt('STATUS','X')}</span>`);
  const reqOut=G.edges.filter(e=>e.type==='requires'&&e.src===n.id), reqIn=G.edges.filter(e=>e.type==='requires'&&e.dst===n.id), rep=G.edges.filter(e=>e.type==='replaces'&&(e.src===n.id||e.dst===n.id)), con=G.edges.filter(e=>e.type==='conflicts'&&(e.src===n.id||e.dst===n.id));
  const other=(e)=>e.src===n.id?e.dst:e.src;
  const link=id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`;
  insp.innerHTML=`<div class="grip" data-grip="1">⠿ <span class="sp"></span><button type="button" data-dock="left" title="dock left">⇤</button><button type="button" data-dock="right" title="dock right">⇥</button><button type="button" data-close="1" aria-label="close">✕</button></div><h3>${esc(n[L])}</h3><div class="meta">${n.id} · ${T('layer','слой')} ${n.layer} ${esc(G.layers[n.layer-1][L])} · ${vt('STATUS',n.status)}${n.since<2030?' · '+T('since','с')+' '+n.since:''}</div>
  <p>${lk(n.desc[L])}</p><div>${flags.join(' ')}</div>
  <button type="button" class="briefbtn" data-brief="${n.id}">${T('Brief →','Бриф →')}</button>
  ${(KEYREFS[n.id]||[]).length?`<div class="space keys"><h4>${T('Key references','Ключевые источники')}</h4>${KEYREFS[n.id].map(r=>`<div class="kr"><a href="${r.url}" target="_blank" rel="noopener">[${r.n}]</a> ${esc(r.label.length>92?r.label.slice(0,90)+'…':r.label)}${r.year?' <span class="empty">· '+r.year+'</span>':''}</div>`).join('')}</div>`:''}
  <div class="space"><h4>${T('Design space — coordinates','Пространство проектирования — координаты')}</h4><dl>${rows.map(([k,v,key])=>`<dt class="${lr.includes(key)?'lensrow':''}">${k}</dt><dd class="${lr.includes(key)?'lensrow':''}">${esc(v)}</dd>`).join('')}</dl></div>
  <div class="space"><h4>${T('Evaluation space — dated attributes','Пространство оценки — датированные атрибуты')}</h4>${n.defines.length?n.defines.map(d=>`<div class="def"><div><span class="k">${esc(d.metric)}</span> → <b>${esc(d.value)}</b></div><div class="d">${T('defines','определяет')}: ${vt('OUT',d.out)} · ${d.date} · <a href="${d.url}" target="_blank" rel="noopener">${T('source','источник')}</a></div></div>`).join(''):`<p class="empty">${T('no dated attribute','нет датированных атрибутов')}</p>`}${n.attrs[L]?`<p style="margin:6px 0 0">${lk(n.attrs[L])}</p>`:''}</div>
  ${(n.records||[]).length?`<div class="space"><h4>${T('Standard records','Стандартные рекорды')}</h4>${n.records.map(r=>{const RK=(G.vocab.RECKEYS||{})[r.key]||[r.key,r.key]; const val=r.num==null?`<span class="empty">${T('not published','не опубликовано')}</span>`:(r.unit==='s'?fmtT(Math.log10(r.num)):(r.unit==='Hz'?r.num.toExponential(1)+' Hz':(r.unit==='count'?String(r.num):(r.num<0.01||r.num>1e4?r.num.toExponential(2):String(+r.num.toPrecision(3)))))); return `<div class="def"><div><span class="k">${esc(T(...RK))}</span> → <b>${val}</b> <span class="empty">· ${r.scope}</span></div><div class="d">${esc(r.text)} · ${r.date} · <a href="${r.url}" target="_blank" rel="noopener">${T('source','источник')}</a> [${r.tag}]${r.note?` <span class="empty" title="${esc(r.note)}">ⓘ</span>`:''}</div></div>`;}).join('')}</div>`:''}
  <div class="space"><h4>${T('Actors & goals — annotations','Акторы и цели — аннотации')}</h4>${(prim[n.id]||[]).concat(alt[n.id]||[]).map(p=>`<div class="pathtag"><i class="sw" style="--c:${FAMC[PATH[p].family]}"></i>${esc(PATH[p][L])}${(alt[n.id]||[]).includes(p)?' <span class="empty">('+T('alternate','альтернатива')+')</span>':''}<span class="empty"> — ${esc(PATH[p].actors)} · ${PATH[p].goals}</span></div>`).join('')||`<p class="empty">${T('not on any platform path','не входит ни в один путь платформы')}</p>`}</div>
  <div class="space"><h4>${T('Edges','Рёбра')}</h4>
   ${reqOut.length?`<div><b>${T('requires','требует')}:</b> ${reqOut.map(e=>link(e.dst)+(e.any?'<span class="empty">°</span>':'')).join(', ')}</div>`:''}
   ${reqIn.length?`<div><b>${T('provides for','обеспечивает')}:</b> ${reqIn.map(e=>link(e.src)).join(', ')}</div>`:''}
   ${rep.length?`<div><b>${T('alternatives','альтернативы')}:</b> ${rep.map(e=>link(other(e))).join(', ')}</div>`:''}
   ${con.length?`<div><b style="color:var(--crit)">${T('conflicts with','конфликтует с')}:</b></div>`+con.map(e=>`<div class="conf"><div>${link(other(e))} <span class="cst ${e.status}">${esc(vt('CONSTAT',e.status))}</span></div><div class="cm">${lk(e[L])}</div><div class="cm"><span class="tk">${T('price','цена')}</span> ${lk(e.price?e.price[L]:'')}</div><div class="cm"><span class="tk">${T('mitigation','снятие')}</span> ${lk(e.mitig?e.mitig[L]:'')}${e.url?' · <a href="'+e.url+'" target="_blank" rel="noopener">'+e.date+'</a>':''}</div></div>`).join(''):''}
   ${(reqOut.length||reqIn.length||rep.length||con.length)?`<div class="empty" style="margin-top:4px">° ${T('one-of dependency','зависимость «одно из»')}</div>`:`<p class="empty">—</p>`}</div>`;
  insp.querySelectorAll('[data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; wrap.scrollTo({left:Math.max(0,m.x-200),top:Math.max(0,m.y-200),behavior:'smooth'});}));
  insp.querySelector('[data-close]').addEventListener('click',()=>select(null)); wireCard();
}
document.querySelectorAll('#mapbar [data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; wrap.scrollTo({left:Math.max(0,m.x-200),top:Math.max(0,m.y-200),behavior:'smooth'}); document.getElementById('mapwrap').scrollIntoView({block:'nearest'});}));
// ---------- controls
const bar=document.getElementById('mapbar');
const chipsWrap=document.getElementById('pathchips');
G.paths.forEach(p=>{const b=document.createElement('button'); b.className='chip'; b.dataset.chipPath=p.id; b.setAttribute('aria-pressed','false'); b.innerHTML=`<i class="sw" style="--c:${FAMC[p.family]}"></i><span class="t"></span>`; b.addEventListener('click',()=>{state.isolate=state.isolate===p.id?null:p.id; chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.chipPath===state.isolate))); if(state.isolate){ state.focus=null; st.classed('sel',false); drawEdges(); inspectPath(p); pcHighlight(null);} else if(!state.focus){ inspectEmpty(); } dimming();}); chipsWrap.appendChild(b);});
const lensSel=document.getElementById('lens'); Object.keys(LENSES).forEach(k=>{const o=document.createElement('option'); o.value=k; lensSel.appendChild(o);}); lensSel.addEventListener('change',()=>{state.lens=lensSel.value; state.lensFilter=null; applyLens(); dimming();});
document.getElementById('tg-conf').addEventListener('click',ev=>{state.showConf=!state.showConf; ev.currentTarget.setAttribute('aria-pressed',String(state.showConf)); drawEdges();});
document.getElementById('tg-rep').addEventListener('click',ev=>{state.showRep=!state.showRep; ev.currentTarget.setAttribute('aria-pressed',String(state.showRep)); drawEdges();});
document.getElementById('tg-req').addEventListener('click',ev=>{state.showReq=!state.showReq; ev.currentTarget.setAttribute('aria-pressed',String(state.showReq)); drawEdges();});
document.getElementById('tg-reset').addEventListener('click',()=>{state.isolate=null; state.showConf=state.showRep=state.showReq=false; ['tg-conf','tg-rep','tg-req'].forEach(i=>document.getElementById(i).setAttribute('aria-pressed','false')); chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false')); select(null);});
// ---------- parallel coordinates
const pcHost=document.getElementById('pc');
const PCW=1100, PCH=300, PX0=70, PX1=PCW-30, PY0=34, PY1=PCH-46;
const pcsvg=d3.select(pcHost).append('svg').attr('viewBox',`0 0 ${PCW} ${PCH}`).attr('role','img').attr('aria-label','Parallel coordinates of all technologies across the seven design coordinates');
const AXES=[{k:'aff',en:'(a) carrier',ru:'(a) носитель'},{k:'b',en:'(b) time',ru:'(b) время'},{k:'c',en:'(c) readout',ru:'(c) считывание'},{k:'d',en:'(d) mobility',ru:'(d) подвижность'},{k:'e',en:'(e) control',ru:'(e) управление'},{k:'f',en:'(f) error',ru:'(f) ошибка'},{k:'g',en:'(g) fab',ru:'(g) производство'}];
const ORD={aff:[0,0.25,0.5,0.75,1],d:['none','static','shared','longrange','bus','transport','flying'],e:['none','lf@RT','mw@RT','eo@RT','opt@RT','opt@vac','mw@4K','lf@mK','mw@mK'],f:['none','pauli','coherent','leak','burst','bias','gauss','erasure','loss','unknown'],g:['none','sclitho','3d','cmos','mbe','mems','pic','optics','stm','diamond'],c:['none','spd','disp','erasure','s2c','qcap','fluor','img']};
const xAx=i=>PX0+i*(PX1-PX0)/(AXES.length-1);
const tScale=d3.scaleLinear().domain([-8.5,-1]).range([PY1,PY0]);
function yOf(n,k){ if(k==='aff')return PY1-(ORD.aff.indexOf(n.aff))*(PY1-PY0)/4; if(k==='b')return n.b.t==null?PY1+10:tScale(n.b.t); if(k==='c'){const m=n.c?n.c.mech:'none'; const i=ORD.c.indexOf(m); return PY1-i*(PY1-PY0)/(ORD.c.length-1);} if(k==='e'){const key=n.e.mod==='none'?'none':n.e.mod+'@'+n.e.place; let i=ORD.e.indexOf(key); if(i<0)i=0; return PY1-i*(PY1-PY0)/(ORD.e.length-1);} const arr=ORD[k]; const v=k==='f'?(n.f[0]||'none'):n[k]; let i=arr.indexOf(v); if(i<0)i=0; return PY1-i*(PY1-PY0)/(arr.length-1); }
const pcAxes=pcsvg.append('g'); const pcLines=pcsvg.append('g'); const pcLabel=pcsvg.append('text').attr('x',PX0).attr('y',PCH-8).attr('fill','var(--ink)').attr('font-size',12).attr('font-weight',600);
function renderPC(){ pcAxes.selectAll('*').remove();
  AXES.forEach((a,i)=>{const g=pcAxes.append('g').attr('class','pc-axis'); const x=xAx(i); g.append('line').attr('x1',x).attr('x2',x).attr('y1',PY0-6).attr('y2',PY1+12); g.append('text').attr('class','t').attr('x',x).attr('y',PY0-14).attr('text-anchor','middle').text(a[lang()]);
    let ticks=[]; if(a.k==='aff')ticks=ORD.aff.map(v=>[PY1-ORD.aff.indexOf(v)*(PY1-PY0)/4,vt('AFF',v).split(' ')[0]]); else if(a.k==='b')ticks=[-8,-7,-6,-5,-4,-3,-2].map(v=>[tScale(v),fmtT(v)]); else if(a.k==='c')ticks=ORD.c.map((v,j)=>[PY1-j*(PY1-PY0)/(ORD.c.length-1),v==='none'?'—':vt('MECH',v).split(' ')[0]]); else if(a.k==='e')ticks=ORD.e.map((v,j)=>[PY1-j*(PY1-PY0)/(ORD.e.length-1),v==='none'?'—':v]); else {const arr=ORD[a.k], tab={d:'MOB',f:'ERR',g:'FAB'}[a.k]; ticks=arr.map((v,j)=>[PY1-j*(PY1-PY0)/(arr.length-1),v==='none'?'—':vt(tab,v).split(' ')[0]]);}
    ticks.forEach(([y,t])=>{g.append('line').attr('x1',x-3).attr('x2',x+3).attr('y1',y).attr('y2',y); g.append('text').attr('x',x+(i===AXES.length-1?-6:6)).attr('y',y+3.5).attr('text-anchor',i===AXES.length-1?'end':'start').text(t);}); });
  const pl=d3.line().x(d=>d[0]).y(d=>d[1]).curve(d3.curveMonotoneX);
  pcLines.selectAll('path').data(G.nodes,d=>d.id).join('path').attr('class','pcline').attr('stroke',d=>d._fam?FAMC[d._fam]:'var(--mid)').attr('d',d=>pl(AXES.map((a,i)=>[xAx(i),yOf(d,a.k)])))
    .on('mouseenter',(ev,d)=>{pcHighlight(d.id,true); pcLabel.text(d[lang()]);}).on('mouseleave',()=>{pcHighlight(state.focus); pcLabel.text(state.focus?NODE[state.focus][lang()]:'');}).on('click',(ev,d)=>{select(d.id); wrap.scrollTo({left:Math.max(0,d.x-200),top:Math.max(0,d.y-200),behavior:'smooth'});});
  pcHighlight(state.focus); }
function pcHighlight(id,hover){ pcLines.selectAll('path').classed('hi',d=>d.id===id).classed('dim',d=>id?d.id!==id:(state.lensFilter!=null?!nodeMatchesFilter(d):false)); if(!hover)pcLabel.text(id?NODE[id][lang()]:''); }
// ---------- init
window.__relabelMap=relabel;
// select a station from outside the map (used by the technology briefs)
window.__selectNode=function(id){ if(!NODE[id])return false; select(id); const m=NODE[id]; wrap.scrollTo({left:Math.max(0,m.x-200),top:Math.max(0,m.y-200),behavior:'smooth'}); return true; };
relabel(); inspectEmpty(); applyLens(); renderPC();
})();

// ---------- collapsible map
(function(){ const body=document.getElementById('mapbody'); if(!body)return; const KEY='qmap.collapsed';
  function setC(c){ body.hidden=c; document.querySelectorAll('[data-mapcollapse]').forEach(b=>{b.setAttribute('aria-expanded',String(!c)); b.querySelectorAll('.when-open').forEach(x=>x.hidden=c); b.querySelectorAll('.when-closed').forEach(x=>x.hidden=!c);}); try{localStorage.setItem(KEY,c?'1':'0');}catch(e){} }
  let c=false; try{c=localStorage.getItem(KEY)==='1';}catch(e){}
  setC(c); document.querySelectorAll('[data-mapcollapse]').forEach(b=>b.addEventListener('click',()=>setC(!body.hidden)));
  window.__expandMap=()=>setC(false);
  document.querySelectorAll('a[href="#map"]').forEach(a=>a.addEventListener('click',()=>setC(false)));
})();

// ---------- floating card: drag, dock, remember
const CARDKEY='qmap.card';
function cardState(){ try{return JSON.parse(localStorage.getItem(CARDKEY)||'{}');}catch(e){return {};} }
function saveCard(o){ try{localStorage.setItem(CARDKEY,JSON.stringify(o));}catch(e){} }
function placeCard(){ const o=cardState(); const w=insp.offsetWidth||336; const vw=window.innerWidth, vh=window.innerHeight;
  if(o.mode==='free'&&o.x!=null){ insp.style.left=Math.max(0,Math.min(vw-w,o.x))+'px'; insp.style.top=Math.max(0,Math.min(vh-80,o.y))+'px'; insp.style.right='auto'; }
  else if(o.mode==='right'){ insp.style.left='auto'; insp.style.right='16px'; insp.style.top=(o.y!=null?Math.max(0,Math.min(vh-80,o.y)):84)+'px'; }
  else { insp.style.left='16px'; insp.style.right='auto'; insp.style.top=(o.y!=null?Math.max(0,Math.min(vh-80,o.y)):84)+'px'; }
  if(o.w){ insp.style.width=Math.min(o.w,vw-32)+'px'; }
  insp.querySelectorAll('[data-dock]').forEach(b=>b.setAttribute('aria-pressed',String((o.mode||'left')===b.dataset.dock))); }
function wireCard(){ placeCard();
  insp.querySelectorAll('[data-dock]').forEach(b=>b.addEventListener('click',ev=>{ev.stopPropagation(); const o=cardState(); o.mode=b.dataset.dock; saveCard(o); placeCard();}));
  const g=insp.querySelector('[data-grip]'); if(!g)return;
  g.addEventListener('pointerdown',ev=>{ if(ev.target.closest('button'))return; ev.preventDefault(); const r=insp.getBoundingClientRect(); const dx=ev.clientX-r.left, dy=ev.clientY-r.top; insp.classList.add('dragging'); g.setPointerCapture(ev.pointerId);
    const mv=e=>{ insp.style.left=(e.clientX-dx)+'px'; insp.style.top=(e.clientY-dy)+'px'; insp.style.right='auto'; };
    const up=e=>{ g.removeEventListener('pointermove',mv); g.removeEventListener('pointerup',up); insp.classList.remove('dragging'); const rr=insp.getBoundingClientRect(); saveCard(Object.assign(cardState(),{mode:'free',x:rr.left,y:rr.top})); };
    g.addEventListener('pointermove',mv); g.addEventListener('pointerup',up); });
}
new ResizeObserver(()=>{ if(insp.hidden)return; const o=cardState(); const w=insp.offsetWidth; if(w&&Math.abs((o.w||336)-w)>2){o.w=w; saveCard(o);} }).observe(insp);
window.addEventListener('resize',()=>{ if(!insp.hidden)placeCard(); });
try{ matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{buildScales(); applyLens();}); new MutationObserver(()=>{buildScales(); applyLens();}).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']}); }catch(e){}
"""
