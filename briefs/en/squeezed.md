---
id: squeezed
name: Squeezed light mode (CV)
layer: "1 Carrier"
status: demonstrated
since: 2012
one_line: "A continuous-variable optical mode with one quadrature below vacuum noise; the carrier for GKP and cluster-state photonics, where integration loss, not nonlinearity, sets the ceiling."
verdict: "Real: 1.4 dB directly measured on TFLN, 15 dB in bulk optics. Unproven: GKP effective squeezing beyond 0.62 dB on chip against ~9.75 dB needed. Demote if no on-chip GKP figure above 2 dB by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An optical mode whose vacuum fluctuations are redistributed between conjugate quadratures by parametric down-conversion in a χ⁽²⁾ medium: one quadrature drops below vacuum noise, the other rises. Predicted in the 1970s, first observed in 1985; the lineage that matters is waveguide squeezers feeding CV cluster states and GKP encoding. Coordinates: flying carrier, heralded generation at ~1 µs; readout by single-photon detection at ~10 ns, destructive, not mid-circuit; electro-optic room-temperature control, Gaussian-plus-loss errors, photonic-IC fabrication.

## Physics & limits
Squeezing is a loss thermometer: the medium can produce arbitrarily strong quadrature reduction, but every dB of loss between generation and detection pulls the measured value toward vacuum, so the number describes the optical path, not the squeezer. Hence 15 dB in bulk optics [D][2] against 1.4 dB measured on chip, over 10 dB once a 4 dB homodyne loss budget is subtracted [D][5]. Do not conflate raw quadrature squeezing with the *effective* squeezing of a GKP grid state, which folds in non-Gaussian preparation fidelity as well as loss: fault tolerance prices the latter at ~9.75 dB against 0.62 dB on chip [D][1]. Only lower loss, better coupling and higher detection efficiency move it.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2016 | 15 dB squeezing, bulk optics | Vahlbruch et al., Hannover | [D][2] |
| 2025-06 | On-chip GKP effective squeezing 0.62 dB vs ~9.75 dB required | Xanadu | [D][1] |
| 2025-08 | 1.4 dB measured on poled TFLN, >10 dB inferred at 62 mW pump | Shi et al. | [D][5] |
| 2026-08 | Loss 24.1× above threshold, 1.0× targeted 2030 | Xanadu | [R][3][G:XANADU-SPAC-2026-03] |

The on-chip-to-bulk gap is ~13 dB, the GKP gap ~9 dB.

## Manufacturing, materials & supply chain
Squeezers ride the CV photonic-IC line — SiN and thin-film lithium niobate with periodic poling. Merchant TFLN supply is thin: HyperLight (USD 37 M Series B, 2024-09) and Lightium (USD 7 M seed) [P][G:TFLN-FUNDING-2024-09], plus the PIXEurope pilot line [G:PIXEUROPE-2024-11]. Xanadu builds rather than buys; no cost per squeezer is public. Poling uniformity and waveguide loss are the yield-limiting defects, both acting on the headline dB. I/O is one pump and one homodyne chain per mode plus phase locking; Aurora ran 35 chips at 12 modes on a 1 MHz cycle [D][4]. At 10³ modes the wall is pump distribution and phase stability; at 10⁴–10⁶, detector and DAC channel count. No ECCN names squeezers; 4A906 catches the machine [G:BIS-QUANTUM-ECCN-2024-09].

## Role in the stack
Requires a photonic-IC foundry; provides the modes for CV Gaussian gates with GKP-assisted non-Gaussian operations and for GKP grid encoding on Xanadu's path. It replaces discrete photons as carrier — DV trades erasure-dominated errors for Gaussian-plus-loss ones, and switching costs the whole detector chain. Squeezing level sets the error floor of every CV operation, bounding the derived clock indirectly rather than contributing a gate time. Verification: 0.62 dB is single-source and unreplicated; the independent TFLN result measures raw squeezing, and its ">10 dB" is inferred by subtracting detection loss [D][5].

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Xanadu | developer | CA | Only actor fielding on-chip CV/GKP systems | [D][1] |
| HyperLight, Lightium | supplier | US, CH | TFLN chips and foundry service | [P][G:TFLN-FUNDING-2024-09] |
| DARPA | investor | US | QBI Stage B, up to USD 15 M | [G:QBI-STAGEB-2025-11] |
| Government of Canada | investor | CA | CAD 195 M, Toronto factory | [G:XANADU-LIQUIDITY-2026-06] |

