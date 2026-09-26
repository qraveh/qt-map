---
id: cx_aod
name: Atom transport by AOD tweezers (zoned architecture)
layer: "4 Connectivity / transport"
status: demonstrated
since: 2022
one_line: "Crossed acousto-optic deflectors move tweezers to shuttle atoms between storage, entangling and readout zones at ~99.95% per move."
verdict: "Real: 610 µm in 1.6 ms at 99.95% survival; 448 atoms under fault-tolerant control. Unverified: AOD channel bandwidth past 10⁴ atoms. Demote if no >10³-atom zoned system runs long-memory QEC by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An RF tone in a crystal makes an acoustic grating whose first-order diffraction angle tracks the tone, so sweeping the RF sweeps a tweezer and the atom in it; crossed x/y deflectors turn a comb of tones into a grid of movable traps. The zoned architecture partitions the plane into storage, entangling and readout regions, taking connectivity from moving atoms rather than fixed couplings — introduced by Bluvstein et al.'s 2022 coherent-transport processor (Harvard/MIT).

Attributes. **Mobility: transport** — atoms relocate hundreds of µm between zones, the platform's only long-range coupling. **Time ~10⁻³ s per move**, classical repositioning, neither deterministic nor heralded entanglement; the error is loss, not phase.

## Physics & limits

Two clocks bound a move: acoustic transit across the beam aperture sets how fast a tone can change (µs for millimetre apertures), and trap radial frequency sets how fast the atom can accelerate without heating out. The second dominates — transport error is release-and-recapture loss driven by trajectory jerk, so minimum-jerk profiles and deeper transit traps, not faster electronics, buy fidelity. Measured: 610 µm in 1.6 ms at 99.95%, 270 µm in 400 µs at 99.8% [D][124].

Coherence is not binding here: hyperfine $T_2$ is 12.6 s in the same 6,100-atom array [D][124] and 1.09(3) s under dynamical decoupling in a continuously reloaded 3,000-atom system [D][130]. So the signature is loss — detectable by imaging, hence erasure-convertible, and over 80% of all leakage; used as a supercheck with ML decoding it gave 2.14(13)× suppression at d=3→5 [D][4][G:HARVARD-LOSS-QEC-2025]. What moves the floor: minimum-jerk trajectories, deeper transit traps, and an acousto-optic lens adding the axial axis — so far a design study with no atoms [S][391].

## Engineering state of the art

Best demonstrated: 610 µm in 1.6 ms at 99.95% [D][124]. Typical at scale is the 448-atom zoned processor, where transport is interleaved with gates, not benchmarked alone [D][4].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-03 | 6,100-atom Cs array, hyperfine $T_2$ 12.6 s; moves 610 µm/1.6 ms at 99.95% | Caltech | [D][124] |
| 2025-09 | 3,217 atoms at 99.3% filling held >2 h, 30,000 initialised qubits/s | Harvard | [D][130] |
| 2025-11 | 448 atoms under fault-tolerant control, up to 96 logical qubits active | Harvard/MIT/QuEra | [D][4] |

Dominant error term: atom loss at release and recapture — the channel that makes the platform erasure-friendly.

## Manufacturing, materials & supply chain

