---
id: cx_shuttle
name: Spin shuttling (conveyor mode)
layer: "4 Connectivity / transport"
status: emerging
since: 2025
one_line: "Coherent transport of a spin qubit along a gate-defined conveyor, buying distance and layout sparsity with a dephasing budget rather than with wiring."
verdict: "Transport is no longer the limiting error in a shuttling circuit; the static exchange gates are. Demote if no 300 mm foundry conveyor link reaches 99% per 10 µm by end-2027."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

Conveyor-mode spin shuttling moves a single spin along a gate-defined channel on a travelling potential wave: overlapping clavier gates driven with fixed phase offsets by four sinusoids (eight two-tone), the carrier riding the moving minimum. Bucket-brigade shuttling needs one pulsed control per hop; a conveyor needs a control count set by the number of phases, not by distance. That is the node's whole economic case, and this brief is its price. Bluhm's group at RWTH Aachen and Forschungszentrum Jülich introduced it as the QuBus: 420 nm channel, four sinusoids, 99.42 ± 0.02% single-electron shuttling — charge, not spin [D][1]. Spin coherence at length followed at Delft [D][2].

Attributes. **a — affinity:** fully fabricated, an electron in a lithographic ²⁸Si/SiGe well. **b — time:** ~2 × 10⁻⁷ s per 10 µm transit [D][2]; entangling not applicable, this is transport. **c — readout:** none of its own, it borrows the register's charge sensor. **d — mobility:** transport, the node's entire function. **e — control:** no modality or placement of its own, one shared radio-frequency drive. **f — error as the code sees it:** coherent, dephasing and position-dependent rotations, no loss channel. **g — manufacturing:** CMOS, the same 300 mm line as the dots.

## Physics & limits

Gates at 180 nm pitch driven to 300 MHz make a moving confinement minimum; the carrier follows adiabatically at 36 m/s single-tone, 64 m/s two-tone [D][2]. Adiabaticity bounds transit time from below through orbital and valley splittings, spin coherence from above. Spin–orbit coupling and micromagnet gradients make transport a deterministic, position-dependent rotation — coherent, hence calibratable in principle — and motion also helps, Delft attributing the improved coherence of moving spins to motional averaging [D][3]. Charge noise and disorder pin the carrier and excite it at valley–orbit anticrossings [S][4]. Nothing thermodynamic bounds any of this, so the floor is materials: valley-splitting uniformity along a line, and charge noise. Moving it takes interface engineering, quieter gate stacks, echo during transport (in germanium, echo lifted the characteristic shuttle number from 64–77 to above 300 [D][5]) or confinement modulation [S][6]. Surface-code simulation gives a dephasing threshold of several percent and moderate overhead to ~1% error per shuttle [S][7] — forgiving, but conditional on gates and readout already sitting below threshold, which on spins they do not.

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-08 | 420 nm conveyor, four controls, 99.42 ± 0.02% single-electron (charge) shuttling | RWTH Aachen | [D][1] |
| 2024-07-08 | Germanium holes, bucket-brigade: 99.97% per shuttle, basis states only, 312 µm effective | QuTech | [D][5] |
| 2025-06-09 | Conveyor: 10 µm in under 200 ns at 99.54 ± 0.03% spin fidelity | QuTech | [D][2][G:SHUTTLE-DELFT-2025-06] |
| 2026-05-06 | Controlled-phase gate between two *moving* spins: 98.86 ± 0.29%, 240 nm, 58 ns | QuTech | [D][3] |
| 2026-07-29 | Weight-four parity, mobile ancilla: 97.7(1)% per 1.2 µm round trip; Z-parity 72.2(6)% | QuTech | [D][8] |

The dominant error term is counter-intuitive: in the five-qubit parity device the limit is incoherent noise in the exchange interaction, dephasing during shuttling and idling being about a quarter of the total [D][8]. Transport has stopped being the worst thing in a shuttling circuit; the static gates are, and the route past 99% is gate-stack change, not faster conveyors. Typical-at-scale does not exist: every result above is on a research-fab heterostructure, and no conveyor link has been published on a 300 mm device.

## Manufacturing, materials & supply chain

