---
id: phonon
name: Bosonic motional mode of trapped ions (phonons)
layer: "1 Qubit carrier"
status: emerging
since: 1995
one_line: The vibration of a trapped-ion crystal used as a bosonic register, not only as a gate bus, controlled through the ions' internal levels; best figures are two GKP qubits in two modes of one ion entangled at 0.680 logical process fidelity in 993 µs and a 99.1% phonon beam splitter.
verdict: Five laboratories have computed with motional modes since 2019, on one to five ions, but 10–200 ms of motional coherence against gates of hundreds of microseconds, and a readout that destroys the register on a bright outcome, keep it emerging; a multi-mode error-corrected register would confirm it, dephasing still dominating in 2028 would demote it.
updated: 2026-11-22
---

SDF = state-dependent force (red and blue motional sidebands driven together, displacing the motion in a direction set by the internal state); GKP = Gottesman–Kitaev–Preskill grid code; MS = Mølmer–Sørensen gate; CZ = controlled-Z gate; eSWAP = exponential-SWAP gate; Fock state = state of definite phonon number; ISA = instruction set architecture; QCCD = quantum charge-coupled device (ions moved between trap zones); NIST = National Institute of Standards and Technology; NUS = National University of Singapore; CQT = its Centre for Quantum Technologies; SNP = spin–phonon primitive (a conditional displacement); SQUID = superconducting quantum interference device; CX = controlled-X gate; DC = direct current; RF = radio frequency; UV = ultraviolet; T1 / T2 = energy-relaxation / dephasing time.

## Identity & lineage

Ions in one trap share collective modes of vibration, and every trapped-ion entangling gate borrows one as a bus (`cx_bus`, `g_ms`). The same modes are harmonic oscillators whose quanta, phonons, can hold information themselves — a qubit in the two lowest Fock states, a qudit in more, a GKP code across the phase space — with the ion's internal levels as the ancilla that prepares, transforms and reads them through the motional sidebands.

The motion was a carrier from the start. NIST's 1995 controlled-NOT stored its two qubits in the internal and external degrees of freedom of one ion cooled to the zero-point energy, the motion carrying one of them [D][374]; months later the group prepared Fock, coherent and squeezed motional states and read their number distribution through the internal state [D][944]. The Atlas dates the technology by the 1995 gate — the earliest peer-reviewed hardware found in which a motional mode served as a computational carrier in a two-qubit device, the experiment that also dates `ion`. Bosonic encodings came later: ETH Zürich encoded a GKP qubit in the motion of one ⁴⁰Ca⁺ ion in 2019, logical states at 87.3 ± 0.7% average squared fidelity [D][945], and in 2022 corrected it by dissipative pumping, tripling the logical lifetime [D][946]; NUS built a conditional beam splitter that swaps two modes depending on the internal state [D][947].

Multi-mode work brought the engineering stage. Tsinghua programmed beam splitters between four collective modes of a five-ion ¹⁷¹Yb⁺ chain [D][948]; Sydney ran a universal gate set on two GKP qubits in two modes of one ¹⁷¹Yb⁺ ion, with what the authors' preprint presents as the first entangling gate between GKP code words [D][949]; Maryland and Duke simulated a Yukawa model on a three-ion chain, fermions in the internal states and the scalar field in two or three transverse modes per circuit, reproducing occupations up to eight phonons in one mode of a two-mode run (Nature Physics, Sep 2026) [D][884]. An Oct 2026 NUS preprint adds an eSWAP gate between two modes [P][950]. The software layer is theory: the hybrid oscillator–qubit ISA of Liu et al. [S][951] and a ⁴⁰Ca⁺ qudit–oscillator instruction set validated only in simulation [S][952].

