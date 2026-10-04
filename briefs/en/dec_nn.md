---
id: dec_nn
name: Neural decoders (AlphaQubit 2, CNN, transformers)
layer: "8 Decoder"
status: demonstrated
since: 2024
one_line: "Learned syndrome decoders — recurrent transformers, CNNs, LSTMs, state-space models — that beat matching by absorbing non-Pauli device noise from data."
verdict: "The accuracy lead is real, but real-time speed is shown only on recorded or simulated data, to distance 11, and live only at distance 3; the open question is whether the lead survives live throughput and drift beyond distance 11."
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A neural decoder replaces the combinatorial inference step of error correction with a trained function approximator: syndrome history in, logical correction out. Decoding is Bayesian inference over a detector-error hypergraph, and minimum-weight perfect matching is exact only when that hypergraph is graphlike — every error flips at most two detectors, with independent, known, static probabilities. Real devices break all three: leakage parks a qubit outside the computational subspace for many rounds, correlated bursts couple distant detectors, readout is analog before thresholding, and noise drifts. A learned decoder fits the joint distribution from labelled data instead, consuming soft readout and leakage flags matching cannot represent. The lineage runs from convolutional decoders (2017) to the recurrent-transformer AlphaQubit, published by Google DeepMind with Google Quantum AI on 2024-11-20 [D][657][G:ALPHAQUBIT-2024-11], and to AlphaQubit 2, named in the July 2026 Willow paper as "a scalable and real-time neural decoder for topological quantum codes" [D][2].

Attributes: carrier affinity 0.5 and no carrier of its own; no characteristic time or entangling operation, inheriting the host's syndrome period (1.1 µs on Willow [D][1][G:WILLOW-QEC-2024-12]); no readout, though it consumes the soft values matching discards; no mobility beyond the detector-error graph it was trained on; no control modality — placement is the variable, room-temperature logic today, cold silicon proposed; Pauli error structure, with its value in the non-Pauli residue; no manufacturing of its own.

## Physics & limits

The floor is information-theoretic and computational, not physical: the ceiling is maximum-likelihood decoding, and matching sits measurably below it. On Sycamore data AlphaQubit reached 2.748(15)×10⁻² logical error per round at distance 5 against 2.915(16)×10⁻² for the tensor-network decoder, an approximate maximum-likelihood decoder, and 2.901(23)×10⁻² versus 3.028(23)×10⁻² at distance 3 — about 6% and 4% fewer errors [D][657]; against correlated matching at distance 5 it made ~30% fewer [C][731]. On simulated data with crosstalk and leakage, correlated matching tuned to that noise and fed the analog readouts made 1.25× AlphaQubit's errors at distance 3, 1.4× at 9 and 1.25× at 11 [D][657]. The lead holds out to distance 11 without growing steadily, and it comes from noise outside matching's model — crosstalk and leakage.

The computational limit is the backlog condition: a decoder slower than the syndrome rate accumulates an unbounded queue and the logical clock stalls, which on a transmon means roughly 10⁶ decode-rounds per second per logical qubit. Google's 2024 framing: AlphaQubit "is still too slow to correct errors in a superconducting processor in real time" [C][731]. Cost scaling is architectural: attention over a distance-d patch is O(d⁴) per round against O(d²) for a state-space recurrence, and the cheaper model measured a *higher* real-time threshold, 1.04% versus 0.97%, because latency-induced degradation belongs in that figure of merit [S][732].

Failure modes are statistical: distribution shift degrades a fine-tuned model with no error signal, retraining needs data from the same processor, and there is no proved threshold, only a measured one. Soft information, joint training with the calibration loop and O(d²) architectures would move the floor.

