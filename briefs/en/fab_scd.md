---
id: fab_scd
name: Superconductor-digital fabrication (multilayer niobium processes, SFQ/AQFP logic)
layer: "10 Manufacturing"
status: demonstrated
since: 2010
one_line: "Planarised multilayer niobium processes for superconducting digital logic, up to eight Nb wiring layers with 10 kA/cm² junctions on 200 mm wafers or two junction layers in one stack; the family's smaller members, three to six layers at 250 A/cm² to 1 kA/cm², make the SFQ control dies and on-chip flux DACs of superconducting quantum processors."
verdict: "An industrial process family, demonstrated in quantum hardware through D-Wave's annealers, whose qubits, flux DACs and readout share one multilayer stack; for gate-model machines it is still emerging — the SFQ dies that have driven qubits came from three-layer research processes and one five-qubit company module, and the eight-layer nodes have built classical circuits only. Confirm with an SFQ control die from a multilayer node driving more than twenty gate-model qubits; demote its gate-model role if none exists by 2029."
updated: 2026-11-22
---

SFQ = single flux quantum; RSFQ / ERSFQ = rapid / energy-efficient rapid SFQ logic; AQFP = adiabatic quantum-flux-parametron; QFP = quantum flux parametron; J_c = junction critical current density; I_c = junction critical current; MCM = multichip module; CMP = chemical-mechanical planarisation; DAC = digital-to-analogue converter; MIT LL = MIT Lincoln Laboratory; AIST = National Institute of Advanced Industrial Science and Technology (Japan); SIMIT = Shanghai Institute of Microsystem and Information Technology (Chinese Academy of Sciences); NIST = US National Institute of Standards and Technology; PECVD = plasma-enhanced chemical vapour deposition; QPU = quantum processing unit; IARPA = US Intelligence Advanced Research Projects Activity; BIS = US Bureau of Industry and Security; ECCN = export control classification number; CMOS = complementary metal–oxide–semiconductor.

## Identity & lineage

Superconductor digital logic stores a bit as one flux quantum and switches it with shunted Josephson junctions; its process is a planarised stack of niobium wiring layers, one or two Nb/Al–AlOx/Nb junction layers, resistors and oxide, the opposite of the minimal stack on which most qubits are made (`fab_sc`), a contrast D-Wave's 2026 whitepaper draws itself [C][316]. MIT LL's nodes are the reference: SFQ4ee, eight superconducting layers at 0.5 µm, and SFQ5ee, eight Nb wiring layers at 350 nm plus a MoNx kinetic-inductance layer, each with one layer of 10 kA/cm² junctions (700 nm minimum) and fully planarised circuit layers on 200 mm wafers [D][953]. AIST's line runs from the nine-layer ADP2 to a 10 kA/cm² planarised process and two low-J_c variants for qubit-interface circuits, 250 A/cm² and the 1 kA/cm² 1KP of 2025 [D][571]; Yokohama National University's AQFP logic was built in 2017 in an AIST process with two active layers around one ground plane [D][954]. SIMIT-Nb08 (Oct 2026) puts two junction layers and dual ground planes into an eight-layer niobium process [D][955]. SEEQC, spun out of Hypres in 2019, owns a commercial multilayer foundry in Elmsford, New York [C][572]; imec has made NbTiN junctions and interconnects within a 420 °C CMOS back-end budget on 300 mm wafers (Dec 2024) [C][956].

The quantum link predates the gate-model work. In 2010 D-Wave programmed an eight-qubit cell through an on-chip SFQ demultiplexer and 64 flux DACs made in the qubits' own four-Nb-layer process, and read 128 qubits through QFP latches [D][957], [608]; Johnson and colleagues cite earlier SFQ-control experiments on flux qubits, not reached here. Gate-model control — by the later authors' account the first SFQ-driven gates — began in 2019 with an SFQ driver co-fabricated on a transmon chip (three Nb layers, about 1 kA/cm²) [D][566], moved in 2023 to a separate die made at NIST Boulder (three superconducting layers, 1 kA/cm²) and bump-bonded to two transmons [D][249], and reached a five-qubit flip-chip module at millikelvin temperature at SEEQC in 2026, its SFQ carrier chip made in SEEQC's own foundry in a 1 kA/cm² niobium junction process with a high-kinetic-inductance layer and further niobium wiring and ground-plane layers [D][304]. No SFQ die that has driven a qubit is published as a product of an eight-layer node; those nodes appear through designs, DigiQ's cell library calibrated against SFQ5ee and QECOOL's built on AIST's 10 kA/cm² library [S][958], [745].

