BRIEF_JS = r"""
(function(){
'use strict';
var app=document.getElementById('app');
var openId=null, prevY=0;
function sec(id){ return document.getElementById('brief-'+id); }
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
