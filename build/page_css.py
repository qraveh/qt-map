CSS = r"""
:root{
  color-scheme: light;
  --bg:#F3F5F8; --surface:#FFFFFF; --surface2:#EEF2F6; --ink:#16202B; --ink2:#46525F; --muted:#76838F; --rule:#D6DDE5; --rule2:#E7ECF1;
  --accent:#1F4E86; --focus:#2a78d6; --crit:#D03B3B; --warn:#B7791F;
  --nat:#EB6834; --fab:#2A78D6; --mid:#9AA3AD;
  --sc:#2A78D6; --ion:#EB6834; --atom:#1BAF7A; --photon:#4A3AA7; --spin:#E87BA4; --defect:#EDA100; --topo:#6C7684; --anneal:#8D97A3;
  --lens1:#CDE2FB; --lens2:#86B6EF; --lens3:#3987E5; --lens4:#1C5CAB;
  --shadow:0 1px 2px rgba(22,32,43,.06), 0 8px 24px rgba(22,32,43,.06);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme: dark;
    --bg:#0E141B; --surface:#151D26; --surface2:#1B2530; --ink:#E7ECF2; --ink2:#B9C3CE; --muted:#8895A3; --rule:#2A3642; --rule2:#1F2A35;
    --accent:#8FBFF5; --focus:#3987E5; --crit:#E05656; --warn:#D9A441;
    --nat:#D95926; --fab:#3987E5; --mid:#6C7682;
    --sc:#3987E5; --ion:#D95926; --atom:#199E70; --photon:#9085E9; --spin:#D55181; --defect:#C98500; --topo:#8A95A3; --anneal:#6F7A88;
    --lens1:#184F95; --lens2:#256ABF; --lens3:#5598E7; --lens4:#9EC5F4;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
  }
}
:root[data-theme="dark"]{
  color-scheme: dark;
  --bg:#0E141B; --surface:#151D26; --surface2:#1B2530; --ink:#E7ECF2; --ink2:#B9C3CE; --muted:#8895A3; --rule:#2A3642; --rule2:#1F2A35;
  --accent:#8FBFF5; --focus:#3987E5; --crit:#E05656; --warn:#D9A441;
  --nat:#D95926; --fab:#3987E5; --mid:#6C7682;
  --sc:#3987E5; --ion:#D95926; --atom:#199E70; --photon:#9085E9; --spin:#D55181; --defect:#C98500; --topo:#8A95A3; --anneal:#6F7A88;
  --lens1:#184F95; --lens2:#256ABF; --lens3:#5598E7; --lens4:#9EC5F4;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
}
html,body{background:var(--bg);color:var(--ink);}
body{margin:0;font-family:"Golos Text",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased;}
*{box-sizing:border-box}
a{color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:2px}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:3px}
.mono,code,kbd{font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
code{font-size:.85em;background:var(--surface2);padding:.05em .35em;border-radius:3px}
#app{max-width:1880px;margin:0 auto;padding:0 20px 80px}
/* language switching */
#app[data-lang="ru"] .lang-en{display:none !important}
#app[data-lang="en"] .lang-ru{display:none !important}
/* masthead */
.mast{display:grid;grid-template-columns:1fr auto;gap:18px 32px;align-items:end;padding:36px 0 20px;border-bottom:1px solid var(--rule)}
.eyebrow{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1.title{font-family:"Unbounded","Golos Text",system-ui,sans-serif;font-weight:700;font-size:clamp(26px,3.2vw,40px);line-height:1.08;letter-spacing:-.01em;margin:.35em 0 .3em;text-wrap:balance;max-width:24ch}
.subtitle{font-size:17px;color:var(--ink2);max-width:62ch;margin:0;text-wrap:pretty}
.controls{display:flex;flex-direction:column;align-items:flex-end;gap:10px}
.seg{display:inline-flex;border:1px solid var(--rule);border-radius:8px;overflow:hidden;background:var(--surface)}
.seg button{appearance:none;border:0;background:transparent;color:var(--ink2);font:inherit;font-weight:500;padding:7px 14px;cursor:pointer}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.jump{font-size:14px}
.thesis{margin:22px 0 0;padding:16px 20px;border-left:3px solid var(--fab);background:var(--surface);border-radius:0 8px 8px 0;font-size:15.5px;color:var(--ink2)}
.thesis b{color:var(--ink)}
/* layout */
.page{display:grid;grid-template-columns:236px minmax(0,1fr);gap:36px;margin-top:8px}
nav.toc{position:sticky;top:16px;align-self:start;max-height:calc(100vh - 32px);overflow:auto;padding-right:8px;font-size:13.5px}
nav.toc ol{list-style:none;margin:0;padding:0}
nav.toc li{margin:0;padding:3px 0}
nav.toc a{color:var(--ink2);text-decoration:none;display:flex;gap:8px}
nav.toc a .n{font-family:"JetBrains Mono",monospace;color:var(--muted);min-width:1.6em}
nav.toc a:hover{color:var(--ink)}
nav.toc .mapl a{color:var(--accent);font-weight:600}
main{min-width:0}
.prose{max-width:none}
.prose p,.prose ul,.prose ol,.prose blockquote,.prose dl{max-width:78ch}
.prose .tbl table,.bbody .tbl table,.bidx table{width:100%}
.prose h2{font-size:24px;font-weight:600;line-height:1.2;margin:2.4em 0 .7em;padding-top:.6em;border-top:1px solid var(--rule);display:flex;gap:14px;align-items:baseline;text-wrap:balance}
.prose h2 .num{font-family:"Unbounded",sans-serif;font-weight:500;font-size:15px;color:var(--muted);letter-spacing:.02em}
.prose h3{font-size:18px;font-weight:600;margin:1.8em 0 .5em;text-wrap:balance}
.prose p{margin:.7em 0;text-wrap:pretty}
.prose ul,.prose ol{padding-left:1.3em}
.prose li{margin:.3em 0}
.prose blockquote{margin:1em 0;padding:12px 18px;border-left:3px solid var(--rule);background:var(--surface);border-radius:0 8px 8px 0;color:var(--ink2)}
.prose hr{border:0;border-top:1px solid var(--rule);margin:2em 0}
.prose strong{font-weight:600}
.prose .m{font-family:"JetBrains Mono",monospace;font-size:.92em;white-space:nowrap}
.prose sup,.prose sub{line-height:0}
.tbl{max-width:none;overflow-x:auto;margin:1em 0;border:1px solid var(--rule);border-radius:8px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14px;font-variant-numeric:tabular-nums}
th,td{padding:8px 10px;border-bottom:1px solid var(--rule2);vertical-align:top;text-align:left}
th{font-weight:600;background:var(--surface2);position:sticky;top:0;white-space:nowrap}
tr:last-child td{border-bottom:0}
td code{white-space:nowrap}
.big-table table{font-size:12.5px}
.big-table th,.big-table td{padding:6px 8px}
details.fold{margin:1em 0;border:1px solid var(--rule);border-radius:8px;background:var(--surface)}
details.fold>summary{cursor:pointer;padding:10px 14px;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}
details.fold>summary::after{content:"+";font-family:"JetBrains Mono",monospace;color:var(--muted)}
details.fold[open]>summary::after{content:"–"}
details.fold>summary::-webkit-details-marker{display:none}
details.fold .tbl{border:0;border-top:1px solid var(--rule);border-radius:0;margin:0;max-height:70vh;overflow:auto}
/* radar small multiples */
.radars{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0 6px}
.radar{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:8px 6px 4px;text-align:center}
.radar svg{width:100%;height:auto;display:block}
.radar .cap{font-size:12.5px;color:var(--ink2);margin-top:2px}
.radar .cap b{color:var(--ink)}
.figcap{font-size:13px;color:var(--muted);margin:4px 0 14px}
/* map section */
.mapsec{margin:34px 0 10px}
.mapsec h2{font-size:24px;font-weight:600;margin:0 0 4px;display:flex;gap:14px;align-items:baseline}
.mapsec h2 .num{font-family:"Unbounded",sans-serif;font-weight:500;font-size:15px;color:var(--muted)}
.mapsec .lead{color:var(--ink2);max-width:80ch;margin:.2em 0 14px;text-wrap:pretty}
.mapbar{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:10px 12px;border:1px solid var(--rule);border-radius:10px 10px 0 0;background:var(--surface);font-size:13.5px}
.mapbar .grp{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.mapbar .lbl{color:var(--muted);font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-right:2px}
.chip{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);font:inherit;font-size:13px;padding:4px 10px 4px 8px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;line-height:1.2}
.chip .sw{width:10px;height:10px;border-radius:2px;background:var(--c);display:inline-block}
.chip[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.chip.off{opacity:.45}
.chip.tog[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
select.sel{font:inherit;font-size:13px;padding:4px 8px;border:1px solid var(--rule);border-radius:6px;background:var(--surface);color:var(--ink)}
.mapfull{margin-left:0}
.mapgrid{position:relative;display:grid;grid-template-columns:minmax(0,1fr);border:1px solid var(--rule);border-top:0;border-radius:0 0 10px 10px;background:var(--surface);overflow:hidden}
.mapwrap{overflow:auto;max-height:82vh;position:relative}
.mapwrap svg{display:block;font-family:"Golos Text",system-ui,sans-serif}
.station{cursor:pointer}
.station rect.box{fill:var(--surface);stroke:var(--mid);stroke-width:1.2}
.station.emerging rect.box{stroke-dasharray:3 2}
.station.empty rect.box{stroke-dasharray:6 3;fill:transparent}
.station.empty text{fill:var(--muted)}
.station text{fill:var(--ink);font-size:11px;pointer-events:none}
.station text.id{font-family:"JetBrains Mono",monospace;font-size:9px;fill:var(--muted)}
.station.offd rect.box{stroke-width:2}
.station.member rect.box{stroke-width:2.4;stroke:var(--ink)}
.station.peek rect.box{stroke-width:3;stroke:var(--ink)}
.tip .sw{display:inline-block;width:9px;height:9px;border-radius:2px;margin:0 3px 0 0;vertical-align:-1px}
.tip .sw.hollow{background:transparent;border:1.5px solid}
.mapcol{margin-left:auto;font-size:12px;font-weight:500;align-self:center}
#mapbody[hidden]{display:none}
.insp h3 .sw{width:11px;height:11px;border-radius:3px;background:var(--c);display:inline-block;margin-right:4px}
.ptab{border-collapse:collapse;width:100%;font-size:12.5px}
.ptab td{padding:3px 6px 3px 0;vertical-align:top;border-top:1px solid var(--rule2,var(--rule))}
.ptab td.ln{white-space:nowrap;color:var(--muted);font-family:"JetBrains Mono",monospace;font-size:10.5px;padding-right:10px}
.ptab a.prim{font-weight:600}
.ptab a.alt{color:var(--ink2)}
.insp .keys .kr{margin:3px 0;font-size:12.5px;line-height:1.35}
.insp .keys a{font-family:"JetBrains Mono",monospace;font-size:11px}
.bkeys{margin:10px 0 0;font-size:12.5px;color:var(--ink2);display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline}
.bkeys a{font-family:"JetBrains Mono",monospace;font-size:11.5px;text-decoration:none;border:1px solid var(--rule);border-radius:999px;padding:1px 7px;color:var(--ink)}
.bkeys a:hover{border-color:var(--ink)}
.bbody a.cite{font-family:"JetBrains Mono",monospace;font-size:.85em;text-decoration:none;color:var(--accent);padding:0 1px}
.bbody a.cite:hover{text-decoration:underline}
.bbody .srcn{font-family:"JetBrains Mono",monospace;font-size:.9em;color:var(--muted);scroll-margin-top:90px;border-radius:4px;padding:0 2px}
.bbody .srcn.hl,.bbody li.hl .srcn{background:var(--accent);color:var(--bg)}
.bbody .fold-src a[href^="http"]{word-break:break-all}
.bbody .fold-src ol{list-style:none;padding-left:0}
.bbody .fold-src li{margin:.35em 0}
.station.hub rect.box{stroke-width:2}
.station.dim{opacity:.22}
.station.sel rect.box{stroke:var(--ink);stroke-width:2.5}
.laneh text{fill:var(--ink2);font-size:11.5px;font-weight:600}
.laneh text.sub{fill:var(--muted);font-weight:400;font-size:10.5px;font-family:"JetBrains Mono",monospace}
.bandl text{fill:var(--muted);font-size:10.5px;font-family:"JetBrains Mono",monospace;letter-spacing:.04em}
.bandline{stroke:var(--rule);stroke-dasharray:2 4}
.pathline{fill:none;stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round;opacity:.85}
.pathline.dim{opacity:.08}
.pathline.neutral{stroke-dasharray:7 5}
.altstub{fill:none;stroke-width:1.2;stroke-dasharray:2 3;opacity:.7}
.altstub.dim{opacity:.05}
.edge{fill:none;stroke-width:1.6}
.edge path.hit{stroke:transparent;stroke-width:14;stroke-dasharray:none;pointer-events:stroke;cursor:pointer}
.edge:hover path.vis{stroke-width:3}
.tip.wide{max-width:440px}
.edge.requires{stroke:var(--ink);opacity:.9}
.edge.replaces{stroke:var(--ink2);stroke-dasharray:5 4}
.edge.conflicts{stroke:var(--crit);stroke-dasharray:3 3;stroke-width:2}
.badge{stroke:none}
.hatch{fill:url(#hatch)}
.tip{position:absolute;pointer-events:none;background:var(--ink);color:var(--bg);font-size:12px;padding:6px 9px;border-radius:6px;max-width:280px;line-height:1.35;box-shadow:var(--shadow);z-index:5;display:none}

/* lens */
.lensed .pathline{stroke:var(--mid) !important;opacity:.28}
.lensed .altstub{stroke:var(--mid) !important;opacity:.35}
.lensed .badge{opacity:.35}
.legend .lk{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);font:inherit;font-size:12.5px;padding:2px 8px 2px 6px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.legend .lk .sw{width:10px;height:10px;border-radius:2px;display:inline-block}
.legend .lk .cnt{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--muted)}
.legend .lk[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.legend .lk.clear{border-style:dashed}
.mapbar .lenslegend{flex-basis:100%;gap:6px 8px;align-items:center;padding-top:6px;border-top:1px dashed var(--rule)}
.mapbar .lenslegend:empty{display:none}
.mapbar .lenslegend .lbl{margin-right:6px}
.lg.band{width:16px;height:12px;border:1px solid var(--sc);border-left:4px solid #2FA66A;border-radius:3px;background:rgba(47,166,106,.22)}
.lg.badges{width:18px;height:12px;display:inline-flex;gap:2px;align-items:flex-end}
.lg.badges b{display:inline-block;width:7px;height:4px;border-radius:1px;background:var(--sc)}
.lg.badges b+b{background:none;border:1px solid var(--atom)}
.insp dl .lensrow{background:var(--surface);box-shadow:inset 3px 0 0 var(--accent);padding-left:6px}
.mast .author{margin:10px 0 0;font-size:15px;color:var(--ink2)}
.mast .author b{color:var(--ink);font-weight:600}
.mast .title .yr{color:var(--muted);font-weight:500}
.pubmeta{margin-top:12px;font-size:12.5px;color:var(--muted);text-align:right;line-height:1.6}
.pubmeta a{color:var(--ink2)}
.colophon{margin:48px 0 0;padding:20px 0 0;border-top:1px solid var(--rule);font-size:13.5px;color:var(--ink2);max-width:90ch}
.colophon p{margin:.6em 0;text-wrap:pretty}
.colophon b{color:var(--ink)}
/* inspector */
.insp{position:fixed;top:84px;left:16px;width:336px;max-height:calc(100vh - 100px);border:1px solid var(--rule);border-radius:12px;padding:0 16px 14px;overflow:auto;font-size:13.5px;background:var(--surface);box-shadow:0 12px 36px rgba(0,0,0,.16);z-index:40;resize:both;min-width:280px;min-height:200px}
.insp .grip{position:sticky;top:0;display:flex;align-items:center;gap:6px;margin:0 -16px 8px;padding:6px 10px;background:var(--surface2);border-bottom:1px solid var(--rule);cursor:move;user-select:none;font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);z-index:2}
.insp .grip .sp{flex:1}
.insp .grip button{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);font:inherit;font-size:11px;padding:1px 7px;border-radius:6px;cursor:pointer}
.insp .grip button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.insp.dragging{opacity:.92}
.insp[hidden]{display:none}
.insp .iclose{display:none}
.insp .conf{margin:6px 0 8px;padding:6px 8px;border-left:2px solid var(--crit);background:var(--surface)}
.insp .conf .cm{color:var(--ink2);margin-top:2px}
.tk{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-right:4px}
.tip .tk{color:var(--bg);opacity:.7}
.cst{font-family:"JetBrains Mono",monospace;font-size:10.5px;padding:1px 6px;border-radius:999px;border:1px solid var(--rule);color:var(--ink2);margin-left:6px}
.cst.open{border-color:var(--crit);color:var(--crit)}
.cst.mitigated{border-color:var(--atom);color:var(--atom)}
.mapbar .glyphs{flex-basis:100%;gap:6px 14px;color:var(--ink2);font-size:12.5px}
.gl{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.lg{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;font-style:normal;font-size:12px;color:var(--ink)}
.lg.hub{color:var(--accent)}
.lg.off{color:var(--crit)}
.lg.emp{color:var(--muted)}
.lg.ed{width:22px;height:0;border-top:2px solid var(--ink)}
.lg.ed.rep{border-top-style:dashed;border-color:var(--ink2)}
.lg.ed.con{border-top-style:dotted;border-color:var(--crit)}
.gl.try a{color:var(--accent)}
.insp h3{margin:0 0 2px;font-size:17px;line-height:1.25;text-wrap:balance}
.insp .meta{color:var(--muted);font-family:"JetBrains Mono",monospace;font-size:11.5px;margin-bottom:10px}
.insp .space{margin:12px 0;padding:10px 12px;border-radius:8px;background:var(--surface2)}
.insp .space h4{margin:0 0 6px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-family:"JetBrains Mono",monospace}
.insp dl{display:grid;grid-template-columns:auto 1fr;gap:3px 10px;margin:0}
.insp dt{color:var(--muted);white-space:nowrap}
.insp dd{margin:0}
.insp .def{border-top:1px dashed var(--rule);padding:6px 0}
.insp .def:first-of-type{border-top:0}
.insp .def .k{color:var(--ink2)}
.insp .def .d{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--muted)}
.insp .pathtag{display:inline-flex;align-items:center;gap:6px;margin:2px 6px 2px 0}
.insp .pathtag .sw{width:10px;height:3px;border-radius:2px;background:var(--c);display:inline-block}
.insp .flag{display:inline-block;padding:1px 7px;border-radius:999px;font-size:12px;border:1px solid var(--rule);margin:2px 4px 2px 0}
.insp .flag.off{border-color:var(--nat);color:var(--ink)}
.insp .flag.hub{border-color:var(--fab)}
.insp .flag.empty{border-style:dashed}
.insp .empty{color:var(--muted)}
.legend{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:12.5px;color:var(--ink2);padding:10px 12px;border:1px solid var(--rule);border-top:0;background:var(--surface);border-radius:0 0 10px 10px;margin-top:-1px}
.legend .k{display:inline-flex;align-items:center;gap:6px}
.legend svg{width:26px;height:16px}
/* parallel coordinates */
.pcwrap{margin-top:14px;border:1px solid var(--rule);border-radius:10px;background:var(--surface);padding:10px 12px 4px}
.pcwrap h3{margin:0 0 4px;font-size:15px}
.pcwrap p{margin:0 0 6px;color:var(--ink2);font-size:13px}
.pcwrap svg{width:100%;height:auto;display:block;font-family:"Golos Text",system-ui,sans-serif}
.pc-axis line{stroke:var(--rule)}
.pc-axis text{fill:var(--muted);font-size:10.5px}
.pc-axis text.t{fill:var(--ink2);font-weight:600;font-size:11.5px}
.pcline{fill:none;stroke-width:1.1;opacity:.45}
.pcline.hi{stroke-width:2.6;opacity:1}
.pcline.dim{opacity:.06}
/* ---------- technology briefs ---------- */
[hidden]{display:none !important}
.insp .briefbtn{display:inline-flex;align-items:center;gap:6px;margin:10px 0 2px;padding:5px 12px;border:1px solid var(--accent);border-radius:999px;background:var(--surface);color:var(--accent);font:inherit;font-size:13px;font-weight:600;cursor:pointer}
.insp .briefbtn:hover{background:var(--accent);color:var(--bg)}
.briefs{margin:2.4em 0 0;padding-top:.6em;scroll-margin-top:12px}
.briefs h2{font-size:24px;font-weight:600;line-height:1.2;margin:0 0 .7em;padding-top:.6em;border-top:1px solid var(--rule);display:flex;gap:14px;align-items:baseline;text-wrap:balance}
.briefs h2 .num{font-family:"Unbounded",sans-serif;font-weight:500;font-size:15px;color:var(--muted);letter-spacing:.02em}
.blede{max-width:78ch;color:var(--ink2)}
.blede p{margin:.7em 0;text-wrap:pretty}
.bidx table{font-size:13px}
.bidx td.r{text-align:right;font-family:"JetBrains Mono",monospace;color:var(--muted);white-space:nowrap}
.bidx td.ol{color:var(--ink2);font-size:12.5px;min-width:28ch}
.bidx tbody tr{cursor:pointer}
.bidx tbody tr:hover{background:var(--surface2)}
a.bref{text-decoration:none}
a.bref code{cursor:pointer;color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:2px}
a.bref:hover code{background:var(--accent);color:var(--bg);text-decoration-color:transparent}
tr.rowflash>td{background:color-mix(in srgb,var(--focus) 20%,transparent)}
/* one brief */
.brief{display:block;max-width:none;margin:18px 0;padding:18px 22px 14px;border:1px solid var(--rule);border-radius:12px;background:var(--surface);box-shadow:var(--shadow);scroll-margin-top:12px}
.brief-head{border-left:4px solid var(--fam,var(--mid));padding:2px 0 2px 14px;margin:0 0 16px}
.brief-head .bclose{float:right;margin-left:12px}
.bmeta{font-family:"JetBrains Mono",monospace;font-size:11.5px;color:var(--muted);letter-spacing:.02em}
.bmeta .bid{color:var(--fam,var(--ink2));font-weight:500}
.btitle{font-family:"Unbounded","Golos Text",system-ui,sans-serif;font-weight:700;font-size:clamp(20px,2.2vw,27px);line-height:1.15;letter-spacing:-.01em;margin:.25em 0 .3em;text-wrap:balance;max-width:26ch}
.bone{margin:.2em 0 .7em;color:var(--ink2);max-width:78ch;text-wrap:pretty}
.bverdict{margin:0;padding:10px 14px;max-width:78ch;background:var(--surface2);border-left:3px solid var(--fam,var(--accent));border-radius:0 8px 8px 0;text-wrap:pretty}
.bverdict b{color:var(--ink)}
.bbody{max-width:none}
.bbody p,.bbody ul,.bbody ol{max-width:78ch}
.bbody h3.bh3{font-size:17px;font-weight:600;margin:1.7em 0 .5em;padding-top:.7em;border-top:1px solid var(--rule2);text-wrap:balance}
.bbody p{margin:.7em 0;text-wrap:pretty}
.bbody ul,.bbody ol{padding-left:1.3em}
.bbody li{margin:.25em 0}
.bbody .m{font-family:"JetBrains Mono",monospace;font-size:.92em;white-space:nowrap}
.bbody sup,.bbody sub{line-height:0}
.bbody .tbl{max-width:100%;overflow-x:auto}
.bbody table{font-size:12.5px}
.bbody th,.bbody td{padding:6px 8px}
.bbody th{position:static}
.bbody details.bfold{margin:1.4em 0 .4em}
.bbody details.bfold>summary{font-size:15px}
.bbody .bfoldin{padding:2px 14px 10px;border-top:1px solid var(--rule)}
.bbody .bfoldin p{font-size:13px;color:var(--ink2);word-break:break-word}
.bbody a{word-break:break-word}
/* evidence tags */
.tag{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;line-height:1.35;padding:1px 4px;margin:0 1px;border:1px solid var(--rule);border-radius:3px;background:var(--surface2);color:var(--ink2);cursor:help;white-space:nowrap;vertical-align:.08em}
.tag-D{border-color:var(--atom);color:var(--atom)}
.tag-C{border-color:var(--nat);color:var(--nat)}
.tag-R{border-color:var(--warn);color:var(--warn)}
.tag-S{border-color:var(--photon);color:var(--photon)}
.tag-G{border-color:var(--mid);color:var(--ink2)}
.tag-P{border-color:var(--spin);color:var(--spin)}
.tag-reg{border-style:dashed;border-color:var(--rule);color:var(--muted);background:transparent}
a.tag-link{text-decoration:none;border-bottom:1px solid var(--accent);cursor:pointer}
a.tag-link:hover{background:var(--accent);color:var(--bg)}
.bnav{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 2px;padding-top:12px;border-top:1px solid var(--rule)}
.bnav .chip{font-size:12.5px}
@media (max-width:900px){.brief{padding:14px 14px 10px}.bidx td.ol{display:none}.bidx th:last-child{display:none}}
@media (max-width:1100px){.insp{width:min(336px,92%);left:8px;top:64px}}
@media (max-width:900px){.mapfull{margin-left:0}.page{grid-template-columns:1fr}nav.toc{position:static;max-height:none;display:none}.mast{grid-template-columns:1fr}.controls{align-items:flex-start}}
@media (prefers-reduced-motion:no-preference){.station rect.box,.pathline,.altstub,.pcline{transition:opacity .25s ease}}
@media print{.mapbar,.controls{display:none}.mapwrap{max-height:none;overflow:visible}#app{max-width:none}}
"""
