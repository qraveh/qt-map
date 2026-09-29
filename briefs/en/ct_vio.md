---
id: ct_vio
name: Vertical (out-of-plane) signal delivery — VIO, Coaxmon, 3-D wiring
layer: "5 Control"
status: demonstrated
since: 2016
one_line: "Control and readout lines from room-temperature electronics reach each superconducting qubit through the face of the chip — coaxial pins, contact probes, superconducting vias or a stacked signal die — instead of being routed in the chip plane to its edge."
verdict: "Carries a 256-qubit processor (RIKEN/Fujitsu) and a >500-qubit wafer-scale package (OQC); it removes the edge-routing wall but not the line count, and line crosstalk has been published only for a four-qubit device as of 2026-09-26."
updated: 2026-09-26
---

TSV = through-silicon via; MXC = mixing chamber, the coldest refrigerator stage; T1, T2e = relaxation and echoed dephasing times; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Lines still start in room-temperature racks (ct_rt); only the last centimetre changes. Instead of a coplanar line routed to a wire-bond pad at the die edge, the signal enters through the chip's face — a spring-loaded or coaxial pin, a contact probe, a superconducting via, or a bump-bonded signal die. Waterloo's quantum socket (2016) pressed spring-mounted coaxial wires onto the chip [D][532]; Oxford's coaxial circuit QED (2017) put qubit and resonator on opposite faces with all wiring perpendicular [D][533], the root of OQC's Coaxmon. RIKEN chose backside superconducting vias over flip-chip interfaces that still bring pads to the edge [C][534] and reviewed the packaging this needs [G][535].
Attributes: microwave control at room temperature; coherent error; superconducting-lithography fabrication.

## Physics & limits
Edge routing. In an m × m lattice every line serving a qubit inside a ring crosses the ring's ~4m inter-qubit gaps; with k lines per qubit and c per gap, routing closes at m = 4c/k — for k = 2 and c = 3–5, N ≈ 36–100 [S]. That is the ~100-qubit plateau QuantWare cites [C][536], with "almost 90% of the chip" spent on routing [C][537]. A flip-chip signal die raises c, but lines still leave through a perimeter ∝ √N while their number grows ∝ N — polynomial, not the vendor's "exponential fan-out" [S]. Vertical entry keeps lines per unit area constant, so the lattice tiles.
The line. A vacuum coaxial hole is 50 Ω at a diameter ratio of 2.3 [S]. OQC's 50 ± 2.5 Ω pins end 0.9 mm (qubit) or 0.4 mm (resonator) from the circuit and couple evanescently below the hole's cutoff: control-line selectivity −40 to −60 dB at 2 mm pitch [D][538]. Non-galvanic pins carry no DC, so flux-tuned qubits and couplers need probes, vias or bumps [S].
Box modes. A 20 mm silicon die can resonate as low as ~3 GHz, inside the qubit band [S]; OQC's inductive pillar lifts the enclosure cutoff to 34.3 GHz and bounds parasitic coupling to |J|/2π < 250 kHz [D][538].
Heat is set per line, not by the route: OQC's fully wired wafer-scale package is estimated at ≤~3 µW on the MXC against 25–30 µW of cooling at 20 mK [D][311].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2016-05 | Spring-mounted coaxial wires, DC–8 GHz, contact ~150 mΩ, mismatch ~10 Ω | Univ. of Waterloo | [D][532] |
| 2017-08 | Superconducting TSVs, zero via-to-via resistance below aluminium's critical temperature | Rigetti | [D][539] |
| 2020 | 10 × 20 × 200 µm TSVs carry control and readout in a bump-bonded stack | MIT Lincoln Laboratory | [D][540] |
| 2021-11 | 127 qubits, wiring on "multiple physical levels" | IBM Eagle | [C][541] |
| 2022-04 | 2 × 2 coaxmons; T1 149(38) µs; single-qubit fidelity 99.982(4)% | Oxford / OQC | [D][538] |
| 2023-03 | 64 qubits, 2 cm chip, contact probes, 96 input + 16 output lines | RIKEN consortium | [C][542] |
| 2025-04 | 256 qubits; density ×4 in the same refrigerator | RIKEN / Fujitsu | [C][51] |
| 2026-02 | >500 qubits on a 3-inch die; median T1 97 µs, T2e 129 µs | OQC | [D][311] |

