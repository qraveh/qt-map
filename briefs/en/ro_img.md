---
id: ro_img
name: Fluorescence imaging of atom arrays
layer: "6 Readout"
status: demonstrated
since: 2016
one_line: Camera-based fluorescence detection of neutral atoms — non-destructive, mid-circuit, millisecond by default, microsecond in single-group demos.
verdict: Sets the neutral-atom QEC round at ~1 ms; unless sub-100 µs low-loss imaging reaches shipped hardware by 2028 it stays the largest fixed cost in the cycle.
updated: 2026-10-09
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An atom on a closed cycling transition scatters photons into a high-NA objective and onto a camera; a photon-count threshold per site decides occupancy or state. Standard on tweezer arrays since about 2016, and the readout every neutral-atom architecture builds on.
Camera fluorescence imaging, ~0.5–1 ms, non-destructive, mid-circuit capable.
Optical control at room temperature; free-space bench optics; error structure is loss.

Resonant fluorescence imaging resolving each site's state in tens of microseconds instead of the 0.5–1 ms exposure atom arrays have always needed [D][4]. Two August-2026 preprints a week apart define the state of the art: Kyoto's coherent excitation on ¹⁷⁴Yb, 17.6 µs at 99.89(5)% discrimination and 98.80(44)% survival [D][261], and USTC's site-resolved adaptive protection with continuous photon counting, 15 µs average probe [D][623].

## Physics & limits
Signal is collection solid angle times quantum efficiency times scattering rate times integration time, and threshold error falls exponentially in collected photons: discrimination is cheap. The cost is recoil: every scattered photon heats the atom, and past a few thousand it leaves the trap, so the failure mode is loss — 0.46% bit-flip against 0.24% loss at 448 atoms [D][4]. Shorter probes improve survival: both 2026 microsecond results report loss an order below the millisecond baseline. NA and quantum efficiency sit near their practical ceiling, leaving recooling during the probe, brighter transitions and parallel zones. Architecturally the round matters: CZ gates take 270 ns while a QEC round takes 1–4.5 ms, imaging 0.5–1 ms of it and transport the rest [D][4].

The floor is a photon budget. Discrimination needs enough detected photons to separate bright from dark above camera read noise, and detected photons are the scattered count times collection efficiency — an NA-0.6 objective collects about a tenth of 4π [D][261]. Every scattered photon carries two recoils, so the heating that ejects the atom scales with the same count that buys the discrimination: survival and fidelity trade through one variable. Both 2026 results therefore attack the count, not the exposure — Kyoto by exciting coherently, halving the heating rate of incoherent schemes [D][261], USTC by stopping the scattering at each site the moment continuous photon counting has decided its state, reaching 4.1×10⁻⁵ discrimination infidelity at 2.1×10⁻⁴ loss [D][623]. What moves the floor is collection: higher NA, cavity collection, photon-counting arrays in place of EMCCD (electron-multiplying CCD) cameras, cooling during the probe.

## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-11 | 0.5–1 ms, 0.46% bit-flip, 0.24% loss, 448-atom FT array | Harvard/MIT/QuEra | [D][4] |
| 2026-08 | 17.6 µs, 99.89(5)% discrimination, 98.80(44)% survival, spinless ¹⁷⁴Yb | Kyoto/Yaqumo | [P][261] |
| 2026-08 | 15 µs probe on a 25-site subarray, 4.1×10⁻⁵ infidelity, 2.1×10⁻⁴ loss | USTC | [P][623] |

Dominant error: imaging-induced loss, not misassignment.

The dominant term is no longer the exposure: at 17.6 µs the optical step is a twenty-sixth of the classical chain [C][826] and an order of magnitude below transport [D][4]. What enters the code is loss during the probe, not discrimination.

## Manufacturing, materials & supply chain
No fab: an objective, dichroics and a camera on a bench. Hamamatsu's ORCA-Quest qCMOS is the named sensor across the Harvard/QuEra line, with no second source at this sensitivity [P][329]; objectives are commodity microscope optics. Imaging sits inside the QEC cycle, so its cost is per round, not per shot. At 10³ atoms one frame covers the array; at 10⁴–10⁶ pixel count, frame rate and illumination power force parallel zones with a camera each — the regime where beam steering also stops scaling in one device: a deflector resolves as many spots as its rf bandwidth times the acoustic transit across the beam, a transit that also bounds how fast it re-points a trap, and liquid-crystal modulators reframe only at tens of hertz. Export exposure is indirect: 4A906 binds the machine only when its qubit count and C-NOT error fall in the same band, from 34–99 qubits at ≤ 10⁻⁴ to any error from 2,000 qubits [G:BIS-3A901A-CRYOCMOS]; nothing names tweezer optics or cameras [G][301].

