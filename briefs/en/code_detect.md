---
id: code_detect
name: Error-detection codes ([[4,2,2]], d = 2 surface, iceberg, spacetime)
layer: "7 Code"
status: demonstrated
since: 2017
one_line: "Codes that flag any single fault and discard the run instead of correcting it: [[4,2,2]], the distance-2 surface code, the [[k+2,k,2]] iceberg code and spacetime checks on Clifford circuits."
verdict: "Detection lifts post-selected circuit fidelity up to 236× above the bare circuit, at an acceptance that decays exponentially with circuit volume and with no distance to scale. The register's {{N_T_CODE_DETECT_MACHINES_W}} carriers are all filed for detection runs; the ion machines, where the largest runs live, carry it only as an alternate to their high-rate codes."
updated: 2026-09-30
---

[[n,k,d]] = n physical qubits carrying k logical qubits at distance d; acceptance = fraction of runs kept after post-selection; Λ = error-suppression factor per code-distance step; RB = randomised benchmarking; CZ = controlled-Z gate; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A distance-2 stabiliser code turns any single-qubit error into a non-trivial syndrome but cannot locate it, so the run is discarded (post-selected), not repaired. Members: [[4,2,2]], checks XXXX and ZZZZ; the distance-2 rotated surface code [[4,1,2]]; Quantinuum's iceberg code [[k+2,k,2]] [D][673]; and spacetime codes, which treat a Clifford circuit's outcome bits as a code and add checks that catch faults anywhere in it [S][710]. Fault-tolerant detection dates from 2017: [[4,2,2]] on trapped ions [D][711] and on IBM's five-qubit cloud chips [D][712]. The d = 2 surface code followed on transmons at ETH Zurich [D][713] and QuTech [D][714], and Google ran a small surface-code detection experiment beside its repetition codes [D][715].
Carrier-agnostic; static wiring; no control or readout of its own; stochastic Pauli errors only — leakage and loss need their own flags.

## Physics & limits
One fault flips a check, so an undetected logical error needs two: post-selected infidelity scales as O(ε²), not O(ε) — how IBM's encoded magic state beat every physical qubit pair on its chip [D][716]. The price is acceptance. With N fault locations each faulting detectably with probability p, acceptance ≈ e^(−pN) and the sampling overhead, its inverse [D][717], is e^(pN) — ~2×10⁴ runs per kept sample at p = 10⁻³, N = 10⁴ — while residual error grows as ~Np² [S]. A fixed distance-2 code has no threshold and no Λ; circuit volume, not code size, sets the exponent. Iceberg rotations are compiled non-fault-tolerantly, letting some single faults through [D][673]. A threshold returns only when detection codes are concatenated and upper levels correct: Knill's C4/C6 scheme gave evidence for computing above 3% error per gate [S][718], and concatenated iceberg codes suppress post-selection by raising the distance [D][105].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2017-10 | [[4,2,2]] fault-tolerant encoding and syndrome measurement | Maryland, trapped ions | [D][711] |
| 2019-02 | [[4,2,2]] logical RB: two-qubit infidelity 5.8(2)% → 0.60(3)% | Harper & Flammia, IBM cloud | [D][719] |
| 2020-06 | d = 2 surface code, 7 transmons, logical initialisation 96.1% | ETH Zurich | [D][713] |
| 2024-01 | Iceberg: 8 logical qubits, up to 256 layers, logical quantum volume 2⁸ | Quantinuum H1-2 | [D][673] |
| 2025-04 | Spacetime checks: 50 logical qubits, 2,450 CZ, fidelity gain up to 236× | IBM Heron (ibm_kingston) | [D][717] |
| 2025-11 | d = 2 surface: transversal CNOT 88.9(5)%, logical Bell 79.4–79.5% | Origin Wukong | [D][720] |
| 2026-02 | Iceberg and concatenated iceberg: 48–94 logical qubits beyond break-even | Quantinuum Helios | [D][105] |
| 2026-09 | Spacetime-coded sampling: 76 physical qubits, 10× gate-error suppression, fidelity ≥ 0.349 (95%) | IBM/UChicago | [D][46] |

Best demonstrated as of 2026-09-26: Helios' 94 iceberg-detected logical qubits [D][105]. Dominant term: acceptance, rarely printed beside the headline.

## Manufacturing, materials & supply chain
Nothing is fabricated for detection; its supply chain is the host machine's. Connectivity decides the code: on heavy-hex, [[4,2,2]] uses flag qubits — extra ancillas that catch faults spreading out of a syndrome circuit [D][716]; iceberg's global parity checks suit all-to-all ion traps [D][673]; spacetime checks are searched for under whatever connectivity the chip has [D][717].

