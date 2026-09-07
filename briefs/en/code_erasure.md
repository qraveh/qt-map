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

An erasure-adapted code is a stabiliser code whose decoder takes, besides the syndrome, a per-qubit flag saying "this qubit was lost or left the code space here", with layout and schedule chosen for a channel in which located errors dominate. A located error removes the *which* question and leaves only the *what*, so the surface code fails only when erasures percolate — a 50% code-capacity threshold set by square-lattice bond percolation [S][7], against 18.9(3)% for depolarising noise [S][2] — and its distance against erasures is d rather than ⌈d/2⌉. Maximum-likelihood erasure decoding is linear-time peeling on a spanning forest [S][8]; Union-Find extends it to Pauli errors in O(n α(n)) [S][9]. The hardware turn came in 2022: 98% of ¹⁷¹Yb errors convertible, lifting the circuit-level surface-code threshold from 0.937% to 4.15% [S][1], and dual-rail transmons, where at 1% erasure the code tolerates 0.51% Pauli error, 5.2× the standard figure [S][2]; the first full loss-correction cycle had run on five trapped ions in 2020 [D][16]. The flags belong to the *Mid-circuit erasure check* brief (layer 6); this brief covers what the code does with them.

Coordinates (graph record; legend: a affinity natural↔fabricated; b time, deterministic/heralded entangling; c readout; d mobility; e control @ placement; f error structure; g manufacturing):
- a = 0.5 — carrier-agnostic; one decoder serves atoms and transmons.
- b = no time or entangling of its own.
- c = none — it consumes the check's flag.
- d = static.
- e = no control modality, no placement.
- f = erasure — located loss dominant, small Pauli residual.
- g = none — layout and software.
Rank 3 of 96; a hub reaching the neutral-atom and superconducting families; its off-diagonal cell pairs a fabricated carrier with an erasure error structure.

## Physics & limits

The gain has three parts, each taxed. Threshold: the converted fraction sets it. Wu's 4.15% assumes 98% conversion [S][1]; measured fractions are 56(4)% of single-qubit and ≈33% of two-qubit errors on ¹⁷¹Yb [D][37] and 38(6)% of Princeton's CZ error [D][12], so the realised threshold sits between the Pauli and erasure limits; biased-erasure XZZX codes lift the ceiling to 8.2%, hybrid-fusion to 10.3% [S][3]. Checks are not free: each exposes the qubit to T₁, and erasure qubits win only when the check is short against the cycle [S][5]; with false positives and negatives the threshold stays at least twice the Pauli value and the effective distance roughly doubled [S][6]. Erasures spread through gates, and a missed erasure re-enters as leakage, the error the surface code handles worst [S][4]. The idealised ceiling is Quantum Circuits' simulation: ancilla erasure 0.4%, data erasure 0.1%, dephasing 0.04/0.01/0.01% and perfect checks delayed to the end of each round give Λ ≈ 27 per distance step against Λ ≈ 14 for 0.1% depolarising noise [S][17]; Google's hardware surface code sits at Λ = 2.14(2) [D][20]. The bias behind such numbers is ≈40:1 — 6×10⁻³ erasure against 1.6×10⁻⁴ Pauli per operation [S][2] — matching AWS's measured 42(1) [D][18] [G:AWS-ERASURE-2026-04]. What moves the floor: conversion under two-qubit gates, the false-negative rate, check time, and decoders that use delayed loss information so no mid-circuit check is needed [S][11].

## Engineering state of the art