No chip: sensors, objectives and lasers. Three camera vendors appear across every sourced result — Hamamatsu qCMOS in the Harvard/QuEra line [C][G:HAMAMATSU-CAMERA-CONC-2026], Andor (Oxford Instruments) EMCCD at Kyoto [D][261], Teledyne Kinetix in Quantum Machines' stack [C][826] — and no atom-array company makes one, so the sensor is the clearest single point of failure. Export exposure is asymmetric: the machine is caught by ECCN 4A906 (BIS, 2024-09-06) [G][301], the cameras are dual-use instruments outside the 2024 quantum ECCNs.

## Control, readout & I/O burden
Fast imaging removes one term, not the cycle. An atom QEC round is imaging (0.5–1 ms) plus transport (hundreds of µs) plus gates, 1–4.5 ms in total [D][4]; taking imaging to 17.6 µs leaves transport and the classical chain, so the round improves by about a factor of two, not the 30–50× the imaging figures alone suggest. The classical chain is the larger term: 442 µs camera-to-server transfer plus 21–85 µs processing, 460 µs on a 10×10 array [C][826] — twenty-six times the exposure. At 10³ sites the camera link binds; at 10⁴–10⁶ only per-site counting with an on-sensor decision scales.

## Role in the stack
It is the readout of all three neutral-atom architectures: the alkali (Rb/Cs) and alkaline-earth(-like) (Yb/Sr) Rydberg tweezer arrays and the neutral-atom analogue simulator. Requires an alkali or alkaline-earth(-like) atom with a cycling transition; provides the non-destructive mid-circuit measurement real-time decoding needs, and turns atom loss into detectable erasure, not silent Pauli error. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 1.3×10⁻³ s, transport first and this readout second at 501 µs, not the 270 ns gate — ~10³× a superconducting round. Verification: both microsecond results are single-group and single-species; Kyoto's uses spinless ¹⁷⁴Yb, so it establishes occupancy discrimination, not hyperfine state readout, and USTC's 15 µs averages over a 25-site subarray. Neither has run inside a logical memory.

Fast imaging is, so far, an alkaline-earth(-like) result: Kyoto's 17.6 µs is on ¹⁷⁴Yb [D][261] and USTC does not state its species [D][623], so the microsecond end of this readout is tied to the Yb/Sr architecture until an alkali array shows it. At ~18 µs it would cut ~0.5 ms from the 1.3 ms round and leave transport (~800 µs) the largest term.

## Evidence — how the numbers were measured
Both are single-lab preprints a week apart, neither replicated. Kyoto's 17.6 µs is imaging alone, with no array size in the abstract [D][261]. USTC's 15 µs is an average probe time, and the 1.7 kHz, 120-round run applied adaptive protection to a 25-site subarray of a 100-qubit array [D][623] — untested where it matters. The precedent is Atom Computing's toric code: suppression survived 90 rounds but vanished once reloading was included, 0.63% against 0.64% per cycle [D][148]. Continuous operation is proven separately — >3,000 qubits over two hours [D][144] — never with microsecond readout.

The Kyoto/Yaqumo 17.6 µs result is on spinless ¹⁷⁴Yb, which has no hyperfine qubit: it is occupancy discrimination, not state readout. QuNorth's €80 M Magne order is sourced from trade press, with no vendor release. That scientific cameras fall outside the 2024 quantum ECCNs is read from those ECCNs' own scope [301], not from a camera-specific ruling. Quantum Machines' 460 µs chain figure is self-reported and not independently audited [826]. Not published: the camera used in the Kyoto demonstration, and a unit cost per readout channel for camera plus objective. Not stated in the abstract of arXiv:2608.17189: USTC's atom species and transition, detector type and collection NA.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Harvard/MIT | research | US | 448-atom fault-tolerant baseline | [D][4] |
| QuEra Computing | developer | US | Ships this readout in its roadmap | [C][153] |
| Atom Computing | developer | US | Yb arrays; Magne with Microsoft | [C][154] |
| Kyoto Univ./Yaqumo | research | Japan | 17.6 µs Yb imaging demo | [P][261] |
| Hamamatsu Photonics | supplier | Japan | qCMOS sensor, no second source | [P][329] |
| USTC | research | China | 15 µs adaptive probe with sub-µs feed-forward decoding | [D][623] |
| Quantum Machines | supplier | Israel | Sells the classical readout chain | [C][826] |

**Money.** 2025-09-09 · QuEra · Series B · $230 M+ USD · Google, SoftBank VF2, NVentures [C][153]. 2025-11-06 · DARPA · QBI Stage B · ≤$15 M each · Atom and QuEra among eleven [G][65]. 2026-02 · Infleqtion · NYSE listing · >$550 M USD, plus $100 M DoC LOI [C][155]. 2026-06 · Atom Computing · raise · $300 M+ USD incl. $100 M Commerce LOI [C][154]. 2026 · QuNorth · Magne order, 50 logical · €80 M · Atom/Microsoft [P][12]. 2025-02-25 · Quantum Machines · Series C · $170 M · closed [C][528][G:QM-SERIESC-2025-02]. Nothing is funded as fast readout: it is instrument spend inside platform budgets, and both defining results came from universities, not the companies that need them.

