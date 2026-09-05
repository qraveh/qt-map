---
id: ro_qcap
name: rf quantum-capacitance parity readout
layer: "6 Readout"
tier: 3
status: emerging
since: 2025
one_line: Dispersive gate sensing of a Majorana island's quantum capacitance by rf reflectometry, reading fermion parity without charge transfer; non-destructive and mid-circuit.
verdict: The method is real and independently replicated; falsified as fault-tolerance-grade unless an assignment error below 10⁻³ at a stated integration time is published by 2028, on any stack.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A dot–nanowire interference loop's ground state disperses differently with gate charge in the two parity sectors; that curvature is a quantum capacitance, read as a dispersive shift of an off-chip resonator by rf reflectometry, with no charge transfer. Microsoft, Nature 2025-02-19: 1% assignment error, SNR 1 in 3.6 µs, dwell above 1 ms near 2 T [D][1]. This is the single-wire (Z-type) measurement; the joint projection a gate needs is unbuilt.
a fabricated (1.0) · b not a gate · c quantum capacitance, ~4 µs, non-destructive, mid-circuit
d no transport · e rf reflectometry from room temperature · f assignment error plus poisoning · g MBE wire stack

## Physics & limits
Signal accumulates as √t while parity survives only until a quasiparticle arrives, so assignment error is a race, modelled as err ≈ ½[1 − e^(−2t/τ)·erf(SNR/√2)²] at mean SNR near 1.2 per µs [D][2]. The floor is the poisoning time τ, set by loop geometry, not the amplifier: the same device gives 12.4 ms on the Z loop against 14.5 µs on the X loop, attributed to the two-loop configuration's larger quasiparticle-capture cross-section [D][2]. Lead replaced aluminium to raise τ [D][3]. What it reads is contested: Nature's editor's note says the results do not by themselves establish Majorana zero modes [P][7].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-02 | 1% assignment error, SNR 1 in 3.6 µs, dwell >1 ms, InAs–Al | Microsoft Azure Quantum | [D][1] |
| 2026-02 | Independent single-shot parity readout, ~1.85 ms switching, InSb Kitaev chain | QuTech | [D][4] |
| 2026-06 | ~20 s parity switching in one InAs–Pb wire, same readout family | Microsoft Quantum | [D][3] |
Typical at scale is undefined: no multiplexed multi-tetron readout is published; the 2026 device came up one wire at a time [D][3].

## Manufacturing, materials & supply chain
No dedicated process: dots, gates and loop share the wire device's lithography, resonator off-chip. Room-temperature rf drive and demodulation feed a millikelvin amplifier, from the merchant control-electronics base superconducting readout uses [C][G:NVQLINK-LAUNCH-2025-10-28]; no single point of failure beyond the wire stack, and no export-control category specific to it. I/O is a gate line and a resonator per measurable parity, multiplexed on a shared feedline: 10³ is solved packaging. The wall is time: 3.6 µs is fast against 12.4 ms, slow against 14.5 µs, so at 10⁴–10⁶ the limit is how many X projections fit in the shorter window.

## Role in the stack
The one demonstrated block the topological path owns: it requires the Majorana-parity carrier and provides the projective measurement a measurement-based gate would consume, non-destructively and mid-circuit, the precondition for measurement-only architecture. It sets the path's derived clock alone: max(gate, readout, transport) = ~3.6 µs to SNR 1 [D][1]. Verification: QuTech's Nature paper (2026-02-11) independently replicates the principle on InSb dot-based Kitaev chains rather than a tetron, at ~1.85 ms telegraph lifetimes [D][4]; its follow-up shows coherent parity oscillations with only limited protection [D][5]. Legg disputes whether the read regions are gapped at all [D][6]. Nobody has replicated the 1% error.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Microsoft Quantum | developer | US | Originated the method; used on every tetron device | [D][1] |
| QuTech | research | NL | Independent parity readout and coherent parity qubit, on Eindhoven-grown InSb wires | [D][4] |
| DARPA | investor | US | Funds the only industrial user; US2QC final stage since 2025-02-06 | [G:MSFT-US2QC-PARTNERS-2025-02] |

