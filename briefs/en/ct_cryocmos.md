---
id: ct_cryocmos
name: Cryo-CMOS controller (4 K / mK)
layer: 5 Control
status: demonstrated
since: 2024
one_line: Commercial CMOS ASICs inside the cryostat that synthesise qubit control waveforms and bias next to the qubits, replacing room-temperature racks and their coaxial lines.
verdict: Proven end-to-end on 18 spin qubits and at room-temperature parity on 156 transmons for flux only; the binding constraint is milliwatts per qubit against a 2 W 4 K plant. Demote if nothing drives >50 qubits end-to-end by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A cryo-CMOS controller is a silicon ASIC on a cold plate in the refrigerator, generating microwave, flux and gate-bias waveforms next to the qubits. Nothing quantum happens in it: the gain is thermal and topological. It became hardware with Horse Ridge (Intel/QuTech, 22 nm FinFET, 4 K, 2019–2020) [C][8] and Gooseberry (Microsoft/Sydney, 100 mK) [D][4].

Coordinates (a affinity; b time; c readout; d mobility; e control @ placement; f error structure; g manufacturing):
- a = 1.0, wholly fabricated; a foundry part, not a carrier.
- b = none; it holds no quantum state.
- c = none; it serves the host's readout.
- d = none; fixed to a cold plate.
- e = microwave @ 4 K; placement is the technology.
- f = coherent: amplitude, phase, timing, crosstalk.
- g = CMOS, 130 nm to 14 nm.

Rank 5 of 96; a hub reaching superconducting and spin paths.

## Physics & limits

The floor is a heat budget, not a coherence time. Plants are small: 2 W at 4 K (Bluefors XLD1000sl), 24 W (IBM Goldeneye concept), 200 W (Fermilab Colossus) [S][6]. The only power attached to a working two-qubit gate is IBM's 23 mW per qubit [D][2]; the same review's optimistic case is 5 mW, its lowest demonstrations under 2 mW [S][6]. A 2 W plant thus holds ~87 qubits at 23 mW, ~1,000 at 2 mW.

At millikelvin the regime changes kind: baseband, duty-cycled cells that hold a gate voltage and refresh it — 18 nW per cell for 100 mV pulses at 100 mK [D][4], ~20 nW MHz⁻¹ per cell at 7 mK [D][3].

Failure is coherent: drift and quantisation become rotation-angle error — a Delft converter drifted 60 µV/s to 18 mV/s [C][7] — jitter becomes over-rotation, finite isolation crosstalk. The stochastic channel is back-action, worth 0.07% of single-qubit fidelity [D][3]. The floor moves with a cold-characterised process [C][12] or superconducting logic at ~1.6 µW/qubit [S][6].

## Engineering state of the art

Best demonstrated: HRL's 130 nm RF CMOS controller at 4 K — ≤3.5 W, 366 DACs, a 250 MHz sequencer — driving 54 dots as 18 exchange-only qubits at mean single-qubit error 2×10⁻⁴ and mean CNOT 3×10⁻³ (best reproducible 9×10⁻⁴), closing a distance-5 repetition code at 5.0×10⁻³ over 200 rounds, Λ₅/₃ = 4.7, with nothing warm in the loop [D][1] [G:HRL-2026]. IBM ran 14 nm flux-bias ASICs on a 156-qubit Heron R2 at median two-qubit error ≈2.3×10⁻³, parity with warm electronics on the same processor [C][5]. Typical at scale: none — everything above ~10 qubits runs from warm racks [D][G:SEEQC-2026].

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2021-01-25 | 100 mK, 18 nW/cell, 100 mV pulses | Microsoft | [D] | [4] |
| 2024-02-14 | Gate from 4 K: 23 mW/qubit, 1Q 8×10⁻⁴ | IBM | [D] | [2] |
| 2025-06-25 | 7 mK, ~20 nW MHz⁻¹/cell, 0.07% fidelity cost | Sydney | [D] | [3] |
| 2026-03-16 | Flux ASICs, 156 qubits, median 2Q 2.3×10⁻³ | IBM | [C] | [5] |
| 2026-07-29 | ≤3.5 W, 366 DACs, 18 qubits, Λ₅/₃ = 4.7 | HRL | [D] | [1] |

Dominant term: channel-to-channel non-uniformity — mean CNOT 3×10⁻³ against best reproducible 9×10⁻⁴, ~80% of it extrinsic, from control and calibration [D][1].

## Manufacturing, materials & supply chain