## Engineering state of the art

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-11 | Distance-5 Sycamore memory 2.748(15)×10⁻²/round vs 2.915(16)×10⁻² for the tensor-network decoder (~6% fewer errors); at simulated distance 11 matching makes 1.25× as many errors | Google DeepMind (AlphaQubit) | [D][657][G:ALPHAQUBIT-2024-11] |
| 2025-10 | State-space decoder: real-time threshold 1.04% vs 0.97% transformer, O(d²) vs O(d⁴) per round | Yonsei University | [S][732] |
| 2025-12 | Non-neural bar: clustering decoder under 1 µs/round to distance 17 on one Xilinx VU19P, ~6% of logic cells | Riverlane | [D][238][G:RIVERLANE-LCD-2025-12] |
| 2026-05 | First closed-loop neural decoding on hardware: 124 ns decode, 184 ns throughput period, 550 ns loop, distance 3, 6.9(2)%/round vs offline matching 7.2(2)% | International Quantum Academy | [D][729] |
| 2026-07 | AlphaQubit 2 decodes the distance-7 Willow record, 7.72(9)×10⁻⁴ logical error per cycle, with no live decode stated; its own preprint times under 1 µs per cycle to distance 11 on TPUs, on recorded or simulated data | Google Quantum AI | [D][2][G:ALPHAQUBIT2-2026-07] |

Best demonstrated splits in two: for accuracy, the July 2026 Willow record, decoded with no live loop stated [D][2]; for live operation, the Shenzhen distance-3 loop [D][729]. Google's only live surface-code decode remains the 2024 distance-5 Willow run, on a Sparse Blossom matcher [G:WILLOW-RTDECODER-2024]. Typical at scale is still matching or clustering; beyond Google, too, neural decoders run offline or without a stated real-time loop — on Zuchongzhi 3.2, the 448-atom fault-tolerant processor and Sqale. The decoder's own budget is dominated by model mismatch and latency, not arithmetic precision — the Shenzhen implementation quantised weights to 6-bit integers and lost nothing against offline matching [D][729]. At system level the distance-7 record is limited by two-qubit gate and readout errors, and no Λ is reported for it [D][2].

## Manufacturing, materials & supply chain

The node is fabricated only through its host; three placements exist as of 3 Sep 2026. In room-temperature logic, the Shenzhen LSTM (32 hidden units, separate X and Z decoders, four pipelined stages on DSP blocks) fits a mid-range AMD Kintex-7 XC7K410T at distance 3, with current parts ceilinged near distance 13 [D][729]; Riverlane's clustering decoder takes ~6% of the lookup tables of a Xilinx VU19P to distance 17 [D][238][G:RIVERLANE-LCD-2025-12] — a learned decoder buys accuracy with silicon. On graphics processors, NVQLink puts a GH200-class host in the loop at 3.84 µs mean round trip [C][324][G:NVQLINK-2025]. In cold silicon, the "Pinball" cryo-CMOS predecoder claims 3,780× syndrome-bandwidth reduction under 0.56 mW at 4 K, but is an unfabricated design study [S][733][G:PINBALL-2025-12].

AMD (Xilinx) and NVIDIA supply essentially all decode silicon, with no second source at the part sizes required. Yield is not a decoder problem; portability is — a fine-tune is per-processor, and nobody has published how many devices one trained model covers. Export exposure is indirect: the decoder ships as firmware in a control rack and inherits the accelerator's controls and the classification of the system it serves.

## Control, readout & I/O burden

The burden is bandwidth and latency, not lines or lasers. A distance-7 patch produces 48 ancilla bits per 1.1 µs cycle — about 44 Mbit/s per logical qubit, so ~4.4 Gbit/s at 100 logical qubits and ~44 Gbit/s at 1,000, every bit needing a decision inside the feedback window. At 10³ physical qubits one mid-range part suffices. At 10⁴ the wall is aggregate: dozens of patches wanting sub-microsecond turnaround, and NVQLink's 3.84 µs round trip is three and a half Willow cycles — fine for millisecond-cycle ion and atom machines, marginal for transmons unless decode is local to the fridge [C][324][G:NVQLINK-2025]. At 10⁶ neither room-temperature fabric nor a shared accelerator closes, and the syndrome must be reduced in the cold stage [S][733]. The Shenzhen result proves the loop closes at all: 222 ns acquisition, 148 ns decoder logic and 180 ns electronic delay inside a 1.25 µs cycle [D][729].

## Role in the stack

