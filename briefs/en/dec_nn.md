---
id: dec_nn
name: Neural decoders (AlphaQubit2, CNN, transformers)
layer: "8 Decoder"
tier: 1
status: demonstrated
since: 2024
one_line: "Learned syndrome decoders — recurrent transformers, CNNs, LSTMs, state-space models — that beat matching by absorbing non-Pauli device noise from data."
verdict: "The accuracy lead is real and now real-time at distance 7; the open question is whether it survives the throughput and drift regime beyond distance 11."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A neural decoder replaces the combinatorial inference step of error correction with a trained function approximator: syndrome history in, logical correction out. Decoding is Bayesian inference over a detector-error hypergraph, and minimum-weight perfect matching is exact only when that hypergraph is graphlike — every error flips at most two detectors, with independent, known, static probabilities. Real devices break all three: leakage parks a qubit outside the computational subspace for many rounds, correlated bursts couple distant detectors, readout is analogue before thresholding, and noise drifts. A learned decoder fits the joint distribution from labelled data instead, consuming soft readout and leakage flags matching cannot represent. The lineage runs from convolutional decoders (2017) to the recurrent-transformer AlphaQubit, published by Google DeepMind with Google Quantum AI on 2024-11-20 [D][1][G:ALPHAQUBIT-2024-11], and to AlphaQubit2, named in the July 2026 Willow paper as "a scalable and real-time neural decoder for topological quantum codes" [D][2].

Coordinates: carrier affinity 0.5 and no carrier of its own; no characteristic time or entangling operation, inheriting the host's syndrome period (1.1 µs on Willow [D][3][G:WILLOW-QEC-2024-12]); no readout, though it consumes the soft values matching discards; no mobility beyond the detector-error graph it was trained on; no control modality — placement is the variable, room-temperature logic today, cold silicon proposed; Pauli error structure, with its value in the non-Pauli residue; no manufacturing of its own.

## Physics & limits

The floor is information-theoretic and computational, not physical: the ceiling is maximum-likelihood decoding, and matching sits measurably below it. On Sycamore data AlphaQubit reached 2.748(15)×10⁻² logical error per round at distance 5 against 2.915(16)×10⁻² for correlated matching, and 2.901(23)×10⁻² versus 3.028(23)×10⁻² at distance 3 — about 6% relative, rising to roughly 25–30% at simulated distance 11 [D][1][16]. The gain grows with distance and with how far the device departs from the assumed model.

The computational limit is the backlog condition: a decoder slower than the syndrome rate accumulates an unbounded queue and the logical clock stalls, which on a transmon means roughly 10⁶ decode-rounds per second per logical qubit. Google's 2024 framing: AlphaQubit "is still too slow to correct errors in a superconducting processor in real time" [C][16]. Cost scaling is architectural: attention over a distance-d patch is O(d⁴) per round against O(d²) for a state-space recurrence, and the cheaper model measured a *higher* real-time threshold, 1.04% versus 0.97%, because latency-induced degradation belongs in that figure of merit [S][4].

Failure modes are statistical: distribution shift degrades a fine-tuned model with no error signal, retraining needs data from the same processor, and there is no proved threshold, only a measured one. Soft information, joint training with the calibration loop and O(d²) architectures would move the floor.

## Engineering state of the art

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-11 | Distance-5 Sycamore memory 2.748(15)×10⁻²/round vs 2.915(16)×10⁻² correlated matching; ~25–30% fewer errors at simulated distance 11 | Google DeepMind (AlphaQubit) | [D][1][G:ALPHAQUBIT-2024-11] |
| 2025-10 | State-space decoder: real-time threshold 1.04% vs 0.97% transformer, O(d²) vs O(d⁴) per round | academic preprint | [S][4] |
| 2025-12 | Non-neural bar: clustering decoder under 1 µs/round to distance 17 on one Xilinx VU19P, ~6% of logic cells | Riverlane | [D][5][G:RIVERLANE-LCD-2025-12] |
| 2026-05 | First closed-loop neural decoding on hardware: 124 ns decode, 184 ns throughput period, 550 ns loop, distance 3, 6.9(2)%/round vs offline matching 7.2(2)% | International Quantum Academy | [D][6] |
| 2026-07 | AlphaQubit2 decoding Willow in real time at distance 7: 7.72(9)×10⁻⁴ logical error per cycle | Google Quantum AI | [D][2] |

