#!/usr/bin/env python3
"""Build data/machines.json (SPEC step C2, "machines on the Atlas") from the machines register.

Inputs : the machines register's CSVs — QT_MACHINES_DIR if set, else the live register folder when this machine has it, else the
         snapshot data/register/ that this script copies after every run (so the repository carries the exact inputs of machines.json)
         data/graph.json (layers, vocab.RECKEYS)
Output : data/machines.json  -- deterministic: same inputs give identical bytes.

Every cell carries "state": technology | gap | none | undisclosed (see cell_state); "gap" is kept as a boolean for the consumers
that predate the register schema of 26 Sep 2026. Cells whose node is not in graph.json are reported (unknown_nodes).

Record numbers are rounded to 6 significant digits. No existing determinize rule was found in
data/graph_data.py or build/*.py, so the rule is implemented here (sig6).
"""
import re, csv, json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, 'data', 'register')   # the register's input files as read for the committed machines.json (published with the repo, 26 Sep 2026)
INPUTS = ('machines.csv', 'machine-stations.csv', 'machine-stations-evidence.csv', 'records-candidates.csv', 'machine-codes.csv',
          'roadmap-feasibility.csv', 'machine-refs-verified.csv', 'map-gaps.csv')
_REG_LIVE = '/home/claude/work/QT-Map/quantum-machines/data'
REG = os.environ.get('QT_MACHINES_DIR') or (_REG_LIVE if os.path.isdir(_REG_LIVE) else SNAP)   # the live register when present, else the snapshot
OUT = os.path.join(ROOT, 'data', 'machines.json')
EDITION = '2026.09'
SOURCE = {"register": "quantum-machines · 17 Sep 2026, re-cut 26 Sep 2026 (three ion paths, two analog paths, 14 gaps → technologies, sentinels → cell values), extended 29 Sep 2026 (24 machines added, 3 renamed, 3 split, 1 removed; ten cell corrections — data/register/patch-2026-09-29.json)",
          "evidence": "machine-stations-evidence.csv · 17 Sep 2026 (locator passes 1–3)"}
FAMILY_ORDER = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']
GAP_PREFIX = '∅'
# A cell's node is one of four things (register schema of 26 Sep 2026, decision D5): an Atlas technology; a gap `∅G-…` (the Atlas has
# no technology for what the machine runs); `none` (nothing in this layer — no code, no decoder, no interconnect, no encoding
# layer, no entangling gate); `undisclosed` (the machine has something here but publishes nothing). Only the first is a node.
SENTINELS = ('none', 'undisclosed')


def cell_state(node):
    if node.startswith(GAP_PREFIX): return 'gap'
    if node in SENTINELS: return node
    return 'station'


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
                  'decoder', 'realtime', 'roadmap', 'role', 'gate_evidence', 'decoder_mode')

# Three register columns of 2 Oct 2026 (review R1, findings 2 and 5; the editor's criterion of 2 Oct) replace two rules that read free text:
#   role           '' | scale-demonstrator (built to prove scale or a technology, performance not published, not operated for users: Condor)
#                  | exploratory (operated for users as a technical demonstration: Osprey / ibm_seattle)
#   gate_evidence  what stands behind the machine's entangling-gate figure — device-benchmark (a paper with its protocol) | platform-calibration
#                  (calibration data on a cloud platform) | vendor-dashboard (a datasheet, spec sheet or dashboard) | vendor-figure (a number in a
#                  release or blog, protocol unstated) | figure (a number whose source class is not yet tagged) | vendor-statement (words only:
#                  "comparable to", "consistent with") | none. A device is *benchmarked* when a figure of any class exists; the frontier tables
#                  count benchmarked devices (Condor, "comparable to Osprey", is not one). A blank cell is derived from err_2q_median and the flags.
#   decoder_mode   none | planned | offline | real-time-throughput (keeps up with the syndrome stream, no feedback into the circuit: Willow)
#                  | feed-forward (the decoder's output acts inside the run — closed-loop decoding). A blank cell is derived from `realtime`.
#   qubits_accessible  the qubits a vendor made usable when fewer than the physical count (Osprey: 413 of 433); the frontier counts these.
FIGURE_CLASSES = ('device-benchmark', 'platform-calibration', 'vendor-dashboard', 'vendor-figure', 'figure')
DECODER_MODES = ('none', 'planned', 'offline', 'real-time-throughput', 'feed-forward')
_NO_FIGURE = re.compile(r'^\s*(not published|none published|not disclosed|never published|no (2q|two-qubit|fidelit|gate|published)|none\b|n/a|as [A-Z]|-+\s*$|$)', re.I)