## Control, readout & I/O burden
Detection needs syndrome bits, not a decoder in the loop: discarding can follow the run, so there is no latency budget unless preparation is adaptive [D][716]. Wukong read its stabilisers from the final data measurement alone, with no mid-circuit readout [D][720]. The burden is shots: injection on ibm_fez kept 36.28(9)% of runs, ~2.8 runs per state [D][721]; QPU time grows as e^(pN) [S].

## Role in the stack
Slot 7 of three architectures: Transmon lattice with tunable couplers; Trapped ions — QCCD (transport between zones); Trapped ions — linear Paul trap with individual laser addressing. It **requires** syndrome measurement (dispersive readout on transmons). It **provides** post-selected logical states and gates, a first rehearsal of transversal logic [D][720], and the discard stage of magic-state preparation: ibm_fez injection gave |H_L⟩ 0.8806(2) and |T_L⟩ 0.8665(3), above the 0.854 and 0.827 distillation thresholds [D][721]. It is **replaced** by the rotated surface code — correction instead of detection. Algorithmic fault tolerance takes nothing further: its guarantee is exponential in distance [S][152].

The register lists {{N_T_CODE_DETECT_MACHINES_W}} carriers, {{N_T_CODE_DETECT_PRIMARY_W}} primary and {{N_T_CODE_DETECT_ALTERNATE_W}} alternate. The superconducting ones are all primary. IBM Quantum Heron r2 [D][721], IBM Quantum Heron r3 (ibm_pittsburgh) [D][46], Origin Wukong (3rd gen) [D][720] and the IQM six-qubit star QPU (Deneb-class), 0.25(2)–0.91(3)% logical error per [[4,2,2]] cycle [D][488], match their evidence; Origin Wukong 102 is listed by inference from the Wukong paper. IBM Quantum Falcon r5.11 is carried by the [[4,2,2]] magic state on ibm_peekskill [D][716], not by its distance-3 subsystem code, decoded by matching with only leakage post-selected (4.37–4.91% of shots per round) — correction [D][722]. Rigetti Ankaa-2 is not a carrier: its 8-qubit stability experiment was decoded in real time, with no post-selection reported [D][723]. The alternates are ion machines: System Model H1 (H1-1), for the iceberg run on H1-2 [D][673], and Helios [D][105]; the iceberg run on H2-1 (up to 20 logical qubits) [D][724] is not listed. A quantum-dot spin device is primary too: HRL exchange-only silicon spin processor (18 EO qubits from 54 quantum dots). This answers gap G-detect7: transmon slot 7 listed only correcting codes, while what shipped was detection.

## Evidence — how the numbers were measured
Every headline here is conditional on acceptance: Harper & Flammia's 0.60(3)% is logical RB inside the code space [D][719]; Wukong's gates and the ibm_fez states are post-selected [D][720][D][721]. Acceptance belongs beside every fidelity, and the physical baseline deserves the same discard. Microsoft and Quantinuum report correction and detection on the same codes, 11× to 800× below physical baselines [D][667]. Detection can also certify: IBM's spacetime-coded sampling bounds fidelity from syndrome statistics, device-dependent but under weaker assumptions than proxy benchmarks [D][46] — fidelity, not hardness: version 1's 70-qubit circuit (bound 0.284) was simulated classically in 37.3 min on 256 H100 GPUs, log-XEB 0.350 [D][47]; version 3 (2026-09-02) reports 76 physical qubits and a bound of 0.349 [D][46].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IBM | developer | US | [[4,2,2]] magic state on Falcon; spacetime checks on Heron | [D][716][D][717] |
| Quantinuum | developer | US/UK | Iceberg code on H1-2, H2-1 and Helios | [D][673][D][105] |
| Origin Quantum | developer | CN | d = 2 surface-code logical gate set on Wukong | [D][720] |
| IQM | developer | FI | [[4,2,2]] on a star-topology processor | [D][488] |

**Money.** No dated financial item is specific to error-detection codes as of 2026-09-26; they are paid for inside machine and research budgets.

**Market & supply chain.** Nobody sells detection; vendors sell QPU time, which detection multiplies by 1/acceptance. It pays into G2 — IBM reports lower sampling overhead than error mitigation [D][717] — and into G3 only as rehearsal and state-preparation discard.

**IP & standards.** No detection-specific patent family or reporting standard found as of 2026-09-26; the codes are published [D][673][S][710].

