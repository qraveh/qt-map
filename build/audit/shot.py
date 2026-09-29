#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Screenshots of the built page at chosen viewports (a look, not a check).

    python3 build/audit/shot.py --out DIR [--w 390 --h 844] [--touch] [--scroll-to '#mapbody'] [--js 'expr'] [--full] [--lang ru]
"""
import argparse, os, sys, time
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--out', required=True); a.add_argument('--w', type=int, default=390); a.add_argument('--h', type=int, default=844)
    a.add_argument('--touch', action='store_true'); a.add_argument('--scroll-to', default=None); a.add_argument('--js', action='append', default=[])
    a.add_argument('--full', action='store_true'); a.add_argument('--lang', default='en'); a.add_argument('--name', default='shot'); a.add_argument('--wait', type=int, default=800)
    o = a.parse_args()
    page_path = os.path.join(ROOT, 'dist', '' if o.lang == 'en' else o.lang, 'index.html')   # any language folder (29 Sep 2026)
    os.makedirs(o.out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={'width': o.w, 'height': o.h}, device_scale_factor=2, has_touch=o.touch, is_mobile=o.touch)
        pg = ctx.new_page()
        pg.goto('file://' + page_path, wait_until='load', timeout=120000)
        pg.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0", timeout=60000)
        time.sleep(0.6)
        if o.scroll_to:
            pg.evaluate("sel=>{const e=document.querySelector(sel); if(e) e.scrollIntoView({block:'start'});}", o.scroll_to)
        for js in o.js:
            pg.evaluate(js); time.sleep(0.3)
        time.sleep(o.wait / 1000)
        out = os.path.join(o.out, o.name + '.png')
        pg.screenshot(path=out, full_page=o.full)
        print(out, pg.evaluate("()=>({w:innerWidth,h:innerHeight,sy:scrollY,zoom:(document.getElementById('zoomlvl')||{}).value})"))
        b.close()


if __name__ == '__main__':
    main()
