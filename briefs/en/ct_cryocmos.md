---
id: ct_cryocmos
name: Cryo-CMOS controller (4 K / mK)
layer: 5 Control
status: demonstrated
since: 2024
one_line: Commercial CMOS ASICs inside the cryostat that synthesise qubit control waveforms and bias next to the qubits, replacing room-temperature racks and their coaxial lines.
verdict: Proven end-to-end on 18 spin qubits and at room-temperature parity on 156 transmons for flux only; the binding constraint is milliwatts per qubit against a 2 W 4 K plant. Demote if nothing drives >50 qubits end-to-end by end-2027.
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A cryo-CMOS controller is a silicon ASIC on a cold plate in the refrigerator, generating microwave, flux and gate-bias waveforms next to the qubits. Nothing quantum happens in it: the gain is thermal and topological. It became hardware with Horse Ridge (Intel/QuTech, 22 nm FinFET, 4 K, 2019–2020) [C][548] and Gooseberry (Microsoft/Sydney, 100 mK) [D][549].

Attributes (a affinity; b time; c readout; d mobility; e control @ placement; f error structure; g manufacturing):
- a = 1.0, wholly fabricated; a foundry part, not a carrier.
- b = none; it holds no quantum state.
- c = none; it serves the host's readout.
- d = none; fixed to a cold plate.
- e = microwave @ 4 K; placement is the technology.
- f = coherent: amplitude, phase, timing, crosstalk.
- g = CMOS, 130 nm to 14 nm.

Rank 5 of 111; shared by the superconducting and spin architectures.

## Physics & limits

The floor is a heat budget, not a coherence time. Plants are small: 2 W at 4 K (Bluefors XLD1000sl), 24 W (IBM Goldeneye concept), 200 W (Fermilab Colossus) [S][550]. The only power attached to a working two-qubit gate is IBM's 23 mW per qubit [D][296]; the same review's optimistic case is 5 mW, its lowest demonstrations under 2 mW [S][550]. A 2 W plant thus holds ~87 qubits at 23 mW, ~1,000 at 2 mW.

At millikelvin the regime changes kind: baseband, duty-cycled cells that hold a gate voltage and refresh it — 18 nW per cell for 100 mV pulses at 100 mK [D][549], ~20 nW MHz⁻¹ per cell at 7 mK [D][551].

Failure is coherent: drift and quantisation become rotation-angle error — a Delft converter drifted 60 µV/s to 18 mV/s [C][552] — jitter becomes over-rotation, finite isolation crosstalk. The stochastic channel is back-action, worth 0.07% of single-qubit fidelity [D][551]. The floor moves with a cold-characterised process [C][553] or superconducting logic at ~1.6 µW/qubit [S][550].

## Engineering state of the art

Best demonstrated: HRL's 130 nm RF CMOS controller at 4 K — ≤3.5 W, 366 DACs, a 250 MHz sequencer — driving 54 dots as 18 exchange-only qubits at mean single-qubit error 2×10⁻⁴ and mean CNOT 3×10⁻³ (best reproducible 9×10⁻⁴), closing a distance-5 repetition code at 5.0×10⁻³ over 200 rounds, Λ₅/₃ = 4.7, with nothing warm in the loop [D][190] [G:HRL-2026]. IBM ran 14 nm flux-bias ASICs on a 156-qubit Heron R2 at median two-qubit error ≈2.3×10⁻³, parity with warm electronics on the same processor [C][527]. Typical at scale: none — everything else above ~10 qubits runs from warm racks [D][G:SEEQC-2026].

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2021-01-25 | 100 mK, 18 nW/cell, 100 mV pulses | Microsoft | [D] | [549] |
| 2024-02-14 | Gate from 4 K: 23 mW/qubit, 1Q 8×10⁻⁴ | IBM | [D] | [296] |
| 2025-06-25 | 7 mK, ~20 nW MHz⁻¹/cell, 0.07% fidelity cost | Sydney | [D] | [551] |
| 2026-03-16 | Flux ASICs, 156 qubits, median 2Q 2.3×10⁻³ | IBM | [C] | [527] |
| 2026-07-29 | ≤3.5 W, 366 DACs, 18 qubits, Λ₅/₃ = 4.7 | HRL | [D] | [190] |