Among the register's carriers, beyond 256 gate-coupled qubits only claims exist: VIO-40K, 40,000 lines for 10,000 qubits in chiplet modules, shipping 2028 [C][536]. No Japanese machine has a two-qubit error in the register, and OQC's package reports coherence and readout, not gates [D][311].

## Manufacturing, materials & supply chain
Vias: MIT Lincoln Laboratory fabricates qubits on a TSV-bearing surface [D][540]; Rigetti's sloped walls let evaporated or sputtered films coat the via [D][539]. Pins: OQC's package manages differential thermal contraction across 3 inches with 0.5 mm pin gaps [D][311]. Stacks: QuantWare integrates "all signal conditioning components" [C][537] and opens KiloFab, Delft, in 2026 at 20× its 2025 capacity [C][536]. Pin, via and bump yields at 10³–10⁴ contacts are unpublished as of 2026-09-26.

## Control, readout & I/O burden
Vertical delivery moves lines; it does not remove them. RIKEN's 64 qubits take 112 lines [C][542], 1.75 per qubit [S]; OQC's four-qubit device two per qubit [D][538]; VIO-40K four [C][536]. OQC's wafer-scale package shares each line among nine qubits, control riding on readout [D][311] — ~0.11 per qubit [S]; the dimon, GENESIS's qubit [C][543], drives both modes through one control line [D][250]. At 10³ qubits that is 10²–4×10³ lines [S]; at 10⁴ QuantWare claims one cryostat [C][537]; at 10⁶ only cold multiplexing — ct_cryocmos, ct_sfq — closes the gap [S]. Loop latency is unchanged [S].

## Role in the stack
Slot 5 of "Transmon lattice with tunable couplers" and "Dual-rail erasure qubits". It **requires** ct_rt's electronics behind the vertical wiring and fab_sc's vias, pins and interposers; it and ct_rt **replace** one another ("edge-routed vs vertical signal delivery"); no **provides** edge is recorded. What it frees is the die edge, for chip-to-chip links between edge qubits [C][537] — a precondition for ic_multidie. Six register machines carry it, all primary. RIKEN 64 and RIKEN–Fujitsu 256 are ✅ on vendor figures; Toshiko's ✅ rests on the four-qubit paper, GENESIS's on the dual-rail paper, VIO-40K's on its announcement. The Fujitsu 1,000-qubit machine is 🔎: the cited article names high-density packaging, not perpendicular wiring [P][546]; the 10,000-qubit cell's wiring is undisclosed. Contralto-A17 and Tenor-D64 are not among them: the source presents Contralto-A as "a cost-efficient upgrade path to QuantWare's VIO-powered QPUs", not as one [C][544], and the D-line page pictures "VIO 1K" and "VIO 40K" modules without naming a processor [C][545]. Gap G-vio, answered: lines per qubit span 0.11–4; routing-layer count is undisclosed by every carrier.

## Evidence — how the numbers were measured
Line crosstalk exists only as OQC's four-qubit selectivity matrix [D][538]; RIKEN, Fujitsu and QuantWare publish none in the sources opened, as of 2026-09-26. OQC's package is the one many-qubit dataset: median T1, T2e ~100 µs over ~100 qubits, readout fidelity 97.5% and qubit temperature 36 mK over 54 [D][311]. Missing: simultaneous benchmarks over >100 lines; contact yield across thermal cycles.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| RIKEN | research | JP | Contact-probe package, 64 qubits | [C][542] |
| Fujitsu | developer | JP | 256-qubit unit-cell tiling; 1,000 qubits listed for 2026 | [C][51] |
| Oxford Quantum Circuits | developer | UK | Coaxmon on Toshiko and GENESIS; wafer-scale package | [C][543][D][311] |
| QuantWare | supplier | NL | VIO chip stack; VIO-40K for 2028 | [C][537] |
| MIT Lincoln Laboratory | research | US | TSVs in bump-bonded stacks | [D][540] |
| Rigetti Computing | developer | US | Superconducting TSV process | [D][539] |
| IBM | developer | US | Multi-level wiring (Eagle) | [C][541] |

**Money.**
- 2026-05-05 · QuantWare · Series B led by Intel Capital and In-Q-Tel, naming VIO-40K and KiloFab · USD 178 M · announced [C][547]
- 2026-06-02 · OQC · Series C led by Bullhound Capital, Coaxmon not named · GBP 260 M · announced [C][60]

