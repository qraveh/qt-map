---
id: cx_lr
name: Long-range on-chip couplers (c-couplers, mm-scale)
layer: 4 Connectivity / transport
tier: 1
status: emerging
since: 2023
one_line: Waveguide- or resonator-extended tunable couplers that entangle fixed superconducting qubits millimetres apart, buying the degree-6 graphs that qLDPC codes need.
verdict: One 2 mm CZ at 99.81% (IQM, 2023) and IBM's Loon components without numbers; demote if no coupler of ≥ 5 mm reports a CZ ≥ 99.5% with error bars by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A long-range on-chip coupler is a microwave element — an extended capacitor, a transmission-line section, a resonator or a chain of them, usually with a flux-tunable transmon or SQUID in the middle — that mediates an exchange or ZZ interaction between superconducting qubits that are not lattice neighbours, millimetres apart, by virtual-photon exchange through the structure's detuned mode. Yale's cavity bus of 2007-09 moved quantum information between qubits "on opposite sides of a chip" through a cavity "a few millimetres long" [D][12]; MIT's giant atoms, coupled to one waveguide at several points, gave distant qubits decoherence-free exchange in 2020-07 [D][13]; Caltech's metamaterial bus gave ten qubits a tunable hopping range in 2023 [D][14]. The graph record dates the node to 2023, when IQM published a CZ of 99.81 ± 0.02% between transmons 1.96 mm apart through a floating transmon coupler whose two "waveguide extenders" carry both the qubit–coupler and the direct qubit–qubit coupling [D][1]. IBM's "c-coupler" (2025-06 vocabulary; "l-couplers" link chips [C][5]) is the same object built for a code, and Loon (2025-11) the first chip claiming a lattice of them [C][4].

Coordinates (legend: a = affinity natural↔fabricated; b = time, deterministic/heralded; c = readout; d = mobility; e = control @ placement; f = error structure; g = manufacturing), quoting the graph record:
- a = 1.0: a fully fabricated carrier.
- b = no characteristic time, determinism not applicable: the link sets no clock; the CZ it hosts is deterministic, 33 ns in the record device [D][1].
- c = no readout function.
- d = long-range: connectivity beyond nearest neighbour without moving the qubit.
- e = no control modality at no placement: the flux line is booked under the qubits joined.
- f = coherent: residual ZZ, phase miscalibration, crosstalk.
- g = superconducting lithography.
Rank 2 of 96; a hub reaching the superconducting and annealing paths; off-diagonal reading: a fabricated carrier with far-range mobility.

## Physics & limits

At 4 GHz on silicon the guided wavelength is about 30 mm, so IQM's 2 mm extenders are electrically short capacitors; the coupler idles at 3.195 GHz below qubits at 4.10 and 3.89 GHz, with qubit–coupler couplings of 51.5 and 53.9 MHz against a direct 3.7 MHz, the net exchange being their difference [D][1]. The gate is a coupler flux excursion that turns on the |11⟩↔|20⟩ interaction for 22 ns plus 11 ns idle; the separation also cuts next-nearest-neighbour coupling below 30 kHz [D][1]. Beyond a few millimetres the extender's own standing-wave modes enter the qubit band (a 1 cm half-wave line resonates near 6 GHz), so the coupling must come from a hybridised resonator–transmon mode: Nanjing's 1 cm coupler measures 23.5 MHz of XX coupling and up to 100 MHz of ZZ, switchable by more than 10² and 10⁴ respectively [D][8]. Links of 1 cm to 0.5 m exist only in simulation [S][9][10][11].