Best demonstrated, atoms: Harvard/MIT/QuEra's surface code on up to 448 atoms, 2.14(13)× below threshold in a four-round characterisation circuit, loss information plus machine-learning decoding giving 1.73(13)× over conventional decoding [D][14]; Princeton's [[4,2,2]] block, whose logical decay slows 1.9(4)× with erasure flags in the decoder [D][12]; Microsoft/Atom Computing's 24 logical qubits in 48 atoms with 1.8 lost atoms corrected per run [D][15]. Superconductors: no erasure-decoded code has run on dual-rail hardware as of 3 Sep 2026; the largest erasure-encoded circuits are SUSTech's four dual-rail transmons at 98.8% logical Bell fidelity [D][19] [G:SUSTECH-DUALRAIL-2025] and Quantum Circuits' 8-qubit Seeker, error-detecting only [C][32] [G:QCI-SEEKER-2024-11]. Typical at scale: only the Harvard and Microsoft machines decode with loss flags above 100 atoms.

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2009 | 50% loss threshold (bond percolation) | Stace/Barrett/Doherty | [S] | [7] |
| 2022-01 | Threshold 0.937% → 4.15% at 98% conversion | Princeton/Yale | [S] | [1] |
| 2022-08 | Dual-rail: 0.51% Pauli tolerated at 1% erasure, 5.2× | AWS | [S] | [2] |
| 2023-02 | XZZX biased erasure 8.2%; hybrid-fusion 10.3% | Yale/Princeton | [S] | [3] |
| 2024-11 | 24 logical in 48 atoms; 1.8 lost atoms corrected per run | Microsoft/Atom | [D] | [15] |
| 2025-06 | [[4,2,2]] decay 1.9(4)× slower with erasure flags | Princeton | [D] | [12] |
| 2025-06 | 2.14(13)× below threshold; loss info + ML 1.73(13)× | Harvard/QuEra | [D] | [14] |
| 2026-08 | Λ ≈ 27 vs 14, structured dual-rail noise, perfect checks | QCI/D-Wave | [S] | [17] |

Dominant error term today: on atoms the unconverted two-qubit error, ≈62–67% of CZ error [D][12][37]; on dual-rail the ancilla's erasure per CZ, 0.400(4)%, and check dead time [D][17] [G:DUALRAIL-CZ-2026-08]; on both, a false-negative tail nobody has counted over many rounds.

## Manufacturing, materials & supply chain

Nothing is fabricated for the code; its burden lands on the hardware it selects. Dual-rail asks for two good transmons or two cavities per site — a yield-squared problem — plus an ancilla per cavity pair [S][23], hence Quantum Circuits' hand-assembled 8 → 17 → 49 → 181 plan [R][33] [G:DWAVE-QCI-2026-01]. Alkaline-earth atoms add no hardware but cost single-qubit fidelity in the metastable manifold, 99.12(4)% against 99.968(3)% in the ground state of JILA's device [D][38]. The decoder is the code's only artefact: Union-Find on a Xilinx VCU129 decodes d = 21 at 11.5 ns per round under 0.1% phenomenological noise [D][22]; erasure input is native to Union-Find [S][9] but no FPGA benchmark with erasure flags is published; Stim exposes HERALDED_ERASE [P][31]. Unit cost: 2× physical qubits per site on dual-rail, against Quantum Circuits' claim of 10–20 physical per logical instead of ≈200 [C][32]. Export control: the BIS rule of 2024-09-06 [G][28] [G:BIS-QUANTUM-2024] controls computers of ≥34 qubits (4A906), software "specially designed" for developing or producing controlled qubit and control devices (4D906) and the related technology (4E906); a decoder shipped as firmware for a controlled control system falls inside 4D906.

## Control, readout & I/O burden

The code adds one bit per qubit per cycle to the syndrome stream and a decision: reset and re-entangle the erased qubit before the next round, or defer. On dual-rail that is feed-forward within ≈1 µs (0.50 µs gate, 0.38 µs check) [D][17][18]; on atoms a camera frame and a reload, ≈1 ms [D][14]. Delayed-erasure decoding [S][11] and superchecks [D][14] remove the mid-circuit branch at the price of correlated decoding. Walls: at 10³ the wall is the hardware's; at 10⁴ the decoder must absorb ≈10⁴ flags plus syndromes per microsecond — 10 Gbit/s, within FPGA reach [D][22] but untested with erasures; at 10⁶ dual-rail means 2×10⁶ transmons, and on atoms the frame budget of the *Mid-circuit erasure check* brief applies unchanged.

## Role in the stack

