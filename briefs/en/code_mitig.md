---
id: code_mitig
name: Error mitigation in the code slot (ZNE, PEC) — not a code
layer: "7 Code"
status: demonstrated
since: 2017
one_line: "Classical post-processing of many noisy runs — zero-noise extrapolation, probabilistic error cancellation or amplification, readout twirling, tensor-network noise inversion — that removes bias from expectation values without encoding, detecting or correcting a single error."
verdict: "The only error handling in most utility-scale superconducting experiments, including two of IBM's three July-2026 advantage claims; it buys bias reduction at a shot cost exponential in the circuit's error mass and yields no logical qubit, so as of 2026-09-26 it is a placeholder for a code, not a step towards one."
updated: 2026-09-26
---

ZNE = zero-noise extrapolation; PEC = probabilistic error cancellation; PEA = probabilistic error amplification; TREX = twirled readout error extinction; TEM = tensor-network error mitigation; γ = norm of the signed mixture that inverts the noise; P = summed Pauli error probability in an observable's backward light cone (the gates that can affect it); CZ = controlled-Z; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Error mitigation estimates an observable's noiseless expectation value from many noisy runs and classical post-processing; nothing is encoded, no syndrome is measured, no error corrected [G][719]. Temme, Bravyi and Gambetta proposed extrapolation to zero noise by Richardson's method and cancellation by quasi-probability resampling in 2016 [D][720]; Li and Benjamin independently extrapolated boosted errors to zero [D][721]. Hardware ZNE followed in 2019 [D][722]; then PEA, amplifying a learned noise model with injected Pauli errors [D][234], TREX for readout [C][719] and TEM, a tensor-network inverse of the global noise [S][723]. Attributes: platform-agnostic, static, no transport or control modality; Pauli error class after twirling.

## Physics & limits
PEC writes each layer's inverse noise as a signed mixture of implementable operations of norm γ ≥ 1; the estimate is unbiased, but shots grow as γ² and γ exponentially with depth [C][719]. For Pauli noise γ ≈ e^(2P), so shots multiply by ≈ e^(4P) [S]. At Heron r3's median CZ error of 0.15% [D][724], 1,000 CZs in the light cone give P ≈ 1.5 and ≈ 400× the shots, 7,500 give ~10¹⁹× [S]; today's 10²–10³× budgets cap P near 1.2–1.7 [S]. ZNE samples at amplified noise — by default three factors, nominally ~3× [C][719] — and extrapolates; it is biased by its fit and must resolve a signal attenuated by up to e^(−2P), so its cost grows comparably [S]. TEM claims the square root of PEC's overhead [S][723], still exponential [S]. The limit is general: overhead grows exponentially with depth for any protocol under local depolarising noise [D][725], nonlinear post-processing included [D][726], and worst-case estimation needs superpolynomially many samples at shallow depth [D][727]. Only lower physical error moves the exponent.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2019-03-27 | ZNE by stretched pulses; variational chemistry and magnetism | IBM, Kandala et al. | [D][722] |
| 2023-05-08 | PEC with a learned sparse Pauli–Lindblad model, crosstalk included, 20 qubits | IBM, van den Berg et al. | [D][728] |
| 2023-06-14 | 127 qubits, up to 60 layers, 2,880 CNOTs; ZNE with PEA | IBM Eagle, Kim et al. | [D][234] |
| 2023-06/08 | Classical reproductions: tensor network more accurate than the hardware; Pauli dynamics on one laptop core; converged to <0.01 | Tindall et al.; Begušić, Chan; Begušić, Gray, Chan | [D][235][D][729][D][730] |
| 2025-11-12 | "samplomatic" cuts PEC sampling overhead 100× | IBM | [C][373] |
| 2026-07-27 | QESEM (PEC- and ZNE-based) on Heron r3, 51–74 qubits, up to 30 Floquet cycles; tensor networks fail to converge | Qedma, RIKEN, BlueQubit | [D][196] |
| 2026-07-28 | PEC on 56 qubits, circuits up to ~1,000 CZs: ~1.5 h and ~4 h of QPU time at two depths | Algorithmiq et al., ibm_boston | [D][724] |
| 2026-08-31 | PEA observable estimation on 7,500-gate circuits | IBM Nighthawk r2 | [C][697] |

