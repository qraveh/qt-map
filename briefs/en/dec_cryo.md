---
id: dec_cryo
name: Cryogenic / on-chip decoder (SFQ, cryo-CMOS)
layer: "8 Decoder"
tier: 2
status: empty slot
since: —
one_line: Syndrome decoding or pre-decoding executed inside the cryostat — SFQ logic at millikelvin, CMOS at 4 K — instead of at room temperature.
verdict: Four design studies, zero silicon as of 4 Sep 2026. Room-temperature FPGA decoders meet the 1.1 µs superconducting cycle, so only feedthrough count at 10⁴+ qubits can force this node into existence.
updated: 2026-09-04
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
A cryogenic decoder evaluates the syndrome-to-correction map inside the refrigerator instead of shipping every syndrome bit up the harness. Two substrates compete: single-flux-quantum (SFQ) logic switching quantised flux pulses at tens of GHz at millikelvin, and CMOS characterised at 4 K. The lineage is architectural: a per-qubit SFQ decoder in 2020 [S][2], an online SFQ surface-code decoder in 2021 [S][1], then in 2025–26 an inversion — compressing syndromes at 4 K rather than decoding them [S][3][S][4].
- Control and placement: cold digital logic at the millikelvin or 4 K stage.
- Manufacturing: Nb multilayer lithography or 4 K-characterised CMOS; no decoder-specific process exists.

## Physics & limits
The limit is thermal bookkeeping. An SFQ junction transition dissipates of order I_cΦ₀ ≈ 10⁻¹⁹ J, so a 10⁵-junction decoder at 2 GHz sits in the tens of µW — 2.78 µW is the published point [S][1] — against a dilution unit delivering hundreds of µW at 100 mK. Cryo-CMOS trades that for a ≈2 W plant at 4 K [S][11], of which one design spends 1.5 W to serve 2,668 logical qubits at d = 21 [S][3]. Neither floor is fundamental: it is allocation against a budget control already claims, moved only by adiabatic flux-parametron logic. The dominant failure mode is not a Pauli error — a decoder whose throughput falls below the syndrome rate accumulates unbounded backlog, so latency and bandwidth set the design. SFQ near the qubit die adds a second mechanism: pulse edges radiate, and photon-mediated quasiparticle poisoning measured 1.2(1)% error per Clifford on a separate-die SFQ driver that switches far less than a decoder would [D][G:SFQ-QP-POISONING-2023].

## Engineering state of the art
All decoder figures are post-synthesis; the last row is the nearest fabricated analogue.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-03 | SFQ surface-code decoder: 2.78 µW at 2 GHz, 1.0% threshold, d = 5–13 | Ueno et al. | [S][1] |
| 2025-12 | 22 nm FDSOI predecoder at 4 K: 3,780.72× bandwidth cut, peak < 0.56 mW | Univ. Michigan | [S][G:PINBALL-2025-12] |
| 2026-06 | 22 nm FDSOI compressor at 4 K: 48× at d = 17, 14,238× combined, 100 ns/round | Univ. Michigan | [S][G:CRYOZIP-2026-06] |
| 2026-07 | Fabricated 4 K CMOS controller self-sequencing a d = 5 repetition code, ≤3.5 W | HRL Laboratories | [D][G:HRL-CRYOCMOS-4K-2026] |

The dominant budget term is classical: off-cryostat bandwidth and round-trip latency.

## Manufacturing, materials & supply chain
Both cryo-CMOS designs run on 22 nm FDSOI characterised at 4 K, and both took that PDK from Semiwise Ltd (UK) [S][4] — one small supplier between every academic group and a tape-out. GlobalFoundries' 22FDX is the volume path behind it [C][G:GF-QTS-2026-05]. The SFQ path depends on SEEQC's multilayer Nb foundry in Elmsford NY [D][G:SEEQC-FUNDING], the only merchant line of its class. No yield or unit cost exists: nothing has taped out. ECCN 3A901.a covers CMOS ICs "designed to operate at" ≤4.5 K — design intent, not performance — so the layout is controlled pre-fabrication [G:BIS-3A901A-CRYOCMOS].

## Control, readout & I/O burden
The node exists to cut I/O. The superconducting QEC cycle is 1.1 µs [D][12] and a distance-d logical qubit emits d²−1 syndrome bits per round — ≈0.4 Gb/s at d = 21. At 10³ physical qubits nothing binds — a local clustering decoder holds under 1 µs per round to d = 17 on a Xilinx VU19P using ≈6% of its LUTs [D][G:RIVERLANE-LCD-2025-12], and exact FPGA matching averages 0.8 µs at d = 13 [D][7]. The wall at 10⁴–10⁶ is mechanical before computational: feedthrough count, harness heat load, serialiser bandwidth crossing 4 K. Compression attacks that term.

