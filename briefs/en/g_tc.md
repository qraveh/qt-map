---
id: g_tc
name: Tunable-coupler CZ / iSWAP
layer: "3 Gate mechanism"
tier: 2
status: demonstrated
since: 2014
one_line: A flux-tuned coupler switches the exchange and ZZ interaction between transmons on and off, giving deterministic 25–70 ns CZ or iSWAP gates.
verdict: Falsifiable — isolated pairs are already at the coherence limit, so if fleet-width error does not fall below 0.2% by 2027 the binding constraint is T1 and calibration, not the coupler.
updated: 2026-09-03
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
A flux-tunable coupler is a third element — usually a tunable transmon — bridging two data qubits. Its frequency sets an indirect coupling path that interferes with the direct capacitive one, so a bias sweep tunes net exchange through zero: at the off point static ZZ cancels; a pulse away from it drives a deterministic CZ or iSWAP via the |11⟩–|20⟩ crossing. Google/UCSB introduced it as the gmon in 2014, coupling settable to zero at nanosecond resolution without spoiling coherence [D][1].
Coordinates: carrier affinity a = 1.0, fully fabricated, no natural analogue. Gate time ~10⁻⁷·⁴ s (≈40 ns), deterministic.

## Physics & limits
The coupler buys speed and isolation at the cost of a third noisy degree of freedom. Tens of MHz on-coupling sets 25–70 ns gates. Three mechanisms set the floor. Coherence: at 40 ns against Willow's mean T1 of 68 µs, relaxation and dephasing during the pulse already cost a few 10⁻⁴, most of the gap between the 99.88% device mean and unity [D][4] — pulse shaping cannot recover it, only longer T1 or shorter gates. Leakage: the pulse passes near |20⟩ and the coupler's second level, so population leaves the computational space — an unheralded, sticky error to the code. And 1/f flux noise on the bias moves the off point between calibrations, leaving a drifting residual ZZ that appears as coherent, correlated error. What moves the floor: higher T1, larger anharmonicity (fluxonium couplers), shaped flux pulses, and couplers biased at a flux-insensitive point.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-11 | Double-transmon coupler CZ 99.90% in 48 ns | Toshiba | [D][2] |
| 2024-12 | Willow, 105 q: mean 2Q 99.88%, mean T1 68 µs, 1.1 µs cycle | Google | [D][4] |
| 2025-08 | CZ 99.93% over 40 h, 1Q 99.98%, readout >99.94% on one device | IQM | [D][3] |
| 2026-07 | Fleet EPLG, full width: best 0.19%, typical 0.37% | IBM | [C][5] |

Three regimes, not one number: a characterised pair reaches 99.93% [D][3]; a 105-qubit device averages 99.88% [D][4]; IBM's full-width fleet benchmark reads 0.37% typical, 0.19% best [C][5]. Zuchongzhi 3.0 sits at 99.62% over 105 qubits [D][7]. The two-qubit gate is still ~40% of Google's colour-code error budget, leakage next [D][8].

## Manufacturing, materials & supply chain
There is no separate coupler process: the coupler is another junction and SQUID loop in the same superconducting lithography, so its defects are the platform's own — junction-frequency spread and two-level-system defects pulling the off point. The manufacturing cost is I/O, not lithography: Nighthawk carries 218 couplers across 120 qubits, each demanding a bias line [C][6]. QuantWare is the only merchant seller of tunable-coupler chips, funded by a $178 M Series B and building a Delft fab [P][9]. Export control names whole computers (4A906) and cryogenic electronics (3A901), not gate mechanisms [G][10]. No coupler yield or cost is published.

## Control, readout & I/O burden
On a square lattice couplers outnumber qubits about two to one, each needing a fast flux line with its own DAC and filtering. At 10³ qubits that is thousands of flux lines; at 10⁴ it binds before fidelity does, and the only demonstrated escape is an on-chip bias source, as in D-Wave's flip-chip flux DAC on a fluxonium at 10 mK [C][11]. The recurring cost is calibration, not latency: off points drift with 1/f flux noise, so calibration scales with coupler count — hence Google steering it by reinforcement learning during error correction, at 7.72×10⁻⁴ logical error per cycle at d=7 [D][12].

