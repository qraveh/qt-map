---
id: ro_imgfast
name: Fast (≤ 20 µs) atom-array readout
layer: "6 Readout"
tier: 2
status: emerging
since: 2026
one_line: Sub-20-microsecond fluorescence imaging of atom-array qubits, replacing millisecond exposures and moving readout out of the neutral-atom QEC cycle's critical path.
verdict: Fast imaging takes readout off the critical path but leaves transport and the camera link, so the round improves ~2×, not 30×. Demote if no group shows sub-20 µs readout on a full array under continuous reloading by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Resonant fluorescence imaging resolving each site's state in tens of microseconds instead of the 0.5–1 ms exposure atom arrays have always needed [D][4]. Two August-2026 preprints a week apart define the state of the art: Kyoto's coherent excitation on ¹⁷⁴Yb, 17.6 µs at 99.89(5)% discrimination and 98.80(44)% survival [D][1], and USTC's site-resolved adaptive protection with continuous photon counting, 15 µs average probe [D][2].
c = optical imaging at ~17.6 µs (10⁻⁴·⁷⁵ s), non-destructive, mid-circuit-capable [graph].
e = optical control at room temperature; g = optics only — camera and collection optics, no chip [graph].

## Physics & limits
The floor is a photon budget. Discrimination needs enough detected photons to separate bright from dark above camera read noise, and detected photons are the scattered count times collection efficiency — an NA-0.6 objective collects about a tenth of 4π [D][1]. Every scattered photon carries two recoils, so the heating that ejects the atom scales with the same count that buys the discrimination: survival and fidelity trade through one variable. Both 2026 results therefore attack the count, not the exposure — Kyoto by exciting coherently, halving the heating rate of incoherent schemes [D][1], USTC by stopping the scattering at each site the moment continuous photon counting has decided its state, reaching 4.1×10⁻⁵ discrimination infidelity at 2.1×10⁻⁴ loss [D][2]. What moves the floor is collection: higher NA, cavity collection, photon-counting arrays in place of EMCCD, cooling during the probe.

## Engineering state of the art
| Year | Figure | Who | Tag+Key |
|---|---|---|---|
| 2025-11 | non-destructive readout 0.46% bit-flip, 0.24% loss; imaging 0.5–1 ms | Harvard University | [D][4][G:HARVARD-LOSS-QEC-2025] |
| 2026-08-17 | 15 µs average probe, 4.1×10⁻⁵ infidelity, 1.7 kHz over 120 rounds | USTC | [D][2][G:USTC-FASTREADOUT-2026-08] |
| 2026-08-24 | 17.6 µs imaging, 99.89(5)% discrimination, 98.80(44)% survival | Kyoto University | [D][1][G:KYOTO-FASTIMG-2026-08] |

The dominant term is no longer the exposure: at 17.6 µs the optical step is a twenty-sixth of the classical chain [C][3] and an order of magnitude below transport [D][4]. What enters the code is loss during the probe, not discrimination.

## Manufacturing, materials & supply chain
No chip: sensors, objectives and lasers. Three camera vendors appear across every sourced result — Hamamatsu qCMOS in the Harvard/QuEra line [C][G:HAMAMATSU-CAMERA-CONC-2026], Andor (Oxford Instruments) EMCCD at Kyoto [D][1], Teledyne Kinetix in Quantum Machines' stack [C][3] — and no atom-array company makes one, so the sensor is the clearest single point of failure. Export exposure is asymmetric: the machine is caught by ECCN 4A906 (BIS, 2024-09-06) [G][9], the cameras are dual-use instruments outside the 2024 quantum ECCNs.

## Control, readout & I/O burden
Fast imaging removes one term, not the cycle. An atom QEC round is imaging (0.5–1 ms) plus transport (hundreds of µs) plus gates, 1–4.5 ms in total [D][4]; taking imaging to 17.6 µs leaves transport and the classical chain, so the round improves by about a factor of two, not the 30–50× the imaging figures alone suggest. The classical chain is the larger term: 442 µs camera-to-server transfer plus 21–85 µs processing, 460 µs on a 10×10 array [C][3] — twenty-six times the exposure. At 10³ sites the camera link binds; at 10⁴–10⁶ only per-site counting with an on-sensor decision scales.

