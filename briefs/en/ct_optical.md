---
id: ct_optical
name: Optical delivery of qubit control (fibre link + cryogenic photodiode)
layer: "5 Control"
status: emerging
since: 2024
one_line: Control waveforms synthesised at room temperature travel into the refrigerator as modulated light on an optical fibre and a cryogenic photodiode turns them back into microwave and flux pulses; through it a single-qubit gate has reached 99.915% and a CZ 99.676% (pure; 99.445% dressed), and a gate set has crossed 10 km of fibre from one refrigerator to another.
verdict: The fibre removes the coaxial lines and attenuators above the photodiode, and one preprint puts an optically driven gate 0.19% below its coaxial baseline; but in the two best 2026 results the photodiode sits at 4 K, so the lines from 4 K to the qubits remain and the I/O wall moves down rather than away. Confirm with an optically driven processor of ten or more qubits at its coaxial baseline, or photodiodes at the mixing chamber inside its cooling budget; demote if no work goes beyond two qubits by 2028.
updated: 2026-11-22
---

PD = photodiode; UTC-PD = uni-travelling-carrier photodiode; InGaAs = indium gallium arsenide; EOM = electro-optic modulator; XEB = cross-entropy benchmarking; RB = randomised benchmarking; CZ = controlled-Z gate; XY / Z = a transmon's microwave drive and flux control; T1 / T2 = energy-relaxation / dephasing time; DC = direct current; IC = integrated circuit; I/O = input/output; BAQIS = Beijing Academy of Quantum Information Sciences.

## Identity & lineage

Superconducting qubits are driven through coaxial lines that cross the refrigerator with a cascade of attenuators — the wall the room-temperature route (`ct_rt`) runs into. This technology keeps the room-temperature electronics and replaces the cable: the waveform is written onto a laser's intensity, carried down an optical fibre of negligible thermal conductance, and regenerated as a photocurrent by a PD on a cold stage that feeds the qubit's line. NIST Boulder showed it in 2021 with a commercial InGaAs PD at 20 mK: Rabi oscillations at 44 MHz from a 4 µA photocurrent, a Ramsey T2 of 37 µs whether the qubit was read out through the link or through coax, and 98% single-shot readout; for the gates, "High qubit gate fidelity is expected" — none was benchmarked [D][981].

Benchmarked gates followed. USTC's directly modulated link gave a single-qubit XEB error of 0.139% (Jan 2024) [D][982]. Nanjing University, with the PD on the mixing-chamber plate, reached a single-qubit RB Clifford fidelity of 98.35% against 97.88% through coax — comparable, by the authors' reading — and separately drove two qubits at once, with Rabi oscillations and no benchmark (Mar 2025) [D][983]. Harvard and Rigetti used a lithium-niobate electro-optic transducer at about 15 mK as the receiver, for Rabi oscillations only (Apr 2025) [D][984]. In Sep 2026 USTC put the PDs at 4 K, sent the XY and Z controls of two tunable transmons through fibre, and reached single-qubit 99.915% and CZ 99.676% [D][985]. A Tsinghua–USTC–ShanghaiTech line with its own UTC-PD arrays then delivered a gate set from one refrigerator to another over 10.1 km of fibre: a Brillouin microwave-to-optical transducer in the first writes the waveform onto light, PDs in the second regenerate it, and a transmon and a cavity qubit are entangled through it (Nov 2026) [P][986].

The `since` year is 2024, the earliest peer-reviewed benchmarked gate found through an optical link; NIST's 2021 drive, with no gate benchmarked, is the founding demonstration, as the 2012 shared-line drive is for `ct_fdm`. Optical readout — qubit signals converted to light by electro-optic, optomechanical or piezo-optomechanical transducers — is the reverse direction and a readout technology [P][987].

Attributes (technology graph): carrier affinity 1.0 — fabricated. Characteristic time: none of its own. Readout: none. Mobility: none. Control modality: electro-optic, placed first at the 4 K stage (the PD position of the two best 2026 results), then at the millikelvin stage (NIST, Nanjing), with laser and modulator at room temperature. Error structure: coherent (the drive amplitude follows optical power and polarisation) and stochastic Pauli (shot-noise excitation). Manufacturing: telecom photonic components — III–V photodiodes, lithium-niobate modulators, lasers; nothing on the qubit chip.

## Physics & limits

A PD is a square-law detector: power modulated at the qubit frequency yields a microwave current at that frequency on top of a mean photocurrent [D][981]. Intensity cannot be negative, so the mean current dissipates without driving anything — biasing the modulator at its null point instead of its quadrature point cuts the thermal load and improves the signal-to-noise ratio [D][983] — and pre-distorted flux pulses need an added bias [D][985].

