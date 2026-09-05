---
id: dec_corr
name: Correlated / loss-aware decoding (transversal, atom loss)
layer: "8 Decoder"
tier: 3
status: demonstrated
since: 2025
one_line: Decoders that consume atom-loss heralds as located erasures and decode across transversal gate layers instead of round-by-round.
verdict: Real on one dataset (1.73(13)× over a loss-blind decoder, 448 atoms, four rounds); unproven under reloading, at depth, or in a second lab.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Not hardware, a decoding discipline. Loss-aware decoding consumes the herald: a missing atom is an erasure at a known site, so stabilizers touching the vacancy multiply into higher-weight *supercheck* operators that still commute with the surviving code [1]. Correlated decoding solves the joint syndrome history across transversal (block-to-block) layers rather than block-by-block; Cain et al. (Harvard, 2024-03-05) showed the rounds between Clifford gates drop O(d)→O(1) [2], generalised as algorithmic fault tolerance (Nature 2025) [3].
f = loss + erasure; a/c/d/e/g = none — classical compute, no fab or placement [graph].

## Physics & limits
The herald is the asset: >80% of Rydberg-array leakage is atom loss, and imaging finds it [1]. A located erasure costs the decoder only the Pauli frame, not the position — why erasure conversion lifts circuit-level thresholds 3–4× at fixed gate physics [4]. The price is distance: each supercheck is a product of two stabilizers, so every vacancy locally thins the code. Correlated decoding pays differently: transversal CNOTs propagate errors between blocks, so the graph grows with circuit depth, not d. Nothing moves the floor — the unheralded residual is untouched, m_F leakage 0.008(1)% per atom per gate against atom loss 0.087(5)% [G:HARVARD-CZ-2026-04].
## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-11-10 | 1.73(13)× gain from loss flags + ML over conventional decoding, same 448-atom data | Harvard/MIT/QuEra | [D][1][G:HARVARD-LOSS-QEC-2025] |
| 2026-03 | Correlated-loss decoder: 4% threshold vs 3.2% assuming independent loss; 144 µs/round; simulation | QPerfect | [S][5][G:QPERFECT-CORRLOSS-2026-03] |
| 2026-06-12 | [[4,2,2]] ¹⁷¹Yb: unconditional decay 1.9(4)× slower with erasure information (3.6(1)× is the post-selected hold) | Princeton | [D][6][G:PRINCETON-ERASURE-RESOLVED-2026-09] |

Same circuit: 2.14(13)×, d=3→5, four rounds. Dominant term: atom loss, not Pauli error.

## Manufacturing, materials & supply chain
No fab: classical compute already bought for matching. Latency sets scope: 144 µs/round fits a 1–4.5 ms atom cycle with 7–30× margin [5] but is ~130× over a 1.1 µs superconducting cycle — why this stays atom-specific. Loss-flag bandwidth is one bit per site per round, so the wall at 10³–10⁴ atoms is the ~0.5–1 ms imaging and a decode window scaling with logical depth, not the link. Inherited single points of failure: Hamamatsu qCMOS imaging [G:HAMAMATSU-CAMERA-CONC-2026] and two AOD vendors [G:AOD-VENDORS-2026].

## Role in the stack
Requires high-rate concatenated codes with transversal gates; provides the decoding half of algorithmic fault tolerance, whose constant-round claim is otherwise unbacked on hardware. Derived clock = max(gate 270 ns, readout ~1 ms, transport ~100 µs) ≈ 1 ms, ~1.0 kHz; the decoder must return inside it, not set it. Verification: 1.73× is a decoder-vs-decoder ratio on one lab's data, unreplicated; 4% is simulation [5].  Four rounds test neither drift nor reloading; Atom Computing's toric code is the control, suppression vanishing with reloading (0.63% vs 0.64% per cycle) [7]. Princeton's 1.9(4)×/3.6(1)× discrepancy is resolved: one paper, two quantities [G:PRINCETON-ERASURE-RESOLVED-2026-09].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly | Evidence |
|---|---|---|---|---|
| Harvard/MIT | research | US | Correlated decoding, superchecks, 1.73(13)× | [D][1][2] |
| QuEra | developer | US | Co-author; Libra 2028 assumes it | [D][1][C][8] |
| QPerfect (BTQ) | supplier | FR | Correlated-loss decoder; aQCess twin | [S][5][C][10] |
| Atom Computing | user | US | Erasure-native Yb; reloading counter-example | [D][7][C][11] |

