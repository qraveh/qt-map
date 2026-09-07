---
id: dec_fpga
name: FPGA real-time decoders (LCD, Deltaflow)
layer: "8 Decoder"
status: demonstrated
since: 2025
one_line: Room-temperature FPGAs running clustering or matching decoders fast enough to clear surface-code syndromes inside the QEC cycle, ahead of GPU and cryogenic alternatives.
verdict: Throughput under 1 µs per round is published to d=17 and closed-loop correction to d=3; nothing has decoded live syndromes above d=7, and the accuracy gap to neural decoders is real.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Classical hardware consuming syndrome bits and emitting corrections inside the code cycle. The lineage is the backlog argument: if mean decode time exceeds cycle time, undecoded rounds accumulate without bound and the classical hardware sets the logical error rate. FPGAs won for deterministic latency, not speed.
Coordinates: a compute module, not a carrier (affinity 0.5); no time, readout, mobility, control or fabrication of its own.
Error structure it consumes: Pauli syndromes from the rotated surface code.

## Physics & limits
Throughput must clear one round per cycle — 1.1 µs on Willow-class hardware [D][1] — which Riverlane's clustering decoder meets to d=17 [D][2]. Reaction latency gates every non-Clifford gate and only a closed loop measures it: Shenzhen's closed one in 550 ns at d=3, inside a 1.25 µs cycle [D][4]. Accuracy pays for latency: LCD thresholds at 0.55% against 0.7% for software MWPM [D][2], and on identical Willow syndromes matching gave Λ = 2.04 where a neural decoder gave 2.14 [D][1]. Area is the other wall: LCD at d=17 costs ~6% of a Xilinx VU19P [D][2] — a few dozen logical qubits per top-end part.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02-20 | Exact MWPM at 0.8 µs average, d=13, p=0.1%, 62 MHz | Yale (Micro Blossom) | [D][3] |
| 2025-12-17 | Clustering under 1 µs per round to d=17 on one FPGA | Riverlane | [D][2] |
| 2026-05-06 | First closed-loop FPGA decode on a live processor, 550 ns at d=3 | IQA Shenzhen | [D][4] |

IBM's Relay-BP for the gross code reports a 24 ns iteration and under 1 µs per cycle below p = 3×10⁻³, from simulated syndromes [S][5].

## Manufacturing, materials & supply chain
No fab: a commercial FPGA card in the room-temperature rack. Every published real-time decoder runs on AMD/Xilinx silicon (VU19P for LCD [D][2], VMK180 for Micro Blossom [D][3]); the only merchant alternative changed hands when Intel sold 51% of Altera to Silver Lake at an $8.75 B valuation in April 2025 [G][11] — a duopoly with one side under private equity. High-end FPGAs sit inside US export-control scope. The I/O burden is the syndrome pipe: trivial at 10³ qubits, but at 10⁴–10⁶ the rate forces predecoding at 4 K or many parallel cards.

## Role in the stack
Requires the rotated surface code and provides the correction stream fault tolerance needs; it replaces GPU decoding, whose tail latency is non-deterministic — 3.84 µs mean, 3.96 µs max just to cross NVQLink [C][7]. Its contribution to the derived clock is a floor, not a term: it must stay under the 1.1 µs cycle, and does. Verification: these are decoder-in-isolation figures on replayed or simulated syndromes, only the d=3 loop live; Micro Blossom's quoted 367 ns is a repository figure in no paper, the published number being 0.8 µs [D][3].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Riverlane | supplier | UK | LCD and Deltaflow, the only merchant QEC stack | [D][2] |
| AMD | supplier | US | The FPGA silicon under every published decoder | [D][2] |
| Google | user | US | 63 µs baseline at d=5 [D][1], then neural decoding at d=7 | [D][6] |
| IQA Shenzhen | research | CN | First closed-loop FPGA decode on a live processor | [D][4] |

**Money.**
2024-08-06 · Riverlane · Series C · $75 M · Planet First Partners lead · closed [C][8][G:RIVERLANE-FUNDING]
2025-04-14 · Intel/Altera · divestment of 51% · $8.75 B enterprise valuation · Silver Lake · announced [G][11][G:ALTERA-SILVERLAKE-2025]

