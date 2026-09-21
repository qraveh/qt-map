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


def laptop(pw):
    """Editor's screenshot of 20 Sep (laptop, OS scaling → ~1000 CSS px): a mouse laptop keeps the floating card (no bottom sheet), the card
    drags by its grip; a phone-width sheet resizes by dragging its grip and remembers the height; a machine clicked in "Used by" becomes the
    selection (machine card, its stations lit) and the map is scrolled into view; a double click does not undo it; a fitted map stays fitted
    across a resize and the page keeps room for the sheet; 0 console errors."""
    fails, errors = [], []
    b = pw.chromium.launch()
    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)
    CLICK = "id=>{const g=[...document.querySelectorAll('#mapwrap g.station')].find(g=>g.querySelector('text.id')&&g.querySelector('text.id').textContent===id); g.dispatchEvent(new MouseEvent('click',{bubbles:true}));}"
    STATE = "()=>{const i=document.getElementById('insp'); const r=i.getBoundingClientRect(); const cs=getComputedStyle(i); const mw=document.getElementById('mapwrap').getBoundingClientRect(); return {hidden:i.hidden, sheet:cs.position==='fixed'&&Math.round(r.left)===0&&Math.round(r.right)===innerWidth, left:Math.round(r.left), top:Math.round(r.top), h:Math.round(r.height), title:(i.querySelector('h3')||{}).textContent||'', lit:[...document.querySelectorAll('#mapwrap g.station')].filter(g=>!g.classList.contains('dim')).length, machine:(document.getElementById('machine')||{}).value||'', mapTop:Math.round(mw.top), mapBottom:Math.round(mw.bottom), svgW:Math.round(document.querySelector('#mapwrap svg').getBoundingClientRect().width), wrapW:document.getElementById('mapwrap').clientWidth, hasSheet:document.body.classList.contains('has-sheet'), vh:innerHeight, vw:innerWidth};}"
    def drag(p, sel, dx, dy):
        el = p.locator(sel).first; bb = el.bounding_box()
        x0, y0 = bb['x'] + min(12, bb['width'] / 2), bb['y'] + bb['height'] / 2
        p.mouse.move(x0, y0); p.mouse.down(); p.mouse.move(x0 + dx / 2, y0 + dy / 2, steps=4); p.mouse.move(x0 + dx, y0 + dy, steps=4); p.mouse.up(); p.wait_for_timeout(150)
    print('laptop — 1000×625, mouse')
    ctx = b.new_context(viewport={'width': 1000, 'height': 625}); p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text)); p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0 && document.querySelectorAll('#machine option').length>1", timeout=60000)
    p.evaluate(CLICK, 'ae_atom'); p.wait_for_timeout(400); s0 = p.evaluate(STATE)
    check('1000 px + mouse: floating card, not a sheet', not s0['hidden'] and not s0['sheet'] and s0['h'] <= s0['vh'] - 90, s0)
    drag(p, '#insp [data-grip]', 180, 60); s1 = p.evaluate(STATE)
    check('card drags by its grip', abs(s1['left'] - s0['left'] - 180) <= 6 and abs(s1['top'] - s0['top'] - 60) <= 6, (s0['left'], s0['top'], s1['left'], s1['top']))
    n = p.evaluate("()=>document.querySelectorAll('#insp [data-mach]').length")
    first = p.evaluate("()=>{const a=document.querySelector('#insp [data-mach]'); return a?[a.dataset.mach,a.textContent]:null;}")
    p.locator('#insp [data-mach]').first.click(); p.wait_for_timeout(1200); s2 = p.evaluate(STATE)
    check('"Used by" click: the machine is selected, its card shows, its stations are lit', n >= 1 and s2['machine'] == first[0] and first[1].strip()[:20] in s2['title'] and 0 < s2['lit'] < 96, (first, s2['machine'], s2['title'][:40], s2['lit']))
    check('"Used by" click: the map is in view', s2['mapBottom'] > 120 and s2['mapTop'] < s2['vh'] * 0.6, (s2['mapTop'], s2['mapBottom'], s2['vh']))
    # double click on a machine link inside a station card must not undo the selection
    p.evaluate(CLICK, 'enc_dualrail'); p.wait_for_timeout(400)
    tgt = p.evaluate("()=>{const a=document.querySelector('#insp [data-mach]'); return a?a.dataset.mach:null;}")
    if tgt:
        p.locator('#insp [data-mach]').first.dblclick(); p.wait_for_timeout(500); s3 = p.evaluate(STATE)
        check('double click on a machine link keeps the machine selected', s3['machine'] == tgt, (tgt, s3['machine']))
    # fit stays fitted across a resize
    p.click('#zoom-fit'); p.wait_for_timeout(300); p.set_viewport_size({'width': 1200, 'height': 700}); p.wait_for_timeout(600); s4 = p.evaluate(STATE)
    check('fit width follows a resize', s4['svgW'] <= s4['wrapW'] + 2 and s4['svgW'] >= s4['wrapW'] - 40, (s4['svgW'], s4['wrapW']))
    p.set_viewport_size({'width': 1000, 'height': 625}); p.wait_for_timeout(600); s5 = p.evaluate(STATE)
    check('fit width follows a resize back', s5['svgW'] <= s5['wrapW'] + 2, (s5['svgW'], s5['wrapW']))
    ctx.close()
    print('phone — 400×800, touch: the sheet')
    ctx = b.new_context(viewport={'width': 400, 'height': 800}, has_touch=True, is_mobile=True); p = ctx.new_page()
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text)); p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
    p.evaluate(CLICK, 'ae_atom'); p.wait_for_timeout(500); t0 = p.evaluate(STATE)
    check('400 px: bottom sheet, page has room above it', not t0['hidden'] and t0['sheet'] and t0['hasSheet'] and t0['h'] <= t0['vh'] * 0.5, t0)
    drag(p, '#insp [data-grip]', 0, -150); t1 = p.evaluate(STATE)
    check('sheet grip drag makes the sheet taller', t1['h'] >= t0['h'] + 100, (t0['h'], t1['h']))
    p.reload(wait_until='load'); p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
    p.evaluate(CLICK, 'ae_atom'); p.wait_for_timeout(500); t2 = p.evaluate(STATE)
    check('sheet height is remembered after a reload', abs(t2['h'] - t1['h']) <= 12, (t1['h'], t2['h']))
    p.set_viewport_size({'width': 1000, 'height': 625}); p.wait_for_timeout(600); t3 = p.evaluate(STATE)
    check('resize to 1000 px on a touch screen keeps the sheet and the page room', t3['sheet'] and t3['hasSheet'], t3)
    ctx.close(); b.close()
    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    return fails