**Market & supply chain.** RIKEN/Fujitsu and OQC build their own packages; QuantWare sells VIO to "scale the qubit chiplets and designs of third parties" [C][547]. Serves G2–G4 (transmon) and G3–G4 (dual-rail).

**IP & standards.** OQC calls the Coaxmon "patented" [C][543], no number traced; QuantWare pitches VIO-40K as the standard of its Quantum Open Architecture [P][495]. No standards body, as of 2026-09-26.

**Roadmaps & track record.** In July 2020 RIKEN aimed for a 64-qubit device "within the next three years" [C][534] and opened it on 2023-03-27 [C][542] — kept. Fujitsu still lists 1,000 qubits for 2026 [C][75], no launch found as of 2026-09-26. QuantWare: VIO-40K 2028 [C][536]; no interim VIO data, as of 2026-09-26.

**Strategic reading.** Past ~100 qubits vertical entry decides whether a die tiles, not whether a refrigerator can feed it; value moves to via, bump and pin capacity and to whoever first publishes crosstalk and yield at scale.

## Outlook & open questions
Confirm if, by 2027-12-31, a vertically wired processor above 256 qubits publishes two-qubit errors with simultaneous crosstalk; demote if Fujitsu's 1,000-qubit machine passes 2026-12-31 undisclosed or VIO-40K slips past 2028. Open questions. (1) What pitch holds selectivity below −40 dB at 1 mm qubit spacing? (2) Can non-galvanic pins serve flux-tuned couplers? (3) What is contact yield per thermal cycle at 10⁴ pins? (4) Does nine-way line sharing survive coupled qubits and gates? (5) At what scale does the stack's own heat bind?

## Sources

