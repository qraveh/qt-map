---
id: g_lointer
name: Programmable linear-optical interferometer (no entangling primitive)
layer: "3 Gate mechanism"
status: demonstrated
since: 2020
one_line: "A programmable passive unitary on N optical modes — a beamsplitter/phase-shifter mesh or time-bin fibre loops — that scatters squeezed light or single photons into detectors for sampling, with no entangling gate and no feed-forward."
verdict: "A working sampler, not a gate: 8,176 modes and up to 3,050 detected photons (Jiuzhang 4.0, 2026). Every earlier advantage claim was matched on its own benchmarks by a published classical sampler; as of 2026-09-26 none was found for Jiuzhang 4.0, and ORCA publishes no mode, loss or clock figure for PT-2."
updated: 2026-09-26
---

GBS = Gaussian boson sampling; MZI = Mach–Zehnder interferometer; EOM = electro-optic modulator; PNR = photon-number-resolving; SNSPD = superconducting nanowire single-photon detector; TES = transition-edge sensor; MPS = matrix-product state (a tensor network); USTC = University of Science and Technology of China; NQCC = UK National Quantum Computing Centre; G1–G7 = the report's goal classes (G1: analog and NISQ simulation).

## Identity & lineage
A passive network maps input modes onto outputs, a†ᵢ → Σⱼ Uⱼᵢ a†ⱼ, with U an N×N unitary. Reck et al. factorised any U into N(N−1)/2 beamsplitter–phase-shifter pairs [G][452]; Clements et al. halved the footprint and balanced the loss [G][453]; loops reuse one interference point on every time bin [G][454]. A six-mode, 15-MZI chip set 100 Haar-random unitaries at fidelity 0.999 ± 0.001 [D][455]. Machines on this technology use the network only to sample — single photons after Aaronson and Arkhipov [G][456], squeezed light after Hamilton et al. [G][268]. Attributes: flying carrier, no gate time or determinism class, loss-dominated error, electro-optic room-temperature control, bulk or photonic-IC fabrication.

## Physics & limits
Output probabilities are permanents of n×n submatrices of U; exact polynomial-time classical sampling would collapse the polynomial hierarchy, and approximate hardness rests on two conjectures [G][456]. With squeezed inputs they are hafnians, also #P-hard [G][268]. The mesh entangles modes when fed squeezed light [D][270] but has no entangling gate on encoded qubits: linear optics without ancilla photons distinguishes Bell states with at most 50% probability [G][457], and universality needs detector feed-forward [G][337]. The limits are loss and distinguishability. Transmission compounds with depth: at 0.99 per MZI, a 100-mode Clements mesh passes ~0.37 [S][453]. Noisy GBS is efficiently simulable once squeezing, transmission and detector quality satisfy an inequality [S][269]; tensor networks are likely efficient when surviving photons scale as √N for N inputs [S][458]; at fixed partial distinguishability, simulation cost grows only polynomially with photon number [S][459].

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2015-05 | Six-mode universal chip, fidelity 0.999 ± 0.001 | Carolan et al. | [D][455] |
| 2020-12 | 50 squeezed states, 100 modes, up to 76 clicks | USTC, Jiuzhang 1.0 | [D][460] |
| 2021-09 | Workstation samplers beat Jiuzhang 1.0/2.0 on marginal distances | Google Quantum AI | [S][461] |
| 2022-06-01 | 216 time-bin modes, three loops, up to 219 photons, ~33% transmittance | Xanadu, Borealis | [D][270] |
| 2023-10-10 | Up to 255 clicks; 1.27 µs per sample vs ~600 years on Frontier | USTC, Jiuzhang 3.0 | [D][462] |
| 2024-06-25 | MPS sampler beats Jiuzhang 2.0/3.0 and Borealis on correlations; 288 GPUs, ~72 min for 10⁷ samples | Univ. of Chicago / Argonne | [S][463] |
| 2026-05-13 | 1,024 squeezed states, 8,176 modes, up to 3,050 photons, 25.6 µs per sample | USTC, Jiuzhang 4.0 | [D][175] |

Jiuzhang 4.0 answers the MPS attack with efficiency — 92% at the source, 51% end to end — which by the authors' estimate needs bond dimension above 8×10²¹, over 10⁴² years on El Capitan [S][175]; validation is on subsystems, with a margin growing with size, not at full scale [D][175].

