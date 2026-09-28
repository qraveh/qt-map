---
id: cx_reload
name: Continuous atom reload (reservoir + conveyor)
layer: "4 Connectivity / transport"
status: demonstrated
since: 2024
one_line: "A continuously fed atom reservoir (optical-lattice conveyor belts from a distant MOT, a cavity-enhanced lattice or a molasses-stopped beam) from which tweezers extract fresh atoms into the array while the stored qubits keep their coherence."
verdict: "Demonstrated as an enabler: Harvard/MIT held over 3,000 atoms for over 2 h and sort 15,000 qubits/s, the authors' own sufficiency figure for a ~10,000-qubit processor; as of 2026-09-26 the largest published QEC run with reservoir reloading found is 64 atoms, and the register's only carrier has no entangling result."
updated: 2026-09-26
---

MOT = magneto-optical trap; AOD = acousto-optic deflector; DD = dynamical decoupling (XY16 = its 16-pulse sequence); T2 / T2* = echo / Ramsey coherence time; ³P₀ = metastable clock state of Sr and Yb; QEC = quantum error correction; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A tweezer array is normally loaded once and sorted by AOD moves — Caltech's 6,100 atoms fill about half of ~12,000 sites [D][138] — and then only loses atoms. This technology adds a reservoir refilled during the computation, from which tweezers extract fresh atoms without disturbing stored qubits. Feeds: lattice conveyor belts from a MOT 0.5 m away (Harvard/MIT, Rb) [D][144]; a repetitively filled cavity-enhanced lattice (Atom Computing, ¹⁷¹Yb) [D][505]; a molasses-stopped reservoir several hundred µm from the qubits (Princeton, ¹⁷¹Yb) [D][506].
Attributes: natural carrier; transport mobility; removes loss; optical control at room temperature; optics manufacturing.

## Physics & limits
N atoms of lifetime τ are lost at N/τ: the first loss comes after ~τ/N, and one lifetime leaves e⁻¹ ≈ 37 % of the array [S]. At Harvard's ~60 s storage lifetime [D][144], 3,000 atoms lose 50 per second; at Caltech's 23 min [D][138], the first of 10⁴ atoms goes after ~0.14 s [S]. Operations lose more: entangling errors and readout join trap lifetime as loss sources [D][144], and loss is "a significant fraction of all errors" [D][506]. Chiu et al. estimate that 15,000 rearranged qubits/s replenish ~10,000 qubits at ~99.5 % gate fidelity and 1 ms per layer [S][144] — 1.5 × 10⁻³ replacements per qubit per layer, ~1 % of them due to a 60 s lifetime [S]. Cryogenic lifetimes of 5,000–6,000 s [D][507][D][146] remove only that 1 %.
Light constrains refilling: MOT and imaging light is near-resonant for Rb qubits, so Harvard adds distance, a differential pumping tube tilted ~4° and a 1529 nm light shift of 5P₃/₂ that suppresses scattering >10⁴-fold [D][144]. The Yb ³P₀ qubit is isolated from cooling and imaging light [D][506]; stored ⁸⁸Sr is shelved in ³P₀ (13 s lifetime) with the MOT repumper off [D][259].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-06 | Tweezers at ~4 K, lifetime >6,000 s | Institut d'Optique | [D][507] |
| 2024-01 | 1,225 Yb sites, 99 % filled from a lattice reservoir | Atom Computing | [D][505] |
| 2024-02 | >1,000 Sr atoms, ~130 refilled per 2.5 s cycle, >1.5 h | MPQ | [D][259] |
| 2024-03 | >6,100 atoms, single load, 23 min lifetime | Caltech | [D][138] |
| 2025-06 | 7.3 × 10⁴ atoms/s extracted; 1 ms per replacement | Princeton | [D][506] |
| 2025-09 | 3 × 10⁵ atoms/s into tweezers; >3 × 10⁴ qubits/s; >3,000 atoms for >2 h | Harvard/MIT | [D][144] |
| 2026-04 | 1,024-atom defect-free arrays at 4 K, ~5,000 s | Lim et al. | [D][146] |
| 2026-06 | Toric code, 90 cycles with reservoir reloading | Atom Computing/Microsoft | [D][148] |

Harvard/MIT sort 15,000 qubits/s in 600-qubit batches [D][144], one per ~40 ms [S]; one of six 540-site storage subarrays is refilled every ~80 ms [D][144], so each atom is replaced about every 0.5 s — 6.75 × 10³ atoms/s over >2 h, the ~5 × 10⁷ reported [S]. The run proves throughput and 99.3 % filling [D][144], not hours-long qubit survival [S].

