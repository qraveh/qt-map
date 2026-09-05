---
id: g_cv
name: CV Gaussian gates + GKP-assisted non-Gaussian ops
layer: "3 Gate mechanism"
tier: 3
status: demonstrated
since: 2020
one_line: "Beam-splitters, squeezers and homodyne feed-forward on optical modes, with GKP grid states supplying the non-Gaussian resource fault tolerance requires."
verdict: "On-chip GKP effective squeezing is 0.62 dB against the ~10 dB the architecture needs — an ~8.7× grid-noise-variance gap. If Xanadu's 2028–29 fault-tolerance milestone slips, this is the slowest photonic track."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Gates act on optical quadratures — beam-splitters, phase shifts, squeezers — closed by homodyne feed-forward. Gaussian operations with homodyne detection are classically simulable, so universality needs a non-Gaussian resource: the Gottesman–Kitaev–Preskill grid state, 2001 [S][3]. Time-domain multiplexing predates the companies — the University of Tokyo entangled over 10,000 modes in 2013 [D][4]; Xanadu added the modular chip version [D][1] and the first integrated GKP source [D][2]. Coordinates: flying carrier, partly fabricated, ~1 µs deterministic step, Gaussian-noise and loss-dominated error; electro-optic control at room temperature, photonic-IC fabrication.

## Physics & limits
Loss acts as a Gaussian random-displacement channel on the grid, blurring the GKP peaks until modular-quadrature measurement cannot resolve the logical value; the floor is effective squeezing, not gate count. Xanadu's on-chip source reports 0.62 dB [D][2] — grid-noise variance ~0.87 of vacuum against ~0.10 at the ~10 dB assumed, an ~8.7× reduction still to find [S], a different quantity from Xanadu's 24.1× loss factor above threshold [C][6]. Only lower per-element loss, better sources and deeper multiplexing move it. Feed-forward adds a second floor: electronics must act inside the ~1 µs clock, and the published CV loop is 196 ns [P][7].

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2013-11 | >10,000-mode time-domain CV cluster state | Univ. of Tokyo | [D][4] |
| 2025-01 | Aurora: 35 chips, 12 modes per 1 MHz cycle, 2 h, ~14 dB loss | Xanadu | [D][1] |
| 2025-06-05 | First integrated GKP source, 0.62 dB effective squeezing, SiN | Xanadu | [D][2] |

No GKP logical qubit exists; Aurora ran two hours without error correction and reported no logical fidelity, so it shows stability, not computation [D][1].

## Manufacturing, materials & supply chain
Fabrication is silicon-nitride lithography on 300 mm-class wafers, shared with the discrete-variable sector; the CV-specific additions are squeezers and high-efficiency homodyne receivers rather than switches, and the GKP source runs at room temperature [D][2]. Packaging is Corning fibre arrays and DISCO singulation [C][9].  Control is the heavy part: every mode needs a homodyne receiver, an ADC and a loop closing inside the clock, scaling linearly with no published shortcut. At 10³ modes that is a rack of receivers, at 10⁴ the analogue front end dominates, and nothing addresses 10⁶. ECCN 4A906 applies to the machine [G:BIS-QUANTUM-2024].

## Role in the stack
The continuous-variable path's gate layer, requiring squeezed sources and room-temperature feed-forward. It substitutes for rather than complements discrete-variable fusion: CV measures quadratures where fusion detects single photons, so switching paths replaces sources, detectors and decoders together. Derived clock 1.0 MHz [D][1]. Verification is thin: the 0.62 dB is single-group, unreplicated, and routinely confused with raw quadrature squeezing — the 1.4 dB in periodically poled TFLN [P][5] is a different quantity.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Xanadu | developer | CA | Aurora, integrated GKP source, GKP+qLDPC roadmap | [D][1][D][2] |
| University of Tokyo | research | JP | Origin of large-scale time-domain CV cluster states | [D][4] |
| Corning | supplier | US | Fibre arrays behind Xanadu's coupling figure | [C][9] |

**Money.**
2025-11-06 · Xanadu · DARPA QBI Stage B selection · up to USD 15 M · DARPA · announced [G:QBI-STAGEB-2025-11]
2026-03-26 · Xanadu · SPAC merger with Crane Harbor · ~USD 302 M gross, ~40% below plan · closed [C][G:XANADU-SPAC-2026-03]
2026-08-28 · Xanadu · Toronto factory funding · CAD 195 M · Government of Canada · announced [C][6]
2026-08-31 · Xanadu · liquidity · ~USD 686 M at 2026-06-30 · reported [C][G:XANADU-LIQUIDITY-2026-06]

