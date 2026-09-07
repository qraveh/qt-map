---
id: ct_base
name: Baseband electrical control (spins, Majorana)
layer: "5 Control"
status: demonstrated
since: 2012
one_line: DC-to-few-GHz voltage pulses on lithographic gate electrodes drive exchange, tunnelling and parity in spin and Majorana devices, with no resonant drive.
verdict: The physics is settled and the wiring is not. HRL attributes roughly 80% of its CNOT error to control and calibration rather than the qubit, so cold co-location — not faster pulses — is the lever.
updated: 2026-09-04
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
Baseband control manipulates a qubit with DC-to-few-GHz voltage pulses on lithographic gates rather than a resonant drive: a pulse shifts the electrostatic potential, and with it the exchange coupling between dots or the tunnel coupling of a Majorana junction. The licence is old and precise: DiVincenzo, Bacon, Kempe, Burkard and Whaley showed in 2000 that the Heisenberg interaction alone suffices for universal computation, at about 3× more qubits and ~10× more two-qubit operations [S][1]. Every exchange-only architecture since pays that bill to delete microwave hardware.
- Control and placement: low-frequency voltage pulses generated warm, routed to millikelvin gates.
- Error structure: coherent and correlated, not stochastic — miscalibration is what the code sees.

## Physics & limits
Exchange coupling J depends exponentially on detuning and barrier height, so a rotation angle is the time integral of J and a small voltage error is a proportionally large angle error. There is no drive-frequency selectivity: 1/f charge noise modulates the same potential that carries the signal, and crosstalk from a neighbouring gate is indistinguishable from an intended pulse. Hence the field's most useful number — HRL measures ~80% of its CNOT error as extrinsic, in control and calibration rather than the qubit [D][G:HRL-CRYOCMOS-4K-2026]. The floor is waveform accuracy and recalibration cadence, not T₂: foundry devices reach 1.31(4) ms echo coherence [D][G:DIRAQ-8Q-2026-07] against 58 ns exchange gates [D][G:SHUTTLE-CZ-DELFT-2026-05]. Moving it means a shorter electrical path — a controller on the cold stage, ideally on-die — plus automated recalibration.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-07 | Microwave-free hopping control, 2×2 array with a micromagnet gradient: hopping-gate fidelity lower bound 99.50(6)%, echo T₂ up to ~49 µs | QuTech | [D][G:QUTECH-BASEBAND-2025-07] |
| 2026-07-29 | 18 exchange-only qubits from 54 dots, sequenced by a 4 K controller: mean 1Q error 2×10⁻⁴, mean CNOT 3×10⁻³ (best 9×10⁻⁴) | HRL | [D][G:HRL-CRYOCMOS-4K-2026] |
| 2026-07-29 | Same device, distance-5 repetition code over 200 rounds: logical error 5.0×10⁻³, Λ₅/₃ = 4.7 — bit-flip only | HRL | [D][G:HRL-2026] |

Dominant term: extrinsic control and calibration, ~80% of the CNOT budget.

## Manufacturing, materials & supply chain
The node rides ordinary CMOS: Intel's 300 mm EUV line reports over 24,000 devices per wafer at 96% tune-up yield [D][2] and Quantum Motion characterises 1,024 dots in five minutes on GlobalFoundries 22FDX [C][3]. That is the asset and the exposure: each developer sole-sources one foundry it does not own — Quobly to STMicroelectronics, Quantum Motion to GlobalFoundries, Diraq to imec — so a fab-side decision is a company-level failure mode. Room-temperature pulse generation is uncontrolled, but a controller "designed to operate at" ≤4.5 K falls under ECCN 3A901.a from the design file on [G:BIS-3A901A-CRYOCMOS]: cold integration imports export control.

## Control, readout & I/O burden
Baseband control costs about one line per gate and two to four gates per dot, so a naive 10³-qubit array wants 10³–10⁴ addressed lines from room temperature. HRL's counter-example is the number to hold: 296 lines and 366 DACs at ≤3.5 W driving 54 dots, with a 250 MHz on-chip sequencer and no room-temperature real-time electronics [D][G:HRL-CRYOCMOS-4K-2026] — ~20 DACs per qubit, cold multiplexing rather than wire elimination. At 10³ the harness is impractical without cold DACs; at 10⁴ per-qubit DAC count must fall an order of magnitude; at 10⁶ nothing exists. The binding constraint is recalibration cadence.