Best demonstrated is the July 2026 Willow run; typical at scale is still matching or clustering, since every stack outside Google is deterministic. The decoder's own budget is dominated by model mismatch and latency, not arithmetic precision — the Shenzhen implementation quantised weights to 6-bit integers and lost nothing against offline matching [D][6]. At system level the distance-7 record is limited by two-qubit gate and readout errors, and no Λ is reported for it [D][2].

## Manufacturing, materials & supply chain

The node is fabricated only through its host; three placements exist as of 3 Sep 2026. In room-temperature logic, the Shenzhen LSTM (32 hidden units, separate X and Z decoders, four pipelined stages on DSP blocks) fits a mid-range AMD Kintex-7 XC7K410T at distance 3, with current parts ceilinged near distance 13 [D][6]; Riverlane's clustering decoder takes ~6% of the look-up tables of a Xilinx VU19P to distance 17 [D][5][G:RIVERLANE-LCD-2025-12] — a learned decoder buys accuracy with silicon. On graphics processors, NVQLink puts a GH200-class host in the loop at 3.84 µs mean round trip [C][7][G:NVQLINK-2025]. In cold silicon, the "Pinball" cryo-CMOS pre-decoder claims 3,780× syndrome-bandwidth reduction under 0.56 mW at 4 K, but is an unfabricated design study [S][8][G:PINBALL-2025-12].

AMD (Xilinx) and NVIDIA supply essentially all decode silicon, with no second source at the part sizes required. Yield is not a decoder problem; portability is — a fine-tune is per-processor, and nobody has published how many devices one trained model covers. Export exposure is indirect: the decoder ships as firmware in a control rack and inherits the accelerator's controls and the classification of the system it serves.

## Control, readout & I/O burden

The burden is bandwidth and latency, not lines or lasers. A distance-7 patch produces 48 ancilla bits per 1.1 µs cycle — about 44 Mbit/s per logical qubit, so ~4.4 Gbit/s at 100 logical qubits and ~44 Gbit/s at 1,000, every bit needing a decision inside the feedback window. At 10³ physical qubits one mid-range part suffices. At 10⁴ the wall is aggregate: dozens of patches wanting sub-microsecond turnaround, and NVQLink's 3.84 µs round trip is three and a half Willow cycles — fine for millisecond-cycle ion and atom machines, marginal for transmons unless decode is local to the fridge [C][7][G:NVQLINK-2025]. At 10⁶ neither room-temperature fabric nor a shared accelerator closes, and the syndrome must be reduced in the cold stage [S][8]. The Shenzhen result proves the loop closes at all: 222 ns acquisition, 148 ns decoder logic and 180 ns electronic delay inside a 1.25 µs cycle [D][6].

## Role in the stack

It sits on the superconducting transmon path (Google, IBM, Rigetti, IQM, Oxford Quantum Circuits, USTC/Zhejiang, Fujitsu) and the alkali neutral-atom path (Harvard/MIT, QuEra, Pasqal, Infleqtion, Google), reaching both. It requires the rotated surface code and its yoked variants — every deployed model is trained on surface-code syndromes, and none has run on a sparse quantum parity-check code. It provides for in-loop reinforcement-learning calibration: the decoder is fast enough to sit inside the loop the calibration agent occupies [D][2]. It replaces minimum-weight perfect matching at an asymmetric switching price — going learned costs a training pipeline, per-device fine-tuning and worst-case guarantees; going back costs only accuracy.

