---
id: code_color
name: Colour code (transversal Cliffords)
layer: "7 Code"
tier: 2
status: demonstrated
since: 2024
one_line: Triangular 2D stabilizer code whose whole Clifford group acts transversally, skipping lattice surgery, at roughly 1.9× the surface code's teraquop footprint.
verdict: The colour code's future is as the magic-state factory feeding surface-code memory, not as the memory. Demote the memory case if no platform reports a colour-code logical memory beating the surface code on total qubits for a fixed logical target by 2028.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A 2D topological stabilizer code on a three-colourable trivalent lattice, each plaquette carrying an X and a Z stabilizer of weight 6. Because the two types share support, the entire Clifford group — H, S, CNOT — is transversal, where the surface code gets only CNOT natively and pays lattice surgery for the rest. Bombín and Martín-Delgado introduced it in 2006 [D][5]; the first full hardware demonstration is Google's, submitted December 2024 [D][1]. The price is density: ~1.9× the surface code's teraquop footprint, 1,250 against 650 physical per logical at 0.1% noise [S][12][G:SURFACE-TERAQUOP-650].
d = static triangular lattice, no transport; e = inherits the host's control modality and placement [graph].
f = Pauli stabilizers only; a = 0.5 — identical on fabricated and natural carriers, needing only a static nearest-neighbour lattice [graph].

## Physics & limits
The transversal gate needs no merge/split: Google puts a logical Hadamard at ~20 ns against ~1,000× longer through lattice surgery [C][2]. Weight-6 checks mean deeper extraction and hook errors that cut the effective distance unless the schedule avoids them — a 2026 construction avoids all malign bulk hook errors with one auxiliary per plaquette [S][3]. Errors also fire three detectors, so the syndrome is a hypergraph: matching does not apply and decoders must project or search. Hence the gap: Λ₃/₅ = 1.56(4) [D][1] against 2.14 for the surface code on the same processor family [D][11], and Google's 2026 d=5 colour-code memory reached 8.19(14)×10⁻³ per cycle only with the search-based Tesseract decoder [D][10]. What moves the floor is circuit scheduling and decoders, not the code.

## Engineering state of the art
| Year | Figure | Who | Tag+Key |
|---|---|---|---|
| 2024-12 | Λ₃/₅ = 1.56(4); transversal Clifford adds 0.0027(3) | Google Quantum AI | [D][1] |
| 2025-07 | first logical 5-to-1 distillation, d=3 and d=5 patches | QuEra | [D][6] |
| 2026-07 | distance-5 colour-code memory, 8.19(14)×10⁻³ per cycle | Google Quantum AI | [D][10] |

Dominant term: the syndrome round, not the transversal gate — weight-6 extraction and hypergraph decoding leave Λ at 1.56 against 2.14 [D][1][11].

## Manufacturing, materials & supply chain
No fabrication of its own: it inherits the host's chip, trap or tweezer array, tiled hexagonally rather than square, and brings no new supplier [D][1]. Export exposure is the host's: quantum computers sit under ECCN 4A906 (BIS, 2024-09-06) [G:BIS-3A901A-CRYOCMOS], while the code is published mathematics from 2006 [D][5].

## Control, readout & I/O burden
Control and readout per qubit match the host's surface-code burden. The difference is per round: each data qubit sits in six weight-6 checks against the surface code's four weight-4 checks, so a round costs about 1.5× the two-qubit gates on a deeper schedule, and that is where the threshold goes. Against it, a logical Clifford needs no merge/split rounds at all. Decoding is the harder item: hypergraph syndromes rule out a stock matching engine, and the only published d=5 hardware decode is Google's Tesseract search decoder [D][10].

## Role in the stack
Sits in the superconducting, trapped-ion and neutral-atom paths [graph]; requires the same static nearest-neighbour lattice as the surface code and hosts magic-state factories. All three 2025–26 magic-state milestones ran in colour codes: cultivation to 0.9999(1) at 8% acceptance before code-switching out [D][9], Quantinuum's [[15,1,3]]→[[7,1,3]] switching at ≤5.1(2.7)×10⁻⁴ [D][7], QuEra's 5-to-1 distillation [D][6]. It replaces the surface code where transversal Cliffords beat the ~1.9× footprint; switching costs a decoder and a layout, not hardware. Clock contribution ~20 ns per logical Hadamard [C][2] against a 1.1 µs host cycle, so the code does not set the derived clock (derived clock = max(gate, readout, transport) for the path). Neighbouring empty slot: no hardware colour-code decoder.