It sits on the superconducting transmon architecture (Google, IBM, Rigetti, IQM, Oxford Quantum Circuits, USTC/Zhejiang, Fujitsu) and the alkali neutral-atom architecture (Harvard/MIT, QuEra, Pasqal, Infleqtion, Google), reaching both. It requires the rotated surface code and its yoked variants — every deployed model is trained on surface-code syndromes, and none has run on a sparse quantum parity-check code. It is not part of the in-loop reinforcement-learning calibration: that agent learns from the detection-event rate and reweights a matching graph, and AlphaQubit 2 decoded the calibrated record run separately [D][2]. It replaces minimum-weight perfect matching at an asymmetric switching price — going learned costs a training pipeline, per-device fine-tuning and worst-case guarantees; going back costs only accuracy.

Nothing in the architecture is superconducting-specific, so the same family serves millisecond-cycle atom machines offline and microsecond-cycle transmons only with dedicated silicon; only the training data and latency budget differ. Contribution to the derived clock (derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the architecture): zero while decode latency stays under the syndrome period — 0.65 µs derived on the transmon architecture — which it does live only at distance 3, where feedback-conditioned operations consume 0.55 µs of a 1.25 µs cycle [D][729], and to distance 11 only on recorded or simulated data [G:ALPHAQUBIT2-2026-07]. Neighbouring empty slots: a fabricated cryogenic neural-decoder ASIC, and a learned decoder for bivariate bicycle codes on hardware.

## Evidence — how the numbers were measured

Headline numbers come from memory experiments — run N syndrome rounds, fit logical fidelity against N — decoded offline or, since 2026, in the loop. The protocol misses three things. The baseline is a choice: on the same distance-5 Sycamore data AlphaQubit makes ~6% fewer errors than the tensor-network decoder [D][657] but ~30% fewer than correlated matching [C][731], and 20–29% fewer than matching in simulation to distance 11 [D][657] — so a single band over matching mixes two baselines. Generalisation is untested: a model fine-tuned on one processor and evaluated on it is not evidence of transfer. And latency distributions are rarely reported, though only the tail causes backlog.

Conflicts: none over AlphaQubit — the blog's "6% fewer errors than tensor network methods" and "30% fewer errors than correlated matching" both describe the largest Sycamore experiments [C][731] and agree with the Nature figures, 5.7% below the tensor-network decoder at distance 5 [D][657]; the two percentages differ by baseline, not by regime. Riverlane's Series C is announced as $75 M (2024-08-06) but its 2026 roadmap states "$85 million in 2024" and "$120 million+" total [C][661][G:RIVERLANE-FUNDING]; trust the 2024 release. No group has replicated AlphaQubit 2 on non-Google hardware as of 3 Sep 2026.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Google DeepMind | developer | UK | AlphaQubit and AlphaQubit 2 architecture and training | [D][2], [657] |
| Google Quantum AI | developer | US | Decoded the distance-7 Willow record with AlphaQubit 2, no live decode stated | [D][2] |
| Riverlane | supplier | UK | Sells the deterministic rival (clustering decoder, Deltaflow) | [D][238][C][658] |
| NVIDIA | supplier | US | NVQLink and CUDA-Q QEC; 3.84 µs host-in-the-loop round trip | [C][324] |
| International Quantum Academy | research | CN | First closed-loop neural decoder on a superconducting chip | [D][729] |
| Qblox | supplier | NL | Control hardware for the sub-microsecond closed loop | [C][659] |
| IBM | developer | US | Relay-BP decoder, under 1 µs/cycle in simulation | [S][48] |
| AMD | supplier | US | Kintex-7 and Virtex parts hosting both decoder families | [D][238], [729] |

**Money.**
- 2024-05-01 · Riverlane · Horizon Europe EIC Transition grant (SkyTALE, with Qblox) · £2.1 M · European Innovation Council · closed [G:RIVERLANE-FUNDING]
- 2024-08-06 · Riverlane · Series C · $75 M · Planet First Partners (lead), ETF Partners, EDBI, Cambridge Innovation Capital, Amadeus, NSSIF, Altair · company later states $85 M, $120 M+ cumulative · closed, disputed [C][661][G:RIVERLANE-FUNDING]
- 2025-11-17 · NVIDIA · NVQLink launch, price undisclosed; Quantinuum Helios first deployment · — · announced [C][324][G:NVQLINK-2025]
- 2025-11 · DARPA · QBI Stage B: eleven teams, no pure decoder vendor · — · programme record [G][65]
- 2026-03-12 · Riverlane · roadmap: 10⁶ reliable operations before 2030, 10¹² from 2033 · — · roadmap [C][R][658][G:RIVERLANE-ROADMAP-2026-03]
- 2026-03-17 · Qblox and Riverlane · closed-loop demo, 250 physical / 1 logical qubit, 10,000 operations · — · announced [C][659][G:QBLOX-RIVERLANE-2026-03]

