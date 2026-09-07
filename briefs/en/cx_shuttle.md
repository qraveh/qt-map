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

Conveyor-mode spin shuttling moves a single spin along a gate-defined channel on a travelling potential wave: overlapping clavier gates driven with fixed phase offsets by four sinusoids (eight two-tone), the carrier riding the moving minimum. Bucket-brigade shuttling needs one pulsed control per hop; a conveyor needs a control count set by the number of phases, not by distance. That is the node's whole economic case, and this brief is its price. Bluhm's group at RWTH Aachen and Forschungszentrum Jülich introduced it as the QuBus: 420 nm channel, four sinusoids, 99.42 ± 0.02% single-electron shuttling — charge, not spin [D][4]. Spin coherence at length followed at Delft [D][1].

Coordinates. **a — affinity:** fully fabricated, an electron in a lithographic ²⁸Si/SiGe well. **b — time:** ~2 × 10⁻⁷ s per 10 µm transit [D][1]; entangling not applicable, this is transport. **c — readout:** none of its own, it borrows the register's charge sensor. **d — mobility:** transport, the node's entire function. **e — control:** no modality or placement of its own, one shared radio-frequency drive. **f — error as the code sees it:** coherent, dephasing and position-dependent rotations, no loss channel. **g — manufacturing:** CMOS, the same 300 mm line as the dots.

## Physics & limits

Gates at 180 nm pitch driven to 300 MHz make a moving confinement minimum; the carrier follows adiabatically at 36 m/s single-tone, 64 m/s two-tone [D][1]. Adiabaticity bounds transit time from below through orbital and valley splittings, spin coherence from above. Spin–orbit coupling and micromagnet gradients make transport a deterministic, position-dependent rotation — coherent, hence calibratable in principle — and motion also helps, Delft attributing the improved coherence of moving spins to motional averaging [D][2]. Charge noise and disorder pin the carrier and excite it at valley–orbit anticrossings [S][19]. Nothing thermodynamic bounds any of this, so the floor is materials: valley-splitting uniformity along a line, and charge noise. Moving it takes interface engineering, quieter gate stacks, echo during transport (in germanium, echo lifted the characteristic shuttle number from 64–77 to above 300 [D][5]) or confinement modulation [S][8]. Surface-code simulation gives a dephasing threshold of several percent and moderate overhead to ~1% error per shuttle [S][6] — forgiving, but conditional on gates and readout already sitting below threshold, which on spins they do not.

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-08 | 420 nm conveyor, four controls, 99.42 ± 0.02% single-electron (charge) shuttling | RWTH Aachen | [D][4] |
| 2024-07-08 | Germanium holes, bucket-brigade: 99.97% per shuttle, basis states only, 312 µm effective | QuTech | [D][5] |
| 2025-06-09 | Conveyor: 10 µm in under 200 ns at 99.54 ± 0.03% spin fidelity | QuTech | [D][1][G:SHUTTLE-DELFT-2025-06] |
| 2026-05-06 | Controlled-phase gate between two *moving* spins: 98.86 ± 0.29%, 240 nm, 58 ns | QuTech | [D][2] |
| 2026-07-29 | Weight-four parity, mobile ancilla: 97.7(1)% per 1.2 µm round trip; Z-parity 72.2(6)% | QuTech | [D][3] |

The dominant error term is counter-intuitive: in the five-qubit parity device the limit is incoherent noise in the exchange interaction, dephasing during shuttling and idling being about a quarter of the total [D][3]. Transport has stopped being the worst thing in a shuttling circuit; the static gates are, and the route past 99% is gate-stack change, not faster conveyors. Typical-at-scale does not exist: every result above is on a research-fab heterostructure, and no conveyor link has been published on a 300 mm device.

## Manufacturing, materials & supply chain

Three overlapping gate layers at ~180 nm pitch over an enriched ²⁸Si/SiGe well, 7 nm thick at Delft [D][1] — nominally 300 mm-compatible, and the node's hard dependency is exactly that: uniform conveyor gates on a CMOS line. Dots need only resemble each other; a bus must be uniform along its whole length, because one pinning defect breaks the channel and a conveyor carries no redundancy. No yield or uniformity statistic has been published for conveyors, conspicuous beside Intel's 24,000-plus spin devices per wafer at 96% tune-up yield [D][16]. Supply: enriched ²⁸Si from a handful of isotope separators, the single point of failure the silicon-spin path already shares, and SiGe epitaxy and overlay at imec, Intel, GlobalFoundries and STMicroelectronics. Cost per bus is not quotable; no ECCN mapping of the quantum dual-use regime is asserted here.