**Market & supply chain.** One commercial actor, so no market — only Xanadu's supply relationships and the packaging concentration it shares with photonics generally. CV pays for G1 today; G3/G4 only if squeezing closes, G6 the natural adjacency.

**IP & standards.** No dated CV/GKP patent count from a named database as of 2026-09-04; Strawberry Fields/Blackbird is the only CV-native open-source stack, used by no other vendor.

**Roadmaps & track record.** The 2026-08-31 release is Xanadu's first quantified schedule (promised 2026-08: fault tolerance 2028–29, 200 logical qubits 2029, 1,000+ by 2031) — too new to score [C][6]; against it stands one miss, the SPAC closing ~40% below plan [C][G:XANADU-SPAC-2026-03]. Its physics claims are self-critical; its financing claims are not.

**Strategic reading.** If effective squeezing improves an order of magnitude, CV's flying room-temperature carrier is the natural networking substrate and G6 is Xanadu's to lose. If not, no second actor exists to inherit the track, and its suppliers are worth more than its architecture.

*Open niche:* a small QCVV group could own the missing measurement discipline — reporting effective squeezing, raw squeezing and loss at declared reference planes, so 0.62 dB and 1.4 dB stop being quoted as commensurable.

## Outlook & open questions
Confirm by 2027: effective squeezing above 3 dB on chip; demote the 2028–29 milestone if it stays below 1 dB. Best case 2029: a small GKP logical qubit at low distance. Worst case: uncorrected demonstrations continue and the schedule slips as the financing did. Open: how much of the gap is loss versus fabrication; do homodyne front-ends scale.

## Sources
[1] Xanadu, "Scaling and networking a modular photonic quantum computer" (Aurora), Nature 638, 2025-01 [D] — https://www.nature.com/articles/s41586-024-08406-9
[2] Xanadu, "Integrated photonic source of Gottesman–Kitaev–Preskill qubits," Nature, 2025-06-05 [D] — https://www.nature.com/articles/s41586-025-09044-5
[3] Gottesman, Kitaev, Preskill, "Encoding a qubit in an oscillator," Phys. Rev. A 64, 012310, 2001 [S] — https://journals.aps.org/pra/abstract/10.1103/PhysRevA.64.012310
[4] Yokoyama, Ukai, Armstrong, Sornphiphatphong, Kaji, Suzuki, Yoshikawa, Yonezawa, Menicucci, Furusawa (University of Tokyo), "Ultra-large-scale continuous-variable cluster states multiplexed in the time domain," Nature Photonics, 2013-11-17 [D] — https://www.nature.com/articles/nphoton.2013.287
[5] Shi et al., "Squeezed light generation in periodically poled thin-film lithium niobate waveguides," arXiv:2508.08599, 2025-08-12 [P] — https://arxiv.org/abs/2508.08599
[6] Xanadu, "Xanadu Charts Path to Over 1,000 Logical Qubits by 2031," GlobeNewswire, 2026-08-31 [C] — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html
[7] Duggan, Filgis, Bregnsbo, Saalmüller, Neergaard-Nielsen, Wintermantel, Andersen, "FPGA Based Feedforward System for Photonic Quantum Computing Applications," arXiv:2606.03500, 2026-06-02 [P] — https://arxiv.org/abs/2606.03500
[8] HPCwire, "Xanadu Unveils 1st On-Chip Error-Resistant Photonic Qubit," 2025-06-05 [P] — https://www.hpcwire.com/off-the-wire/xanadu-unveils-1st-on-chip-error-resistant-photonic-qubit/
[9] PR Newswire, "Xanadu Sets New Industry Benchmark in Photonic Chip Packaging," 2026-06-10 [C] — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html

## Open verification items
The nature.com page for the GKP source could not be consulted; its date, platform and room-temperature operation are taken from the publisher's press coverage [8], and the 0.62 dB figure from the main report. The ~10 dB threshold is the main report's figure; published GKP threshold estimates vary with decoder and architecture and no single authoritative value was verified here. The 0.87→0.10 variance conversion is derived here, not quoted. Xanadu's 24.1× loss factor and the 0.62 dB effective squeezing are different quantities that no source reconciles. Affiliations for arXiv:2606.03500 and arXiv:2508.08599 were not confirmed from their abstract pages. No independent replication of the 0.62 dB result exists.
