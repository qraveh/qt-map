---
id: ro_imgfast
name: Fast (≤ 20 µs) atom-array readout
layer: "6 Readout"
status: emerging
since: 2026
one_line: Sub-20-microsecond fluorescence imaging of atom-array qubits, replacing millisecond exposures and moving readout out of the neutral-atom QEC cycle's critical path.
verdict: Fast imaging takes readout off the critical path but leaves transport and the camera link, so the round improves ~2×, not 30×. Demote if no group shows sub-20 µs readout on a full array under continuous reloading by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Resonant fluorescence imaging resolving each site's state in tens of microseconds instead of the 0.5–1 ms exposure atom arrays have always needed [D][4]. Two August-2026 preprints a week apart define the state of the art: Kyoto's coherent excitation on ¹⁷⁴Yb, 17.6 µs at 99.89(5)% discrimination and 98.80(44)% survival [D][264], and USTC's site-resolved adaptive protection with continuous photon counting, 15 µs average probe [D][469].
c = optical imaging at ~17.6 µs (10⁻⁴·⁷⁵ s), non-destructive, mid-circuit-capable [graph].
e = optical control at room temperature; g = optics only — camera and collection optics, no chip [graph].

## Physics & limits
The floor is a photon budget. Discrimination needs enough detected photons to separate bright from dark above camera read noise, and detected photons are the scattered count times collection efficiency — an NA-0.6 objective collects about a tenth of 4π [D][264]. Every scattered photon carries two recoils, so the heating that ejects the atom scales with the same count that buys the discrimination: survival and fidelity trade through one variable. Both 2026 results therefore attack the count, not the exposure — Kyoto by exciting coherently, halving the heating rate of incoherent schemes [D][264], USTC by stopping the scattering at each site the moment continuous photon counting has decided its state, reaching 4.1×10⁻⁵ discrimination infidelity at 2.1×10⁻⁴ loss [D][469]. What moves the floor is collection: higher NA, cavity collection, photon-counting arrays in place of EMCCD, cooling during the probe.

## Engineering state of the art
| Year | Figure | Who | Tag+Key |
|---|---|---|---|
| 2025-11 | non-destructive readout 0.46% bit-flip, 0.24% loss; imaging 0.5–1 ms | Harvard University | [D][4][G:HARVARD-LOSS-QEC-2025] |
| 2026-08-17 | 15 µs average probe, 4.1×10⁻⁵ infidelity, 1.7 kHz over 120 rounds | USTC | [D][469][G:USTC-FASTREADOUT-2026-08] |
| 2026-08-24 | 17.6 µs imaging, 99.89(5)% discrimination, 98.80(44)% survival | Kyoto University | [D][264][G:KYOTO-FASTIMG-2026-08] |

The dominant term is no longer the exposure: at 17.6 µs the optical step is a twenty-sixth of the classical chain [C][621] and an order of magnitude below transport [D][4]. What enters the code is loss during the probe, not discrimination.

## Manufacturing, materials & supply chain
No chip: sensors, objectives and lasers. Three camera vendors appear across every sourced result — Hamamatsu qCMOS in the Harvard/QuEra line [C][G:HAMAMATSU-CAMERA-CONC-2026], Andor (Oxford Instruments) EMCCD at Kyoto [D][264], Teledyne Kinetix in Quantum Machines' stack [C][621] — and no atom-array company makes one, so the sensor is the clearest single point of failure. Export exposure is asymmetric: the machine is caught by ECCN 4A906 (BIS, 2024-09-06) [G][225], the cameras are dual-use instruments outside the 2024 quantum ECCNs.

## Control, readout & I/O burden
Fast imaging removes one term, not the cycle. An atom QEC round is imaging (0.5–1 ms) plus transport (hundreds of µs) plus gates, 1–4.5 ms in total [D][4]; taking imaging to 17.6 µs leaves transport and the classical chain, so the round improves by about a factor of two, not the 30–50× the imaging figures alone suggest. The classical chain is the larger term: 442 µs camera-to-server transfer plus 21–85 µs processing, 460 µs on a 10×10 array [C][621] — twenty-six times the exposure. At 10³ sites the camera link binds; at 10⁴–10⁶ only per-site counting with an on-sensor decision scales.

## Role in the stack
Requires alkaline-earth (Yb/Sr) atoms on the graph record's edge, matching Kyoto's ¹⁷⁴Yb [D][264]. It replaces millisecond imaging [graph] and gives a faster round only with faster transport: the platform's cycle is ~10³× slower than superconducting [D][4] and imaging is about half of it. Clock contribution ~18 µs of readout against a derived clock still set by 800 µs of transport (derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path) — it cuts ~0.5 ms from the 1.3 ms round and leaves transport the largest term. Empty slot nearby: fast non-destructive readout on a full array under reloading.

