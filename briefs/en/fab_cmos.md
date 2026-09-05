---
id: fab_cmos
name: 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)
layer: 10 Manufacturing
tier: 1
status: demonstrated
since: 2022
one_line: Industrial 300 mm CMOS lines fabricating quantum-dot spin qubits, cryo-CMOS controllers and superconducting wiring; the only qubit manufacturing route with wafer-scale yield statistics.
verdict: Uniformity is proven (96% device yield, sub-nm CD); fidelity is not yet a foundry deliverable. Demote if no 300 mm device with >20 qubits and all-pairs 2Q ≥ 99.5% appears by end-2027.
updated: 2026-09-03
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage

This node is a manufacturing regime, not a qubit: 300 mm CMOS production lines making gate-defined quantum-dot arrays (Si/SiGe, Si-MOS, Ge), their cryo-CMOS ASICs, and superconducting qubit and wiring layers. A quantum dot is an accumulation-mode transistor at single-electron occupancy; at 45–100 nm pitch the foundry supplies uniformity, interface quality and isotopic control, not resolution, across tens of thousands of devices per wafer with cryogenic wafer-level test.

CEA-Leti opened the route in 2016 with a spin qubit in a 28 nm FD-SOI flow [D][13]. Intel and QuTech made the first all-optically patterned 300 mm qubits in March 2022 [D][3], fixing *since 2022*; Intel added EUV arrays and 1.6 K wafer statistics in 2024 [D][1][2]. imec produced 300 mm transmons in 2024 [D][4] and, with Diraq, unit cells above 99% in 2025 [D][6]. GlobalFoundries' 22FDX became the merchant option in 2025 [D][5], ST started 28Si FD-SOI lots in December 2025 [P][38], and US CHIPS letters of intent followed in May 2026 [G][18].

Coordinates (technology graph):
a, carrier affinity: fabricated, 1.0; the node is fabrication itself.
b, characteristic time: none; no gate time or entangling mode.
c, readout: none.
d, mobility and connectivity: none.
e, control modality: none.
f, error structure: coherent; device-to-device variability read as calibration error.
g, manufacturing: CMOS.

## Physics & limits

Mechanism. The fab fixes four inherited quantities: geometric uniformity, critical dimension within 0.5 nm at 45–100 nm pitch [D][1]; electrostatic disorder, a random threshold-voltage spread of 59 mV on Intel Si/SiGe [D][2]; isotopic purity, 800 ppm residual 29Si at Intel [D][1] and 400 ppm at imec [D][6]; and interface quality, which sets charge noise and, in Si/SiGe, the valley-splitting distribution.

Scales. T2*/T2echo reach 5/205 µs on 28Si Si/SiGe against 0.6/98 µs on natural silicon [D][2]; Hahn-echo T2 reaches 1.31 ms on imec SiMOS [D][7].

Floor. For spins it is material: residual 29Si, interface charge noise and the Si/SiGe valley-splitting tail that turns some dots into leakage sinks. For transmons it is junction targeting: 8% wafer-level resistance spread gives 5–7% frequency spread [D][4], an order above collision-free lattice needs; alternating-bias annealing (97.4% targeting [D][14]) is post-fab, not a foundry property.

As the code sees it: coherent, calibratable error (HRL attributes about 80% of CNOT error on its 54-dot array to control and calibration [D][10]) plus leakage and slow drift; nothing is erasure-convertible; wafer gradients [D][4] become spatially correlated error. Moving the floor needs 10-ppm-class 28Si, engineered valley splitting (simulation only [S][39]), Ge/SiGe holes or in-flow junction trimming.

## Engineering state of the art

Best demonstrated: four Diraq/imec unit cells, every operation above 99% (1Q 99.97%, CZ 99.04–99.56%, SPAM 99.95% at 100 µs), gate-set tomography, September 2025 [D][6][G:IMEC-300MM-2025]. Typical at scale: Intel's 232 twelve-dot devices on one wafer gave 99.8% dot and 96% full-device yield, May 2024 [D][2]; unmodified 22FDX gave 28–40% "good dot" yield over 1,024 dots, January 2025 [D][5]; imec's eight-qubit array validated one pair of four, July 2026 [D][7].

