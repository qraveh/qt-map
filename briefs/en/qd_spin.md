---
id: qd_spin
name: Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge)
layer: "1 Carrier"
tier: 1
status: demonstrated
since: 2012
one_line: "Electron or hole spin in a lithographically gated dot; exchange gives deterministic ns-scale two-qubit gates on a CMOS die."
verdict: "Only carrier fabricated on a 300 mm line at scale, but two-qubit fidelity has sat at 99.0-99.6% on foundry devices for a year and no array above 12 qubits has published all-pairs numbers."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An electron or hole is trapped in an electrostatic well ~50 nm across, formed by metal gates over a Si/SiGe quantum well, a Si-MOS inversion layer, or a Ge/SiGe hole gas. The spin is the computational degree of freedom; the barrier between neighbouring dots sets an exchange coupling J, and pulsing J for ħπ/J gives a deterministic entangling gate. Loss and DiVincenzo proposed the architecture in 1998; the first single-spin and singlet–triplet qubits in silicon appeared 2010–2012, the lineage date used here.

Coordinates, as the graph record records them:
- **a — affinity:** 1.0, wholly fabricated; every dot is a lithography outcome.
- **b — characteristic time:** ~50 ns per operation, entangling **deterministic** via exchange, not heralded.
- **c — readout:** spin-to-charge conversion on an rf charge sensor, ~6 µs, non-destructive, mid-circuit capable.
- **d — mobility:** static, unless a separate shuttling mechanism is invoked.
- **e — control:** baseband gate voltages plus microwave or EDSR drive, electronics normally at room temperature.
- **f — error structure as the code sees it:** coherent, Pauli, and leakage into valley or charge states.
- **g — manufacturing:** CMOS.

## Physics & limits

Three energy scales govern everything. Zeeman splitting (~10–100 µeV at 0.3–1 T) defines the qubit; exchange J, tunable over 10–100 MHz, defines the gate; valley splitting in silicon (0.1–0.3 meV, non-uniform because it tracks interface roughness) defines the leakage floor. Ge hole dots have no valley degeneracy and need no micromagnet, but their spin–orbit coupling turns electrical noise directly into dephasing.

Two baths set the coherence floor. Nuclear spins are suppressible: ²⁸Si enrichment gives Hahn-echo T2 of 1.31(4) ms on foundry material and Ramsey T2* of 41(2) µs [D][11]. Charge noise is not — 1/f fluctuators in the oxide couple through exchange, so fidelity degrades exactly when J is on: the entangling interaction is also the dominant noise channel. Errors reach the code as coherent over-/under-rotation, Pauli dephasing, and leakage that repetition and surface codes miss without leakage-reduction units. HRL's dissection is the most useful single statement of where the error lives: about **80% of its CNOT error is extrinsic — control and calibration, not physics** [D][2]. Moving the floor needs quieter dielectrics, more uniform valley splitting and better calibration, in that order of difficulty and the inverse order of cost.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: two-qubit fidelity 99.04–99.56% on a 300 mm foundry Si-MOS device [D][1]; 18 qubits in one array, twice, on different materials [D][2][D][3]. Typical at scale is worse, and the gap is the story — imec's eight-qubit 300 mm device validated a two-qubit gate on **one of four** double-dot pairs [D][11]. No device above 12 qubits has published all-pairs two-qubit fidelities on this platform.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2022-01 | 2Q 99.5% (gate-set tomography), Si/SiGe — first crossing of the surface-code threshold | QuTech/TU Delft | [D][13] |
| 2024-03 | 2Q 98.9% at 1 K operating temperature | Diraq/UNSW | [D][5] |
| 2025-09 | 2Q 99.04–99.56%, SPAM 99.9%, on 300 mm foundry Si-MOS | Diraq + imec | [D][1] |
| 2026-04 | 18-qubit Ge 2×N array; 1Q mean 99.8%, median 99.9% | Groove Quantum + QuTech | [D][3] |
| 2026-05 | CZ between two *moving* spins, 98.86 ± 0.29%, 58 ns | QuTech/TU Delft | [D][4] |
| 2026-07 | 8-qubit 300 mm device; Hahn-echo T2 1.31 ms; 2Q on 1 of 4 pairs | imec + Diraq | [D][11] |
| 2026-07 | 18 exchange-only qubits from 54 dots; 1Q 2×10⁻⁴, CNOT 3×10⁻³; d=5 repetition code, 200 rounds, Λ₅/₃ = 4.7 | HRL Laboratories | [D][2] |