No fab here — free-space optics bolted to a vacuum cell, so "yield" is array filling fraction: 99.3% after rearrangement [D][130], 60.5% before it in a metasurface array [D][131]. Named hardware in the 448-atom system: crossed AODs (DTSX-400, AA Opto-Electronic), Hamamatsu modulator and camera, Spectrum Instrumentation AWGs, Rohde & Schwarz microwave sources [D][4]; Gooch & Housego supplies deflectors in the 3,000- and 6,100-qubit papers [P][392]. That is the concentration risk: two small acousto-optics houses serve the published field, neither public nor separately funded. Cost per channel is not quotable. Export exposure is nil — the BIS rule of 2024-09-06 names no tweezer optics or deflectors, controlling only the resulting ≥34-qubit machines (4A906) [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

The burden is one RF tone per trap per axis, synthesised by AWG; count scales with atoms, not zones, and intermodulation between tones — not laser power — caps simultaneous traps. The cycle is the real cost: transport 0.4–1.6 ms plus imaging 0.5–1 ms gives QEC rounds of 1–4.5 ms, ~10³× a superconducting cycle, with the decoder obliged to keep up. At 10³ atoms a few AWG channels suffice; at 10⁴ the stated wall is AOD/SLM refresh, which no source consulted here quantifies against atom number; at 10⁶ the only design point puts RSA-2048 at 19 M atoms and 5.6 days at 1 ms cycles [S][30].

## Role in the stack

It requires laser plus AOD/SLM optical control and provides for bivariate-bicycle qLDPC codes, high-rate concatenated codes with transversal gates, and algorithmic fault tolerance — none reachable with fixed nearest-neighbour coupling, so it is a prerequisite, not a convenience. Paths served: alkali (Rb/Cs) and alkaline-earth (Yb/Sr) atoms. Nothing replaces or conflicts with it in the graph; pressure comes from other transport physics — the 3,000-qubit continuous system moves atoms 0.5 m on optical-lattice conveyor belts, using tweezers only for local rearrangement [D][130]. Contribution to the derived clock: dominant, at ~2.0×10⁻⁴ s per move it is 0.80 ms of the 1.31 ms sum of the syndrome round: gate layers + transport + readout + reset on both paths, since CZ runs at 270 ns.

## Verification (QCVV)

Move fidelity is post-recapture survival by fluorescence imaging: a loss metric, not a state fidelity, so 99.95% certifies the atom arrived, not that its phase did. No source isolates transport-only error at the logical level; the 448-atom results fold transport, gates and readout together [D][4]. The sharpest negative evidence is Atom Computing's toric-code run, where suppression over four cycles vanished once continuous reloading was included (0.63% versus 0.64% per cycle over 90 rounds) [D][133] — reloading and transport are the operations this node owns. Harvard and Caltech report 99.8–99.95% survival on different deflector hardware, consistent but not a replication.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Harvard | research | US | Originated zoned transport; 448-atom and 3,000-qubit systems | [D][4] |
| QuEra | developer | US | Commercialises the zoned architecture; QBI Stage B | [C][137] |
| Caltech | research | US | 6,100-atom array, move-fidelity records | [D][124] |
| Atom Computing | developer | US | Alkaline-earth zoned system; reloading-with-QEC data | [D][133] |
| Pasqal | developer | FR | AOD/SLM systems; photonic-chip trap alternative | [C][259] |
| Infleqtion | developer | US | NYSE-listed neutral-atom vendor | [G][261] |
| AA Opto-Electronic | supplier | FR | Crossed AODs (DTSX-400) in the 448-atom system | [D][4] |
| Gooch & Housego | supplier | UK | Deflectors in the 3,000- and 6,100-qubit papers | [P][392] |

**Money.**
- 2025-07-17 · QuNorth · order for Magne (Atom Computing/Microsoft, 50 logical) · €80 M · EIFO + Novo Nordisk Foundation · delivery turn of 2026/27 [G][11]
- 2025-09-09 · QuEra · financing round · $230 M+ · Google, SoftBank Vision Fund 2, NVentures · closed [C][137]
- 2026-06-16 · Atom Computing · Series C plus CHIPS LOI · >$300 M total · Third Point · closed + LOI [C][138][G:ATOM-300M-2026-06]
- 2026-08-12 · Infleqtion · Q2 revenue, FY guidance · $12.6 M, ~$43 M FY2026 · — · reported [G][261]
- 2026-08-28 · Pasqal · SPAC merger completed (Nasdaq PSQL) · ~$360 M cash · — · closed [P][140]

**Market & supply chain.** The equipment is generic photonics with one exception: crossed AODs, where AA Opto-Electronic and Gooch & Housego are the only vendors named in sourced material [D][4][P][392]. Deflector-channel demand grows linearly with atom count, so a small supplier could gate a platform. Unit economics are not quotable. G3 and G4 pay directly; G1 partly; G2, G5, G6, G7 indirectly.

**IP & standards.** No dated patent family with assignee and year was found for AOD-based zoned transport, and no standards body governs tweezer hardware. The one vendor specification with numbers is QuEra's Gemini page: 260 physical qubits, 99.2% global two-qubit fidelity, one shot per second [C][G:QUERA-GEMINI-SPEC-2026-09].

**Roadmaps & track record.** QuEra (promised Jan 2024 · 100 logical qubits in 2026 · status 2026-09-03: replaced by Libra 2028, >256 logical — a two-year slip) [R][142]. Atom Computing/Microsoft (2025-07 · Magne, 50 logical, turn of 2026/27 · installing) [G][11]. Pasqal (2024 · 10,000 physical in 2026 · slipped to 2028) [C][140]. Google entered March 2026 with no hardware result [C][9]. Experimental groups deliver what they publish; vendor logical-qubit dates have slipped about two years each.

**Strategic reading.** If zoned transport scales, Harvard's lineage companies and the two deflector houses win, and fixed-connectivity Rydberg machines lose the code families that matter. The substitution threat is other optics, not another node: metasurface arrays (11,022 atoms, no gates) [D][131] and photonic-chip trap delivery (4 atoms, 27.5 s, claimed 50× footprint cut) [C][259] would displace bulk AOD/SLM stacks if they reach gate quality.

*Open niche:* a small QCVV/SFQ research company could benchmark transport-induced loss and dephasing separately from gate and readout error — an interleaved-transport randomised benchmark no published source runs, since every result reports the combined figure.

## Outlook & open questions

Confirm by end-2027 a zoned system holding >1,000 atoms under fault-tolerant control; demote if by end-2028 no group shows long-memory suppression (Λ > 2) with continuous reloading — the case where suppression has already vanished once [D][133]. Best case by 2029: transport loss cut several-fold and the axial axis in use, unlocking 10⁴-atom zones. Worst case: channel count and refresh cap zones near 10³–10⁴ atoms. Open questions: does move fidelity hold at QEC duty cycles under reloading; can channel count scale past refresh limits; who else supplies deflectors at volume?

## Sources

[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[9] H. Neven, “Building superconducting and neutral atom quantum computers,” Google, Mar. 24, 2026. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]
[11] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [G]
[30] H. Zhou *et al.*, “Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays,” *Proc. 52nd Annu. Int. Symp. Comput. Archit. (ISCA)*, 2025, doi: [10.1145/3695053.3731039](https://doi.org/10.1145/3695053.3731039). [arXiv:2505.15907](https://arxiv.org/abs/2505.15907). [S]
[124] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[130] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[131] Y. Wang *et al.*, “Trapping 11,000 Atoms in a Tweezer Array Generated by a Single Metasurface,” [arXiv:2606.02715](https://arxiv.org/abs/2606.02715), Jun. 2026. [D]
[133] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[137] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[138] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[140] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[142] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[259] Pasqal, “Pasqal brings qubit control on-chip, advancing the path to fault-tolerant quantum computing at scale,” Aug. 10, 2026. [Online]. Available: https://www.pasqal.com/news/pasqal-brings-qubit-control-on-chip-advancing-the-path-to-fault-tolerant-quantum-computing-at-scale/ [C]
[261] Infleqtion, “Infleqtion Reports Record Q2 Revenue, Raises 2026 Outlook as Quantum Commercialization Accelerates,” Aug. 12, 2026. [Online]. Available: https://ir.infleqtion.com/news-events/press-releases/detail/201/infleqtion-reports-record-q2-revenue-raises-2026-outlook-as-quantum-commercialization-accelerates [G]
[391] Z. Guo, R. A. van Herk, E. J. Vredenbregt, and S. J. Kokkelmans, “Acousto-optic lens for 3D shuttling of atoms in a neutral atom quantum computer,” [arXiv:2510.09398](https://arxiv.org/abs/2510.09398), Oct. 2025. [S]
[392] Gooch & Housego (G&H), “G&H Acousto-Optic Deflectors Referenced in Nature Papers Demonstrating 3,000 & 6,100 Qubit Quantum Systems,” G&H, Mar. 2026. [Online]. Available: https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [P]

## Open verification items

- The "AOD/SLM refresh near 10 MHz is insufficient above ~10⁴ qubits" wall is carried from the main report; no source consulted here quantifies channel count or refresh rate against atom number.
- No source isolates transport-only fidelity from combined transport + gate + readout logical numbers.
- Bluvstein et al.'s 2022 coherent-transport paper is cited as lineage from the technology-graph record; no numbered source is given for it.
- No dated patent family (assignee + year) found for AOD-based zoned atom transport.
- AA Opto-Electronic and Gooch & Housego capacity and scale-up plans not found; neither appears separately funded or public.
- [391] is an optical design study with no trapped atoms; its axial range, speed and survival are not established experimentally.
- [4]'s online date (2025-11-10) differs from its print date (Jan 2026); dated 2025-11 per the graph record.