Shot noise reaches the qubit as thermal-like microwave noise. NIST saw the excited-state population rise linearly with photocurrent, as shot noise predicts, with no excess noise resolved, and they infer a negligible effect at the 4 µA used for gates [D][981]; their estimated floor is an error probability above 4×10⁻⁵ for a 6 GHz qubit on a 50 Ω line with a 1 ms external decay time, and a PD shared by several qubits drives them all with its noise [S][981].

A fibre's passive load on the mixing chamber is about 3 pW against 14 nW for a 2.16 mm stainless-steel coax [S][981]; the active load is the absorbed light itself. USTC estimates 0.058 mW per XY channel and 0.752 mW with Z, so the 1.5 W of a 4 K stage serves about 25,800 XY channels or 2,000 XY-and-Z channels, and the 19 µW of the mixing chamber, at 0.006 mW per XY channel there, about three XY-only channels and not one with flux [S][985] — USTC's stated reason for regenerating the signal at 4 K and running the last stretch on coax [D][985]; the 10-km link's PDs also sit on the 4 K stage [P][986]. NIST's millikelvin case rests on a low duty cycle [S][981].

Cold PDs add two limits. InGaAs's cut-off moves from 1,687 nm to 1,508–1,511 nm on cooling, so USTC and NIST drive their InGaAs PDs at 1,490 nm [D][985], [981], while Nanjing reports a 1,550 nm laser on its PD at the mixing chamber [D][983]; UTC-PDs run at zero bias, with no DC wiring and a bandwidth above 9 GHz at 3.4 K [P][986]. And the gate amplitude becomes an optical power: polarisation drift in the fibre moves the optimal X-gate drive [D][985], and intensity noise of the optical reference damps the 10 km link's Rabi oscillations [P][986].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: in one refrigerator, PDs at 4 K carrying the XY and Z controls of two tunable transmons with a coupler — single-qubit Pauli fidelities 99.915 ± 0.005% and 99.854 ± 0.014%, CZ 99.676 ± 0.041% by XEB [D][985]; between refrigerators, single-qubit RB (95.36 ± 0.13)% and a Bell state at 80.6 ± 13.1% across 10.1 km [P][986]. Typical at scale: none — no published device beyond two qubits and a coupler is driven through fibre; USTC's 2026 multichannel abstract gives no channel count [D][988].

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-03 | PD at 20 mK drives a transmon: Rabi 44 MHz at 4 µA; T2 the same read out through link or coax; no gate benchmark | NIST Boulder | [D][981] |
| 2024-01 | Earliest benchmarked gate found through an optical link: single-qubit XEB error 0.139% | USTC | [D][982] |
| 2025-03 | PD on the mixing-chamber plate: single-qubit RB 98.35% vs 97.88% through coax; two qubits driven at once (Rabi only) | Nanjing University | [D][983] |
| 2025-04 | Electro-optic transducer at ~15 mK as the receiver: Rabi oscillations only | Harvard / Rigetti | [D][984] |
| 2025-12 | UTC-PD arrays at 3.3 K: RB 99.59%, 0.19% below coax; optical readout added | Tsinghua / USTC / ShanghaiTech / BAQIS | [P][987] |
| 2025-12 | Storage cavity: Fock states up to ten photons; control over 15 km above 95% | Tsinghua / USTC / ShanghaiTech | [P][989] |
| 2026-09 | PDs at 4 K carry XY and Z: single-qubit 99.915 ± 0.005%, CZ 99.676 ± 0.041% | USTC / QuantumCTek | [D][985] |
| 2026-11 | Two refrigerators, 10.1 km: single-qubit RB (95.36 ± 0.13)%, Bell state 80.6 ± 13.1% | Tsinghua / USTC / ShanghaiTech / BAQIS | [P][986] |

Dominant error term: in the best single-refrigerator result, not the link — its estimated control error, 0.004–0.053%, lies far below the qubits' decoherence [D][985]; across refrigerators, relaxation, dephasing and drive-amplitude fluctuations [P][986].

## Manufacturing, materials & supply chain

