---
id: fab_3d
name: 3D machined superconducting cavities
layer: 10 Manufacturing
status: demonstrated
since: 2013
one_line: CNC-machined aluminium or niobium resonator bodies with internal Q above 0.5×10⁹; the cm-scale body per mode is the structural cost of cavity-based bosonic codes.
verdict: The process buys the best error structure in superconducting hardware and pays for it in volume; no vendor has published a yield, cost or density roadmap as of 2026-09-04.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Precision-machined bulk metal bodies — λ/2 or λ/4 coaxial-stub and waveguide geometries in high-purity aluminium or niobium — that host the bosonic mode. Yale's 2013 aluminium cavities reached Q > 0.5×10⁹ and a 10 ms photon lifetime, making the process qubit-grade [D][1]. A manufacturing step, not an operating device: no control modality, readout or gate time. It fixes photon loss in the mode it hosts.

## Physics & limits
The advantage is geometric: the field lives in vacuum rather than at a lithographed metal–dielectric interface, so the surface participation ratio — and the two-level-system loss that caps planar resonators — falls by orders of magnitude [D][1]. What remains is surface oxide, seam conductance and radiative leakage, answered by electropolishing, indium seals and individual tuning. Those are craft steps, which is why the floor moves slowly: 10 ms photon lifetime in 2013, 25.6 ms with 34 ms coherence in 2023 — one order in a decade [D][1][D][2]. Further movement needs surface treatment and seamless geometry, plus decoupling the mode from its ancilla [D][2].

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2013 | Machined aluminium cavity, Q > 0.5×10⁹, photon lifetime 10 ms | Yale | [D][1] |
| 2023-09 | Cavity qubit: T1 25.6 ms, T2 34 ms | Weizmann Institute | [D][2] |
| 2026-08 | Paired λ/4 coaxial bodies for dual-rail qubits | Quantum Circuits | [D][3] |

The limiting figure is volume, not Q: no per-body yield, cost or tuning-time number has been published.

## Manufacturing, materials & supply chain
Bodies are CNC- or EDM-machined from high-purity stock, polished, sealed and tuned one at a time. The binding constraint is cryostat volume, not wafer area — the inverse of a planar roadmap. Nothing is integrated on-chip, so each mode carries its own coax to room temperature; at 10³ modes the wall is coax count and cold-plate area, and 10⁴–10⁶ is out of reach. Alice & Bob's 18-mode Helium draws ~40 kW whole-system [C][4]. Machining is in-house at every vendor, with no third-party cavity foundry found; the one named external supplier nearby, NASA's Jet Propulsion Laboratory, fabricates D-Wave's cryogenic control chip, not bodies [C][5]. Refrigerators concentrate on Bluefors, which also owns Cryomech [G:BLUEFORS-CRYOMECH-2023]. No export rule specific to cavity bodies was found; exposure runs through general machine-tool controls.

## Role in the stack
Provides the bodies for the bosonic cavity mode and hence cat and GKP encodings, dual-rail erasure and ancilla-mediated gates. It replaces planar lithography and conflicts with dense 2D tiling: cm-scale bodies cannot follow transmons to 10⁴–10⁶ on a die. It contributes nothing to the derived clock — 1.44 µs derived against a measured 2.8 µs on the cat path, 2.8 µs derived against ~2 µs measured on dual-rail — setting lifetime, not timing. The adjacent empty slot is a batch or wafer-scale bosonic-mode process. Verification: the 2013 Q and the 2023 lifetime are single-group results from different groups; no Q is published for the 2026 λ/4 bodies [D][3].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Alice & Bob | developer | FR | Machines its own cat cavity bodies; 48-cat chips claimed next | [C][4] |
| D-Wave | developer | US | New Haven bench machines λ/4 coaxial dual-rail pairs | [D][3] |
| NASA JPL | supplier | US | Fabricates part of D-Wave's cryogenic control chip | [C][5] |
| Bluefors | supplier | FI | Dilution refrigerators, the volume these bodies compete for | [G:BLUEFORS-CRYOMECH-2023] |

