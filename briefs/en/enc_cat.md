---
id: enc_cat
name: Cat-code encoding (biased noise)
layer: 2 Encoding
status: demonstrated
since: 2020
one_line: A two-photon-dissipation-stabilised coherent-state qubit whose bit-flips fall exponentially with photon number while phase-flips rise linearly with it.
verdict: The bias is real but small where measured — bias > 25 under a CX at n̄ = 2; the resource estimates imply a cavity lifetime near 50 ms, twice the best ever built.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A qubit spanned by two coherent states of a cavity mode, held there by engineered two-photon exchange with a lossy buffer. Bit-flips must cross phase space between the lobes, exponentially suppressed in n̄; one photon loss flips the phase, linear in n̄. Demonstrated from about 2020 (Lescanne, Leghtas and colleagues), commercialised by Alice & Bob and AWS. It has no gate time or readout of its own; its only product is the asymmetry.

## Physics & limits
Γ_Z ≈ n̄/T1: the encoding turns cavity lifetime directly into logical quality, and photon number buys bit-flip suppression at a linear price. Ocelot closes the loop: at n̄ = 2 the storage lifetime is 57–68 µs [D][75]. Run that arithmetic at the operating point the estimates assume, n̄ ≈ 19 and 10⁻³ phase-flip per cycle, and the required cavity T1 is n̄·t/p ≈ 53 ms [S][75], [89]. The best published cavity memory is 25.6 ms, built by decoupling the mode from its ancilla — the opposite of what a stabilised cat does [D][247]. That is the floor: the qubit-count argument is a claim about cavity lifetime under strong drive. What moves it: lower single-photon loss at high pump power, or squeezed cats [D][73].

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02 | Per CX at n̄ = 2: phase-flip 9.6(4)×10⁻², bit-flip 3.5(4)×10⁻³ → bias > 25, idle > 30; repetition code 1.75(2)% (d=3, n̄=1) → 1.65(3)% (d=5, n̄=1.5) per 2.8 µs cycle | AWS/Caltech | [D][75] |
| 2025-09 | 12-cat chip: mean bit-flip 44 min, peak 252 min, preliminary | Alice & Bob | [C][72] |
| 2025-02 | Squeezed-cat variant: 22 s bit-flip | Alice & Bob | [D][73] |

Phase-flip dominates: ~10⁻¹ per cycle where a code has run, against the ~10⁻³ assumed; bit-flip suppression stopped being the problem two years ago.

## Manufacturing, materials & supply chain
It has no fabrication step of its own, adding a continuous parametric pump and buffer mode to the host cavity. That pump is the I/O cost: a drive line, a pump line and a shared ancilla readout chain per cat. Ocelot spends five buffers and four ancilla transmons on five cats [D][75]. At 10³ cats the wall is pump-line count and pump heating in one dilution unit; 10⁴–10⁶ needs multiplexed cryogenic drive, undemonstrated here. Supply chain and export exposure are the host cavity's.

## Role in the stack
Requires a bosonic cavity mode; provides the biased inner qubit for repetition-cat and LDPC-cat concatenation and for a cat–cat CNOT. It replaces the bare two-level encoding, competes with GKP and conflicts with the unbiased surface code. Derived round 1.44 µs, gate-set, against the measured 2.8 µs syndrome cycle [D][75]. Verification: the distance-3 and distance-5 points were taken at n̄ = 1 and n̄ = 1.5, so "flat with distance" mixes distance with operating point [D][75]. The 44-minute mean bit-flip is preliminary; the same vendor's roadmap quotes a 252-minute peak from that run [C][72][C][328].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Alice & Bob | developer | FR | Bit-flip records, 18-cat Helium, a cat-only roadmap | [C][72] |
| AWS | developer | US | Ocelot, the only published cat code with a budget | [D][75] |
| DARPA | investor | US | Stage B selected Nord Quantique, not Alice & Bob | [G:QBI-STAGEB-2025-11] |

**Money.**
2025-01-28 · Alice & Bob · Series B · €100 M · — · closed [G:AB-SERIESB-2025-01]
2026-05-22 · Alice & Bob · Series B extension · undisclosed · NVentures lead · closed [C][83]

**Market & supply chain.** Nothing is sold at this layer; the encoding is a design choice on the cavity supply chain, bought as a promise about G3 and G4. Alice & Bob's business rests on it.

**IP & standards.** No dated patent family specific to cat-code encoding was found; filings attach to gates, pumps and readout.