| year | figure | who | tag+key |
|---|---|---|---|
| 2016 | spin qubit in a 300 mm 28 nm FD-SOI flow | CEA-Leti | [D][13] |
| 2022-03 | >10,000 dot arrays per wafer; 1Q 99.0–99.1% | Intel/QuTech | [D][3] |
| 2024-09 | 300 mm transmons: median T1 75 µs, 98.25% yield | imec/KU Leuven | [D][4] |
| 2024-12 | >24,000 devices per wafer, CD < 0.5 nm (EUV) | Intel | [D][1] |
| 2025-01 | 1,024 dots on 22FDX, 1:1,024 cryo-CMOS mux, < 10 min | Quantum Motion/GF | [D][5] |
| 2025-09 | CZ 99.04–99.56% on 300 mm SiMOS, 4 of 4 devices > 99% | Diraq/imec | [D][6] |
| 2026-07 | 4 K CMOS controller (366 DACs, ≤ 3.5 W) runs d=5 repetition code, Λ = 4.7 | HRL | [D][10][G:HRL-2026] |

Dominant error term: the 2Q plateau at 99.0–99.6% is charge noise plus exchange calibration [D][6][10]; 100 µs readout for 99.9%-class SPAM [D][6] sets a 100–300 µs cycle; no 300 mm device above twelve qubits has published all-pairs 2Q; for transmons the limit is junction spread, not coherence [D][4].

## Manufacturing, materials & supply chain

Platforms. Intel D1: Si/SiGe wells, immersion and EUV lithography, cryo-prober screening [D][1][2]. imec: SiMOS with overlapping polysilicon gates below 100 nm pitch on 400 ppm 28Si [D][6], plus a transmon flow with dry-etched overlap junctions [D][4]. FD-SOI: GlobalFoundries 22FDX (Quantum Motion [D][5]; Equal1 [C][31]) and ST 28 nm at Crolles on Soitec 28Si substrates, first lots December 2025 [P][38]. HRL and SkyWater run 200 mm [D][10][C][26].

Yield. 96% device yield on a quantum-optimised flow [D][2] against 28–40% on a merchant flow [D][5] is this node's central number.

Cost and energy. No foundry publishes a quantum wafer price; Diraq's < $1 per qubit target [R][33] and vendors' rack-scale claims [C][29][30][32] are unaudited.

Supply chain. Lines: Intel (captive); imec, coordinator of the EU SPINS pilot line [G][22]; GlobalFoundries' Quantum Technology Solutions unit [C][23]; IBM Albany, becoming Anderon for superconducting wiring, TSVs and bumps [C][24]; SkyWater, 200 mm, IonQ-owned since 2026-07-31 [C][26]. Materials: enriched 28Si, historically Russian; Silex completed a plant for up to 20 kg per year in June 2026, commissioning late 2026, for SQC [C][34]. Equipment: cryogenic wafer probers from Bluefors/Afore (< 2 K, 300 mm, 768 DC, 48 RF lines) [C][35] and FormFactor [C][36]. Single points of failure: EUV dots only at Intel and imec; one 28Si plant; a prober duopoly.

Export control. BIS's rule of 2024-09-06 controls cryogenic CMOS ICs for ≤ 4.5 K (ECCN 3A901), cryogenic systems ≥ 600 µW at ≤ 0.1 K (3A904), cryogenic wafer probers (3B904) and quantum computers from 34 qubits (4A906), with License Exception IEC for allies [G][19][G:BIS-QUANTUM-2024]; EU and UK lists match.

## Control, readout & I/O burden

