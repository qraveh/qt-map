---
id: g_exch
name: Exchange gate (spins; incl. shuttled-spin CZ)
layer: "3 Gate mechanism"
status: demonstrated
since: 2018
one_line: Voltage-pulsed Heisenberg exchange between neighbouring or shuttled spins in gate-defined dots or donors — the only entangling mechanism that needs nothing but CMOS gate electrodes.
verdict: Best exchange CNOT is 9×10⁻⁴ (HRL, 18 qubits) and foundry pairs sit at 99.0–99.6%, but ~80% of two-qubit error is calibration rather than physics, and no device past eight qubits publishes all-pairs fidelity.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A voltage pulse lowers the tunnel barrier between two neighbouring quantum-dot or donor spins, turning on Heisenberg exchange J for a set time to realise a SWAP-family entangler; nothing is radiated, so no antenna, laser or resonator is needed. Loss and DiVincenzo proposed spin qubits on it in 1998; DiVincenzo, Bacon, Kempe, Burkard and Whaley showed in 2000 that exchange alone is universal at ~3× more qubits and ~10× more two-qubit operations — the encoding HRL builds on [S][7]. The shuttled variant moves one electron through a conveyor potential into exchange range with a distant partner.
Coordinates: fully fabricated carrier; deterministic entangling at ≈10⁻⁷ s (~100 ns), static nearest-neighbour coupling by default.
Baseband voltage control, room temperature but moving cryogenic; error coherent, Pauli, leakage; manufacturing is CMOS.

## Physics & limits
J rises exponentially as the barrier is lowered and tunes electrically from near zero to tens of MHz; gate time goes as 1/J, which is why measured gates land at 58–500 ns for 10–90 MHz exchange. The exponential is the liability: the lever that makes J fast makes δJ/J large under gate-voltage and charge-trap noise, so there is a working point rather than a maximum — push J up and charge noise dephases the gate, pull it down and the longer pulse does. Hence HRL's finding that roughly 80% of two-qubit error is extrinsic control and calibration, not decoherence [D][2]. Beneath that sit the residual ²⁹Si bath, 1/f charge noise at the oxide interface and small valley splitting, which makes leakage a first-class error. Moving the floor needs ²⁸Si enrichment, better interfaces, and a controller that keeps 1/f noise off the barrier gates.

## Engineering state of the art
Best exchange gate: HRL's exchange-only CNOT at 9×10⁻⁴ best reproducible, 3×10⁻³ mean across 18 qubits formed from 54 dots, single-qubit mean 2×10⁻⁴, sequenced by a 4 K controller in commercial 130 nm RF CMOS [D][2]. At foundry scale Diraq and imec report 99.04–99.56% two-qubit and 99.9% SPAM on 300 mm SiMOS [D][1]. The shuttled variant adds a weight-four parity check at 97.7% per 1.2 µm round trip, motion and idling supplying about a quarter of its error [D][4]. SQC's 11-qubit donor device is different in kind: nuclear spins hyperfine-coupled to a shared electron, registers linked by exchange [D][5]. Nothing beyond eight qubits publishes all-pairs fidelity.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-09 | Two-qubit 99.04–99.56%, 300 mm foundry | Diraq with imec | [D][1] |
| 2025-12 | 11 donor qubits, registers linked by exchange | Silicon Quantum Computing | [D][5] |
| 2026-05 | Shuttled-spin CZ 98.86% in 58 ns | QuTech | [D][3] |
| 2026-07 | Exchange-only CNOT 9×10⁻⁴ best, 18 qubits | HRL Laboratories | [D][2] |

## Manufacturing, materials & supply chain
It needs only gate electrodes and voltage pulses, so it rides existing lines: Intel 300 mm EUV (>24,000 devices per wafer, 96% tune-up yield) [D][8], imec 300 mm, GlobalFoundries 22FDX, STMicroelectronics FD-SOI. Two concentrations matter — GlobalFoundries has folded the modality into one business unit behind a USD 375 M CHIPS letter of intent [C][18], and Quantum Machines' control stack sits under Diraq, HRL, imec, Equal1, Sandia and the UK NQCC [C][17]. Export exposure is direct: the 2024-09-06 BIS rule created ECCN 3A901.a for CMOS circuits *designed* to run at or below 4.5 K — a design-intent test, so a cryo-CMOS controller design file of the HRL type is itself controlled [G][16].

## Control, readout & I/O burden
A double dot needs roughly 4–6 baseband channels, so wiring grows faster than qubit count under room-temperature control; HRL's answer is 296 lines and 366 DACs inside the fridge at ≤3.5 W, with no real-time room-temperature loop [D][2]. Readout, not the gate, sets the cycle: 1–100 µs against a 58–500 ns gate. At 10³ qubits room-temperature fan-out is impractical without cryogenic integration; at 10⁴–10⁶ the crossbar schemes that cut wire count collide with the need to calibrate every exchange pair separately — this mechanism's unresolved architectural conflict.

