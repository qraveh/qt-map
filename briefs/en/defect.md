---
id: defect
name: Colour-centre / defect spin (NV, SiV, SnV, T)
layer: 1 Carrier
status: demonstrated
since: 2004
one_line: An optically addressable point-defect spin in diamond or silicon whose electron couples coherently to a photon, making it a network node with a small nuclear register rather than a processor qubit.
verdict: The best spin–photon interface in solid state, but link rates of millihertz to hertz keep every actor in networking and sensing; no defect platform has a logical qubit or a dated processor roadmap.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A point defect — nitrogen-vacancy, the group-IV silicon- and tin-vacancies in diamond, or silicon's T centre — read by fluorescence and entangled with an emitted photon, nearby nuclei as a small memory. Coherent single-spin control dates to 2004. The split that matters is symmetry: NV is polar and spectrally unstable, unlike SiV, SnV and the T centre.
Attributes: natural defect, engineered placement, static host with a flying photon, ~1 µs gates; fluorescence readout ~100 µs, non-destructive and mid-circuit; optical plus microwave control; Pauli and loss error.

## Physics & limits
Everything rests on the chance an excited defect puts a usable photon into fibre. NV emits a few per cent into its zero-phonon line and diffuses spectrally under charge switching, so a cavity is mandatory — Delft's fibre microcavity took resonant collection from ~0.05% to ~0.5% at echo coherence above 100 µs [D][291]. Group-IV centres fix the linewidth by symmetry but pay in temperature: SiV below 100 mK, SnV nearer 1–4 K. Heralded rate goes as efficiency squared — 10× optical gain is 100× in rate; link rate, not gate error, is the figure of merit. Loss is heralded, entering the code as erasure — the one structural edge over dot and donor spins.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2024-05-15 | SiV nodes at 0.69(7) over 35 km of deployed fibre, 17 dB loss | Harvard | [D][177] |
| 2026-01-15 | fibre-microcavity photon collection ~0.05% → ~0.5% | QuTech | [D][291] |
| 2026-05-26 | unconditional teleported CNOT between cryostats, 63(4)%; GHZ 64(4)% | QuTech | [D][292] |

Local gates are not the problem: Fujitsu and QuTech report NV errors below 0.1% by gate-set tomography [P][176]. Collection dominates; no defect platform has a logical qubit.

## Manufacturing, materials & supply chain
Hosts: CVD diamond with implanted defects, or defect-engineered silicon for T centres. Element Six is the only named merchant supplier, selling DNV-B1 (2020-06-15) by catalogue — but that grade targets NV *ensembles* [C][293]; single-defect nodes need electronic-grade plates. Yield is the honest number: 2 of 327 SnV nanocavity devices exceeded cooperativity one [D][294]. Optical I/O does not multiplex — each node needs its own resonant laser, microwave line, detector and fast feed-forward [D][292], so burden scales per node and 10³ nodes is nobody's target. No ECCN names diamond.

## Role in the stack
Requires diamond growth or implantation; provides spin gating, fluorescence readout and the spin–photon link consumed upstream. The derived clock is transport-dominated by six to nine orders: ~1 µs gates against heralded links at 7.5 mHz (T centre, 40 m) to ~1 Hz (SiV, 20 m) [P][295][D][177]. Two teleported-CNOT claims coexist, one on T centres and one on NV, and *both* are right. Photonic Inc.'s T-centre tCNOT between cryostats was post-selected, no feed-forward and no gate fidelity, at Bell 0.60(8) [P][295]; QuTech's NV gate is unconditional at 63(4)% [D][292]. Only the second is a gate.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | developer | Netherlands | NV cavities, SnV yield, teleported CNOT | [D][291], [292], [294] |
| Photonic Inc. | developer | Canada | Silicon T-centre modules | [P][295] |
| Harvard | research | USA | SiV nodes over urban fibre | [D][177] |
| Element Six | supplier | UK | Merchant CVD diamond | [C][293] |
| Quantum Brilliance | developer | Australia | Room-temperature diamond units | [P][296] |

**Money.** 2025-11-06 · Photonic Inc. · QBI Stage B · up to USD 15 M · DARPA · awarded [G:QBI-STAGEB-2025-11]. 2026-05-12 · Photonic Inc. · equity · USD 200 M at USD 2 B · Microsoft returning · USD 350 M cumulative · closed [P][160]. 2026-07 · QuantumDiamonds · EUR 91 M, EUR 76 M of it EU Chips Act · closed [P][296].