def derive_gate_evidence(m):
    """The evidence class of a row that does not state one, from err_2q_median and the flags (the migration of 2 Oct 2026)."""
    txt = (m.get('err_2q_median') or '').strip(); tl = txt.lower(); flags = set(x.strip() for x in m.get('flags', '').split(';') if x.strip())
    num = num_or_none(m.get('err_2q_median_num'))
    if num is None and (_NO_FIGURE.search(txt) or not re.search(r'\d', txt)):
        return 'vendor-statement' if re.search(r'comparable|consistent|class\b|as [A-Z]', txt) else 'none'
    if num is None: return 'none'
    if 'eplg' in tl or 'dashboard' in tl or 'calibration' in tl or 'spec sheet' in tl or 'datasheet' in tl or 'data sheet' in tl: return 'vendor-dashboard'
    if 'claim' in tl or 'press' in tl or 'unverified' in tl or 'headline' in tl or 'product page' in tl or flags & {'press-only', 'estimated-baseline', 'emulator-numbers'}: return 'vendor-figure'
    return 'figure'


def derive_decoder_mode(m):
    """decoder_mode from the free-text `realtime` field for rows that do not state one: the old rule (in-loop by the word) minus its defect —
    an 'in-loop' text alone no longer makes a closed loop; the five rows that said so were re-read at the source on 2 Oct 2026 and hold the field."""
    u = (m.get('realtime') or '').lower().strip()
    if u.startswith('offline'): return 'offline'
    if u.startswith(('planned', 'intended')): return 'planned'
    if u.startswith('in-loop') or 'real-time' in u: return 'real-time-throughput'   # a claim of real-time decoding without a re-read source: throughput at most
    return 'none'


def profile(m):
    """Register fields the report's machines chapter reasons about (strings as in machines.csv; numbers parsed)."""
    p = {k: m.get(k, '') for k in PROFILE_FIELDS}
    p['err_2q_median_num'] = sig6(num_or_none(m.get('err_2q_median_num')))
    p['flags'] = sorted(x.strip() for x in m.get('flags', '').split(';') if x.strip())
    p['qubits_accessible'] = int_or_none(m.get('qubits_accessible', ''))
    if not p['gate_evidence']: p['gate_evidence'] = derive_gate_evidence(m); p['gate_evidence_derived'] = True
    else: p['gate_evidence_derived'] = False
    if not p['decoder_mode']: p['decoder_mode'] = derive_decoder_mode(m); p['decoder_mode_derived'] = True
    else: p['decoder_mode_derived'] = False
    assert p['decoder_mode'] in DECODER_MODES, (m.get('machine_id'), p['decoder_mode'])
    assert p['gate_evidence'] in FIGURE_CLASSES + ('vendor-statement', 'none'), (m.get('machine_id'), p['gate_evidence'])
    p['benchmarked'] = p['gate_evidence'] in FIGURE_CLASSES
    return p


def fam_key(m):
    f = m['family']
    return (FAMILY_ORDER.index(f) if f in FAMILY_ORDER else len(FAMILY_ORDER), f, m['id'])


def _clean_curator(v):
    v2 = re.sub(r'\s*[-–—;,]\s*not re-fetched\b\.?', '', v)     # "x - not re-fetched" → "x"
    v2 = re.sub(r'\(\s*not re-fetched\s*\)', '', v2)             # "(not re-fetched)" → ""
    v2 = re.sub(r'\bnot re-fetched\b[.;]?\s*', '', v2)            # bare
    return re.sub(r'\s{2,}', ' ', v2).strip(' ;,-')


ATLAS_WORD = re.compile(r"(?<![-_.#/])\b([Ss])tation(s?)\b(?![-_])")
def atlas_words(x):
    """The register says "station" for a node of the map; the Atlas's reader word is "technology" (editor, 28 Sep 2026). Applied to every
    string of the document in place (node ids, urls and keys never contain the word as a whole word); returns the count."""
    n = 0
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(v, str):
                if ' ' in v and k != 'state' and ATLAS_WORD.search(v):   # prose only: vocabulary tokens ('state': 'station') stay
                    x[k] = ATLAS_WORD.sub(lambda m: ('T' if m.group(1) == 'S' else 't') + 'echnolog' + ('ies' if m.group(2) else 'y'), v); n += 1
            else: n += atlas_words(v)
    elif isinstance(x, list):
        for v in x: n += atlas_words(v)
    return n


def strip_curator_notes(x):
    """Remove the register's verification remark "not re-fetched" from every string of the document, in place; return the count.
    What stays is the substance the remark qualified ("the 94.9% GHZ figure is not in the cited sources"), which a reader can use."""
    n = 0
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(v, str):
                if 'not re-fetched' in v: x[k] = _clean_curator(v); n += 1
            else:
                n += strip_curator_notes(v)
    elif isinstance(x, list):
        for v in x: n += strip_curator_notes(v)
    return n