Nothing on the qubit chip changes. The parts are telecom photonics: a 1,490 nm distributed-feedback laser modulated directly, chosen for linearity over an external modulator [D][985], or a laser with an EOM [D][981]; InGaAs photodiodes, commercial at NIST [D][981], or UTC-PD arrays from ShanghaiTech's device laboratory [P][986]; fibre amplifiers and feedthroughs. The fragile step is cold optical coupling: NIST's PD fell from 0.7 to 0.5 A/W on cooling, probably through thermal contraction of the alignment [D][981]; the 10 km link's transducer couples at 1.4% each way through a cryogenic nanopositioner [P][986]. On-chip multi-wavelength sources and modulators — the photonic-IC route (`fab_pic`) — are the authors' stated direction [P][987]. Export-control exposure: that of the cryogenic and quantum items around it [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

Above the PD each coaxial line and its attenuators become a fibre; below it nothing changes yet — with the PD at 3.3 K, about 1 m of coax still runs to the qubits [P][987], a segment USTC calls a challenge shared with cryogenic electronics [D][985]. A broadband PD lets one fibre carry several tones: one optical channel synthesised 4.954 GHz gate pulses and 7.584 GHz readout probe tones together [P][987], and the two-refrigerator link addressed qubit and cavity with one transducer by choosing the optical reference [P][986]. Flux pulses ride the same link [D][985]; the receiving module needs no synthesiser or local oscillator [P][986].

## Role in the stack

Architectures: an alternate control technology on the transmon lattice with tunable couplers (`sc`), shown on tunable transmons and on a transmon–cavity pair. It requires the room-temperature route (`ct_rt`) — whose sources synthesise the waveforms and whose coax still carries the last stretch — and is its alternative: coaxial lines against optical fibre into the refrigerator. It is also an alternative to cryo-CMOS (`ct_cryocmos`) and single-flux-quantum control (`ct_sfq`), which generate pulses cold, as USTC sets out [D][985]. It complements frequency-division multiplexing (`ct_fdm`), which a broadband PD carries naturally, and vertical delivery (`ct_vio`), which still routes the pulse into the chip. Between refrigerators it is the classical companion of the quantum links: cryogenic microwave links (`ic_cryolink`) span tens of metres [P][986], and the quantum transducer (`ic_transducer`) must convert quantum states, whereas the same kind of device used here as a classical modulator works at a system efficiency of 1.5×10⁻⁷ [P][986]. It is not `ct_eo`, the electro-optic switching of photonic machines, where the light is the qubit. Price of switching: cold photodiodes, cryogenic optical alignment, a heat budget at 4 K; gained: picowatts of passive load per channel above the PD.

## Evidence — how the numbers were measured

The 99.915% is a Pauli fidelity from XEB with speckle purity benchmarking, 50 ns gates; the CZ's 99.676% is the pure fidelity derived from a dressed 99.445 ± 0.041%, with a 38 ns gate; the link's control error — XEB error minus purity error — is 0.004–0.053% [D][985]. A Pauli fidelity is not a Clifford RB average, so it does not compare one-to-one with the RB figures of the UTC-PD preprint (99.59%) [P][987] or Nanjing (98.35%) [D][983]. In the two-refrigerator work RB used 1 µs pulses over 50 repetitions; the Bell fidelity came from a reconstructed density matrix over five repetitions, hence ±13.1%; readout and tomography used local microwave lines; T1 is not given [P][986]. The heat figures are calculations, not measured loads [S][985], [981].

Light and coherence: NIST saw T1 unchanged with 2 µW on the PD [D][981]; Nanjing saw no effect within its sensitivity [D][983]; the UTC-PD preprint saw T1 ≈ 51 µs and T2 ≈ 8.8 µs unchanged under continuous illumination [P][987]; the two-refrigerator authors report unexplained "unconventional decoherence processes" in their link [P][986]. Value conflicts: the UTC-PD preprint gives 99.5% in its introduction and 99.59% in its results (the Atlas uses the result); USTC's two 2026 CZ figures, 99.676% (pure, with its method described; 99.445% dressed) and 99.424% (stated in the second paper's abstract without its method), are both given, the first as the record. Not published: an optically driven device beyond two qubits, a measured heat load at scale, benchmarked two-qubit gates with the PD at the mixing chamber.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| NIST Boulder (Teufel, Quinlan, Diddams) | research | US | PD at 20 mK; the founding demonstration, 2021 | [D][981] |
| USTC / Hefei National Laboratory (Zhu, Peng, Pan) | research | CN | Directly modulated lasers, PDs at 4 K; the 99.915% and CZ records | [D][982], [985], [988] |
| QuantumCTek | developer | CN | A co-author's affiliation on USTC's 2026 paper | [D][985] |
| Nanjing University (Sun, Wu) | research | CN | Null-biased modulator, PD at the mixing chamber, two qubits | [D][983] |
| Tsinghua / USTC / ShanghaiTech / BAQIS (Sun, Zou, Chen, Yu) | research | CN | UTC-PD arrays, all-optical I/O, the 10 km link | [P][987], [986] |
| Harvard (Lončar) / Rigetti Computing | research / developer | US | Transducer at the mixing chamber driving a Rigetti-made transmon | [D][984] |

