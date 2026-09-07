---
id: ct_ionmw
name: Chip-integrated microwave control (ions)
layer: "5 Control"
status: demonstrated
since: 2024
one_line: Ion gate drive synthesised as electrical signals and delivered by conductors inside the trap chip instead of by laser beams.
verdict: Fidelity records are real but two-ion; the ~200-sources-per-1,000-qubits wiring claim remains a 2023 design study, with no multi-zone chip-integrated microwave device published as of 2026-09-03.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

The control layer of the laser-free ion machine: the electronics generating the qubit drive, the chip conductors radiating it, and the wiring between. Hyperfine splittings sit at 1–13 GHz, so the wavelength exceeds the whole trap and nothing is focused. Addressing is geometric, via the near field of a trace tens of micrometres from the ion, or spectral, when a static magnetic gradient gives each ion its own resonance. One family descends from NIST Boulder's near-field gates of the early 2010s, carried today by Oxford Ionics inside IonQ; the other is Wunderlich's magnetic-gradient-induced coupling from Siegen, commercialised by eleQtron as MAGIC.

Coordinates: carrier affinity 1.0, fully fabricated — the ion is natural, everything this node owns is lithographic; no characteristic time and no entangling action of its own; no readout, fluorescence stays optical; no mobility, the structure is static and ions are transported past it; microwave modality at room-temperature placement, only routing on-chip; Pauli error structure, no leakage channel of its own; MEMS-class manufacturing, a multilayer surface-electrode metal stack. The node dates from 2024, when the sub-part-per-million single-qubit gate [D][3] and the first fielded MAGIC demonstrator [C][8] arrived.

## Physics & limits

A 10 GHz photon carries ~40 µeV against an optical Raman photon's ~2 eV. Driving through a virtual excited state costs spontaneous scattering, which floors laser gates near 10⁻⁴ and converts part of that error into leakage; a microwave drive touches no excited state, so the term vanishes. What remains is classical — source amplitude and phase noise, magnetic-field noise, calibration drift — hence a floor of 1.5(4)×10⁻⁷ per Clifford on a ⁴³Ca⁺ clock qubit, T₂ ≈ 70 s, at room temperature, unshielded, calibration error below 10⁻⁸ [D][3].

The bill arrives in current: spin–motion coupling, the entangling ingredient treated in the sibling gate brief, needs a gradient, and a gradient at the ion means amperes microns away. Three consequences follow. Ohmic dissipation, since the 10 GHz copper skin depth is sub-micrometre and the heat lands in the chip holding the ion; global reach, since every ion sees a drive whose wavelength dwarfs the trap, so selectivity must be built from routing or frequency separation; and drive-induced motional heating, which shows up not as a control error but as a degraded entangling gate later. Superconducting traces and on-chip switching that keeps unselected zones cold would move the floor.

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-05-22 | 1,000 fully connected qubits from ~200 signal sources (design) | Malinowski, Allcock, Ballance (Oxford Ionics) | [S][2] |
| 2023-05-22 | ~40–2,600 gate layers per second projected | Oxford Ionics | [S][2] |
| 2024-05-30 | First MAGIC demonstrator delivered, 10 qubits, Hamburg | eleQtron / NXP / ParityQC | [C][8] |
| 2024-12-05 | 1Q error 1.5(4)×10⁻⁷ per Clifford, no magnetic shielding | Oxford (Lucas group) | [D][3] |
| 2025-10-20 | 2Q error 8.4(7)×10⁻⁵, no ground-state cooling | Oxford Ionics / IonQ | [D][4] |

Every record above was taken on one or two ions in a laboratory trap; no public device drives eight or more zones from chip-integrated conductors. The largest ion machine in service, the 98-ion Helios, is laser-driven with 1,228 electrodes and ≥7 wavelengths, and spends ~55 ms per full-width layer on transport, sorting and cooling against a ~70 µs gate [D][1]. The dominant Oxford error term is decoherence plus leakage and measurement, not the drive electronics [D][3]; at system scale it should be crosstalk and drive-induced heating, neither published.

## Manufacturing, materials & supply chain

The chip is an RF circuit that happens to trap ions: metal levels with a top layer sized for ~1 A at gigahertz frequencies, vias moving the DC fan-out off the ion-facing surface, and — in WISE — switching devices integrated in a form "compatible with its fabrication and operation constraints", synthesis left outside [S][2]. That is a semiconductor-fab specification, not an optics-shop one, and it explains capital allocation better than any roadmap slide. IonQ bought Oxford Ionics for $1.075 B (closed 2025-09-17) [G:IONQ-OXIONICS-2025], then the 200 mm foundry SkyWater for ~$1.8 B (closed 2026-07-31) [G:IONQ-SKYWATER-2026], while disclosing only a "semiconductor-based approach to manufacturing" [C][6]. In Germany the split is contractual: eleQtron builds trap and MAGIC hardware, NXP the control and regulation electronics, ParityQC the architecture layer [G][7].

