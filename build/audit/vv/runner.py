from pathlib import Path
"""Differential / combinatorial / random runner (SPEC D.3-D.6). Compares the page (via driver.MapPage) with oracle.expected.

python3 runner.py <single|pairs|multi|machines|random|metamorphic|static|summary> [--n N] [--seed S] [--out results/] [--limit L]

--limit L (runner extra, for smoke runs): evenly spaced subset of L states of the suite's full state list.
Driver is NOT edited; runner overrides driver.PAGE to the frozen baseline and adds helpers (value mapping, transform read,
page_state->oracle state) locally.
"""
import argparse, collections, itertools, json, math, pathlib, random, re, sys, time, traceback

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oracle  # noqa: E402
import driver  # noqa: E402

import os as _os
driver.PAGE = Path(_os.environ['VV_PAGE']) if _os.environ.get('VV_PAGE') else HERE / 'baseline-8106b9e.html'   # target the frozen baseline (or VV_PAGE), not dist/
GRAPH = HERE.parents[2] / 'data' / 'graph.json'
TOG = oracle.TOGGLES
STEP_TIMEOUT_MS = 8000


# ---------------------------------------------------------------- value mapping (oracle value <-> page data-lv)
def page_key(lens, v):
    if lens == 'aff':
        return '%g' % float(v)
    if lens == 'time':
        return 'none' if v == oracle.NONE else str(int(v) + 9)   # page bins decades -9..-3 as 0..6
    if lens in ('destr', 'mid'):
        return {True: 'yes', False: 'no'}.get(v, 'none')
    return str(v)


def build_maps(model):
    fwd = {l: {v: page_key(l, v) for v in oracle.lens_values(model, l)} for l in oracle.LENSES}
    inv = {l: {k: v for v, k in d.items()} for l, d in fwd.items()}
    return fwd, inv


# ---------------------------------------------------------------- serialisation
def jv(v):
    return v if isinstance(v, (str, int, float, bool)) or v is None else str(v)


def ser_state(s):
    d = {'lens': s['lens'], 'values': sorted((jv(v) for v in s['values']), key=lambda x: (type(x).__name__, str(x))),
         'toggles': ''.join(t[0] for t in TOG if s['toggles'].get(t)) or '-', 'isolate': s['isolate'], 'focus': s['focus']}
    if s.get('machine'):   # C2: only when set, so keys of pre-C2 records stay identical (resumable suites)
        d['machine'] = s['machine']
    return d


def ostate(lens, values, toggles, isolate, focus, machine=None):
    return {'lens': lens, 'values': set(values), 'toggles': dict(toggles), 'isolate': isolate, 'focus': focus, 'machine': machine}


def skey(s):
    return json.dumps(ser_state(s), sort_keys=True)


def diff(exp, act):
    out = {}
    for k in ('stations', 'lines', 'edges'):
        e, a = set(exp[k]), set(act[k])
        if e != a:
            out[k] = {'missing': sorted(map(list, e - a) if k == 'edges' else e - a),
                      'extra': sorted(map(list, a - e) if k == 'edges' else a - e)}
    return out


def sizes(r):
    return {k: len(r[k]) for k in ('stations', 'lines', 'edges')}


class Out:
    def __init__(self, outdir, suite, total):
        self.dir = pathlib.Path(outdir); self.dir.mkdir(parents=True, exist_ok=True)
        self.path = self.dir / f'{suite}.jsonl'
        self.suite, self.total = suite, total
        self.done_keys = set(); self.dis = 0; self.done = 0
        if self.path.exists():
            for line in self.path.read_text().splitlines():
                try:
                    o = json.loads(line)
                except ValueError:
                    continue
                self.done_keys.add(o.get('key')); self.done += 1; self.dis += 0 if o.get('agree') else 1
        self.fh = open(self.path, 'a', buffering=1)
        self.t0 = time.time(); self.new = 0
        self.log = open(self.dir / 'progress.log', 'a', buffering=1)

    def write(self, obj):
        self.fh.write(json.dumps(obj, sort_keys=True, default=jv) + '\n')
        self.done += 1; self.new += 1
        if not obj.get('agree'):
            self.dis += 1
        if self.done % 25 == 0:
            self.log.write(f'SUITE {self.suite} {self.done}/{self.total} disagreements={self.dis}\n')

    def finish(self):
        secs = time.time() - self.t0
        self.log.write(f'SUITE {self.suite} DONE {self.done}/{self.total} disagreements={self.dis} seconds={secs:.1f}\n')
        per = secs / self.new if self.new else 0
        print(f'{self.suite}: done={self.done}/{self.total} new={self.new} disagreements={self.dis} seconds={secs:.1f} s/state={per:.3f}')
        self.fh.close(); self.log.close()


# ---------------------------------------------------------------- page helpers (not in driver.py)
def open_page(viewport=(1600, 1000)):
    m = driver.MapPage().open(viewport=viewport)
    m.page.set_default_timeout(STEP_TIMEOUT_MS)
    return m


