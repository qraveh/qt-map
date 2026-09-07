---
id: ic_mcm
name: Multi-chip modules / l-couplers (same cryostat)
layer: "9 Interconnect"
status: emerging
since: 2025
one_line: Splitting a superconducting processor across several dies inside one cryostat, joined by bump-bonded chiplet links or metre-scale superconducting l-couplers.
verdict: Chiplet tiling ships and costs fidelity — 99.5% at four chiplets, 99.1% at twelve; l-couplers have no published fidelity. Demote if no two-module entangling figure by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A multi-chip module partitions one processor across several superconducting dies sharing a single dilution refrigerator, with quantum-coherent links between them. Two different links wear the label. The short one is a chiplet join: dies flip-chip mounted on a common carrier at sub-millimetre pitch, coupled through indium bumps or vacuum-gap capacitors, so an inter-die coupler is electrically a slightly longer on-chip coupler. The long one is IBM's "l-coupler", a superconducting cable of centimetre-to-metre length carrying a microwave mode between separately packaged modules under one mixing chamber. Both differ from inter-fridge links, which cross a room-temperature gap, and from on-chip long-range couplers, which never leave the die.

Lineage: Rigetti entangled qubits across four separate silicon dies in 2021-03, iSWAP 99.1 ± 0.5% and CZ 98.3 ± 0.3%, with a Bell violation between dies [D][5]; SUSTech linked five modules with aluminium coaxial interconnects in 2023-02 [D][6]; IBM says l-couplers were "first demonstrated in 2024" on Flamingo [C][2]. The graph record dates the node to 2025, when tiling became a shipped product rather than a demonstration.

Coordinates. Affinity: fully fabricated, a packaging structure with no natural counterpart. Characteristic time and determinism: not applicable — the node carries no entangling primitive, it inherits the gate it transports. Readout: none. Mobility: long-range, the property it exists to supply. Control: microwave at millikelvin. Error structure as the code sees it: coherent. Manufacturing: superconducting lithography plus packaging steps.

## Physics & limits

The short-link floor is frequency crowding, not loss. Each chiplet is a separate fabrication instance with its own junction-resistance distribution, so tiling k dies convolves k frequency distributions that were never co-targeted; collisions between qubit, coupler and inter-die modes are fixed at packaging time and cannot be tuned away. Hence the coherent error structure: a mis-set detuning is a deterministic phase, not a stochastic click. The bonds themselves are benign — multi-chip tunable couplers built from vacuum-gap capacitors or indium bumps reported two-qubit fidelity "at the same level" as a single-chip tunable coupler, with no coherence penalty from one or more bonds [D][9].

The long-link floor is cable loss and mode density. A metre-scale cable is a multimode resonator whose free spectral range is of order 100 MHz, so tens of modes fall in the 3–5.5 GHz band the qubits use [D][8]. Loss sets transfer error: at an internal quality factor of 1.24 × 10⁶ on an indium press-mold cable-to-chip join, photon lifetime is Q/ω ≈ 49 µs, so a 100 ns inter-module SWAP costs about 2 × 10⁻³ [S][8]. Joins dominate in practice — contact resistances of 6 × 10⁻⁴ Ω at an inner-conductor splice and 8.5 × 10⁻⁴ Ω cable-to-chip are the measured levers [D][8].

Underneath both is a yield argument: monolithic yield falls as y^N in qubit count, and tiling k chiplets of n qubits replaces one exponential with k smaller ones plus an assembly step. The price shows in the only shipped data, 99.5% at four chiplets against 99.1% at twelve [C][3][4]. Moving the floor needs co-targeted junction trimming across a chiplet set [D][G:ABAA-2024-08] and joins whose loss and mode comb stay out of the way.

## Engineering state of the art

