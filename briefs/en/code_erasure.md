---
id: code_erasure
name: Erasure-adapted codes
layer: 7 Code
status: emerging
since: 2025
one_line: Surface and block codes decoded with located-error flags; thresholds 4–10% and Λ ≈ 27 in simulation, 1.7–1.9× gains in hardware.
verdict: Theory promises Λ ≈ 27 and 4–10% thresholds; hardware shows only 1.7–1.9× from erasure information and no erasure-decoded superconducting code. Confirm if a d=3→5 erasure-decoded memory reports Λ ≥ 3 by end-2027; demote otherwise.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An erasure-adapted code is a stabiliser code whose decoder takes, besides the syndrome, a per-qubit flag saying "this qubit was lost or left the code space here", with layout and schedule chosen for a channel in which located errors dominate. A located error removes the *which* question and leaves only the *what*, so the surface code fails only when erasures percolate — a 50% code-capacity threshold set by square-lattice bond percolation [S][1], against 18.9(3)% for depolarising noise [S][2] — and its distance against erasures is d rather than ⌈d/2⌉. Maximum-likelihood erasure decoding is linear-time peeling on a spanning forest [S][3]; Union-Find extends it to Pauli errors in O(n α(n)) [S][4]. The hardware turn came in 2022: 98% of ¹⁷¹Yb errors convertible, lifting the circuit-level surface-code threshold from 0.937% to 4.15% [S][5], and dual-rail transmons, where at 1% erasure the code tolerates 0.51% Pauli error, 5.2× the standard figure [S][2]; the first full loss-correction cycle had run on five trapped ions in 2020 [D][6]. The flags belong to the *Mid-circuit erasure check* brief (layer 6); this brief covers what the code does with them.

Attributes (graph record; legend: a affinity natural↔fabricated; b time, deterministic/heralded entangling; c readout; d mobility; e control @ placement; f error structure; g manufacturing):
- a = 0.5 — carrier-agnostic; one decoder serves atoms and transmons.
- b = no time or entangling of its own.
- c = none — it consumes the check's flag.
- d = static.
- e = no control modality, no placement.
- f = erasure — located loss dominant, small Pauli residual.
- g = none — layout and software.
Rank 3 of 96; a hub reaching the neutral-atom and superconducting families; its off-diagonal cell pairs a fabricated carrier with an erasure error structure.

## Physics & limits

The gain has three parts, each taxed. Threshold: the converted fraction sets it. Wu's 4.15% assumes 98% conversion [S][5]; measured fractions are 56(4)% of single-qubit and ≈33% of two-qubit errors on ¹⁷¹Yb [D][7] and 38(6)% of Princeton's CZ error [D][8], so the realised threshold sits between the Pauli and erasure limits; biased-erasure XZZX codes lift the ceiling to 8.2%, hybrid-fusion to 10.3% [S][9]. Checks are not free: each exposes the qubit to T₁, and erasure qubits win only when the check is short against the cycle [S][10]; with false positives and negatives the threshold stays at least twice the Pauli value and the effective distance roughly doubled [S][11]. Erasures spread through gates, and a missed erasure re-enters as leakage, the error the surface code handles worst [S][12]. The idealised ceiling is Quantum Circuits' simulation: ancilla erasure 0.4%, data erasure 0.1%, dephasing 0.04/0.01/0.01% and perfect checks delayed to the end of each round give Λ ≈ 27 per distance step against Λ ≈ 14 for 0.1% depolarising noise [S][13]; Google's hardware surface code sits at Λ = 2.14(2) [D][14]. The bias behind such numbers is ≈40:1 — 6×10⁻³ erasure against 1.6×10⁻⁴ Pauli per operation [S][2] — matching AWS's measured 42(1) [D][15] [G:AWS-ERASURE-2026-04]. What moves the floor: conversion under two-qubit gates, the false-negative rate, check time, and decoders that use delayed loss information so no mid-circuit check is needed [S][16].

## Engineering state of the art

