---
id: code_fusion
name: Fusion-based fault tolerance
layer: "7 Code"
status: theory
since: 2030
one_line: "A fault-tolerant code assembled from destructive linear-optical fusions on pre-made photonic resource states, tolerating 2.7-17.4% photon loss in theory and never run end-to-end."
verdict: "Real: loss thresholds derived in simulation, 2.7% (boosted 6-ring) to 17.4% ({7,4} encoded). Unproven: any hardware run of the scheme; only components exist. Demote if no fusion-lattice demonstration by 2029."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A fault-tolerant architecture with no deterministic two-qubit gate: pre-made photonic resource states are consumed by destructive linear-optical fusions, and the code lives in the pattern of which fusions succeeded, failed or reported loss. Bartolucci, Birchall, Bombín and colleagues at PsiQuantum formalised it with thresholds in 2023 [S][1]. It replaces GKP-bosonic concatenation as photonics' route to fault tolerance. Coordinates: flying photons, no native control modality and no clock of its own; pure-loss errors, no manufacturing precursor beyond fusion and resource-state generation.

## Physics & limits
Loss is the design variable: a lost photon heralds a fusion failure, that failure is an erasure with a known location, and the decoder routes around it. Hence unusually high tolerances — 2.7% loss per photon with a boosted 6-ring, 17.4% with a {7,4}-encoded state of ~168 photons nobody can make [S][2]. The catch sits below threshold. A 2026 re-analysis shows fusion failure alone, at zero physical loss, leaves a logical-error floor shrinking only with code distance, so being under threshold says nothing about the overhead for 10⁻¹⁰; emitter-mediated fusion raises the threshold to 7.0–7.3% against an unencoded 6-ring's 0.38–0.82% [S][4][G:SPARROW-SUBTHRESHOLD-2026-06]. Moving the floor takes lower-loss photonics, boosted fusion, or emitters.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2023-02 | FBQC framework and thresholds derived | Bartolucci et al., PsiQuantum | [S][1] |
| 2025-02 | Component fusion Bell fidelity 99.22% | PsiQuantum | [D][3] |
| 2025-06 | Loss threshold 2.7% (boosted 6-ring) to 17.4% ({7,4}) | theory | [S][2] |
| 2026-06 | Fusion-failure floor at zero loss; 7.0–7.3% emitter threshold | Sparrow | [S][4] |

On the report's cross-platform table photonics scores zero on every fault-tolerance primitive: no below-threshold scaling, no logical qubit past break-even, no logical two-qubit gate, detection-only decoding [D][7].

## Manufacturing, materials & supply chain
Nothing is manufactured for this code; it inherits the photonic-IC stack of its inputs (300 mm silicon at GlobalFoundries) [C][G:GF-QTS-2026-05]. No yield, cost or energy figure exists because nothing runs it. The burden it imposes is synchronisation: a {7,4}-encoded state means ~168 photons per round, each with a source, switch path and detector channel, against a record of 8 fused photons at 0.4–2.3 per minute [D][5]. At 10³ fusions/s the constraint is switch loss; at the 10⁶ a useful machine needs, cryogenic detector channels and GHz feed-forward, neither built. ECCN 4A906 covers the assembled machine [G:BIS-QUANTUM-ECCN-2024-09].

## Role in the stack
Requires linear-optical fusion and a resource-state factory, neither at code-relevant scale, and provides nothing downstream — it tops the photonic fusion path (PsiQuantum, Quandela, QuiX). It replaces GKP-bosonic concatenation, and the switch is total: different carrier, detectors, error model. Its MHz cycle is a design claim, not a measurement: the real cycle is resource-state supply, ~0.4–2.3 per minute [D][5]. Verification: the thresholds are decoder simulations under stated noise models, never measured or independently reproduced; the 2026 re-analysis is the first published challenge to the framework's relevance, unanswered as of 4 Sep 2026.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US | Originated FBQC; sole roadmap bet on it | [S][1] |
| Quandela | developer | FR | Fields compatible linear-optical hardware | [C][G:QUANDELA-LUCY-HPC-2026-04] |
| Sparrow Quantum | research | DK | Published the 2026 subthreshold critique | [S][G:SPARROW-SUBTHRESHOLD-2026-06] |
| DARPA | investor | US | QBI Stage C V&V of PsiQuantum's stack | [G:PSIQ-QBI-C-2026-07] |