**Roadmaps & track record.** No vendor roadmap sets a detection milestone. Quantinuum moved from distance-2 iceberg (2024) to distance-4 concatenated iceberg (2026) within one code family [D][673][D][105].

**Strategic reading.** Detection is the honest NISQ-to-QEC step: encoding, fault-tolerant preparation and logical gates at a stated discard cost, no scaling claimed. It favours platforms whose fidelity keeps pN small — the largest runs are on ions [D][105] — and gives transmon vendors a compiler-level route to better G2 circuits. It undercuts only reporting that calls a distance-2 block a fault-tolerant logical qubit.

## Outlook & open questions
Confirm if by 2027-12-31 a detection-certified sampling run holds a fidelity bound above 0.3 on a circuit no published classical method reproduces within a week; demote to history if by 2028-12-31 magic-state preparation and utility circuits on transmons and ions run with correction, not discard. Open questions. (1) Where do detection and probabilistic error cancellation cross in sampling cost at 100–150 qubits? (2) How much gain survives a baseline given the same leakage discard? (3) Can spacetime checks leave the Clifford regime, where valid checks thin out exponentially [D][717]? (4) What acceptance do Helios' 94-qubit iceberg runs keep at depth? (5) Is concatenated detection a cheaper route to early fault tolerance on 2D chips than surface-code memories?

