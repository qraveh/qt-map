---
id: src_resource
name: Multi-photon resource-state factory (6-ring etc.)
layer: "3 Gate mechanism"
status: empty slot
since: 2030
one_line: "The source-plus-fusion subsystem that must mass-produce encoded multi-photon graph states at code rate to feed fusion-based fault tolerance; nothing runs near that rate."
verdict: "Real: 8 photons fused into 6-rings and 7-trees at 0.4–2.3 coincidences/minute. Unproven: any generator within nine orders of magnitude of the needed rate. Demote if no fused state above 16 photons by 2029."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The source-plus-fusion subsystem that must manufacture, at code rate, the encoded graph states — canonically the 6-ring — that fusion-based fault tolerance consumes and destroys. Browne–Rudolph type-II fusion (2005) made it possible; Bartolucci et al. fixed the 6-ring as reference resource and set its loss budget [S][3]. Best instance: MPQ Garching fused deterministically emitted photons into 6-rings and 7-trees, 8 photons, 0.4–2.3 coincidences/minute [D][1]. Coordinates: flying photons from fabricated emitters, heralded entangling, no fixed clock; electro-optic room-temperature control, pure-loss errors, photonic-IC fabrication.

## Physics & limits
An n-photon graph from k-photon primitives costs ~n/k fusions, each 50% unboosted or 75% boosted; failure heralds as erasure, but every attempt burns a photon that must be indistinguishable and lossless. Yield is brightness × indistinguishability × fusion success × transmission over the whole state — the exponent is photon count, not depth. Hence the code's tolerance: 2.7% loss per photon with 6-rings, ~17% only with 168-photon states nobody can build [S][3][4]. A 2026 re-analysis sharpens this: fusion failure alone sets a logical-error floor at zero loss, forcing very large distance for 10⁻¹⁰, while emitter-mediated fusion raises the threshold to 7.0–7.3% against an unencoded 6-ring's 0.38–0.82% [S][2][G:SPARROW-SUBTHRESHOLD-2026-06].

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2024-05 | 8 photons fused into 6-ring/7-tree graphs, 0.4–2.3/min, fidelity 0.34–0.85 | MPQ | [D][1] |
| 2025-02 | Fusion Bell fidelity 99.22% (component only) | PsiQuantum | [D][5][G:PSIQ-OMEGA-METRICS-2025] |
| 2025-05 | Reconfigurable 4-photon graph states, one QD, ~0.5 Hz | C2N Paris-Saclay | [D][6] |
| 2026-06 | Emitter-fusion loss threshold 7.0–7.3% vs 0.38–0.82% | Sparrow | [S][2] |

Rate is the gap: components clear 99%, but nobody has fused past eight photons since 2024.

## Manufacturing, materials & supply chain
No factory product exists; the nearest base is 300 mm photonic IC — GlobalFoundries' Quantum Technology Solutions [C][G:GF-QTS-2026-05] and PIXEurope [G:PIXEUROPE-2024-11]. Deterministic sources are the single point of failure: Sparrow Quantum, sole merchant vendor as of 4 Sep 2026, ships 20–35% system efficiency against its own 55.3% best device and USTC's 71.2% record [D][G:SPARROW-SERIESA-2025-04]; no cost or yield per state is public. I/O scales with photon count, not qubit count: a pump, switch tree and detectors per source, feed-forward within the photon's flight time per fusion — ~0.1–0.2 dB per switch against a ~0.5 dB budget at multiplexing depth ~10 [D][5]. At 10³ states/s the wall is switch loss; at 10⁶, thousands of cryogenic detector channels under GHz feed-forward. ECCN 4A906 catches the machine; none names photon sources [G:BIS-QUANTUM-ECCN-2024-09].

## Role in the stack
In the photonic fusion-based path (PsiQuantum, Quandela, QuiX): requires linear-optical fusion and single photons, provides the only input fusion-based fault tolerance accepts. It sets the path's clock — with no syndrome round on a fusion path, sum of the syndrome round: gate layers + transport + readout + reset gives way to generation at ~0.4–2.3 min⁻¹ [D][1] against the ~10⁹ s⁻¹ a teraquop machine needs; the 24–168-photon slot next door is empty. Verification: the record is coincidence-counted tomography with fidelity 0.34–0.85 by graph type, unreplicated; nearest independent work is 4-photon states [D][6]. Every threshold quoted is simulation.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US | In-house fusion and generation | [D][G:PSIQ-OMEGA-METRICS-2025] |
| Quandela | developer | FR | QD sources; Lucy on Joliot-Curie | [C][G:QUANDELA-LUCY-HPC-2026-04] |
| Sparrow Quantum | supplier | DK | Sole merchant source vendor | [D][G:SPARROW-SERIESA-2025-04] |
| MPQ Garching | research | DE | Holds the 8-photon record | [D][1] |