Attributes (technology graph): carrier affinity 1.0, fabricated. Characteristic time: none. Readout: none of its own. Mobility: none. Control modality: none; its products sit at 4 K or millikelvin. Error structure: coherent, the critical-current and inductance spread that circuits absorb as margin or calibration. Manufacturing: superconducting lithography, multilayer niobium on 200 mm silicon; NbTiN on 300 mm CMOS lines in development.

## Physics & limits

At 4.2 K a logic junction needs I_c of 100–300 µA for its Josephson energy to dwarf thermal energy, hence digital nodes near 10 kA/cm²; at 10 mK, I_c ≳ 0.4 µA suffices, so AIST chose 1 kA/cm² for a 10 µA minimum junction [D][571]. The price is inductor area, about 2 nH for a 1 µA junction [D][571]. Inductor area binds at 4.2 K too: SFQ5ee added a kinetic-inductance layer, target 8 pH/sq, for the ~100 pH bias inductors of ERSFQ circuits [D][953]. In the 1KP, RSFQ dissipates 3.2% of conventional RSFQ, and a qubit-control pulse generator would fall from 51.7 µW to 1.65 µW [S][571], against about 10 µW of cooling at 10 mK, as the authors cite [D][571].

Superconductor electronics integrate 1–10 million junctions per cm² against more than 10 billion transistors per cm² in advanced CMOS, as Papanikolaou and colleagues cite [D][897]. A second junction layer attacks routing congestion: for a routed 320-cell shift register SIMIT's post-route benchmark estimates 32.2% less area, 25.0% higher maximum frequency and 65.3% less power than with its Nb03 process [S][955]. Hydrogen dissolved in niobium shifts junction I_c by up to about 10% [D][953]; the smallest 1KP junctions scatter by 5.17% at 4.2 K, the large ones by under 1% [D][571].

At the qubit the process decides how much dissipation arrives. Co-fabricated, the 2019 driver coupled 1.6(2) × 10⁻³ quasiparticles to the transmon per phase slip and held gates near 95% [D][566]; on a separate die across indium bumps the coupling fell 43-fold to 3.7(5) × 10⁻⁵, leaving photon-mediated poisoning through millimetre-wave antenna modes [D][249]. A millikelvin-optimised low-J_c process is projected to cut quasiparticle generation about 100-fold, since dissipation per phase slip scales with I_c [S][566].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: D-Wave's multilayer annealer stack with 4,608 on-chip SFQ flux DACs for 512 qubits on 56 lines (2014) [D][430]; for gate-model control, a NIST-made SFQ die on a two-transmon module, 1.2(1)% error per Clifford on the benchmarked qubit [D][249], and SEEQC's five-qubit module, X/2 fidelities of 99.69–99.75% across the five qubits, four of them driven through a 1:4 demultiplexer [D][304]. Typical at scale: no gate-model product uses an SFQ control die.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2010-04 | SFQ demultiplexer and 64 flux DACs for eight qubits, in the qubits' four-Nb-layer process | D-Wave | [D][957] |
| 2014-01 | Six superconducting metal layers, one 250 A/cm² trilayer; 4,608 DACs on 512 qubits | D-Wave | [D][430] |
| 2015-09 | SFQ5ee: eight Nb wiring layers at 350 nm, 10 kA/cm², 200 mm | MIT LL | [D][953] |
| 2017-06 | AQFP in a process with two active layers around one ground plane | AIST / Yokohama National University | [D][954] |
| 2019-01 | SFQ driver co-fabricated with a transmon: gates near 95% | Wisconsin / Syracuse | [D][566] |
| 2023-07 | Separate NIST-made SFQ die on two transmons: 1.2(1)% per Clifford | Wisconsin / Syracuse / NIST | [D][249] |
| 2025-11 | 1KP, 1 kA/cm²: RSFQ and AQFP cells at 4.2 K for qubit interfaces | AIST / Yokohama National University | [D][571] |
| 2026-03 | Five transmons driven by SFQ logic at millikelvin temperature in a flip-chip MCM; carrier chip in SEEQC's 1 kA/cm² Nb process; X/2 99.69–99.75%, four qubits through a 1:4 demultiplexer | SEEQC | [D][304] |
| 2026-10 | SIMIT-Nb08: two junction layers at 6.15 / 6.26 kA/cm²; divider above 100 GHz | SIMIT | [D][955] |

