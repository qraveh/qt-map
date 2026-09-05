---
id: g_fusion
name: Linear-optical fusion (heralded)
layer: "3 Gate mechanism"
tier: 3
status: demonstrated
since: 2005
one_line: "Probabilistic Bell-basis measurement on two photons — 50% unboosted, 75% with ancillae — whose failure heralds as erasure; the entangling primitive of fusion-based photonics."
verdict: "Real: single fusions at 99.22% Bell fidelity on chip, 99.72% chip-to-chip (PsiQuantum, 2025-02). Unproven: any chained fusion network with an end-to-end success rate. Demote if no multi-fusion result is published by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A Bell-basis measurement — beamsplitter, phase shifters, number-resolving detectors — projecting two photons onto a Bell state or destroying both and saying so, handing the code erasure rather than Pauli error. Browne and Rudolph introduced type-I/II fusion in 2005 to grow cluster states without a deterministic gate [S][1]; linear optics caps unambiguous discrimination at 50%, unentangled ancillae lift it to 75% [S][2]. Coordinates: flying photons, heralded entangling at ~100 ns; electro-optic room-temperature control, loss-dominated errors, photonic-IC fabrication.

## Physics & limits
The 50%/75% ceiling is information-theoretic: two of four Bell states are indistinguishable to passive linear optics, and routes past 75% buy success with ancilla photons that must themselves survive. The operating figure is success probability × transmission²; loss turns a success into heralded failure at best, an undetected error at worst. The gate is not the problem: 99.22 ± 0.12% on chip, 99.72 ± 0.04% chip-to-chip over 42 m at ~2 K [D][3][G:PSIQ-OMEGA-METRICS-2025]. The floor is the path around it — SiN 1.8 ± 0.2 dB/m, BTO switch 100 mdB, fibre-to-chip 52 mdB, on-chip SNSPD 93.4% median [D][3] — and failure itself: a 2026 re-analysis puts a logical-error floor at zero loss, so all-linear-optics designs need very large distance, while emitter-mediated fusion tolerates 7.0–7.3% [S][5][G:SPARROW-SUBTHRESHOLD-2026-06].

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2005 | Type-I/II fusion, 50% success, proposed | Browne & Rudolph | [S][1] |
| 2014 | 75% Bell measurement with unentangled ancillae | Ewert & van Loock | [S][2] |
| 2025-02 | Bell fidelity 99.22 ± 0.12% on chip; 99.72 ± 0.04% chip-to-chip, 42 m | PsiQuantum | [D][3] |
| 2026-06 | Fusion-failure noise floor at zero loss; 7.0–7.3% threshold | Sparrow | [S][5] |

Every dated fidelity is one fusion measured alone; no chained-fusion success rate is public.

## Manufacturing, materials & supply chain
No fusion-specific materials: the gate reuses the platform stack — SiN waveguides, BTO switches, on-chip SNSPDs on 300 mm silicon at GlobalFoundries [C][G:GF-QTS-2026-05]. Manufacturing decides loss per element, and every element sits inside the attempt: switch 100 mdB, fibre-to-chip 52 mdB [D][3]; best packaged coupling is Xanadu's 0.085 dB/facet [C][G:XANADU-PACKAGING-2026-06]. I/O is channels and latency: 2–4 number-resolving detectors per fusion plus feed-forward within the photon's flight time; Aurora runs 12 modes on a 1 MHz cycle [D][4]. At 10³ fusions/s the constraint is accumulated switch loss; at 10⁴–10⁶, cryogenic channel count and GHz feed-forward, unbuilt. ECCN 4A906 covers the machine, 3A901 sub-4.5 K electronics [G:BIS-QUANTUM-ECCN-2024-09].

## Role in the stack
Requires single photons, single-photon detection for heralding and electro-optic switching for feed-forward; provides the fusion measurements consumed by resource-state generation and fusion-based fault tolerance (PsiQuantum, Quandela, QuiX). It replaces CV Gaussian combination on the Xanadu path — switching changes detectors, encoding and error model together. Clock contribution ~1.0 × 10⁻⁷ s per attempt, divided by success probability and multiplexing depth, so generation, not the gate, dominates the derived clock. Verification: the headline numbers are tomography of one fusion; no protocol reports success-at-depth, and no second group has replicated them.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US | Highest published fusion fidelity, 300 mm line | [D][G:PSIQ-OMEGA-METRICS-2025] |
| Quandela | developer | FR | Fielded linear-optical hardware | [C][G:QUANDELA-LUCY-HPC-2026-04] |
| QuiX Quantum | developer | NL | MBQC hardware at DLR | [C][G:QUIX-SERIESA-2025-07] |
| Sparrow Quantum | research | DK | Threshold case against linear-optics fusion | [S][G:SPARROW-SUBTHRESHOLD-2026-06] |
| DARPA | investor | US | Funds PsiQuantum Stage C, Quandela QBIT | [G:PSIQ-QBI-C-2026-07] |

