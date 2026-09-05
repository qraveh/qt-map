---
id: code_highrate
name: High-rate concatenated codes with transversal gates
layer: "7 Code"
tier: 1
status: demonstrated
since: 2024
one_line: "Many logical qubits per block (iceberg, tesseract, concatenated [[4,2,2]]), Clifford gates transversal, paid for with all-to-all connectivity and post-selection."
verdict: "The reason ions and atoms quote 48–96 logical qubits while superconducting quotes 1–2; holds only at distance 2–4 and only where acceptance stays above ~50%."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

Block codes whose rate k/n is a large fraction of unity and whose logical Cliffords run transversally — depth-one layers of two-local physical gates — instead of d rounds of lattice surgery. Four members define the node. The **iceberg code** [[k+2,k,2]] detects any single-qubit error (Quantinuum: Self, Benedetti, Amaro; Nature Physics 20, 219, 2024-07-26) [D][3]. Two-level concatenation gives [[(k₁+2)(k₂+2), k₁k₂, 4]]; **[[80,48,4]]** (k₁=6, k₂=8) is the largest cycle executed anywhere [D][1]. The **tesseract colour code [[16,6,4]]** is a doubly-even self-dual 4D CSS code from the [16,5,8] Reed–Muller code (subsystem variant [[16,4,2,4]]), its logical Clifford group depth-one [D][5]. Goto's **many-hypercube codes** concatenate [[4,2,2]] blocks to ~30% rate [S][7].

Coordinates: no carrier of its own (affinity 0.0), it inherits the platform's; no characteristic time and no entangling determinism here; no readout of its own; mobility by physical transport of the carriers, which supplies the required all-to-all; no control modality, placed nowhere; error structure as the code sees it, depolarising Pauli noise; no manufacturing.

## Physics & limits

[[80,48,4]] costs 1.67 physical qubits per logical at distance 4 [D][1], the tesseract 2.67 [D][5]; a teraquop surface code costs 650 under 0.1% noise [S][15], IBM's [[144,12,12]] 24 at distance 12 [D][16]. The comparison is not like-for-like, and that is the limitation: distance 4 corrects one error, suppression goes roughly as p², and there is no Λ-style exponential handle. Distance 2 corrects nothing — it detects, and detection means discarding.

Hence acceptance: the [[80,48,4]] cycle accepted 0.62(2) of shots after post-selecting uncorrectable errors [D][1], and the 64-logical XY-model simulation accepted 3.2% at algorithmic depth [D][8]. Acceptance falls exponentially in circuit volume, so a claim here that omits it is unreadable.

Transversality is not universality (Eastin–Knill): magic states come from outside the block — [[6,2,2]] at 7×10⁻⁵ on ions [D][12], 5-to-1 colour-code distillation on atoms [D][11]. Transversal CNOT correlates errors across blocks, so decoding must be block-wide; algorithmic fault tolerance is the compensating theory, a constant number of syndrome rounds per logical gate rather than d [S][10]. Ion leakage at 1.1×10⁻⁵ per Clifford [D][8] and atom loss are not Pauli errors, so loss-aware decoding is a precondition.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: 48 error-corrected logical qubits in one [[80,48,4]] block on a 98-qubit machine, logical gate infidelity (1.0–1.2)×10⁻⁴ against ~8×10⁻⁴ bare physical two-qubit error [D][1][8]. Typical at scale is thinner — that platform's 94 "logical" qubits are distance-2 iceberg, detection only [D][1].

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-07 | Iceberg [[k+2,k,2]]: 8 logical qubits, 256 layers, logical quantum volume 2⁸ | Quantinuum | [D][3] |
| 2024-09 | Tesseract [[16,6,4]]: graph states on 12 logical qubits, 5 correction rounds | Microsoft + Quantinuum | [D][4] |
| 2025-11 | [[16,6,4]] on 448 atoms: 96 logical qubits active, hundreds of teleportations | Harvard/MIT/QuEra | [D][2] |
| 2026-02 | [[80,48,4]]: 48 corrected logical qubits, cycle infidelity ≤4×10⁻⁵, acceptance 0.62(2) | Quantinuum Helios | [D][1] |
| 2026-06 | Carbon [[12,2,4]] + tesseract: 11×–800× logical-error improvement | Microsoft + Quantinuum | [D][4] |