Dominant error term: in gate-model modules, quasiparticle poisoning from the SFQ die, 0.96(2)% incoherent error per Clifford in 2023 [D][249]; in the process, junction critical-current spread [D][953].

## Manufacturing, materials & supply chain

MIT LL's tool set is a 248 nm-generation CMOS line: sputter cluster, 150 °C PECVD oxide, stepper, plasma etch and CMP on 200 mm silicon [D][953]. The dies that drove qubits came from smaller lines, three-inch wafers at NIST Boulder [D][249], an i-line process at Wisconsin [D][566] and SEEQC's foundry [D][304]. AIST's 1KP is a four-Nb-layer stack made in its Qufab facility, with Ti/Pd/Ti resistors because they stay resistive at 10 mK, a choice first made for AIST's quantum-annealing devices [D][571]. imec swaps niobium for NbTiN to scale on 300 mm [C][956]; its 2023 preprint proposes 16 NbTiN layers for 400 million junctions per cm², with development then at two metal layers [S][959].

Operators: MIT LL, whose SFQ5ee serves outside designers [P][897] and whose separate SQUILL foundry makes qubit circuits for more than 30 groups [C][570]; AIST; SIMIT; SEEQC; NIST. D-Wave's 10-K describes a "multilayer integrated circuit process" [G:DWAVE-FAB-10K], run on a line SkyWater Technology Foundry operates under a Semiconductor Line Operation Agreement of Dec 2012, whose 2025 amendment sets wafer lot sizes and per-lot CMP changeovers but names no materials [G][960]; SkyWater has belonged to IonQ since Jul 2026 [G:IONQ-SKYWATER-2026]. Yield: all 64 DACs of D-Wave's 2010 cell worked, with 1.2% coupling spread over 121 identical DACs on a 16-cell chip, but couplings missed design by up to 30% for want of accurate 3D inductance modelling [D][957]. The 2024 BIS rule created ECCNs for cryogenic electronics, coolers and probers [G:BIS-QUANTUM-ECCN-2024-09]. Single points of failure: a handful of planarised multilayer lines, junction-barrier know-how and cryogenic test.

## Control, readout & I/O burden

The process fixes the line count: six address and two power lines for D-Wave's 64 DACs (2010) [D][957], 56 lines for 4,608 DACs by XYZ addressing (2014) [D][430], 2√N + 2 lines to read N qubits [D][608]. The 2023 gate-model MCM still needed a flux-bias line, an SFQ bias line and a trigger per qubit [D][249]. On a 4 K budget of about 1 W (QECOOL) to a few watts (DigiQ), DigiQ's leanest design reaches more than 42,000 qubits at 10 W [S][958], a QECOOL decoder unit of 3,177 junctions would draw 2.78 µW at 2 GHz in ERSFQ [S][745] and a NISQ+ module 13.08 µW at a 163 ps cycle [S][744]. None was fabricated.

## Role in the stack

Architectures: the transmon lattice (`sc`), slot 10, beside `fab_sc` and `fab_cmos`, and the flux-qubit annealer (`anneal`), slot 10, beside `fab_sc`. It makes the SFQ control die of `ct_sfq` (the qubit die is `fab_sc`, the bump-bonded pair `ic_multidie`) and would make an SFQ cryogenic decoder (`dec_cryo`). Its alternative for the same cold logic is `fab_cmos`, serving `ct_cryocmos`; its complement is `fab_sc`. The annealer (`anneal`) is made in this family: D-Wave's `fluxq`, `ct_fluxdac` and `ro_fluxro` share one multilayer stack, four Nb layers in 2010 and six superconducting metal layers in 2014 [D][957], [430], and imec's authors list D-Wave's 2010 process among the state-of-the-art niobium processes for digital circuits [P][959]. D-Wave's 2026 fluxonium module joins a minimal-stack qubit chip to a multilayer control chip across a ~7 µm gap, the `fab_sc` + `fab_scd` split in one assembly [C][316]. Conflict: an SFQ stack on the qubit die poisons the qubit; a separate die mitigates it. Contribution to the derived clock: none.

## Evidence — how the numbers were measured

