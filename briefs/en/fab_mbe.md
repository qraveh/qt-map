---
id: fab_mbe
name: III-V MBE heterostructures (InAs–Pb wires, QD sources)
layer: "10 Manufacturing"
tier: 3
status: demonstrated
since: 2018
one_line: Molecular-beam epitaxy of III-V nanostructures with vacuum-unbroken superconductor shells for Majorana wires, and of quantum dots for single-photon sources.
verdict: The process works and is single-source; falsified as a reproducible platform unless a group outside Microsoft publishes an independently grown InAs–Pb device with comparable parity signatures by 2028.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two unrelated devices share a tool class. The first is a III-V nanowire or 2DEG grown by molecular-beam epitaxy with a superconductor deposited in the same vacuum, so the interface is never exposed: aluminium through 2025, lead in the 2026 tetron as the higher-gap shell [D][1]. The second is GaAs-based quantum dots as single-photon sources, same reactors, different physics [G:QBI-QBIT-2026]. The lineage dates to 2018; its founding result, quantized Majorana conductance, was retracted on 2021-03-08 [D][5].
a mostly fabricated (0.75) · b a process, not a clock · c none · d none
e none · f disorder-dominated · g molecular-beam epitaxy

## Physics & limits
The floor is disorder. Unintentional doping, interface roughness and shell strain produce trivial sub-gap Andreev states whose signatures mimic Majorana modes, which is the Nature dispute: Legg argues the regions used for parity readout are disordered and gapless [D][3]. Lead raises the induced gap above aluminium, though no Pb-shell gap value is published [D][1]. Moving the floor means a mean free path well above the coherence length, verified by a published mobility or disorder metric rather than device outcomes; none exists, which is why a materials argument runs through transport data.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018 | Quantized-conductance Majorana claim; retracted 2021-03-08 | Delft (Kouwenhoven et al.) | [D][5] |
| 2025-02 | InAs–Al stack supports 1% parity assignment error | Microsoft Azure Quantum | [D][2] |
| 2026-06 | InAs–Pb stack, higher-gap shell, ~20 s parity switching, one wire | Microsoft Quantum | [D][1] |
No yield, uniformity or disorder figure is published; the only public scaling aid is an rf method resolving wire-end-state splitting to µeV for per-device bring-up [D][1].

## Manufacturing, materials & supply chain
Growth needs a III-V MBE reactor under ultra-high vacuum with in-situ superconductor deposition, keeping the interface clean enough for a hard gap. Microsoft's recipe is in-house, and since 2025-11-13 the full Majorana chip core is fabricated at Lyngby in Denmark [P][G:MSFT-LYNGBY-LAB-2025-11]; nobody outside has grown an equivalent stack, so one recipe in one building is the path's single point of failure [D][3]. An independent III-V base exists for another geometry: Eindhoven-grown InSb wires carry QuTech's Kitaev devices [D][4]. Export exposure is asymmetric: the BIS rule of 2024-09-06 created quantum classifications including 3C907 for epitaxial materials, but none for MBE growth equipment — the wafer is controlled, the reactor is not [P][6].

## Role in the stack
Everything in the topological path stands on this stack: encoding, readout and the unbuilt gate inherit its disorder. It provides no clock and no fidelity, only the ceiling on everyone else's; its one load-bearing fact is negative: no independent replication [D][3]. The same tool class supplies quantum-dot single-photon sources to the photonic path [G:QBI-QBIT-2026]. Verification here is materials verification and does not exist: the Nature exchange of 2026-06-24 disputes transport data from one laboratory's wafers, Microsoft conceding nothing [D][3]; no second laboratory has attempted the Pb shell.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Microsoft Quantum | developer | US | Grows and consumes the InAs–Pb stack; fab in Lyngby | [P][G:MSFT-LYNGBY-LAB-2025-11] |
| DARPA | investor | US | Funds both users: US2QC final stage, QBIT Stage A | [G:MSFT-US2QC-PARTNERS-2025-02] |

