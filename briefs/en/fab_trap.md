---
id: fab_trap
name: Surface-electrode ion-trap microfabrication
layer: "10 Manufacturing"
tier: 2
status: demonstrated
since: 2006
one_line: Planar RF/DC electrode chips that confine and shuttle ions, built on MEMS lines or, increasingly, on merchant semiconductor foundry wafers.
verdict: Falsifiable — if no vendor publishes wafer-level heating or yield data by end-2027, trap fabrication stays craft, and Sol/Apollo schedule risk sits in signal count and packaging, not gate physics.
updated: 2026-09-03
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
A surface-electrode trap flattens the Paul trap into one lithographic plane — electrodes side by side, the ion held tens of micrometres above — so trap geometry becomes mask layout. NIST demonstrated it in 2006, holding ²⁴Mg⁺ about 40 µm above planar gold and measuring the heating rate directly [D][1]. It is the layer beneath the ion carrier: it fixes electrode count, zone and junction geometry, and the surface chemistry above it.
Coordinates: carrier affinity a = 0.0, fully fabricated. Manufacturing g = MEMS lithography moving onto merchant 6–12-inch semiconductor lines [C][7].

## Physics & limits
The floor is anomalous field noise from the electrode surface, not lithographic resolution. Over ion heights of 30–3,000 µm it falls roughly as d⁻⁴ [D][15]: halving the height to pack zones costs ~16× in heating. Heating becomes gate error, since entangling gates ride a shared motional mode for tens to hundreds of microseconds, and forces re-cooling between transport steps. The noise is an adsorbate layer, not a bulk property: cooling gold traps to 6 K suppressed heating ~7 orders of magnitude [D][5]; argon-ion bombardment cut it 100-fold on an already-clean trap [D][6]. The error structure the code sees is coherent and correlated — stray charge on dielectric gaps gives micromotion and phase drift shared across a zone, and one open electrode kills that zone. What moves the floor: niobium electrodes, in-vacuum cleaning, shielded dielectric, cryogenics by default.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2006 | ²⁴Mg⁺ ~40 µm above planar gold; heating first measured | NIST | [D][1] |
| 2012 | 100× field-noise reduction, in-situ argon-ion cleaning | NIST | [D][6] |
| 2025-10 | 2Q error 8.4×10⁻⁵, laser-free, commercial-fab chip | Oxford Ionics | [D][2] |
| 2025-11 | 1,228 electrodes, 273 independent signals, 8 zones | Quantinuum | [D][3] |

Helios's chip is the largest fielded trap; most groups still run bespoke traps of tens to ~100 electrodes. Nobody publishes yield, defect rate or cost per trap, so the layer has no public quality metric, and measured error stays dominated by heating, micromotion and calibration load, not lithographic defects.

