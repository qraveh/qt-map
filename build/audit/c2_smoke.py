#!/usr/bin/env python3
"""C2 smoke — machines on the Map (sync Playwright API). Runs the same script at 1600×1000 and 400×800:
default 96 stations lit → select google-willow (lit = its non-gap nodes, only path `sc` lit) → requires on (edges only among lit)
→ click transmon (lit ⊆ machine ∪ {transmon}; station card has "Used by" with ≥ 10 machines) → reset (96 lit, select empty,
no altuse) → RU labels. Exit 0 iff every check passes and there are 0 console errors (Google Fonts ERR_TUNNEL ignored)."""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / 'dist' / 'Quantum-Technology-Map-2026.09.html'
MACH = json.load(open(ROOT / 'data' / 'machines.json', encoding='utf-8'))
WILLOW = next(m for m in MACH['machines'] if m['id'] == 'google-willow')
WILLOW_NODES = {c['node'] for cells in WILLOW['layers'].values() for c in cells if not c['node'].startswith('∅')}
WILLOW_ALT = {c['node'] for cells in WILLOW['layers'].values() for c in cells if c['role'] == 'alternate' and not c['node'].startswith('∅')}
# lens select (brief E, 17 Sep): the editor's order with plain labels, no coordinate letters, no reading-marks lens
LENS_ORDER = ['family', 'g', 'f', 'd', 'mod', 'place', 'time', 'mech', 'destr', 'mid', 'det', 'aff', 'status']
LENS_EN = ['Platform family', 'Manufacturing technology', 'Dominant error structure', 'Mobility / connectivity', 'Control: modality',
           'Control: placement (temperature stage)', 'Characteristic time (gate or readout)', 'Readout: mechanism', 'Readout: destructive?',
           'Readout: mid-circuit?', 'Entangling: deterministic / heralded', 'Carrier affinity: natural ↔ fabricated', 'Technology status']
LENS_RU = ['Семейство платформ', 'Технология производства', 'Доминирующая структура ошибок', 'Подвижность / связность', 'Управление: модальность',
           'Управление: размещение (температурная ступень)', 'Характерное время (гейт или считывание)', 'Считывание: механизм', 'Считывание: разрушающее?',
           'Считывание: внутрисхемное?', 'Перепутывание: детерминированное / heralded', 'Сродство носителя: естественный ↔ изготовленный', 'Статус технологии']

READ = """()=>({
  lit:[...document.querySelectorAll('#mapwrap g.station:not(.dim)')].map(g=>g.querySelector('text.id').textContent),
  altuse:[...document.querySelectorAll('#mapwrap g.station.altuse')].map(g=>g.querySelector('text.id').textContent),
  lines:[...document.querySelectorAll('#mapwrap path.pathline:not(.dim)')].map(p=>p.dataset.path),
  edges:[...document.querySelectorAll('#mapwrap g.edge')].map(g=>{const e=d3.select(g).datum(); return [e.src,e.dst,e.type];}),
  machine:document.getElementById('machine').value,
  card:document.getElementById('insp').hidden?'':document.getElementById('insp').innerText,
  usedby:document.querySelectorAll('#insp ul.useby li:not(.fam)').length,
  hscroll:document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
  inspOver:(()=>{const i=document.getElementById('insp'); if(i.hidden)return false; return i.scrollWidth>i.clientWidth+2;})()
})"""


