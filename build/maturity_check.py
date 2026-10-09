#!/usr/bin/env python3
"""§3.1's maturity table against the anchors of §1.2 (the editor's decision D6-4, 9 Oct 2026).

A, B and C are the three scores whose anchors name a measured figure; this script derives them from the register and prints them
beside the typed values of report/report_EN.md's Table 3.1, so a typed cell that the register no longer supports shows up.
D (fault-tolerance progress) is checked by eye against §3.2; E and F are the editor's judgement.

  A  best two-qubit error (err_2q_median_num) of a DEVICE (machines_chapter's definition) with >= 50 physical qubits, counted only
     when data/register/machine-2q-classes.csv puts the figure in a class consistent with "full-width parallel operation": a named
     protocol (P-avg / P-proc), measured simultaneously, in a layer or in a code cycle (S-sim / S-layer / S-cycle), unconditioned
     (C-none…), confidence high or medium. Bands: <= 1e-4 -> 5; <= 1e-3 -> 4; <= 5e-3 -> 3 (also below 50 qubits, if >= 10);
     <= 1e-2 at >= 10 qubits, or better only at <= 10 qubits -> 2; else 1. The anchor's "or <= 5e-3 with a demonstrated erasure
     or bias structure" (score 4) is a judgement the register does not encode: printed as AMBIGUOUS where it would raise the score.
  B  QEC-cycle time: the register has no cycle-time field, so the cycle times quoted in data/register/machine-codes.csv (best
     instance and note, "N us cycle"; a quoted target is skipped) of devices are read; bands <= 1 us -> 5; <= 10 us -> 4;
     ~100 us -> 3; 1-10 ms -> 2; >= 10 ms -> 1. A platform with no quoted cycle keeps its typed value (printed as such).
  C  physical qubits of the largest device whose class-consistent figure meets the platform's rule-derived A band.
     Bands: >= 1,000 -> 5; >= 100 -> 4; >= 50 -> 3; >= 10 -> 2; else 1.

    python3 build/maturity_check.py
"""
import csv, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build')); sys.path.insert(0, os.path.join(ROOT, 'data'))
import machines_chapter as mc

# Table 3.1's rows → the register's machines (family, and map path where a platform is an architecture of a family)
PLATFORMS = [
    ('Superconducting', lambda m: m['family'] == 'SC' and m.get('map_path') not in ('cat', 'dualrail')),
    ('Neutral atoms', lambda m: m['family'] == 'ATOM'),
    ('Trapped ions', lambda m: m['family'] == 'ION'),
    ('Bosonic (cat/GKP/dual-rail)', lambda m: m['family'] == 'SC' and m.get('map_path') in ('cat', 'dualrail')),
    ('Spin qubits (Si/Ge)', lambda m: m['family'] == 'SPIN'),
    ('Photonic', lambda m: m['family'] == 'PHOTON'),
    ('Topological', lambda m: m['family'] == 'TOPO'),
    ('Annealing', lambda m: m['family'] == 'ANNEAL'),
]
A_BANDS = [(1e-4, 5), (1e-3, 4), (5e-3, 3), (1e-2, 2)]


def typed_table(path=os.path.join(ROOT, 'report', 'report_EN.md')):
    """Table 3.1 as typed: platform -> the six cells"""
    s = open(path, encoding='utf-8').read()
    i = s.index('### 3.1 '); j = s.index('\n\n', s.index('|---', i))
    out = {}
    for ln in s[i:j].splitlines():
        c = [x.strip().strip('*') for x in ln.strip().strip('|').split('|')]
        if len(c) >= 7 and not ln.startswith('|---') and c[0] != 'Platform': out[c[0]] = c[1:7]
    return out


