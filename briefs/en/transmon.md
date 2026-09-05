---
id: transmon
name: Transmon
layer: 1 Carrier
tier: 1
status: demonstrated
since: 2007
one_line: Capacitively shunted Josephson junction (Koch 2007); the carrier behind Willow, Heron/Nighthawk and Zuchongzhi, with the fastest deterministic gate and QEC cycle of any demonstrated qubit.
verdict: Best-funded and fastest carrier, capped by ~10⁻³ two-qubit and ~10⁻² readout errors at scale and hourly correlated bursts. Confirm if a ≥100-qubit lattice shows Λ ≥ 3 with median 2Q error < 10⁻³ by 2028; otherwise demote to component status.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A transmon is an Al/AlOx/Al Josephson junction shunted by a large capacitor so that E_J/E_C ≈ 50–100 [D][1]. Charge dispersion falls exponentially in √(8E_J/E_C), removing 1/f charge noise at the price of a weak anharmonicity α ≈ −E_C ≈ −200 to −300 MHz; the qubit is the lowest two levels of a 4–6 GHz oscillator [D][1]. Koch et al. proposed it in 2007 [D][1]; the 3D transmon (2011) [D][2] and the UCSB/Google Xmon (2014) [D][3] fixed the two lineages still in use, fixed-frequency (IBM) and flux-tunable (Google, IQM, USTC).

Coordinates (technology graph):
- a: affinity 1.0, fabricated (no natural counterpart).
- b: characteristic time 10⁻⁸ s, deterministic entangling; the 1/α leakage bound puts the pulse floor near 10 ns.
- c: readout dispersive microwave, 10⁻⁶·⁵ s (≈ 320 ns), non-destructive, mid-circuit capable.
- d: mobility static, nearest-neighbour wiring.
- e: control microwave from room-temperature electronics; cold-stage variants (cryo-CMOS, SFQ) at ≤ 5 qubits.
- f: error structure leakage + stochastic Pauli + correlated bursts + coherent/calibration.
- g: manufacturing superconducting lithography.

## Physics & limits

Residual thermal population (0.1% at 35 mK in a 3D transmon [D][54], ≈ 1% at 40–60 mK for a 5 GHz qubit [S][54]) makes reset and readout the SPAM floor. Anharmonicity bounds single-qubit gates at 10–25 ns and tunable-coupler CZ at 25–50 ns [D][4][7][P][5]; cross-resonance takes ≈ 200–500 ns [D][6].

The floor is decoherence over gate time: with Willow's mean T1 = 68 µs [D][7] a 40 ns CZ carries ≈ 6×10⁻⁴ of incoherent error [S][7]; at the record T1 = 1.68 ms of a single Ta-on-Si test transmon [D][8] it falls below 5×10⁻⁵ [S][8]. Loss is dominated by two-level systems (TLS) in amorphous interface oxides [D][8], with quasiparticles, Purcell decay and flux noise below.

Most of the twirled channel is stochastic Pauli, so Willow's Λ = 2.14 [D][7] matches theory. Leakage to |2⟩ accumulates under QEC unless removed each cycle (USTC's all-microwave reset cut it 72×, to 6.4×10⁻⁴, on 107 qubits [D][9]). Coherent errors (residual ZZ, TLS drift) forced reinforcement-learning recalibration inside Google's 2026-07 QEC run [D][10]. Correlated bursts (ionizing particles flooding the chip with quasiparticles) hit all qubits at once — roughly one per 10 s on Sycamore in 2021 [D][11], about one per hour on Willow after gap engineering [D][7][12] — truncating long memory runs by bursts, not distance. Moving the floor means new materials (Ta, encapsulated Nb), fluxonium-scale anharmonicity, radiation management or erasure conversion (dual-rail).

## Engineering state of the art

Best isolated devices: T1 1.68 ms, Q 2.5×10⁷, 1Q 99.994% [D][8]; CZ 99.93% and 280 ns readout at 99.94% on a two-qubit IQM chip [D][13]; Toshiba's double-transmon coupler CZ 99.90% in 48 ns [D][4].

Typical at ≥ 100 qubits: Willow, 105 q — mean T1 68 µs, CZ error 0.33%, readout 99.5%, QEC cycle 1.1 µs [D][7][C][14]; IBM fleet error-per-layered-gate 3.7×10⁻³ typical, 1.9×10⁻³ best (2026-07) [C][15]; Zuchongzhi 3.0, 105 q — 2Q 99.62%, readout 99.13% [D][16]; Rigetti Cepheus-1-108Q chiplets — median 2Q 99.1% [C][G:RIGETTI-FIN-2026].