Three overlapping gate layers at ~180 nm pitch over an enriched ²⁸Si/SiGe well, 7 nm thick at Delft [D][2] — nominally 300 mm-compatible, and the node's hard dependency is exactly that: uniform conveyor gates on a CMOS line. Dots need only resemble each other; a bus must be uniform along its whole length, because one pinning defect breaks the channel and a conveyor carries no redundancy. No yield or uniformity statistic has been published for conveyors, conspicuous beside Intel's 24,000-plus spin devices per wafer at 96% tune-up yield [D][9]. Supply: enriched ²⁸Si from a handful of isotope separators, the single point of failure the silicon-spin path already shares, and SiGe epitaxy and overlay at imec, Intel, GlobalFoundries and STMicroelectronics. Cost per bus is not quotable; no ECCN mapping of the quantum dual-use regime is asserted here.

## Control, readout & I/O burden

Four or eight shared radio-frequency lines drive an arbitrarily long bus, so line count scales with the number of buses, not with distance or stops served; a bucket-brigade link of equal reach needs one pulsed line per hop. Sparsity is what makes co-located electronics fit — the argument HRL's 4 K controller makes from the other end at ≤3.5 W and 366 DACs for 18 qubits [D][10][G:HRL-CRYOCMOS-4K-2026]. The node has no readout; a mobile ancilla is measured at a dedicated site [D][8]. Latency is not the binding constraint: 4 ns hops and 58 ns moving-spin gates sit two to three orders below spin readout at 1–100 µs, so shuttling does not lengthen the syndrome cycle. The walls: at 10³ qubits, channel uniformity on 300 mm; at 10⁴, phase calibration across thousands of drifting conveyors; at 10⁶, the dephasing budget — at 10⁻³ per µm, one micron of travel per syndrome extraction is affordable and one hundred is not.

## Role in the stack

The node belongs to the silicon and germanium quantum-dot spin path (Intel, Diraq, Quantum Motion, HRL under IBM, QuTech, Quobly). It requires gate-defined dot spins to move and a 300 mm CMOS foundry for uniform conveyor gates, and provides nothing downstream: its value is realised inside the path it serves, which is why it will never be sold as a product. It replaces static nearest-neighbour exchange, which costs no transport error; a shuttled link buys distance with a dephasing budget and a calibration burden, worth paying only when control and readout electronics must be interleaved among the qubits. Off-diagonal reading: the node sits far from the fabrication cluster it depends on, its physics set by disorder in research heterostructures and its economics by a 300 mm line it has never run on. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: transport contributes 2.0 × 10⁻⁷ s and gates 5.8 × 10⁻⁸ s each, so the path stays readout-limited at 8.5 × 10⁻⁶ s, readout 6.3 µs of it and reset 1 µs. Empty neighbouring slots: transport across a die boundary, and a link with in-flight leakage detection.

## Verification (QCVV)

The silicon figure comes from interleaved randomised benchmarking of a shuttle "gate" over the 10 µm path [D][2]; the germanium figure from exponential fits to a characteristic shuttle number [D][5]. Different observables, routinely quoted side by side: 99.97% per shuttle in germanium is basis-state only, 99.54% in silicon a spin fidelity over a path. Benchmarking a shuttle also assumes twirlability, questionable for a deterministic position-dependent rotation, since motional averaging can flatten the benchmark below the physical error at any single point. Neither protocol reports leakage out of the valley or orbital subspace, and no shuttling result has been cycle- or mirror-benchmarked, so the correlated error a code would see is unmeasured. Conveyor transport is shown at charge level by RWTH Aachen, at spin level by Delft; the 10 µm figure has no independent replication as of 3 Sep 2026.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | research | NL | Every conveyor spin record: 10 µm link, moving-spin gate, mobile ancilla | [D][2], [3], [8] |
| RWTH Aachen | research | DE | Invented conveyor mode; SpinBus architecture | [D][1][S][7] |
| Forschungszentrum Jülich | research | DE | Conveyor co-parent; hosts ARQUE's first system | [C][11] |
| ARQUE Systems | developer | DE | Sells patented shuttling paths; five-qubit processor | [C][11] |
| IBM | developer | US | Acquired HRL: exchange-only silicon plus 4 K cryo-CMOS | [G][12] |
| Diraq | developer | AU | 300 mm silicon MOS with imec; sparse layouts underpin its cost claim | [D][9] |
| Quantum Motion | developer | UK | 22FDX CMOS, full-stack system at NQCC | [C][13] |
| imec | supplier | BE | 300 mm spin line; would fabricate any foundry conveyor | [D][9] |

