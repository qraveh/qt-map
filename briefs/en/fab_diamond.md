---
id: fab_diamond
name: Diamond growth / implantation (NV, SiV, SnV)
layer: "10 Manufacturing"
tier: 3
status: demonstrated
since: 2010
one_line: Plasma CVD growth of single-crystal diamond, ion implantation and annealing to form NV, SiV or SnV centres, and undercut etching to build the nanophotonics around them.
verdict: Two independent lotteries — where the ion stops and how the cavity lands on it — multiply into single-digit device yield; 2 of 327 SnV cavities above cooperativity one is the honest state of the art.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Plasma CVD grows single-crystal diamond on a seed; nitrogen, silicon or tin is implanted; a high-temperature anneal mobilises vacancies that bind the impurity into a colour centre; the optical structure is then cut from the bulk. That last step is the defining constraint: there is no diamond-on-insulator wafer and no sacrificial layer, so cavities are released by undercut etching of the same crystal that hosts the defect. Implantation-based fabrication matured around 2010; QuTech's 2026 SnV study sets the benchmark [D][1].
Coordinates: engineered placement of a natural defect, no mobility and no control step, Pauli error once fabricated, diamond fabrication with no CMOS analogue.

## Physics & limits
Three independent things must go right at one site. The ion must stop where intended: straggle is tens of nanometres, an order worse than STM donor placement. It must convert into an optically good centre — only a fraction take the wanted charge state, and residual damage broadens the line. Then the etched cavity must put its field maximum on that centre: cooperativity goes as g²/κγ, with g set by position inside a mode a few hundred nanometres across. Multiply three partial yields: 2 of 327 devices above cooperativity one [D][1]. Only deterministic single-ion implantation with event detection, or in-growth delta doping with registration, moves that floor; neither exists at device scale.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2024-05-15 | implanted SiV nanophotonic nodes at 0.69(7) over 35 km of fibre | Harvard | [D][4] |
| 2026-01-15 | fibre microcavity around a bulk NV raises collection ~0.05% → ~0.5% | QuTech | [D][6] |
| 2026-06-25 | 327 SnV nanocavity devices on two chips, 2 above cooperativity one | QuTech | [D][1] |

Dominant term: device yield. The fibre microcavity is a fabrication answer as much as an optical one: the resonator sits outside the crystal, removing the undercut-etch lottery.

## Manufacturing, materials & supply chain
Element Six is the only named merchant supplier, selling plates by catalogue; its DNV-B1 grade (2020-06-15) targets NV *ensembles*, while single-defect work needs electronic-grade single crystal [C][2]. Growth capacity sits in the UK and California, no second source found [C][2]. Implantation runs on general-purpose accelerators; ¹²C-enriched growth costs more. Nothing is on a 300 mm path: millimetre-scale plates processed individually, with no published wafer count, cost or throughput. No ECCN names diamond growth or colour centres, so export exposure is nil. Burden passed upward: a laser and a detector per site.

## Role in the stack
Provides the host crystal colour-centre spins and their gates require, hence the defect-node path. It is the counterpart of STM hydrogen lithography, not a substitute: implantation buys area throughput at two orders of placement precision, and neither route publishes a yield distribution. Verification: the 327-device figure is one institution, in a news release rather than a peer-reviewed paper as of 4 Sep 2026, with nothing to replicate it against.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | research | Netherlands | SnV nanocavity fabrication, yield data | [D][1] |
| Element Six | supplier | UK | Merchant CVD diamond plates | [C][2] |
| Harvard | research | USA | Implanted SiV nanophotonics | [D][4] |
| Quantum Brilliance | developer | Australia | Room-temperature units | [P][3] |
| QuantumDiamonds | developer | Germany | NV microscopy, Munich | [P][3] |