Best demonstrated as of 2026-09-03: inter-module SWAP at the 99% level in under 100 ns between two modules in one cryostat, remote-entanglement error near 1% [D][7]. Typical at scale: Rigetti's Cepheus-1-108Q, 108 qubits from twelve 9-qubit chiplets, median two-qubit 99.1%, single-qubit 99.9%, ~60 ns gates [C][3]. No l-coupled processor exists; IBM's 2026 milestone is two coupled cryogenic cells with no qubits in them [C][1].

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-03 | iSWAP 99.1 ± 0.5%, CZ 98.3 ± 0.3% across four dies; Bell violation | Rigetti | [D][5] |
| 2023-02 | five modules on Al coax, Q 8.1 × 10⁵, transfer and Bell 99%, 12-qubit GHZ 55.8 ± 1.8% | SUSTech | [D][6] |
| 2024-09 | indium cable-to-chip join, Q 1.24 × 10⁶, contact resistance 8.5 × 10⁻⁴ Ω | academic | [D][8] |
| 2025-06 | inter-module SWAP 99% in < 100 ns, remote entanglement error ≈ 1% | Illinois | [D][7] |
| 2025-07-16 | 36 qubits, four chiplets, median 2Q 99.5%, 2× error cut vs Ankaa-3 | Rigetti | [C][4] |
| 2026-04-07 | 108 qubits, twelve chiplets, median 2Q 99.1% | Rigetti | [C][3] |
| 2026-08-19 | two cryogenic cells coupled; 0.53 m² wiring, 2.75 m³ vacuum per cell | IBM | [C][1] |

The dominant term is not the interconnect. Rigetti's own comparison isolates it: same chiplet, same join, three times as many, 40 basis points of two-qubit fidelity lost [C][3][4]. Nothing published attributes that loss, which makes frequency targeting across a tiled set the leading suspect and the leading unknown.

## Manufacturing, materials & supply chain

Superconducting lithography plus a packaging line: flip-chip bonding, indium bumps or press-mold joins, through-silicon vias, a carrier. IBM builds on 300 mm at Albany NanoTech [C][G:IBM-LOON-2025-11]; QuantWare sells 3D vertical integration as a product — a stack of chiplet modules with chip-to-chip connections targeting 10,000 qubits, first delivery 2028, with a Kilofab in Delft opening 2026 to raise capacity 20× [P][10][G:QUANTWARE-VIO]. Rigetti fabricates 9-qubit chiplets on its own line [C][4].

The single points of failure sit outside the fab. The cryostat is one: IBM's cell architecture is a bespoke refrigerator programme, and the merchant alternative is Bluefors' KIDE, quoted at more than 4,000 RF lines and "over 1000 qubits" on nine pulse tubes [C][G:BLUEFORS-KIDE]. Bump-bond and TSV capacity for superconducting stacks sits with a handful of lines — Albany, Kilofab, GlobalFoundries under its CHIPS letter of intent [G:CHIPS-LOI-2026-05], SkyWater now inside IonQ [G:IONQ-SKYWATER-2026]. Export exposure is direct: cryogenic refrigerators fall under ECCN 3A904 and quantum computers of ≥ 34 qubits under 4A906 in the BIS rule of 2024-09-06 [G:BIS-3A901A-CRYOCMOS], so module and fridge are controlled together.

## Control, readout & I/O burden

Packaging does not reduce lines per qubit; it relocates them and buys wiring area. Rigetti's 108-qubit system remains per-qubit coax [C][3]. At 10³ qubits one merchant cryostat suffices — KIDE's 4,000-plus RF lines cover it [C][G:BLUEFORS-KIDE]. At 10⁴ the choice is 40,000 lines through vertical I/O, QuantWare's 2028 promise [P][G:QUANTWARE-VIO], or cold multiplexing. At 10⁶ neither works: many cells plus on-chip control generation, whose published pointer is millikelvin SFQ control at 1Q > 99% [G:SEEQC-2026].

Latency is not the l-coupler's problem — the demonstrated inter-module SWAP is under 100 ns [D][7] against readout of roughly 0.5 µs. The decoder is: cross-module syndrome extraction must close inside a ~1 µs cycle while a parity check spans two packages, and no such demonstration exists as of 2026-09-03. NVQLink's 3.84 µs round trip [P][G:NVQLINK-2025] is a host-QPU budget, far too slow for an intra-cryostat check.