def run(pw, w, h):
    fails, errors = [], []
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={'width': w, 'height': h})
    p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text))
    p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0 && document.querySelectorAll('#machine option').length>1", timeout=60000)
    if p.locator('#mapbody').evaluate('e=>e.hidden'):
        p.locator('[data-mapcollapse]').first.click()

    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)

    def read(): return p.evaluate(READ)

    def click_station(nid):
        loc = p.locator('#mapwrap g.station').filter(has=p.locator(f'xpath=./*[local-name()="text" and contains(concat(" ",@class," ")," id ") and text()="{nid}"]'))
        try:
            loc.scroll_into_view_if_needed(timeout=3000); loc.locator('rect.box').click(timeout=3000)
        except Exception:
            loc.dispatch_event('click')   # covered by the bottom sheet (≤ 1024 px): fire the click on the station itself
        p.wait_for_function("id=>[...document.querySelectorAll('#mapwrap g.station.sel')].some(g=>g.querySelector('text.id').textContent===id)", arg=nid)

    print(f'viewport {w}×{h}')
    r = read()
    check('default: 96 stations lit, 14 lines, no edges, no machine', len(r['lit']) == 96 and len(r['lines']) == 14 and not r['edges'] and r['machine'] == '', (len(r['lit']), len(r['lines'])))
    opt = p.evaluate("()=>[...document.querySelectorAll('#machine optgroup')].map(o=>[o.label,o.children.length])")
    check('selector: optgroups in family order with 136 machines', [o[0] for o in opt] == ['superconducting circuits', 'trapped ions', 'neutral atoms', 'photonics', 'semiconductor spins', 'defect spins', 'topological', 'quantum annealers'] and sum(o[1] for o in opt) == 136, opt)

    p.select_option('#machine', 'google-willow')
    r = read()
    check('willow: lit stations == its non-gap nodes', set(r['lit']) == WILLOW_NODES, (sorted(set(r['lit']) ^ WILLOW_NODES)))
    check('willow: only path sc lit', set(r['lines']) == {'sc'}, r['lines'])
    check('willow: altuse == nodes used only as alternate', set(r['altuse']) == WILLOW_ALT, (r['altuse'], sorted(WILLOW_ALT)))
    check('willow: machine card shown (title, register link, evidence footer)', 'Willow' in r['card'] and 'register card' in r['card'] and '✅ 14 / 16' in r['card'], r['card'][:120])
    check('willow: card shows the Map gaps', 'Map gap: ∅G-lru' in r['card'], '')
    check('willow: no horizontal overflow', not r['hscroll'] and not r['inspOver'], (r['hscroll'], r['inspOver']))
    p.locator('#bartog').click()
    check('bar summary names the machine', 'machine: Willow' in p.locator('#barsum').inner_text())
    p.locator('#bartog').click()

    p.locator('#tg-req').click()
    r = read()
    check('requires on: edges drawn, all among lit stations', len(r['edges']) > 0 and all(e[0] in set(r['lit']) and e[1] in set(r['lit']) and e[2] == 'requires' for e in r['edges']), r['edges'][:5])

    click_station('transmon')
    r = read()
    check('transmon focused: lit ⊆ machine ∪ {transmon}', set(r['lit']) <= WILLOW_NODES | {'transmon'}, sorted(set(r['lit']) - WILLOW_NODES))
    check('transmon focused: station card wins, Used by ≥ 10 machines', 'used by' in r['card'].lower() and r['usedby'] >= 10, (r['usedby'], r['card'][:80]))
    check('transmon focused: Used-by names Willow, machine select unchanged', 'Willow' in r['card'] and r['machine'] == 'google-willow')
    check('transmon focused: edges still among lit stations', all(e[0] in set(r['lit']) and e[1] in set(r['lit']) for e in r['edges']))
    check('no horizontal overflow with the station card', not r['hscroll'] and not r['inspOver'], (r['hscroll'], r['inspOver']))

    p.locator('#tg-reset').click()
    r = read()
    check('reset: 96 lit, 14 lines, no edges, select empty, no altuse, card closed', len(r['lit']) == 96 and len(r['lines']) == 14 and not r['edges'] and r['machine'] == '' and not r['altuse'] and r['card'] == '', (len(r['lit']), r['machine'], r['altuse']))

    # brief E (17 Sep): lens labels, reading marks as badges, static glyph keys
    opts = p.evaluate("()=>[...document.querySelectorAll('#lens option')].map(o=>[o.value,o.textContent])")
    check('lens select: 13 options in the editor\'s order, plain EN labels', [o[0] for o in opts] == LENS_ORDER and [o[1] for o in opts] == LENS_EN, opts)
    click_station('code_surface'); r = read()
    check('code_surface card: hub badge with family count and names', 'reading marks' in r['card'].lower() and '◎ hub — required by stations of 2 families (' in r['card'], r['card'][:300])
    click_station('ct_sfq'); r = read()
    check('ct_sfq card: off-diagonal badge with the flag definition', '⤢ off-diagonal — fabricated carrier + control/decoding in the cold stage' in r['card'], r['card'][:300])
    p.keyboard.press('Escape')
    # brief F (17 Sep): place is a list — 4 K lights ct_cryocmos, ct_sfq, ro_spd; mK lights ct_sfq too; no 'vac' anywhere; the card joins the stages
    p.select_option('#lens', 'place'); p.wait_for_function("document.querySelectorAll('#lenslegend [data-lv]').length>0")
    lv = p.evaluate("()=>[...document.querySelectorAll('#lenslegend [data-lv]')].map(b=>[b.dataset.lv,b.querySelector('.cnt')?b.querySelector('.cnt').textContent:''])")
    check('place lens: values RT / 4K / mK / none with counts 45 / 3 / 9 / 41, no vac', lv == [['RT', '45'], ['4K', '3'], ['mK', '9'], ['none', '41']], lv)
    p.locator('#lenslegend [data-lv="4K"]').dispatch_event('click'); r = read()
    check('place = 4 K stage lights ct_cryocmos, ct_sfq and ro_spd', set(r['lit']) == {'ct_cryocmos', 'ct_sfq', 'ro_spd'}, sorted(r['lit']))
    p.locator('#lenslegend [data-lv="4K"]').dispatch_event('click')
    p.locator('#lenslegend [data-lv="mK"]').dispatch_event('click'); r = read()
    check('place = millikelvin stage lights ct_sfq (and ct_cryocmos), 9 stations', 'ct_sfq' in r['lit'] and 'ct_cryocmos' in r['lit'] and len(r['lit']) == 9, sorted(r['lit']))
    click_station('ct_sfq'); r = read()
    check('ct_sfq card: (e) control shows every stage — "microwave @ 4 K stage / millikelvin stage"', 'microwave @ 4 K stage / millikelvin stage' in r['card'], r['card'][:300])
    click_station('ct_cryocmos'); r = read()
    check('ct_cryocmos card: "microwave @ 4 K stage / millikelvin stage"', 'microwave @ 4 K stage / millikelvin stage' in r['card'], r['card'][:300])
    p.keyboard.press('Escape')
    p.select_option('#lens', 'family'); r = read()   # a lens change clears the value filter
    check('back to the family lens: 96 lit', len(r['lit']) == 96, len(r['lit']))
    novac = p.evaluate("()=>{const h=document.documentElement.outerHTML; return !document.querySelector('[data-lv=\"vac\"]') && h.indexOf('\"vac\"')<0 && h.indexOf(\"'vac'\")<0 && h.indexOf('@vac')<0 && h.indexOf('in-vacuum integrated')<0;}")
    check('no value "vac" anywhere in the DOM', novac)
    keys = p.evaluate("()=>[...document.querySelectorAll('#glyphlegend [data-glyph]')].map(e=>({k:e.dataset.glyph,n:e.querySelector('.cnt').textContent,title:e.title,role:e.getAttribute('role')}))")
    check('glyph legend: 3 static keys with counts and definitions, no button role', [k['k'] for k in keys] == ['hub', 'offd', 'empty'] and [k['n'] for k in keys] == ['24', '19', '5'] and all(k['title'] and k['role'] is None for k in keys), keys)
    p.locator('#glyphlegend [data-glyph="hub"]').dispatch_event('click'); r = read()
    check('glyph key click: no lens change, nothing dimmed', p.locator('#lens').evaluate('e=>e.value') == 'family' and len(r['lit']) == 96, (p.locator('#lens').evaluate('e=>e.value'), len(r['lit'])))

    p.locator('[data-setlang="ru"]').filter(visible=True).first.click()
    p.wait_for_function("document.getElementById('app').getAttribute('data-lang')==='ru'")
    vis = p.evaluate("()=>[...document.querySelectorAll('.machgrp .lbl')].filter(e=>getComputedStyle(e).display!=='none').map(e=>e.textContent)")
    og = p.evaluate("()=>[...document.querySelectorAll('#machine optgroup')].map(o=>o.label)")
    check('RU: machine label and optgroups in Russian', vis == ['машина'] and og[0] == 'сверхпроводниковые схемы', (vis, og[:2]))
    opts = p.evaluate("()=>[...document.querySelectorAll('#lens option')].map(o=>o.textContent)")
    check('RU: lens select labels', opts == LENS_RU, opts)
    p.select_option('#machine', 'google-willow')
    r = read()
    check('RU: machine card in Russian', 'карточка реестра' in r['card'] and 'источники: ✅ 14 / 16' in r['card'], r['card'][:100])
    p.locator('[data-setlang="en"]').filter(visible=True).first.click()

    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    ctx.close(); b.close()
    return fails