Two paths: superconducting dual-rail erasure (D-Wave/Quantum Circuits, AWS, SUSTech) and alkaline-earth neutral atoms (Atom Computing/Microsoft, Princeton, Caltech). The code requires the mid-circuit erasure check's flags, provides logical qubits to nothing yet registered downstream, and replaces the Pauli-decoded surface code. The price of switching is hardware, not software: 2× physical qubits and a check per cycle on dual-rail, the metastable fidelity tax on atoms, plus a decoder that weights erased edges to zero. It conflicts with nothing formally but competes with IBM's qLDPC memory for the same G4 budget [R][G:IBM-ROADMAP]. Hub reading: the atom and superconducting camps share one artefact, the decoder. Off-diagonal reading: a fabricated carrier with an erasure error structure is genuine on dual-rail; atoms bring erasure as a natural carrier and sit on the diagonal. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path: 2.8 µs on dual-rail (gate-limited, four 0.5 µs layers over the 0.40 µs check), 1.3 ms on atoms (transport); the code rides on the host code's d₂ and adds no term. Neighbouring slots: erasure-adapted qLDPC codes (no demonstration found), the cold-stage decoder, and, one column over, photonic fusion-based computation at 10.4% tolerated loss per fusion [S][21], where Xanadu reports loss 24.1× above threshold in 2026 [R][G:XANADU-SPAC-2026-03].

## Verification (QCVV)

