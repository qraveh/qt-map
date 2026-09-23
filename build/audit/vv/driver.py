"""Playwright driver for the built Map page (SPEC step D.2). Implementation-side half; see DRIVER.md."""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAGE = ROOT / 'dist' / 'Quantum-Technology-Map-2026.09.html'
TOGGLE_ID = {'requires': 'tg-req', 'alternatives': 'tg-rep', 'conflicts': 'tg-conf'}
EDGE_TYPE = {'requires': 'requires', 'replaces': 'alternatives', 'conflicts': 'conflicts'}  # page/graph type -> toggle name

_READ_JS = r"""() => {
  const wrap=document.getElementById('mapwrap');
  const st=[...wrap.querySelectorAll('g.station')];
  const idOf=g=>g.querySelector('text.id').textContent;
  const stations=st.filter(g=>!g.classList.contains('dim')).map(idOf);
  const lines=[...wrap.querySelectorAll('path.pathline')].filter(p=>!p.classList.contains('dim')).map(p=>p.dataset.path);
  const edges=[...wrap.querySelectorAll('g.edge')].map(g=>{const d=g.__data__; return [d.src,d.dst,d.type];});
  const legend={glyphs:[...document.querySelectorAll('#glyphlegend [data-mark]')].map(e=>({key:e.dataset.mark,text:e.innerText.trim()})),
    lens:[...document.querySelectorAll('#lenslegend [data-lv]')].map(b=>({key:b.dataset.lv,pressed:b.getAttribute('aria-pressed')==='true',
      count:b.querySelector('.cnt')?parseInt(b.querySelector('.cnt').textContent,10):null,text:b.innerText.trim()}))};
  const altuse=st.filter(g=>g.classList.contains('altuse')).map(idOf);
  const insp=document.getElementById('insp');
  // the machine card (C2) is the inspector content with the "clear machine" button; station/path cards have none
  const machine_card=(!insp.hidden&&insp.querySelector('[data-mclose]'))?insp.innerText.trim():'';
  const vw=window.innerWidth, vh=window.innerHeight; const over=[];
  document.querySelectorAll('#mapbar, #mapbar *, #mapwrap, #insp:not([hidden])').forEach(e=>{ const r=e.getBoundingClientRect();
    if(r.width===0&&r.height===0)return; if(getComputedStyle(e).display==='none')return;
    for(let a=e.parentElement;a&&a!==document.body;a=a.parentElement){ const ox=getComputedStyle(a).overflowX; if(ox!=='visible'&&ox!=='clip'){ const ar=a.getBoundingClientRect(); if(ar.left>=-1&&ar.right<=vw+1)return; } }
    if(r.left<-1||r.right>vw+1) over.push((e.id||e.className&&e.className.baseVal===undefined&&e.className||e.tagName)+''); });
  return {stations, lines, edges, legend, altuse, machine_card,
    machine_select: (document.getElementById('machine')||{value:null}).value||null,
    path_card: insp.hidden?'':insp.innerText.trim(),
    selection_summary: document.getElementById('barsum').hidden?'':(document.getElementById('barsum').innerText||'').trim(),
    bar_collapsed: document.getElementById('mapbar').classList.contains('collapsed'),
    overflow_elems: over.slice(0,20),
    doc_hscroll: document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
    zoom: (document.getElementById('zoomlvl')||{}).value};
}"""