**Money.** 2026-07 · QuantumDiamonds · grant and equity · EUR 91 M, EUR 76 M of it EU Chips Act · financing a EUR 152 M Munich facility · closed [P][3]. 2025-01 · Quantum Brilliance · Series A · USD 20 M · ~USD 58 M cumulative · closed [P][3]. No QBI stage names diamond manufacturing.

**Market & supply chain.** One substrate supplier with no second source is the concentration risk; accelerators and etch tools are generic. Unit economics are unpublished. Pays into G6 and sensing.

**IP & standards.** No dated patent family from a named database as of 4 Sep 2026; Element Six's DNV grades are a de facto benchmark.

**Roadmaps & track record.** QuTech (modular-computing programme · on schedule) [D][1]. QuantumDiamonds (Munich facility, 2026-07 · too new to judge) [P][3]. Quantum Brilliance (units at three laboratories · delivered, dates unstated) [P][3]. No actor publishes a dated yield target.

**Strategic reading.** Element Six wins in every scenario: it sells substrate to actors who compete with each other, not it. The fibre microcavity is the quiet threat — a resonator outside the crystal removes most of the nanofabrication problem.

*Open niche:* every laboratory reports yield on its own terms. A common definition — cooperativity, linewidth and coherence measured alike over a stated device population — is a measurement standard a small QCVV company can sell without a fab.

## Outlook & open questions
Confirm/demote (12–24 months): deterministic single-ion implantation with event detection, or percent-level cooperativity yield, confirms; two more years at sub-percent demotes this to a research process. Best case 2029: chip-scale arrays with tens of usable nodes. Worst case: every node stays hand-selected. Open: (1) can implantation precision approach one nanometre; (2) does a second merchant supplier appear; (3) does external-cavity coupling displace monolithic nanophotonics.

## Sources
[1] QuTech · "A step toward faster quantum networks" (327 SnV nanocavity devices on two chips, 2 above cooperativity one; funders listed) · institutional release · 2026-06-25 · https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/ [D]
[2] Element Six · "Element Six launches DNV-B1, its first commercially-available, general-purpose quantum grade diamond" (NV-ensemble grade; UK and California production) · company release · 2020-06-15 · https://www.e6.com/en/about/news/dnv-b1-launch [C]
[3] The Quantum Insider · "Top Diamond NV-Centre Quantum Computing Companies in 2026" · 2026-07-10 · https://thequantuminsider.com/2026/07/10/8-quantum-computing-companies-working-with-nv-centre-in-diamond-technology/ [P]
[4] Knaut, Suleymanzade, Wei, Assumpcao, Stas, Huan, Machielse, Bhaskar, Park, Lončar, Lukin (Harvard) · "Entanglement of nanophotonic quantum memory nodes in a telecom network" · Nature 629 · 2024-05-15 · https://www.nature.com/articles/s41586-024-07252-z [D]
[5] Fujitsu and QuTech · "Fujitsu and QuTech realize high-precision quantum gates" (NV gates below 0.1% on implanted registers; no primary paper located) · The Quantum Insider · 2025-03-28 · https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ [P]
[6] Fischer et al. (QuTech, Delft) · cavity-enhanced NV photon collection with a fibre microcavity · Nature Communications · 2026-01-15 · https://www.nature.com/articles/s41467-025-66722-8 [D]

## Open verification items
- The 327-device SnV yield is published as an institutional news item [1]; the underlying peer-reviewed paper was not located, so the figure is single-source and unreplicated.
- Element Six's quantum-technologies product page returned 404 on 2026-09-04; no dated capacity, revenue or investment figure specific to its quantum segment was found, and its sole-supplier status rests on a secondary survey [3].
- Implantation straggle is stated as tens of nanometres from platform convention, not from a dated measurement in the sources used; no source gives an ion-to-usable-centre conversion yield.
- No cost per device, wafer count or throughput figure exists for any diamond quantum process.
- The main report's front-matter framing "327 SnV devices, cooperativity > 1" is corrected here: 2 of 327 devices exceeded cooperativity one.