The dominant budget term is the residual weight-2 error at distance 4 plus the discarded fraction: at 62% acceptance per cycle, a hundred-cycle circuit is out of reach.

## Manufacturing, materials & supply chain

No fabrication of its own; the dependency is the connectivity hardware. On ions that is the QCCD trap — Helios runs 1,228 electrodes and at least seven laser wavelengths, and Sol (2027) moves to a Honeywell-fabricated 2D grid trap [D][8][R][27]. On atoms it is AOD/SLM tweezer optics and the laser chain [D][2]. Single points of failure: ion-trap chip fabrication (Honeywell in-house; IonQ bought SkyWater's foundry, ~$1.8 B, closed 2026-07-31 [G:IONQ-SKYWATER-2026]), acousto-optic deflectors, high-power lasers. Export control attaches to the machines, not the mathematics: US EAR quantum-computer controls and EU dual-use equivalents cover traps and lasers; the codes are published and ship as software.

## Control, readout & I/O burden

The burden is decoding, not wiring. Syndrome extraction is shallow, but each transversal gate correlates errors across the block, so the decoder handles block-wide syndromes and, on atoms, loss flags, inside the reaction time. Not yet binding: ion cycles run 1–5 ms and atom cycles ~1–4.5 ms [D][8][D][2] against decoders at tens of microseconds. Pinnacle instead assumes a 1 µs cycle and 10 µs reaction time [S][6] — superconducting or photonic numbers, where real-time correlated decoding becomes the wall. At 10³ physical qubits one [[80,48,4]] block plus routing fits; at 10⁴ the constraint is all-to-all *between* blocks; at 10⁶ the family does not close without long-range couplers or bounded-degree qLDPC.

## Role in the stack

Three paths: ions with QCCD and laser gates (Quantinuum, AQT); ions with electronic gates and chip control (IonQ/Oxford Ionics, eleQtron, Quantum Art); alkali neutral atoms (Harvard/MIT, QuEra, Pasqal, Infleqtion, Google). It requires transport-supplied connectivity — AOD tweezer transport in a zoned architecture, ion shuttling through QCCD junctions and grid traps, or a single chain's motional bus — and provides for correlated, loss-aware decoding. It replaces the surface code at an explicit price: the surface code needs only nearest-neighbour coupling and has a mature ~1% threshold with exponential distance scaling, while this family needs all-to-all and buys width instead of depth, and it conflicts with nearest-neighbour connectivity outright.

Hub reading: this node explains the largest divergence in the 2026 fault-tolerance table — 48 and 96 logical qubits on ions and atoms against 1–2 on superconducting — a connectivity fact, not a qubit-quality fact. It adds no clock of its own; it sets the QEC cycles per logical layer, ≈1 with transversal gates plus correlated decoding versus ≈d for lattice surgery [S][10]. Derived clock (= sum of the syndrome round: gate layers + transport + readout + reset): 9.66 ms on the ion QCCD path, transport-set, against the ~55 ms Helios full-width layer, and 1.31 ms on the atom path against a measured ~1–4.5 ms round. Empty slots nearby: no high-rate transversal code on a nearest-neighbour platform, no member above distance 4, no magic-state factory inside a high-rate block.

## Verification (QCVV)

Headline numbers come from repeated logical preparation and measurement in both bases, post-selected on detected-but-uncorrectable events. Two cautions: the Helios ≤4×10⁻⁵ cycle figure is a confidence upper bound from zero logical errors in 5,000 shots per basis, not a measured rate [D][1]; and no number is interpretable without its acceptance [D][1][D][8]. Leakage and loss sit outside the Pauli model — IonQ's [[18,4,3]] break-even needed leakage post-selection [D][9]. Nothing here reports Λ-style distance scaling. Replication is good: the tesseract has run on two unrelated platforms [D][4][D][2].

Conflicts. The tesseract is [[16,6,4]], not [[16,4,4]] — I trust the Error Correction Zoo entry and the arXiv abstract [D][5][D][4]. "48 corrected" and "94 detected" on Helios are different codes at different distances, routinely conflated [D][1]. Iceberg's sub-100,000-qubit RSA-2048 claim assumes p=10⁻³ with 1 µs cycles [S][6], not comparable to Gidney's <1 M [S][14].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK | Introduced the iceberg code; ran [[80,48,4]] on Helios | [D][1][D][3] |
| Microsoft Quantum | developer / user | US | Co-authored the tesseract demonstrations on Quantinuum hardware | [D][4] |
| Harvard/MIT (Lukin) | research | US | [[16,6,4]] with 96 logical qubits on 448 atoms | [D][2] |
| QuEra | developer | US | Commercialises that architecture; Libra 2028 targets >256 logical | [R][G:QUERA-LIBRA-2026] |
| IonQ (incl. Oxford Ionics) | developer | US/UK | Nine codes on 40 ions incl. [[18,4,3]] break-even; Iceberg partner | [D][9][C][19] |
| Iceberg Quantum | supplier (architecture) | AU/DE/US | Only pure-play: licenses high-rate/qLDPC architectures (Pinnacle) | [S][6][P][17] |
| DARPA | funder | US | QBI Stage B funds Quantinuum, IonQ, QuEra, Atom Computing | [G:QBI-STAGEB-2025-11] |
| IBM | competitor | US | Bivariate-bicycle qLDPC is the substitution threat | [D][16] |

**Money.**
- 2025-03-24 · Iceberg Quantum · pre-seed · $2 M · Blackbird lead, LocalGlobe · closed [P][18]
- 2025-09-04 · Quantinuum · equity · $600 M at $10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G:QTM-600M-2025-09]
- 2025-09-17 · IonQ · M&A, Oxford Ionics · $1.075 B · closed [G:IONQ-OXIONICS-2025]
- 2025-11-06 · DARPA · QBI Stage B, up to $15 M each, eleven performers · announced [G:QBI-STAGEB-2025-11]
- 2026-02-13 · Iceberg Quantum · seed · $6 M · LocalGlobe lead, Blackbird, DCVC · cumulative ~$8 M · closed [P][17]
- 2026-06-03 · Quantinuum · IPO · $1.68 B gross, Nasdaq QNT; Q2-2026 revenue $8.0 M · closed [G:QTM-IPO-2026-06]
- 2026-06-16 · Atom Computing · $100 M Series C + $100 M DoC CHIPS LOI · >$300 M · closed + LOI [G:ATOM-300M-2026-06]
- 2026-07-31 · IonQ · M&A, SkyWater Technology · ~$1.8 B · closed [G:IONQ-SKYWATER-2026]

