---
id: fluxonium
name: Fluxonium
layer: 1 Carrier
tier: 3
status: demonstrated
since: 2009
one_line: Josephson-junction-array-shunted superconducting qubit at 0.2–1 GHz with large anharmonicity and long T1, bought at the price of a flux-bias line per qubit.
verdict: Best two-qubit number on any superconducting carrier (99.94% CNOT, 60 ns, stable 24 days) yet nobody's product carrier as of 2026-09-04; it wins only if cold flux control arrives before transmon couplers close the gap.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A superconducting circuit shunted by a large junction-array inductance, putting the 0→1 transition at 0.2–1 GHz with gigahertz anharmonicity; Manucharyan, Koch, Glazman and Devoret, 2009. Charge dispersion vanishes.
Coordinates: fabricated carrier; deterministic entangling ~50 ns (10^-7.3 s); dispersive readout ~0.3 µs, non-destructive, mid-circuit-capable.
Static mobility; low-frequency flux control at room temperature; Pauli plus coherent error; superconducting lithography.

## Physics & limits
Dielectric loss scales with ω, so T1 of 160–260 µs at ~300 MHz is routine where a transmon fights the same bath at 5 GHz [D][2]. But kT/h ≈ 420 MHz at 20 mK: equilibrium leaves tens of percent in |1⟩, making active reset (~98% [D][4]) mandatory. The floor is 1/f flux dephasing — T2* 20–110 µs against those T1 [D][2][5] — second-order at the sweet spot and untunable. In the record CNOT the dominant term is instead coherent: off-resonant control-qubit flips, residual error below 2×10⁻⁴ [D][2]. A quieter bias generated closer to the chip is what moves the floor.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2023-09-25 | CZ 99.922 ± 0.009% (RL-optimised mean) | MIT / MIT Lincoln Lab | [D][1] |
| 2024-07-22 | CNOT 99.94% in 60 ns, >99.9% for 24 days uncalibrated | Maryland–EPFL–UMass–Wisconsin | [D][2] |
| 2025-01-14 | Single-qubit gate 99.998% | MIT EQuS | [D][3] |
| 2026-01-23 | On-chip flux-DAC control, T1 ≈ 200 µs preserved | D-Wave | [D][5] |

All one- or two-qubit devices; no fluxonium lattice or QEC cycle exists as of 2026-09-04.

## Manufacturing, materials & supply chain
Same Nb/Al junction lithography as transmon, inheriting its foundries and its TLS problem; record devices come from MIT Lincoln Laboratory and no merchant supplier exists. The I/O cost is drive, readout and a flux line per qubit: a fridge carries a few hundred DC bias lines, so the burden bites at 10³, and at 10⁴–10⁶ the bias must be generated cold. D-Wave flip-chips a multiplexed Φ-DAC die across a ~7 µm gap at 10 mK with no resolvable added decoherence (T1 ≈ 200 µs [D][5]), key parts from NASA JPL [C][6]; Shenzhen runs XY and Z down one warm line per qubit [D][4]. Export exposure is generic superconducting (US EAR ECCN 3A901).

## Role in the stack
A drop-in Layer-1 alternative on the superconducting path, replacing transmon where coherence beats control simplicity; nothing downstream requires it. Its 60 ns gate does not set the derived clock — dispersive readout at ~0.3 µs does, as for transmon — so fluxonium buys error, not speed. Verification: the headline numbers are RB averages on isolated pairs, blind to lattice crosstalk, flux drift and fluxon leakage, and 99.94% is unreplicated; the main report's 99.92% record [D][1] is superseded by it, and 99.922% is itself an RL-optimised mean (unassisted peaks 99.85–99.9%).

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Google | developer | US | Absorbed Atlantic Quantum's fluxonium team; silent since | [P][7] |
| D-Wave | developer | US | On-chip Φ-DAC control of a fluxonium | [D][5] |
| University of Maryland | research | US | Manucharyan-group 99.94% CNOT | [D][2] |
| S Lab, Shenzhen | research | CN | Single-channel unified flux control | [D][4] |

**Money.**
2025-10-03 · Google · acquisition of Atlantic Quantum · terms undisclosed · closed [P][7][G:GOOGLE-ATLANTIC-2025-10]
2025-11-06 · Atlantic Quantum · absent from QBI Stage B (11 teams, ≤ $15 M each) · DARPA · official [G:QBI-STAGEB-2025-11]
2026-08-06 · D-Wave · H1-2026 revenue $5.9 M, cash $546.2 M · reported [C][8][G:DWAVE-FIN-2026]

