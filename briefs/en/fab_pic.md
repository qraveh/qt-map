---
id: fab_pic
name: Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm)
layer: "10 Manufacturing"
tier: 1
status: demonstrated
since: 2015
one_line: A CMOS foundry flow putting low-loss nitride waveguides, electro-optic switches, single-photon detectors and fibre attach on one 300 mm wafer.
verdict: Demonstrated once, by one line (GlobalFoundries Fab 8 for PsiQuantum, 2025). No wafer-level yield, uniformity or ageing statistic has ever been published; single-source risk defines the layer.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

The photonic IC foundry supplies the optics a photonic quantum computer is made of — SiN waveguides and delay lines, barium-titanate (BTO) or thin-film lithium niobate (TFLN) electro-optic switches, on-die superconducting-nanowire single-photon detectors (SNSPD), cryo-compatible fibre attach — on a 300 mm CMOS line with wafer-scale process control. A photonic qubit is never stored, only transmitted, so the figure of merit is a loss budget in decibels, not a coherence time. Lineage: ultra-low-loss dielectric waveguides (early 2010s, LioniX and UCSB), foundry access from about 2015 (AIM Photonics, imec), the first full quantum stack on 300 mm in 2025 [D][1].

Coordinates: **carrier affinity** fabricated-leaning (0.25), the line hosting no qubit but the modes that carry one; **characteristic time** not applicable, entangling downstream heralded, not deterministic; **readout** none intrinsically, but it supplies the on-chip SNSPDs, whose counting is destructive; **mobility** none — fixed lithography is what buys the photons theirs; **control modality** none, though it supplies the switches; **error structure** loss, seen by the code as heralded erasure; **manufacturing** a photonic-IC process line.

## Physics & limits

Everything converts into one currency. Single-mode SiN routing at 1.8 ± 0.2 dB/m [D][1] costs 34% of the photons per metre of on-chip delay; the wider multimode waveguide in the same process reaches 0.5 dB/m [D][1]. Against an architectural budget near 0.5 dB for a whole fusion path, one BTO switch at 100 mdB spends a fifth of it, a fibre-to-chip transition at 52 ± 12 mdB a tenth, a median on-chip SNSPD at 93.4% efficiency 0.30 dB by itself [D][1]. The dielectric floor is Rayleigh scattering from sidewall roughness, scaling with the mode's overlap with the etched interface, plus N–H absorption near 1520 nm that a 1150 °C anneal drives out. Both are beaten by weakening confinement: the 0.060 dB/m record used a 40 nm-thin core on a 100 mm wafer [D][2], a geometry with millimetre bend radii. That is the trade — loss is bought with area, area with wafers — so a foundry routing waveguide is thirty times lossier than the record and must be. The other failure mode is phase: thermal gradients and stress birefringence detune interferometers, so a line that cannot hold film thickness ships chips needing per-die trimming. Moving the floor needs an electro-optic material whose Pockels coefficient shrinks switches faster than their loss grows — BTO's is an order of magnitude above lithium niobate's, which is why PsiQuantum and DARPA bet on it [P][7].

## Engineering state of the art

Best demonstrated is one wafer run; typical at scale is undefined, because no wafer-level distribution has been published by anyone.

**Records timeline**

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2018-09-24 | TFLN modulator: Vπ 1.4 V at 20 mm, insertion loss < 0.5 dB, 210 Gbit/s | Harvard (Lončar group) | [D][3] |
| 2021-02-10 | SiN loss 0.060 dB/m, intrinsic Q 422 M (100 mm wafer, 40 nm core) | UCSB / Honeywell | [D][2] |
| 2025-02-26 | 300 mm quantum PIC: SiN 1.8 ± 0.2 dB/m single-mode and 0.5 dB/m multimode, splitter 0.5 ± 0.2 mdB, BTO switch 100 mdB, median SNSPD 93.4%, fibre-to-chip 52 ± 12 mdB, fusion Bell 99.22 ± 0.12%, at ~2 K | PsiQuantum + GlobalFoundries | [D][1] |
| 2026-06 | Edge coupling 0.085 dB per facet | Xanadu | [C][4] |