## Role in the stack
This is a hub. It requires nothing upstream, provides the exchange gate directly, and reaches three qubit families: quantum-dot spins (Intel, Diraq, Quantum Motion, HRL/IBM, QuTech, Quobly, Equal1), donor spins (Silicon Quantum Computing) and Majorana devices, where gate voltages tune the dots that report parity. It competes with microwave and electric-dipole spin resonance, which buys frequency selectivity at the price of antennas and heating. Its clock contribution is negligible: exchange gates run at ~58 ns [D][G:SHUTTLE-CZ-DELFT-2026-05] against 6.3 µs readout, so derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 8.5 µs here, set by readout with reset next.

## Verification (QCVV)
Fidelities come from randomised benchmarking and gate-set tomography, and the headline QuTech number is a lower bound, not a point estimate [D][G:QUTECH-BASEBAND-2025-07]. The 80% extrinsic share deserves most scrutiny: it is inferred from measured error against a modelled noise budget, not independently partitioned, and unreplicated. No spin device above 12 qubits has published all-pairs two-qubit fidelities, so simultaneous-operation crosstalk — this node's own failure mode — is uncharacterised at scale. HRL's Λ₅/₃ = 4.7 is a repetition code, bit-flip only, not below-threshold evidence, and its [[4,2,2]] fidelity of 0.95 is post-selected [D][G:HRL-2026]. On the Majorana side the control works but the qubit does not exist: parity readout is real, X-loop lifetimes ran ~1,000× shorter than Z-loop, no two-qubit operation [D][11].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| HRL Laboratories | Developer | USA | Only self-sequenced baseband QEC demonstration; acquired by IBM | [D][G:HRL-CRYOCMOS-4K-2026] |
| Diraq | Developer | Australia | SiMOS exchange qubits on imec's 300 mm line | [D][G:DIRAQ-8Q-2026-07] |
| Quantum Motion | Developer | UK | Full-stack 300 mm CMOS system at the UK NQCC | [C][G:QM-160M-2026-05] |
| QuTech | Research | Netherlands | Microwave-free hopping control, 2D array | [D][G:QUTECH-BASEBAND-2025-07] |
| Microsoft | Developer | USA | Gate-voltage-tuned parity measurement in tetrons | [D][11] |

**Money.** 2025-11-06 · Diraq, Quantum Motion, Silicon Quantum Computing · DARPA QBI Stage B · up to $15 M USD each · programme [G:QBI-STAGEB-2025-11]. 2026-05-07 · Quantum Motion · Series C · $160 M USD · DCVC, Kembara · closed [C][G:QM-160M-2026-05]. 2026-05-21 · Diraq · CHIPS letter of intent · up to $38 M USD · US Commerce · non-binding [G:CHIPS-LOI-2026-05]. 2026-06-03 · Quobly · Series A · €115 M · Bpifrance, SEALSQ, STMicro · €134 M cumulative · closed [C][G:QUOBLY-115M-2026-06]. 2026-07-23 · IBM · acquires HRL · undisclosed · announced [C][G:IBM-HRL-2026-07].

**Market & supply chain.** Nothing is sold as "baseband control"; what sells is foundry capacity, enriched ²⁸Si, and the warm waveform racks Quantum Machines dominates with over half of developers as customers [C][G:QM-SERIESC-2025-02]. Cold integration threatens that rack business, and is why IBM bought HRL. Diraq's under-$1-per-qubit figure is a target, not a cost. This node pays for G3 and G4 on the spin path, G4 on the Majorana path if a qubit appears.

**IP & standards.** No patent family specific to baseband gate-voltage control was found in a named dated database as of 4 Sep 2026. The foundational exchange-only claim is a 2000 publication, long out of patent term [S][1] — part of why this layer is crowded. IBM's HRL deal brings undisclosed controller IP in-house. No standards body governs gate-pulse interfaces today.

**Roadmaps & track record.** Diraq (2026-08-27 · 150 k physical, 1 k logical by 2029, > 2 M by 2031 · its 2026-07-09 release said "thousands by 2029") — low on messaging, real on devices [G:DIRAQ-FUNDING]. Quantum Motion (full-stack delivery · met, NQCC 2025-09-15) — the only met hardware date here. HRL/IBM (no public date · QPU delivered 2026-07-29) — strongest result here. Microsoft ("years not decades" → 2029 · no two-qubit operation) — no base.