**Money.**
2025-04-09 · BTQ Technologies · €2 M into QPerfect at €10 M pre-money (16.67%) · term sheet [P][9]
2026-07-22 · QPerfect · aQCess twin, Equipex+ ANR-21-ESRE-0032 · announced [C][10]
2026-06-16 · Atom Computing · $100 M Series C (Third Point) + $100 M CHIPS LOI · closed + LOI [C][11][G:ATOM-300M-2026-06]
2025-11-06 · DARPA QBI Stage B · Atom Computing, QuEra among eleven · ≤$15 M each [G:QBI-STAGEB-2025-11]

**Market & supply chain.** No component market: GPU/FPGA cycles already bought for matching; concentration risk sits upstream, in imaging and AODs. Pays G3/G4 only.

**IP & standards.** No dated patent family names loss-aware or correlated decoding as of 4 Sep 2026; methods open, code academic.

**Roadmaps & track record.** O(d)→O(1) rounds (2024-03): in Nature 2025, shown only in a four-round circuit. QuEra 100 logical (2024-01, for 2026): now Libra 2028 [G:QUERA-LIBRA-2026]. Physics on time, products late.

**Strategic reading.** If it holds, atoms turn their worst liability into a cheap accounted channel and transversal architectures beat lattice surgery on space-time cost: QuEra, Atom Computing, Pasqal and Infleqtion gain, superconducting vendors lose decoder latency as a differentiator. Substitution threat: a Rydberg CZ past 99.95% shrinks the loss term. Non-rival: no supplier can rent it.

*Open niche:* both headline numbers are ratios against a baseline the same team chose; a QCVV shop with no atom hardware can re-derive the 1.73× against an optimal loss-blind decoder on published syndrome data and stress the 4% threshold under reloading.

## Outlook & open questions
Confirm if the QPerfect decoder runs on real syndromes or a second vendor publishes its own loss-aware gain; demote if the gain dies under reloading or past four rounds. Best case 2029: default across neutral-atom FT stacks; worst case, one group's architecture, never past 10³ atoms. Open: does 1.73× hold at 10⁴ atoms, at depths where the correlated graph outgrows memory, and on ions [12]?

