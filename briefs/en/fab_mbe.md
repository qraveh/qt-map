---
id: fab_mbe
name: III-V MBE heterostructures (InAs–Pb wires, QD sources)
layer: "10 Manufacturing"
status: demonstrated
since: 2015
one_line: Molecular beam epitaxy of III-V nanostructures with vacuum-unbroken superconductor shells for Majorana wires, and of quantum dots for single-photon sources.
verdict: The process works and is single-source; falsified as a reproducible platform unless a group outside Microsoft publishes an independently grown InAs–Pb device with comparable parity signatures by 2028.
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two unrelated devices share a tool class. The first is a III-V nanowire or 2DEG (two-dimensional electron gas) grown by molecular beam epitaxy (MBE) with a superconductor deposited in the same vacuum, so the interface is never exposed: aluminium through 2025, lead in the 2026 tetron as the higher-gap shell [D][21]. The second is GaAs-based quantum dots as single-photon sources, same reactors, different physics [G:QBI-QBIT-2026]. The lineage dates to 2015, when Copenhagen grew aluminium epitaxially on InAs nanowires without breaking vacuum [D][G:KROGSTRUP-EPI-2015]; the field's 2018 headline, quantised Majorana conductance in InSb–Al wires, was retracted on 2021-03-08 [D][365].
a mostly fabricated (0.75) · b a process, not a clock · c none · d none
e none · f disorder-dominated · g molecular beam epitaxy

## Physics & limits
The floor is disorder. Unintentional doping, interface roughness and shell strain produce trivial sub-gap Andreev states whose signatures mimic Majorana zero modes (MZMs), which is the Nature dispute: Legg argues the regions used for parity readout are disordered and gapless [D][22]. Lead raises the gaps above aluminium's: in Microsoft's tetron stack the lead film's own gap is ≈1.3 meV and the gap it induces in the wire ≈570 µeV, against 295 µeV and 129 µeV with aluminium, while the topological gap, taken at the top quintile of its measured values, only doubles, from ~30 to ~70 µeV [D][21], [G:MSFT-TGP-PRB-2023]; epitaxial Pb on InAs nanowires holds a hard 1.25 meV gap to 8.5 T (Copenhagen, 2021) [D][G:KANNE-PB-INAS-2021]. Moving the floor means a mean free path well above the coherence length, verified by a published mobility or disorder metric rather than device outcomes. Microsoft published such metrics for InAs–Al — mobility 60,000–100,000 cm²/V·s, a charged-defect density of 2.7 × 10¹² cm⁻² [D][G:MSFT-TGP-PRB-2023] — and for the Pb stack only Hall-bar values of its active region, a surface charge density of ≈2 × 10¹² cm⁻² and a buried-well mobility above 350,000 cm²/V·s [D][21]; none is measured on a device, which is why the materials argument runs through transport data.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018 | Quantised-conductance Majorana claim in InSb–Al wires; retracted 2021-03-08 | Delft (Kouwenhoven et al.) | [D][365] |
| 2025-02 | InAs–Al stack supports 1% parity assignment error | Microsoft Azure Quantum | [D][13] |
| 2026-06 | InAs–Pb stack, higher-gap shell, ~20 s parity switching, one wire | Microsoft Quantum | [D][21] |

No yield or uniformity figure is published for either stack, and the Pb one's disorder figures come from Hall bars, not devices; the only public scaling aid is an rf method resolving wire-end-state splitting to µeV for per-device bring-up [D][21].

## Manufacturing, materials & supply chain
Growth needs a III-V MBE reactor under ultra-high vacuum with in-situ superconductor deposition, keeping the interface clean enough for a hard gap. Microsoft's recipe is in-house, and since 2025-11-13 the full Majorana chip core is fabricated at Lyngby in Denmark [P][G:MSFT-LYNGBY-LAB-2025-11]; nobody outside has grown an equivalent stack, so one recipe in one building is the architecture's single point of failure [D][22]. An independent III-V base exists for another geometry: Eindhoven-grown InSb wires carry QuTech's Kitaev devices [D][216]. Export exposure predates the quantum rules: MBE growth equipment has long been on the Wassenaar dual-use list (US Export Control Classification Number 3B001.a.3), and a III-V hetero-epitaxial wafer falls, if anywhere, under 3C001.d [G:MBE-EXPORT-CONTROL-2024-09]; the BIS rule of 2024-09-06 added 3C907 only for epitaxial layers of isotopically enriched silicon or germanium, which leaves an InAs–Pb stack outside it [G][301][P][818].

## Role in the stack
Everything in the topological architecture stands on this stack: encoding, readout and the unbuilt gate inherit its disorder. It provides no clock and no fidelity, only the ceiling on everyone else's; its one load-bearing fact is negative: no independent replication [D][22]. The same tool class supplies quantum-dot single-photon sources to the fusion-based photonic architecture [G:QBI-QBIT-2026]. The register lists {{N_T_FAB_MBE_MACHINES_W}} machines using it, among them Lucy, Belenos, Majorana 1 and Majorana 2. Verification here is materials verification and does not exist: the Nature exchange of 2026-06-24 disputes transport data from one laboratory's wafers, Microsoft conceding nothing [D][22]; no second laboratory has grown the planar Pb stack, though Copenhagen put epitaxial Pb on InAs nanowires in 2021 [D][G:KANNE-PB-INAS-2021].

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Microsoft Quantum | developer | US | Grows and consumes the InAs–Pb stack; fab in Lyngby | [P][G:MSFT-LYNGBY-LAB-2025-11] |
| DARPA | investor | US | Funds both users: US2QC final stage, QBIT Stage A | [G:MSFT-US2QC-PARTNERS-2025-02] |

