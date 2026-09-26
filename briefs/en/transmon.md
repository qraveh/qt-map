---
id: transmon
name: Transmon
layer: 1 Carrier
status: demonstrated
since: 2007
one_line: Capacitively shunted Josephson junction (Koch 2007); the carrier behind Willow, Heron/Nighthawk and Zuchongzhi, with the fastest deterministic gate and QEC cycle of any demonstrated qubit.
verdict: Best-funded and fastest carrier, capped by ~10⁻³ two-qubit and ~10⁻² readout errors at scale and hourly correlated bursts. Confirm if a ≥100-qubit lattice shows Λ ≥ 3 with median 2Q error < 10⁻³ by 2028; otherwise demote to component status.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A transmon is an Al/AlOx/Al Josephson junction shunted by a large capacitor so that E_J/E_C ≈ 50–100 [D][206]. Charge dispersion falls exponentially in √(8E_J/E_C), removing 1/f charge noise at the price of a weak anharmonicity α ≈ −E_C ≈ −200 to −300 MHz; the qubit is the lowest two levels of a 4–6 GHz oscillator [D][206]. Koch et al. proposed it in 2007 [D][206]; the 3D transmon (2011) [D][207] and the UCSB/Google Xmon (2014) [D][208] fixed the two lineages still in use, fixed-frequency (IBM) and flux-tunable (Google, IQM, USTC).

Attributes (technology graph):
- a: affinity 1.0, fabricated (no natural counterpart).
- b: characteristic time 10⁻⁸ s, deterministic entangling; the 1/α leakage bound puts the pulse floor near 10 ns.
- c: readout dispersive microwave, 10⁻⁶·⁵ s (≈ 320 ns), non-destructive, mid-circuit capable.
- d: mobility static, nearest-neighbour wiring.
- e: control microwave from room-temperature electronics; cold-stage variants (cryo-CMOS, SFQ) at ≤ 5 qubits.
- f: error structure leakage + stochastic Pauli + correlated bursts + coherent/calibration.
- g: manufacturing superconducting lithography.

## Physics & limits

Residual thermal population (0.1% at 35 mK in a 3D transmon [D][209], ≈ 1% at 40–60 mK for a 5 GHz qubit [S][209]) makes reset and readout the SPAM floor. Anharmonicity bounds single-qubit gates at 10–25 ns and tunable-coupler CZ at 25–50 ns [D][1], [36][P][210]; cross-resonance takes ≈ 200–500 ns [D][211].

The floor is decoherence over gate time: with Willow's mean T1 = 68 µs [D][1] a 40 ns CZ carries ≈ 6×10⁻⁴ of incoherent error [S][1]; at the record T1 = 1.68 ms of a single Ta-on-Si test transmon [D][212] it falls below 5×10⁻⁵ [S][212]. Loss is dominated by two-level systems (TLS) in amorphous interface oxides [D][212], with quasiparticles, Purcell decay and flux noise below.

Most of the twirled channel is stochastic Pauli, so Willow's Λ = 2.14 [D][1] matches theory. Leakage to |2⟩ accumulates under QEC unless removed each cycle (USTC's all-microwave reset cut it 72×, to 6.4×10⁻⁴, on 107 qubits [D][3]). Coherent errors (residual ZZ, TLS drift) forced reinforcement-learning recalibration inside Google's 2026-07 QEC run [D][2]. Correlated bursts (ionizing particles flooding the chip with quasiparticles) hit all qubits at once — roughly one per 10 s on Sycamore in 2021 [D][213], about one per hour on Willow after gap engineering [D][1], [214] — truncating long memory runs by bursts, not distance. Moving the floor means new materials (Ta, encapsulated Nb), fluxonium-scale anharmonicity, radiation management or erasure conversion (dual-rail).

## Engineering state of the art

Best isolated devices: T1 1.68 ms, Q 2.5×10⁷, 1Q 99.994% [D][212]; CZ 99.93% and 280 ns readout at 99.94% on a two-qubit IQM chip [D][37]; Toshiba's double-transmon coupler CZ 99.90% in 48 ns [D][36].