## Sources
[1] Bluvstein et al. (Harvard/MIT/QuEra), "Architectural mechanisms of a universal fault-tolerant quantum computer", Nature 649, 39, 2025-11-10 (arXiv:2506.20661) — https://www.nature.com/articles/s41586-025-09848-5
[2] Cain, Zhao, Zhou, Meister, Bonilla Ataides, Jaffe, Bluvstein, Lukin, "Correlated decoding of logical algorithms with transversal gates", arXiv:2403.03272, 2024-03-05 (rev. 2025-04-07) — https://arxiv.org/abs/2403.03272
[3] Zhou, Zhao, Cain, Bluvstein, Maskara, Duckering, Hu, Wang, Kubica, Lukin, "Low-overhead transversal fault tolerance for universal quantum computation", Nature, 2025, doi 10.1038/s41586-025-09543-5 (arXiv:2406.17653) — https://arxiv.org/abs/2406.17653
[4] Wu, Kolkowitz, Puri, Thompson, "Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays", arXiv:2201.03540, 2022-01 — https://arxiv.org/abs/2201.03540
[5] Perrin, Roger, Pupillo (Univ. Strasbourg/CNRS, QPerfect SAS), "Correlated atom loss as a resource for quantum error correction", arXiv:2603.24237, 2026-03 — https://arxiv.org/html/2603.24237
[6] Princeton, [[4,2,2]] metastable ¹⁷¹Yb erasure conversion, Nature Physics 22, 910, 2026-06-12 (arXiv:2506.13724v2) — https://arxiv.org/html/2506.13724v2
[7] Atom Computing/Microsoft, toric code with continuous reloading, arXiv:2606.04079, 2026-06 — https://arxiv.org/abs/2606.04079
[8] QuEra, $230 M financing round, press release [C] — https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing
[9] The Quantum Insider, "BTQ Technologies to invest over $2 million in QPerfect", 2025-04-09 [P] — https://thequantuminsider.com/2025/04/09/btq-technologies-to-invest-over-2-million-in-qperfect-to-advance-neutral-atom-quantum-computing/
[10] BTQ Technologies / QPerfect and University of Strasbourg, aQCess partnership, PR Newswire, 2026-07-22 [C] — https://www.prnewswire.com/news-releases/btq-technologies-qperfect-subsidiary-and-the-university-of-strasbourg-partner-to-support-frances-first-public-neutral-atom-quantum-computing-platform-302831874.html
[11] Atom Computing, raise of more than $300 M including a $100 M DoC letter of intent, 2026-06-16 [C] — https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[12] Microsoft Quantum + Quantinuum, [[16,6,4]] tesseract code, Nature 654, 2026-06-10 — https://www.nature.com/articles/s41586-026-10628-y
[G] Bluvstein et al. (Harvard/MIT/QuEra), Nature 649, 39 (online 2025-11-10; arXiv:2506.20661, 2025-06-25): surface code on up to 448 atoms, 2.14(13)× below threshold in a four-round c… · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[G] Evered, Xu, Li, Geim, Bonilla Ataides, Kalinowski, Bluvstein, Maskara, Kokail, Greiner, Vuletic, Lukin (Harvard/MIT), "High-fidelity entangling gates and nonlocal circuits with neu… · 2026-04-28 · https://arxiv.org/abs/2604.25987
[G] Perrin, Roger, Pupillo (Univ. Strasbourg/CNRS, QPERFECT SAS), "Correlated Atom Loss as a Resource for Quantum Error Correction", arXiv:2603.24237 (2026-03): fast correlated-loss de… · 2026-03 · https://arxiv.org/html/2603.24237
[G] CONFLICT RESOLVED: the 1.9(4)x and 3.6x figures both appear in arXiv:2506.13724v2 (Princeton [[4,2,2]] metastable 171-Yb) and describe different quantities — the logical decay rate… · 2026-09-04 · https://arxiv.org/html/2506.13724v2
[G] Hamamatsu Photonics ORCA-Quest qCMOS is the named single-photon-sensitivity camera in the Harvard/QuEra 448-atom fluorescence-imaging line and in MIT, NIST/UMD and Osaka neutral-at… · 2026-09 · https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html
[G] Only two acousto-optic deflector suppliers are named across the sourced neutral-atom literature: AA Opto-Electronic (France; DTSX-400 crossed AODs in the Harvard 448-atom system, a… · 2026-09-04 · https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers
[G] QuEra: Libra fault-tolerant system 2028 (>256 logical, 10⁻⁶, on Braket) and gigaquop system 2028–29 — its Jan-2024 roadmap had promised 100 logical qubits in 2026 · 2026-06-15 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[G] Atom Computing: $100 M Series C (Third Point) plus $100 M DoC CHIPS LOI, total > $300 M, 2026-06-16 · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[G] DARPA QBI Stage B (announced 2025-11-06, ~12 months, up to $15 M each): Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon… · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
## Open verification items
- The 1.73(13)× gain is unreplicated outside the Harvard/MIT/QuEra 448-atom dataset, and its baseline decoder was the same team's choice.
- The QPerfect 4% vs 3.2% threshold is simulation only; no hardware-syndrome test found as of 4 Sep 2026.
- BTQ's option to acquire QPerfect in full was exercised between 2025-04 and 2026-07 (the later release calls QPerfect wholly owned); no dated closing or price found.
- No dated patent family found for loss-aware or correlated decoding.