**Money.**
2025-11-06 · Xanadu · DARPA QBI Stage B · up to USD 15 M · announced [G:QBI-STAGEB-2025-11]
2026-03-26 · Xanadu · SPAC with Crane Harbor · ~USD 302 M gross, ~40% below plan · closed [C][G:XANADU-SPAC-2026-03]
2026-08-28 · Xanadu · Canadian factory funding · CAD 195 M · confirmed [G:XANADU-LIQUIDITY-2026-06]

**Market & supply chain.** No merchant squeezer exists; upstream the tradable goods are TFLN wafers and poling from two small vendors — concentration risk for anyone not vertically integrated. Only G3/G4 pay for squeezing quality.

**IP & standards.** No dated patent family specific to on-chip squeezers as of 4 Sep 2026, and no standard defines how effective squeezing is reported.

**Roadmaps & track record.** (2026-08-31 · loss 24.1× → 1.0× by 2030 · not due); (2026-08-31 · 200 logical qubits by 2029 · not due). Good disclosure record, but every squeezing promise is forward-dated.

**Strategic reading.** Squeezing quality, not mode count, gates the CV bet: if the on-chip GKP figure does not move, the 2030 target fails and CV loses to DV fusion, having no alternative carrier. If it moves, TFLN and poling suppliers become strategic.

*Open niche:* a standardised homodyne benchmark for effective squeezing, raw and loss-corrected reported apart, is a clean QCVV product.

## Outlook & open questions
Confirm by 2028: on-chip GKP effective squeezing above 2 dB with its loss budget; demote if still below 1 dB. Best case 2029: a second group publishes a competing GKP figure. Worst case: integration loss pins it near 1 dB and CV/GKP stays a research path. Open: does loss fall as the roadmap claims; can poled TFLN reach GKP-grade fidelity.

## Sources
[1] Xanadu, "Generation of a squeezed GKP state on an integrated photonic chip," Nature, 2025-06 — https://www.nature.com/articles/s41586-025-09044-5
[2] Vahlbruch, Mehmet, Danzmann, Schnabel, "Detection of 15 dB squeezed states of light," Phys. Rev. Lett. 117, 110801, 2016 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.117.110801
[3] Xanadu, "Xanadu charts path to over 1,000 logical qubits by 2031," GlobeNewswire [C], 2026-08-31 — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html
[4] Xanadu, "Scaling and networking a modular photonic quantum computer" (Aurora), Nature, 2025-01 — https://www.nature.com/articles/s41586-024-08406-9
[5] Shi, Baiju, Chen, Mohanraj, Wang, Dhyani, Shajilal, Zhao, Yang, Li, Wu, Hao, Leong, Lam, Zhu, "Squeezed light generation in periodically poled thin-film lithium niobate waveguides," Nanophotonics / arXiv:2508.08599, 2025-08-12 (v2 2025-10-29) — https://arxiv.org/abs/2508.08599
[6] optics.org [P], "Lithium niobate in vogue as thin-film developers raise cash," 2024-09 — https://optics.org/news/lithium-niobate-in-vogue-as-thin-film-developers-raise-cash
[7] imec / European Commission, PIXEurope pilot-line selection, 2024-11-24 — https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line

## Open verification items
An independent on-chip squeezing number does exist: Shi et al. report 1.4 dB measured on PPLN TFLN [5]. What remains single-source is the *GKP effective* squeezing of 0.62 dB (Xanadu only).
The ">10 dB" TFLN figure is loss-corrected, not measured, and is stated at one pump power; it is not comparable with the 15 dB bulk-optics measurement.
The ~9.75 dB fault-tolerance requirement comes from the graph record's fact-checked entry; the main report rounds it to ~10 dB. No conflict of substance, but no single primary source could be consulted directly (nature.com returned 502 on 4 Sep 2026).
The "since 2012" front-matter year comes from the graph record and is not anchored to a specific paper.
Xanadu's CAD 195 M and USD 686 M figures both come from the 2026-08-31 release, not an audited filing.