## Control, readout & I/O burden

Four or eight shared radio-frequency lines drive an arbitrarily long bus, so line count scales with the number of buses, not with distance or stops served; a bucket-brigade link of equal reach needs one pulsed line per hop. Sparsity is what makes co-located electronics fit — the argument HRL's 4 K controller makes from the other end at ≤3.5 W and 366 DACs for 18 qubits [D][15][G:HRL-CRYOCMOS-4K-2026]. The node has no readout; a mobile ancilla is measured at a dedicated site [D][3]. Latency is not the binding constraint: 4 ns hops and 58 ns moving-spin gates sit two to three orders below spin readout at 1–100 µs, so shuttling does not lengthen the syndrome cycle. The walls: at 10³ qubits, channel uniformity on 300 mm; at 10⁴, phase calibration across thousands of drifting conveyors; at 10⁶, the dephasing budget — at 10⁻³ per µm, one micron of travel per syndrome extraction is affordable and one hundred is not.

## Role in the stack

The node belongs to the silicon and germanium quantum-dot spin path (Intel, Diraq, Quantum Motion, HRL under IBM, QuTech, Quobly). It requires gate-defined dot spins to move and a 300 mm CMOS foundry for uniform conveyor gates, and provides nothing downstream: its value is realised inside the path it serves, which is why it will never be sold as a product. It replaces static nearest-neighbour exchange, which costs no transport error; a shuttled link buys distance with a dephasing budget and a calibration burden, worth paying only when control and readout electronics must be interleaved among the qubits. Off-diagonal reading: the node sits far from the fabrication cluster it depends on, its physics set by disorder in research heterostructures and its economics by a 300 mm line it has never run on. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: transport contributes 2.0 × 10⁻⁷ s and gates 5.8 × 10⁻⁸ s each, so the path stays readout-limited at 8.5 × 10⁻⁶ s, readout 6.3 µs of it and reset 1 µs. Empty neighbouring slots: transport across a die boundary, and a link with in-flight leakage detection.

## Verification (QCVV)

The silicon figure comes from interleaved randomised benchmarking of a shuttle "gate" over the 10 µm path [D][1]; the germanium figure from exponential fits to a characteristic shuttle number [D][5]. Different observables, routinely quoted side by side: 99.97% per shuttle in germanium is basis-state only, 99.54% in silicon a spin fidelity over a path. Benchmarking a shuttle also assumes twirlability, questionable for a deterministic position-dependent rotation, since motional averaging can flatten the benchmark below the physical error at any single point. Neither protocol reports leakage out of the valley or orbital subspace, and no shuttling result has been cycle- or mirror-benchmarked, so the correlated error a code would see is unmeasured. Conveyor transport is shown at charge level by RWTH Aachen, at spin level by Delft; the 10 µm figure has no independent replication as of 3 Sep 2026.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | research | NL | Every conveyor spin record: 10 µm link, moving-spin gate, mobile ancilla | [D][1][2][3] |
| RWTH Aachen | research | DE | Invented conveyor mode; SpinBus architecture | [D][4][S][6] |
| Forschungszentrum Jülich | research | DE | Conveyor co-parent; hosts ARQUE's first system | [C][7] |
| ARQUE Systems | developer | DE | Sells patented shuttling paths; five-qubit processor | [C][7] |
| IBM | developer | US | Acquired HRL: exchange-only silicon plus 4 K cryo-CMOS | [G][9] |
| Diraq | developer | AU | 300 mm silicon MOS with imec; sparse layouts underpin its cost claim | [D][16] |
| Quantum Motion | developer | UK | 22FDX CMOS, full-stack system at NQCC | [C][12] |
| imec | supplier | BE | 300 mm spin line; would fabricate any foundry conveyor | [D][16] |

**Money.**
- 2022-09 · ARQUE Systems · spin-off founded by Bluhm and three colleagues · undisclosed · Jülich, RWTH Aachen · announced [C][7]
- 2025-11-06 · DARPA QBI Stage B · eleven teams including Diraq, Quantum Motion · up to $15 M each · announced [G][11][G:QBI-STAGEB-2025-11]
- 2026-05-07 · Quantum Motion · Series C · $160 M · DCVC, Kembara · closed [C][12][G:QM-160M-2026-05]
- 2026-05-21 · Diraq · CHIPS letter of intent · up to $38 M · US Commerce · LOI [G][10][G:CHIPS-LOI-2026-05]
- 2026-06-03 · Quobly · Series A · €115 M · Bpifrance, SEALSQ, STMicroelectronics · closed [C][13][G:QUOBLY-115M-2026-06]
- 2026-07-23 · IBM · acquisition of HRL Laboratories · undisclosed · close targeted end Q3 2026 · announced [G][9][G:IBM-HRL-2026-07]