Dominant term: channel-to-channel non-uniformity — mean CNOT 3×10⁻³ against best reproducible 9×10⁻⁴, ~80% of it extrinsic, from control and calibration [D][190].

## Manufacturing, materials & supply chain

No exotic process; the difficulty is a commercial node run 300 K outside its qualified range: 130 nm RF CMOS (HRL) [D][190], 14 nm FinFET (IBM) [D][296], 22 nm FinFET (Horse Ridge, Delft converters) [C][548], [552], 28 nm FD-SOI (Gooseberry, Sydney) [D][549], [551], 22FDX (Equal1) [C][273]. The scarce input is the model, not the wafer: design kits stop at −40 °C, so actors keep private cryogenic models or buy a cryo-optimised process — SemiQon quotes 0.32 mV/dec subthreshold swing at 420 mK against ~60 mV/dec at 300 K [C][553]. Yield and cost per channel are unpublished. Concentration sits in foundries willing to run unqualified corners and in dilution refrigerators [C][G:BLUEFORS-KIDE]. Export exposure is direct: the BIS rule of 2024-09-06 created ECCN 3A901.a for CMOS circuits "designed to operate at an ambient temperature equal to or less (better) than 4.5 K", catching this node by design intent rather than performance, beside controls on refrigerators and cryogenic probers [G][301] [G:BIS-QUANTUM-2024]. The controlled item can therefore be a design file.

## Control, readout & I/O burden

HRL removed warm waveform generation, but the cable count did not fall: 296 lines for 18 qubits, ~16 each — the win was the rack, not the wiring [D][190]. The wiring win is a millikelvin one, where demultiplexing turns N terminals into ~log N inputs: Pando Tree's 64 terminals at 10–20 mK [C][272], Delft's 648 devices from 96 voltages under 120 µW [C][552]. Latency is the second argument: 200 code rounds closed with nothing warm in the loop [D][190], against 3.84 µs mean round trip on a warm GPU link [G:NVQLINK-2025]. The walls follow the heat budget: 10³ qubits needs the sub-2 mW class on a 2 W plant; 10⁴ needs Goldeneye- or Colossus-class cooling at ≤5 mW/qubit; 10⁶ means ~90 modules of 10,000 qubits dissipating 50 W each at 4 K — outside anything sold in 2026 [S][550].

## Role in the stack

Two architectures: superconducting transmons (IBM, Google, IQM) and silicon or germanium quantum-dot spins (Intel, Diraq, Quantum Motion, HRL, Quobly, Equal1). It requires a 300 mm CMOS foundry — a dependency spins already carry, so they get cryo-CMOS as a by-product while superconducting vendors fund it separately. It provides the cold digital substrate a cryogenic decoder needs: a 4 K predecoder costed under 0.56 mW for 3,780× syndrome-bandwidth reduction [S][G:PINBALL-2025-12]. It replaces room-temperature control, the only part of this layer with revenue, and competes with single-flux-quantum control, published above 99% at millikelvin [D][G:SEEQC-2026]; switching buys cold silicon on an 18–24-month tape-out loop, paid for in cooling budget that would otherwise buy qubits. The node is a non-quantum object whose only distinguishing attribute is placement at 4 K. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset; this node does not bind it — 4.0 ns sequencer granularity [D][190] against a 0.65 µs round whose largest term is 282 ns of readout. Empty slots next door: a cryogenic readout digitiser and a standard cold digital interface.

## Evidence — how the numbers were measured

Every headline number is measured through the qubit, never on the controller: interleaved randomised benchmarking, whose 1.71 and 17.51 instructions per Clifford (single- and two-qubit) must accompany any comparison [D][296]; repetition-code Λ scaling across distances 3 and 5 for HRL [D][190]; and, for IBM's 2026 flux result, an A/B comparison against warm electronics on the same processor — the right design, and the rarest.

Randomised benchmarking averages over Cliffords and is blind to slow coherent drift, so converter drift [C][552] appears in no RB number; back-action, duty-cycle transients, channel non-uniformity and cold reliability need bespoke measurements [D][551]. Replication is reasonable at 4 K (IBM, HRL) and at millikelvin (Microsoft, Sydney, Delft, QuTech [C][554]).