The 2023 claim of accuracy "beyond brute-force classical computation" [D][234] was matched classically within weeks, and converged values exposed bias in its extrapolation [D][730]; the 2026 claims rest on classical heuristics disagreeing, not on proven hardness [D][724]. Dominant term: P. Faster shots — Nighthawk r2's 100,000 circuits per second, 25× Heron — shorten wall-clock time, not the exponent [C][697].

## Manufacturing, materials & supply chain
Nothing is fabricated; the bill is QPU time and classical compute — 3.2 million shots, ~45 min of QPU time per point for Algorithmiq's rescaled estimate [D][724]. Supply is the vendor runtime [C][719] plus Qedma's QESEM, which learns device noise, adapts circuits and post-processes [C][731], and Algorithmiq's TEM in IBM's Qiskit Functions Catalog [C][732].

## Control, readout & I/O burden
The requirement is a calibrated, stable noise model: PEA and PEC learn a sparse Pauli–Lindblad model per layer of entangling gates under random Pauli twirling [D][234][D][728]; every circuit is compiled in many randomised instances [S]. TREX randomises measurements with X gates and classical bit flips, diagonalising the readout matrix for inversion [C][719]. Drift is the failure mode: a model learned before a four-hour PEC run is wrong by whatever drifts during it [S]. There is no feed-forward, and the output is expectation values, not samples [G][719].

## Role in the stack
Slot 7 of the Transmon lattice with tunable couplers path, beside code_surface, code_color, code_qldpc, code_magic and code_detect. It **requires** ct_rt, for calibrated noise models; it **provides** nothing downstream — no logical qubit, no syndrome for slot 8's decoders; it is **replaced** by code_surface, and the open conflict edge (2023-06) lists no remedy for its exponential overhead. code_detect discards flagged runs at a cost of 1/acceptance, also exponential in circuit size; mitigation keeps every run and reweights, removing bias only on average [S]. The gap ledger's "all three IBM July-2026 advantage claims" is two of three — QESEM on Heron r3 [D][196] and PEC on ibm_boston [D][724]; IBM–UChicago's post-selects on spacetime codes, a code_detect result [C][44]. The ledger's ion placement was not taken, though Qedma repeated cycles on Quantinuum H2 and Helios [D][196]. Register: IBM Eagle r1–r3 (primary, retired); Heron r1 and r3, Nighthawk r1 and r2, Zuchongzhi 3.0, Tianyan-287 (alternate).

## Verification (QCVV)
PEC is unbiased, with error bars, if its noise model is right, so verification becomes validating the model [C][44]. One of seven register cells is verified ✅ (Nighthawk r2, with a section locator); six are 🔎. Eagle's source supports its cell; Heron r1 and r3 cite a press article on r3 that names no mitigation method [P][733], and the July-2026 ibm_boston preprints are r3's missing primary evidence; Nighthawk r1 cites the r2 blog. Zuchongzhi 3.0 and Tianyan-287 run random-circuit sampling scored on raw fidelity; their abstracts mention neither mitigation nor correction [D][34][D][734], so as of 2026-09-26 their code slot is empty, not mitigated.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IBM | developer | US | TREX, ZNE, PEA, PEC in Qiskit Runtime; 2023 utility experiment; PEA at 7,500 gates | [C][719][D][234][C][697] |
| Qedma | software vendor | IL | QESEM: noise learning, PEC- and ZNE-based estimators | [D][196] |
| Algorithmiq | software vendor | IT (formerly FI) | TEM in IBM's catalogue; PEC in the Loschmidt-echo claim | [C][732][D][724] |
| Flatiron Institute | research | US | Contributor to the open advantage tracker | [C][373] |

**Money.**
- 2025-07-03 · Qedma · Series A led by Glilot Capital Partners, IBM participating · USD 26 M · announced [C][731]
- 2026-05-11 · Algorithmiq · round led by United Ventures, with CDP and Inventure · EUR 18 M (EUR 36 M in total) · announced [C][735]

**Market & supply chain.** Sold as runtime options and third-party functions on the hardware vendor's cloud, with IBM holding equity in Qedma: a vertically tied market. It pays into G2 only; G3–G4 need a code.

**IP & standards.** No standard defines a figure of merit for mitigated estimates or a noise-model disclosure format; no dated patent count from a named database, as of 2026-09-26.