Best demonstrated, atoms: Harvard/MIT/QuEra's surface code on up to 448 atoms, 2.14(13)× below threshold in a four-round characterisation circuit, loss information plus machine-learning decoding giving 1.73(13)× over conventional decoding [D][17]; Princeton's [[4,2,2]] block, whose logical decay slows 1.9(4)× with erasure flags in the decoder [D][8]; Microsoft/Atom Computing's 24 logical qubits in 48 atoms with 1.8 lost atoms corrected per run [D][18]. Superconductors: no erasure-decoded code has run on dual-rail hardware as of 3 Sep 2026; the largest erasure-encoded circuits are SUSTech's four dual-rail transmons at 98.8% logical Bell fidelity [D][19] [G:SUSTECH-DUALRAIL-2025] and Quantum Circuits' 8-qubit Seeker, error-detecting only [C][20] [G:QCI-SEEKER-2024-11]. Typical at scale: only the Harvard and Microsoft machines decode with loss flags above 100 atoms.

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2009 | 50% loss threshold (bond percolation) | Stace/Barrett/Doherty | [S] | [1] |
| 2022-01 | Threshold 0.937% → 4.15% at 98% conversion | Princeton/Yale | [S] | [5] |
| 2022-08 | Dual-rail: 0.51% Pauli tolerated at 1% erasure, 5.2× | AWS | [S] | [2] |
| 2023-02 | XZZX biased erasure 8.2%; hybrid-fusion 10.3% | Yale/Princeton | [S] | [9] |
| 2024-11 | 24 logical in 48 atoms; 1.8 lost atoms corrected per run | Microsoft/Atom | [D] | [18] |
| 2025-06 | [[4,2,2]] decay 1.9(4)× slower with erasure flags | Princeton | [D] | [8] |
| 2025-06 | 2.14(13)× below threshold; loss info + ML 1.73(13)× | Harvard/QuEra | [D] | [17] |
| 2026-08 | Λ ≈ 27 vs 14, structured dual-rail noise, perfect checks | QCI/D-Wave | [S] | [13] |

Dominant error term today: on atoms the unconverted two-qubit error, ≈62–67% of CZ error [D][7], [8]; on dual-rail the ancilla's erasure per CZ, 0.400(4)%, and check dead time [D][13] [G:DUALRAIL-CZ-2026-08]; on both, a false-negative tail nobody has counted over many rounds.

## Manufacturing, materials & supply chain

Nothing is fabricated for the code; its burden lands on the hardware it selects. Dual-rail asks for two good transmons or two cavities per site — a yield-squared problem — plus an ancilla per cavity pair [S][21], hence Quantum Circuits' hand-assembled 8 → 17 → 49 → 181 plan [R][22] [G:DWAVE-QCI-2026-01]. Alkaline-earth atoms add no hardware but cost single-qubit fidelity in the metastable manifold, 99.12(4)% against 99.968(3)% in the ground state of JILA's device [D][23]. The decoder is the code's only artefact: Union-Find on a Xilinx VCU129 decodes d = 21 at 11.5 ns per round under 0.1% phenomenological noise [D][24]; erasure input is native to Union-Find [S][4] but no FPGA benchmark with erasure flags is published; Stim exposes HERALDED_ERASE [P][25]. Unit cost: 2× physical qubits per site on dual-rail, against Quantum Circuits' claim of 10–20 physical per logical instead of ≈200 [C][20]. Export control: the BIS rule of 2024-09-06 [G][26] [G:BIS-QUANTUM-2024] controls computers of ≥34 qubits (4A906), software "specially designed" for developing or producing controlled qubit and control devices (4D906) and the related technology (4E906); a decoder shipped as firmware for a controlled control system falls inside 4D906.

## Control, readout & I/O burden

The code adds one bit per qubit per cycle to the syndrome stream and a decision: reset and re-entangle the erased qubit before the next round, or defer. On dual-rail that is feed-forward within ≈1 µs (0.50 µs gate, 0.38 µs check) [D][13], [15]; on atoms a camera frame and a reload, ≈1 ms [D][17]. Delayed-erasure decoding [S][16] and superchecks [D][17] remove the mid-circuit branch at the price of correlated decoding. Walls: at 10³ the wall is the hardware's; at 10⁴ the decoder must absorb ≈10⁴ flags plus syndromes per microsecond — 10 Gbit/s, within FPGA reach [D][24] but untested with erasures; at 10⁶ dual-rail means 2×10⁶ transmons, and on atoms the frame budget of the *Mid-circuit erasure check* brief applies unchanged.

## Role in the stack