**Money.** 2025-02-06 · Microsoft · US2QC final Validation & Co-Design stage · undisclosed · DARPA · announced [G:MSFT-US2QC-PARTNERS-2025-02]. 2026-01-23 · Microsoft · Quantum Pioneers Program, readout an award topic · ≤ USD 200,000 per proposal · announced [P][G:MSFT-QUPP-2026-01].

**Market & supply chain.** No standalone market; rf reflectometry and cryogenic amplification are generic and multi-sourced, so concentration risk sits in the wire stack. G3 and G4 only.

**IP & standards.** Dispersive gate sensing is common property across semiconductor-qubit groups; no dated patent count specific to parity readout as of 4 Sep 2026.

**Roadmaps & track record.** (used in every public Microsoft device from 2025-02, implicitly for fault tolerance by 2029; status 4 Sep 2026: no fidelity or speed target published for the readout) [C][8]. QuTech publishes with no schedule to defend, the more credible record.

**Strategic reading.** The method is public and replicated, so Microsoft's exclusivity has moved into the wire stack; whoever first publishes assignment error near 10⁻³ at a stated integration time sets the downstream pace.

*Open niche:* Re-deriving assignment error against integration time from published traces, separating infidelity from poisoning, is a QCVV exercise on open data.

## Outlook & open questions
Falsifiable in 12–24 months: a third group publishing parity readout; a sub-1% assignment error from anyone but Microsoft; a directly measured poisoning rate. Confirm if two land; demote if it stays a two-laboratory result to 2028. Best case, readout stops being the open variable; worst case, τ on a joint loop stays in tens of µs. Open: does multiplexed multi-tetron readout work; is 1% reproducible off Microsoft's devices.

## Sources
[1] Microsoft Azure Quantum — "Interferometric single-shot parity measurement in InAs–Al hybrid devices" — Nature 638, 651–655 — 2025-02-19 — https://www.nature.com/articles/s41586-024-08445-2
[2] Aghaee et al. (Microsoft Quantum) — tetron parity lifetimes and continuous dispersive readout — arXiv:2507.08795 — 2025-07 — https://arxiv.org/abs/2507.08795
[3] Aghaee et al. (Microsoft Quantum) — "20 Second Parity Lifetime in an InAs–Pb Tetron Device" — arXiv:2606.03884 — 2026-06-02 — https://arxiv.org/abs/2606.03884
[4] van Loo, Zatelli, Steffensen, Roovers et al. (QuTech/TU Delft, TU Eindhoven, CSIC) — "Single-shot parity readout of a minimal Kitaev chain" — Nature 650 — 2026-02-11 — https://www.nature.com/articles/s41586-025-09927-7
[5] Zatelli, Roovers, van Loo et al. (QuTech/TU Delft) — "Majorana parity qubit in coupled minimal Kitaev chains" — arXiv:2607.09511 — 2026-07-10 — https://arxiv.org/abs/2607.09511
[6] Legg — "On the robustness of topological gap detection via transport" — Nature, Matters Arising — 2026-06-24 (Microsoft reply same day) — https://www.nature.com/articles/s41586-026-10567-8
[7] APS Physics — coverage of the Microsoft parity-readout paper, including Nature's editor's note [P] — 2025 — https://physics.aps.org/articles/v18/57
[8] Microsoft — "Majorana 2: a scalable, error-corrected quantum processor" — Azure Quantum blog [C] — 2026-06 — https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor
[9] DARPA — "Quantum computing approaches" (US2QC) — DARPA news — 2025-02-06 — https://www.darpa.mil/news/2025/quantum-computing-approaches

## Open verification items
The mean SNR ~1.2 per µs and the assignment-error expression come from the arXiv full text of [2], not from the fact-checked report summary; that text also gives X ~4 µs and Z ~9.3 ms for other tunings against the 14.5 µs / 12.4 ms used here. The quasiparticle poisoning rate during a readout dwell has never been measured directly, only inferred. No multiplexed multi-tetron readout and no readout-specific R&D spend is public.
