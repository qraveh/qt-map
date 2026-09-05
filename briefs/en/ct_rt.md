---
id: ct_rt
name: Room-temperature electronics + per-qubit coax/flex
layer: "5 Control"
tier: 2
status: demonstrated
since: 2007
one_line: One coherent line per drive, flux and readout port runs from room-temperature racks through attenuated coax or flex ribbon into the mixing chamber.
verdict: Line count and mixing-chamber heat, not gate physics, cap qubits per fridge; falsifiable if one fridge runs >2,000 qubits on RT lines before cryo-CMOS or SFQ ships at comparable scale.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The incumbent control architecture for essentially every gate-model superconducting qubit: microwave drive, flux bias and readout tones synthesised at room temperature, carried down the dilution refrigerator on coax or flex ribbon, attenuated at each stage, reaching the chip at 10–20 mK. Every control degree of freedom is a conductor crossing a 300 K → 10 mK gradient — a thermal and mechanical problem, not a quantum one. In use since the first transmon setups (2007). Coordinates: e = microwave control placed entirely at room temperature, no cryogenic amplification or demultiplexing; f = coherent error as the code sees it — crosstalk, phase noise, amplitude drift.

## Physics & limits
The binding constraint is the cooling budget, not coherence. Each line carries a passive conduction load plus an active load from the ~60 dB of attenuation that brings 300 K Johnson noise down to the 10 mK photon floor, most of it dumped at 4 K and the still. Cooling power per stage is fixed — a Bluefors XLD400 gives roughly 1 W at 4 K, microwatts at the mixing chamber — so lines scale O(N) against a constant. Krinner et al.'s measured budget supports 50 qubits at 14 mK in that fridge, about 150 at most [D][2]; every gain since is thinner cable and denser packing, not new physics. Failure is coherent — crosstalk and phase drift appear as control error, so these machines degrade by needing recalibration rather than by decohering. What moves the floor: multiplexing qubits per conductor, or moving synthesis into the fridge.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2019 | 50 qubits per XLD400 measured; ~150 thermal upper bound | ETH Zürich | [D][2] |
| 2023-12 | 1,121 qubits on one fridge (Condor), largest ever wired this way | IBM | [C][14] |
| 2025-11-10 | 8 channels per flex, +50% per port, 1,536 lines per XLDsl | Delft Circuits | [C][3] |
| 2026-06-16 | KIDE specified at >4,000 RF lines, >1,000 qubits | Bluefors | [C][1] |

Wiring sets the N at which errors are worth correcting, not the floor: the dominant term is still two-qubit infidelity — Willow, 105 qubits at 99.88% mean 2Q, 1.1 µs cycle [D][16].

## Manufacturing, materials & supply chain
Yield here is mechanical (connectors per port, flex delamination, thermal anchoring) and thermal, not lithographic; racks are near-COTS. Cryogenic wiring is the thin layer — Delft Circuits is the leading independent flex supplier and ships inside Bluefors systems [C][3]. Refrigerators concentrate the risk: Bluefors absorbed Cryomech's pulse tubes and helium plants in 2023, taking the stage beneath the dilution unit in-house at combined revenue above EUR 160 M [C][12]; Oxford Instruments is the only comparable merchant alternative, ULVAC a Japanese third source since 2025 [C][15]. Export control cuts asymmetrically: refrigerators past the BIS threshold (≥600 µW at 0.1 K, 48 h) fall under ECCN 3A904, and 3A901.a controls CMOS designed to run at ≤4.5 K — catching the cryo-CMOS alternative — while RT racks are uncontrolled [G][8].

## Control, readout & I/O burden
Two to four lines per qubit: drive, flux, and readout feedlines multiplexing 5–10 qubits each. At 10³ the architecture works and fills most of a large fridge; KIDE's >4,000 lines is specified for >1,000 qubits, about four each [C][1]. At 10⁴ the flex roadmap (40,000+ lines by 2029) is a projection with no interim demonstration [R][3], and multiplexing depth rather than cable count becomes the limit. At 10⁶ no RT path exists; every roadmap past ~10⁴ assumes in-fridge control or multi-fridge partitioning. The RT round trip also adds cable delay plus rack processing at µs scale [C][4] against Willow's 1.1 µs cycle [D][16].