Typical at ≥ 100 qubits: Willow, 105 q — mean T1 68 µs, CZ error 0.33%, readout 99.5%, QEC cycle 1.1 µs [D][1][C][31]; IBM fleet error-per-layered-gate 3.7×10⁻³ typical, 1.9×10⁻³ best (2026-07) [C][33]; Zuchongzhi 3.0, 105 q — 2Q 99.62%, readout 99.13% [D][34]; Rigetti Cepheus-1-108Q chiplets — median 2Q 99.1% [C][G:RIGETTI-FIN-2026].

| Year | Figure | Who | Evidence |
|---|---|---|---|
| 2019 | Sycamore 53 q, simultaneous 2Q error 0.62% | Google | [D][215] |
| 2023 | Condor, 1,121 qubits on one chip | IBM | [C][216] |
| 2024 | Willow 105 q, Λ = 2.14 | Google | [D][1] |
| 2025 | 2D transmon T1 1.68 ms | Princeton | [D][212] |
| 2026 | d=7 logical error 7.72×10⁻⁴ per cycle | Google | [D][2] |

At scale the two-qubit gate is the largest error term (~40% of Google's colour-code budget) [D][40], then readout (~10⁻² on fleets [C][33]) and leakage; the lattice tail matters more than the median.

## Manufacturing, materials & supply chain

Process: Nb or Ta on high-resistivity Si or sapphire; shadow-evaporated Al/AlOx/Al junctions; flip-chip 3D integration. On 300 mm CMOS tooling imec/KU Leuven reported 393 of 400 working transmons (98.25%), median T1 ≈ 75 µs (42–113 µs) [D][217][G:IMEC-300MM-2025]: uniformity, not coherence. Fixed-frequency lattices must also hit frequency targets (junction scatter becomes collisions) by laser annealing (IBM), alternating-bias annealing (Rigetti, 97.4% success) [D][218] or tunable couplers.

Cost and energy: no vendor publishes $/qubit; proxies are IQM's €33 M LUMI contract [P][219] and IBM's 14 nm cryo-controller at 23 mW per qubit at 4 K [D][220] — tens of watts at 10³ qubits, hence the SFQ case (nW per qubit claimed [C][52]).

Supply chain: dilution refrigerators from Bluefors (FI), Oxford Instruments (UK), FormFactor and Maybell (US); ³He from tritium decay in state inventories (US: NNSA [G][221]), no merchant producer; 4 K HEMT amplifiers effectively one vendor (Low Noise Factory, SE); control electronics competitive (Quantum Machines, Qblox, Zurich Instruments); merchant QPUs from QuantWare (NL) [P][222]; foundries Anderon (IBM Albany spin-off, 2026-05; $1 B CHIPS letter of intent, $1 B IBM cash stated separately) [P][223][G][224] and GlobalFoundries ($375 M LOI) [G][224].

Export controls: the BIS interim final rule of 2024-09-06 covers quantum computers from 34 qubits (ECCN 4A906), dilution refrigerators ≥ 600 µW at 0.1 K for 48 h (3A904), cryogenic wafer probers (3B904) and parametric amplifiers (3A901.b) [G][225][G:BIS-QUANTUM-2024]; Chinese vendors therefore build 10 mK refrigerators domestically (2026-05-15) [P][226].

## Control, readout & I/O burden

A tunable lattice needs one XY and one Z line per qubit plus one per coupler (Sycamore: ≈ 3.6 control lines per qubit before readout [D][215]); readout multiplexes ≈ 6–10 qubits per feedline [D][1]; each line is a DAC channel plus attenuated coax, so cost and heat scale with N.

Latency: the QEC cycle is 1.1 µs; Google's real-time decoder ran at 63 µs mean latency for d=5 [D][1]; IBM's Relay-BP targets < 1 µs per cycle in simulation [S][46] for the gross code (IBM's [[144,12,12]] bivariate-bicycle qLDPC code, 12 logical qubits in 288 physical [D][227]).

Walls: 10³ reached (Condor, 1,121 qubits [C][216]); Bluefors' KIDE (> 4,000 RF lines, > 1,000 qubits; product page, 2026-06) [C][228] is one cryostat's ceiling. 10⁴ needs 4 K cryo-CMOS (HRL: d=5 repetition code from a ≤ 3.5 W controller [D][163][G:HRL-2026]) or millikelvin SFQ (SEEQC: 1Q up to 99.9% on ≤ 5 qubits [D][229][G:SEEQC-2026]) plus multi-cryostat modules (IBM coupled two cells, 2026-08 [C][48]). 10⁶ has no closed design: on-chip flux DACs, cold decoding and inter-fridge links (ETH: 30 m at 80.4% Bell fidelity [D][230]) are sub-scale.

## Role in the stack

Paths: the superconducting path and the dual-rail erasure path (transmon as ancilla or one rail); no off-diagonal reading, not a hub. Requires superconducting lithography; provides the carrier for tunable-coupler and cross-resonance gates, the ancilla for bosonic-cavity gates, the bare-qubit subspace, the dispersive shift for microwave readout and the microwave side of the optical transducer. Replaced by fluxonium, which buys anharmonicity and T1 for a flux bias per qubit, sub-GHz control and redesigned readout. Conflicts with SFQ control: switching photons poisoned qubits with quasiparticles in the 2023 multi-chip module (0.96 of 1.2% error per Clifford) [D][231]; SEEQC claims it engineered away [C][52], so the conflict stands until an independent lattice-scale check. Derived clock of the superconducting path ≈ 6.5×10⁻⁷ s (651 ns; derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path), readout 282 ns of it and readout-plus-reset two-thirds, against the measured 1.1 µs Willow cycle [D][1] — the fastest demonstrated path, which G4 (large-scale fault tolerance) pays for. Bordering empty slots: the microwave–optical transducer (≈ 3 orders of magnitude short of remote gates [S][232]) and cryogenic decoding.

## Verification (QCVV)

Headline numbers come from Clifford RB/IRB, simultaneous XEB (Google), IBM's layer fidelity/EPLG and readout assignment matrices; Λ is a fit of logical error vs distance under one decoder. Missed here: isolated vs simultaneous operation (record chips are isolated); coherent errors averaged into a depolarising number; leakage, invisible to RB and often post-selected away; drift between calibration and use; and conventions (Rigetti quotes medians, IBM its best device, IQM a two-qubit chip). IBM's 2026-07 "70 logical qubits" is an error-detecting, post-selected result [D][45], not fault tolerance.

Replication: below-threshold scaling reproduced by USTC on 107 qubits with Λ = 1.40 [D][3]. Disputes: 2019 supremacy sampling reproduced by tensor networks [D][233]; the 2023 IBM "utility" experiment simulated classically within weeks [D][234], [235]; Google's 2026-07 paper reports no Λ for the d=7 run [D][2]. Value conflict: imec's 300 mm T1 is often quoted as "> 100 µs"; the paper's median is ≈ 75 µs [D][217][G:IMEC-300MM-2025], used here.

## Actors & economics

**Who.**

| Organisation | Role | Country | Activity | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | Willow 105 q, Λ = 2.14; d=7 memory | [D][1], [2] |
| IBM | developer | US | Heron/Nighthawk fleet; Starling roadmap; Anderon spin-out | [C][33], [62][P][223] |
| Rigetti | developer | US | Cepheus-1-108Q chiplets; own fab | [C][236] |
| IQM | developer | FI | 26 systems sold, 17 installed | [C][56][G:IQM-LISTING-2026-07] |
| USTC | research | CN | Zuchongzhi 3.x, 105 q; Λ = 1.40 | [D][3], [34] |
| SEEQC | supplier | US | millikelvin SFQ control; IBM integration under QBI | [D][229][G:SEEQC-2026] |

**Money.**
- 2025-11-06 · DARPA · QBI Stage B (up to $15 M each) · IBM the only transmon-lattice vendor of eleven; Google and Rigetti stayed at Stage A [G][60][G:QBI-STAGEB-2025-11][G:QBI-STAGEA-2025-04]
- 2026-01-20 · D-Wave · M&A, Quantum Circuits (dual-rail cavities on transmon ancillae) · $550 M (stock + cash) · closed [C][14][G:DWAVE-QCI-2026-01][G:DUALRAIL-CZ-2026-08]
- 2026-05-05 · QuantWare (merchant QPUs; VIO-40K roadmap [R][G:QUANTWARE-VIO]) · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners (new investors, no lead) · > $210 M cumulative · closed [P][222]
- 2026-05-18 · Nord Quantique · growth-equity financing · $30 M at a $1.4 B valuation · closed [C][84][G:NQ-1.4B-2026-05]
- 2026-05-21 · US Dept of Commerce · CHIPS letters of intent ($2.013 B, nine companies) · IBM/Anderon $1 B, GlobalFoundries $375 M, Rigetti ≤ $100 M, D-Wave $100 M · non-binding LOI [G][224][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · commitment · > $10 B over five years, the $1 B cash into Anderon stated separately · announced [C][237][G:IBM-10B-2026-06]
- 2026-06-03 · OQC (coaxmon developer [D][238]) · Series C · £260 M (~$350 M) · led by Bullhound · valuation undisclosed · closed [C][57][G:OQC-SERIESC-2026-06]
- 2026-07-02 · IQM · listing, Nasdaq and Helsinki · pro-forma cash €337 M · closed [C][G:IQM-LISTING-2026-07]
- 2026-08-04 · IQM · H1-2026 results · revenue €8.9 M (+47%), cash €309 M · reported [P][219]
- 2026-08-06 · Rigetti · Q2-2026 results · revenue $5.1 M, GAAP loss $52.6 M, cash $541.3 M · reported [C][236]

**Market & supply chain.** Enabling equipment is more concentrated than the QPU market. Unit economics are unpublished; the €33 M IQM contract [P][219] and the $550 M Quantum Circuits price [C][G:DWAVE-QCI-2026-01] are the only quotable points. Paying goals: G7 (deployable systems) and G2 (error-mitigated utility) today; G3 (early fault tolerance) via QBI-style programmes from 2027 [G:QBI-STAGEC-2026]; G4 (large-scale fault tolerance) after 2029 [R][G:IBM-ROADMAP]; G1 (analog simulation), G5 (optimisation) and G6 (networking) bring no transmon-specific revenue.

**IP & standards.** PatSnap (to 2026-06-30): IBM 4,388 quantum patent families, Google 2,385, Microsoft 1,175; superconducting devices (H10N 60) IBM 783, Google 357 [P][239][G:PATSNAP-2026-06]. No litigation found; no transmon-specific family verified. Open stacks commoditise the layer above: Qiskit (IBM claims ≈ 70% of developers [C][237]), Cirq/Stim, OpenQASM 3, NVQLink [C][G:NVQLINK-2025].

**Roadmaps & track record.**
- IBM Kookaburra (2022-05-10 · 2025, as a 1,386-qubit multi-chip processor [C][240]; re-promised 2025-06-10 · 2026, as the first qLDPC module [R][62] · not delivered as of 2026-09-03 [R][67][G:IBM-ROADMAP]).
- IBM Nighthawk (2025-06-10 · 2025 · delivered 2025-12) and Starling (2025-06-10 · 2029, 200 logical / 10⁸ gates · open) [R][G:IBM-ROADMAP].
- Google milestone 3, 10⁻⁶ logical error (undated · no Willow successor published; neutral-atom track opened 2026-03-24) [R][2][G:GOOGLE-ATOMS-2026-03].
- Rigetti 108 q at 99.5% (promised for end-2025 · GA 2026-04-07 at median 99.1%; 99.5% moved to "later 2026") [C][G:RIGETTI-FIN-2026].
- Fujitsu/RIKEN 1,000 qubits (promised 2025-04-22 · fiscal 2026 · not launched as of 2026-09-03) [R][70][G:FUJITSU-1000Q].
Credibility: IBM high on cadence, weak on its first qLDPC module and on "advantage" claims; Google high on physics, opaque on schedule; Rigetti chronic slips; Fujitsu unproven.

**Strategic reading.** If transmons win, foundry owners and cryogenic suppliers win regardless of vendor; fabless transmon start-ups lose — consolidation (Atlantic Quantum → Google, 2025-10-03 [P][53][G:GOOGLE-ATLANTIC-2025-10]; Quantum Circuits → D-Wave) is visible. Substitution threats: fluxonium in the same fab, dual-rail/bosonic encodings that demote the transmon to an ancilla, atoms and spins for density. ³He, HEMT and fridge suppliers hold bargaining power; platform vendors escape by vertical integration.

*Open niche:* the credibility gap is at-scale QCVV — simultaneous, drift-aware, leakage- and burst-resolved benchmarks that buyers (EuroHPC, C-DAC, DARPA-style audits) lack — and the transmon–SFQ conflict (quasiparticle poisoning under cold digital control) is a measurement problem a QCVV/SFQ house can own first.

## Outlook & open questions

Milestones, 12–24 months: (1) Kookaburra runs a gross-code memory below break-even — confirm; nothing by end-2027 demotes IBM's 2029 date [R][G:IBM-ROADMAP]. (2) Google publishes Λ ≥ 3 or a 10⁻⁶ logical memory at d ≥ 9 — confirm; a second year without a Willow successor demotes [D][2]. (3) QBI Stage C (expected around Q4 2026 [G:QBI-STAGEC-2026][P][241]) promotes a transmon vendor. (4) SFQ or cryo-CMOS drives ≥ 50 transmons without a fidelity penalty [D][163], [229]. Best case 2029: a Starling-class 200-logical machine [R][G:IBM-ROADMAP] and a d ≥ 11 Google memory; worst: Λ near 2, readout at 10⁻², bursts cap distance, the transmon survives only as an ancilla and capital rotates to atoms and spins. Open questions: does millisecond Ta/Si coherence survive a 100-qubit process with couplers; is the at-scale 2Q floor coherent (calibration) or incoherent; can readout reach 10⁻³ in < 300 ns across a lattice. Watch: Google's next paper, Kookaburra, the Stage C list.

## Sources

[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[31] Y. Chen and M. Devoret, “Our quantum hardware: the engine for verifiable quantum advantage,” Google Blog, Oct. 22, 2025. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ [C]
[33] IBM Quantum, “What's new at IBM Quantum - Q2 2026.” [Online]. Available: https://www.ibm.com/quantum/blog/whats-new-q2-2026 [C]
[34] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[36] R. Li, K. Kubo, Y. Ho, Z. Yan, Y. Nakamura, and H. Goto, “Realization of High-Fidelity CZ Gate Based on a Double-Transmon Coupler,” *Phys. Rev. X*, vol. 14, no. 4, Art. no. 041050, Nov. 2024, doi: [10.1103/PhysRevX.14.041050](https://doi.org/10.1103/PhysRevX.14.041050). [arXiv:2402.18926](https://arxiv.org/abs/2402.18926). [D]
[37] F. Marxer *et al.*, “Above 99.9% Fidelity Single-Qubit Gates, Two-Qubit Gates, and Readout in a Single Superconducting Quantum Device,” *PRX Quantum*, vol. 7, Art. no. 020333, 2026, doi: [10.1103/n86s-2b88](https://doi.org/10.1103/n86s-2b88). [arXiv:2508.16437](https://arxiv.org/abs/2508.16437). [D]
[40] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[45] S. Martiel *et al.*, “Sampling hard circuits with verifiably high fidelity,” [arXiv:2607.25941](https://arxiv.org/abs/2607.25941), Jul. 2026. [D]
[46] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[48] C. Dundon, S. Hall, M. Hollister, and A. Lindler, “IBM's new modular architecture for cryogenic systems,” IBM Quantum Computing Blog, Aug. 19, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/modular-cryogenics [C]
[52] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [C]
[53] M. Swayne, “Atlantic Quantum Joins Google Quantum AI,” The Quantum Insider, Oct. 3, 2025. [Online]. Available: https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/ [P]
[56] IQM Quantum Computers, “IQM Quantum Computers Becomes First European Quantum Computing Company Listed on a Major U.S. Exchange,” Jul. 2, 2026. [Online]. Available: https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ [C]
[57] A. Curbison, “OQC raises £260m in Europe's largest ever private quantum computing funding round,” OQC, Jun. 2, 2026. [Online]. Available: https://oqc.tech/company/newsroom/series-c [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[62] IBM, “IBM Sets the Course to Build World's First Large-Scale, Fault-Tolerant Quantum Computer at New IBM Quantum Data Center,” Jun. 10, 2025. [Online]. Available: https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center [C]
[67] IBM, “Quantum Roadmap.” [Online]. Available: https://www.ibm.com/roadmaps/quantum/ [R]
[70] Fujitsu, “Fujitsu Quantum.” [Online]. Available: https://global.fujitsu/en-global/technology/research/quantum [R]
[84] Nord Quantique, “Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment,” Business Wire, May 18, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment [C]
[163] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[206] J. Koch *et al.*, “Charge-insensitive qubit design derived from the Cooper pair box,” *Phys. Rev. A*, vol. 76, no. 4, Art. no. 042319, Oct. 2007, doi: [10.1103/PhysRevA.76.042319](https://doi.org/10.1103/PhysRevA.76.042319). [arXiv:cond-mat/0703002](https://arxiv.org/abs/cond-mat/0703002). [D]
[207] H. Paik *et al.*, “Observation of High Coherence in Josephson Junction Qubits Measured in a Three-Dimensional Circuit QED Architecture,” *Phys. Rev. Lett.*, vol. 107, no. 24, Art. no. 240501, Dec. 2011, doi: [10.1103/PhysRevLett.107.240501](https://doi.org/10.1103/PhysRevLett.107.240501). [arXiv:1105.4652](https://arxiv.org/abs/1105.4652). [D]
[208] R. Barends *et al.*, “Superconducting quantum circuits at the surface code threshold for fault tolerance,” *Nature*, vol. 508, no. 7497, pp. 500–503, Apr. 2014, doi: [10.1038/nature13171](https://doi.org/10.1038/nature13171). [arXiv:1402.4848](https://arxiv.org/abs/1402.4848). [D]
[209] X. Y. Jin *et al.*, “Thermal and Residual Excited-State Population in a 3D Transmon Qubit,” *Phys. Rev. Lett.*, vol. 114, no. 24, Art. no. 240501, Jun. 2015, doi: [10.1103/PhysRevLett.114.240501](https://doi.org/10.1103/PhysRevLett.114.240501). [arXiv:1412.2772](https://arxiv.org/abs/1412.2772). [D]
[210] C. Choucair, “Oxford Researchers Demonstrate Fast, 99.8% Fidelity Two-Qubit Gate Using Simplified Circuit Design,” The Quantum Insider, Mar. 26, 2025. [Online]. Available: https://thequantuminsider.com/2025/03/26/oxford-researchers-demonstrate-fast-99-8-fidelity-two-qubit-gate-using-simplified-circuit-design/ [P]
[211] A. Kandala *et al.*, “Demonstration of a High-Fidelity CNOT Gate for Fixed-Frequency Transmons with Engineered ZZ Suppression,” *Phys. Rev. Lett.*, vol. 127, no. 13, Art. no. 130501, Sep. 2021, doi: [10.1103/PhysRevLett.127.130501](https://doi.org/10.1103/PhysRevLett.127.130501). [D]
[212] M. P. Bland *et al.*, “2D transmons with lifetimes and coherence times exceeding 1 millisecond,” [arXiv:2503.14798](https://arxiv.org/abs/2503.14798), Mar. 2025. [D]
[213] M. McEwen *et al.*, “Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits,” *Nat. Phys.*, vol. 18, no. 1, pp. 107–111, Dec. 2021, doi: [10.1038/s41567-021-01432-8](https://doi.org/10.1038/s41567-021-01432-8). [arXiv:2104.05219](https://arxiv.org/abs/2104.05219). [D]
[214] M. McEwen *et al.*, “Resisting High-Energy Impact Events through Gap Engineering in Superconducting Qubit Arrays,” *Phys. Rev. Lett.*, vol. 133, no. 24, Art. no. 240601, Dec. 2024, doi: [10.1103/PhysRevLett.133.240601](https://doi.org/10.1103/PhysRevLett.133.240601). [arXiv:2402.15644](https://arxiv.org/abs/2402.15644). [D]
[215] F. Arute *et al.*, “Quantum supremacy using a programmable superconducting processor,” *Nature*, vol. 574, no. 7779, pp. 505–510, Oct. 2019, doi: [10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5). [D]
[216] J. Gambetta, “The hardware and software for the era of quantum utility is here,” IBM Quantum Computing Blog, Dec. 4, 2023. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-roadmap-2033 [C]
[217] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[218] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[219] Investing.com, “IQM Q2 2026 slides: backlog surges 52%, revenue up 47% in H1,” Aug. 4, 2026. [Online]. Available: https://www.investing.com/news/company-news/iqm-q2-2026-slides-backlog-surges-52-revenue-up-47-in-h1-93CH-4834587 [P]
[220] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[221] U.S. Government Accountability Office, “Managing Critical Isotopes: Weaknesses in DOE's Management of Helium-3 Delayed the Federal Response to a Critical Supply Shortage,” U.S. Government Accountability Office, May 2011. [Online]. Available: https://www.gao.gov/products/gao-11-472 [G]
[222] M. Ivezic, “QuantWare Raises $178M Series B — What It Means for Quantum Open Architecture,” PostQuantum.com, May 6, 2026. [Online]. Available: https://postquantum.com/industry-news/quantware-178m-series-b-qoa/ [P]
[223] L. James, “IBM spins off America's first quantum chip foundry with $2 billion in federal and private funding — newly-minted 'Anderon' foundry to offer 300mm quantum wafer fab and manufacturing services,” Tom's Hardware, May 26, 2026. [Online]. Available: https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding [P]
[224] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[226] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[227] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[228] Bluefors, “KIDE Cryogenic Platform — For Large-Scale Quantum Computing,” Jun. 16, 2026. [Online]. Available: https://bluefors.com/products/kide-cryogenic-platform/ [C]
[229] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[230] S. Storz *et al.*, “Loophole-free Bell inequality violation with superconducting circuits,” *Nature*, vol. 617, no. 7960, pp. 265–270, May 2023, doi: [10.1038/s41586-023-05885-0](https://doi.org/10.1038/s41586-023-05885-0). [D]
[231] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[232] N. Dirnegger *et al.*, “Distilled remote entanglement between superconducting qubits across optical channels,” [arXiv:2503.10842](https://arxiv.org/abs/2503.10842), Mar. 2025. [S]
[233] F. Pan, K. Chen, and P. Zhang, “Solving the Sampling Problem of the Sycamore Quantum Circuits,” *Phys. Rev. Lett.*, vol. 129, no. 9, Art. no. 090502, Aug. 2022, doi: [10.1103/PhysRevLett.129.090502](https://doi.org/10.1103/PhysRevLett.129.090502). [arXiv:2111.03011](https://arxiv.org/abs/2111.03011). [D]
[234] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[235] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[236] Rigetti Computing, “Rigetti Computing Reports Second Quarter 2026 Financial Results,” Rigetti Investor Relations, Aug. 6, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2026-financial-results [C]
[237] IBM, “IBM Commits More Than $10 Billion to Quantum Computing, Funding Its Roadmap from Today's Leading Systems to the World's First Fault-Tolerant Quantum Computers,” Jun. 2, 2026. [Online]. Available: https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers [C]
[238] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [D]
[239] PatSnap, “Quantum Computing Patent Landscape 2026,” Jun. 30, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape/ [P]
[240] J. Gambetta, “Expanding the IBM Quantum roadmap to anticipate the future of quantum-centric supercomputing,” IBM Quantum Blog, May 10, 2022. [Online]. Available: https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025 [C]
[241] Quantum Ledger, “DARPA QBI Tracker.” [Online]. Available: https://quantumledger.report/darpa-qbi [P]

## Open verification items

- IQM market capitalisation ≈ $2.6 B (2026-08): no primary source found; the figure is not listed.
- Rigetti's 1,000-qubit / 99.9% target and its date: no source was established for either, and both are omitted.
- Bluefors KIDE "> 4,000 RF lines / > 1,000 qubits": product page revised 2026-06-16; no launch date established.
- IBM "> $1.1 B of client contracts since 2017" [C][237]: not independently verified; the figure is not listed.
- Cross-resonance gate time ≈ 200–500 ns: fleet-typical range inferred from a single-device paper [211]; no fleet-wide source.
- Cepheus-1-108Q chiplet count: no verified figure, so none is given.
- imec 300 mm yield 393 of 400 (98.25%): cited against [217]; the median T1 for that run is ≈ 75 µs.
- Source [232] (arXiv:2503.10842): no author list is given for it; the "≈ 3 orders of magnitude" transduction gap is cited from the literature.
- "4 K HEMT amplifiers effectively one vendor (Low Noise Factory)": a market observation; no database source.