**Market & supply chain.** One vendor's sensor sits in the critical path of every leading array, the rest being commodity optics — sharp concentration risk. It pays into G3 and G4: no mid-circuit imaging, no real-time decoding. The enabling suppliers are camera vendors (Hamamatsu, Andor, Teledyne) and control vendors (Quantum Machines); no fast-atom-readout product exists. Sensor concentration is severe: three vendors, none replaceable in-house. Capturable value sits in the classical chain, which is why the control vendor publishes the benchmarks [C][826]. Pays into G3 and G4, and into G1 where shot rate is throughput.

**IP & standards.** No dated patent family or standard specific to atom-array imaging. No dated patent family for fast atom-array readout surfaced as of 4 Sep 2026; both results are preprints and the only company on either author list is Yaqumo Inc. [D][261]. No standards body governs sensor choice. The absence of IP is itself a finding: the technique is published, not fenced.

**Roadmaps & track record.** (2026-08 · fast imaging shown standalone · not folded into a logical run); (2028–29 · QuEra Libra and Magne targets · assume the cycle keeps shrinking) [R][153]. Vendor roadmaps price in a speed-up shown only on subarrays. Atom Computing with Microsoft (2025-07 · Magne, 50 logical, €80 M, turn of 2026/27 · being installed) [R][11]. QuEra (2026-06 · Libra 2028, >256 logical · its 2024 roadmap promised 100 logical in 2026 — a two-year slip) [R][162]. Nobody has dated a commitment to ship sub-20 µs readout; the sector's record is a ~2-year slip.

**Strategic reading.** Whoever ships sub-100 µs low-loss imaging first collapses the largest fixed cost in the neutral-atom cycle taking a factor of several in effective clock, the platform's one structural weakness. Camera suppliers hold more leverage than their revenue implies; atom vendors none over them. The winner is whichever atom company gets the camera out of the loop, not whichever gets the exposure shortest: the bottleneck measured is a 442 µs frame transfer, not a 17.6 µs probe [C][826]. Camera vendors hold supplier power today and lose it the moment integrated detection arrives. The platform reading is soberer — closing the imaging term moves the atom cycle disadvantage from ~10³× to perhaps ~10²×, which does not settle the architecture argument [D][4].

## Outlook & open questions
Confirm if a microsecond result is folded into a logical memory run by 2028; demote if it stays readout-only. Best case 2029: sub-50 µs imaging is standard and QEC rounds fall below 0.5 ms. Worst case: millisecond imaging stays the default and caps the cycle near 1 ms. Open: does fast imaging hold across a full array, and does it shift the loss-versus-Pauli mix decoders assume?

Confirm/demote in 12–24 months: either result reproduced by a second group; sub-20 µs readout inside a live logical-qubit run; readout held under reloading at full array size. Best case 2029: microsecond imaging is standard, the round is transport-limited at a few hundred µs, and loss detection is cheap enough to make erasure conversion routine. Worst case: the numbers hold only on small static subarrays. Open questions: what species USTC used; does adaptive stopping survive on a full array where counting runs everywhere at once; who builds the first sensor with the decision on the die.

## References
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[11] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [R]
[12] M. Abdel-Kareem, “Denmark's QuNorth to Acquire 50-Logical-Qubit Magne Quantum Computer from Atom Computing and Microsoft,” Quantum Computing Report, Jul. 17, 2025. [Online]. Available: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ [P]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[144] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[153] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[155] L. Roady, “Infleqtion Becomes First Neutral-Atom Quantum Company to Go Public,” Infleqtion, Feb. 17, 2026. [Online]. Available: https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [C]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[329] M. Ivezic, “The Tweezer Array's Hidden Supply Chain: Who Really Wins If Neutral-Atom Quantum Computing Wins,” PostQuantum.com, Nov. 17, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/neutral-atom-quantum-ecosystem/ [P]
[528] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[623] Xu-Zhao-Qiu Zeng *et al.*, “Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor,” [arXiv:2608.17189](https://arxiv.org/abs/2608.17189), Aug. 2026. [P]
[826] U. Akhouri, “Classically Accelerated Readout for Neutral Atoms with CPU/GPU Integration,” Quantum Machines Blog, Jun. 2026. [Online]. Available: https://www.quantum-machines.co/resources/blog/classically-accelerated-readout-neutral-atoms-cpu-gpu-readout/ [C]