TZ = """()=>{
  const h3id=num=>{ const h=[...document.querySelectorAll('#app .lang-en h3')].find(x=>x.textContent.startsWith(num+' ')); return h?h.id:''; };   // h3 ids carry a running counter that shifts when a chapter is added — resolve by the printed number
  const fold=id=>{ let e=document.getElementById(id); while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return e; const w=e.querySelector&&e.querySelector('.tbl'); if(w)return w; } return null; };
  const st=w=>{ const t=w&&w.querySelector('table'); if(!t)return null; const m=/scale\\(([\\d.]+)\\)/.exec(t.style.transform||'');
    return {bar:!!w.querySelector('.tblzoom:not([hidden])'),z:m?parseFloat(m[1]):1,zoomed:w.classList.contains('zoomed'),big:t.offsetWidth>w.clientWidth+8,hscroll:w.scrollWidth>w.clientWidth+1,fits:w.scrollWidth<=w.clientWidth+1}; };
  const small=[...document.querySelectorAll('#app .prose.lang-en .tbl')].find(w=>!w.closest('details')&&w.clientWidth>0&&w.querySelector('table').scrollWidth<=w.clientWidth);
  return {node:st(fold(h3id('7.2'))),edge:st(fold(h3id('7.10'))),small:small?{bar:!!small.querySelector('.tblzoom:not([hidden])'),zoomed:small.classList.contains('zoomed')}:null,
    bars:document.querySelectorAll('.tbl .tblzoom:not([hidden])').length,
    vpover:document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
    barover:[...document.querySelectorAll('.tblzoom:not([hidden])')].some(b=>b.getBoundingClientRect().right>document.documentElement.clientWidth+1||b.scrollWidth>b.clientWidth+1)};
}"""


