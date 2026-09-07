---
id: dec_mwpm
name: MWPM / Sparse Blossom (+correlated matching)
layer: "8 Decoder"
status: demonstrated
since: 2015
one_line: Graph-matching decoder turning a syndrome round into the likeliest Pauli error chain; the accuracy reference and the shipped real-time decoder for surface codes.
verdict: Matching stays the surface-code default through 2026 — Google's own below-threshold run decodes with Sparse Blossom. Demote if a live-hardware, same-syndrome test shows a non-matching decoder beating it on accuracy and latency together by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
MWPM makes each violated stabilizer a vertex on a weighted graph whose edges are the errors flipping two detectors; the lowest-weight pairing explaining the set is the maximum-likelihood error chain. Dennis, Kitaev, Landahl and Preskill introduced it (2002) [D][1]; Fowler showed in 2015 that below threshold it is maintainable incrementally in constant average time per round, independent of lattice size [D][2]. Correlated matching reweights edges so a Y error is not charged twice. The engine is Higgott and Gidney's Sparse Blossom (*Quantum* 9, 1600, 2025-01-20) [D][3], a sparse reformulation of Edmonds' 1965 blossom algorithm, shipped as PyMatching v2.
a = 0.5 — classical post-processing, no carrier; b, c, d, e do not apply [graph].
f = Pauli chain on a matching graph; g = none — software, no fabrication [graph].

## Physics & limits
Throughput must exceed syndrome production or the backlog diverges and the machine stalls: Sparse Blossom clears ~10⁶ errors per core-second, under 1 µs per round at d=17 [D][3], inside Willow's 1.1 µs cycle [D][4]. Latency binds only where a logical measurement gates the next operation: 63 µs at d=5 is ~57 cycles of dead time [D][4]. The accuracy floor is structural: matching is maximum-likelihood only when errors flip two detectors, so hyperedges (Y errors, correlated measurement errors, leakage, loss) must be projected onto a matchable graph. That projection is the whole gap to a decoder modelling them — Λ = 2.04 ± 0.02 for matching against 2.14 ± 0.02 for the neural decoder on Willow's syndromes [D][4], AlphaQubit ~25% better at simulated d=11 [D][11]. What moves the floor is the graph: fitted edge weights, soft readout, leakage edges.

## Engineering state of the art
| Year | Figure | Who | Tag+Key |
|---|---|---|---|
| 2023-03 | <1 µs/round at d=17, ~10⁶ errors/core-second, simulated | Google Quantum AI | [D][3] |
| 2024-12 | 63 µs real-time latency at d=5 over 10⁶ cycles | Google Quantum AI | [D][4][G:WILLOW-QEC-2024-12] |
| 2025-03 | 0.8 µs FPGA latency at d=13, p=0.1%, 62 MHz | Yale University | [D][5][G:MICROBLOSSOM-2026] |

Dominant term: the decoding graph — mis-calibrated weights, unrepresented leakage — not the matcher [D][4].

## Manufacturing, materials & supply chain
No fabrication: MIT-licensed software [7] on general compute, acceleration the paid, single-sourced layer. Every published real-time QEC decoder runs on AMD/Xilinx logic — Riverlane's on a VU19P at ≈6% of LUTs for d≤17 [D][6], Micro Blossom on a Versal VMK180 [D][5], the Shenzhen neural decoder on a Kintex-7 [D][10], IBM's Relay-BP on AMD parts [P][8] — and GPU decoding is NVIDIA-only. No MWPM ASIC exists (4 Sep 2026). Export exposure is on that hardware: the BIS rule of 2024-09-06 controls quantum computers (4A906) and sub-4.5 K control ICs (3A901.a) [G][9]; published decoder source is outside the EAR under 15 CFR §734.7.

## Control, readout & I/O burden
At 10³ qubits one core suffices. At 10⁴ the binding term is syndrome bandwidth, not compute — d² detectors per logical qubit per 1.1 µs — hence cryogenic pre-compression, claimed at up to 3,780× below 0.56 mW at 4 K but not fabricated [S][G:PINBALL-2025-12]. At 10⁶ the interconnect decides: NVQLink's 3.84 µs round trip [C][12] exceeds a transmon cycle, so GPU matching runs windowed there.

## Role in the stack
Default real-time decoder for surface- and colour-code memories on the superconducting, ion, photonic and spin paths [graph]; it needs the near-planar graph a static nearest-neighbour lattice supplies free. It replaces neural and belief-propagation decoders, which win once checks stop being matchable; switching is asymmetric — leaving costs a hardware implementation and a new verification story, returning costs nothing. Clock contribution ≈1.0 µs per round at d=17 [D][3] against a derived clock of 0.65 µs for the transmon surface-code path (derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path). Empty slot nearby: no real-time matcher consumes soft readout or leakage flags.