**Money.**
- 2022-09 · ARQUE Systems · spin-off founded by Bluhm and three colleagues · undisclosed · Jülich, RWTH Aachen · announced [C][11]
- 2025-11-06 · DARPA QBI Stage B · eleven teams including Diraq, Quantum Motion · up to $15 M each · announced [G][14][G:QBI-STAGEB-2025-11]
- 2026-05-07 · Quantum Motion · Series C · $160 M · DCVC, Kembara · closed [C][13][G:QM-160M-2026-05]
- 2026-05-21 · Diraq · CHIPS letter of intent · up to $38 M · US Commerce · LOI [G][15][G:CHIPS-LOI-2026-05]
- 2026-06-03 · Quobly · Series A · €115 M · Bpifrance, SEALSQ, STMicroelectronics · closed [C][16][G:QUOBLY-115M-2026-06]
- 2026-07-23 · IBM · acquisition of HRL Laboratories · undisclosed · close targeted end Q3 2026 · announced [G][12][G:IBM-HRL-2026-07]

None of these is financing for shuttling as such: it is a feature funded inside spin-qubit companies, not a fundable line item, with ARQUE the sole exception — and its funding undisclosed.

**Market & supply chain.** Nobody sells a shuttle. Enabling supply is 300 mm lithography and overlay, SiGe epitaxy, enriched ²⁸Si substrates and multi-channel waveform generation. G3 and G4 pay for it, since sparsity only earns its dephasing cost at code scale; G7 marginally, through the Jülich installation; G1 and G5 nothing.

**IP & standards.** The conveyor family originates with RWTH Aachen and Forschungszentrum Jülich; ARQUE commercialises a patented shuttling mechanism [C][11]. No dated family count from a named database exists for this node, so none is quoted, and no standards body covers spin transport.

**Roadmaps & track record.** (promised 2021-08 · conveyor as a scalable bus · status 2026-09-03: single-channel level only, never on a foundry wafer). (ARQUE Systems, promised 2026 · five-qubit shuttling processor at Jülich · status: installation under way, no acceptance data [C][11]). (QuTech, promised 2026-07 · above-99% shuttled parity via gate-stack change · status: 97.7% per shuttle [D][8]). (Diraq, promised 2026-08-27 · 150 k physical and 1 k logical qubits by 2029 · status: eight-qubit foundry device with one working pair, its own July release saying "thousands by 2029" [C][G:DIRAQ-FUNDING][G:DIRAQ-8Q-2026-07]). QuTech is the strongest actor here; ARQUE is unproven but the only vehicle with a delivery date; Diraq's numbers move faster than its devices.

**Strategic reading.** If the conveyor reaches foundry uniformity, the winners are the CMOS spin vendors whose thesis is density-through-sparsity — IBM with HRL, Diraq, Quantum Motion, Quobly — and the cryogenic control suppliers, since sparse lattices are what make co-located electronics fit. Losers: dense nearest-neighbour exchange architectures, and foundries selling dot uniformity rather than line uniformity. Bargaining power sits with the 300 mm lines and the enriched-silicon suppliers; a transport primitive with no standalone product will be absorbed as an IP position, which is what the Aachen and Jülich patents already are.

*Open niche:* the opening is the measurement gap. No shuttle has been cycle-benchmarked, and benchmarking a deterministic, position-dependent rotation is a questionable primitive. A small QCVV house could define a position-resolved, leakage-sensitive shuttling benchmark separating calibratable coherent error from stochastic dephasing, plus automated calibration for tens of clavier phases per bus. On the SFQ side, the conveyor drive is four to eight phase-locked sinusoids at a few hundred megahertz per bus — a deterministic, repetitive, low-power waveform of the kind single-flux-quantum generation produces at 4 K and below.

## Outlook & open questions

Falsifiable milestones for 12–24 months. Confirm: a conveyor spin link on a 300 mm foundry device at ≥99% per 10 µm by 2027-09; a shuttled-ancilla parity check above 99%, the target the Delft authors set themselves [D][8]; independent replication by a group other than Delft. Demote: if shuttled-ancilla parity stays below ~90% through 2027, the sparse-architecture argument loses its only experimental leg; or if valley-splitting variation along channels proves irreducible on foundry material. Best case by 2029, a distance-3 to distance-5 surface-code patch on a sparse spin lattice with shuttled syndrome extraction; worst case, shuttling stays a Delft and Aachen speciality on research heterostructures.

