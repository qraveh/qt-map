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
    check('desktop: no page errors', not errors, errors[:3])
    b.close()


def main():
    a = argparse.ArgumentParser(); a.add_argument('--shots', default=None); o = a.parse_args()
    if o.shots: os.makedirs(o.shots, exist_ok=True)
    with sync_playwright() as pw:
        phone(pw, o.shots); tablet(pw, o.shots); desktop(pw, o.shots)
    print('RESULT: ' + ('PASS' if not FAILS else 'FAIL ' + str(FAILS)))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