## Verification (QCVV)
Both are single-lab preprints a week apart, neither replicated. Kyoto's 17.6 µs is imaging alone, with no array size in the abstract [D][264]. USTC's 15 µs is an average probe time, and the 1.7 kHz, 120-round run applied adaptive protection to a 25-site subarray of a 100-qubit array [D][469] — untested where it matters. The precedent is Atom Computing's toric code: suppression survived 90 rounds but vanished once reloading was included, 0.63% against 0.64% per cycle [D][133]. Continuous operation is proven separately — >3,000 qubits over two hours [D][130] — never with microsecond readout.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Kyoto University | Research | JP | First ≤20 µs atom-array imaging, on ¹⁷⁴Yb | [D][264] |
| USTC | Research | CN | 15 µs adaptive probe with sub-µs feed-forward decoding | [D][469] |
| Quantum Machines | Supplier | IL | Sells the classical readout chain | [C][621] |
| Hamamatsu Photonics | Supplier | JP | qCMOS sensor of the main imaging line | [C][G:HAMAMATSU-CAMERA-CONC-2026] |

**Money.** 2025-02-25 · Quantum Machines · Series C · $170 M · closed [C][412][G:QM-SERIESC-2025-02]. 2025-11-06 · DARPA QBI Stage B · programme · up to $15 M per team · Atom Computing and QuEra among eleven [G][60]. 2026-06-16 · Atom Computing · Series C plus a $100 M non-binding CHIPS LOI of 2026-05-21 · $100 M from Third Point, >$300 M total · closed and LOI [C][138][G][224]. Nothing is funded as fast readout: it is instrument spend inside platform budgets, and both defining results came from universities, not the companies that need them.

**Market & supply chain.** The enabling suppliers are camera vendors (Hamamatsu, Andor, Teledyne) and control vendors (Quantum Machines); no fast-atom-readout product exists. Sensor concentration is severe: three vendors, none replaceable in-house. Capturable value sits in the classical chain, which is why the control vendor publishes the benchmarks [C][621]. Pays into G3 and G4, and into G1 where shot rate is throughput.

**IP & standards.** No dated patent family for fast atom-array readout surfaced as of 4 Sep 2026; both results are preprints and the only company on either author list is Yaqumo Inc. [D][264]. No standards body governs sensor choice. The absence of IP is itself a finding: the technique is published, not fenced.

**Roadmaps & track record.** Atom Computing with Microsoft (2025-07 · Magne, 50 logical, €80 M, turn of 2026/27 · being installed) [R][11]. QuEra (2026-06 · Libra 2028, >256 logical · its 2024 roadmap promised 100 logical in 2026 — a two-year slip) [R][142]. Nobody has dated a commitment to ship sub-20 µs readout; the sector's record is a ~2-year slip.

**Strategic reading.** The winner is whichever atom company gets the camera out of the loop, not whichever gets the exposure shortest: the bottleneck measured is a 442 µs frame transfer, not a 17.6 µs probe [C][621]. Camera vendors hold supplier power today and lose it the moment integrated detection arrives. The platform reading is soberer — closing the imaging term moves the atom cycle disadvantage from ~10³× to perhaps ~10²×, which does not settle the architecture argument [D][4].

*Open niche:* neither result states its conditions fully and neither has run under reloading — a matched-conditions harness reporting discrimination infidelity and loss separately, on one array under load, is a referee's job. The second entry is detector-side: per-site photon counting with the decision made in logic rather than after a frame transfer.

## Outlook & open questions
Confirm/demote in 12–24 months: either result reproduced by a second group; sub-20 µs readout inside a live logical-qubit run; readout held under reloading at full array size. Best case 2029: microsecond imaging is standard, the round is transport-limited at a few hundred µs, and loss detection is cheap enough to make erasure conversion routine. Worst case: the numbers hold only on small static subarrays. Open questions: what species USTC used; does adaptive stopping survive on a full array where counting runs everywhere at once; who builds the first sensor with the decision on the die.

## Sources
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[11] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [R]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[130] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[133] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[138] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[142] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[224] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[264] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [D]
[412] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[469] Xu-Zhao-Qiu Zeng *et al.*, “Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor,” [arXiv:2608.17189](https://arxiv.org/abs/2608.17189), Aug. 2026. [D]
[621] U. Akhouri, “Classically Accelerated Readout for Neutral Atoms with CPU/GPU Integration,” Quantum Machines Blog, Jun. 2026. [Online]. Available: https://www.quantum-machines.co/resources/blog/classically-accelerated-readout-neutral-atoms-cpu-gpu-readout/ [C]

## Open verification items
USTC's atom species and transition are not stated in the retrievable abstract of arXiv:2608.17189, nor is the detector type or collection NA; the 1.7 kHz / 120-round figure applies to a 25-site subarray of the 100-qubit array [469].
Kyoto's array size is not stated in the retrievable abstract; the 17.6 µs is imaging time alone, not a full readout cycle [264].
Neither fast-readout result has third-party replication, and neither has been run under continuous atom reloading as of 4 Sep 2026.
The claim that scientific cameras fall outside the 2024 quantum ECCNs rests on those ECCNs' own scope [225]; the camera-specific control category is unverified.
Quantum Machines' 460 µs chain figure is self-reported and not independently audited [621].