## Role in the stack
Serves the transmon, bosonic cat/GKP and dual-rail erasure paths — the whole superconducting tree — and requires nothing upstream, its commercial strength. Its substitutes (4 K cryo-CMOS, millikelvin SFQ, on-chip flux DACs) each cost a fresh cryogenic qualification burden, and none has displaced it at scale: SEEQC's millikelvin SFQ module reaches 1Q fidelity above 99% and up to 99.9% on five qubits [D][6]; HRL's 4 K controller runs 18 silicon spin qubits at Λ₅/₃ = 4.7 [D][7]; IBM reports cryo-CMOS flux ASICs at parity with RT electronics on a 156-qubit Heron R2, but as conference abstracts only [C][13]. RT wiring adds no gate or readout time, so the derived round stays 0.65 µs, inside the measured 1.1 µs QEC cycle [D][16]. Neighbouring empty slot: a multiplexed cryogenic control layer proven at array scale.

## Verification (QCVV)
Every line count above 1,536 is product literature, not a wired system: Bluefors' >4,000 and Delft Circuits' 40,000-by-2029 have no named installation, and neither publishes crosstalk or phase-stability data at high channel count. No independent measurement of aggregate crosstalk above ~1,000 simultaneous lines exists as of 4 Sep 2026 — the gap that matters, since crosstalk is how this architecture fails.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Bluefors | supplier | Finland | Refrigerators with integrated looms; KIDE at >4,000 lines | [C][1] |
| Delft Circuits | supplier | Netherlands | Cri/oFlex ribbon, 8 channels per flex, inside Bluefors XLDsl | [C][3] |
| Quantum Machines | supplier | Israel | OPX control racks and controller software | [C][5] |
| Zurich Instruments | supplier | Switzerland | ZQCS racks on Fujitsu/RIKEN's 256-qubit system | [C][4] |
| Qblox | supplier | Netherlands | Modular control stacks, lower price point | [C][10] |
| IBM | developer | USA | Condor, 1,121 qubits on one fridge; cryo-CMOS challenger | [C][14] |
| SEEQC | developer | USA | Millikelvin SFQ control, the in-fridge substitute | [D][6] |

**Money.**
2023-03-28 · Bluefors · M&A, Cryomech · undisclosed, combined revenue > EUR 160 M · closed [C][12]
2024-06-20 · Qblox · Series A · USD 26 M · Quantonation, Invest-NL Deep Tech · closed [C][10]
2025-02-25 · Quantum Machines · Series C · USD 170 M · PSG Equity lead · USD 280 M cumulative · closed [C][5]
2025-12-03 · Delft Circuits · Series A extension · EUR 8 M · DeepTech XL, HTGF, QuVest · EUR 15 M cumulative · closed [P][9]
2026-06-17 · Quantum Machines · M&A, PCB Engineering (Hungary) · undisclosed · closed [C][5]

**Market & supply chain.** Racks are competitive and commoditising: five vendors qualified for NVQLink [C][11], Quantum Machines best capitalised at USD 280 M cumulative [C][5], Qblox an order of magnitude smaller [C][10]. Fridges and their wiring are concentrated, and Delft Circuits at EUR 15 M cumulative [P][9] is the one significant independent flex supplier — a single point of failure. Pays for G2, G3, G7; not G4.

**IP & standards.** No dated patent-family count for cryogenic RF cabling or RT control was found in a named database — no dated fact found. No formal standard; the closest is NVQLink, which since 2025-10-28 defines a common GPU-side interface across five control vendors [C][11] while each pulse stack stays proprietary.

**Roadmaps & track record.** Delft Circuits (2025-11-10, for 2029): 40,000+ lines per fridge, no interim milestone [R][3]. Bluefors (2026-06-16, undated): KIDE at >4,000 lines, product page only [C][1]. Zurich Instruments (2026-03-09, undated): "several thousand qubits" [C][4]. Both cabling vendors have shipped every density step they announced; 2029 is nonetheless a straight-line projection.

**Strategic reading.** If RT wiring reaches 10⁴ qubits, the rack vendors and Bluefors keep the control budget and cryo-CMOS/SFQ stay research programmes; SEEQC and the cryogenic-ASIC teams lose. If density stalls near 4,000–5,000 lines, bargaining power moves inside the fridge, where no RT vendor owns IP — and the strongest cryo-CMOS results sit with IBM and HRL, now one company. Export control favours the incumbent [G][8].

*Open niche:* the plug-in is not the racks, which are crowded and COTS-adjacent, but independent characterisation of what no vendor publishes — aggregate crosstalk, phase stability and measured heat budget at 10³-plus simultaneous lines, the go/no-go input for every cryo-CMOS and SFQ decision.

## Outlook & open questions
Confirm by end-2027 if one fridge runs >2,000 qubits on RT lines with published fidelity at that density; demote after another year of line-count specifications without a wired system. Best case by 2029: flex density plus deeper multiplexing reaches 10⁴ qubits, stack unchanged. Worst case: density plateaus near 4,000–5,000 lines while roadmaps beyond assume undelivered cryo-CMOS or SFQ. Open questions: does crosstalk grow faster than linearly past ~1,000 lines; do flex density and multiplexing compound or hit independent walls; will any vendor commit to in-fridge control before RT wiring visibly fails; does multi-fridge partitioning make the per-fridge ceiling irrelevant.

