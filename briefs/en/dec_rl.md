---
id: dec_rl
name: In-loop RL calibration / decoder steering
layer: "8 Decoder"
status: demonstrated
since: 2026
one_line: Detection events from the running code double as the reward signal for a reinforcement-learning agent that retunes control parameters during QEC, replacing scheduled recalibration.
verdict: One team, one chip, one paper; it improves the point error at fixed distance and is not shown to change Λ, which is what the 10⁻⁶ milestone actually needs.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
RL as a control optimiser on transmons is not new: the widely quoted 99.92% fluxonium CZ record is an RL-optimised *mean* of 99.922(9)% from 2023 [G:MIT-FLUXONIUM-CZ-2023], but offline and per-gate. Sivak, Morvan, Broughton, Cortiñas et al. (Google, arXiv 2025-11-11; Nature 655, 2026-07-08) changed the loop: detection events serve as both syndromes and learning signal, so calibration runs concurrently with computation [1].
a = 1.0, a fully engineered classical-control layer, f = coherent — it chases systematic drift (TLS, flux, temperature), not stochastic Pauli error [graph].

## Physics & limits
No new physical floor: this tracks an existing floor without the dead time between calibrations. The load-bearing claim is architectural — optimisation speed independent of system size [D][1], the only route past a per-parameter sweep that dies above ~10³ knobs. The limits follow from the reward: an error producing no detection event is invisible, so leakage inside the code space and Willow's roughly hourly correlated bursts are untouched, as is readout at ~10⁻². It does not change the exponent: no Λ is reported for the record d=7 run, so what moved is the point error at fixed distance, not the slope that decides whether d≈25 reaches 10⁻⁶.

## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2026-07-08 | d=7 surface code, real-time AlphaQubit2 decoding: 7.72(9)×10⁻⁴ per cycle; no Λ reported | Google Quantum AI | [D][1][G:ALPHAQUBIT2-2026-07] |
| 2026-07-08 | d=5 colour code, Tesseract decoder: 8.19(14)×10⁻³ per cycle; 3.5× stability against injected drift | Google Quantum AI | [D][1] |
| 2024-12-09 | Λ = 2.14(2) with the neural decoder vs 2.04(2) with ensembled matching on identical Willow syndromes | Google Quantum AI | [D][2][G:WILLOW-RTDECODER-2024] |

## Manufacturing, materials & supply chain
No dedicated silicon and, unlike matching or clustering decoders, no FPGA resource claim to audit [G:RIVERLANE-LCD-2025-12]. The cost is control-plane traffic — detection events out, parameter updates in, over the decoder's own link; NVQLink's 3.84 µs mean, 3.96 µs maximum round trip is the vendor-neutral version of it [C][G:NVQLINK-NUMBERS-2025-11]. Updates run on a slow timescale outside the 1.1 µs cycle, which is why it coexists with Willow where heavier in-loop computation would not. Supply is GPU/TPU capacity plus the control stack; no specific export rule.

## Role in the stack
Requires a decoder in the loop to steer against — the real-time neural decoder AlphaQubit2, which as of 4 Sep 2026 has no stand-alone publication and exists only inside the RL paper [G:ALPHAQUBIT2-2026-07]. Superconducting transmons only; derived round unchanged at 0.65 µs against the measured 1.1 µs QEC cycle, ~0.91 MHz. Verification: no Λ for the record run, no second-platform replication, and the only live closed-loop neural decoding elsewhere is a d=3 demonstration with a 550 ns loop [D][6]. Value conflict: 20% and >1,000 parameters come from trade press [P][3], the abstract gives 3.5× [D][1]; trust the paper.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | RL control, AlphaQubit2, Willow | [D][1] |
| Google DeepMind | developer | UK | Neural decoders, AlphaQubit line | [D][4] |
| Q-CTRL | supplier | AU | Boulder Opal calibration software | [C][5] |
| IQA Shenzhen | research | CN | Only live closed-loop neural decoding | [D][6] |

**Money.**
2024-10-08 · Q-CTRL · Series B expanded · USD $113 M (AUD $166 M) · GP Bullhound lead · closed [C][5]
2025-10-03 · Google Quantum AI · absorbed Atlantic Quantum, cold-stage control · undisclosed [P][G:GOOGLE-ATLANTIC-2025-10]
2025-11-06 · DARPA QBI Stage B · IBM the only transmon vendor, Google absent · ≤$15 M each [G:QBI-STAGEB-2025-11]

**Market & supply chain.** No component market; the priced substitute is calibration software plus GPU/TPU cycles, sold only by Q-CTRL, on Diraq, Oxford Quantum Circuits and Rigetti [C][5]. Pays G3/G4.

**IP & standards.** No dated patent family for RL-steered QEC calibration as of 4 Sep 2026; Google publishes the method and withholds the decoder — that is the moat.