## Verification (QCVV)
Λ₃/₅ = 1.56(4) and the 0.0027(3) transversal-Clifford error are Google's own, one processor, unreplicated by a second vendor [D][1]. Two framings of that paper conflict: it reports 86.5(1)–90.7(1)% teleported-state fidelities for lattice surgery, while Google's blog presents 86–91% as "two-qubit gate fidelity" [C][2] — trust the paper. Magic injection exceeds 99% only with post-selection keeping ~75% of runs [D][1]. The footprint claims are not comparable either: "fewer physical qubits per code distance" [C][2] against total qubits for a fixed logical target [S][12]. Nothing published separates code error from decoder error in the transversal figure.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Google Quantum AI | Developer/user | US | Only superconducting colour-code memory; cultivation host | [D][1][9] |
| Quantinuum | Developer/user | US | Colour-code code switching; tesseract [[16,6,4]] on Helios | [D][7][8] |
| Microsoft Quantum | Developer | US | Co-authored the tesseract colour-code result | [D][8] |
| QuEra | Developer/user | US | First logical 5-to-1 distillation on colour-code patches | [D][6] |

**Money.** 2025-07-14 · QuEra · publication (first logical 5-to-1 distillation) · no figure · funded from its $230 M+ 2025 round [C][15] · published [D][6]. 2025-11-06 · DARPA QBI Stage B · up to $15 M per team · eleven teams, Quantinuum and QuEra among them [G][16]. 2026-06-03 · Quantinuum · IPO · $1.68 B gross at $60/share, Nasdaq QNT; Q2-2026 revenue $8.0 M, cash $2.1 B · closed [G][14]. No round, grant or acquisition is specific to the colour code: it is a line item inside platform programmes.

**Market & supply chain.** No dedicated supply chain; it rides the host's fab and the general classical stack. The market it moves is decoding: hypergraph syndromes need search or projection decoders (FPGA/GPU work from AMD and NVIDIA), and no vendor ships a colour-code hardware decoder as of 4 Sep 2026. Pays into G3 and G4 through magic-state factories: every logical magic-state milestone since 2025 ran in a colour code [D][6][7][9].

**IP & standards.** The code is published mathematics from 2006 [D][5]. PatSnap's April 2026 landscape counts 12 QEC patents — Google 6, IBM 4, Tencent 2 — with no colour-code cluster [P][13]. Google's granted surface-code patent covers gauge operators, not this code [G:SURFACE-CODE-PATENTS]. No standards body; the de facto interface is a Stim detector-error model.

**Roadmaps & track record.** Google (2025-06-23 · colour code a "workhorse configuration", no dated milestone · a d=5 memory followed in July 2026) [C][2][D][10]. Quantinuum (2024-09 · Helios 2025 → Sol 2027 → Apollo 2029 · Helios shipped 2025-11-05 and carried the tesseract result) [R][G:QTM-ROADMAP]. QuEra (2026-06 · Libra, >256 logical, 2028 · its January-2024 roadmap promised 100 logical in 2026, undelivered) [R][G:QUERA-LIBRA-2026]. Google's claims have been measurements, not promises; Quantinuum's schedule has held; QuEra's research runs ahead of its product roadmap.

**Strategic reading.** The colour code favours platforms where qubits are cheap and logical time expensive — superconducting and neutral atoms — over trapped ions, where a 1.9× premium falls on the scarce resource. Its likeliest 2029 position is not memory but the T-state factory feeding surface-code memory: cultivation cut magic-state cost ~40× inside a colour code and then switched out [D][9], making it a component of a surface-code machine rather than a competitor. Substitution threats: high-rate qLDPC blocks with transversal gates, and algorithmic fault tolerance replacing O(d) rounds per logical gate. Losers: toolchains built only around lattice surgery.

*Open niche:* a QCVV shop could supply what no vendor has published — a protocol separating code error from decoder error in a transversal logical Clifford (0.0027(3) mixes both), and a reconciliation of the two footprint framings on one noise model. Both are refereeing jobs an interested party cannot credibly do.

## Outlook & open questions
Confirm/demote in 12–24 months: a colour-code memory beyond d=5 with Λ approaching 2.14; a second vendor reproducing transversal Cliffords. Best case 2029: cultivation makes it the standard magic-state substrate, the footprint premium confined to factory patches. Worst case: hook-error and decoder overheads keep Λ near 1.5 and it survives only as a distillation substrate. Open questions: does the one-auxiliary-per-plaquette circuit [S][3] recover a competitive threshold on hardware; do planar non-Clifford circuits [S][4] beat distillation; will anyone publish a total-footprint comparison.

