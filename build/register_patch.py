# -*- coding: utf-8 -*-
"""Apply a register patch (the research of 29 Sep 2026: renames, status changes, updates, splits, aliases, cell corrections)
to a machines-register folder — the repository's snapshot data/register/ and, run on the editor's machine, the live register.

    python3 build/register_patch.py PATCH.json [--dir DIR] [--dry]

PATCH.json is the researcher's file: {"rows": [{"machine_id", "action", "fields", "old", "evidence", "note"}], "doubts": [...]}.
Actions applied here: status | update | rename | split (the existing row's part) | alias | no-row (a row that is not a machine is
removed with its cells, evidence, refs, codes and roadmap rows). "add" rows are NOT applied here — a new machine needs its
cells per layer with evidence, written by hand (build/register_add.py writes them from a filled-in sidecar).
Cell corrections come from the doubts and from "stations.<layer>" fields: "<node> primary; <node> alternate (new); drop <node>".
The applier is idempotent: applying the same patch twice changes nothing the second time.
"""
import csv, json, os, sys, io, re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYERS = ('carrier', 'encoding', 'gate', 'connect', 'control', 'readout', 'code', 'decoder', 'interconnect', 'fab')
ST_COL = {'carrier': 'st_carrier', 'encoding': 'st_encoding', 'gate': 'st_gate', 'connect': 'st_connect', 'control': 'st_control',
          'readout': 'st_readout', 'code': 'st_code', 'decoder': 'st_decoder', 'interconnect': 'st_interconnect', 'fab': 'st_fab'}


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        r = csv.DictReader(f); return r.fieldnames, [OrderedDict(x) for x in r]


def write(path, fields, rows, dry):
    if dry: return
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader()
        for r in rows: w.writerow({k: r.get(k, '') for k in fields})


# ---- explicit cell corrections (the doubts of 29 Sep 2026); each: machine, layer, node, role, action, summary, url, locator
CELLS = [
    ('quantinuum-h1', 'control', 'ct_ionlaser', 'primary', 'replace', 'ct_ionaod',
     'room-temperature electronics; free-space laser beams focused into the gate zones, propagating parallel to the trap surface (no integrated photonics)',
     'https://arxiv.org/abs/2107.07505', 'hardware section: laser beams delivered from outside the vacuum chamber'),
    ('quantinuum-h2', 'control', 'ct_ionlaser', 'primary', 'replace', 'ct_ionaod',
     'room-temperature electronics; free-space gate beam pairs and sheet cooling beams (no integrated photonics)',
     'https://arxiv.org/abs/2305.03828', 'hardware section: laser light generation and delivery'),
    ('google-willow', 'readout', 'ro_reset', 'alternate', 'add', None,
     'multi-level reset of the measure qubits every cycle; DQLR leakage removal on the data qubits',
     'https://arxiv.org/abs/2408.13687', 'Methods: reset and leakage removal'),
    ('atom-computing-phoenix', 'readout', 'ro_erasure', 'alternate', 'drop', None, '', '', ''),
]