Multiplexing moves on-die or in-package: a 1:1,024 cryo-CMOS multiplexer on 13 lines [D][5]; imec's multiplexer routing transmon pulses below 15 mK with > 99.9% 1Q preserved [D][8]; a 32-cell 28 nm FD-SOI chip at 7 mK, ~20 nW/MHz per cell [D][9]; HRL's 4 K controller, 366 DACs at ≤ 3.5 W (~10 mW per channel), running a repetition code [D][10]; IBM's 4 K controller at 23 mW per qubit [D][11]. Crossbar sharing needs T = 6√g − 1 lines for a square array of g dots (23 for 16) [D][12].

Walls. 10³: per-qubit lines suffice; the burden is tune-up time. 10⁴: 10–23 mW per channel at 4 K means 100–230 W, beyond any cryostat's 4 K stage, forcing ≥ 10:1 multiplexing or millikelvin nW-class cells. 10⁶: only crossbar sharing (~6,000 lines [D][12]) plus millikelvin CMOS or SFQ closes; whether shared control keeps coherent error below threshold is open. Latency: spin cycles are readout-bound, 100 µs integration [D][6].

## Role in the stack

A layer-10 root: it requires nothing and provides the dot arrays and cryo-ASICs the spin path assumes. It replaces STM-lithography donor fabrication (11-qubit registers, serial, no foundry route [D][17]); for ion traps it is the alternative to MEMS trap fabs, the switching price being CMOS re-qualification, paid by Oxford Ionics (part of IonQ since 2025-09-17), whose 99.99% two-qubit fidelity on standard-fab chips is reported in an IonQ release [C][27][G:IONQ-OXIONICS-2025]. Off-diagonal reading: natural carriers (trapped ions) inheriting semiconductor manufacturing. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path; this node adds no term; the spin path's derived round is 8.5 µs, readout-set, against a measured 100–300 µs cycle [D][6]. Conveyor shuttling at 10 µm and 99.5% [D][16], shown on a Delft-made device, is what uniform 300 mm gates must reproduce. Neighbouring empty slots: no spin-module interconnect (300 mm photonics is the candidate, unproven at millikelvin) and no fabricated cryogenic decoder; a cryo-CMOS predecoder design claims 3,780× syndrome-bandwidth reduction below 0.56 mW [S][15].

## Verification (QCVV)

Yield numbers come from cryo-probers at 1.6–1.7 K (automated tune-up, turn-on/pinch-off and charge-sensing criteria [D][1][2]): transistor statistics. Fidelities come from few devices in dilution refrigerators: gate-set tomography (12,263 sequences) for the unit cells [D][6], randomised benchmarking on Tunnel Falls [D][1], T1/T2 wafer maps for transmons [D][4].

Not captured: (1) 1.6 K probing cannot see valley splitting, exchange or coherence, so device yield says nothing about qubit yield; (2) selection: 4 of 20 imec devices characterised [D][6], 6 of > 10,000 arrays cooled in 2022 [D][3]; (3) criteria: 28–40% and 96% define "working" differently [D][2][5]; (4) no simultaneous all-pairs 2Q on any 300 mm array [D][7]; (5) ageing: 3.7% junction drift in 146 days [D][4] is absent from fidelity claims.

Replication: imec's SiMOS numbers reproduce across four devices and two institutions [D][6]; Intel's are single-vendor. Flagged: Quantum Motion's "first full-stack silicon CMOS quantum computer" without published fidelities [C][29]; Equal1's commercial-process dots without qubit metrics [C][31].

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Intel | developer; captive supplier | US | Si/SiGe EUV arrays; cryo-prober wafer statistics; 12-qubit chip at Argonne | [D][1][2]; [G][21] |
| imec | research; supplier | BE | 300 mm SiMOS dots, transmons, millikelvin multiplexer; SPINS coordinator | [D][4][6][8]; [G][22] |
| GlobalFoundries | supplier (merchant foundry) | US | 22FDX dots and cryo-CMOS; Quantum Technology Solutions unit; $375 M LOI | [C][23][28]; [G][18] |
| IBM | developer; supplier | US | Anderon: 300 mm superconducting wafers, TSVs, bumps; $1 B LOI | [C][24][25]; [G][18] |
| Diraq | developer | AU | SiMOS unit cells at imec; QBI Stage B; CHIPS LOI up to $38 M | [D][6][7]; [G][18][20] |
| Quantum Motion | developer | UK | 22FDX 1,024-dot arrays; NQCC system; QBI Stage B | [D][5]; [C][29]; [G][20] |