The hub reading: nothing in the architecture is superconducting-specific, so the same family serves millisecond-cycle atom machines offline and microsecond-cycle transmons only with dedicated silicon; only the training data and latency budget differ. Contribution to the derived clock (derived clock = max(gate, readout, transport) for the path): zero while decode latency stays under the syndrome period, which it now does, though feedback-conditioned operations consume 0.55 µs of a 1.3 µs cycle [D][6]. Neighbouring empty slots: a fabricated cryogenic neural-decoder ASIC, and a learned decoder for bivariate-bicycle codes on hardware.

## Verification (QCVV)

Headline numbers come from memory experiments — run N syndrome rounds, fit logical fidelity against N — decoded offline or, since 2026, in the loop. The protocol misses three things. The baseline is a choice: "25–30% better" is against *correlated* matching at simulated distance 11 while the hardware distance-5 figure is ~6% [D][1][16], so the graph record's 5–25% band is the honest span. Generalisation is untested: a model fine-tuned on one processor and evaluated on it is not evidence of transfer. And latency distributions are rarely reported, though only the tail causes backlog.

Conflicts: the AlphaQubit blog claims "30% fewer errors than correlated matching" [C][16] while the Nature figures imply ~5.7% at distance 5 [D][1] — simulated and measured regimes conflated; trust the Nature numbers. Riverlane's Series C is announced as $75 M (2024-08-06) but its 2026 roadmap states "$85 million in 2024" and "$120 million+" total [C][9][G:RIVERLANE-FUNDING]; trust the 2024 release. No group has replicated AlphaQubit2 on non-Google hardware as of 3 Sep 2026.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Google DeepMind | developer | UK | AlphaQubit and AlphaQubit2 architecture and training | [D][1][2] |
| Google Quantum AI | developer | US | Runs AlphaQubit2 in real time on Willow at distance 7 | [D][2] |
| Riverlane | supplier | UK | Sells the deterministic rival (clustering decoder, Deltaflow) | [D][5][C][10] |
| NVIDIA | supplier | US | NVQLink and CUDA-Q QEC; 3.84 µs host-in-the-loop round trip | [C][7] |
| International Quantum Academy | research | CN | First closed-loop neural decoder on a superconducting chip | [D][6] |
| Qblox | supplier | NL | Control hardware for the sub-microsecond closed loop | [C][11] |
| IBM | developer | US | Relay-BP decoder, under 1 µs/cycle in simulation | [S][13] |
| AMD | supplier | US | Kintex-7 and Virtex parts hosting both decoder families | [D][5][6] |

**Money.**
- 2024-05-01 · Riverlane · Horizon Europe EIC Transition grant (SkyTALE, with Qblox) · £2.1 M · European Innovation Council · closed [G:RIVERLANE-FUNDING]
- 2024-08-06 · Riverlane · Series C · $75 M · Planet First Partners (lead), ETF Partners, EDBI, Cambridge Innovation Capital, Amadeus, NSSIF, Altair · company later states $85 M, $120 M+ cumulative · closed, disputed [C][9][G:RIVERLANE-FUNDING]
- 2025-11-17 · NVIDIA · NVQLink launch, price undisclosed; Quantinuum Helios first deployment · — · announced [C][7][G:NVQLINK-2025]
- 2025-11 · DARPA · QBI Stage B: eleven teams, no pure decoder vendor · — · programme record [G][14]
- 2026-03-12 · Riverlane · roadmap: 10⁶ reliable operations before 2030, 10¹² from 2033 · — · roadmap [C][R][10][G:RIVERLANE-ROADMAP-2026-03]
- 2026-03-17 · Qblox and Riverlane · closed-loop demo, 250 physical / 1 logical qubit, 10,000 operations · — · announced [C][11][G:QBLOX-RIVERLANE-2026-03]

