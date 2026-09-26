---
id: g_rydanalog
name: Analog Rydberg Hamiltonian evolution
layer: "3 Gate mechanism"
status: demonstrated
since: 2017
one_line: "Global laser fields drive a programmable Rydberg Ising Hamiltonian on a whole tweezer array at once: the waveforms Ω(t), Δ(t), a fixed local-detuning pattern and the atom geometry are the program, and there is no discrete gate."
verdict: "Demonstrated to 256–289 atoms and productive for many-body physics, but graded by observables, not gate error: the reference many-body fidelity benchmark reports 0.095 at 60 atoms on an academic Sr machine, the register holds no fidelity figure for Aquila or Fresnel as of 2026-09-26, and the mode admits no error correction."
updated: 2026-09-26
---

Λ = error-suppression factor per code-distance step; MIS = maximum independent set; SA = simulated annealing; F_d = cross-entropy-type many-body fidelity estimator; MPS = matrix-product state (χ = bond dimension); AHS = analog Hamiltonian simulation, Amazon Braket's program type; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The array evolves under one Hamiltonian, H/ℏ = Σᵢ (Ω(t)/2) σˣᵢ − Σᵢ [Δ(t) + hᵢ Δ_loc(t)] nᵢ + Σ_{i<j} C₆ r_ij⁻⁶ nᵢ nⱼ: global waveforms, one static site pattern $h_i$, couplings fixed by atom positions [C][622][C][630]. Station g_ryd uses the same blockade for a two-atom CZ inside a circuit; here it acts on all pairs for the whole run, and the output is a bit-string sample. Station g_anneal, the rf-SQUID flux annealer, sets couplings with programmable on-chip couplers [D][437]; here geometry is the coupling matrix, and blockade confines the dynamics to independent sets of a unit-disk graph, the basis of MIS encoding [D][631]. Lineage: 51 atoms in 1D, Harvard/MIT, 2017 [D][623]; Pasqal's 2020 architecture naming analog "Hamiltonian sequences" beside circuits [D][624]; Aquila on Amazon Braket [C][622].
Attributes: natural carrier; no step time (one evolution, ≤4 µs on Aquila); readout inherited; no mobility during the program; optical control at room temperature; coherent and loss errors; optics manufacturing.

## Physics & limits
Aquila: Ω ≤ 15.8 rad/µs, |Δ| ≤ 125 rad/µs, $C_6$ = 5,420,503 µm⁶ rad/µs (70S), spacing ≥4 µm, program ≤4 µs, T2* 5.8 µs, driven T2 7.5 µs [C][622]: a blockade radius $(C_6/\Omega)^{1/6}$ ≈ 8.4 µm at full drive, and a program of ~half the driven T2, ~10 Rabi periods [S]. Named error terms: laser amplitude and phase noise; thermal motion (Doppler, 0.200 µm position spread); scattering via the intermediate state, which continues with the drive off; detuning inhomogeneity, 0.37 rad/µs RMS across the field and 0.18 rad/µs shot-to-shot [C][622]. Via r⁻⁶ the position spread gives ~30% shot-to-shot spread of a 5.5 µm bond (δV/V = 6δr/r) [S] — harmless deep in blockade, decisive where V ≈ Ω, which selects the ordered phase. Local detuning is a fixed pattern with a waveform ≤0, and programs using it decohere faster than the listed T2 [C][630]. Errors integrate coherently over a run with no point to measure a syndrome, so no code acts [S]; erasure detection on Sr raised a Bell-pair fidelity bound from ≥0.9971 to ≥0.9985 by discarding flagged shots [D][129] — post-selection, not correction.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2017-11 | 51 atoms, 1D; Z₂ order, oscillations after quench | Harvard/MIT | [D][623] |
| 2021-07 | 64–256 atoms, 2D; (2+1)D Ising transition | Harvard/MIT | [D][632] |
| 2021-07 | Up to 196 atoms, square and triangular antiferromagnets | Institut d'Optique | [D][633] |
| 2021-12 | 219 atoms on kagome links; topological spin liquid | Harvard/MIT | [D][634] |
| 2022-06 | Up to 289 atoms; MIS, superlinear speed-up vs SA | Harvard-led | [D][635] |
| 2024 | 60 Sr atoms; F_d = 0.095(11) at saturated entanglement | Caltech | [D][636] |
| 2025-06-04 | (2+1)D string breaking on Aquila | QuEra et al. | [D][191] |