def build():
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    layer_no = {l['id']: str(l['n']) for l in G['layers']}
    reckeys = set(G['vocab']['RECKEYS'])
    report = {'dropped_records': [], 'unknown_layers': [], 'no_primary': [], 'orphan_rows': [], 'unknown_nodes': [], 'unknown_paths': []}
    node_ids = {n['id'] for n in G['nodes']}; path_ids = {p['id'] for p in G['paths']}

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
    KIND_ORDER = ['paper', 'whitepaper', 'product', 'docs', 'blog', 'press', 'other']
    refs_by = {}
    try:
        for r in rows('machine-refs-verified.csv'):   # attribution-verified links (20 Sep 2026): only rows the page was seen to name the machine
            if r.get('verdict', '').strip() != '✅' or r['machine_id'] not in ids: continue
            lst = refs_by.setdefault(r['machine_id'], [])
            if any(x['url'] == r['url'] for x in lst): continue
            lst.append({'url': r['url'], 'title': (r.get('found_title') or r.get('title') or '').strip()[:140], 'kind': r.get('kind', 'other').strip() or 'other'})
    except FileNotFoundError:
        pass
    for lst in refs_by.values():
        lst.sort(key=lambda x: (KIND_ORDER.index(x['kind']) if x['kind'] in KIND_ORDER else 99, x['title'], x['url']))
    codes_by = {}
    for r in rows('machine-codes.csv'):
        if r['machine_id'] not in ids:
            report['orphan_rows'].append(('code', r['machine_id'])); continue
        codes_by.setdefault(r['machine_id'], set()).add(r['code_id'])

    out, by_node = [], {}
    for m in machines:
        mid = m['machine_id']
        if m['map_path'] not in path_ids: report['unknown_paths'].append((mid, m['map_path']))
        layers = {str(n): [] for n in range(1, 11)}
        ver = tot = 0
        for r in ev_by.get(mid, []):
            node = r['node_id']
            if cell_state(node) == 'station' and node not in node_ids: report['unknown_nodes'].append((mid, node))
            v = r['verification'].strip() == '✅'
            ver += v; tot += 1
            layers[layer_no[r['layer']]].append({
                "node": node, "role": r['role'], "gap": node.startswith(GAP_PREFIX), "state": cell_state(node),
                "summary": r['usage_summary'],
                "evidence": {"type": r['evidence_type'], "url": r['evidence_url'],
                             "locator": r['evidence_locator'], "verified": v}})
            if cell_state(node) == 'station':   # by_node indexes Atlas technologies only; gaps and cell values are counted per machine
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
                    "refs": refs_by.get(mid, []),
                    "profile": profile(m)})
    out.sort(key=fam_key)
    bn = {k: {"primary": sorted(v['primary']), "alternate": sorted(v['alternate'])} for k, v in sorted(by_node.items())}
    doc = {"edition": EDITION, "source": SOURCE, "machines": out, "by_node": bn, "roadmaps": road}
    n_cur = strip_curator_notes(doc)
    # the cataloguer's working remarks ("not re-fetched") never reach a reader (27 Sep 2026: 31 did)
    n_words = atlas_words(doc)   # 'station' -> 'technology' in the register's notes (28 Sep 2026)
    report['curator_notes_stripped'] = [n_cur]; report['atlas_words'] = [n_words]
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write('\n')
    return doc, report


def snapshot():
    """copy the input files into data/register so the repository carries the exact inputs of data/machines.json"""
    import shutil
    if os.path.abspath(REG) == os.path.abspath(SNAP): return
    os.makedirs(SNAP, exist_ok=True)
    for n in INPUTS:
        src = os.path.join(REG, n)
        if os.path.exists(src): shutil.copyfile(src, os.path.join(SNAP, n))


if __name__ == '__main__':
    doc, rep = build(); snapshot()
    print('wrote %s: %d machines, %d nodes, %d bytes' % (os.path.relpath(OUT, ROOT), len(doc['machines']),
          len(doc['by_node']), os.path.getsize(OUT)))
    for k, v in rep.items():
        print('  %s: %d%s' % (k, len(v), (' ' + str(v[:10])) if v else ''))
    from collections import Counter
    ge = Counter(m['profile']['gate_evidence'] for m in doc['machines']); dm = Counter(m['profile']['decoder_mode'] for m in doc['machines'])
    print('  gate evidence (stated %d, derived %d): %s' % (sum(1 for m in doc['machines'] if not m['profile']['gate_evidence_derived']),
          sum(1 for m in doc['machines'] if m['profile']['gate_evidence_derived']), ', '.join('%s %d' % kv for kv in sorted(ge.items()))))
    print('  decoder mode (stated %d, derived %d): %s' % (sum(1 for m in doc['machines'] if not m['profile']['decoder_mode_derived']),
          sum(1 for m in doc['machines'] if m['profile']['decoder_mode_derived']), ', '.join('%s %d' % kv for kv in sorted(dm.items()))))