## Role in the stack
It entangles two families: silicon and germanium quantum-dot spins (Intel, Diraq, Quantum Motion, HRL under IBM, Quobly, Equal1) and donor spins (SQC). It requires a gate-defined dot or donor plus baseband control, and provides the entangling layer both families build codes on — at HRL a distance-5 repetition code with Λ(5/3) = 4.7 over 200 rounds, which detects bit flips only and is therefore not a below-threshold result for a full code, plus a post-selected [[4,2,2]] at 0.95 logical fidelity [D][2]. It conflicts with crossbar addressing, calibration being per pair. Derived round 8.5 µs on dot spins and 7.7 µs on donors, readout-limited, against the ~100–300 µs typically run: the gate is not the bottleneck. Neighbouring empty slot: an all-pairs, same-chip result past eight qubits.

## Verification (QCVV)
HRL's headline figures and the 80% calibration split are vendor-reported and unreplicated [D][2]. Diraq and imec's 99.04–99.56% is a population statistic over foundry devices, not an all-pairs same-chip result; imec's eight-qubit device validates exchange on one of four pairs [D][6]. Nature's July 2026 spin-qubit feature was corrected on 2026-08-04, revising single-qubit error rates attributed to HRL and QuTech [P][20]. No below-threshold logical memory exists on any spin platform as of 2026-09-04.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Diraq | developer | Australia | 300 mm foundry two-qubit gates, 99.04–99.56% | [D][1] |
| HRL Laboratories (IBM) | developer | US | 18 exchange-only qubits, sequenced at 4 K | [D][2] |
| QuTech | research | Netherlands | Shuttled-spin CZ, mobile-ancilla parity checks | [D][3] |
| Silicon Quantum Computing | developer | Australia | Donor registers linked by electron exchange | [D][5] |
| Quantum Motion | developer | UK | Full-stack 22FDX system at the UK NQCC | [C][9] |
| Quantum Machines | supplier | Israel | Control stack under most published spin results | [C][17] |

**Money.**
- 2025-11-06 · DARPA · QBI Stage B · ≤USD 15 M each · Diraq, Quantum Motion, SQC of eleven · awarded [G][14]
- 2026-05-07 · Quantum Motion · Series C · USD 160 M · DCVC, Kembara · closed [C][9]
- 2026-05-21 · Diraq · CHIPS letter of intent · up to USD 38 M · US Commerce · LOI, not an award [G][15]
- 2026-08-26 · IBM · M&A, HRL Laboratories · terms undisclosed · closed [C][12]

**Market & supply chain.** No lasers, no vacuum: the equipment is a CMOS line plus baseband electronics, so the supply chain is four foundry lines and one control vendor — a cost argument and a concentration risk at once. Diraq's "<USD 1 per qubit by 2031" is a target, not a cost [R][13]. It sells G1 and G2 devices; IBM's purchase bets it carries to G3 and G4.

**IP & standards.** The foundational results — Loss–DiVincenzo 1998 and exchange-only universality in 2000 [S][7] — are published, not proprietary, so defensible IP sits in device geometry, cryogenic control silicon and calibration software. No dated patent-family count specific to this gate was found as of 2026-09-04.

**Roadmaps & track record.** Diraq (promised 2026-08-27 · 150 k physical, 1 k logical by 2029 · six weeks earlier the same company said "thousands by 2029") [R][13] — inconsistent. Intel (promised 2026-01 · Tunnel Falls scaling to "hundreds of dots" · no dated follow-up) [C][19] — unscorable. IBM (promised 2026-07-23 · HRL close by end Q3 2026 · closed 2026-08-26) [C][11][12] — met.

**Strategic reading.** If exchange gates reach fault-tolerant fidelity, the winners are the foundries and whoever owns the cryogenic controller — the qubit becomes a process option, not a product — and the losers are platforms whose cost base is optics and vacuum. IBM's acquisition turns HRL into a hyperscaler's spin programme and forces Diraq, Quantum Motion and Quobly to compete on balance sheet. If calibration burden persists, spins stay a G1/G2 curiosity.

*Open niche:* a small QCVV house could measure the calibration-versus-physics split in two-qubit error across foundry lines — HRL's 80% is self-reported — or build the cross-lab protocol for shuttled-spin CZ, where every published number comes from one group.

## Outlook & open questions
Falsifiable in 12–24 months: confirm/demote that a foundry device publishes all-pairs fidelity past eight qubits, and that IBM places a dated spin milestone on a public roadmap. Best case by 2029: a cryogenically sequenced foundry chip shows below-threshold logical memory with a full code. Worst case: uniformity stalls past ten qubits and roadmaps stay two orders ahead of hardware. Open: can calibration error fall without importing the controller's own error budget; does shuttled CZ displace static exchange; what IBM does with HRL's silicon.