**Money.** 2025-02-06 · Microsoft · US2QC enters its final stage · undisclosed · DARPA · announced [G:MSFT-US2QC-PARTNERS-2025-02]. 2025-11-13 · Microsoft · Lyngby (DK) Majorana chip-core fab · >DKK 1 bn national total, Microsoft's outlay undisclosed · announced [P][G:MSFT-LYNGBY-LAB-2025-11]. 2026-06-16 · Quandela · DARPA QBIT Stage A selection · announced [G:QBI-QBIT-2026].

**Market & supply chain.** MBE reactors are a small merchant market, but the tool is not the bottleneck: the recipe is, and it is not for sale. G3/G4 pay for the wires, G6 for the photon sources.

**IP & standards.** No dated patent count specific to this process as of 4 Sep 2026; no standard covers these interfaces.

**Roadmaps & track record.** (three wire generations, InSb–Al 2018 → InAs–Al 2025 → InAs–Pb 2026, promised as the base for fault tolerance by 2029; status 4 Sep 2026: materials delivered, no yield metric published) [C][215]. Lyngby opened as announced; the retracted 2018 result is why outsiders discount later ones.

**Strategic reading.** While the recipe stays secret every claim above it is unfalsifiable from outside; independent replication either way is worth more than another Microsoft device. Success means a stack nobody can second-source; failure moves value to the InSb base.

## Outlook & open questions
Falsifiable in 12–24 months: an outside lab publishing an independently grown planar InAs–Pb device with parity readout; a published yield, or a disorder metric measured on Microsoft's Pb devices rather than Hall bars. Confirm on the first; without it the dispute is unresolvable. Best case, an academic group reproduces the stack; worst case, the recipe stays proprietary and the architecture unauditable to 2029. Open: the spread of topological gaps behind the top-quintile ~70 µeV; yield per wafer; whether anyone outside Microsoft grows the planar Pb stack.

## References
[13] Microsoft Azure Quantum, “Interferometric single-shot parity measurement in InAs–Al hybrid devices,” *Nature*, vol. 638, no. 8051, pp. 651–655, Feb. 2025, doi: [10.1038/s41586-024-08445-2](https://doi.org/10.1038/s41586-024-08445-2). [D]
[21] M. Aghaee *et al.*, “20 Second Parity Lifetime in an InAs–Pb Tetron Device,” [arXiv:2606.03884](https://arxiv.org/abs/2606.03884), Jun. 2026. [D]
[22] H. F. Legg, “On the robustness of topological gap detection via transport,” *Nature*, vol. 654, no. 8120, pp. E22–E26, Jun. 2026, doi: [10.1038/s41586-026-10567-8](https://doi.org/10.1038/s41586-026-10567-8). [arXiv:2503.08944](https://arxiv.org/abs/2503.08944). [D]
[215] C. Nayak, “Majorana 2 – Microsoft's Scalable Quantum Processor With Reliable, Long-Lasting Qubits,” Microsoft Quantum. [Online]. Available: https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor [C]
[216] N. van Loo *et al.*, “Single-shot parity readout of a minimal Kitaev chain,” *Nature*, vol. 650, no. 8101, pp. 334–339, Feb. 2026, doi: [10.1038/s41586-025-09927-7](https://doi.org/10.1038/s41586-025-09927-7). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[365] H. Zhang *et al.*, “Quantized Majorana conductance,” *Nature*, vol. 556, no. 7699, pp. 74–79, Mar. 2018, doi: [10.1038/nature26142](https://doi.org/10.1038/nature26142). Retracted: *Nature*, vol. 591, p. E30, Mar. 2021, doi: [10.1038/s41586-021-03373-x](https://doi.org/10.1038/s41586-021-03373-x). [D]
[818] J. P. Barker *et al.*, “Commerce Implements Export Controls on Semiconductor, Additive Manufacturing, and Quantum Computing Items,” Arnold & Porter, Sep. 10, 2024. [Online]. Available: https://www.arnoldporter.com/en/perspectives/advisories/2024/09/semiconductor-additive-manufacturing-and-quantum-computing [P]

## Open verification items
For InAs–Al, Microsoft published an induced gap of 129 µeV, topological gaps of 20–60 µeV, a mobility and a charged-defect density (Physical Review B, 2023) [G:MSFT-TGP-PRB-2023], from a gap protocol whose reading Legg disputes [D][22]; for the InAs–Pb stack the tetron paper gives the lead film's gap (≈1.3 meV), the induced gap (≈570 µeV), a top-quintile topological gap (~70 µeV) and Hall-bar charge density and mobility [21], but no yield metric. No dated revenue or market-share figure for merchant MBE tool vendors was obtained; the Riber financial-results page returned 404. ECCN scope is now read from the regulation itself: 3C907 covers only silicon or germanium with an isotopic impurity below 0.08% [G][301]; whether a given III-V stack falls under 3C001.d depends on its layers and doping, and no BIS ruling was found.
