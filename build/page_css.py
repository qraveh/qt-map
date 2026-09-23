CSS = r"""
:root{
  color-scheme: light;
  --bg:#F3F5F8; --surface:#FFFFFF; --surface2:#EEF2F6; --ink:#16202B; --ink2:#46525F; --muted:#76838F; --rule:#D6DDE5; --rule2:#E7ECF1;
  --accent:#1F4E86; --focus:#2a78d6; --crit:#D03B3B; --warn:#B7791F;
  --nat:#EB6834; --fab:#2A78D6; --mid:#9AA3AD;
  --sc:#2A78D6; --ion:#EB6834; --atom:#1BAF7A; --photon:#4A3AA7; --spin:#E87BA4; --defect:#EDA100; --topo:#6C7684; --anneal:#8D97A3;
  --lens1:#CDE2FB; --lens2:#86B6EF; --lens3:#3987E5; --lens4:#1C5CAB;
  --shadow:0 1px 2px rgba(22,32,43,.06), 0 8px 24px rgba(22,32,43,.06);
  --surface-t0:rgba(255,255,255,0);   /* fully transparent twin of --surface (fade masks) */
  --surface-t85:rgba(255,255,255,.85); /* translucent twin (zoom row) */
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
    --surface-t0:rgba(21,29,38,0);
  --surface-t85:rgba(21,29,38,.85);
    --surface-t85:rgba(21,29,38,.85);
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
  --surface-t0:rgba(21,29,38,0);
}
html,body{background:var(--bg);color:var(--ink);}
body{margin:0;font-family:"Golos Text",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased;}
*{box-sizing:border-box}
a{color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:2px}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:3px}
.mono,code,kbd{font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
code{font-size:.85em;background:var(--surface2);padding:.05em .35em;border-radius:3px}
#app{max-width:none;margin:0 auto;padding:0 24px 80px}
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
.prose p{margin:.7em 0;text-wrap:pretty;text-align:justify;hyphens:auto;-webkit-hyphens:auto}   /* justified running text with automatic hyphenation (lang attributes on the prose blocks); lists, tables and captions stay left-aligned */
.prose li p,.prose td p,.prose th p,.prose .empty,.prose p.small{text-align:left}
@media (max-width:700px){.prose p{text-align:left}}
.prose ul,.prose ol{padding-left:1.3em}
.prose li{margin:.3em 0}
/* labelled items "(a) …", "(i) …" hang their label; definition-style items "Term — text" put the term on its own line (21 Sep 2026) */
.prose li.lbl{list-style:none;position:relative;padding-left:2.5em}
.prose li.lbl .lb{position:absolute;left:0;color:var(--muted);font-variant-numeric:tabular-nums}
.prose ol ol,.prose ol ul,.prose ul ol{margin:.35em 0 .5em}
.prose li.def>strong,.prose li.def>p>strong{display:block;margin-bottom:.12em}
.prose li.def{margin:.55em 0}
.prose ol.es>li{text-align:justify;hyphens:auto;-webkit-hyphens:auto}
@media (max-width:700px){.prose ol.es>li{text-align:left}}
.mast .author .orcid{display:inline-block;line-height:0;margin-left:2px;vertical-align:-3px;border-radius:50%}
.mast .author .orcid:hover{box-shadow:0 0 0 2px var(--accent)}
.mast .author .orcid-id{display:block}
.pubmeta .ghlink{display:inline-flex;align-items:center;gap:4px;text-decoration:none}
.pubmeta .ghlink:hover span{text-decoration:underline}
/* references: source codes and cross-references are links; a source entry's own code is its anchor */
.prose a.cite{text-decoration:none;font-variant-numeric:tabular-nums}
.prose a.cite:hover{text-decoration:underline}
.prose a.xref{text-decoration:none;border-bottom:1px dotted currentColor}
.prose a.xref:hover{border-bottom-style:solid}
.prose .src{font-weight:600;scroll-margin-top:70px}
/* §9 (23 Sep 2026): one IEEE-numbered list — hanging numbers, entries in a slightly smaller size, long URLs allowed to break */
.prose ol.refs{list-style:none;padding-left:0;margin:8px 0 0}
.prose ol.refs li{position:relative;padding-left:3.4em;margin:0 0 7px;font-size:.93em;line-height:1.5;text-align:left;scroll-margin-top:70px}
.prose ol.refs li .src{position:absolute;left:0;top:0;width:2.9em;text-align:right;font-variant-numeric:tabular-nums}
.prose ol.refs li:target{background:var(--surface2);box-shadow:0 0 0 4px var(--surface2);border-radius:3px}
.prose ol.refs li a{overflow-wrap:anywhere}
.prose .refnote{font-size:.92em;color:var(--muted);margin-top:6px}
/* tooltips on terms: a faint dotted underline marks a term the page explains in place; the text is shown by #gtip (script) */
.tt{text-decoration:underline dotted;text-decoration-color:var(--muted);text-underline-offset:3px;cursor:help;outline:none}
.tt:hover,.tt:focus{text-decoration-color:var(--accent)}
th .tt,td .tt{text-decoration-thickness:1px}
#gtip{position:absolute;z-index:60;max-width:min(400px,calc(100vw - 24px));padding:.5rem .65rem;border:1px solid var(--rule);border-radius:8px;background:var(--surface);color:var(--ink);font:400 .86rem/1.45 system-ui,sans-serif;text-align:left;box-shadow:0 6px 24px rgba(0,0,0,.14);white-space:normal;user-select:text;-webkit-user-select:text;cursor:text}
#gtip.pinned{border-color:var(--accent)}
#gtip[hidden]{display:none}
.prose [id^="en-h"],.prose [id^="ru-h"],.prose td[id],.prose figure[id]{scroll-margin-top:70px}
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
.mapsec{margin:18px 0 10px}
.maphead{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:0 0 6px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* full screen: the map block takes the screen; the wrapper's height is set by script to what is left under the bar */
#mapbody:fullscreen,#mapbody:-webkit-full-screen,#mapbody.fsfake{background:var(--bg);overflow:auto;padding:8px 12px 12px;box-sizing:border-box}
#map,#mapbody{overflow-anchor:none}
#mapbody.fsfake{position:fixed;inset:0;z-index:80;width:100vw;height:100vh;height:100dvh}
#mapbody.fs .mapgrid{border-radius:0 0 10px 10px}
.zoomctl .zfs i{display:inline-flex;align-items:center;gap:4px;font-style:normal}
.zoomctl .zfs[aria-pressed="true"]{background:var(--surface2)}
.mapsec h2{font-size:24px;font-weight:600;margin:0 0 4px;display:flex;gap:14px;align-items:baseline}
.mapsec h2 .num{font-family:"Unbounded",sans-serif;font-weight:500;font-size:15px;color:var(--muted)}
.mapbar{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:10px 12px;border:1px solid var(--rule);border-radius:10px 10px 0 0;background:var(--surface);font-size:13.5px}
.mapbar .grp{display:flex;flex-wrap:wrap;gap:6px;align-items:center;min-width:0;max-width:100%}
.mapbar .lbl{color:var(--muted);font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-right:2px}
.chip{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);font:inherit;font-size:13px;padding:4px 10px 4px 8px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;line-height:1.2}
.chip .sw{width:10px;height:10px;border-radius:2px;background:var(--c);display:inline-block}
.chip[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.chip.off{opacity:.45}
.chip.tog[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
/* global reset: an action, not a toggle — so not a pill: square corners, dashed outline, icon, muted until hovered */
.resetbtn{appearance:none;border:1px dashed var(--muted);background:transparent;color:var(--ink2);font:inherit;font-size:12.5px;padding:4px 9px 4px 7px;border-radius:5px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;line-height:1.2}
.resetbtn:hover,.resetbtn:focus-visible{border-style:solid;border-color:var(--accent);color:var(--accent);outline:none}
.resetbtn:active{background:var(--surface2)}
select.sel{font:inherit;font-size:13px;padding:4px 8px;border:1px solid var(--rule);border-radius:6px;background:var(--surface);color:var(--ink);max-width:100%}
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
.mapcol{margin-left:auto;font-size:12px;font-weight:500;align-self:center;flex:0 0 auto;white-space:nowrap}
#mapbody[hidden]{display:none}
.insp h3 .sw{width:11px;height:11px;border-radius:3px;background:var(--c);display:inline-block;margin-right:4px}
.ptab{border-collapse:collapse;width:100%;font-size:12.5px}
.ptab td{padding:3px 6px 3px 0;vertical-align:top;border-top:1px solid var(--rule2,var(--rule))}
.ptab td.ln{white-space:nowrap;color:var(--muted);font-family:"JetBrains Mono",monospace;font-size:10.5px;padding-right:10px}
.ptab a.prim{font-weight:600}
.ptab a.alt{color:var(--ink2)}
/* machines on the Map (C2): a station the selected machine uses only as an alternate keeps a dashed outline while lit */
.station.altuse rect.box{stroke-dasharray:4 3}
#machine{width:300px;max-width:100%;min-width:0}
.insp .mlinks{margin:-4px 0 8px;font-size:12.5px;display:flex;flex-wrap:wrap;gap:2px 6px}
.insp .mtab td{min-width:0}
.insp .mtab td.ln{white-space:normal;width:30%;max-width:104px;line-height:1.25}
.insp .mtab .mc{margin:1px 0;overflow-wrap:anywhere}
.insp .mtab .ms{font-size:11.5px;color:var(--ink2);line-height:1.3;margin:1px 0 3px}
.insp .ev{text-decoration:none;font-size:13px}
.insp .loc{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--muted);overflow-wrap:anywhere}
.insp .vf{font-size:11px}
.insp .mfoot{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;justify-content:space-between;margin:8px 0 0;font-size:12.5px;color:var(--ink2)}
.insp ul.useby{list-style:none;margin:0;padding:0}
.insp ul.useby li{display:flex;flex-wrap:wrap;gap:2px 6px;align-items:baseline;padding:2px 0;border-top:1px dashed var(--rule);font-size:12.5px;min-width:0;overflow-wrap:anywhere}
.insp ul.useby li.fam{border-top:0;margin-top:5px;font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.insp ul.useby li.fam .sw{width:10px;height:3px;border-radius:2px;background:var(--c);display:inline-block}
.insp ul.useby li.cur > a:first-child{font-weight:700;text-decoration:underline}
.insp ul.useby li.alternate > a:first-child{color:var(--ink2)}
.insp ul.useby a.mref{font-size:11px;color:var(--muted);text-decoration:none;border:1px solid var(--rule);border-radius:9px;padding:0 6px;margin-left:2px;white-space:nowrap}
.insp ul.useby a.mref:hover{color:var(--accent);border-color:var(--accent)}
.insp ul.useby a.reg{text-decoration:none;font-size:11px}
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
.pathline.dim{opacity:.05}
.iso .pathline.dim{opacity:0}
.lensed .pathline.dim{opacity:.05}
.iso.lensed .pathline.dim{opacity:0}
.pathline.neutral{stroke-dasharray:7 5}
.phit{fill:none;stroke:transparent;stroke-width:14;pointer-events:stroke;cursor:pointer} .phit.dim{pointer-events:none}
.pathline.hov{stroke-width:5.5;opacity:1}
.altstub{fill:none;stroke-width:1.2;stroke-dasharray:2 3;opacity:.7}
.altstub.dim{opacity:.05}
.iso .altstub.dim{opacity:0}
.lensed .altstub.dim{opacity:.05}
.edge{fill:none;stroke-width:1.6}
.edge path.hit{stroke:transparent;stroke-width:14;stroke-dasharray:none;pointer-events:stroke;cursor:pointer}
.edge:hover path.vis{stroke-width:3}
.tip.wide{max-width:440px}
.edge.requires{stroke:var(--ink);opacity:.9}
.edge.replaces{stroke:var(--ink2);stroke-dasharray:5 4}
.edge.conflicts{stroke:var(--crit);stroke-dasharray:3 3;stroke-width:2}
.rel{padding-left:14px;text-indent:-14px;line-height:1.35}
.badge{stroke:none}
.hatch{fill:url(#hatch)}
.tip{position:absolute;pointer-events:none;background:var(--ink);color:var(--bg);font-size:12px;padding:6px 9px;border-radius:6px;width:max-content;max-width:280px;line-height:1.35;box-shadow:var(--shadow);z-index:5;display:none}

/* lens */
.lensed .pathline{stroke:var(--mid) !important;opacity:.28} .lensed .pathline.hov{opacity:.9}
.lensed .altstub{stroke:var(--mid) !important;opacity:.35}
.lensed .badge{opacity:.35}
.lk{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);font:inherit;font-size:12.5px;padding:2px 9px 2px 24px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;position:relative;overflow:hidden}
.lk .sw{position:absolute;left:0;top:0;bottom:0;width:17px;border-radius:0 !important;border:0 !important;border-right:1px solid rgba(0,0,0,.12) !important;display:block}
.lk.clear{padding-left:9px}
.lk .cnt{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--muted)}
.lk[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink);font-weight:600}
.lk:hover{background:var(--surface2)}
.lk.clear{border-style:dashed}
.mapbar .lenslegend{flex-basis:100%;gap:6px 8px;align-items:center;padding-top:6px;border-top:1px dashed var(--rule)}
.mapbar .lenslegend:empty{display:none}
.mapbar .lenslegend .lbl{margin-right:6px}
.lg.stn{width:50px;height:16px}   /* two miniature stations: as drawn (outline = family), then with a lens on (tint + left band) */
.lg.stn svg{display:block}
.lg.badges{width:18px;height:12px;display:inline-flex;gap:2px;align-items:flex-end}
.lg.badges b{display:inline-block;width:7px;height:4px;border-radius:1px;background:var(--sc)}
.lg.badges b+b{background:none;border:1px solid var(--atom)}
.insp dl .lensrow{background:var(--surface);box-shadow:inset 3px 0 0 var(--accent);padding-left:6px}
.mast .author{margin:2px 0 10px;font-size:15px;color:var(--ink2)}
.mast .author b{color:var(--ink);font-weight:600}
.mast .title .yr{color:var(--muted);font-weight:500}
.pubmeta{margin-top:12px;font-size:12.5px;color:var(--muted);text-align:right;line-height:1.6}
.pubmeta a{color:var(--ink2)}
.colophon{margin:48px 0 0;padding:20px 0 0;border-top:1px solid var(--rule);font-size:13.5px;color:var(--ink2);max-width:90ch}
.colophon p{margin:.6em 0;text-wrap:pretty}
.colophon b{color:var(--ink)}
/* inspector */
.insp{position:fixed;top:84px;left:16px;width:336px;max-height:calc(100vh - 100px);max-height:calc(100dvh - 100px);border:1px solid var(--rule);border-radius:12px;padding:0 16px 14px;overflow:auto;font-size:13.5px;background:var(--surface);box-shadow:0 12px 36px rgba(0,0,0,.16);z-index:40;resize:both;min-width:280px;min-height:200px}
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
.mapbar .glyphs{flex-basis:100%;color:var(--ink2);font-size:12.5px}
.mapbar details.glyphs>summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:6px;padding:3px 0}
.mapbar details.glyphs>summary::-webkit-details-marker{display:none}
.mapbar details.glyphs>summary::after{content:"▾";color:var(--muted);font-size:11px}
.mapbar details.glyphs:not([open])>summary::after{content:"▸"}
.glyphlist{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
.gl{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.gl.long{white-space:normal;max-width:100%} .gl.long .lg{flex:0 0 auto}
.gl.mark{cursor:help} .gl.mark .cnt{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--muted)}   /* static keys with counts (brief E): the definition is the title */
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
.insp .marks{margin:4px 0 2px} .insp .marks>div{margin:2px 0;font-size:12.5px} .insp .marks .tk{display:block;margin-bottom:2px}
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
/* ================================================================
   RESPONSIVE / CROSS-BROWSER PASS
   Breakpoints: phone ≤600 · tablet 601–1024 · desktop >1024 · wide ≥1600.
   Every block below is labelled with the breakpoint it serves.
   ================================================================ */

/* [all widths] fluid base size; the desktop value (16px) is reached at ~857px and above */
body{font-size:clamp(14px,0.35vw + 13px,16px)}
/* [all widths] measure never exceeds the column (min() keeps the desktop 78ch measure) */
.prose p,.prose ul,.prose ol,.prose blockquote,.prose dl{max-width:min(78ch,100%)}
.bone,.bverdict,.blede,.bbody p,.bbody ul,.bbody ol{max-width:min(78ch,100%)}
/* [all widths] long URLs / identifiers wrap instead of pushing the page wide */
.prose a,.bbody a,.colophon a,.pubmeta a,.bidx a,.insp a{word-break:break-word;overflow-wrap:anywhere}
.prose td>a.src,.prose td>a.cite,.prose td>a.xref{word-break:normal;overflow-wrap:normal;white-space:nowrap}   /* a code such as F1a in a narrow first column never breaks inside (Table 8.5, 23 Sep 2026) */
h1.title,.prose h2,.prose h3,.mapsec h2,.briefs h2,.btitle,.bbody h3.bh3,.insp h3{overflow-wrap:break-word}
/* [all widths] nothing in the grid may establish a min-content floor wider than the viewport */
main,.prose,.brief,.mapgrid,.mapbar,.bbody{min-width:0}
/* [all widths] a nowrap math run longer than ~50 characters must be allowed to wrap */
.prose .m.long,.bbody .m.long,.m.long{white-space:normal;overflow-wrap:break-word}
/* [all widths] wide boxes scroll inside themselves, with momentum, without chaining to the page */
.tbl,.bbody .tbl,.bidx .tbl,details.fold .tbl{-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}
.mapwrap{-webkit-overflow-scrolling:touch;overscroll-behavior:contain;touch-action:pan-x pan-y pinch-zoom}
.insp{-webkit-overflow-scrolling:touch;overscroll-behavior:contain}
/* [all widths] vh first, dvh second — browsers without dvh keep the vh line */
.mapwrap{max-height:82vh}
.mapwrap{max-height:82dvh}
/* [all widths] map-bar zoom control */
/* [all widths] page chrome that only exists below 1025px */
.mobilebar{display:none}
.tocdrawer,.tocbackdrop{display:none}

/* [desktop >1024] the glyph legend is always open and needs no summary (unchanged look) */
@media (min-width:1025px){
  .mapbar details.glyphs>summary{display:none}
  .tocdrawer,.tocbackdrop,.mobilebar{display:none !important}
}
/* [desktop 1025–1100] narrow desktops: the floating card hugs the left edge (as before) */
@media (min-width:1025px) and (max-width:1100px){.insp{width:min(336px,92%);left:8px;top:64px}}

/* ---------------- [tablet + phone ≤1024] ---------------- */
@media (max-width:1024px){
  /* single-column page; the sidebar TOC is replaced by the sticky bar + drawer below */
  .page{grid-template-columns:minmax(0,1fr);gap:0}
  nav.toc{position:static;max-height:none;display:none}
  .mapfull{margin-left:0}
  /* masthead: one column, right-aligned meta becomes left-aligned, nothing overflows */
  .mast{grid-template-columns:minmax(0,1fr);gap:10px;padding:18px 0 16px}
  .controls{flex-direction:row;flex-wrap:wrap;align-items:center;gap:10px 14px}
  .controls .seg,.controls .jump{display:none}
  .pubmeta{text-align:left;margin-top:6px}
  .eyebrow{white-space:normal}
  /* sticky navigation bar */
  .mobilebar{display:flex;position:sticky;top:0;z-index:55;align-items:center;gap:8px;
    margin:0 -20px;padding:6px 14px;background:var(--surface);border-bottom:1px solid var(--rule)}
  .mobilebar .mb-btn{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);
    font:inherit;font-size:13.5px;font-weight:500;line-height:1.2;padding:8px 12px;border-radius:999px;
    cursor:pointer;text-decoration:none;white-space:nowrap}
  .mobilebar .mb-sp{flex:1}
  .mobilebar .seg button{padding:7px 10px;font-size:13px}
  /* TOC drawer */
  .tocbackdrop{display:block;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(10,16,22,.45);z-index:70}
  .tocdrawer{display:flex;flex-direction:column;position:fixed;top:0;left:0;bottom:0;
    width:86vw;max-width:340px;z-index:71;background:var(--surface);border-right:1px solid var(--rule);
    box-shadow:0 0 40px rgba(0,0,0,.28)}
  .tocdrawer .td-head{display:flex;align-items:center;justify-content:space-between;gap:10px;
    padding:12px 14px;border-bottom:1px solid var(--rule);font-weight:600;flex:0 0 auto}
  .tocdrawer .td-close{appearance:none;border:1px solid var(--rule);background:var(--surface);color:var(--ink);
    font:inherit;font-size:15px;line-height:1;padding:7px 11px;border-radius:8px;cursor:pointer}
  .tocdrawer .td-body{flex:1 1 auto;overflow:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;
    padding:8px 14px 32px;font-size:14px}
  .tocdrawer .td-body ol{list-style:none;margin:0;padding:0}
  .tocdrawer .td-body li{margin:0;padding:0}
  .tocdrawer .td-body a{color:var(--ink2);text-decoration:none;display:flex;gap:10px;padding:9px 4px;border-radius:6px}
  .tocdrawer .td-body a .n{font-family:"JetBrains Mono",monospace;color:var(--muted);min-width:1.8em}
  .tocdrawer .td-body .mapl a{color:var(--accent);font-weight:600}
  body.drawer-open{overflow:hidden}
  /* the sticky bar covers anchor targets unless they reserve room for it */
  :target,#map,#mapbody,#mapbar,#mapwrap,.brief,.briefs,.mapsec,.prose h2,.prose h3{scroll-margin-top:60px}
  /* map: shorter canvas so the bar, the map and the page all fit */
  .mapwrap{max-height:70vh}
  .mapwrap{max-height:70dvh}
  /* map bar: the 14 path chips become one horizontally scrollable row with a fade affordance */
  .mapbar{gap:8px 10px;padding:8px 10px}
  .mapbar .chipsrow{position:relative;flex-basis:100%;flex-wrap:nowrap;align-items:center;min-width:0;gap:6px}
  .mapbar .chipsrow #pathchips{flex:1 1 auto;flex-wrap:nowrap;overflow-x:auto;min-width:0;
    -webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;scrollbar-width:thin;padding:2px 24px 6px 0}
  .mapbar .chipsrow #pathchips .chip{flex:0 0 auto}
  .mapbar .chipsrow::after{content:"";position:absolute;right:0;top:0;bottom:6px;width:26px;pointer-events:none;
    background:linear-gradient(to left,var(--surface),var(--surface-t0))}
  /* the lens legend and the glyph legend wrap; the glyph legend collapses */
  .mapbar .lenslegend{gap:6px 8px}
  /* the wide edge tip must never be wider than the phone */
  .tip,.tip.wide{max-width:min(320px,86vw)}
  .gl{white-space:normal}
  .chip,.legend .lk{min-height:30px}
  /* the inspector's bottom-sheet rules live in their own query below (narrow, or touch up to 1024px) */
  /* long inline formulas must be allowed to break rather than widen the page */
  .prose .m,.bbody .m{white-space:normal}
  /* briefs */
  .brief{padding:14px 14px 10px}
  .bnav{gap:6px}
}
@media (max-width:700px), ((max-width:1024px) and (pointer:coarse)){
  /* inspector becomes a bottom sheet (JS ignores the stored desktop position in sheet mode: narrow viewports, or touch screens up to 1024px — a mouse laptop keeps the floating card) */
  .insp{position:fixed;left:0;right:0;bottom:0;top:auto;width:auto;max-width:none;
    max-height:62vh;border-radius:14px 14px 0 0;border-left:0;border-right:0;border-bottom:0;
    resize:none;min-width:0;min-height:0;padding:0 14px 18px;z-index:60;
    box-shadow:0 -10px 34px rgba(0,0,0,.24)}
  .insp{max-height:62dvh}
  /* the sheet must not bury the map: it opens at under half the screen and the page gets room to scroll the map above it */
  .insp{max-height:46vh;max-height:46dvh}
  body.has-sheet{padding-bottom:48vh;padding-bottom:48dvh}
  html{scroll-padding-top:60px}
  .insp.sheet-max{max-height:90vh}
  .insp.sheet-max{max-height:90dvh}
  .insp .grip{margin:0 -14px 8px;padding:8px 12px}
  .insp .grip [data-dock]{display:none}
  .insp .grip button{padding:4px 10px;font-size:12px}
  .insp .grip{cursor:ns-resize;touch-action:none}
  .insp.sheet-max .grip{cursor:default}
}

/* ---------------- [phone ≤600] ---------------- */
@media (max-width:600px){
  #app{padding:0 12px 60px}
  .mobilebar{margin:0 -12px;padding:6px 10px}
  .mast{padding:14px 0 14px}
  .prose h2,.mapsec h2,.briefs h2{font-size:20px;gap:10px;flex-wrap:wrap}
  .prose h3{font-size:16.5px}
  .thesis{padding:12px 14px;font-size:14.5px}
  .subtitle{font-size:15.5px}
  /* tables: 13px on phones, first column pinned so the row is identifiable while scrolling */
  table{font-size:13px}
  .big-table table,.bbody table,.bidx table{font-size:12px}
  th,td{padding:6px 8px}
  th{white-space:normal}
  .prose .tbl table th{z-index:2}
  .prose .tbl table td:first-child,.prose .tbl table th:first-child{position:sticky;left:0}
  .prose .tbl table td:first-child{background:var(--surface);z-index:1}
  .prose .tbl table th:first-child{background:var(--surface2);z-index:3}
  .bidx td.ol{display:none}
  .bidx th:last-child{display:none}
  .radars{grid-template-columns:repeat(auto-fit,minmax(130px,1fr))}
  .insp{font-size:13px}
  .colophon{font-size:13px}
}

/* [touch] no hover: tap targets grow, hover-only affordances stay reachable */
@media (hover:none),(pointer:coarse){
  .chip,.legend .lk,.seg button,.mobilebar .mb-btn{min-height:32px}
  .edge path.hit{stroke-width:22}
  .tip,.tip.wide{max-width:min(320px,86vw)}
}

@media (prefers-reduced-motion:no-preference){.station rect.box,.pathline,.altstub,.pcline{transition:opacity .25s ease}}
@media print{.mapbar,.controls,.mobilebar,.tocdrawer,.tocbackdrop{display:none}.mapwrap{max-height:none;overflow:visible}#app{max-width:none}}

/* map zoom — a translucent window in the top-right corner of the map bar (desktop); the paths row keeps a margin
   clear of it. On ≤1024 px the same control moves into the scroller and pins to its bottom-right corner. */
.zoomwin{margin-left:auto;align-self:center}
#pathchips .zoomwin{margin-left:auto}
@media (min-width:1025px){
  .mapbar .chipsrow{display:block;flex:1 1 100%;line-height:1.2}
  .mapbar .chipsrow > .zoomwin{float:right;margin:0 0 6px 10px}
  .mapbar .chipsrow > .bartog{margin:0 8px 6px 0;vertical-align:middle}
  .mapbar .chipsrow > .lbl{display:inline-block;margin:0 6px 6px 0;vertical-align:middle}
  .mapbar .chipsrow > .barsum{display:inline-block;max-width:60%;vertical-align:middle;margin-bottom:6px}
  .mapbar .chipsrow #pathchips{display:inline}
  .mapbar .chipsrow #pathchips .chip{margin:0 6px 6px 0;vertical-align:middle}
  .mapbar.collapsed .chipsrow{display:block}
}
.zoomctl{display:inline-flex;align-items:center;gap:2px;padding:3px;border:1px solid var(--rule);border-radius:9px;background:var(--surface-t85);box-shadow:var(--shadow)}
@supports (backdrop-filter:blur(6px)) or (-webkit-backdrop-filter:blur(6px)){.zoomctl{-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}}
.zoomctl .zb{display:inline-flex;align-items:center;justify-content:center;gap:4px;height:26px;min-width:26px;padding:0 6px;border:0;border-radius:6px;background:transparent;color:var(--ink);font:600 12px/1 "JetBrains Mono",monospace;cursor:pointer}
.zoomctl .zb:hover{background:var(--surface2)}
.zoomctl .zb:active{transform:translateY(1px)}
.zoomctl .zb:focus-visible,.zoomctl .zlvl:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.zoomctl .zt{font-weight:500;font-size:11.5px;letter-spacing:.02em}
.zoomctl .zt span{display:none}
.zoomctl .zhint{display:none}
.zoomctl .zlvl{width:4.6em;height:24px;padding:0 4px;border:1px solid var(--rule);border-radius:6px;background:var(--surface);color:var(--ink);font:500 11.5px/1 "JetBrains Mono",monospace;text-align:center;font-variant-numeric:tabular-nums;-moz-appearance:textfield}
.zoomctl .zlvl::-webkit-outer-spin-button,.zoomctl .zlvl::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
.zoomctl .zlvl:focus{border-color:var(--accent);outline:none}
.zoomctl .zsep{width:1px;height:16px;background:var(--rule);margin:0 3px}
.zoomctl .zhint{font-size:10.5px;color:var(--muted);margin:0 6px 0 4px;letter-spacing:.04em;text-transform:uppercase}
.zoombar{position:sticky;bottom:0;left:0;height:0;overflow:visible;z-index:4;pointer-events:none}
.zoombar .zoomctl{position:absolute;right:6px;bottom:8px;pointer-events:auto}
@media (max-width:600px){.zoomctl{padding:2px}.zoomctl .zb{height:30px;min-width:30px}.zoomctl .zt span{display:none}.zoomctl .zt{padding:0 5px}.zoomctl .zhint{display:none}}
.mapwrap.tall{max-height:none}
/* beta stamp (editions.py STATUS='beta'): visible but quiet */
.beta{display:inline-block;padding:0 6px;border-radius:999px;border:1px solid var(--accent);color:var(--accent);font:600 10.5px/16px "JetBrains Mono",monospace;letter-spacing:.06em;text-transform:uppercase;vertical-align:1px}
.pubmeta .doi{font-family:"JetBrains Mono",monospace;color:var(--muted);border-bottom:1px dotted var(--line);cursor:help}

/* collapsible map bar: one line (toggle · summary · zoom) when collapsed */
.bartog{appearance:none;display:inline-flex;align-items:center;gap:6px;border:1px solid var(--ink2);background:var(--surface2);color:var(--ink);border-radius:8px;height:30px;padding:0 10px 0 9px;cursor:pointer;font:600 13px/1 "Inter",system-ui,sans-serif;margin-right:4px;flex:0 0 auto}
.bartog:hover{background:var(--surface);border-color:var(--accent);color:var(--accent)}
.bartog .when-open,.bartog .when-closed{font-size:11px;color:var(--muted)}
.bartog:hover .when-open,.bartog:hover .when-closed{color:inherit}
.mapbar.collapsed .chipsrow > .lbl{display:none}
.maplead{margin:10px 0 2px}
.maplead .lead{color:var(--ink2);max-width:100ch;margin:6px 0 0;font-size:14.5px;line-height:1.55;text-wrap:pretty}
.maplead details>summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--ink2);padding:2px 0}
.maplead details>summary::-webkit-details-marker{display:none}
.maplead details>summary::after{content:"▸";color:var(--muted);font-size:11px}
.maplead details[open]>summary::after{content:"▾"}
.maplead details>summary:hover{color:var(--accent)}
#mapbody:fullscreen .maplead,#mapbody:-webkit-full-screen .maplead,#mapbody.fsfake .maplead{display:none}
.barsum{color:var(--ink2);font-size:12.5px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.barsum b{color:var(--ink);font-weight:600}
.barsum .sw{display:inline-block;width:9px;height:9px;border-radius:2px;vertical-align:-1px;margin-right:4px}
.mapbar.collapsed > .grp:not(.chipsrow),.mapbar.collapsed > details,.mapbar.collapsed > #lenslegend{display:none}
.mapbar.collapsed .chipsrow #pathchips .chip{display:none}
.mapbar.collapsed .chipsrow{flex:1 1 100%;flex-wrap:nowrap;align-items:center}
.mapbar.collapsed .chipsrow #pathchips{flex:1 1 auto;justify-content:flex-end}
.mapbar.collapsed .chipsrow::after{display:none}
/* zoom bar for the big tables (editor's review of 17 Sep 2026, item 3): the bar sits inside the wrapper above the table and
   stays in view while the wrapper scrolls sideways; the sizer's box follows the scaled table; the sticky header / first
   column are switched off while the table is scaled (.zoomed) — sticky offsets are computed in unscaled units */
.tblzoom{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:5px 8px;border-bottom:1px solid var(--rule);background:var(--surface2);position:sticky;left:0;z-index:4;box-sizing:border-box;max-width:100%}
.tblzoom .zoomctl{flex-wrap:wrap;box-shadow:none;background:var(--surface);max-width:100%}
.tblzoom .zoomctl .zt span{display:inline}
.tblzoom .zoomctl .zt .tzi{font-size:13px;margin-right:2px}
.tblzoom .tzl{font:500 10.5px/1 "JetBrains Mono",monospace;color:var(--muted);margin:0 6px 0 4px;letter-spacing:.04em;text-transform:uppercase}
.tblsizer{overflow:clip}
.tblsizer>table{transform-origin:0 0}
.tbl.zoomed table th,.tbl.zoomed table td:first-child,.tbl.zoomed table th:first-child,.prose .tbl.zoomed table th,.prose .tbl.zoomed table td:first-child,.prose .tbl.zoomed table th:first-child{position:static}
/* sortable tables (editor's review of 17 Sep 2026, second batch, brief D): the header button looks like the header text; the
   indicator is muted; the ↺ button sits in the zoom bar when there is one, else in a minimal bar styled like it */
.sortbtn{appearance:none;background:none;border:0;padding:0;margin:0;font:inherit;color:inherit;text-align:inherit;letter-spacing:inherit;text-transform:inherit;white-space:inherit;cursor:pointer;border-radius:3px}
.sortbtn:hover{color:var(--accent)}
.sortbtn:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.sortbtn .sortind{color:var(--muted);font-size:.8em;font-weight:500}
th[aria-sort="ascending"] .sortbtn,th[aria-sort="descending"] .sortbtn{color:var(--accent)}
.tblbar{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:5px 8px;border-bottom:1px solid var(--rule);background:var(--surface2);position:sticky;left:0;z-index:4;box-sizing:border-box;max-width:100%}
.tsreset{display:inline-flex;align-items:center;gap:4px;height:26px;padding:0 8px;border:1px solid var(--rule);border-radius:6px;background:var(--surface);color:var(--ink);font:500 11.5px/1 "JetBrains Mono",monospace;letter-spacing:.02em;cursor:pointer;white-space:nowrap;max-width:100%}
.tsreset .tsi{font-size:13px}
.tsreset:hover{background:var(--surface2)}
.tsreset:active{transform:translateY(1px)}
.tsreset:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.tsreset.idle{color:var(--muted)}
.tblzoom .tsreset{margin-left:2px}
/* §8 figure (build/fig81.py): inline SVG that follows the page's ink and surface tokens */
figure.fig81{margin:1em 0 1.2em;padding:0}
figure.fig81 figcaption{font-size:13px;color:var(--ink2);margin-top:6px;text-align:left}
figure.fig81 .pt:hover .mk{stroke-width:2.6}
"""
