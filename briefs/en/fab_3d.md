---
id: fab_3d
name: 3D machined superconducting cavities
layer: 10 Manufacturing
status: demonstrated
since: 2013
one_line: CNC-machined aluminium or niobium resonator bodies with internal Q above 0.5×10⁹; the cm-scale body per mode is the structural cost of cavity-based bosonic codes.
verdict: The process buys the best error structure in superconducting hardware and pays for it in volume; no vendor has published a yield, cost or density roadmap as of 2026-09-04.
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Precision-machined bulk metal bodies — λ/2 or λ/4 coaxial-stub and waveguide geometries in high-purity aluminium or niobium — that host the bosonic mode. Yale's 2013 aluminium cavities reached Q > 0.5×10⁹ and a 10 ms photon lifetime, making the process qubit-grade [D][318]. A manufacturing step, not an operating device: no control modality, readout or gate time. It fixes photon loss in the mode it hosts.

## Physics & limits
The advantage is geometric: the field lives in vacuum rather than at a lithographed metal–dielectric interface, so the surface participation ratio — and the two-level-system loss that caps planar resonators — falls by orders of magnitude [D][318]. What remains is surface oxide, seam conductance and radiative leakage, answered by electropolishing, indium seals and individual tuning. Those are craft steps, which is why the floor moves slowly in cavities built for qubit experiments: 10 ms photon lifetime in 2013, 25.6 ms with 34 ms coherence in 2023 — a factor of 2.6 in lifetime in a decade [D][318][D][319]. Accelerator technology shows how low the floor can go: Fermilab's niobium cavities, their niobium-oxide two-level-system loss suppressed by vacuum heat treatment at 340–450 °C, kept photons for 0.5–2 s at about 10 mK, measured down to a few photons — bare, with no qubit or ancilla attached [D][G:FNAL-SRF-CAVITY-2020]. Carrying that into a qubit memory needs surface treatment and seamless geometry, plus decoupling the mode from its ancilla [D][319].

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2013 | Machined aluminium cavity, Q > 0.5×10⁹, photon lifetime 10 ms | Yale | [D][318] |
| 2020-03 | Niobium accelerator cavities, no qubit attached: photon lifetime 0.5–2 s at ~10 mK | Fermilab | [D][G:FNAL-SRF-CAVITY-2020] |
| 2023-09 | Cavity qubit: T1 25.6 ms, T2 34 ms | Weizmann Institute | [D][319] |
| 2026-08 | Paired λ/4 coaxial bodies for dual-rail qubits | Quantum Circuits | [D][84] |

The limiting figure is volume, not Q: no per-body yield, cost or tuning-time number has been published.

## Manufacturing, materials & supply chain
Bodies are CNC-machined (computer numerical control) or EDM-machined from high-purity stock, polished, sealed and tuned one at a time. The binding constraint is cryostat volume, not wafer area — the inverse of a planar roadmap. Nothing is integrated on chip, so each mode carries its own coax to room temperature; at 10³ modes the wall is coax count and cold-plate area, and 10⁴–10⁶ is out of reach. The two cat-qubit vendors build planar: AWS's Ocelot holds its bosonic modes in coplanar-waveguide resonators on two bump-bonded dies [D][80], and Alice & Bob's chips are tantalum-on-sapphire circuits, Boson 3's memory a quarter-wave coplanar resonator [G:ALICEBOB-CAT-PLANAR-2024]; Nord Quantique's GKP mode stays in a double-post cavity of high-purity aluminium [D][82]. Machining is in-house at every vendor, with no third-party cavity foundry found; the one named external supplier nearby, NASA's Jet Propulsion Laboratory, fabricated key components of D-Wave's cryogenic-control multi-chip package, not bodies [C][281]. Refrigerators concentrate on Bluefors, which also owns Cryomech [G:BLUEFORS-CRYOMECH-2023]. No export rule specific to cavity bodies was found; exposure runs through general machine-tool controls.