Four floors. Loss: a coupler mode with T₁ > 40 µs [D][1] costs at most 33 ns/40 µs ≈ 8×10⁻⁴ per gate, ~10⁻⁵ at dispersive participation — below the record's 1.9 ± 0.2 ×10⁻³, attributed "mostly" to one qubit's T₁ falling to 14 µs during the flux excursion [D][1]. Crowding: each extra mode is a frequency collision, and a degree-6 vertex holds six couplers off resonance at once. Coherent error: residual ZZ under 2 kHz [D][1] is 0.013 rad of conditional phase per microsecond of idling per pair, correlated rather than stochastic. Geometry: degree above four needs crossings, hence routing layers; the bivariate-bicycle Tanner graph is "a degree-6 graph that consists of two edge-disjoint planar subgraphs" [D][2], so two suffice topologically. The floor moves with lower-loss routing layers — Loon claims "multiple high-quality, low-loss routing layers" [C][4] — and qubits whose T₁ survives flux tuning.

## Engineering state of the art

Best demonstrated: 99.81(2)% CZ at 1.96 mm in 33 ns (IQM, published 2023-02) [D][1]. Typical at scale, as of 3 Sep 2026: none — no multi-qubit processor with mm-scale couplers has published gate fidelities; Loon shows "6-way qubit connections" without numbers [C][4][6], and IQM's resonator-hub Star devices reach "above 99.3%" on a MOVE–CZ–MOVE sequence [C][17].

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2007-09 | Two qubits on opposite sides of a chip coupled through a few-mm cavity bus | Yale | [D] | [12] |
| 2023-02 | CZ 99.81(2)% across 1.96 mm, 33 ns, ZZ < 2 kHz | IQM | [D] | [1] |
| 2025-03 | 6-qubit star resonator: [[4,2,2]] logical error per cycle 0.25(2)–0.91(3)% | IQM | [D] | [16] |
| 2025-05-20 | Advantage2 GA, 4,400+ qubits at degree 20 (16 internal + 2 external + 2 odd couplers) | D-Wave | [C] | [19] [G:DWAVE-FIN-2026] |
| 2025-06 | 1 cm hybrid-mode coupler, XX 23.5 MHz, ZZ contrast > 10⁴, no gate | Nanjing | [D] | [8] |
| 2025-11-12 | Loon: 6-way connections, longer couplers, multilayer routing, no numbers | IBM | [C] | [4][6] |

Dominant error term today: qubit relaxation during the flux excursion (T₁,eff 14 µs on one qubit, 43 µs on the other) [D][1]; for degree-6 lattices the budget is unpublished.

## Manufacturing, materials & supply chain

Standard Nb/Al Josephson lithography plus multilayer, low-loss routing so couplers can cross qubit rows. IBM builds Loon on 300 mm wafers at Albany NanoTech and credits the line with "a ten-fold increase" in chip complexity [C][4][6]; D-Wave's 10-K describes "a multilayer integrated circuit process" [G][20]. Each tunable coupler adds a junction and a flux line: a 288-qubit gross-code module at degree 6 [D][2] carries 864 couplers if all are tunable, three per qubit against 1.8 on Nighthawk (218 couplers, 120 qubits) [C][4]. Yield per coupler is unpublished.

Supply chain: IBM fabricates in-house with NY CREATES [C][4]; IQM in Espoo [D][1]; D-Wave uses "existing third-party foundries", demonstrated a second source with the 2000Q LN [G][21], and its 10-K filings mention SkyWater (nine full-text hits, 2023–2026) [G][22] — a foundry that IonQ, a platform competitor, has owned since 2026-07-31 [C][23] [G:IONQ-SKYWATER-2026]. The single points of failure are the three or four fabs with qualified low-loss multilayer processes. Export exposure: the BIS rule of 2024-09-06 [G][27] [G:BIS-QUANTUM-2024] controls computers of ≥ 34 qubits (4A906) and dilution refrigerators (3A904), not coupler designs.

## Control, readout & I/O burden

