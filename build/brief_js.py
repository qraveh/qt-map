BRIEF_JS = r"""
(function(){
'use strict';
var app=document.getElementById('app');
var openId=null, prevY=0;
function sec(id){ return document.getElementById('brief-'+id); }
// the key-reference chips of every brief header are made at load from window.__KEYREFS (the technology cards' records): [n] short year, the IEEE entry as the tooltip
// load-time work on the page's text, re-run on every block a language fragment brings in (window.__hydrate, 27 Sep 2026)
var H=(window.__hydrators=window.__hydrators||[]);
(function(){ var K=window.__KEYREFS||{}; function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  // the IEEE text of work n is the brief's own Sources entry (the records carry no label since 27 Sep 2026); the page's own
  // language's list first, the English list as the fallback (a Russian page carries its lists in full)
  var PL=(document.getElementById('app')||{getAttribute:function(){return 'en';}}).getAttribute('data-page-lang')||'en';
  window.__keyLabel=function(sid,n){ var el=document.getElementById('brief-'+sid+'-'+PL+'-src-'+n)||document.getElementById('brief-'+sid+'-en-src-'+n); var r=el&&el.querySelector('.ref'); return r?r.textContent.trim():''; };
  function run(root){ var ds=(root||document).querySelectorAll('.bkeys[data-keys]'); for(var i=0;i<ds.length;i++){ var sid=ds[i].getAttribute('data-keys'); var rs=K[sid]||[]; var out='';
    for(var j=0;j<rs.length;j++){ var r=rs[j]; out+='<a href="'+esc(r.url)+'" target="_blank" rel="noopener" title="'+esc(window.__keyLabel(sid,r.n))+'">['+r.n+'] '+esc(r.short||'')+(r.year?' '+r.year:'')+'</a>'; }
    ds[i].insertAdjacentHTML('beforeend',' '+out); ds[i].removeAttribute('data-keys'); } }
  run(document); H.push(run); })();
// a Russian brief's Sources list is cloned from the English one (same works, same numbers, English entries): ids and §-links switch to ru
(function(){ function run(root){ var ols=(root||document).querySelectorAll('ol.refs[data-clone]'); for(var i=0;i<ols.length;i++){ var src=document.getElementById(ols[i].getAttribute('data-clone')); if(!src) continue;
  ols[i].innerHTML=src.innerHTML.split('-en-src-').join('-ru-src-').split('#en-s').join('#ru-s'); ols[i].removeAttribute('data-clone'); } }
  run(document); H.push(run); })();
// a self-labelled link (class u) is written without href: the address is its text (sources._link)
(function(){ function run(root){ var as=(root||document).querySelectorAll('a.u:not([href])'); for(var i=0;i<as.length;i++){ as[i].setAttribute('href',as[i].textContent); } }
  run(document); H.push(run); })();
function setHash(h){ try{ history.replaceState(null,'',h); }catch(e){ location.hash=h; } }
function closeBrief(restore){
  if(!openId) return;
  var s=sec(openId); if(s) s.hidden=true;
  openId=null;
  if((location.hash||'').indexOf('#brief-')===0) setHash('#briefs');
  if(restore) window.scrollTo(0,prevY);
}
function openBrief(id,noscroll){
  var s=sec(id); if(!s) return false;
  if(openId===id){ if(!noscroll) s.scrollIntoView({block:'start',behavior:'smooth'}); return true; }
  if(!openId) prevY=window.pageYOffset||document.documentElement.scrollTop||0;
  closeBrief(false);
  s.hidden=false; openId=id;
  setHash('#brief-'+id);
  if(!noscroll) s.scrollIntoView({block:'start',behavior:'smooth'});
  return true;
}
function gotoMap(id){
  closeBrief(false);
  if(window.__expandMap) window.__expandMap();
  if(window.__selectNode) window.__selectNode(id);
  var host=document.getElementById('mapbar')||document.getElementById('mapwrap');
  if(host) host.scrollIntoView({block:'start',behavior:'smooth'});
}
function gotoRow(id){
  var lang=app.getAttribute('data-lang')||'en';
  var rows=document.querySelectorAll('tr[data-row="'+id+'"]'), tr=null, i;
  for(i=0;i<rows.length;i++){ if(rows[i].closest('.lang-'+lang)){ tr=rows[i]; break; } }
  if(!tr) tr=rows[0];
  if(!tr) return;
  closeBrief(false);
  var d=tr.closest('details');
  while(d){ d.open=true; d=d.parentElement?d.parentElement.closest('details'):null; }
  tr.scrollIntoView({block:'center',behavior:'smooth'});
  tr.classList.add('rowflash');
  setTimeout(function(){ tr.classList.remove('rowflash'); },1800);
}
document.addEventListener('click',function(ev){
  var t=ev.target; if(!t||!t.closest) return;
  var c=t.closest('[data-briefclose]');
  if(c){ ev.preventDefault(); closeBrief(true); return; }
  var m=t.closest('[data-mapstation]');
  if(m){ ev.preventDefault(); gotoMap(m.getAttribute('data-mapstation')); return; }
  var r=t.closest('[data-tablerow]');
  if(r){ ev.preventDefault(); gotoRow(r.getAttribute('data-tablerow')); return; }
  var b=t.closest('[data-brief]');
  if(b){ ev.preventDefault(); openBrief(b.getAttribute('data-brief')); return; }
});
document.addEventListener('keydown',function(ev){
  if(ev.key==='Escape'&&openId) closeBrief(true);
});
window.addEventListener('hashchange',function(){
  var h=location.hash||'';
  if(h==='#brief-'+openId) return;
  if(h.indexOf('#brief-')===0) openBrief(h.slice(7));
  else if(openId) closeBrief(false);
});
window.openBrief=openBrief; window.closeBrief=closeBrief;
var h0=location.hash||'';
if(h0.indexOf('#brief-')===0) openBrief(h0.slice(7));
})();

document.addEventListener('click',function(ev){
  var a=ev.target.closest('a.cite'); if(!a)return; var id=a.getAttribute('href').slice(1); var t=document.getElementById(id); if(!t)return;
  ev.preventDefault(); var d=t.closest('details'); while(d){ d.open=true; d=d.parentElement?d.parentElement.closest('details'):null; }
  t.scrollIntoView({block:'center',behavior:'smooth'}); document.querySelectorAll('.srcn.hl').forEach(function(x){x.classList.remove('hl');}); t.classList.add('hl'); setTimeout(function(){t.classList.remove('hl');},2500);
});
"""
