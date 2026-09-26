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
The quantised harmonic mode of a machined 3D or planar superconducting resonator, driven and read out dispersively through a coupled transmon ancilla. Yale's 3D circuit-QED work made it a carrier in 2013: Q > 0.5×10⁹, 10 ms single-photon lifetime in aluminium [D][246]. Readout is ancilla-mediated at ~1 µs, non-destructive, mid-circuit capable; the carrier is fabricated, bus-connected, room-temperature microwave driven.

## Physics & limits
A harmonic mode's dominant decay channel is amplitude damping alone — the whole argument for bosonic codes, since an encoding can target one known channel instead of an unstructured Pauli basis. Loss scales linearly with occupation, so κ caps the bias any cat encoding can reach. The floor is surface two-level systems, seam conductance and radiative leakage: 25.6 ms lifetime, 34 ms coherence (Weizmann, 2023), from a geometry that "couples minimally to the control qubit" [D][247]. That phrase is the limit — a mode whose ancilla is driven hard inherits its dephasing, and Nord Quantique's working GKP mode runs T1 = 360 µs [D][77]. Moving it means ancilla decoupling and surface treatment.

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2013 | Aluminium 3D cavity, Q > 0.5×10⁹, photon lifetime 10 ms | Yale | [D][246] |
| 2023-09 | Cavity memory: T1 25.6 ms, T2 34 ms | Weizmann Institute | [D][247] |
| 2026-08 | Paired λ/4 coaxial cavities: dual-rail CZ ≈500 ns, erasure 0.5%/gate, Pauli 0.029(6)% | Quantum Circuits | [D][79] |

Typical at scale is far below best: 18 cat modes (Helium), five storage modes (Ocelot) [C][82][D][75]. The dominant operating term is ancilla-induced dephasing plus gate-visible loss, the 0.5%-per-gate erasure being that loss detected [D][79].

## Manufacturing, materials & supply chain
Bodies are precision-machined aluminium or niobium, polished and sealed; a mode occupies cm scale against a transmon's ~100 µm — that ratio, not Q, is the liability. Per mode the burden is one drive line plus an ancilla with its own drive and readout chain. No cryogenic-CMOS or on-chip multiplexing of cavity control exists, so lines grow linearly: at 10³ modes the wall is coax count and cryostat volume in one dilution unit; 10⁴–10⁶ needs different packaging. Machining is in-house everywhere; no third-party foundry and no cavity-specific export rule were found. Concentration sits around it: Bluefors refrigerators, Cryomech pulse tubes included [G:BLUEFORS-CRYOMECH-2023].

## Role in the stack
Requires machined 3D cavities; provides the mode for cat and GKP encodings, dual-rail erasure, ancilla-mediated gates and dispersive readout. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: 2.8 µs on the dual-rail cavity path, four 500 ns CZ layers over a ~0.4 µs check [D][79], and 1.44 µs on the cat path, gate-set, against its measured 2.8 µs cycle [D][75]. Verification: the 25.6/34 ms figures are single-group and unreplicated [D][247]; the dual-rail CZ's Pauli error is post-selected, and its Λ ≈ 27 is simulated, not measured [S][G:QCI-LAMBDA27-2026-08].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Alice & Bob | developer | FR | 18-cat-mode Helium system, ~40 kW, sold to GENCI | [C][82] |
| D-Wave | developer | US | λ/4 coaxial cavity dual-rail qubits, via Quantum Circuits | [D][79] |
| AWS | developer | US | Ocelot: five storage modes, four ancillas, five buffers | [D][75] |
| Nord Quantique | developer | CA | Multimode cavity GKP, T1 360 µs | [D][77] |
| Weizmann Institute | research | IL | Cavity memory record holder | [D][247] |

**Money.**
2026-01-20 · D-Wave · M&A of Quantum Circuits · $550 M · — · closed [G:DWAVE-QCI-2026-01]
2026-08-06 · D-Wave · Q2 report · $9.3 M acquisition cost, $2.3 M inherited bookings · reported [G:DWAVE-QCI-INTEGRATION-2026-08]
2026-05-18 · Nord Quantique · growth equity · $30 M at $1.4 B · — · closed [C][84]

**Market & supply chain.** Nobody sells cavities; the money is downstream in fridges and amplifiers. Unit economics are unpublished — Helium's ~40 kW for 18 modes is a whole-system figure [C][82]. G3 pays here, G4 does not at cm scale.

**IP & standards.** No dated patent family specific to the cavity mode was found; Amazon's US 11,748,652 B1 covers the layer above [G:AMZN-ERASURE-PATENT].

**Roadmaps & track record.** Alice & Bob delivered Helium 2026-06 as promised, without logical data [C][82]. D-Wave promises DR17 (2026), DR49 (2027), DR181 (2028), 10 logical (2030), 100 logical (2032) at Λ = 10 [R][G:DWAVE-DR-NAMING-2026-08]. Both ship on time and defer the numbers that matter.

**Strategic reading.** If cavity modes stay the best-structured error channel in superconducting hardware, their vendors trade error quality for fewer physical qubits; if planar dual-rail or on-chip GKP match those erasure fractions, cm-scale bodies lose on density and the branch narrows to a memory niche.

*Open niche:* no cross-vendor loss budget exists — intrinsic κ, seam loss and ancilla dephasing separated by one protocol across vendors.

## Outlook & open questions
Confirm by 2028 if an operating multi-mode device holds photon lifetime above 1 ms; demote if operating lifetimes stay near 10² µs while planar erasure qubits close the gap. Best case 2029: multiplexed control, sub-cm bodies; worst case, single-digit-mode demonstrators indefinitely. Open: how much operating dephasing is ancilla-borne; will anyone publish Q for the λ/4 bodies? Watch Alice & Bob logical data and DR49.

## Sources
[75] H. Putterman *et al.*, “Hardware-efficient quantum error correction via concatenated bosonic qubits,” *Nature*, vol. 638, no. 8052, pp. 927–934, Feb. 2025, doi: [10.1038/s41586-025-08642-7](https://doi.org/10.1038/s41586-025-08642-7). [D]
[77] S. Turcotte *et al.*, “Quantum error correction of a grid-state qubit with state preparation and measurement errors below 10⁻³,” [arXiv:2607.06718](https://arxiv.org/abs/2607.06718), Jul. 2026. [D]
[79] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [D]
[82] N. Coppola, “Alice & Bob Unveils First Quantum System, Helium,” Alice & Bob, Jun. 10, 2026. [Online]. Available: https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/ [C]
[84] Nord Quantique, “Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment,” Business Wire, May 18, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment [C]
[246] M. Reagor *et al.*, “Reaching 10 ms single photon lifetimes for superconducting aluminum cavities,” [arXiv:1302.4408](https://arxiv.org/abs/1302.4408), Feb. 2013. [D]
[247] O. Milul *et al.*, “Superconducting Cavity Qubit with Tens of Milliseconds Single-Photon Coherence Time,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030336, Sep. 2023, doi: [10.1103/PRXQuantum.4.030336](https://doi.org/10.1103/PRXQuantum.4.030336). [D]

## Open verification items
The 25.6 ms / 34 ms Weizmann figures are single-group; no independent replication was found as of 2026-09-04, and the cavity's material (aluminium vs niobium) is not stated in the abstract or journal summary consulted.
No cavity quality factor has been published for the λ/4 coaxial bodies used in the 2026-08 dual-rail CZ [79].
SUSTech's dual-rail work uses four transmon qubits, so SUSTech is not an actor for this carrier.
Helium's "up to 200× lower hardware requirements" is a company claim with no logical-level data behind it [C][82].