**Market & supply chain.** There is no decoder market in the ordinary sense: Google's decoder is captive, and the one merchant vendor of consequence, Riverlane, sells a deterministic decoder rather than a trained model. Enabling equipment is AMD programmable logic, NVIDIA accelerators and control racks from Qblox, Zurich Instruments and Quantum Machines; concentration risk sits with two American vendors. Unit economics are unquotable; the resource data give a proxy of one to two orders of magnitude more silicon per logical qubit than clustering. G3 and G4 pay for this node and G7 pays for it embedded; G1, G2 and G5 do not, since analog and error-mitigated machines emit no syndromes.

**IP & standards.** Riverlane holds GB 2641501 A "Quantum decoder" (Ziad, Zalawadiya, Barber, Škorić; filed 2024-05-31, published 2025-12-10) on grouped processing elements running clustering in hardware — adjacent to, not on, learned models [G][15][G:SURFACE-CODE-PATENTS]. Google LLC holds US 12,518,194 (granted 2026-01-06) on surface codes with densely packed gauge operators, which shapes the syndrome a decoder reads [G][15]. No dated patent-database count for neural-decoder families was found. Standards are absent; the de facto interfaces are NVQLink and CUDA-Q QEC, against open-source Stim, PyMatching and Tesseract.

**Roadmaps & track record.** Google DeepMind: "too slow for real time" (2024-11) · real-time decoding · delivered at distance 7 on 2026-07-08 [D][2]. Riverlane: sub-microsecond hardware decoding to distance 17 (2024–25) · delivered 2025-12 [D][5]; 10⁶ operations before 2030 (2026-03) · not yet testable [R][10]. NVIDIA: single-digit-microsecond quantum-classical link (2025-11) · demonstrated with IQM by 2026-03 [P][12]. IBM: Relay-BP under 1 µs/cycle (2025-10) · simulation only, target module slipped a year [S][13]. Google delivers and publishes; Riverlane delivers on engineering but is loose about its funding history; NVIDIA delivers plumbing; IBM's decoder promises run ahead of its hardware.

**Strategic reading.** If learned decoding becomes necessary rather than merely better, value migrates from the processor vendor to whoever owns the trained model and the silicon under it — and only Google owns chip, control loop and model together. IBM, Rigetti, IQM and Oxford Quantum Circuits would buy decoding — Riverlane's thesis. The two may split by regime: learned where accuracy binds, clustering where throughput binds. The substitution threat is physics — erasure conversion and lower physical error rates shrink the non-graphlike residue the network is paid to model. Bargaining power sits with AMD and NVIDIA, who sell into every branch.

*Open niche:* verification of learned decoders is an unclaimed niche suited to a small QCVV house. No published protocol certifies a decoder under distribution shift: a drift-stress benchmark, latency-tail reporting rather than means, and baseline-disclosure rules. A second entry point is the cold stage — single-flux-quantum or 4-K pre-decoding, where the published work is a design study and no device exists.

## Outlook & open questions

Confirm if by 2027-09 a learned decoder runs in real time at distance ≥ 9 with published latency tails, decodes a sparse quantum code on hardware, or is taped out as an ASIC. Demote if by 2028-09 none has run beyond distance 7 in real time, or a matching-class decoder comes within 5% of learned accuracy at distance ≥ 11 — that would make the silicon premium indefensible. Best case by 2029: learned decoding is default on superconducting machines at distance 15–25 on cold silicon, buying a distance step of physical-qubit savings. Worst case: erasure conversion and better physical error rates make graphlike decoders sufficient and the wall near distance 13 is never crossed.

Open questions. (1) Does the accuracy advantage grow, plateau or invert with distance once latency is charged honestly? (2) How fast does a fine-tuned model degrade between calibrations, and can training fold into the in-loop calibration agent? (3) Is there an architecture keeping O(d²) cost with full correlated-noise capacity outside simulation? (4) Can a learned decoder be certified when its worst case is unbounded? (5) Who pays when processor and decoder vendors differ?

Watch for: an AlphaQubit2 result on non-Google hardware; the first neural decoder on a bivariate-bicycle code; a cryogenic decoder tape-out; and NVQLink latency good enough for shared-accelerator decoding on transmons.

## Sources