## Role in the stack

Three platform paths use it: superconducting transmons, superconducting bosonic cat/GKP, superconducting dual-rail erasure. It requires superconducting-qubit lithography with multilayer routing and flip-chip packaging. It replaces inter-fridge cryogenic links, and the price is thermal: everything shares one cooling budget and one vacuum, so scaling stops at the fridge rather than at the network. Its contribution is manufacturability, not gate physics.

Off-diagonal reading: a fabricated carrier acquiring far-range connectivity through packaging, where atoms and ions acquire it through motion. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path: 0.65 µs, readout at 282 ns its largest term, and the < 100 ns inter-module SWAP [D][7] is under 15% of the round, so transport does not bind. Neighbouring empty slots: cross-module error correction, and a qLDPC code whose checks span modules — compilation for such machines exists only in simulation [S][14].

## Verification (QCVV)

Rigetti's 99.1% and 99.5% are company medians without error bars or a stated protocol [C][3][4]; the 2021 die-to-die numbers carry explicit uncertainties [D][5]. SUSTech's 99% is a state-transfer and Bell-state fidelity, not a gate fidelity, and its 12-qubit GHZ at 55.8 ± 1.8% shows what five linked modules do at depth [D][6]. The Illinois figure is a SWAP *efficiency* with a separately stated ~1% error called threshold-level; the two should not be conflated [D][7]. IBM's coupled-cell result contains no qubits and no fidelity claim [C][1]. No value conflicts were found; the gap is that nothing explains the 99.5% → 99.1% step.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IBM | developer | US | l-couplers between modules; modular cryogenic cells; Cockatoo 2027, Starling 2029 | [C][1][2] [G:IBM-ROADMAP] |
| Rigetti | developer | US | only shipped multi-chip system: 4- and 12-chiplet processors | [C][3][4] [G:RIGETTI-FIN-2026] |
| QuantWare | supplier | Netherlands | merchant 3D-integrated chiplet stacks; VIO-40K, Kilofab Delft | [P][10] [G:QUANTWARE-VIO] |
| SUSTech | research | CN | five-module aluminium-coax interconnect network | [D][6] |
| Univ. of Illinois Urbana-Champaign | research | US | interchangeable modules, 99% inter-module SWAP < 100 ns | [D][7] |
| Bluefors | supplier | FI | KIDE platform, > 4,000 RF lines, the merchant multi-module fridge | [C][G:BLUEFORS-KIDE] |
| GlobalFoundries | supplier | US | multi-modality foundry under CHIPS letter of intent, $375 M | [G:CHIPS-LOI-2026-05] |
| DARPA | investor | US | QBI Stage B funds IBM's modular path; Rigetti not on the list | [G:QBI-STAGEB-2025-11] |

**Money.**
- 2025-11-06 · IBM · DARPA QBI Stage B selection · up to $15 M each · DARPA · announced [G:QBI-STAGEB-2025-11]
- 2026-05-05 · QuantWare · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners, no single lead · cumulative > $210 M · closed [P][G:QUANTWARE-SERIESB-2026-05]
- 2026-05-21 · Rigetti · CHIPS letter of intent · up to $100 M · Dept of Commerce, within a $2.013 B package (GlobalFoundries $375 M, IBM/Anderon $1 B) · LOI, non-binding [G:CHIPS-LOI-2026-05]
- 2026-07-31 · IonQ · acquisition of SkyWater Technology · ~$1.8 B at announcement · closed [G:IONQ-SKYWATER-2026]
- 2026-08 · Rigetti · Q2-2026 results · revenue $5.1 M, GAAP loss $52.6 M, cash $541.3 M · reported [G:RIGETTI-FIN-2026]

**Market & supply chain.** No one sells an l-coupler; it is a captive design block. The merchant layer is one company deep — QuantWare is the only vendor selling 3D-integrated multi-chip QPUs to third parties [P][10] — plus Bluefors for the enclosure and a short list of lines that can do superconducting flip-chip at volume. Who pays: G3 and G4 above all, since Starling depends on modules rather than a bigger die; G7 for deployable multi-cell systems; G2 through wider processors.

