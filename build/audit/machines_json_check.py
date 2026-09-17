#!/usr/bin/env python3
"""Check data/machines.json against data/graph.json, map-gaps.csv and the register CSVs. Exit 1 on any failure."""
import csv, collections, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.environ.get('QT_MACHINES_DIR', '/home/claude/work/QT-Map/quantum-machines-2026.09/data')
fails, notes = [], []


def rows(name):
    with open(os.path.join(REG, name), encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))


M = json.load(open(os.path.join(ROOT, 'data', 'machines.json'), encoding='utf-8'))
G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
node_layer = {n['id']: n['layer'] for n in G['nodes']}
gaps = {'∅' + r['gap_id'] for r in rows('map-gaps.csv')}
reckeys = set(G['vocab']['RECKEYS'])

# 1. every node id exists in graph.json (and sits on the right layer) or is a map gap
for m in M['machines']:
    for L, sts in m['layers'].items():
        for s in sts:
            nid = s['node']
            if s['gap'] != nid.startswith('∅'):
                fails.append('%s L%s %s: gap flag wrong' % (m['id'], L, nid))
            if nid.startswith('∅'):
                if nid not in gaps: fails.append('%s L%s %s: gap id not in map-gaps.csv' % (m['id'], L, nid))
            elif nid not in node_layer:
                fails.append('%s L%s %s: node not in graph.json' % (m['id'], L, nid))
            elif str(node_layer[nid]) != L:
                fails.append('%s L%s %s: node is on layer %s in graph.json' % (m['id'], L, nid, node_layer[nid]))
for nid in M['by_node']:
    if not (nid in node_layer or nid in gaps): fails.append('by_node %s unknown' % nid)

# 2. every machine has 10 layers with >= 1 primary
for m in M['machines']:
    if sorted(m['layers'], key=int) != [str(i) for i in range(1, 11)]:
        fails.append('%s: layers %s' % (m['id'], sorted(m['layers'])))
    for L, sts in m['layers'].items():
        if not any(s['role'] == 'primary' for s in sts): fails.append('%s L%s: no primary' % (m['id'], L))

# 3. counts match the CSVs
mc = rows('machines.csv'); ev = rows('machine-stations-evidence.csv')
rc = rows('records-candidates.csv'); cc = rows('machine-codes.csv')
def eq(label, a, b):
    (notes if a == b else fails).append('%s: json %s vs csv %s' % (label, a, b))
eq('machines', len(M['machines']), len(mc))
eq('machine id set equal', sorted(m['id'] for m in M['machines']) == sorted(r['machine_id'] for r in mc), True)
eq('station rows', sum(len(s) for m in M['machines'] for s in m['layers'].values()), len(ev))
eq('verified rows', sum(m['evidence_counts']['verified'] for m in M['machines']), sum(r['verification'].strip() == '✅' for r in ev))
eq('evidence_counts.total', sum(m['evidence_counts']['total'] for m in M['machines']), len(ev))
eq('primary rows', sum(s['role'] == 'primary' for m in M['machines'] for L in m['layers'].values() for s in L), sum(r['role'] == 'primary' for r in ev))
eq('by_node memberships', sum(len(v['primary']) + len(v['alternate']) for v in M['by_node'].values()),
   len({(r['node_id'], r['role'], r['machine_id']) for r in ev}))
kept = [r for r in rc if r['key'] in reckeys]
eq('records (vocab keys)', sum(len(m['records']) for m in M['machines']), len(kept))
if len(kept) != len(rc): notes.append('records dropped (key not in RECKEYS): %d' % (len(rc) - len(kept)))
eq('code links', sum(len(m['codes']) for m in M['machines']), len({(r['machine_id'], r['code_id']) for r in cc}))
fam = collections.Counter(m['family'] for m in M['machines'])
notes.append('families: %s' % dict(fam))

for n in notes: print('ok   ' + n)
for f in fails: print('FAIL ' + f)
print('%s: %d failures' % ('PASS' if not fails else 'FAIL', len(fails)))
sys.exit(1 if fails else 0)