Conflicts: IBM's 23 mW per qubit [D][296] against 5 mW and under 2 mW [S][550] are different quantities — active versus idle, drive-only versus full chain — with no common definition; 23 mW is used here as the only figure tied to a working gate. Equal1's fidelity figures are product-page claims [C][273] against a published six-qubit device at 0.3 K [G:EQUAL1-60M-2026-01].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with it | Evidence |
|---|---|---|---|---|
| HRL Laboratories | developer | US | 4 K controller sequencing 18 qubits | [D][190] [G:HRL-2026] |
| IBM Quantum | developer | US | 14 nm flux ASICs; acquired HRL | [D][296] [C][10], [527] [G:IBM-HRL-CLOSED-2026-08] |
| Intel | developer | US | Horse Ridge, Pando Tree | [C][272] [G:INTEL-2026] |
| Microsoft | research | US | Gooseberry at 100 mK; charge-lock patent | [D][549] [G][555] |
| University of Sydney | research | AU | mK CMOS driving Diraq spins | [D][551] |
| Equal1 | developer | IE | Qubits and control on one die | [C][273] [G:EQUAL1-60M-2026-01] |
| Quantum Machines | supplier | IL | Warm racks this node displaces | [C][528] |

**Money.**
- 2025-02-25 · Quantum Machines · Series C · $170 M · PSG Equity · $280 M cumulative [C][528]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each · eleven teams incl. IBM, Diraq [G:QBI-STAGEB-2025-11]
- 2026-05-21 · GlobalFoundries; Diraq · CHIPS letters of intent · $375 M; $38 M · LOI [G:CHIPS-LOI-2026-05]
- 2026-06-29 · SEEQC · S-1 for Nasdaq beside an Allegro merger · $1 B enterprise value, $65 M PIPE [C][556] [P][557]; SPAC merger terminated 2026-08-25, S-1 continues, IPO unpriced as of 30 Sep 2026 [G:SEEQC-SPAC-TERMINATED-2026-08]
- 2026-07-23 · IBM · acquires HRL Laboratories · undisclosed · closed 2026-08-26 [C][10] [G:IBM-HRL-2026-07][G:IBM-HRL-CLOSED-2026-08]

**Market & supply chain.** Nobody sells a cryo-CMOS controller as of 3 Sep 2026; the layer's revenue is warm racks from Quantum Machines, Zurich Instruments, Keysight and QBLOX, and Quantum Machines alone has raised $280 M [C][528], [558]. Cryo-CMOS itself is captive R&D; merchant offers are pre-revenue: SemiQon, FrostByte (€1.3 M) and Rhonexum ($1 M) [C][553], [559] [P][560]. G3, G4 and G7 pay for it; G1, G2 and G5 do not.

**IP & standards.** Microsoft Technology Licensing holds US 11,838,022 on the cryogenic-CMOS qubit interface (granted 2023-12-05), the charge-lock architecture behind Gooseberry [G][555]; MIT holds US 12,705,525 on baseband pulsing (2026-08-11) [G][561]; Intel's closed-loop calibration filing is an application only [G][562]. No database publishes a dated family count [P][563]. Standards: none, and no agreed power-per-qubit definition.

**Roadmaps & track record.**
- Intel: 2020-12-03 · Horse Ridge II for scaled spin systems · no successor [G:INTEL-2026].
- Microsoft: 2021-01-27 · Gooseberry to "thousands of qubits" · not delivered [C][564].
- IBM: 2024-02-14 · cryo-CMOS as the route to scalable control · partly delivered, flux only [D][296] [C][527].
- HRL: 2026-04-17 · a processor with no warm waveform generators · delivered [D][190].
Credibility: HRL alone named a dated deliverable and shipped it, and IBM bought it; IBM publishes A/B comparisons, not headline claims; Intel has no peer-reviewed fidelity on a Horse Ridge part; Microsoft's line is five years dormant.

**Strategic reading.** Winners if cold control becomes standard: integrated CMOS houses — IBM with HRL, Intel if it re-engages — and spin companies whose qubits and controllers share a line. Losers: warm-rack vendors, protected only while nobody below a thousand qubits needs an ASIC. The other cold route, SFQ control, is projected to draw less power per qubit [S][550] and has no two-qubit gate yet; its developer, SEEQC, has filed for a Nasdaq listing, offering size undisclosed [P][557]. Bargaining power stays with platform vendors; the scarce supplier is the refrigerator maker.

