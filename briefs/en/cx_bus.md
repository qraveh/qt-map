---
id: cx_bus
name: Ion-chain motional bus (all-to-all in chain)
layer: "4 Connectivity / transport"
status: demonstrated
since: 2003
one_line: A shared collective motional mode entangles any pair in one trap, giving genuine all-to-all connectivity at the price of gate time growing with chain length.
verdict: Real all-to-all to ~30 benchmarked ions and ~100 claimed; IonQ's 10,000-ions-on-one-chip target for 2027 has no published heating, gate-time or mode-spectrum data behind it.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Ions in one trap share collective motional modes; a spin-dependent force through a shared mode entangles any pair without moving them, so connectivity is all-to-all by construction. Cirac–Zoller (1995) and Mølmer–Sørensen (1999) gave the mechanism; chain gates date from 2003.
Bus mobility, one shared mode, no transport; MEMS-adjacent trap fabrication.
No control modality or readout of its own; coherent error — mode addressing and heating, not loss.

## Physics & limits
N ions carry N motional modes in a fixed bandwidth, so mode spacing falls as ~1/N: a gate must resolve one mode spectrally, costing time, or close all with shaped pulses, costing power and calibration. Gate time therefore rises with chain length — 550–883 µs, median 672 µs, on a 30-ion chain against 110 µs for one qubit [D][2]. Electrode noise heats the shared mode, and error grows with N as every pair borrows the same excitation. Above a critical anisotropy the chain buckles into a zigzag: long chains need weak axial confinement, hence lower frequencies and slower gates. The floor moves with laser-free electronic gates (2Q 8.4×10⁻⁵ [D][3]) and shaped pulses.

## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-08 | 30-ion chain, 435 pairs benchmarked; MS 550–883 µs | IonQ Forte | [D][2] |
| 2024 | 512-ion 2D crystal, analog only | Tsinghua | [D][8] |
| 2025-10 | 2Q error 8.4×10⁻⁵, electronic gate, no cooling | IonQ/Oxford Ionics | [D][3] |
| 2026-06 | [[18,4,3]] qLDPC memory break-even, 3.95±0.68 s vs 3.3±0.9 s | IonQ | [D][6] |

Tempo: 100 ions, #AQ 64, no gate time [C][1]. Dominant term: gate time, not fidelity.

## Manufacturing, materials & supply chain
IonQ closed its SkyWater acquisition on 2026-07-31, naming microfabricated-trap fabs in Minnesota, Florida and Texas, no wafer size or node disclosed [C][G:IONQ-SKYWATER-FAB-2026]. Control splits two ways: laser MS gates need several wavelengths and per-ion optics; electronic gates use on-chip current and microwave lines. At 10³ ions the wall is the mode spectrum, not wiring: the answer is many short chains joined by shuttling or photonics — IonQ's first two-system entanglement (2026-04-14) disclosed no rate or fidelity [C][G:IONQ-PHOTONIC-INTERCONNECT-2026-04]. Export exposure is by qubit count under ECCN 4A906; no rule names ion traps [G][12].

## Role in the stack
Requires nothing; provides the non-local checks bivariate-bicycle qLDPC and high-rate transversal codes assume, as IonQ's [[18,4,3]] break-even memory shows [D][6]. It competes with QCCD shuttling, which buys chain length with transport time: Helios gets all-to-all from a ring plus junction at ~55 ms per full-width layer, transport ~60% of H2 runtime [D][7]. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 1.5×10⁻³ s, gate layers 1.4 ms of it. Verification: Forte's figure is an all-pairs benchmark over 435 pairs, so position effects are visible; Tempo publishes #AQ 64 and "99.9% fidelity" with no gate time or per-pair data — a disclosure gap, not a dispute.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| IonQ | developer | US | Forte and Tempo chains; owns SkyWater | [C][1] |
| Oxford Ionics | developer | UK | Electronic laser-free gates; IonQ unit | [D][3] |
| Quantinuum | developer | US/UK | Rival transport architecture | [D][7] |
| eleQtron | developer | Germany | MAGIC microwave ion control | [C][11] |