## Role in the stack
Provides the bodies for the bosonic cavity mode and hence cat and GKP encodings, dual-rail erasure and ancilla-mediated gates. It replaces planar lithography and conflicts with dense 2D tiling: cm-scale bodies cannot follow transmons to 10⁴–10⁶ on a die. It contributes nothing to the derived clock — 1.44 µs derived against a measured 2.8 µs on the cat architecture, 2.8 µs derived against ~2 µs measured on dual-rail — setting lifetime, not timing. The adjacent empty slot is a batch or wafer-scale bosonic-mode process. Verification: the 2023 lifetime is a single-group result; the 2013 Q has since been exceeded independently, by Fermilab's niobium cavities with no ancilla attached [D][G:FNAL-SRF-CAVITY-2020]; the 2026 λ/4 bodies report cavity lifetimes of 231–652 µs, a Q of 1–3×10⁷ [D][84].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Nord Quantique | developer | CA | GKP qubit in a double-post cavity of high-purity aluminium | [D][82] |
| D-Wave | developer | US | New Haven bench builds paired λ/4 coaxial cavities for dual-rail qubits; material and machining not published | [D][84] |
| NASA JPL | supplier | US | Fabricated key components of D-Wave's cryogenic-control multi-chip package | [C][281] |
| Bluefors | supplier | FI | Dilution refrigerators, the volume these bodies compete for | [G:BLUEFORS-CRYOMECH-2023] |

**Money.**
2026-01-20 · D-Wave · M&A of Quantum Circuits · $550 M · — · closed [G:DWAVE-QCI-2026-01]
2026-01-06 · D-Wave · on-chip cryogenic control, key package components fabricated at JPL · — · announced [C][281]
2026-08-06 · D-Wave · Q2 report · H1 bookings $35.5 M, obligations $40.7 M · reported [G:DWAVE-Q2-2026-GATEMODEL]

**Market & supply chain.** There is no cavity-machining market: each vendor runs a small internal shop, which is the single point of failure. Bargaining power sits with the fridge makers. G1 and G3 pay; G4 does not.

**IP & standards.** No dated patent family specific to the machining process was found, and no standard covers cavity qualification.

**Roadmaps & track record.** No cavity density or cost roadmap exists. D-Wave's DR17 → DR49 → DR181 ladder implies rising body counts with no fabrication plan [R][G:DWAVE-DR-NAMING-2026-08], silent where an ASIC roadmap would be explicit.

**Strategic reading.** This process is why bosonic error structure is good and bosonic density is bad; it becomes a liability the moment planar dual-rail or on-chip GKP match its erasure fractions.

## Outlook & open questions
Confirm by 2028 if a vendor publishes a per-body yield figure or a sub-cm body at comparable Q; demote if the bench stays silent while planar erasure qubits scale. Best case 2029: batch-fabricated cavity arrays. Worst case: hand-machined bodies indefinitely, capping the branch near 10² modes. Open: does seamless machining raise Q; what is the real cost per mode? Watch D-Wave's DR49 and whether Nord Quantique goes beyond one cavity mode.

## References
[80] H. Putterman *et al.*, “Hardware-efficient quantum error correction via concatenated bosonic qubits,” *Nature*, vol. 638, no. 8052, pp. 927–934, Feb. 2025, doi: [10.1038/s41586-025-08642-7](https://doi.org/10.1038/s41586-025-08642-7). [D]
[82] S. Turcotte *et al.*, “Quantum error correction of a grid-state qubit with state preparation and measurement errors below 10⁻³,” [arXiv:2607.06718](https://arxiv.org/abs/2607.06718), Jul. 2026. [D]
[84] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [D]
[281] D-Wave, “D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits,” Jan. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/ [C]
[318] M. Reagor *et al.*, “Reaching 10 ms single photon lifetimes for superconducting aluminum cavities,” [arXiv:1302.4408](https://arxiv.org/abs/1302.4408), Feb. 2013. [D]
[319] O. Milul *et al.*, “Superconducting Cavity Qubit with Tens of Milliseconds Single-Photon Coherence Time,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030336, Sep. 2023, doi: [10.1103/PRXQuantum.4.030336](https://doi.org/10.1103/PRXQuantum.4.030336). [D]

## Open verification items
The 34 ms figure is from the Weizmann Institute (T1 25.6 ms, T2 34 ms), not a Yale-lineage group, and neither the abstract nor the journal summary consulted states that the cavity is niobium-coated.
No per-body yield, tuning time or cost figure was found for any vendor.
The 2013 Q > 0.5×10⁹ has been exceeded independently — Fermilab's niobium accelerator cavities kept photons for 0.5–2 s at about 10 mK, with no qubit or ancilla attached [G:FNAL-SRF-CAVITY-2020]; no independent replication of the 2023 cavity-qubit lifetime was located.
Source [281] names neither the package components JPL fabricated nor any role in cavity-body machining; this brief assumes it has none.
Nord Quantique [82] names its cavity's material and geometry (high-purity aluminium, double-post) but not how the body is made; AWS [80] uses no machined body.
