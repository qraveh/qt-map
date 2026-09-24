---
id: dec_relaybp
name: Relay-BP for qLDPC (FPGA)
layer: "8 Decoder"
status: demonstrated
since: 2025
one_line: "Belief propagation with disordered, partly negative memory strengths, chained in relay legs, decoding bivariate-bicycle qLDPC syndromes at 24 ns per iteration on an FPGA."
verdict: "Removes the OSD post-processor that made qLDPC decoding non-real-time: 24 ns/iteration and under 1 µs average per cycle on FPGA. Never run on live syndromes — no gross-code memory exists on any QPU as of 2026-09-04."
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Belief propagation in which each variable node carries its own *memory strength* — a damping coefficient drawn from a disordered distribution that must include negative values — with decoding run as a chain of relay legs, each restarted from the previous leg's messages. IBM (Müller, Alexander, Beverland, Bühler, Johnson, Maurer, Vandeth) introduced it on 2025-06-02 [D][1]; a second IBM team put it on an FPGA on 2025-10-24 for the [[144,12,12]] gross code [D][2][G:GROSSCODE-FPGA-2025-10]. Attributes: d = no physical connectivity, an off-chip classical block; e/f/g = no control modality, corrects Pauli errors, no fabrication — an FPGA bitstream (graph record).

## Physics & limits
The limit is an accuracy-versus-latency budget, not a physical one. Plain BP stalls on degenerate stabiliser codes — distinct error patterns carry identical likelihood, so messages oscillate into trapping sets — and the standard repair, ordered-statistics post-processing, has a data-dependent cost no real-time loop absorbs. Relay-BP's claim is that disordered memory strengths break exactly the symmetry that stalls BP, making the post-processor unnecessary; the paper states a distribution containing negative values is indispensable [D][1].

That buys latency: 24 ns per BP iteration and an *average* per-cycle decoding time under 1 µs for physical error probabilities below 3×10⁻³ [D][2]. Average is where the risk sits — iteration count is data-dependent, so the latency distribution has a tail, and a decoder fed a fixed-rate stream at the 1.1 µs superconducting cycle must buffer, the backlog diverging rather than degrading if that tail exceeds the cycle time often enough. Neither paper reports anything but the mean. The second floor is the error rate itself: above 3×10⁻³ iteration counts climb, so the real-time property is conditional on the hardware already being good. What moves the floor: an ASIC, or windowing that commits early cycles while later ones converge.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-06 | Relay-BP beats BP+OSD+CS-10 on bivariate-bicycle codes, matching-class on surface codes | IBM | [D][1] |
| 2025-10 | FPGA: 24 ns/iteration, average < 1 µs per cycle at p < 3×10⁻³, simulated syndromes | IBM | [D][2][G:GROSSCODE-FPGA-2025-10] |
| 2025-12 | Local Clustering Decoder: < 1 µs/round to d=17 using ≈6% of a Xilinx VU19P's LUTs | Riverlane | [D][3][G:RIVERLANE-LCD-2025-12] |

Both FPGA results are simulation-driven: no gross-code memory has run on any QPU, so Relay-BP has never consumed a hardware syndrome [D][4]. The target code is IBM's [[144,12,12]], 288 physical qubits at a 0.8% threshold on a degree-6 Tanner graph [D][5][G:IBM-BBCODE-2024]; the only qLDPC break-even anywhere is IonQ's [[18,4,3]] trapped-ion memory, leakage post-selected [D][6][G:IONQ-QLDPC-BREAKEVEN-2026-06].