**Market & supply chain.** Two concentration points: Element Six for substrate, a thin detector base for readout. Sensing revenue funds the field; nothing here is bought against G3 or G4.

**IP & standards.** No dated patent family from a named database as of 4 Sep 2026; Element Six's DNV grades are a de facto benchmark.

**Roadmaps & track record.** Photonic Inc. (2023-11 · fault-tolerant distributed computing "within five years" · unmet; its published rate is seven orders below its own ~200 kHz target) [P][296]. Quantum Brilliance ships rather than promises; QuTech is on schedule.

**Strategic reading.** Defect spins win only if distributed modules bind before monolithic fault tolerance does — then every platform buys this interface instead of building it. Element Six holds supplier power because it never competes on qubit design.

*Open niche:* nobody reports link metrics alike: post-selected against unconditional, per-attempt against per-second. A neutral heralded-link benchmark is a QCVV product needing no fabrication.

## Outlook & open questions
Confirm/demote (12–24 months): an unconditional inter-node gate above 90%, or a link above 1 kHz, confirms the thesis; two more years at hertz rates demotes it to sensing. Best case 2029: a multi-node repeater segment with error detection. Worst case: laboratory links only. Open: (1) does SnV yield rise above the percent level; (2) does a second merchant diamond supplier appear; (3) can T-centre rates close on SiV.

## Sources
[160] M. Abdel-Kareem, “Photonic Inc. Reaches $2B Valuation with $200M Final Close,” Quantum Computing Report, May 12, 2026. [Online]. Available: https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ [P]
[176] M. Swayne, “Fujitsu And QuTech Realize High-Precision Quantum Gates,” The Quantum Insider, Mar. 28, 2025. [Online]. Available: https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ [P]
[177] C. M. Knaut *et al.*, “Entanglement of nanophotonic quantum memory nodes in a telecom network,” *Nature*, vol. 629, no. 8012, pp. 573–578, May 2024, doi: [10.1038/s41586-024-07252-z](https://doi.org/10.1038/s41586-024-07252-z). [D]
[291] J. Fischer *et al.*, “Spin-photon correlations from a Purcell-enhanced diamond nitrogen-vacancy center coupled to an open microcavity,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11680, Nov. 2025, doi: [10.1038/s41467-025-66722-8](https://doi.org/10.1038/s41467-025-66722-8). [D]
[292] M. Iuliano *et al.*, “Unconditionally teleported quantum gates between remote solid-state qubit registers,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 4694, May 2026, doi: [10.1038/s41467-026-72818-6](https://doi.org/10.1038/s41467-026-72818-6). [D]
[293] Element Six, “Element Six launches DNV-B1™ – its first commercially-available, general-purpose quantum grade diamond,” Jun. 15, 2020. [Online]. Available: https://www.e6.com/en/about/news/dnv-b1-launch [C]
[294] QuTech, “Coherent coupling of diamond colour centre to a nanocavity,” Jun. 25, 2026. [Online]. Available: https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/ [D]
[295] F. Afzal *et al.*, “Distributed Quantum Computing in Silicon,” [arXiv:2406.01704](https://arxiv.org/abs/2406.01704), Jun. 2024. [P]
[296] M. U. Rehman, “Top Diamond NV-Centre Quantum Computing Companies in 2026,” The Quantum Insider, Jul. 10, 2026. [Online]. Available: https://thequantuminsider.com/2026/07/10/8-quantum-computing-companies-working-with-nv-centre-in-diamond-technology/ [P]

## Open verification items
- The Fujitsu/QuTech "below 0.1%" NV gate error is sourced only to a joint press release relayed by trade press [176]; no peer-reviewed paper with the gate-set-tomography error bars was located, so it is tagged [P] here, not [D] as in the main report.
- Element Six publishes no capacity, revenue or quantum-segment figure; sole-supplier status rests on a secondary survey [296], and its quantum-technologies product page returned 404 on 2026-09-04.
- Photonic Inc.'s T-centre work has no journal publication as of 2026-09-04, and its tCNOT is post-selected with no gate fidelity stated [295].
- Quantum Brilliance's three deployment sites (Oak Ridge, Fraunhofer IAF, Pawsey) are named without dates [296].