**Roadmaps & track record.** IBM promised Nighthawk revisions at 5,000, 7,500, 10,000 and 15,000 gates [R][373]; the 7,500-gate step, its 2026 milestone, shipped on 2026-08-31 with PEA [C][697].

**Strategic reading.** Mitigation makes the noise model the product and keeps value inside the hardware vendor's stack. Only noise learning carries over to fault tolerance; when a code runs, the station empties.

*Open niche:* for one mitigated observable, publish the learned noise model, its drift during the run, the shot multiplier spent and the bias against a converged classical value — the model validation IBM names, feasible through cloud access.

## Outlook & open questions
Confirm if an unbiased PEC estimate on ≥5,000 gates appears with error bars by 2027-12-31, or a July-2026 claim survives to 2027-07-31 without converged classical reproduction; demote those claims to utility if converged tensor-network or Pauli-propagation values match them, as in 2023.
Open questions. (1) How stable is a learned Pauli–Lindblad model over a multi-hour run at 10³–10⁴ gates? (2) Does TEM's quadratic saving survive model error on hardware? (3) At what size does a detection code plus mitigation beat mitigation alone in shots? (4) Can a mitigated expectation-value task be proven classically hard? (5) What shot multiplier did Nighthawk r2's 7,500-gate PEA run spend?

## Sources