[51] Fujitsu Limited and RIKEN, “Fujitsu and RIKEN develop world-leading 256-qubit superconducting quantum computer,” Fujitsu Global, Apr. 22, 2025. [Online]. Available: https://info.archives.global.fujitsu/global/about/resources/news/press-releases/2025/0422-01.html [C]
[60] A. Curbison, “OQC raises £260m in Europe's largest ever private quantum computing funding round,” OQC, Jun. 2, 2026. [Online]. Available: https://oqc.tech/company/newsroom/series-c [C]
[75] Fujitsu, “Fujitsu Quantum.” [Online]. Available: https://global.fujitsu/en-global/technology/research/quantum [C]
[250] J. Wills, M. T. Haque, and B. Vlastakis, “Error-detected coherence metrology of a dual-rail encoded fixed-frequency multimode superconducting qubit,” [arXiv:2506.15420](https://arxiv.org/abs/2506.15420), Jun. 2025. [D]
[311] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [D]
[495] M. Abdel-Kareem, “QuantWare Debuts VIO-40K™ Architecture to Enable 10,000-Qubit Superconducting Processors,” Quantum Computing Report, Dec. 10, 2025. [Online]. Available: https://quantumcomputingreport.com/quantware-debuts-vio-40k-architecture-to-enable-10000-qubit-superconducting-processors/ [P]
[532] J. H. Béjanin *et al.*, “The Quantum Socket: Three-Dimensional Wiring for Extensible Quantum Computing,” *Phys. Rev. Appl.*, vol. 6, Art. no. 044010, 2016, doi: [10.1103/PhysRevApplied.6.044010](https://doi.org/10.1103/PhysRevApplied.6.044010). [arXiv:1606.00063](https://arxiv.org/abs/1606.00063). [D]
[533] J. Rahamim *et al.*, “Double-sided coaxial circuit QED with out-of-plane wiring,” *Appl. Phys. Lett.*, vol. 110, no. 22, Art. no. 222602, May 2017, doi: [10.1063/1.4984299](https://doi.org/10.1063/1.4984299). [arXiv:1703.05828](https://arxiv.org/abs/1703.05828). [D]
[534] RIKEN, “Wiring a new path to scalable quantum computing,” Jul. 3, 2020. [Online]. Available: https://www.riken.jp/en/news_pubs/research_news/rr/20200703_2/index.html [C]
[535] S. Tamate, Y. Tabuchi, and Y. Nakamura, “Toward Realization of Scalable Packaging and Wiring for Large-Scale Superconducting Quantum Computers,” *IEICE Trans. Electron.*, vol. E105.C, no. 6, pp. 290–295, Jun. 2022, doi: [10.1587/transele.2021SEP0007](https://doi.org/10.1587/transele.2021SEP0007). [G]
[536] QuantWare, “QuantWare announces scaling breakthrough with VIO-40K™, delivering 10,000 qubit Quantum Processors for the first time,” Dec. 8, 2025. [Online]. Available: https://quantware.com/news/quantware-announces-scaling-breakthrough-with-vio-40k [C]
[537] QuantWare, “Technology — VIO™ 3D Scaling Architecture.” [Online]. Available: https://quantware.com/technology [C]
[538] P. A. Spring *et al.*, “High coherence and low cross-talk in a tileable 3D integrated superconducting circuit architecture,” *Sci. Adv.*, vol. 8, no. 16, Art. no. eabl6698, Apr. 2022, doi: [10.1126/sciadv.abl6698](https://doi.org/10.1126/sciadv.abl6698). [arXiv:2107.11140](https://arxiv.org/abs/2107.11140). [D]
[539] M. Vahidpour *et al.*, “Superconducting Through-Silicon Vias for Quantum Integrated Circuits,” [arXiv:1708.02226](https://arxiv.org/abs/1708.02226), Aug. 2017. [D]
[540] D.-R. W. Yost *et al.*, “Solid-state qubits integrated with superconducting through-silicon vias,” *npj Quantum Inf.*, vol. 6, Art. no. 59, 2020, doi: [10.1038/s41534-020-00289-8](https://doi.org/10.1038/s41534-020-00289-8). [arXiv:1912.10942](https://arxiv.org/abs/1912.10942). [D]
[541] J. Chow, O. Dial, and J. Gambetta, “IBM Quantum breaks the 100‑qubit processor barrier,” IBM Quantum Computing Blog, Nov. 16, 2021. [Online]. Available: https://www.ibm.com/quantum/blog/127-qubit-quantum-processor-eagle [C]
[542] NTT (joint release of RIKEN, AIST, NICT, Osaka University, Fujitsu and NTT), “Japanese joint research group launches quantum computing cloud service: Opening access to Japan's first superconducting quantum computer,” Mar. 24, 2023. [Online]. Available: https://group.ntt/en/newsrelease/2023/03/24/230324a.html [C]
[543] Oxford Quantum Circuits, “Devices – OQC,” OQC. [Online]. Available: https://oqc.tech/tech/devices/ [C]
[544] QuantWare, “Introducing Contralto-A: a QPU for quantum error correction,” Feb. 25, 2025. [Online]. Available: https://quantware.com/news/introducing-contralto-a-qpu-for-quantum-error-correction [C]
[545] QuantWare, “D-line QPUs — Build bigger, scale faster.” [Online]. Available: https://quantware.com/product/processors/d-line [C]
[546] M. Swayne, “How Fujitsu Is Tackling a 10,000-Qubit Quantum Computer for Practical Applications,” The Quantum Insider, Dec. 8, 2025. [Online]. Available: https://thequantuminsider.com/2025/12/08/how-fujitsu-is-tackling-a-10000-qubit-quantum-computer-for-practical-applications/ [P]
[547] QuantWare, “QuantWare Raises $178 Million to Build World’s Most Powerful Quantum Processors at an Industrial Scale,” May 5, 2026. [Online]. Available: https://quantware.com/news/quantware-raises-178-million [C]

## Open verification items
- arXiv:2407.02769, named in the brief request as Tamate et al. 2024, is an unrelated image-classification paper (checked 2026-09-26); RIKEN's review is Tamate, Tabuchi and Nakamura, IEICE Trans. Electron. E105.C (2022), whose full text was blocked, so none of its figures is used.
- Crossref, Europe PMC, OpenAlex and Semantic Scholar returned HTTP 429 on 2026-09-26; the Béjanin and Yost records carry the year only.
- The IBM post opened does not say whether Eagle-generation signals enter through the chip face, and the register lists no IBM carrier; Rigetti Ankaa's signal delivery and any imec vertical-delivery work were not found (2026-09-26).
- QuantWare publishes no crosstalk, impedance, yield or heat-load data for VIO, and does not say which processor carries "VIO 1K" (2026-09-26).
- OQC's nine-way sharing (56 cells) is from its HTML full text; the number of lines entering the package, and whether its qubits are coupled, are not stated (2026-09-26).