## Manufacturing, materials & supply chain
Vacuum and optics, not a fabricated part: a second MOT chamber behind a differential pumping tube and two lattice stages, ~39 cm and ~17 cm, delivering ~2.5 × 10⁶ atoms every ~150 ms [D][144]; Atom Computing's MOT sits 30 cm below its array [D][148]. Delivery, ~1.7 × 10⁷ atoms/s, exceeds tweezer loading ~50-fold, so extraction bounds the flux [S]. Optical access to the science region, shared with tweezers, Rydberg beams and imaging, is the scaling limit [S].

## Control, readout & I/O burden
Three synchronised loops — reservoir delivery (~150 ms), batch extraction, imaging and sorting, storage refill (~80 ms) — interleave with XY16 DD on stored qubits [D][144]. Every fresh atom is imaged: 25–50 camera frames and rearrangement solutions per second [S]. Yb needs no shield; Princeton prepares 30 complete arrays per second [D][506].

## Role in the stack
Slot 4 of Rydberg tweezer array — alkali (Rb/Cs) and Rydberg tweezer array — alkaline-earth (Yb/Sr), erasure-native, beside cx_aod. It **requires** ct_laser (lattice and tweezer light) and fab_optics (second MOT region, conveyor optics, vacuum). It **replaces** one-shot loading (the edge from cx_aod), though every machine keeps AOD tweezers for extraction and sorting. The gap ledger holds: AOD moves span hundreds of micrometres in 0.4–1.6 ms; a conveyor carries a ~10⁶-atom reservoir half a metre [D][144]. Filed by function: a lattice reservoir or a molasses-stopped beam does the same job. Conflicts with alkali (scattered MOT light) and ae_atom (repumper depleting stored atoms) are mitigated (2025-09; 2024-02). It **provides** reload flux and run length: >2 h, >5 × 10⁷ atoms through 3,000 sites [D][144].
Reload closes the loop erasure conversion opens: converting 98 % of ¹⁷¹Yb errors to erasures raised the simulated threshold from 0.937 % to 4.15 % [S][8]; Atom Computing corrected on average 1.8 lost atoms across 24 logical qubits [D][149]; delayed-erasure decoding uses loss of unknown timing [S][508]. Each converted error is a hole that mid-circuit imaging locates and the reservoir fills [D][148]; without reload, conversion shortens the run.
Register: one machine, harvard-continuous-3000 (Harvard/MIT, primary, demonstrated Aug 2026), cell ✅ verified (arXiv:2506.20660, Fig. 1a); two-qubit error n/a — an enabler without an entangling result.

## Evidence — how the numbers were measured
The discriminating test is stored-qubit coherence with reload on versus off. Harvard (Rb, XY16): T2 1.34(4) s reference, 1.15(3) s with the MOT, 1.09(3) s adding imaging and shielding [D][144] — 14–19 % lower, ~4–5σ [S]. Princeton (Yb): echo T2 5.4(9) versus 7(1) s, T2* 0.73(2) versus 0.69(2) s, unchanged within 1.5σ [D][506]. No gate fidelity on stored qubits during reload is published, as of 2026-09-26. The one logical figure: 0.63(3) % and 0.64(4) % error per cycle over up to 90 cycles with reloading, on 32- and 64-atom toric codes, cycle time unstated [D][148]. Flux is quoted as atoms, initialised or sorted qubits, a tenfold spread; the Atlas uses initialised qubits/s.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Harvard University / MIT | research | US | Two-stage lattice conveyor, 3,000-atom continuous array | [D][144] |
| QuEra Computing | developer | US | Libra roadmap with a reloading reservoir | [R][509] |
| Atom Computing (with Microsoft) | developer | US | Lattice reservoir; toric code with reloading | [D][505][D][148] |
| Princeton University | research | US | Yb metastable reservoir | [D][506] |
| MPQ | research | DE | Refilled Sr lattice array | [D][259] |
| Caltech | research | US | Single-load reference array | [D][138] |

**Money.** No dated financial item is specific to continuous reloading as of 2026-09-26.

**Market & supply chain.** No separate market: makers build reservoirs from the laser, modulator and vacuum classes they already buy. The technology pays into G1, G3 and G7 by lifting the depth bound.

**IP & standards.** No patent count was checked; no standard defines how reload flux or coherence during reload is reported, as of 2026-09-26.

**Roadmaps & track record.** (for 2028 · QuEra Libra · >10,000 physical, 256 logical qubits at 10⁻⁶, fresh qubits loaded "mid-circuit from Libra's reloading reservoir") [R][509]; Chiu et al.: ~99.9 % fidelity with 80,000 qubits/s could run several hundred surface-code logical qubits at 10⁻⁸ [S][144]. Flux is ahead of plan; integration is behind — gates plus reload are published only at 64 atoms.