Above ~100 atoms nothing is checked exactly: the 196-atom work matched numerics only to ~100 [D][633]. The 2022 speed-up did not survive: classical solvers reach optimality on the same Union-Jack-like instances to thousands of nodes within minutes [D][631]. Pasqal offers a 100-qubit analog QPU on Google Cloud (2025-05-13) [C][637]; no Fresnel datasheet like Aquila's was found as of 2026-09-26.

## Manufacturing, materials & supply chain
No wafer; optical assembly shared with the digital atom paths. Orion Gamma: 140 qubits, room temperature, 3 kW average, 5 µm minimum spacing [C][610]. The analog-specific addition is a site-resolved detuning field whose hardware QuEra has not described [C][638]; nothing else in the sources separates the analog bill of materials from the digital one [S].

## Control, readout & I/O burden
Control is independent of N: a few waveforms, one pattern and a geometry [C][622]. The cost moves to readout and repetition. Aquila misreads 8% of Rydberg and 1% of ground atoms and leaves 0.7% of sites empty [C][622], so a 256-site snapshot, half excited, reads error-free with probability 0.92¹²⁸×0.99¹²⁸ ≈ 6×10⁻⁶, and ~17% of shots have a defect-free register [S]. Shots run below 10 Hz on Aquila [C][622] and at ≥0.25 Hz effective on Orion Gamma [C][610]: 10⁴ shots take ≥17 min to ~11 h [S].

## Role in the stack
Slot 3 of the Rydberg analog simulator path (alkali atom → ground–Rydberg analog qubit → this station → AOD transport → laser + AOD/SLM control → fluorescence imaging; layers 7–9 empty; optical assembly), serving G1. It **requires** the alkali atom, the ground–Rydberg encoding and global Rydberg lasers; it **provides** nothing upward; it **replaces** nothing and is replaced by g_ryd when a machine turns digital. Register: Aquila (QuEra, 256 sites) and Fresnel/Fresnel 2 (Pasqal, 100 qubits) carry it as primary, both ✅; Pasqal's Orion line carries it as alternate on the "Rydberg tweezer array — alkali (Rb/Cs)" path, 🔎. The gap ledger proposed the alkali and alkaline-earth array paths; the station got its own path, and no alkaline-earth register machine runs it, though the fidelity benchmark above used Sr [D][636] — the requires-alkali edge is narrower than the physics.

## Verification (QCVV)
With no gate error, fidelity comes from observables: order parameters against numerics, valid to ~100 atoms [D][633]; F_d, which weights measured bit-strings by simulated probabilities — 0.095(11) at 60 atoms, where a lightcone MPS at χ* = 3400 (~110 GB, ~180 core-days) keeps pace [D][636]; and problem output such as MIS size, cheap to validate but not to prove optimal [D][631]. F_d needs classical probabilities, so what it certifies can be simulated. Λ is undefined. The Orion cell stays 🔎: its cited page (2026-01-29) mentions local detuning for materials simulation and a 2026 Vela with over 256 qubits, but not analog mode, MIS, Orion or ≤100 qubits [C][629].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| QuEra Computing | developer | US | Aquila, 256 sites, on Braket since 2022 | [C][142] |
| Pasqal | developer | FR | 100-qubit analog QPU; analog mode on Orion | [C][637] |
| Amazon Web Services | cloud channel | US | Aquila local detuning by request, 2024-04-11 | [C][639] |
| Harvard/MIT | research | US | 51- to 289-atom experiments | [D][635] |
| Caltech | research | US | F_d benchmark, 60 Sr atoms | [D][636] |

**Money.**
- 2025-09-09 · QuEra · Series B extended, NVentures joins · USD 230 M · announced; aimed at fault tolerance [C][137]
- 2026-08-28 · Pasqal · SPAC merger, Nasdaq PSQL · ~USD 360 M cash · closed [P][140]