def apply_cells(d, dry, log):
    p_ev = os.path.join(d, 'machine-stations-evidence.csv'); p_st = os.path.join(d, 'machine-stations.csv'); p_m = os.path.join(d, 'machines.csv')
    f_ev, ev = read(p_ev); f_st, st = read(p_st); f_m, ms = read(p_m)
    for mid, layer, node, role, act, new, summary, url, loc in CELLS:
        if act == 'replace':
            n = 0
            for r in ev + st:
                if r['machine_id'] == mid and r['layer'] == layer and r['node_id'] == node: r['node_id'] = new; n += 1
            for r in ev:
                if r['machine_id'] == mid and r['layer'] == layer and r['node_id'] == new and summary: r['usage_summary'] = summary
            for m in ms:
                if m['machine_id'] == mid and m.get(ST_COL[layer]) == node: m[ST_COL[layer]] = new; n += 1
            log.append('%s: %s %s → %s (%d cells)' % (mid, layer, node, new, n))
        elif act == 'add':
            if not any(r['machine_id'] == mid and r['layer'] == layer and r['node_id'] == node for r in ev):
                ev.append(OrderedDict(machine_id=mid, layer=layer, node_id=node, role=role, usage_summary=summary, evidence_type='paper',
                                      evidence_url=url, evidence_locator=loc, verification='🔎'))
                st.append(OrderedDict(machine_id=mid, layer=layer, node_id=node, role=role, note=''))
                log.append('%s: + %s %s (%s)' % (mid, layer, node, role))
        elif act == 'drop':
            before = len(ev) + len(st)
            ev[:] = [r for r in ev if not (r['machine_id'] == mid and r['layer'] == layer and r['node_id'] == node)]
            st[:] = [r for r in st if not (r['machine_id'] == mid and r['layer'] == layer and r['node_id'] == node)]
            log.append('%s: − %s %s (%d rows)' % (mid, layer, node, before - len(ev) - len(st)))
    write(p_ev, f_ev, ev, dry); write(p_st, f_st, st, dry); write(p_m, f_m, ms, dry)


ALIASES = {'iqm-garnet-20': 'IQM Crystal 20', 'iqm-emerald-54': 'IQM Crystal 54', 'zhuangzi-2.0': 'Chuang-tzu 2.0'}


def main():
    a = sys.argv[1:]; dry = '--dry' in a
    d = a[a.index('--dir') + 1] if '--dir' in a else os.path.join(ROOT, 'data', 'register')
    patch = json.load(open([x for x in a if x.endswith('.json')][0], encoding='utf-8'))
    log = []
    p_m = os.path.join(d, 'machines.csv'); f_m, ms = read(p_m); by = {m['machine_id']: m for m in ms}
    removed = []
    for r in patch['rows']:
        act = r['action']; mid = r['machine_id']; m = by.get(mid)
        if act in ('keep', 'add'): continue
        if act == 'no-row':
            if m is not None: removed.append(mid); ms.remove(m); del by[mid]; log.append('%s: row removed (%s)' % (mid, r.get('note', '')[:60]))
            continue
        if m is None: log.append('%s: NOT IN REGISTER (%s)' % (mid, act)); continue
        for k, v in (r.get('fields') or {}).items():
            if k in f_m and v not in (None, ''):
                if m.get(k) != v: m[k] = v; log.append('%s: %s ← %s' % (mid, k, str(v)[:70]))
        if act == 'alias' and mid in ALIASES and ALIASES[mid] not in m['name']:
            m['name'] = '%s (%s)' % (m['name'], ALIASES[mid]); log.append('%s: alias → %s' % (mid, m['name']))
    for dbt in patch.get('doubts', []):
        c = dbt.get('correction')
        if not c: continue
        if c.get('machine_id') == 'iqm-star-24' and 'status_date' in c.get('layer/field', ''):
            m = by.get('iqm-star-24')
            if m and not m['status_date'].startswith('Sep 2025'):
                m['status_date'] = 'Sep 2025 (first 24-qubit Star delivered as VLQ at IT4I; on IQM Resonance as IQM Star 24 by Sep 2026)'; log.append('iqm-star-24: status_date ← Sep 2025')
    write(p_m, f_m, ms, dry)
    # the removed rows' dependants
    if removed:
        for fn in ('machine-stations-evidence.csv', 'machine-stations.csv', 'machine-refs-verified.csv', 'machine-codes.csv', 'roadmap-feasibility.csv', 'records-candidates.csv', 'machine-algorithms.csv'):
            p = os.path.join(d, fn)
            if not os.path.exists(p): continue
            f, rows = read(p); keep = [x for x in rows if x.get('machine_id') not in removed]
            if len(keep) != len(rows): write(p, f, keep, dry); log.append('%s: %d rows of %s removed' % (fn, len(rows) - len(keep), ', '.join(removed)))
    apply_cells(d, dry, log)
    for l in log: print(l)
    print('%s%d changes' % ('dry run: ' if dry else '', len(log)))


if __name__ == '__main__':
    main()