**Market & supply chain.** One merchant decoder vendor, one dominant FPGA vendor, NVIDIA pushing NVQLink as the alternative — open endpoint, single-sourced accelerator [C][7]. Riverlane's stack ships integrated with Qblox control hardware [C][10]. It pays into G3 and G4 only.

**IP & standards.** Riverlane GB 2641501 A "Quantum decoder" (published 2025-12-10) claims grouped processing elements running clustering on the decoding hypergraph — the LCD architecture itself [G][12]. No decoder standard exists.

**Roadmaps & track record.** Riverlane (2026-03-12 · megaquop before 2030, teraquop from 2033 · LCD published on time [C][9]). IBM (2025-10 · FPGA gross-code decoding · still simulation as of 2026-09-04 [S][5]).

**Strategic reading.** Whoever owns the decoder sits between every superconducting QPU and fault tolerance — but the layer is thin enough that QPU vendors build it in-house, as IBM and Google did. AMD wins either way; the threat is NVQLink commoditising the interface.

*Open niche:* nobody has cross-validated competing decoders on one live syndrome stream. A neutral harness replaying a recorded trace through LCD, Micro Blossom, Relay-BP and a neural decoder, reporting latency distribution with logical error, would make these claims comparable.

## Outlook & open questions
Confirm by end-2027: a closed-loop decode on live syndromes at d ≥ 7, or Relay-BP on real gross-code hardware; demote if both stay simulated. Best case 2029: a portable interface with second-source silicon; worst case, per-vendor decoders nobody can compare. Does reaction latency or throughput bind first at d=17? Do decoder vendors survive QPU vendors building in-house? Does export control reach FPGAs?

## Sources
[1] Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920, 2024-12-09 (parallel Sparse Blossom, 63 µs mean) — https://www.nature.com/articles/s41586-024-08449-y
[2] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane), "Local clustering decoder as a fast and adaptive hardware decoder for the surface code", Nature Communications 16, 11048, 2025-12-17 — https://www.nature.com/articles/s41467-025-66773-x
[3] Wu, Liyanage, Zhong (Yale), "Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction", ASPLOS 2025; arXiv:2502.14787, 2025-02-20 — https://arxiv.org/abs/2502.14787
[4] Yang, Sun, Wu et al. (IQA Shenzhen / SUSTech / Peking / Hefei), "Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder", arXiv:2605.04892, 2026-05-06 — https://arxiv.org/abs/2605.04892
[5] Maurer, Buehler, Kroener et al. (IBM), "Real-time decoding of the gross code memory with FPGAs", arXiv:2510.21600, 2025-10-24 [S] — https://arxiv.org/abs/2510.21600
[6] Sivak, Morvan, Broughton et al. (Google Quantum AI), "Reinforcement learning control of quantum error correction", Nature 655, 2026-07-08 (real-time neural decoding at d=7) — https://www.nature.com/articles/s41586-026-10759-2
[7] NVIDIA, NVQLink architecture (3.84 µs mean, 3.96 µs maximum round trip; 67 µs median BP-OSD decode), 2025-11-17 [C] — https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
[8] Riverlane, Series C release, 2024-08-06 [C] — https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology
[9] Riverlane, QEC technology roadmap and Deltaflow datasheet, 2026-03-12 / 2026-05 [C][R] — https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap
[10] Qblox and Riverlane, closed-loop QEC integration (250 physical / 1 logical, sub-µs feedback), 2026-03-17 [C] — https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html
[11] Altera, Silver Lake acquires 51% at an $8.75 B enterprise valuation, 2025-04-14 [G] — https://www.altera.com/newsroom/news/press-release/altera-silver-lake
[12] Riverlane Ltd, GB 2641501 A "Quantum decoder", published 2025-12-10 [G] — https://patents.google.com/patent/GB2641501A/en

## Open verification items
Micro Blossom's 367 ns is a GitHub repository claim appearing in no paper; the published ASPLOS 2025 result is 0.8 µs average at d=13, p=0.1%.
IBM's Relay-BP FPGA numbers come from simulated syndromes, and the abstract's 24 ns / <1 µs conflicts with a 480 ns-per-12-cycle figure carried elsewhere [G:RELAYBP-LATENCY-CONFLICT].
Riverlane's Series C is $75 M in the 2024 release and $85 M in the 2026 roadmap; unreconciled.
The IBM–AMD FPGA decoder collaboration is trade-press only, terms unconfirmed.