Two paths: superconducting dual-rail erasure (D-Wave/Quantum Circuits, AWS, SUSTech) and alkaline-earth neutral atoms (Atom Computing/Microsoft, Princeton, Caltech). The code requires the mid-circuit erasure check's flags, provides logical qubits to nothing yet registered downstream, and replaces the Pauli-decoded surface code. The price of switching is hardware, not software: 2× physical qubits and a check per cycle on dual-rail, the metastable fidelity tax on atoms, plus a decoder that weights erased edges to zero. It conflicts with nothing formally but competes with IBM's qLDPC memory for the same G4 budget [R][G:IBM-ROADMAP]. Hub reading: the atom and superconducting camps share one artefact, the decoder. Off-diagonal reading: a fabricated carrier with an erasure error structure is genuine on dual-rail; atoms bring erasure as a natural carrier and sit on the diagonal. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path: 2.8 µs on dual-rail (gate-limited, four 0.5 µs layers over the 0.40 µs check), 1.3 ms on atoms (transport); the code rides on the host code's d₂ and adds no term. Neighbouring slots: erasure-adapted qLDPC codes (no demonstration found), the cold-stage decoder, and, one column over, photonic fusion-based computation at 10.4% tolerated loss per fusion [S][27], where Xanadu reports loss 24.1× above threshold in 2026 [R][G:XANADU-SPAC-2026-03].

## Verification (QCVV)