**Roadmaps & track record.** The published ladder runs Helium (18 cats, 1 logical, 10⁻², delivered 2026-06) → Lithium (48/4, 10⁻³) → Beryllium (250/5, 10⁻⁴) → Graphene (2,000/100, 10⁻⁶, 2030) [R][328]. Chips arrive on time, but no logical error rate has been published for any, so every defining number is a promise. AWS has published no cat roadmap past Ocelot.

**Strategic reading.** If phase-flip per cycle falls two orders, cat encoding wins the physical-qubit count; if not, the branch is a memory technology and the budget goes to qLDPC or dual-rail erasure.

*Open niche:* bias is reported without a convention — idle or under gate, at what n̄, over what cycle. One protocol fixing all three across vendors would make it comparable.

## Outlook & open questions
Confirm by 2027 if phase-flip per cycle falls below 10⁻² with bias above 100 at fixed n̄; demote the efficiency claims if it stays near 10⁻¹. Best case 2029: a cat at n̄ ≥ 5 with millisecond lifetime under active stabilisation. Worst case: bias saturates and the 758-cat and 126,133-cat estimates stay unreachable [S][89], [90]. Open: does squeezing survive multi-qubit operation; can pump power rise without loading T1? Watch Lithium and any Ocelot successor.

## Sources
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[72] N. Coppola, “Alice & Bob Shares Preliminary Results Vastly Surpassing Previous Bit-Flip Time Record,” Alice & Bob, Sep. 25, 2025. [Online]. Available: https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record [C]
[73] N. Coppola, “Alice & Bob Improves Error Suppression in Quantum Computers by 'Squeezing' Cat Qubits,” Alice & Bob, Mar. 11, 2025. [Online]. Available: https://alice-bob.com/newsroom/squeezed-cat-qubit/ [D]
[75] H. Putterman *et al.*, “Hardware-efficient quantum error correction via concatenated bosonic qubits,” *Nature*, vol. 638, no. 8052, pp. 927–934, Feb. 2025, doi: [10.1038/s41586-025-08642-7](https://doi.org/10.1038/s41586-025-08642-7). [D]
[83] N. Coppola, “Alice & Bob announces Series B Extension,” Alice & Bob, May 22, 2026. [Online]. Available: https://alice-bob.com/newsroom/alice-bob-announces-series-b-extension/ [C]
[89] É. Gouzien, D. Ruiz, F.-M. Le Régent, J. Guillaud, and N. Sangouard, “Performance Analysis of a Repetition Cat Code Architecture: Computing 256-bit Elliptic Curve Logarithm in 9 Hours with 126133 Cat Qubits,” *Phys. Rev. Lett.*, vol. 131, Art. no. 040602, Jul. 2023, doi: [10.1103/PhysRevLett.131.040602](https://doi.org/10.1103/PhysRevLett.131.040602). [arXiv:2302.06639](https://arxiv.org/abs/2302.06639). [S]
[90] D. Ruiz, J. Guillaud, A. Leverrier, M. Mirrahimi, and C. Vuillot, “LDPC-cat codes for low-overhead quantum computing in 2D,” *Nat. Commun.*, vol. 16, Art. no. 1040, 2025, doi: [10.1038/s41467-025-56298-8](https://doi.org/10.1038/s41467-025-56298-8). [arXiv:2401.09541](https://arxiv.org/abs/2401.09541). [S]
[247] O. Milul *et al.*, “Superconducting Cavity Qubit with Tens of Milliseconds Single-Photon Coherence Time,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030336, Sep. 2023, doi: [10.1103/PRXQuantum.4.030336](https://doi.org/10.1103/PRXQuantum.4.030336). [D]
[328] Alice & Bob, “Roadmap,” Jun. 23, 2026. [Online]. Available: https://alice-bob.com/roadmap/ [C]

## Open verification items
9.6×10⁻² is the phase-flip error of the CX gate at n̄ = 2, not a per-QEC-cycle figure, and the noise bias is > 25 under the CX and > 30 idle — the "27–33" in circulation are phase-flip *times* in µs, not bias values [D][75].
The 44-minute mean bit-flip time (12-cat chip, September 2025) is preliminary and vendor-published; no peer-reviewed follow-up was found, and the roadmap page states a 252-minute peak for the same period.
The 53 ms cavity-lifetime requirement is this brief's arithmetic from Γ_Z ≈ n̄/T1 using the estimates' own assumptions; neither source states it.
Nord Quantique's QBI Stage B award [60] is cited for programme context; its GKP route does not use this encoding.