No exotic process; the difficulty is a commercial node run 300 K outside its qualified range: 130 nm RF CMOS (HRL) [D][1], 14 nm FinFET (IBM) [D][2], 22 nm FinFET (Horse Ridge, Delft converters) [C][8][7], 28 nm FDSOI (Gooseberry, Sydney) [D][4][3], 22FDX (Equal1) [C][15]. The scarce input is the model, not the wafer: design kits stop at −40 °C, so actors keep private cryogenic models or buy a cryo-optimised process — SemiQon quotes 0.32 mV/dec subthreshold swing at 420 mK against ~60 mV/dec at 300 K [C][12]. Yield and cost per channel are unpublished. Concentration sits in foundries willing to run unqualified corners and in dilution refrigerators [C][G:BLUEFORS-KIDE]. Export exposure is direct: the BIS rule of 2024-09-06 created ECCN 3A901.a for CMOS circuits "designed to operate at an ambient temperature equal to or less (better) than 4.5 K", catching this node by design intent rather than performance, beside controls on refrigerators and cryogenic probers [G][11] [G:BIS-QUANTUM-2024]. The controlled item can therefore be a design file.

## Control, readout & I/O burden

HRL removed warm waveform generation, but the cable count did not fall: 296 lines for 18 qubits, ~16 each — the win was the rack, not the wiring [D][1]. The wiring win is a millikelvin one, where demultiplexing turns N terminals into ~log N inputs: Pando Tree's 64 terminals at 10–20 mK [C][9], Delft's 648 devices from 96 voltages under 120 µW [C][7]. Latency is the second argument: 200 code rounds closed with nothing warm in the loop [D][1], against 3.84 µs mean round trip on a warm GPU link [G:NVQLINK-2025]. The walls follow the heat budget: 10³ qubits needs the sub-2 mW class on a 2 W plant; 10⁴ needs Goldeneye- or Colossus-class cooling at ≤5 mW/qubit; 10⁶ means ~90 modules of 10,000 qubits dissipating 50 W each at 4 K — outside anything sold in 2026 [S][6].

## Role in the stack

Two paths: superconducting transmons (IBM, Google, IQM) and silicon or germanium quantum-dot spins (Intel, Diraq, Quantum Motion, HRL, Quobly, Equal1). It requires a 300 mm CMOS foundry — a dependency spins already carry, so they get cryo-CMOS as a by-product while superconducting vendors fund it separately. It provides the cold digital substrate a cryogenic decoder needs: a 4 K predecoder costed under 0.56 mW for 3,780× syndrome-bandwidth reduction [S][G:PINBALL-2025-12]. It replaces room-temperature control, the only part of this layer with revenue, and competes with single-flux-quantum control, published above 99% at millikelvin [D][G:SEEQC-2026]; switching buys cold silicon on an 18–24-month tape-out loop, paid for in cooling budget that would otherwise buy qubits. The off-diagonal reading is the cold-fabrication corner: a non-quantum object whose only distinguishing coordinate is placement at 4 K. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset; this node does not bind it — 4.0 ns sequencer granularity [D][1] against a 0.65 µs round whose largest term is 282 ns of readout. Empty slots next door: a cryogenic readout digitiser and a standard cold digital interface.

## Verification (QCVV)

Every headline number is measured through the qubit, never on the controller: interleaved randomized benchmarking, whose 1.71 and 17.51 instructions per Clifford (single- and two-qubit) must accompany any comparison [D][2]; repetition-code Λ scaling across distances 3 and 5 for HRL [D][1]; and, for IBM's 2026 flux result, an A/B comparison against warm electronics on the same processor — the right design, and the rarest.

Randomized benchmarking averages over Cliffords and is blind to slow coherent drift, so converter drift [C][7] appears in no RB number; back-action, duty-cycle transients, channel non-uniformity and cold reliability need bespoke measurements [D][3]. Replication is reasonable at 4 K (IBM, HRL) and at millikelvin (Microsoft, Sydney, Delft, QuTech [C][25]).

Conflicts: IBM's 23 mW per qubit [D][2] against 5 mW and under 2 mW [S][6] are different quantities — active versus idle, drive-only versus full chain — with no common definition; 23 mW is used here as the only figure tied to a working gate. Equal1's fidelity figures are product-page claims [C][15] against a published six-qubit device at 0.3 K [G:EQUAL1-60M-2026-01].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with it | Evidence |
|---|---|---|---|---|
| HRL Laboratories | developer | US | 4 K controller sequencing 18 qubits | [D][1] [G:HRL-2026] |
| IBM Quantum | developer | US | 14 nm flux ASICs; buying HRL | [D][2] [C][5][16] |
| Intel | developer | US | Horse Ridge, Pando Tree | [C][9] [G:INTEL-2026] |
| Microsoft | research | US | Gooseberry at 100 mK; charge-lock patent | [D][4] [G][17] |
| University of Sydney | research | AU | mK CMOS driving Diraq spins | [D][3] |
| Equal1 | developer | IE | Qubits and control on one die | [C][15] [G:EQUAL1-60M-2026-01] |
| Quantum Machines | supplier | IL | Warm racks this node displaces | [C][21] |

