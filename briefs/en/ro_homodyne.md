---
id: ro_homodyne
name: Homodyne quadrature detection (CV)
layer: "6 Readout"
status: demonstrated
since: 2012
one_line: "A signal mode interfered with a strong local oscillator on a balanced photodiode pair, whose difference current samples one chosen field quadrature — the computational measurement of continuous-variable and GKP machines."
verdict: "The receiver physics is mature — integrated detectors stay shot-noise-limited to 9–20 GHz against a 1 MHz machine clock — but as of 2026-09-26 no CV machine has published the efficiency or electronic-noise clearance of its computational homodyne channels, and upstream loss, not the detector, sets the error floor."
updated: 2026-09-26
---

LO = local oscillator; GKP = Gottesman–Kitaev–Preskill grid state; MBQC = measurement-based quantum computation; PNR = photon-number-resolving; TES = transition-edge sensor; TIA = transimpedance amplifier; OPA = optical parametric amplifier; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A weak signal mode and a strong LO meet on a 50:50 beam-splitter; subtracting the two photocurrents cancels the LO's classical noise and leaves a signal proportional to the quadrature x̂_θ = x̂ cos θ + p̂ sin θ, θ set by the LO phase. Heterodyne detection measures two conjugate quadratures at once for one extra unit of vacuum noise. It became a computational readout when time-multiplexed CV cluster states were read mode by mode — Tokyo [D][635] and DTU [D][636], both 2019 — and moved onto chips in Xanadu's Aurora [D][173].
Attributes: destructive but mid-circuit (in MBQC the measurement angle is the gate); ~10⁻⁶ s per measurement at the 1 MHz clock; room-temperature electro-optic control; Gaussian-noise errors; photonic-IC fabrication.

## Physics & limits
Efficiency η acts as loss before an ideal detector: variance V is recorded as ηV + (1−η) in vacuum units, so observing 10 dB of squeezing needs η > 0.90 even for infinite input squeezing [S]. For GKP states, rescaling by 1/√η turns inefficiency into a Gaussian displacement of variance (1−η)/η: η = 0.99 adds 0.010, a tenth of the 0.106 the Atlas's ~9.75 dB target allows (~0.4 dB); η = 0.95 alone drags 9.75 dB to 8.0 dB [S]. Electronic-noise clearance C dB is an equivalent efficiency 1 − 10^(−C/10): 20 dB costs 1 %, 28 dB 0.16 % [S]. LO phase jitter δθ admits the anti-squeezed quadrature, V ≈ V_sq + V_anti·δθ²; at 15 dB anti-squeezing, 1° rms costs as much as 1 % inefficiency [S]. Bandwidth must exceed the inverse mode duration — Tokyo's 40 ns bins sat under ~100 MHz detectors [D][635]. A GKP outcome is binned to the nearest multiple of √π and its parity read as the logical value; q̂, p̂ and q̂+p̂ implement Z, X and Y, and the distance to the bin edge can weight the outer decoder [S][637].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2019 | 2D cluster state; ~100 MHz homodyne, efficiency 0.75–0.80; nullifiers −4.8 to −5.3 dB | Univ. of Tokyo | [D][635] |
| 2019 | >30,000-mode 2D cluster state; two fibre homodyne detectors; nullifiers −4.7 / −4.3 dB | DTU | [D][636] |
| 2021 | Ge-on-Si + SiGe receiver: 1.7 GHz 3-dB bandwidth, shot-noise-limited beyond 9 GHz | Univ. of Bristol | [D][638] |
| 2021 | Silicon photonics + GaAs TIA: shot-noise-limited beyond 20 GHz, 28 dB clearance | Ghent Univ. | [D][639] |
| 2023 | OPA pre-amplification: 5.2 ± 0.5 dB squeezing, DC–43 GHz, uncorrected | Univ. of Tokyo, NTT | [D][640] |
| 2025 | Aurora: on-chip homodyne, 12 modes per 1 MHz cycle, single-cycle feed-forward | Xanadu | [D][173] |
| 2026 | Squeezer and homodyne on one chip: 34 modes, ~3 dB, 72 % efficiency | Univ. of Virginia | [D][641] |

Speed is solved three orders of magnitude beyond need; efficiency is not. The one generation-plus-detection chip reaches 72 % [D][641], and Aurora states no efficiency, bandwidth or clearance for its channels [D][173]. OPA pre-amplification sidesteps the detector: equivalent post-amplifier loss falls from 92.4 % to 0.4 % [D][640]. Dominant term: loss upstream — ~56 % in Aurora's heralding paths, over 95 % in its heralded paths, against ~1 % budgets [D][173].