## Manufacturing, materials & supply chain
Two lineages. Research MEMS lines (Sandia's MESA complex, GTRI, university cleanrooms) put gold or niobium on sapphire, fused silica or oxidised silicon at one-off volumes [G][11]. The live shift is merchant fabrication: Infineon's Villach platform runs 6–12-inch wafers with anodic bonding for Oxford Ionics, eleQtron [C][9], Innsbruck and ETH Zurich; its Gen-3 out-of-plane electrodes claim ~10× confinement with no heating rate published [C][7]. Honeywell fabricates Quantinuum's traps captively, Sol's grid trap included [R][8]; IonQ closed SkyWater on 2026-07-31 for design, fabrication and packaging on US lines [C][4]. Infineon is the single point of failure: one merchant fab, several vendors, no second source named. Export exposure is mild — the 2024-09-06 BIS rule enumerates quantum computers (4A906) and sub-4.5 K electronics (3A901), but no ECCN names traps [G][17].

## Control, readout & I/O burden
The trap sets the wiring floor before any optical or microwave line exists: 273 independent signals for 98 ions, 2.8 per qubit, for confinement and transport alone [D][3], each a DAC channel, filter and feedthrough. At that ratio 10³ ions needs ~3,000 DC lines, past practical feedthrough counts, and 10⁶ is impossible without switching under the trap. The published escape is on-chip switching: Oxford Ionics' WISE drives 1,000 fully connected ions from ~200 sources, with no chip built and no dissipation budget [S][16].

## Role in the stack
This layer underlies both ion paths — QCCD laser gates (Quantinuum, AQT) and electronic gates with chip control (IonQ/Oxford Ionics, eleQtron, Quantum Art [P][12]) — providing the carrier, the junction and grid geometry, and traces for chip-integrated microwave control. It replaces bespoke MEMS with foundry fabrication, priced in design-rule and UHV qualification and re-measured heating, not physics. Its clock contribution is indirect and large: derived clock = sum of the syndrome round: gate layers + transport + readout + reset, and transport is 9.0 ms of a 9.7 ms ion round — a ~70 µs gate against it, transport near 60% of H2 runtime [D][3] — so zone count and junction quality buy more clock than gate speed. No neighbouring empty slot in the technology graph.

## Verification (QCVV)
Electrode and signal counts are vendor-reported and unaudited. Heating is published per trap at one operating point, never as a wafer or batch distribution, and no vendor discloses yield. The 8.4×10⁻⁵ gate is a two-ion measurement without ground-state cooling, not a fleet average, unreplicated externally as of 4 Sep 2026 [D][2]. No dated dispute between vendors over fabrication claims was found.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IonQ | developer | US | Owns trap design house and a US foundry | [C][4] |
| Oxford Ionics | developer | UK | Electronic-gate trap chips on commercial fab lines | [D][2] |
| Infineon Technologies | supplier | Austria | Merchant trap fab, Villach, 6–12-inch wafers | [C][7] |
| SkyWater Technology | supplier | US | US foundry, eight quantum customers, IonQ-owned | [G][10] |
| Quantinuum | developer | US | Fields the 1,228-electrode trap; Sol in validation | [D][3] |

**Money.**
- 2025-09-17 · IonQ · M&A (Oxford Ionics) · $1.075 B · — · closed [G:IONQ-OXIONICS-2025]
- 2026-07-31 · IonQ · M&A (SkyWater) · ~$1.8 B ($15.00 cash + 0.4883 IonQ shares per share) · — · closed [C][4][G:IONQ-SKYWATER-2026]
- 2025-12-28 · SkyWater · FY2025 revenue · $442.1 M, 19.7% GAAP margin, quantum +30% YoY · filed [G][10]
- 2025-11-06 · DARPA · QBI Stage B (IonQ, Quantinuum of eleven) · ≤$15 M each · announced [G][13][G:QBI-STAGEB-2025-11]

**Market & supply chain.** Enabling equipment is ordinary semiconductor capital plus UHV parts, none concentrated; concentration sits in the fab — Infineon merchant, Honeywell captive, Sandia research-only, plus an IonQ–Sandia co-design MOU on 2026-08-04 [C][14]. Trap unit economics are unpublished; the nearest number is SkyWater's 19.7% gross margin on $442.1 M [G][10]. G3 and G4 pay for this layer, G7 for rack modules.

**IP & standards.** PatSnap's 2026 review names MIT Lincoln Laboratory's chip-integrated voltage-source and photonics families (2016, 2019) and ETH Zurich's cryogenic co-fabricated optics (2020) as core integration IP, with no count isolated to trap fabrication [P][18]. The key wiring architecture is published, not fenced [S][16]; no litigation, no acceptance standard.

**Roadmaps & track record.** Quantinuum: Sol on a Honeywell-fabricated grid trap (promised 2024-09-10 · for 2027 · in validation as of 2026-09-03) [R][8]; Helios shipped on time, so fab-linked credibility is good. IonQ: SkyWater (promised 2026-01-26 · for Q2–Q3 2026 · closed 2026-07-31) [C][4], but 10,000 ions on one chip in 2027 rests on no published 2D-trap heating or yield data, and the 2020 roadmap missed its 2026 count ~40×.

**Strategic reading.** If foundry fabrication works, the differentiator moves off trap craft onto control electronics, packaging and codes. Winners: IonQ, which removes a fab dependency; Quantinuum, already captive-supplied; Infineon, which gains everyone else's volume. Losers: national-lab lines lose their monopoly. The substitution threat is not a rival trap but the clock — fabrication cannot fix a layer time 10³–10⁵× slower than superconducting unless it multiplies zones. Power sits with the fab; IonQ bought one, and carries its ~20% margin.

*Open niche:* Trap fabrication is capital-locked, but its metrology is empty: nobody publishes heating distributions across a wafer, electrode-defect statistics, or a replication of the 8.4×10⁻⁵ gate on a second chip. A batch-level acceptance protocol — heating and micromotion as a wafer-acceptance test reporting a distribution, not a best-die number — needs no fab.

## Outlook & open questions
Confirm or demote by end-2027: does a SkyWater-fabricated trap hold ions in a shipped system; does Sol validate on schedule at 1,200+ electrodes in 2D; does anyone publish a yield or per-wafer heating distribution. Best case 2029: merchant trap wafers with published acceptance data and switching that cuts signals per ion five-fold. Worst case: electrode counts plateau near 10³ because feedthroughs and DAC channels are the wall, and tighter 2D geometry raises heating enough to push Apollo right. Open questions: does a 2D grid keep the linear trap's heating rate; can switching run at 4 K inside a dissipation budget; will Infineon stay merchant.

## Sources
[1] Seidelin, Chiaverini et al. (NIST) · "Microfabricated surface-electrode ion trap for scalable quantum information processing" · arXiv/PRL · 2006-01 · https://arxiv.org/abs/quant-ph/0601173 [D]
[2] Oxford Ionics / IonQ · Two-qubit gate error 8.4×10⁻⁵ with electronic (laser-free) gates · arXiv:2510.17286 · 2025-10 · https://arxiv.org/abs/2510.17286 [D]
[3] Quantinuum · "Helios" system paper (1,228 electrodes, 273 signals, 8 zones) · arXiv:2511.05465 · 2025-11 · https://arxiv.org/abs/2511.05465 [D]
[4] IonQ · "IonQ Completes Acquisition of SkyWater Technology" · company newsroom · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[5] Labaziewicz et al. (MIT) · "Suppression of heating rates in cryogenic surface-electrode ion traps" · Phys. Rev. Lett. 100, 013001 · 2008 · https://arxiv.org/abs/0706.3763 [D]
[6] Hite et al. (NIST) · "100-fold reduction of electric-field noise in an ion trap cleaned with in situ argon-ion-beam bombardment" · Phys. Rev. Lett. 109, 103001 · 2012 · https://arxiv.org/abs/1112.5419 [D]
[7] Infineon Technologies · Trapped-ion QPU platform, Villach (6–12-inch wafers, anodic bonding, Gen-3 out-of-plane electrodes; users eleQtron, Oxford Ionics, Innsbruck, ETH; Quantinuum partnership 2024-11-19) · company page · accessed 2026-09-03 · https://www.infineon.com/promo/trapped-ions [C]
[8] Quantinuum · Accelerated roadmap to fault tolerance (Sol 2027, Apollo 2029) · press release · 2024-09-10 · https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[9] eleQtron · €57 M Series A · company newsroom · 2026-05-05 · https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[10] SkyWater Technology · Q4 and full fiscal year 2025 results (EX-99.1) · SEC EDGAR · 2026-02-26 · https://www.sec.gov/Archives/edgar/data/1819974/000181997426000005/skyt-20251228xex991.htm [G]
[11] Sandia National Laboratories · Sandia–Quantinuum CRADA renewal; MESA photonics for trapped ions · Sandia Lab News · 2026-08-27 · https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/ [G]
[12] Quantum Computing Report · "Quantum Art Extends Series A to $140M" · trade press · 2026-04-27 · https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[13] DARPA · Quantum Benchmarking Initiative Stage B selection · programme page · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[14] IonQ · "IonQ and Sandia National Laboratories Sign MOU to Accelerate Quantum Co-Design" · company newsroom · 2026-08-04 · https://www.ionq.com/news/ionq-and-sandia-national-laboratories-sign-mou-to-accelerate-quantum-co-design-for-national-security-applications [C]
[15] Brownnutt, Kumph, Rabl, Blatt · "Ion-trap measurements of electric-field noise near surfaces" · Rev. Mod. Phys. 87, 1419 · 2015 (arXiv 2014-09-23) · https://arxiv.org/abs/1409.6572 [D]
[16] Malinowski, Allcock, Ballance (Oxford Ionics) · "How to wire a 1000-qubit trapped ion quantum computer" (WISE) · PRX Quantum 4, 040313 · 2023-05-22 · https://arxiv.org/abs/2305.12773 [S]
[17] US Bureau of Industry and Security · "Implementation of Additional Export Controls: Certain Advanced Computing Items; Quantum Computing Items" (ECCN 4A906, 3A901, 3A904, 3B904) · Federal Register · effective 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and [G]
[18] PatSnap Eureka · "Trapped Ion Quantum Computing 2026" patent review · database blog · 2026 · https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]

## Open verification items
- Trap electrode yield, defect rate and cost per trap: not published by IonQ, Quantinuum, Infineon, AQT or eleQtron as of 2026-09-04.
- Whether Infineon fabricated the specific chip behind the 8.4×10⁻⁵ result: neither the Infineon platform page nor the preprint says so; the Oxford Ionics–Infineon link is asserted at company level only.
- No published heating rate for Infineon's Gen-3 out-of-plane electrodes; the ~10× confinement figure is unverified by measurement.
- Independent replication of the 8.4×10⁻⁵ electronic two-qubit gate: none found as of 2026-09-04.
- Whether a bare ion-trap die falls under ECCN 4A906 or outside the enumerated categories: the rule does not name traps and no BIS advisory opinion was found.
