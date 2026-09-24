---
id: ae_atom
name: Alkaline-earth atom (Yb/Sr) — erasure-native
layer: "1 Carrier"
status: demonstrated
since: 2019
one_line: Ytterbium/strontium tweezer qubits whose metastable clock manifold makes decay and loss optically detectable, converting physical errors into heralded erasures rather than silent Pauli errors.
verdict: Erasure conversion is real and internally consistent (1.9(4)× unconditional decay suppression), but the metastable encoding costs ~6× in CZ error and is unreplicated outside Princeton and Caltech.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
¹⁷¹Yb and ⁸⁷Sr have two valence electrons: a seconds-scale ³P₀/³P₂ metastable triplet above the ¹S₀ ground singlet, on a narrow clock line (578 nm Yb, 698 nm Sr). A ground-manifold imaging beam is dark to a metastable-manifold qubit, so decay and loss scatter photons while the code space stays quiet — the "omg" (optical–metastable–ground) scheme, from a 2021 ion-trap blueprint [D][1]. Errors then arrive located, as erasures, not silent Pauli flips. Demonstrated in Yb (Princeton) and Sr (Caltech), May 2023 [D][2], [3].
Attributes: natural carrier; deterministic Rydberg-blockade entanglement ~250 ns; fluorescence readout ~0.5 ms, non-destructive, mid-circuit-capable.
Optical control from room temperature; error structure erasure and loss, not native Pauli; manufacture by optical assembly, not lithography.

## Physics & limits
Erasure conversion relabels error rather than reducing it; the payoff is in the decoder — at 1% erasure the erasure-aware surface code tolerates Pauli error to 0.51%, 5.2× the standard protocol [D][4]. The gate floor sits elsewhere: Rydberg-blockade CZ runs in a few hundred nanoseconds against Rydberg spontaneous plus blackbody decay (0.05–0.1%), laser phase noise (0.1–0.2%) and thermal motion (~0.1%), which a 2026 review argues caps the standard scheme near 99.9% absent a new gate mechanism [P][5]. Atom loss is over 80% of leakage events [D][6] — precisely what omg sees. Moving the floor needs a cryogenic enclosure against blackbody-driven Rydberg decay, lower trap-light scattering out of the metastable manifold (it sets the check interval), and imaging that spares neighbouring sites.

## Engineering state of the art
| Year | Figure | Who | Tag/key |
|---|---|---|---|
| 2023-05 | 56% of 1Q errors → erasures, ¹⁷¹Yb (98% ceiling) | Princeton | [D][2] |
| 2024-07 | Sr CZ 99.71% | Caltech | [D][7] |
| 2024-11 | Yb CZ 99.72% post-selected / 99.40% raw | Atom Computing | [D][8] |
| 2026-06 | Metastable CZ error 0.016(1), 38(6)% flagged; [[4,2,2]] decay 1.9(4)× slower | Princeton | [D][9][G:PRINCETON-ERASURE-V2-2026-06] |
| 2026-08 | 17.6 µs imaging, 99.89(5)% discrimination, 98.80(44)% survival, ¹⁷⁴Yb | Kyoto/Yaqumo | [P][10][G:KYOTO-FASTIMG-2026-08] |

The dominant term is the gate, not the erasure machinery: Princeton's metastable CZ error 0.016(1) is ~6× Atom Computing's raw ground-state Yb CZ of 0.0060 [D][8], [9], and only ~38% of it returns as flags. The 17.6 µs record is spinless ¹⁷⁴Yb, not ¹⁷¹Yb readout, so 0.5 ms stays the honest cycle.