**Market & supply chain.** Two vendors, two cloud channels. Pasqal reports seven QPUs deployed and markets its platform as analog today [P][140]; QuEra's analog offer is one machine. It pays into G1 only.

**IP & standards.** No analog-specific patent count as of 2026-09-26; the program format is cloud-defined (Braket AHS) [C][630]; no standards body.

**Roadmaps & track record.** Pasqal promised 10,000 physical qubits for 2026 (2024-03-13) [R][145]; its 2026 launch is Vela, over 256 qubits [R][629] — ~39× short [S] — and its brochure says delivery 2027, 200+ [C][610]. QuEra's Libra (2028) is digital, with no analog specification [R][142].

**Strategic reading.** Analog is both vendors' revenue bridge while g_ryd matures. With certified advantage above ~100 atoms it stays a G1 instrument; without, it becomes a mode of digital machines, as on Orion.

*Open niche:* F_d versus time and atom number on Aquila through the cloud, with the published readout errors folded in.

## Outlook & open questions
Confirm if, by 2027-12-31, a commercial analog machine publishes a many-body fidelity at ≥60 atoms, or an analog result survives a year of classical challenge; demote if Vela and QuEra's next systems ship without analog specifications. Open questions. (1) Can F_d certify beyond the size where MPS keeps pace? (2) What are per-site local-detuning calibration errors? (3) How does driven-T2 loss split between phase noise, Doppler and scattering? (4) Can erasure excision post-select many-body runs at tolerable shot cost? (5) Will the requires-alkali edge survive alkaline-earth analog machines?

## Sources