**Money.**

| date | actor | event | amount | lead or programme | cumulative | status |
|---|---|---|---|---|---|---|
| 2025-11-06 | Diraq; Quantum Motion; SQC | grant | up to $15 M each | DARPA QBI Stage B | — | definitive [G][20][G:QBI-STAGEB-2025-11] |
| 2026-01-15 | Equal1 | round | $60 M | ISIF | > $85 M | closed [C][32][G:EQUAL1-60M-2026-01] |
| 2026-04-03 | imec + 25 partners | grant | €50 M | EU Chips JU SPINS pilot line | — | announced [G][22] |
| 2026-05-07 | Quantum Motion | Series C | $160 M | DCVC, Kembara | — | closed [C][30][G:QM-160M-2026-05] |
| 2026-05-21 | GlobalFoundries | CHIPS LOI | $375 M | US Commerce ($2.013 B over nine LOIs) | — | LOI, non-binding [G][18][C][23][G:CHIPS-LOI-2026-05] |
| 2026-05-21 | IBM (Anderon) | CHIPS LOI | $1 B + $1 B IBM cash | US Commerce | — | LOI, non-binding [G][18][C][24] |
| 2026-05-21 | Diraq | CHIPS LOI | up to $38 M | US Commerce | > $100 M raised [P][G:DIRAQ-FUNDING] | LOI, not awarded [G][18] |
| 2026-06-03 | Quobly | Series A | €115 M | Bpifrance, SEALSQ, STMicroelectronics | €134 M | closed [P][37][G:QUOBLY-115M-2026-06] |
| 2026-06 | Silex Systems | Q-Si plant completed | A$5.1 M + A$4.35 M | Defence Trailblazer; SQC | — | commissioning late 2026 [C][34] |
| 2026-07-23 | IBM | M&A: HRL Laboratories | undisclosed | — | — | announced, closing Q3 2026; potential plans for spin qubits at Anderon [C][25][G:IBM-HRL-2026-07] |
| 2026-07-31 | IonQ | M&A: SkyWater | $15.00 + 0.4883 IonQ shares per share (~$1.8 B) | — | — | closed [C][26][G:IONQ-SKYWATER-2026] |

**Market & supply chain.** Quantum is immaterial to foundry revenue. Concentration: two EUV-capable dot lines, one merchant FD-SOI option (ST entering), a prober duopoly, one 28Si plant. Unit economics: unpublished beyond Diraq's target [R][33]. Payers: G4 for 10⁶-qubit CMOS density; G7, as of 3 Sep 2026, for rack-scale spin systems; superconducting vendors buy Anderon/GF wiring for G2–G4; ion vendors buy standard-fab traps for G2, G3, G7.

**IP & standards.** Portfolios: Intel, HRL, Diraq/UNSW, Quantum Motion/UCL, Quobly (CEA/CNRS licences), Equal1; no litigation public; no dated family count from a named database found. SPINS promises quantum PDKs and multi-project-wafer access [G][22]; GF markets FDX cryogenic models [C][23]; no open cryogenic device-model standard exists.