**Money.**
- 2025-02-25 · Quantum Machines · Series C · $170 M · PSG Equity · $280 M cumulative [C][21]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each · eleven teams incl. IBM, Diraq [G:QBI-STAGEB-2025-11]
- 2026-05-21 · GlobalFoundries; Diraq · CHIPS letters of intent · $375 M; $38 M · LOI [G:CHIPS-LOI-2026-05]
- 2026-07-02 · SEEQC · S-1 for Nasdaq beside an Allegro merger · $1 B enterprise value, $65 M PIPE [C][23] [P][24]; SPAC merger terminated 2026-08-25, S-1 continues [G:SEEQC-SPAC-TERMINATED-2026-08]
- 2026-07-23 · IBM · acquires HRL Laboratories · undisclosed · closing end Q3 2026 [C][16] [G:IBM-HRL-2026-07]

**Market & supply chain.** Nobody sells a cryo-CMOS controller as of 3 Sep 2026; the layer's revenue is warm racks from Quantum Machines, Zurich Instruments, Keysight and QBLOX, and Quantum Machines alone has raised $280 M [C][21][22]. Cryo-CMOS itself is captive R&D; merchant offers are pre-revenue: SemiQon, FrostByte (€1.3 M) and Rhonexum ($1 M) [C][12][13] [P][14]. G3, G4 and G7 pay for it; G1, G2 and G5 do not.

**IP & standards.** Microsoft Technology Licensing holds US 11,838,022 on the cryogenic-CMOS qubit interface (granted 2023-12-05), the charge-lock architecture behind Gooseberry [G][17]; MIT holds US 12,705,525 on baseband pulsing (2026-08-11) [G][18]; Intel's closed-loop calibration filing is an application only [G][19]. No database publishes a dated family count [P][20]. Standards: none, and no agreed power-per-qubit definition.

**Roadmaps & track record.**
- Intel: 2020-12-03 · Horse Ridge II for scaled spin systems · no successor [G:INTEL-2026].
- Microsoft: 2021-01-27 · Gooseberry to "thousands of qubits" · not delivered [C][10].
- IBM: 2024-02-14 · cryo-CMOS as the route to scalable control · partly delivered, flux only [D][2] [C][5].
- HRL: 2026-04-17 · a processor with no warm waveform generators · delivered [D][1].
Credibility: HRL alone named a dated deliverable and shipped it, and IBM bought it; IBM publishes A/B comparisons, not headline claims; Intel has no peer-reviewed fidelity on a Horse Ridge part; Microsoft's line is five years dormant.

**Strategic reading.** Winners if cold control becomes standard: integrated CMOS houses — IBM with HRL, Intel if it re-engages — and spin companies whose qubits and controllers share a line. Losers: warm-rack vendors, protected only while nobody below a thousand qubits needs an ASIC. The substitution threat is single-flux-quantum control, three orders cheaper per qubit [S][6] and now financing itself publicly at $1 B [P][24]. Bargaining power stays with platform vendors; the scarce supplier is the refrigerator maker.

*Open niche:* the missing instrument is controller-side QCVV. Every number above is measured through the qubit, so no protocol separates the controller's drift from the qubit's own; a small QCVV/SFQ company could sell cold-controller characterisation — converter drift, channel amplitude and phase non-uniformity, back-action heating against duty cycle, and the controller's share of the error budget.

## Outlook & open questions

Confirm within 12–24 months if IBM publishes a peer-reviewed full chain — drive, flux and readout — on ≥100 superconducting qubits at warm-rack parity; if the HRL controller reappears inside IBM above 18 qubits; if anyone reports a defined power per qubit below 5 mW at 4 K under load. Demote if by end-2027 nothing drives more than about fifty qubits end-to-end in a peer-reviewed result and Heron-class systems still ship warm racks. Best case by 2029: cold control standard on spin machines and IBM's flux path, a 10,000-qubit module on one 4 K plant at ≤5 mW/qubit. Worst case: the budget stays binding, single-flux-quantum logic takes the superconducting path, and cryo-CMOS survives only as millikelvin biasing for spins.