[1] Bausch, Senior, Heras et al. (Google DeepMind, Google Quantum AI) · Learning high-accuracy error decoding for quantum processors · Nature 635, 834–840 · 2024-11-20 · https://www.nature.com/articles/s41586-024-08148-8
[2] Sivak, Morvan, Broughton et al. (Google Quantum AI) · Reinforcement learning control of quantum error correction · Nature 655 (8124), published 2026-07-08 · https://www.nature.com/articles/s41586-026-10759-2 · preprint arXiv:2511.08493 · https://arxiv.org/abs/2511.08493
[3] Google Quantum AI · Quantum error correction below the surface code threshold · Nature 638, 920 · 2024-12-09 · https://www.nature.com/articles/s41586-024-08449-y
[4] Scalable Neural Decoders for Practical Real-Time Quantum Error Correction · arXiv:2510.22724 · 2025-10 · https://arxiv.org/abs/2510.22724
[5] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane) · Local clustering decoder as a fast and adaptive hardware decoder for the surface code · Nature Communications 16, 11048 · 2025-12-17 · https://www.nature.com/articles/s41467-025-66773-x
[6] Yang, Sun, Wu, Zhang, Jiang, Linpeng, Zhou, Chu, Niu, Zhong, Liu, Yu (International Quantum Academy; Southern University of Science and Technology; Peking University; Hefei National Laboratory) · Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder · arXiv:2605.04892 · 2026-05-06 · https://arxiv.org/abs/2605.04892 · full text https://arxiv.org/html/2605.04892
[7] NVIDIA · NVQLink architecture integrates accelerated computing with quantum processors · developer blog [C] · 2025-11-17 · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
[8] Knapen, Tao, Mack et al. · Pinball: a cryo-CMOS surface-code pre-decoder · arXiv:2512.09807 · 2025-12-10 · https://arxiv.org/abs/2512.09807
[9] Riverlane · Riverlane raises $75 million · press release [C] · 2024-08-06 · https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology
[10] Riverlane · QEC Technology Roadmap · press release [C] · 2026-03-12 · https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap
[11] Qblox and Riverlane · Integration enabling real-time quantum error correction · PR Newswire [C] · 2026-03-17 · https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html
[12] Quantum Computing Report · IQM and Zurich Instruments develop real-time QEC via NVIDIA NVQLink [P] · 2026 · https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/
[13] IBM · Relay-BP: a fast and flexible decoder for quantum LDPC codes · arXiv:2510.21600 · 2025-10 · https://arxiv.org/abs/2510.21600
[14] DARPA · Quantum Benchmarking Initiative, Stage B selection · 2025-11 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[15] Riverlane Ltd · GB 2641501 A "Quantum decoder" (filed 2024-05-31, published 2025-12-10) · https://patents.google.com/patent/GB2641501A/en · with Google LLC US 12,518,194 (granted 2026-01-06)
[16] Google DeepMind · AlphaQubit: Google's research on quantum error correction · blog [C] · 2024-11-20 · https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction/

## Open verification items

- AlphaQubit2 has no stand-alone publication as of 3 Sep 2026; it is named and described only inside the July 2026 Nature paper [2]. Architecture, parameter count, host silicon and measured latency are unpublished.
- No Λ is reported for the distance-7 AlphaQubit2 run, so the gain attributable to the decoder rather than to the reinforcement-learning calibration cannot be separated.
- Riverlane Series C conflicts: $75 M (2024-08-06 release) versus "$85 million in 2024" and "$120 million+" (2026-03-12 roadmap release); no extension announcement located.
- Authors and affiliations of arXiv:2510.22724 were not retrieved (partial page content); its threshold figures are cited without attribution to a group.
- Export-control classification of a stand-alone decoder product is unverified; no ECCN confirmed from a primary source.
- Machine-learning decoding on neutral atoms (an offline ~1.7× gain appears in the main report's cross-cutting section) has no primary source here and is not carried in this brief.
- No dated patent-database count for neural-decoder patent families was found from a named database.
