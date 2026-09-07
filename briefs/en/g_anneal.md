---
id: g_anneal
name: Analog annealing evolution
layer: "3 Gate mechanism"
status: demonstrated
since: 2011
one_line: Continuous-time Hamiltonian evolution (coherent quench, 3.6–27 ns) driving Ising or Rydberg spins toward a ground state; not a discrete gate.
verdict: No platform has an unchallenged advantage claim as of 4 Sep 2026; falsified if one survives a full classical-rebuttal round by 2028, confirmed non-advantage if erosion keeps repeating.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Continuous-time Hamiltonian evolution — sweeping a transverse field, laser detuning or blockade radius — carrying a many-body system toward a ground state with no discrete gate. Kadowaki–Nishimori (1998) and Farhi et al. (2000) gave it its form; D-Wave commercialised it from 2011, and Rydberg arrays run it with optics instead of flux.
Fabricated carriers; ~4 ns characteristic quench, no deterministic entangling operation; no readout of its own — a mechanism, not a qubit.
Long-range interaction; low-frequency or optical control at mK or in vacuum; coherent plus Pauli error; superconducting lithography or tweezer optics.

## Physics & limits
Two clocks bound the schedule. From below, control bandwidth — DAC slew for flux, AOM switching for Rydberg: D-Wave's fastest coherent quenches run 3.6–27 ns across 1,222–5,627 qubits [D][1]. From above, decoherence. Between them sits the adiabatic condition, which for hard instances demands time scaling inversely with the square of a gap that itself closes exponentially — so the useful regime is a fast diabatic quench whose output is a sample, not a certified minimum. Rydberg adds spontaneous emission, flux adds 1/f noise. The floor moves not with faster electronics but with a way to certify the sample.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-03 | Coherent quench 3.6–27 ns, up to 5,627 qubits; beyond-classical claim | D-Wave | [D][1] |
| 2025–26 | Claim eroded by tensor networks and t-VMC | Tindall; Mauron & Carleo | [D][2][3] |
| 2025 | 69-qubit analog-digital simulator, beyond-classical on XEB only | Google | [D][5] |
| 2025 | Aquila, 256 atoms, gauge-theory string breaking, no claim | QuEra | [D][6] |

Dominant limitation: no accepted certificate that analog output matches the Hamiltonian.

## Manufacturing, materials & supply chain
Two supply chains carry one mechanism: Nb/Al superconducting lithography (D-Wave) and vacuum/laser/AOM tweezer stacks (QuEra, Pasqal). The I/O burdens scale oppositely: flux annealers push everything through one mK stage on multiplexed on-chip DACs, while tweezer machines add laser power, deflectors and imaging per atom — the optical table is the constraint. Pasqal has begun displacing bulk optics with a silicon-nitride photonic IC: four traps from one chip, atom lifetime ~27.5 s [C][G:PASQAL-PIC-2026-08]. No export rule names analog evolution: exposure is inherited from the carrier — ECCN 4A906 and 3A904 for the flux line, nothing for tweezer optics.

## Role in the stack
Feeds analog carriers only and provides nothing to a gate-model stack; the field's standard error is reading an analog sampling claim as gate-model advantage. Quantinuum's magnetism result is quoted alongside these but is Trotterised digital simulation competing for the same budget [D][7]. No derived clock applies; the figure is quench time, ~4 ns to µs, plus one measurement. Verification is comparison against classical solvers, never randomized benchmarking, and the target moves: D-Wave's March 2025 claim was eroded within weeks [2][3], its counter arguing the tensor-network scaling used against it is unvalidated [P][4]. Unresolved as of 4 Sep 2026.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| D-Wave Quantum | developer | US/Canada | Coherent-quench annealer; the disputed claim | [D][1] |
| QuEra Computing | developer | US | Aquila Rydberg on Braket; Libra 2028 | [D][6] |
| Pasqal | developer | France | Analog Rydberg arrays; Nasdaq since 2026-08 | [P][10] |
| Google Quantum AI | developer | US | Analog-digital simulator; atom track 2026-03 | [G:GOOGLE-ATOMS-2026-03] |