## Manufacturing, materials & supply chain
No fabrication process: the deliverable is a bitstream and the supply chain is merchant FPGA silicon, a duopoly restructured in 2025 when Intel sold 51% of Altera to Silver Lake at an $8.75 B valuation, taking ~$4.46 B and retaining 49% [G][7]. Every named real-time decoder here runs on AMD parts (Riverlane's LCD on a VU19P [D][3]), and IBM's is reported as AMD by trade press whose page could not be retrieved [P][8][G:IBM-AMD-RELAYBP-FPGA-2025]. No decoder-specific export-control category exists as of 2026-09-04.

## Control, readout & I/O burden
The decoder drives nothing; its burden is syndrome bandwidth and fan-in. One gross module is 144 data plus 144 check qubits, so a cycle yields 144 bits — ~0.14 Gbit/s per module at a 1 µs cycle [S][5]. Scaled naively, 10⁴ physical qubits is ~5 Gbit/s and 10⁶ ~0.5 Tbit/s at fixed rate: the wall is not BP arithmetic but getting bits out of the cryostat into enough parallel instances.

## Role in the stack
It requires the bivariate-bicycle/gross qLDPC family and replaces minimum-weight perfect matching; the graph record marks it a hub reaching the superconducting, trapped-ion electronic-gate and photonic continuous-variable paths. Derived clock contribution: < 1.0 µs per cycle (2 s.f.), the first decoder figure that fits inside a 1.1 µs superconducting cycle without an offline pass [D][2], [9]. Switching costs a code change, not a board change: gross codes need degree-6 long-range couplers IBM has shown only as components, where LCD assumes the nearest-neighbour grid hardware already has [D][3][G:IBM-TOURDEGROSS-2025]. Adjacent empty slot: a merchant decoder ASIC.

## Verification (QCVV)
Every headline is from simulated syndromes under a noise model with neither leakage nor correlated bursts — the dominant real-device terms [D][4]. No independent group has reproduced either number, and Riverlane's LCD uses a different code and FPGA, so the two are not commensurable [D][3].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IBM | Developer | USA | Invented Relay-BP and built the FPGA implementation for its gross code | [D][1], [2] |
| AMD | Supplier | USA | Xilinx FPGA silicon under IBM's demonstration and most rival decoders | [P][8][G:IBM-AMD-RELAYBP-FPGA-2025] |
| Altera | Supplier | USA | The only other merchant high-end FPGA source; 51% Silver Lake-owned since 2025 | [G][7] |
| Riverlane | Developer | UK | Competing FPGA decoder for the surface code, sold as a product | [D][3][G:RIVERLANE-LCD-2025-12] |
| DARPA | Regulator | USA | QBI Stage B funds IBM's fault-tolerance programme this serves | [G][10][G:QBI-STAGEB-2025-11] |

**Money.** 2024-08-06 · Riverlane · Series C · $75 M (its 2026 roadmap says $85 M — unreconciled) · Planet First Partners lead · closed [C][11][G:RIVERLANE-FUNDING]. 2025-04-14 · Intel/Silver Lake · 51% of Altera at $8.75 B valuation, ~$4.46 B to Intel · announced [G][7]. 2025-11-06 · DARPA · QBI Stage B, up to $15 M each, IBM the only transmon vendor · awarded [G][10][G:QBI-STAGEB-2025-11]. Relay-BP itself has no round, grant or licence: in-house IBM work as of 2026-09-04.

**Market & supply chain.** Decoding is priced as bundled firmware, not silicon: Riverlane sells Deltaflow [C][G:RIVERLANE-DELTAFLOW-PAGE-2026-05], IBM ships Relay-BP inside its own stack. Concentration risk is FPGA supply — two vendors, one newly under private-equity control [G][7]. Goal exposure is narrow, G3 and G4 only: a real-time decoder is worthless until a code needs it, so willingness to pay is vendors insuring their own 2027–2029 roadmaps.

**IP & standards.** Riverlane holds GB 2641501 A "Quantum decoder" (published 2025-12-10) on hardware clustering over the decoding hypergraph [G:SURFACE-CODE-PATENTS]; IBM's bivariate-bicycle estate covers the code, not the decoder, and no Relay-BP family appears in any named database. No standards body addresses decoder interfaces.

**Roadmaps & track record.** IBM: (2025-06 · Relay-BP algorithm · delivered); (2025-10 · FPGA implementation · delivered); (2023 roadmap · Kookaburra qLDPC module for 2026 · slipped a year, undelivered) [R][4][G:IBM-ROADMAP]. Riverlane: (2026-03 · teraquop decoding from 2033 · too early) [C][G:RIVERLANE-ROADMAP-2026-03]. IBM's decoder software is on time twice over; the hardware it decodes is not.

**Strategic reading.** If Relay-BP holds up, IBM removes the strongest objection to qLDPC — that its decoder cannot run in real time — and the ~10× qubit saving over the surface code becomes bankable, hurting surface-code-shaped roadmaps and helping whoever can build degree-6 connectivity. If not, matching decoders keep the field. Decoding is becoming a component business with no dedicated supplier: two FPGA vendors, one GPU vendor pushing an alternative, no merchant ASIC. Bargaining power stays with the QPU vendor that picks the code.

*Open niche:* no decoder in this layer has been benchmarked against live device noise — leakage, correlated bursts, drifting detector priors — and none publishes latency *distributions*, only means. A replay service streaming recorded syndrome traces through each vendor's decoder, reporting tail latency and accuracy under real noise, is an open niche with no incumbent.

## Outlook & open questions
Falsifiable (12–24 months): confirm if Kookaburra ships and a gross-code memory is decoded in real time by end-2027; demote if Relay-BP has consumed no hardware syndrome by then. Best case 2029: Relay-BP-class decoding inside IBM's Starling stack at the demonstrated latency. Worst case: gross-code hardware keeps slipping and GPU or matching decoders take the installed base. Open questions: the 99.9th-percentile latency rather than the mean; whether accuracy survives leakage and correlated bursts; whether anyone builds a decoder ASIC. Watch: Kookaburra delivery, any live-syndrome decode, the first latency histogram.

## Sources
[1] T. Müller *et al.*, “Improved belief propagation is sufficient for real-time decoding of quantum memory,” [arXiv:2506.01779](https://arxiv.org/abs/2506.01779), Jun. 2025.
[2] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025.
[3] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x).
[4] IBM, “Quantum Roadmap.” [Online]. Available: https://www.ibm.com/roadmaps/quantum/ [R]
[5] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, pp. 778–782, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915).
[6] E. Tham *et al.*, “Breakeven demonstration of quantum low-density parity-check codes,” [arXiv:2606.06455](https://arxiv.org/abs/2606.06455), Jun. 2026.
[7] Altera, “Altera Closes Silver Lake Investment to Become World's Largest Pure-play FPGA Solutions Provider,” Sep. 15, 2025. [Online]. Available: https://www.altera.com/newsroom/news/press-release/altera-silver-lake [G]
[8] A. Woodie, “IBM Touts Affordable Quantum Error Correction on AMD FPGAs,” HPCwire, Oct. 28, 2025. [Online]. Available: https://www.hpcwire.com/2025/10/28/ibm-touts-affordable-quantum-error-correction-on-amd-fpgas/ [P]
[9] Qblox and Riverlane, “Qblox and Riverlane demonstrate integration enabling real-time quantum error correction (250 physical / 1 logical, sub-µs feedback),” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[10] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[11] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” company press release, Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]

## Open verification items
Neither abstract states the FPGA part, LUT/memory usage or arithmetic precision; the AMD attribution rests on trade press [8], whose page could not be retrieved (redirect loop).
No latency distribution or tail percentile is published for Relay-BP — only the average.
Riverlane's Series C is stated as $75 M in the 2024 release and $85 M in its 2026-03 roadmap release [G:RIVERLANE-FUNDING].