## Outlook & open questions

Confirm within 12–24 months if IBM publishes a peer-reviewed full chain — drive, flux and readout — on ≥100 superconducting qubits at warm-rack parity; if the HRL controller reappears inside IBM above 18 qubits; if anyone reports a defined power per qubit below 5 mW at 4 K under load. Demote if by end-2027 nothing drives more than about fifty qubits end-to-end in a peer-reviewed result and Heron-class systems still ship warm racks. Best case by 2029: cold control standard on spin machines and IBM's flux path, a 10,000-qubit module on one 4 K plant at ≤5 mW/qubit. Worst case: the budget stays binding, superconducting machines keep warm racks, and cryo-CMOS survives only as millikelvin biasing for spins.

Open questions: (1) a defensible power-per-qubit definition? (2) will a foundry qualify a cryogenic corner? (3) does controller drift dominate below 10⁻⁴ qubit error? (4) must per-qubit power fall, or can the plant grow tenfold? (5) will IBM keep HRL's 130 nm design? Watch ISSCC 2027, IBM's post-acquisition disclosures, and any 4 K plant marketed above 20 W.

## References
[10] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [C]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[272] S. Subramanian and S. Pellerano, “Intel's Millikelvin Quantum Research Control Chip Provides Denser Integration with Qubits,” Intel Community, Jun. 20, 2024. [Online]. Available: https://community.intel.com/t5/Blogs/Tech-Innovation/Data-Center/Intel-s-Millikelvin-Quantum-Research-Control-Chip-Provides/post/1608558 [C]
[273] Equal1, “UnityQ.” [Online]. Available: https://www.equal1.com/technology [C]
[296] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[528] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[548] Intel Corporation, “Intel Debuts 2nd-Gen Horse Ridge Cryogenic Quantum Control Chip,” Dec. 3, 2020. [Online]. Available: https://www.intc.com/news-events/press-releases/detail/1429/intel-debuts-2nd-gen-horse-ridge-cryogenic-quantum-control [C]
[549] S. J. Pauka *et al.*, “A cryogenic CMOS chip for generating control signals for multiple qubits,” *Nat. Electron.*, vol. 4, no. 1, pp. 64–70, Jan. 2021, doi: [10.1038/s41928-020-00528-y](https://doi.org/10.1038/s41928-020-00528-y). [D]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[551] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[552] J. van Staveren *et al.*, “Cryo-CMOS Bias-Voltage Generation and Demultiplexing at mK Temperatures for Large-Scale Arrays of Quantum Devices,” *IEEE Trans. Quantum Eng.*, vol. 6, pp. 1–18, 2025, doi: [10.1109/TQE.2025.3580377](https://doi.org/10.1109/TQE.2025.3580377). [C]
[553] SemiQon, “SemiQon Cryo-CMOS™.” [Online]. Available: https://www.semiqon.com/technology/semiqon-cryo-cmos [C]
[554] QuTech, “Scalable diamond Quantum Computing with cryogenic chip integration,” Feb. 17, 2026. [Online]. Available: https://qutech.nl/2026/02/17/scalable-diamond-quantum-computing-with-cryogenic-chip-integration/ [C]
[555] Microsoft Technology Licensing, LLC, “Cryogenic-CMOS interface for controlling qubits,” USPTO, Dec. 2023. [Online]. Available: https://patents.justia.com/patent/11838022 [G]
[556] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [C]
[557] M. Abdel-Kareem, “SEEQC Files Form S-1 for Nasdaq IPO Parallel to Ongoing Allegro Merger Process,” Quantum Computing Report, Jul. 2, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-files-form-s-1-for-nasdaq-ipo-parallel-to-ongoing-allegro-merger-process/ [P]
[558] Quantum Machines, “Quantum Machines Makes Second European Acquisition in Six Weeks as Quantum Closes In on Real-World Advantage,” Jun. 17, 2026. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-acquisition-pcb-engineering/ [C]
[559] QuTech, “QuTech spinoff FrostByte raises €1.3 million for cryo-electronics for scalable quantum computers,” May 11, 2026. [Online]. Available: https://qutech.nl/2026/05/11/qutech-spinoff-frostbyte-raises-e1-3-million-for-cryo-electronics-for-scalable-quantum-computers/ [C]
[560] M. Abdel-Kareem, “Rhonexum Raises $1M Pre-Seed to Solve the Quantum Cabling Bottleneck via Cryo-CMOS,” Quantum Computing Report, Mar. 18, 2026. [Online]. Available: https://quantumcomputingreport.com/rhonexum-raises-1m-pre-seed-to-solve-the-quantum-cabling-bottleneck-via-cryo-cmos/ [P]
[561] W. D. Oliver and S. Gustavsson, “Scalable control of quantum bits using baseband pulsing,” USPTO, Aug. 2026. [Online]. Available: https://patents.justia.com/patent/12705525 [G]
[562] Intel Corporation, “Technologies for Closed-Loop Qubit Calibration,” USPTO, Jul. 2026. [Online]. Available: https://patents.justia.com/patent/20260187510 [G]
[563] PatSnap, “Cryogenic CMOS Circuit Technology Landscape 2026,” Apr. 20, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/articles/cryo-cmos-technology-landscape-2026/ [P]
[564] C. Nayak, “Full stack ahead: Pioneering quantum hardware allows for controlling up to thousands of qubits at cryogenic temperatures,” Microsoft Research Blog, Jan. 27, 2021. [Online]. Available: https://www.microsoft.com/en-us/research/blog/full-stack-ahead-pioneering-quantum-hardware-allows-for-controlling-up-to-thousands-of-qubits-at-cryogenic-temperatures/ [C]

## Open verification items

- Power per qubit at 4 K: IBM's measured 23 mW under active control [D][296] against "optimistic 5 mW" and "below 2 mW" in the resource review [S][550]; definitions differ (active vs idle, drive-only vs full chain) and none is published. 23 mW used.
- Gooseberry's 18 nW per cell [D][549] and the Sydney chip's ~20 nW MHz⁻¹ per cell [D][551] are quoted interchangeably in secondary sources; different quantities, not reconciled.
- Cooling powers for the Bluefors XLD1000sl, IBM Goldeneye and Fermilab Colossus come from the resource review [S][550]; the Bluefors XLD product page returned HTTP 404 on 2026-09-03 and the primary specification is unconfirmed.
- IBM's 2026 cryo-CMOS flux result exists only as conference abstracts [C][527]; no preprint or paper as of 2026-09-03, and the 14 nm FinFET attribution rests on the abstract text. IBM's modular-cryogenics blog (2026-08) gives cell wiring area and vacuum volume but no cooling power at 4 K.
- Equal1's 99.9% / 99.3% / 99% fidelities and "35 monolithic quantum cells" are product-page claims [C][273] with no paper or dated release.
- SemiQon's process node, fab location and the size of its 2026-07 PostScriptum investment are undisclosed.
- SEEQC's revenue and cash appear in its S-1 filings, not in the filing announcement or the trade-press summary [C][556] [P][557]: $4.2 M revenue in 2025 and $18.1 M cash at 2026-06-30 (S-1 amendment of 2026-08-28) [G:SEEQC-S1A-2026-08]; the offering size is still blank, and the $1 B enterprise value and $65 M PIPE describe the terminated Allegro merger.
- Quantum Machines' revenue is undisclosed and its ">50% of companies developing quantum computers" customer share is a company claim [C][528]; Zurich Instruments, Keysight and QBLOX publish nothing comparable, so the warm-control market this node would displace cannot be sized.
- The QuTech/Fujitsu diamond cryo-CMOS ISSCC 2026 paper's power, channel count and process node were not obtainable; only the institutional release [C][554].
- Cryo-CMOS patent-family counts: no named database publishes a dated count; PatSnap gives only regional "key result" tallies with a completeness disclaimer [P][563].
- HRL's controller cost, tape-out schedule and whether IBM retains the 130 nm design are unstated in the acquisition release [C][10]; the acquisition closed on 2026-08-26 [G:IBM-HRL-CLOSED-2026-08].