None of these is financing for shuttling as such: it is a feature funded inside spin-qubit companies, not a fundable line item, with ARQUE the sole exception — and its funding undisclosed.

**Market & supply chain.** Nobody sells a shuttle. Enabling supply is 300 mm lithography and overlay, SiGe epitaxy, enriched ²⁸Si substrates and multi-channel waveform generation. G3 and G4 pay for it, since sparsity only earns its dephasing cost at code scale; G7 marginally, through the Jülich installation; G1 and G5 nothing.

**IP & standards.** The conveyor family originates with RWTH Aachen and Forschungszentrum Jülich; ARQUE commercialises a patented shuttling mechanism [C][7]. No dated family count from a named database exists for this node, so none is quoted, and no standards body covers spin transport.

**Roadmaps & track record.** (promised 2021-08 · conveyor as a scalable bus · status 2026-09-03: single-channel level only, never on a foundry wafer). (ARQUE Systems, promised 2026 · five-qubit shuttling processor at Jülich · status: installation under way, no acceptance data [C][7]). (QuTech, promised 2026-07 · above-99% shuttled parity via gate-stack change · status: 97.7% per shuttle [D][3]). (Diraq, promised 2026-08-27 · 150 k physical and 1 k logical qubits by 2029 · status: eight-qubit foundry device with one working pair, its own July release saying "thousands by 2029" [C][G:DIRAQ-FUNDING][G:DIRAQ-8Q-2026-07]). QuTech is the strongest actor here; ARQUE is unproven but the only vehicle with a delivery date; Diraq's numbers move faster than its devices.

**Strategic reading.** If the conveyor reaches foundry uniformity, the winners are the CMOS spin vendors whose thesis is density-through-sparsity — IBM with HRL, Diraq, Quantum Motion, Quobly — and the cryogenic control suppliers, since sparse lattices are what make co-located electronics fit. Losers: dense nearest-neighbour exchange architectures, and foundries selling dot uniformity rather than line uniformity. Bargaining power sits with the 300 mm lines and the enriched-silicon suppliers; a transport primitive with no standalone product will be absorbed as an IP position, which is what the Aachen and Jülich patents already are.

*Open niche:* the opening is the measurement gap. No shuttle has been cycle-benchmarked, and benchmarking a deterministic, position-dependent rotation is a questionable primitive. A small QCVV house could define a position-resolved, leakage-sensitive shuttling benchmark separating calibratable coherent error from stochastic dephasing, plus automated calibration for tens of clavier phases per bus. On the SFQ side, the conveyor drive is four to eight phase-locked sinusoids at a few hundred megahertz per bus — a deterministic, repetitive, low-power waveform of the kind single-flux-quantum generation produces at 4 K and below.

## Outlook & open questions

Falsifiable milestones for 12–24 months. Confirm: a conveyor spin link on a 300 mm foundry device at ≥99% per 10 µm by 2027-09; a shuttled-ancilla parity check above 99%, the target the Delft authors set themselves [D][3]; independent replication by a group other than Delft. Demote: if shuttled-ancilla parity stays below ~90% through 2027, the sparse-architecture argument loses its only experimental leg; or if valley-splitting variation along channels proves irreducible on foundry material. Best case by 2029, a distance-3 to distance-5 surface-code patch on a sparse spin lattice with shuttled syndrome extraction; worst case, shuttling stays a Delft and Aachen speciality on research heterostructures.

Open questions. (1) Is benchmarking of a shuttle a meaningful fidelity, or an artefact of motional averaging? (2) Does motional averaging survive foundry-level charge disorder, or invert into pinning? (3) What is the leakage rate at valley anticrossings? (4) Can conveyor phase calibration be automated across thousands of buses? (5) Can a spin cross a die boundary? Watch: any 300 mm shuttling result from imec, Intel, GlobalFoundries or STMicroelectronics; ARQUE's acceptance data at Jülich; QuTech's follow-up to the weight-four parity device.

## Sources