## Verification (QCVV)
Sparse Blossom's throughput comes from simulated Stim streams [D][3]. The one hardware-integrated figure, Willow's 63 µs at d=5, used a specialised parallel Sparse Blossom built by Google, not stock PyMatching [D][4]. Micro Blossom's 0.8 µs at d=13 is peer-reviewed (ASPLOS 2025) but replays syndromes [D][5]; the repository's 367 ns appears in no paper [C][G:MICROBLOSSOM-2026]. The much-quoted threshold spread is no conflict: 0.7% (PyMatching), 0.65% and 0.55% (Riverlane's software and hardware clustering decoders) come from one comparison under one noise model [D][6]. Every challenger publishes MWPM as baseline; none replicates its speed.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Google Quantum AI | Developer/user | US | Co-authored Sparse Blossom; runs it in Willow | [D][3][4] |
| Riverlane | Supplier | UK | Sells Deltaflow QEC hardware; quotes MWPM as reference | [C][G:RIVERLANE-DELTAFLOW-PAGE-2026-05] |
| Yale University | Research | US | Micro Blossom exact-MWPM FPGA accelerator | [D][5] |
| AMD | Supplier | US | Its parts carry every published real-time decoder | [D][5][6] |
| NVIDIA | Supplier | US | CUDA-Q QEC and the NVQLink GPU–QPU bus | [C][12] |

**Money.** 2024-08-06 · Riverlane · Series C · $75 M (its roadmap says $85 M) · Planet First Partners lead · >$120 M cumulative · closed [C][16]. 2025-11-17 · NVIDIA · NVQLink launch · undisclosed · Quantinuum first QPU partner [C][G:NVQLINK-QUANTINUUM-2025-11]. 2026-07-24 · Quantum X Labs · result · none disclosed · NVIDIA, Quantum Machines/IQCC · unquantified [C][14]. No decoder-specific DARPA award exists; QBI funds eleven Stage B teams, each needing one [G:QBI-STAGEB-2025-11]. No later Riverlane round located as of 4 Sep 2026.

**Market & supply chain.** Nobody sells MWPM: the algorithm is free and the reference MIT-licensed [7], so value accrues to the box that runs it — Deltaflow, CUDA-Q QEC/NVQLink, in-house firmware. Concentration is one-deep twice: AMD for logic, NVIDIA for GPUs. The one public resource figure, ≈6% of a VU19P for d≤17 [D][6], implies ~16 patches per part. Pays into G3 and G4.

**IP & standards.** No MWPM patent family — Edmonds (1965) via Dennis–Kitaev–Landahl–Preskill (2002) [D][1]; PyMatching and Micro Blossom are MIT-licensed [7][5]. The IP is on hardware decoders: Riverlane GB 2641501 A (published 2025-12-10), Google US 12,518,194 (granted 2026-01-06) [G:SURFACE-CODE-PATENTS]. PatSnap counted 12 QEC patents in April 2026 (Google 6, IBM 4, Tencent 2), no decoder cluster [P][15]. De facto interfaces: Stim detector-error models, NVQLink.

**Roadmaps & track record.** Higgott and Gidney (2023-03 · sub-µs decoding at scale · met, and inside Willow's loop) [D][3]. Yale (2025-03 · d=13 at 0.8 µs on FPGA · met; the repository's 367 ns is not) [D][5]. Riverlane (2026-03-12 · megaquop before 2030, teraquop from 2033 · no interim milestone due) [R][13]. Google's claims track delivery and are the only ones measured live; Riverlane's roadmap is unfalsifiable before 2029.

**Strategic reading.** If matching holds, AMD and every surface-code builder win: the reference stays free and differentiation collapses to firmware. Riverlane's hardware decoder trades threshold (0.55% vs 0.7%) for latency and area [D][6], so its moat is "under the cycle time" — which Micro Blossom now offers for exact MWPM, MIT-licensed [D][5]. If matching loses it loses to belief propagation on qLDPC: decoder, code and connectivity change together.

*Open niche:* the missing artefact is an impartial cross-decoder harness — one archived corpus of live-hardware syndromes, one calibration, replayed through PyMatching, a clustering decoder, Relay-BP and a neural decoder, reporting accuracy, latency and logic area on one FPGA family, which no challenger's own author can credibly run.

## Outlook & open questions
Confirm/demote in 12–24 months: a same-qubit, same-calibration comparison of matching against a challenger (all current ones are simulated, offline or self-refereed); an FPGA matcher closing a live loop at d≥7. Best case 2029: matching stays default past 10⁴ physical qubits, reaction time down from 63 µs to ~1 µs. Worst case: qLDPC memories carry the machines and belief propagation owns the socket. Open questions: does matching extend to loss-dominated atom syndromes; will anyone fund a decoder ASIC when 6% of an FPGA suffices; will QBI Stage C fix a decoder-agnostic benchmark.

## Sources
[1] Dennis, Kitaev, Landahl, Preskill, "Topological quantum memory", J. Math. Phys. 43, 4452 (2002) — https://arxiv.org/abs/quant-ph/0110143
[2] Fowler, "Minimum weight perfect matching of fault-tolerant topological quantum error correction in average O(1) parallel time", Quantum Inf. Comput. 15, 0145 (2015) — https://arxiv.org/abs/1307.1740
[3] Higgott, Gidney, "Sparse Blossom: correcting a million errors per core second with minimum-weight matching", Quantum 9, 1600 (2025-01-20) — https://quantum-journal.org/papers/q-2025-01-20-1600/ ; arXiv:2303.15933 — https://arxiv.org/abs/2303.15933
[4] Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920 (2024-12-09) — https://www.nature.com/articles/s41586-024-08449-y ; arXiv:2408.13687 — https://arxiv.org/abs/2408.13687 [G:WILLOW-QEC-2024-12]
[5] Wu, Liyanage, Zhong (Yale), "Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction", ASPLOS 2025 (arXiv 2025-02-20) — https://arxiv.org/abs/2502.14787 ; repository https://github.com/yuewuo/micro-blossom [G:MICROBLOSSOM-2026]
[6] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane), "Local clustering decoder as a fast and adaptive hardware decoder for the surface code", Nature Communications 16, 11048 (2025-12-17) — https://www.nature.com/articles/s41467-025-66773-x [G:RIVERLANE-LCD-2025-12]
[7] Higgott, "PyMatching" v2, MIT licence — https://github.com/oscarhiggott/PyMatching
[8] Maurer et al. (IBM), "Real-time decoding of the gross code memory with FPGAs", arXiv:2510.21600 (2025-10-24) — https://arxiv.org/abs/2510.21600 [G:GROSSCODE-FPGA-2025-10]
[9] US BIS, interim final rule, "Commerce Control List Additions and Revisions" (2024-09-06), ECCNs 3A901.a, 3A904, 3B904, 4A906 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent [G]
[10] Yang, Sun, Wu et al. (International Quantum Academy Shenzhen / SUSTech), "Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder", arXiv:2605.04892 (2026-05-06) — https://arxiv.org/abs/2605.04892 [G:NN-DECODER-FPGA-2026-05]
[11] Bausch et al. (Google DeepMind / Google Quantum AI), "Learning high-accuracy error decoding for quantum processors", Nature 635, 834 (2024-11-20) — https://www.nature.com/articles/s41586-024-08148-8 [G:ALPHAQUBIT-2024-11]
[12] NVIDIA, "NVQLink architecture integrates accelerated computing with quantum processors" (2025-11-17) — https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C][G:NVQLINK-2025]
[13] Riverlane, "Riverlane publishes QEC Technology Roadmap" (2026-03-12) — https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [C][G:RIVERLANE-ROADMAP-2026-03]
[14] Quantum X Labs, "Quantum X Labs Reports Meaningful Error Correction Decoder Results with NVIDIA CUDA-Q QEC", GlobeNewswire (2026-07-24) — https://www.globenewswire.com/news-release/2026/07/24/3332879/0/en/quantum-x-labs-reports-meaningful-error-correction-decoder-results-with-nvidia-cuda-q-qec.html [C][G:QXLABS-QECCT-2026-07]
[15] PatSnap Insights, "Quantum error correction patent landscape 2026" (2026-04-22) — https://www.patsnap.com/resources/blog/articles/quantum-error-correction-patent-landscape-2026/ [P][G:PATSNAP-QEC-LANDSCAPE-2026-04]
[16] Riverlane, "Riverlane raises $75 million to meet surging global demand for quantum error correction technology" (2024-08-06) — https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C][G:RIVERLANE-FUNDING]

## Open verification items
Micro Blossom: the peer-reviewed figure is 0.8 µs average latency at d=13 (ASPLOS 2025) [5]; the repository's 367 ns and 10⁶ rounds/s appear in no paper and carry no stated code distance — a repository claim, not a measurement.
Riverlane's Series C amount conflicts between its own release ($75 M, 2024-08-06) and its 2026 roadmap ($85 M) [G:RIVERLANE-FUNDING]; no extension release exists and no later round was located as of 4 Sep 2026.
Quantum X Labs' claim that its transformer decoder outperforms MWPM carries no quantitative figure and no peer review [14].
Willow's real-time decoder is described only as a specialised Sparse Blossom variant; no separate publication, hardware platform or resource figure for it was located, so its 63 µs cannot be attributed to a named part.