No yield, uniformity or cost-per-qubit figure is public for a microwave trap chip as of 2026-09-03. The one quotable ratio is 0.2 signal sources per qubit at 1,000 qubits [S][2], against a laser system's per-zone beam path and ≥7 wavelengths [D][1]. Single points of failure sit in trap fabrication — Sandia, Infineon, Honeywell in-house, IonQ's captive SkyWater — not in the commodity microwave chain; export exposure runs through the September 2024 US quantum controls, ECCN unverified.

## Control, readout & I/O burden

Per qubit: one tone at 1–13 GHz with sub-milliradian phase control, plus trap DC voltages and a stable magnetic environment. The naive build gives one synthesiser, amplifier and coaxial feedthrough per zone, and it is feedthrough count and heat load, not qubits, that stops the machine at a few hundred. WISE answers with demultiplexing — synthesis at room temperature, simple switches on the chip, one shared high-power signal fanned out to the selected zone — yielding ~200 sources for 1,000 qubits at 40–2,600 layers per second [S][2]. That is the move superconducting digital control makes when one digital input feeds several qubits [D][13].

At 10³ qubits the binding question is whether an on-chip switch can sit micrometres from an ion without charging dielectrics or adding electric-field noise: unpublished, and the load-bearing unknown here. At 10⁴ the wall is thermal — parallel gates dissipating tens of milliwatts to watts each cannot run together in a 4 K trap with a one-watt cooling budget, so parallelism trades against clock rate, which the record's room-temperature operation avoids at the price of higher anomalous heating [D][3]. At 10⁶ nothing published applies; it needs gigahertz synthesis on-chip. Latency stays comfortable: 10–1,000 µs gates leave FPGA control three orders of magnitude of headroom, the inverse of the superconducting case.

## Role in the stack

The node sits on the path *Trapped ions — electronic gates, chip control* (IonQ/Oxford Ionics, eleQtron, Quantum Art). It **requires** surface-electrode ion-trap microfabrication, specifically the current-carrying traces; it **provides** the signal sources for the electronic near-field microwave gate; it **replaces** laser control of ions. The switching price is precise: gate lasers go, but cooling, state-preparation and readout lasers stay, so a "laser-free" machine still carries optics, the trap chip becomes a microwave design problem, and the species choice narrows to hyperfine ions with a usable clock transition. The off-diagonal reading is a natural carrier driven by a wholly fabricated control structure — the manufacturing burden moves off the qubit onto the chip around it.

Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: 1.5×10⁻³ s — seven gate layers of today's electronic gate plus readout and reset, no transport — against ~5.5×10⁻² s on a transport-based machine of the Helios type [D][1]. Neighbouring empty slots: cryogenic on-chip microwave synthesis; a trap-qualified on-chip current switch with a published electric-field-noise spectrum; superconducting current traces in an ion trap.

## Verification (QCVV)

The 10⁻⁷ figure is a randomised-benchmarking number whose per-Clifford decay is comparable to slow drift, so it states as much about long-run stability and the leakage and SPAM model as about the gate [D][3]. Benchmarking here does not capture spectator crosstalk from the global far field, a.c. Zeeman shifts on neighbours, or drive-induced heating, which surfaces only in a later entangling gate. No simultaneous randomised benchmarking, crosstalk-RB or cycle benchmarking exists for a chip-integrated microwave device, and the 8.4(7)×10⁻⁵ two-qubit result has no independent replication as of 2026-09-03 [D][4]. Two source issues: the main report attributes gate durations of 225.8 µs (2025) and ≈120 µs (2024) to a paper whose abstract states neither, so those are carried as reported; and WISE's source count and layer rate are architectural estimates [S][2], not measurements.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IonQ (incl. Oxford Ionics) | developer | US / UK | Chip-integrated microwave control; electronic 2Q gate at 8.4(7)×10⁻⁵; owns WISE | [D][4], [S][2] |
| eleQtron | developer | DE | MAGIC static gradient plus global microwave; builds the QSea processor | [C][8] |
| NXP Semiconductors | supplier | NL / DE | Control and regulation electronics for the QSea demonstrators | [G][7] |
| ParityQC | supplier | AT | Architecture and algorithm layer for QSea | [G][7] |
| DLR Quantum Computing Initiative | user / funder | DE | QSea I, 2023-03-01 → 2027-02-28, demonstrator in Hamburg | [G][7] |
| SkyWater Technology | supplier (captive) | US | 200 mm foundry acquired by IonQ, closed 2026-07-31 | [G:IONQ-SKYWATER-2026] |
| Oxford (Lucas group) | research | UK | 1Q record 1.5(4)×10⁻⁷ with an on-chip microwave resonator | [D][3] |
| Universal Quantum | developer | UK | Global microwave plus magnetic gradients; no dated figure verified | — |
| Quantinuum | competitor | US | Laser control at scale, 1,228 electrodes, ≥7 wavelengths | [D][1] |
| DARPA (QBI) | funder | US | Stage A included Oxford Ionics; Stage B includes IonQ | [G:QBI-STAGEB-2025-11] |

