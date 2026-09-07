---
id: cavity
name: Bosonic cavity mode
layer: 1 Carrier
status: demonstrated
since: 2013
one_line: A harmonic microwave mode of a 3D or planar superconducting resonator used as the qubit carrier; its error is structured photon loss, not generic Pauli noise.
verdict: Laboratory memories reach 25.6 ms photon lifetime, but working bosonic devices run two to three orders shorter; the carrier's limit is the ancilla coupled to it, not the cavity.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The quantised harmonic mode of a machined 3D or planar superconducting resonator, driven and read out dispersively through a coupled transmon ancilla. Yale's 3D circuit-QED work made it a carrier in 2013: Q > 0.5×10⁹, 10 ms single-photon lifetime in aluminium [D][1]. Readout is ancilla-mediated at ~1 µs, non-destructive, mid-circuit capable; the carrier is fabricated, bus-connected, room-temperature microwave driven.

## Physics & limits
A harmonic mode's dominant decay channel is amplitude damping alone — the whole argument for bosonic codes, since an encoding can target one known channel instead of an unstructured Pauli basis. Loss scales linearly with occupation, so κ caps the bias any cat encoding can reach. The floor is surface two-level systems, seam conductance and radiative leakage: 25.6 ms lifetime, 34 ms coherence (Weizmann, 2023), from a geometry that "couples minimally to the control qubit" [D][2]. That phrase is the limit — a mode whose ancilla is driven hard inherits its dephasing, and Nord Quantique's working GKP mode runs T1 = 360 µs [D][6]. Moving it means ancilla decoupling and surface treatment.

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2013 | Aluminium 3D cavity, Q > 0.5×10⁹, photon lifetime 10 ms | Yale | [D][1] |
| 2023-09 | Cavity memory: T1 25.6 ms, T2 34 ms | Weizmann Institute | [D][2] |
| 2026-08 | Paired λ/4 coaxial cavities: dual-rail CZ ≈500 ns, erasure 0.5%/gate, Pauli 0.029(6)% | Quantum Circuits | [D][3] |

Typical at scale is far below best: 18 cat modes (Helium), five storage modes (Ocelot) [C][4][D][5]. The dominant operating term is ancilla-induced dephasing plus gate-visible loss, the 0.5%-per-gate erasure being that loss detected [D][3].

## Manufacturing, materials & supply chain
Bodies are precision-machined aluminium or niobium, polished and sealed; a mode occupies cm scale against a transmon's ~100 µm — that ratio, not Q, is the liability. Per mode the burden is one drive line plus an ancilla with its own drive and readout chain. No cryogenic-CMOS or on-chip multiplexing of cavity control exists, so lines grow linearly: at 10³ modes the wall is coax count and cryostat volume in one dilution unit; 10⁴–10⁶ needs different packaging. Machining is in-house everywhere; no third-party foundry and no cavity-specific export rule were found. Concentration sits around it: Bluefors refrigerators, Cryomech pulse tubes included [G:BLUEFORS-CRYOMECH-2023].

## Role in the stack
Requires machined 3D cavities; provides the mode for cat and GKP encodings, dual-rail erasure, ancilla-mediated gates and dispersive readout. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: 2.8 µs on the dual-rail cavity path, four 500 ns CZ layers over a ~0.4 µs check [D][3], and 1.44 µs on the cat path, gate-set, against its measured 2.8 µs cycle [D][5]. Verification: the 25.6/34 ms figures are single-group and unreplicated [D][2]; the dual-rail CZ's Pauli error is post-selected, and its Λ ≈ 27 is simulated, not measured [S][G:QCI-LAMBDA27-2026-08].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Alice & Bob | developer | FR | 18-cat-mode Helium system, ~40 kW, sold to GENCI | [C][4] |
| D-Wave | developer | US | λ/4 coaxial cavity dual-rail qubits, via Quantum Circuits | [D][3] |
| AWS | developer | US | Ocelot: five storage modes, four ancillas, five buffers | [D][5] |
| Nord Quantique | developer | CA | Multimode cavity GKP, T1 360 µs | [D][6] |
| Weizmann Institute | research | IL | Cavity memory record holder | [D][2] |

**Money.**
2026-01-20 · D-Wave · M&A of Quantum Circuits · $550 M · — · closed [G:DWAVE-QCI-2026-01]
2026-08-06 · D-Wave · Q2 report · $9.3 M acquisition cost, $2.3 M inherited bookings · reported [G:DWAVE-QCI-INTEGRATION-2026-08]
2026-05-18 · Nord Quantique · growth equity · $30 M at $1.4 B · — · closed [C][9]

