---
id: g_ryd
name: Rydberg-blockade CZ
layer: "3 Gate mechanism"
status: demonstrated
since: 2010
one_line: "Global laser pulses drive neighbouring tweezer-trapped atoms to a Rydberg state whose interaction blocks double excitation, giving a deterministic 270 ns CZ."
verdict: "Best natural-carrier entangler by speed; 99.854% raw as of April 2026, but the standard scheme sits within ~0.05% of its own ceiling and its residual error is atom loss."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

Two atoms ~2 µm apart in tweezers are driven on the qubit-to-Rydberg transition by one beam covering both. Because a doubly-excited pair repels through a van der Waals shift $V=C_6/R^6$ far larger than the drive, double excitation is pushed out of resonance and the pair acquires a phase set by how many atoms started in the coupled state — a controlled-phase gate. Jaksch, Cirac, Zoller, Rolston, Côté and Lukin proposed it in 2000 [D][1]; blockade between two atoms was seen in 2009 (~58% fidelity) [P][2], with the first gates and a CNOT in 2010. Levine et al. replaced the three-pulse addressed sequence with a two-pulse global time-optimal CZ in 2019 (97.4%) [D][3] — the form every leading group still runs, and why the gate needs no per-qubit control line.

Attributes (technology graph). **a — carrier affinity:** fully natural; the gate adds no fabricated structure to the qubit. **b — characteristic time:** $10^{-6.6}$ s ≈ 250 ns, deterministic rather than heralded. **c — readout:** not set here; inherited from the atom and imaging nodes. **d — mobility:** connectivity by physically transporting atoms between gate zones, not fixed couplers. **e — control @ placement:** optical, generated entirely at room temperature. **f — error structure as the code sees it:** atom loss, leakage out of the qubit space, coherent over/under-rotation. **g — manufacturing:** optics, not lithography.

## Physics & limits

Three scales set everything. The drive $\Omega$ (Harvard: peak $2\pi\times17$ MHz, two-photon 420 + 1015 nm at 7.8 GHz intermediate detuning, Rb $53S_{1/2}$) fixes the gate at 270 ns [D][4][D][5]; the blockade shift must satisfy $V\gg\hbar\Omega$, residual double excitation costing roughly $(\Omega/V)^2$. The Rydberg lifetime (tens of µs at $n\approx53$, blackbody-limited) costs the Rydberg dwell time divided by it. Raising $\Omega$ cuts decay and raises leakage, so the optimum is shallow: a 2026 review adds spontaneous Rydberg emission (0.05–0.1%), laser phase noise (0.1–0.2%) and thermal motion (~0.1%) and concludes the standard blockade CZ has a "physical limit of 99.9%" absent new mechanisms such as Förster-resonance gates [P][2].

The measured budget agrees in shape but not in villain. In the April 2026 Harvard result the largest single term is **atom loss, 0.087(5)% per gate, about 60% of the total error**, with leakage to other hyperfine levels 0.008(1)% per atom per gate; the authors assign the remainder to ground-Rydberg coherence ($T_2^*$), intermediate-state scattering and unwanted coupling to a nearby Rydberg level, and project 99.9–99.95% from better $T_2^*$, suppression of that coupling and more laser power [D][4]. That makes the gate structurally interesting: its dominant failure is *detectable* — the atom is gone from the image — so it converts to an erasure, not an unlocated Pauli. Loss-post-selection lifts the same data from 99.854(4)% to 99.941(3)% [D][4], and in the 448-atom architecture >80% of leakage events are atom loss, used as "supercheck" information in decoding [D][5][G:HARVARD-LOSS-QEC-2025].

What moves the floor: single-photon UV excitation, with no intermediate state to scatter from — the Yb and Sr route [D][6][D][7]; spectrally clean lasers against servo-bump phase noise at $\Omega$; ground-state cooling against Doppler and position spread; and new gate physics (Förster resonance, modulated off-resonant driving, circular Rydberg states) [P][2]. None is demonstrated above 99.9% raw as of 3 Sep 2026.

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2009 | ~58% two-atom entanglement via blockade | Wisconsin (Saffman/Walker) | [P][2] |
| 2019 | 97.4% CZ, two-pulse global scheme | Harvard/MIT (Levine) | [D][3] |
| 2023 | 99.5% CZ, parallel across an array | Harvard/MIT/QuEra (Evered) | [D][8] |
| 2024-07 | 99.71(5)% CZ, Sr, leakage-corrected | Caltech (Endres) | [D][7] |
| 2024-11 | 99.72(3)% post-selected / 99.40(3)% raw, ¹⁷¹Yb nuclear spin | Atom Computing | [D][6] |
| 2026-04 | **99.854(4)% raw / 99.941(3)% loss-post-selected**, stable 10 h | Harvard | [D][4] |
| 2026 | 99.2% global two-qubit on a 260-physical-qubit product | QuEra Gemini | [C][9] |