class MapPage:
    def __init__(self, headless=True):
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=headless)
        self.page = None
        self._errors = []
        self._state = None

    # ---------- lifecycle
    def open(self, viewport=(1600, 1000), theme=None, lang=None):
        ctx_args = {'viewport': {'width': viewport[0], 'height': viewport[1]}}
        if theme in ('light', 'dark'):
            ctx_args['color_scheme'] = theme
        self._ctx = self._browser.new_context(**ctx_args)
        self.page = p = self._ctx.new_page()
        p.on('console', lambda m: m.type == 'error' and self._errors.append(m.text))
        p.on('pageerror', lambda e: self._errors.append('pageerror: ' + str(e)))
        # the sandbox has no outbound network for Chromium: external requests (web fonts) are answered empty so that
        # a missing network is not reported as a page console error; they are logged in self.external
        self.external = []
        def _ext(route):
            self.external.append(route.request.url)
            route.fulfill(status=200, body='', content_type='text/css' if 'css' in route.request.url else 'application/octet-stream')
        p.route(lambda url: not url.startswith('file:') and not url.startswith('data:'), _ext)
        p.goto(PAGE.as_uri(), wait_until='load', timeout=120000)
        p.wait_for_function("document.querySelectorAll('#mapwrap g.station').length>0 && document.querySelectorAll('#pathchips .chip').length>0", timeout=60000)
        # the map may start collapsed (stored preference) — expand it
        if p.locator('#mapbody').count() and p.locator('#mapbody').evaluate('e=>e.hidden'):
            p.locator('[data-mapcollapse]').first.click()
            p.wait_for_function("!document.getElementById('mapbody').hidden")
        # the controls bar starts collapsed (23 Sep 2026) — the driver works with it open
        if p.evaluate("()=>document.getElementById('mapbar').classList.contains('collapsed')"):
            p.locator('#bartog').click()
            p.wait_for_function("!document.getElementById('mapbar').classList.contains('collapsed')")
        self._state = {'lens': 'family', 'values': set(), 'isolate': None, 'focus': None, 'machine': None,
                       'toggles': {'requires': False, 'alternatives': False, 'conflicts': False}}
        if theme:
            self.set_theme(theme)
        if lang:
            self.set_lang(lang)
        return self

    def close(self):
        try:
            self._browser.close()
        finally:
            self._pw.stop()

    def errors(self):
        return list(self._errors)

    # ---------- helpers
    def _pressed(self, sel, val):
        self.page.wait_for_function("([s,v])=>{const e=document.querySelector(s); return e&&e.getAttribute('aria-pressed')===v;}", arg=[sel, val])

    # ---------- controls
    def set_lens(self, name):
        self.page.locator('#lens').select_option(name)
        self.page.wait_for_function("n=>document.getElementById('lens').value===n", arg=name)
        self._state['lens'] = name
        self._state['values'] = set()

    def select_value(self, value, multi=False):
        value = str(value)
        btn = self.page.locator(f'#lenslegend [data-lv="{value}"]')
        before = btn.get_attribute('aria-pressed')
        btn.click(modifiers=['Control'] if multi else [])
        s = self._state['values']
        if multi:
            s.symmetric_difference_update({value})
        else:
            self._state['values'] = set() if (s == {value}) else {value}
        want = 'true' if value in self._state['values'] else 'false'
        # the legend is re-rendered on every click — wait for the new button's pressed state
        self._pressed(f'#lenslegend [data-lv="{value}"]', want)
        return before

    def select_mark(self, mark, multi=False):
        """Glyph-legend mark (hub/offd/empty): switches the lens to 'marks'."""
        if self._state['lens'] != 'marks':
            self._state['lens'] = 'marks'; self._state['values'] = set()
        self.page.locator(f'#glyphlegend [data-mark="{mark}"]').click(modifiers=['Control'] if multi else [])
        s = self._state['values']
        if multi:
            s.symmetric_difference_update({mark})
        else:
            self._state['values'] = set() if s == {mark} else {mark}
        self._pressed(f'#lenslegend [data-lv="{mark}"]', 'true' if mark in self._state['values'] else 'false')

    def clear_values(self):
        clr = self.page.locator('#lenslegend [data-lv=""]')
        if clr.count():
            clr.click()
            self.page.wait_for_function("!document.querySelector('#lenslegend [data-lv=\"\"]')")
        self._state['values'] = set()

    def toggle(self, edge_type, on: bool):
        tid = TOGGLE_ID[edge_type]
        cur = self.page.locator('#' + tid).get_attribute('aria-pressed') == 'true'
        if cur != on:
            self.page.locator('#' + tid).click()
            self._pressed('#' + tid, 'true' if on else 'false')
        self._state['toggles'][edge_type] = on

    def isolate(self, path_id):
        sel = f'#pathchips [data-chip-path="{path_id}"]'
        if self.page.locator(sel).get_attribute('aria-pressed') != 'true':
            self.page.locator(sel).click()
            self._pressed(sel, 'true')
        self._state['isolate'] = path_id   # C2: isolating no longer clears the focused station (the terms narrow each other)

    def clear_isolate(self):
        pid = self._state['isolate'] or self.page.evaluate("()=>{const c=document.querySelector('#pathchips .chip[aria-pressed=\"true\"]'); return c?c.dataset.chipPath:null;}")
        if pid:
            sel = f'#pathchips [data-chip-path="{pid}"]'
            self.page.locator(sel).click()
            self._pressed(sel, 'false')
        self._state['isolate'] = None

    def focus(self, node_id):
        loc = self.page.locator('#mapwrap g.station').filter(has=self.page.locator(f'xpath=./*[local-name()="text" and contains(concat(" ",@class," ")," id ") and text()="{node_id}"]'))
        if loc.evaluate("g=>g.classList.contains('sel')"):
            self._state['focus'] = node_id
            return
        loc.scroll_into_view_if_needed()
        loc.locator('rect.box').click(force=False)
        self.page.wait_for_function("id=>[...document.querySelectorAll('#mapwrap g.station.sel')].some(g=>g.querySelector('text.id').textContent===id)", arg=node_id)
        self._state['focus'] = node_id

    def clear_focus(self):
        # Escape is the page's own keyboard shortcut for deselecting (svg background click also works)
        self.page.keyboard.press('Escape')
        self.page.wait_for_function("!document.querySelector('#mapwrap g.station.sel')")
        self._state['focus'] = None

    def select_machine(self, machine_id):
        """C2 Machine selector: `<select id="machine">` in the map bar (option values = machine ids, optgroups per family).
        None (or '') selects the empty option = no machine. The page applies it on the select's change event."""
        mid = machine_id or ''
        sel = self.page.locator('#machine')
        if sel.evaluate('e=>e.value') != mid:
            sel.select_option(mid)
        self.page.wait_for_function("v=>document.getElementById('machine').value===v", arg=mid)
        self._state['machine'] = mid or None

    def clear_machine(self):
        self.select_machine(None)

    def reset(self):
        self.page.locator('#tg-reset').click()
        self.page.wait_for_function("document.getElementById('lens').value==='family' && !document.querySelector('#mapwrap g.station.sel') && !document.querySelector('#pathchips .chip[aria-pressed=\"true\"]') && !((document.getElementById('machine')||{}).value)")
        self._state = {'lens': 'family', 'values': set(), 'isolate': None, 'focus': None, 'machine': None,
                       'toggles': {'requires': False, 'alternatives': False, 'conflicts': False}}

    def zoom(self, percent):
        zl = self.page.locator('#zoomlvl')
        zl.click()
        zl.fill(str(int(percent)))
        zl.press('Enter')
        # the percentage is relative to the fitted width (23 Sep 2026); the scale factor is clamped to [0.2, 2.5], so the value
        # shown is the clamped one
        self.page.wait_for_function("p=>{const f=window.__fitScale?window.__fitScale():1; const z=Math.max(0.2,Math.min(2.5,p/100*f)); return document.getElementById('zoomlvl').value===Math.round(z/f*100)+'%';}", arg=int(percent))

    def _zoom_changed_after(self, sel):
        w0 = self.page.evaluate("()=>document.querySelector('#mapwrap svg').getAttribute('width')")
        self.page.locator(sel).click()
        # the fit may legitimately equal the current zoom; wait for layout to settle either way
        self.page.wait_for_function("()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>r(true))))")
        self.wait_scroll_settled()
        return w0

    def wait_scroll_settled(self, max_ms=1000):
        """The page scrolls (window and #mapwrap, sometimes smoothly) to align the bar when fitting: poll the scroll
        positions until unchanged for 2 consecutive frames, at most max_ms."""
        self.page.evaluate("""max=>new Promise(res=>{ const w=document.getElementById('mapwrap');
          const pos=()=>[window.scrollX,window.scrollY,w?w.scrollLeft:0,w?w.scrollTop:0].join(',');
          const t0=performance.now(); let last=pos(), same=0;
          const step=()=>{ const p=pos(); same=(p===last)?same+1:0; last=p; if(same>=2||performance.now()-t0>max)res(same>=2); else requestAnimationFrame(step); };
          requestAnimationFrame(step); })""", max_ms)

    def fit_width(self):
        self._zoom_changed_after('#zoom-fit')

    def fit_height(self):
        self._zoom_changed_after('#zoom-fith')

    def set_theme(self, theme):
        # the page has no theme control; it follows prefers-color-scheme and honours <html data-theme>
        self.page.emulate_media(color_scheme=theme)
        self.page.evaluate("t=>document.documentElement.setAttribute('data-theme',t)", theme)
        self.page.wait_for_function("t=>document.documentElement.getAttribute('data-theme')===t", arg=theme)

    def set_lang(self, lang):
        b = self.page.locator(f'[data-setlang="{lang}"]').filter(visible=True).first
        b.click()
        self.page.wait_for_function("l=>document.getElementById('app').getAttribute('data-lang')===l", arg=lang)

    def set_viewport(self, w, h):
        self.page.set_viewport_size({'width': w, 'height': h})
        self.page.wait_for_function("([w,h])=>window.innerWidth===w&&window.innerHeight===h", arg=[w, h])

    def collapse_bar(self, collapsed: bool):
        cur = self.page.evaluate("()=>document.getElementById('mapbar').classList.contains('collapsed')")
        if cur != collapsed:
            self.page.locator('#bartog').click()
            self.page.wait_for_function("c=>document.getElementById('mapbar').classList.contains('collapsed')===c", arg=collapsed)

    # ---------- readers
    def read(self):
        r = self.page.evaluate(_READ_JS)
        r['stations'] = set(r['stations'])
        r['altuse'] = set(r['altuse'])
        r['lines'] = set(r['lines'])
        r['edges'] = {tuple(e) for e in r['edges']}
        r['edges_toggle_names'] = {(u, v, EDGE_TYPE.get(t, t)) for u, v, t in r['edges']}
        r['bbox_overflow'] = bool(r['overflow_elems']) or r['doc_hscroll']
        return r

    def table_rows(self):
        """§7.2 node table in the current language: visible rows in order. The table is static (no sort/filter UI)."""
        return self.page.evaluate(r"""()=>{
          const L=document.getElementById('app').getAttribute('data-lang')||'en';
          const h=[...document.querySelectorAll('h3')].find(x=>/^7\.2\s/.test(x.textContent.trim()) && x.id.startsWith(L+'-'));
          if(!h) return {rows:[],sort:null,filter:null,heading:null};
          let t=h.nextElementSibling; while(t&&!t.querySelector('table')&&t.tagName!=='TABLE') t=t.nextElementSibling;
          const tb=t.tagName==='TABLE'?t:t.querySelector('table');
          const rows=[...tb.querySelectorAll('tbody tr')].filter(r=>r.offsetParent!==null||getComputedStyle(r).display!=='none')
            .map(r=>({id:r.dataset.row, cells:[...r.cells].map(c=>c.innerText.trim())}));
          return {heading:h.textContent.trim(), header:[...tb.querySelectorAll('thead th')].map(x=>x.innerText.trim()), rows, sort:null, filter:null};
        }""")

    def state(self):
        s = self._state
        return {'lens': s['lens'], 'values': set(s['values']), 'toggles': dict(s['toggles']),
                'isolate': s['isolate'], 'focus': s['focus'], 'machine': s.get('machine')}

    def page_state(self):
        """Cross-check: the page's own control state read back from the DOM controls (not from JS internals)."""
        return self.page.evaluate("""()=>({lens:document.getElementById('lens').value,
          values:[...document.querySelectorAll('#lenslegend [data-lv][aria-pressed="true"]')].map(b=>b.dataset.lv),
          toggles:{requires:document.getElementById('tg-req').getAttribute('aria-pressed')==='true',
                   alternatives:document.getElementById('tg-rep').getAttribute('aria-pressed')==='true',
                   conflicts:document.getElementById('tg-conf').getAttribute('aria-pressed')==='true'},
          isolate:(document.querySelector('#pathchips .chip[aria-pressed="true"]')||{dataset:{}}).dataset.chipPath||null,
          focus:(()=>{const g=document.querySelector('#mapwrap g.station.sel'); return g?g.querySelector('text.id').textContent:null;})(),
          machine:(document.getElementById('machine')||{value:''}).value||null})""")