Open questions. (1) Is benchmarking of a shuttle a meaningful fidelity, or an artefact of motional averaging? (2) Does motional averaging survive foundry-level charge disorder, or invert into pinning? (3) What is the leakage rate at valley anticrossings? (4) Can conveyor phase calibration be automated across thousands of buses? (5) Can a spin cross a die boundary? Watch: any 300 mm shuttling result from imec, Intel, GlobalFoundries or STMicroelectronics; ARQUE's acceptance data at Jülich; QuTech's follow-up to the weight-four parity device.

## Sources

[1] I. Seidler *et al.*, “Conveyor-mode single-electron shuttling in Si/SiGe for a scalable quantum computing architecture,” [arXiv:2108.00879](https://arxiv.org/abs/2108.00879), Aug. 2021.
[2] M. De Smet *et al.*, “High-fidelity single-spin shuttling in silicon,” *Nat. Nanotechnol.*, vol. 20, no. 7, pp. 866–872, Jun. 2025, doi: [10.1038/s41565-025-01920-5](https://doi.org/10.1038/s41565-025-01920-5).
[3] Y. Matsumoto *et al.*, “Two-qubit logic and teleportation with mobile spin qubits in silicon,” *Nature*, vol. 653, no. 8114, pp. 391–397, May 2026, doi: [10.1038/s41586-026-10423-9](https://doi.org/10.1038/s41586-026-10423-9).
[4] N. Ciroth *et al.*, “Numerical simulation of coherent spin-shuttling in a QuBus with charged defects,” [arXiv:2512.03588](https://arxiv.org/abs/2512.03588), Dec. 2025. [S]
[5] F. van Riggelen *et al.*, “Coherent spin qubit shuttling through germanium quantum dots,” *Nat. Commun.*, vol. 15, Art. no. 5716, Jul. 2024, doi: [10.1038/s41467-024-49358-y](https://doi.org/10.1038/s41467-024-49358-y).
[6] D. Q. L. Nguyen, M. Rimbach-Russ, and S. Bosco, “Suppressing spin qubit decoherence during shuttling via confinement modulation,” [arXiv:2605.00611](https://arxiv.org/abs/2605.00611), May 2026. [S]
[7] B. Yenilen, A. Sala, H. Bluhm, M. Müller, and M. Rispler, “Performance of the spin qubit shuttling architecture for a surface code implementation,” [arXiv:2503.10601](https://arxiv.org/abs/2503.10601), Mar. 2025. [S]
[8] B. Undseth *et al.*, “Weight-four parity checks in a spin-shuttling architecture,” *Nature*, vol. 655, no. 8125, pp. 1160–1166, Jul. 2026, doi: [10.1038/s41586-026-10766-3](https://doi.org/10.1038/s41586-026-10766-3).
[9] P. Steinacker *et al.*, “Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity,” *Nature*, vol. 646, no. 8083, pp. 81–87, Sep. 2025, doi: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9).
[10] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026.
[11] Forschungszentrum Jülich, “Jülich-Aachen Start-up Paves the Way for Scalable Quantum Computers,” fz-juelich.de, Apr. 8, 2026. [Online]. Available: https://www.fz-juelich.de/en/news/archive/press-release/2026/julich-aachen-start-up-arque-systems [C]
[12] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [G]
[13] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[14] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[15] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[16] Quobly, “Quobly secures €115 million Series A to bring silicon-based quantum computers to market,” Jun. 3, 2026. [Online]. Available: https://www.quobly.io/press-releases/quobly-secures-e115-million-series-a-to-bring-silicon-based-quantum-computers-to-market [C]

## Open verification items

- ARQUE Systems funding: no round, amount or investor disclosed in the Forschungszentrum Jülich release [11]; no company or database page is cited for it. Headcount and a dated installation milestone at Jülich Supercomputing Centre are likewise unverified.
- arXiv:2503.10601 [7]: no author list, institution or date is available for it; the threshold figures quoted come from the abstract text only.
- arXiv:2605.00611 [6]: abstract not machine-readable; cited by title only, no quantitative claim taken from it.
- Export-control classification: no ECCN or category mapping for quantum-computing items and enriched ²⁸Si substrates is established here; no rule number is asserted.
- No published yield, channel-uniformity or per-bus cost data exist for conveyor structures on any 300 mm line as of 2026-09-03 — an absence, not a conflict.
- Source conflict, minor: "99.5%" (abstract) versus "99.54 ± 0.03%" (interleaved randomised benchmarking) in [2] — same measurement; this brief uses 99.54%. Cross-platform: the germanium "99.97% per shuttle" [5] is a basis-state figure, not comparable with the silicon conveyor spin fidelity [2].