## Sources
[1] Diraq with imec, two-qubit gates on 300 mm SiMOS foundry devices · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9 — [D]
[2] HRL Laboratories, digitally controlled silicon quantum processing unit (18 exchange-only qubits, 4 K controller) · arXiv:2604.16216, Nature 2026-07-29 · 2026-04-17 · https://arxiv.org/abs/2604.16216 — [D]
[3] QuTech / TU Delft, controlled-phase gate between shuttled spins · Nature 653 · 2026-05-06 · https://www.nature.com/articles/s41586-026-10423-9 — [D]
[4] QuTech / TU Delft, weight-four parity checks with a mobile ancilla · Nature 655 · 2026-07-29 · https://www.nature.com/articles/s41586-026-10766-3 — [D]
[5] Edlbauer, Wang, Huq et al. (Silicon Quantum Computing), "An 11-qubit atom processor in silicon" · Nature 648, 569–575 / arXiv:2506.03567 · 2025-12-17 · https://arxiv.org/abs/2506.03567 — [D]
[6] Nickl, Dumoulin Stuyck, Steinacker et al. (imec), eight-qubit 300 mm SiMOS device · Nature Communications 17, 5878 · 2026-07-09 · https://www.nature.com/articles/s41467-026-74597-6 — [D]
[7] DiVincenzo, Bacon, Kempe, Burkard, Whaley, "Universal quantum computation with the exchange interaction" · Nature 408, 339 / arXiv:quant-ph/0005116 · 2000 · https://arxiv.org/abs/quant-ph/0005116 — [S]
[8] Intel, 300 mm spin-qubit wafer statistics · arXiv:2410.16583 · 2024 · https://arxiv.org/abs/2410.16583 — [D]
[9] Quantum Motion, "Quantum Motion Raises $160 Million Series C" · press release · 2026-05-07 · https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ — [C]
[10] The Quantum Insider, "Quobly Secures €115 Million Series A" · trade press · 2026-06-03 · https://thequantuminsider.com/2026/06/03/quobly-secures-e115-million-series-a-to-bring-silicon-based-quantum-computers-to-market/ — [P]
[11] IBM Newsroom, "IBM to Acquire HRL Laboratories to Power the Future of Quantum" · press release · 2026-07-23 · https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum — [C]
[12] IBM Newsroom, "IBM Completes Acquisition of HRL Laboratories" · press release · 2026-08-26 · https://newsroom.ibm.com/2026-08-26-ibm-completes-acquisition-of-hrl-laboratories-to-accelerate-the-future-of-quantum — [C]
[13] Diraq, "Diraq Sets Roadmap for Utility-Scale Quantum Computing" · press release · 2026-08-27 · https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip — [R]
[14] DARPA, "Quantum Benchmarking Initiative — Stage B Selection" · programme page · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection — [G]
[15] US Department of Commerce / NIST, CHIPS letters of intent to nine companies · news release · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion — [G]
[16] US Bureau of Industry and Security, "Commerce Control List Additions and Revisions: Implementation of Controls on Advanced Technologies" (ECCN 3A901.a, cryogenic CMOS) · Federal Register interim final rule · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies — [G]
[17] Quantum Machines, semiconductor spin-qubit control stack and named customers · company page · accessed 2026-09-04 · https://www.quantum-machines.co/qubit-types/semiconductor-spin-qubits/ — [C]
[18] GlobalFoundries, "GlobalFoundries Launches Quantum Technology Solutions" · press release · 2026-05-21 · https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ — [C]
[19] Argonne National Laboratory, "Argonne Launches Silicon Quantum Processor Collaboration with Intel" · news release · 2026-01-06 · https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel — [C]
[20] Nature, "Underdog 'spin qubits' leap forward in race to a useful quantum computer" (correction 2026-08-04 to single-qubit error rates) · news feature · 2026-07-29 · https://www.nature.com/articles/d41586-026-02357-z — [P]
[21] Silicon Quantum Computing, NRFC investment · company news · 2026-06 · https://sqc.com/news/nrfc-investment — [C]

## Open verification items
HRL's ~80% calibration share of two-qubit error is self-reported, single-vendor and unreplicated as of 2026-09-04. SQC fidelity range conflict: the arXiv abstract of [5] states all fidelities 99.5–99.99% and Bell states beyond 99%, while the published Nature version gives 99.10–99.99% with Bell up to 99.5%, and the main report quotes a single 99.90% donor nuclear CZ — three different framings of the same experiment, and the 99.90% could not be isolated in the abstract. Financial terms of the IBM–HRL acquisition are undisclosed in both the announcement and the closing release. Diraq's total raised (">USD 100 M") comes from trade press, not a company release. No dated patent-family count specific to exchange gates was found.