## Manufacturing, materials & supply chain
No lithographic chip: the fab is a UHV chamber, a high-NA objective, SLM/AOD steering and clock, Rydberg, imaging and shelving lasers; yield is per-site loading probability plus SLM-aberration trap non-uniformity. Optics is the cost driver — Fraunhofer ILT's 2026 system makes 2,000 controllable Rydberg tweezers from four beams totalling 20 W [D][G:FRAUNHOFER-TWEEZER-2026-07], about 10 mW per site, so 10⁴ sites is a 100 W-class laser problem [S]. The thin points are not foundries: two crossed-AOD vendors appear anywhere in the literature (AA Opto-Electronic, Gooch & Housego) [D][G:AOD-VENDORS-2026] and Hamamatsu's SLM and camera line has no identified alternative [P][G:HAMAMATSU-CAMERA-CONC-2026]. Export exposure is at system level: ECCN 4A906 controls quantum computers above a qubit-count and error-rate threshold (in force 2024-09-06, Licence Exception IEC for partners); no ECCN names tweezer optics, AODs or UHV chambers [G][11][G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden
Addressing is AOD/SLM tweezers plus global clock and Rydberg beams; readout is imaging at 0.5–1 ms. A mid-circuit erasure check must be manifold-selective and must not heat the neighbours it illuminates — the constraint holding demonstrated conversion at 38–56% rather than the 98% ceiling [D][2], [9]. Global beams plus AOD addressing suffice at 10³ sites; at 10⁴ the ~10 MHz AOD/SLM refresh bottlenecks parallel local operations and trap power crosses 100 W; at 10⁶ no path exists short of metasurface or photonic delivery.

## Role in the stack
This carrier defines the "Neutral atoms — alkaline-earth (Yb/Sr), erasure-native" path (Atom Computing/Microsoft, Princeton, Caltech): optical assembly only, no foundry and no cryostat, hence no CHIPS-style capital wall. It feeds Rydberg-blockade CZ, the omg encoding, imaging readout, fast (≤20 µs) array readout and the atom–photon cavity interface. It replaces alkali species; a Rb incumbent's switching cost is a new laser and imaging system. Derived clock = sum of the syndrome round (gates 1 µs, transport 800 µs, 1Q 0.34 µs, readout 501 µs) = 1.3 ms, transport-limited, against the measured ~1–4 ms round. The salient empty slot is an erasure-aware real-time decoder fed by live array syndromes.

## Verification (QCVV)
Fractions come from state-selective fluorescence after gates; CZ fidelity from randomized benchmarking or tomography, reported raw and post-selected on the flag. A code spends a correction cycle on every heralded erasure, so raw numbers govern cost. The 1.9(4)× vs 3.6× conflict resolves inside arXiv:2506.13724v2: both figures are in that paper and describe different quantities — decay is 3.6(1)× slower during hold for the post-selected logical qubit, 1.9(4)× slower under unconditional decoding with erasure information [D][9]. Only 1.9(4)× is architecturally meaningful; the Nature Physics text is paywalled [9]. The 56% (1Q, 2023) and 38(6)% (CZ, 2026) figures are different metrics and must not be averaged. No independent replication was found.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Atom Computing | developer | US | Ships ¹⁷¹Yb arrays; 1,225-site Magne | [C][12] |
| Princeton University | research | US | Originated Yb erasure conversion; [[4,2,2]] logical qubit | [D][2], [9] |
| Caltech | research | US | Sr erasure excision; 99.71% CZ | [D][3], [7] |
| Microsoft | developer | US | Co-sells Magne; QEC and decoder stack | [C][13] |
| Hamamatsu Photonics | supplier | JP | SLM and camera; sole identified source | [P][14] |
| US Dept of Commerce | regulator | US | CHIPS LOI; ECCN 4A906 | [G][11], [15] |

**Money.**
2025-07-17 · QuNorth · "Magne" order, 1,225 physical / 50 logical, from Atom Computing/Microsoft · €80 M · EIFO + Novo Nordisk Foundation · ordered [C][13][G:MAGNE-2025-07]
2025-11-06 · Atom Computing · DARPA QBI Stage B · up to $15 M · DARPA · awarded [G][16][G:QBI-STAGEB-2025-11]
2026-05-21 · Atom Computing · CHIPS letter of intent · $100 M · US DoC, $2.013 B package · LOI [G][15][G:CHIPS-LOI-2026-05]
2026-06-16 · Atom Computing · Series C · $100 M · Third Point · cumulative > $300 M · closed [C][12][G:ATOM-300M-2026-06]

**Market & supply chain.** Specialty optics, not silicon: narrow-linewidth lasers, crossed AODs (two vendors named anywhere), SLMs and cameras (one), UHV chambers. No $/qubit is public; QuNorth's €80 M for 1,225 physical / 50 logical implies ≈ €65 k per site and ≈ €1.6 M per logical qubit [C][13]. G3 pays for this node, G4 conditionally, G1 shared with Rb arrays.

**IP & standards.** No dated patent family specific to alkaline-earth erasure encoding was found; the nearest grant is Amazon's US 11,748,652 B1 (2023-09-05), heralding amplitude-damping decay on dual-rail superconducting embodiments, not atoms [G][17][G:AMZN-ERASURE-PATENT]. No standards activity identified.

**Roadmaps & track record.** Magne, 50 logical (promised 2025-07-17 · for turn of 2026/27 · no completion announcement as of 4 Sep 2026) [R][13]; QuEra, 100 logical (2024-01 · for 2026 · became Libra, >256 logical, 2028) [R][18]; Pasqal, 10,000 physical (2024-03 · for 2026 · slipped to 2028, SPAC-funded ~$360 M) [R][19]. Princeton is peer-reviewed and self-consistent; Atom Computing ships hardware but saw suppression vanish once reloading was included [D][20].

**Strategic reading.** If erasure bias holds at code distance, Yb/Sr gains a structural overhead edge toward G3/G4 over Rb incumbents, who must pivot lasers and imaging or invent native-Rb heralding; Google's undeclared species is the tell [C][21]. Optics suppliers win either way, so the AOD and camera duopolies hold the durable bargaining power. The substitution threat is superconducting dual-rail erasure on a ~500 ns clock, D-Wave's $550 M purchase of Quantum Circuits being the bet [C][G:DWAVE-QCI-2026-01].

*Open niche:* independent verification of conversion fractions under realistic gate sequences — reconciling 1Q (56%), CZ-embedded (38(6)%) and post-selected-versus-unconditional reporting into one code-agnostic erasure-bias factor, and measuring its decay under reloading — is a gap none of Atom Computing, Princeton or Caltech fills.

## Outlook & open questions
Milestones (12–24 months): Magne shows 50 logical qubits under erasure-biased decoding in situ, not post-selected (confirm); an outside group replicates >50% 1Q conversion (confirm); a real-time decoder consumes array erasure flags inside the cycle budget (confirm) — or conversion vanishes under reloading as Λ did (demote). Best case 2029: erasure-native arrays underpin a >100-logical-qubit machine with validated overhead reduction; worst case, conversion stays a single-gate effect and the millisecond cycle decides the platform. Open questions: does conversion survive ms-scale reloading; can the metastable encoding recover its 6× gate deficit; does trap power or AOD bandwidth bind first above 10⁴. Watch: Magne acceptance, Google's species choice, the first non-Princeton replication.

## Sources
[1] D. T. C. Allcock *et al.*, “omg blueprint for trapped ion quantum computing with metastable states,” *Appl. Phys. Lett.*, vol. 119, no. 21, Art. no. 214002, Nov. 2021, doi: [10.1063/5.0069544](https://doi.org/10.1063/5.0069544). [arXiv:2109.01272](https://arxiv.org/abs/2109.01272).
[2] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493).
[3] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406).
[4] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461).
[5] J. Wang, Z. Wang, L. Li, F. Wang, S. Liang, and K. Yan, “Neutral Atom Quantum Computing: Principles, Routes, Progress, and Challenges,” [arXiv:2608.05010](https://arxiv.org/abs/2608.05010), Aug. 2026. [P]
[6] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661).
[7] R. B.-S. Tsai, X. Sun, A. L. Shaw, R. Finkelstein, and M. Endres, “Benchmarking and linear response modeling of high-fidelity Rydberg gates,” [arXiv:2407.20184](https://arxiv.org/abs/2407.20184), Jul. 2024.
[8] J. A. Muniz *et al.*, “High-fidelity universal gates in the ¹⁷¹Yb ground state nuclear spin qubit,” [arXiv:2411.11708](https://arxiv.org/abs/2411.11708), Nov. 2024.
[9] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0).
[10] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[11] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[12] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[13] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [C]
[14] M. Abdel-Kareem, “Hamamatsu Photonics, NKT Photonics, and Yaqumo Form Alliance to Industrialize Cold-Atom Quantum Core Components,” Quantum Computing Report, Jun. 4, 2026. [Online]. Available: https://quantumcomputingreport.com/hamamatsu-photonics-nkt-photonics-and-yaqumo-form-alliance-to-industrialize-cold-atom-quantum-core-components/ [P]
[15] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[16] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[17] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]
[18] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [C]
[19] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[20] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026.
[21] H. Neven, “Building superconducting and neutral atom quantum computers,” Google, Mar. 24, 2026. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]

## Open verification items
The published Nature Physics version of the Princeton [[4,2,2]] result could not be read (paywalled); the 1.9(4)× / 3.6(1)× reconciliation rests on arXiv v2 [9], where both numbers appear with distinct definitions. No independent replication of either the 56% or the 38(6)% conversion fraction was found. Magne's installation status beyond the 2025-07-17 order announcement is unconfirmed. The ≈10 mW/site trap-power extrapolation to 10⁴ sites is derived from the Fraunhofer figures, not measured [S]. No ECCN names tweezer optics, AODs or UHV chambers; only the finished system is controlled.