MIT LL's layers, dimensions and J_c are process targets, process parameters tracked on about 3,300 room-temperature test structures per site and J_c on 216 junctions per wafer [D][953]; AIST measured 1,248 A/cm² on 1,000-junction arrays at 4.2 K, about 20% above target [D][571]. SIMIT-Nb08's figures are from the publisher's abstract; the full text was not reached, so its eight layers are not broken down. SFQ gate errors are randomised-benchmarking averages, the incoherent share comes from purity benchmarking and quasiparticle numbers from T₁ recovery fits [D][566], [249]. SEEQC's fidelities are randomised-benchmarking figures for each qubit measured on its own, not simultaneously, and its carrier chip's process is named only in the paper's supplementary section — 1 kA/cm² niobium junctions, a high-kinetic-inductance layer, niobium wiring and ground planes [D][304]; the layer count is not given. The D-Wave–SkyWater tie rests on the agreement and the 10-K; neither names niobium. Not published in what was read: a yield for any qubit-control SFQ die, the layer count of SEEQC's process, a 10 mK measurement of AIST's 1KP circuits.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| MIT Lincoln Laboratory | foundry / research | US | SFQ4ee and SFQ5ee nodes; separate SQUILL qubit foundry | [D][953][C][570] |
| AIST / Yokohama National University | foundry / research | JP | 10 kA/cm² process, low-J_c variants for qubit interfaces; AQFP | [D][571], [954] |
| SIMIT | foundry / research | CN | Nb03, Nb04, Nb08; two junction layers | [D][955] |
| SEEQC | developer / foundry | US | Commercial multilayer foundry; five-qubit SFQ module made in its 1 kA/cm² Nb process | [C][572][D][304] |
| NIST Boulder; Wisconsin–Madison; Syracuse | research | US | SFQ die and qubit control, 2019 and 2023 | [D][566], [249] |
| D-Wave (line run by SkyWater) | developer | CA / US | Annealer QPUs with on-chip SFQ flux DACs | [D][430][G][960] |
| imec | research | BE | 300 mm NbTiN building blocks | [C][956] |

**Money.** IARPA sponsored SFQ4ee and SFQ5ee for its Cryogenic Computing Complexity programme [D][953] and partly funded the 2023 SFQ-driver fabrication [D][249]. Hypres put more than $100 M into the foundry and IP that passed to SEEQC [G:SEEQC-FUNDING], whose Series A raised $22.4 M led by EQT Ventures [C][572]. No figure is published for AIST's, SIMIT's or imec's lines.

**Market & supply chain.** No merchant market for qubit-control SFQ dies exists: MIT LL and AIST run research lines, SEEQC a commercial multilayer foundry, SkyWater the line it operates for D-Wave; imec's 300 mm route names no quantum customer.

**IP & standards.** No patent search was made for this record. Cell libraries are the working standards, AIST's RSFQ and AQFP libraries among them [D][571].

**Roadmaps & track record.** MIT LL planned future nodes with 0.35 µm, then 0.25 µm, minimum spacing and resistor width (2015) [R][953]; AIST's next step is testing 1KP circuits at 10 mK [R][571]; SEEQC's roadmap puts digital flux control and readout on the die [R][53]. Track record: D-Wave's on-chip DAC count grew 72-fold from 2010 to 2014.

**Strategic reading.** The process family sits beside, not inside, gate-model quantum computing: the leaders' qubit lines are minimal stacks (`fab_sc`) and the larger cold-control demonstrations are cryo-CMOS (`ct_cryocmos`). Its hold is the annealer, the processor class whose qubits and control share a multilayer stack, and the low-J_c variants (SEEQC, AIST, NIST) built for millikelvin control. If SFQ control scales, the scarce asset is a qualified low-J_c multilayer node with a qubit-compatible bump process.

## Outlook & open questions

