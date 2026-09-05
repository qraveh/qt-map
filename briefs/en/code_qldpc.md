---
id: code_qldpc
name: Bivariate-bicycle qLDPC (gross) codes
layer: "7 Code"
tier: 1
status: emerging
since: 2025
one_line: Sparse high-rate stabiliser codes on a degree-6 torus that cut physical-per-logical overhead roughly tenfold against the surface code.
verdict: Real overhead win, proven only at distance 3–4 on 18–32 qubits; without a delivered long-range-coupled module by end-2027 it stays a paper advantage.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes.

## Identity & lineage

A bivariate bicycle (BB) code is a CSS stabiliser code whose two parity-check matrices are polynomials in a pair of commuting cyclic shifts, so the checks tile a torus: every check touches six qubits, every qubit sits in six checks. Four neighbours are near, two are long-range wraps — sparsity and high rate bought with non-planar connectivity. The lineage runs from MacKay's bicycle codes and Tillich–Zémor hypergraph products through Panteleev–Kalachev lifted products to Bravyi, Cross, Gambetta, Maslov, Rall and Yoder, Nature 627, 778 (2024-03-27), whose [[144,12,12]] "gross code" holds 12 logical in 288 physical qubits at a circuit-level threshold of 0.8%, against ≈3,000 physical for the same 12 logical in the surface code at p = 0.1% [D][1].

Coordinates (technology graph): carrier affinity 0.5 — a code layer, indifferent between natural and fabricated carriers but inheriting their errors. Characteristic time: none of its own; entangling neither deterministic nor heralded here. Readout: none of its own — it consumes fast non-destructive mid-circuit syndrome measurement from the carrier. Mobility: long-range, the defining requirement. Control modality: none, at no placement. Error structure as the code sees it: Pauli. Manufacturing: none.

## Physics & limits

The code sets no energy scale, only an accounting rate: k/n and syndrome depth. The gross code encodes one twelfth of its data qubits, and its depth-7 syndrome circuit costs seven two-qubit layers plus a measurement per round — the surface code's depth, on a graph the hardware does not have [D][1]. The floor is the threshold, 0.8% under circuit-level depolarising noise [D][1]; below it, suppression per distance step beats the surface code because the block carries more logical qubits per unit of syndrome information, not because any qubit is better.

Two structural penalties are real. Distance is not free: distance 12 in 288 qubits needs the long-range wraps, and deleting them collapses the family to something a heavy-hex lattice can host, rate advantage gone. Decoding is harder: the Tanner graph has short cycles, so minimum-weight matching does not apply and plain belief propagation does not converge; the practical choices are BP with ordered-statistics post-processing (accurate, too slow) or Relay-BP [S][5]. The worst failure mode is anything the code does not see as Pauli — leakage, ion or atom loss — a sparse code having fewer redundant checks to localise a hyper-edge. Erasure conversion and leakage removal move this floor further than better gates.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: 4 logical qubits in 18 trapped ions at break-even (IonQ, June 2026) [D][3]. Typical at scale: nothing — no BB code has run on more than 32 physical qubits, and none has hosted a logical two-qubit gate.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-03 | [[144,12,12]]: 288 physical for 12 logical, threshold 0.8%, ≈10× fewer qubits than surface code | IBM | [D][1] |
| 2025-05 | First BB code on hardware: [[18,4,4]] on 32 transmons, 8.91 ± 0.17% per logical qubit per cycle — above physical error | Zhejiang University | [D][4] |
| 2025-06 | Modular architecture: 288-qubit module + 90-qubit logical processing unit, 5,000 physical → 121 logical at p = 10⁻³ | IBM | [S][2] |
| 2025-10 | Gross-code decoding on FPGA: 24 ns belief-propagation iteration, under 1 µs mean per cycle at p < 3×10⁻³ | IBM | [S][5] |
| 2026-06 | First qLDPC break-even: 3.95 ± 0.68 s vs 3.3 ± 0.9 s physical (leakage post-selected), 9× better logical error than the transmon run | IonQ | [D][3] |

Dominant error term: on the ion run, post-selected leakage and loss; on the transmon run, two-qubit error over a depth-7 round on couplers up to 6.5 mm [D][3][4].

## Manufacturing, materials & supply chain