Open questions: (1) a defensible power-per-qubit definition? (2) will a foundry qualify a cryogenic corner? (3) does controller drift dominate below 10⁻⁴ qubit error? (4) must per-qubit power fall, or can the plant grow tenfold? (5) will IBM keep HRL's 130 nm design? Watch ISSCC 2027, IBM's post-acquisition disclosures, and any 4 K plant marketed above 20 W.

## Sources

[1] Ziegler, A. et al. (HRL Laboratories) · A digitally controlled silicon quantum processing unit · arXiv:2604.16216; Nature (2026-07-29) · 2026-04-17 · https://arxiv.org/abs/2604.16216
[2] Underwood, D. et al. (IBM Quantum) · Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate · PRX Quantum 5, 010326 · 2024-02-14 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326
[3] Bartee, S. K. et al. (Univ. of Sydney, Diraq, UNSW, Keio) · Spin-qubit control with a milli-kelvin CMOS chip · Nature 643 (8071) · 2025-06-25 · https://www.nature.com/articles/s41586-025-09157-x
[4] Pauka, S. J. et al. (Microsoft Quantum Sydney, Purdue) · A cryogenic CMOS chip for generating control signals for multiple qubits · Nature Electronics 4, 64–70 · 2021-01-25 · https://www.nature.com/articles/s41928-020-00528-y
[5] [C] Noori, A. et al. (IBM) · A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2 · APS Global Physics Summit 2026 abstract · 2026-03-16 · https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2
[6] Kawabata, S. (Hosei University) · Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers · arXiv:2601.03922 · 2026-01-08 · https://arxiv.org/abs/2601.03922
[7] [C] Bluefors with TU Delft (Sebastiano et al.) · Researchers Develop Millikelvin Cryo-CMOS System for Large-Scale Quantum Devices — IEEE Transactions on Quantum Engineering, DOI 10.1109/TQE.2025.3580377 · 2025-07-09 · https://bluefors.com/news/researchers-develop-millikelvin-cryo-cmos-system-for-large-scale-quantum-devices/
[8] [C] Intel Corporation · Intel Debuts 2nd-Gen Horse Ridge Cryogenic Quantum Control Chip · press release · 2020-12-03 · https://www.intc.com/news-events/press-releases/detail/1429/intel-debuts-2nd-gen-horse-ridge-cryogenic-quantum-control
[9] [C] Intel Corporation · Intel's Millikelvin Quantum Research Control Chip Provides Denser Integration with Qubits (Pando Tree) · Intel blog · 2024-06-20 · https://community.intel.com/t5/Blogs/Tech-Innovation/Data-Center/Intel-s-Millikelvin-Quantum-Research-Control-Chip-Provides/post/1608558
[10] [C] Microsoft Research · Full stack ahead: Pioneering quantum hardware allows for controlling up to thousands of qubits at cryogenic temperatures · 2021-01-27 · https://www.microsoft.com/en-us/research/blog/full-stack-ahead-pioneering-quantum-hardware-allows-for-controlling-up-to-thousands-of-qubits-at-cryogenic-temperatures/
[11] [G] US Bureau of Industry and Security · Commerce Control List Additions and Revisions: Implementation of Controls on Advanced Technologies (ECCN 3A901, 3A904, 3B904, 4A906) · Federal Register 2024-19633 · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[12] [C] SemiQon · SemiQon Cryo-CMOS · company technology page, accessed 2026-09-03 · https://www.semiqon.com/technology/semiqon-cryo-cmos
[13] [C] QuTech · QuTech spinoff FrostByte raises €1.3 million for cryo-electronics for scalable quantum computers · 2026-05-11 · https://qutech.nl/2026/05/11/qutech-spinoff-frostbyte-raises-e1-3-million-for-cryo-electronics-for-scalable-quantum-computers/
[14] [P] Quantum Computing Report · Rhonexum Raises $1M Pre-Seed to Solve the Quantum Cabling Bottleneck via Cryo-CMOS · trade press · 2026-03-18 · https://quantumcomputingreport.com/rhonexum-raises-1m-pre-seed-to-solve-the-quantum-cabling-bottleneck-via-cryo-cmos/
[15] [C] Equal1 · UnityQ technology page · company website, accessed 2026-09-03 · https://www.equal1.com/technology
[16] [C] IBM · IBM to acquire HRL Laboratories to power the future of quantum · newsroom · 2026-07-23 · https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum
[17] [G] USPTO (via Justia Patents) · US 11,838,022, Cryogenic-CMOS interface for controlling qubits, Microsoft Technology Licensing LLC (Das, Moini, Reilly), filed 2019-12-05 · granted 2023-12-05 · https://patents.justia.com/patent/11838022
[18] [G] USPTO (via Justia Patents) · US 12,705,525, Scalable control of quantum bits using baseband pulsing, Massachusetts Institute of Technology (Oliver, Gustavsson), filed 2023-02-08 · granted 2026-08-11 · https://patents.justia.com/patent/12705525
[19] [G] USPTO (via Justia Patents) · US 2026/0187510 A1, Technologies for closed-loop qubit calibration, Intel Corporation, filed 2024-12-27 · published 2026-07-02 · https://patents.justia.com/patent/20260187510
[20] [P] PatSnap · Cryo-CMOS technology landscape 2026 · vendor analytics blog · 2026 · https://www.patsnap.com/resources/blog/articles/cryo-cmos-technology-landscape-2026/
[21] [C] Quantum Machines · Quantum Machines Raises $170 Million in Series C Funding (PSG Equity; Intel Capital, Red Dot Capital Partners; $280 M total raised) · press release · 2025-02-25 · https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/
[22] [C] Quantum Machines · Quantum Machines Expands with Second European Acquisition (PCB Engineering, Hungary) · press release · 2026-06-17 · https://www.quantum-machines.co/press-release/quantum-machines-acquisition-pcb-engineering/
[23] [C] SEEQC · SEEQC Files Registration Statement for Proposed Initial Public Offering (Nasdaq: SEQC) · Business Wire · 2026-06-29 · https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering
[24] [P] Quantum Computing Report · SEEQC Files Form S-1 for Nasdaq IPO Parallel to Ongoing Allegro Merger Process ($1 B enterprise value, $65 M PIPE; filed 2026-07-02) · trade press · 2026-07 · https://quantumcomputingreport.com/seeqc-files-form-s-1-for-nasdaq-ipo-parallel-to-ongoing-allegro-merger-process/
[25] [C] QuTech · Scalable diamond quantum computing with cryogenic chip integration (ISSCC 2026; funded by Fujitsu) · 2026-02-17 · https://qutech.nl/2026/02/17/scalable-diamond-quantum-computing-with-cryogenic-chip-integration/