**IP & standards.** IBM holds US 12,517,856, "Modular quantum system with discrete levels of connectivity" (filed 2022-09-28, granted 2026-01-06), and US 12,587,192 on chains of resonators with tunable inductive couplers (granted 2026-03-24) [G:LRCOUPLER-PATENTS] — the l-coupler is patented before it is published. For Rigetti's chiplet packaging and QuantWare's vertical I/O, no dated patent fact was found within budget. There is no inter-module interface standard and no open-source packaging stack.

**Roadmaps & track record.**
- IBM: promised 2025-06-10 · l-couplers demonstrated on Flamingo in 2024 · claimed delivered, no public number as of 2026-09-03 [C][2].
- IBM: promised 2025-06-10 · Cockatoo 2027, entanglement between modules via the universal adapter; Nighthawk on nine l-coupled modules for 1,080 qubits by 2028 · pending [R][2] [G:IBM-ROADMAP].
- Rigetti: promised 2025-07-16 · 100+ qubit chiplet system at median 99.5% before end-2025 · delivered 2026-04-07 at 99.1%, target moved to "later in 2026" [C][3][4].
- QuantWare: promised 2025-12-08 · VIO-40K, 10,000 qubits, first delivery 2028 · pending [P][G:QUANTWARE-VIO].

Credibility: IBM hits its named-processor dates but publishes packaging as architecture rather than measurement, so its modular claims stay unfalsifiable until Cockatoo; Rigetti ships what it describes, a fidelity step behind its own target; QuantWare has money and a fab but no delivered multi-chip QPU at scale to judge.

**Strategic reading.** If multi-chip modules work, the decisive asset moves from lithography to packaging and cryogenics, and the winner is whoever controls bump-bond, TSV and fridge capacity — IBM by vertical integration, QuantWare by merchant supply, IonQ through SkyWater. The loser is any roadmap assuming a single ever-larger die. Substitution threats: on-chip long-range couplers, which buy connectivity without packaging risk, and inter-fridge links, which buy unlimited scale at the price of a room-temperature crossing. Supplier bargaining power is high: there are more credible qubit vendors than lines that can bond them.

*Open niche:* a small QCVV/SFQ research company has two entry points. Measurement: nobody has published a protocol separating inter-die from intra-die error in a tiled processor, and the 99.5% → 99.1% step is what such a protocol would name — a chiplet-boundary benchmark is a vendor-neutral product. Control: an l-coupled module needs flux and drive generated near it rather than routed from 300 K, and millikelvin SFQ is the only demonstrated way to do that [G:SEEQC-2026].

## Outlook & open questions

Confirm within 12–24 months if: IBM's Cockatoo demonstrates entanglement between two l-coupled modules with a published fidelity by end-2027 [R][2]; Rigetti's 108-qubit system reaches median 99.5% [C][3]; anyone runs a stabilizer round whose checks cross a module boundary. Demote if no l-coupler fidelity is published by end-2027. Best case by 2029: a few thousand qubits in coupled cells with cross-module error correction at Λ comparable to monolithic. Worst case: tiling saturates near 10² qubits because frequency targeting across dies does not scale.

Open questions: what causes the 40-basis-point tiling tax, per-join or per-calibration? Can a metre-scale cable's mode comb be pushed out of band without shortening it? What is an l-coupler's fidelity, two years after the claim? Does a qLDPC check spanning modules survive the extra transport error? Watch Rigetti's roadmap update, IBM's first Cockatoo measurement, QuantWare's Kilofab yield, and any paper benchmarking a chiplet boundary as such.

## Sources

