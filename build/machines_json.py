#!/usr/bin/env python3
"""Build data/machines.json (SPEC step C2, "machines on the Map") from the machines register.

Inputs : quantum-machines-2026.09/data/{machines,machine-stations-evidence,records-candidates,machine-codes,roadmap-feasibility}.csv
         data/graph.json (layers, vocab.RECKEYS)
Output : data/machines.json  -- deterministic: same inputs give identical bytes.

Record numbers are rounded to 6 significant digits. No existing determinize rule was found in
data/graph_data.py or build/*.py, so the rule is implemented here (sig6).
"""
import csv, json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.environ.get('QT_MACHINES_DIR', '/home/claude/work/QT-Map/quantum-machines-2026.09/data')
OUT = os.path.join(ROOT, 'data', 'machines.json')
EDITION = '2026.09'
SOURCE = {"register": "quantum-machines-2026.09 · 17 Sep 2026",
          "evidence": "machine-stations-evidence.csv · 17 Sep 2026 (locator passes 1–3)"}
FAMILY_ORDER = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']
GAP_PREFIX = '∅'


def rows(name):
    with open(os.path.join(REG, name), encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))


def sig6(x):
    """Round a float to 6 significant digits (None stays None)."""
    if x is None:
        return None
    x = float(x)
    if x == 0 or not math.isfinite(x):
        return x
    return float('%.6g' % x)


def num_or_none(s):
    s = (s or '').strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def int_or_none(s):
    v = num_or_none(s)
    return int(v) if v is not None and v == int(v) else None


PROFILE_FIELDS = ('qubit_type', 'gate_mechanism', 'connectivity', 'degree', 'control', 'control_placement', 'readout',
                  'err_2q_median', 'err_2q_best', 'readout_error', 't1', 't2', 't_2q', 't_meas', 'best_logical',
                  'decoder', 'realtime', 'roadmap')


def profile(m):
    """Register fields the report's machines chapter reasons about (strings as in machines.csv; numbers parsed)."""
    p = {k: m.get(k, '') for k in PROFILE_FIELDS}
    p['err_2q_median_num'] = sig6(num_or_none(m.get('err_2q_median_num')))
    p['flags'] = sorted(x.strip() for x in m.get('flags', '').split(';') if x.strip())
    return p


def fam_key(m):
    f = m['family']
    return (FAMILY_ORDER.index(f) if f in FAMILY_ORDER else len(FAMILY_ORDER), f, m['id'])


def build():
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    layer_no = {l['id']: str(l['n']) for l in G['layers']}
    reckeys = set(G['vocab']['RECKEYS'])
    report = {'dropped_records': [], 'unknown_layers': [], 'no_primary': [], 'orphan_rows': []}

    machines = rows('machines.csv')
    ids = {m['machine_id'] for m in machines}
    ev_by = {}
    for r in rows('machine-stations-evidence.csv'):
        if r['machine_id'] not in ids:
            report['orphan_rows'].append(('evidence', r['machine_id'])); continue
        if r['layer'] not in layer_no:
            report['unknown_layers'].append((r['machine_id'], r['layer'])); continue
        ev_by.setdefault(r['machine_id'], []).append(r)
    rec_by = {}
    for r in rows('records-candidates.csv'):
        if r['machine_id'] not in ids:
            report['orphan_rows'].append(('record', r['machine_id'])); continue
        if r['key'] not in reckeys:
            report['dropped_records'].append((r['machine_id'], r['key'])); continue
        rec_by.setdefault(r['machine_id'], []).append(r)
    road = []
    for r in rows('roadmap-feasibility.csv'):
        road.append({k: r.get(k, '') for k in ('roadmap_id', 'org', 'machine_id', 'year', 'q_r', 'eps_r', 'g_r',
                                                'algorithm_id', 'verdict', 'deficit')})
    road.sort(key=lambda r: (r['roadmap_id'], r['algorithm_id']))
    codes_by = {}
    for r in rows('machine-codes.csv'):
        if r['machine_id'] not in ids:
            report['orphan_rows'].append(('code', r['machine_id'])); continue
        codes_by.setdefault(r['machine_id'], set()).add(r['code_id'])

    out, by_node = [], {}
    for m in machines:
        mid = m['machine_id']
        layers = {str(n): [] for n in range(1, 11)}
        ver = tot = 0
        for r in ev_by.get(mid, []):
            node = r['node_id']
            v = r['verification'].strip() == '✅'
            ver += v; tot += 1
            layers[layer_no[r['layer']]].append({
                "node": node, "role": r['role'], "gap": node.startswith(GAP_PREFIX),
                "summary": r['usage_summary'],
                "evidence": {"type": r['evidence_type'], "url": r['evidence_url'],
                             "locator": r['evidence_locator'], "verified": v}})
            by_node.setdefault(node, {"primary": set(), "alternate": set()})[r['role']].add(mid)
        for k, lst in layers.items():
            lst.sort(key=lambda s: (s['role'] != 'primary', s['node'], s['evidence']['url'], s['summary']))
            if not any(s['role'] == 'primary' for s in lst):
                report['no_primary'].append((mid, k))
        recs = [{"key": r['key'], "num": sig6(num_or_none(r['num'])), "unit": r['unit'], "text": r['note'],
                 "scope": r['scope'], "date": r['date'], "url": r['url']} for r in rec_by.get(mid, [])]
        recs.sort(key=lambda r: (r['key'], r['date'], r['scope'], r['url'], r['num'] if r['num'] is not None else -1, r['text']))
        out.append({"id": mid, "name": m['name'], "org": m['org'], "org_id": m['org_id'],
                    "country": m['org_country'], "family": m['family'], "map_path": m['map_path'],
                    "status": m['status'], "status_date": m['status_date'],
                    "physical_qubits_num": int_or_none(m['physical_qubits_num']), "access": m['access'],
                    "layers": layers, "records": recs, "codes": sorted(codes_by.get(mid, ())),
                    "evidence_counts": {"verified": ver, "total": tot},
                    "profile": profile(m)})
    out.sort(key=fam_key)
    bn = {k: {"primary": sorted(v['primary']), "alternate": sorted(v['alternate'])} for k, v in sorted(by_node.items())}
    doc = {"edition": EDITION, "source": SOURCE, "machines": out, "by_node": bn, "roadmaps": road}
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write('\n')
    return doc, report


if __name__ == '__main__':
    doc, rep = build()
    print('wrote %s: %d machines, %d nodes, %d bytes' % (os.path.relpath(OUT, ROOT), len(doc['machines']),
          len(doc['by_node']), os.path.getsize(OUT)))
    for k, v in rep.items():
        print('  %s: %d%s' % (k, len(v), (' ' + str(v[:10])) if v else ''))
