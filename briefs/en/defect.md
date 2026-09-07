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
Coordinates: natural defect, engineered placement, static host with a flying photon, ~1 µs gates; fluorescence readout ~100 µs, non-destructive and mid-circuit; optical plus microwave control; Pauli and loss error.

## Physics & limits
Everything rests on the chance an excited defect puts a usable photon into fibre. NV emits a few per cent into its zero-phonon line and diffuses spectrally under charge switching, so a cavity is mandatory — Delft's fibre microcavity took resonant collection from ~0.05% to ~0.5% at echo coherence above 100 µs [D][3]. Group-IV centres fix the linewidth by symmetry but pay in temperature: SiV below 100 mK, SnV nearer 1–4 K. Heralded rate goes as efficiency squared — 10× optical gain is 100× in rate; link rate, not gate error, is the figure of merit. Loss is heralded, entering the code as erasure — the one structural edge over dot and donor spins.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2024-05-15 | SiV nodes at 0.69(7) over 35 km of deployed fibre, 17 dB loss | Harvard | [D][1] |
| 2026-01-15 | fibre-microcavity photon collection ~0.05% → ~0.5% | QuTech | [D][3] |
| 2026-05-26 | unconditional teleported CNOT between cryostats, 63(4)%; GHZ 64(4)% | QuTech | [D][4] |

Local gates are not the problem: Fujitsu and QuTech report NV errors below 0.1% by gate-set tomography [P][2]. Collection dominates; no defect platform has a logical qubit.

## Manufacturing, materials & supply chain
Hosts: CVD diamond with implanted defects, or defect-engineered silicon for T centres. Element Six is the only named merchant supplier, selling DNV-B1 (2020-06-15) by catalogue — but that grade targets NV *ensembles* [C][7]; single-defect nodes need electronic-grade plates. Yield is the honest number: 2 of 327 SnV nanocavity devices exceeded cooperativity one [D][8]. Optical I/O does not multiplex — each node needs its own resonant laser, microwave line, detector and fast feed-forward [D][4], so burden scales per node and 10³ nodes is nobody's target. No ECCN names diamond.

## Role in the stack
Requires diamond growth or implantation; provides spin gating, fluorescence readout and the spin–photon link consumed upstream. The derived clock is transport-dominated by six to nine orders: ~1 µs gates against heralded links at 7.5 mHz (T centre, 40 m) to ~1 Hz (SiV, 20 m) [P][5][D][1]. Two teleported-CNOT claims coexist, one on T centres and one on NV, and *both* are right. Photonic Inc.'s T-centre tCNOT between cryostats was post-selected, no feed-forward and no gate fidelity, at Bell 0.60(8) [P][5]; QuTech's NV gate is unconditional at 63(4)% [D][4]. Only the second is a gate.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | developer | Netherlands | NV cavities, SnV yield, teleported CNOT | [D][3][4][8] |
| Photonic Inc. | developer | Canada | Silicon T-centre modules | [P][5] |
| Harvard | research | USA | SiV nodes over urban fibre | [D][1] |
| Element Six | supplier | UK | Merchant CVD diamond | [C][7] |
| Quantum Brilliance | developer | Australia | Room-temperature diamond units | [P][6] |

**Money.** 2025-11-06 · Photonic Inc. · QBI Stage B · up to USD 15 M · DARPA · awarded [G:QBI-STAGEB-2025-11]. 2026-05-12 · Photonic Inc. · equity · USD 200 M at USD 2 B · Microsoft returning · USD 350 M cumulative · closed [P][9]. 2026-07 · QuantumDiamonds · EUR 91 M, EUR 76 M of it EU Chips Act · closed [P][6].

**Market & supply chain.** Two concentration points: Element Six for substrate, a thin detector base for readout. Sensing revenue funds the field; nothing here is bought against G3 or G4.

**IP & standards.** No dated patent family from a named database as of 4 Sep 2026; Element Six's DNV grades are a de facto benchmark.

**Roadmaps & track record.** Photonic Inc. (2023-11 · fault-tolerant distributed computing "within five years" · unmet; its published rate is seven orders below its own ~200 kHz target) [P][6]. Quantum Brilliance ships rather than promises; QuTech is on schedule.

**Strategic reading.** Defect spins win only if distributed modules bind before monolithic fault tolerance does — then every platform buys this interface instead of building it. Element Six holds supplier power because it never competes on qubit design.

*Open niche:* nobody reports link metrics alike: post-selected against unconditional, per-attempt against per-second. A neutral heralded-link benchmark is a QCVV product needing no fabrication.

## Outlook & open questions
Confirm/demote (12–24 months): an unconditional inter-node gate above 90%, or a link above 1 kHz, confirms the thesis; two more years at hertz rates demotes it to sensing. Best case 2029: a multi-node repeater segment with error detection. Worst case: laboratory links only. Open: (1) does SnV yield rise above the percent level; (2) does a second merchant diamond supplier appear; (3) can T-centre rates close on SiV.

## Sources
[1] Knaut, Suleymanzade, Wei, Assumpcao, Stas, Huan, Machielse, Bhaskar, Park, Lončar, Lukin (Harvard) · "Entanglement of nanophotonic quantum memory nodes in a telecom network" · Nature 629 · 2024-05-15 · https://www.nature.com/articles/s41586-024-07252-z [D]
[2] Fujitsu and QuTech · "Fujitsu and QuTech realize high-precision quantum gates" (NV gate-set tomography below 0.1%; no primary paper located) · The Quantum Insider · 2025-03-28 · https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ [P]
[3] Fischer et al. (QuTech, Delft) · cavity-enhanced NV photon collection · Nature Communications · 2026-01-15 · https://www.nature.com/articles/s41467-025-66722-8 [D]
[4] Hanson et al. (QuTech, Delft) · "Unconditionally teleported quantum gates between remote solid-state qubit registers" · Nature Communications · 2026-05-26 · https://www.nature.com/articles/s41467-026-72818-6 [D]
[5] Photonic Inc. · "Distributed Quantum Computing in Silicon" · arXiv:2406.01704 · 2024-06-03 · https://arxiv.org/html/2406.01704v1 [P]
[6] The Quantum Insider · "Top Diamond NV-Centre Quantum Computing Companies in 2026" · 2026-07-10 · https://thequantuminsider.com/2026/07/10/8-quantum-computing-companies-working-with-nv-centre-in-diamond-technology/ [P]
[7] Element Six · "Element Six launches DNV-B1, its first commercially-available, general-purpose quantum grade diamond" · company release · 2020-06-15 · https://www.e6.com/en/about/news/dnv-b1-launch [C]
[8] QuTech · "A step toward faster quantum networks" (327 SnV nanocavity devices, 2 above cooperativity 1) · institutional release · 2026-06-25 · https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/ [D]
[9] Quantum Computing Report · "Photonic Inc. reaches $2 B valuation with $200 M final close" · 2026-05-12 · https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ [P]

## Open verification items
- The Fujitsu/QuTech "below 0.1%" NV gate error is sourced only to a joint press release relayed by trade press [2]; no peer-reviewed paper with the gate-set-tomography error bars was located, so it is tagged [P] here, not [D] as in the main report.
- Element Six publishes no capacity, revenue or quantum-segment figure; sole-supplier status rests on a secondary survey [6], and its quantum-technologies product page returned 404 on 2026-09-04.
- Photonic Inc.'s T-centre work has no journal publication as of 2026-09-04, and its tCNOT is post-selected with no gate fidelity stated [5].
- Quantum Brilliance's three deployment sites (Oak Ridge, Fraunhofer IAF, Pawsey) are named without dates [6].