## References
[46] S. Martiel *et al.*, “Sampling hard circuits with verifiably high fidelity,” [arXiv:2607.25941](https://arxiv.org/abs/2607.25941), Jul. 2026. [D]
[47] H. Manabe, H. Gu, and F. Pan, “Classical Simulation and Design Frontiers for IBM's Doped Clifford Sampling Experiment,” [arXiv:2608.13110](https://arxiv.org/abs/2608.13110), Aug. 2026. [D]
[105] S. Dasu *et al.*, “Computing with many encoded logical qubits beyond break-even,” [arXiv:2602.22211](https://arxiv.org/abs/2602.22211), Feb. 2026. [D]
[152] H. Zhou *et al.*, “Low-Overhead Transversal Fault Tolerance for Universal Quantum Computation,” *Nature*, vol. 646, no. 8084, pp. 303–308, 2025, doi: [10.1038/s41586-025-09543-5](https://doi.org/10.1038/s41586-025-09543-5). [arXiv:2406.17653](https://arxiv.org/abs/2406.17653). [S]
[488] F. Vigneau *et al.*, “Quantum error detection in qubit-resonator star architecture,” [arXiv:2503.12869](https://arxiv.org/abs/2503.12869), Mar. 2025. [D]
[667] A. Paetznick *et al.*, “Improved quantum processor logical error rates via correction and detection,” *Nature*, vol. 654, no. 8118, pp. 349–355, Jun. 2026, doi: [10.1038/s41586-026-10628-y](https://doi.org/10.1038/s41586-026-10628-y). [D]
[673] C. N. Self, M. Benedetti, and D. Amaro, “Protecting expressive circuits with a quantum error detection code,” *Nat. Phys.*, vol. 20, no. 2, pp. 219–224, Jan. 2024, doi: [10.1038/s41567-023-02282-2](https://doi.org/10.1038/s41567-023-02282-2). [arXiv:2211.06703](https://arxiv.org/abs/2211.06703). [D]
[710] N. Delfosse and A. Paetznick, “Spacetime codes of Clifford circuits,” [arXiv:2304.05943](https://arxiv.org/abs/2304.05943), Apr. 2023. [S]
[711] N. M. Linke *et al.*, “Fault-tolerant quantum error detection,” *Sci. Adv.*, vol. 3, no. 10, Art. no. e1701074, Oct. 2017, doi: [10.1126/sciadv.1701074](https://doi.org/10.1126/sciadv.1701074). [arXiv:1611.06946](https://arxiv.org/abs/1611.06946). [D]
[712] C. Vuillot, “Is error detection helpful on IBM 5Q chips?,” *Quantum Inf. Comput.*, vol. 18, no. 11&12, pp. 949–964, 2018. [arXiv:1705.08957](https://arxiv.org/abs/1705.08957). [D]
[713] C. K. Andersen *et al.*, “Repeated quantum error detection in a surface code,” *Nat. Phys.*, vol. 16, no. 8, pp. 875–880, Jun. 2020, doi: [10.1038/s41567-020-0920-y](https://doi.org/10.1038/s41567-020-0920-y). [arXiv:1912.09410](https://arxiv.org/abs/1912.09410). [D]
[714] J. F. Marques *et al.*, “Logical-qubit operations in an error-detecting surface code,” *Nat. Phys.*, vol. 18, p. 80, 2022, doi: [10.1038/s41567-021-01423-9](https://doi.org/10.1038/s41567-021-01423-9). [arXiv:2102.13071](https://arxiv.org/abs/2102.13071). [D]
[715] Z. Chen *et al.*, “Exponential suppression of bit or phase errors with cyclic error correction,” *Nature*, vol. 595, pp. 383–387, Jul. 2021, doi: [10.1038/s41586-021-03588-y](https://doi.org/10.1038/s41586-021-03588-y). [D]
[716] R. S. Gupta *et al.*, “Encoding a magic state with beyond break-even fidelity,” *Nature*, vol. 625, pp. 259–263, Jan. 2024, doi: [10.1038/s41586-023-06846-3](https://doi.org/10.1038/s41586-023-06846-3). [arXiv:2305.13581](https://arxiv.org/abs/2305.13581). [D]
[717] S. Martiel and A. Javadi-Abhari, “Low-overhead error detection with spacetime codes,” [arXiv:2504.15725](https://arxiv.org/abs/2504.15725), Apr. 2025. [D]
[718] E. Knill, “Quantum computing with realistically noisy devices,” *Nature*, vol. 434, pp. 39–44, Mar. 2005, doi: [10.1038/nature03350](https://doi.org/10.1038/nature03350). [arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199). [S]
[719] R. Harper and S. T. Flammia, “Fault-Tolerant Logical Gates in the IBM Quantum Experience,” *Phys. Rev. Lett.*, vol. 122, no. 8, Art. no. 080504, Feb. 2019, doi: [10.1103/PhysRevLett.122.080504](https://doi.org/10.1103/PhysRevLett.122.080504). [arXiv:1806.02359](https://arxiv.org/abs/1806.02359). [D]
[720] J. Zhang *et al.*, “Demonstrating a universal logical gate set in error-detecting surface codes on a superconducting quantum processor,” *npj Quantum Inf.*, vol. 11, Art. no. 177, Nov. 2025, doi: [10.1038/s41534-025-01118-6](https://doi.org/10.1038/s41534-025-01118-6). [D]
[721] Y. Kim, M. Sevior, and M. Usman, “Magic state injection on IBM quantum processors above the distillation threshold,” *Sci. Rep.*, vol. 16, Art. no. 11189, Feb. 2026, doi: [10.1038/s41598-026-40381-1](https://doi.org/10.1038/s41598-026-40381-1). [arXiv:2412.01446](https://arxiv.org/abs/2412.01446). [D]
[722] N. Sundaresan *et al.*, “Demonstrating multi-round subsystem quantum error correction using matching and maximum likelihood decoders,” *Nat. Commun.*, vol. 14, Art. no. 2852, May 2023, doi: [10.1038/s41467-023-38247-5](https://doi.org/10.1038/s41467-023-38247-5). [D]
[723] L. Caune *et al.*, “Demonstrating real-time and low-latency quantum error correction with superconducting qubits,” *Nat. Commun.*, vol. 17, Art. no. 7383, Jun. 2026, doi: [10.1038/s41467-026-73331-6](https://doi.org/10.1038/s41467-026-73331-6). [arXiv:2410.05202](https://arxiv.org/abs/2410.05202). [D]
[724] Z. He, D. Amaro, R. Shaydulin, and M. Pistoia, “Performance of quantum approximate optimization with quantum error detection,” *Commun. Phys.*, vol. 8, Art. no. 217, May 2025, doi: [10.1038/s42005-025-02136-8](https://doi.org/10.1038/s42005-025-02136-8). [arXiv:2409.12104](https://arxiv.org/abs/2409.12104). [D]

## Open verification items
- Heron r3 cell: its version-3 figures come from the abstract, and the processor name (ibm_pittsburgh in the register) could not be read from any version of arXiv:2607.25941 — only its abstract and contents rendered (tried 2026-09-26); version 1's 70-qubit and 0.284 figures are confirmed only through the classical-simulation paper (arXiv:2608.13110).
- Vuillot's paper (arXiv:1705.08957): the abstract was read, but title, journal and volume could not be confirmed — the arXiv page rendered without metadata and Crossref returned HTTP 429 (tried 2026-09-26).
- The sampling overhead of IBM's 50-qubit, 236× spacetime-check run could not be read unambiguously from its Table 1 (tried 2026-09-26).
- Acceptance for Helios' 94-logical-qubit iceberg runs is not in the text that rendered (tried 2026-09-26).
