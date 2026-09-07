---
id: g_cr
name: Cross-resonance (fixed-frequency, all-microwave)
layer: "3 Gate mechanism"
status: demonstrated
since: 2011
one_line: All-microwave entangling gate driving one fixed-frequency transmon at its neighbour's frequency through a static bus; no flux line, no tunable coupler.
verdict: Superseded on IBM's own fleet at Heron (2023-12) yet still the only two-qubit gate needing zero coupler control; it returns only if post-fabrication frequency trimming beats a flux DAC per coupler on cost.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Driving a control transmon at its neighbour's frequency through a fixed bus produces a ZX interaction; Chow, Córcoles, Gambetta et al. (IBM), 2011 [D][1]. Kandala et al. reached CNOT 99.77(2)% in a single 180 ns pulse in 2021 by suppressing the static ZZ intrinsically, two fixed-frequency coupling elements retuning the dressed levels rather than extra cancellation drives [D][2].
Coordinates: fabricated carrier, static connectivity, microwave control at room temperature; deterministic entangling at 10^-6.5 s (~320 ns typical, 180 ns best).
Coherent plus Pauli error; standard superconducting lithography, no added process.

## Physics & limits
The ZX rate is second order, ∝ JΩ/(Δ(Δ+α)), fastest in the straddling regime −α < Δ < 0, so the detuning must sit inside a band of order the anharmonicity, ~300 MHz. The static ZZ, ∝ 2J²α/(Δ(Δ+α)), never switches off, so coherent error dominates the budget. The floor is not one pair but frequency targeting: every neighbour adds a collision constraint inside that band, and junction spread as fabricated is of order a per cent, so collision-free yield collapses with lattice size. What moves the floor is post-fabrication trimming — annealing junctions to target, 97.4% success [D][7] — not better pulses.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2011 | First all-microwave CR entangling gate | IBM | [D][1] |
| 2021-09-22 | CNOT 99.77(2)% in a single 180 ns pulse | IBM | [D][2] |
| 2026-06-25 | Fixed-frequency lattice patch, CNOT > 98% simulated | Hanyang University | [S][4] |

No fleet-average CR number was ever published; IBM's EPLG today (3.7×10⁻³ [D][10]) is Heron hardware, which replaced CR in 2023-12 [C][5]. The painful reference is Oxford/OQC's fixed-coupling CZ, 99.8% in 25 ns [C][6] — no coupler control either, seven times faster.

## Manufacturing, materials & supply chain
No process of its own. The cost lands in binning and trimming: a collision cannot be detuned away after fabrication, only masked in software or annealed out, so frequency targeting — laser annealing at IBM, alternating-bias annealing at Rigetti [D][7] — is the supply-chain item CR drives. Its advantage is the I/O ledger: one drive line per qubit and nothing per coupler, where tunable couplers add a flux line and a DAC channel each, roughly 1.5–2× the lines. At 10³ that is a crowded fridge against an impossible one; at 10⁴–10⁶ it is the whole wiring budget. Export exposure is the carrier's (ECCN 3A901).

## Role in the stack
The fixed-frequency branch of the superconducting-transmon path — IBM Falcon through Condor, 2019–2023 [C][5] — providing entanglement with no coupler control; its alternative is the tunable coupler, and switching is a chip redesign, not firmware. On the derived clock it loses: 180–500 ns against ~50 ns for a tunable-coupler CZ, so every QEC cycle pays 3–7× on the gate layer. Verification: 99.77% is interleaved RB on an isolated pair, blind to spectators; CR error is coherent, so RB understates it and gate-set tomography is the honest measurement.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| IBM | developer (ex-user) | US | Invented and scaled CR to Condor; retired it at Heron | [D][2] |
| Hanyang University | research | KR | Fixed-frequency lattice-patch design reviving CR | [S][4] |
| OQC | developer | UK | Fixed-frequency coaxmons with a fixed-coupling CZ, not CR | [C][6] |

**Money.**
2026-06-02 · IBM · investment commitment · > $10 B over five years · announced [G][8][G:IBM-10B-2026-06]
2026-06-03 · OQC · Series C · £260 M · Bullhound lead · closed [C][9][G:OQC-SERIESC-2026-06]