**Money.**
- 2023-03-01 · DLR QCI with eleQtron, NXP, ParityQC · QSea I contract to 2027-02-28 · value not disclosed · active [G][7]
- 2024-05-30 · eleQtron, NXP, ParityQC · QSea I demonstrator delivered, Hamburg · no amount · delivered [C][8]
- 2025-06-09 · IonQ · M&A, Oxford Ionics · $1.075 B · closed 2025-09-17 [G:IONQ-OXIONICS-2025]
- 2025-07-08 / 2025-10-12 · IonQ · equity · $1.0 B then $2.0 B at $93/share · cash $3.0 B, Q2-2026 revenue $80.1 M · closed [G:IONQ-EQUITY-2025]
- 2025-11-06 · DARPA · QBI Stage B incl. IonQ · up to $15 M each · announced [G:QBI-STAGEB-2025-11]
- 2026-01-26 · IonQ · M&A, SkyWater · ~$1.8 B ($15.00 cash + 0.4883 shares per share) · closed 2026-07-31 [G:IONQ-SKYWATER-2026]
- 2026-05-05 · eleQtron · Series A · €57 M, €54 M backlog · closed [C][9][G:ELEQTRON-57M-2026-05]

**Market & supply chain.** The enabling equipment is microwave synthesis and amplification — AWG and direct-digital sources, GaN/GaAs amplifiers, coaxial feedthroughs — a commoditised dual-use base with almost no vendor bargaining power, unlike the narrow-linewidth-laser oligopoly the optical machines need. Concentration risk migrates upstream into multilayer trap fabrication, the segment IonQ has internalised; unit economics are undisclosed. G3 (early fault tolerance) pays through gate fidelity and G7 (deployable systems) through removal of the gate-laser optical table; G4 pays later, G1 and G6 not at all.

**IP & standards.** The relevant families are Oxford Ionics' electronic-qubit-control filings (Ballance/Malinowski lineage from 2019, now IonQ-assigned), the Siegen magnetic-gradient family behind MAGIC, and Universal Quantum's modular-microwave filings. No dated patent-database query was run, so no count is claimed; no litigation, standard or open-source stack is specific to microwave ion control.

**Roadmaps & track record.** IonQ (promised 2025-06-13 · for 2026 · 256 qubits at 99.99% · slipped to commissioning H1 2027); IonQ (promised 2025-06-13 · for 2027 · 10,000 physical qubits on one chip · no multi-zone chip-integrated microwave data as of 2026-09-03); IonQ (promised 2025-06-13 · for 2030 · 2 M physical / 40–80 k logical) [R][G:IONQ-ROADMAP]; eleQtron with DLR (promised 2023-03 · for year one · a MAGIC demonstrator in Hamburg · delivered 2024-05-30), QSea II (for 2027-02-28 · industry-ready successor · no public target) [G][7][C][8]. IonQ's gate physics leads the world and its component claims have held; its scale claims have not, the 2020 roadmap having missed 4,000 qubits by 2026 roughly 40-fold, and the architecture behind the 10,000-qubit promise is still a paper. eleQtron is small and has delivered what it contracted for, where the deliverable was a demonstrator rather than a fidelity record.

**Strategic reading.** If this works at 10³ ions, value accrues to whoever owns a qualified multilayer trap line plus an RF design team; IonQ has bought both, and NXP gives the European line the same pairing without vertical integration. The losers are the laser supply chain and the integration advantage of the optical incumbents, since Helios's 1,228 electrodes and seven wavelengths do not transfer to a microwave chip [D][1]. The substitution threat runs the other way with equal force — laser control has run 98 ions with all-to-all connectivity, microwave control two — so the node trades proven scale for a better error floor and a better wiring asymptote.