**Market & supply chain.** Nobody sells cavities; the money is downstream in fridges and amplifiers. Unit economics are unpublished — Helium's ~40 kW for 18 modes is a whole-system figure [C][4]. G3 pays here, G4 does not at cm scale.

**IP & standards.** No dated patent family specific to the cavity mode was found; Amazon's US 11,748,652 B1 covers the layer above [G:AMZN-ERASURE-PATENT].

**Roadmaps & track record.** Alice & Bob delivered Helium 2026-06 as promised, without logical data [C][4]. D-Wave promises DR17 (2026), DR49 (2027), DR181 (2028), 10 logical (2030), 100 logical (2032) at Λ = 10 [R][G:DWAVE-DR-NAMING-2026-08]. Both ship on time and defer the numbers that matter.

**Strategic reading.** If cavity modes stay the best-structured error channel in superconducting hardware, their vendors trade error quality for fewer physical qubits; if planar dual-rail or on-chip GKP match those erasure fractions, cm-scale bodies lose on density and the branch narrows to a memory niche.

*Open niche:* no cross-vendor loss budget exists — intrinsic κ, seam loss and ancilla dephasing separated by one protocol across vendors.

## Outlook & open questions
Confirm by 2028 if an operating multi-mode device holds photon lifetime above 1 ms; demote if operating lifetimes stay near 10² µs while planar erasure qubits close the gap. Best case 2029: multiplexed control, sub-cm bodies; worst case, single-digit-mode demonstrators indefinitely. Open: how much operating dephasing is ancilla-borne; will anyone publish Q for the λ/4 bodies? Watch Alice & Bob logical data and DR49.

## Sources
[1] Reagor, Paik, Catelani, Sun, Axline, Holland, Pop, Masluk, Brecht, Frunzio, Devoret, Glazman, Schoelkopf (Yale) · "Reaching 10 ms single photon lifetimes for superconducting aluminum cavities" · arXiv:1302.4408 · 2013-02-18 — https://arxiv.org/abs/1302.4408
[2] Milul, Guttel, Goldblatt, Hazanov, Joshi, Chausovsky, Kahn, Çiftyürek, Lafont, Rosenblum (Weizmann Institute) · "Superconducting cavity qubit with tens of milliseconds single-photon coherence time" · PRX Quantum 4, 030336 · 2023-09-14 — https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030336
[3] Quantum Circuits / D-Wave · dual-rail cavity CZ with erasure detection · Nature 656, 47 · 2026-08-05 — https://www.nature.com/articles/s41586-026-10822-y
[4] Alice & Bob · "Alice & Bob unveils first quantum system" (Helium) · newsroom · 2026-06-10 [C] — https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/
[5] Putterman et al. (AWS/Caltech) · "Hardware-efficient quantum error correction using concatenated bosonic qubits" (Ocelot) · Nature 638, 927–934 · 2025-02-26 — https://www.nature.com/articles/s41586-025-08642-7
[6] Nord Quantique · single-mode GKP characterisation, T1 360 µs, logical error 8.1×10⁻³ per round · arXiv:2607.06718 · 2026-07 — https://arxiv.org/abs/2607.06718
[7] D-Wave · "D-Wave to acquire Quantum Circuits Inc." · press release · 2026-01-07 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[8] Chou et al. (Yale) · "Demonstrating a superconducting dual-rail cavity qubit with erasure-detected logical measurements" · Nature Physics 20, 1454 · arXiv:2307.03169 · 2023-07-06 — https://arxiv.org/abs/2307.03169
[9] Nord Quantique · "$1.4 Billion USD Valuation with Latest Investment" · BusinessWire · 2026-05-18 [C] — https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment

## Open verification items
The 25.6 ms / 34 ms Weizmann figures are single-group; no independent replication was found as of 2026-09-04, and the cavity's material (aluminium vs niobium) is not stated in the abstract or journal summary consulted.
No cavity quality factor has been published for the λ/4 coaxial bodies used in the 2026-08 dual-rail CZ [3].
SUSTech's dual-rail work uses four transmon qubits, so SUSTech is not an actor for this carrier.
Helium's "up to 200× lower hardware requirements" is a company claim with no logical-level data behind it [C][4].