Attributes (technology graph): carrier affinity 0.0 — natural, the motion of identical ions in a potential the trap sets. Characteristic time ≈ 300 µs (10^−3.5 s), deterministic: beam splitters of 255–468 µs, single-qubit GKP gates of 196–339 µs. Readout: through the spin — a sideband or SDF pulse, then fluorescence; about 200 µs, destructive on a bright outcome, mid-circuit only by post-selection on the dark one. Mobility: shared bus — two modes couple through any ion that moves in both. Control modality: optical, placed at room temperature. Error structure: coherent (motional dephasing from trap-frequency drift) and Gaussian small-shift (heating). Manufacturing: the ion trap.

## Physics & limits

A mode is an oscillator at the trap's secular frequency, 0.59–3.05 MHz in these experiments, with an unbounded Hilbert space: the Maryland register needed no truncation, where a binary qubit encoding of its most excited mode would have needed at least four qubits [D][884]. Control passes through the Lamb–Dicke factor and is weak — Sydney's SDF runs at a Rabi rate of 2π × 2.4 kHz, so GKP gates take hundreds of microseconds [D][949]. Dephasing, a mode's T2, follows the trap frequency — ETH recalibrated its 1.85 MHz mode every 5 min against drifts of up to 1.8 Hz/min [D][945] — and dominates Sydney's GKP gates [D][949] and the NUS eSWAP [P][950]. Heating, its T1, follows electrode noise and is worst on the centre-of-mass mode: 2.3 × 10³ quanta/s on Tsinghua's, none above the error bars on the four transverse modes the network used instead [D][948]. Motional coherence is ≲ 10 ms at Maryland against ≈ 1.5 s of idle spin coherence [D][884], ~50 ms for a Fock superposition at Sydney [D][949], 10 ms radial and 100–200 ms axial at NUS [P][950].

Two limits are structural. Mode crowding: N ions carry N transverse modes in a fixed band, so mode-selective operations slow with N; Tsinghua projects several milliseconds per beam splitter on one hundred ions at 5 µm spacing, and N times that for a fully connected interferometer [S][948]. Readout recoil: photons scattered in a bright fluorescence detection decohere the motional modes, so Sydney proceeds only when the ancilla is projected into its down state [D][949], and ETH continued a sequence only "conditional on the dark measurement result" [D][945].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: two GKP qubits in two modes of one ¹⁷¹Yb⁺ ion with a universal gate set — single-qubit logical process fidelities 0.943–0.960 in 196–339 µs, a CZ at 0.680 in 993 µs, a Bell state at 0.842 [D][949]; a 50:50 phonon beam splitter at 99.1%, 95.6% with preparation and detection [D][948]. Typical at scale: none — no register found exceeds four modes, and no commercial system is known to expose its modes as a register.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 1995-12 | Controlled-NOT between the motional and the internal qubit of one trapped ion | NIST | [D][374] |
| 1996-03 | Fock, coherent and squeezed motional states of one ⁹Be⁺ ion | NIST | [D][944] |
| 2019-02 | GKP qubit in one ⁴⁰Ca⁺ ion's motion; logical states 87.3 ± 0.7% | ETH Zürich | [D][945] |
| 2020-04 | Conditional beam splitter between two modes; single-shot parity measurement | NUS (CQT) | [D][947] |
| 2022-02 | GKP qubit corrected by dissipative pumping; logical lifetime × 3 | ETH Zürich | [D][946] |
| 2023-02 | Four-mode programmable network, five-ion chain; beam splitter 99.1% | Tsinghua | [D][948] |
| 2025-08 | Universal GKP gate set in two modes of one ion; CZ 0.680 in 993 µs | Univ. of Sydney | [D][949] |
| 2026-09 | Yukawa-model dynamics on a three-ion chain, three register modes in one circuit; in a two-mode run, occupations to eight phonons | Maryland / Duke | [D][884] |
| 2026-10 | eSWAP between two motional modes; characteristic-function overlaps 63 ± 4% and 78 ± 3% | NUS (CQT) | [P][950] |

Dominant error term: motional dephasing during preparation and gates [D][949], then heating of low-frequency and centre-of-mass modes [D][948], [P][950].