Confirm within 12–24 months if an SFQ control die from a multilayer node (SFQ5ee-class, AIST's 1KP, SIMIT's or SEEQC's) drives more than twenty qubits or a two-qubit gate, or if AIST's 1KP publishes circuits measured at 10 mK. Demote if gate-model SFQ control stays at five qubits or fewer by end-2028 while cryo-CMOS takes the cold-control slot. Best case by 2029: a low-J_c node supplying control and decoder dies to a thousand-qubit module; worst case: the family survives in quantum computing only inside D-Wave's annealers.

Open questions: (1) how many layers does SEEQC's 1 kA/cm² process stack, and with what junction spread? (2) do 1 kA/cm² junctions hold I_c spreads near 1% at 10 mK? (3) how many junction layers does D-Wave's current stack have, and is it still made at SkyWater under IonQ? (4) does 300 mm NbTiN logic meet a qubit's quasiparticle budget across a bump bond?

## References

[53] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [C]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [arXiv:2503.09879](https://arxiv.org/abs/2503.09879). [D]
[316] D-Wave Quantum Inc., “Digital control of a high-coherence fluxonium qubit,” D-Wave Quantum Inc., Jan. 2026. [Online]. Available: https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf [C]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[566] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[570] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[571] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[572] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[608] A. J. Berkley *et al.*, “A scalable readout system for a superconducting adiabatic quantum optimization system,” *Supercond. Sci. Technol.*, vol. 23, Art. no. 105014, 2010. [arXiv:0905.0891](https://arxiv.org/abs/0905.0891). [D]
[744] A. Holmes *et al.*, “NISQ+: Boosting quantum computing power by approximating quantum error correction,” [arXiv:2004.04794](https://arxiv.org/abs/2004.04794), Apr. 2020. [S]
[745] Y. Ueno, M. Kondo, M. Tanaka, Y. Suzuki, and Y. Tabuchi, “QECOOL: On-Line Quantum Error Correction with a Superconducting Decoder for Surface Code,” arXiv, Nov. 8, 2021. [Online]. Available: https://arxiv.org/abs/2103.14209 [S]
[897] P. Papanikolaou, A. Vanasse, H. Jin, G. Tzimpragos, and J. Volk, “Duplication-aware retiming and cell interface redesign for superconductor circuit minimization,” [arXiv:2610.02333](https://arxiv.org/abs/2610.02333), Oct. 2026. [D]
[953] S. K. Tolpygo *et al.*, “Advanced Fabrication Processes for Superconducting Very Large Scale Integrated Circuits,” *IEEE Trans. Appl. Supercond.*, 2016, doi: [10.1109/TASC.2016.2519388](https://doi.org/10.1109/TASC.2016.2519388). [arXiv:1509.05081](https://arxiv.org/abs/1509.05081). [D]
[954] T. Ando *et al.*, “Three-dimensional adiabatic quantum-flux-parametron fabricated using a double-active-layered niobium process,” *Supercond. Sci. Technol.*, vol. 30, no. 7, Art. no. 075003, Jun. 2017, doi: [10.1088/1361-6668/aa6ef4](https://doi.org/10.1088/1361-6668/aa6ef4). [D]
[955] M. Chen *et al.*, “A double-active-layer Nb-based fabrication process for superconducting digital integrated circuits,” *Supercond. Sci. Technol.*, vol. 39, no. 10, Art. no. 105024, Oct. 2026, doi: [10.1088/1361-6668/aeaeb2](https://doi.org/10.1088/1361-6668/aeaeb2). [D]
[956] imec, “Imec demonstrates core building blocks of a scalable, CMOS-fab compatible superconducting digital technology,” Dec. 10, 2024. [Online]. Available: https://www.imec-int.com/en/press/imec-demonstrates-core-building-blocks-scalable-cmos-fab-compatible-superconducting-digital [C]
[957] M. W. Johnson *et al.*, “A scalable control system for a superconducting adiabatic quantum optimization processor,” *Supercond. Sci. Technol.*, vol. 23, no. 6, Art. no. 065004, Apr. 2010, doi: [10.1088/0953-2048/23/6/065004](https://doi.org/10.1088/0953-2048/23/6/065004). [arXiv:0907.3757](https://arxiv.org/abs/0907.3757). [D]
[958] M. R. Jokar *et al.*, “DigiQ: A Scalable Digital Controller for Quantum Computers Using SFQ Logic,” arXiv, Apr. 2022. [Online]. Available: https://arxiv.org/abs/2202.01407 [S]
[959] A. Herr *et al.*, “Scaling NbTiN-based ac-powered Josephson digital to 400M devices/cm²,” [arXiv:2303.16792](https://arxiv.org/abs/2303.16792), Mar. 2023. [P]
[960] SkyWater Technology Foundry, Inc.; D-Wave Systems Inc., “Fifteenth Amendment to the Semiconductor Line Operation Agreement (Exhibit 10.23 to D-Wave Quantum Inc. Form 10-K for FY2025; agreement dated 2012-12-23, amendment effective 2025-01-14),” SEC EDGAR, Feb. 26, 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1907982/000190798226000026/exhibit1023-amendment15tod.htm [G]