def tables(pw, w, h):
    """Zoom bar for the big tables (editor's review, item 3): §7.2 node table and §7.10 edge list get a bar and are scaled to
    fit, a small table gets none, 1:1 restores scale 1, 60 + Enter gives 0.6, nothing overflows the viewport, 0 console errors."""
    fails, errors = [], []
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={'width': w, 'height': h})
    p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text))
    p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)

    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)

    print(f'tables — viewport {w}×{h}')
    # open every EN fold (the big tables live in closed folds; the bar is measured when a fold opens)
    p.evaluate("()=>document.querySelectorAll('#app .lang-en details.fold').forEach(d=>{d.open=true;})")
    p.wait_for_function("()=>{const h=[...document.querySelectorAll('#app .lang-en h3')].find(x=>x.textContent.startsWith('7.2 ')); let e=h; while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return !!e.querySelector('.tblzoom:not([hidden])'); } return false;}", timeout=20000)
    p.wait_for_timeout(300)
    r = p.evaluate(TZ)
    check('§7.2 node table: bar present, scaled < 1, fits (no horizontal scroll)', r['node'] and r['node']['bar'] and r['node']['z'] < 1 and r['node']['zoomed'] and r['node']['fits'], r['node'])
    # the edge list has 3 columns and fits its wrapper at 1280 and at 400 px (headers wrap on phones): bar iff big, scaled to fit when big
    check('§7.10 edge list: bar iff wider than its wrapper; scaled to fit when big', r['edge'] and r['edge']['bar'] == r['edge']['big'] and (not r['edge']['big'] or (r['edge']['z'] < 1 and r['edge']['fits'])), r['edge'])
    check('a small table gets no bar', r['small'] is not None and not r['small']['bar'] and not r['small']['zoomed'], r['small'])
    print(f"  bars with every EN fold open: {r['bars']}")
    nid = p.evaluate("()=>{const h=[...document.querySelectorAll('#app .lang-en h3')].find(x=>x.textContent.startsWith('7.2 ')); return h?h.id:'';}")
    node = p.locator(f'#{nid} ~ details.fold div.tbl, #{nid} ~ div.tbl').first   # the §7.2 node table lives inside the fold (the same element TZ measures), not among the heading's siblings
    node.locator('[data-tz="one"]').click()
    p.wait_for_timeout(100)
    r1 = p.evaluate(TZ)
    check('1:1 restores scale 1 (sticky rules back on)', r1['node']['z'] == 1 and not r1['node']['zoomed'] and r1['node']['bar'], r1['node'])
    lvl = node.locator('.zlvl')
    lvl.click(); lvl.fill('60'); lvl.press('Enter')
    p.wait_for_timeout(100)
    r2 = p.evaluate(TZ)
    check('typing 60 + Enter gives scale 0.6', abs(r2['node']['z'] - 0.6) < 1e-9 and r2['node']['zoomed'] and lvl.evaluate('e=>e.value') == '60%', (r2['node'], lvl.evaluate('e=>e.value')))
    check('bars exist and nothing overflows the viewport', r2['bars'] >= 2 and not r2['vpover'] and not r2['barover'], (r2['bars'], r2['vpover'], r2['barover']))
    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    ctx.close(); b.close()
    return fails