def apply_state(m, s, fwd):
    """reset(), then the actions for oracle state s. Returns list of unmappable values (page has no such button)."""
    m.reset()
    bad = []
    keys = []
    for v in sorted(s['values'], key=oracle._sortkey):
        k = fwd[s['lens']].get(v)
        if k is None or not m.page.locator(f'#lenslegend [data-lv="{k}"]').count() and s['lens'] == m.state()['lens']:
            pass
        keys.append((v, k))
    if s['lens'] and (s['lens'] != 'family' or s['values']):
        m.set_lens(s['lens'])
    for i, (v, k) in enumerate(keys):
        if m.page.locator(f'#lenslegend [data-lv="{k}"]').count() == 0:
            bad.append(jv(v)); continue
        m.select_value(k, multi=bool(m.state()['values']))
    for t in TOG:
        if s['toggles'].get(t):
            m.toggle(t, True)
    if s['isolate']:
        m.isolate(s['isolate'])
    if s.get('machine'):   # C2: after isolate (the page shows the card of the later selection), before focus (station card wins)
        m.select_machine(s['machine'])
    if s['focus']:
        m.focus(s['focus'])
    return bad


def page_to_oracle(ps, inv):
    lens = ps['lens']
    vals = set()
    unm = []
    for k in ps['values']:
        if k in inv.get(lens, {}):
            vals.add(inv[lens][k])
        else:
            unm.append(k)
    return ostate(lens, vals, ps['toggles'], ps['isolate'], ps['focus'], ps.get('machine')), unm


def transform(m):
    return m.page.evaluate("""()=>{const w=document.getElementById('mapwrap'), s=w.querySelector('svg');
      return {w:s.getAttribute('width'),h:s.getAttribute('height'),vb:s.getAttribute('viewBox'),
              tr:(s.querySelector('g')||{getAttribute:()=>null}).getAttribute('transform'),
              sl:Math.round(w.scrollLeft),st:Math.round(w.scrollTop),z:(document.getElementById('zoomlvl')||{}).value};}""")


def compare_record(model, state, act, key, extra=None):
    exp = oracle.expected(model, state)
    d = diff(exp, act)
    rec = {'key': key, 'state': ser_state(state), 'expected': sizes(exp), 'actual': sizes(act), 'agree': not d}
    if d:
        rec['diff'] = d
    if extra:
        rec.update(extra)
        if extra.get('unmappable'):
            rec['agree'] = False
    return rec


def subset(items, limit):
    if not limit or limit >= len(items):
        return items
    step = len(items) / limit
    return [items[int(i * step)] for i in range(limit)]


# ---------------------------------------------------------------- differential suites
def st(lens='family', values=(), toggles=(), isolate=None, focus=None, machine=None):
    s = oracle.default_state()
    s['lens'], s['values'] = lens, set(values)
    for t in toggles:
        s['toggles'][t] = True
    s['isolate'], s['focus'], s['machine'] = isolate, focus, machine
    return s


def states_single(model, a):
    return list(oracle.all_single_states(model))


def states_pairs(model, a):
    rng = random.Random(a.seed)
    lv = [(l, v) for l in oracle.LENSES for v in oracle.lens_values(model, l)]
    out = []
    out += [st(l, [v], [t]) for (l, v) in lv for t in TOG]
    out += [st(l, [v], isolate=p) for (l, v) in lv for p in model.path_ids]
    out += [st(toggles=[t], isolate=p) for t in TOG for p in model.path_ids]
    out += [st(isolate=p, focus=f) for p in model.path_ids for f in model.station_ids]
    allf = [(l, v, f) for (l, v) in lv for f in model.station_ids]
    out += [st(l, [v], focus=f) for (l, v, f) in rng.sample(allf, min(a.n or 300, len(allf)))]
    combos = [tuple(t for t, on in zip(TOG, bits) if on) for bits in itertools.product([0, 1], repeat=3)]
    # 17 Sep: the reading-marks lens is gone (RULES.md adjudication 10); the toggle-combination x isolate states use the status lens instead
    out += [st('status', [v], c, isolate=p) for c in combos for p in model.path_ids for v in oracle.lens_values(model, 'status')]
    seen, uniq = set(), []
    for s in out:
        k = skey(s)
        if k not in seen:
            seen.add(k); uniq.append(s)
    return uniq


def states_multi(model, a):
    out = []
    for l in oracle.LENSES:
        vals = oracle.lens_values(model, l)
        for k in (2, 3):
            for c in itertools.combinations(vals, k):
                out.append(st(l, c))
                out.append(st(l, c, TOG))
    return out