## Role in the stack
It belongs to the superconducting-transmon path (Google, IBM, Rigetti, IQM, OQC, USTC, Fujitsu) and requires the transmon carrier. It replaces fixed-frequency cross-resonance; the switching price is redesigning every qubit-coupler-qubit cell, roughly double the bias lines and a new calibration stack — the trade IBM accepted with Nighthawk after a decade on cross-resonance [C][6]. Its clock contribution is negligible: derived clock = max(gate, readout, transport) is 1.1 µs per error-correction cycle against a 0.048 µs gate [D][4], so this node moves the error budget, not the clock. No neighbouring empty slot in the technology graph.

## Verification (QCVV)
The 99.90% and 99.93% headlines are interleaved randomised benchmarking on one characterised pair, and RB is blind to leakage unless a leakage protocol runs alongside — leakage being this gate's second error term. EPLG is a different observable, full-width layered gates including crosstalk, so the 0.37% versus 0.07% gap is definitional as much as fleet variability. Neither record has been replicated by an independent laboratory. One attribution conflict: the cited "25 ns at 99.8%" Oxford result is a fixed-coupling coaxmon pair with no coupler at all [C][13].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Google | developer | US | Originated the gmon; Willow uses tunable couplers | [D][1] |
| IBM | developer | US | Nighthawk: 218 couplers on 120 qubits; coupler patent | [C][6] |
| IQM | developer | Finland | Record CZ 99.93% with a floating tunable coupler | [D][3] |
| QuantWare | supplier | Netherlands | Sells tunable-coupler transmon chips; Delft fab | [P][9] |
| Rigetti | developer | US | Tunable-coupler chiplets, median 2Q 99.1% | [C][G:RIGETTI-FIN-2026] |

**Money.**
- 2026-06-02 · IBM · programme (5-year quantum commitment) · >$10 B · — · announced [G:IBM-10B-2026-06]
- 2026-05-05 · QuantWare · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners · closed [P][9][G:QUANTWARE-SERIESB-2026-05]
- 2026-07-02 · IQM · listing (Nasdaq/Helsinki) · cash €337 M, H1-2026 revenue €8.9 M · closed [G:IQM-LISTING-2026-07]
- 2025-11-06 · DARPA · QBI Stage B, IBM the only transmon vendor of eleven · ≤$15 M each · announced [G:QBI-STAGEB-2025-11]

**Market & supply chain.** What this gate consumes is flux control — multi-channel AWGs and DACs from Zurich Instruments, Quantum Machines and Keysight, none coupler-specific — so concentration risk sits in chips, not instruments. QuantWare is the only merchant route; everyone else fabricates in-house, making coupler design proprietary and control electronics commodity. G2 and G3 pay for this node: both need 10⁻³ two-qubit error at fleet width.

**IP & standards.** IBM holds US 11,727,297 B2, "Tunable quantum coupler facilitating a quantum gate between qubits" (granted 2023-08-15), claiming an opposite-sign second coupling path that cancels unwanted coherent rotation [G][14]; Google's 2014 gmon work is published prior art [D][1]. No litigation identified, no standards body for coupler design or reporting.

**Roadmaps & track record.** IBM: Nighthawk 5,000 two-qubit gates per circuit (promised 2025-06-10 · for 2025 · delivered 2025-12) → 7,500 in 2026 → 10,000 in 2027 [R][G:IBM-ROADMAP], on schedule, though the coupler switch is one generation old. IQM: 2Q above 99.94% (promised for 2025–26) is within error of the 99.93% delivered [D][3]. Rigetti: 108 qubits at 99.5% slipped to "later 2026", the gap sitting in the coupler-mediated gate [C][G:RIGETTI-FIN-2026].

**Strategic reading.** IBM's move off cross-resonance settles the architecture argument for tunable coupling, strengthening control-electronics vendors — every coupler is another channel sold — and merchant chip suppliers. The substitution threat is not cross-resonance but passive ZZ cancellation by design: a fixed-coupling coaxmon pair reached 25 ns at 99.8% with no coupler and no flux line [C][13]; if that scales, the line tax becomes a liability. Bargaining power stays with whoever owns the fab.

*Open niche:* This gate is reported almost entirely as best-pair interleaved RB, and the one public fleet-versus-record comparison mixes two observables. A vendor-neutral protocol measuring how much isolated-pair fidelity survives at full lattice width — leakage separated from Pauli error, ZZ drift tracked between calibrations — is a low-capital QCVV wedge.

## Outlook & open questions
Confirm or demote within 12–24 months: does Nighthawk reach 7,500 two-qubit gates by end-2026; does any fleet report typical EPLG below 0.2%; does a second laboratory reproduce 99.93%. Best case by 2029: fleet-width error near 10⁻³ at 10³ qubits, on-chip biasing removing the line tax. Worst case: coupler count caps chips near 10³ qubits and the 40 ns coherence limit holds error at a few 10⁻⁴, too high for Λ to grow. Open questions: does IBM's patent constrain merchant coupler chips; can fluxonium couplers cut leakage; will fixed coupling remove the line tax at scale.