**Money.**
2025-04-10 · Sparrow Quantum · Series A · EUR 21.5 M · lead undisclosed · closed [P][G:SPARROW-SERIESA-2025-04]
2025-09 · PsiQuantum · Series E · USD 1 B at USD 7 B · closed [P][G:PSIQ-1B-2025-09]
2026-07-22 · PsiQuantum · DARPA QBI Stage C expansion · USD 125 M · definitive [G:PSIQ-QBI-C-2026-07]

**Market & supply chain.** No merchant product; money goes to the inputs — source chips (Sparrow, a chokepoint) and fusion-capable PICs. Unit economics unquotable; only G3/G4 pay.

**IP & standards.** No dated patent family specific to resource-state generation as of 4 Sep 2026; the adjacent grant is ORCA's US 12,437,225 [G:ORCA-DUALRAIL-PATENT-2025]. No throughput standard exists.

**Roadmaps & track record.** (2025-07 · QuiX error-corrected generation 2027 · pending); (2025 · Quandela first logical qubit · missed; QBIT Stage A entered 2026-06-16 [G:QBI-QBIT-2026]). No dated rate milestone exists.

**Strategic reading.** Generation rate, not fidelity, decides fusion photonics; a source vendor that also owns fusion gains leverage over integrators building sources in-house. If it fails, the path loses to CV/GKP and to matter qubits.

*Open niche:* independent throughput-and-fidelity benchmarking of graph-state fusion is an unclaimed QCVV niche.

## Outlook & open questions
Confirm by 2028: a fused state above 16 photons published with fidelity and rate; demote if still single digits. Best case 2029: merchant emitters plus on-chip fusion reach ≥10³ states/s. Worst case: the subthreshold floor holds and all-linear-optics 6-rings are abandoned. Open: can multiplexed sources beat emitters per useful state; does Sparrow close its 20–35%-to-55% gap. Watch: any rate figure in DARPA Stage C V&V.

## Sources
[1] Thomas, Ruscio, Morin, Rempe (MPQ Garching), "Fusion of deterministically generated photonic graph states," Nature 629, 2024-05-08 — https://www.nature.com/articles/s41586-024-07357-5
[2] Löbl, Pettersson, Dragašević, Chen, Sandberg (Sparrow Quantum / Center for Hybrid Quantum Networks), "The subthreshold issue of fusion-based quantum computing," arXiv:2606.28490, 2026-06-26 — https://arxiv.org/abs/2606.28490
[3] Bartolucci et al. (PsiQuantum), "Fusion-based quantum computation," Nature Communications 14, 2023-02-16 — https://www.nature.com/articles/s41467-023-36493-1
[4] Loss-tolerant fusion architectures with large encoded resource states, arXiv:2506.11975, 2025-06 — https://arxiv.org/abs/2506.11975
[5] PsiQuantum, "A manufacturable, multi-chip photonic architecture for scalable quantum computing" (Omega), Nature 638, 2025-02 — https://www.nature.com/articles/s41586-025-08820-7
[6] Coste, Senellart et al. (C2N Paris-Saclay), "Deterministic and reconfigurable graph state generation with a single solid-state quantum emitter," Nature Communications, 2025-05-09 — https://www.nature.com/articles/s41467-025-59693-3
[7] The Quantum Insider [P], "Quandela deploys photonic quantum computer integrated with HPC system," 2026-04-14 — https://thequantuminsider.com/2026/04/14/quandela-photonic-quantum-hpc/
[8] Quantum Computing Report [P], "Sparrow Quantum secures €21.5M ($24M USD) in Series A funding," 2025-04-10 — https://quantumcomputingreport.com/sparrow-quantum-secures-e21-5m-24m-usd-in-series-a-funding-to-advance-photonic-quantum-chip-production/

## Open verification items
Fidelity of the 8-photon fused states spans 0.34–0.85 by graph type with no reconciled headline value — treat as a range, not a point estimate.
Conflict: Quandela's 12-qubit Belenos/Lucy delivery to CEA is dated 2025-10, while the Lucy/Joliot-Curie HPC launch is dated 2026-04-14; both may be true (delivery then integration) but no single source reconciles them — 2026-04 is used here.
arXiv:2506.11975 (17% loss tolerance with 168-photon resource states) is cited as reported in the main report; author list unverified.
No independent group has replicated or exceeded the 2024 MPQ 8-photon record as of 4 Sep 2026.