Best-versus-typical is the story: the record comes from ~8 sparsely spaced gate sites at 20–30 Hz [D][4], the shipped figure is 99.2% global on 260 qubits [C][9], the largest array under fault-tolerant control is 448 atoms [D][5], and arrays of 6,100 and 11,000 atoms exist without gates at these fidelities [D][10][D][11].

## Manufacturing, materials & supply chain

There is no wafer; the manufacturing surface is the laser and beam-steering chain. Alkali two-photon excitation needs a fibre-amplified 1013–1015 nm source of tens of watts plus a frequency-doubled 420 nm beam; Yb/Sr need a single ~300–320 nm UV source; all need phase noise suppressed near the Rabi frequency, plus acousto-optic deflectors and spatial light modulators for placement. Yield and uniformity become intensity and phase homogeneity across the array; Harvard's 10-hour run drifted mainly through Rydberg laser power and pointing [D][4]. The vendor pool for narrow-linewidth high-power lasers, UV sources, AODs and SLMs is small — TOPTICA, M Squared, Coherent, AA Opto-Electronic, Gooch & Housego, Hamamatsu, Meadowlark are the usual names — but no dated procurement disclosure ties a machine to a supplier (see Open verification items). Export control runs through the US BIS quantum controls of September 2024 (ECCN 3A901 and related) and Category 6 laser entries; which applies to a 10 W 1013 nm amplifier is unsettled in any public ruling found.

## Control, readout & I/O burden

The gate is *global*: one beam pair entangles every blockaded pair at once, so per-qubit control lines scale as O(1), not O(N). The cost is optical power — holding $2\pi\times17$ MHz over $N$ atoms scales power linearly in $N$ — and steering bandwidth, since SLM/AOD refresh near 10 MHz is judged insufficient above ~$10^4$ qubits. At $10^3$ nothing breaks; at $10^4$ power and steering bind; at $10^6$ multi-core optical interconnects are required and undemonstrated. The gate's own control latency is sub-µs, but it sits inside a round dominated by ~0.8 ms of transport between gate layers and ~0.5 ms imaging, giving measured QEC rounds of ~1–4.5 ms [D][5][S][12]; the compensating theory is transversal gates with correlated decoding, keeping syndrome rounds constant per logical gate [S][13].

## Role in the stack

The gate serves both neutral-atom paths — alkali (Rb/Cs: Harvard/MIT, QuEra, Pasqal, Infleqtion, Google) and alkaline-earth (Yb/Sr: Atom Computing/Microsoft, Princeton, Caltech). It requires an atom in a tweezer plus the laser and deflector chain, and provides the entangling channel every atom-based code consumes; it has no in-platform replacement at comparable fidelity, so the switching price is the platform itself. Off-diagonal reading: a *natural, unfabricated* carrier gets a sub-microsecond deterministic entangler where trapped ions pay 10–100 µs — hence the platform's clock problem lives in imaging and transport, not the gate. Derived clock = sum of the syndrome round (gates 1×10⁻⁶ s, transport 8×10⁻⁴ s, 1Q 1×10⁻⁵ s, readout 5×10⁻⁴ s) ≈ **1.3 ms** on both atom paths, of which the gate is 0.08%. Neighbouring empty slots: sub-100 µs non-destructive array readout, and a blockade gate whose dominant error is not atom loss.

## Verification (QCVV)

