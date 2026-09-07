---
id: code_aft
name: Algorithmic FT / transversal architectures
layer: "7 Code"
status: emerging
since: 2025
one_line: Replacing O(d) syndrome-extraction rounds per logical gate with a constant number, via transversal block-to-block gates plus correlated decoding.
verdict: The transversal half is measured on atoms and ions; the correlated-decoding half is a proof plus simulation. No run has closed transversal gate, correlated decode and feed-forward in real time.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Algorithmic fault tolerance, introduced by Zhou, Bluvstein, Kubica, Lukin and co-workers as a preprint in June 2024 and published in Nature in 2025 [D][1], runs logical gates transversally between code blocks and decodes the algorithm's whole syndrome history jointly, so a logical gate costs a constant number of extraction rounds rather than the O(d) lattice surgery needs.

Mobility: it presumes a machine that can bring any two blocks into register — tweezer transport or ion shuttling — not a fixed lattice. Error structure: no new channel — the code's own Pauli and erasure noise, atom loss dominant, with physical-cycle overhead traded for classical decoding overhead.

## Physics & limits
The d-round rule exists because one round cannot distinguish a measurement error from a data error; repeating the syndrome circuit d times makes the detector graph's space-time distance equal the code distance. That redundancy is only needed when each block is decoded alone: a transversal CNOT maps a fault in one block to its partner in the other, so the joint graph across blocks and time still has distance d after O(1) rounds — if the decoder uses it. The proof bounds deviation from the ideal logical measurement distribution as exponentially small [D][1].

The cost moves to the classical side, structurally. The joint graph does not factorise, so the sliding window that keeps per-block decoding local in time is no longer exact: the decoder spans several logical gates, cannot close its window until the next feed-forward point, and its work grows with the blocks entangled since the last measurement, not with d.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-06 | O(d) → O(1) rounds per logical gate, >10× space-time reduction (proof, simulation) | Harvard/QuEra | [D][1] |
| 2025-05 | RSA-2048 in 5.6 days on 19 M atoms at a 1 ms cycle, ~50× faster than comparable | Harvard/QuEra | [S][3] |
| 2025-11 | 448 atoms: transversal CNOTs, hundreds of teleportations, 96 logical qubits | Harvard/QuEra | [D][2] |
| 2026-03 | Shor with 10,000 atoms (26,000 for speed): P-256 in days, RSA-2048 far longer | Harvard/Caltech | [S][4] |
| 2026-06 | [[16,6,4]] tesseract code, transversal logical Cliffords, on trapped ions | Quantinuum | [D][6] |

Every reported gain is simulation or an offline decode of stored syndromes: no published run closes the loop — transversal gate, correlated decode, feed-forward — in real time.

## Manufacturing, materials & supply chain
An architecture and decoding layer with no process, yield or unit cost. Its supply-chain exposure is second-hand but specific: crossed acousto-optic deflectors, where AA Opto-Electronic and Gooch & Housego are the only vendors named in the 448-atom work [D][2], and the classical hardware running the decode. NVIDIA's NVQLink sets the yardstick at 3.84 µs round trip and 67 µs median BP-OSD decode — on the far easier per-block problem [C][7].

## Control, readout & I/O burden
No new laser, control line or detector; the burden is classical and real-time. A correlated decoder must ingest syndromes from every block touched by a transversal gate and return a correction before the next feed-forward point — within milliseconds on atoms, on a graph 10²–10³× larger than the single-block problem GPUs handle now. At 10³ logical qubits the evidence is simulation; at 10⁴–10⁶ no latency model has been published, and both resource estimates assume decoding keeps up [S][3][S][4]. That assumption, not atom count, is where this fails if it fails.

## Role in the stack
It applies on any path that can move qubits: the alkali neutral-atom path (QuEra, Pasqal, Infleqtion, Atom Computing) and — though the graph record models it as atoms-only — the trapped-ion shuttling path, where Quantinuum runs the same [[16,6,4]] code transversally [D][6]. It requires transport plus correlated, loss-aware decoding, and conflicts with fixed nearest-neighbour lattices, which cannot pair arbitrary blocks without a routing layer. It adds no term to the derived clock but multiplies it, cutting rounds per logical gate from ~d (at d = 7 on atoms, ~9 ms per gate) to O(1). Neighbouring empty slot: a real-time correlated decoder.