The dominant budget term is not the waveguide but switch insertion loss, facet coupling and detector inefficiency — everything happening where the photon changes medium. The second is invisible: with no yield statistic, nobody can distinguish a process from a good die.

## Manufacturing, materials & supply chain

The demonstrated flow is a 300 mm CMOS line with LPCVD nitride and a high-temperature anneal, BTO as an integrated active layer, SNSPDs patterned in situ, cryo-compatible fibre attach, at ~2 K rather than millikelvin [D][1]. TFLN is made differently — ion-sliced bulk lithium niobate bonded to oxide — which is why HyperLight and Lightium are separate companies rather than modules in that line [P][13]. The merchant market is otherwise 200 mm or smaller: LIGENTEC runs nitride on X-FAB's automotive-qualified 200 mm line and added X-FAB's SOI platform in 2026 [C][12]; LioniX supplies TriPleX modules; imec and AIM Photonics run research lines.

The only public number with a distribution behind it is "median SNSPD efficiency 93.4%" [D][1] — a median implying a spread nobody has shown. No die yield, wafer map or 2 K thermal-cycle ageing data exists, and no foundry publishes quantum MPW or mask-set pricing, so cost per mode is unquotable as of 3 Sep 2026. Single points of failure: one 300 mm line has demonstrated the full stack; BTO deposition tooling is no merchant market; TFLN wafer supply is thin and concentrated; integrated SNSPDs exist at one vendor. Export-control exposure is indirect but real — the BIS interim final rule of 2024-09-06 created ECCNs 3A901 (cryogenic CMOS below 4.5 K), 3A904 (cryocoolers ≥ 600 µW below 0.1 K), 3B904 (cryogenic wafer probing), 3D901/3E901 and 4A906, with License Exception IEC [G][14]. PIC processes and SNSPDs are not named; the cryogenic *test* equipment is.

## Control, readout & I/O burden

The I/O burden is fibre and bias lines. At 52 mdB per facet [D][1] per-channel loss is affordable; the wall is assembly throughput, since 10⁶ modes need of order 10⁵–10⁶ alignment steps. Detection adds a bias line and an amplifier per SNSPD at 2 K, which by 10⁴ channels forces cryogenic readout ASICs — the cryo-CMOS controlled under 3A901 [G][14] and now sold as a GlobalFoundries product line [C][5]. Feed-forward must drive the switch within a delay line's lifetime, at MHz–GHz; the 100 mdB BTO switch at 2 K is both the enabling device and the item DARPA is paying to validate [P][7]. At 10³ modes nothing binds; at 10⁴ fibre attach and channel count bind; at 10⁶ the constraints are wafer-scale integration, the cryoplant, and an unpublished yield.

## Role in the stack

The layer floors two paths: fusion-based photonic computing (PsiQuantum, Quandela, QuiX) and continuous-variable/GKP computing (Xanadu). It provides single photons and squeezed modes, switches for routing and feed-forward, modulators, chip-to-fibre coupling, and the electro-optic chips transducers are built from. Its hub reading matters most: the same 300 mm line delivers integrated laser optics for trapped ions and PIC-generated tweezer optics for neutral atoms, so capital spent here is not modality-specific — the least-correlated bet in the manufacturing layer. It replaces the bulk-optics table, and switching back costs area, alignment drift and any path past a few hundred modes. Derived clock = max(gate, readout, transport) for the path; this layer contributes only transport, roughly 5 ns per metre of on-chip delay, negligible against the 100 ns-class feed-forward the fusion architecture needs [D][1]. Neighbouring empty slots: a merchant 300 mm BTO switch process, a second source for integrated SNSPDs, any published wafer-level acceptance statistic.

## Verification (QCVV)

