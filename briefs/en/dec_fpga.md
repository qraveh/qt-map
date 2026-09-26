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
Attributes: a compute module, not a carrier (affinity 0.5); no time, readout, mobility, control or fabrication of its own.
Error structure it consumes: Pauli syndromes from the rotated surface code.

## Physics & limits
Throughput must clear one round per cycle — 1.1 µs on Willow-class hardware [D][1] — which Riverlane's clustering decoder meets to d=17 [D][199]. Reaction latency gates every non-Clifford gate and only a closed loop measures it: Shenzhen's closed one in 550 ns at d=3, inside a 1.25 µs cycle [D][537]. Accuracy pays for latency: LCD thresholds at 0.55% against 0.7% for software MWPM [D][199], and on identical Willow syndromes matching gave Λ = 2.04 where a neural decoder gave 2.14 [D][1]. Area is the other wall: LCD at d=17 costs ~6% of a Xilinx VU19P [D][199] — a few dozen logical qubits per top-end part.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02-20 | Exact MWPM at 0.8 µs average, d=13, p=0.1%, 62 MHz | Yale (Micro Blossom) | [D][535] |
| 2025-12-17 | Clustering under 1 µs per round to d=17 on one FPGA | Riverlane | [D][199] |
| 2026-05-06 | First closed-loop FPGA decode on a live processor, 550 ns at d=3 | IQA Shenzhen | [D][537] |

IBM's Relay-BP for the gross code reports a 24 ns iteration and under 1 µs per cycle below p = 3×10⁻³, from simulated syndromes [S][46].

## Manufacturing, materials & supply chain
No fab: a commercial FPGA card in the room-temperature rack. Every published real-time decoder runs on AMD/Xilinx silicon (VU19P for LCD [D][199], VMK180 for Micro Blossom [D][535]); the only merchant alternative changed hands when Intel sold 51% of Altera to Silver Lake at an $8.75 B valuation in April 2025 [G][543] — a duopoly with one side under private equity. High-end FPGAs sit inside US export-control scope. The I/O burden is the syndrome pipe: trivial at 10³ qubits, but at 10⁴–10⁶ the rate forces predecoding at 4 K or many parallel cards.

## Role in the stack
Requires the rotated surface code and provides the correction stream fault tolerance needs; it replaces GPU decoding, whose tail latency is non-deterministic — 3.84 µs mean, 3.96 µs max just to cross NVQLink [C][253]. Its contribution to the derived clock is a floor, not a term: it must stay under the 1.1 µs cycle, and does. Verification: these are decoder-in-isolation figures on replayed or simulated syndromes, only the d=3 loop live; Micro Blossom's quoted 367 ns is a repository figure in no paper, the published number being 0.8 µs [D][535].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Riverlane | supplier | UK | LCD and Deltaflow, the only merchant QEC stack | [D][199] |
| AMD | supplier | US | The FPGA silicon under every published decoder | [D][199] |
| Google | user | US | 63 µs baseline at d=5 [D][1], then neural decoding at d=7 | [D][2] |
| IQA Shenzhen | research | CN | First closed-loop FPGA decode on a live processor | [D][537] |

**Money.**
2024-08-06 · Riverlane · Series C · $75 M · Planet First Partners lead · closed [C][500][G:RIVERLANE-FUNDING]
2025-04-14 · Intel/Altera · divestment of 51% · $8.75 B enterprise valuation · Silver Lake · announced [G][543][G:ALTERA-SILVERLAKE-2025]

**Market & supply chain.** One merchant decoder vendor, one dominant FPGA vendor, NVIDIA pushing NVQLink as the alternative — open endpoint, single-sourced accelerator [C][253]. Riverlane's stack ships integrated with Qblox control hardware [C][498]. It pays into G3 and G4 only.

**IP & standards.** Riverlane GB 2641501 A "Quantum decoder" (published 2025-12-10) claims grouped processing elements running clustering on the decoding hypergraph — the LCD architecture itself [G][501]. No decoder standard exists.

**Roadmaps & track record.** Riverlane (2026-03-12 · megaquop before 2030, teraquop from 2033 · LCD published on time [C][497]). IBM (2025-10 · FPGA gross-code decoding · still simulation as of 2026-09-04 [S][46]).

**Strategic reading.** Whoever owns the decoder sits between every superconducting QPU and fault tolerance — but the layer is thin enough that QPU vendors build it in-house, as IBM and Google did. AMD wins either way; the threat is NVQLink commoditising the interface.

*Open niche:* nobody has cross-validated competing decoders on one live syndrome stream. A neutral harness replaying a recorded trace through LCD, Micro Blossom, Relay-BP and a neural decoder, reporting latency distribution with logical error, would make these claims comparable.

## Outlook & open questions
Confirm by end-2027: a closed-loop decode on live syndromes at d ≥ 7, or Relay-BP on real gross-code hardware; demote if both stay simulated. Best case 2029: a portable interface with second-source silicon; worst case, per-vendor decoders nobody can compare. Does reaction latency or throughput bind first at d=17? Do decoder vendors survive QPU vendors building in-house? Does export control reach FPGAs?

## Sources
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[46] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[199] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[253] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[497] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [C]
[498] Qblox; Riverlane, “Qblox and Riverlane Demonstrate Integration Enabling Real-Time Quantum Error Correction,” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[500] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[501] Z. A. Bracken, A. Zalawadiya, B. Barber, and L. Skoric, “Quantum decoder,” Google Patents, Dec. 10, 2025. [Online]. Available: https://patents.google.com/patent/GB2641501A/en [G]
[535] Y. Wu, N. Liyanage, and L. Zhong, “Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction,” [arXiv:2502.14787](https://arxiv.org/abs/2502.14787), Feb. 2025. Also https://github.com/yuewuo/micro-blossom. [D]
[537] X. Yang *et al.*, “Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder,” [arXiv:2605.04892](https://arxiv.org/abs/2605.04892), May 2026. Also https://arxiv.org/html/2605.04892. [D]
[543] Altera, “Altera Closes Silver Lake Investment to Become World's Largest Pure-play FPGA Solutions Provider,” Sep. 15, 2025. [Online]. Available: https://www.altera.com/newsroom/news/press-release/altera-silver-lake [G]

## Open verification items
Micro Blossom's 367 ns is a GitHub repository claim appearing in no paper; the published ASPLOS 2025 result is 0.8 µs average at d=13, p=0.1%.
IBM's Relay-BP FPGA numbers come from simulated syndromes, and the abstract's 24 ns / <1 µs conflicts with a 480 ns-per-12-cycle figure carried elsewhere [G:RELAYBP-LATENCY-CONFLICT].
Riverlane's Series C is $75 M in the 2024 release and $85 M in the 2026 roadmap; unreconciled.
The IBM–AMD FPGA decoder collaboration is trade-press only, terms unconfirmed.