## Role in the stack
Requires alkaline-earth (Yb/Sr) atoms on the graph record's edge, matching Kyoto's ¹⁷⁴Yb [D][1]. It replaces millisecond imaging [graph] and gives a faster round only with faster transport: the platform's cycle is ~10³× slower than superconducting [D][4] and imaging is about half of it. Clock contribution ~18 µs of readout against a derived clock still set by 800 µs of transport (derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path) — it cuts ~0.5 ms from the 1.3 ms round and leaves transport the largest term. Empty slot nearby: fast non-destructive readout on a full array under reloading.

## Verification (QCVV)
Both are single-lab preprints a week apart, neither replicated. Kyoto's 17.6 µs is imaging alone, with no array size in the abstract [D][1]. USTC's 15 µs is an average probe time, and the 1.7 kHz, 120-round run applied adaptive protection to a 25-site subarray of a 100-qubit array [D][2] — untested where it matters. The precedent is Atom Computing's toric code: suppression survived 90 rounds but vanished once reloading was included, 0.63% against 0.64% per cycle [D][5]. Continuous operation is proven separately — >3,000 qubits over two hours [D][6] — never with microsecond readout.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Kyoto University | Research | JP | First ≤20 µs atom-array imaging, on ¹⁷⁴Yb | [D][1] |
| USTC | Research | CN | 15 µs adaptive probe with sub-µs feed-forward decoding | [D][2] |
| Quantum Machines | Supplier | IL | Sells the classical readout chain | [C][3] |
| Hamamatsu Photonics | Supplier | JP | qCMOS sensor of the main imaging line | [C][G:HAMAMATSU-CAMERA-CONC-2026] |

**Money.** 2025-02-25 · Quantum Machines · Series C · $170 M · closed [C][7][G:QM-SERIESC-2025-02]. 2025-11-06 · DARPA QBI Stage B · programme · up to $15 M per team · Atom Computing and QuEra among eleven [G][13]. 2026-06-16 · Atom Computing · Series C plus a $100 M non-binding CHIPS LOI of 2026-05-21 · $100 M from Third Point, >$300 M total · closed and LOI [C][10][G][8]. Nothing is funded as fast readout: it is instrument spend inside platform budgets, and both defining results came from universities, not the companies that need them.

**Market & supply chain.** The enabling suppliers are camera vendors (Hamamatsu, Andor, Teledyne) and control vendors (Quantum Machines); no fast-atom-readout product exists. Sensor concentration is severe: three vendors, none replaceable in-house. Capturable value sits in the classical chain, which is why the control vendor publishes the benchmarks [C][3]. Pays into G3 and G4, and into G1 where shot rate is throughput.

**IP & standards.** No dated patent family for fast atom-array readout surfaced as of 4 Sep 2026; both results are preprints and the only company on either author list is Yaqumo Inc. [D][1]. No standards body governs sensor choice. The absence of IP is itself a finding: the technique is published, not fenced.

**Roadmaps & track record.** Atom Computing with Microsoft (2025-07 · Magne, 50 logical, €80 M, turn of 2026/27 · being installed) [R][12]. QuEra (2026-06 · Libra 2028, >256 logical · its 2024 roadmap promised 100 logical in 2026 — a two-year slip) [R][11]. Nobody has dated a commitment to ship sub-20 µs readout; the sector's record is a ~2-year slip.

**Strategic reading.** The winner is whichever atom company gets the camera out of the loop, not whichever gets the exposure shortest: the bottleneck measured is a 442 µs frame transfer, not a 17.6 µs probe [C][3]. Camera vendors hold supplier power today and lose it the moment integrated detection arrives. The platform reading is soberer — closing the imaging term moves the atom cycle disadvantage from ~10³× to perhaps ~10²×, which does not settle the architecture argument [D][4].

