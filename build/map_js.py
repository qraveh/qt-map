JS = r"""
(function(){
'use strict';
const KEYREFS=window.__KEYREFS||{}; const G=window.__GRAPH, SHORT=window.__SHORT;
// machines register (C2): slim copy embedded at build time — machines[], by_node{}, families[], urls{register,tech}
const MACH=window.__MACH||{machines:[],by_node:{},families:['SC','ION','ATOM','PHOTON','SPIN','DEFECT','TOPO','ANNEAL'],urls:{register:'',tech:''}};
const MBY=Object.fromEntries(MACH.machines.map(m=>[m.id,m]));
const REG_URL=id=>(MACH.urls&&MACH.urls.register||'')+id, TECH_URL=id=>(MACH.urls&&MACH.urls.tech||'')+id;
const app=document.getElementById('app');
const lang=()=>app.getAttribute('data-lang')||'en';
const T=(en,ru)=>lang()==='en'?en:ru;
const FAMC={SC:'var(--sc)',ION:'var(--ion)',ATOM:'var(--atom)',PHOTON:'var(--photon)',SPIN:'var(--spin)',DEFECT:'var(--defect)',TOPO:'var(--topo)',ANNEAL:'var(--anneal)'};
const FAMN={SC:['superconducting circuits','сверхпроводниковые схемы'],ION:['trapped ions','ионы в ловушках'],ATOM:['neutral atoms','нейтральные атомы'],PHOTON:['photonics','фотоника'],SPIN:['semiconductor spins','полупроводниковые спины'],DEFECT:['defect spins','дефектные спины'],TOPO:['topological','топологические'],ANNEAL:['quantum annealers','квантовый отжиг']};   // full platform names (editor, 17 Sep: "neutral atoms", not "atoms")
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
// zoom control: pinned top-right on desktop; on ≤1024 px it moves to the end of the scroller and pins bottom-right
// (the sticky page bar would otherwise cover it whenever the map's top edge scrolls under the bar)
(function(){ const zb=wrap.querySelector('.zoombar'), win=document.querySelector('#mapbar .zoomwin'), ctl=document.querySelector('.zoomctl'); if(!zb||!win||!ctl)return; let mq=null; try{ mq=window.matchMedia('(max-width:1024px)'); }catch(e){}
  const place=()=>{ if(mq&&mq.matches){ zb.appendChild(ctl); wrap.appendChild(zb); } else { win.appendChild(ctl); const pc=document.getElementById('pathchips'); if(pc)pc.appendChild(win); } };
  window.__placeZoom=place; place(); if(mq){ if(mq.addEventListener)mq.addEventListener('change',place); else if(mq.addListener)mq.addListener(place); } })();
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
// path lines are selectable: a wide invisible twin of each line takes the pointer — hover names the path, click isolates it (same as its chip)
const gPathHit=svg.insert('g',function(){return gAlt.node();}).attr('class','pathhits');
const pathHit=gPathHit.selectAll('path').data(G.paths).join('path').attr('class','phit').attr('d',d=>line(pathPoints(d))).attr('data-path',d=>d.id);
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
// ≤1024 the inspector is a bottom sheet lying over the lower part of the map; report its top edge
function sheetCover(){ const i=document.getElementById('insp'); if(!i||i.hidden)return null;
  const wr=wrap.getBoundingClientRect(), ir=i.getBoundingClientRect();
  if(ir.width<10||ir.height<10)return null;
  return (ir.left<=wr.left+2&&ir.right>=wr.right-2&&ir.top>wr.top&&ir.top<wr.bottom)?ir.top:null; }
function placeTip(ev){ const r=wrap.getBoundingClientRect(); let x=ev.clientX-r.left+wrap.scrollLeft+14, y=ev.clientY-r.top+wrap.scrollTop+14; const tw=tip.offsetWidth, th=tip.offsetHeight; if(ev.clientX-r.left+14+tw>wrap.clientWidth) x=ev.clientX-r.left+wrap.scrollLeft-tw-14; if(ev.clientY-r.top+14+th>wrap.clientHeight) y=ev.clientY-r.top+wrap.scrollTop-th-14;
  const sc=sheetCover(); if(sc!=null){ const maxY=sc-r.top+wrap.scrollTop-th-8; if(y>maxY)y=maxY; }
  tip.style.left=Math.max(wrap.scrollLeft,x)+'px'; tip.style.top=Math.max(wrap.scrollTop,y)+'px'; }
function stationTip(d){ const L=lang(); const k=state.lens; let h=`<b>${esc(d[L])}</b> <span style="opacity:.7">${d.id}</span><br>${vt('STATUS',d.status)} · ${d.since<2030?d.since:'—'} · ${T('layer','слой')} ${d.layer}`;
  const ps=(prim[d.id]||[]), as=(alt[d.id]||[]);
  if(ps.length||as.length) h+=`<br><span class="tk">${T('lines','линии')}</span> `+ps.map(p=>`<i class="sw" style="background:${FAMC[PATH[p].family]}"></i>${esc(PATH[p][L])}`).concat(as.map(p=>`<i class="sw hollow" style="border-color:${FAMC[PATH[p].family]}"></i>${esc(PATH[p][L])} <span style="opacity:.7">(${T('alternate','альтернатива')})</span>`)).join(' · ');
  if(k==='family'){ const f=d._fams; h+=`<br><span class="tk">${T('outline','рамка')}</span> ${f.length?f.map(x=>T(...FAMN[x])).join(' + '):'—'}`; }
  else { const c=lensColor(d,k); const v=lensValue(d,k); const lab=k==='aff'?vt('AFF',d.aff):(k==='time'?(v==='none'?T('no time','нет времени'):TBINS[+v][1]):catLabel(k,v)); h+=`<br><span class="tk">${T('lens','линза')}</span> ${esc(LENSES[k][L])}: <i class="sw" style="background:${c||'transparent'};border:1px solid ${c||'var(--bg)'}"></i>${esc(lab)}`; }
  const fl=[]; if(d.hub)fl.push('◎ '+T('hub','хаб')); if(d.offdiag&&d.offdiag.length)fl.push('⤢ '+T('off-diagonal','внедиагональный')); if(d.status==='X')fl.push('∅ '+T('empty slot','пустой слот')); if(fl.length)h+=`<br>${fl.join(' · ')}`;
  h+=`<br><span style="opacity:.6">${T('click for the card','клик — карточка')}</span>`; return h; }
st.on('mousemove',(ev,d)=>{if(tipPinned)return; tip.style.display='block'; tip.classList.add('wide'); tip.innerHTML=stationTip(d); placeTip(ev);}).on('mouseleave',()=>{if(!tipPinned)hideTip();});
st.on('click',(ev,d)=>{ev.stopPropagation(); unpinTip(); select(d.id===state.focus?null:d.id);}).on('keydown',(ev,d)=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault(); select(d.id===state.focus?null:d.id);}});
svg.on('click',()=>select(null));
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')select(null);});
// ---------- state & rendering
const state={focus:null,isolate:null,machine:null,lens:'family',lensFilter:null,showConf:false,showRep:false,showReq:false,zoom:1};
// zoom scales the *rendered* SVG only; the viewBox and every node coordinate stay in map units,
// so anything that scrolls the wrapper to a node must multiply that node's coordinates by state.zoom.
function scrollToNode(m){ const z=state.zoom||1; wrap.scrollTo({left:Math.max(0,m.x*z-200),top:Math.max(0,m.y*z-200),behavior:'smooth'}); }
function noHover(){ try{ return window.matchMedia('(hover: none)').matches; }catch(e){ return false; } }
function hideTip(){ tip.style.display='none'; tip.classList.remove('wide'); }
// A tip opened by a tap is "pinned": it must survive the synthetic mouse events and the edge redraw
// that the same tap triggers. Only another tap (outside an edge) or a station click takes it down.
let tipPinned=false;
function unpinTip(){ tipPinned=false; hideTip(); }
document.addEventListener('pointerdown',function(ev){ const t=ev.target; if(t&&t.closest&&t.closest('g.edge'))return; unpinTip(); },true);
const LENSES={   // editor's order of 17 Sep 2026: family → manufacturing → error structure → mobility → control (modality, placement) → time → readout (mechanism, destructive, mid-circuit) → entangling → affinity → status
 // plain names, no coordinate letters (brief E): the letter stays on the station card's coordinate rows and, muted, in the lens legend's title
 family:{en:'Platform family',ru:'Семейство платформ'},
 g:{en:'Manufacturing technology',ru:'Технология производства'},
 f:{en:'Dominant error structure',ru:'Доминирующая структура ошибок'},
 d:{en:'Mobility / connectivity',ru:'Подвижность / связность'},
 mod:{en:'Control: modality',ru:'Управление: модальность'},
 place:{en:'Control: placement (temperature stage)',ru:'Управление: размещение (температурная ступень)'},
 time:{en:'Characteristic time (gate or readout)',ru:'Характерное время (гейт или считывание)'},
 mech:{en:'Readout: mechanism',ru:'Считывание: механизм'},
 destr:{en:'Readout: destructive?',ru:'Считывание: разрушающее?'},
 mid:{en:'Readout: mid-circuit?',ru:'Считывание: внутрисхемное?'},
 det:{en:'Entangling: deterministic / heralded',ru:'Перепутывание: детерминированное / heralded'},
 aff:{en:'Carrier affinity: natural ↔ fabricated',ru:'Сродство носителя: естественный ↔ изготовленный'},
 status:{en:'Technology status',ru:'Статус технологии'}};
const LENSCOORD={g:'(g)',f:'(f)',d:'(d)',mod:'(e)',place:'(e)',time:'(b)/(c)',mech:'(c)',destr:'(c)',mid:'(c)',det:'(b)',aff:'(a)'};   // the report's coordinate letter, shown once as a muted suffix of the lens legend's title
// reading marks (brief E, editor's decision): no lens — glyphs on the stations, static legend keys with counts, badges on the station card
const HUBDEF=['a station that stations of at least two families (or one family, recently) require — where a fix or a stall propagates across platforms','станция, которую требуют станции как минимум двух семейств (или одного — недавно): где исправление или застой распространяются на другие платформы'];
const OFFDEF=['a station that takes a trait from the other side of the natural/fabricated divide (see §7.6)','станция, берущая свойство с другой стороны раздела естественное/изготовленное (см. §7.6)'];
const EMPTYDEF=['a station with no demonstrated technology yet','станция, для которой технологии ещё нет'];
const isHub=n=>!!n.hub, isOffd=n=>!!(n.offdiag&&n.offdiag.length), isEmpty=n=>n.status==='X';
function glyphKeys(){ document.querySelectorAll('#glyphlegend [data-glyph]').forEach(el=>{ const k=el.dataset.glyph; const f=k==='hub'?isHub:(k==='offd'?isOffd:isEmpty); const c=el.querySelector('.cnt'); if(c)c.textContent=G.nodes.filter(f).length; el.title=T(...(k==='hub'?HUBDEF:(k==='offd'?OFFDEF:EMPTYDEF))); }); }
// categorical lens palette (deliberately not the family palette: while a lens is active, path lines turn neutral so colour means the lens value only)
const LENSPAL=['#3B6FD4','#E0862B','#2FA66A','#C94C6B','#7C5CC4','#C7A22B','#2AA5B8','#8B6A45','#D07AB5','#6E7F91'];
const CATS={
 mech:['disp','s2c','qcap','erasure','fluor','img','spd','none'], d:['static','longrange','shared','bus','transport','flying','none'],
 mod:['mw','lf','eo','opt','none'], place:['RT','4K','mK','none'], f:['pauli','coherent','leak','burst','bias','gauss','erasure','loss','unknown','none'],
 g:['sclitho','3d','cmos','mbe','mems','pic','optics','stm','diamond','none'], status:['D','E','T','X'],
 det:['det','her','na'], destr:['yes','no','none'], mid:['yes','no','none']};
const VTAB={mech:'MECH',d:'MOB',mod:'MOD',place:'PLACE',f:'ERR',g:'FAB',status:'STATUS',det:'DET'};
const YESNO={yes:['yes','да'],no:['no','нет'],none:['no readout','без считывания']};
function catLabelSafe(k,v){ try{ if(k==='family')return T(...FAMN[v]); if(k==='aff')return vt('AFF',Number(v)); if(k==='time')return v==='none'?'—':TBINS[Number(v)][1]; return catLabel(k,v);}catch(e){return String(v);} }
function catLabel(k,v){ if(k==='destr'||k==='mid')return T(...YESNO[v]); return vt(VTAB[k],v); }
function lensValues(n,k){ if(k==='f')return (n.f&&n.f.length)?n.f:['none']; if(k==='place')return (n.e.place&&n.e.place.length)?n.e.place:['none']; if(k==='family')return n._fams; return [lensValue(n,k)]; }   // every value a station carries for a lens (f and place are lists; place since 17 Sep 2026)
function lensValue(n,k){ if(k==='mech')return n.c?n.c.mech:'none'; if(k==='d')return n.d; if(k==='mod')return n.e.mod; if(k==='place')return (n.e.place&&n.e.place[0])||'none'; if(k==='f')return n.f[0]||'none'; if(k==='g')return n.g; if(k==='status')return n.status;
  if(k==='det')return n.b.det||'na'; if(k==='destr')return n.c?(n.c.destr?'yes':'no'):'none'; if(k==='mid')return n.c?(n.c.mid?'yes':'no'):'none'; if(k==='aff')return String(n.aff); if(k==='time'){const t=timeOf(n); return t==null?'none':timeBin(t);} return null;}
function timeOf(n){ if(n.b.t!=null)return n.b.t; if(n.c&&n.c.t!=null)return n.c.t; return null; }
const TBINS=[[-8.5,'≤ 3 ns'],[-7.5,'~30 ns'],[-6.5,'~300 ns'],[-5.5,'~3 µs'],[-4.5,'~30 µs'],[-3.5,'~300 µs'],[-2.5,'≥ 3 ms']];
function timeBin(t){ let best=0; TBINS.forEach((b,i)=>{ if(Math.abs(b[0]-t)<Math.abs(TBINS[best][0]-t))best=i; }); return String(best); }
// resolve CSS colour tokens at runtime (d3 cannot interpolate var(--x) strings); re-resolved on theme change
function css(v){ return getComputedStyle(document.documentElement).getPropertyValue(v).trim()||'#888'; }
let affScale=null, timeScale=null;
function buildScales(){ affScale=d3.scaleLinear().domain([0,0.5,1]).range([css('--nat'),css('--mid'),css('--fab')]).interpolate(d3.interpolateRgb); timeScale=d3.scaleLinear().domain([-8.5,-6.5,-4.5,-2.5]).range([css('--lens4'),css('--lens3'),css('--lens2'),css('--lens1')]).interpolate(d3.interpolateRgb).clamp(true); }   // fast = the strong end of the ramp, slow = the pale end
buildScales();
function lensColor(n,k){ if(k==='family')return null; if(k==='aff')return affScale(n.aff); if(k==='time'){const t=timeOf(n); return t==null?null:timeScale(t);} let v=lensValue(n,k); if((k==='f'||k==='place')&&state.lensFilter){ const hit=lensValues(n,k).find(x=>state.lensFilter.has(x)); if(hit)v=hit; }   // a multi-value station takes the colour of the value it is lit for
  if(v==null||v==='none')return null; const i=CATS[k].indexOf(v); return i<0?null:LENSPAL[i%LENSPAL.length]; }
function tint(c){ const x=d3.color(c); if(!x)return 'var(--surface)'; x.opacity=0.22; return x.formatRgb(); }
function lensItems(k){ const count=v=>G.nodes.filter(n=>lensValues(n,k).includes(v)).length;
  if(k==='family') return Object.keys(FAMC).map(f=>({c:FAMC[f],t:T(...FAMN[f]),v:f,n:G.nodes.filter(n=>n._fams.includes(f)).length}));
  if(k==='aff') return [0,0.25,0.5,0.75,1].map(a=>({c:affScale(a),t:vt('AFF',a),v:String(a),n:count(String(a))}));
  if(k==='time') return TBINS.map((b,i)=>({c:timeScale(b[0]),t:b[1],v:String(i),n:count(String(i))})).concat([{c:null,t:T('no time (code, decoder, fab)','нет времени (код, декодер, производство)'),v:'none',n:count('none')}]);
  return CATS[k].map(v=>({c:v==='none'?null:LENSPAL[CATS[k].indexOf(v)%LENSPAL.length],t:catLabel(k,v),v,n:count(v)})); }
function nodeMatchesFilter(n){ const k=state.lens, v=state.lensFilter; if(v==null)return true; if(k==='family')return n._fams.some(f=>v.has(f)); return lensValues(n,k).some(x=>v.has(x)); }
function filterHas(x){ return !!(state.lensFilter&&state.lensFilter.has(x)); }
// plain click: keep only this value (click again to clear); Ctrl / ⌘ / Shift-click: add or remove this value
function toggleFilter(v,multi){ if(v===''){ state.lensFilter=null; return; }
  if(multi){ const st=new Set(state.lensFilter||[]); if(st.has(v))st.delete(v); else st.add(v); state.lensFilter=st.size?st:null; }
  else state.lensFilter=(state.lensFilter&&state.lensFilter.size===1&&state.lensFilter.has(v))?null:new Set([v]); }
function applyLens(){ const k=state.lens; const leg=document.getElementById('lenslegend'); const lensed=k!=='family';
  svg.classed('lensed',lensed);
  st.select('rect.box').attr('stroke',d=>{ if(!lensed){ const f=d._fams; return f.length===1?FAMC[f[0]]:(f.length>1?'var(--ink)':'var(--mid)'); } const c=lensColor(d,k); return c||'var(--mid)'; })
    .attr('fill',d=>{ if(!lensed)return 'var(--surface)'; const c=lensColor(d,k); return c?tint(c):'var(--surface)'; });
  st.select('rect.lensbar').attr('fill',d=>{ if(!lensed)return 'transparent'; return lensColor(d,k)||'transparent'; });
  pcLines.selectAll('path').attr('stroke',d=>lensed?(lensColor(d,k)||'var(--mid)'):(d._fam?FAMC[d._fam]:'var(--mid)'));
  const items=lensItems(k).filter(it=>it.n>0);
  leg.innerHTML='<span class="lbl">'+T('lens legend · click a value to keep only those stations · Ctrl-click adds a value','легенда линзы · клик по значению оставляет только эти станции · Ctrl-клик добавляет значение')+(LENSCOORD[k]?' <span class="cnt">'+T('coordinate','координата')+' '+LENSCOORD[k]+'</span>':'')+'</span>'+items.map(it=>`<button type="button" class="k lk" data-lv="${it.v}" aria-pressed="${String(filterHas(it.v))}"><i class="sw" style="background:${it.c||'transparent'};border:1px solid ${it.c?it.c:'var(--mid)'}"></i>${esc(it.t)} <span class="cnt">${it.n}</span></button>`).join('')+(state.lensFilter!=null?`<button type="button" class="k lk clear" data-lv="">${T('clear filter','сбросить фильтр')} ✕</button>`:'');
  leg.querySelectorAll('[data-lv]').forEach(b=>{ b.addEventListener('click',ev=>{ toggleFilter(b.dataset.lv,ev.ctrlKey||ev.metaKey||ev.shiftKey); applyLens(); drawEdges(); dimming(); pcHighlight(state.focus); });
    b.addEventListener('mouseenter',()=>{ const v=b.dataset.lv; if(v==='')return; st.classed('peek',d=>lensValues(d,k).includes(v)); });
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
  glyphKeys();
  document.querySelectorAll('#machine optgroup').forEach(o=>{ if(FAMN[o.dataset.fam])o.label=T(...FAMN[o.dataset.fam]); });
  applyLens(); if(state.focus)inspect(NODE[state.focus]); else if(state.machine&&MBY[state.machine])inspectMachine(MBY[state.machine]); else if(state.isolate)inspectPath(PATH[state.isolate]); else inspectEmpty(); renderPC();
}
function select(id){ state.focus=id; st.classed('sel',d=>d.id===id); drawEdges(); dimming(); if(id){insp.hidden=false; inspect(NODE[id]);} else if(state.machine&&MBY[state.machine]){ inspectMachine(MBY[state.machine]); } else {insp.hidden=true; insp.innerHTML='';} pcHighlight(id); sheetRoom(); }
function sheetRoom(){ try{ document.body.classList.toggle('has-sheet', !insp.hidden && sheetMode()); }catch(e){} }   // room to scroll the map above the bottom sheet (≤ 1024 px)
function edgeOn(e){ return (e.type==='conflicts'&&state.showConf)||(e.type==='replaces'&&state.showRep)||(e.type==='requires'&&state.showReq); }
// neighbours through the relation types currently toggled on — the toggles decide which relations exist on the map at all
function neighbours(id){ const s=new Set([id]); G.edges.forEach(e=>{ if(!edgeOn(e))return; if(e.src===id)s.add(e.dst); if(e.dst===id)s.add(e.src); }); return s; }
// what stays lit: keepN = stations, keepP = lines; null = everything. One rule for the map and for the edges.
//   isolated path      -> its stations and its line
//   focused station    -> its lines in full (every station on every path through it, primary or alternate) plus its neighbours
//                         through the toggled relation types
//   lens value         -> the stations with that value; a family value also keeps that family's lines
// the three narrow each other (intersection); the focused station itself is always lit
function litSets(){ const f=state.focus, iso=state.isolate;
  let keepN=null, keepP=null;
  if(iso){ keepP=new Set([iso]); keepN=pathMembers(iso); }
  if(f){ const ps=new Set((prim[f]||[]).concat(alt[f]||[])); keepP=keepP?new Set([...keepP].filter(p=>ps.has(p))):ps;
    const pm=new Set(); ps.forEach(pid=>pathMembers(pid).forEach(x=>pm.add(x))); neighbours(f).forEach(x=>pm.add(x)); pm.add(f);
    keepN=keepN?new Set([...keepN].filter(n=>pm.has(n))):pm; }
  if(state.lensFilter!=null){ const lf=new Set(G.nodes.filter(nodeMatchesFilter).map(n=>n.id)); keepN=keepN?new Set([...keepN].filter(x=>lf.has(x))):lf;
    if(state.lens==='family'){ const fp=new Set(G.paths.filter(p=>state.lensFilter.has(p.family)).map(p=>p.id)); keepP=keepP?new Set([...keepP].filter(p=>fp.has(p))):fp; } }
  // machine (register): one more term of the same intersection — its real stations on every layer (primary and alternate) and its own path line
  const mm=state.machine&&MBY[state.machine]; if(mm){ const ms=machNodes(mm).all; keepN=keepN?new Set([...keepN].filter(x=>ms.has(x))):new Set(ms);
    const mp=new Set([mm.path]); keepP=keepP?new Set([...keepP].filter(p=>mp.has(p))):mp; }
  if(f&&keepN)keepN.add(f);
  return {keepN:keepN,keepP:keepP}; }
// the machine's stations: all real (non-gap) nodes across the ten layers; alt = used only as an alternate
function machNodes(m){ if(m._nodes)return m._nodes; const all=new Set(), pr=new Set(), al=new Set();
  Object.values(m.layers||{}).forEach(cells=>cells.forEach(c=>{ if(!NODE[c[0]])return; all.add(c[0]); (c[1]==='alternate'?al:pr).add(c[0]); }));
  m._nodes={all:all,alt:new Set([...al].filter(x=>!pr.has(x)))}; return m._nodes; }
function machCell(m,id){ const n=NODE[id]; if(!n)return null; return ((m.layers||{})[String(n.layer)]||[]).find(c=>c[0]===id)||null; }
function dimming(){ const f=state.focus, iso=state.isolate; const L=litSets(), keepN=L.keepN, keepP=L.keepP;
  st.classed('dim',d=>keepN?!keepN.has(d.id):false); const mm=state.machine&&MBY[state.machine], ma=mm?machNodes(mm).alt:null;
  st.classed('altuse',d=>!!(ma&&ma.has(d.id)&&(!keepN||keepN.has(d.id))));   // used by the machine only as an alternate — dashed while lit
  st.classed('member',d=>iso?!!(PATH[iso].slots&&Object.values(PATH[iso].slots).flat().includes(d.id)):false);
  const lf=state.lensFilter!=null;   // a lens filter keeps stations, not lines: every line goes quiet unless a path is isolated or a station focused
  svg.classed('iso',!!iso);
  pathSel.classed('dim',d=>keepP?!keepP.has(d.id):lf); pathHit.classed('dim',d=>keepP?!keepP.has(d.id):lf);
  gAlt.selectAll('path').classed('dim',d=>keepP?!keepP.has(d.p.id):lf);
  gPaths.selectAll('circle.emptyslot').attr('opacity',d=>keepP?(keepP.has(d.p.id)?1:.08):(lf?.08:1));
  if(window.__barSummary)window.__barSummary();
  sheetRoom();
}
function edgePath(a,b){ const dx=b.cx-a.cx; if(Math.abs(dx)<1){ const x=a.cx+NW/2; return `M${a.cx+NW/2-2},${a.cy} C${x+22},${a.cy} ${x+22},${b.cy} ${b.cx+NW/2-2},${b.cy}`; }
  const sx=dx>0?a.cx+NW/2:a.cx-NW/2, tx=dx>0?b.cx-NW/2:b.cx+NW/2; const mx=(sx+tx)/2; return `M${sx},${a.cy} C${mx},${a.cy} ${mx},${b.cy} ${tx},${b.cy}`; }
function pathMembers(pid){ return new Set(Object.values(PATH[pid].slots).flat()); }
function drawEdges(){ gEdges.selectAll('*').remove(); const f=state.focus;
  // the edge toggles alone decide which relation types are drawn — with or without a selection, focused station included;
  // whatever is lit (litSets) narrows them to the relations among the lit stations (with a lens value on: within the lens)
  const lit=litSets().keepN;
  const es=G.edges.filter(e=>{ if(e.type==='defines'||e.type==='transfers')return false;
    if(lit&&!(lit.has(e.src)&&lit.has(e.dst)))return false;
    return edgeOn(e); });
  const ETYPE={requires:['requires','требует'],replaces:['is an alternative to','— альтернатива для'],conflicts:['conflicts with','конфликтует с']};
  const edgeTip=e=>{const L=lang(); const a=NODE[e.src][L], b=NODE[e.dst][L]; let h=`<b>${esc(a)}</b> ${T(...ETYPE[e.type])} <b>${esc(b)}</b>${e.any?' <span style="opacity:.7">('+T('one-of','одно из')+')</span>':''}`;
    if(e[L]) h+=`<br>${esc(e[L])}`;
    if(e.type==='conflicts'&&e.price){ h+=`<br><span class="tk">${T('price','цена')}</span> ${esc(e.price[L])}<br><span class="tk">${T('mitigation','снятие')}</span> ${esc(e.mitig[L])}<br><span class="tk">${T('status','статус')}</span> ${esc(vt('CONSTAT',e.status))} · ${e.date}`; }
    return h; };
  const g=gEdges.selectAll('g').data(es).join('g').attr('class',e=>'edge '+e.type);
  g.append('path').attr('class','hit').attr('d',e=>edgePath(NODE[e.src],NODE[e.dst]));
  g.append('path').attr('class','vis').attr('d',e=>edgePath(NODE[e.src],NODE[e.dst])).attr('marker-end',e=>e.type==='requires'?'url(#arr)':null);
  g.on('mousemove',(ev,e)=>{if(tipPinned)return; tip.style.display='block'; tip.classList.add('wide'); tip.innerHTML=edgeTip(e); placeTip(ev);}).on('mouseleave',()=>{if(!tipPinned)hideTip();})
   .on('click',(ev,e)=>{ev.stopPropagation(); if(e.type==='conflicts'){ select(state.focus===e.src?e.dst:e.src); }})
   // touch (no hover): a tap on an edge shows its tip at the tap point, clamped by placeTip
   .on('pointerdown',(ev,e)=>{ if(ev.pointerType==='mouse'&&!noHover())return; ev.stopPropagation(); tipPinned=true; tip.style.display='block'; tip.classList.add('wide'); tip.innerHTML=edgeTip(e); placeTip(ev); }); }
// ---------- inspector
const insp=document.getElementById('insp');
function esc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
// no negative lookbehind here: Safari before 16.4 throws a SyntaxError on it and would kill the script.
// Instead match an already-built href="…" first and pass it through unchanged.
function lk(s){ return esc(s).replace(/arXiv:\s?((?:\d{4}\.\d{4,5}|[a-z\-]+\/\d{7})(?:v\d+)?)/g,(m,id)=>`<a href="https://arxiv.org/abs/${id}" target="_blank" rel="noopener">${m}</a>`).replace(/\b(10\.\d{4,9}\/[^\s,;)]+)/g,(m,d)=>`<a href="https://doi.org/${d}" target="_blank" rel="noopener">${m}</a>`).replace(/href="https?:\/\/[^"]*"|https?:\/\/[^\s<)]+/g,m=>m.indexOf('href="')===0?m:`<a href="${m}" target="_blank" rel="noopener">${m}</a>`); }
// card header: drag grip + dock buttons on desktop; on ≤ 1024 the card is a bottom sheet,
// so the dock buttons are hidden by CSS and a ⌃/⌄ button grows the sheet to 90vh instead.
function gripHTML(){ const sheet=insp.classList.contains('sheet-max');
  return '<div class="grip" data-grip="1">⠿ <span class="sp"></span>'+
    '<button type="button" data-dock="left" title="dock left">⇤</button>'+
    '<button type="button" data-dock="right" title="dock right">⇥</button>'+
    '<button type="button" data-sheet="1" aria-pressed="'+String(sheet)+'" aria-label="expand card">'+(sheet?'⌄':'⌃')+'</button>'+
    '<button type="button" data-close="1" aria-label="close">✕</button></div>'; }
function inspectPath(p){ const L=lang(); insp.hidden=false;
  const members=new Set(Object.values(p.slots).flat());
  const rows=G.layers.map(l=>{const ids=p.slots[String(l.n)]||[]; return `<tr><td class="ln">${l.n} ${esc(l[L])}</td><td>${ids.length?ids.map((id,i)=>`<a href="#" data-goto="${id}" class="${i?'alt':'prim'}">${esc(NODE[id][L])}</a>`).join('<span class="empty"> · </span>'):`<span class="empty">∅ ${T('empty slot','пустой слот')}</span>`}</td></tr>`;}).join('');
  const R=p.round||{}, RP=R.parts||{}, RX=p.react||{}, CO=p.coh||{}; const PN={gates:['gates','гейты'],transport:['transport','транспорт'],'1q':['1Q','1Q'],readout:['readout','считывание'],reset:['reset','сброс']};
  const fS=x=>{if(x==null)return '—'; if(x===0)return '0'; return fmtT(Math.log10(x));}; const fE=x=>x==null?'—':x.toExponential(1).replace('e+','e').replace('e-','e−');
  const hubs=[...members].filter(id=>NODE[id].hub), offs=[...members].filter(id=>NODE[id].offdiag&&NODE[id].offdiag.length), empties=[...members].filter(id=>NODE[id].status==='X');
  const rel=G.edges.filter(e=>members.has(e.src)&&members.has(e.dst)&&(e.type==='requires'||e.type==='replaces'||e.type==='conflicts'));
  const relRows=(type,head,glyph)=>{ const xs=rel.filter(e=>e.type===type); if(!xs.length)return ''; const nm=id=>`<a href="#" data-goto="${id}" title="${esc(NODE[id][L])}">${esc(SHORT[id]?SHORT[id][L==='en'?0:1]:NODE[id][L])}</a>`;
    return `<div><span class="tk">${glyph} ${head} · ${xs.length}</span></div>`+xs.map(e=>`<div class="rel ${e.type}">${nm(e.src)} <span class="empty">${type==='requires'?T('requires','требует'):type==='replaces'?T('alternative to','альтернатива для'):T('conflicts with','конфликтует с')}</span> ${nm(e.dst)}${e.any?' <span class="empty">('+T('one-of','одно из')+')</span>':''}${type==='conflicts'&&e.status?' <span class="empty">· '+esc(vt('CONSTAT',e.status))+'</span>':''}</div>`).join(''); };
  const relHTML=rel.length?relRows('requires',T('dependencies','зависимости'),'→')+relRows('conflicts',T('conflicts','конфликты'),'✕')+relRows('replaces',T('alternatives','альтернативы'),'⇄'):`<div class="empty">${T('no recorded relations among these stations','между этими станциями связей не записано')}</div>`;
  insp.innerHTML=`${gripHTML()}<h3><i class="sw" style="--c:${FAMC[p.family]}"></i> ${esc(p[L])}</h3><div class="meta">${T('platform path','путь платформы')} · ${p.id} · ${members.size} ${T('stations','станций')}</div>
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
  <div class="space"><h4>${T('Relations within the path','Связи внутри пути')}</h4>${relHTML}<div class="empty" style="margin-top:3px">${T('the edge toggles draw each type on the map, among these stations only','переключатели рёбер рисуют каждый тип на карте — только между этими станциями')}</div></div>
  <div class="space"><h4>${T('Reading','Чтение')}</h4><div>◎ ${T('hubs','хабы')}: ${hubs.length?hubs.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div><div>⤢ ${T('off-diagonal','внедиагональные')}: ${offs.length?offs.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div><div>∅ ${T('empty slots','пустые слоты')}: ${empties.length?empties.map(id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`).join(', '):'—'}</div></div>`;
  insp.querySelectorAll('[data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; scrollToNode(m);}));
  insp.querySelector('[data-close]').addEventListener('click',()=>{state.isolate=null; chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false')); inspectEmpty(); drawEdges(); dimming();}); wireCard();
}
function inspectEmpty(){ insp.hidden=true; insp.innerHTML=''; sheetRoom(); }
// ---------- machines (register): evidence glyphs, the machine card, the "Used by" block
const EVG=[[/figure/,'▣'],[/whitepaper/,'▥'],[/paper/,'▤'],[/vendor/,'▦'],[/datasheet/,'▧'],[/press/,'▨']];
function evGlyph(t){ t=String(t||''); for(const [re,g] of EVG)if(re.test(t))return g; return '◌'; }
// the glyph is the link to the evidence (title = its type), the locator follows in small type, then ✅ verified / 🔎 not yet
function evHTML(c){ const g=evGlyph(c[3]); const a=c[4]?`<a class="ev" href="${esc(c[4])}" target="_blank" rel="noreferrer" title="${esc(c[3]||'')}">${g}</a>`:`<span class="ev" title="${esc(c[3]||'')}">${g}</span>`;
  return a+(c[5]?` <span class="loc">${esc(c[5])}</span>`:'')+` <span class="vf" title="${c[6]?T('verified','проверено'):T('not verified','не проверено')}">${c[6]?'✅':'🔎'}</span>`; }
function machLabel(m){ return m.name+' · '+m.org; }
function inspectMachine(m){ const L=lang(); insp.hidden=false; const gaps=m.gaps||{};
  const rows=G.layers.map(l=>{ const k=String(l.n); const cells=(m.layers||{})[k]||[], gs=gaps[k]||[];
    const cellHTML=cells.map(c=>{ const n=NODE[c[0]]; const name=n?`<a href="#" data-goto="${c[0]}" class="${c[1]==='alternate'?'alt':'prim'}">${esc(n[L])}</a>`:esc(c[0]);
      return `<div class="mc">${name} <span class="empty">· ${c[1]==='alternate'?T('alternate','альтернатива'):T('primary','основная')}</span> ${evHTML(c)}${c[2]?`<div class="ms">${lk(c[2])}</div>`:''}</div>`; }).join('');
    const gapHTML=gs.map(g=>`<div class="mc empty">— (${T('Map gap','пробел Карты')}: ${esc(g)})</div>`).join('');
    return `<tr><td class="ln">${l.n} ${esc(l[L])}</td><td>${cellHTML+gapHTML||`<span class="empty">—</span>`}</td></tr>`; }).join('');
  const ev=m.ev||[0,0]; const q=(m.q!=null&&m.q!=='')?`${m.q} ${T('physical qubits','физических кубитов')}`:T('qubits not published','число кубитов не опубликовано');
  insp.innerHTML=`${gripHTML()}<h3><i class="sw" style="--c:${FAMC[m.family]||'var(--mid)'}"></i> ${esc(m.name)}</h3><div class="meta">${esc(m.org)} · ${T(...(FAMN[m.family]||[m.family,m.family]))} · ${esc(m.status)}${m.status_date?' ('+esc(m.status_date)+')':''} · ${q}</div>
  <div class="mlinks"><a href="${REG_URL(m.id)}" target="_blank" rel="noreferrer">↗ ${T('register card','карточка реестра')}</a> <span class="empty">· ${T('path','путь')}: ${PATH[m.path]?esc(PATH[m.path][L]):esc(m.path)}</span></div>
  <div class="space"><h4>${T('Stations by layer — the machine\'s cell per layer','Станции по слоям — ячейка машины на каждом слое')}</h4><table class="ptab mtab">${rows}</table>
   <div class="empty" style="margin-top:4px">${T('lit on the map: these stations and the machine\'s path line; dashed outline = used only as an alternate','подсвечено на карте: эти станции и линия пути машины; пунктирная рамка = только как альтернатива')}</div></div>
  <div class="mfoot"><span>${T('evidence','источники')}: ✅ ${ev[0]} / ${ev[1]}</span> <button type="button" class="chip" data-mclose="1">${T('clear machine','снять машину')} ✕</button></div>`;
  insp.querySelectorAll('[data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const n=NODE[a.dataset.goto]; if(n)scrollToNode(n);}));
  insp.querySelectorAll('[data-close],[data-mclose]').forEach(b=>b.addEventListener('click',ev=>{ev.stopPropagation(); setMachine(null);})); wireCard(); sheetRoom();
}
// "Used by" — the machines whose register cell on this station's layer is this station (primary first, then alternate, grouped by family)
function usedByHTML(n){ const L=lang(); const ub=MACH.by_node[n.id]||{primary:[],alternate:[]}; const P=(ub.primary||[]).filter(id=>MBY[id]), A=(ub.alternate||[]).filter(id=>MBY[id]&&!P.includes(id));
  const N=P.length+A.length; const head=N?`${T('Used by','Используют')} ${N} ${T(N===1?'machine':'machines','машин')} (${P.length} ${T('primary','основная')} · ${A.length} ${T('alternate','альтернатива')})`:T('Used by no registered machine','Не используется ни одной зарегистрированной машиной');
  if(!N)return `<div class="space useby"><h4>${head}</h4></div>`;
  const li=(id,role)=>{ const m=MBY[id]; const c=machCell(m,n.id); return `<li class="${role}${state.machine===id?' cur':''}"><a href="#" data-mach="${id}" title="${esc(machLabel(m))}">${esc(m.name)}</a> <span class="empty">${esc(m.org)}</span> <a class="reg" href="${REG_URL(id)}" target="_blank" rel="noreferrer" title="${T('register card','карточка реестра')}">↗</a>${c?' '+evHTML(c):''}${role==='alternate'?` <span class="empty">(${T('alternate','альтернатива')})</span>`:''}</li>`; };
  const fams=MACH.families||Object.keys(FAMC); const groups=fams.map(f=>{ const ps=P.filter(id=>MBY[id].family===f), as=A.filter(id=>MBY[id].family===f); if(!ps.length&&!as.length)return '';
    return `<li class="fam"><i class="sw" style="--c:${FAMC[f]||'var(--mid)'}"></i>${T(...(FAMN[f]||[f,f]))} <span class="empty">${ps.length+as.length}</span></li>`+ps.map(id=>li(id,'primary')).join('')+as.map(id=>li(id,'alternate')).join(''); }).join('');
  return `<div class="space useby"><h4>${head}</h4><ul class="useby">${groups}</ul><div class="empty" style="margin-top:4px">${T('click a machine to light its stations on the map · ↗ its register card','клик по машине подсвечивает её станции на карте · ↗ карточка реестра')}</div></div>`; }
function placeText(n){ const ps=(n.e.place&&n.e.place.length)?n.e.place:['none']; return CATS.place.filter(p=>ps.includes(p)).concat(ps.filter(p=>!CATS.place.includes(p))).map(p=>vt('PLACE',p)).join(' / '); }   // every stage the station carries, in the vocabulary's order (RT → 4 K → mK)
function inspect(n){ const L=lang(); const c=n.c; const rows=[[T('(a) carrier affinity','(a) сродство носителя'),vt('AFF',n.aff),'aff'],
  [T('(b) time · entangling','(b) время · перепутывание'),(n.b.t!=null?fmtT(n.b.t):'—')+(n.b.det!=='na'?' · '+vt('DET',n.b.det):''),'b'],
  [T('(c) readout','(c) считывание'),c?`${vt('MECH',c.mech)} · ${fmtT(c.t)} · ${c.destr?T('destructive','разрушающее'):T('non-destructive','неразрушающее')} · ${c.mid?'mid-circuit':T('no mid-circuit','без mid-circuit')}`:'—','c'],
  [T('(d) mobility','(d) подвижность'),vt('MOB',n.d),'d'],[T('(e) control','(e) управление'),n.e.mod==='none'?'—':`${vt('MOD',n.e.mod)} @ ${placeText(n)}`,'e'],
  [T('(f) error structure','(f) структура ошибки'),n.f.map(x=>vt('ERR',x)).join(', '),'f'],[T('(g) manufacturing','(g) производство'),vt('FAB',n.g),'g']];
  const lr=LENSROWS[state.lens]||[];
  // reading marks: one line per badge (hub — the N families beyond its own that require it; off-diagonal — its flag definitions; empty slot)
  const marks=[];
  if(isHub(n)){ const own=n._fam; let names=(n.reach||[]).filter(f=>f!==own); const N=n.reach_degree!=null?n.reach_degree:names.length; if(names.length!==N)names=n.reach||[];
    marks.push(`<div><span class="flag hub" title="${esc(T(...HUBDEF))}">◎ ${T('hub','хаб')}</span> — ${T('required by stations of','требуется станциям')} ${N} ${T(N===1?'family':'families',N===1?'семейства':'семейств')} (${esc(names.map(f=>T(...(FAMN[f]||[f,f]))).join(', '))})</div>`); }
  if(isOffd(n)) marks.push(`<div><span class="flag off" title="${esc(T(...OFFDEF))}">⤢ ${T('off-diagonal','внедиагональная')}</span> — ${esc(n.offdiag.map(o=>vt('OFFDIAG',o)).join('; '))}</div>`);
  if(isEmpty(n)) marks.push(`<div><span class="flag empty" title="${esc(T(...EMPTYDEF))}">∅ ${T('empty slot','пустой слот')}</span></div>`);
  const flags=marks.length?[`<div class="marks"><span class="tk">${T('Reading marks','Метки чтения')}</span>${marks.join('')}</div>`]:[];
  const reqOut=G.edges.filter(e=>e.type==='requires'&&e.src===n.id), reqIn=G.edges.filter(e=>e.type==='requires'&&e.dst===n.id), rep=G.edges.filter(e=>e.type==='replaces'&&(e.src===n.id||e.dst===n.id)), con=G.edges.filter(e=>e.type==='conflicts'&&(e.src===n.id||e.dst===n.id));
  const other=(e)=>e.src===n.id?e.dst:e.src;
  const link=id=>`<a href="#" data-goto="${id}">${esc(NODE[id][L])}</a>`;
  insp.innerHTML=`${gripHTML()}<h3>${esc(n[L])}</h3><div class="meta">${n.id} · ${T('layer','слой')} ${n.layer} ${esc(G.layers[n.layer-1][L])} · ${vt('STATUS',n.status)}${n.since<2030?' · '+T('since','с')+' '+n.since:''}</div>
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
   ${(reqOut.length||reqIn.length||rep.length||con.length)?`<div class="empty" style="margin-top:4px">° ${T('one-of dependency','зависимость «одно из»')}</div>`:`<p class="empty">—</p>`}</div>
  ${usedByHTML(n)}`;
  insp.querySelectorAll('[data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; scrollToNode(m);}));
  insp.querySelectorAll('[data-mach]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); setMachine(a.dataset.mach===state.machine?null:a.dataset.mach);}));
  insp.querySelector('[data-close]').addEventListener('click',()=>select(null)); wireCard();
}
pathHit.on('mousemove',(ev,p)=>{ if(tipPinned)return; pathSel.classed('hov',d=>d.id===p.id); tip.style.display='block'; tip.classList.remove('wide'); tip.innerHTML=`<i class="sw" style="background:${FAMC[p.family]}"></i><b>${esc(p[lang()])}</b> · ${T('click to isolate this path','клик — изолировать этот путь')}`; placeTip(ev); })
  .on('mouseleave',()=>{ pathSel.classed('hov',false); if(!tipPinned)hideTip(); })
  .on('click',(ev,p)=>{ ev.stopPropagation(); hideTip(); pathSel.classed('hov',false); isolatePath(p.id); });
document.querySelectorAll('#mapbar [data-goto]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault(); select(a.dataset.goto); const m=NODE[a.dataset.goto]; scrollToNode(m); document.getElementById('mapwrap').scrollIntoView({block:'nearest'});}));
// ---------- controls
const bar=document.getElementById('mapbar');
const chipsWrap=document.getElementById('pathchips');
function isolatePath(pid){ state.isolate=state.isolate===pid?null:pid; chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.chipPath===state.isolate))); if(state.isolate){ if(!state.focus){ inspectPath(PATH[pid]); pcHighlight(null); } } else if(!state.focus){ inspectEmpty(); } drawEdges(); dimming(); }   // a focused station stays focused: the three terms narrow each other
G.paths.forEach(p=>{const b=document.createElement('button'); b.className='chip'; b.dataset.chipPath=p.id; b.setAttribute('aria-pressed','false'); b.innerHTML=`<i class="sw" style="--c:${FAMC[p.family]}"></i><span class="t"></span>`; b.addEventListener('click',()=>isolatePath(p.id)); chipsWrap.appendChild(b);});
if(window.__placeZoom)window.__placeZoom();   // the zoom window sits at the end of the paths row (desktop) — chips exist now
const lensSel=document.getElementById('lens'); Object.keys(LENSES).forEach(k=>{const o=document.createElement('option'); o.value=k; lensSel.appendChild(o);}); lensSel.addEventListener('change',()=>{state.lens=lensSel.value; state.lensFilter=null; applyLens(); drawEdges(); dimming();});
// machine selector: one optgroup per family (register order), options "name · org" by name; the machine is one more term of the lit set
const machSel=document.getElementById('machine');
if(machSel){ (MACH.families||[]).forEach(f=>{ const ms=MACH.machines.filter(m=>m.family===f).sort((a,b)=>a.name.localeCompare(b.name)||a.org.localeCompare(b.org)); if(!ms.length)return;
    const og=document.createElement('optgroup'); og.dataset.fam=f; og.label=T(...(FAMN[f]||[f,f])); ms.forEach(m=>{ const o=document.createElement('option'); o.value=m.id; o.textContent=machLabel(m); og.appendChild(o); }); machSel.appendChild(og); });
  machSel.addEventListener('change',()=>setMachine(machSel.value||null)); }
function setMachine(id){ state.machine=(id&&MBY[id])?id:null; if(machSel&&machSel.value!==(state.machine||''))machSel.value=state.machine||'';
  drawEdges(); dimming();
  if(state.focus)inspect(NODE[state.focus]);                       // a focused station keeps its card; the machine stays a term of the lit set
  else if(state.machine)inspectMachine(MBY[state.machine]);
  else if(state.isolate)inspectPath(PATH[state.isolate]); else inspectEmpty(); }
window.__selectMachine=id=>{ setMachine(id||null); return state.machine; };
document.getElementById('tg-conf').addEventListener('click',ev=>{ if(window.__barSummary)setTimeout(window.__barSummary,0);state.showConf=!state.showConf; ev.currentTarget.setAttribute('aria-pressed',String(state.showConf)); drawEdges(); dimming();});
document.getElementById('tg-rep').addEventListener('click',ev=>{ if(window.__barSummary)setTimeout(window.__barSummary,0);state.showRep=!state.showRep; ev.currentTarget.setAttribute('aria-pressed',String(state.showRep)); drawEdges(); dimming();});
document.getElementById('tg-req').addEventListener('click',ev=>{ if(window.__barSummary)setTimeout(window.__barSummary,0);state.showReq=!state.showReq; ev.currentTarget.setAttribute('aria-pressed',String(state.showReq)); drawEdges(); dimming();});
// reset map: the default view — every path, the family lens with no value kept, no edges, nothing isolated or focused (zoom and the bar's collapsed state are view settings and stay)
document.getElementById('tg-reset').addEventListener('click',()=>{state.isolate=null; state.machine=null; if(machSel)machSel.value=''; st.classed('altuse',false); state.showConf=state.showRep=state.showReq=false; ['tg-conf','tg-rep','tg-req'].forEach(i=>document.getElementById(i).setAttribute('aria-pressed','false')); chipsWrap.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false'));
  state.lens='family'; state.lensFilter=null; lensSel.value='family'; applyLens(); select(null);});
// ---------- zoom: rendered width/height only, viewBox untouched (so the map stays crisp and text stays text)
const ZSTEPS=[0.5,0.6,0.7,0.85,1,1.25,1.5,2];   // the − / + buttons walk these
const ZMIN=0.2, ZMAX=2.5;                        // fit-width on a phone needs to go below ZSTEPS[0]
function applyZoom(z,keepCentre){
  z=Math.max(ZMIN,Math.min(ZMAX,z));
  const old=state.zoom||1; let fx=0,fy=0;
  if(keepCentre){ fx=(wrap.scrollLeft+wrap.clientWidth/2)/(W*old); fy=(wrap.scrollTop+wrap.clientHeight/2)/(H*old); }
  state.zoom=z; svg.attr('width',Math.floor(W*z)).attr('height',Math.floor(H*z));
  const el=document.getElementById('zoomlvl'); if(el&&document.activeElement!==el)el.value=Math.round(z*100)+'%';
  if(keepCentre){ wrap.scrollLeft=Math.max(0,fx*W*z-wrap.clientWidth/2); wrap.scrollTop=Math.max(0,fy*H*z-wrap.clientHeight/2); }
}
function zoomStep(d){ let i=0; for(let k=1;k<ZSTEPS.length;k++){ if(Math.abs(ZSTEPS[k]-state.zoom)<Math.abs(ZSTEPS[i]-state.zoom))i=k; } applyZoom(ZSTEPS[Math.max(0,Math.min(ZSTEPS.length-1,i+d))],true); }
(function(){ const zi=document.getElementById('zoom-in'), zo=document.getElementById('zoom-out'), zf=document.getElementById('zoom-fit'), z1=document.getElementById('zoom-100');
  if(zi)zi.addEventListener('click',()=>zoomStep(1));
  if(zo)zo.addEventListener('click',()=>zoomStep(-1));
  // fit width: a first pass can leave a horizontal bar when the vertical scrollbar appears (or vanishes) at the new
  // height and changes clientWidth; measure again after layout and settle on the width that actually fits.
  // scrollbar-aware fits: compute from the box that will exist at the target zoom, so pressing again changes nothing
  function sbSize(){ const d=document.createElement('div'); d.style.cssText='position:absolute;top:-9999px;left:-9999px;width:100px;height:100px;overflow:scroll;visibility:hidden'; document.body.appendChild(d); const r={w:d.offsetWidth-d.clientWidth,h:d.offsetHeight-d.clientHeight}; d.remove(); return r; }
  function box(){ const cs=getComputedStyle(wrap); const sb=sbSize(); const bw=(parseFloat(cs.borderLeftWidth)||0)+(parseFloat(cs.borderRightWidth)||0), bh=(parseFloat(cs.borderTopWidth)||0)+(parseFloat(cs.borderBottomWidth)||0);
    const w0=wrap.offsetWidth-bw; let h0=parseFloat(cs.maxHeight); if(!(h0>0))h0=wrap.offsetHeight-bh; return {w0:w0,h0:h0,sb:sb}; }
  function fitWidth(){ const b=box(); let z=(b.w0-2)/W; if(Math.floor(H*z)>b.h0) z=(b.w0-b.sb.w-2)/W; applyZoom(z,false); wrap.scrollLeft=0; }
  if(zf)zf.addEventListener('click',fitWidth);
  // fit height: the whole map, top to bottom, in the window — so it first does what align-top does (bar to the top of the
  // window, wrapper allowed to take the rest), instantly, then measures the height actually visible below the wrapper's
  // top edge and fits to that; if the page cannot scroll far enough for the bar to reach the top, the smaller visible
  // height wins, so the bottom of the map is never below the window
  function fitHeight(){ const off=pageBarH()+4; const bar=document.getElementById('mapbar')||wrap;
    wrap.classList.add('tall'); wrap.style.maxHeight=tallHeight()+'px';
    const y=bar.getBoundingClientRect().top+window.pageYOffset-off; window.scrollTo(0,Math.max(0,y));
    const b=box(); const cs=getComputedStyle(wrap); const bh=(parseFloat(cs.borderTopWidth)||0)+(parseFloat(cs.borderBottomWidth)||0);
    const top=wrap.getBoundingClientRect().top; const avail=Math.max(200,Math.min(b.h0,window.innerHeight-top-6));
    wrap.style.maxHeight=avail+'px';
    const inner=avail-bh; let z=(inner-1)/H; if(Math.floor(W*z)>b.w0) z=(inner-b.sb.h-1)/H;
    applyZoom(z,false); wrap.scrollTop=0; }
  const zfh=document.getElementById('zoom-fith'); if(zfh)zfh.addEventListener('click',fitHeight);
  // align top: the map *header* (the bar with the controls and the zoom window) goes to the top of the window and the map
  // takes the rest of the height; the wrapper keeps that height until the window is resized
  function pageBarH(){ const b=document.querySelector('.mobilebar'); return (b&&getComputedStyle(b).position==='sticky'&&b.offsetParent)?b.offsetHeight:0; }
  function tallHeight(){ const off=pageBarH()+4; const bar=document.getElementById('mapbar'); const gap=bar?(wrap.getBoundingClientRect().top-bar.getBoundingClientRect().top):0; return Math.max(300,window.innerHeight-off-gap-6); }
  function alignTop(){ const off=pageBarH()+4; const bar=document.getElementById('mapbar')||wrap; wrap.classList.add('tall'); wrap.style.maxHeight=tallHeight()+'px';
    const y=bar.getBoundingClientRect().top+window.pageYOffset-off; window.scrollTo({top:Math.max(0,y),behavior:'smooth'}); }
  const zt=document.getElementById('zoom-top'); if(zt)zt.addEventListener('click',alignTop);
  window.__refitTall=function(){ if(wrap.classList.contains('tall')){ wrap.style.maxHeight=tallHeight()+'px'; } };
  window.addEventListener('resize',window.__refitTall);
  if(z1)z1.addEventListener('click',()=>applyZoom(1,true));
  const zl=document.getElementById('zoomlvl');
  if(zl){ const commit=()=>{ const v=parseInt(String(zl.value).replace(/[^0-9]/g,''),10); if(!isNaN(v)&&v>0)applyZoom(v/100,true); zl.value=Math.round((state.zoom||1)*100)+'%'; };
    zl.addEventListener('focus',()=>{ zl.value=String(Math.round((state.zoom||1)*100)); try{zl.select();}catch(e){} });
    zl.addEventListener('keydown',ev=>{ if(ev.key==='Enter'){ev.preventDefault(); commit(); zl.blur();} else if(ev.key==='Escape'){ev.preventDefault(); zl.value=Math.round((state.zoom||1)*100)+'%'; zl.blur();} else if(ev.key==='ArrowUp'||ev.key==='ArrowDown'){ ev.preventDefault(); const cur=parseInt(String(zl.value).replace(/[^0-9]/g,''),10)||Math.round((state.zoom||1)*100); const nv=Math.max(Math.round(ZMIN*100),Math.min(Math.round(ZMAX*100),cur+(ev.key==='ArrowUp'?5:-5))); applyZoom(nv/100,true); zl.value=String(Math.round((state.zoom||1)*100)); } });
    zl.addEventListener('input',()=>{ const c=String(zl.value).replace(/[^0-9]/g,''); if(c!==zl.value)zl.value=c; });
    zl.addEventListener('blur',commit); }
  // phones: 0.85 only if station labels stay ≥ 10 px at that scale, otherwise 1.0
  let z=1;
  try{ if(window.matchMedia('(max-width:600px)').matches){ const t=wrap.querySelector('g.station text'); const fs=t?(parseFloat(getComputedStyle(t).fontSize)||11):11; z=(fs*0.85>=10)?0.85:1; } }catch(e){}
  applyZoom(z,false); })();
// collapsible map bar: one line with a summary of the current selection and the zoom window
(function(){ const bar=document.getElementById('mapbar'), tog=document.getElementById('bartog'), sum=document.getElementById('barsum'); if(!bar||!tog||!sum)return; const KEY='qmap.barcollapsed';
  function summary(){ const L=lang(); const parts=[];
    if(state.machine&&MBY[state.machine])parts.push(T('machine','машина')+': <b>'+esc(MBY[state.machine].name)+'</b>');
    if(state.isolate){ const p=PATH[state.isolate]; parts.push(`<i class="sw" style="background:${FAMC[p.family]}"></i><b>${esc(p[L])}</b>`); } else parts.push(T('all paths','все пути'));
    if(state.lens&&state.lens!=='family'){ const lz=LENSES[state.lens]; parts.push(T('lens','линза')+': <b>'+esc(lz?(lz[L]||lz.en||state.lens):state.lens)+'</b>'+(state.lensFilter!=null?' = <b>'+esc([...state.lensFilter].map(v=>catLabelSafe(state.lens,v)).join(', '))+'</b>':'')); }
    const ed=[]; if(state.showReq)ed.push(T('requires','требует')); if(state.showRep)ed.push(T('alternatives','альтернативы')); if(state.showConf)ed.push(T('conflicts','конфликты')); if(ed.length)parts.push(T('edges','рёбра')+': '+ed.join(', '));
    if(state.focus)parts.push(T('station','станция')+': <b>'+esc(NODE[state.focus][L])+'</b>');
    sum.innerHTML=parts.join(' · '); }
  function setC(c){ bar.classList.toggle('collapsed',c); tog.setAttribute('aria-expanded',String(!c)); tog.querySelector('.when-open').hidden=c; tog.querySelector('.when-closed').hidden=!c; sum.hidden=!c; if(c)summary(); try{localStorage.setItem(KEY,c?'1':'0');}catch(e){} if(window.__refitTall)window.__refitTall(); }
  window.__barSummary=()=>{ if(bar.classList.contains('collapsed'))summary(); };
  let c=false; try{c=localStorage.getItem(KEY)==='1';}catch(e){}
  setC(c); tog.addEventListener('click',()=>setC(!bar.classList.contains('collapsed')));
  document.querySelectorAll('[data-setlang]').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{ if(bar.classList.contains('collapsed'))summary(); },0)));
})();
// ---------- parallel coordinates
const pcHost=document.getElementById('pc');
const PCW=1100, PCH=300, PX0=70, PX1=PCW-30, PY0=34, PY1=PCH-46;
const pcsvg=d3.select(pcHost).append('svg').attr('viewBox',`0 0 ${PCW} ${PCH}`).attr('role','img').attr('aria-label','Parallel coordinates of all technologies across the seven design coordinates');
const AXES=[{k:'aff',en:'(a) carrier',ru:'(a) носитель'},{k:'b',en:'(b) time',ru:'(b) время'},{k:'c',en:'(c) readout',ru:'(c) считывание'},{k:'d',en:'(d) mobility',ru:'(d) подвижность'},{k:'e',en:'(e) control',ru:'(e) управление'},{k:'f',en:'(f) error',ru:'(f) ошибка'},{k:'g',en:'(g) fab',ru:'(g) производство'}];
const ORD={aff:[0,0.25,0.5,0.75,1],d:['none','static','shared','longrange','bus','transport','flying'],e:['none','lf@RT','mw@RT','eo@RT','opt@RT','mw@4K','lf@mK','mw@mK'],f:['none','pauli','coherent','leak','burst','bias','gauss','erasure','loss','unknown'],g:['none','sclitho','3d','cmos','mbe','mems','pic','optics','stm','diamond'],c:['none','spd','disp','erasure','s2c','qcap','fluor','img']};
const xAx=i=>PX0+i*(PX1-PX0)/(AXES.length-1);
const tScale=d3.scaleLinear().domain([-8.5,-1]).range([PY1,PY0]);
function yOf(n,k){ if(k==='aff')return PY1-(ORD.aff.indexOf(n.aff))*(PY1-PY0)/4; if(k==='b')return n.b.t==null?PY1+10:tScale(n.b.t); if(k==='c'){const m=n.c?n.c.mech:'none'; const i=ORD.c.indexOf(m); return PY1-i*(PY1-PY0)/(ORD.c.length-1);} if(k==='e'){const key=n.e.mod==='none'?'none':n.e.mod+'@'+((n.e.place&&n.e.place[0])||'none'); let i=ORD.e.indexOf(key); if(i<0)i=0; return PY1-i*(PY1-PY0)/(ORD.e.length-1);} const arr=ORD[k]; const v=k==='f'?(n.f[0]||'none'):n[k]; let i=arr.indexOf(v); if(i<0)i=0; return PY1-i*(PY1-PY0)/(arr.length-1); }
const pcAxes=pcsvg.append('g'); const pcLines=pcsvg.append('g'); const pcLabel=pcsvg.append('text').attr('x',PX0).attr('y',PCH-8).attr('fill','var(--ink)').attr('font-size',12).attr('font-weight',600);
function renderPC(){ pcAxes.selectAll('*').remove();
  AXES.forEach((a,i)=>{const g=pcAxes.append('g').attr('class','pc-axis'); const x=xAx(i); g.append('line').attr('x1',x).attr('x2',x).attr('y1',PY0-6).attr('y2',PY1+12); g.append('text').attr('class','t').attr('x',x).attr('y',PY0-14).attr('text-anchor','middle').text(a[lang()]);
    let ticks=[]; if(a.k==='aff')ticks=ORD.aff.map(v=>[PY1-ORD.aff.indexOf(v)*(PY1-PY0)/4,vt('AFF',v).split(' ')[0]]); else if(a.k==='b')ticks=[-8,-7,-6,-5,-4,-3,-2].map(v=>[tScale(v),fmtT(v)]); else if(a.k==='c')ticks=ORD.c.map((v,j)=>[PY1-j*(PY1-PY0)/(ORD.c.length-1),v==='none'?'—':vt('MECH',v).split(' ')[0]]); else if(a.k==='e')ticks=ORD.e.map((v,j)=>[PY1-j*(PY1-PY0)/(ORD.e.length-1),v==='none'?'—':v]); else {const arr=ORD[a.k], tab={d:'MOB',f:'ERR',g:'FAB'}[a.k]; ticks=arr.map((v,j)=>[PY1-j*(PY1-PY0)/(arr.length-1),v==='none'?'—':vt(tab,v).split(' ')[0]]);}
    ticks.forEach(([y,t])=>{g.append('line').attr('x1',x-3).attr('x2',x+3).attr('y1',y).attr('y2',y); g.append('text').attr('x',x+(i===AXES.length-1?-6:6)).attr('y',y+3.5).attr('text-anchor',i===AXES.length-1?'end':'start').text(t);}); });
  const pl=d3.line().x(d=>d[0]).y(d=>d[1]).curve(d3.curveMonotoneX);
  pcLines.selectAll('path').data(G.nodes,d=>d.id).join('path').attr('class','pcline').attr('stroke',d=>d._fam?FAMC[d._fam]:'var(--mid)').attr('d',d=>pl(AXES.map((a,i)=>[xAx(i),yOf(d,a.k)])))
    .on('mouseenter',(ev,d)=>{pcHighlight(d.id,true); pcLabel.text(d[lang()]);}).on('mouseleave',()=>{pcHighlight(state.focus); pcLabel.text(state.focus?NODE[state.focus][lang()]:'');}).on('click',(ev,d)=>{select(d.id); scrollToNode(d);});
  pcHighlight(state.focus); }
function pcHighlight(id,hover){ pcLines.selectAll('path').classed('hi',d=>d.id===id).classed('dim',d=>id?d.id!==id:(state.lensFilter!=null?!nodeMatchesFilter(d):false)); if(!hover)pcLabel.text(id?NODE[id][lang()]:''); }
// ---------- init
window.__relabelMap=relabel;
// theme changes must re-resolve the CSS colour tokens; buildScales/applyLens live in this closure
window.__mapTheme=function(){ buildScales(); applyLens(); };
// select a station from outside the map (used by the technology briefs)
window.__selectNode=function(id){ if(!NODE[id])return false; select(id); const m=NODE[id]; scrollToNode(m); return true; };
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
// ≤ 1024 the card is a bottom sheet: the stored desktop position is ignored and every inline
// position style is cleared so the sheet rules in the stylesheet apply.
function sheetMode(){ try{ return window.matchMedia('(max-width:1024px)').matches; }catch(e){ return false; } }
function placeCard(){ const o=cardState(); const w=insp.offsetWidth||336; const vw=window.innerWidth, vh=window.innerHeight;
  if(sheetMode()){ insp.style.left=''; insp.style.right=''; insp.style.top=''; insp.style.width=''; insp.style.height='';
    insp.querySelectorAll('[data-dock]').forEach(b=>b.setAttribute('aria-pressed','false')); return; }
  insp.classList.remove('sheet-max');
  if(o.mode==='free'&&o.x!=null){ insp.style.left=Math.max(0,Math.min(vw-w,o.x))+'px'; insp.style.top=Math.max(0,Math.min(vh-80,o.y))+'px'; insp.style.right='auto'; }
  else if(o.mode==='right'){ insp.style.left='auto'; insp.style.right='16px'; insp.style.top=(o.y!=null?Math.max(0,Math.min(vh-80,o.y)):84)+'px'; }
  else { insp.style.left='16px'; insp.style.right='auto'; insp.style.top=(o.y!=null?Math.max(0,Math.min(vh-80,o.y)):84)+'px'; }
  if(o.w){ insp.style.width=Math.min(o.w,vw-32)+'px'; }
  insp.querySelectorAll('[data-dock]').forEach(b=>b.setAttribute('aria-pressed',String((o.mode||'left')===b.dataset.dock))); }
function wireCard(){ placeCard();
  const sb=insp.querySelector('[data-sheet]');
  if(sb) sb.addEventListener('click',function(ev){ ev.stopPropagation(); const on=!insp.classList.contains('sheet-max');
    if(on) insp.classList.add('sheet-max'); else insp.classList.remove('sheet-max');
    sb.textContent=on?'⌄':'⌃'; sb.setAttribute('aria-pressed',String(on)); });
  if(sheetMode()) return;   // no dragging or docking on a bottom sheet
  insp.querySelectorAll('[data-dock]').forEach(b=>b.addEventListener('click',ev=>{ev.stopPropagation(); const o=cardState(); o.mode=b.dataset.dock; saveCard(o); placeCard();}));
  const g=insp.querySelector('[data-grip]'); if(!g)return;
  g.addEventListener('pointerdown',ev=>{ if(ev.target.closest('button'))return; ev.preventDefault(); const r=insp.getBoundingClientRect(); const dx=ev.clientX-r.left, dy=ev.clientY-r.top; insp.classList.add('dragging'); g.setPointerCapture(ev.pointerId);
    const mv=e=>{ insp.style.left=(e.clientX-dx)+'px'; insp.style.top=(e.clientY-dy)+'px'; insp.style.right='auto'; };
    const up=e=>{ g.removeEventListener('pointermove',mv); g.removeEventListener('pointerup',up); insp.classList.remove('dragging'); const rr=insp.getBoundingClientRect(); saveCard(Object.assign(cardState(),{mode:'free',x:rr.left,y:rr.top})); };
    g.addEventListener('pointermove',mv); g.addEventListener('pointerup',up); });
}
// the sheet is viewport-wide by design — never record that width as the desktop card width
new ResizeObserver(()=>{ if(insp.hidden||sheetMode())return; const o=cardState(); const w=insp.offsetWidth; if(w&&Math.abs((o.w||336)-w)>2){o.w=w; saveCard(o);} }).observe(insp);
window.addEventListener('resize',()=>{ if(!insp.hidden)placeCard(); });
try{ var __th=function(){ if(window.__mapTheme)window.__mapTheme(); };
  var __mq=matchMedia('(prefers-color-scheme: dark)');
  if(__mq.addEventListener)__mq.addEventListener('change',__th); else if(__mq.addListener)__mq.addListener(__th);
  new MutationObserver(__th).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']}); }catch(e){}

// ---------- zoom bar for the big tables (editor's review of 17 Sep 2026, item 3): fit width · 1:1 · percentage
// A table is big when its natural width exceeds its wrapper (div.tbl) by more than 8 px. It then gets a small .zoomctl row
// above it (div.tblzoom) and is scaled with a transform; a sizer (div.tblsizer) keeps the layout box in step with the
// scaled table, so no dead space and no clipped rows. Default: fit width; the choice is kept per table in memory only.
// Measuring is driven by a ResizeObserver on every wrapper (load, window resize, fold opened, language switched, brief
// opened — each changes the wrapper's width from/to 0 or to another value); the work itself runs in the next frame.
(function(){
  var ZMIN=0.2, ZMAX=2, SLACK=8;
  var wraps=[].slice.call(document.querySelectorAll('div.tbl')); if(!wraps.length)return;
  var ST=new WeakMap();
  function clamp(z){ return Math.max(ZMIN,Math.min(ZMAX,z)); }
  function tableOf(w){ var st=ST.get(w); return st?st.t:w.querySelector('table'); }
  function show(st,force){ if(force||document.activeElement!==st.lvl) st.lvl.value=Math.round(st.z*100)+'%'; }
  function mk(w,t){
    var s=document.createElement('div'); s.className='tblsizer'; w.insertBefore(s,t); s.appendChild(t);
    var bar=document.createElement('div'); bar.className='tblzoom';
    bar.innerHTML='<div class="zoomctl" role="group" aria-label="table zoom"><span class="tzl"><span class="lang-en">table</span><span class="lang-ru">таблица</span></span>'
      +'<button type="button" class="zb zt" data-tz="fit" title="fit width"><span class="tzi" aria-hidden="true">⟷</span><span class="lang-en">fit width</span><span class="lang-ru">по ширине</span></button>'
      +'<button type="button" class="zb zt" data-tz="one" title="actual size">1:1</button>'
      +'<input class="zlvl" type="text" inputmode="numeric" pattern="[0-9]*" value="100%" aria-label="table zoom percent — type a number (20–200) and press Enter" title="type a percentage (20–200) and press Enter"></div>';
    w.insertBefore(bar,s);
    var st={w:w,t:t,s:s,bar:bar,lvl:bar.querySelector('.zlvl'),natW:0,natH:0,z:1,mode:'fit'};
    ST.set(w,st);
    bar.querySelector('[data-tz="fit"]').addEventListener('click',function(){ st.mode='fit'; run([w]); });
    bar.querySelector('[data-tz="one"]').addEventListener('click',function(){ st.mode='one'; run([w]); });
    var lvl=st.lvl;
    function commit(){ var v=parseInt(String(lvl.value).replace(/[^0-9]/g,''),10); if(!isNaN(v)&&v>0&&v!==Math.round(st.z*100)){ st.mode='pct'; st.z=clamp(v/100); run([w]); } show(st); }
    lvl.addEventListener('focus',function(){ lvl.value=String(Math.round(st.z*100)); try{lvl.select();}catch(e){} });
    lvl.addEventListener('keydown',function(ev){ if(ev.key==='Enter'){ ev.preventDefault(); commit(); lvl.blur(); } else if(ev.key==='Escape'){ ev.preventDefault(); show(st,true); lvl.blur(); } });
    lvl.addEventListener('input',function(){ var c=String(lvl.value).replace(/[^0-9]/g,''); if(c!==lvl.value)lvl.value=c; });
    lvl.addEventListener('blur',commit);
    return st;
  }
  // one reflow for all reads: reset every table to its natural box, read, then apply
  function run(list){
    var jobs=[];
    list.forEach(function(w){ var t=tableOf(w); if(!t)return; var st=ST.get(w);
      t.style.transform=''; t.style.width=''; if(st){ st.s.style.width=''; st.s.style.height=''; } jobs.push([w,t,st]); });
    var reads=jobs.map(function(j){ var w=j[0], t=j[1]; var cw=w.clientWidth; return {cw:cw,big:cw>0&&t.scrollWidth>cw+SLACK,natW:t.offsetWidth,natH:t.offsetHeight}; });
    jobs.forEach(function(j,i){ var w=j[0], t=j[1], st=j[2], r=reads[i];
      if(!r.big){ if(st){ st.bar.hidden=true; w.classList.remove('zoomed'); } return; }
      if(!st) st=mk(w,t);
      st.natW=r.natW; st.natH=r.natH;
      var z=st.mode==='one'?1:(st.mode==='pct'?st.z:clamp(Math.min(1,(r.cw-2)/r.natW)));
      st.z=z; t.style.width=r.natW+'px'; t.style.transform=z===1?'':'scale('+z+')';
      st.s.style.width=Math.ceil(r.natW*z)+'px'; st.s.style.height=Math.ceil(r.natH*z)+'px';
      w.classList.toggle('zoomed',z!==1); st.bar.hidden=false; show(st); });
  }
  var pending=[], raf=0;
  function flush(){ raf=0; var l=pending; pending=[]; run(l); }
  function schedule(w){ if(pending.indexOf(w)<0)pending.push(w); if(!raf)raf=requestAnimationFrame(flush); }
  if(typeof ResizeObserver==='function'){
    var seen=new WeakMap();
    var ro=new ResizeObserver(function(entries){ entries.forEach(function(e){ var w=e.target, cw=Math.round(e.contentRect.width); if(seen.get(w)===cw)return; seen.set(w,cw); if(cw>0)schedule(w); }); });
    wraps.forEach(function(w){ ro.observe(w); });
  } else {
    var tm=0; var all=function(){ clearTimeout(tm); tm=setTimeout(function(){ run(wraps.filter(function(w){ return w.clientWidth>0; })); },150); };
    window.addEventListener('resize',all); document.addEventListener('toggle',all,true); all();
  }
})();

// ---------- sortable tables (editor's review of 17 Sep 2026, second batch, brief D): asc → desc → default order
// A div.tbl[data-sort] (tagged at build time) remembers its build order per tbody (WeakMap) and moves the same <tr> nodes
// when a header is clicked. data-sort decides which columns sort: `numeric` — every column where ≥ 60 % of the non-null body cells
// parse to a number (the first number in the text that is not glued to a letter, so `1Q ×1.0` reads 1.0 and `H2` reads
// nothing; `—`, `n/a`, `not published`, empty → null, last in both directions); `date` — the column headed date/дата or
// whose cells look like 2024-12 (also `Dec 2024`); `centrality` — the column headed centrality/центральность;
// `platform-default` — the first column's header restores the build order, the other columns are numeric.
// The ↺ button lives in the zoom bar (div.tblzoom) when the table has one showing, otherwise in a minimal bar of its own.
(function(){
  var wraps=[].slice.call(document.querySelectorAll('div.tbl[data-sort]')); if(!wraps.length)return;
  var NUM=/[-−+]?\d[\d,]*(\.\d+)?([eE][-+]?\d+)?/g, LET=/[A-Za-zА-Яа-яЁё]/;
  var MON={jan:1,feb:2,mar:3,apr:4,may:5,jun:6,jul:7,aug:8,sep:9,oct:10,nov:11,dec:12,'янв':1,'фев':2,'мар':3,'апр':4,'май':5,'мая':5,'июн':6,'июл':7,'авг':8,'сен':9,'окт':10,'ноя':11,'дек':12};
  function txt(el){ return (el.textContent||'').replace(/\s+/g,' ').trim(); }
  function isNull(s){ return s===''||/^(?:—|–|-|∅|n\/a|na|not published|не опубликовано)(?:$|[\s—–:;,.(])/i.test(s); }
  function num(s){
    if(isNull(s))return null; NUM.lastIndex=0; var m;
    while((m=NUM.exec(s))){ var a=m.index, b=a+m[0].length;
      if((a>0&&LET.test(s.charAt(a-1)))||(b<s.length&&LET.test(s.charAt(b))))continue;
      var v=parseFloat(m[0].replace(/,/g,'').replace('−','-')); return isNaN(v)?null:v; }
    return null;
  }
  function date(s){
    if(isNull(s))return null; var m=/(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?/.exec(s);
    if(m) return +m[1]*10000+(+(m[2]||0))*100+(+(m[3]||0));
    m=/([A-Za-zА-Яа-яЁё]{3})[A-Za-zА-Яа-яЁё.]*\s+(\d{4})/.exec(s); if(m&&MON[m[1].toLowerCase()]) return +m[2]*10000+MON[m[1].toLowerCase()]*100;
    return null;
  }
  function T(en,ru){ return '<span class="lang-en">'+en+'</span><span class="lang-ru">'+ru+'</span>'; }
  var ORIG=new WeakMap();
  wraps.forEach(function(w){
    var t=w.querySelector('table'); if(!t)return;
    var head=t.tHead&&t.tHead.rows[0]; if(!head)return;
    var bodies=[].slice.call(t.tBodies); if(!bodies.length)return;
    bodies.forEach(function(b){ ORIG.set(b,[].slice.call(b.rows)); });
    var ths=[].slice.call(head.cells), kind=w.getAttribute('data-sort'), n=ths.length;
    function colCells(i){ var out=[]; bodies.forEach(function(b){ [].forEach.call(b.rows,function(r){ if(r.cells[i]) out.push(r.cells[i]); }); }); return out; }
    // ≥ 60 % of the non-null body cells (— / n/a / empty do not count, so a sparse column such as 7.12 B's T2 still sorts), and ≥ 2 numbers
    function numeric(i){ var c=colCells(i), k=0, nn=0; c.forEach(function(x){ var s=txt(x); if(isNull(s))return; nn++; if(num(s)!==null)k++; }); return k>=2&&k>=0.6*nn; }
    var cols=[];   // per column: null (not sortable) | 'num' | 'date' | 'reset'
    for(var i=0;i<n;i++){
      var h=txt(ths[i]).toLowerCase(), c=null;
      if(kind==='numeric') c=numeric(i)?'num':null;
      else if(kind==='platform-default') c=i===0?'reset':(numeric(i)?'num':null);
      else if(kind==='date'){ if(/date|дата/.test(h)) c='date'; else { var cc=colCells(i); var k=0; cc.forEach(function(x){ if(/^\d{4}-\d{2}/.test(txt(x)))k++; }); if(cc.length&&k>=0.6*cc.length)c='date'; } }
      else if(kind==='centrality') c=/centrality|центральность/.test(h)?'num':null;
      cols.push(c);
    }
    if(!cols.some(function(c){return c;}))return;
    var state={col:-1,dir:0}, btns=[];
    ths.forEach(function(th,i){
      if(!cols[i]){ btns.push(null); return; }
      var b=document.createElement('button'); b.type='button'; b.className='sortbtn'+(cols[i]==='reset'?' sortreset':'');
      while(th.firstChild) b.appendChild(th.firstChild);
      if(cols[i]!=='reset'){ var ind=document.createElement('span'); ind.className='sortind'; ind.setAttribute('aria-hidden','true'); b.appendChild(ind); th.setAttribute('aria-sort','none'); }
      b.title=cols[i]==='reset'?'default order / исходный порядок':'sort: ascending → descending → default order';
      th.appendChild(b); btns.push(b);
      b.addEventListener('click',function(){
        if(cols[i]==='reset'){ restore(); return; }
        // first click: ascending, or descending when the table asks for it (data-sort-first="desc": the brief index's centrality — editor, 17 Sep)
        var first=w.getAttribute('data-sort-first')==='desc'?-1:1;
        var dir=state.col===i?(state.dir===first?-first:(state.dir===-first?0:first)):first;
        if(dir===0) restore(); else sortBy(i,dir);
      });
    });
    function keyOf(cell,i){ var s=txt(cell); return cols[i]==='date'?date(s):num(s); }
    function sortBy(i,dir){
      bodies.forEach(function(b){
        var orig=ORIG.get(b), rows=orig.map(function(r,k){ return {r:r,k:k,v:r.cells[i]?keyOf(r.cells[i],i):null}; });
        rows.sort(function(a,c){ if(a.v===null&&c.v===null)return a.k-c.k; if(a.v===null)return 1; if(c.v===null)return -1; return a.v===c.v?a.k-c.k:(a.v<c.v?-dir:dir); });
        rows.forEach(function(x){ b.appendChild(x.r); });
      });
      state.col=i; state.dir=dir; paint();
    }
    function restore(){ bodies.forEach(function(b){ ORIG.get(b).forEach(function(r){ b.appendChild(r); }); }); state.col=-1; state.dir=0; paint(); }
    function paint(){
      ths.forEach(function(th,i){ if(!cols[i]||cols[i]==='reset')return; var on=state.col===i;
        th.setAttribute('aria-sort',on?(state.dir===1?'ascending':'descending'):'none');
        var ind=btns[i].querySelector('.sortind'); ind.textContent=on?(state.dir===1?' ▲':' ▼'):''; });
      w.classList.toggle('sorted',state.col>=0); reset.classList.toggle('idle',state.col<0);
    }
    // ↺ default order: in the zoom bar when one is showing, else in a minimal bar of our own
    var reset=document.createElement('button'); reset.type='button'; reset.className='tsreset idle';
    reset.innerHTML='<span class="tsi" aria-hidden="true">↺</span> '+T('default order','исходный порядок');
    reset.addEventListener('click',restore);
    var bar=document.createElement('div'); bar.className='tblbar'; bar.appendChild(reset); w.insertBefore(bar,w.firstChild);
    function place(){
      var z=null; for(var c=w.firstElementChild;c;c=c.nextElementSibling){ if(c.classList.contains('tblzoom')){ z=c; break; } }
      var host=(z&&!z.hidden)?z:bar;
      if(reset.parentNode!==host) host.appendChild(reset);
      if(bar.hidden!==(host!==bar)) bar.hidden=(host!==bar);   // only on change: the observer watches `hidden`
    }
    place();
    if(typeof MutationObserver==='function') new MutationObserver(place).observe(w,{childList:true,attributes:true,attributeFilter:['hidden'],subtree:true});
  });
})();
"""
