---
id: code_color
name: Colour code (transversal Cliffords)
layer: "7 Code"
status: demonstrated
since: 2024
one_line: Triangular 2D stabilizer code whose whole Clifford group acts transversally, skipping lattice surgery, at roughly 1.9× the surface code's teraquop footprint.
verdict: The colour code's future is as the magic-state factory feeding surface-code memory, not as the memory. Demote the memory case if no platform reports a colour-code logical memory beating the surface code on total qubits for a fixed logical target by 2028.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A 2D topological stabilizer code on a three-colourable trivalent lattice, each plaquette carrying an X and a Z stabilizer of weight 6. Because the two types share support, the entire Clifford group — H, S, CNOT — is transversal, where the surface code gets only CNOT natively and pays lattice surgery for the rest. Bombín and Martín-Delgado introduced it in 2006 [D][502]; the first full hardware demonstration is Google's, submitted December 2024 [D][40]. The price is density: ~1.9× the surface code's teraquop footprint, 1,250 against 650 physical per logical at 0.1% noise [S][493][G:SURFACE-TERAQUOP-650].
d = static triangular lattice, no transport; e = inherits the host's control modality and placement [graph].
f = Pauli stabilizers only; a = 0.5 — identical on fabricated and natural carriers, needing only a static nearest-neighbour lattice [graph].

## Physics & limits
The transversal gate needs no merge/split: Google puts a logical Hadamard at ~20 ns against ~1,000× longer through lattice surgery [C][503]. Weight-6 checks mean deeper extraction and hook errors that cut the effective distance unless the schedule avoids them — a 2026 construction avoids all malign bulk hook errors with one auxiliary per plaquette [S][504]. Errors also fire three detectors, so the syndrome is a hypergraph: matching does not apply and decoders must project or search. Hence the gap: Λ₃/₅ = 1.56(4) [D][40] against 2.14 for the surface code on the same processor family [D][1], and Google's 2026 d=5 colour-code memory reached 8.19(14)×10⁻³ per cycle only with the search-based Tesseract decoder [D][2]. What moves the floor is circuit scheduling and decoders, not the code.

## Engineering state of the art
| Year | Figure | Who | Tag+Key |
|---|---|---|---|
| 2024-12 | Λ₃/₅ = 1.56(4); transversal Clifford adds 0.0027(3) | Google Quantum AI | [D][40] |
| 2025-07 | first logical 5-to-1 distillation, d=3 and d=5 patches | QuEra | [D][132] |
| 2026-07 | distance-5 colour-code memory, 8.19(14)×10⁻³ per cycle | Google Quantum AI | [D][2] |

Dominant term: the syndrome round, not the transversal gate — weight-6 extraction and hypergraph decoding leave Λ at 1.56 against 2.14 [D][1], [40].

## Manufacturing, materials & supply chain
No fabrication of its own: it inherits the host's chip, trap or tweezer array, tiled hexagonally rather than square, and brings no new supplier [D][40]. Export exposure is the host's: quantum computers sit under ECCN 4A906 (BIS, 2024-09-06) [G:BIS-3A901A-CRYOCMOS], while the code is published mathematics from 2006 [D][502].

## Control, readout & I/O burden
Control and readout per qubit match the host's surface-code burden. The difference is per round: each data qubit sits in six weight-6 checks against the surface code's four weight-4 checks, so a round costs about 1.5× the two-qubit gates on a deeper schedule, and that is where the threshold goes. Against it, a logical Clifford needs no merge/split rounds at all. Decoding is the harder item: hypergraph syndromes rule out a stock matching engine, and the only published d=5 hardware decode is Google's Tesseract search decoder [D][2].

## Role in the stack
Sits in the superconducting, trapped-ion and neutral-atom paths [graph]; requires the same static nearest-neighbour lattice as the surface code and hosts magic-state factories. All three 2025–26 magic-state milestones ran in colour codes: cultivation to 0.9999(1) at 8% acceptance before code-switching out [D][41], Quantinuum's [[15,1,3]]→[[7,1,3]] switching at ≤5.1(2.7)×10⁻⁴ [D][505], QuEra's 5-to-1 distillation [D][132]. It replaces the surface code where transversal Cliffords beat the ~1.9× footprint; switching costs a decoder and a layout, not hardware. Clock contribution ~20 ns per logical Hadamard [C][503]; the code does set d₂, the gate-layer count summed into the round (derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path), 0.65 µs derived against the measured 1.1 µs host cycle. Neighbouring empty slot: no hardware colour-code decoder.