No funding event or QBI stage names cross-resonance.

**Market & supply chain.** No incremental supplier: the same lithography, cryostat and coax chain, minus per-coupler flux electronics. It paid for G1 and early G2 only.

**IP & standards.** IBM holds the foundational family (Chow 2011, Kandala 2021); no dated CR-specific patent count was found as of 2026-09-04. Qiskit still ships CR as a native two-qubit template.

**Roadmaps & track record.** IBM (2022-05-10 · no long-term CR commitment · retired on schedule at Heron, 2023-12 [G:IBM-ROADMAP-2022]). Hanyang (2026-06-25 · simulation only · nothing fabricated). IBM's record is good precisely because it dropped CR when yield turned.

**Strategic reading.** Nobody wins from CR's supersession except tunable-coupler and cryogenic-control vendors. Its residual value is cheap wiring: if annealing reaches near-unity frequency-targeting yield, a fixed-frequency chiplet undercuts a tunable-coupler chip on cost. Power now sits with the control-electronics vendors — what CR was designed to avoid.

*Open niche:* CR's error is coherent and spectator-dependent, so the useful QCVV product is spectator-aware characterisation — gate-set tomography resolving residual ZZ against neighbour state — before anyone commits silicon to fixed-frequency revivals.

## Outlook & open questions
Confirm by 2028: a fabricated fixed-frequency processor above eight qubits with CR fidelity published under simultaneous operation, or the Hanyang patch measured above 98%; else demote to legacy. Best case 2029: a cheap fixed-frequency chiplet; worst case, CR survives only as a Qiskit compilation target. Does anyone outside IBM run CR in production? Does frequency targeting reach collision-free yield past ~100 qubits? Would a foundry pick CR on cost rather than physics?

## Sources
[1] Chow, Córcoles, Gambetta et al. (IBM), "Simple All-Microwave Entangling Gate for Fixed-Frequency Superconducting Qubits", Phys. Rev. Lett. 107, 080502, 2011 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.107.080502
[2] Kandala, Wei, Srinivasan, Magesan, Carnevale, Keefe, Klaus, Dial, McKay (IBM), "Demonstration of a High-Fidelity CNOT Gate for Fixed-Frequency Transmons with Engineered ZZ Suppression", Phys. Rev. Lett. 127, 130501, 2021-09-22 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501
[3] Zuchongzhi 3.0 (tunable couplers, contrast case), Phys. Rev. Lett. 134, 090601 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.090601
[4] Kim, Kang, Kwon (Hanyang University), "Lattice patch structure for fixed-frequency transmon quantum computer with high-fidelity CNOT gates", arXiv:2606.27017, 2026-06-25 [S] — https://arxiv.org/abs/2606.27017
[5] IBM Quantum roadmap [C] — https://www.ibm.com/roadmaps/quantum/
[6] Oxford (Leek Lab) / OQC, fixed-coupling CZ at 99.8% in 25 ns, 2025-03-21 [C] — https://oqc.tech/company/newsroom/oxford-research-group-demonstrate-fundamental-speed-up-of-two-qubit-gate
[7] Pappas, Field, Kopas et al. (Rigetti), "Alternating bias assisted annealing of amorphous oxide tunnel junctions", Communications Materials 5, 150, 2024-08-12 — https://www.nature.com/articles/s43246-024-00596-z
[8] IBM, "$10 billion investment FAQ", 2026-06-02 — https://www.ibm.com/quantum/blog/10-billion-investment-faq
[9] OQC, Series C, 2026-06-03 [C] — https://oqc.tech/company/newsroom/series-c
[10] IBM Quantum, "What's new Q2 2026" (fleet EPLG) — https://www.ibm.com/quantum/blog/whats-new-q2-2026

## Open verification items
No fleet-average CR fidelity for IBM's pre-Heron generations (Falcon–Condor) was ever published; only the isolated-pair 99.77(2)% is sourced.
No CR-specific patent count from a named database was found as of 2026-09-04.
The PRL by Kandala et al. reports intrinsic ZZ suppression through two fixed-frequency coupling elements, not active cancellation.