## Sources
[1] Lacroix, Bourassa, Heras, Zhang et al. (Google Quantum AI), "Scaling and logic in the colour code on a superconducting quantum processor", Nature 645, 614 (2025); arXiv:2412.14256 (2024-12-18) — https://www.nature.com/articles/s41586-025-09061-4 ; https://arxiv.org/abs/2412.14256
[2] Google Research, "A colorful quantum future" (2025-06-23) — https://research.google/blog/a-colorful-quantum-future/ [C][G:GOOGLE-COLORBLOG-2025-06]
[3] "Color code off-the-hook: avoiding hook errors with a single auxiliary per plaquette", arXiv:2603.28852 (2026-03) — https://arxiv.org/abs/2603.28852 [S]
[4] "Planar fault-tolerant circuits for non-Clifford gates on the 2D color code", arXiv:2505.05175; accepted, PRX Quantum 10.1103/p7c9-x1m9 — https://arxiv.org/abs/2505.05175 [S]
[5] Bombín, Martín-Delgado, "Topological quantum distillation", Phys. Rev. Lett. 97, 180501 (2006); arXiv:quant-ph/0605138 — https://arxiv.org/abs/quant-ph/0605138
[6] Cantu et al. (QuEra, Harvard, MIT), "Experimental demonstration of logical magic state distillation", Nature 645, 620 (2025-07-14) — https://www.nature.com/articles/s41586-025-09367-3 [G:MAGIC-MSD-NEUTRAL-2025-07]
[7] Daguerre, Blume-Kohout, Brown, Hayes, Kim (Quantinuum), "Experimental demonstration of high-fidelity logical magic states from code switching", Phys. Rev. X 15, 041008; arXiv:2506.14169 (2025-06-17) — https://arxiv.org/abs/2506.14169 [G:MAGIC-CODESWITCH-2025-06]
[8] Microsoft Quantum with Quantinuum, tesseract [[16,6,4]] colour code, Nature 654 (2026-06-10) — https://www.nature.com/articles/s41586-026-10628-y [G:TESSERACT-16-6-4]
[9] Rosenfeld, Gidney, Roberts, Morvan, Lacroix et al. (Google Quantum AI), "Magic state cultivation on a superconducting quantum processor", arXiv:2512.13908 (2025-12-15) — https://arxiv.org/abs/2512.13908 [G:MAGIC-CULTIVATION-2025-12]
[10] Sivak, Morvan, Broughton et al. (Google Quantum AI), "Reinforcement learning control of quantum error correction", Nature 655 (2026-07-08) — https://www.nature.com/articles/s41586-026-10759-2 [G:ALPHAQUBIT2-2026-07]
[11] Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920 (2024-12-09) — https://www.nature.com/articles/s41586-024-08449-y [G:WILLOW-QEC-2024-12]
[12] Gidney, Jones (Google), "New circuits and an open source decoder for the colour code", arXiv:2312.08813 (2023-12-14) — https://arxiv.org/abs/2312.08813 [S][G:SURFACE-TERAQUOP-650]
[13] PatSnap Insights, "Quantum error correction patent landscape 2026" (2026-04-22) — https://www.patsnap.com/resources/blog/articles/quantum-error-correction-patent-landscape-2026/ [P][G:PATSNAP-QEC-LANDSCAPE-2026-04]
[14] Quantinuum, "Quantinuum announces pricing of upsized initial public offering" (2026-06-03) — https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G:QTM-IPO-2026-06]
[15] QuEra, "QuEra expands $230 million financing round" (2025) — https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C][G:QUERA-230M-2025]
[16] DARPA, QBI Stage B selection (2025-11-06) — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G:QBI-STAGEB-2025-11]

## Open verification items
The authors and institutions of arXiv:2603.28852 ("Color code off-the-hook") could not be resolved from the abstract page; the hook-error and single-auxiliary claims are stated there, the Monte Carlo improvement is not quantified [3].
The quantitative claims of arXiv:2505.05175 (planar non-Clifford circuits on the 2D colour code) could not be extracted; only its title and PRX Quantum acceptance are confirmed [4].
Google's blog reports 86–91% as "two-qubit gate fidelity" where the paper reports 86.5(1)–90.7(1)% teleported-state fidelities via lattice surgery [1][2] — same numbers, different quantity; unreconciled by either source.
"Fewer physical qubits for the same code distance" [2] and the 1,250-against-650 teraquop footprint [12] measure different quantities; no published source reconciles them.
No independent, non-Google replication of Λ₃/₅ = 1.56(4) was located as of 4 Sep 2026.