[129] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[137] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[140] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[142] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [C]
[145] J. Russell, “PASQAL Issues Roadmap to 10,000 Qubits in 2026 and Fault Tolerance in 2028,” HPCwire, Mar. 13, 2024. [Online]. Available: https://www.hpcwire.com/2024/03/13/pasqal-issues-roadmap-to-10000-qubits-in-2026-and-fault-tolerance-in-2028/ [R]
[191] D. González-Cuadra *et al.*, “Observation of string breaking on a (2 + 1)D Rydberg quantum simulator,” *Nature*, vol. 642, no. 8067, pp. 321–326, Jun. 2025, doi: [10.1038/s41586-025-09051-6](https://doi.org/10.1038/s41586-025-09051-6). [D]
[437] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[610] Pasqal and O. Q.-C. P. brochure, “The Power of Neutral Atom Quantum Processors by Pasqal — Unlock Quantum Computing for Real-World Solutions,” Pasqal, product brochure (PDF). [Online]. Available: https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf [C]
[622] J. Wurtz *et al.*, “Aquila: QuEra's 256-qubit neutral-atom quantum computer,” [arXiv:2306.11727](https://arxiv.org/abs/2306.11727), Jun. 2023. [C]
[623] H. Bernien *et al.*, “Probing many-body dynamics on a 51-atom quantum simulator,” *Nature*, vol. 551, pp. 579–584, Nov. 2017, doi: [10.1038/nature24622](https://doi.org/10.1038/nature24622). [arXiv:1707.04344](https://arxiv.org/abs/1707.04344). [D]
[624] L. Henriet *et al.*, “Quantum computing with neutral atoms,” *Quantum*, vol. 4, Art. no. 327, Sep. 2020, doi: [10.22331/q-2020-09-21-327](https://doi.org/10.22331/q-2020-09-21-327). [arXiv:2006.12326](https://arxiv.org/abs/2006.12326). [D]
[629] L. Garbini, “Inside Pasqal's 2026 Vision on Quantum for Industry and Research,” Pasqal, Jan. 29, 2026. [Online]. Available: https://www.pasqal.com/blog/inside-pasqals-2026-vision-on-quantum-for-industry-and-research/ [C]
[630] Amazon Web Services, “Explore Experimental Capabilities - Amazon Braket,” Amazon Braket Developer Guide. [Online]. Available: https://docs.aws.amazon.com/braket/latest/developerguide/braket-access-local-detuning.html [C]
[631] R. S. Andrist *et al.*, “Hardness of the Maximum Independent Set Problem on Unit-Disk Graphs and Prospects for Quantum Speedups,” *Phys. Rev. Research*, vol. 5, no. 4, Art. no. 043277, 2023, doi: [10.1103/PhysRevResearch.5.043277](https://doi.org/10.1103/PhysRevResearch.5.043277). [arXiv:2307.09442](https://arxiv.org/abs/2307.09442). [D]
[632] S. Ebadi *et al.*, “Quantum Phases of Matter on a 256-Atom Programmable Quantum Simulator,” *Nature*, vol. 595, p. 227, Jul. 2021, doi: [10.1038/s41586-021-03582-4](https://doi.org/10.1038/s41586-021-03582-4). [arXiv:2012.12281](https://arxiv.org/abs/2012.12281). [D]
[633] P. Scholl *et al.*, “Programmable quantum simulation of 2D antiferromagnets with hundreds of Rydberg atoms,” *Nature*, vol. 595, p. 233, Jul. 2021, doi: [10.1038/s41586-021-03585-1](https://doi.org/10.1038/s41586-021-03585-1). [arXiv:2012.12268](https://arxiv.org/abs/2012.12268). [D]
[634] G. Semeghini *et al.*, “Probing Topological Spin Liquids on a Programmable Quantum Simulator,” *Science*, vol. 374, p. 1242, Dec. 2021, doi: [10.1126/science.abi8794](https://doi.org/10.1126/science.abi8794). [arXiv:2104.04119](https://arxiv.org/abs/2104.04119). [D]
[635] S. Ebadi *et al.*, “Quantum Optimization of Maximum Independent Set using Rydberg Atom Arrays,” *Science*, vol. 376, p. 1209, Jun. 2022, doi: [10.1126/science.abo6587](https://doi.org/10.1126/science.abo6587). [arXiv:2202.09372](https://arxiv.org/abs/2202.09372). [D]
[636] A. L. Shaw *et al.*, “Benchmarking highly entangled states on a 60-atom analog quantum simulator,” *Nature*, vol. 628, pp. 71–77, 2024, doi: [10.1038/s41586-024-07173-x](https://doi.org/10.1038/s41586-024-07173-x). [arXiv:2308.07914](https://arxiv.org/abs/2308.07914). [D]
[637] Pasqal, “Pasqal's Neutral-Atom Quantum Computer Available on Google Cloud Marketplace,” May 13, 2025. [Online]. Available: https://www.pasqal.com/newsroom/pasqals-neutral-atom-quantum-computer-available-on-google-cloud-marketplace/ [C]
[638] QuEra Computing, “Local Qubit Control Brings New Capabilities to QuEra's Quantum Computer,” Apr. 17, 2024. [Online]. Available: https://www.quera.com/press-releases/local-qubit-control-brings-new-capabilities-to-queras-quantum-computer [C]
[639] Amazon Web Services, “Local detuning now available on QuEra's Aquila device with Braket Direct,” AWS What's New, Apr. 11, 2024. [Online]. Available: https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-braket-experimental-capabilities-quera-device-braket-direct/ [C]

## Open verification items
- Aquila's local-detuning limits (magnitude, resolution, per-site calibration error) are exposed only through Braket SDK device properties, not read here; the hardware mechanism (light-shift beam or otherwise) is not described in QuEra's release (tried 2026-09-26).
- The Aquila whitepaper gives no Rydberg lifetime or atom-loss rate during evolution; no Fresnel datasheet (Ω, Δ, T2, detection errors) was found, and Scaleway's Pasqal QPU page did not render (2026-09-26).
- The register's Orion cell ("analog MIS/optimisation and materials Hamiltonians shown at ≤100 qubits") is not supported by its cited page; it stays 🔎 (2026-09-26).
- The dipolar XY variant in the node description has no register machine and was not checked against a primary source (2026-09-26).
- Aquila's continued Braket service is inferred from QuEra's 2026-06-15 release, which does not state it explicitly (2026-09-26).