**Roadmaps & track record.** Intel (promised 2022 · wafer-scale qubits · delivered 2024, Argonne 2026-01-06 [G][21][G:INTEL-2026]; no successor or roadmap as of 2026-09-03). Diraq (promised 2026-07-09 · "thousands" by 2029, restated 2026-08-27 as 150,000 physical · eight qubits shown [D][7][R][33][G:DIRAQ-FUNDING]). Quantum Motion (promised 2025-01 · NQCC system · delivered 2025-09-15, no published fidelity [C][28][29]). Quobly (promised 2025-12 · ST-lot metrics Q1 2026 [P][38] · none found as of 2026-09-03). GF, Anderon: no wafer dates promised [C][23][24]. Credibility: imec/Diraq (peer-reviewed, replicated) first; Intel manufactures without a product path; Quantum Motion, Quobly, Equal1 deliver systems without metrics; roadmap slides last.

**Strategic reading.** Success rewards foundries and suppliers (GF, imec, ST/Soitec, Bluefors) and spin vendors whose bill of materials shrinks to wafers plus racks; bespoke routes (STM lithography, university lift-off) and MEMS trap fabs lose. Supplier bargaining power is high (few lines, quantum revenue immaterial), but three or four substitutable lines and state money cap what foundries extract. Substitution threats: Ge/SiGe holes, photonic-interconnect fabs, SFQ against cryo-CMOS.

*Open niche:* A small QCVV/SFQ research company plugs in at the gap this brief keeps hitting: protocols mapping 1.6 K wafer statistics to millikelvin qubit performance, benchmarks for shared-control arrays where standard randomised benchmarking assumes individual addressability, and months-scale drift quantification. SPINS' multi-project-wafer channel is the entry point; imec's CMOS-compatible superconducting stack suits an SFQ-on-CMOS control test vehicle.

## Outlook & open questions

Milestones, 12–24 months: (1) a 300 mm device with > 20 qubits and published all-pairs 2Q ≥ 99.5% confirms; none by end-2027 demotes; (2) SPINS multi-project-wafer runs with a public quantum PDK; (3) GF's LOI made definitive, a named 22FDX quantum product; (4) a spin-qubit lot at Anderon after IBM–HRL closes; (5) Intel naming a Tunnel Falls successor or exiting.

2029 best case: two merchant 300 mm lines with quantum PDKs, 10³-dot arrays with on-die multiplexing, 2Q ≥ 99.5% typical, a below-threshold spin memory. Worst: merchant yields at tens of percent, 2Q at 99–99.6%, roadmaps cut again, GF's unit reduced to packaging for superconducting and photonic customers.

Open questions: can valley splitting and charge noise be made wafer-uniform, or must every array be post-selected? What is the qubit-fidelity yield of a 300 mm flow? Does shared control keep coherent error below threshold? Can in-flow junction targeting reach sub-percent? Watch the first fidelity-yield number, SPINS' first multi-project wafer, definitive CHIPS awards, Intel.

## Sources