## Sources
[1] Bluefors, KIDE cryogenic platform product page (revised 2026-06-16) — https://bluefors.com/products/kide-cryogenic-platform/ [C]
[2] Krinner, Storz, Kurpiers, Magnard, Heinsoo, Keller, Luetolf, Eichler, Wallraff, "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems", EPJ Quantum Technology 6, 2 (2019); arXiv:1806.07862 — https://link.springer.com/article/10.1140/epjqt/s40507-019-0072-0 [D]
[3] "Delft Circuits, Bluefors: the engine-room driving joined-up quantum innovation", Physics World, 2025-11-10 — https://physicsworld.com/a/delft-circuits-bluefors-the-engine-room-driving-joined-up-quantum-innovation/ [C] [G:DELFT-BLUEFORS-CRIOFLEX-2025-11]
[4] Zurich Instruments ZQCS platform launch, QuantumWire, 2026-03-09 — http://quantumwire.com/article/17731132975802.html [C] [G:ZI-ZQCS-2026-03]
[5] Quantum Machines, "Quantum Machines raises $170 million in Series C funding", 2025-02-25 — https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C] [G:QM-SERIESC-2025-02]
[6] Jordan, Bernhardt, Rahamim, Kirichenko et al. (SEEQC), "A quantum computer controlled by superconducting digital electronics at millikelvin temperature", Nature Electronics, 2026-03-10 — https://www.nature.com/articles/s41928-026-01576-6 [D] [G:SEEQC-MK-SFQ-2026-03]
[7] HRL Laboratories, 18-qubit SiGe QPU with 4 K cryo-CMOS controller, Nature 2026-07-29; arXiv:2604.16216 — https://arxiv.org/abs/2604.16216 [D] [G:HRL-CRYOCMOS-4K-2026]
[8] US BIS interim final rule, "Commerce Control List additions and revisions: implementation of controls on advanced technologies", 2024-09-06 (ECCN 3A901.a, 3A904, 3B904, 4A906) — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G] [G:BIS-3A901A-CRYOCMOS]
[9] "Delft Circuits names Martin Danoesastro CEO and extends funding round", The Quantum Insider, 2025-12-03 — https://thequantuminsider.com/2025/12/03/delft-circuits-new-ceo-financing/ [P]
[10] Qblox, "Qblox secures Series A funding to accelerate quantum control stack development", 2024-06-20 — https://qblox.com/newsroom/qblox-secures-series-a-funding-quantum-control-stack-development [C]
[11] NVIDIA, "NVIDIA NVQLink", 2025-10-28 — https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing [C] [G:NVQLINK-LAUNCH-2025-10-28]
[12] Bluefors, "Bluefors closes the acquisition of Cryomech", 2023-03-28 — https://bluefors.com/press-releases/bluefors-closes-the-acquisition-of-cryomech/ [C] [G:BLUEFORS-CRYOMECH-2023]
[13] IBM Research, "A cryo-CMOS control system for large-scale superconducting qubit quantum computing, part 2", APS Global Physics Summit abstract, 2026-03-16 — https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C] [G:IBM-CRYOCMOS-FLUX-2026-03]
[14] IBM, Quantum roadmap to 2033 (Condor, 1,121 qubits, 2023-12) — https://www.ibm.com/quantum/blog/quantum-roadmap-2033 [C]
[15] ULVAC, next-generation dilution refrigerator developed with IBM input, 2025-03-21 — https://www.nasdaq.com/press-release/ulvac-developing-next-generation-dilution-refrigerator-quantum-computing-2026-2025-03 [C] [G:ULVAC-IBM-REFRIG-2025]
[16] Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920 (2024-12-09) — https://www.nature.com/articles/s41586-024-08449-y [D] [G:WILLOW-QEC-2024-12]

## Open verification items
No vendor publishes per-line or per-loom cost; no unit economics for cryogenic wiring are quotable. No measured heat budget or crosstalk data exists for a >1,000-line flex loom — Bluefors' >4,000-line and Delft Circuits' 40,000-by-2029 figures are unverified at system level. Delft Circuits' and Zurich Instruments' revenue and customer counts are undisclosed. IBM's cryo-CMOS flux-bias parity result exists only as APS conference abstracts, with no preprint or paper as of 2026-09-04. No dated ECCN determination was found for RT control racks specifically; that they are uncontrolled is read from the absence of a matching entry in the 2024 rule, not from an explicit BIS statement.