| Year | Figure | Who | Evidence |
|---|---|---|---|
| 2019 | Sycamore 53 q, simultaneous 2Q error 0.62% | Google | [D][20] |
| 2023 | Condor, 1,121 qubits on one chip | IBM | [C][21] |
| 2024 | Willow 105 q, Λ = 2.14 | Google | [D][7] |
| 2025 | 2D transmon T1 1.68 ms | Princeton | [D][8] |
| 2026 | d=7 logical error 7.72×10⁻⁴ per cycle | Google | [D][10] |

At scale the two-qubit gate is the largest error term (~40% of Google's colour-code budget) [D][22], then readout (~10⁻² on fleets [C][15]) and leakage; the lattice tail matters more than the median.

## Manufacturing, materials & supply chain

Process: Nb or Ta on high-resistivity Si or sapphire; shadow-evaporated Al/AlOx/Al junctions; flip-chip 3D integration. On 300 mm CMOS tooling imec/KU Leuven reported 393 of 400 working transmons (98.25%), median T1 ≈ 75 µs (42–113 µs) [D][23][G:IMEC-300MM-2025]: uniformity, not coherence. Fixed-frequency lattices must also hit frequency targets (junction scatter becomes collisions) by laser annealing (IBM), alternating-bias annealing (Rigetti, 97.4% success) [D][24] or tunable couplers.

Cost and energy: no vendor publishes $/qubit; proxies are IQM's €33 M LUMI contract [P][26] and IBM's 14 nm cryo-controller at 23 mW per qubit at 4 K [D][27] — tens of watts at 10³ qubits, hence the SFQ case (nW per qubit claimed [C][58]).

Supply chain: dilution refrigerators from Bluefors (FI), Oxford Instruments (UK), FormFactor and Maybell (US); ³He from tritium decay in state inventories (US: NNSA [G][55]), no merchant producer; 4 K HEMT amplifiers effectively one vendor (Low Noise Factory, SE); control electronics competitive (Quantum Machines, Qblox, Zurich Instruments); merchant QPUs from QuantWare (NL) [P][29]; foundries Anderon (IBM Albany spin-off, 2026-05; $1 B CHIPS letter of intent, $1 B IBM cash stated separately) [P][30][G][31] and GlobalFoundries ($375 M LOI) [G][31].

Export controls: the BIS interim final rule of 2024-09-06 covers quantum computers from 34 qubits (ECCN 4A906), dilution refrigerators ≥ 600 µW at 0.1 K for 48 h (3A904), cryogenic wafer probers (3B904) and parametric amplifiers (3A901.b) [G][32][G:BIS-QUANTUM-2024]; Chinese vendors therefore build 10 mK refrigerators domestically (2026-05-15) [P][19].

## Control, readout & I/O burden

A tunable lattice needs one XY and one Z line per qubit plus one per coupler (Sycamore: ≈ 3.6 control lines per qubit before readout [D][20]); readout multiplexes ≈ 6–10 qubits per feedline [D][7]; each line is a DAC channel plus attenuated coax, so cost and heat scale with N.

Latency: the QEC cycle is 1.1 µs; Google's real-time decoder ran at 63 µs mean latency for d=5 [D][7]; IBM's Relay-BP targets < 1 µs per cycle in simulation [S][33] for the gross code (IBM's [[144,12,12]] bivariate-bicycle qLDPC code, 12 logical qubits in 288 physical [D][57]).

Walls: 10³ reached (Condor, 1,121 qubits [C][21]); Bluefors' KIDE (> 4,000 RF lines, > 1,000 qubits; product page, 2026-06) [C][34] is one cryostat's ceiling. 10⁴ needs 4 K cryo-CMOS (HRL: d=5 repetition code from a ≤ 3.5 W controller [D][35][G:HRL-2026]) or millikelvin SFQ (SEEQC: 1Q up to 99.9% on ≤ 5 qubits [D][28][G:SEEQC-2026]) plus multi-cryostat modules (IBM coupled two cells, 2026-08 [C][36]). 10⁶ has no closed design: on-chip flux DACs, cold decoding and inter-fridge links (ETH: 30 m at 80.4% Bell fidelity [D][37]) are sub-scale.

## Role in the stack

Paths: the superconducting path and the dual-rail erasure path (transmon as ancilla or one rail); no off-diagonal reading, not a hub. Requires superconducting lithography; provides the carrier for tunable-coupler and cross-resonance gates, the ancilla for bosonic-cavity gates, the bare-qubit subspace, the dispersive shift for microwave readout and the microwave side of the optical transducer. Replaced by fluxonium, which buys anharmonicity and T1 for a flux bias per qubit, sub-GHz control and redesigned readout. Conflicts with SFQ control: switching photons poisoned qubits with quasiparticles in the 2023 multi-chip module (0.96 of 1.2% error per Clifford) [D][39]; SEEQC claims it engineered away [C][58], so the conflict stands until an independent lattice-scale check. Derived clock of the superconducting path ≈ 6.5×10⁻⁷ s (651 ns; derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path), readout 282 ns of it and readout-plus-reset two-thirds, against the measured 1.1 µs Willow cycle [D][7] — the fastest demonstrated path, which G4 (large-scale fault tolerance) pays for. Bordering empty slots: the microwave–optical transducer (≈ 3 orders of magnitude short of remote gates [S][40]) and cryogenic decoding.

## Verification (QCVV)

Headline numbers come from Clifford RB/IRB, simultaneous XEB (Google), IBM's layer fidelity/EPLG and readout assignment matrices; Λ is a fit of logical error vs distance under one decoder. Missed here: isolated vs simultaneous operation (record chips are isolated); coherent errors averaged into a depolarising number; leakage, invisible to RB and often post-selected away; drift between calibration and use; and conventions (Rigetti quotes medians, IBM its best device, IQM a two-qubit chip). IBM's 2026-07 "70 logical qubits" is an error-detecting, post-selected result [D][41], not fault tolerance.

Replication: below-threshold scaling reproduced by USTC on 107 qubits with Λ = 1.40 [D][9]. Disputes: 2019 supremacy sampling reproduced by tensor networks [D][42]; the 2023 IBM "utility" experiment simulated classically within weeks [D][43][44]; Google's 2026-07 paper reports no Λ for the d=7 run [D][10]. Value conflict: imec's 300 mm T1 is often quoted as "> 100 µs"; the paper's median is ≈ 75 µs [D][23][G:IMEC-300MM-2025], used here.

## Actors & economics

**Who.**

| Organisation | Role | Country | Activity | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | Willow 105 q, Λ = 2.14; d=7 memory | [D][7][10] |
| IBM | developer | US | Heron/Nighthawk fleet; Starling roadmap; Anderon spin-out | [C][15][59][P][30] |
| Rigetti | developer | US | Cepheus-1-108Q chiplets; own fab | [C][17] |
| IQM | developer | FI | 26 systems sold, 17 installed | [C][46][G:IQM-LISTING-2026-07] |
| USTC | research | CN | Zuchongzhi 3.x, 105 q; Λ = 1.40 | [D][9][16] |
| SEEQC | supplier | US | millikelvin SFQ control; IBM integration under QBI | [D][28][G:SEEQC-2026] |

**Money.**
- 2025-11-06 · DARPA · QBI Stage B (up to $15 M each) · IBM the only transmon-lattice vendor of eleven; Google and Rigetti stayed at Stage A [G][50][G:QBI-STAGEB-2025-11][G:QBI-STAGEA-2025-04]
- 2026-01-20 · D-Wave · M&A, Quantum Circuits (dual-rail cavities on transmon ancillae) · $550 M (stock + cash) · closed [C][48][G:DWAVE-QCI-2026-01][G:DUALRAIL-CZ-2026-08]
- 2026-05-05 · QuantWare (merchant QPUs; VIO-40K roadmap [R][G:QUANTWARE-VIO]) · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners (new investors, no lead) · > $210 M cumulative · closed [P][29]
- 2026-05-18 · Nord Quantique · growth-equity financing · $30 M at a $1.4 B valuation · closed [C][49][G:NQ-1.4B-2026-05]
- 2026-05-21 · US Dept of Commerce · CHIPS letters of intent ($2.013 B, nine companies) · IBM/Anderon $1 B, GlobalFoundries $375 M, Rigetti ≤ $100 M, D-Wave $100 M · non-binding LOI [G][31][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · commitment · > $10 B over five years, the $1 B cash into Anderon stated separately · announced [C][45][G:IBM-10B-2026-06]
- 2026-06-03 · OQC (coaxmon developer [D][25]) · Series C · £260 M (~$350 M) · led by Bullhound · valuation undisclosed · closed [C][47][G:OQC-SERIESC-2026-06]
- 2026-07-02 · IQM · listing, Nasdaq and Helsinki · pro-forma cash €337 M · closed [C][G:IQM-LISTING-2026-07]
- 2026-08-04 · IQM · H1-2026 results · revenue €8.9 M (+47%), cash €309 M · reported [P][26]
- 2026-08-06 · Rigetti · Q2-2026 results · revenue $5.1 M, GAAP loss $52.6 M, cash $541.3 M · reported [C][17]

**Market & supply chain.** Enabling equipment is more concentrated than the QPU market. Unit economics are unpublished; the €33 M IQM contract [P][26] and the $550 M Quantum Circuits price [C][G:DWAVE-QCI-2026-01] are the only quotable points. Paying goals: G7 (deployable systems) and G2 (error-mitigated utility) today; G3 (early fault tolerance) via QBI-style programmes from 2027 [G:QBI-STAGEC-2026]; G4 (large-scale fault tolerance) after 2029 [R][G:IBM-ROADMAP]; G1 (analog simulation), G5 (optimisation) and G6 (networking) bring no transmon-specific revenue.

**IP & standards.** PatSnap (to 2026-06-30): IBM 4,388 quantum patent families, Google 2,385, Microsoft 1,175; superconducting devices (H10N 60) IBM 783, Google 357 [P][52][G:PATSNAP-2026-06]. No litigation found; no transmon-specific family verified. Open stacks commoditise the layer above: Qiskit (IBM claims ≈ 70% of developers [C][45]), Cirq/Stim, OpenQASM 3, NVQLink [C][G:NVQLINK-2025].

**Roadmaps & track record.**
- IBM Kookaburra (2022-05-10 · 2025, as a 1,386-qubit multi-chip processor [C][56]; re-promised 2025-06-10 · 2026, as the first qLDPC module [R][59] · not delivered as of 2026-09-03 [R][53][G:IBM-ROADMAP]).
- IBM Nighthawk (2025-06-10 · 2025 · delivered 2025-12) and Starling (2025-06-10 · 2029, 200 logical / 10⁸ gates · open) [R][G:IBM-ROADMAP].
- Google milestone 3, 10⁻⁶ logical error (undated · no Willow successor published; neutral-atom track opened 2026-03-24) [R][10][G:GOOGLE-ATOMS-2026-03].
- Rigetti 108 q at 99.5% (promised for end-2025 · GA 2026-04-07 at median 99.1%; 99.5% moved to "later 2026") [C][G:RIGETTI-FIN-2026].
- Fujitsu/RIKEN 1,000 qubits (promised 2025-04-22 · fiscal 2026 · not launched as of 2026-09-03) [R][18][G:FUJITSU-1000Q].
Credibility: IBM high on cadence, weak on its first qLDPC module and on "advantage" claims; Google high on physics, opaque on schedule; Rigetti chronic slips; Fujitsu unproven.

**Strategic reading.** If transmons win, foundry owners and cryogenic suppliers win regardless of vendor; fabless transmon start-ups lose — consolidation (Atlantic Quantum → Google, 2025-10-03 [P][38][G:GOOGLE-ATLANTIC-2025-10]; Quantum Circuits → D-Wave) is visible. Substitution threats: fluxonium in the same fab, dual-rail/bosonic encodings that demote the transmon to an ancilla, atoms and spins for density. ³He, HEMT and fridge suppliers hold bargaining power; platform vendors escape by vertical integration.

*Open niche:* the credibility gap is at-scale QCVV — simultaneous, drift-aware, leakage- and burst-resolved benchmarks that buyers (EuroHPC, C-DAC, DARPA-style audits) lack — and the transmon–SFQ conflict (quasiparticle poisoning under cold digital control) is a measurement problem a QCVV/SFQ house can own first.

## Outlook & open questions

Milestones, 12–24 months: (1) Kookaburra runs a gross-code memory below break-even — confirm; nothing by end-2027 demotes IBM's 2029 date [R][G:IBM-ROADMAP]. (2) Google publishes Λ ≥ 3 or a 10⁻⁶ logical memory at d ≥ 9 — confirm; a second year without a Willow successor demotes [D][10]. (3) QBI Stage C (expected around Q4 2026 [G:QBI-STAGEC-2026][P][51]) promotes a transmon vendor. (4) SFQ or cryo-CMOS drives ≥ 50 transmons without a fidelity penalty [D][28][35]. Best case 2029: a Starling-class 200-logical machine [R][G:IBM-ROADMAP] and a d ≥ 11 Google memory; worst: Λ near 2, readout at 10⁻², bursts cap distance, the transmon survives only as an ancilla and capital rotates to atoms and spins. Open questions: does millisecond Ta/Si coherence survive a 100-qubit process with couplers; is the at-scale 2Q floor coherent (calibration) or incoherent; can readout reach 10⁻³ in < 300 ns across a lattice. Watch: Google's next paper, Kookaburra, the Stage C list.

## Sources

[1] Koch et al. · Charge-insensitive qubit design derived from the Cooper pair box · Phys. Rev. A 76, 042319 · 2007-10 · https://arxiv.org/abs/cond-mat/0703002
[2] Paik et al. · Observation of high coherence in Josephson junction qubits measured in a three-dimensional circuit QED architecture · Phys. Rev. Lett. 107, 240501 · 2011-12 · https://arxiv.org/abs/1105.4652
[3] Barends et al. · Superconducting quantum circuits at the surface code threshold for fault tolerance · Nature 508, 500 · 2014-04 · https://arxiv.org/abs/1402.4848
[4] Toshiba (Kubo et al.) · Double-transmon coupler CZ 99.90% in 48 ns · Phys. Rev. X 14, 041050 · 2024-11 · https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050
[5] [P] The Quantum Insider · Oxford researchers demonstrate fast 99.8%-fidelity two-qubit gate (25 ns CZ) · trade press · 2025-03-26 · https://thequantuminsider.com/2025/03/26/oxford-researchers-demonstrate-fast-99-8-fidelity-two-qubit-gate-using-simplified-circuit-design/
[6] Kandala et al. (IBM) · Engineered-ZZ cross-resonance CNOT at 99.77% · Phys. Rev. Lett. 127, 130501 · 2021-09 · https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501
[7] Google Quantum AI · Quantum error correction below the surface code threshold · Nature · 2024-12 · https://www.nature.com/articles/s41586-024-08449-y
[8] Bland et al. (Princeton) · 2D transmons with lifetimes and coherence times exceeding 1 millisecond · arXiv:2503.14798; Nature · 2025-03-19 · https://arxiv.org/abs/2503.14798
[9] USTC · 107-qubit surface code below threshold with leakage reset · Phys. Rev. Lett. · 2025-12 · https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31
[10] Google Quantum AI · RL-steered QEC, d=7 logical error 7.72×10⁻⁴ per cycle (arXiv:2511.08493) · Nature · 2026-07 · https://www.nature.com/articles/s41586-026-10759-2
[11] McEwen et al. · Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits · Nature Physics 18, 107 · 2022-01 · https://arxiv.org/abs/2104.05219
[12] McEwen et al. · Resisting high-energy impact events through gap engineering in superconducting qubit arrays · arXiv:2408.13687 · 2024-08 · https://arxiv.org/abs/2408.13687
[13] IQM · Above 99.9% fidelity single-qubit gates, two-qubit gates, and readout in a single superconducting quantum device · arXiv:2508.16437; PRX Quantum · 2025-08 · https://arxiv.org/abs/2508.16437
[14] [C] Google Quantum AI · Willow fidelities and "Quantum Echoes" verifiable advantage · Google blog · 2025-10 · https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/
[15] [C] IBM Quantum · What's new Q2 2026 (fleet EPLG) · IBM Quantum blog · 2026-07 · https://www.ibm.com/quantum/blog/whats-new-q2-2026
[16] Gao et al. (USTC) · Zuchongzhi 3.0, 105-qubit processor · Phys. Rev. Lett. 134, 090601 · 2025-03 · https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.090601
[17] [C] Rigetti · Second-quarter 2026 financial results · investor release · 2026-08-06 · https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2026-financial-results
[18] [C] Fujitsu · Quantum research page (1,000-qubit machine, fiscal 2026) · fujitsu.com · accessed 2026-09-03 · https://global.fujitsu/en-global/technology/research/quantum
[19] [P] The Quantum Insider · 10-plus companies leading the quantum technologies race in China · trade press · 2026-05-15 · https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/
[20] Arute et al. · Quantum supremacy using a programmable superconducting processor · Nature 574, 505 · 2019-10 · https://www.nature.com/articles/s41586-019-1666-5
[21] [C] IBM · Quantum roadmap to 2033 (Condor 1,121 qubits) · IBM Quantum blog · 2023-12 · https://www.ibm.com/quantum/blog/quantum-roadmap-2033
[22] Google Quantum AI · Scaling and logic in the colour code on a superconducting quantum processor · Nature · 2025-05 · https://www.nature.com/articles/s41586-025-09061-4
[23] Van Damme et al. (imec/KU Leuven) · Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers · Nature 634 · 2024-09-18 · https://www.nature.com/articles/s41586-024-07941-9
[24] Rigetti (Pappas et al.) · Alternating-bias assisted annealing of junctions · Communications Materials · 2024-08 · https://www.nature.com/articles/s43246-024-00596-z
[25] OQC · More than 500 qubits on one 3-inch die · arXiv:2602.12773 · 2026-02 · https://arxiv.org/abs/2602.12773
[26] [P] Investing.com · IQM Q2 2026 results slides: backlog up 52%, revenue up 47% in H1 · trade press · 2026-08 · https://www.investing.com/news/company-news/iqm-q2-2026-slides-backlog-surges-52-revenue-up-47-in-h1-93CH-4834587
[27] IBM · 14 nm cryo-CMOS qubit controller at 4 K · PRX Quantum 5, 010326 · 2024-02 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326
[28] SEEQC · SFQ qubit control at millikelvin · Nature Electronics · 2026-03-10 · https://www.nature.com/articles/s41928-026-01576-6
[29] [P] PostQuantum · QuantWare $178 M Series B (Intel Capital, In-Q-Tel, ETF Partners) · trade press · 2026-05-06 · https://postquantum.com/industry-news/quantware-178m-series-b-qoa/
[30] [P] Tom's Hardware · IBM spins off Anderon quantum chip foundry · trade press · 2026-05 · https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding
[31] US Department of Commerce / NIST · Letters of intent to 9 quantum companies, $2 billion · nist.gov · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[32] US BIS · Interim final rule: quantum ECCNs 4A906, 3A904, 3B904, 3A901.b · Federal Register (BIS-2024-0020) · 2024-09-06 · https://downloads.regulations.gov/BIS-2024-0020-0001/content.htm
[33] IBM · Relay-BP decoder for bivariate-bicycle codes on FPGA · arXiv:2510.21600 · 2025-10 · https://arxiv.org/abs/2510.21600
[34] [C] Bluefors · KIDE cryogenic platform (> 4,000 RF lines, > 1,000 qubits) · product page · revised 2026-06-16, accessed 2026-09-03 · https://bluefors.com/products/kide-cryogenic-platform/
[35] HRL Laboratories · Self-sequencing 4 K controller running a d=5 repetition code · arXiv:2604.16216; Nature · 2026-04-17 · https://arxiv.org/abs/2604.16216
[36] [C] IBM · Modular cryogenics: two coupled cells · IBM Quantum blog · 2026-08 · https://www.ibm.com/quantum/blog/modular-cryogenics
[37] Storz et al. (ETH Zürich) · Loophole-free Bell inequality violation with superconducting circuits (30 m cryogenic link, Bell-state fidelity 80.4%) · Nature 617, 265 · 2023-05 · https://www.nature.com/articles/s41586-023-05885-0
[38] [P] The Quantum Insider · Atlantic Quantum joins Google Quantum AI · trade press · 2025-10-03 · https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/
[39] Liu et al. · SFQ multi-chip module control limited by quasiparticle poisoning · PRX Quantum 4, 030310 · 2023-07 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310
[40] (authors not recorded) · Microwave–optical transduction gap analysis · arXiv:2503.10842 · 2025-03 · https://arxiv.org/abs/2503.10842
[41] Martiel, Chung, Seif, Ghosh, Hincks, Deshpande, Fefferman, Gambetta, Javadi-Abhari (IBM) · "Sampling hard circuits with verifiably high fidelity" — 70-qubit, depth-70 logical circuit with 468 T gates encoded in spacetime codes on 97 physical qubits, ~10× error suppression by syndrome post-selection · arXiv:2607.25941 · 2026-07-28 · https://arxiv.org/abs/2607.25941
[42] Pan, Chen, Zhang · Solving the sampling problem of the Sycamore quantum circuits · Phys. Rev. Lett. 129, 090502 · 2022-08 · https://arxiv.org/abs/2111.03011
[43] Kim et al. (IBM) · Evidence for the utility of quantum computing before fault tolerance · Nature 618, 500 · 2023-06 · https://www.nature.com/articles/s41586-023-06096-3
[44] Tindall et al. · Efficient tensor network simulation of IBM's Eagle kicked Ising experiment · PRX Quantum 5, 010308 · 2024-01 · https://arxiv.org/abs/2306.14887
[45] [C] IBM · IBM commits more than $10 billion to quantum computing · IBM newsroom · 2026-06-02 · https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers
[46] [C] IQM · IQM becomes first European quantum computing company listed on a major U.S. exchange · press release · 2026-07-02 · https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/
[47] [C] OQC · Series C, £260 M led by Bullhound · OQC newsroom · 2026-06-03 · https://oqc.tech/company/newsroom/series-c
[48] [C] D-Wave · D-Wave to acquire Quantum Circuits Inc. · press release · 2026-01-07 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[49] [C] Nord Quantique · Nord Quantique reaches $1.4 billion USD valuation · Business Wire · 2026-05-18 · https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment
[50] DARPA · QBI Stage B selection · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[51] [P] Quantum Ledger · DARPA QBI tracker (rosters, 2026-03 solicitation, Stage C timing) · secondary database · 2026-03 · https://quantumledger.report/darpa-qbi
[52] [P] PatSnap · Quantum computing patent landscape (data to 2026-06-30) · PatSnap blog · 2026-07 · https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape/
[53] [C] IBM · Quantum development and innovation roadmap (Kookaburra listed for 2026) · ibm.com · accessed 2026-09-03 · https://www.ibm.com/roadmaps/quantum/
[54] Jin et al. (MIT) · Thermal and residual excited-state population in a 3D transmon qubit · Phys. Rev. Lett. 114, 240501 · 2015-06 · https://arxiv.org/abs/1412.2772
[55] US GAO · Managing critical isotopes: weaknesses in DOE's management of helium-3 delayed the federal response to a critical supply shortage (GAO-11-472) · gao.gov · 2011-05-12 · https://www.gao.gov/products/gao-11-472
[56] [C] IBM · Expanding the IBM Quantum roadmap to anticipate the future of quantum-centric supercomputing (Kookaburra 1,386 q in 2025) · IBM Quantum blog · 2022-05-10 · https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025
[57] Bravyi et al. (IBM) · High-threshold and low-overhead fault-tolerant quantum memory · Nature 627, 778 · 2024-03 · https://arxiv.org/abs/2308.07915
[58] [P] Quantum Computing Report · SEEQC and IBM collaborate on SFQ control integration under DARPA's QBI · trade press · 2025-06-12 · https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/
[59] [C] IBM · IBM sets the course to build world's first large-scale, fault-tolerant quantum computer (Starling 2029, Blue Jay 2033) · IBM newsroom · 2025-06-10 · https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center

## Open verification items

- IQM market capitalisation ≈ $2.6 B (2026-08): no primary source found; the figure is not listed.
- Rigetti's 1,000-qubit / 99.9% target and its date: no source was established for either, and both are omitted.
- Bluefors KIDE "> 4,000 RF lines / > 1,000 qubits": product page revised 2026-06-16; no launch date established.
- IBM "> $1.1 B of client contracts since 2017" [C][45]: not independently verified; the figure is not listed.
- Cross-resonance gate time ≈ 200–500 ns: fleet-typical range inferred from a single-device paper [6]; no fleet-wide source.
- Cepheus-1-108Q chiplet count: no verified figure, so none is given.
- imec 300 mm yield 393 of 400 (98.25%): cited against [23]; the median T1 for that run is ≈ 75 µs.
- Source [40] (arXiv:2503.10842): no author list is given for it; the "≈ 3 orders of magnitude" transduction gap is cited from the literature.
- "4 K HEMT amplifiers effectively one vendor (Low Noise Factory)": a market observation; no database source.
