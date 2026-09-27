#!/usr/bin/env python3
"""records_check — a record's key is a physics claim; its own text must not deny it.

27 Sep 2026: the topological architecture derived a T₁ of 22 s from a record filed under `t1` whose note said "not a qubit T1"
(a single-wire parity dwell time), and a cat qubit's bit-flip time stood as "T1 relaxation · best in the world, any modality".
This check reads every standard record of the graph (data/graph.json nodes[].records) and of the machines (data/machines.json
machines[].records) and fails when a record's text or note says "not a <its own key's label>", and warns on superlatives
("best in the world", "record", "unprecedented") in a scope or text field, which belong to the source, not to the register.

    python3 build/audit/records_check.py          # exit 1 on a denial; superlatives are warnings
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUPERLATIVE = re.compile(r'best in the world|world record|world-record|unprecedented|first ever', re.I)


def label_words(label):
    """the words of a key's label that a denial would name: 'T1 relaxation' → ['T1', 'T₁'], 'feed-forward latency' → ['feed-forward']"""
    w = label.split(' (')[0].split()[0]
    return list({w, w.replace('1', '₁').replace('2', '₂')})


def main():
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    M = json.load(open(os.path.join(ROOT, 'data', 'machines.json'), encoding='utf-8'))
    RK = G['vocab']['RECKEYS']
    errors, warns = [], []
    def look(owner, r):
        key = r.get('key'); lab = (RK.get(key) or [key])[0]
        txt = ' '.join(str(r.get(f) or '') for f in ('text', 'note', 'scope'))
        for w in label_words(lab):
            if r.get('num') is not None and re.search(r'\bnot (a|an|the)( qubit| true| real)? ' + re.escape(w) + r'\b', txt, re.I):
                msg = '%s · %s: filed under %s but says "%s"' % (owner, key, lab, re.search(r'.{0,40}\bnot (a|an|the)[^.;]{0,60}', txt, re.I).group(0).strip())
                (warns if re.search(r'analogue|proxy|stands in', txt, re.I) else errors).append(msg)   # a declared proxy is a warning, not a denial
        if re.search(r'flag heavily|re-fetch|TODO|check this', txt, re.I): errors.append('%s · %s: curator remark in a register field: "%s"' % (owner, key, txt[:80]))
        m = SUPERLATIVE.search(txt)
        if m: warns.append('%s · %s: superlative "%s" in a register field' % (owner, key, m.group(0)))
    for n in G['nodes']:
        for r in n.get('records') or []: look(n['id'], r)
    for m in M['machines']:
        for r in m.get('records') or []: look(m['id'], r)
    print('records_check: %d graph records, %d machine records; %d denial(s), %d superlative(s)' % (
        sum(len(n.get('records') or []) for n in G['nodes']), sum(len(m.get('records') or []) for m in M['machines']), len(errors), len(warns)))
    for e in errors: print('  ERROR', e)
    for w in warns: print('  warn ', w)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