**Roadmaps & track record.** Google's next milestone, a long-lived logical qubit at 10⁻⁶ (no date): 7.72×10⁻⁴ at d=7 is three orders short, needing d≈25 at Λ≈2 [D][2]; Google is absent from QBI Stage B [G]. Q-CTRL shipped Boulder Opal on three platforms by 2024-10 — delivered, at nothing like Google's scale.

**Strategic reading.** Software margin on hardware someone else owns. If it diffuses, control vendors and Q-CTRL capture it and calibration headcount falls; if AlphaQubit2 stays unpublished, Google's advantage is the decoder, not the RL. Substitution threat: hardware that drifts less — fluxonium, cold-stage SFQ control — shrinks the problem.

*Open niche:* the 3.5× is measured against drift the same team injected. A QCVV shop can define the platform-neutral drift-injection and reporting protocol that nothing currently standardises, and settle whether RL steering moves Λ or only the point error at fixed distance.

## Outlook & open questions
Confirm if RL-in-loop calibration appears on a second platform, or a Λ is published for an RL-steered run; demote if it stays Willow-only. Best case 2029: standard across superconducting FT stacks, sold by control vendors. Worst case: one unreplicated chip. Open: does size-independent optimisation survive outside simulation, and can the loop be made decoder-agnostic?

## Sources
[1] Sivak, Morvan, Broughton, Cortiñas et al. (Google Quantum AI), "Reinforcement learning control of quantum error correction", Nature 655, 2026-07-08 (preprint arXiv:2511.08493, 2025-11-11) — https://www.nature.com/articles/s41586-026-10759-2
[2] Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920, 2024-12-09 — https://www.nature.com/articles/s41586-024-08449-y
[3] "Google uses AI reinforcement learning for quantum error correction", The Next Platform, 2026-07-20 [P] — https://www.nextplatform.com/compute/2026/07/20/google-uses-ai-reinforcement-learning-for-quantum-error-correction/5275023
[4] Bausch et al. (Google DeepMind / Google Quantum AI), "Learning high-accuracy error decoding for quantum processors", Nature 635, 834–840, 2024-11-20 — https://www.nature.com/articles/s41586-024-08148-8
[5] Q-CTRL, "Q-CTRL sets global quantum technology fundraising record, increasing Series B to USD $113M, led by GP Bullhound", 2024-10-08 [C] — https://q-ctrl.com/blog/q-ctrl-sets-global-quantum-technology-fundraising-record-increasing-series-b-to-usd-113m-led-by-gp-bullhound
[6] Yang, Sun, Wu et al. (IQA Shenzhen / SUSTech / Peking University / Hefei), "Real-time surface-code error correction using an FPGA-based neural-network decoder", arXiv:2605.04892, 2026-05-06 — https://arxiv.org/abs/2605.04892
[G] AlphaQubit2 is named and described as "a scalable and real-time neural decoder for topological quantum codes" in Sivak, Morvan, Broughton et al. (Google Quantum AI), "Reinforcement… · 2026-07-08 · https://link.springer.com/article/10.1038/s41586-026-10759-2
[G] Google Quantum AI, "Quantum error correction below the surface code threshold" (Nature 638, 920; arXiv:2408.13687): the real-time decoder for the distance-5 10^6-cycle run is a spe… · 2024-12-09 · https://arxiv.org/abs/2408.13687
[G] Ding, Hays, Sung, ... Serniak, Oliver (MIT / MIT Lincoln Laboratory), Phys. Rev. X 13, 031035 (2023-09-25): fluxonium CZ with transmon coupler, peak CZ fidelities 99.85-99.9%, rein… · 2023-09-25 · https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035
[G] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane), "Local clustering decoder as a fast and adaptive hardware decoder for the surface code", Nature Communications… · 2025-12-17 · https://www.nature.com/articles/s41467-025-66773-x
[G] NVIDIA developer blog (2025-11-17) detail: RoCE round trip 3.84 us mean, 0.035 us standard deviation, 3.96 us MAXIMUM over 1,000 samples (a bounded tail, not just a mean); BP+OSD o… · 2025-11-17 · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
[G] Atlantic Quantum (fluxonium, cold-stage control) joined Google Quantum AI, 2025-10-03 · 2025-10-03 · https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/
[G] DARPA QBI Stage B (announced 2025-11-06, ~12 months, up to $15 M each): Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon… · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
## Open verification items
- No Λ is reported for the RL-steered d=7 run, so the effect on code-distance scaling is unmeasured.
- The "~20% logical-error reduction" and ">1,000 live control parameters" figures appear only in trade press [3]; the paper's abstract quotes 3.5× and tens of thousands of parameters in simulation.
- AlphaQubit2 has no stand-alone publication as of 4 Sep 2026.
- No second-platform replication of RL-in-loop calibration found.
- Q-CTRL's Series B is quoted as USD $113 M by the company and as "$167 M" in Australian trade press, which is the AUD $166 M figure restated; the company release governs.