def selections(pw):
    """Editor's reproduction of 21 Sep: click the trapped-ions line, then the dual-rail station — the superconducting path was missing
    (the lit set was the empty intersection of an isolated path and a station off it). Adjudication 12: a selection that cannot share a line
    with an older selection releases it. Checks the three pairings in both orders at 1280×800; 0 console errors."""
    fails, errors = [], []
    b = pw.chromium.launch(); ctx = b.new_context(viewport={'width': 1280, 'height': 800}); p = ctx.new_page()
    def check(label, cond, detail=''):
        print(f"  [{'ok' if cond else 'FAIL'}] {label}{(' — ' + str(detail)) if (detail and not cond) else ''}")
        if not cond: fails.append(label)
    CLICK = "id=>{const g=[...document.querySelectorAll('#mapwrap g.station')].find(g=>g.querySelector('text.id')&&g.querySelector('text.id').textContent===id); g.dispatchEvent(new MouseEvent('click',{bubbles:true}));}"
    LINE = "id=>{const h=document.querySelector('#mapwrap path.phit[data-path=\"'+id+'\"]'); h.dispatchEvent(new MouseEvent('click',{bubbles:true}));}"
    print('selections — 1280×800')
    p.on('console', lambda m: m.type == 'error' and errors.append(m.text)); p.on('pageerror', lambda e: errors.append('pageerror: ' + str(e)))
    p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
    rd = lambda: p.evaluate(READ)
    ion = p.evaluate("()=>[...document.querySelectorAll('#pathchips .chip')].map(c=>c.dataset.chipPath).find(x=>x.startsWith('ion'))")
    pressed = lambda: p.evaluate("()=>[...document.querySelectorAll('#pathchips .chip[aria-pressed=\"true\"]')].map(c=>c.dataset.chipPath)")
    GR = json.load(open(ROOT / 'data' / 'graph.json', encoding='utf-8'))
    slots = {q['id']: [x for v in q['slots'].values() for x in v] for q in GR['paths']}
    dual_paths = {q for q, xs in slots.items() if 'enc_dualrail' in xs}
    # 1. the editor's steps: isolate the ion path, click dual-rail
    p.evaluate(LINE, ion); p.wait_for_timeout(300); r0 = rd()
    check('click on the trapped-ions line isolates it', r0['lines'] == [ion] and pressed() == [ion], (r0['lines'], pressed()))
    p.evaluate(CLICK, 'enc_dualrail'); p.wait_for_timeout(400); r1 = rd()
    check('then click on dual-rail: its paths are lit, the ion isolate is released', set(r1['lines']) == dual_paths and pressed() == [] and 'enc_dualrail' in r1['lit'], (r1['lines'], pressed()))
    check('… and the station card shows', 'dual-rail' in r1['card'].lower() or 'dual' in r1['card'].lower(), r1['card'][:60])
    # 2. mirror: focus dual-rail, then isolate the ion path -> the focus is released, the ion path stands alone with its card
    p.keyboard.press('Escape'); p.wait_for_timeout(200); p.evaluate(CLICK, 'enc_dualrail'); p.wait_for_timeout(300)
    p.evaluate(LINE, ion); p.wait_for_timeout(400); r2 = rd(); sel = p.evaluate("()=>[...document.querySelectorAll('#mapwrap g.station.sel')].length")
    check('focus dual-rail, then isolate the ion path: the focus is released, the ion line stands alone', r2['lines'] == [ion] and sel == 0 and pressed() == [ion], (r2['lines'], sel, pressed()))
    # 3. compatible pair keeps the intersection: a station on the isolated path
    on_ion = slots[ion][0]
    p.evaluate(CLICK, on_ion); p.wait_for_timeout(300); r3 = rd()
    check('a station on the isolated path keeps the isolate (intersection)', r3['lines'] == [ion] and pressed() == [ion] and on_ion in r3['lit'], (r3['lines'], pressed()))
    # 4. machine x isolate: a superconducting machine chosen while the ion path is isolated releases the isolate
    p.select_option('#machine', 'google-willow'); p.wait_for_timeout(400); r4 = rd()
    check('a machine on another path releases the isolate', r4['lines'] == [WILLOW['map_path']] and pressed() == [] and r4['machine'] == 'google-willow', (r4['lines'], pressed(), r4['machine']))
    p.evaluate(LINE, ion); p.wait_for_timeout(400); r5 = rd()
    check('isolating another path releases the machine', r5['lines'] == [ion] and r5['machine'] == '' and pressed() == [ion], (r5['lines'], r5['machine']))
    # 5. machine x focus: a station off the machine's path releases the machine; one on it keeps it
    p.click('#tg-reset'); p.wait_for_timeout(300); p.select_option('#machine', 'google-willow'); p.wait_for_timeout(300)
    p.evaluate(CLICK, 'transmon'); p.wait_for_timeout(300); r6 = rd()
    check('a station on the machine\'s path keeps the machine', r6['machine'] == 'google-willow' and r6['lines'] == [WILLOW['map_path']], (r6['machine'], r6['lines']))
    p.evaluate(CLICK, 'ae_atom'); p.wait_for_timeout(300); r7 = rd()
    check('a station off the machine\'s path releases the machine and lights its own paths', r7['machine'] == '' and len(r7['lines']) >= 1 and WILLOW['map_path'] not in r7['lines'] and 'ae_atom' in r7['lit'], (r7['machine'], r7['lines']))
    ctx.close(); b.close()
    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    return fails


if __name__ == '__main__':
    with sync_playwright() as pw:
        f = run(pw, 1600, 1000) + run(pw, 400, 800) + tables(pw, 1280, 900) + tables(pw, 400, 800) + sorting(pw, 1280, 900) + sorting(pw, 400, 800) + chapter8(pw, 1280, 900) + chapter8(pw, 400, 800) + laptop(pw) + selections(pw)
    print('RESULT:', 'PASS' if not f else f'FAIL {f}')
    sys.exit(1 if f else 0)