## Open verification items

- Power per qubit at 4 K: IBM's measured 23 mW under active control [D][2] against "optimistic 5 mW" and "below 2 mW" in the resource review [S][6]; definitions differ (active vs idle, drive-only vs full chain) and none is published. 23 mW used.
- Gooseberry's 18 nW per cell [D][4] and the Sydney chip's ~20 nW MHz⁻¹ per cell [D][3] are quoted interchangeably in secondary sources; different quantities, not reconciled.
- Cooling powers for the Bluefors XLD1000sl, IBM Goldeneye and Fermilab Colossus come from the resource review [S][6]; the Bluefors XLD product page returned HTTP 404 on 2026-09-03 and the primary specification is unconfirmed.
- IBM's 2026 cryo-CMOS flux result exists only as conference abstracts [C][5]; no preprint or paper as of 2026-09-03, and the 14 nm FinFET attribution rests on the abstract text. IBM's modular-cryogenics blog (2026-08) gives cell wiring area and vacuum volume but no cooling power at 4 K.
- Equal1's 99.9% / 99.3% / 99% fidelities and "35 monolithic quantum cells" are product-page claims [C][15] with no paper or dated release.
- SemiQon's process node, fab location and the size of its 2026-07 PostScriptum investment are undisclosed.
- SEEQC's revenue, cash and offering size appear in neither the filing announcement nor the trade-press summary [C][23] [P][24]; the $1 B enterprise value and $65 M PIPE are trade-press figures and the S-1 itself was not read.
- Quantum Machines' revenue is undisclosed and its ">50% of companies developing quantum computers" customer share is a company claim [C][21]; Zurich Instruments, Keysight and QBLOX publish nothing comparable, so the warm-control market this node would displace cannot be sized.
- The QuTech/Fujitsu diamond cryo-CMOS ISSCC 2026 paper's power, channel count and process node were not obtainable; only the institutional release [C][25].
- Cryo-CMOS patent-family counts: no named database publishes a dated count; PatSnap gives only regional "key result" tallies with a completeness disclaimer [P][20].
- HRL's controller cost, tape-out schedule and whether IBM retains the 130 nm design are unstated in the acquisition release [C][16]; the acquisition was not confirmed closed as of 2026-09-03.
