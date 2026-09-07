---
id: fluxq
name: rf-SQUID flux qubit (annealer)
layer: "1 Carrier"
status: demonstrated
since: 2011
one_line: Superconducting double-well loop used as a programmable Ising spin in D-Wave's annealers; no gate set, no code.
verdict: No D-Wave beyond-classical claim has survived rebuttal as of 4 Sep 2026; falsified if one holds through 2028, confirmed as sampler-not-solver if erosion repeats.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A superconducting loop with a compound Josephson junction: flux bias sets barrier and tilt; the two circulating-current states are an Ising spin. D-Wave's line, D-Wave One (2011) through Advantage2 (GA 2025-05-20: 4,400+ qubits, Zephyr degree-20, 12.5 kW) [P][1], rests on it. No gate set, only a programmable transverse-field Ising Hamiltonian, sampled.
Fabricated carrier; ~3 ns characteristic time, no deterministic entangling operation; dispersive readout ~1 µs, non-destructive, not mid-circuit.
Degree-20 coupling; low-frequency flux control at mK; Pauli plus coherent error; superconducting lithography.

## Physics & limits
Tunnelling amplitude and persistent current set the well. Landau–Zener demands a sweep slow against the square of the minimum gap, which for hard instances closes exponentially in size: the first floor is combinatorial, not material. The thermal floor binds sooner: at 15–20 mK kT is a few hundred MHz, so below that gap the chip equilibrates with its bath and emits a quasi-Boltzmann sample, not a ground state. 1/f flux noise dephases in the energy eigenbasis, making diabatic loss indistinguishable from a hard gap. Colder stages, larger persistent current or nanosecond quenches move the floor.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-09 | Zephyr topology, degree 20 | D-Wave | [G:DWAVE-ZEPHYR-2021] |
| 2025-03 | Beyond-classical claim — quench dynamics, not optimisation | D-Wave | [D][2] |
| 2025-05-20 | Advantage2 GA: 4,400+ qubits, 12.5 kW | D-Wave | [P][1] |
| 2025–26 | Eroded by belief-propagation tensor networks; t-VMC | Tindall et al.; Mauron & Carleo | [D][3]; [D][4] |

Dominant error: thermal excitation near the minimum gap.

## Manufacturing, materials & supply chain
Nb/Al multilayer superconducting lithography, the transmon fabs' family. The FY2024 10-K cites third-party foundries with a demonstrated second source; EDGAR returns nine SkyWater mentions in D-Wave 10-Ks 2023–26 [G:DWAVE-FAB-10K], and SkyWater is IonQ-owned since 2026-07-31 [G:IONQ-SKYWATER-2026] — that source sits inside a competitor. The real asset is I/O: multiplexed on-chip flux DACs hold room-temperature line count at O(100) for tens of thousands of qubits and couplers, versus O(qubits) for gate machines — though D-Wave quotes 200 bias wires (2026-01-06) and ~300 (whitepaper, 2026-01-23), unreconciled [C][G:DWAVE-FLUXDAC-LINECOUNT-CONFLICT]. The wall at 10⁴–10⁶ spins is minor-embedding overhead and the 12.5 kW cryoplant, not wiring. ECCN 4A906 keys on two-qubit gate error, undefined here; 3A904 refrigerators bite instead [G][9].

## Role in the stack
Serves the annealing path only and feeds no gate-model path: D-Wave's gate roadmap runs on acquired Quantum Circuits dual-rail hardware, a different carrier [C][G:DWAVE-QCI-2026-01]. The transfer runs the other way: the flux-DAC chip now drives fluxonium, key parts made at NASA JPL [C][10]. No derived clock applies, nor randomized benchmarking or quantum volume, so every headline is time-to-solution against a classical solver. The March 2025 claim was eroded within weeks [3][4]; D-Wave's counter (arXiv:2508.15759) inverts the burden, using the QPU as ground truth to argue tensor-network scaling extrapolations are unreliable [P][5]. Unresolved as of 4 Sep 2026.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| D-Wave Quantum | developer | US/Canada | Sole annealer vendor; Advantage2, Leap | [C][8] |
| US Dept of Commerce | investor | US | $100 M CHIPS letter of intent | [G:CHIPS-LOI-2026-05] |
| Anduril Industries | user | US | Stride solver on Advantage2 | [P][G:DWAVE-FAU-ANDURIL-2026-01] |
| Florida Atlantic University | user | US | $20 M campus Advantage2 | [P][6] |
| NASA JPL | supplier | US | Made flux-DAC chip parts | [C][10] |