1. H. C. George et al. · "12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line" · Nano Letters (arXiv:2410.16583, 2024-10-22) · 2024-12-21 · https://arxiv.org/abs/2410.16583
2. S. Neyens et al. · "Probing single electrons across 300-mm spin qubit wafers" · Nature 629, 80–85 · 2024-05-01 · https://www.nature.com/articles/s41586-024-07275-6
3. A. M. J. Zwerver et al. · "Qubits made by advanced semiconductor manufacturing" · Nature Electronics 5, 184–190 · 2022-03-29 · https://www.nature.com/articles/s41928-022-00727-9
4. J. Van Damme et al. · "Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers" · Nature 634, 74–79 · 2024-09-18 · https://www.nature.com/articles/s41586-024-07941-9
5. E. J. Thomas et al. · "Rapid cryogenic characterization of 1,024 integrated silicon quantum dot devices" · Nature Electronics 8, 75–83 · 2025-01-03 · https://www.nature.com/articles/s41928-024-01304-y
6. P. Steinacker et al. · "Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity" · Nature 646, 81–87 · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9
7. Nickl, Dumoulin Stuyck, Steinacker et al., Tanttu (Diraq/imec) · "Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device" · Nature Communications 17, 5878 · 2026-07-09 · https://www.nature.com/articles/s41467-026-74597-6
8. R. Acharya et al. · "Multiplexed superconducting qubit control at millikelvin temperatures with a low-power cryo-CMOS multiplexer" · Nature Electronics 6, 900–909 · 2023-09-25 · https://www.nature.com/articles/s41928-023-01033-8
9. S. K. Bartee et al. · "Spin-qubit control with a milli-kelvin CMOS chip" · Nature 643, 382–387 · 2025-06-25 · https://www.nature.com/articles/s41586-025-09157-x
10. HRL Quantum Team · "A digitally controlled silicon quantum processing unit" · arXiv:2604.16216; Nature (2026-07-29) · 2026-04-17 · https://arxiv.org/abs/2604.16216
11. D. J. Underwood et al. · "Using cryogenic CMOS control electronics to enable a two-qubit cross-resonance gate" · PRX Quantum 5, 010326 · 2024-02 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326
12. F. Borsoi et al. · "Shared control of a 16 semiconductor quantum dot crossbar array" · Nature Nanotechnology 19, 21–27 · 2024-01 · https://www.nature.com/articles/s41565-023-01491-3
13. R. Maurand et al. · "A CMOS silicon spin qubit" · Nature Communications 7, 13575 · 2016-11 · https://www.nature.com/articles/ncomms13575
14. D. P. Pappas, M. Field, C. J. Kopas et al. (Rigetti) · "Alternating-bias assisted annealing of amorphous oxide tunnel junctions" · Communications Materials 5, 150 · 2024-08-12 · https://www.nature.com/articles/s43246-024-00596-z
15. A. Knapen, G. Tao, J. Mack et al. · "Pinball: a cryogenic predecoder for surface code decoding under circuit-level noise" · arXiv:2512.09807 · 2025-12-10 · https://arxiv.org/abs/2512.09807
16. M. De Smet, Y. Matsumoto, A.-M. J. Zwerver et al. · "High-fidelity single-spin shuttling in silicon" · Nature Nanotechnology 20, 866–872 · 2025-06-09 · https://www.nature.com/articles/s41565-025-01920-5
17. H. Edlbauer, J. Wang, A. M. S.-E. Huq et al. · "An 11-qubit atom processor in silicon" · Nature 648, 569–575 · 2025-12-17 · https://www.nature.com/articles/s41586-025-09827-w
18. [G] NIST / US Department of Commerce · "Department of Commerce announces letters of intent to 9 companies for $2 billion" · nist.gov · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
19. [G] US Bureau of Industry and Security · interim final rule on quantum, semiconductor and additive-manufacturing items · Federal Register 89/173 · 2024-09-06 · https://www.govinfo.gov/content/pkg/FR-2024-09-06/html/2024-19633.htm
20. [G] DARPA · "Quantum Benchmarking Initiative — Stage B selection" · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
21. [G] Argonne National Laboratory · "Argonne launches silicon quantum processor collaboration with Intel" · anl.gov · 2026-01-06 · https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel
22. [G] imec (coordinator, EU Chips Joint Undertaking pilot line) · "Semiconductor-based quantum pilot line SPINS launched with EU support" · imec press release · 2026-04-03 · https://www.imec-int.com/en/press/semiconductor-based-quantum-pilot-line-spins-launched-eu-support
23. [C] GlobalFoundries · "GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" · GF investor newsroom · 2026-05-21 · https://investors.gf.com/news-releases/news-release-details/globalfoundries-launches-quantum-technology-solutions-scale-us
24. [C] IBM · "IBM and U.S. Department of Commerce announce America's first purpose-built quantum foundry" · IBM newsroom · 2026-05-21 · https://newsroom.ibm.com/ibm-and-u-s-department-of-commerce-announce-americas-first-purpose-built-quantum-foundry
25. [C] IBM · "IBM to acquire HRL Laboratories to power the future of quantum" · IBM newsroom · 2026-07-23 · https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum
26. [C] IonQ · "IonQ completes acquisition of SkyWater Technology" · IonQ newsroom · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
27. [C] IonQ · "IonQ achieves landmark result, setting new world record in quantum computing" (99.99% two-qubit fidelity on Oxford Ionics chips from standard semiconductor fabs) · IonQ newsroom · 2025-10 · https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing
28. [C] Quantum Motion · "Partnership with GlobalFoundries" (1,024-dot chip) · quantummotion.com · 2025-01-06 · https://quantummotion.com/partnership-with-globalfoundries/
29. [C] Quantum Motion · "Quantum Motion delivers the industry's first full-stack silicon CMOS quantum computer" · quantummotion.com · 2025-09-15 · https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/
30. [C] Quantum Motion · "Quantum Motion raises $160 million Series C to deliver quantum computing's transistor moment" · quantummotion.com · 2026-05-07 · https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/
31. [C] Equal1 · "Validation of a commercial CMOS process on GlobalFoundries 22FDX" · equal1.com · 2025-04-16 · https://www.equal1.com/post/commercial_cmos_process
32. [C] Equal1 / NovaUCD · "Equal1 announces $60 M funding round" · ucd.ie · 2026-01-15 · https://www.ucd.ie/innovation/news-and-events/2026/equal1-announces-funding-round/
33. [C] Diraq · "Diraq sets roadmap for utility-scale quantum computing with millions of qubits on a single silicon chip" · diraq.com · 2026-08-27 · https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip
34. [C] Silex Systems · "Silex ZS-Si production for quantum computing" (Q-Si product page) · silex.com.au · page as of 2026-09 · https://www.silex.com.au/silex-technology/silex-zs-si-production-for-quantum-computing/
35. [C] Bluefors · "Cryogenic wafer prober" (product page) · bluefors.com · page as of 2026-09 · https://bluefors.com/products/cryogenic-wafer-prober/
36. [C] FormFactor · "HPD IQ3000 4 K cryogenic probe station" (product page) · formfactor.com · page as of 2026-09 · https://www.formfactor.com/product/quantum-cryo/quantum-wafer-multi-chip-cryogenic/iq3000/
37. [P] HPCwire · "Quobly raises €115M Series A to industrialize silicon quantum computing" · HPCwire · 2026-06-03 · https://www.hpcwire.com/off-the-wire/quobly-raises-e115m-series-a-to-industrialize-silicon-quantum-computing/
38. [P] IT Brief Asia · "Quobly runs silicon-28 quantum wafers through ST fab" · IT Brief Asia · 2025-12-12 · https://itbrief.asia/story/quobly-runs-silicon-28-quantum-wafers-through-st-fab
39. M. P. Losert et al. · "Practical strategies for enhancing the valley splitting in Si/SiGe quantum wells" · Physical Review B 108, 125405 · 2023-09 · https://journals.aps.org/prb/abstract/10.1103/PhysRevB.108.125405

## Open verification items

- SPAM for the imec/Diraq unit cells: 99.95% at 100 µs [6] (v1 value, retained) against 99.9% recorded for imec's 300 mm line (2025).
- Shuttling fidelity [16]: v1 gave 99.54%; the abstract states "99.5% on average"; the abstract value is used.
- Silex funding (A$5.1 M Defence Trailblazer, A$4.35 M SQC): amounts undated on the Silex page [34]; the ledger row is dated by the June 2026 plant completion.
- [39] Losert et al.: bibliographic details are cited from the standard literature and not confirmed against the publisher's page.
- Dropped from v1 as unverified here: the "~1% Commerce equity stake" in GF's CHIPS LOI (v1 cited [18][23][24] jointly), IBM's 30× device-output claim for Anderon (trade-press proxy only), and Intel's 91% single-electron-sensing figure [2] versus 96% tune-up [1] (different device sets and criteria).