## Role in the stack
It requires millikelvin SFQ or 4 K cryo-CMOS control first, provides for nothing downstream, and blocks no one. It replaces room-temperature FPGA decoding: an FPGA is reprogrammable as codes and noise models change, a cold ASIC is fixed-function, competes with control for cold watts, and is export-controlled from the design file. The argument for an ASIC is supply-side: merchant high-end FPGAs are an AMD/Altera duopoly, one side private-equity-controlled since 2025 [G:ALTERA-SILVERLAKE-2025]. As a pre-decoder it adds ≈0.10 µs per round [S][G:CRYOZIP-2026-06] outside derived clock = sum of the syndrome round: gate layers + transport + readout + reset, which stays ≈0.65 µs against the measured 1.1 µs cycle; only the cabling cost changes.

## Verification (QCVV)
Every decoder number is post-synthesis power/performance/area on a cryo-characterised PDK plus vector simulation, syndromes drawn from noise models rather than a device; the 2025 predecoder is at least evaluated under circuit-level rather than code-capacity noise, and neither study is replicated outside an overlapping author set. Power per qubit at 4 K has no shared definition — 23 mW measured by IBM driving a two-qubit gate, against an "optimistic" 5 mW and sub-2 mW claims [S][G:CRYOCMOS-POWER-CONFLICT]; only 23 mW is tied to a running gate. The repeated 367 ns FPGA matching latency comes from a repository with no code distance and no paper; the peer-reviewed figure is 0.8 µs at d = 13 [D][7], used here.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| University of Michigan | Research | USA | Authored both cold predecoder and compressor designs | [S][G:PINBALL-2025-12] |
| SEEQC Inc. | Developer, supplier | USA | Nb foundry and millikelvin SFQ control; only credible SFQ host | [D][G:SEEQC-MK-SFQ-2026-03] |
| HRL Laboratories | Developer | USA | Only fabricated cold logic inside a QEC loop | [D][G:HRL-CRYOCMOS-4K-2026] |
| IBM | Developer, acquirer | USA | Cryo-CMOS flux-bias ASICs on 156 qubits; buying HRL | [C][G:IBM-CRYOCMOS-FLUX-2026-03] |
| Semiwise Ltd | Supplier | UK | Sole source of the 4 K 22 nm FDSOI PDK used | [S][4] |
| Riverlane | Developer, rival | UK | Room-temperature FPGA decoding incumbent | [D][G:RIVERLANE-LCD-2025-12] |
| US Bureau of Industry and Security | Regulator | USA | Controls ≤4.5 K CMOS ICs by design intent | [G:BIS-3A901A-CRYOCMOS] |

**Money.** 2025-12/2026-06 · University of Michigan · DOE ARQC award DE-SC0025633, amount undisclosed · funds both studies · ongoing [S][4]. 2026-05-21 · GlobalFoundries · CHIPS letter of intent · $375 M USD · US Commerce · non-binding [G:CHIPS-LOI-2026-05]. 2026-07-02 · SEEQC · S-1 for Nasdaq listing after a 2026-01-16 Allegro merger agreement · $75 M offering plus $65 M PIPE at ~$1 B enterprise value · filed, not closed [G][14]; the Allegro SPAC merger itself was terminated 2026-08-25 [G:SEEQC-SPAC-TERMINATED-2026-08]. 2026-07-23 · IBM · acquisition of HRL Laboratories · terms undisclosed · announced [C][G:IBM-HRL-2026-07]. No programme funds cryogenic decoding directly.

**Market & supply chain.** Nobody sells this. The enabling goods sit one layer down: cryo-PDKs, 22FDX capacity, Nb multilayer runs, and the racks a cold decoder would displace. Concentration is severe at both ends; no unit economics are quotable. Only G4 pays for this.

**IP & standards.** No patent family specific to cryogenic decoding was found in a named dated database. The nearest is Riverlane's GB 2641501 A "Quantum decoder" (published 2025-12-10), claiming room-temperature hardware clustering [G:SURFACE-CODE-PATENTS]. No standard exists for a syndrome interface across the 4 K boundary; NVIDIA's NVQLink standardises the warm side instead.

**Roadmaps & track record.** Michigan predecoder and compressor (2025-12-10, 2026-06-29 · no tape-out date · design-only as of 4 Sep 2026) — real PDK data, no fabrication commitment. SEEQC SFQ control (peer-reviewed 2026-03-10 · decode absent from its roadmap) — the only actor with process and listing proceeds to fund a tape-out. IBM cryo-CMOS control (abstracts 2026-03-16 · no preprint) — unproven at publication standard.

**Strategic reading.** If cold decoding works the winners already own cold silicon and cooling budget — SEEQC on SFQ, IBM/HRL and GlobalFoundries on CMOS — because decode folds into a chip they ship anyway. Losers are standalone decoder vendors whose value is reprogrammability, and accelerator vendors betting decode migrates to GPUs over a warm link. Bargaining power sits with the substrate owner.

*Open niche:* a small QCVV/SFQ group could take the measurement neither study has — decoder latency, power and backlog driven by real device syndromes rather than sampled noise — and characterise cold decode logic against the poisoning channel that damaged early SFQ control fidelity.

