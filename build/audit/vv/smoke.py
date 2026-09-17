"""Smoke test for driver.py: default read, one action of each kind, read sizes after each; exit 0 iff no console errors
and the driver's state matches the page's control state after every step."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from driver import MapPage

m = MapPage().open()
fails = []
def show(label):
    r = m.read(); ps = m.page_state(); ds = m.state()
    ok = (ps['lens'] == ds['lens'] and set(ps['values']) == ds['values'] and ps['toggles'] == ds['toggles']
          and ps['isolate'] == ds['isolate'] and ps['focus'] == ds['focus'])
    if not ok: fails.append((label, ds, ps))
    print(f"{label:28s} stations={len(r['stations']):3d} lines={len(r['lines']):2d} edges={len(r['edges']):3d} "
          f"legend={len(r['legend']['lens'])} card={len(r['path_card']):4d} summary={r['selection_summary'][:40]!r} "
          f"overflow={r['bbox_overflow']} state_ok={ok}")
    return r
try:
    r = show('default')
    assert len(r['stations']) == 96 and len(r['lines']) == 14 and not r['edges'], 'default state'
    m.set_lens('aff'); show('set_lens(aff)')
    v = m.read()['legend']['lens'][0]['key']
    m.select_value(v); show(f'select_value({v})')
    v2 = m.read()['legend']['lens'][1]['key']
    m.select_value(v2, multi=True); show(f'select_value({v2},multi)')
    m.clear_values(); show('clear_values')
    m.toggle('requires', True); show('toggle(requires,on)')
    m.toggle('alternatives', True); show('toggle(alternatives,on)')
    m.toggle('conflicts', True); show('toggle(conflicts,on)')
    pid = m.page.locator('#pathchips .chip').first.get_attribute('data-chip-path')
    m.isolate(pid); show(f'isolate({pid})')
    m.clear_isolate(); show('clear_isolate')
    m.focus('transmon'); show('focus(transmon)')
    m.clear_focus(); show('clear_focus')
    m.select_mark('hub'); show('select_mark(hub)')
    m.collapse_bar(True); show('collapse_bar(True)')
    m.collapse_bar(False); show('collapse_bar(False)')
    m.reset(); show('reset')
    m.zoom(60); show('zoom(60)')
    m.fit_width(); show('fit_width')
    m.fit_height(); show('fit_height')
    m.set_theme('dark'); show('set_theme(dark)')
    m.set_lang('ru'); show('set_lang(ru)')
    t = m.table_rows(); print('table_rows', t['heading'], len(t['rows']), t['rows'][0]['id'] if t['rows'] else None)
    m.set_lang('en')
    m.set_viewport(390, 844); show('set_viewport(390,844)')
    t = m.table_rows(); print('table_rows', t['heading'], len(t['rows']))
    print('overflow elems at 390:', m.read()['overflow_elems'], 'external requests:', m.external)
finally:
    errs = m.errors(); m.close()
print('console errors:', len(errs)); [print('  ', e) for e in errs[:10]]
print('state mismatches:', fails)
sys.exit(1 if errs or fails else 0)