**Market & supply chain.** Nobody sells a code. Value accrues to machine vendors that can quote logical-qubit counts (Quantinuum, QuEra, Atom/Microsoft), to one architecture licensor (Iceberg Quantum [C][19]), and to the decoder layer (Riverlane, NVIDIA's NVQLink transport [G:NVQLINK-2025]). Concentration risk is extreme: the experimental record rests on three groups and two hardware families, one of which authored both the code and the machine. Unit economics are the rate — 1.67 physical per logical at d=4 [D][1] against 650 for a teraquop surface code [S][15]. Goals paid for: **G3** primarily, **G2** (bare iceberg as a cheap detection layer [D][3]), **G7** where a machine is sold in logical qubits, **G4** only if concatenation beyond d=4 survives leakage.

**IP & standards.** The iceberg code is published (Nature Physics 2024) [D][3] and the tesseract catalogued in the open Error Correction Zoo [P][5]; Microsoft and Quantinuum publish jointly rather than cross-licensing visibly [D][4]. Pinnacle is a preprint with no disclosed patent position [S][6]. No dated patent count exists for this code family — the PatSnap figures cited are device-class [P][G:PATSNAP-2026-06]. Tooling is open; no standards body governs code choice.

**Roadmaps & track record.** Quantinuum (promised 2024-09 · Sol 2027 ~100 logical, Apollo 2029 · Helios on schedule 2025-11, [[80,48,4]] delivered 2026-02) [R][G:QTM-ROADMAP] — credible; code results ran ahead of the hardware. QuEra/Harvard (promised 2024-01 · 100 logical in 2026 · slipped to Libra 2028) [R][G:QUERA-LIBRA-2026] — the 96 logical qubits were physics, not product. IonQ (promised 2025-06 · 25–50 physical per logical by 2030) [R][G:IONQ-ROADMAP] — needs high-rate codes; its 2020 roadmap missed 2026 by ~40×. Iceberg Quantum (promised 2026-02 · partners at utility scale in 3–5 years) [P][17] — seed-stage, no hardware.

**Strategic reading.** Winners: all-to-all platforms and anyone selling logical-qubit counts. Losers: 2D-local platforms, which must buy long-range couplers to compete on rate. The substitution threat is near — bounded-degree qLDPC gets most of the rate *and* real distance scaling without all-to-all [D][16]; if IBM's gross-code module works in 2026–27, this family retreats to cheap distance-2/4 detection. Bargaining power sits with hardware vendors; a code-architecture supplier has none unless its IP proves essential.

*Open niche:* measurement discipline here is weak in a way that suits a small QCVV house. Nobody has published a standard for acceptance-weighted logical performance — an acceptance-versus-volume curve, logical layer fidelity under block load, and whether a headline number is a measured rate or a zero-error confidence bound (the Helios ≤4×10⁻⁵ is the latter [D][1]). A protocol making those mandatory, plus a decoder harness injecting loss and leakage rather than Pauli noise, would be usable by every actor above.

## Outlook & open questions

**Confirm** within 12–24 months if: a distance-6 or -8 member of the concatenated iceberg family runs with acceptance above 0.5 (Sol, 2027); a high-rate block is sustained over ≥50 QEC cycles without post-selection; or a partner names Pinnacle in a published roadmap by end-2027. **Demote** if 2027 machines still quote logical counts only at single-digit-percent acceptance at depth, or if IBM's gross-code module matches the rate at distance 12 on degree-≤7 connectivity. Best case by 2029: Apollo- and Libra-class machines run hundreds of logical qubits at constant syndrome rounds per logical gate [S][6][S][14]. Worst case: the family stays a detection layer and bounded-degree qLDPC takes the fault-tolerant road.

Open questions: (1) does concatenation to d≥6 keep the rate advantage once leakage and loss are modelled honestly? (2) can a magic-state factory live inside a high-rate block? (3) what is the true acceptance scaling with circuit volume? (4) can block-wide loss-aware decoders keep up at 1 µs cycles? (5) is any nearest-neighbour route cheaper than long-range couplers? Watch Sol's first logical results, Quantinuum's unpublished "near five-nines" code-family claim, IBM Kookaburra, and the first partner adoption of Pinnacle.

## Sources

[1] Quantinuum · "Computing with many encoded logical qubits beyond break-even" (concatenated iceberg codes on Helios) · arXiv:2602.22211 · 2026-02 · https://arxiv.org/abs/2602.22211
[2] Bluvstein et al. (Harvard/MIT/QuEra) · "Architectural mechanisms of a universal fault-tolerant quantum computer" · Nature · 2025-11 · https://www.nature.com/articles/s41586-025-09848-5 (preprint arXiv:2506.20661)
[3] C. N. Self, M. Benedetti, D. Amaro (Quantinuum) · "Protecting expressive circuits with a quantum error detection code" · Nature Physics 20, 219–224 · published 2024-07-26 · https://arxiv.org/abs/2211.06703
[4] A. Paetznick, B. W. Reichardt, M. P. da Silva, C. Ryan-Anderson et al. (Microsoft Quantum; Quantinuum) · "Improved quantum processor logical error rates via correction and detection" · Nature 654 (8118) · 2026-06-10 · https://www.nature.com/articles/s41586-026-10628-y (preprint arXiv:2409.04628, 2024-09-06)
[5] Error Correction Zoo [P] · "[[16,6,4]] tesseract color code" · accessed 2026-09-03 · https://errorcorrectionzoo.org/c/stab_16_6_4
[6] P. Webster, L. Berent, O. Chandra, E. T. Hockings, N. Baspin, F. Thomsen, S. C. Smith, L. Z. Cohen (Iceberg Quantum) · "Pinnacle" fault-tolerant architecture · arXiv:2602.11457 · 2026-02-12 (rev. 2026-05-05) · https://arxiv.org/abs/2602.11457
[7] H. Goto (Toshiba) · "Many-hypercube codes: high-rate quantum error-correcting codes for high-performance fault-tolerant quantum computation" · Science Advances 10, eadp6388 · 2024 · https://arxiv.org/abs/2403.16054
[8] Quantinuum · Helios system paper · arXiv:2511.05465 · Nature 2026-06 · https://www.nature.com/articles/s41586-026-10676-4
[9] IonQ · "Breakeven demonstration of quantum low-density parity-check codes" · arXiv:2606.06455 · https://arxiv.org/abs/2606.06455
[10] H. Zhou et al. · "Algorithmic fault tolerance for fast quantum computing" · arXiv:2406.17653 · https://arxiv.org/abs/2406.17653
[11] Harvard/MIT/QuEra · "Experimental demonstration of logical magic state distillation" · Nature · 2025 · https://www.nature.com/articles/s41586-025-09367-3
[12] Quantinuum · magic states in the [[6,2,2]] code · arXiv:2506.14688 · https://arxiv.org/abs/2506.14688
[13] Neutral-atom fault-tolerant architecture study (transversal; RSA-2048 resource estimate) · arXiv:2505.15907 · https://arxiv.org/abs/2505.15907
[14] C. Gidney (Google) · "How to factor 2048-bit RSA integers with less than a million noisy qubits" · arXiv:2505.15917 · 2025-05-21 · https://arxiv.org/abs/2505.15917
[15] C. Gidney, C. Jones (Google) · teraquop footprint, surface vs colour codes · arXiv:2312.08813 · 2023-12-14 · https://arxiv.org/abs/2312.08813
[16] S. Bravyi et al. (IBM) · "High-threshold and low-overhead fault-tolerant quantum memory" ([[144,12,12]] gross code) · Nature 627, 778 · 2024-03-27 · https://arxiv.org/abs/2308.07915
[17] The Quantum Insider [P] · "Iceberg Quantum unveils Pinnacle architecture … and raises $6 million seed round" · 2026-02-13 · https://thequantuminsider.com/2026/02/13/trifecta-iceberg-quantum-unveils-pinnacle-architecture-claims-sub-100000-qubits-could-break-rsa-2048-and-raises-6-million-seed-round/
[18] HPCwire [P] · "Iceberg Quantum launches with $2M and PsiQuantum partnership" · 2025-03-24 · https://www.hpcwire.com/off-the-wire/iceberg-quantum-launches-with-2m-and-psiquantum-partnership/
[19] Iceberg Quantum [C] · company site: founders and hardware partners (PsiQuantum 2025-03, Oxford Ionics 2025-07, Diraq 2025-08) · accessed 2026-09-03 · https://www.iceberg-quantum.com/
[20] Honeywell · "$600 million capital raise for Quantinuum at $10B pre-money" · 2025-09-04 · https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale
[21] Quantinuum · IPO pricing, 2026-06-03 · https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering ; Q2-2026 results · https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results
[22] IonQ · completion of Oxford Ionics acquisition · https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum ; completion of SkyWater acquisition · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
[23] QuEra · $230 M financing · https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing ; Libra 2028 roadmap · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[24] Atom Computing · ">$300 million" raise including DoC letter of intent · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html ; QuNorth "Magne" order · https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/
[25] DARPA · QBI Stage B selection · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[26] IonQ · accelerated roadmap · 2025-06-13 · https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality
[27] Quantinuum · accelerated roadmap (Helios → Sol → Apollo) · 2024-09-10 · https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030
[28] Atom Computing/Microsoft · toric-code logical qubits with continuous reloading · arXiv:2606.04079 · https://arxiv.org/abs/2606.04079

## Open verification items

- Iceberg Quantum's headquarters: trade press describes a Berlin base with a US presence while the founding institution is the University of Sydney [P][17][C][19]; the company site gives no location. Recorded AU/DE/US, unresolved.
- Acceptance for the Harvard [[16,6,4]] 96-logical-qubit runs is not quoted in the sources consulted; only the ion-side figures (0.62(2), 3.2%) are verified.
- Quantinuum's Q2-2026 call claim of "near five-nines logical fidelity with a novel code family" has no public paper as of 2026-09-03; whether it refers to this family is unverified.
- No dated patent-database count exists for this code family; the PatSnap figures cited are device-class only.
- Goto's many-hypercube codes have no hardware demonstration found; the 30% rate (64 logical in 216 physical) is simulation only [S][7].
