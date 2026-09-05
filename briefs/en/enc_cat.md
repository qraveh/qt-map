---
id: enc_cat
name: Cat-code encoding (biased noise)
layer: 2 Encoding
tier: 3
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
Γ_Z ≈ n̄/T1: the encoding turns cavity lifetime directly into logical quality, and photon number buys bit-flip suppression at a linear price. Ocelot closes the loop: at n̄ = 2 the storage lifetime is 57–68 µs [D][1]. Run that arithmetic at the operating point the estimates assume, n̄ ≈ 19 and 10⁻³ phase-flip per cycle, and the required cavity T1 is n̄·t/p ≈ 53 ms [S][1][6]. The best published cavity memory is 25.6 ms, built by decoupling the mode from its ancilla — the opposite of what a stabilised cat does [D][9]. That is the floor: the qubit-count argument is a claim about cavity lifetime under strong drive. What moves it: lower single-photon loss at high pump power, or squeezed cats [D][2].

## Engineering state of the art
| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02 | Per CX at n̄ = 2: phase-flip 9.6(4)×10⁻², bit-flip 3.5(4)×10⁻³ → bias > 25, idle > 30; repetition code 1.75(2)% (d=3, n̄=1) → 1.65(3)% (d=5, n̄=1.5) per 2.8 µs cycle | AWS/Caltech | [D][1] |
| 2025-09 | 12-cat chip: mean bit-flip 44 min, peak 252 min, preliminary | Alice & Bob | [C][3] |
| 2025-02 | Squeezed-cat variant: 22 s bit-flip | Alice & Bob | [D][2] |

Phase-flip dominates: ~10⁻¹ per cycle where a code has run, against the ~10⁻³ assumed; bit-flip suppression stopped being the problem two years ago.

## Manufacturing, materials & supply chain
It has no fabrication step of its own, adding a continuous parametric pump and buffer mode to the host cavity. That pump is the I/O cost: a drive line, a pump line and a shared ancilla readout chain per cat. Ocelot spends five buffers and four ancilla transmons on five cats [D][1]. At 10³ cats the wall is pump-line count and pump heating in one dilution unit; 10⁴–10⁶ needs multiplexed cryogenic drive, undemonstrated here. Supply chain and export exposure are the host cavity's.

## Role in the stack
Requires a bosonic cavity mode; provides the biased inner qubit for repetition-cat and LDPC-cat concatenation and for a cat–cat CNOT. It replaces the bare two-level encoding, competes with GKP and conflicts with the unbiased surface code. Derived clock 2.8 µs, set by the syndrome cycle [D][1]. Verification: the distance-3 and distance-5 points were taken at n̄ = 1 and n̄ = 1.5, so "flat with distance" mixes distance with operating point [D][1]. The 44-minute mean bit-flip is preliminary; the same vendor's roadmap quotes a 252-minute peak from that run [C][3][C][4].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Alice & Bob | developer | FR | Bit-flip records, 18-cat Helium, a cat-only roadmap | [C][3] |
| AWS | developer | US | Ocelot, the only published cat code with a budget | [D][1] |
| DARPA | investor | US | Stage B selected Nord Quantique, not Alice & Bob | [G:QBI-STAGEB-2025-11] |

**Money.**
2025-01-28 · Alice & Bob · Series B · €100 M · — · closed [G:AB-SERIESB-2025-01]
2026-05-22 · Alice & Bob · Series B extension · undisclosed · NVentures lead · closed [C][5]

**Market & supply chain.** Nothing is sold at this layer; the encoding is a design choice on the cavity supply chain, bought as a promise about G3 and G4. Alice & Bob's business rests on it.

**IP & standards.** No dated patent family specific to cat-code encoding was found; filings attach to gates, pumps and readout.

**Roadmaps & track record.** The published ladder runs Helium (18 cats, 1 logical, 10⁻², delivered 2026-06) → Lithium (48/4, 10⁻³) → Beryllium (250/5, 10⁻⁴) → Graphene (2,000/100, 10⁻⁶, 2030) [R][4]. Chips arrive on time, but no logical error rate has been published for any, so every defining number is a promise. AWS has published no cat roadmap past Ocelot.

**Strategic reading.** If phase-flip per cycle falls two orders, cat encoding wins the physical-qubit count; if not, the branch is a memory technology and the budget goes to qLDPC or dual-rail erasure.

*Open niche:* bias is reported without a convention — idle or under gate, at what n̄, over what cycle. One protocol fixing all three across vendors would make it comparable.

## Outlook & open questions
Confirm by 2027 if phase-flip per cycle falls below 10⁻² with bias above 100 at fixed n̄; demote the efficiency claims if it stays near 10⁻¹. Best case 2029: a cat at n̄ ≥ 5 with millisecond lifetime under active stabilisation. Worst case: bias saturates and the 758-cat and 126,133-cat estimates stay unreachable [S][6][7]. Open: does squeezing survive multi-qubit operation; can pump power rise without loading T1? Watch Lithium and any Ocelot successor.

## Sources
[1] Putterman et al. (AWS/Caltech) · "Hardware-efficient quantum error correction using concatenated bosonic qubits" (Ocelot) · Nature 638, 927–934 · 2025-02-26 — https://www.nature.com/articles/s41586-025-08642-7
[2] Alice & Bob · squeezed cat qubit, 22 s bit-flip · newsroom and arXiv:2502.07892 · 2025-02 [C] — https://alice-bob.com/newsroom/squeezed-cat-qubit/
[3] Alice & Bob · "Alice & Bob surpasses bit-flip stability record" · newsroom · 2025-09 [C] — https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record
[4] Alice & Bob · public roadmap, per-milestone logical error targets · retrieved 2026-09-04 [C] — https://alice-bob.com/roadmap/
[5] Alice & Bob · "Alice & Bob announces Series B extension" · newsroom · 2026-05-22 [C] — https://alice-bob.com/newsroom/alice-bob-announces-series-b-extension/
[6] Gouzien, Ruiz, Le Régent, Guillaud, Sangouard · cat-qubit resource estimate, 126,133 cats in 9 h for a 256-bit elliptic-curve break · arXiv:2302.06639 · 2023-02-13 — https://arxiv.org/abs/2302.06639
[7] Ruiz et al. · LDPC-cat architecture estimate, 758 cats for 100 logical qubits · arXiv:2401.09541 · 2024-01-17 — https://arxiv.org/abs/2401.09541
[8] DARPA · Quantum Benchmarking Initiative, Stage B selection · 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[9] Milul et al. (Weizmann Institute) · "Superconducting cavity qubit with tens of milliseconds single-photon coherence time", T1 25.6 ms · PRX Quantum 4, 030336 · 2023-09-14 — https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030336

## Open verification items
9.6×10⁻² is the phase-flip error of the CX gate at n̄ = 2, not a per-QEC-cycle figure, and the noise bias is > 25 under the CX and > 30 idle — the "27–33" in circulation are phase-flip *times* in µs, not bias values [D][1].
The 44-minute mean bit-flip time (12-cat chip, September 2025) is preliminary and vendor-published; no peer-reviewed follow-up was found, and the roadmap page states a 252-minute peak for the same period.
The 53 ms cavity-lifetime requirement is this brief's arithmetic from Γ_Z ≈ n̄/T1 using the estimates' own assumptions; neither source states it.
Nord Quantique's QBI Stage B award [8] is cited for programme context; its GKP route does not use this encoding.