**Strategic reading.** Reload makes loss the cheapest error to correct, as both atom architectures' QEC plans assume. The flux record comes from a group whose senior authors co-founded QuEra [D][144]; only Atom Computing's reservoir has run inside QEC. If coherence and gate fidelity hold under reload at 10³–10⁴ atoms, depth stops being the atom platform's weakness; if not, runs stay bounded by τ/N.

## Outlook & open questions
Confirm if, by 2027-12-31, a published experiment runs gates or QEC rounds on ≥1,000 atoms while reloading, with logical error flat across reload events; demote if QuEra's 2028 reservoir has no such precursor by then. Open questions. (1) Does flux scale with array area, or do extraction and imaging cap it? (2) What gate-fidelity tax do stored qubits pay beside an active preparation zone? (3) What does re-cooling fresh atoms cost in time? (4) Can a conveyor share optical access with a zoned architecture at 10⁴ sites? (5) At 5,000–6,000 s cryogenic lifetimes, is operation-induced loss the whole budget?

## Sources

[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[138] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[144] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[146] D. Lim *et al.*, “Defect-free arrays at the thousand-atom scale in a 4-K cryogenic environment,” *PRX Quantum*, vol. 7, Art. no. 033032, Apr. 2026, doi: [10.1103/45t1-vl5y](https://doi.org/10.1103/45t1-vl5y). [arXiv:2604.07205](https://arxiv.org/abs/2604.07205). [D]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[149] B. W. Reichardt *et al.*, “Fault-tolerant quantum computation with a neutral atom processor,” [arXiv:2411.11822](https://arxiv.org/abs/2411.11822), Nov. 2024. [D]
[259] F. Gyger *et al.*, “Continuous operation of large-scale atom arrays in optical lattices,” *Phys. Rev. Research*, vol. 6, no. 3, Art. no. 033104, Feb. 2024, doi: [10.1103/PhysRevResearch.6.033104](https://doi.org/10.1103/PhysRevResearch.6.033104). [arXiv:2402.04994](https://arxiv.org/abs/2402.04994). [D]
[505] M. A. Norcia *et al.*, “Iterative assembly of ¹⁷¹Yb atom arrays with cavity-enhanced optical lattices,” *PRX Quantum*, vol. 5, no. 3, Art. no. 030316, Jan. 2024, doi: [10.1103/PRXQuantum.5.030316](https://doi.org/10.1103/PRXQuantum.5.030316). [arXiv:2401.16177](https://arxiv.org/abs/2401.16177). [D]
[506] Y. Li, Y. Bao, M. Peper, C. Li, and J. D. Thompson, “Fast, continuous and coherent atom replacement in a neutral atom qubit array,” [arXiv:2506.15633](https://arxiv.org/abs/2506.15633), Jun. 2025. [D]
[507] K.-N. Schymik *et al.*, “Single Atoms with 6000-Second Trapping Lifetimes in Optical-Tweezer Arrays at Cryogenic Temperatures,” *Phys. Rev. Appl.*, vol. 16, no. 3, Art. no. 034013, Jun. 2021, doi: [10.1103/PhysRevApplied.16.034013](https://doi.org/10.1103/PhysRevApplied.16.034013). [arXiv:2106.07414](https://arxiv.org/abs/2106.07414). [D]
[508] G. Baranes *et al.*, “Leveraging Qubit Loss Detection in Fault-Tolerant Quantum Algorithms,” *Phys. Rev. X*, vol. 16, no. 1, Art. no. 011002, Jan. 2026, doi: [10.1103/ycwc-3myc](https://doi.org/10.1103/ycwc-3myc). [arXiv:2502.20558](https://arxiv.org/abs/2502.20558). [S]
[509] QuEra Computing, “Our Quantum Roadmap,” Sep. 15, 2026. [Online]. Available: https://www.quera.com/our-quantum-roadmap [R]

## Open verification items
- 2026-09-26: The Harvard/MIT batch cadence is derived from flux and batch size, not quoted; figures were read from arXiv:2506.20660 (HTML, v2 of 2026-05-21), not the Nature version.
- 2026-09-26: Atom Computing's 30 cm MOT distance and per-cycle logical errors come from an automated read of arXiv:2606.04079 v1; no journal version, author count or syndrome-cycle time found.
- 2026-09-26: Affiliations of Lim et al. (arXiv:2604.07205; the dossier says Pasqal/Institut d'Optique), Schymik et al. and the MPQ authors were not shown on the arXiv abstract pages.
- 2026-09-26: Caltech's lifetime is the abstract's 23 min; the dossier's 22.9(1) min and 51.2 % fill were not checked in the full text.
- 2026-09-26: No patent search was run; the register lists only harvard-continuous-3000 here — Atom Computing's toric-code machine is a candidate second carrier.