**Money.** 2025-09-17 · IonQ · M&A, Oxford Ionics · $1.075 B USD · closed [G:IONQ-OXIONICS-2025]. 2025-10-12 · IonQ · equity · $2.0 B USD at $93/share · closed [G:IONQ-EQUITY-2025]. 2025-11-06 · DARPA · QBI Stage B · up to $15 M each · IonQ and Quantinuum among eleven [G][10]. 2026-05-05 · eleQtron · Series A · €57 M · closed [C][11]. 2026-07-31 · IonQ · M&A, SkyWater · ~$1.8 B USD · closed [G:IONQ-SKYWATER-2026]. 2026-08 · IonQ · Q2-2026 revenue $80.1 M (+287% YoY), cash $3.0 B [C][4].

**Market & supply chain.** The bus buys a trap chip, lasers or microwave lines and one vacuum system; concentration risk sits with narrowband laser and AOM vendors, whom electronic gates remove. It pays into G3 and G5.

**IP & standards.** PatSnap names IonQ the filing leader on motional-mode engineering [P][G:PATSNAP-IONQ-PATENTS-2026]; no standards body.

**Roadmaps & track record.** (2025-06 · for 2026 · 256 qubits at 99.99% · slipped to H1 2027); (for 2027 · 10,000 on one chip · no heating data); (for 2030 · 2 M physical) [R][9]. Fidelity claims land, scale dates do not: the 2020 roadmap promised 4,000 qubits by 2026, missed ~40×.

**Strategic reading.** If chain all-to-all holds to a few hundred ions, ion vendors keep the connectivity advantage that makes high-rate codes cheap, and IonQ's owned fabs speed trap iteration. If not, the bus is a module-internal detail and value moves to interconnects.

*Open niche:* An all-pairs benchmark of a large chain, reporting fidelity and gate time by ion position, is publishable QCVV using only cloud access.

## Outlook & open questions
Confirm if IonQ publishes Tempo gate times and per-pair fidelities, or ships 256 qubits in H1 2027; demote if disclosure stays headline-only. Best case 2029: electronic gates on owned-fab traps carry chains past 100 ions. Worst case: chains stall near 30–50 ions. Open: how does mode heating scale at 100 ions?

## Sources
[1] IonQ — Tempo system page — company product page [C] — accessed 2026-09-04 — https://ionq.com/quantum-systems/tempo
[2] IonQ — benchmarking a 30-ion chain over all 435 pairs (Forte) — arXiv [D] — 2023-08-09 — https://arxiv.org/abs/2308.05071
[3] IonQ / Oxford Ionics — 2Q error 8.4×10⁻⁵ with electronic gates — arXiv [D] — 2025-10-20 — https://arxiv.org/abs/2510.17286
[4] IonQ — "IonQ announces record second quarter 2026 revenues, growing 287% YoY" — company newsroom [C] — 2026-08 — https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy
[5] IonQ — "IonQ completes acquisition of SkyWater Technology" — company newsroom [C] — 2026-07-31 — https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
[6] Tham, Goldman, Debnath et al. (IonQ) — "Breakeven demonstration of quantum low-density parity-check codes" — arXiv [D] — 2026-06-04 — https://arxiv.org/abs/2606.06455
[7] Quantinuum — Helios system paper — arXiv [D] — 2025-11 — https://arxiv.org/abs/2511.05465
[8] Tsinghua — 512-ion two-dimensional crystal for analog simulation — Nature [D] — 2024 — https://www.nature.com/articles/s41586-024-07459-0
[9] IonQ — accelerated roadmap — company blog [R] — 2025-06-13 — https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality
[10] DARPA — QBI Stage B selection — official [G] — 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[11] eleQtron — €57 M Series A — company newsroom [C] — 2026-05-05 — https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/
[12] US BIS — "Implementation of Additional Export Controls: Quantum Computing Items" (ECCN 4A906) — Federal Register [G] — 2024-09-06 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and

## Open verification items
Tempo's 2Q gate time and per-pair fidelity: not published; only #AQ 64 and a "99.9% fidelity" headline. KISTI's Tempo-100 contract value: undisclosed in the sources found, so the deployment is omitted from the ledger. No published heating, mode-spectrum or interconnect data reconciles IonQ's 10,000-ions-on-one-chip 2027 target with the chain-length trade-off. The 100-ion Tempo chain is a company claim; the largest independently benchmarked chain remains 30 ions.