## Manufacturing, materials & supply chain

Nothing is added to an ion machine — the modes come with the trap, the control with the gate lasers — but the trap is judged differently: a register needs low heating, set by the electrode surface [G:ION-TRAP-HEATING-FLOOR], and a stable frequency difference between the modes used together, which Tsinghua ties to the DC voltages (a single mode's frequency to the RF power) — 1 s of coherence at 1 MHz would need stability of order 10⁻⁶ [S][948]. The papers name a blade trap at Maryland [D][884], a linear Paul trap at NUS [P][950] and a room-temperature Paul trap at Sydney [D][949]; none reports a surface-electrode chip. Maryland and Sydney drive the coupling with 355 nm pulsed-laser Raman transitions [D][884], [949]; UV sources are the ion supply chain's concentrated input [G:ION-SUPPLYCHAIN-2026]. The 2024 US export rule names no ion-trap item [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

Control adds tones, not lines: an SDF is two sideband tones driven together on an individually addressed ion, a beam splitter two equally detuned red sidebands on the ion that moves most in both modes [D][948], and Sydney's GKP gates are optimal-control waveforms of the SDF phases [D][949]. Readout is indirect: a zero/non-zero phonon detection by adiabatic red sideband takes ~200 µs, at 96.7% (one phonon) and 95.6% (two) with preparation [D][948]; a GKP Pauli expectation is an SDF pulse plus fluorescence [D][949]; a Fock distribution is a fit to red-sideband flopping over repeated runs [D][884]. None reads the register mid-circuit without risking it. The burden grows as spectral resolution — each mode adds a tone that must clear its neighbours, the arithmetic that slows `cx_bus`.

## Role in the stack

Architectures: the laser-addressed chain (`ion_chain`), slot 1 beside `ion`; every demonstration was laser-driven on one to five ions without transport. It requires the ion (`ion`) as host and ancilla, a laser route (`ct_ionaod`, used throughout, or `ct_ionlaser`) and fluorescence readout of the ancilla (`ro_fluor`). It is the trapped-ion alternative to the cavity mode (`cavity`) and, where the logical qubit lives in the motion, to the internal levels. It shares modes with `g_ms` and `cx_bus`: Maryland kept one set of transverse modes for MS gates and the other for the register [D][884].

Bosonic gates (`g_bos`) are defined by superconducting-circuit primitives — cat CX, dual-rail CZ, the parametric beam splitter — mediated by a transmon ancilla or a driven SQUID coupler. The mechanism carries over to motional modes with the internal levels as ancilla. The conditional displacement is Maryland's spin–phonon primitive SNP(θ, φ) = exp[−iθσʸ(e^{iφ}a + e^{−iφ}a†)/2], a resonant bichromatic SDF, with the free-boson rotations exp(−iθa†a) applied virtually as laser-phase shifts [D][884]. The beam splitter is spin-dependent, σ_z(a_m a_n† + a_m† a_n) [D][948], conditioned on one internal level in the NUS gate [D][947], and composed into an eSWAP [P][950]. The differences are of degree: gates of hundreds of microseconds against `g_bos`'s ~0.1–0.5 µs, an ancilla with seconds of coherence (T2* = 8.7 s at Sydney [D][949]), and all-to-all coupling among a chain's modes [D][948].

For bosonic simulation the register removes the encoding overhead — by Maryland's estimate O(N) qubits instead of O(N + N log Λ) at boson cutoff Λ [S][884]; for codes it is a GKP carrier (`enc_gkp`) with its own line from 2019 [D][945]. Empty neighbouring slots: a non-destructive mid-circuit readout of a mode, and laser-free bosonic control on `ion_elec`, for which no demonstration was found.

## Evidence — how the numbers were measured

Maryland's occupations are fits of red-sideband flopping of one probe ion, with Ω_n = √n Ω_1 observed empirically and a boson cutoff of 15 in the comparison [D][884] — an ensemble estimate, not a single-shot Fock-resolved readout; mode 2 of the four-site model ran separately because it decouples in the model. Figures are from the arXiv version; the published text and its Supplementary Information were not reached. Sydney's fidelities are logical process tomography through the stabiliser subsystem decomposition; the CZ was read with plain logical Pauli operators, which the authors' simulation prices at about 0.05 [D][949]. Tsinghua's 99.1% is fitted from fidelity decay over repeated beam splitters [D][948]. The NUS figures are overlaps of characteristic-function slices, against 75 ± 3% and 81 ± 2% simulated, not gate fidelities [P][950]. ETH's 87.3% averages five data sets under a 90.8% ceiling set by the approximate code states [D][945]. Value conflict: coherence depends on the mode family, so each value is quoted with its mode. Not published: the fraction of runs discarded on bright outcomes, and per-gate fidelities of the SNP gates.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| University of Sydney (Tan) | research | AU | Universal GKP gate set in two modes of one ion | [D][949] |
| ETH Zürich (Home) | research | CH | GKP encoding (2019), dissipative correction (2022) | [D][945], [946] |
| Tsinghua University (Kihwan Kim) | research | CN | Programmable four-mode phononic network | [D][948] |
| University of Maryland / Duke (Linke) | research | US | Yukawa-model simulation on a phonon register | [D][884] |
| NUS, Centre for Quantum Technologies (Matsukevich) | research | SG | Conditional beam splitter, eSWAP | [D][947], [P][950] |
| NIST | research | US | Motional qubit in the 1995 gate; nonclassical motional states | [D][374], [944] |
| North Carolina State University; a multi-institution collaboration for the hybrid ISA | theory | US | Qudit–oscillator instruction set; hybrid ISA | [S][952], [951] |

**Money.** No dated money is attached. The NUS work is funded by the National Research Foundation, Singapore, through the Centre for Quantum Technologies Funding Initiative and the Quantum Engineering Programme [P][950].

**Market & supply chain.** No product is known to offer its modes as a register; every ion vendor ships them as a gate bus, so adoption costs calibration and software, not hardware.

**IP & standards.** No patent search was made for this record. PatSnap names IonQ the filing leader on motional-mode engineering, a bus topic [P][G:PATSNAP-IONQ-PATENTS-2026]. No standard.

**Roadmaps & track record.** No vendor roadmap found names a motional register. Sydney simulates that a tenfold stronger coupling and 200 ms of motional coherence would bring dephasing error below 5 × 10⁻³ [S][949].

**Strategic reading.** Every ion machine already carries these oscillators, so the register is an option on installed hardware. Against cavities it trades speed for a long-lived ancilla and coupling between any two modes; bosonic simulation is the near use, a GKP memory the far one.

## Outlook & open questions

Confirm within 12–24 months if a GKP qubit in ion motion is error-corrected while entangled with a second, if a register of more than four modes runs in a chain of ten ions or more, or if a second species reads the ancilla mid-circuit without post-selection. Demote if motional dephasing still dominates every multi-mode result by 2028. Best case by 2029: ion machines exposing their modes as a register for bosonic simulation and GKP memory; worst case: a one- and two-mode laboratory technique.

Open questions: (1) can the ancilla be read mid-circuit without heating the register? (2) does mode crowding cap the register at a few modes per chain? (3) does QCCD transport preserve a motional state? (4) should `enc_gkp` name ion motion as a carrier? (5) can microwave gradients drive the SDF on `ion_elec` hardware?

## References

[374] C. R. Monroe, D. M. Meekhof, B. E. King, W. M. Itano, and D. J. Wineland, “Demonstration of a Fundamental Quantum Logic Gate,” *Phys. Rev. Lett.*, vol. 75, no. 25, pp. 4714–4717, Dec. 1995, doi: [10.1103/PhysRevLett.75.4714](https://doi.org/10.1103/PhysRevLett.75.4714). [D]
[884] A. T. Than *et al.*, “Quantum field theory dynamics on a spin–phonon quantum computer,” *Nat. Phys.*, Sep. 2026, doi: [10.1038/s41567-026-03402-4](https://doi.org/10.1038/s41567-026-03402-4). [arXiv:2509.11477](https://arxiv.org/abs/2509.11477). [D]
[944] D. M. Meekhof, C. Monroe, B. E. King, W. M. Itano, and D. J. Wineland, “Generation of Nonclassical Motional States of a Trapped Atom,” *Phys. Rev. Lett.*, vol. 76, no. 11, pp. 1796–1799, Mar. 1996, doi: [10.1103/PhysRevLett.76.1796](https://doi.org/10.1103/PhysRevLett.76.1796). [D]
[945] C. Flühmann, T. L. Nguyen, M. Marinelli, V. Negnevitsky, K. Mehta, and J. P. Home, “Encoding a qubit in a trapped-ion mechanical oscillator,” *Nature*, vol. 566, no. 7745, pp. 513–517, Feb. 2019, doi: [10.1038/s41586-019-0960-6](https://doi.org/10.1038/s41586-019-0960-6). [arXiv:1807.01033](https://arxiv.org/abs/1807.01033). [D]
[946] B. de Neeve, T.-L. Nguyen, T. Behrle, and J. P. Home, “Error correction of a logical grid state qubit by dissipative pumping,” *Nat. Phys.*, vol. 18, no. 3, pp. 296–300, Feb. 2022, doi: [10.1038/s41567-021-01487-7](https://doi.org/10.1038/s41567-021-01487-7). [arXiv:2010.09681](https://arxiv.org/abs/2010.09681). [D]
[947] H. C. J. Gan, G. Maslennikov, K.-W. Tseng, C. Nguyen, and D. Matsukevich, “Hybrid Quantum Computing with Conditional Beam Splitter Gate in Trapped Ion System,” *Phys. Rev. Lett.*, vol. 124, no. 17, Art. no. 170502, Apr. 2020, doi: [10.1103/PhysRevLett.124.170502](https://doi.org/10.1103/PhysRevLett.124.170502). [arXiv:1908.10117](https://arxiv.org/abs/1908.10117). [D]
[948] W. Chen *et al.*, “Scalable and programmable phononic network with trapped ions,” *Nat. Phys.*, vol. 19, no. 6, pp. 877–883, Feb. 2023, doi: [10.1038/s41567-023-01952-5](https://doi.org/10.1038/s41567-023-01952-5). [arXiv:2207.06115](https://arxiv.org/abs/2207.06115). [D]
[949] V. G. Matsos *et al.*, “Universal quantum gate set for Gottesman–Kitaev–Preskill logical qubits,” *Nat. Phys.*, vol. 21, no. 10, pp. 1664–1669, Aug. 2025, doi: [10.1038/s41567-025-03002-8](https://doi.org/10.1038/s41567-025-03002-8). [arXiv:2409.05455](https://arxiv.org/abs/2409.05455). [D]
[950] E. J. W. Koh, R. Zhang, and D. Matsukevich, “Exponential-SWAP gate between bosonic motional modes of trapped ions,” [arXiv:2610.23208](https://arxiv.org/abs/2610.23208), Oct. 2026. [P]
[951] Y. Liu *et al.*, “Hybrid Oscillator-Qubit Quantum Processors: Instruction Set Architectures, Abstract Machine Models, and Applications,” *PRX Quantum*, vol. 7, no. 1, Art. no. 010201, Jan. 2026, doi: [10.1103/4rf7-9tfx](https://doi.org/10.1103/4rf7-9tfx). [arXiv:2407.10381](https://arxiv.org/abs/2407.10381). [S]
[952] M. H. Heris, Y. Liu, and F. Mueller, “A Hardware-Native Trapped-Ion Hybrid Qudit-Oscillator Instruction Set,” [arXiv:2610.13843](https://arxiv.org/abs/2610.13843), Oct. 2026. [S]