**Money.** No dated money is attached to this technology; the Chinese work names national science programmes [P][986], and no product or financing round appears in the sources read.

**Market & supply chain.** The parts are telecom commodities; adoption would move value from coaxial cable, attenuator and connector vendors to photonic-transceiver makers and to whoever qualifies PD arrays at 4 K.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** No vendor roadmap read for this record names optical control delivery. NIST's 2021 path "towards a million-qubit universal quantum computer" [D][981] has led to benchmarked and two-qubit gates, but to no device beyond two qubits.

**Strategic reading.** After a US founding paper the work is mostly Chinese. Its strongest case is not inside one refrigerator, where cryo-CMOS and multiplexing attack the same wall, but between refrigerators: a modular machine needs drives and phase references in every module, and an optical link delivers them with no synthesiser at the receiver [P][986].

## Outlook & open questions

Confirm within 12–24 months if an optically driven processor of ten or more qubits matches its coaxial baseline, if PDs at the mixing chamber run benchmarked two-qubit gates inside its cooling budget, or if a vendor ships optical control lines. Demote if no work goes beyond two qubits by 2028, or if cryo-CMOS takes the 4 K stage while the coax below it stays one line per drive. Best case by 2029: a multi-refrigerator superconducting machine whose drives and references arrive over fibre; worst case: a laboratory alternative to coax that no processor needs.

Open questions: (1) does T1 stay unchanged at the photocurrents of a full processor, with PDs at the mixing chamber? (2) how many tones can one PD carry before shot noise and intermodulation set the error? (3) what is the heat per channel at 4 K when measured? (4) what feed-forward latency does a kilometre-scale link add against a microsecond error-correction cycle? (5) can the PD arrays and multi-wavelength sources move onto photonic chips?

## References

[981] F. Lecocq, F. Quinlan, K. Cicak, J. Aumentado, S. A. Diddams, and J. D. Teufel, “Control and readout of a superconducting qubit using a photonic link,” *Nature*, vol. 591, no. 7851, pp. 575–579, Mar. 2021, doi: [10.1038/s41586-021-03268-x](https://doi.org/10.1038/s41586-021-03268-x). [arXiv:2009.01167](https://arxiv.org/abs/2009.01167). [D]
[982] N. Li *et al.*, “Optical transmission of microwave control signal towards large-scale superconducting quantum computing,” *Optics Express*, vol. 32, Art. no. 3989, Jan. 2024, doi: [10.1364/oe.514909](https://doi.org/10.1364/oe.514909). [D]
[983] W. Xu *et al.*, “Manipulations of a transmon qubit with a null-biased electro-optic fiber link,” *Nat. Commun.*, vol. 16, Art. no. 2629, Mar. 2025, doi: [10.1038/s41467-025-57820-8](https://doi.org/10.1038/s41467-025-57820-8). [D]
[984] H. K. Warner *et al.*, “Coherent control of a superconducting qubit using light,” *Nat. Phys.*, vol. 21, pp. 831–838, Apr. 2025, doi: [10.1038/s41567-025-02812-0](https://doi.org/10.1038/s41567-025-02812-0). [arXiv:2310.16155](https://arxiv.org/abs/2310.16155). [D]
[985] Y.-H. Li *et al.*, “High-fidelity control of superconducting qubits with an optically transmitted signal,” *Phys. Rev. A*, vol. 114, no. 3, Art. no. 032427, Sep. 2026, doi: [10.1103/m1wg-synr](https://doi.org/10.1103/m1wg-synr). [arXiv:2608.19602](https://arxiv.org/abs/2608.19602). [D]
[986] C. Ma *et al.*, “Universal two-qubit control across dilution refrigerators via a 10-km coherent optical link,” [arXiv:2611.12481](https://arxiv.org/abs/2611.12481), Nov. 2026. [P]
[987] X. Pan *et al.*, “All-optical control and multiplexed readout of multiple superconducting qubits,” [arXiv:2512.21199](https://arxiv.org/abs/2512.21199), Dec. 2025. [P]
[988] N. Li *et al.*, “Towards fault-tolerant quantum computing with optically controlled superconducting qubits,” *Optics Express*, vol. 34, Art. no. 43602, Nov. 2026, doi: [10.1364/oe.616363](https://doi.org/10.1364/oe.616363). [D]
[989] C. Ma *et al.*, “Scalable Optical Links for Controlling Bosonic Quantum Processors,” [arXiv:2512.10706](https://arxiv.org/abs/2512.10706), Dec. 2025. [P]

