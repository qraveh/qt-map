#!/usr/bin/env python3
"""Dependencies against the paths (27 Sep 2026, the edge audit).

For every path and every station in its slots, each hard dependency of the station must be met inside the path: the needed
station itself, or any member of its one-of group, somewhere in the path's slots (primary or alternate). Soft dependencies
(the usual route) are not checked; link-scoped needs (a detector the link brings with it) are exempt. A primary station's
unmet need is an error; an alternate's is a warning. Two rules on top of the edges:
  R1  a path whose primary gate is analog or non-entangling (b.det = na) holds no code and no decoder;
  R2  a path holding a syndrome code (any code other than fusion-based, mitigation or a detection code) holds a readout
      station that measures mid-circuit.
Usage: python3 build/audit/edges_check.py [--graph data/graph.json] [--strict]   (exit 1 on errors; --strict also on warnings)
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check(G):
    node = {n['id']: n for n in G['nodes']}
    req = [e for e in G['edges'] if e['type'] == 'requires']
    by_src = {}
    for e in req:
        by_src.setdefault(e['src'], []).append(e)
    errors, warnings = [], []
    for p in G['paths']:
        members = set(i for ids in p['slots'].values() for i in ids)
        for L, ids in p['slots'].items():
            for i, sid in enumerate(ids):
                role = 'primary' if i == 0 else 'alternate'
                groups_seen = set()
                for e in by_src.get(sid, []):
                    if e.get('strength') == 'soft' or e.get('scope') == 'link':
                        continue
                    if e.get('group'):
                        key = (sid, e['group'])
                        if key in groups_seen:
                            continue
                        groups_seen.add(key)
                        alts = [x['dst'] for x in by_src[sid] if x.get('group') == e['group']]
                        if not any(a in members for a in alts):
                            (errors if role == 'primary' else warnings).append(
                                '%s: %s (%s, layer %s) needs one of %s — none in the path' % (p['id'], sid, role, L, alts))
                    elif e['dst'] not in members:
                        (errors if role == 'primary' else warnings).append(
                            '%s: %s (%s, layer %s) needs %s — not in the path' % (p['id'], sid, role, L, e['dst']))
        # R1
        g = (p['slots'].get('3') or [None])[0]
        if g and node[g]['b'].get('det') == 'na' and (p['slots'].get('7') or p['slots'].get('8')):
            errors.append('%s: R1 — analog or non-entangling gate %s with a code/decoder slot filled' % (p['id'], g))
        # R2
        codes = [c for c in p['slots'].get('7', []) if c not in ('code_fusion', 'code_mitig', 'code_detect')]
        if codes:
            ro = [node[r] for r in p['slots'].get('6', [])]
            if not any(r.get('c') and r['c'].get('mid') for r in ro):
                errors.append('%s: R2 — syndrome code(s) %s without a mid-circuit readout station' % (p['id'], codes))
    return errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph', default=os.path.join(ROOT, 'data', 'graph.json'))
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()
    G = json.load(open(a.graph, encoding='utf-8'))
    errors, warnings = check(G)
    for w in warnings:
        print('WARN', w)
    for e in errors:
        print('ERROR', e)
    print('edges_check: %d error(s), %d warning(s)' % (len(errors), len(warnings)))
    sys.exit(1 if errors or (a.strict and warnings) else 0)


if __name__ == '__main__':
    main()
