#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small-screen and touch checks on the built page (28 Sep 2026): the zoom control on top, the card as a bottom sheet with
its picture, pinch zoom about the fingers, the two-swipe hand-over at the map's edge, and the find bar (both viewports).

    python3 build/audit/mobile_check.py [--shots DIR]
"""
import argparse, os, sys, time
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.join(ROOT, 'dist', 'index.html')
FAILS = []


def check(name, ok, info=None):
    print(('  [ok]   ' if ok else '  [FAIL] ') + name + ('' if ok else ' — ' + str(info)[:400]))
    if not ok: FAILS.append(name)


TOUCH_JS = """(args)=>{ const [type, pts] = args; const el=document.getElementById('mapwrap');
  const touches=pts.map((p,i)=>new Touch({identifier:i, target:el, clientX:p[0], clientY:p[1], pageX:p[0], pageY:p[1]+window.scrollY}));
  const ev=new TouchEvent(type,{touches:type==='touchend'?[]:touches, targetTouches:type==='touchend'?[]:touches, changedTouches:touches, bubbles:true, cancelable:true});
  el.dispatchEvent(ev); return true; }"""


def phone(pw, shots):
    b = pw.chromium.launch(); ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, has_touch=True, is_mobile=True)
    p = ctx.new_page(); errors = []
    p.on('pageerror', lambda e: errors.append(str(e)))
    p.goto('file://' + PAGE, wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000); time.sleep(0.8)
    print('phone 390×844, touch')
    # 1. zoom control: first child of the scroller, top-right, below the sticky bar when the map's top passes under it
    r = p.evaluate("()=>{const w=document.getElementById('mapwrap'); const zb=w.firstElementChild; const c=document.querySelector('.zoomctl').getBoundingClientRect(); const wr=w.getBoundingClientRect(); return {first:zb&&zb.classList.contains('zoombar'), inWrap:!!document.querySelector('#mapwrap .zoomctl'), top:Math.round(c.top-wr.top), right:Math.round(wr.right-c.right), width:Math.round(c.width), fith:getComputedStyle(document.getElementById('zoom-fith')).display, vw:innerWidth};}")
    check('phone: the zoom control sits inside the scroller, first child, top-right', r['first'] and r['inWrap'] and 0 <= r['top'] < 30 and 0 <= r['right'] < 30, r)
    check('phone: fit-height and align-top hidden, the control narrower than the screen', r['fith'] == 'none' and r['width'] < r['vw'] - 60, r)
    p.evaluate("()=>{document.getElementById('mapwrap').scrollIntoView({block:'start'}); window.scrollBy(0,120);}"); time.sleep(0.4)
    r2 = p.evaluate("()=>{const c=document.querySelector('.zoomctl').getBoundingClientRect(); const mb=document.querySelector('.mobilebar').getBoundingClientRect(); const wr=document.getElementById('mapwrap').getBoundingClientRect(); return {ctop:Math.round(c.top), barBottom:Math.round(mb.bottom), wtop:Math.round(wr.top)};}")
    check('phone: with the map\'s top under the page bar, the control is pushed below the bar', r2['wtop'] < r2['barBottom'] and r2['ctop'] >= r2['barBottom'] - 1, r2)
    if shots: p.screenshot(path=os.path.join(shots, 'phone_zoomtop.png'))
    # 2. tap a technology: the sheet opens with a picture
    p.evaluate("()=>{window.scrollTo(0,0); document.getElementById('mapwrap').scrollIntoView({block:'start'});}"); time.sleep(0.3)
    box = p.evaluate("()=>{const g=[...document.querySelectorAll('#mapwrap g.station')].find(g=>g.__data__&&g.__data__.id==='transmon'); const r=g.querySelector('rect.box').getBoundingClientRect(); const w=document.getElementById('mapwrap'); w.scrollLeft=Math.max(0,r.left+w.scrollLeft-40); w.scrollTop=Math.max(0,r.top-w.getBoundingClientRect().top+w.scrollTop-80); const r2=g.querySelector('rect.box').getBoundingClientRect(); return {x:r2.left+r2.width/2, y:r2.top+r2.height/2};}")
    p.touchscreen.tap(box['x'], box['y']); time.sleep(0.8)
    c = p.evaluate("()=>{const i=document.getElementById('insp'); const f=i.querySelector('figure.cardpic img'); const r=i.getBoundingClientRect(); return {open:!i.hidden, title:(i.querySelector('h3')||{}).textContent, pic:!!f, src:f?f.getAttribute('src'):'', bottom:Math.round(innerHeight-r.bottom), sheet:getComputedStyle(i).position};}")
    check('phone: a tap opens the technology card as a bottom sheet', c['open'] and 'Transmon' in (c['title'] or '') and c['sheet'] == 'fixed' and abs(c['bottom']) < 2, c)
    check('phone: the card shows the technology\'s picture from media/', c['pic'] and c['src'].startswith('media/') and c['src'].endswith('.jpg'), c)
    if shots: p.screenshot(path=os.path.join(shots, 'phone_card.png'))
    p.evaluate("()=>{const b=document.querySelector('#insp [data-close]'); if(b)b.click();}"); time.sleep(0.3)
    # 3. pinch: two fingers spread → zoom in about the midpoint; the content point under the midpoint stays put
    before = p.evaluate("()=>{const w=document.getElementById('mapwrap'); const z=parseInt(document.getElementById('zoomlvl').value)||0; const r=w.getBoundingClientRect(); return {z:z, sl:w.scrollLeft, st:w.scrollTop, left:r.left, top:r.top, zoom:(window.__pinchState? 1:0)};}")
    wl, wt = before['left'], before['top']
    pts0 = [[wl + 150, wt + 300], [wl + 230, wt + 300]]; pts1 = [[wl + 110, wt + 300], [wl + 270, wt + 300]]
    p.evaluate(TOUCH_JS, ['touchstart', pts0]); time.sleep(0.05)
    p.evaluate(TOUCH_JS, ['touchmove', [[wl + 130, wt + 300], [wl + 250, wt + 300]]]); time.sleep(0.08)
    p.evaluate(TOUCH_JS, ['touchmove', pts1]); time.sleep(0.15)
    p.evaluate(TOUCH_JS, ['touchend', pts1]); time.sleep(0.3)
    after = p.evaluate("()=>{const w=document.getElementById('mapwrap'); const z=parseInt(document.getElementById('zoomlvl').value)||0; return {z:z, sl:w.scrollLeft, st:w.scrollTop, svgw:document.querySelector('#mapwrap svg').getAttribute('width')};}")
    ratio = after['z'] / max(1, before['z'])
    # midpoint (190,300) inside the wrap: the content coordinate under it before = (sl+190)/z0, after = (sl'+190)/z1
    z0 = before['z']; z1 = after['z']
    cx0 = (before['sl'] + 190) / z0 if z0 else 0; cx1 = (after['sl'] + 190) / z1 if z1 else 1
    check('phone: a spreading pinch zooms in (fingers 80 → 160 px apart ≈ ×2)', 1.7 < ratio < 2.3, (before['z'], after['z']))
    check('phone: the point under the fingers stays under them (scroll follows the zoom)', abs(cx0 - cx1) / max(cx0, 1e-6) < 0.03, (cx0, cx1, before, after))
    # pinch in: back near the start
    p.evaluate(TOUCH_JS, ['touchstart', pts1]); time.sleep(0.05); p.evaluate(TOUCH_JS, ['touchmove', pts0]); time.sleep(0.15); p.evaluate(TOUCH_JS, ['touchend', pts0]); time.sleep(0.3)
    z2 = p.evaluate("()=>parseInt(document.getElementById('zoomlvl').value)||0")
    check('phone: a closing pinch zooms out again', abs(z2 - before['z']) <= max(3, 0.06 * before['z']), (before['z'], z1, z2))
    # 4. two swipes at the bottom hand over to the page
    p.evaluate("()=>{const w=document.getElementById('mapwrap'); w.scrollTop=w.scrollHeight; window.scrollTo(0, w.getBoundingClientRect().top+window.scrollY-60);}"); time.sleep(0.4)
    y0 = p.evaluate("()=>window.scrollY")
    for k in range(2):
        r = p.evaluate("()=>document.getElementById('mapwrap').getBoundingClientRect()")
        p.evaluate(TOUCH_JS, ['touchstart', [[r['left'] + 150, r['top'] + 400]]]); time.sleep(0.05)
        p.evaluate(TOUCH_JS, ['touchmove', [[r['left'] + 150, r['top'] + 350]]]); time.sleep(0.05)
        p.evaluate(TOUCH_JS, ['touchend', [[r['left'] + 150, r['top'] + 350]]]); time.sleep(0.25)
    time.sleep(1.2)
    y1 = p.evaluate("()=>window.scrollY")
    check('phone: two swipes at the map\'s bottom hand the scroll over to the page', y1 > y0 + 100, (y0, y1))
    # 5. find bar on the phone: opens from the bar button, full width under the page bar
    p.evaluate("()=>window.scrollTo(0,0)"); time.sleep(0.2)
    p.click('.mobilebar [data-findopen]'); time.sleep(0.3)
    f = p.evaluate("()=>{const b=document.getElementById('findbar'); const r=b.getBoundingClientRect(); const mb=document.querySelector('.mobilebar').getBoundingClientRect(); return {open:!b.hidden, top:Math.round(r.top), barBottom:Math.round(mb.bottom), left:Math.round(r.left), right:Math.round(innerWidth-r.right), focused:document.activeElement===document.getElementById('findq')};}")
    check('phone: the find bar opens under the page bar, edge to edge, with the input focused', f['open'] and f['top'] >= f['barBottom'] - 2 and f['left'] < 12 and f['right'] < 12 and f['focused'], f)
    n = p.evaluate("()=>window.__find.search('erasure',{scope:'this',cs:false,whole:false})"); time.sleep(0.2)
    c0 = p.evaluate("()=>document.getElementById('findcount').textContent")
    fr = p.evaluate("()=>{window.__find.go(0); const c=document.getElementById('findcount').textContent; const h=window.__find.hits()[window.__find.cur()]; let vis=false; if(h&&h.kind==='text'){ const r=document.createRange(); const g=h.run.segs[0]; r.setStart(g.node,0); r.setEnd(g.node,g.node.length); const rr=r.getBoundingClientRect(); vis=rr.top>=0&&rr.bottom<=innerHeight; } return {count:c, n:window.__find.hits().length, vis:vis, rows:document.querySelectorAll('#findlist li').length};}")
    check('phone: "erasure" finds hits — the count reads "— / N" until a jump, then "1 / N" with the hit in view and the list filled', n > 20 and c0.startswith('— / ') and fr['count'].startswith('1 / ') and fr['vis'] and fr['rows'] > 10, (c0, fr))
    if shots: p.screenshot(path=os.path.join(shots, 'phone_find.png'))
    # 6. nothing overflows the phone's width — at the top, with a brief open, in Russian (the RU fragment loaded)
    p.evaluate("()=>{window.__find.close(); document.querySelector('#insp [data-close]')&&document.querySelector('#insp [data-close]').click(); window.scrollTo(0,0);}"); time.sleep(0.3)
    p.wait_for_function("!document.documentElement.classList.contains('lang-loading')", timeout=60000)
    OVER = """()=>{const vw=innerWidth; const out=[]; const bad=[]; const inScroller=el=>{ for(let p=el.parentElement;p;p=p.parentElement){ const o=getComputedStyle(p).overflowX; if(o==='auto'||o==='scroll'||o==='hidden')return true; } return false; };
      document.querySelectorAll('body *').forEach(el=>{ if(bad.length>12)return; const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden'||cs.position==='fixed')return; const r=el.getBoundingClientRect(); if(!r.width)return; if(r.right>vw+2&&!inScroller(el)) bad.push(el.tagName+'.'+String(el.className).slice(0,40)+' right='+Math.round(r.right)); });
      return {sw:document.documentElement.scrollWidth, vw:vw, bad:bad};}"""
    o1 = p.evaluate(OVER)
    check('phone: nothing wider than the screen on the English page (no horizontal page scroll)', o1['sw'] <= o1['vw'] + 1 and not o1['bad'], o1)
    p.evaluate("()=>window.__openBrief('transmon')"); time.sleep(0.6)
    o2 = p.evaluate(OVER)
    check('phone: nothing wider than the screen with a brief open', o2['sw'] <= o2['vw'] + 1 and not o2['bad'], o2)
    if shots: p.screenshot(path=os.path.join(shots, 'phone_brief.png'))
    p.evaluate("()=>{window.__closeBrief(false); window.__setLang('ru'); window.scrollTo(0,0);}"); time.sleep(0.6)
    o3 = p.evaluate(OVER)
    check('phone: nothing wider than the screen on the Russian page', o3['sw'] <= o3['vw'] + 1 and not o3['bad'], o3)
    mb = p.evaluate("()=>{const r=document.querySelector('.mobilebar .mb-seg').getBoundingClientRect(); return {right:Math.round(r.right), vw:innerWidth};}")
    check('phone (Russian): the page bar\'s language switch is fully on screen', mb['right'] <= mb['vw'], mb)
    if shots: p.screenshot(path=os.path.join(shots, 'phone_ru_top.png'))
    p.evaluate("()=>window.__setLang('en')")
    # 7. the find window is sticky (29 Sep 2026): stored open, it reopens after a reload — still the band under the page bar, no grip
    p.evaluate("()=>{window.scrollTo(0,0); window.__find.open(null);}"); time.sleep(0.5)
    p.reload(wait_until='load', timeout=120000); p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000); time.sleep(0.6)
    f2 = p.evaluate("()=>{const b=document.getElementById('findbar'); const r=b.getBoundingClientRect(); const mb=document.querySelector('.mobilebar').getBoundingClientRect(); return {open:!b.hidden, top:Math.round(r.top), barBottom:Math.round(mb.bottom), left:Math.round(r.left), right:Math.round(innerWidth-r.right), grip:getComputedStyle(b.querySelector('.fgrip')).display};}")
    check('phone: stored open, the find window reopens after a reload — edge to edge under the page bar, no grip', f2['open'] and f2['top'] >= f2['barBottom'] - 2 and f2['left'] < 12 and f2['right'] < 12 and f2['grip'] == 'none', f2)
    check('phone: no page errors', not errors, errors[:3])
    b.close()


def tablet(pw, shots):
    b = pw.chromium.launch(); ctx = b.new_context(viewport={'width': 768, 'height': 1024}, device_scale_factor=2, has_touch=True, is_mobile=True)
    p = ctx.new_page(); errors = []
    p.on('pageerror', lambda e: errors.append(str(e)))
    p.goto('file://' + PAGE, wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000); time.sleep(0.6)
    print('tablet 768×1024, touch')
    r = p.evaluate("()=>{const w=document.getElementById('mapwrap'); const c=document.querySelector('.zoomctl').getBoundingClientRect(); const wr=w.getBoundingClientRect(); return {inWrap:!!document.querySelector('#mapwrap .zoomctl'), top:Math.round(c.top-wr.top), sw:document.documentElement.scrollWidth, vw:innerWidth, fith:getComputedStyle(document.getElementById('zoom-fith')).display};}")
    check('tablet: the zoom control sits at the top of the scroller with all its buttons; no horizontal page scroll', r['inWrap'] and 0 <= r['top'] < 30 and r['fith'] != 'none' and r['sw'] <= r['vw'] + 1, r)
    p.evaluate("()=>window.__selectNode('ion')"); time.sleep(0.5)
    c = p.evaluate("()=>{const i=document.getElementById('insp'); const r=i.getBoundingClientRect(); return {open:!i.hidden, sheet:getComputedStyle(i).position==='fixed'&&Math.abs(innerHeight-r.bottom)<2, pic:!!i.querySelector('figure.cardpic')};}")
    check('tablet (touch): the card is a bottom sheet with the picture', c['open'] and c['sheet'] and c['pic'], c)
    if shots: p.screenshot(path=os.path.join(shots, 'tablet_card.png'))
    check('tablet: no page errors', not errors, errors[:3])
    b.close()


def desktop(pw, shots):
    b = pw.chromium.launch(); ctx = b.new_context(viewport={'width': 1280, 'height': 860})
    p = ctx.new_page(); errors = []
    p.on('pageerror', lambda e: errors.append(str(e)))
    p.goto('file://' + PAGE, wait_until='load', timeout=120000)
    p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
    p.wait_for_function("!document.documentElement.classList.contains('lang-loading')", timeout=60000); time.sleep(0.5)
    print('desktop 1280×860')
    r = p.evaluate("()=>{const c=document.querySelector('#mapbar .zoomwin .zoomctl'); return {inBar:!!c, findbtn:!!document.querySelector('nav.toc .findopen')};}")
    check('desktop: the zoom control stays in the map bar; the contents column offers Find', r['inBar'] and r['findbtn'], r)
    p.keyboard.press('/'); time.sleep(0.2)
    check('desktop: "/" opens the find bar with the input focused', p.evaluate("()=>!document.getElementById('findbar').hidden && document.activeElement===document.getElementById('findq')"))
    p.keyboard.type('threshold'); p.keyboard.press('Enter'); time.sleep(0.6)
    r1 = p.evaluate("()=>({count:document.getElementById('findcount').textContent, n:window.__find.hits().length, cur:window.__find.cur(), hl:!!(CSS.highlights&&CSS.highlights.get('findcur'))})")
    check('desktop: Enter searches — "threshold" has many hits, the first is current and highlighted', r1['n'] > 30 and r1['cur'] == 0 and r1['count'].startswith('1 / ') and r1['hl'], r1)
    p.keyboard.press('Enter'); time.sleep(0.3); p.keyboard.press('Enter'); time.sleep(0.3)
    p.keyboard.press('Shift+Enter'); time.sleep(0.3)
    r2 = p.evaluate("()=>({cur:window.__find.cur(), count:document.getElementById('findcount').textContent})")
    check('desktop: Enter, Enter, Shift+Enter → the second hit is current', r2['cur'] == 1 and r2['count'].startswith('2 / '), r2)
    # a hit inside a closed brief: reveal opens the brief
    n = p.evaluate("()=>window.__find.search('quasiparticle poisoning')"); time.sleep(0.5)
    r3 = p.evaluate("()=>{const hs=window.__find.hits(); const i=hs.findIndex(h=>h.kind==='text'&&h.run.segs[0].node.parentElement.closest('section.brief')); if(i<0)return {i:-1}; window.__find.go(i); const s=hs[i].run.segs[0].node.parentElement.closest('section.brief'); return {i:i, n:hs.length, open:!s.hidden, id:s.id};}"); time.sleep(0.4)
    check('desktop: a hit inside a closed brief opens that brief', r3['i'] >= 0 and r3['open'], r3)
    # wildcards and whole word
    n_w = p.evaluate("()=>window.__find.search('quasi\\\\w*\\\\s+poison.ng')")
    n_cls = p.evaluate("()=>window.__find.search('[Ee]rasure conv')")
    n_word = p.evaluate("()=>window.__find.search('ion',{whole:true})"); n_sub = p.evaluate("()=>window.__find.search('ion',{whole:false})")
    n_cs = p.evaluate("()=>window.__find.search('Transmon',{cs:true})"); n_ci = p.evaluate("()=>window.__find.search('Transmon',{cs:false})")
    lab = p.evaluate("()=>({word:document.getElementById('findword').textContent.trim(), cs:document.getElementById('findcase').textContent.trim(), lang:document.getElementById('findlangname').textContent.trim()})")
    check('desktop: regex (\\w* \\s+ . []) matches; whole word narrows; match case narrows; the toggles name their state', n_w > 0 and n_cls > 0 and 0 < n_word < n_sub and 0 < n_cs < n_ci and lab['word'] and lab['cs'] and lab['lang'], (n_w, n_cls, n_word, n_sub, n_cs, n_ci, lab))
    # the other language: a Russian query in scope "other" switches the page to Russian on reveal
    n_ru = p.evaluate("()=>window.__find.search('стиран\\\\w*',{scope:'ru',whole:false,cs:false})"); time.sleep(0.2)
    r4 = p.evaluate("()=>{window.__find.go(0); document.getElementById('findlang').click(); const menu=document.querySelectorAll('#findlangmenu button').length; const names=[...document.querySelectorAll('#findlangmenu button')].map(b=>b.textContent.trim()); document.getElementById('findlang').click(); return {lang:document.getElementById('app').getAttribute('data-lang'), n:window.__find.hits().length, menu:menu, names:names};}"); time.sleep(0.5)
    r4['lang'] = p.evaluate("()=>document.getElementById('app').getAttribute('data-lang')")
    check('desktop: a hit in the other language (scope: that language) switches the page to it; the language menu lists the languages and "all"', n_ru > 0 and r4['lang'] == 'ru' and r4['menu'] >= 3, r4)
    p.evaluate("()=>window.__setLang('en')"); time.sleep(0.3)
    # metadata: a tooltip hit
    n_m = p.evaluate("()=>window.__find.search('show or hide the map controls',{scope:'this',cs:false,whole:false})")
    r5 = p.evaluate("()=>{const hs=window.__find.hits(); return {n:hs.length, meta:hs.filter(h=>h.kind==='meta').length};}")
    check('desktop: tooltip text is searched as metadata', r5['n'] > 0, r5)
    # a card hit opens the card
    p.evaluate("()=>window.__find.search('Fluxonium',{scope:'this'})"); time.sleep(0.3)
    r6 = p.evaluate("()=>{const hs=window.__find.hits(); const i=hs.findIndex(h=>h.kind==='card'&&h.card.kind==='node'&&h.card.id==='fluxonium'); if(i<0)return {i:-1}; window.__find.go(i); const t=(document.querySelector('#insp h3')||{}).textContent||''; return {i:i, open:!document.getElementById('insp').hidden, title:t, note:document.getElementById('findwhere').textContent};}"); time.sleep(0.3)
    check('desktop: a hit in a technology card opens that card on the map', r6['i'] >= 0 and r6['open'] and 'Fluxonium' in r6['title'], r6)
    # the cards are searched as rendered: a machine card's status line ("DEPLOYED · 256 q") is found, and opens the machine's card
    n_r = p.evaluate("()=>window.__find.search('DEPLOYED',{scope:'this',cs:true,whole:true})"); time.sleep(0.2)
    r6b = p.evaluate("()=>{const hs=window.__find.hits(); const i=hs.findIndex(h=>h.kind==='card'&&h.card.kind==='machine'); if(i<0)return {i:-1,n:hs.length}; window.__find.go(i); const insp=document.getElementById('insp'); return {i:i, n:hs.length, open:!insp.hidden, mclose:!!insp.querySelector('[data-mclose]'), txt:(insp.textContent||'').indexOf('DEPLOYED')>=0};}"); time.sleep(0.3)
    check('desktop: rendered card text ("DEPLOYED") is searched; the hit opens the machine card', n_r > 0 and r6b['i'] >= 0 and r6b['open'] and r6b['mclose'] and r6b['txt'], r6b)
    # closing the machine card keeps the machine selected; the chip reopens the card; organisation names link to their pages
    r6c = p.evaluate("()=>{const insp=document.getElementById('insp'); const sel=document.getElementById('machine'); const before=sel.value; const org=!!insp.querySelector('a[href*=\"organisation/\"]'); insp.querySelector('[data-close]').click(); const chip=document.getElementById('machcard'); const after=sel.value; const chipShown=chip&&!chip.hidden; if(chipShown) chip.click(); return {before:before, after:after, chipShown:chipShown, reopened:!insp.hidden, org:org};}"); time.sleep(0.2)
    check('desktop: closing the machine card keeps the machine; the "card" chip reopens it; the card links the organisation', r6c['before'] and r6c['after'] == r6c['before'] and r6c['chipShown'] and r6c['reopened'] and r6c['org'], r6c)
    p.evaluate("()=>{const insp=document.getElementById('insp'); const b=insp.querySelector('[data-mclose]'); if(b)b.click();}"); time.sleep(0.2)
    # the find window opens where the user clicked
    p.evaluate("()=>window.__find.close()")
    p.mouse.click(300, 400); time.sleep(0.1)
    p.evaluate("()=>{window.__find.open({clientX:300,clientY:400});}"); time.sleep(0.2)
    r6d = p.evaluate("()=>{const r=document.getElementById('findbar').getBoundingClientRect(); return {left:Math.round(r.left), top:Math.round(r.top), op:getComputedStyle(document.getElementById('findbar')).opacity};}")
    check('desktop: the find window opens beside the click', 200 <= r6d['left'] <= 300 and 380 <= r6d['top'] <= 440, r6d)
    if shots: p.screenshot(path=os.path.join(shots, 'desktop_find.png'))
    p.keyboard.press('Escape'); time.sleep(0.2)
    check('desktop: Escape closes the find bar and clears the highlights', p.evaluate("()=>document.getElementById('findbar').hidden && !(CSS.highlights&&CSS.highlights.get('findall'))"))
    # the floating language switch: hidden while the masthead's switch is on screen, shown once it has scrolled away, and it switches
    p.evaluate("()=>window.scrollTo(0,0)"); time.sleep(0.4)
    f0 = p.evaluate("()=>{const f=document.getElementById('floatlang'); return f?{show:f.classList.contains('show'), op:getComputedStyle(f).opacity}:null;}")
    p.evaluate("()=>{const h=document.getElementById('en-s6'); if(h)h.scrollIntoView(); else window.scrollTo(0,1600);}"); time.sleep(0.5)
    f1 = p.evaluate("()=>{const f=document.getElementById('floatlang'); if(!f)return null; const r=f.getBoundingClientRect(); return {show:f.classList.contains('show'), op:getComputedStyle(f).opacity, top:Math.round(r.top), right:Math.round(innerWidth-r.right)};}")
    check('desktop: the floating language switch appears only once the masthead switch has scrolled away (top right, translucent)', f0 and not f0['show'] and f0['op'] == '0' and f1 and f1['show'] and 0 < float(f1['op']) < 1 and f1['top'] < 40 and f1['right'] < 40, (f0, f1))
    p.click('#floatlang [data-setlang="ru"]'); time.sleep(0.3)
    p.wait_for_function("!document.documentElement.classList.contains('lang-loading')", timeout=60000)
    f2 = p.evaluate("()=>({lang:document.getElementById('app').getAttribute('data-lang'), pressed:document.querySelector('#floatlang [data-setlang=\"ru\"]').getAttribute('aria-pressed')})")
    check('desktop: the floating switch switches the language and shows the state', f2['lang'] == 'ru' and f2['pressed'] == 'true', f2)
    # the pill steps aside while the map's controls bar (with the zoom buttons at its right end) passes under its corner
    p.evaluate("()=>{window.__setLang('en'); document.getElementById('mapbar').scrollIntoView();}"); time.sleep(0.5)
    f3 = p.evaluate("()=>{const f=document.getElementById('floatlang'); const r=document.getElementById('mapbar').getBoundingClientRect(); return {show:f.classList.contains('show'), barTop:Math.round(r.top)};}")
    check('desktop: the floating switch hides while the map bar is at the top of the window (no overlap with the zoom buttons)', f3 and not f3['show'] and f3['barTop'] < 64, f3)
    p.evaluate("()=>{window.__setLang('en'); window.scrollTo(0,0);}"); time.sleep(0.3)
    # the desktop card picture
    p.evaluate("()=>window.__selectNode('ion')"); time.sleep(0.5)
    r7 = p.evaluate("()=>{const f=document.querySelector('#insp figure.cardpic'); return {pic:!!f, cap:f?f.querySelector('figcaption').textContent.length:0, img:f?f.querySelector('img').naturalWidth:0};}")
    check('desktop: the technology card carries a captioned picture', r7['pic'] and r7['cap'] > 20, r7)
    find_window(p)
    keep_place(p)
    check('desktop: no page errors', not errors, errors[:3])
    b.close()


def wait(p, js, timeout=30000):
    try: p.wait_for_function(js, timeout=timeout); return True
    except Exception: return False


BAR = "()=>{const b=document.getElementById('findbar'), r=b.getBoundingClientRect(), l=document.getElementById('findlist'); return {open:!b.hidden, x:Math.round(r.left), y:Math.round(r.top), r:Math.round(r.right), b:Math.round(r.bottom), h:Math.round(r.height), vw:innerWidth, vh:innerHeight, list:getComputedStyle(l).display==='none'?0:Math.round(l.getBoundingClientRect().height), opts:getComputedStyle(b.querySelector('.findopts')).display, glyph:document.getElementById('findfold').textContent, exp:document.getElementById('findfold').getAttribute('aria-expanded'), q:document.getElementById('findq').value, count:document.getElementById('findcount').textContent};}"


def find_window(p):
    """The find window moves, folds and is sticky (the editor, 29 Sep 2026)."""
    p.evaluate("()=>{const c=document.querySelector('#insp [data-close]'); if(c)c.click(); window.scrollTo(0,0); window.__find.open({clientX:300,clientY:200});}"); time.sleep(0.3)
    g = p.evaluate("()=>{const g=document.querySelector('#findbar .fgrip').getBoundingClientRect(); return {x:g.left+g.width/2, y:g.top+g.height/2, cur:getComputedStyle(document.querySelector('#findbar .fgrip')).cursor};}")
    a0 = p.evaluate(BAR)
    p.mouse.move(g['x'], g['y']); p.mouse.down(); p.mouse.move(g['x'] + 110, g['y'] + 80, steps=4); p.mouse.move(g['x'] + 220, g['y'] + 160, steps=4); p.mouse.up(); time.sleep(0.2)
    a1 = p.evaluate(BAR)
    check('desktop: dragging the grip by (+220, +160) moves the find window by that much and keeps it inside the viewport (grab cursor)', abs(a1['x'] - a0['x'] - 220) <= 3 and abs(a1['y'] - a0['y'] - 160) <= 3 and a1['x'] >= 0 and a1['y'] >= 0 and a1['r'] <= a1['vw'] and a1['b'] <= a1['vh'] and g['cur'] == 'grab', (a0, a1, g['cur']))
    c = p.evaluate("()=>{const r=document.getElementById('findcount').getBoundingClientRect(); return {x:r.left+r.width/2, y:r.top+r.height/2};}")   # a bare part of the row drags too
    p.mouse.move(c['x'], c['y']); p.mouse.down(); p.mouse.move(c['x'] + 1500, c['y'] + 1500, steps=6); p.mouse.up(); time.sleep(0.2)
    a2 = p.evaluate(BAR)
    check('desktop: dragged by a bare part of the top row far past the corner, the window stops inside the viewport', a2['x'] > a1['x'] and a2['y'] > a1['y'] and a2['r'] <= a2['vw'] - 4 and a2['b'] <= a2['vh'] - 4, (a1, a2))
    p.evaluate("()=>window.__find.open({clientX:424,clientY:136})"); time.sleep(0.2)   # back to (400, 150)
    # fold: one line; unfold: as it was
    p.evaluate("()=>window.__find.search('threshold',{scope:'this',cs:false,whole:false})"); time.sleep(0.3)
    b0 = p.evaluate(BAR); p.click('#findfold'); time.sleep(0.2); b1 = p.evaluate(BAR); p.click('#findfold'); time.sleep(0.2); b2 = p.evaluate(BAR)
    check('desktop: ▾ folds the find window to its one row (< 60 px; the options, the location line and the list hidden; ▸) and ▸ restores it', b0['list'] > 50 and b1['h'] < 60 and b1['list'] == 0 and b1['opts'] == 'none' and b1['glyph'] == '▸' and b1['exp'] == 'false' and abs(b2['h'] - b0['h']) <= 2 and b2['list'] > 50 and b2['glyph'] == '▾' and (b1['x'], b1['y']) == (b0['x'], b0['y']), (b0, b1, b2))
    # sticky: a reload reopens it where it was, with its query, and searches
    p.click('#findq'); p.keyboard.press('Control+A'); p.keyboard.type('erasure'); time.sleep(0.8)
    c0 = p.evaluate(BAR)
    p.reload(wait_until='load', timeout=120000); p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
    ok = wait(p, r"()=>{const m=/\/ (\d+)/.exec(document.getElementById('findcount').textContent); return !!m&&+m[1]>0&&!document.getElementById('findlist').hidden;}")
    c1 = p.evaluate(BAR)
    check('desktop: the find window is sticky — after a reload it is open at the same place with the same query, and the search has run (a hit count, the list)', ok and c1['open'] and (c1['x'], c1['y']) == (c0['x'], c0['y']) and c1['q'] == 'erasure' and c1['list'] > 50, (c0, c1))
    wait(p, "!document.documentElement.classList.contains('lang-loading') && window.__langLoaded('ru')", 60000)


P4 = """(L)=>{const c=document.querySelector('.secbody[data-sec="'+L+'-s5"]'); const p=c&&c.querySelectorAll('p')[3]; if(!p||!p.getClientRects().length) return null; const r=p.getBoundingClientRect(); return {top:Math.round(r.top), h:Math.round(r.height), text:p.textContent.slice(0,30)};}"""
VIEW = "()=>{const w=document.getElementById('mapwrap'), m=window.__mapContext(), i=document.getElementById('insp'); return {zoom:document.getElementById('zoomlvl').value, sl:Math.round(w.scrollLeft), st:Math.round(w.scrollTop), focus:m.focus, isolate:m.isolate, machine:m.machine, brief:!document.getElementById('brief-transmon').hidden, card:!i.hidden, cardFrac:Math.round(1000*i.scrollTop/Math.max(1,i.scrollHeight))/1000};}"


def switch(p, L):
    p.evaluate("(L)=>window.__setLang(L)", L); wait(p, "!document.documentElement.classList.contains('lang-loading')", 60000); time.sleep(0.4)


def keep_place(p):
    """A language switch keeps the reader's place and leaves the rest of the view as it was (the editor, 29 Sep 2026)."""
    p.evaluate("()=>{window.__find.close(); const p=document.querySelectorAll('.secbody[data-sec=\"en-s5\"] p')[3]; window.scrollTo(0, p.getBoundingClientRect().top + scrollY - 30);}"); time.sleep(0.4)
    d0 = p.evaluate(P4, 'en'); switch(p, 'ru'); d1 = p.evaluate(P4, 'ru'); switch(p, 'en'); d2 = p.evaluate(P4, 'en')
    check('desktop: the 4th paragraph of §5 at the top (30 px down) → in Russian its twin is within 40 px of the top, and back in English the paragraph again', d0 and d1 and d2 and abs(d0['top'] - 30) <= 2 and abs(d1['top']) <= 40 and abs(d2['top']) <= 40, (d0, d1, d2))
    # a card scrolled 40 % inside, an isolated architecture, an open brief, a zoomed map: the switch keeps them all
    p.evaluate("()=>{const a=window.__GRAPH.paths.find(x=>Object.values(x.slots).flat().includes('transmon')); window.__isolatePath(a.id); window.__selectNode('transmon'); window.__openBrief('transmon',true); document.getElementById('zoom-in').click();}"); time.sleep(0.6)
    p.evaluate("()=>{const i=document.getElementById('insp'); i.scrollTop=0.4*i.scrollHeight; const w=document.getElementById('mapwrap'); w.scrollLeft=120; w.scrollTop=60;}"); time.sleep(0.3)
    v0 = p.evaluate(VIEW); switch(p, 'ru'); v1 = p.evaluate(VIEW)
    check('desktop: with a technology card open and scrolled 40 % inside, a language switch keeps the card open at 40 % ± 10 %', v0['card'] and abs(v0['cardFrac'] - 0.4) <= 0.01 and v1['card'] and abs(v1['cardFrac'] - 0.4) <= 0.04, (v0['cardFrac'], v1['cardFrac']))
    same = {k: (v0[k], v1[k]) for k in v0 if k != 'cardFrac' and v0[k] != v1[k]}
    check('desktop: … and leaves the rest as it was — the selection, the isolated architecture, the open brief, the map\'s zoom and scroll', not same and v0['isolate'] and v0['brief'], (same, v0))
    # a chosen machine whose card was closed stays closed across a switch
    switch(p, 'en'); p.evaluate("()=>{document.getElementById('tg-reset').click(); window.__showMachine('google-willow');}"); time.sleep(0.4)
    p.evaluate("()=>{const c=document.querySelector('#insp [data-mclose]')&&document.querySelector('#insp [data-close]'); if(c)c.click();}"); time.sleep(0.2)
    m0 = p.evaluate("()=>({card:!document.getElementById('insp').hidden, machine:window.__mapContext().machine})")
    switch(p, 'ru'); m1 = p.evaluate("()=>({card:!document.getElementById('insp').hidden, machine:window.__mapContext().machine})"); switch(p, 'en')
    check('desktop: a closed machine card stays closed across a language switch (the machine stays chosen)', m0 == {'card': False, 'machine': 'google-willow'} and m1 == m0, (m0, m1))


HE_PAGE = os.path.join(ROOT, 'dist', 'he', 'index.html')


def hebrew(pw, shots):
    """The Hebrew page (29 Sep 2026): right to left on a phone and on a desktop — nothing wider than the screen (at the top, with a brief
    open, in each language), the phone bar's three-language switch fully on screen, the zoom control and the contents on the start side."""
    for W, H, mobile in ((390, 844, True), (1280, 860, False)):
        b = pw.chromium.launch(); ctx = b.new_context(viewport={'width': W, 'height': H}, device_scale_factor=2 if mobile else 1, has_touch=mobile, is_mobile=mobile)
        p = ctx.new_page(); errors = []
        p.on('pageerror', lambda e: errors.append(str(e)))
        p.goto('file://' + HE_PAGE, wait_until='load', timeout=120000)
        p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
        p.wait_for_function("!document.documentElement.classList.contains('lang-loading') && window.__langLoaded('en') && window.__langLoaded('ru')", timeout=60000); time.sleep(0.6)
        tag = 'phone' if mobile else 'desktop'
        print('Hebrew page, %s %d×%d' % (tag, W, H))
        r = p.evaluate("()=>({dir:document.documentElement.dir, lang:document.documentElement.lang})")
        check('HE %s: <html dir="rtl" lang="he">' % tag, r == {'dir': 'rtl', 'lang': 'he'}, r)
        o1 = p.evaluate(OVER)
        check('HE %s: nothing wider than the screen at the top' % tag, o1['sw'] <= o1['vw'] + 1 and not o1['bad'], o1)
        if mobile:
            mb = p.evaluate("()=>{const s=document.querySelector('.mobilebar .mb-seg'), r=s.getBoundingClientRect(); return {left:Math.round(r.left), right:Math.round(r.right), vw:innerWidth, names:[...s.querySelectorAll('[data-setlang]')].map(b=>b.textContent.trim())};}")
            check('HE phone: the page bar\'s switch — English · Русский · עברית — is fully on screen', mb['left'] >= 0 and mb['right'] <= mb['vw'] and sorted(mb['names']) == ['English', 'Русский', 'עברית'], mb)
            z = p.evaluate("()=>{const w=document.getElementById('mapwrap').getBoundingClientRect(), c=document.querySelector('#mapwrap .zoomctl').getBoundingClientRect(); return {left:Math.round(c.left-w.left), right:Math.round(w.right-c.right)};}")
            check('HE phone: the zoom control sits in the scroller\'s top-left corner (mirrored)', 0 <= z['left'] < 30 and z['right'] > 60, z)
        else:
            t = p.evaluate("()=>{const t=document.querySelector('nav.toc').getBoundingClientRect(), m=document.querySelector('main').getBoundingClientRect(), f=document.getElementById('floatlang'); return {toc:Math.round(t.left), main:Math.round(m.right)};}")
            check('HE desktop: the contents column is on the right', t['toc'] >= t['main'], t)
        if shots: p.screenshot(path=os.path.join(shots, 'he_%s_top.png' % tag))
        p.evaluate("()=>window.__openBrief('transmon')"); time.sleep(0.6)
        o2 = p.evaluate(OVER)
        check('HE %s: nothing wider than the screen with a brief open' % tag, o2['sw'] <= o2['vw'] + 1 and not o2['bad'], o2)
        if shots: p.screenshot(path=os.path.join(shots, 'he_%s_brief.png' % tag))
        p.evaluate("()=>window.__closeBrief(false)")
        for L in ('en', 'ru', 'he'):
            p.evaluate("(L)=>{window.__setLang(L); window.scrollTo(0,0);}", L); time.sleep(0.6)
            o3 = p.evaluate(OVER)
            check('HE %s, switched to %s: nothing wider than the screen' % (tag, L), o3['sw'] <= o3['vw'] + 1 and not o3['bad'], o3)
        check('HE %s: no page errors' % tag, not errors, errors[:3])
        b.close()


OVER = """()=>{const vw=innerWidth; const out=[]; const bad=[]; const inScroller=el=>{ for(let p=el.parentElement;p;p=p.parentElement){ const o=getComputedStyle(p).overflowX; if(o==='auto'||o==='scroll'||o==='hidden')return true; } return false; };
      document.querySelectorAll('body *').forEach(el=>{ if(bad.length>12)return; const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden'||cs.position==='fixed')return; const r=el.getBoundingClientRect(); if(!r.width)return; if((r.right>vw+2||r.left<-2)&&!inScroller(el)) bad.push(el.tagName+'.'+String(el.className).slice(0,40)+' left='+Math.round(r.left)+' right='+Math.round(r.right)); });
      return {sw:document.documentElement.scrollWidth, vw:vw, bad:bad};}"""   # both edges: a right-to-left page overflows on the left


def main():
    a = argparse.ArgumentParser(); a.add_argument('--shots', default=None); o = a.parse_args()
    if o.shots: os.makedirs(o.shots, exist_ok=True)
    with sync_playwright() as pw:
        phone(pw, o.shots); tablet(pw, o.shots); desktop(pw, o.shots); hebrew(pw, o.shots)
    print('RESULT: ' + ('PASS' if not FAILS else 'FAIL ' + str(FAILS)))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