*Open niche:* neither result states its conditions fully and neither has run under reloading — a matched-conditions harness reporting discrimination infidelity and loss separately, on one array under load, is a referee's job. The second entry is detector-side: per-site photon counting with the decision made in logic rather than after a frame transfer.

## Outlook & open questions
Confirm/demote in 12–24 months: either result reproduced by a second group; sub-20 µs readout inside a live logical-qubit run; readout held under reloading at full array size. Best case 2029: microsecond imaging is standard, the round is transport-limited at a few hundred µs, and loss detection is cheap enough to make erasure conversion routine. Worst case: the numbers hold only on small static subarrays. Open questions: what species USTC used; does adaptive stopping survive on a full array where counting runs everywhere at once; who builds the first sensor with the decision on the die.

## Sources
[1] Yokoyama, Kashimoto, Shibata et al. (Kyoto University, with Yaqumo Inc.), fast ¹⁷⁴Yb atom-array imaging, arXiv:2605.24175v2 (2026-08-24) — https://arxiv.org/html/2605.24175 [G:KYOTO-FASTIMG-2026-08]
[2] Zeng, You, Pan et al. (USTC), "Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor", arXiv:2608.17189 (2026-08-17) — https://arxiv.org/abs/2608.17189 [G:USTC-FASTREADOUT-2026-08]
[3] Quantum Machines, "Classically accelerated readout for neutral atoms" (2026-06) — https://www.quantum-machines.co/resources/blog/classically-accelerated-readout-neutral-atoms-cpu-gpu-readout/ [C]
[4] Bluvstein et al. (Harvard, MIT, QuEra), "Architectural mechanisms of a universal fault-tolerant quantum computer", Nature 649, 39 (2025-11-10); arXiv:2506.20661 — https://www.nature.com/articles/s41586-025-09848-5 [G:HARVARD-LOSS-QEC-2025]
[5] Atom Computing with Microsoft, toric-code memory with continuous reloading, arXiv:2606.04079 (2026-06) — https://arxiv.org/abs/2606.04079 [D]
[6] Continuous operation of a 3,000-qubit atom array, Nature (2025) — https://www.nature.com/articles/s41586-025-09596-6 [D]
[7] Quantum Machines, "Quantum Machines raises $170 million in Series C funding" (2025-02-25) — https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C][G:QM-SERIESC-2025-02]
[8] US Dept of Commerce / NIST, CHIPS letters of intent, nine companies, $2.013 B (2026-05-21) — https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G:CHIPS-LOI-2026-05]
[9] US BIS, interim final rule, "Commerce Control List Additions and Revisions" (2024-09-06), ECCNs 3A901.a, 3A904, 3B904, 4A906 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent [G:BIS-3A901A-CRYOCMOS]
[10] Atom Computing, "Atom Computing raises more than $300 million" (2026-06-16) — https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C][G:ATOM-300M-2026-06]
[11] QuEra, "QuEra announces 2028 fault-tolerant quantum computer" (2026-06) — https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R][G:QUERA-LIBRA-2026]
[12] Novo Nordisk Foundation / QuNorth, "Magne" order from Atom Computing and Microsoft, €80 M (2025-07-17) — https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [G:MAGNE-2025-07]
[13] DARPA, QBI Stage B selection (2025-11-06) — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G:QBI-STAGEB-2025-11]

## Open verification items
USTC's atom species and transition are not stated in the retrievable abstract of arXiv:2608.17189, nor is the detector type or collection NA; the 1.7 kHz / 120-round figure applies to a 25-site subarray of the 100-qubit array [2].
Kyoto's array size is not stated in the retrievable abstract; the 17.6 µs is imaging time alone, not a full readout cycle [1].
Neither fast-readout result has third-party replication, and neither has been run under continuous atom reloading as of 4 Sep 2026.
The claim that scientific cameras fall outside the 2024 quantum ECCNs rests on those ECCNs' own scope [9]; the camera-specific control category is unverified.
Quantum Machines' 460 µs chain figure is self-reported and not independently audited [3].