TS = """(sel)=>{ const w=typeof sel==='string'?document.querySelector(sel):sel; if(!w)return null; const t=w.querySelector('table');
  const tx=e=>(e.textContent||'').replace(/\\s+/g,' ').trim();
  const head=[...t.tHead.rows[0].cells];
  return {cols:head.map(tx),sortable:head.map(h=>!!h.querySelector('.sortbtn')),aria:head.map(h=>h.getAttribute('aria-sort')),
    rows:[...t.tBodies[0].rows].map(r=>[...r.cells].map(tx)),ncells:[...t.tBodies[0].rows].map(r=>r.cells.length),
    reset:(()=>{const b=w.querySelector('.tsreset'); return b?{vis:b.offsetParent!==null,idle:b.classList.contains('idle'),inZoom:!!b.closest('.tblzoom')}:null;})(),
    barover:[...w.querySelectorAll('.tblbar:not([hidden]),.tblzoom:not([hidden])')].some(b=>b.scrollWidth>b.clientWidth+1||b.getBoundingClientRect().right>document.documentElement.clientWidth+1),
    vpover:document.documentElement.scrollWidth>document.documentElement.clientWidth+1}; }"""


def sorting(pw, w, h):
    """Sortable tables (editor's review, second batch, brief D): §3.1 Maturity index asc → desc, Platform restores; §7.4 a numeric
    header twice → descending, ↺ restores; §7.11 the ion T2 row has as many cells as the header, date asc, ↺ restores; the brief
    index sorts by centrality and restores in both languages; nothing overflows; 0 console errors."""
    fails, errors = [], []
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={'width': w, 'height': h})
    p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text))
    p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0 && document.querySelectorAll('div.tbl[data-sort] .sortbtn').length>0", timeout=60000)

    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)

    def num(s):
        import re
        m = re.search(r'[-−+]?\d[\d,]*(\.\d+)?([eE][-+]?\d+)?', s or '')
        return float(m.group(0).replace(',', '').replace('−', '-')) if m else None

    def click(loc):
        try:
            loc.scroll_into_view_if_needed(timeout=3000); loc.click(timeout=3000)
        except Exception:
            loc.dispatch_event('click')
        p.wait_for_timeout(60)

    def hdr(sel, name):   # the sort button whose header text is `name` (plus an optional ▲/▼ indicator)
        import re
        return p.locator(sel).first.locator('thead th .sortbtn').filter(has_text=re.compile('^' + re.escape(name) + r'\s*[▲▼]?$')).first

    def state(sel): return p.evaluate(TS, sel)

    print(f'sorting — viewport {w}×{h}')
    p.evaluate("()=>document.querySelectorAll('#app .lang-en details.fold').forEach(d=>{d.open=true;})")
    p.wait_for_timeout(300)
    EN = '#app .prose.lang-en '
    # §3.1 — Platform restores, the other columns sort; Maturity index twice → descending
    s31 = EN + 'div.tbl[data-sort="platform-default"]'
    o = state(s31)
    check('§3.1: tagged, Platform + 7 numeric headers sortable, build order first', o and o['sortable'] == [True] * 8 and o['rows'][0][0] == 'Superconducting' and o['reset']['idle'], o and (o['sortable'], o['rows'][0][:1]))
    click(hdr(s31, 'Maturity index')); a = state(s31)
    va = [num(r[-1]) for r in a['rows']]; nn = [v for v in va if v is not None]
    check('§3.1: one click → ascending by Maturity index, n/a last (aria-sort=ascending, ▲)', nn == sorted(nn) and va[:len(nn)] == nn and a['aria'][-1] == 'ascending' and '▲' in a['cols'][-1], (va, a['aria'][-1]))
    click(hdr(s31, 'Maturity index')); d = state(s31)
    vd = [num(r[-1]) for r in d['rows']]; nn = [v for v in vd if v is not None]
    check('§3.1: second click → descending (24 first, n/a last)', nn == sorted(nn, reverse=True) and vd[:len(nn)] == nn and nn[0] == 24 and d['aria'][-1] == 'descending' and not d['reset']['idle'], vd)
    click(hdr(s31, 'Platform')); r = state(s31)
    check('§3.1: Platform → build order restored, indicators cleared', r['rows'] == o['rows'] and all(x in (None, 'none') for x in r['aria']) and '▲' not in ''.join(r['cols']) and '▼' not in ''.join(r['cols']) and r['reset']['idle'], [x[0] for x in r['rows']])
    # §7.4 — numeric columns; a header twice → descending; ↺ → original
    s74 = EN + 'div.tbl[data-sort="numeric"]'
    o = state(s74)
    nsort = sum(o['sortable'])
    check('§7.4: numeric headers sortable (≥ 8 of 16), Path not sortable', nsort >= 8 and not o['sortable'][0], (nsort, o['sortable']))
    col = 'T₂'
    click(hdr(s74, col)); click(hdr(s74, col)); d = state(s74)
    i = next(k for k, c in enumerate(d['cols']) if c.startswith(col))
    vals = [num(r[i]) for r in d['rows']]; nn = [v for v in vals if v is not None]
    check('§7.4: T₂ twice → descending, nulls last', nn == sorted(nn, reverse=True) and vals[:len(nn)] == nn and d['aria'][i] == 'descending', vals)
    click(p.locator(s74).locator('.tsreset').first); r = state(s74)
    check('§7.4: ↺ restores the build order', r['rows'] == o['rows'] and all(x in (None, 'none') for x in r['aria']), [x[0] for x in r['rows']][:3])
    check('§7.4: ↺ sits in the zoom bar iff the table shows one', r['reset']['vis'] and (r['reset']['inZoom'] == bool(p.locator(s74).locator('.tblzoom:not([hidden])').count())), r['reset'])
    # §7.5 / §7.6 / §7.12 B — tagged, each with ≥ 1 numeric column
    for k, lab in ((1, '§7.5'), (2, '§7.6'), (3, '§7.12 B')):
        t = p.evaluate(TS, p.locator(s74).nth(k).element_handle())
        check(f'{lab}: ≥ 1 numeric column sortable, first column not', t and sum(t['sortable']) >= 1 and not t['sortable'][0], t and (t['cols'], t['sortable']))
        if lab == '§7.12 B': check('§7.12 B: T1, T2, 1Q, feed-forward, SPAM columns sortable (sparse columns count non-null cells)', all(t['sortable'][3:8]), t['sortable'])
    # §7.11 — the ion T2 record row is whole; date asc; ↺ restores
    s711 = EN + 'div.tbl[data-sort="date"]'
    o = state(s711)
    ion = next((r for r in o['rows'] if '4,235' in ' '.join(r)), None)
    check('§7.11: the ion T2 row has as many cells as the header (|0>,|1> no longer splits it)', ion is not None and len(ion) == len(o['cols']) and '|0>,|1>' in ion[2], ion and (len(ion), len(o['cols'])))
    check('§7.11: only the Date column is sortable', o['sortable'] == [False, False, False, False, True, False], o['sortable'])
    click(hdr(s711, 'Date')); a = state(s711)
    check('§7.11: date asc → first row date ≤ last, all rows kept', a['rows'][0][4] <= a['rows'][-1][4] and len(a['rows']) == len(o['rows']) and a['aria'][4] == 'ascending', (a['rows'][0][4], a['rows'][-1][4]))
    click(p.locator(s711).locator('.tsreset').first); r = state(s711)
    check('§7.11: ↺ restores the build order', r['rows'] == o['rows'], [x[0] for x in r['rows']][:3])
    # brief index — centrality asc/desc, ↺ restores, both languages
    for lang in ('en', 'ru'):
        if lang == 'ru':
            p.locator('[data-setlang="ru"]').filter(visible=True).first.click()
            p.wait_for_function("document.getElementById('app').getAttribute('data-lang')==='ru'")
        sb = f'#app .lang-{lang} div.tbl.bidx[data-sort="centrality"]'
        o = state(sb)
        cname = 'centrality' if lang == 'en' else 'центральность'
        check(f'brief index {lang}: 96 rows, only centrality sortable, grouped by layer at load', o and len(o['rows']) == 96 and o['sortable'] == [False, False, False, True, False] and o['rows'][0][0].startswith('1 '), o and (len(o['rows']), o['sortable']))
        click(hdr(sb, cname)); d = state(sb)
        vd = [num(r[3]) for r in d['rows']]
        check(f'brief index {lang}: centrality desc on the first click (data-sort-first)', vd == sorted(vd, reverse=True), vd[:5])
        click(hdr(sb, cname)); a = state(sb)
        va = [num(r[3]) for r in a['rows']]
        check(f'brief index {lang}: centrality asc on the second click', va == sorted(va), va[:5])
        click(p.locator(sb).locator('.tsreset').first); r = state(sb)
        check(f'brief index {lang}: ↺ restores the build order', r['rows'] == o['rows'], [x[1] for x in r['rows']][:4])
    over = p.evaluate("()=>({vp:document.documentElement.scrollWidth>document.documentElement.clientWidth+1, bars:[...document.querySelectorAll('.tblbar:not([hidden]),.tblzoom:not([hidden])')].filter(b=>b.offsetParent!==null&&(b.scrollWidth>b.clientWidth+1||b.getBoundingClientRect().right>document.documentElement.clientWidth+1)).length})")
    check('nothing overflows (viewport, bars)', not over['vp'] and over['bars'] == 0, over)
    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    ctx.close(); b.close()
    return fails