Headline numbers are logical decay rates versus hold time decoded with and without flags (Princeton) [D][8], or detected-error ratios between distances in a four-round circuit (Harvard's 2.14(13)×) [D][17]; simulated Λ comes from Stim-style circuit noise with an assumed bias [S][13]. Not captured: post-selection — Princeton's teleportation fidelities, 0.771(9) → 0.802(8), are conditioned on trivial syndromes and a flag [D][8]; four rounds are not a memory over 10⁵ rounds; the Λ ≈ 27 simulation assumes perfect checks, no false negatives, no check-induced dephasing [S][13]; nobody reports survival beside Λ. Independent replications: Harvard/QuEra [D][17], Microsoft/Atom [D][18], Princeton [D][8]; theory from AWS [S][2], [10], [12], Yale [S][9], [11], Duke [S][28]. Conflicts: (i) the [[4,2,2]] gain is 1.9(4)× in arXiv v1 and v2 (2026-06-23) [D][8] but 3.6× in the technology graph from the Nature Physics text [D][8] [G:PRINCETON-ERASURE-2026-06]; the published text is paywalled and 1.9(4)× is used. (ii) 98% conversion [S][5] against 38–56% measured [D][7], [8]. (iii) Λ ≈ 27 [S][13] against Λ = 2.14(2) on the best Pauli-decoded hardware [D][14] — a simulation-to-hardware gap.

## Actors & economics

**Who.**

| Organisation | Role | Country | What it does with erasure-adapted codes | Evidence |
|---|---|---|---|---|
| Quantum Circuits (D-Wave unit) | developer | US | Dual-rail cavity qubits; Λ ≈ 27 simulation; 17-qubit system due 2026 | [D][13] [C][29] |
| AWS Center for Quantum Computing | developer | US | Dual-rail transmon theory and hardware; check-schedule optimisation | [S][2], [10] [D][15] |
| Yale University | research | US | Biased-erasure XZZX codes; imperfect-check theory; C2QA partner | [S][9], [11] [G][30] |
| Princeton University | research | US | ¹⁷¹Yb erasure conversion; first erasure-decoded logical qubit | [S][5] [D][8] |
| Harvard University | research | US | Loss-aware surface-code decoding on 448 atoms; delayed-erasure decoder | [D][17] [S][16] |
| QuEra Computing | developer | US | Libra 2028, >256 logical at 10⁻⁶; QBI Stage B | [R][31] [G:QBI-STAGEB-2025-11] |
| Atom Computing | developer | US | ¹⁷¹Yb machines; loss correction with Microsoft's decoder; Magne | [D][18] [G:MAGNE-2025-07] |
| Google Quantum AI | developer | US | Stim HERALDED_ERASE; Pauli-decoded baseline Λ = 2.14; atom track since 2026-03 | [P][25] [D][14] [G:GOOGLE-ATOMS-2026-03] |
| Caltech | research | US | ⁸⁸Sr erasure conversion; erasure-code theory | [D][32] [S][12] |

**Money.**
- 2024-08-15 · Quantum Circuits · Series B close · >$60 M · ARCH, F-Prime, Sequoia, Hither Creek · ≈$84 M cumulative per trade press · closed [G:QCI-FUNDING]
- 2025-11-04 · US DOE · NQISRC renewal, C2QA (Brookhaven/Yale) · $125 M of $625 M over up to five years · programme · awarded [G][30], [33]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each · Atom Computing, QuEra among eleven; no dual-rail vendor · official [G][34] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · acquires Quantum Circuits · $550 M ($300 M stock + $250 M cash) · closed 2026-01-19/20 [C][35] [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; Atom Computing · US DoC CHIPS letters of intent · $100 M each · LOI [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · Series C · $100 M · Third Point · >$300 M cumulative · closed [G:ATOM-300M-2026-06]
- 2026-08-06 · D-Wave · Q2-2026 results · revenue $3.1 M, cash $546.2 M; $1.57 M NSF grant for gate-model work · reported [C][29] [G:DWAVE-FIN-2026]

**Market & supply chain.** Nobody sells an erasure-adapted code; the decoders are open-source (Stim, PyMatching, Union-Find) [P][25] and the FPGA implementations academic [D][24], so the money is in the hardware overhead: two transmons or two cavities plus an ancilla per site, or a metastable manifold and a camera. Concentration risk is the dual-rail readout chain and refrigerators, BIS-listed [G][26]; on atoms, the ¹⁷¹Yb/⁸⁸Sr laser set. G3 and G4 buy the full code; G2 and G1 pay today for erasure *detection* as post-selection (Seeker [C][20], Caltech's excised Rydberg simulator [D][32]); G5–G7 do not pay.

**IP & standards.** Amazon Technologies US 11,748,652 B1, heralded amplitude-damping decay for QEC (Kubica, Retzker; granted 2023-09-05) [G][36] [G:AMZN-ERASURE-PATENT]; Yale US 12,288,135, asymmetric-error-channel ancilla (granted 2025-04-29) [G][37]; Quantum Circuits' cavity families sit with D-Wave. No Princeton or Harvard erasure patent surfaced in the searches run; no database count found. No standard; Stim's HERALDED_ERASE [P][25] is the de-facto interface; D-Wave announced a forthcoming gate-model simulator for "error-aware programming" [C][29].

**Roadmaps & track record.**
- D-Wave: promised 2026-01-07 · first dual-rail system in 2026 · not delivered as of 2026-09-03; restated 2026-08-06 as a 17-qubit system with logical error 2× below physical in 2026 [C][29], [35].
- D-Wave: promised 2026-06-01 · 49 qubits / 20× (2027), 181 / 2,000× (2028), 10 logical (2030), 100 logical (2032), Λ = 10 · pending [R][22] [G:DWAVE-QCI-2026-01].
- QuEra: promised 2024-01 · 100 logical qubits in 2026 · missed; restated 2026-06-15 as Libra, >256 logical at 10⁻⁶ in 2028 [R][31] [G:QUERA-LIBRA-2026].
- Atom Computing/Microsoft: promised 2025-07-17 · Magne, 50 logical qubits, delivery around the turn of 2026/27 · pending [G:MAGNE-2025-07].
Credibility: Quantum Circuits/D-Wave publish the physics and miss the dates; Harvard/QuEra deliver papers on schedule, roadmaps late; Microsoft/Atom on schedule, silent on the code; AWS publishes and promises nothing; Princeton delivers each step of its 2022 proposal [S][5], smaller than promised.

**Strategic reading.** If erasure-adapted codes reach Λ ≥ 5 on hardware, the winners own erasure-native qubits at scale — D-Wave's cavity line, AWS's transmon pairs, the ¹⁷¹Yb camp (Atom Computing, Google's atom track) — and the decoder becomes a commodity; the losers are Pauli-only roadmaps buying Λ with fidelity alone (Google's superconducting line, IBM's qLDPC) and rubidium vendors without a metastable manifold. Substitution runs both ways: delayed-erasure decoding [S][16] and superchecks [D][17] give atoms most of the gain without erasure-native qubits; qutrit erasure encodings would strip the 2× overhead from transmons. Bargaining power sits with platform vendors; decoder authors have none.

*Open niche:* a small QCVV/SFQ research company could plug in at the decoder's input: a survival-corrected Λ benchmark reporting logical error, post-selection fraction and false-negative leakage together, run on Stim circuits with HERALDED_ERASE for dual-rail and atom groups alike; the SFQ angle is a cold-stage Union-Find front end clustering erased edges at zero weight before the syndrome leaves the fridge.

## Outlook & open questions

Confirm within 12–24 months if: any group decodes a d = 3 → 5 memory with erasure flags over ≥ 10 rounds and reports Λ ≥ 3 with survival; D-Wave's 17-qubit system shows logical error 2× below physical by mid-2027 [C][29]; a dual-rail simulation with measured false negatives and check dephasing still returns Λ ≥ 10; atom conversion under two-qubit gates passes 70%. Demote if end-2027 arrives with erasure decoding worth < 2× on every platform. Best case by 2029: dual-rail memories at Λ ≈ 5–10 with 100–200 qubits and Yb machines running loss-aware codes by default. Worst case: a decoder option worth 1.7–1.9× while Pauli-decoded transmons reach Λ ≈ 3–4 without it.

Open questions: (1) what is Λ once false negatives accumulate as leakage over 10³ rounds? (2) does the 40:1 bias survive parallel gates on shared readout lines? (3) can the metastable fidelity tax on Yb be removed? (4) is an erasure-adapted qLDPC code with a fast decoder possible? Watch: D-Wave's 2026 delivery, AWS's next multi-qubit paper, Google/Kaufman's Yb results.

## Sources

[1] T. M. Stace, S. D. Barrett, and A. C. Doherty, “Thresholds for Topological Codes in the Presence of Loss,” *Phys. Rev. Lett.*, vol. 102, no. 20, Art. no. 200501, May 2009, doi: [10.1103/PhysRevLett.102.200501](https://doi.org/10.1103/PhysRevLett.102.200501). [arXiv:0904.3556](https://arxiv.org/abs/0904.3556).
[2] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461).
[3] N. Delfosse and G. Zémor, “Linear-time maximum likelihood decoding of surface codes over the quantum erasure channel,” *Phys. Rev. Res.*, vol. 2, no. 3, Art. no. 033042, Jul. 2020, doi: [10.1103/PhysRevResearch.2.033042](https://doi.org/10.1103/PhysRevResearch.2.033042). [arXiv:1703.01517](https://arxiv.org/abs/1703.01517).
[4] N. Delfosse and N. H. Nickerson, “Almost-linear time decoding algorithm for topological codes,” *Quantum*, vol. 5, Art. no. 595, Dec. 2021, doi: [10.22331/q-2021-12-02-595](https://doi.org/10.22331/q-2021-12-02-595). [arXiv:1709.06218](https://arxiv.org/abs/1709.06218).
[5] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540).
[6] R. Stricker *et al.*, “Experimental deterministic correction of qubit loss,” *Nature*, vol. 585, no. 7824, pp. 207–210, Sep. 2020, doi: [10.1038/s41586-020-2667-0](https://doi.org/10.1038/s41586-020-2667-0). [arXiv:2002.09532](https://arxiv.org/abs/2002.09532).
[7] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493).
[8] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724).
[9] K. Sahay, J. Jin, J. Claes, J. D. Thompson, and S. Puri, “High-Threshold Codes for Neutral-Atom Qubits with Biased Erasure Errors,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041013, Oct. 2023, doi: [10.1103/PhysRevX.13.041013](https://doi.org/10.1103/PhysRevX.13.041013). [arXiv:2302.03063](https://arxiv.org/abs/2302.03063).
[10] S. Gu, Y. Vaknin, A. Retzker, and A. Kubica, “Optimizing Quantum Error-Correction Protocols with Erasure Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040354, Oct. 2025, doi: [10.1103/985g-58gd](https://doi.org/10.1103/985g-58gd).
[11] K. Chang *et al.*, “Surface Code with Imperfect Erasure Checks,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040355, Dec. 2025, doi: [10.1103/d1v7-nctj](https://doi.org/10.1103/d1v7-nctj).
[12] S. Gu, A. Retzker, and A. Kubica, “Fault-tolerant quantum architectures based on erasure qubits,” *Phys. Rev. Res.*, vol. 7, no. 1, Art. no. 013249, Mar. 2025, doi: [10.1103/PhysRevResearch.7.013249](https://doi.org/10.1103/PhysRevResearch.7.013249). [arXiv:2312.14060](https://arxiv.org/abs/2312.14060).
[13] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935).
[14] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y).
[15] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026.
[16] G. Baranes *et al.*, “Leveraging Qubit Loss Detection in Fault-Tolerant Quantum Algorithms,” *Phys. Rev. X*, vol. 16, no. 1, Art. no. 011002, Jan. 2026, doi: [10.1103/ycwc-3myc](https://doi.org/10.1103/ycwc-3myc). [arXiv:2502.20558](https://arxiv.org/abs/2502.20558).
[17] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661).
[18] B. W. Reichardt *et al.*, “Fault-tolerant quantum computation with a neutral atom processor,” [arXiv:2411.11822](https://arxiv.org/abs/2411.11822), Nov. 2024.
[19] W. Huang *et al.*, “Logical multi-qubit entanglement with dual-rail superconducting qubits,” *Nat. Phys.*, vol. 22, no. 4, pp. 591–597, Mar. 2026, doi: [10.1038/s41567-026-03211-9](https://doi.org/10.1038/s41567-026-03211-9). [arXiv:2504.12099](https://arxiv.org/abs/2504.12099).
[20] Quantum Circuits, “Quantum Circuits Makes Error-Detecting Qubits,” Nov. 19, 2024. [Online]. Available: https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/ [C]
[21] J. D. Teoh *et al.*, “Dual-rail encoding with superconducting cavities,” *Proc. Natl. Acad. Sci. USA*, vol. 120, no. 41, Art. no. e2221736120, Oct. 2023, doi: [10.1073/pnas.2221736120](https://doi.org/10.1073/pnas.2221736120). [arXiv:2212.12077](https://arxiv.org/abs/2212.12077).
[22] M. Swayne, “D-Wave's New Gate-Model Roadmap Puts Pin in 2032 For 100 Logical-Qubit System,” The Quantum Insider, Jun. 1, 2026. [Online]. Available: https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/ [P]
[23] J. W. Lis *et al.*, “Mid-circuit operations using the omg-architecture in neutral atom arrays,” [arXiv:2305.19266](https://arxiv.org/abs/2305.19266), May 2023.
[24] N. Liyanage, Y. Wu, A. Deters, and L. Zhong, “Scalable Quantum Error Correction for Surface Codes using FPGA,” [arXiv:2301.08419](https://arxiv.org/abs/2301.08419), Jan. 2023.
[25] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[26] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[27] S. Bartolucci *et al.*, “Fusion-based quantum computation,” *Nat. Commun.*, vol. 14, Art. no. 912, Feb. 2023, doi: [10.1038/s41467-023-36493-1](https://doi.org/10.1038/s41467-023-36493-1). [arXiv:2506.11975](https://arxiv.org/abs/2506.11975).
[28] M. Kang, W. C. Campbell, and K. R. Brown, “Quantum Error Correction with Metastable States of Trapped Ions Using Erasure Conversion,” *PRX Quantum*, vol. 4, no. 2, Art. no. 020358, Jun. 2023, doi: [10.1103/PRXQuantum.4.020358](https://doi.org/10.1103/PRXQuantum.4.020358). [arXiv:2210.15024](https://arxiv.org/abs/2210.15024).
[29] D-Wave Quantum Inc., “D-Wave Reports Second Quarter 2026 Results,” Aug. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ [C]
[30] Brookhaven National Laboratory, “DOE Renews Brookhaven Lab-led Quantum Research Center,” BNL Newsroom, Nov. 4, 2025. [Online]. Available: https://www.bnl.gov/newsroom/news.php?a=122687 [G]
[31] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [C]
[32] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406).
[33] US Department of Energy, “Energy Department Announces $625 Million to Advance the Next Phase of National Quantum Information Science Research Centers,” Energy.gov, Nov. 4, 2025. [Online]. Available: https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information [G]
[34] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[35] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[36] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]
[37] Justia, “Shruti PURI Inventions, Patents and Patent Applications - Justia Patents Search.” [Online]. Available: https://patents.justia.com/inventor/shruti-puri [G]

## Open verification items

- [[4,2,2]] erasure-information gain: 1.9(4)× in arXiv:2506.13724 v1 and v2 (2026-06-23) [D][8] versus 3.6× in the technology graph from Nature Physics 22, 910 [D][8]; published text paywalled; 1.9(4)× used.
- Gu, Retzker, Kubica [S][12]: thresholds published as surfaces, not single values; qualitative result only.
- Kang, Campbell, Brown [S][28]: PRX Quantum 4 (2023) article number not confirmed.
- No Princeton or Harvard erasure patent family found in two patent searches; absence not proven.
- planqc's and Google's neutral-atom species not confirmed from accessible sources; neither is claimed.
- FPGA decoding with erasure flags: no published benchmark; 11.5 ns per round [D][24] is for phenomenological noise.
- Cost or energy per logical qubit: unpublished by every actor.
- D-Wave's "$1.57 million in NSF funding for gate-model development" [C][29]: award not identified.