*Open niche:* the unmeasured quantities here are all QCVV quantities — no simultaneous randomised benchmarking, crosstalk-RB or cycle benchmarking on a chip-integrated microwave device, no drive-induced heating spectrum versus gate current, no calibration-drift model of the kind a 10⁻⁷ gate sustained over hours requires. A small group can own that suite without owning a trap, partnering with one of the few laboratories that have devices; the on-chip demultiplexing question is structurally digital fan-out, as in superconducting single-flux-quantum control.

## Outlook & open questions

Confirm if a device with ≥8 zones driven by chip-integrated conductors is published with simultaneous-RB crosstalk figures before 2027-12, if IonQ commissions 256 qubits at 99.99% in H1 2027 on full-register rather than pairwise benchmarking, or if eleQtron publishes a QSea II fidelity before 2027-02-28. Demote if no multi-zone device appears by end-2027, or if the first one reports drive-induced heating forcing one source per zone, since the wiring advantage then evaporates. Best case by 2029: a 10³-ion register wired by on-chip switching at ~200 sources, two-qubit error near 10⁻⁴, no gate lasers. Worst case: the records stand, the architecture does not, and microwave control survives as the single-qubit layer of an optically entangled machine.

Open questions. (1) How much anomalous heating do drive currents inject at entangling-gate gradients? (2) Can an on-chip switch operate micrometres from an ion without dielectric charging? (3) Room temperature or 4 K, given that lower heating buys no headroom for parallel drive? (4) Does frequency addressing scale past ~10 ions per chain? (5) In a static register, is the derived clock gate- or transport-limited?

## Sources

[1] Quantinuum · Helios, 98-qubit trapped-ion processor · arXiv:2511.05465; Nature, Jun 2026 · https://arxiv.org/abs/2511.05465 [D]
[2] Malinowski, Allcock, Ballance · How to wire a 1000-qubit trapped ion quantum computer · PRX Quantum 4, 040313 · 2023-05-22 · https://arxiv.org/abs/2305.12773 [S]
[3] Smith, Leu, Miyanishi, Gely, Lucas · Single-qubit gates with errors at the 10⁻⁷ level · arXiv · 2024-12-05 · https://arxiv.org/abs/2412.04421 [D]
[4] Hughes, Srinivas, Löschnauer, Knaack, Matt, Ballance, Malinowski, Harty, Sutherland · Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling · arXiv · 2025-10-20 · https://arxiv.org/abs/2510.17286 [D]
[5] IonQ · Completion of the Oxford Ionics acquisition · newsroom · 2025-09-17 · https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[6] IonQ · Completion of the SkyWater acquisition · newsroom · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[7] DLR Quantum Computing Initiative · QSea I project page · accessed 2026-09-03 · https://qci.dlr.de/en/qsea-i/ [G]
[8] NXP Semiconductors · NXP, eleQtron and ParityQC reveal their first quantum computing demonstrator · newsroom · 2024-05-30 · https://www.nxp.com/company/about-nxp/newsroom/NW-NXP-ELEQTRON-AND-PARITYQC-FIRST-QUANTUM [C]
[9] eleQtron · €57 million Series A · newsroom · 2026-05-05 · https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[10] IonQ · Accelerated roadmap · blog · 2025-06-13 · https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[11] IonQ · Second-quarter 2026 results · newsroom · 2026-08 · https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[12] DARPA · QBI Stage B selection · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[13] Jordan, Bernhardt, Rahamim, Kirichenko et al. (Seeqc) · A quantum computer controlled by superconducting digital electronics at millikelvin temperature · Nature Electronics · 2026-03-10 · https://www.nature.com/articles/s41928-026-01576-6 [D]
[14] Quantum Computing Report · Quantum Art extends Series A to $140 M · 2026-04-27 · https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]

## Open verification items

- Electronic-gate duration 225.8 µs (2025) / ≈120 µs (2024): from the main report via arXiv:2510.17286, whose abstract gives neither figure.
- Universal Quantum: DLR contract value, funding and 2025–2026 status unverified (site gave no dated figures; /news 404 on 2026-09-03).
- NIST Boulder near-field microwave gate (Ospelkaus et al., ~2011): cited as lineage only, from the standard literature without a numbered source, no number attached.
- ECCN for ion-trap microwave control chips under the September 2024 US quantum export controls: not verified.
- QSea I / QSea II contract values in EUR, patent counts for the three families, and per-qubit cost or yield for microwave trap chips: no public figure found.