## Outlook & open questions
Confirm by 2028 if any cryogenic predecoder tapes out with measured silicon; demote if the 2027 literature is still post-synthesis. Best case 2029: a compressor at 4 K inside a QBI-adjacent system absorbs syndrome traffic before the harness. Worst case: room-temperature decoding scales with qLDPC codes and faster links. Open questions: which power baseline should size a cold decoder; can decode logic share a stage with control without reintroducing quasiparticle poisoning; does any platform hit the feedthrough wall before 10⁴ qubits. Watch the SEEQC listing and IBM's post-HRL roadmap.

## Sources
[1] Ueno, Kondo, Tanaka, Suzuki, Tabuchi · "QECOOL: On-Line Quantum Error Correction with a Superconducting Decoder for Surface Code" · DAC 2021, arXiv:2103.14209 · 2021-03-25 [S] — https://arxiv.org/abs/2103.14209
[2] Holmes, Jokar, Pasandi, Ding, Pedram, Chong · "NISQ+: Boosting quantum computing power by approximating quantum error correction" · ISCA 2020, arXiv:2004.04794 · 2020-04-09 [S] — https://arxiv.org/abs/2004.04794
[3] Knapen, Tao, Mack, Bruno, Sylvester, Zhang, Ravi, Saligane (Univ. Michigan) · "Pinball: A Cryogenic Predecoder for Surface Code Decoding Under Circuit-Level Noise" · HPCA 2026, arXiv:2512.09807 · 2025-12-10 [S] — https://arxiv.org/abs/2512.09807
[4] Tao, Knapen, Mack, Ravi, Zhang, Sylvester (Michigan), Saligane (Brown) · "CryoZip: An Efficient Cryogenic Compressor for Quantum Error Correction Syndromes" · arXiv:2606.30805 · 2026-06-29 [S] — https://arxiv.org/html/2606.30805v1
[5] Jordan, Bernhardt, Rahamim, Kirichenko et al. (SEEQC) · "A quantum computer controlled by superconducting digital electronics at millikelvin temperature" · Nature Electronics · 2026-03-10 [D] — https://www.nature.com/articles/s41928-026-01576-6
[6] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane) · "Local clustering decoder as a fast and adaptive hardware decoder for the surface code" · Nature Communications 16, 11048 · 2025-12-17 [D] — https://www.nature.com/articles/s41467-025-66773-x
[7] Wu, Liyanage, Zhong (Yale) · "Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction" · ASPLOS 2025, arXiv:2502.14787 · 2025-02-20 [D] — https://arxiv.org/abs/2502.14787
[8] HRL Laboratories · 18-qubit exchange-only SiGe processor with a 4 K cryo-CMOS controller · arXiv:2604.16216; Nature · 2026-07-29 [D] — https://arxiv.org/abs/2604.16216
[9] US Bureau of Industry and Security · interim final rule creating ECCN 3A901.a (cryogenic CMOS ≤4.5 K) · Federal Register · 2024-09-06 [G] — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[10] Liu, Ballard, Olaya, Schmidt, Biesecker et al. · quasiparticle poisoning of an SFQ driver · PRX Quantum 4, 030310 · 2023-07-24 [D] — https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310
[11] Kawabata et al. · 4 K resource review (power per qubit, plant capacities) · arXiv:2601.03922 · 2026-01-08 [S] — https://arxiv.org/abs/2601.03922
[12] Google Quantum AI · "Quantum error correction below the surface code threshold" (1.1 µs QEC cycle) · Nature 638, 920 · 2024-12-09 [D] — https://www.nature.com/articles/s41586-024-08449-y
[13] SEEQC · S-1 registration statement for a proposed Nasdaq offering · BusinessWire · 2026-07-02 [P] — https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering
[14] SEEQC / Allegro Merger Corp. · registration statement: $65 M PIPE, $75 M offering, up to 6,434,293 shares · SEC EDGAR · 2026-05-26 [G] — https://www.sec.gov/Archives/edgar/data/1779977/000121390026061108/ea0278139-04.htm
[15] IBM Newsroom · "IBM to Acquire HRL Laboratories" · 2026-07-23 [C] — https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum
[16] GlobalFoundries · "GlobalFoundries launches Quantum Technology Solutions" ($375 M CHIPS LOI) · 2026-05-21 [C] — https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/
[17] Quantum Machines · Series C press release ($170 M, 2025-02-25, PSG Equity lead) [C] — https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/

## Open verification items
DOE ARQC award DE-SC0025633 is acknowledged in the CryoZip paper but no dollar amount appears in any source consulted; treated as unquantified.
SEEQC's revenue and cash position are not in the registration statement, and the listing had not closed as of 4 Sep 2026.
4 K power per qubit remains unresolved (23 mW vs 5 mW vs sub-2 mW); every cold-decoder power comparison inherits the ambiguity.
No patent family specific to cryogenic decoding located in a named dated database; absence of evidence only.