**Market & supply chain.** There is no decoder market in the ordinary sense: Google's decoder is captive, and the one merchant vendor of consequence, Riverlane, sells a deterministic decoder rather than a trained model. Enabling equipment is AMD programmable logic, NVIDIA accelerators and control racks from Qblox, Zurich Instruments and Quantum Machines; concentration risk sits with two American vendors. Unit economics are unquotable; the resource data give a proxy of one to two orders of magnitude more silicon per logical qubit than clustering. G3 and G4 pay for this node and G7 pays for it embedded; G1, G2 and G5 do not, since analog and error-mitigated machines emit no syndromes.

**IP & standards.** Riverlane holds GB 2641501 A "Quantum decoder" (Ziad, Zalawadiya, Barber, Skoric; filed 2024-05-31, published 2025-12-10) on grouped processing elements running clustering in hardware — adjacent to, not on, learned models [G][662][G:SURFACE-CODE-PATENTS]. Google LLC holds US 12,518,194 (granted 2026-01-06) on surface codes with densely packed gauge operators, which shapes the syndrome a decoder reads [G][656]. No dated patent-database count for neural-decoder families was found. Standards are absent; the de facto interfaces are NVQLink and CUDA-Q QEC, against open-source Stim, PyMatching and Tesseract.

**Roadmaps & track record.** Google DeepMind: "too slow for real time" (2024-11) · real-time decoding · under 1 µs per cycle to distance 11 on recorded or simulated data (preprint, 2025-12-08), with no live decode stated for the distance-7 record of 2026-07-08 — not yet delivered on hardware [G:ALPHAQUBIT2-2026-07][D][2]. Riverlane: sub-microsecond hardware decoding to distance 17 (2024–25) · delivered 2025-12 [D][238]; 10⁶ operations before 2030 (2026-03) · not yet testable [R][658]. NVIDIA: single-digit-microsecond quantum-classical link (2025-11) · demonstrated with IQM by 2026-03 [P][239]. IBM: Relay-BP under 1 µs/cycle (2025-10) · simulation only, target module slipped a year [S][48]. Google delivers and publishes; Riverlane delivers on engineering but is loose about its funding history; NVIDIA delivers plumbing; IBM's decoder promises run ahead of its hardware.

**Strategic reading.** If learned decoding becomes necessary rather than merely better, value migrates from the processor vendor to whoever owns the trained model and the silicon under it — and only Google owns chip, control loop and model together. IBM, Rigetti, IQM and Oxford Quantum Circuits would buy decoding — Riverlane's thesis. The two may split by regime: learned where accuracy binds, clustering where throughput binds. The substitution threat is physics — erasure conversion and lower physical error rates shrink the non-graphlike residue the network is paid to model. Bargaining power sits with AMD and NVIDIA, who sell into every branch.

## Outlook & open questions

Confirm if by 2027-09 a learned decoder runs live in real time at distance ≥ 9 with published latency tails, decodes a sparse quantum code on hardware, or is taped out as an ASIC. Demote if by 2028-09 none has run live beyond distance 7, or a matching-class decoder comes within 5% of learned accuracy at distance ≥ 11 — that would make the silicon premium indefensible. Best case by 2029: learned decoding is default on superconducting machines at distance 15–25 on cold silicon, buying a distance step of physical-qubit savings. Worst case: erasure conversion and better physical error rates make graphlike decoders sufficient and the wall near distance 13 is never crossed.