## Manufacturing, materials & supply chain
Aurora's QPU array is five modules on AIM Photonics' 300 mm silicon-photonic platform — SiN and Si waveguides, germanium photodiodes, carrier-depletion modulators — with the LO envelope shaped by an Exail MXIQER-LN-30 modulator [D][173]. Squeezing wants low-loss waveguides, detection strong absorption; Virginia joined both on one chip by heterogeneously integrating photodiodes [D][641]. Bandwidth is photodiode capacitance against the amplifier — SiGe electronics at Bristol [D][638], a GaAs pHEMT TIA at Ghent [D][639]. The parts are coherent-telecom stock; Tokyo's receiver is a 5G photodiode [D][640].

## Control, readout & I/O burden
Each channel is a photodiode pair, TIA, ADC, phase-controlled LO path and a feed-forward link acting within one clock. In Aurora a reference laser carries the phase that stabilises measurement angles, and a controller informed by algorithm and decoder selects bases every cycle, with single-clock-cycle feed-forward [D][173]; DTU locked its LOs by AC demodulation [D][636]. Receivers run at room temperature; heralding by Aurora's 36 PNR detectors is a separate chain [D][173]. Channels scale linearly with modes per clock — 12 in Aurora; at 10³–10⁴ the ADC and feed-forward budget, not the optics, dominates [S].

## Role in the stack
The Readout slot of the Continuous-variable photonic — GKP architecture, beside single-photon detection. It **requires** a squeezed-light source (a quadrature to measure) and electro-optic control (LO phase); it **provides** no downstream edge; single-photon detection **replaces** it wherever photons are counted. The gap ledger (G-homodyne) created it because SNSPD/TES counting heralds a CV machine but does not compute; Aurora confirms the fix [D][173], while GKP preparation still heralds with PNR detectors quoted above 99 % efficiency [P][642]. Register: Aurora primary, cell ✅. Borealis does not carry it: its 216 squeezed modes pass a 1-to-16 demultiplexer onto 95 %-efficient TES PNR detectors, no homodyne stated [D][270].

## Evidence — how the numbers were measured
Receivers are qualified by shot-noise linearity, clearance and squeezed-light efficiency calibration; systems by nullifier variances below the −3 dB entanglement bound — all 1,500 of DTU's were [D][636]. Such figures include detection, like the uncorrected 5.2 dB at 43 GHz [D][640]; loss-corrected squeezing and GKP effective squeezing — 0.62 dB for Xanadu's integrated source in the Atlas's record [D][174] — are other quantities. Thresholds depend on architecture: static linear optics needs 10.1 dB with all modes GKP, 13.6 dB with one per macronode, lossless [S][637]. As of 2026-09-26 Aurora reports path losses but no per-channel efficiency, clearance or phase noise [D][173].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Xanadu | developer | Canada | On-chip homodyne with single-cycle feed-forward (Aurora) | [D][173] |
| University of Tokyo, NTT | research | Japan | Cluster-state readout; OPA-amplified 43 GHz measurement | [D][635], [640] |
| DTU | research | Denmark | Cluster state read by fibre homodyne detectors | [D][636] |
| University of Bristol | research | UK | Ge-on-Si + SiGe receiver, 9 GHz | [D][638] |
| Ghent University | research | Belgium | Silicon photonics + GaAs TIA, >20 GHz | [D][639] |
| AIM Photonics | foundry | US | 300 mm platform with Ge photodiodes for Aurora | [D][173] |

**Money.** No dated financial item specific to homodyne readout was found as of 2026-09-26.

**Market & supply chain.** No merchant market in computational receivers; the parts are shared with CV key distribution and random-number generation [D][639]. It pays into G4 and G6; the G1 sampler does without it.

**IP & standards.** As of 2026-09-26 no standard for reporting homodyne efficiency or clearance, and no dated patent count specific to it.

**Roadmaps & track record.** No developer has published a dated homodyne target as of 2026-09-26. Aurora's 35 chips and 86.4 billion modes over 2 h are a scale result, not a readout-quality one [D][173].

**Strategic reading.** If effective squeezing nears threshold, receivers become a CV machine's most numerous active component — one per mode per clock — and value moves to whoever co-integrates them with feed-forward on the photonic die; OPA pre-amplification is the hedge. If not, homodyne stays in key distribution and metrology.

## Outlook & open questions
Confirm if, by 2027-12-31, a CV machine publishes per-channel homodyne efficiency ≥ 99 % with ≥ 20 dB clearance, or on-chip GKP effective squeezing exceeds 3 dB; demote if by 2028-06-30 no CV system paper discloses receiver figures while effective squeezing stays below 1 dB.

Open questions. (1) Aurora's per-channel efficiency and clearance? (2) Can photodiodes on a low-loss squeezing platform reach 99 %? (3) Does OPA pre-amplification scale to one locked pump per mode? (4) What LO phase noise does GKP binning tolerate near 10 dB? (5) How much of the gap from 0.62 dB is detection loss?

## Sources