**Money.** 2025-02-06 · Microsoft · US2QC enters its final stage · undisclosed · DARPA · announced [G:MSFT-US2QC-PARTNERS-2025-02]. 2025-11-13 · Microsoft · Lyngby (DK) Majorana chip-core fab · >DKK 1 bn national total, Microsoft's outlay undisclosed · announced [P][G:MSFT-LYNGBY-LAB-2025-11]. 2026-06-16 · Quandela · DARPA QBIT Stage A selection · announced [G:QBI-QBIT-2026].

**Market & supply chain.** MBE reactors are a small merchant market, but the tool is not the bottleneck: the recipe is, and it is not for sale. G3/G4 pay for the wires, G6 for the photon sources.

**IP & standards.** No dated patent count specific to this process as of 4 Sep 2026; no standard covers these interfaces.

**Roadmaps & track record.** (three wire generations, 2018 → InAs–Al 2025 → InAs–Pb 2026, promised as the base for fault tolerance by 2029; status 4 Sep 2026: materials delivered, no yield or disorder metric published) [C][7]. Lyngby opened as announced; the retracted 2018 result is why outsiders discount later ones.

**Strategic reading.** While the recipe stays secret every claim above it is unfalsifiable from outside; independent replication either way is worth more than another Microsoft device. Success means a stack nobody can second-source; failure moves value to the InSb base.

*Open niche:* Auditing public transport and spectroscopy data across the wire generations for internal consistency is materials QCVV needing no growth access.

## Outlook & open questions
Falsifiable in 12–24 months: an outside lab publishing an independently grown epitaxial-Pb wire; any published mobility, yield or disorder metric from Microsoft. Confirm on the first; without it the dispute is unresolvable. Best case, an academic group reproduces the stack; worst case, the recipe stays proprietary and the path unauditable to 2029. Open: the Pb-shell induced gap; yield per wafer; whether anyone outside Microsoft attempts the Pb shell.

## Sources
[1] Aghaee et al. (Microsoft Quantum) — "20 Second Parity Lifetime in an InAs–Pb Tetron Device" — arXiv:2606.03884 — 2026-06-02 — https://arxiv.org/abs/2606.03884
[2] Microsoft Azure Quantum — "Interferometric single-shot parity measurement in InAs–Al hybrid devices" — Nature 638, 651–655 — 2025-02-19 — https://www.nature.com/articles/s41586-024-08445-2
[3] Legg — "On the robustness of topological gap detection via transport" — Nature, Matters Arising — 2026-06-24 (Microsoft reply same day) — https://www.nature.com/articles/s41586-026-10567-8
[4] van Loo, Zatelli, Steffensen, Roovers et al. (QuTech/TU Delft, TU Eindhoven, CSIC) — "Single-shot parity readout of a minimal Kitaev chain" — Nature 650 — 2026-02-11 — https://www.nature.com/articles/s41586-025-09927-7
[5] Zhang, Liu, Gazibegovic et al. (Kouwenhoven) — "Quantized Majorana conductance" — Nature 556, 74–79, 2018-03-28; retracted 2021-03-08 (doi 10.1038/s41586-021-03373-x) — https://www.nature.com/articles/nature26142
[6] Arnold & Porter — "Commerce Implements Export Controls on Semiconductor, Additive Manufacturing, and Quantum Computing Items" (on the BIS interim final rule of 2024-09-06) [P] — 2024-09 — https://www.arnoldporter.com/en/perspectives/advisories/2024/09/semiconductor-additive-manufacturing-and-quantum-computing
[7] Microsoft — "Majorana 2: a scalable, error-corrected quantum processor" — Azure Quantum blog [C] — 2026-06 — https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor
[8] DARPA — "Quantum computing approaches" (US2QC) — DARPA news — 2025-02-06 — https://www.darpa.mil/news/2025/quantum-computing-approaches

## Open verification items
No induced-gap value, mobility, disorder or yield metric is published for any generation of the InAs–Al or InAs–Pb stack, so the "higher gap" claim for lead is qualitative. No dated revenue or market-share figure for merchant MBE tool vendors was obtained; the Riber financial-results page returned 404. The exact scope of ECCN 3C907 was read from a legal advisory, not from the Federal Register text, so whether a superconductor–semiconductor hybrid wafer falls inside it is unconfirmed.