## Verification (QCVV)
Transversal gates and 96 active logical qubits are hardware measurements [D][2]; the >10× reduction is a theorem plus simulation [D][1], unreproduced outside the author group. The two resource estimates differ by three orders in space — a trade curve, not a contradiction: 19 M atoms buys RSA-2048 in 5.6 days [S][3], while 10,000–26,000 atoms buys P-256 in days and RSA-2048 one to two orders slower [S][4]; "RSA-2048 with 10,000 atoms" is what neither paper says. The sharpest counter-evidence is Atom Computing and Microsoft's toric code: Λ_Z ≈ 1.9 but Λ_X ≈ 1.2, average 1.30 over four cycles, and with reloading over 90 rounds suppression vanished (0.63% versus 0.64% per cycle) [D][5]. Atoms have not shown sustained below-threshold memory, and constant-round fault tolerance is a claim about long algorithms.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do here | Evidence |
|---|---|---|---|---|
| Harvard | research | US | Originated the scheme; 448-atom transversal demo | [D][1][2] |
| QuEra | developer | US | Co-author and hardware; Libra 2028 needs the gain | [C][G:QUERA-LIBRA-2026] |
| Quantinuum | developer | US/UK | Transversal logical Cliffords on ions, same code | [D][6] |
| Atom Computing | developer | US | Zoned transport; published the counter-result | [D][5] |
| Google Quantum AI | developer | US | Neutral-atom track since 2026-03, QEC-focused | [C][8] |
| Pasqal | developer | FR | Transport architecture, 100 logical by 2029 | [C][G:PASQAL-SPAC-2026-08] |

**Money.** 2025-09-09 · QuEra · round · $230 M+ · Google, SoftBank Vision Fund 2, NVentures · closed [G][10][G:QUERA-230M-2025]. 2025-11-06 · Atom Computing and QuEra · QBI Stage B · ≤$15 M each · active [G][15][G:QBI-STAGEB-2025-11]. 2026-02-17 · Infleqtion · IPO · >$550 M · NYSE INFQ [G][12]. 2026-05-21 · Atom Computing and Infleqtion · CHIPS LOI · $100 M each · US Commerce · non-binding [G][14][G:CHIPS-LOI-2026-05]. 2026-06-16 · Atom Computing · Series C · $100 M, Third Point [G][11][G:ATOM-300M-2026-06]. 2026-08-28 · Pasqal · SPAC · ~$360 M cash · Nasdaq PSQL [G][13][G:PASQAL-SPAC-2026-08].

**Market & supply chain.** Nothing is sold under this name; it multiplies someone else's machine, so rent accrues to the transport optics and the decoder stack. It pays for G3, cutting physical-per-logical from ~10³ toward ~10², and for G4 if it holds; nothing for G1 or G5.

**IP & standards.** The founding work is peer-reviewed in Nature and open on arXiv, as is the ISCA resource analysis; no patent family specific to algorithmic fault tolerance or correlated decoding was found as of 2026-09-04.

**Roadmaps & track record.** QuEra: Libra promised 2026-06-15 for 2028 (>256 logical, 10⁻⁶) after a January 2024 promise of 100 logical qubits in 2026 — a two-year slip, so the schedule now leaning on constant-round fault tolerance has been reset once [R][9][G:QUERA-LIBRA-2026]. Pasqal: 10,000 physical slipped 2026 to 2028 [R][G:PASQAL-SPAC-2026-08]. Every atom roadmap past 2027 prices in this gain; none names it as a dependency.

**Strategic reading.** If it holds at scale, every transport-capable vendor's fault-tolerance date moves left at once and the millisecond atom cycle stops being disqualifying — the bet behind zoned architectures. Ions gain equally and are further along on transversal Cliffords, so the winner need not be an atom company. The losers are fixed nearest-neighbour superconducting lattices, which cannot claim the discount.

*Open niche:* Correlated decoding has no published latency or accuracy benchmark above roughly 10² logical qubits. A small QCVV team could specify one — joint detector graphs of stated block count and depth, a noise model including atom loss, a wall-clock budget tied to a 1 ms cycle — and publish reference instances: the number every roadmap above assumes and none reports.