Headline numbers are logical decay rates versus hold time decoded with and without flags (Princeton) [D][12], or detected-error ratios between distances in a four-round circuit (Harvard's 2.14(13)×) [D][14]; simulated Λ comes from Stim-style circuit noise with an assumed bias [S][17]. Not captured: post-selection — Princeton's teleportation fidelities, 0.771(9) → 0.802(8), are conditioned on trivial syndromes and a flag [D][12]; four rounds are not a memory over 10⁵ rounds; the Λ ≈ 27 simulation assumes perfect checks, no false negatives, no check-induced dephasing [S][17]; nobody reports survival beside Λ. Independent replications: Harvard/QuEra [D][14], Microsoft/Atom [D][15], Princeton [D][12]; theory from AWS [S][2][4][5], Yale [S][3][6], Duke [S][10]. Conflicts: (i) the [[4,2,2]] gain is 1.9(4)× in arXiv v1 and v2 (2026-06-23) [D][12] but 3.6× in the technology graph from the Nature Physics text [D][13] [G:PRINCETON-ERASURE-2026-06]; the published text is paywalled and 1.9(4)× is used. (ii) 98% conversion [S][1] against 38–56% measured [D][12][37]. (iii) Λ ≈ 27 [S][17] against Λ = 2.14(2) on the best Pauli-decoded hardware [D][20] — a simulation-to-hardware gap.

## Actors & economics

**Who.**

| Organisation | Role | Country | What it does with erasure-adapted codes | Evidence |
|---|---|---|---|---|
| Quantum Circuits (D-Wave unit) | developer | US | Dual-rail cavity qubits; Λ ≈ 27 simulation; 17-qubit system due 2026 | [D][17] [C][26] |
| AWS Center for Quantum Computing | developer | US | Dual-rail transmon theory and hardware; check-schedule optimisation | [S][2][5] [D][18] |
| Yale University | research | US | Biased-erasure XZZX codes; imperfect-check theory; C2QA partner | [S][3][6] [G][25] |
| Princeton University | research | US | ¹⁷¹Yb erasure conversion; first erasure-decoded logical qubit | [S][1] [D][12] |
| Harvard University | research | US | Loss-aware surface-code decoding on 448 atoms; delayed-erasure decoder | [D][14] [S][11] |
| QuEra Computing | developer | US | Libra 2028, >256 logical at 10⁻⁶; QBI Stage B | [R][27] [G:QBI-STAGEB-2025-11] |
| Atom Computing | developer | US | ¹⁷¹Yb machines; loss correction with Microsoft's decoder; Magne | [D][15] [G:MAGNE-2025-07] |
| Google Quantum AI | developer | US | Stim HERALDED_ERASE; Pauli-decoded baseline Λ = 2.14; atom track since 2026-03 | [P][31] [D][20] [G:GOOGLE-ATOMS-2026-03] |
| Caltech | research | US | ⁸⁸Sr erasure conversion; erasure-code theory | [D][36] [S][4] |

**Money.**
- 2024-08-15 · Quantum Circuits · Series B close · >$60 M · ARCH, F-Prime, Sequoia, Hither Creek · ≈$84 M cumulative per trade press · closed [G:QCI-FUNDING]
- 2025-11-04 · US DOE · NQISRC renewal, C2QA (Brookhaven/Yale) · $125 M of $625 M over up to five years · programme · awarded [G][24][25]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each · Atom Computing, QuEra among eleven; no dual-rail vendor · official [G][35] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · acquires Quantum Circuits · $550 M ($300 M stock + $250 M cash) · closed 2026-01-19/20 [C][34] [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; Atom Computing · US DoC CHIPS letters of intent · $100 M each · LOI [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · Series C · $100 M · Third Point · >$300 M cumulative · closed [G:ATOM-300M-2026-06]
- 2026-08-06 · D-Wave · Q2-2026 results · revenue $3.1 M, cash $546.2 M; $1.57 M NSF grant for gate-model work · reported [C][26] [G:DWAVE-FIN-2026]

**Market & supply chain.** Nobody sells an erasure-adapted code; the decoders are open-source (Stim, PyMatching, Union-Find) [P][31] and the FPGA implementations academic [D][22], so the money is in the hardware overhead: two transmons or two cavities plus an ancilla per site, or a metastable manifold and a camera. Concentration risk is the dual-rail readout chain and refrigerators, BIS-listed [G][28]; on atoms, the ¹⁷¹Yb/⁸⁸Sr laser set. G3 and G4 buy the full code; G2 and G1 pay today for erasure *detection* as post-selection (Seeker [C][32], Caltech's excised Rydberg simulator [D][36]); G5–G7 do not pay.

**IP & standards.** Amazon Technologies US 11,748,652 B1, heralded amplitude-damping decay for QEC (Kubica, Retzker; granted 2023-09-05) [G][29] [G:AMZN-ERASURE-PATENT]; Yale US 12,288,135, asymmetric-error-channel ancilla (granted 2025-04-29) [G][30]; Quantum Circuits' cavity families sit with D-Wave. No Princeton or Harvard erasure patent surfaced in the searches run; no database count found. No standard; Stim's HERALDED_ERASE [P][31] is the de-facto interface; D-Wave announced a forthcoming gate-model simulator for "error-aware programming" [C][26].

**Roadmaps & track record.**
- D-Wave: promised 2026-01-07 · first dual-rail system in 2026 · not delivered as of 2026-09-03; restated 2026-08-06 as a 17-qubit system with logical error 2× below physical in 2026 [C][34][26].
- D-Wave: promised 2026-06-01 · 49 qubits / 20× (2027), 181 / 2,000× (2028), 10 logical (2030), 100 logical (2032), Λ = 10 · pending [R][33] [G:DWAVE-QCI-2026-01].
- QuEra: promised 2024-01 · 100 logical qubits in 2026 · missed; restated 2026-06-15 as Libra, >256 logical at 10⁻⁶ in 2028 [R][27] [G:QUERA-LIBRA-2026].
- Atom Computing/Microsoft: promised 2025-07-17 · Magne, 50 logical qubits, delivery around the turn of 2026/27 · pending [G:MAGNE-2025-07].
Credibility: Quantum Circuits/D-Wave publish the physics and miss the dates; Harvard/QuEra deliver papers on schedule, roadmaps late; Microsoft/Atom on schedule, silent on the code; AWS publishes and promises nothing; Princeton delivers each step of its 2022 proposal [S][1], smaller than promised.

**Strategic reading.** If erasure-adapted codes reach Λ ≥ 5 on hardware, the winners own erasure-native qubits at scale — D-Wave's cavity line, AWS's transmon pairs, the ¹⁷¹Yb camp (Atom Computing, Google's atom track) — and the decoder becomes a commodity; the losers are Pauli-only roadmaps buying Λ with fidelity alone (Google's superconducting line, IBM's qLDPC) and rubidium vendors without a metastable manifold. Substitution runs both ways: delayed-erasure decoding [S][11] and superchecks [D][14] give atoms most of the gain without erasure-native qubits; qutrit erasure encodings would strip the 2× overhead from transmons. Bargaining power sits with platform vendors; decoder authors have none.

*Open niche:* a small QCVV/SFQ research company could plug in at the decoder's input: a survival-corrected Λ benchmark reporting logical error, post-selection fraction and false-negative leakage together, run on Stim circuits with HERALDED_ERASE for dual-rail and atom groups alike; the SFQ angle is a cold-stage Union-Find front end clustering erased edges at zero weight before the syndrome leaves the fridge.

## Outlook & open questions

Confirm within 12–24 months if: any group decodes a d = 3 → 5 memory with erasure flags over ≥ 10 rounds and reports Λ ≥ 3 with survival; D-Wave's 17-qubit system shows logical error 2× below physical by mid-2027 [C][26]; a dual-rail simulation with measured false negatives and check dephasing still returns Λ ≥ 10; atom conversion under two-qubit gates passes 70%. Demote if end-2027 arrives with erasure decoding worth < 2× on every platform. Best case by 2029: dual-rail memories at Λ ≈ 5–10 with 100–200 qubits and Yb machines running loss-aware codes by default. Worst case: a decoder option worth 1.7–1.9× while Pauli-decoded transmons reach Λ ≈ 3–4 without it.

Open questions: (1) what is Λ once false negatives accumulate as leakage over 10³ rounds? (2) does the 40:1 bias survive parallel gates on shared readout lines? (3) can the metastable fidelity tax on Yb be removed? (4) is an erasure-adapted qLDPC code with a fast decoder possible? Watch: D-Wave's 2026 delivery, AWS's next multi-qubit paper, Google/Kaufman's Yb results.

## Sources

[1] Wu, Y., Kolkowitz, S., Puri, S., Thompson, J. D. · Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays · Nature Communications 13, 4657 (arXiv:2201.03540) · 2022-01 · https://arxiv.org/abs/2201.03540
[2] Kubica, A., Haim, A., Vaknin, Y., Brandão, F., Retzker, A. (AWS) · Erasure qubits: Overcoming the T1 limit in superconducting circuits · Phys. Rev. X 13, 041022 (arXiv:2208.05461) · 2022-08-10 · https://arxiv.org/abs/2208.05461
[3] Sahay, K., Jin, J., Claes, J., Thompson, J. D., Puri, S. · High threshold codes for neutral atom qubits with biased erasure errors · Phys. Rev. X 13, 041013 (arXiv:2302.03063) · 2023-02-06 · https://arxiv.org/abs/2302.03063
[4] Gu, S., Retzker, A., Kubica, A. · Fault-tolerant quantum architectures based on erasure qubits · Phys. Rev. Research 7, 013249 (arXiv:2312.14060) · 2023-12-21 · https://arxiv.org/abs/2312.14060
[5] Gu, S., Vaknin, Y., Retzker, A., Kubica, A. · Optimizing quantum error-correction protocols with erasure qubits · PRX Quantum 6, 040354 · 2025-12-04 · https://journals.aps.org/prxquantum/abstract/10.1103/985g-58gd
[6] Chang, K., Singh, S., Claes, J., Sahay, K., Teoh, J., Puri, S. (Yale / Quantum Circuits) · Surface code with imperfect erasure checks · PRX Quantum 6, 040355 · 2025-12-04 · https://journals.aps.org/prxquantum/abstract/10.1103/d1v7-nctj
[7] Stace, T. M., Barrett, S. D., Doherty, A. C. · Thresholds for topological codes in the presence of loss · Phys. Rev. Lett. 102, 200501 (arXiv:0904.3556) · 2009-04 · https://arxiv.org/abs/0904.3556
[8] Delfosse, N., Zémor, G. · Linear-time maximum likelihood decoding of surface codes over the quantum erasure channel · Phys. Rev. Research 2, 033042 (arXiv:1703.01517) · 2017-03 · https://arxiv.org/abs/1703.01517
[9] Delfosse, N., Nickerson, N. H. · Almost-linear time decoding algorithm for topological codes · Quantum 5, 595 (arXiv:1709.06218) · 2017-09 · https://arxiv.org/abs/1709.06218
[10] Kang, M., Campbell, W. C., Brown, K. R. · Quantum error correction with metastable states of trapped ions using erasure conversion · PRX Quantum 4 (arXiv:2210.15024) · 2023-07-03 · https://arxiv.org/abs/2210.15024
[11] Baranes, G., Cain, M., Bonilla Ataides, J. P., Bluvstein, D., Sinclair, J., Vuletić, V., Zhou, H., Lukin, M. D. (Harvard) · Leveraging atom loss errors in fault tolerant quantum algorithms · Phys. Rev. X 16, 011002 (arXiv:2502.20558) · 2025-02-27 · https://arxiv.org/abs/2502.20558
[12] Zhang, B. et al. (Princeton / Yale) · Logical qubits with erasure conversion using metastable neutral atoms · arXiv:2506.13724 v2 · 2026-06-23 · https://arxiv.org/html/2506.13724
[13] Zhang, B. et al. (Princeton / Yale) · Logical qubits with erasure conversion using metastable neutral atoms · Nature Physics 22, 910–916 · 2026-06-12 · https://www.nature.com/articles/s41567-026-03309-0
[14] Bluvstein, D. et al. (Harvard / MIT / QuEra) · A fault-tolerant neutral-atom architecture for universal quantum computation (arXiv: Architectural mechanisms of a universal fault-tolerant quantum computer) · Nature 649, 39–46 (arXiv:2506.20661) · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[15] Reichardt, B. W. et al. (Microsoft / Atom Computing) · Fault-tolerant quantum computation with a neutral atom processor · arXiv:2411.11822 (v3 2025-06-09) · 2024-11-18 · https://arxiv.org/abs/2411.11822
[16] Stricker, R. et al. (University of Innsbruck) · Experimental deterministic correction of qubit loss · Nature 585, 207–210 (arXiv:2002.09532) · 2020-09-09 · https://www.nature.com/articles/s41586-020-2667-0
[17] Quantum Circuits / D-Wave Quantum · An entangling gate for dual-rail erasure qubits · Nature 656, 47–53 (arXiv:2503.10935) · 2026-08-05 · https://www.nature.com/articles/s41586-026-10822-y
[18] Hung, J. S.-C. et al. (AWS Center for Quantum Computing) · Fast, high-fidelity erasure detection of dual-rail qubits with symmetrically coupled readout · arXiv:2604.16292 · 2026-04-17 · https://arxiv.org/abs/2604.16292
[19] Huang, W. et al. (SUSTech) · Logical multi-qubit entanglement with dual-rail superconducting qubits · arXiv:2504.12099; Nature Physics 2026, doi:10.1038/s41567-026-03211-9 · 2025-04-16 · https://arxiv.org/abs/2504.12099
[20] Google Quantum AI · Quantum error correction below the surface code threshold · Nature 638, 920–926 · 2024-12-09 · https://www.nature.com/articles/s41586-024-08449-y
[21] Bartolucci, S. et al. (PsiQuantum) · Fusion-based quantum computation · Nature Communications 14, 912 (arXiv:2101.09310) · 2021-01-22 · https://arxiv.org/abs/2101.09310
[22] Liyanage, N., Wu, Y., Deters, A., Zhong, L. (Yale) · Scalable quantum error correction for surface codes using FPGA · arXiv:2301.08419 · 2023-01-20 · https://arxiv.org/abs/2301.08419
[23] Teoh, J. D. et al. (Yale) · Dual-rail encoding with superconducting cavities · PNAS 120, e2221736120 (arXiv:2212.12077) · 2023-10-17 · https://arxiv.org/abs/2212.12077
[24] [G] US Department of Energy · Energy Department Announces $625 Million to Advance the Next Phase of National Quantum Information Science Research Centers · energy.gov · 2025-11-04 · https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information
[25] [G] Brookhaven National Laboratory · DOE Renews Brookhaven Lab-led Quantum Research Center (C2QA, $125 M over five years) · BNL newsroom · 2025-11-04 · https://www.bnl.gov/newsroom/news.php?a=122687
[26] [C] D-Wave Quantum · D-Wave Reports Second Quarter 2026 Results · company press release · 2026-08-06 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/
[27] [C] QuEra Computing · QuEra Announces 2028 Fault-Tolerant Quantum Computer (Libra) and Expanded Multi-Year Strategic Collaboration with AWS · company press release · 2026-06-15 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[28] [G] US Bureau of Industry and Security · Commerce Control List Additions and Revisions: Implementation of Controls on Advanced Technologies Consistent with Controls Implemented by International Partners (ECCNs 4A906, 4D906, 4E906) · Federal Register 2024-19633 · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[29] [G] USPTO (via Google Patents) · US 11,748,652 B1, Heralding of amplitude damping decay noise for quantum error correction, Amazon Technologies, Inc. (Kubica, Retzker) · patent, filed 2021-12-10 · granted 2023-09-05 · https://patents.google.com/patent/US11748652B1/en
[30] [G] USPTO (via Justia Patents) · US 12,288,135, Quantum information processing with an asymmetric error channel, Yale University · patent, filed 2019-06-28 · granted 2025-04-29 · https://patents.justia.com/inventor/shruti-puri
[31] [P] quantumlib/Stim · Gate reference: HERALDED_ERASE, HERALDED_PAULI_CHANNEL_1 · GitHub documentation · accessed 2026-09-03 · https://github.com/quantumlib/Stim/blob/main/doc/gates.md
[32] [C] Quantum Circuits · Quantum Circuits make error-detecting qubits (Aqumen Seeker) · company newsroom · 2024-11-19 · https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/
[33] [P] The Quantum Insider · D-Wave's New Gate-Model Roadmap Puts Pin in 2032 for 100-Logical-Qubit System · trade press · 2026-06-01 · https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/
[34] [C] D-Wave Quantum · D-Wave to Acquire Quantum Circuits Inc. · company press release · 2026-01-07 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[35] [G] DARPA · Quantum Benchmarking Initiative — Stage B selection · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[36] Scholl, P. et al. (Caltech) · Erasure conversion in a high-fidelity Rydberg quantum simulator · Nature 622, 273 (arXiv:2305.03406) · 2023-05-05 · https://arxiv.org/abs/2305.03406
[37] Ma, S. et al. (Princeton) · High-fidelity gates and mid-circuit erasure conversion in an atomic qubit · Nature 622, 279 (arXiv:2305.05493) · 2023-10-11 · https://arxiv.org/abs/2305.05493
[38] Lis, J. W. et al. (JILA) · Mid-circuit operations using the omg-architecture in neutral atom arrays · Phys. Rev. X 13, 041035 (arXiv:2305.19266) · 2023-05-30 · https://arxiv.org/abs/2305.19266

## Open verification items

- [[4,2,2]] erasure-information gain: 1.9(4)× in arXiv:2506.13724 v1 and v2 (2026-06-23) [D][12] versus 3.6× in the technology graph from Nature Physics 22, 910 [D][13]; published text paywalled; 1.9(4)× used.
- Gu, Retzker, Kubica [S][4]: thresholds published as surfaces, not single values; qualitative result only.
- Kang, Campbell, Brown [S][10]: PRX Quantum 4 (2023) article number not confirmed.
- No Princeton or Harvard erasure patent family found in two patent searches; absence not proven.
- planqc's and Google's neutral-atom species not confirmed from accessible sources; neither is claimed.
- FPGA decoding with erasure flags: no published benchmark; 11.5 ns per round [D][22] is for phenomenological noise.
- Cost or energy per logical qubit: unpublished by every actor.
- D-Wave's "$1.57 million in NSF funding for gate-model development" [C][26]: award not identified.