1. De Smet, M., Matsumoto, Y., Zwerver, A.-M. J. et al. (Vandersypen group, QuTech and Kavli Institute of Nanoscience, TU Delft) · High-fidelity single-spin shuttling in silicon · Nature Nanotechnology 20, 866–872 · 2025-06-09 · https://www.nature.com/articles/s41565-025-01920-5
2. Matsumoto, Y. et al. (Vandersypen group, QuTech, TU Delft) · Two-qubit gate between moving spins · Nature 653 (8114) · 2026-05-06 · https://www.nature.com/articles/s41586-026-10423-9
3. Undseth, B. et al. (Vandersypen group, QuTech, TU Delft) · Weight-four parity checks with a mobile ancilla spin qubit · Nature 655, 1160–1166 · 2026-07-29 · https://www.nature.com/articles/s41586-026-10766-3
4. Seidler, I., Struck, T. et al. (Bluhm group, RWTH Aachen and Forschungszentrum Jülich) · Conveyor-mode single-electron shuttling in Si/SiGe for a scalable quantum computing architecture · arXiv:2108.00879 · 2021-08 · https://arxiv.org/abs/2108.00879
5. van Riggelen-Doelman, F. et al. (Veldhorst group, QuTech, TU Delft) · Coherent spin qubit shuttling through germanium quantum dots · Nature Communications · 2024-07-08 · https://www.nature.com/articles/s41467-024-49358-y
6. Performance of the spin qubit shuttling architecture for a surface code implementation (SpinBus-motivated; author list not captured) · arXiv:2503.10601 · 2025-03 · https://arxiv.org/abs/2503.10601 [S]
7. Forschungszentrum Jülich · Jülich-Aachen start-up paves the way for scalable quantum computers (ARQUE Systems) · press release · 2026 · https://www.fz-juelich.de/en/news/archive/press-release/2026/julich-aachen-start-up-arque-systems [C]
8. Suppressing spin qubit decoherence during shuttling via confinement modulation · arXiv:2605.00611 · 2026-05 · https://arxiv.org/abs/2605.00611 [S] (abstract not retrieved; see open verification)
9. IBM · IBM to acquire HRL Laboratories · newsroom · 2026-07-23 · https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [G]
10. US Department of Commerce and NIST · Letters of intent with nine companies, $2.013 B · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
11. DARPA · Quantum Benchmarking Initiative Stage B selection · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
12. Quantum Motion · $160 M Series C; full-stack CMOS system at NQCC · 2026-05-07 · https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
13. Quobly · €115 M Series A; enriched-silicon FD-SOI lots at ST Crolles · 2026-06-03 · https://www.quobly.io/ [C]
14. Groove Quantum and QuTech · 18-qubit germanium array · arXiv:2604.01063 · 2026-04 · https://arxiv.org/abs/2604.01063
15. HRL Laboratories · Self-sequenced 18-qubit Si/SiGe processor with 4 K cryo-CMOS control · arXiv:2604.16216, Nature 2026-07-29 · https://arxiv.org/abs/2604.16216
16. Diraq and imec · Two-qubit gates on 300 mm foundry silicon-MOS devices · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9
17. Argonne National Laboratory · Silicon quantum processor collaboration with Intel · 2026-01-06 · https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel [P]
18. Equal1 · $60 M round; cryo-CMOS quantum system-on-chip · 2026-01-15 · https://www.equal1.com/ [C]
19. Numerical simulation of coherent spin-shuttling in a QuBus with charged defects · arXiv:2512.03588 · 2025-12 · https://arxiv.org/abs/2512.03588 [S]

## Open verification items

- ARQUE Systems funding: no round, amount or investor disclosed in the Forschungszentrum Jülich release [7]; no company or database page is cited for it. Headcount and a dated installation milestone at Jülich Supercomputing Centre are likewise unverified.
- arXiv:2503.10601 [6]: no author list, institution or date is available for it; the threshold figures quoted come from the abstract text only.
- arXiv:2605.00611 [8]: abstract not machine-readable; cited by title only, no quantitative claim taken from it.
- Export-control classification: no ECCN or category mapping for quantum-computing items and enriched ²⁸Si substrates is established here; no rule number is asserted.
- No published yield, channel-uniformity or per-bus cost data exist for conveyor structures on any 300 mm line as of 2026-09-03 — an absence, not a conflict.
- Source conflict, minor: "99.5%" (abstract) versus "99.54 ± 0.03%" (interleaved randomised benchmarking) in [1] — same measurement; this brief uses 99.54%. Cross-platform: the germanium "99.97% per shuttle" [5] is a basis-state figure, not comparable with the silicon conveyor spin fidelity [1].