**Money.**
2024-04 · PsiQuantum · Australian federal and Queensland commitment · A$940 M · announced [P][G:PSIQ-BRISBANE-940M]
2025-09-10 · PsiQuantum · Series E · USD 1 B at USD 7 B · closed [G:PSIQ-1B-2025-09]
2026-05-21 · PsiQuantum · US CHIPS letter of intent · USD 100 M · non-binding [G:CHIPS-LOI-2026-05]
2026-07-22 · PsiQuantum · DARPA QBI Stage C expansion · USD 125 M · definitive [G:PSIQ-QBI-C-2026-07]

**Market & supply chain.** No product, no market: the asset is a roadmap plus government commitments; the suppliers that matter sit upstream. Pays for G3/G4 alone.

**IP & standards.** No dated patent family specific to the fusion-lattice code as of 4 Sep 2026; nearest is ORCA's US 12,437,225 [G:ORCA-DUALRAIL-PATENT-2025].

**Roadmaps & track record.** (2024-04 · Brisbane machine useful by end-2027 · at risk: site moved, groundbreaking slipped to 2026-06, cryoplant not due until 2H 2027) [P][G:PSIQ-BRISBANE-940M]. Strong paper record, weak schedule.

**Strategic reading.** If the subthreshold critique holds, the largest privately funded photonics bet needs a far lower-loss network or a pivot to emitter hybrids — a redesign for a company already late. Winners if it works: PsiQuantum, its foundry, detector vendors; losers: bosonic GKP and anyone selling a fast gate rather than cheap erasure.

*Open niche:* independently reproducing the 2.7%/17.4% threshold simulations under an open decoder, beside the Sparrow noise models, is a theory audit nobody offers.

## Outlook & open questions
Confirm by 2028: an end-to-end fusion-lattice demonstration at any code distance with measured loss and logical error; demote if only component numbers persist. Best case 2029: a small working lattice. Worst case: it stays a paper and emitter hybrids inherit it. Open: does anyone rebut the 2026 critique; which threshold survives hardware; does Stage C publish a code-level number.

## Sources
[1] Bartolucci, Birchall, Bombín, Cable, Dawson, Gimeno-Segovia, Johnston, Kieling, Nickerson, Pant, Pastawski, Rudolph, Sparrow (PsiQuantum), "Fusion-based quantum computation," Nature Communications 14, 912, 2023-02-16 — https://www.nature.com/articles/s41467-023-36493-1
[2] Loss-tolerant fusion architectures with encoded resource states, arXiv:2506.11975, 2025-06 — https://arxiv.org/abs/2506.11975
[3] PsiQuantum, "A manufacturable, multi-chip photonic architecture for scalable quantum computing" (Omega), Nature 638, 2025-02 — https://www.nature.com/articles/s41586-025-08820-7
[4] Löbl, Pettersson, Dragašević, Chen, Sandberg (Sparrow Quantum), "The subthreshold issue of fusion-based quantum computing," arXiv:2606.28490, 2026-06-26 — https://arxiv.org/abs/2606.28490
[5] Thomas, Ruscio, Morin, Rempe (MPQ Garching), "Fusion of deterministically generated photonic graph states," Nature 629, 2024-05-08 — https://www.nature.com/articles/s41586-024-07357-5
[6] Quantum Computing Report [P], "PsiQuantum secures $125 million expanded agreement with DARPA under QBI program," 2026-07-22 — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/
[7] This report, §3.2 fault-tolerance primitives by platform, 2026-09-03 (main report)
[8] Forbes Australia [P], "PsiQuantum's stalled quantum plant to break ground after location switch," 2026 — https://www.forbes.com.au/news/innovation/psiquantums-stalled-quantum-plant-to-break-ground-after-location-switch/

## Open verification items
Source conflict on the 6-ring loss threshold: the loss-tolerant-architecture paper gives 2.7% per photon for a *boosted* 6-ring [2], while the 2026 Sparrow re-analysis gives 0.38–0.82% (static bias) for an *unencoded* 6-ring [4]. The assumptions differ (boosting, bias model, decoder), so the two are not directly comparable; both are stated here rather than reconciled.
The high threshold appears both as "17.4% ({7,4} encoded)" and as "up to 17% with 168-qubit resource states"; the photon count for the {7,4} encoding was not re-derived from the source.
All thresholds are simulation, never measured, and no independent group has reproduced them.
PsiQuantum has published no response to the 2026-06 subthreshold critique as of 4 Sep 2026, and no 2026 hardware result at all — progress is visible only through DARPA V&V contracting.