Open questions. (1) Does the accuracy advantage grow, plateau or invert with distance once latency is charged honestly? (2) How fast does a fine-tuned model degrade between calibrations, and can training fold into the in-loop calibration agent? (3) Is there an architecture keeping O(d²) cost with full correlated-noise capacity outside simulation? (4) Can a learned decoder be certified when its worst case is unbounded? (5) Who pays when processor and decoder vendors differ?

Watch for: an AlphaQubit 2 result on non-Google hardware; the first neural decoder on a bivariate bicycle code; a cryogenic decoder tape-out; and NVQLink latency good enough for shared-accelerator decoding on transmons.

## References
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[48] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[238] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[239] M. Abdel-Kareem, “IQM and Zurich Instruments Develop Real-Time QEC via NVIDIA NVQLink,” Quantum Computing Report, Mar. 17, 2026. [Online]. Available: https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/ [P]
[324] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[656] Google LLC, “Surface codes with densely packed gauge operators,” U.S. Patent 12,518,194 B2, Jan. 6, 2026. [Online]. Available: https://patents.google.com/patent/US12518194B2/en Also https://patents.justia.com/search?q=%22surface+code%22+quantum+error+correction&company=google. [G]
[657] J. Bausch *et al.*, “Learning high-accuracy error decoding for quantum processors,” *Nature*, vol. 635, no. 8040, pp. 834–840, Nov. 2024, doi: [10.1038/s41586-024-08148-8](https://doi.org/10.1038/s41586-024-08148-8). [D]
[658] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [R]
[659] Qblox; Riverlane, “Qblox and Riverlane Demonstrate Integration Enabling Real-Time Quantum Error Correction,” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[661] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[662] A. B. Ziad, A. Zalawadiya, B. Barber, and L. Skoric, “Quantum decoder,” Google Patents, Dec. 10, 2025. [Online]. Available: https://patents.google.com/patent/GB2641501A/en [G]
[729] X. Yang *et al.*, “Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder,” [arXiv:2605.04892](https://arxiv.org/abs/2605.04892), May 2026. Also https://arxiv.org/html/2605.04892. [D]
[731] Google DeepMind and Google Quantum AI, “AlphaQubit tackles one of quantum computing's biggest challenges,” Google The Keyword, Nov. 20, 2024. [Online]. Available: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction/ [C]
[732] C. Lee, T. Hur, and D. K. Park, “Scalable Neural Decoders for Practical Real-Time Quantum Error Correction,” [arXiv:2510.22724](https://arxiv.org/abs/2510.22724), Oct. 2025. [S]
[733] A. Knapen *et al.*, “Pinball: A Cryogenic Predecoder for Surface Code Decoding Under Circuit-Level Noise,” [arXiv:2512.09807](https://arxiv.org/abs/2512.09807), Dec. 2025. [S]

## Open verification items

- AlphaQubit 2's own paper is a preprint (arXiv:2512.07737, v1 2025-12-08, v2 2026-03-11): it decodes recorded Willow data at distances 3–7 and times under 1 µs per cycle to distance 11 on Trillium TPUs, on recorded or simulated data; no live decode on hardware is reported, and the July 2026 Nature paper [2] does not state that its distance-7 decode ran live [G:ALPHAQUBIT2-2026-07].
- No Λ is reported for the distance-7 AlphaQubit 2 run, so the gain attributable to the decoder rather than to the reinforcement-learning calibration cannot be separated.
- Riverlane Series C conflicts: $75 M (2024-08-06 release) versus "$85 million in 2024" and "$120 million+" (2026-03-12 roadmap release); no extension announcement located.
- arXiv:2510.22724 is by C. Lee, T. Hur and D. K. Park (Yonsei University) [732]; its real-time thresholds are simulated — a standard superconducting circuit-noise model (SI1000) plus injected noise standing for decoder latency.
- Export-control classification of a stand-alone decoder product is unverified; no ECCN confirmed from a primary source.
- Machine-learning decoding on neutral atoms has one primary source: atom-loss information plus machine-learning decoding improved QEC performance 1.73(13)× over conventional decoding on Harvard/MIT/QuEra data from up to 448 atoms, decoded in post-processing [4]; the gain is unreplicated outside that dataset.
- No dated patent-database count for neural-decoder patent families was found from a named database.