def states_machines(model, a):
    """C2 `machines` suite: every machine alone; x each toggle on; x isolate = own path and one other path (seeded);
    60 sampled machine x lens-value pairs and 60 sampled machine x focus pairs (seeded)."""
    rng = random.Random(a.seed)
    mids = list(model.machine_ids)
    out = [st(machine=mid) for mid in mids]
    out += [st(toggles=[t], machine=mid) for mid in mids for t in TOG]
    out += [st(isolate=model.machines[mid].path, machine=mid) for mid in mids]
    out += [st(isolate=rng.choice([p for p in model.path_ids if p != model.machines[mid].path]), machine=mid) for mid in mids]
    lv = [(l, v) for l in oracle.LENSES for v in oracle.lens_values(model, l)]
    out += [st(l, [v], machine=mid) for (mid, (l, v)) in zip(rng.sample(mids * ((60 // len(mids)) + 1), 60) if mids else [],
                                                            rng.sample(lv, min(60, len(lv))))] if mids else []
    out += [st(focus=f, machine=mid) for (mid, f) in zip(rng.sample(mids * ((60 // len(mids)) + 1), 60) if mids else [],
                                                         rng.sample(model.station_ids * ((60 // len(model.station_ids)) + 1), 60))] if mids else []
    seen, uniq = set(), []
    for s in out:
        k = skey(s)
        if k not in seen:
            seen.add(k); uniq.append(s)
    return uniq


def machine_checks(m, model, s, act):
    """Extra assertions of the machines suite (C2 brief §3). Returns the list of failed checks (empty = pass)."""
    fails = []
    mach = model.machines[s['machine']]
    # ADJ-12: a focused station off the machine's path (or an isolate of another path applied before the machine) releases the machine;
    # then the page must show no machine at all (selector empty, no machine card, no altuse) and the other checks do not apply
    iso_e, mid_e, foc_e = oracle.effective(model, s)
    if mid_e is None:
        ps = m.page_state()
        if ps.get('machine') or act['machine_card'] or act['altuse']:
            fails.append({'check': 'released-machine-still-shown', 'machine_select': ps.get('machine'), 'card': bool(act['machine_card']), 'altuse': sorted(act['altuse'])[:5]})
        m.reset(); r = m.read()
        if r['machine_select'] or m.page_state()['machine']:
            fails.append({'check': 'reset-keeps-machine-select', 'value': r['machine_select']})
        return fails
    # the machine card is shown unless a station is focused (then the station card wins)
    if s['focus']:
        if act['machine_card']:
            fails.append({'check': 'machine-card-shown-despite-focus'})
    elif not act['machine_card']:
        fails.append({'check': 'machine-card-missing', 'path_card': act['path_card'][:120]})
    elif mach.name not in act['machine_card']:
        fails.append({'check': 'machine-card-wrong-name', 'card': act['machine_card'][:120]})
    # the bar summary (only rendered while the bar is collapsed) names the machine
    m.collapse_bar(True)
    summ = m.read()['selection_summary']
    m.collapse_bar(False)
    if mach.name not in summ:
        fails.append({'check': 'bar-summary-missing-machine', 'summary': summ[:200]})
    # altuse (dashed = used only as an alternate) only on lit stations, and only on the machine's alternate-only stations
    if not act['altuse'] <= act['stations']:
        fails.append({'check': 'altuse-not-subset-of-lit', 'extra': sorted(act['altuse'] - act['stations'])})
    if not act['altuse'] <= set(mach.alt):
        fails.append({'check': 'altuse-not-machine-alternate', 'extra': sorted(act['altuse'] - set(mach.alt))})
    # reset clears the machine: select empty, no altuse
    m.reset()
    r = m.read()
    if r['machine_select'] or m.page_state()['machine']:
        fails.append({'check': 'reset-keeps-machine-select', 'value': r['machine_select']})
    if r['altuse']:
        fails.append({'check': 'reset-keeps-altuse', 'altuse': sorted(r['altuse'])[:10]})
    return fails


def run_differential(suite, model, a):
    fwd, inv = build_maps(model)
    gen = {'single': states_single, 'pairs': states_pairs, 'multi': states_multi, 'machines': states_machines}[suite]
    items = subset(gen(model, a), a.limit if suite in ('pairs', 'machines') else (a.limit or a.n))
    o = Out(a.out, suite, len(items))
    m = open_page()
    try:
        for s in items:
            k = skey(s)
            if k in o.done_keys:
                continue
            t0 = time.time()
            try:
                bad = apply_state(m, s, fwd)
                act = m.read()
                ps = m.page_state()
                pstate, _ = page_to_oracle(ps, inv)
                extra = {'ms': round((time.time() - t0) * 1000)}
                if bad:
                    extra['unmappable'] = bad
                if skey(pstate) != k:
                    extra['page_state'] = ser_state(pstate)   # control interplay differs from the requested state
                if suite == 'machines':
                    extra['card'] = 'machine' if act['machine_card'] else ('none' if not act['path_card'] else ('station' if s['focus'] else 'path'))
                    extra['altuse'] = sorted(act['altuse'])
                    mc = machine_checks(m, model, s, act)
                    if mc:
                        extra['violations'] = mc
                rec = compare_record(model, s, act, k, extra)
                if extra.get('violations'):
                    rec['agree'] = False
            except Exception as e:  # noqa: BLE001
                rec = {'key': k, 'state': ser_state(s), 'agree': False, 'error': f'{type(e).__name__}: {str(e)[:300]}'}
                m.close(); m = open_page()
            o.write(rec)
    finally:
        errs = m.errors(); m.close()
        if errs:
            (pathlib.Path(a.out) / f'{suite}.console.txt').write_text('\n'.join(errs))
        o.finish()


# ---------------------------------------------------------------- random sequences
VIEWPORTS = (400, 600, 1024, 1600)


def run_random(model, a):
    fwd, inv = build_maps(model)
    n = a.n or 5000
    o = Out(a.out, 'random', n)
    m = open_page()
    m.reset()
    init = m.read()
    init_sig = (init['stations'], init['lines'], init['edges'], [(x['key'], x['pressed'], x['count']) for x in init['legend']['lens']])
    try:
        for i in range(n):
            key = f'seq-{a.seed}-{i}'
            if key in o.done_keys:
                continue
            rng = random.Random(f'{a.seed}-{i}')
            attempting = None
            L = rng.randint(10, 40)
            viol, steps, info = [], [], []
            t0 = time.time()
            try:
                m.reset(); m.set_viewport(1600, 1000)
                nerr = len(m.errors())
                for j in range(L):
                    s = m.state()
                    kinds = ['lens', 'add', 'remove', 'toggle', 'isolate', 'clear_isolate', 'focus', 'clear_focus', 'reset',
                             'zoom', 'fit_width', 'fit_height', 'theme', 'lang', 'viewport', 'select_machine', 'clear_machine']
                    act = rng.choice(kinds)
                    desc = [act]
                    attempting = desc
                    lang_before = None
                    if act == 'lens':
                        l = rng.choice(oracle.LENSES); m.set_lens(l); desc.append(l)
                    elif act == 'add':
                        opts = [k for k in fwd[s['lens']].values() if k not in s['values']
                                and m.page.locator(f'#lenslegend [data-lv="{k}"]').count()]
                        if not opts:
                            act = desc[0] = 'noop'
                        else:
                            k = rng.choice(opts); m.select_value(k, multi=bool(s['values'])); desc.append(k)
                    elif act == 'remove':
                        if not s['values']:
                            act = desc[0] = 'noop'
                        else:
                            k = rng.choice(sorted(s['values'])); m.select_value(k, multi=len(s['values']) > 1); desc.append(k)
                    elif act == 'toggle':
                        t = rng.choice(TOG); m.toggle(t, not s['toggles'][t]); desc.append(t)
                    elif act == 'isolate':
                        p = rng.choice(model.path_ids); m.isolate(p); desc.append(p)
                    elif act == 'clear_isolate':
                        if s['isolate']:
                            m.clear_isolate()
                        else:
                            act = desc[0] = 'noop'
                    elif act == 'focus':
                        f = rng.choice(model.station_ids); m.focus(f); desc.append(f)
                    elif act == 'clear_focus':
                        if m.page_state()['focus']:
                            m.clear_focus()
                        else:
                            act = desc[0] = 'noop'
                    elif act == 'reset':
                        m.reset()
                    elif act == 'select_machine':
                        if model.machine_ids:
                            mid = rng.choice(model.machine_ids); m.select_machine(mid); desc.append(mid)
                        else:
                            act = desc[0] = 'noop'
                    elif act == 'clear_machine':
                        if s.get('machine'):
                            m.clear_machine()
                        else:
                            act = desc[0] = 'noop'
                    elif act == 'zoom':
                        z = rng.choice([20, 50, 80, 100, 150, 250]); m.zoom(z); desc.append(z)
                    elif act in ('fit_width', 'fit_height'):
                        fn = getattr(m, act); fn(); t1 = transform(m); fn(); t2 = transform(m)
                        if t1 != t2:
                            viol.append({'step': j, 'check': f'{act}-not-idempotent', 'a': t1, 'b': t2})
                    elif act == 'theme':
                        th = rng.choice(['light', 'dark']); m.set_theme(th); desc.append(th)
                    elif act == 'lang':
                        cur = m.page.evaluate("()=>document.getElementById('app').getAttribute('data-lang')")
                        lg = 'ru' if cur != 'ru' else 'en'
                        b = m.read(); bps = m.page_state()
                        m.set_lang(lg); desc.append(lg)
                        lang_before = (b, bps)
                    elif act == 'viewport':
                        w = rng.choice(VIEWPORTS); m.set_viewport(w, 900 if w > 600 else 800); desc.append(w)
                    steps.append(desc)
                    r = m.read(); ps = m.page_state()
                    ostate, unm = page_to_oracle(ps, inv)
                    exp = oracle.expected(model, ostate)
                    d = diff(exp, r)
                    if d:
                        viol.append({'step': j, 'check': 'lit-set', 'state': ser_state(ostate), 'diff': d})
                    if unm:
                        viol.append({'step': j, 'check': 'unmappable-value', 'values': unm})
                    ds = m.state()
                    if skey(ds) != skey(ostate(ps['lens'], ps['values'], ps['toggles'], ps['isolate'], ps['focus'], ps.get('machine'))):
                        viol.append({'step': j, 'check': 'driver-state-drift', 'driver': ser_state(ds), 'page': ps})
                        m._state = ostate(ps['lens'], ps['values'], ps['toggles'], ps['isolate'], ps['focus'], ps.get('machine'))
                    if not r['altuse'] <= r['stations']:
                        viol.append({'step': j, 'check': 'altuse-not-subset-of-lit', 'extra': sorted(r['altuse'] - r['stations'])[:10]})
                    bad_e = [e for e in r['edges'] if e[0] not in r['stations'] or e[1] not in r['stations']]
                    if bad_e:
                        viol.append({'step': j, 'check': 'edge-touches-unlit', 'edges': sorted(map(list, bad_e))[:10]})
                    # ADJ-6: every lens legend (family totals included) shows static totals by design -> checked against the
                    # static total, not against the lit set. ADJ-10 (17 Sep): the reading-marks lens is gone; its glyph keys are
                    # static keys with totals and no longer a lens legend, so the former marks check has nothing to inspect.
                    attr = model.lens_attr.get(ps['lens'], {})
                    for x in r['legend']['lens']:
                        if x['count'] is None or x['key'] == '' or x['key'] not in inv.get(ps['lens'], {}):
                            continue
                        v = inv[ps['lens']][x['key']]
                        tot = sum(1 for sid in model.station_ids if v in attr[sid])
                        if x['count'] != tot:
                            viol.append({'step': j, 'check': 'legend-static-total-mismatch', 'lens': ps['lens'], 'value': x['key'],
                                         'count': x['count'], 'total': tot})
                            break
                    if act == 'reset':
                        sig = (r['stations'], r['lines'], r['edges'], [(x['key'], x['pressed'], x['count']) for x in r['legend']['lens']])
                        if sig != init_sig:
                            viol.append({'step': j, 'check': 'reset-not-initial'})
                    if lang_before:
                        b, bps = lang_before
                        if (b['stations'], b['lines'], b['edges']) != (r['stations'], r['lines'], r['edges']) or bps != ps:
                            viol.append({'step': j, 'check': 'lang-switch-changed-state', 'before': bps, 'after': ps})
                    if len(m.errors()) > nerr:
                        viol.append({'step': j, 'check': 'console-error', 'errors': m.errors()[nerr:][:3]}); nerr = len(m.errors())
                    if r['bbox_overflow']:
                        vw = m.page.viewport_size['width']
                        viol.append({'step': j, 'check': 'bbox-overflow', 'viewport': vw, 'elems': r['overflow_elems'][:5], 'doc_hscroll': r['doc_hscroll']})
            except Exception as e:  # noqa: BLE001
                viol.append({'step': len(steps), 'check': 'action-error', 'action': attempting, 'after_steps': len(steps), 'error': f'{type(e).__name__}: {str(e)[:300]}'})
                m.close(); m = open_page()
            # collapse repeated identical checks (e.g. overflow at every step of a narrow viewport)
            kinds_seen = collections.Counter(v['check'] for v in viol)
            first = {}
            for v in viol:
                first.setdefault(v['check'], v)
            finfo = {}
            for v in info:
                finfo.setdefault(v['check'], v)
            o.write({'key': key, 'length': L, 'steps': steps, 'agree': not viol, 'checks_failed': dict(kinds_seen),
                     'violations': list(first.values()), 'checks_info': dict(collections.Counter(v['check'] for v in info)),
                     'informational': list(finfo.values()), 'ms': round((time.time() - t0) * 1000), 'states': len(steps)})
    finally:
        m.close(); o.finish()


# ---------------------------------------------------------------- metamorphic (on the page)
def rd(m):
    r = m.read(); return {'stations': r['stations'], 'lines': r['lines'], 'edges': r['edges']}


def run_metamorphic(model, a):
    fwd, inv = build_maps(model)
    n = a.limit or 200
    rng = random.Random(a.seed)
    o = Out(a.out, 'metamorphic', n)
    m = open_page()
    try:
        for i in range(n):
            s = oracle.random_state(model, rng)
            k2 = f'meta-{a.seed}-{i}'
            if k2 in o.done_keys:
                continue
            viol = []
            try:
                apply_state(m, s, fwd); base = rd(m)
                vals = oracle.lens_values(model, s['lens'])
                rest = [v for v in vals if v not in s['values']]
                if rest and s['values']:
                    v = rng.choice(rest); m.select_value(fwd[s['lens']][v], multi=True); after = rd(m)
                    attr = model.lens_attr[s['lens']]
                    lost = {x for x in base['stations'] - after['stations']}
                    if lost:
                        viol.append({'check': 'M1-add-value-shrank', 'added': jv(v), 'lost': sorted(lost)})
                    apply_state(m, s, fwd)
                if not s['isolate']:
                    # ADJ-12: isolating a path that cannot share a line with the focused station or the machine releases them, so the
                    # identity holds only for a compatible path; an incompatible one is a different check (the release is expected)
                    comp = [q for q in model.path_ids if (not s['focus'] or q in model.station_paths[s['focus']]) and (not s.get('machine') or model.machines[s['machine']].path == q)]
                    if comp:
                        p = rng.choice(comp); m.isolate(p); m.clear_isolate(); r2 = rd(m)
                        if r2 != base:
                            viol.append({'check': 'M2-isolate-clear-not-identity' + ('-with-focus' if s['focus'] else ''), 'path': p, 'diff': diff(base, r2)})
                        apply_state(m, s, fwd)
                    inc = [q for q in model.path_ids if q not in comp]
                    if inc and (s['focus'] or s.get('machine')):
                        # only the term that cannot share the new line is released: a focus whose station lies on the path stays,
                        # a machine whose path it is stays (23 Sep 2026: the check was over-strict for the mixed focus + machine case)
                        p = rng.choice(inc); m.isolate(p); ps2 = m.page_state()
                        exp_focus = s['focus'] if (s['focus'] and p in model.station_paths[s['focus']]) else None
                        exp_mach = s['machine'] if (s.get('machine') and model.machines[s['machine']].path == p) else None
                        if (ps2['focus'] or None) != exp_focus or (ps2.get('machine') or None) != exp_mach or ps2['isolate'] != p:
                            viol.append({'check': 'M2b-incompatible-isolate-did-not-release', 'path': p, 'expected': {'focus': exp_focus, 'machine': exp_mach}, 'page_state': ser_state(page_to_oracle(ps2, inv)[0])})
                        apply_state(m, s, fwd)
                t = rng.choice(TOG); cur = m.state()['toggles'][t]
                m.toggle(t, not cur); m.toggle(t, cur); r3 = rd(m)
                if r3 != base:
                    viol.append({'check': 'M3-double-toggle-not-identity', 'toggle': t, 'diff': diff(base, r3)})
                s0 = dict(s, lens='family', values=set(), toggles=dict(s['toggles']))
                apply_state(m, s0, fwd); unf = rd(m)
                us, ul = set(), set()
                for v in oracle.lens_values(model, 'family'):
                    m.select_value(fwd['family'][v]); r4 = rd(m); us |= r4['stations']; ul |= r4['lines']
                miss = (unf['stations'] - us) - {'dec_cryo'}
                if miss or (us - unf['stations']) or ul != unf['lines']:
                    viol.append({'check': 'M4-family-union-ne-unfiltered', 'missing': sorted(miss), 'extra': sorted(us - unf['stations']),
                                 'lines_missing': sorted(unf['lines'] - ul), 'lines_extra': sorted(ul - unf['lines'])})
                dec = {'unfiltered_has_dec_cryo': 'dec_cryo' in unf['stations'], 'union_has_dec_cryo': 'dec_cryo' in us}
            except Exception as e:  # noqa: BLE001
                viol.append({'check': 'action-error', 'error': f'{type(e).__name__}: {str(e)[:300]}'}); dec = None
                m.close(); m = open_page()
            o.write({'key': k2, 'state': ser_state(s), 'agree': not viol, 'violations': viol, 'dec_cryo': dec})
    finally:
        m.close(); o.finish()


# ---------------------------------------------------------------- static
def run_static(model, a):
    o = Out(a.out, 'static', 6)
    o.done_keys = set()
    m = open_page()
    ids = set(model.station_ids)
    html = driver.PAGE.read_text(encoding='utf-8')
    try:
        # 1 station ids
        dom = set(m.page.evaluate("()=>[...document.querySelectorAll('#mapwrap g.station text.id')].map(t=>t.textContent)"))
        o.write({'key': 'station-ids', 'agree': dom == ids, 'dom': len(dom), 'graph': len(ids),
                 'dom_not_graph': sorted(dom - ids), 'graph_not_dom': sorted(ids - dom)})
        # 2 anchors referenced by the map (bar, map, inspector for each focused station) resolve in the page
        js_anchor = r"""()=>[...document.querySelectorAll('#mapbar a[href^="#"], #mapwrap a[href^="#"], #insp a[href^="#"]')]
            .map(a=>a.getAttribute('href')).filter(h=>h.length>1).filter(h=>!document.getElementById(decodeURIComponent(h.slice(1))))"""
        js_all = r"""()=>[...document.querySelectorAll('#mapbar a[href^="#"], #mapwrap a[href^="#"], #insp a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1)"""
        broken, seen = set(), set()
        gotos_bad = set()
        for sid in model.station_ids:
            m.focus(sid)
            seen |= set(m.page.evaluate(js_all)); broken |= set(m.page.evaluate(js_anchor))
            gotos_bad |= set(m.page.evaluate("ids=>[...document.querySelectorAll('#insp [data-goto], #mapbar [data-goto]')].map(a=>a.dataset.goto).filter(g=>!ids.includes(g))", sorted(ids)))
        m.reset()
        for pid in model.path_ids:
            m.isolate(pid)
            seen |= set(m.page.evaluate(js_all)); broken |= set(m.page.evaluate(js_anchor))
        m.reset()
        # anchor-like literals in the page's scripts (e.g. "#brief-x") that must resolve
        scripts = m.page.evaluate("()=>[...document.scripts].map(s=>s.textContent).join('\\n')")
        lit = set(re.findall(r'#(brief-[A-Za-z0-9_\-]+)', scripts))
        lit_bad = sorted(x for x in lit if not m.page.evaluate("i=>!!document.getElementById(i)", x))
        o.write({'key': 'anchors', 'agree': not broken and not gotos_bad and not lit_bad, 'hash_links_seen': len(seen),
                 'broken': sorted(broken), 'data_goto_not_station': sorted(gotos_bad), 'script_brief_literals': len(lit), 'script_literal_broken': lit_bad,
                 'note': 'map links to nodes use data-goto (station ids), not #anchors; brief ids are brief-<id>'})
        # 3 RU fallbacks (ADJ-8): the build itself prints "0 RU fallbacks" and the page has no marker, so this check lists
        # bilingual strings whose RU text is identical to EN (T('en','ru') calls in the scripts and {en,ru} objects in JSON
        # data blocks), skipping proper nouns / ids; informational (agree) unless some RU value is empty where EN is not.
        scripts = m.page.evaluate("()=>[...document.scripts].map(s=>s.textContent).join('\\n')")
        pairs = [('T', a1, a2) for a1, a2 in re.findall(r"\bT\(\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\)", scripts)]
        pairs += [(p_, e_, r_) for p_, e_, r_ in m.page.evaluate(r"""()=>{const out=[]; for(const s of document.scripts){ if(!/json/.test(s.type))continue; let d; try{d=JSON.parse(s.textContent)}catch(e){continue}
            const walk=(o,p)=>{ if(o&&typeof o==='object'){ if(!Array.isArray(o)&&('en' in o)&&('ru' in o)&&typeof o.en==='string'&&typeof o.ru==='string') out.push([p,o.en,o.ru]);
              for(const k in o) walk(o[k],p+'.'+k);} }; walk(d,s.id||'script'); } return out;}""")]
        def proper_or_id(t):
            t = t.strip()
            return (not t or re.fullmatch(r'[A-Za-z0-9_.\-/:#%+]+', t) and not re.search(r'[a-z]{4,}', t)  # ids, codes, numbers
                    or not re.search(r'[a-z]{3,}', re.sub(r'\b[A-Z][A-Za-z0-9]*', '', t))          # only capitalised words
                    or re.fullmatch(r'[a-z0-9_]+', t) is not None)                                   # snake_case id
        same = collections.Counter(e_ for _, e_, r_ in pairs if e_ == r_ and not proper_or_id(e_))
        empty_ru = sorted({p_ for p_, e_, r_ in pairs if e_.strip() and not r_.strip()})
        o.write({'key': 'ru-fallbacks', 'agree': not empty_ru, 'informational': not empty_ru,
                 'method': 'RU string identical to EN for non-proper-noun/non-id keys (T() calls + JSON {en,ru}); page has no fallback marker',
                 'pairs_scanned': len(pairs), 'identical_distinct': len(same), 'identical': same.most_common(40),
                 'empty_ru': empty_ru[:20], 'empty_ru_count': len(empty_ru)})
        # 4 bilingual string tables: object literals with en:/ru: keys must carry both; T('en','ru') calls must have both args
        objs = re.findall(r'\{[^{}]*\b(?:en|ru)\s*:[^{}]*\}', scripts)
        one_sided = [x[:120] for x in objs if not (re.search(r'(?<![\w$])en\s*:', x) and re.search(r'(?<![\w$])ru\s*:', x))]
        tcalls = re.findall(r"\bT\(\s*'((?:[^'\\]|\\.)*)'\s*(?:,\s*'((?:[^'\\]|\\.)*)')?\s*\)", scripts)
        t_bad = [a1 for a1, a2 in tcalls if not a2]
        # JSON data blocks with "en"/"ru" keys
        ks = m.page.evaluate(r"""()=>{let n=0,bad=[]; for(const s of document.scripts){ if(!/json/.test(s.type))continue; let d; try{d=JSON.parse(s.textContent)}catch(e){continue}
            const walk=(o,p)=>{ if(o&&typeof o==='object'){ if(!Array.isArray(o)&&(('en' in o)||('ru' in o))){n++; if(!(('en' in o)&&('ru' in o)))bad.push(p);}
              for(const k in o) walk(o[k],p+'.'+k);} }; walk(d,s.id||'script'); } return {n,bad:bad.slice(0,20),nbad:bad.length};}""")
        o.write({'key': 'i18n-key-sets', 'agree': not one_sided and not t_bad and not ks['nbad'], 'object_literals': len(objs),
                 'one_sided': one_sided[:20], 'T_calls': len(tcalls), 'T_missing_ru': t_bad[:20], 'json_bilingual_objects': ks})
        # 5 §7.2 table
        res = {}
        for lg in ('en', 'ru'):
            if lg == 'ru':
                m.set_lang('ru')
            t = m.table_rows(); rid = [r['id'] for r in t['rows']]
            res[lg] = {'heading': t['heading'], 'rows': len(rid), 'ids_eq_graph': set(rid) == ids,
                       'missing': sorted(ids - set(rid)), 'extra': sorted(set(rid) - ids), 'dupes': len(rid) - len(set(rid))}
        m.set_lang('en')
        ok = all(v['rows'] == 96 and v['ids_eq_graph'] and not v['dupes'] for v in res.values())
        o.write({'key': 'table-7.2', 'agree': ok, **res, 'sort_filter': 'N/A (static table, no sort/filter UI)'})
        errs = m.errors()
        o.write({'key': 'console-errors', 'agree': not errs, 'errors': errs[:10], 'external_requests': m.external})
    finally:
        m.close(); o.finish()


# ---------------------------------------------------------------- summary
def signature(rec):
    s = rec.get('state') or {}
    pat = '+'.join(x for x in (
        f"lens:{s.get('lens')}" if s.get('values') else '', f"nvals:{len(s.get('values', []))}" if s.get('values') else '',
        f"tog:{s.get('toggles')}" if s.get('toggles', '-') != '-' else '', 'isolate' if s.get('isolate') else '',
        'focus' if s.get('focus') else '', 'machine' if s.get('machine') else '') if x) or 'default'
    kind = []
    if rec.get('error'):
        kind.append('error:' + rec['error'].split(':')[0])
    if rec.get('unmappable'):
        kind.append('unmappable-value')
    for k, v in (rec.get('diff') or {}).items():
        kind.append(k + ('-missing' if v['missing'] else '') + ('-extra' if v['extra'] else ''))
    for v in rec.get('violations') or []:
        kind.append(v['check'])
    return pat, ','.join(sorted(set(kind))) or 'unknown'


def run_summary(model, a):
    outdir = pathlib.Path(a.out)
    lines = ['# V&V runner summary', '', f'Generated {time.strftime("%Y-%m-%d %H:%M:%S")} from {outdir}/*.jsonl and progress.log.', '']
    lines += ['| suite | total | agree | disagree |', '|---|---|---|---|']
    per, sigs = {}, {}
    for f in sorted(outdir.glob('*.jsonl')):
        recs = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
        suite = f.stem
        ag = sum(1 for r in recs if r.get('agree'))
        per[suite] = (len(recs), ag, len(recs) - ag)
        lines.append(f'| {suite} | {len(recs)} | {ag} | {len(recs) - ag} |')
        g = collections.OrderedDict()
        for r in recs:
            if r.get('agree'):
                continue
            if suite in ('random', 'metamorphic'):
                for v in r.get('violations') or []:
                    k = ('-', v['check'] + (':' + v.get('lens', '') if v.get('lens') else ''))
                    g.setdefault(k, [0, {'key': r['key'], **v}])[0] += 1
            elif suite == 'static':
                g.setdefault((r['key'], 'fail'), [0, r])[0] += 1
            else:
                k = signature(r)
                g.setdefault(k, [0, r])[0] += 1
        sigs[suite] = g
    lines.append('')
    for suite, g in sigs.items():
        if not g:
            continue
        lines += [f'## {suite}: {len(g)} distinct disagreement signatures', '']
        for (pat, kind), (cnt, ex) in sorted(g.items(), key=lambda kv: -kv[1][0]):
            exs = json.dumps(ex, default=jv)
            lines.append(f'- **{kind}** [{pat}] x{cnt} — example: `{exs[:600]}`')
        lines.append('')
    # coverage vs thresholds
    model_single = len(list(oracle.all_single_states(model)))
    a2 = argparse.Namespace(n=300, seed=a.seed, limit=None)
    total_pairs = len(states_pairs(model, a2))
    total_mach = len(states_machines(model, a2))
    def cov(s, tot):
        return f'{per.get(s, (0,))[0]}/{tot} ({100.0 * per.get(s, (0,))[0] / tot:.1f} %)'
    rnd = per.get('random', (0, 0, 0))
    met = per.get('metamorphic', (0, 0, 0))
    lines += ['## Coverage against SPEC claim thresholds', '',
              f'- single 100 %: {cov("single", model_single)}',
              f'- pairwise 100 %: {cov("pairs", total_pairs)} (lens-value x focus sampled n=300)',
              f'- machines (C2) 100 %: {cov("machines", total_mach)} (machine x lens-value / x focus sampled 60 each)',
              f'- random >= 5000 sequences with 0 unadjudicated: {rnd[0]} sequences, {rnd[2]} with violations (adjudication pending)',
              f'- metamorphic green: {met[0]} cases, {met[2]} failing', '']
    prog = outdir / 'progress.log'
    if prog.exists():
        done = [x for x in prog.read_text().splitlines() if ' DONE ' in x]
        lines += ['## progress.log DONE lines', '', '```'] + done[-30:] + ['```', '']
    (outdir.parent / 'SUMMARY.md' if outdir.name == 'results' else outdir / 'SUMMARY.md').write_text('\n'.join(lines))
    print('\n'.join(lines[:12]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('suite', choices=['single', 'pairs', 'multi', 'machines', 'random', 'metamorphic', 'static', 'summary'])
    ap.add_argument('--n', type=int, default=None)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out', default=str(HERE / 'results'))
    ap.add_argument('--limit', type=int, default=None)
    a = ap.parse_args()
    model = oracle.load(GRAPH)
    {'single': lambda: run_differential('single', model, a), 'pairs': lambda: run_differential('pairs', model, a),
     'multi': lambda: run_differential('multi', model, a), 'machines': lambda: run_differential('machines', model, a),
     'random': lambda: run_random(model, a),
     'metamorphic': lambda: run_metamorphic(model, a), 'static': lambda: run_static(model, a),
     'summary': lambda: run_summary(model, a)}[a.suite]()


if __name__ == '__main__':
    main()