A tunable long-range coupler needs one flux line and a 22 ns-class flux pulse [D][1]; a fixed resonator hub needs none but pays with MOVE operations [C][15][17]. At degree 6 the coupler flux lines alone are three per qubit, on top of drive, qubit flux and multiplexed readout — five to six lines per qubit. At 10³ qubits that is 5,000–6,000 lines and cold multiplexing; at 10⁴ it is the 40,000 lines QuantWare promises for 2028 [P][33] [G:QUANTWARE-VIO]; at 10⁶ only on-chip flux generation (cryo-CMOS or SFQ, SEEQC's mK control being the published pointer [G:SEEQC-2026]) closes the gap. Loop latency is unchanged: a bivariate-bicycle round is "a depth-7 circuit composed of nearest-neighbor CNOT gates" [D][2]; what the coupler moves is the decoder, since bicycle codes lack the matching decoders that keep surface-code decoding within a microsecond.

## Role in the stack

Two platform paths: superconducting transmons and quantum annealing. It requires superconducting lithography with multilayer routing and provides the degree-6 long-range checks bivariate-bicycle codes consume: 12 logical qubits in 288 physical where a surface code needs "nearly 3000" at 0.1% physical error [D][2], and 121 logical qubits from a 5,000-qubit gross system at p = 10⁻³ in IBM's architecture study, whose degree "does not exceed seven" [S][3]. It replaces nearest-neighbour couplers at the price of one junction and flux line per added edge, two or more routing layers, and a coupler whose T₁ and spurious modes enter the budget — paid per design, not per gate. Hub reading: a fabricated carrier that buys in lithography the far-range mobility atoms and ions get from motion. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path: on the transmon path the round is 0.65 µs with readout 282 ns its largest term, and the 33 ns long-range CZ [D][1] is 5% of the round, binding only if a MOVE–CZ–MOVE sequence outruns the readout term; on the annealing path the anneal schedule is the clock. Neighbouring empty slots: the chip-to-chip l-coupler promised for IBM's Cockatoo in 2027 [R][5], and the spin-qubit resonator link, where Delft showed iSWAP oscillations between spins 250 µm apart [D][26] without a gate fidelity.

## Verification (QCVV)

The 99.81% is interleaved randomized benchmarking, its 1.9(2)×10⁻³ error decomposed by simulation into a coherence-limited part dominated by one qubit's T₁,eff of 14 µs; ZZ < 2 kHz is measured at the idle point [D][1]. Nanjing's figures are spectroscopic couplings, not gates [D][8]. IQM's star results are logical-state fidelities of a [[4,2,2]] code, folding in readout and idling [D][16]; its "above 99.3%" is a company figure without protocol [C][17]. Loon's claims are release text [C][4][6].

Not captured: crosstalk on shared extenders when several couplers of one vertex fire together; T₁ at the flux points every coupler forces on its qubits; leakage into extender modes; drift of the ZZ null. Independent replications of a mm-scale CZ with error bars: none as of 3 Sep 2026. Conflicts: degree 6 [D][2] against "does not exceed seven" [S][3] — the seventh edge is the logic-unit adapter, so both hold; the graph record's "≥ 2 mm" is the paper's 1.96 mm [D][1]; IQM's 99.3% (Constellation cell) and 99.81% (isolated pair) are different operations, not a regression.

## Actors & economics

**Who.**

| Organisation | Role | Country | What it does with this technology | Evidence |
|---|---|---|---|---|
| IBM | developer | US | c-couplers on Loon; Kookaburra qLDPC module (2026); Starling (2029) | [C][4][5] [G:IBM-ROADMAP] |
| IQM Quantum Computers | developer | Finland | 2 mm coupler record; Star hubs; Constellation 2030+ | [D][1] [C][15][17][18] |
| D-Wave Quantum | developer | US | Zephyr degree-20 annealers | [C][19] [G:DWAVE-FIN-2026] |
| Nanjing University | research | China | 1 cm hybrid-mode coupler; long-range ZZ theory | [D][8] [S][10] |
| QuTech | research | Netherlands | Resonator link between spins 250 µm apart | [D][26] |
| SkyWater Technology | supplier | US | Foundry named in D-Wave's 10-Ks; IonQ-owned since 2026-07-31 | [G][22] [C][23] |
| QuantWare | supplier | Netherlands | 3D-routed chips; VIO-40K roadmap | [P][33] |
| DARPA | regulator | US | QBI Stage B includes IBM (up to $15 M) | [G][28] [G:QBI-STAGEB-2025-11] |

**Money.**
- 2025-09-03 · IQM · Series B · $320 M · closed [G:IQM-LISTING-2026-07]
- 2025-11-06 · DARPA QBI Stage B · IBM among eleven teams · up to $15 M each · official [G][28] [G:QBI-STAGEB-2025-11]
- 2026-05-21 · IBM/Anderon; D-Wave; GlobalFoundries · US DoC CHIPS letters of intent · $1 B (+ $1 B IBM cash); $100 M; $375 M · LOI, non-binding [G][29] [G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · quantum investment commitment · > $10 B over five years · announced [C][30] [G:IBM-10B-2026-06]
- 2026-07-02 · IQM · Nasdaq and Helsinki listing · pro-forma cash €337 M; H1-2026 revenue €8.9 M · closed [C][31] [G:IQM-LISTING-2026-07]
- 2026-07-31 · IonQ · acquisition of SkyWater · ~$1.8 B · closed [C][34] [G:IONQ-SKYWATER-2026]
- 2026-08-06 · D-Wave · H1-2026 results · revenue $5.9 M, cash $546.2 M · reported [C][32] [G:DWAVE-FIN-2026]

**Market & supply chain.** Nobody sells a long-range coupler; it is a design block inside a vendor's chip, and the market is the three or four fabs that can print it — Albany [C][4], IQM's own [D][1], D-Wave's third-party foundries [G][21][22], GlobalFoundries under its LOI [G:CHIPS-LOI-2026-05] — plus QuantWare as the only merchant seller of 3D-routed chips [P][33]. The structural cost is 1.5–3 extra couplers per qubit against a 10× saving in physical qubits per logical qubit [D][2]. Who pays: G4 (IBM's Starling), G3 if Kookaburra runs, G5 on the annealing path [C][19], G1/G2 through fewer SWAPs on Star hubs [C][15].

**IP & standards.** IBM: US 12,517,856 (filed 2022-09-28, granted 2026-01-06) on modular connectivity levels, US 12,587,192 (granted 2026-03-24) on resonator chains with tunable inductive couplers, US 2024/0169232 A1 (filed 2022-11-18) on fluxonium long-range coupling [G][24]. D-Wave: US 10,268,622 (granted 2019-04-23), US 11,507,871 and US 11,494,683 (both 2022-11) on long-range couplers [G][25]. No litigation found; no standard. PatSnap to 2026-06-30 counts IBM at 4,388 quantum families, 783 in superconducting devices [P][G:PATSNAP-2026-06]; no count exists for long-range couplers.

**Roadmaps & track record.**
- IBM: promised 2025-06-10 · Loon in 2025 with c-couplers · delivered 2025-11-12 as components without performance numbers [C][4][5].
- IBM: promised 2025-06-10 · Kookaburra 2026, Cockatoo 2027 (l-couplers), Starling 2029 (200 logical, 10⁸ gates) · Kookaburra not delivered as of 2026-09-03, the rest pending [R][5] [C][7] [G:IBM-ROADMAP].
- IQM: promised 2026-01-05 · 2Q fidelity above 99.94% in 2025–26; qLDPC demonstrators 2027–28; Constellation with long-range couplers 2030+ · pending [R][18].
- D-Wave: described 2021-09-22 · Zephyr topology · delivered with Advantage2 GA 2025-05-20 [C][19] [G:DWAVE-FIN-2026].
Credibility: IBM ships the processor it names in the year it names (Nighthawk delivered 2025-12 [G:IBM-ROADMAP]) but has published no coupler number ten months after Loon; IQM delivered its 2023 physics and ships Star systems, with a roadmap that carries no qubit counts; D-Wave delivered its topology at scale, for annealing only.

**Strategic reading.** If mm-scale couplers reach nearest-neighbour fidelity at degree 6, physical qubits per logical qubit fall by an order of magnitude [D][2]; the winners are the vendors owning both coupler and code — IBM and, later, IQM — plus the fabs holding multilayer processes; the losers are surface-code roadmaps on nearest-neighbour lattices, Google's included [G:GOOGLE-ATLANTIC-2025-10]. Substitution threats: chip-to-chip l-couplers [R][5]; atoms and ions, which get connectivity from motion; better nearest-neighbour gates with SWAP networks. Bargaining power sits with platform vendors on design and with the few fabs on routing layers; IonQ–SkyWater is the first platform vendor owning a rival's named foundry [G][22] [G:IONQ-SKYWATER-2026].

*Open niche:* a small QCVV/SFQ research company could own the missing benchmark — one protocol reporting simultaneous-gate crosstalk on shared extenders, ZZ-null drift and flux-point T₁ at a degree-6 vertex — and, on the SFQ side, cold flux-bias generation for the three coupler lines per qubit that no room-temperature rack scales past 10⁴ qubits.

## Outlook & open questions

Confirm within 12–24 months if: IBM publishes c-coupler CZ fidelities ≥ 99.5% with error bars at ≥ 5 mm and a gross-code memory experiment on Kookaburra by end-2027 [G:IBM-ROADMAP]; any group demonstrates a ≥ 1 cm on-chip CZ at ≥ 99.5% [D][8]; IQM shows a Constellation cell at ≥ 99.9% [C][17]. Demote if by end-2027 no mm-scale coupler reports ≥ 99.9% or no code with long-range checks on superconducting hardware reports Λ > 1. Best case by 2029: Starling-class modules of 288-qubit gross codes with couplers at 99.9% [D][2] [R][5]. Worst case: couplers stay at 99.8% on isolated pairs, qLDPC codes migrate to atoms and ions, and IBM's 2029 machine becomes a surface-code machine.

Open questions: (1) does a qubit's T₁ survive the flux points six couplers force on it? (2) what is the parallel-gate crosstalk on a vertex whose extenders share a routing layer? (3) which decoder runs bicycle codes within the cycle time? Watch: any IBM coupler paper, Kookaburra's 2026 status, IQM's Constellation product date, Nanjing's 1 cm gate.

## Sources

[1] Marxer, F., Vepsäläinen, A., Jolin, S. W., Tuorila, J. et al. (IQM Quantum Computers) · Long-distance transmon coupler with CZ gate fidelity above 99.8% · PRX Quantum 4, 010314 (arXiv:2208.09460, 2022-08-19) · 2023-02 · https://arxiv.org/abs/2208.09460
[2] Bravyi, S., Cross, A. W., Gambetta, J. M., Maslov, D., Rall, P., Yoder, T. J. (IBM) · High-threshold and low-overhead fault-tolerant quantum memory · Nature 627, 778 (arXiv:2308.07915) · 2024-03-27 · https://arxiv.org/abs/2308.07915
[3] Yoder, T. J., Schoute, E., Rall, P., Pritchett, E., Gambetta, J. M., Cross, A. W., Carroll, M., Beverland, M. E. (IBM) · Tour de gross: A modular quantum computer based on bivariate bicycle codes · arXiv:2506.03094 · 2025-06-03 · https://arxiv.org/abs/2506.03094
[4] [C] IBM · IBM Delivers New Quantum Processors, Software, and Algorithm Breakthroughs on Path to Advantage and Fault Tolerance · IBM Newsroom · 2025-11-12 · https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance
[5] [C] IBM · IBM lays out clear path to fault-tolerant quantum computing · IBM Quantum blog · 2025-06-10 · https://www.ibm.com/quantum/blog/large-scale-ftqc
[6] [C] IBM · Quantum Developer Conference 2025: Nighthawk and Loon · IBM Quantum blog · 2025-11-12 · https://www.ibm.com/quantum/blog/qdc-2025
[7] [C] IBM · IBM Quantum development and innovation roadmap · ibm.com · accessed 2026-09-03 · https://www.ibm.com/roadmaps/quantum/
[8] Xu, J., Deng, X., Zheng, W. et al. (Nanjing University / Hefei National Laboratory) · Tunable Hybrid-Mode Coupler Enabling Strong Interactions between Transmons at Centimeter-Scale Distance · arXiv:2506.14128 · 2025-06-18 · https://arxiv.org/abs/2506.14128
[9] Zhao, P., Xu, P., Xue, Z.-Y. · Long-range tunable coupler for modular fluxonium quantum processors · arXiv:2604.12261 · 2026-04-15 · https://arxiv.org/abs/2604.12261
[10] Deng, X., Zheng, W., Liao, X. et al. (Nanjing University) · Long-Range ZZ Interaction via Resonator-Induced Phase in Superconducting Qubits · arXiv:2408.16617 (v2) · 2024-09-12 · https://arxiv.org/abs/2408.16617
[11] Zhao, P., Zhang, Y., Xue, G., Jin, Y., Yu, H. · Tunable coupling of widely separated superconducting qubits: A possible application towards a modular quantum device · Applied Physics Letters (doi:10.1063/5.0097521; arXiv:2201.03184) · 2022-01-10 · https://arxiv.org/abs/2201.03184
[12] Majer, J. et al. (Yale) · Coupling superconducting qubits via a cavity bus · Nature 449, 443–447 · 2007-09-27 · https://www.nature.com/articles/nature06184
[13] Kannan, B. et al. (MIT) · Waveguide quantum electrodynamics with superconducting artificial giant atoms · Nature 583, 775–779 · 2020-07-29 · https://www.nature.com/articles/s41586-020-2529-9
[14] Zhang, X., Kim, E., Mark, D. K., Choi, S., Painter, O. (Caltech) · A superconducting quantum simulator based on a photonic-bandgap metamaterial · Science 379, 278 (2023); arXiv:2206.12803 · 2022-06-25 · https://arxiv.org/abs/2206.12803
[15] [C] IQM Quantum Computers · Jumping off the grid in quantum processor innovation: introducing IQM Star · company blog · 2025-04-30 · https://iqm.tech/blog/jumping-off-the-grid-in-quantum-processor-innovation-introducing-iqm-star/
[16] IQM Quantum Computers · Quantum error detection in qubit-resonator star architecture · arXiv:2503.12869 · 2025-03 · https://arxiv.org/abs/2503.12869
[17] [C] IQM Quantum Computers · IQM Constellation: a new quantum processor architecture for scalable error correction · company blog · 2025-09-30 · https://iqm.tech/blog/iqm-constellation-a-new-quantum-processor-architecture-for-scalable-error-correction/
[18] [C] IQM Quantum Computers · Roadmap · company page, updated 2026-01-05 · accessed 2026-09-03 · https://iqm.tech/technology/roadmap/
[19] [C] Boothby, K., King, A. D., Raymond, J. (D-Wave) · Zephyr Topology of D-Wave Quantum Processors · D-Wave technical report 14-1056A-A · 2021-09-22 · https://www.dwavequantum.com/media/2uznec4s/14-1056a-a_zephyr_topology_of_d-wave_quantum_processors.pdf
[20] [G] D-Wave Quantum Inc. · Form 10-K for fiscal year 2025 · SEC EDGAR · 2026-02-26 · https://www.sec.gov/Archives/edgar/data/1907982/000190798226000026/qbts-20251231.htm
[21] [G] D-Wave Quantum Inc. · Form 10-K for fiscal year 2024 · SEC EDGAR · 2025-03-14 · https://www.sec.gov/Archives/edgar/data/1907982/000190798225000060/qbts-20241231.htm
[22] [G] SEC EDGAR full-text search · "SkyWater" in D-Wave Quantum Inc. Form 10-K filings (nine hits, filings of 2023-04-18 to 2026-02-26) · accessed 2026-09-03 · https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982
[23] [C] IonQ · IonQ to Acquire SkyWater Technology, Creating the Only Vertically Integrated Full-Stack Quantum Platform Company · investor release · 2026-01-26 · https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/default.aspx
[24] [G] USPTO (via Justia Patents) · US 12,517,856 (granted 2026-01-06), US 12,587,192 (granted 2026-03-24), US 2024/0169232 A1 (filed 2022-11-18), International Business Machines Corporation · patents · accessed 2026-09-03 · https://patents.justia.com/search?q=%22long-range+coupler%22+qubit
[25] [G] USPTO (via Justia Patents) · US 10,268,622 (granted 2019-04-23), US 11,507,871 (granted 2022-11-22), US 11,494,683 (granted 2022-11-08), D-Wave Systems Inc. · patents · accessed 2026-09-03 · https://patents.justia.com/search?q=%22long-range+coupler%22+qubit
[26] Dijkema, J., Xue, X., Harvey-Collard, P. et al. (QuTech, Delft) · Two-qubit logic between distant spins in silicon · Nature Physics (doi:10.1038/s41567-024-02694-8; arXiv:2310.16805) · 2023-10-25 · https://arxiv.org/abs/2310.16805
[27] [G] US Bureau of Industry and Security · Commerce Control List Additions and Revisions: Implementation of Controls on Advanced Technologies Consistent with Controls Implemented by International Partners · Federal Register 2024-19633 · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[28] [G] DARPA · Quantum Benchmarking Initiative — Stage B selection · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[29] [G] NIST / US Department of Commerce · Department of Commerce Announces Letters of Intent with 9 Companies for $2 Billion · nist.gov · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[30] [C] IBM · IBM's $10 billion quantum investment: FAQ · IBM Quantum blog · 2026-06-02 · https://www.ibm.com/quantum/blog/10-billion-investment-faq
[31] [C] IQM Quantum Computers · IQM Quantum Computers becomes first European quantum computing company listed on a major U.S. exchange · press release · 2026-07-02 · https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/
[32] [C] D-Wave Quantum · D-Wave Reports Second Quarter 2026 Results · press release · 2026-08-06 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/
[33] [P] Quantum Computing Report · QuantWare Debuts VIO-40K Architecture to Enable 10,000-Qubit Superconducting Processors · trade press · 2025-12-08 · https://quantumcomputingreport.com/quantware-debuts-vio-40k-architecture-to-enable-10000-qubit-superconducting-processors/
[34] [C] IonQ · IonQ Completes Acquisition of SkyWater Technology · press release · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology

## Open verification items

- IBM Loon: qubit count, c-coupler length and any gate fidelity are unpublished as of 2026-09-03 [C][4][6]; no 2026 IBM paper on c-couplers was found.
- The exact 10-K wording of D-Wave's reliance on SkyWater: EDGAR full-text search returns nine hits [G][22], but the sentences could not be extracted from the filings consulted; D-Wave's own text says "existing third-party foundries" with a second source demonstrated on the 2000Q LN [G][21].
- Degree 6 [D][2] versus "does not exceed seven" [S][3]: reconciled here as memory-only versus memory-plus-logic-unit; the seventh edge's assignment is this brief's reading, not the papers' wording.
- IQM arXiv:2503.12869: author list and exact submission day not extracted (organisation cited); Constellation's "above 99.3%" carries no protocol or error bar [C][17].
- Nanjing's 1 cm coupler: XX 23.5 MHz is measured; the 100 MHz ZZ is stated without saying whether measured or simulated [D][8]; treated as a design value.
- The 282 ns readout used for the derived clock is the superconducting path's graph record value, not a figure specific to long-range couplers.
- Cost, energy and yield per coupler: no actor publishes them.
- Patent metadata for [24][25] comes from Justia's index, not USPTO full-text records; no family count exists for long-range couplers specifically.
- Whether IQM's shipped Crystal products use the 2 mm extended coupler of [1] is not stated by the company.