**Strategic reading.** If baseband control scales, foundry-native platforms inherit decades of CMOS investment free while exotic-control platforms fund their own hardware forever — the argument IBM made by buying HRL. Losers are room-temperature control-rack vendors, displaced from inside the cryostat rather than out-competed on price. The live substitution question is warm versus cold placement, not baseband versus microwave drive. Bargaining power sits with the foundries: every developer above depends on a relationship it cannot replace within a product cycle.

*Open niche:* the 80% extrinsic split is a modelled inference the whole spin field quotes, and nobody has independently partitioned it. A small QCVV group could run it — interleaved benchmarking against deliberately perturbed calibrations, crosstalk-resolved tomography on a borrowed device — without owning a fab. The most load-bearing unverified number in this layer.

## Outlook & open questions
Confirm by 2027 if any developer publishes all-pairs two-qubit fidelities above 12 qubits, or an independent group reproduces the extrinsic/intrinsic split; demote if crosstalk caps arrays at ≤20 qubits through 2028. Best case 2029: cold self-sequenced control becomes default and two-qubit errors move from 3×10⁻³ toward 10⁻⁴. Worst case: calibration overhead outruns qubit count and the CMOS argument stalls at demonstration scale. Open questions: does the 80% figure survive independent measurement; can per-qubit DAC counts fall an order of magnitude; does recalibration keep pace with array size; does Majorana control ever get a qubit.

## Sources
[1] DiVincenzo, Bacon, Kempe, Burkard, Whaley · "Universal quantum computation with the exchange interaction" · Nature 408, 339; arXiv:quant-ph/0005116 · 2000 [S] — https://arxiv.org/abs/quant-ph/0005116
[2] Neyens et al. (Intel) · 300 mm quantum-dot device statistics (>24,000 devices/wafer, 96% tune-up yield) · arXiv:2410.16583 · 2024-10 [D] — https://arxiv.org/abs/2410.16583
[3] Quantum Motion · full-stack silicon CMOS quantum computer delivered to the UK NQCC · 2025-09-15 [C] — https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/
[4] HRL Laboratories · 18-qubit exchange-only SiGe processor with a 4 K cryo-CMOS controller · arXiv:2604.16216; Nature · 2026-07-29 [D] — https://arxiv.org/abs/2604.16216
[5] Unseld, Undseth, Raymenants et al. (QuTech/Delft) · "Baseband control of single-electron silicon spin qubits in two dimensions" · Nature Communications · 2025-07-01 [D] — https://www.nature.com/articles/s41467-025-60351-x
[6] Nickl, Dumoulin Stuyck, Steinacker et al. (Diraq/imec) · eight-qubit 300 mm SiMOS device · Nature Communications 17, 5878 · 2026-07-09 [D] — https://www.nature.com/articles/s41467-026-74597-6
[7] Matsumoto et al. (Vandersypen group, QuTech/Delft) · controlled-phase gate between shuttled spins, 58 ns at 1.8 m/s · Nature 653 · 2026-05-06 [D] — https://www.nature.com/articles/s41586-026-10423-9
[8] IBM Newsroom · "IBM to Acquire HRL Laboratories" · 2026-07-23 [C] — https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum
[9] DARPA · QBI Stage B selection · 2025-11-06 [G] — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[10] Diraq · utility-scale roadmap release · 2026-08-27 [C] — https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip
[11] Microsoft Azure Quantum · single-shot interferometric parity measurement in InAs–Al tetrons · Nature 638 · 2025-02-19 [D] — https://www.nature.com/articles/s41586-024-08445-2
[12] Microsoft Azure Quantum · "Majorana 2" InAs–Pb tetron, ~20 s parity switching, no two-qubit operation · arXiv:2606.03884 · 2026-06 [P] — https://arxiv.org/abs/2606.03884
[13] US Bureau of Industry and Security · interim final rule creating ECCN 3A901.a · Federal Register · 2024-09-06 [G] — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[14] Quantum Machines · Series C press release ($170 M, PSG Equity lead) · 2025-02-25 [C] — https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/

## Open verification items
The 80% extrinsic share of CNOT error is a modelled inference from HRL's noise budget, not an independent partition, and has no second-group replication.
No spin device above 12 qubits has published all-pairs two-qubit fidelities, so simultaneous-operation crosstalk is uncharacterised at scale.
The "since 2012" baseline for demonstrated baseband exchange control carries no numbered source; the 2000 exchange-only proposal is verified and cited instead.
Diraq's two 2029 targets, six weeks apart, remain unreconciled.
No dated patent-family count for baseband gate-voltage control was located in any named database.