[173] H. A. Rad *et al.*, “Scaling and networking a modular photonic quantum computer,” *Nature*, vol. 638, no. 8052, pp. 912–919, Jan. 2025, doi: [10.1038/s41586-024-08406-9](https://doi.org/10.1038/s41586-024-08406-9). [D]
[174] M. V. Larsen *et al.*, “Integrated photonic source of Gottesman–Kitaev–Preskill qubits,” *Nature*, vol. 642, no. 8068, pp. 587–591, Jun. 2025, doi: [10.1038/s41586-025-09044-5](https://doi.org/10.1038/s41586-025-09044-5). [D]
[270] L. S. Madsen *et al.*, “Quantum computational advantage with a programmable photonic processor,” *Nature*, vol. 606, no. 7912, pp. 75–81, Jun. 2022, doi: [10.1038/s41586-022-04725-x](https://doi.org/10.1038/s41586-022-04725-x). [D]
[635] W. Asavanant *et al.*, “Time-Domain Multiplexed 2-Dimensional Cluster State: Universal Quantum Computing Platform,” *Science*, vol. 366, p. 373, 2019, doi: [10.1126/science.aay2645](https://doi.org/10.1126/science.aay2645). [arXiv:1903.03918](https://arxiv.org/abs/1903.03918). [D]
[636] M. V. Larsen, X. Guo, C. R. Breum, J. S. Neergaard-Nielsen, and U. L. Andersen, “Deterministic generation of a two-dimensional cluster state,” *Science*, vol. 366, p. 369, 2019, doi: [10.1126/science.aay4354](https://doi.org/10.1126/science.aay4354). [arXiv:1906.08709](https://arxiv.org/abs/1906.08709). [D]
[637] I. Tzitrin *et al.*, “Fault-tolerant quantum computation with static linear optics,” *PRX Quantum*, vol. 2, Art. no. 040353, 2021, doi: [10.1103/PRXQuantum.2.040353](https://doi.org/10.1103/PRXQuantum.2.040353). [arXiv:2104.03241](https://arxiv.org/abs/2104.03241). [S]
[638] J. F. Tasker *et al.*, “Silicon photonics interfaced with integrated electronics for 9 GHz measurement of squeezed light,” *Nat. Photon.*, vol. 15, pp. 11–15, Jan. 2021, doi: [10.1038/s41566-020-00715-5](https://doi.org/10.1038/s41566-020-00715-5). [arXiv:2009.14318](https://arxiv.org/abs/2009.14318). [D]
[639] C. Bruynsteen *et al.*, “Integrated balanced homodyne photonic–electronic detector for beyond 20 GHz shot-noise-limited measurements,” *Optica*, vol. 8, no. 9, pp. 1146–1152, Sep. 2021, doi: [10.1364/OPTICA.420973](https://doi.org/10.1364/OPTICA.420973). [D]
[640] A. Inoue *et al.*, “Toward a multi-core ultra-fast optical quantum processor: 43-GHz bandwidth real-time amplitude measurement of 5-dB squeezed light using modularized optical parametric amplifier with 5G technology,” *Appl. Phys. Lett.*, vol. 122, Art. no. 104001, 2023, doi: [10.1063/5.0137641](https://doi.org/10.1063/5.0137641). [arXiv:2205.14061](https://arxiv.org/abs/2205.14061). [D]
[641] H. Chen *et al.*, “Heterogeneously Integrated Squeezed-Light Generation and Detection on a Single Photonic Chip,” [arXiv:2608.13218](https://arxiv.org/abs/2608.13218), Aug. 2026. [D]
[642] Xanadu, “Xanadu Unveils 1st On-Chip Error-Resistant Photonic Qubit,” HPCwire, Jun. 5, 2025. [Online]. Available: https://www.hpcwire.com/off-the-wire/xanadu-unveils-1st-on-chip-error-resistant-photonic-qubit/ [P]

## Open verification items
- 2026-09-26: the integrated GKP source paper (doi:10.1038/s41586-025-09044-5) could not be opened — nature.com returned 502 twice, Europe PMC was rate-limited (429), PMC served a captcha; the 0.62 dB figure is carried from the Atlas's record, not re-read.
- 2026-09-26: no primary source for the Atlas's ~9.75 dB requirement was found; Tzitrin et al. give 10.1 dB, 13.6 dB or ~10 dB depending on architecture.
- 2026-09-26: Aurora's Nature article states no homodyne efficiency, bandwidth, clearance or feed-forward latency; the arXiv id 2403.15385 proposed for it belongs to an unrelated paper (LATTE3D), and the Nature page lists none.
- 2026-09-26: DTU's 2019 homodyne efficiency is deferred in its arXiv text to earlier work; the Science full texts were not opened.
- 2026-09-26: Bruynsteen et al. were read only through a SciSpace abstract page (Optica served a script challenge, ADS blocked by robots.txt, Crossref rate-limited); co-author names and the frequency at which the 28 dB clearance is quoted are unconfirmed.
- The dossier's "since 2012" is not tied to a verified event; Vahlbruch et al. 2016 (15 dB, photodiode efficiency calibration) returned 403 and is not cited.