**Market & supply chain.** No commercial supply chain: transmon's kit plus cryogenic DAC/SFQ control, built only in-house (D-Wave) or at government laboratories (JPL, MIT Lincoln Laboratory) — a single point of failure on the one scalable control path. Pays for G3/G4 and G7.

**IP & standards.** No dated fluxonium-specific patent family found as of 2026-09-04; PatSnap's 2026-06-30 superconducting-device counts are not broken out by carrier [P][G:PATSNAP-2026-06].

**Roadmaps & track record.** Atlantic Quantum (2025-04 · fluxonium machine under QBI · absorbed, no roadmap survives). D-Wave (2026-06-01 · DR17/DR49/DR181 · dual-rail cavity qubits, not fluxonium [P][G:DWAVE-DR-NAMING-2026-08]) — its fluxonium work is control IP with no product attached.

**Strategic reading.** The advantage over a good transmon is thin — Toshiba's double-transmon coupler gives CZ 99.90% in 48 ns [D][9] — so fluxonium wins only if cold flux control lands first. Then cryogenic-control vendors and die-bonding capacity capture the value and power sits with the control-chip supplier, not the qubit fab.

*Open niche:* the open QCVV job is flux-DAC-induced error — quantisation noise, switching crosstalk into neighbours, drift of the cold bias — invisible in the single-qubit RB numbers D-Wave and Shenzhen publish; a vendor-neutral protocol would serve every flux-tunable platform.

## Outlook & open questions
Confirm by end-2027: a ≥ 4-qubit fluxonium under on-chip flux control with published two-qubit RB, or a replication of 99.94%; demote if neither appears. Best case 2029: 2Q error near 10⁻⁴ cuts the surface-code budget for a given Λ; worst case, switching noise from the control die eats the coherence advantage. Does the flux-noise floor survive multiplexing? Can 0.2–1 GHz readout reach 99.5% in a lattice? What became of the Atlantic Quantum team?

## Sources
[1] Ding, Hays, Sung, Kannan, … Serniak, Oliver (MIT / MIT Lincoln Laboratory), "High-Fidelity, Frequency-Flexible Two-Qubit Fluxonium Gates with a Transmon Coupler", Phys. Rev. X 13, 031035, 2023-09-25 — https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035
[2] Lin, Cho, Chen, Vavilov, Wang, Manucharyan (Maryland, Wisconsin, UMass Amherst, EPFL), "24 days-stable CNOT-gate on fluxonium qubits with over 99.9% fidelity", PRX Quantum 6, 010349 (2025); arXiv:2407.15783, 2024-07-22 — https://arxiv.org/abs/2407.15783
[3] MIT News, "Fast control methods enable record-setting fidelity in superconducting qubit" (MIT EQuS, "Suppressing Counter-Rotating Errors for Fast Single-Qubit Gates with Fluxonium", PRX Quantum), 2025-01-14 — https://news.mit.edu/2025/fast-control-methods-enable-record-setting-fidelity-superconducting-qubit-0114
[4] Pan, Wang, Zhou, Deng, Wang et al. (S Lab, Quantum Science Center of Guangdong–Hong Kong–Macao Greater Bay Area), "Unified Flux Control Architecture for Fluxonium Qubits", arXiv:2605.25948, 2026-05-26 — https://arxiv.org/html/2605.25948v1
[5] D-Wave, whitepaper 14-1090A-A, "Digital Control of High-Coherence Fluxonium Qubits", 2026-01-23 [C] — https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf
[6] D-Wave, "D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits", press release, 2026-01-06 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/
[7] The Quantum Insider, "Atlantic Quantum Joins Google Quantum AI", 2025-10-03 [P] — https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/
[8] D-Wave, Q2-2026 financial results, 2026-08-06 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/
[9] Toshiba, double-transmon coupler CZ 99.90% in 48 ns, Phys. Rev. X 14, 041050 — https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050

## Open verification items
Gate duration of the 99.922% MIT CZ: the graph record says 50 ns; the PRX abstract states none. Unresolved.
The PRX Quantum publication date of source [2] was not confirmed (volume/article number only); the arXiv date is used.
D-Wave quotes 200 bias wires (2026-01-06) and ~300 bias lines (2026-01-23) for the same annealer scheme; unreconciled [G:DWAVE-FLUXDAC-LINECOUNT-CONFLICT].
No fluxonium-specific patent family with a date was found.