## Outlook & open questions
Confirm/demote in 12–24 months: a group closes transversal gate, correlated decode and feed-forward on hardware; an atom system shows sustained below-threshold memory with reloading; QuEra restates Libra without the gain. Best case 2029: constant-round fault tolerance at 10³ logical qubits, compressing every transport-capable roadmap. Worst case: correlated decoding stalls at a few dozen blocks and stays a resource-estimation tool. Open: does decoder latency scale past 10⁴ blocks; does >10× survive loss-heavy noise. Watch: Libra milestones and any real-time correlated-decoder demonstration.

## Sources
[1] Zhou, Zhao, Cain, Bluvstein, Maskara, Duckering, Hu, Wang, Kubica, Lukin · "Low-Overhead Transversal Fault Tolerance for Universal Quantum Computation" · Nature, doi 10.1038/s41586-025-09543-5 (arXiv:2406.17653 v1 2024-06-25, v2 2025-08-04) · https://arxiv.org/abs/2406.17653
[2] Bluvstein et al. (Harvard, MIT, QuEra) · 448-atom fault-tolerant architecture; 96 logical qubits, transversal CNOTs, 2.14(13)× suppression in a four-round circuit · Nature 649, 39 (arXiv:2506.20661) · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[3] Zhou, Duckering, Zhao, Bluvstein, Cain, Kubica, Wang, Lukin · "Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays" · ISCA 2025, doi 10.1145/3695053.3731039 (arXiv:2505.15907) · 2025-05-21 · https://arxiv.org/abs/2505.15907
[4] Cain, Xu, King, Picard, Levine, Endres, Preskill, Huang, Bluvstein · "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits" · arXiv:2603.28627 · 2026-03-30 · https://arxiv.org/abs/2603.28627
[5] Atom Computing and Microsoft · toric code on a neutral-atom array: Λ_Z ≈ 1.9, Λ_X ≈ 1.2, 90 rounds with reloading · arXiv:2606.04079 · 2026-06 · https://arxiv.org/abs/2606.04079
[6] Microsoft Quantum and Quantinuum · [[16,6,4]] tesseract code, transversal logical Clifford group in depth-one circuits, 12 addressable logical CZ pairs · Nature 654 · 2026-06-10 · https://www.nature.com/articles/s41586-026-10628-y
[7] NVIDIA · NVQLink architecture: 3.84 µs mean round trip, 67 µs median BP-OSD decode against Quantinuum Helios · developer blog · 2025-11-17 · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[8] Google · neutral-atom hardware track under Adam Kaufman, QEC adapted to atom connectivity · company blog · 2026-03-24 · https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]
[9] QuEra · Libra 2028 fault-tolerant system (>256 logical, 10⁻⁶) and expanded AWS collaboration · press release · 2026-06-15 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [C]
[10] QuEra · $230 M+ financing round (Google, SoftBank Vision Fund 2, NVentures) · press release · 2025-09-09 · https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[11] Atom Computing · >$300 M raised including a $100 M Commerce letter of intent · press release · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[12] Infleqtion · NYSE listing (INFQ), >$550 M gross proceeds · press release · 2026-02-17 · https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [C]
[13] Pasqal · SPAC merger completed, ~$360 M cash, Nasdaq PSQL · The Quantum Insider · 2026-08-28 · https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[14] US Department of Commerce / NIST · CHIPS letters of intent to nine companies, $2.013 B total · press release · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[15] DARPA · Quantum Benchmarking Initiative Stage B selection (eleven performers incl. Atom Computing and QuEra) · programme page · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection

## Open verification items
- The physical error rate, code distance and decoder model behind the 19 M-atom / 5.6-day and 10,000-atom estimates are not in either abstract; the two were not reconciled against a common assumption set.
- No independent replication of the >10× space-time reduction exists outside the overlapping Harvard/QuEra/Caltech author group.
- No published real-time correlated-decoder latency figure above roughly 10² logical qubits; scaling above that is unverified.
- The graph record's front-matter year (2025) is the Nature publication year; the preprint is 2024-06-25. Both are retained rather than reconciled.