[34] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[44] A. Kandala, A. Javadi-Abhari, and J. Gambetta, “Researchers demonstrate quantum advantage through trusted quantum computation,” IBM Quantum Computing Blog, Jul. 30, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-advantage [C]
[196] E. Leviatan *et al.*, “Resolving Structure in Prethermal Floquet Dynamics with Precision Quantum Computation,” [arXiv:2607.24937](https://arxiv.org/abs/2607.24937), Jul. 2026. [D]
[234] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[235] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[373] R. Mandelbaum, “Scaling for quantum advantage and beyond,” IBM Quantum Computing Blog, Nov. 12, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/qdc-2025 [C]
[697] H. Haas, D. McKay, and R. Davis, “IBM Quantum Nighthawk r2—more circuits, faster,” IBM Quantum Computing Blog, Aug. 31, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/nighthawk-r2 [C]
[719] IBM, “Error mitigation and suppression techniques.” [Online]. Available: https://quantum.cloud.ibm.com/docs/en/guides/error-mitigation-and-suppression-techniques [C]
[720] K. Temme, S. Bravyi, and J. M. Gambetta, “Error mitigation for short-depth quantum circuits,” *Phys. Rev. Lett.*, vol. 119, Art. no. 180509, 2017, doi: [10.1103/PhysRevLett.119.180509](https://doi.org/10.1103/PhysRevLett.119.180509). [arXiv:1612.02058](https://arxiv.org/abs/1612.02058). [D]
[721] Y. Li and S. C. Benjamin, “Efficient Variational Quantum Simulator Incorporating Active Error Minimization,” *Phys. Rev. X*, vol. 7, no. 2, Art. no. 021050, Jun. 2017, doi: [10.1103/PhysRevX.7.021050](https://doi.org/10.1103/PhysRevX.7.021050). [arXiv:1611.09301](https://arxiv.org/abs/1611.09301). [D]
[722] A. Kandala *et al.*, “Error mitigation extends the computational reach of a noisy quantum processor,” *Nature*, vol. 567, pp. 491–495, Mar. 2019, doi: [10.1038/s41586-019-1040-7](https://doi.org/10.1038/s41586-019-1040-7). [arXiv:1805.04492](https://arxiv.org/abs/1805.04492). [D]
[723] S. Filippov, M. Leahy, M. A. C. Rossi, and G. García-Pérez, “Scalable tensor-network error mitigation for near-term quantum computing,” [arXiv:2307.11740](https://arxiv.org/abs/2307.11740), Jul. 2023. [S]
[724] S. V. Barron *et al.*, “Observable Estimation in the Absence of Classical Verification,” [arXiv:2607.25998](https://arxiv.org/abs/2607.25998), Jul. 2026. [D]
[725] R. Takagi, S. Endo, S. Minagawa, and M. Gu, “Fundamental limits of quantum error mitigation,” *npj Quantum Inf.*, vol. 8, Art. no. 114, 2022, doi: [10.1038/s41534-022-00618-z](https://doi.org/10.1038/s41534-022-00618-z). [arXiv:2109.04457](https://arxiv.org/abs/2109.04457). [D]
[726] R. Takagi, H. Tajima, and M. Gu, “Universal Sampling Lower Bounds for Quantum Error Mitigation,” *Phys. Rev. Lett.*, vol. 131, Art. no. 210602, 2023, doi: [10.1103/PhysRevLett.131.210602](https://doi.org/10.1103/PhysRevLett.131.210602). [arXiv:2208.09178](https://arxiv.org/abs/2208.09178). [D]
[727] Y. Quek, D. S. França, S. Khatri, J. J. Meyer, and J. Eisert, “Exponentially tighter bounds on limitations of quantum error mitigation,” *Nat. Phys.*, vol. 20, p. 1648, 2024, doi: [10.1038/s41567-024-02536-7](https://doi.org/10.1038/s41567-024-02536-7). [arXiv:2210.11505](https://arxiv.org/abs/2210.11505). [D]
[728] E. van den Berg, Z. K. Minev, A. Kandala, and K. Temme, “Probabilistic error cancellation with sparse Pauli–Lindblad models on noisy quantum processors,” *Nat. Phys.*, vol. 19, no. 8, pp. 1116–1121, May 2023, doi: [10.1038/s41567-023-02042-2](https://doi.org/10.1038/s41567-023-02042-2). [arXiv:2201.09866](https://arxiv.org/abs/2201.09866). [D]
[729] T. Begušić and G. K.-L. Chan, “Fast classical simulation of evidence for the utility of quantum computing before fault tolerance,” [arXiv:2306.16372](https://arxiv.org/abs/2306.16372), Jun. 2023. [D]
[730] T. Begušić, J. Gray, and G. K.-L. Chan, “Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance,” *Sci. Adv.*, Art. no. eadk4321, 2024, doi: [10.1126/sciadv.adk4321](https://doi.org/10.1126/sciadv.adk4321). [arXiv:2308.05077](https://arxiv.org/abs/2308.05077). [D]
[731] QEDMA, “QEDMA raises $26M with participation from IBM to tackle quantum computing errors and accelerate pace to quantum advantage,” PR Newswire, Jul. 3, 2025. [Online]. Available: https://www.prnewswire.com/news-releases/qedma-raises-26m-with-participation-from-ibm-to-tackle-quantum-computing-errors-and-accelerate-pace-to-quantum-advantage-302497701.html [C]
[732] Algorithmiq, “Algorithmiq Launches High-Performing Error Mitigation Solution in IBM's Qiskit Functions Catalog,” Sep. 16, 2024. [Online]. Available: https://www.algorithmiq.fi/news/press-release-tem-ibm-qiskit-functions/ [C]
[733] M. Ivezic, “IBM Launches Heron R3 (ibm_pittsburgh): ~350 uS T2 and a Quality Upgrade for Its 156-Qubit Platform,” PostQuantum.com, Aug. 1, 2025. [Online]. Available: https://postquantum.com/industry-news/ibm-heron-r3-pittsburgh/ [P]
[734] T. Q. Group, “Tianyan: Cloud services with quantum advantage,” [arXiv:2512.10504](https://arxiv.org/abs/2512.10504), Dec. 2025. [D]
[735] Algorithmiq, “Algorithmiq Establishes Milan Headquarters and raises €18m to Position Europe as the Future of Quantum Software,” May 11, 2026. [Online]. Available: https://algorithmiq.fi/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software/ [C]

## Open verification items
- IBM's 100× PEC-overhead reduction by samplomatic (2025-11-12) is a blog claim; no paper stating its baseline or circuit class was found (tried 2026-09-26).
- Nighthawk r2's 7,500-gate PEA run: shot count, QPU time and observable are not in the blog (checked 2026-09-26).
- Zuchongzhi 3.0 and Tianyan-287: only the arXiv abstracts were read; the full texts were not checked for a mitigation step (2026-09-26).
- Heron r1: no primary source found showing a named mitigation method run on r1 itself (2026-09-26).
- Begušić, Gray and Chan's Science Advances volume and issue not confirmed (Crossref rate-limited, PubMed Central behind a captcha, 2026-09-26); the TREX paper (arXiv:2012.09738) header could not be read, so TREX is cited from IBM's documentation.
- The e^(4P) shot scaling and the P values are derived here from the PEC construction and published error rates, not quoted from a source.