Loss is measured two incompatible ways. Ring-resonator intrinsic Q gives the 0.060 dB/m record [D][2] — one mode, one geometry, no routing. Spiral cut-back on a production reticle gives 1.8 dB/m [D][1] — the waveguide the machine uses, and the only manufacturing number. Note that the main report's "0.5 dB/m" is the *multimode* figure from the Omega paper while the single-mode routing waveguide in the same paper is 1.8 ± 0.2 dB/m: both must be stated, they are not competing measurements [D][1]. Fusion Bell fidelity, HOM visibility and detector efficiency are component metrics on selected dies, with no protocol converting them into a loss budget an architecture can be scored against, and no ageing data. No second group has reproduced any Omega figure on a second line; the only third-party check is DARPA's Stage C validation of the BTO switches, packaging and cryogenics, whose results are not public [P][7]. Second conflict: the PIXEurope budget is ≈€400 M per imec/ICFO [G][10] and €380 M in trade press [P][11]; trust the consortium release.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| GlobalFoundries | supplier (foundry) | US | Fab 8, Malta NY: the 300 mm line carrying Omega; Quantum Technology Solutions launched 2026-05-21 | [C][5][D][1] |
| PsiQuantum | developer / customer | US, AU | Qualified the SiN + BTO + SNSPD + fibre-attach stack at 2 K | [D][1] |
| imec | research foundry | BE | 300 mm CMOS and photonics, BTO-on-SOI heritage, PIXEurope partner | [D][15][G][10] |
| LIGENTEC | supplier | CH, FR, BE | SiN on X-FAB's 200 mm line; added SOI 2026 | [C][12] |
| LioniX International | supplier | NL | TriPleX SiN waveguides, module assembly | [C][12] |
| HyperLight | supplier | US | TFLN modulators, Harvard spin-off | [P][13] |
| AIM Photonics | research / foundry | US | DoD ManTech institute; PDK and Assembly Design Kit, 2026-05-25 | [C][22] |
| Xanadu | developer | CA | TFLN/SiN CV chips; 0.085 dB/facet packaging; Toronto factory | [C][4][C][9] |
| Quandela | developer | FR | GaAs quantum-dot sources; Lucy delivered to CEA/TGCC | [C][18][G:QBI-QBIT-2026] |
| QuiX Quantum | developer | NL | SiN processors; Carina delivered to DLR, 2026-07 | [C][19] |

**Money.**

- 2024-09 · HyperLight · Series B · $37 M · Summit Partners · closed [P][13]
- 2024-09 · Lightium · seed · $7 M · Vsquared Ventures, Lakestar · closed [P][13]
- 2024-11-24 · PIXEurope · EU pilot line · ≈€400 M · Chips JU, Spain, Catalonia · announced [G][10]
- 2025-09-10 · PsiQuantum · Series E · $1 B at $7 B · BlackRock, Temasek, Baillie Gifford · closed [G:PSIQ-1B-2025-09]
- 2026-03-26 · Xanadu · SPAC with Crane Harbor · ≈$302 M gross · Nasdaq/TSX XNDU · closed [G:XANADU-SPAC-2026-03]
- 2026-05-21 · GlobalFoundries · CHIPS letter of intent · $375 M · US Dept of Commerce · LOI, non-binding [G][6]
- 2026-05-21 · PsiQuantum · CHIPS letter of intent · $100 M · US Dept of Commerce · LOI, non-binding [G][6]
- 2026-07-22 · PsiQuantum · QBI Stage C expansion (BTO switches, packaging, cryogenics) · $125 M · DARPA · definitive [G:PSIQ-QBI-C-2026-07]
- 2026-08-28 · Xanadu · federal funding, Toronto factory · CAD 195 M · Government of Canada · announced [C][9]

**Market & supply chain.** The enabling equipment is ordinary semiconductor capital (LPCVD/PECVD, immersion lithography, CMP, wafer bonding, MBE/PLD) from ASML, Lam, ASM, EVG and SUSS, in a market where quantum is a rounding error: good for cost, bad for influence. Concentration risk sits at the process, not the tool; unit economics are unquotable. G3 and G4 pay for this layer, G6 through fibre links and transducer chips, G7 through 2 K over millikelvin; G1 and G2 only via ion and atom optics, nothing in G5.

**IP & standards.** No dated patent count from a named database was retrieved for the PIC-foundry families; the one photonic family verified for this report is ORCA Computing's US 12,437,225 on linear-optical GHZ measurements, granted 2025-10-07 [G:ORCA-DUALRAIL-PATENT-2025]. There is no cross-foundry PDK standard — every design kit is proprietary and incompatible, the practical reason a customer cannot second-source. AIM Photonics publishes the most open kit [C][22].