The 2026 record uses echo randomized benchmarking and symmetric stabilizer benchmarking on ~8 sparse gate sites [D][4]; Atom Computing used Clifford and symmetric-subspace RB with >200 CZ gates per circuit [D][6]; Caltech built a fidelity-response theory and quotes 0.9971(5) *downward-corrected for leakage* [D][7]. What these miss: loss-post-selection removes 60% of the error, so 99.941% is not a circuit-level number and must not be set against a raw superconducting figure; sparse-site benchmarking misses dense-array crosstalk and next-nearest-neighbour blockade error; and none measures the gate *inside* a transport-and-image cycle, where re-trapping and heating act. Conflict: the August 2026 review tabulates a 2025 USTC CZ of 99.84% [P][2] that no primary source corroborates, so this brief uses Harvard's 99.854(4)% [D][4]. Note also three conventions behind three headline numbers — Atom Computing's 99.72/99.40 is post-selected/raw [D][6], Caltech's is leakage-corrected [D][7], Harvard's is raw plus post-selected [D][4].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Harvard/MIT (Lukin, Greiner, Vuletić) | research | US | Hold the CZ record and the 448-atom architecture | [D][4][D][5] |
| QuEra | developer | US | Commercialises that line; Gemini ships 99.2% two-qubit | [C][9][C][G:QUERA-230M-2025] |
| Atom Computing | developer | US | ¹⁷¹Yb nuclear spin, single-photon excitation; builds Magne | [D][6][C][G:ATOM-300M-2026-06] |
| Microsoft | integrator | US | Logical layer on Atom hardware; co-sells Magne | [C][G:MAGNE-2025-07] |
| Pasqal | developer | FR | Rb arrays, analog and digital; SPAC-listed Aug 2026 | [P][G:PASQAL-SPAC-2026-08] |
| Infleqtion | developer | US | Cs arrays, logical qubits with loss correction | [C][G:INFLEQTION-NYSE-2026-02] |
| Caltech (Endres) | research | US | Sr gates, erasure excision, benchmarking theory | [D][7] |
| Princeton (Thompson) | research | US | Metastable Yb erasure conversion on this gate | [D][14] |
| Google Quantum AI | developer | US | Neutral-atom track opened under Adam Kaufman | [C][G:GOOGLE-ATOMS-2026-03] |
| DARPA | funder | US | QBI Stage B includes Atom Computing and QuEra | [G:QBI-STAGEB-2025-11] |
| US Dept of Commerce | funder | US | $100 M CHIPS LOIs to Atom Computing and Infleqtion | [G:CHIPS-LOI-2026-05] |
| QuNorth (EIFO + Novo Nordisk Fdn) | buyer | DK | Ordered Magne, 1,225 physical / 50 logical | [C][G:MAGNE-2025-07] |