**Money.**
2026-01-20 · D-Wave · M&A of Quantum Circuits · $550 M · — · closed [G:DWAVE-QCI-2026-01]
2026-01-06 · D-Wave · on-chip cryogenic control, JPL-fabricated part · — · announced [C][5]
2026-08-06 · D-Wave · Q2 report · H1 bookings $35.5 M, obligations $40.7 M · reported [G:DWAVE-Q2-2026-GATEMODEL]

**Market & supply chain.** There is no cavity-machining market: each vendor runs a small internal shop, which is the single point of failure. Bargaining power sits with the fridge makers. G1 and G3 pay; G4 does not.

**IP & standards.** No dated patent family specific to the machining process was found, and no standard covers cavity qualification.

**Roadmaps & track record.** No cavity density or cost roadmap exists. Alice & Bob claims Helium upgrades to 48-cat chips, unverified [C][4]; D-Wave's DR17 → DR49 → DR181 ladder implies rising body counts with no fabrication plan [R][G:DWAVE-DR-NAMING-2026-08]. Both are silent where an ASIC roadmap would be explicit.

**Strategic reading.** This process is why bosonic error structure is good and bosonic density is bad; it becomes a liability the moment planar dual-rail or on-chip GKP match its erasure fractions.

*Open niche:* cavity Q and seam-loss characterisation as a third-party service — every figure here is self-reported by the group that machined the body.

## Outlook & open questions
Confirm by 2028 if a vendor publishes a per-body yield figure or a sub-cm body at comparable Q; demote if the bench stays silent while planar erasure qubits scale. Best case 2029: batch-fabricated cavity arrays. Worst case: hand-machined bodies indefinitely, capping the branch near 10² modes. Open: does seamless machining raise Q; what is the real cost per mode? Watch Alice & Bob's 48-cat chip and D-Wave's DR49.

## Sources
[1] M. Reagor *et al.*, “Reaching 10 ms single photon lifetimes for superconducting aluminum cavities,” [arXiv:1302.4408](https://arxiv.org/abs/1302.4408), Feb. 2013.
[2] O. Milul *et al.*, “Superconducting Cavity Qubit with Tens of Milliseconds Single-Photon Coherence Time,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030336, Sep. 2023, doi: [10.1103/PRXQuantum.4.030336](https://doi.org/10.1103/PRXQuantum.4.030336).
[3] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935).
[4] N. Coppola, “Alice & Bob Unveils First Quantum System, Helium,” Alice & Bob, Jun. 10, 2026. [Online]. Available: https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/ [C]
[5] D-Wave, “D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits,” press release, Jan. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/ [C]
[6] H. Putterman *et al.*, “Hardware-efficient quantum error correction via concatenated bosonic qubits,” *Nature*, vol. 638, no. 8052, pp. 927–934, Feb. 2025, doi: [10.1038/s41586-025-08642-7](https://doi.org/10.1038/s41586-025-08642-7).
[7] S. Turcotte *et al.*, “Quantum error correction of a grid-state qubit with state preparation and measurement errors below 10⁻³,” [arXiv:2607.06718](https://arxiv.org/abs/2607.06718), Jul. 2026.

## Open verification items
The 34 ms figure is from the Weizmann Institute (T1 25.6 ms, T2 34 ms), not a Yale-lineage group, and neither the abstract nor the journal summary consulted states that the cavity is niobium-coated.
No per-body yield, tuning time or cost figure was found for any vendor.
No independent replication of either the 2013 Q > 0.5×10⁹ or the 2023 lifetime was located; both are single-group results.
Whether JPL's role in D-Wave's control chip extends to cavity-body machining is not stated in source [5]; this brief assumes it does not.
AWS [6] and Nord Quantique [7] use machined bodies but publish nothing about the process, so they are cited for context and not listed as actors on this layer.