**Money.** 2025-09-09 · QuEra · Series B expansion · $230 M+ USD · Google, SoftBank Vision Fund 2, NVentures · closed [C][8]. 2026-08-28 · Pasqal · SPAC merger · ~$360 M USD cash · Nasdaq PSQL · closed [P][10]. 2026-08-06 · D-Wave · H1-2026 revenue $5.9 M (−67% YoY) · reported [C][G:DWAVE-FIN-2026].

**Market & supply chain.** Rydberg buys lasers, deflectors, vacuum and cameras from a thin supplier base; flux buys foundry runs and refrigerators. Money here is G1 instrument spend plus D-Wave's hybrid-solver G5 line; G3/G4 pay nothing.

**IP & standards.** No mechanism-specific patent family or standards body apart from the carrier hardware.

**Roadmaps & track record.** (2024-01 · for 2026 · QuEra 100 logical qubits · missed, replaced by Libra 2028 at >256 logical) [R][9]; (2024 · for 2026 · Pasqal 10,000 physical · missed, restated to 2028) [P][10]; (2025-05 · for 2029 · D-Wave 20,000 qubits · open) [R][G:DWAVE-FIN-2026]. Both atom vendors slipped a flagship target by two years; only D-Wave delivers on schedule.

**Strategic reading.** If one analog claim survives a full classical round, the tweezer vendors capture the value, holding a path to digital; otherwise this is a bridge product and whoever reaches gate operation fastest wins. Laser and cryoplant suppliers keep the pricing power.

*Open niche:* Replaying published analog instances against open classical solvers needs no vendor access and settles the field's one contested question; certifying analog output is an unclaimed QCVV niche.

## Outlook & open questions
Confirm if any platform defends an unchallenged claim through 2028; demote if erosion repeats. Best case 2029: Rydberg vendors convert analog arrays into error-corrected digital machines. Worst case: analog stays a physics instrument. Open: does Pasqal reach 10,000 physical by 2028; does Libra hold at >256 logical?

## Sources
[1] King et al. (D-Wave) — "Beyond-classical computation in quantum simulation" — arXiv, published Science Mar 2025 — 2024-03-01 — https://arxiv.org/abs/2403.00910
[2] Tindall, Mortier, Stoudenmire et al. — belief-propagation tensor-network simulation of the D-Wave instances — arXiv, published Science May 2026 — 2025-03-07 — https://arxiv.org/abs/2503.05693
[3] Mauron & Carleo — t-VMC simulation of quantum annealing dynamics — arXiv — 2025-03-11 — https://arxiv.org/abs/2503.08247
[4] Nocera, Raymond, Bernoudy, Amin, King (D-Wave/UBC) — "Evaluating classical simulations with a quantum processor" — arXiv [P] — 2025-08-21 — https://arxiv.org/abs/2508.15759
[5] Google Quantum AI — 69-qubit analog-digital quantum simulator — Nature — 2025-01 — https://www.nature.com/articles/s41586-024-08460-3
[6] QuEra Computing et al. — string breaking in a lattice gauge theory on Aquila (256 atoms) — Nature — 2025 — https://www.nature.com/articles/s41586-025-09051-6
[7] Quantinuum — digital quantum simulation of magnetism — arXiv [P] — 2025-03-26 — https://arxiv.org/abs/2503.20870
[8] QuEra Computing — "QuEra expands $230 million financing round" — company newsroom [C] — 2025-09-09 — https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing
[9] QuEra Computing — "QuEra announces 2028 fault-tolerant quantum computer and expanded AWS collaboration" — company newsroom [R] — 2026-06-15 — https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[10] The Quantum Insider — "Pasqal completes SPAC merger with $360 million in cash" — trade press [P] — 2026-08-28 — https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/
[11] Google — "Neutral-atom quantum computers" (neutral-atom hardware track) — company blog [G] — 2026-03-24 — https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/

## Open verification items
QuEra's cumulative funding (">$250 M") and the fuller investor list (Valor Equity, Rakuten, Commonwealth of Massachusetts) appear only in secondary reporting; the primary release names Google, SoftBank Vision Fund 2 and NVentures on 2025-09-09. Pasqal's 2025 revenue of €16.5 M is trade-press, not a filed statement. No primary source found for the exact date of Pasqal's Aeponyx acquisition. Whether D-Wave's "most frustrated instances" survive a further classical round beyond Tindall and Mauron/Carleo.