def classes():
    return {r['machine_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'register', 'machine-2q-classes.csv'), encoding='utf-8'))}


def consistent(r):
    return bool(r) and r['err_2q_protocol'] in ('P-avg', 'P-proc') and r['err_2q_cond'].startswith('C-none') and r['confidence'] in ('high', 'medium') \
        and r['err_2q_scope'] in ('S-sim', 'S-layer', 'S-cycle')


def band_A(e):
    for hi, sc in A_BANDS:
        if e <= hi: return sc
    return 1


def band_C(q):
    return 5 if q >= 1000 else 4 if q >= 100 else 3 if q >= 50 else 2 if q >= 10 else 1


def band_B(us):
    # anchors: <= 1 us -> 5; 1-10 us -> 4; ~100 us -> 3; 1-10 ms -> 2; >= 10 ms -> 1 (10-100 us and 0.1-1 ms fall between bands)
    return 5 if us <= 1 else 4 if us <= 10 else 3 if 50 <= us <= 300 else 2 if 1000 <= us <= 10000 else 1 if us >= 10000 else None


def cycles():
    out = {}
    for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'register', 'machine-codes.csv'), encoding='utf-8')):
        txt = r['best_instance'] + ' ' + r['note']
        for mm in re.finditer(r'([\d.]+)\s*(us|µs|ms)\s+(?:QEC\s+)?cycle', txt):
            if 'target' in txt[max(0, mm.start() - 80):mm.start()].lower(): continue   # a roadmap's cycle, not a measured one
            v = float(mm.group(1)) * (1000 if mm.group(2) == 'ms' else 1)
            out.setdefault(r['machine_id'], set()).add(v)
    return out


def main():
    M, G, NODE, LAYERS, PATHS, MS = mc.prep()
    cls = classes(); cyc = cycles(); typed = typed_table()
    rows = []
    for name, sel in PLATFORMS:
        dev = [m for m in MS if sel(m) and m['device']]
        fig = [(m['err'], m['q'] or 0, m['name']) for m in dev if m['err'] is not None and not (m['flags'] & mc.EXCL_ERR_FLAGS) and consistent(cls.get(m['id']))]
        big = sorted(x for x in fig if x[1] >= 50); mid = sorted(x for x in fig if x[1] >= 10)
        note = []
        if big:
            A = band_A(big[0][0]); basis = big[0]
            if A == 3: note.append('A: 4 if the anchor\'s erasure-or-bias clause applies (a judgement the register does not encode)')
        elif mid:
            A = min(3, band_A(mid[0][0])); basis = mid[0]
            if mid[0][0] <= 5e-3: note.append('A: no class-consistent figure at >= 50 q; band 3 read as not requiring 50 q')
        elif fig:
            A = 2; basis = sorted(fig)[0]
        else:
            A = None; basis = None
        if A is not None:
            hi = dict((s, h) for h, s in A_BANDS).get(A, 1e9)
            ok = [x for x in fig if x[0] <= hi]
            C = band_C(max(x[1] for x in ok)) if ok else None
            cbasis = max(ok, key=lambda x: (x[1], x[2])) if ok else None
        else:
            C = cbasis = None
        cy = sorted((min(cyc[m['id']]), m['name']) for m in dev if m['id'] in cyc)
        B = band_B(cy[0][0]) if cy else None
        rows.append((name, typed.get(name, ['?'] * 6), A, basis, B, cy, C, cbasis, note))
    print('Platform | typed A B C | rule A (basis) | rule B (register cycle times) | rule C (basis)')
    for name, ty, A, basis, B, cy, C, cbasis, note in rows:
        fa = f"{A} ({basis[2]}: {basis[0]:.1e} at {basis[1]} q)" if basis else 'none (no class-consistent figure)'
        fb = (f"{B} (" + '; '.join(f"{n} {v:g} us" for v, n in cy) + ")") if cy else 'no cycle time in the register'
        fc = f"{C} ({cbasis[2]}: {cbasis[1]} q)" if cbasis else 'none'
        if not (A is not None and str(A) != ty[0]): note = [x for x in note if not x.startswith('A: 4 if')]
        flag = []
        for k, rv, tv in (('A', A, ty[0]), ('B', B, ty[1]), ('C', C, ty[2])):
            if rv is not None and str(rv) != tv: flag.append(f"{k} typed {tv} / rule {rv}")
        print(f"{name} | {ty[0]} {ty[1]} {ty[2]} | {fa} | {fb} | {fc}" + (' | DIFF: ' + '; '.join(flag) if flag else '') + (' | ' + '; '.join(note) if note else ''))


if __name__ == '__main__':
    main()