The code has no fab of its own, which is why it is a supply-chain question. On superconducting hardware it is unbuildable without multi-layer routing and long on-chip couplers: IBM's Loon, announced 2025-11-12 with six-way connections, longer c-couplers and low-loss routing layers, is the process vehicle, on 300 mm at Albany — no qubit count, coupler length or coupler fidelity published as of 3 Sep 2026 [C][8]. Zhejiang's Kunlun processor shows the alternative: 84 air-bridged overlapping couplers, links to 6.5 mm, on a conventional process — good enough at 32 qubits, not at break-even [D][4]. The single point of failure is a packaging and lithography capability held by two or three organisations: IBM/Albany, IQM's resonator hubs [C][14], the Chinese academic fabs. The ion route has no fab constraint — connectivity comes from the motional bus, which is why IonQ got there first [D][3]. Export-control exposure is indirect: the exposure sits in the hardware (US Export Administration Regulations ECCN 3A901; 3B904/3D901 for equipment and software), not the published mathematics.

## Control, readout & I/O burden

Each round needs one mid-circuit measurement with reset per check qubit — 144 for the gross code — giving 144 syndrome bits per cycle per module, ~144 Mbit/s at a 1 µs cycle, an order of magnitude above a distance-7 surface patch for twelve times the logical qubits. The binding constraint is decode latency, not bandwidth: the decoder must return inside the cycle or the backlog grows without bound, and BP-OSD cannot. IBM's FPGA Relay-BP shows it can be met in principle — 24 ns per iteration, under 1 µs mean per cycle — but it is a simulation-driven study, not a decode of live syndromes [S][5]. At 10³ qubits the burden is unremarkable; at 10⁴ (≈35 modules, ~500 logical) the aggregate rate is ~5 Gbit/s and the decoder must be co-located, making NVQLink-class fabric (3.84 µs round trip) or a cold-stage ASIC a prerequisite [P][16]. At 10⁶ nothing has been designed.

## Role in the stack

Paths: superconducting transmon (IBM, IQM, Zhejiang) and trapped ions with electronic gates and chip control (IonQ/Oxford Ionics). It requires millimetre-scale long-range on-chip couplers, ion shuttling, the ion-chain motional bus, or tweezer transport of atoms; it provides the syndrome stream Relay-BP-class decoders consume; it replaces the surface code; it conflicts with nearest-neighbour-only connectivity — heavy-hex is insufficient without c-couplers. Price of switching: ≈10× in qubits gained; planarity, matching decoders and the body of lattice-surgery technique lost, the BB replacement (adapters, logical processing units) existing only on paper [S][2]. Hub reading: one of the few code-layer nodes reaching superconducting, ion and photonic carriers at once, its value set by whichever delivers degree-6 connectivity first. Derived clock: it sets d₂ — seven gate layers — so the ion path's round is 1.52 ms, gate-set, against a measured ≈1–5 ms; the superconducting round is 0.65 µs derived against the 1.1 µs QEC cycle [D][15]. Neighbouring empty slot: a hardware logical CNOT between two BB blocks.

## Verification (QCVV)

Break-even here is a memory comparison: logical lifetime against the best physical qubit on the same device, over repeated syndrome rounds and a destructive final readout. IonQ's 3.95 ± 0.68 s versus 3.3 ± 0.9 s overlaps within one standard deviation, and is stated with leakage post-selection [D][3] — defensible for a memory claim, but it removes exactly the error class a sparse code handles worst, and the acceptance rate is not in the abstract. The protocol also misses what a code is for: no BB demonstration anywhere reports a logical two-qubit gate, so the overhead advantage is verified only for storage. Value conflict: the main report lists a Harvard/QuEra [[16,6,4]] run beside IonQ's; that is a high-rate block code, not a bivariate bicycle code, and no primary source was found — treat IonQ and Zhejiang as the only BB hardware results. IBM's July-2026 "70 logical qubits, 468 T gates" is an error-*detecting* spacetime code and does not belong here [D][20].

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| IBM | developer | US | Invented the gross code; Loon connectivity chip, Kookaburra module, Relay-BP decoder | [D][1][S][2][5] |
| IonQ (Oxford Ionics) | developer | US/UK | Only break-even qLDPC hardware result, 4 logical in 18 ions | [D][3] |
| Zhejiang University | research | CN | First BB code on hardware, 32-qubit Kunlun processor | [D][4] |
| Photonic Inc. | developer | CA | SHYPS qLDPC family, "up to 20x fewer physical qubits" | [C][9][P][10] |
| IQM | developer | FI | Resonator hubs; qLDPC demonstrators promised 2027-28 | [C][14] |
| DARPA | funder | US | QBI Stage B funds IBM, IonQ, Photonic Inc. and eight others | [G][12][G:QBI-STAGEB-2025-11] |

