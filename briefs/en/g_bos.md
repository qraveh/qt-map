---
id: g_bos
name: Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter)
layer: 3 Gate mechanism
status: demonstrated
since: 2018
one_line: Driven SQUID/SNAIL couplers and transmon ancillas mediate beam-splitter and entangling gates between superconducting bosonic cavity modes, for cat, GKP and dual-rail encodings.
verdict: Dual-rail cavity CZ reaches 0.029% post-selected Pauli error at 500 ns with ~80% of gate error heralded as erasure; no bias-preserving cat-cat entangling gate exists as of 4 Sep 2026.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two bosonic cavity modes are never coupled directly. A nonlinear element between them — a driven DC-SQUID or SNAIL coupler, or a dispersively coupled transmon ancilla — is pumped at the mode-frequency difference, turning pump photons into a bilinear exchange (beam-splitter) or a conditional phase. Yale set the pattern in 2018 with an RF-driven 50:50 beam-splitter between two microwave memories [D][1]; gate fidelities follow from 2023 [D][2].
- b/e: entangling time ≈500 ns (10⁻⁶·³ s), deterministic; microwave drives from room-temperature electronics.
- d/g: modes linked through a shared coupler acting as a bus; 3D-machined cavity hardware, not planar chips.

## Physics & limits
The parametric beam-splitter rate reaches a few MHz, hence ~100 ns swaps [D][2]; a conditional phase accumulates through a dispersive shift χ/2π ≈ 0.1–1 MHz, hence ~500 ns entangling gates [D][3]. The floor is the ancilla, not the cavity: at ancilla T₁ ≈ 50–100 µs against a 0.5-µs gate, ancilla error is ~10⁻² unless it is kept virtual or *relabelled*. Relabelling is the point: dual-rail does not lower total gate error but moves ~80% of it into heralded erasure (0.400(4)% control, 0.096(4)% target), leaving 0.029(6)% unheralded Pauli error and bit-flips at 2.8(4)×10⁻⁶ [D][3]; located erasures buy ~5× more tolerable Pauli error at code level than depolarising noise [P][4]. Failure modes: ancilla decay mid-gate (an erasure in dual-rail, a phase error elsewhere), ancilla dephasing, higher-Fock leakage no check sees, and for cats any gate term failing to commute with the two-photon dissipation. Moving the floor needs higher-coherence ancillas, virtual-ancilla or dissipative coupling, or a bias-preserving cat Hamiltonian — still theory [P][5].

## Engineering state of the art
Best demonstrated: dual-rail cavity CZ, ~500 ns, erasure ≈0.5%/gate, post-selected Pauli 0.029(6)%, SPAM ≈0.02% [D][3][G:DUALRAIL-CZ-2026-08]. D-Wave markets it as "approximately 99.9%" [C][6], neither the raw nor the post-selected value. Typical at scale lags: AWS's transmon check runs 384 ns, erasure 2.54(1)×10⁻²/check, residual 6.0(2)×10⁻⁴, bias 42(1) [D][7]. No cat–cat CNOT exists on hardware [P][5]. Dominant error term: unheralded Pauli error surviving post-selection, plus the check's false negatives.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018-02 | RF-driven 50:50 beam-splitter between two cavity memories | Yale | [D][1] |
| 2023-03 | Cavity swap >99.98%, ~100 ns, DC-SQUID coupler | Yale | [D][2] |
| 2026-04 | Erasure check 384 ns, residual 6.0(2)×10⁻⁴, bias 42(1) | AWS | [D][7] |
| 2026-08 | Dual-rail cavity CZ ~500 ns, post-selected Pauli 0.029(6)% | Quantum Circuits | [D][3] |

## Manufacturing, materials & supply chain
Ancilla and coupler are aluminium- or tantalum-junction circuits on silicon or sapphire; the modes are machined high-purity aluminium 3D cavities, etched to 10⁷–10⁸ Q. No merchant supplier exists — Yale, AWS, Alice & Bob and D-Wave/Quantum Circuits each machine their own — so surface treatment is lab craft, not a qualified process. Below that, the generic superconducting chain: Bluefors, which absorbed pulse-tube maker Cryomech in 2023, and Oxford Instruments [G:BLUEFORS-CRYOMECH-2023]. Export exposure is the 2024 BIS rule: ECCN 4A906 (≥34-qubit machines), 3A904 (refrigerators ≥600 µW at 0.1 K), 3A901 (cryogenic amplifiers) [G][8]. No per-cavity cost or yield is public.