**Money.**
2025-09-10 · PsiQuantum · Series E · USD 1 B at USD 7 B · BlackRock, Temasek · closed [G:PSIQ-1B-2025-09]
2026-06-16 · Quandela · DARPA QBIT Stage A · undisclosed · announced [G:QBI-QBIT-2026]
2026-07-22 · PsiQuantum · DARPA QBI Stage C expansion · USD 125 M · definitive [G:PSIQ-QBI-C-2026-07]

**Market & supply chain.** No separate market: fusion ships inside a photonic IC, so the foundry and packaging house set its usable success probability. Concentration risk sits with GlobalFoundries; only G3/G4 pay.

**IP & standards.** No dated patent family specific to the fusion gate as of 4 Sep 2026; nearest is ORCA's US 12,437,225 [G:ORCA-DUALRAIL-PATENT-2025].

**Roadmaps & track record.** (2025-02 · Omega component metrics · delivered); (2026-07 · Stage C V&V of switches, packaging, cryogenics · in progress, funding validation not publication). Component credibility good, system-level fusion untested.

**Strategic reading.** Component fidelity is table stakes; the contest is success rate at depth, where the 2026 threshold argument favours emitter-mediated fusion — a challenge to PsiQuantum and QuiX, an opening for quantum-dot vendors. If linear optics holds, foundries capture the value.

*Open niche:* vendor-neutral benchmarking of fusion networks — success at depth, correlated failure, erasure-flag fidelity — is unclaimed and needs no fab.

## Outlook & open questions
Confirm by 2027: a published network of ≥3 chained fusions with end-to-end success rate and erasure statistics; demote if only single-fusion figures exist by 2028. Best case 2029: boosted fusion above 75% on chip. Worst case: the zero-loss failure floor holds and linear-optical fusion survives only inside emitter hybrids. Open: how correlated failures are across a chip; whether 93%-efficient number resolution supports boosting.

## Sources
[1] Browne, Rudolph, "Resource-efficient linear optical quantum computation," Phys. Rev. Lett. 95, 010501, 2005 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.95.010501
[2] Ewert, van Loock, "3/4-efficient Bell measurement with passive linear optics and unentangled ancillae," Phys. Rev. Lett. 113, 140403, arXiv:1403.4841, 2014-03-19 — https://arxiv.org/abs/1403.4841
[3] PsiQuantum, "A manufacturable, multi-chip photonic architecture for scalable quantum computing" (Omega), Nature 638, 2025-02 — https://www.nature.com/articles/s41586-025-08820-7
[4] Xanadu, "Scaling and networking a modular photonic quantum computer" (Aurora), Nature, 2025-01 — https://www.nature.com/articles/s41586-024-08406-9
[5] Löbl, Pettersson, Dragašević, Chen, Sandberg (Sparrow Quantum), "The subthreshold issue of fusion-based quantum computing," arXiv:2606.28490, 2026-06-26 — https://arxiv.org/abs/2606.28490
[6] Quantum Computing Report [P], "PsiQuantum secures $125 million expanded agreement with DARPA under QBI program," 2026-07-22 — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/
[7] The Quantum Insider [P], "Quandela deploys photonic quantum computer integrated with HPC system," 2026-04-14 — https://thequantuminsider.com/2026/04/14/quandela-photonic-quantum-hpc/

## Open verification items
No second group has replicated PsiQuantum's 99.22%/99.72% fusion fidelities as of 4 Sep 2026.
No actor has published multi-fusion (network-scale) success-rate data; no source supports describing Quandela's Lucy as a "fusion-based system" — it is described only as a 12-photonic-qubit machine.
Conflict carried from the main report: PsiQuantum waveguide loss is quoted as 0.5 dB/m in the report excerpt but 1.8 ± 0.2 dB/m for single-mode SiN in the Nature paper; the two remain unreconciled and the paper's figure is used here.