**Roadmaps & track record.** PsiQuantum utility scale "before 2033" (promised 2024–25 · for 2033 · Brisbane groundbreaking slipped to 2026-06-17, cryoplant 2H 2027, no 2026 hardware publication) [G:PSIQ-1B-2025-09][P][7]. Xanadu loss 24.1× above threshold → 1.0× in 2030 (promised 2026-08-31 · nothing yet due) [C][9]. PIXEurope pilot line (promised 2024-11 · for 2025 onward · no open-access run reported) [G][10]. GlobalFoundries Quantum Technology Solutions (promised 2026-05-21 · LOI not yet definitive) [C][5][G][6]. GlobalFoundries alone has a record of qualifying a process to production discipline; PsiQuantum has one paper and no second line; the European suppliers deliver at 200 mm, not at the loss-times-scale fault tolerance needs.

**Strategic reading.** If the layer succeeds the winner is the foundry, not the modality: GlobalFoundries collects a per-wafer annuity across five qubit technologies [C][5] while PsiQuantum's differentiation narrows to architecture and cryogenics. If single-mode loss sticks near 1–2 dB/m both paths stall and the value migrates to ion laser delivery, atom tweezers and networking — which is why it is worth funding either way. Substitution: bulk optics below a few hundred modes. Bargaining power sits with the foundry: switching lines means full requalification and a new PDK.

*Open niche:* QCVV here is metrology, not gate benchmarking, and the record is empty exactly where a small independent group is credible: wafer-level loss and uniformity maps, SNSPD efficiency and jitter distributions across a wafer rather than medians, thermal-cycle ageing at 2 K, and an acceptance protocol turning component metrics into an architecture-scored loss budget.

## Outlook & open questions

**Confirm** if by end-2027 any actor publishes a wafer-level yield or uniformity distribution for BTO switches or integrated SNSPDs at 300 mm; if a second line (imec, AIM Photonics, a PIXEurope member) publishes single-mode SiN loss ≤ 1.8 dB/m with monolithic detectors; or if Xanadu's loss factor falls below 10× threshold. **Demote** if PsiQuantum publishes no hardware result beyond Omega by mid-2027, or if the $375 M CHIPS LOI lapses. Best case by 2029: two qualified 300 mm lines, routing below 1 dB/m, switches under 50 mdB, published wafer maps. Worst case: one vendor, one paper, an LOI that never converts.

Open questions. (1) What is the die yield of an integrated SNSPD array on 300 mm, and why has nobody published it? (2) Is BTO manufacturable at volume, or a hero-die material DARPA is paying to find out about? (3) Who second-sources this layer if GlobalFoundries reprioritises?

## Sources