## Verification (QCVV)
Λ₃/₅ = 1.56(4) and the 0.0027(3) transversal-Clifford error are Google's own, one processor, unreplicated by a second vendor [D][40]. Two framings of that paper conflict: it reports 86.5(1)–90.7(1)% teleported-state fidelities for lattice surgery, while Google's blog presents 86–91% as "two-qubit gate fidelity" [C][503] — trust the paper. Magic injection exceeds 99% only with post-selection keeping ~75% of runs [D][40]. The footprint claims are not comparable either: "fewer physical qubits per code distance" [C][503] against total qubits for a fixed logical target [S][493]. Nothing published separates code error from decoder error in the transversal figure.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Google Quantum AI | Developer/user | US | Only superconducting colour-code memory; cultivation host | [D][40], [41] |
| Quantinuum | Developer/user | US | Colour-code code switching; tesseract [[16,6,4]] on Helios | [D][505], [506] |
| Microsoft Quantum | Developer | US | Co-authored the tesseract colour-code result | [D][506] |
| QuEra | Developer/user | US | First logical 5-to-1 distillation on colour-code patches | [D][132] |

**Money.** 2025-07-14 · QuEra · publication (first logical 5-to-1 distillation) · no figure · funded from its $230 M+ 2025 round [C][137] · published [D][132]. 2025-11-06 · DARPA QBI Stage B · up to $15 M per team · eleven teams, Quantinuum and QuEra among them [G][60]. 2026-06-03 · Quantinuum · IPO · $1.68 B gross at $60/share, Nasdaq QNT; Q2-2026 revenue $8.0 M, cash $2.1 B · closed [G][112]. No round, grant or acquisition is specific to the colour code: it is a line item inside platform programmes.

**Market & supply chain.** No dedicated supply chain; it rides the host's fab and the general classical stack. The market it moves is decoding: hypergraph syndromes need search or projection decoders (FPGA/GPU work from AMD and NVIDIA), and no vendor ships a colour-code hardware decoder as of 4 Sep 2026. Pays into G3 and G4 through magic-state factories: every logical magic-state milestone since 2025 ran in a colour code [D][41], [132], [505].

**IP & standards.** The code is published mathematics from 2006 [D][502]. PatSnap's April 2026 landscape counts 12 QEC patents — Google 6, IBM 4, Tencent 2 — with no colour-code cluster [P][507]. Google's granted surface-code patent covers gauge operators, not this code [G:SURFACE-CODE-PATENTS]. No standards body; the de facto interface is a Stim detector-error model.

**Roadmaps & track record.** Google (2025-06-23 · colour code a "workhorse configuration", no dated milestone · a d=5 memory followed in July 2026) [C][503][D][2]. Quantinuum (2024-09 · Helios 2025 → Sol 2027 → Apollo 2029 · Helios shipped 2025-11-05 and carried the tesseract result) [R][G:QTM-ROADMAP]. QuEra (2026-06 · Libra, >256 logical, 2028 · its January-2024 roadmap promised 100 logical in 2026, undelivered) [R][G:QUERA-LIBRA-2026]. Google's claims have been measurements, not promises; Quantinuum's schedule has held; QuEra's research runs ahead of its product roadmap.

**Strategic reading.** The colour code favours platforms where qubits are cheap and logical time expensive — superconducting and neutral atoms — over trapped ions, where a 1.9× premium falls on the scarce resource. Its likeliest 2029 position is not memory but the T-state factory feeding surface-code memory: cultivation cut magic-state cost ~40× inside a colour code and then switched out [D][41], making it a component of a surface-code machine rather than a competitor. Substitution threats: high-rate qLDPC blocks with transversal gates, and algorithmic fault tolerance replacing O(d) rounds per logical gate. Losers: toolchains built only around lattice surgery.

*Open niche:* a QCVV shop could supply what no vendor has published — a protocol separating code error from decoder error in a transversal logical Clifford (0.0027(3) mixes both), and a reconciliation of the two footprint framings on one noise model. Both are refereeing jobs an interested party cannot credibly do.