The dominant error term today is not decoherence but calibration drift: 54 dots need hundreds of interdependent voltages, and the tune-up surface limits array size, not T2.

## Manufacturing, materials & supply chain

The distinguishing claim is fabrication on unmodified CMOS lines — Intel reports >24,000 devices per 300 mm EUV wafer at 96% tune-up yield [D][6], and Quantum Motion characterised 1,024 dots in five minutes on GlobalFoundries 22FDX [C][7]. Process detail belongs to the 300 mm CMOS foundry brief; wafer-scale statistics exist here and for no other carrier.

Materials are the exposure. Enriched ²⁸Si is a genuine single point of failure: **ASP Isotopes began commercial production of enriched silicon-28 at its second Pretoria facility on 2025-03-27**, with two undisclosed US customers [C][23]. On 2026-07-16 the US DOE Office of Isotope R&D and Production announced that ORNL and PNNL now make silane at 99.9999% ²⁸Si and germane with Ge-73 below 1 ppm, "at least 100×" more depleted than any commercial material — a deliberate re-shoring [G][24]. Ge/SiGe heterostructures come from a handful of academic reactors (Scappucci's group at Delft), a narrower bottleneck than the fab. Export-control exposure is indirect: the dies are ordinary CMOS, but enriched isotopes and dilution refrigerators fall under the 2024 multilateral quantum controls (US ECCN 3A901/3A904).

## Control, readout & I/O burden

Baseband voltages plus a microwave or EDSR drive per qubit, and one rf reflectometry sensor per one-to-several dots. No lasers — the I/O problem is line count and heat. HRL's 4 K controller (≤3.5 W typical, 366 DACs, 296 lines) sequenced a full 18-qubit QEC experiment with no room-temperature real-time electronics [D][2]; UNSW/Diraq have shown mK cryo-CMOS beside the qubits [D][8]. Those controllers are the cryo-CMOS control brief's subject.

The wall is readout, not gates. At ~6 µs spin-to-charge conversion plus settling the cycle runs to hundreds of microseconds — three orders slower than the 50 ns gate, so the syndrome round sets the logical clock. At 10³ qubits line count is survivable only with crossbar shared-line addressing; at 10⁴ sensor count and dissipation dominate; at 10⁶ neither dedicated lines nor per-qubit sensors survive.

## Role in the stack

The node sits on one platform path, **Silicon / germanium quantum-dot spins**. It requires a 300 mm CMOS foundry; it provides the dots consumed by exchange gates, exchange-only and singlet–triplet encoding, conveyor-mode spin shuttling, crossbar shared-line control and spin-to-charge readout. It replaces donor spins (SQC's precision-placed phosphorus), which buy 99.10–99.99% gates on 11 qubits [D][27] at the cost of no foundry path — the switching price in one line.

Derived clock for the path = sum of the syndrome round: gate layers + transport + readout + reset = **8.5 µs**, readout 6.3 µs of it and reset 1 µs. The node is not a hub and has no off-diagonal reach: everything it enables is downstream of itself, so a failure here has no fallback elsewhere. The neighbouring empty slot is fast sensor-free readout — Pauli-spin-blockade below 1 µs at >99.9%; nothing in the graph fills it.

## Verification (QCVV)

Headline two-qubit numbers come from interleaved randomized benchmarking or gate-set tomography on the best pair on the die — a legitimate protocol reporting an illegitimate summary, capturing neither cross-talk nor calibration drift. HRL's d=5 repetition code over 200 rounds is the only spin result measuring error *in situ* under continuous operation, and its Λ₅/₃ = 4.7 [D][2] is bit-flip-only, not below-threshold logical memory, which no spin platform has shown.

Conflicts. Diraq's messaging conflicts on scale: a 2026-07-09 release said "thousands of qubits by 2029", the 2026-08-27 roadmap says 150,000 physical and 1,000 logical by 2029 [R][10][G:DIRAQ-FUNDING]; take the roadmap as the company's position and the discrepancy as evidence about the company. No replication of the 300 mm two-qubit result outside the imec line exists.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Diraq | developer | AU | Si-MOS qubits on imec 300 mm; 2Q 99.04–99.56%; 1 K operation | [D][1][D][5] |
| HRL Laboratories | developer | US | Exchange-only SiGe, 18 qubits, self-sequenced d=5 QEC | [D][2] |
| IBM | investor | US | Acquired HRL; adds spins to a superconducting roadmap | [C][9] |
| Intel | developer | US | 300 mm EUV spin devices; 12-qubit Tunnel Falls at Argonne | [D][6][P][19] |
| Quantum Motion | developer | UK | 22FDX dots; full-stack CMOS system delivered to NQCC | [C][7] |
| QuTech (TU Delft) | research | NL | Shuttled-spin gates, parity checks, Ge heterostructures | [D][4][D][26] |
| Groove Quantum | developer | NL | 18-qubit Ge array, spun out of the Delft Ge programme | [D][3] |
| Quobly | developer | FR | ²⁸Si FD-SOI lots at ST Crolles since 2025-12 | [C][17] |
| Equal1 | developer | IE | Bell-1 six-qubit rack unit; RacQ at ESA Frascati | [C][18] |
| SemiQon | supplier | FI | VTT spin-out; cryo-CMOS chips fabricated in Espoo | [P][22] |
| GlobalFoundries | supplier | US | Quantum Technology Solutions unit; 22FDX wafers | [C][20] |

**Money.**

- 2025-02-24 · SemiQon · round · €17.5 M (€15 M equity + €2.5 M grant) · European Innovation Council · closed [P][21]
- 2025-11-06 · Diraq, Quantum Motion, SQC · DARPA QBI Stage B · up to $15 M each · DARPA · three of eleven · announced [G:QBI-STAGEB-2025-11][14]
- 2026-01-15 · Equal1 · round · $60 M · ISIF · >$85 M cumulative · closed [C][G:EQUAL1-60M-2026-01][18]
- 2026-04-30 · Groove Quantum · round · €16 M · undisclosed · €26 M cumulative · closed [P][G:GROOVE-2026]
- 2026-05-07 · Quantum Motion · Series C · $160 M · DCVC, Kembara · closed [C][16]
- 2026-05-21 · Diraq · US CHIPS letter of intent · up to $38 M · Dept of Commerce · LOI [G][15]
- 2026-05-21 · GlobalFoundries · US CHIPS LOI, multi-modality quantum foundry · $375 M · Dept of Commerce · LOI [G][15][C][20]
- 2026-06-03 · Quobly · Series A · €115 M · Bpifrance, SEALSQ, STMicroelectronics · €134 M cumulative · closed [C][17]
- 2026-06 · Silicon Quantum Computing · NRFC (donor route) · A$60 M · Australia NRFC · closed [G:SQC-NRFC-2026]
- 2026-07-03 · SemiQon · strategic investment · undisclosed · PostScriptum · closed [P][22]
- 2026-08-26 · IBM / HRL · M&A **completed** (announced 2026-07-23) · terms undisclosed · sellers Boeing and General Motors, still application partners · definitive [C][9]

**Market & supply chain.** Nobody sells spin qubits; the sold goods are foundry runs, enriched isotopes and cryo-electronics. Foundry access is bought from imec, GlobalFoundries and STMicroelectronics, with GF productising it as a business unit in 2026 and naming Diraq, Equal1 and Quantum Motion as customers [C][20]. Isotope supply is the concentrated risk — one commercial producer of scale plus a restarted US national-lab capability [C][23][G][24]. Diraq's "<$1/qubit at two million qubits" [R][10] is a projection, not a price. What pays today is G3 (HRL's QEC work, QBI Stage B) and G7 (Quantum Motion at NQCC, Equal1 at ESA); nothing here is bought for G1, G2 or G5.

**IP & standards.** The one dated database view available — a PatSnap analysis of 2026-06-02, updated 2026-08-21 — is thin: ~60 records 2005–2026, with NewSouth Innovations (UNSW, Diraq's licensing root) largest at five filings, ahead of SIAT/SIMIT, MIT, Intel and SQC [P][25]. Too small to be a census. No litigation is on record, no spin-specific standards body exists, and HRL's controller IP is now unpublished inside IBM.

**Roadmaps & track record.** Diraq (promised 2026-08-27 · for 2029 · 150 k physical / 1 k logical, >2 M by 2031) — six weeks earlier it said "thousands by 2029" [R][10]: keep the fidelities, discount the counts. Quobly (2026-06 · for 2032 · millions of qubits) — funded and fabbing at ST, no published multi-qubit device: an intention. SQC (for 2033 · commercial scale) — real 11-qubit donor result [D][27], unfalsifiable until 2030. Quantum Motion — the only actor to have delivered a system to a customer on schedule [C][7]. Intel — 12 qubits at Argonne, no successor chip and no dated roadmap as of 3 Sep 2026 [P][19]: alive but unguided. IBM/HRL — no spin milestone yet on Starling (2029) or Blue Jay (mid-2030s) [C][9].

**Strategic reading.** If the platform succeeds the winners are foundries and isotope suppliers, not qubit designers: a Si-MOS qubit is a process recipe, and once qualified the marginal die is cheap and differentiation moves to calibration software. That is why IBM bought HRL — not for 18 qubits but for a cryo-CMOS control stack and packaging reusable across modalities: a supplier acquisition dressed as a platform bet. The losers are pure-play spin startups, whose bargaining power against a foundry that has just productised quantum manufacturing is falling. Manufacturability is the platform's only defensible argument, and if 2Q fidelity is still 99.0–99.6% through 2027 with arrays under 20 qubits, it stops being enough.

*Open niche:* the platform's own best measurement says roughly 80% of two-qubit error is extrinsic control and calibration [D][2], and its published fidelities are single-best-pair numbers no protocol extends across a heterogeneous array. A small QCVV house can sell that gap: array-level cross-talk and drift characterisation, leakage-aware benchmarking that separates valley leakage from Pauli error, and independent verification of foundry claims for fabs and funders. The SFQ angle is adjacent — mK classical logic for readout sequencing is the same wall at 10⁴ qubits — but the QCVV work needs no fab.

## Outlook & open questions

**Confirm** if by end-2027 a group publishes all-pairs two-qubit fidelities above 99% on a ≥16-qubit array, or a spin device shows below-threshold logical memory in a distance-3-to-5 surface code, or IBM places a dated spin milestone on its public roadmap. **Demote** if foundry two-qubit fidelity is still 99.0–99.6% in mid-2027, if Intel makes no further spin announcement, or if Diraq revises its 2029 figure downward a second time.

Best case by 2029: a few hundred physical qubits on a qualified 300 mm process with shared-line control and a working logical memory — two orders of magnitude short of Diraq's 150 k. Worst case: the platform stays a foundry demonstration, the startups consolidate into IBM, GlobalFoundries and STMicroelectronics, and spin qubits become a control-electronics business with qubits attached.

Open questions. (1) Is 99.5%-class two-qubit fidelity reproducible across all pairs of a die, or only the pair that tunes up? (2) Can valley splitting be made uniform enough that leakage stops being a per-device lottery? (3) Does readout get below 1 µs without a charge sensor per qubit? (4) Did IBM buy a qubit or a control stack?

## Sources

[1] Steinacker, Dumoulin Stuyck, Nickl et al. (Diraq/UNSW/imec) · 300 mm foundry spin-qubit unit cell · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9
[2] HRL Laboratories · self-sequenced 18-qubit QPU, d=5 repetition code · arXiv:2604.16216, Nature · 2026-07-29 · https://arxiv.org/abs/2604.16216
[3] Dijkema, Hendrickx et al. (Groove Quantum/QuTech) · 18-qubit germanium array · arXiv:2604.01063 · 2026-04-01 · https://arxiv.org/abs/2604.01063
[4] Matsumoto et al. (QuTech/TU Delft) · CZ between moving spins · Nature 653 · 2026-05-06 · https://www.nature.com/articles/s41586-026-10423-9
[5] Huang, Yang et al. (Diraq/UNSW) · spin qubit operation above 1 K · Nature · 2024-03 · https://www.nature.com/articles/s41586-024-07160-2
[6] Neyens et al. (Intel) · 300 mm EUV wafer statistics · arXiv:2410.16583 · 2024-10 · https://arxiv.org/abs/2410.16583
[7] [C] Quantum Motion · full-stack silicon CMOS system at NQCC · 2025-09-15 · https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/
[8] UNSW/Diraq · mK cryo-CMOS beside the qubits · 2025-06 · https://www.unsw.edu.au/newsroom/news/2025/06/unsw-engineers-crack-challenge-scaling-quantum-computers
[9] [C] IBM · completes acquisition of HRL Laboratories · 2026-08-26 · https://newsroom.ibm.com/2026-08-26-ibm-completes-acquisition-of-hrl-laboratories-to-accelerate-the-future-of-quantum
[10] [C] Diraq · utility-scale roadmap · 2026-08-27 · https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip
[11] Nickl, Dumoulin Stuyck et al. (imec/Diraq) · eight-qubit 300 mm device · Nature Communications 17, 5878 · 2026-07-09 · https://www.nature.com/articles/s41467-026-74597-6
[12] De Smet et al. (QuTech/TU Delft) · single-spin conveyor shuttling · Nature Nanotechnology 20 · 2025-06-09 · https://www.nature.com/articles/s41565-025-01920-5
[13] Xue, Vandersypen et al. · spin logic crossing the surface-code threshold · Nature 601 · 2022-01 · https://arxiv.org/abs/2107.00628
[14] [G] DARPA · QBI Stage B selection · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[15] [G] NIST/US Commerce · CHIPS letters of intent, nine companies · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[16] [C] Quantum Motion · $160 M Series C · 2026-05-07 · https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/
[17] [C] Quobly · €115 M Series A; ST Crolles lots · 2026-06-03 · https://www.quobly.io/
[18] [C] Equal1 · $60 M round; Bell-1; RacQ at ESA · 2026-01-15 · https://www.equal1.com/
[19] [P] Argonne National Laboratory · Intel 12-qubit processor collaboration · 2026-01-06 · https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel
[20] [C] GlobalFoundries · Quantum Technology Solutions launch · 2026-05-21 · https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions/
[21] [P] Quantum Computing Report · SemiQon €17.5 M · 2025-02-24 · https://quantumcomputingreport.com/semiqon-secures-e17-5m-18-3m-usd-to-develop-cryogenic-cmos-technology-for-quantum-systems/
[22] [P] The Quantum Insider · PostScriptum invests in SemiQon · 2026-07-03 · https://thequantuminsider.com/2026/07/03/postscriptum-invests-in-quantum-hardware-developer-semiqon/
[23] [C] ASP Isotopes · commercial production of enriched silicon-28 · 2025-03-27 · https://ir.aspisotopes.com/news-events/press-releases/detail/56/asp-isotopes-inc-commences-commercial-production-of
[24] [G] US DOE Isotope R&D and Production (ORNL, PNNL) · domestic silicon and germanium isotopes · 2026-07-16 · https://www.hpcwire.com/off-the-wire/doe-advances-domestic-supply-of-silicon-germanium-isotopes-for-quantum-computing/
[25] [P] PatSnap Eureka · spin-qubit quantum-dot array patent analysis · 2026-06-02 · https://www.patsnap.com/resources/blog/rd-blog/spin-qubit-silicon-quantum-dot-arrays-2026-patsnap-eureka/
[26] Undseth et al. (QuTech/TU Delft) · weight-four parity checks, mobile ancilla · Nature 655 · 2026-07-29 · https://www.nature.com/articles/s41586-026-10766-3
[27] Edlbauer, Wang, Huq et al. (SQC) · 11-qubit atom processor in silicon · Nature 648 · 2025-12-17 · https://www.nature.com/articles/s41586-025-09827-w

## Open verification items

- SemiQon cumulative funding and the PostScriptum amount undisclosed; the €17.5 M figure is paywalled trade press, round type unstated [P][21][P][22].
- Groove Quantum's €16 M (2026-04-30) has no primary-source URL; investors unnamed [P][G:GROOVE-2026].
- IBM–HRL deal value undisclosed in both releases; no spin milestone dated on IBM's roadmap [C][9].
- ASP Isotopes' enrichment level, capacity and customers undisclosed; DOE quantities and funding unstated [C][23][G][24].
- Diraq conflict on 2029 scale: "thousands" (2026-07-09) vs 150 k physical / 1 k logical (2026-08-27); roadmap figure used [R][10].
- PatSnap dataset (~60 records) omits HRL, imec, Diraq and Quantum Motion; treated as a sample, not a census [P][25].
- No independent replication of the 300 mm two-qubit fidelity range outside the imec line [D][1].