[1] [C] IBM Quantum · Modular cryogenics: coupling two cryogenic cells · IBM Quantum blog · 2026-08-19 · https://www.ibm.com/quantum/blog/modular-cryogenics
[2] [C] IBM Quantum · IBM lays out clear path to fault-tolerant quantum computing (c-couplers, l-couplers, Kookaburra, Cockatoo, nine-module Nighthawk) · IBM Quantum blog · 2025-06-10 · https://www.ibm.com/quantum/blog/large-scale-ftqc
[3] [C] Rigetti Computing · Rigetti Announces General Availability of 108-Qubit System (Cepheus-1-108Q, twelve 9-qubit chiplets) · investor release · 2026-04-07 · https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system
[4] [C] Rigetti Computing · Rigetti Demonstrates Industry's Largest Multi-Chip Quantum Computer; Halves Two-Qubit Gate Error Rate · investor release · 2025-07-16 · https://investors.rigetti.com/news-releases/news-release-details/rigetti-demonstrates-industrys-largest-multi-chip-quantum
[5] [D] Gold, Paquette, Stockklauser et al. (Rigetti) · Entanglement across separate silicon dies in a modular superconducting qubit device · npj Quantum Information · 2021-03 · https://www.nature.com/articles/s41534-021-00484-1 ; https://arxiv.org/abs/2102.13293
[6] [D] Niu, Zhang, Liu, … Yu · Low-loss interconnects for modular superconducting quantum processors · Nature Electronics · 2023-02-06 · https://arxiv.org/abs/2302.02751
[7] [D] Mollenhauer, Irfan, Cao, … Pfaff (Univ. of Illinois Urbana-Champaign) · A high-efficiency elementary network of interchangeable superconducting qubit devices · Nature Electronics 8, 610–619 · 2025-06-27 · https://www.nature.com/articles/s41928-025-01404-3
[8] [D] Mechanically-intermixed indium superconducting connections for microwave quantum interconnects · arXiv · 2024-09 · https://arxiv.org/abs/2409.04634
[9] [D] Modular superconducting qubit architecture with a multi-chip tunable coupler · arXiv · 2023-08 · https://arxiv.org/abs/2308.09240
[10] [P] Quantum Computing Report · QuantWare Debuts VIO-40K Architecture to Enable 10,000-Qubit Superconducting Processors · trade press · 2025-12-08 · https://quantumcomputingreport.com/quantware-debuts-vio-40k-architecture-to-enable-10000-qubit-superconducting-processors/
[11] [C] IBM · $10 billion investment FAQ · IBM Quantum blog · 2026-06 · https://www.ibm.com/quantum/blog/10-billion-investment-faq
[12] [C] IBM · IBM delivers new quantum processors, software, and algorithm breakthroughs (Nighthawk, Loon) · newsroom · 2025-11-12 · https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance
[13] [P] Intel Capital · QuantWare raises $178 million to build the world's most powerful quantum processors at industrial scale · 2026-05-05 · https://www.intelcapital.com/quantware-raises-176-million-to-build-worlds-most-powerful-quantum-processors-at-an-industrial-scale/
[14] [S] Hardware-aware compilation for chip-to-chip coupler-connected modular quantum systems · arXiv · 2025-05 · https://arxiv.org/abs/2505.09036
[15] [C] Bluefors · KIDE cryogenic platform product page · revised 2026-06-16 · https://bluefors.com/products/kide-cryogenic-platform/

## Open verification items
- IBM's l-coupler, "first demonstrated in 2024" on Flamingo [C][1][2]: no length, fidelity, latency or publication found as of 2026-09-03.
- The cause of Rigetti's 99.5% (four chiplets) → 99.1% (twelve chiplets) step is unattributed in both releases [C][3][4]; per-join versus per-calibration cannot be separated from public data.
- arXiv:2308.09240 and arXiv:2409.04634 abstracts do not state author institutions or numeric two-qubit fidelities; the "same level as single-chip" claim in [9] carries no number.
- QuantWare VIO-40K's 40,000 I/O lines appear in the shared fact record [G:QUANTWARE-VIO] but not on the 2025-12-08 trade-press page itself; line count unconfirmed at source.
- Rigetti chiplet-packaging and QuantWare vertical-I/O patent families: no dated assignee record found.