**Money.**
- 2025-07-17 · QuNorth · order (Magne, from Atom Computing/Microsoft) · €80 M · EIFO + Novo Nordisk Foundation · ordered [C][G:MAGNE-2025-07]
- 2025-09-09 · QuEra · financing round · $230 M+ · Google, SoftBank Vision Fund 2, NVentures · closed [C][G:QUERA-230M-2025]
- 2025-11-06 · Atom Computing, QuEra · DARPA QBI Stage B · up to $15 M each · DARPA · selected [G:QBI-STAGEB-2025-11]
- 2026-02-17 · Infleqtion · IPO (NYSE: INFQ) · >$550 M gross · SPAC · closed [C][G:INFLEQTION-NYSE-2026-02]
- 2026-03-24 · Google · neutral-atom hardware programme · amount undisclosed · internal · announced [C][G:GOOGLE-ATOMS-2026-03]
- 2026-05-21 · Atom Computing, Infleqtion · CHIPS letters of intent · $100 M each, of $2.013 B to nine companies · US Dept of Commerce · LOI, non-binding [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · Series C plus LOI · $100 M equity, >$300 M cumulative · Third Point · closed + LOI [C][G:ATOM-300M-2026-06]
- 2026-08-28 · Pasqal · SPAC completion (Nasdaq: PSQL) · ~$360 M cash; 2025 revenue €16.5 M · closed [P][G:PASQAL-SPAC-2026-08]

**Market & supply chain.** What is sold is systems, not gates: Magne prices 1,225 physical / 50 logical qubits at €80 M, roughly €65 k per physical qubit [C][G:MAGNE-2025-07]; Gemini packages 260 physical qubits at 1 shot/second [C][9]. The enabling-equipment pool — high-power 1013 nm amplifiers, UV sources, AODs, SLMs — is narrow enough that one vendor's lead time can gate a machine build, though it is shared with atomic clocks and cold-atom sensing. G1 (analog simulation) and G5 (optimisation) pay for atom arrays today; the gate fidelity discussed here is bought almost entirely for G3 (early fault tolerance) and, through Magne and Libra, G4. G6 (networking) has no demonstrated atom-to-atom photonic link at this scale.

**IP & standards.** No dated patent-family count from a named database was found for Rydberg-gate IP, so none is asserted. Open stacks: QuEra's Bloqade, Pasqal's Pulser, Infleqtion's Superstaq, with AWS Braket the named delivery channel for QuEra's 2028 system [C][G:QUERA-LIBRA-2026]; no gate-level standard or consortium specific to Rydberg CZ exists as of 3 Sep 2026.

**Roadmaps & track record.** QuEra (promised 2024-01 · 100 logical qubits in 2026 · not delivered; superseded 2026-06 by Libra, >256 logical in 2028 — a two-year slip) [C][G:QUERA-LIBRA-2026]. Atom Computing/Microsoft (promised 2025-07 · Magne, 50 logical, turn of 2026/27 · being installed as of 3 Sep 2026) [C][G:MAGNE-2025-07]. Pasqal (promised 2024-03 · 10,000 physical in 2026 · slipped to 2028; 100 logical 2029) [C][G:PASQAL-SPAC-2026-08]. Infleqtion (promised 2025 · 30 logical in 2026 · unverified as of 3 Sep 2026) [C][15]. Judgment: Harvard/MIT's device claims have survived replication and are the most credible; Atom Computing has a customer, a price and a delivery date, the strongest commercial commitment here; QuEra and Pasqal have each slipped a headline number by two years, so their 2028–29 dates read as intentions.

**Strategic reading.** If raw fidelity crosses 99.9% while loss stays erasure-convertible, neutral atoms reach fault tolerance without a wiring problem: platform vendors and laser suppliers win, and the superconducting camp's argument that only cryogenic integration scales loses. If it stalls at 99.85%, the millisecond cycle leaves atoms as the analog-simulation and optimisation platform while ions and superconductors take fault tolerance. There is no substitution threat *within* the platform — every neutral-atom company runs this gate — making the ceiling a sector risk, not a company risk, and giving these laser suppliers more bargaining power than their revenue suggests.

*Open niche:* the three headline numbers here use three conventions (raw, loss-post-selected, leakage-corrected), and no neutral party publishes a protocol reporting all three from one dataset. A small QCVV house could own exactly that: an erasure-aware two-qubit benchmarking primitive separating coherent error, leakage and loss, plus the translation rule that stops a post-selected atom number being compared with a raw superconducting one — a standards-shaped gap, not a hardware one, and specifying it needs no machine access.

## Outlook & open questions

Confirm/demote milestones for 12–24 months: (1) a **raw** CZ ≥99.9% in a dense array by 2027-09 confirms the review's ceiling was engineering, not physics; failure demotes the gate to saturated; (2) Magne accepted at QuNorth with 50 logical qubits by mid-2027; (3) a >50-round below-threshold memory run with continuous reloading showing Λ>2 — the Atom/Microsoft 90-round toric-code run lost its suppression once reloading was included [D][16]; (4) a CZ fidelity measured *inside* a transport-and-image QEC cycle. Best case by 2029: 99.95% raw, loss converted to erasures, Libra-class 256-logical machines on a cloud channel. Worst case: 99.85% raw persists, the millisecond cycle stays, atoms hold G1/G5 and cede G3/G4.

Open questions. Does the loss channel scale with array density and transport, or is 0.087% per gate a floor set by trap depth? Can single-photon UV excitation recover the phase-noise and scattering terms without new UV-induced loss? Is Förster-resonance or modulated-driving physics real above 99.9%? Does erasure conversion survive at circuit level, where a decoder must locate losses inside a 1 ms budget? Watch for a raw record without post-selection, and whether Google's atom track publishes a gate before 2027.

## Sources

[1] Jaksch *et al.*, “Fast quantum gates for neutral atoms,” *Phys. Rev. Lett.*, vol. 85, Art. no. 2208, 2000. [Online]. Available: https://arxiv.org/abs/quant-ph/0004038 [D]
[2] J. Wang, Z. Wang, L. Li, F. Wang, S. Liang, and K. Yan, “Neutral Atom Quantum Computing: Principles, Routes, Progress, and Challenges,” [arXiv:2608.05010](https://arxiv.org/abs/2608.05010), Aug. 2026. [P]
[3] H. Levine *et al.*, “Parallel Implementation of High-Fidelity Multiqubit Gates with Neutral Atoms,” *Phys. Rev. Lett.*, vol. 123, no. 17, Art. no. 170503, Oct. 2019, doi: [10.1103/PhysRevLett.123.170503](https://doi.org/10.1103/PhysRevLett.123.170503). [arXiv:1908.06101](https://arxiv.org/abs/1908.06101). [D]
[4] S. J. Evered *et al.*, “High-fidelity entangling gates and nonlocal circuits with neutral atoms,” [arXiv:2604.25987](https://arxiv.org/abs/2604.25987), Apr. 2026. [D]
[5] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[6] J. A. Muniz *et al.*, “High-fidelity universal gates in the ¹⁷¹Yb ground state nuclear spin qubit,” [arXiv:2411.11708](https://arxiv.org/abs/2411.11708), Nov. 2024. [D]
[7] R. B.-S. Tsai, X. Sun, A. L. Shaw, R. Finkelstein, and M. Endres, “Benchmarking and linear response modeling of high-fidelity Rydberg gates,” [arXiv:2407.20184](https://arxiv.org/abs/2407.20184), Jul. 2024. [D]
[8] S. J. Evered *et al.*, “High-fidelity parallel entangling gates on a neutral-atom quantum computer,” *Nature*, vol. 622, no. 7982, pp. 268–272, Oct. 2023, doi: [10.1038/s41586-023-06481-y](https://doi.org/10.1038/s41586-023-06481-y). [arXiv:2304.05420](https://arxiv.org/abs/2304.05420). [D]
[9] QuEra Computing Inc., “Gemini-Class Gate-Model Quantum Computer.” [Online]. Available: https://www.quera.com/gemini [C]
[10] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[11] Y. Wang *et al.*, “Trapping 11,000 Atoms in a Tweezer Array Generated by a Single Metasurface,” [arXiv:2606.02715](https://arxiv.org/abs/2606.02715), Jun. 2026. [D]
[12] H. Zhou *et al.*, “Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays,” *Proc. 52nd Annu. Int. Symp. Comput. Archit. (ISCA)*, 2025, doi: [10.1145/3695053.3731039](https://doi.org/10.1145/3695053.3731039). [arXiv:2505.15907](https://arxiv.org/abs/2505.15907). [S]
[13] H. Zhou *et al.*, “Low-Overhead Transversal Fault Tolerance for Universal Quantum Computation,” *Nature*, vol. 646, no. 8084, pp. 303–308, 2025, doi: [10.1038/s41586-025-09543-5](https://doi.org/10.1038/s41586-025-09543-5). [arXiv:2406.17653](https://arxiv.org/abs/2406.17653). [S]
[14] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[15] L. Roady, “Infleqtion Unveils New Architecture to Accelerate Its Quantum Computing Roadmap To Achieve 1000 Logical Qubits by 2030,” Infleqtion, Sep. 17, 2025. [Online]. Available: https://infleqtion.com/infleqtion-unveils-new-architecture-to-accelerate-its-quantum-computing-roadmap-to-achieve-1000-logical-qubits-by-2030/ [C]
[16] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]

## Open verification items

- The August 2026 review [2] tabulates a 2025 USTC CZ fidelity of 99.84%; no primary source corroborates it and a targeted search returned nothing. Treated as unverified; the record used here is Harvard's 99.854(4)% of 2026-04 [4].
- Gate duration: 270 ns is the value given in [5]; the April 2026 record paper gives peak Rabi $2\pi\times17$ MHz but its gate duration is not extractable from the text consulted, so both are assumed to be the same scheme.
- Named laser/AOD/SLM suppliers for any specific neutral-atom machine: no dated procurement disclosure found; the vendor names in Manufacturing are the field's usual pool, not a sourced supply chain.
- Export-control classification of high-power 1013 nm Rydberg-laser subsystems (US BIS quantum ECCNs vs Category 6 laser entries): no public ruling found.
- Caltech Sr full error budget and the upgrades claimed to reach >0.999: only the abstract value 0.9971(5), leakage-corrected, is used; the full text was not consulted.
- QuEra Gemini: no availability date, deployment site or price disclosed on the product page.