[1] Alexander et al. (PsiQuantum), "A manufacturable platform for photonic quantum computing", Nature, 2025-02-26 — https://www.nature.com/articles/s41586-025-08820-7 [D]
[2] Puckett, Liu, Chauhan, Zhao, Jin, Cheng, Wu, Behunin, Rakich, Nelson, Blumenthal (UCSB/Honeywell), "422 Million intrinsic quality factor planar integrated all-waveguide resonator with sub-MHz linewidth", Nature Communications 12, 934, 2021-02-10 — https://www.nature.com/articles/s41467-021-21205-4 [D]
[3] Wang, Zhang, Chen, Bertrand, Shams-Ansari, Chandrasekhar, Winzer, Lončar (Harvard), "Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages", Nature 562, 101, 2018-09-24 — https://www.nature.com/articles/s41586-018-0551-y [D]
[4] Xanadu, "Xanadu sets new industry benchmark in photonic chip packaging", press release, 2026-06 — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html [C]
[5] GlobalFoundries, "GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing", 2026-05-21 — https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ [C]
[6] US Department of Commerce / NIST, "Department of Commerce announces letters of intent with 9 companies", 2026-05-21 — https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[7] Quantum Computing Report, "PsiQuantum secures $125 million expanded agreement with DARPA under QBI program", 2026-07-22 — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/ [P]
[8] PsiQuantum newsroom (Series E, CEO change, Brisbane) — https://www.psiquantum.com/news-import/psiquantum-1b-fundraise [C]
[9] Xanadu, "Xanadu charts path to over 1,000 logical qubits by 2031", GlobeNewswire, 2026-08-31 — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html [C]
[10] imec, "The European Commission and Chips JU select the PIXEurope consortium to lead the European Pilot Line on Advanced Photonic Integrated Circuits", 2024-11-24 — https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line [G]
[11] PIC Magazine, "EU to establish €380 million pilot line for photonic integrated circuits", 2024 — https://picmagazine.net/article/123220/EU_to_establish_%E2%82%AC380_million_pilot_line_for_photonic_integrated_circuits [P]
[12] LIGENTEC, "About / our story" (X-FAB 200 mm partnership 2020, SOI platform 2026), accessed 2026-09-03 — https://www.ligentec.com/about-our-story/ [C]
[13] optics.org, "Lithium niobate in vogue as thin-film developers raise cash" (HyperLight $37 M Series B; Lightium $7 M seed), 2024-09 — https://optics.org/news/lithium-niobate-in-vogue-as-thin-film-developers-raise-cash [P]
[14] BIS, "Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies", interim final rule, Federal Register, 2024-09-06 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]; ECCN summary: Morgan Lewis, 2024-09 — https://www.morganlewis.com/pubs/2024/09/us-expands-controls-on-quantum-semiconductor-tech-to-secure-industry-leadership [P]
[15] Nickl, Dumoulin Stuyck, Steinacker et al. (imec/Diraq), 300 mm foundry qubit devices, Nature, 2025-09-24 — https://www.nature.com/articles/s41586-025-09531-9 [D]
[16] Quandela newsroom (NVIDIA NVQLink integration 2026-06-23; executive appointments 2026-05-29), accessed 2026-09-03 — https://www.quandela.com/about-us/newsroom/ [C]
[17] DARPA, Quantum Benchmarking Initiative Stage B selection, 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[18] Quandela, "Quandela delivers Lucy to EuroHPC and GENCI at CEA's TGCC", 2025-10 — https://www.quandela.com/about-us/newsroom/quandela-delivers-lucy-the-most-advanced-photonic-quantum-computer-worldwide-to-eurohpc-and-genci-at-ceas-tgcc/ [C]
[19] QuiX Quantum, "QuiX Quantum delivers Carina core hardware platform to DLR QCI", 2026-07 — https://www.quixquantum.com/news/quix-quantum-delivers-carina-core-hardware-platformto-dlr-qci [C]
[20] Quantum Computing Report, "Photonic Inc. reaches $2 B valuation with $200 M final close", 2026-05-12 — https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ [P]
[21] Bartolucci et al., "Fusion-based quantum computation", Nature Communications 14, 912, 2023 — https://www.nature.com/articles/s41467-023-36493-1 [S]
[22] AIM Photonics newsroom (Assembly Design Kit 2026-05-25; DoD ManTech recognition 2026-02-05), accessed 2026-09-03 — https://www.aimphotonics.com/news [C]

## Open verification items

- LioniX International: no dated 2025–2026 funding, capacity or loss figure retrieved; its row rests on platform description only.
- SNSPD state of the art off-chip (the ~98% system-detection-efficiency result at 1550 nm): the Optica page failed to load; unverified, so no record row was claimed.
- TFLN wafer supply concentration (the widely cited dominance of a single Chinese ion-slicing supplier): no source retrieved; stated qualitatively only.
- PIXEurope budget conflict: ≈€400 M [G][10] versus €380 M [P][11]; consortium release preferred.
- AIM Photonics: founding federal award amount and the wafer diameter of its Albany line are not on the page consulted; not stated.
- Quantum MPW and mask-set pricing at 300 mm: not disclosed by any foundry; cost per mode unquotable.
- Waveguide loss double figure: the main report quotes 0.5 dB/m (multimode) only; the single-mode routing value in the same paper is 1.8 ± 0.2 dB/m. Both stated here — a conflict between excerpts, not between sources.
- Wafer-level yield, uniformity and 2 K thermal-cycle ageing for BTO switches and integrated SNSPDs: no public data from any actor.