## Manufacturing, materials & supply chain
Borealis is fibre and bulk optics: three delays with EOM-driven variable beamsplitters from QUBIG GmbH, 16 TES detectors at 95% behind a 1-to-16 demultiplexer [D][270]. Jiuzhang 4.0 cascades three 16-mode interferometers through two delay-loop arrays onto 16 SNSPDs at 93% [D][175]. ORCA builds rack-mounted room-temperature systems from telecom-grade fibre components [C][464]. Only detectors are cryogenic. No per-element loss of a fielded sampling mesh is published as of 2026-09-26; the 99.8% transmission and >40 dB extinction quoted for Jiuzhang 4.0 belong to its squeezed-light filter [D][175].

## Control, readout & I/O burden
Borealis sets every loop beamsplitter per 167 ns time bin and samples at 10 kHz between loop stabilisations [D][270]. Jiuzhang 4.0 tunes its meshes thermally and loop phases with piezo stretchers; no per-bin electro-optic setting is reported [D][175], so the technology's electro-optic attribute fits Borealis best. Readout is terminal; nothing is fed forward. Time multiplexing decouples detectors from modes: 16 detectors read 216 or 8,176 modes [D][175], [270]. The heavy I/O is classical: checking a sample exactly means computing hafnians [G][268].

## Role in the stack
The gate slot of the Boson sampler architecture (ph_sampler, goal G1). It **requires** photon (single photons or squeezed light in the mesh) and ct_eo (phase shifters and switches); it **provides** no edge — its output is a sample; it **replaces** nothing, and g_fusion replaces it (fusion vs sampling interferometer): the same optics become a gate only when heralded Bell outcomes (g_fusion) or homodyne results (g_cv) are fed forward. This answers gap G-lointer — samplers had a gate layer with nothing gate-like in it — with an architecture of their own rather than the proposed technology on ph_cv and ph_fusion. Register machines, all primary: Borealis (Xanadu, deployed 2022-06), Jiuzhang 4.0 (USTC, demonstrated 2026-05-13), PT-2 (ORCA, deployed 2024–2026). The clock is a sample period: 36 µs (Borealis), 25.6 µs (Jiuzhang 4.0) [D][175], [270].

## Evidence — how the numbers were measured
No gate exists to benchmark; samples are compared with the ideal distribution, and the benchmarks used — low-order correlations, marginal distances — were matched or beaten classically [S][461], [463]. The Borealis ✅ and Jiuzhang 4.0 ✅ cells hold against their papers, the latter with the filter correction above. PT-2 stays 🔎: its evidence page gives no architecture [C][465]. The one description found is third-party — fibre delay loops with variable beamsplitters, capable of two loops where that paper puts the classically hard regime at three, sampling photon-subtracted squeezed states with a PNR detector [P][271] — not the single photons the register records. An ORCA co-authored PT-1 study used one delay line [D][466].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| USTC | developer | CN | Jiuzhang series; 4.0 joins 16-mode meshes with delay-loop arrays, SNSPD readout | [D][175] |
| Xanadu | developer | CA | Borealis: three EOM-programmed fibre loops | [D][270] |
| ORCA Computing | developer | UK | PT-series time-bin loop samplers, rack-mounted | [C][465] |
| QUBIG GmbH | supplier | DE | EOMs in the Borealis loops | [D][270] |
| Google Quantum AI; Univ. of Chicago / Argonne | classical challengers | US | Marginal-matching and MPS samplers | [S][461], [463] |

**Money.**
- 2024-02-05 · NQCC · £30 M testbed competition, ORCA one of seven winners · per-company value undisclosed · awarded [G][467]
- 2024-06-05 · Montana State University · two PT-1 systems, US Air Force-funded · undisclosed · contracted [C][468]
- 2025-06-11 · ORCA · NQCC testbed installed under the UK's £121 M initiative · undisclosed · delivered [C][469]

**Market & supply chain.** Of the register's three machines only PT-2 is sold as a system; USTC is academic, and the register marks Borealis superseded by Aurora. ORCA does not publicise most of its fundraising [P][470].

**IP & standards.** No sampler-specific patent count or benchmark standard found as of 2026-09-26.

**Roadmaps & track record.** NQCC testbeds were due by March 2025 [G][467]; ORCA announced its installation on 2025-06-11, a quarter later [C][469]. PT-3 is "due for release later in 2026" with three switchable modules, claimed to beat classical solvers on up to 25,000-variable problems [R][470].

**Strategic reading.** A contest between loss and classical simulation, not a route to computation; what lasts are the loops, squeezers and number-resolving detectors that fusion and CV machines also need. If PT-3 reaches the three-loop regime with published loss, ORCA holds the only commercial sampler beyond easy simulation; if not, the technology stays academic.