## Outlook & open questions
Confirm/demote in 12–24 months: a colour-code memory beyond d=5 with Λ approaching 2.14; a second vendor reproducing transversal Cliffords. Best case 2029: cultivation makes it the standard magic-state substrate, the footprint premium confined to factory patches. Worst case: hook-error and decoder overheads keep Λ near 1.5 and it survives only as a distillation substrate. Open questions: does the one-auxiliary-per-plaquette circuit [S][504] recover a competitive threshold on hardware; do planar non-Clifford circuits [S][508] beat distillation; will anyone publish a total-footprint comparison.

## Sources
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[40] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[41] E. Rosenfeld *et al.*, “Magic state cultivation on a superconducting quantum processor,” [arXiv:2512.13908](https://arxiv.org/abs/2512.13908), Dec. 2025. [D]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[112] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G]
[132] P. S. Rodriguez *et al.*, “Experimental demonstration of logical magic state distillation,” *Nature*, vol. 645, no. 8081, pp. 620–625, Jul. 2025, doi: [10.1038/s41586-025-09367-3](https://doi.org/10.1038/s41586-025-09367-3). [D]
[137] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[493] C. Gidney and C. Jones, “New circuits and an open source decoder for the color code,” [arXiv:2312.08813](https://arxiv.org/abs/2312.08813), Dec. 2023. [S]
[502] H. Bombín and M. A. Martin-Delgado, “Topological Quantum Distillation,” *Phys. Rev. Lett.*, vol. 97, Art. no. 180501, 2006, doi: [10.1103/PhysRevLett.97.180501](https://doi.org/10.1103/PhysRevLett.97.180501). [arXiv:quant-ph/0605138](https://arxiv.org/abs/quant-ph/0605138). [D]
[503] A. Bourassa and K. Satzinger, “A colorful quantum future,” Google Research Blog, Jun. 23, 2025. [Online]. Available: https://research.google/blog/a-colorful-quantum-future/ [C]
[504] G. Kishony and A. Fowler, “Color code off-the-hook: avoiding hook errors with a single auxiliary per plaquette,” [arXiv:2603.28852](https://arxiv.org/abs/2603.28852), Mar. 2026. [S]
[505] L. Daguerre, R. Blume-Kohout, N. C. Brown, D. Hayes, and I. H. Kim, “Experimental Demonstration of High-Fidelity Logical Magic States from Code Switching,” *Phys. Rev. X*, vol. 15, no. 4, Art. no. 041008, Oct. 2025, doi: [10.1103/dck4-x9c2](https://doi.org/10.1103/dck4-x9c2). [arXiv:2506.14169](https://arxiv.org/abs/2506.14169). [D]
[506] A. Paetznick *et al.*, “Improved quantum processor logical error rates via correction and detection,” *Nature*, vol. 654, no. 8118, pp. 349–355, Jun. 2026, doi: [10.1038/s41586-026-10628-y](https://doi.org/10.1038/s41586-026-10628-y). [D]
[507] PatSnap, “Quantum Error Correction Technology Landscape 2026,” Apr. 22, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/articles/quantum-error-correction-patent-landscape-2026/ [P]
[508] A. Bauer and J. C. M. de la Fuente, “Planar Fault-Tolerant Circuits for Non-Clifford Gates on the 2D Color Code,” *PRX Quantum*, vol. 7, no. 2, Art. no. 020367, Jun. 2026, doi: [10.1103/p7c9-x1m9](https://doi.org/10.1103/p7c9-x1m9). [arXiv:2505.05175](https://arxiv.org/abs/2505.05175). [S]

## Open verification items
The authors and institutions of arXiv:2603.28852 ("Color code off-the-hook") could not be resolved from the abstract page; the hook-error and single-auxiliary claims are stated there, the Monte Carlo improvement is not quantified [504].
The quantitative claims of arXiv:2505.05175 (planar non-Clifford circuits on the 2D colour code) could not be extracted; only its title and PRX Quantum acceptance are confirmed [508].
Google's blog reports 86–91% as "two-qubit gate fidelity" where the paper reports 86.5(1)–90.7(1)% teleported-state fidelities via lattice surgery [40], [503] — same numbers, different quantity; unreconciled by either source.
"Fewer physical qubits for the same code distance" [503] and the 1,250-against-650 teraquop footprint [493] measure different quantities; no published source reconciles them.
No independent, non-Google replication of Λ₃/₅ = 1.56(4) was located as of 4 Sep 2026.