## Control, readout & I/O burden
Each cell needs a cavity drive, an ancilla drive and a dispersive ancilla readout, so lines run ahead of mode count. Erasure conversion adds latency: AWS resolves a check in 384 ns [D][7], the cavity gate in ≈0.4–1 µs [D][3]. That fits an FPGA-local loop but nothing off-chassis: NVQLink's 3.84 µs round trip suits syndrome processing, not heralding [C][G:NVQLINK-2025]. The wall is geometric before electrical: a machined cavity is a cubic-centimetre object, so 10³ modes is a fridge-volume problem and 10⁶ needs planar or transmon variants.

## Role in the stack
The shared entangling primitive of two competing superconducting paths, cat/GKP encoding and dual-rail erasure encoding. It requires a cavity mode plus an ancilla and replaces ancilla-free cat-CNOT schemes: hardware bought for erasure-convertibility or bias, a trade only dual-rail has cashed. Not a hub; it reaches the superconducting branch only. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 1.44 µs, whose largest term is two 500 ns gate layers. Empty neighbouring slots: a bias-preserving cat entangling gate, a merchant high-Q cavity process.

## Verification (QCVV)
Headline figures come from randomised benchmarking on the composite two-mode system with post-selection on ancilla readout; the erasure fraction comes from that same readout, so false negatives fold into the "residual Pauli" bucket. A transmon-qutrit erasure design reports false positives ~2%, false negatives 6–8% [P][9] — the order of what may be misattributed here. Theory keeps the surface-code threshold at least twice the Pauli value under imperfect checks, but only when the check is short against the cycle [D][10]. Conflict: 0.029(6)% vs the 0.12% bound at depth [D][3] vs "≈99.9%" [C][6]; I trust the decomposition. SUSTech replicates the architecture, not the fidelity [D][11]. Discard rates go unreported.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantum Circuits Inc. | developer | USA | Built the 500-ns dual-rail CZ; ships 8-qubit Seeker | [D][3] |
| D-Wave Quantum | developer | USA | Owner since Jan 2026; funds and markets it | [C][12] |
| Yale University | research | USA | Originated ancilla-mediated cavity gates | [D][1] |
| AWS | developer | USA | Transmon erasure checks; Ocelot; CNOT theory | [D][7] |
| Alice & Bob | developer | France | Cat gates; 18-cat Helium, no logical data | [C][13] |
| Nord Quantique | developer | Canada | GKP bosonic gates; QBI Stage B | [C][14] |

**Money.**
| Date | Actor | Event | Amount | Programme / lead | Status |
|---|---|---|---|---|---|
| 2025-01-28 | Alice & Bob | Series B (extension 2026-05-22, undisclosed) | €100M | AVP, Bpifrance | closed [C][G:AB-SERIESB-2025-01] |
| 2025-11-04 | US DOE | centre renewal naming dual-rail | $125M | C2QA/NQISRC | awarded [G][15] |
| 2025-11-06 | DARPA | Stage B, 11 teams, Alice & Bob cut | ≤$15M | QBI | official [G][16] |
| 2026-01-20 | D-Wave | M&A: Quantum Circuits | $550M | — | closed [C][12] |
| 2026-05-18 | Nord Quantique | equity at $1.4B valuation | $30M | — | closed [C][14] |
| 2026-08-06 | D-Wave | H1-2026 revenue | $5.9M (−67% YoY) | — | reported [C][17] |

**Market & supply chain.** Nobody sells into this mechanism: it rides the refrigerator and junction chains common to all superconducting qubits, plus one unshared step, 3D cavity machining, which is the single point of failure. Helium's ~40 kW is the family's only public power figure [C][13]. It pays for G2 and is a credible G3 candidate via dual-rail, not G4: the cat resource case rests on a phase-flip rate two orders below measurement, and D-Wave's Λ = 27 is a simulation of its own error model [S][G:QCI-LAMBDA27-2026-08].

**IP & standards.** Amazon Technologies holds US 11,748,652 B1 (heralding of amplitude-damping decay, granted 2023-09-05), reading directly on heralded-decay dual-rail embodiments [G][18] — awkward for rivals, since AWS alone needs no licence. No Yale or Quantum Circuits family surfaced in a dual-rail patent search [G:ORCA-DUALRAIL-PATENT-2025]. No litigation, no standards body.

**Roadmaps & track record.** D-Wave/Quantum Circuits (2026-06, for 2032: 100 logical at Λ = 10, via 17 qubits in 2026) — gate published, no system delivered as of 4 Sep 2026 [P][G:DWAVE-DR-NAMING-2026-08]; best physics, unproven as product. Alice & Bob (2023, for 2030: 2,000 cats, 100 logical, 10⁻⁶) — Helium shipped without logical data, no Stage B slot; unverified. Nord Quantique (2024, for 2029: 100+ logical at 1:1) — capitalised, unproven. AWS — Ocelot delivered, cat–cat CNOT still theory; claims have not outrun measurements.

