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
    check('selector: optgroups in family order with 136 machines', [o[0] for o in opt] == ['superconducting', 'ions', 'atoms', 'photonics', 'spins', 'defects', 'topological', 'annealing'] and sum(o[1] for o in opt) == 136, opt)

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

    p.locator('[data-setlang="ru"]').filter(visible=True).first.click()
    p.wait_for_function("document.getElementById('app').getAttribute('data-lang')==='ru'")
    vis = p.evaluate("()=>[...document.querySelectorAll('.machgrp .lbl')].filter(e=>getComputedStyle(e).display!=='none').map(e=>e.textContent)")
    og = p.evaluate("()=>[...document.querySelectorAll('#machine optgroup')].map(o=>o.label)")
    check('RU: machine label and optgroups in Russian', vis == ['машина'] and og[0] == 'сверхпроводники', (vis, og[:2]))
    p.select_option('#machine', 'google-willow')
    r = read()
    check('RU: machine card in Russian', 'карточка реестра' in r['card'] and 'источники: ✅ 14 / 16' in r['card'], r['card'][:100])
    p.locator('[data-setlang="en"]').filter(visible=True).first.click()

    errs = [e for e in errors if not ('fonts.g' in e and ('ERR_TUNNEL' in e or 'net::' in e)) and 'ERR_TUNNEL' not in e]
    check('0 console errors', not errs, errs[:3])
    ctx.close(); b.close()
    return fails


TZ = """()=>{
  const fold=id=>{ let e=document.getElementById(id); while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return e; const w=e.querySelector&&e.querySelector('.tbl'); if(w)return w; } return null; };
  const st=w=>{ const t=w&&w.querySelector('table'); if(!t)return null; const m=/scale\\(([\\d.]+)\\)/.exec(t.style.transform||'');
    return {bar:!!w.querySelector('.tblzoom:not([hidden])'),z:m?parseFloat(m[1]):1,zoomed:w.classList.contains('zoomed'),big:t.offsetWidth>w.clientWidth+8,hscroll:w.scrollWidth>w.clientWidth+1,fits:w.scrollWidth<=w.clientWidth+1}; };
  const small=[...document.querySelectorAll('#app .prose.lang-en .tbl')].find(w=>!w.closest('details')&&w.clientWidth>0&&w.querySelector('table').scrollWidth<=w.clientWidth);
  return {node:st(fold('en-s11-19')),edge:st(fold('en-s11-27')),small:small?{bar:!!small.querySelector('.tblzoom:not([hidden])'),zoomed:small.classList.contains('zoomed')}:null,
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
    p.wait_for_function("()=>{let e=document.getElementById('en-s11-19'); while(e&&(e=e.nextElementSibling)){ if(e.matches('.tbl'))return !!e.querySelector('.tblzoom:not([hidden])'); } return false;}", timeout=20000)
    p.wait_for_timeout(300)
    r = p.evaluate(TZ)
    check('§7.2 node table: bar present, scaled < 1, fits (no horizontal scroll)', r['node'] and r['node']['bar'] and r['node']['z'] < 1 and r['node']['zoomed'] and r['node']['fits'], r['node'])
    # the edge list has 3 columns and fits its wrapper at 1280 and at 400 px (headers wrap on phones): bar iff big, scaled to fit when big
    check('§7.10 edge list: bar iff wider than its wrapper; scaled to fit when big', r['edge'] and r['edge']['bar'] == r['edge']['big'] and (not r['edge']['big'] or (r['edge']['z'] < 1 and r['edge']['fits'])), r['edge'])
    check('a small table gets no bar', r['small'] is not None and not r['small']['bar'] and not r['small']['zoomed'], r['small'])
    print(f"  bars with every EN fold open: {r['bars']}")
    node = p.locator('#en-s11-19 ~ div.tbl').first
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


if __name__ == '__main__':
    with sync_playwright() as pw:
        f = run(pw, 1600, 1000) + run(pw, 400, 800) + tables(pw, 1280, 900) + tables(pw, 400, 800)
    print('RESULT:', 'PASS' if not f else f'FAIL {f}')
    sys.exit(1 if f else 0)