**Money.** 2026-01-20 · D-Wave · M&A, Quantum Circuits · $550 M USD · closed [C][G:DWAVE-QCI-2026-01]. 2026-01-27 · FAU sale · $20 M USD · announced [P][6]. 2026-01-27 · QCaaS, Fortune 100 · $10 M USD · announced [C][7]. 2026-05-21 · CHIPS LOI · $100 M USD · Commerce · non-binding [G:CHIPS-LOI-2026-05]. 2026-08-06 · H1-2026 · revenue $5.9 M (−67% YoY), bookings $35.5 M (+1,120%), RPO $40.7 M · reported [C][8].

**Market & supply chain.** One vendor, one carrier, one cryoplant class; foundry capacity shared with gate-model lines. Only G1 and parts of G5 pay for it; G3/G4 cannot, absent a code layer.

**IP & standards.** 975 D-Wave quantum patent families as of 2026-06-30 [P][G:PATSNAP-2026-06]; no annealing-specific litigation or standard found.

**Roadmaps & track record.** (2025-05 · for 2029/2031 · 20,000 then 100,000 qubits · open) [R][8]. Scale milestones land on schedule; claims do not survive classical solvers; revenue collapsed while bookings and RPO rose, so monetisation is deferred, not lost.

**Strategic reading.** D-Wave wins if buyers keep paying for good-enough sampling on cheap I/O, loses if error-mitigated gate machines take the optimisation budget — which is why it bought a gate carrier. Pricing power over customers, none over foundries.

*Open niche:* Auditing annealer claims needs no vendor access: published instances and open solvers suffice. The ownable question is whether output at quoted anneal times is a coherent quench or a quasi-Boltzmann sample.

## Outlook & open questions
Confirm if a claim on a scientifically posed instance class survives a classical round through 2027; demote if erosion repeats. Best case 2029: 20,000 qubits and a defended claim; worst case, the line freezes at Advantage2 while the gate pivot absorbs the cash. Open: does any instance resist belief propagation and t-VMC?

## Sources
[1] The Quantum Insider — "D-Wave Announces General Availability of Advantage2 Quantum Computer" — trade press [P] — 2025-05-20 — https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/
[2] King et al. (D-Wave) — "Beyond-classical computation in quantum simulation" — arXiv, published Science Mar 2025 — 2024-03-01 — https://arxiv.org/abs/2403.00910
[3] Tindall, Mortier, Stoudenmire et al. — belief-propagation tensor-network simulation of the D-Wave instances — arXiv, published Science May 2026 — 2025-03-07 — https://arxiv.org/abs/2503.05693
[4] Mauron & Carleo — t-VMC simulation of quantum annealing dynamics — arXiv — 2025-03-11 — https://arxiv.org/abs/2503.08247
[5] Nocera, Raymond, Bernoudy, Amin, King (D-Wave/UBC) — "Evaluating classical simulations with a quantum processor" — arXiv [P] — 2025-08-21 — https://arxiv.org/abs/2508.15759
[6] Quantum Computing Report — "D-Wave Announces HQ Relocation, $20M System Sale, $10M Fortune 100 Deal, and Dual-Platform Advancements" — trade press [P] — 2026-01-27 — https://quantumcomputingreport.com/d-wave-announces-hq-relocation-20m-system-sale-and-defense-performance-breakthroughs/
[7] D-Wave Quantum — "$10 Million, Two-Year Enterprise QCaaS Agreement with a Fortune 100 Company" — company newsroom [C] — 2026-01-27 — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-announces-10-million-two-year-enterprise-qcaas-agreement-with-fortune-100-company/
[8] D-Wave Quantum — "D-Wave Reports Second Quarter 2026 Results" — company newsroom [C] — 2026-08-06 — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/
[9] US BIS — "Implementation of Additional Export Controls: Quantum Computing Items" (ECCN 4A906, 3A901, 3A904, 3B904) — Federal Register — 2024-09-06 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and
[10] D-Wave Quantum — "D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits" — company newsroom [C] — 2026-01-06 — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/

## Open verification items
Bias-wire count: 200 (release 2026-01-06) vs ~300 (whitepaper 14-1090A-A, 2026-01-23) — unreconciled; the whitepaper figure is tied to a described array. Exact scope of the SkyWater relationship in D-Wave's 10-Ks (nine hits, sentences not extracted). Identity of the Fortune-100 QCaaS customer and of the defence end-customer behind the Anduril/Davidson study. Whether an annealer falls inside ECCN 4A906 when the threshold is stated in two-qubit gate error — no ruling found.