**Strategic reading.** If erasure conversion scales the winners own large superconducting fabs, not bosonic specialities: the mechanism is portable, and IBM, Google or Rigetti could bolt an ancilla check onto existing transmons without 3D cavities [P][9]. That is the substitution threat to D-Wave's $550M purchase, which concentrates Yale-lineage IP but buys no fab moat. Losers if it fails: the cat roadmaps, whose economics rest on a 100× resource reduction the measured phase-flip rate does not support.

*Open niche:* A small QCVV house could sell the missing measurement: erasure-check characterisation separating true heralded loss from undetected higher-Fock leakage, reporting false-negative rate and discard fraction beside the headline fidelity. Nobody publishes those two numbers, on which the code-level value of erasure depends.

## Outlook & open questions
Confirm/demote in 12–24 months: a cat–cat CX on hardware; a dual-rail gate below 0.01% post-selected Pauli outside Quantum Circuits; a delivered 17-qubit system with its promised 2× logical-versus-physical error reduction; a published discard rate. Best case 2029: erasure conversion becomes a standard transmon add-on. Worst case: cat–cat gates stay theory and 3D cavities stall on volume. Open: does the erasure fraction hold at depth 10³; the true false-negative rate; can it be planarised without losing Q; does D-Wave fund Quantum Circuits through 2028 on $5.9M half-year revenue. Watch QBI Stage C.

## Sources
[1] Y. Y. Gao *et al.*, “Programmable interference between two microwave quantum memories,” *Phys. Rev. X*, vol. 8, no. 2, Art. no. 021073, Jun. 2018, doi: [10.1103/PhysRevX.8.021073](https://doi.org/10.1103/PhysRevX.8.021073). [arXiv:1802.08510](https://arxiv.org/abs/1802.08510).
[2] Y. Lu *et al.*, “High-fidelity parametric beamsplitting with a parity-protected converter,” [arXiv:2303.00959](https://arxiv.org/abs/2303.00959), Mar. 2023.
[3] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935).
[4] M. Violaris *et al.*, “Developments in superconducting erasure qubits for hardware-efficient quantum error correction,” [arXiv:2601.02183](https://arxiv.org/abs/2601.02183), Jan. 2026. [P]
[5] Y. Ye *et al.*, “Bias-preserving cat-cat CNOT gate via vacuum-conditional beam-splitter,” [arXiv:2607.22852](https://arxiv.org/abs/2607.22852), Jul. 2026. [P]
[6] K. Chou, J. Teoh, and N. Mehta, “Why D-Wave's New Two-Qubit Gate is a Breakthrough for Quantum Error Correction,” D-Wave Quantum Blog, Aug. 5, 2026. [Online]. Available: https://www.dwavequantum.com/learn/blog/posts/why-d-wave-s-new-two-qubit-gate-is-a-breakthrough-for-quantum-error-correction/ [C]
[7] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026.
[8] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies
[9] B.-J. Liu *et al.*, “Hardware-Efficient Erasure Qubits With Superconducting Transmon Qutrits,” [arXiv:2604.08672](https://arxiv.org/abs/2604.08672), Apr. 2026. [P]
[10] K. Chang *et al.*, “Surface Code with Imperfect Erasure Checks,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040355, Dec. 2025, doi: [10.1103/d1v7-nctj](https://doi.org/10.1103/d1v7-nctj).
[11] W. Huang *et al.*, “Logical multi-qubit entanglement with dual-rail superconducting qubits,” *Nat. Phys.*, vol. 22, no. 4, pp. 591–597, Mar. 2026, doi: [10.1038/s41567-026-03211-9](https://doi.org/10.1038/s41567-026-03211-9). [arXiv:2504.12099](https://arxiv.org/abs/2504.12099).
[12] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[13] N. Coppola, “Alice & Bob Unveils First Quantum System, Helium,” Alice & Bob, Jun. 10, 2026. [Online]. Available: https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/ [C]
[14] Nord Quantique, “Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment,” Business Wire, May 18, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment [C]
[15] US Department of Energy, “Energy Department Announces $625 Million to Advance the Next Phase of National Quantum Information Science Research Centers,” Energy.gov, Nov. 4, 2025. [Online]. Available: https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information
[16] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[17] D-Wave Quantum Inc., “D-Wave Reports Second Quarter 2026 Results,” Aug. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ [C]
[18] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en

## Open verification items
Author list, affiliation and journal reference for arXiv:2303.00959 could not be retrieved (the abstract page returned body text only); the ~100 ns / >99.98% swap figures and the DC-SQUID coupler are confirmed, the Yale attribution rests on the graph record. Alice & Bob's May-2026 Series B extension amount remains undisclosed. Post-selection discard rates for the dual-rail CZ and the beam-splitter swap are unreported. The 0.029(6)% point estimate and the 0.12% bound at depth both appear in Nature [3] without reconciliation, and D-Wave's "≈99.9%" [6] is reconciled with neither.