def chapter8(pw, w, h):
    """§8 Machines (17 Sep 2026): the chapter exists in both languages between §7 and the briefs, its six subsections are in the TOC,
    tables 8.1–8.3 are sortable (numeric) and restore, the verdict lines are present, Sources is §9; 0 console errors."""
    fails, errors = [], []
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={'width': w, 'height': h})
    p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text))
    p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0 && document.querySelectorAll('div.tbl[data-sort] .sortbtn').length>0", timeout=60000)
    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)
    print(f'chapter 8 — viewport {w}×{h}')
    r = p.evaluate("""()=>{
      const q=s=>[...document.querySelectorAll(s)];
      const h2=lang=>q('#app .prose.lang-'+lang+' h2').map(h=>h.textContent.trim());
      const h3=lang=>q('#app .prose.lang-'+lang+' h3').map(h=>h.textContent.trim()).filter(x=>/^8\.\d/.test(x));
      const toc=lang=>q('nav.toc .lang-'+lang+' li a .n').map(x=>x.textContent.trim()).filter(x=>/^8(\.\d)?$/.test(x));
      const en=h2('en'), ru=h2('ru');
      const idx=(arr,pre)=>arr.findIndex(x=>x.startsWith(pre));
      const tbls=q('#app .prose.lang-en h3').filter(h=>/^8\.[123] /.test(h.textContent)).map(h=>{ let e=h; while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return {sort:e.getAttribute('data-sort'),btns:e.querySelectorAll('.sortbtn').length,reset:!!e.querySelector('.tsreset')}; } return null; });
      const verdicts=q('#app .prose.lang-en p').filter(p=>/Verdict:/.test(p.textContent)).length;
      const ledger=q('#app .prose.lang-en h3').filter(h=>/^8\\.5 /.test(h.textContent)).map(h=>{ let e=h; while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return e.querySelectorAll('tbody tr').length; if(e.matches('h3'))break; } return 0; })[0]||0;
      const verdictsRu=q('#app .prose.lang-ru p').filter(p=>/Вердикт:/.test(p.textContent)).length;
      return {en8:idx(en,'8'), en9:idx(en,'9'), en7:idx(en,'7'), ru8:idx(ru,'8'), ru9:idx(ru,'9'), h3en:h3('en'), h3ru:h3('ru'), tocEn:toc('en'), tocRu:toc('ru'), tbls, verdicts, verdictsRu, ledger,
              srcEn:en[idx(en,'9')]||'', srcRu:ru[idx(ru,'9')]||'', macEn:en[idx(en,'8')]||''};
    }""")
    check('§8 follows §7 and precedes §9 (EN and RU)', r['en7'] >= 0 and r['en8'] == r['en7'] + 1 and r['en9'] == r['en8'] + 1 and r['ru8'] == r['en8'] and r['ru9'] == r['en9'], r)
    check('§8 is the machines chapter; §9 is Sources', r['macEn'].startswith('8Quantum machines') and r['srcEn'].startswith('9Sources') and r['srcRu'].startswith('9Источники'), (r['macEn'][:30], r['srcEn'][:20], r['srcRu'][:20]))
    SUBS = ['8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7']
    check('seven subsections 8.1–8.7 in both languages', [x[:3] for x in r['h3en']] == SUBS and [x[:3] for x in r['h3ru']] == SUBS, (r['h3en'], r['h3ru']))
    check('TOC lists §8 with 8.1–8.7 (EN and RU)', r['tocEn'] == ['8'] + SUBS and r['tocRu'] == r['tocEn'], (r['tocEn'], r['tocRu']))
    check('tables 8.1–8.3 tagged numeric, sortable columns present, ↺ present', len(r['tbls']) == 3 and all(x and x['sort'] == 'numeric' and x['btns'] >= 2 and x['reset'] for x in r['tbls']), r['tbls'])
    check('eight verdict lines in each language', r['verdicts'] == 8 and r['verdictsRu'] == 8, (r['verdicts'], r['verdictsRu']))
    check('forecast ledger (Table 8.5) has 8 rows', r['ledger'] == 8, r['ledger'])
    # sort table 8.1 by "Machines" twice → descending; ↺ restores
    t = p.evaluate("""()=>{ const h=[...document.querySelectorAll('#app .prose.lang-en h3')].find(x=>x.textContent.startsWith('8.1 ')); let e=h; while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl')) { e.id=e.id||'smoke-t81'; return e.id; } } return ''; }""")
    sb = '#' + t
    orig = p.evaluate("id=>[...document.querySelector(id).querySelectorAll('tbody tr')].map(r=>r.cells[0].textContent.trim())", sb)
    p.locator(sb).locator('.sortbtn', has_text='Machines').first.click(); p.wait_for_timeout(80)
    p.locator(sb).locator('.sortbtn', has_text='Machines').first.click(); p.wait_for_timeout(80)   # numeric tables sort ascending first; only data-sort-first="desc" tables (the brief index) start descending
    vals = p.evaluate("id=>[...document.querySelector(id).querySelectorAll('tbody tr')].map(r=>parseInt(r.cells[1].textContent.replace(/,/g,''),10))", sb)
    check('table 8.1: Machines column descending after two clicks', vals == sorted(vals, reverse=True), vals)
    p.locator(sb).locator('.tsreset').first.click(); p.wait_for_timeout(80)
    back = p.evaluate("id=>[...document.querySelector(id).querySelectorAll('tbody tr')].map(r=>r.cells[0].textContent.trim())", sb)
    check('table 8.1: ↺ restores the build order', back == orig, back[:4])
    disc = p.evaluate("()=>({en:!![...document.querySelectorAll('footer.colophon .lang-en p')].find(x=>x.textContent.startsWith('Disclosures.')), ru:!![...document.querySelectorAll('footer.colophon .lang-ru p')].find(x=>x.textContent.startsWith('Раскрытие.'))})")
    check('Disclosures paragraph in the colophon (EN and RU)', disc['en'] and disc['ru'], disc)
    over = p.evaluate("()=>document.documentElement.scrollWidth>document.documentElement.clientWidth+1")
    check('nothing overflows the viewport', not over)
    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    ctx.close(); b.close()
    return fails


if __name__ == '__main__':
    with sync_playwright() as pw:
        f = run(pw, 1600, 1000) + run(pw, 400, 800) + tables(pw, 1280, 900) + tables(pw, 400, 800) + sorting(pw, 1280, 900) + sorting(pw, 400, 800) + chapter8(pw, 1280, 900) + chapter8(pw, 400, 800)
    print('RESULT:', 'PASS' if not f else f'FAIL {f}')
    sys.exit(1 if f else 0)