## Sources
[1] Chen et al. (Google/UCSB) · "Qubit architecture with high-coherence and fast tunable coupling" (gmon) · Phys. Rev. Lett. 113, 220502 · 2014 · https://arxiv.org/abs/1402.7367 [D]
[2] Toshiba · Double-transmon coupler, CZ 99.90% in 48 ns · Phys. Rev. X 14, 041050 · 2024-11 · https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050 [D]
[3] Marxer, Vepsäläinen et al. (IQM Quantum Computers, Espoo/Munich) · "Above 99.9% fidelity single-qubit gates, two-qubit gates, and readout in a single superconducting quantum device" · arXiv:2508.16437 · 2025-08-22 · https://arxiv.org/abs/2508.16437 [D]
[4] Google Quantum AI · "Quantum error correction below the surface code threshold" (Willow: 105 q, mean 2Q 99.88%, mean T1 68 µs, 1.1 µs cycle) · Nature · 2024-12 · https://www.nature.com/articles/s41586-024-08449-y [D]
[5] IBM · "What's new in Q2 2026" (fleet EPLG: typical 0.37%, best 0.19% on ibm_boston) · IBM Quantum blog · 2026-07 · https://www.ibm.com/quantum/blog/whats-new-q2-2026 [C]
[6] IBM Newsroom · Nighthawk (120 qubits, 218 tunable couplers, 5,000 two-qubit gates) and Loon · 2025-11-12 · https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance [C]
[7] USTC · Zuchongzhi 3.0 (105 q, 2Q 99.62%) · Phys. Rev. Lett. 134, 090601 · 2025 · https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.090601 [D]
[8] Google Quantum AI · Colour code on a superconducting processor (two-qubit gates ≈40% of the error budget) · Nature · 2025-05 · https://www.nature.com/articles/s41586-025-09061-4 [D]
[9] PostQuantum · "QuantWare $178 M Series B" (Intel Capital, In-Q-Tel, ETF Partners; Delft Kilofab) · trade press · 2026-05-05 · https://postquantum.com/industry-news/quantware-178m-series-b-qoa/ [P]
[10] US Bureau of Industry and Security · Quantum computing export controls (ECCN 4A906, 3A901) · Federal Register · effective 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and [G]
[11] D-Wave · "Digital control of high-coherence fluxonium qubits" (flip-chip on-chip flux DAC at 10 mK) · whitepaper 14-1090A-A · 2026-01-23 · https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf [C]
[12] Google Quantum AI · Reinforcement-learning-steered calibration during error correction (d=7 logical error 7.72×10⁻⁴ per cycle) · Nature · 2026-07 · https://www.nature.com/articles/s41586-026-10759-2 [D]
[13] Oxford Quantum Circuits newsroom · Leek Lab (University of Oxford) fixed-coupling coaxmon CZ: 99.8% in 25 ns, transmon plus inductively shunted transmon, no tunable coupler · 2025-03-21 · https://oqc.tech/company/newsroom/oxford-research-group-demonstrate-fundamental-speed-up-of-two-qubit-gate [C]
[14] IBM · US Patent 11,727,297 B2, "Tunable quantum coupler facilitating a quantum gate between qubits" · USPTO · granted 2023-08-15 · https://patents.google.com/patent/US11727297/en [G]
General facts cited above: [G:IBM-10B-2026-06], [G:IBM-ROADMAP], [G:RIGETTI-FIN-2026], [G:IQM-LISTING-2026-07], [G:OQC-SERIESC-2026-06], [G:QUANTWARE-SERIESB-2026-05], [G:QBI-STAGEB-2025-11].

## Open verification items
- Gate duration for IQM's 99.93% CZ is not stated in the preprint text retrieved; only the fidelity and the 40-hour averaging window are confirmed.
- No vendor publishes a coupler-specific yield or defect rate; only qubit and coupler counts are public.
- Independent replication of the Toshiba 99.90%/48 ns or IQM 99.93% results on separate hardware: none found as of 2026-09-04.
- Whether IBM's US 11,727,297 B2 reads on merchant coupler chips such as QuantWare's: not assessed.
- The share of IBM's fleet EPLG attributable to residual coupler-off ZZ rather than coherence or crosstalk is not separated in any public figure.