**Money.**
- 2025-11-06 · DARPA · QBI Stage B, eleven teams · up to $15 M each (USD) · announced [G][12][G:QBI-STAGEB-2025-11]
- 2026-05-12 · Photonic Inc. · final close · $200 M at $2 B (USD) · Microsoft among returning investors · $350 M total · closed [P][13][G:PHOTONIC-200M-2026-05]
- 2026-05-21 · IBM/Anderon · CHIPS letter of intent · $1 B + $1 B IBM cash (USD) · Dept of Commerce · LOI [G][18][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · five-year quantum commitment · >$10 B (USD) · announced [C][17][G:IBM-10B-2026-06]
- 2026-07-31 · IonQ · SkyWater, captive ion-trap fab · ~$1.8 B (USD) · closed [C][19][G:IONQ-SKYWATER-2026]

**Market & supply chain.** Nobody sells qLDPC. What sells is the connectivity that makes it usable — multi-layer superconducting interconnect (IBM at Albany, IQM's resonator hubs), ion-trap chips (IonQ owns SkyWater [C][19]) — and the decoding that makes it affordable (IBM in-house, NVIDIA's fabric [P][16]). Concentration risk is extreme: one organisation holds both the code and the only connectivity vehicle built for it. Unit economics are the case, ~24 physical per logical against ~1,000 for a distance-25 surface patch [D][1][15]. Only G3 and G4 pay for it.

**IP & standards.** No bivariate-bicycle patent family appears in the Justia index under that phrase as of 2026-09-03 — IBM published rather than fenced [P][21]. Enforceable IP sits one layer down: IBM US 12,517,856 (granted 2026-01-06) and US 12,587,192 on resonator chains with tunable inductive couplers (granted 2026-03-24) [G][22][G:LRCOUPLER-PATENTS]. Decoder IP is filed by others: KAIST US 12,346,774 (2025-07-01), Princeton US 11,941,489 (2024-03-26), US 2026/0172053 on qLDPC decoders (2026-06-18) [G][21]. Stim, PyMatching and BP-OSD carry the field; no standard exists.

**Roadmaps & track record.** IBM: Kookaburra, qLDPC memory plus logical processing unit (promised 2025-06-10 · for 2026 · not delivered as of 2026-09-03); Cockatoo modules (2025-06-10 · 2027 · pending); Starling, 200 logical and 10^8 gates (2025-06-10 · 2029 · pending) [R][6][7]. The 2022-05-10 roadmap had promised Kookaburra as a 1,386-qubit processor for 2025 [C][23][G:IBM-ROADMAP-2022]; IBM has shipped every published component of the stack except the code itself, so 2026 is optimistic and 2027 plausible. IQM: qLDPC demonstrators (2026-01-05 · 2027-28 · pending) [C][14]. Photonic Inc.: SHYPS announced 2025-02-11, peer-reviewed 2026-08, still no hardware [C][9][P][10].

**Strategic reading.** If BB codes work at scale, IBM wins the architecture argument it has made since 2024 and every surface-code roadmap absorbs a 10x overhead disadvantage or switches. Ions and photonic-linked platforms win incidentally; the loser is any platform whose only lever is planar lithography. Bargaining power sits with whoever controls high-degree interconnect, not the code's authors.

*Open niche:* the open ground is verification, not construction. No accepted protocol certifies a qLDPC logical qubit — break-even claims mix post-selection policies, decoders are not interchangeable, and no layer-fidelity-class metric exists for a code block under full syndrome load. A small QCVV house could ship that, plus a reference decoder harness. The adjacent slot is cold-stage decoding: an SFQ front end reducing 144-bit syndromes before the 4 K stage.

## Outlook & open questions

Confirm within 12–24 months if IBM demonstrates a gross-code memory below break-even with real-time decoding (Kookaburra, promised 2026), if any group performs a logical two-qubit gate between BB blocks, or if a BB result appears without leakage post-selection. Demote if Kookaburra slips past end-2027, or if Loon's c-coupler fidelity when published is poor enough to eat the 10× rate advantage. Best case by 2029: Starling-class machines, 200 logical qubits at ≈24–40 physical each, factoring estimates falling to the 10⁵-qubit range [S][11][24]. Worst case: a 20-qubit laboratory curiosity, connectivity costing more fidelity than the rate saves.

Open questions: (1) what two-qubit fidelity does a millimetre-scale coupler cost, and does it exceed the rate advantage? (2) can Relay-BP hold its latency on live syndromes? (3) do BB logical gates via adapters beat lattice surgery once the logical processing unit is counted? (4) how does the threshold move under leakage and loss rather than depolarising noise? (5) does anyone outside IBM adopt this family? Watch the Loon fidelity disclosure and IQM's 2027 demonstrator.

## Sources

[1] Bravyi et al. · High-threshold and low-overhead fault-tolerant quantum memory · Nature 627, 778 · 2024-03-27 · https://arxiv.org/abs/2308.07915
[2] Yoder et al. (IBM) · Tour de gross · arXiv:2506.03094 · 2025-06-03 · https://arxiv.org/abs/2506.03094
[3] Tham et al. (IonQ) · Breakeven demonstration of quantum low-density parity-check codes · arXiv:2606.06455 · 2026-06-04 · https://arxiv.org/abs/2606.06455
[4] Wang, Lu, Zhang et al. (Zhejiang) · Demonstration of low-overhead quantum error correction codes · 2025-05 · https://arxiv.org/html/2505.09684
[5] Maurer et al. (IBM) · Real-time decoding of the gross code memory with FPGAs · arXiv:2510.21600 · 2025-10-24 · https://arxiv.org/abs/2510.21600
[6] IBM Quantum · Clear path to fault-tolerant quantum computing · blog · 2025-06-10 · https://www.ibm.com/quantum/blog/large-scale-ftqc [C]
[7] IBM · Quantum roadmap · 2025-06-10 · https://www.ibm.com/roadmaps/quantum/ [C]
[8] IBM Newsroom · Nighthawk and Loon processors · 2025-11-12 · https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance [C]
[9] Photonic Inc. · Breakthrough results in error correction (SHYPS) · 2025-02-11 · https://photonic.com/news/shyps-codes-announcement/ [C]
[10] The Quantum Insider · Photonic publishes SHYPS qLDPC results in Nature Communications · 2026-08-26 · https://thequantuminsider.com/2026/08/26/photonic-shyps-quantum-error-correction-nature-communications/ [P]
[11] Iceberg Quantum · Pinnacle qLDPC architecture · arXiv:2602.11457 · 2026-02 · https://arxiv.org/abs/2602.11457
[12] DARPA · QBI Stage B selection · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[13] Quantum Computing Report · Photonic Inc. $2 B valuation, $200 M final close · 2026-05-12 · https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ [P]
[14] IQM · Constellation processor architecture · 2025-09-30 · https://iqm.tech/blog/iqm-constellation-a-new-quantum-processor-architecture-for-scalable-error-correction/ [C]
[15] Google Quantum AI · QEC below the surface code threshold · Nature 638, 920 · 2024-12-09 · https://www.nature.com/articles/s41586-024-08449-y
[16] NVIDIA · NVQLink architecture · 2025-11 · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [P]
[17] IBM · $10 B quantum investment FAQ · 2026-06-02 · https://www.ibm.com/quantum/blog/10-billion-investment-faq [C]
[18] NIST · Letters of intent to nine companies, $2.013 B · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[19] IonQ · SkyWater acquisition completed · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[20] Martiel, Chung, Seif, Ghosh, Hincks, Deshpande, Fefferman, Gambetta, Javadi-Abhari (IBM) · "Sampling hard circuits with verifiably high fidelity" — 70-qubit, depth-70 logical circuit with 468 T gates encoded in spacetime codes on 97 physical qubits, ~10× error suppression by syndrome post-selection · arXiv:2607.25941 · 2026-07-28 · https://arxiv.org/abs/2607.25941
[21] Justia Patents · quantum error-correction parity-check index · 2026-09-03 · https://patents.justia.com/search?q=%22parity+check%22+quantum+error+correction+code [P]
[22] Justia Patents · long-range coupler patents (IBM US 12,517,856; US 12,587,192) · 2026 · https://patents.justia.com/search?q=%22long-range+coupler%22+qubit [P]
[23] IBM · 2022 quantum roadmap · 2022-05-10 · https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025 [C]
[24] Gidney · Factoring 2048-bit RSA with under a million noisy qubits · arXiv:2505.15917 · 2025-05-21 · https://arxiv.org/abs/2505.15917

## Open verification items

- IonQ break-even paper: exact code notation, round count, post-selection acceptance rate and per-round logical error are not in the abstract; the graph record's 3.95 ± 0.68 s / 3.3 ± 0.9 s pair is unverified against the full text.
- Harvard/QuEra [[16,6,4]] run cited by the main report: no primary source found, and that code is not a bivariate bicycle code. Conflict flagged.
- Photonic Inc. "up to 20× fewer physical qubits" is a company claim with no stated logical error rate; the Nature Communications DOI and numbers were not retrievable within budget.
- Tour de gross module numbers (288 q + 90-q logical processing unit; 5,000 → 121 logical) are not verified against the preprint.
- No qLDPC patent family in the Justia index; one retry was rate-limited, so absence is not proven.
- IBM's "10× fewer qubits" (blog) versus 288 vs ≈3,000 (Nature): the blog rounds a ratio that depends on the assumed physical error rate. Both stated.