## Outlook & open questions
Confirm if, by 2027-12-31, no classical sampler matches Jiuzhang 4.0 on its subsystem benchmarks and ORCA publishes PT-3 modes, loops and loss with a classical comparison; demote if one matches Jiuzhang 4.0 by then, or PT-3 ships in 2026 without those figures. Open questions. (1) What is the per-element loss of Jiuzhang 4.0's programmable meshes? (2) Does subsystem validation extrapolate to full scale? (3) What does PT-2 inject, and through how many loops? (4) Does any GBS application keep a speed-up at 33–51% transmission? (5) Can a loop sampler become a fusion machine by adding heralding and feed-forward?

## References
[175] H.-L. Liu *et al.*, “Gaussian boson sampling with 1,024 squeezed states in 8,176 modes,” *Nature*, vol. 653, no. 8115, pp. 687–692, May 2026, doi: [10.1038/s41586-026-10523-6](https://doi.org/10.1038/s41586-026-10523-6). [arXiv:2508.09092](https://arxiv.org/abs/2508.09092). [D]
[268] C. S. Hamilton *et al.*, “Gaussian Boson Sampling,” *Phys. Rev. Lett.*, vol. 119, no. 17, Art. no. 170501, Oct. 2017, doi: [10.1103/PhysRevLett.119.170501](https://doi.org/10.1103/PhysRevLett.119.170501). [arXiv:1612.01199](https://arxiv.org/abs/1612.01199). [G]
[269] H. Qi, D. J. Brod, N. Quesada, and R. García-Patrón, “Regimes of Classical Simulability for Noisy Gaussian Boson Sampling,” *Phys. Rev. Lett.*, vol. 124, no. 10, Art. no. 100502, Mar. 2020, doi: [10.1103/PhysRevLett.124.100502](https://doi.org/10.1103/PhysRevLett.124.100502). [arXiv:1905.12075](https://arxiv.org/abs/1905.12075). [S]
[270] L. S. Madsen *et al.*, “Quantum computational advantage with a programmable photonic processor,” *Nature*, vol. 606, no. 7912, pp. 75–81, Jun. 2022, doi: [10.1038/s41586-022-04725-x](https://doi.org/10.1038/s41586-022-04725-x). [D]
[271] J. Park, S. Stepney, and I. D'Amico, “Benchmarking the ORCA PT-2 Boson Sampler using Minimum Dominating Set Problems,” [arXiv:2605.30935](https://arxiv.org/abs/2605.30935), May 2026. [P]
[337] E. Knill, R. Laflamme, and G. Milburn, “Efficient Linear Optics Quantum Computation,” *Nature*, vol. 409, pp. 46–52, Jun. 2000, doi: [10.1038/35051009](https://doi.org/10.1038/35051009). [arXiv:quant-ph/0006088](https://arxiv.org/abs/quant-ph/0006088). [G]
[452] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, “Experimental realization of any discrete unitary operator,” *Phys. Rev. Lett.*, vol. 73, no. 1, pp. 58–61, Jul. 1994, doi: [10.1103/PhysRevLett.73.58](https://doi.org/10.1103/PhysRevLett.73.58). [G]
[453] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, “Optimal design for universal multiport interferometers,” *Optica*, vol. 3, no. 12, p. 1460, Dec. 2016, doi: [10.1364/OPTICA.3.001460](https://doi.org/10.1364/OPTICA.3.001460). [arXiv:1603.08788](https://arxiv.org/abs/1603.08788). [G]
[454] K. R. Motes, A. Gilchrist, J. P. Dowling, and P. P. Rohde, “Scalable Boson Sampling with Time-Bin Encoding Using a Loop-Based Architecture,” *Phys. Rev. Lett.*, vol. 113, no. 12, Art. no. 120501, Sep. 2014, doi: [10.1103/PhysRevLett.113.120501](https://doi.org/10.1103/PhysRevLett.113.120501). [arXiv:1403.4007](https://arxiv.org/abs/1403.4007). [G]
[455] J. Carolan *et al.*, “Universal Linear Optics,” [arXiv:1505.01182](https://arxiv.org/abs/1505.01182), May 2015. [D]
[456] S. Aaronson and A. Arkhipov, “The Computational Complexity of Linear Optics,” *Theory of Computing*, vol. 9, pp. 143–252, 2013, doi: [10.4086/toc.2013.v009a004](https://doi.org/10.4086/toc.2013.v009a004). [arXiv:1011.3245](https://arxiv.org/abs/1011.3245). [G]
[457] J. Calsamiglia and N. Lütkenhaus, “Maximum efficiency of a linear-optical Bell-state analyzer,” *Appl. Phys. B*, vol. 72, no. 1, pp. 67–71, Jan. 2001, doi: [10.1007/s003400000484](https://doi.org/10.1007/s003400000484). [arXiv:quant-ph/0007058](https://arxiv.org/abs/quant-ph/0007058). [G]
[458] M. Liu, C. Oh, J. Liu, L. Jiang, and Y. Alexeev, “Simulating lossy Gaussian boson sampling with matrix-product operators,” *Phys. Rev. A*, vol. 108, no. 5, Art. no. 052604, Nov. 2023, doi: [10.1103/PhysRevA.108.052604](https://doi.org/10.1103/PhysRevA.108.052604). [arXiv:2301.12814](https://arxiv.org/abs/2301.12814). [S]
[459] J. J. Renema *et al.*, “Efficient Classical Algorithm for Boson Sampling with Partially Distinguishable Photons,” *Phys. Rev. Lett.*, vol. 120, no. 22, Art. no. 220502, May 2018, doi: [10.1103/PhysRevLett.120.220502](https://doi.org/10.1103/PhysRevLett.120.220502). [arXiv:1707.02793](https://arxiv.org/abs/1707.02793). [S]
[460] H.-S. Zhong *et al.*, “Quantum computational advantage using photons,” *Science*, vol. 370, no. 6523, pp. 1460–1463, Dec. 2020, doi: [10.1126/science.abe8770](https://doi.org/10.1126/science.abe8770). [arXiv:2012.01625](https://arxiv.org/abs/2012.01625). [D]
[461] B. Villalonga *et al.*, “Efficient approximation of experimental Gaussian boson sampling,” [arXiv:2109.11525](https://arxiv.org/abs/2109.11525), Sep. 2021. [S]
[462] Y.-H. Deng *et al.*, “Gaussian Boson Sampling with Pseudo-Photon-Number-Resolving Detectors and Quantum Computational Advantage,” *Phys. Rev. Lett.*, vol. 131, no. 15, Art. no. 150601, Oct. 2023, doi: [10.1103/PhysRevLett.131.150601](https://doi.org/10.1103/PhysRevLett.131.150601). [arXiv:2304.12240](https://arxiv.org/abs/2304.12240). [D]
[463] C. Oh, M. Liu, Y. Alexeev, B. Fefferman, and L. Jiang, “Classical algorithm for simulating experimental Gaussian boson sampling,” *Nat. Phys.*, vol. 20, pp. 1461–1468, Jun. 2024, doi: [10.1038/s41567-024-02535-8](https://doi.org/10.1038/s41567-024-02535-8). [arXiv:2306.03709](https://arxiv.org/abs/2306.03709). [S]
[464] ORCA Computing, “Technology — ORCA Computing.” [Online]. Available: https://orcacomputing.com/technology/ [C]
[465] ORCA Computing, “ORCA PT-2 — ORCA Computing.” [Online]. Available: https://orcacomputing.com/orca-pt-2/ [C]
[466] A. Makarovskiy *et al.*, “A Binary Optimisation Algorithm for Near-Term Photonic Quantum Processors,” [arXiv:2510.08274](https://arxiv.org/abs/2510.08274), Oct. 2025. [D]
[467] National Quantum Computing Centre, “Science Minister Andrew Griffith announces the results of the £30m quantum computing testbed competition,” NQCC, Feb. 5, 2024. [Online]. Available: https://www.nqcc.ac.uk/updates/science-minister-andrew-griffith-announces-the-results-of-the-30m-quantum-computing-testbed-competition/ [G]
[468] ORCA Computing, “Montana State University Selects ORCA Computing to Advance Distributed Quantum Computing and Communications,” Jun. 5, 2024. [Online]. Available: https://orcacomputing.com/montana-state-university-selects-orca-computing/ [C]
[469] ORCA Computing, “ORCA Computing Delivers First Photonic Quantum Computing System to UK's National Quantum Computing Centre,” Jun. 11, 2025. [Online]. Available: https://orcacomputing.com/installation-marks-key-milestone-in-the-uks-121m-quantum-initiative-advancing-practical-quantum-research/ [C]
[470] Tech Journal UK, “ORCA aims to beat classical computers with PT-3 quantum system,” Jul. 1, 2026. [Online]. Available: https://www.techjournal.uk/p/orca-aims-to-beat-classical-computers [R]

## Open verification items
- The arXiv abstract pages of 2605.30935 and 2109.11525 did not render on 2026-09-26; months are taken from the identifiers, titles and authors from the full-text HTML.
- NQCC system model: ORCA's release of 2025-06-11 says only "PT Series"; the PT-2 page names the NQCC testbed as a 2025 deployment (checked 2026-09-26).
- PT-2 input state: the third-party "photon-subtracted squeezed states" contradicts the register's "single photons (SPDC)"; no ORCA primary source settles it (searched 2026-09-26).
- No classical rebuttal of Jiuzhang 4.0 was found in a search on 2026-09-26; an unindexed preprint may exist.
