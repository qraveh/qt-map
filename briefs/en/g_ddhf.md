---
id: g_ddhf
name: Decoherence-protected electron–nuclear gate (DD / DDRF; colour centres)
layer: "3 Gate mechanism"
status: demonstrated
since: 2012
one_line: The two-qubit gate of colour-centre registers — the electron spin's decoupling pulses are timed to a nuclear spin's hyperfine precession (DD) or interleaved with phase-tracked radio-frequency pulses (DDRF), so the nucleus turns conditionally while the electron stays protected; best 99.93(5)% by gate set tomography on an NV electron–¹⁴N pair.
verdict: Peer-reviewed since 2012 and the entangling gate of Delft's NV registers of three to ten qubits, but slow (typically 0.4–1.6 ms per gate) and, in what was found, benchmarked by gate set tomography only in Delft; a tomography-grade result from a second group or on a spin-1/2 centre would confirm it as the platform's entangling gate, and a move of registers to faster direct gates would demote it.
updated: 2026-11-22
---

DD = dynamical decoupling (π-pulse trains on the electron spin); DDRF = dynamical decoupling interleaved with radio-frequency pulses; RF = radio frequency; GST = gate set tomography; RB = randomised benchmarking; NV = nitrogen-vacancy centre; SiV, SnV = silicon- and tin-vacancy centres in diamond; SiC = silicon carbide; CNOT = controlled-NOT gate; GHZ = Greenberger–Horne–Zeilinger state; ESR = electron spin resonance; A∥, A⊥ = hyperfine coupling components parallel and perpendicular to the magnetic field; ω_L = nuclear Larmor frequency; T₂* = electron dephasing time; CVD = chemical vapour deposition; CMOS = complementary metal–oxide–semiconductor; cryo-CMOS = CMOS circuits operated at cryogenic temperature; ASIC = application-specific integrated circuit; AWS = Amazon Web Services.

## Identity & lineage

A colour centre's electron spin is coupled to the nuclear spins around it — ¹³C in diamond, the centre's own ¹⁴N, ²⁹Si in SiC — by the hyperfine interaction, and because that coupling is anisotropic, each nucleus precesses about an axis that depends on the electron's state. A train of electron π pulses whose spacing is resonant with one nucleus's precession makes that nucleus's small rotations add up, in opposite directions for the two electron states: an electron-controlled ±π/2 rotation, equivalent to a CNOT up to single-qubit rotations. The same pulses decouple the electron from the bath and from the other nuclei, so the gate is not limited by T₂* and reaches nuclei whose coupling is too weak to resolve in a spectrum [D][961], [962]. The DDRF variant adds RF pulses on the target nucleus between the electron pulses, with phases updated to follow its precession; it reaches nuclei with negligible A⊥ and frees the pulse spacing to be chosen for electron coherence [D][963]. Registers mix the two: the seven-qubit logical-qubit device used DD on four ¹³C data qubits and DDRF on a fifth and on the ¹⁴N flag qubit [D][964].

The class begins in April 2012 with a decoherence-protected CNOT on an NV electron and its ¹⁴N at room temperature: decoupling intervals set to τ = (2n+1)π/A on the 2.16 MHz hyperfine coupling, combined with continuous RF driving, gave a process fidelity of 83(1)% (a lower bound that includes initialisation error), a Bell state of 96(1)% with 16 pulses in a 120 µs gate, and Grover's search in 322 µs [D][965]. Its introduction states that for hybrid registers a way to combine decoupling with gates "has thus far remained elusive"; it is the earliest peer-reviewed hardware of the class found. The RF-free resonant-spacing gate followed in September 2012 on weakly coupled ¹³C [D][961], and in 2014 a three-qubit register (an NV electron and two weakly coupled ¹³C) ran a bit-flip correction protocol at room temperature [D][962]. The method then left Delft: Chicago applied it to ²⁹Si in isotopically engineered SiC [D][966], and Harvard with the AWS Center for Quantum Networking built a decoupled CNOT on a SiV–²⁹Si network node [D][967].

Where the line falls. `g_mwspin` covers resonant microwave (and optical) rotations of the electron and direct, spectrally selective pulses — including the hyperfine-resolved microwave pulse that flips the electron conditional on a strongly coupled nucleus, 99.9 ± 0.1% in 30.0 ns on the SiV–²⁹Si register [D][967], and the direct RF CNOT on a strongly coupled ²⁹Si in SiC, 12.7 µs [D][966]. `g_ddhf` covers the conditional nuclear rotation made under electron decoupling, DD or DDRF. On the SiV–²⁹Si register the two meet: the nucleus-controlled electron flip is a selective pulse, while the electron-controlled nuclear flip needed decoupling, because a nuclear π rotation (23 µs) outlasts the electron's T₂* (5 µs) [D][967].

Attributes (technology graph): carrier affinity 0.5 — intermediate (natural nuclear spins around an engineered defect). Characteristic time about 0.5 ms (typically 0.4–1.6 ms; from about 76 µs to 2.4 ms measured), deterministic. Readout: none of its own; the nucleus is read through the electron (`ro_fluor`). Mobility: static — one electron serves as the bus of its register. Control modality: microwave π pulses on the electron, plus RF for DDRF, placed at room temperature, and in one preprint at a 6 K stage. Error structure: stochastic (Pauli) electron dephasing dominant; coherent crosstalk to unwanted nuclei and calibration errors. Manufacturing: inherited from the host (diamond growth and implantation).

## Physics & limits

Each decoupling unit turns the nucleus by only a small angle, of order A⊥/ω_L, so a conditional π/2 takes tens of pulses: N = 32 and 18 in 2014, for 170 and 140 µs [D][962], and up to 90 pulses in the 2019 register [D][963]. The resonances sit at τ_k ≈ (2k−1)π/(2ω_L + A∥) and are narrow, which buys selectivity — couplings near 20 kHz were resolved against an ESR linewidth of 161(1) kHz [D][961] — and costs timing: the cryo-CMOS experiment needed pulse timing to ≲ 100 ps on a resonance about 4 ns wide at 196 mT [P][968]. Weak couplings, which make nuclei good memories, and nuclear RF Rabi frequencies of about 0.5–2 kHz [D][964] make the gate slow by construction: 10²–10³ µs.

Four effects bound the fidelity. Electron dephasing during the long gate is the measured floor: GST attributes the infidelity of the 99.93% gate mainly to stochastic dephasing and bit flips of the electron [D][969], and in 2019 merely connecting the RF source lowered the electron's preserved population from 0.999(2) to 0.992(2) [D][963]. Crosstalk is coherent: nuclei within about 1 kHz of the target forced gates of 2.2–2.4 ms with Bell fidelities of 0.85(2) and 0.81(2) [D][963], and nuclear–nuclear couplings up to 16.90(4) Hz had to be echoed out over sequences up to 100 ms [D][964]. Electron spin-1/2 centres (SiV, SnV, the T centre) lose DD selectivity intrinsically; DDRF recovers part of it, and on a SnV it gave a gate fidelity of 0.874(4) [D][970]. Finally, the hyperfine coupling that makes the gate also dephases the register whenever the electron is optically read or reset [D][964]; on the SiV node, 14 electron readouts at 95% fidelity cost a 1/e loss of nuclear coherence [D][967].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: 99.93(5)% for the electron–¹⁴N DDRF gate by two-qubit GST (four-run mean 99.923 ± 0.026%), at 4 K in isotopically purified diamond [D][969]. Typical at scale: 0.95–0.99 per gate, estimated from Bell-state fidelities, for the five ¹³C gates of the seven-qubit logical-qubit experiment, at 419–1556 µs per gate; its ¹⁴N gate, 389 µs, has a lower bound of 0.94(1) [D][964].

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2012-04 | Decoherence-protected CNOT, NV electron + ¹⁴N, room temperature: process fidelity 83(1)% (lower bound), Bell 96(1)% | TU Delft, Ames Laboratory, UC Santa Barbara, Univ. of Southern California | [D][965] |
| 2012-09 | RF-free DD conditional rotation of weakly coupled ¹³C (couplings to about 20 kHz), maximally entangling at N = 28 | TU Delft, Ulm, Ames Laboratory | [D][961] |
| 2014-02 | Three-qubit register (NV + two ¹³C): conditional ±π/2 in 140–170 µs; bit-flip correction protocol | TU Delft, Ames Laboratory | [D][962] |
| 2019-09 | DDRF gate: Bell 0.972(8), gate 0.991(9) (model estimate, one pair; 0.93(1) / 0.97(1) in the register); ten-qubit register, all 45 pairs entangled, GHZ up to 7 qubits | QuTech, Element Six | [D][963] |
| 2020-12 | DD gate on weakly coupled ²⁹Si in isotopically purified SiC: conditional ±π/2 at 97(1)% | University of Chicago | [D][966] |
| 2022-06 | Logical qubit on seven spins: DD and DDRF gates on ¹³C 0.95–0.99 in 419–1556 µs; ¹⁴N gate ≥ 0.94(1) in 389 µs | QuTech | [D][964] |
| 2022-11 | SiV–²⁹Si decoupled CNOT (DD + interleaved RF): 93.7 ± 0.7% in 292 µs | Harvard, AWS | [D][967] |
| 2025-03 | Electron–¹⁴N DDRF gate: 99.93(5)% by two-qubit GST | QuTech (Fujitsu joint programme) | [D][969] |
| 2025-04 | SnV (spin-1/2) + ¹³C DDRF gate: 0.874(4), Bell 72(3)% | QuTech | [D][970] |
| 2026-06 | Six DDRF gates in a seven-qubit register by GST: mean 99.18(2)%, best 99.61(5)% | QuTech | [P][971] |
| 2026-10 | DD gate driven by a cryo-CMOS controller at 6 K: Bell 88.6(8)%, gate ≥ 95(2)% | QuTech, TU Delft | [P][968] |

Dominant error term: stochastic dephasing of the electron spin during the decoupled gate [D][969]; coherent crosstalk where spectrally close nuclei exist [D][963].

## Manufacturing, materials & supply chain

The gate adds no fabrication of its own but turns the host's nuclear-spin statistics into a supply question. In natural-abundance diamond (1.1% ¹³C) a register is found, not made: three weakly coupled ¹³C were controlled for each of three NV centres studied in 2014 [D][962], and the logical-qubit device drew on 27 characterised ¹³C around one NV selected for having none coupled above 500 kHz [D][964]. Isotopic purification trades register size for clean spectra: the 99.93% gate used diamond targeted at 0.01% ¹³C and therefore the ¹⁴N [D][969], and Chicago computed an optimal isotope fraction for SiC that maximises the number of usable nuclear memories [D][966]. RF delivery heats the sample: an amplified RF line cost readout photons through heating in 2019 [D][963], and the cryo-CMOS experiment attributes a drop in readout contrast likely to sample heating [P][968].

## Control, readout & I/O burden

One microwave line for the electron and one RF line shared by every nucleus of the register: nuclei are selected by frequency and pulse spacing, so the wiring grows per defect, not per qubit. The price is serial operation — the single electron is the bus — and nanosecond timing: the logical-qubit experiment timed gates to 1 ns from a room-temperature arbitrary waveform generator [D][964]. In the cryo-CMOS demonstration, a controller ASIC glued beside the diamond on a 6 K cold head generated the GHz electron drive and the MHz nuclear drive — 45 mW for the electron driver from a 1.1 V supply, 17 mW for the nuclear driver, 12 mW idle. Its DD gate on a ¹³C (A∥ = 31 kHz, A⊥ = 130 kHz) used N = 28 pulses at τ = 1.3507 µs, about 76 µs by the paper's own T = 2Nτ, with parts of the sequence still run by the room-temperature system [P][968]. Readout is the electron's (`ro_fluor`): a nucleus is measured by mapping it onto the electron, and the laser is shut within 2 µs of a detected photon to limit nuclear dephasing [D][964].

## Role in the stack

Architectures: the colour-centre architecture (`defect`), slot 3, beside `g_mwspin`, as its decoherence-protected entangling gate. It requires the carrier `defect`, `g_mwspin` for the decoupling π pulses, and a control route — `ct_rt`, which the path holds, or `ct_cryocmos`, which one preprint now shows driving the gate [P][968]. It complements `enc_spin_ld` (the nuclear-spin qubits it addresses), `ro_fluor` (readout through the electron) and `ic_spinphoton`, since a decoupled gate is what swaps the electron's state into a nuclear memory [D][967]. It is not an alternative to `g_mwspin`, whose pulses it is made of, nor to `g_exch`, which couples electrons rather than an electron and a nucleus. Derived clock: a weight-four stabiliser needs four sequential electron–nuclear gates, so at 389–1556 µs per gate one round takes several milliseconds before readout [S][964]; the electron gates of `g_mwspin` (1.344 µs for a direct microwave π/2 [D][969]) never bind.

## Evidence — how the numbers were measured

The 99.93(5)% is an average gate fidelity from two-qubit GST process matrices; across four runs it is 99.923 ± 0.026% [D][969]. It is the result behind the Fujitsu/QuTech release of Mar 2025, which trade press carried as error rates "below 0.1%" [P][208]: the paper (Phys. Rev. Applied, 21 Mar 2025) acknowledges the joint Fujitsu–TU Delft programme "Modular quantum computers", and its two-qubit gate is a DDRF gate. The seven-qubit figures are GST too [P][971]. The other fidelities are weaker estimates: the 2019 0.991(9) and the logical-qubit 0.95–0.99 convert electron–nuclear Bell-state fidelities through a depolarising model [D][963], [964]; the cryo-CMOS ≥ 95(2)% is a lower bound from a Bell fidelity of 88.6(8)% that assumes all other gates ideal [P][968]; the 2012 83(1)% is process tomography including about 5% initialisation error [D][965]. The Delft authors note that a 99.92% electron–nuclear gate fidelity reported elsewhere by subspace RB is an upper limit rather than a best estimate [D][969]. Not published: the duration of the 99.93% gate in its paper's main text, an error budget for the cryo-CMOS gate, a GST benchmark of a DD or DDRF gate outside Delft (none found), and parallel gates on two nuclei, a future avenue named in 2019 [D][963].

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| QuTech / TU Delft (Taminiau and Hanson groups) | research | NL | Originated the DD (2012–14) and DDRF (2019) gates; GST to 99.93%; logical qubit; SnV and cryo-CMOS work | [D][962], [969] |
| TU Delft cryo-CMOS designers (Sebastiano, Babaie) | research | NL | Cryo-CMOS electron- and nuclear-spin controller | [P][968] |
| Ames Laboratory / Iowa State University (Dobrovitski) | research | US | Gate design and theory of 2012 | [D][965] |
| Harvard University with the AWS Center for Quantum Networking | research / industry | US | Decoupled CNOT on a SiV–²⁹Si network node | [D][967] |
| University of Chicago (Awschalom) | research | US | DD gates on ²⁹Si in isotopically engineered SiC | [D][966] |
| Fujitsu | industry partner | JP | Joint research programme with TU Delft acknowledged in the 99.93% paper | [D][969], [P][208] |
| Element Six | supplier | UK | CVD diamond for the Delft registers; co-authors | [D][963] |

**Money.** No dated money is attached to this gate; the Fujitsu–TU Delft programme is acknowledged without an amount [D][969].

**Market & supply chain.** No product is documented as using the gate; it is a laboratory method resting on merchant diamond and on microwave and RF electronics common to every spin platform.

**IP & standards.** No patent search was made for this record. No standard covers the gate.

**Roadmaps & track record.** The 2014 paper pointed to "surface-code quantum computing based on multi-qubit nodes" [D][962]; the record since is a seven-qubit logical qubit with flagged stabiliser measurements [D][964] and a seven-qubit register presented as "at the threshold for distributed quantum computation" [P][971]. No dated roadmap names the gate.

**Strategic reading.** The gate turns a colour centre from one qubit into a node. Its slowness costs little against photonic links but decides local error correction, where millisecond gates meet optical readouts that dephase the register. Whether the spin-1/2 centres (SiV, SnV, T centre) reach NV-class fidelity with DDRF decides how far it travels beyond the NV.

## Outlook & open questions

Confirm within 12–24 months if a group outside Delft publishes a GST- or RB-benchmarked DD or DDRF gate above 99%, if a spin-1/2 centre passes 99%, or if a cryo-CMOS-driven gate reaches the 99% class. Demote if colour-centre registers move to faster direct or optimal-control gates on strongly coupled nuclei, or if the seven-qubit GST results remain without a journal version by end-2027. Best case by 2029: ten-qubit nodes with gates at 99.5% or better, driven by cold CMOS beside the diamond; worst case: a Delft NV specialty, while spin-1/2 nodes keep one or two strongly coupled nuclei driven by selective pulses.

Open questions: (1) can two nuclei be gated in parallel by frequency multiplexing? (2) what limits the cryo-CMOS gate — timing jitter, heating or electron dephasing? (3) does DDRF reach 99% on SiV, SnV or T centres? (4) can millisecond gates fit repeated error-correction rounds whose optical readouts dephase the register? (5) does the 99.9% class carry over from ¹⁴N to ¹³C qubits with crosstalk?

## References

[208] M. Swayne, “Fujitsu And QuTech Realize High-Precision Quantum Gates,” The Quantum Insider, Mar. 28, 2025. [Online]. Available: https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ [P]
[961] T. H. Taminiau, J. J. T. Wagenaar, T. van der Sar, F. Jelezko, V. V. Dobrovitski, and R. Hanson, “Detection and control of individual nuclear spins using a weakly coupled electron spin,” *Phys. Rev. Lett.*, vol. 109, no. 13, Art. no. 137602, Sep. 2012, doi: [10.1103/PhysRevLett.109.137602](https://doi.org/10.1103/PhysRevLett.109.137602). [arXiv:1205.4128](https://arxiv.org/abs/1205.4128). [D]
[962] T. H. Taminiau, J. Cramer, T. van der Sar, V. V. Dobrovitski, and R. Hanson, “Universal control and error correction in multi-qubit spin registers in diamond,” *Nat. Nanotechnol.*, vol. 9, no. 3, pp. 171–176, Feb. 2014, doi: [10.1038/nnano.2014.2](https://doi.org/10.1038/nnano.2014.2). [arXiv:1309.5452](https://arxiv.org/abs/1309.5452). [D]
[963] C. E. Bradley *et al.*, “A Ten-Qubit Solid-State Spin Register with Quantum Memory up to One Minute,” *Phys. Rev. X*, vol. 9, no. 3, Art. no. 031045, Sep. 2019, doi: [10.1103/PhysRevX.9.031045](https://doi.org/10.1103/PhysRevX.9.031045). [arXiv:1905.02094](https://arxiv.org/abs/1905.02094). [D]
[964] M. H. Abobeih *et al.*, “Fault-tolerant operation of a logical qubit in a diamond quantum processor,” *Nature*, vol. 606, no. 7916, pp. 884–889, Jun. 2022, doi: [10.1038/s41586-022-04819-6](https://doi.org/10.1038/s41586-022-04819-6). [arXiv:2108.01646](https://arxiv.org/abs/2108.01646). [D]
[965] T. van der Sar *et al.*, “Decoherence-protected quantum gates for a hybrid solid-state spin register,” *Nature*, vol. 484, no. 7392, pp. 82–86, Apr. 2012, doi: [10.1038/nature10900](https://doi.org/10.1038/nature10900). [arXiv:1202.4379](https://arxiv.org/abs/1202.4379). [D]
[966] A. Bourassa *et al.*, “Entanglement and control of single nuclear spins in isotopically engineered silicon carbide,” *Nat. Mater.*, vol. 19, no. 12, pp. 1319–1325, Dec. 2020, doi: [10.1038/s41563-020-00802-6](https://doi.org/10.1038/s41563-020-00802-6). [arXiv:2005.07602](https://arxiv.org/abs/2005.07602). [D]
[967] P.-J. Stas *et al.*, “Robust multi-qubit quantum network node with integrated error detection,” *Science*, vol. 378, no. 6619, pp. 557–560, Nov. 2022, doi: [10.1126/science.add9771](https://doi.org/10.1126/science.add9771). [arXiv:2207.13128](https://arxiv.org/abs/2207.13128). [D]
[968] H. B. van Ommen *et al.*, “Two-qubit cryo-CMOS control of a spin register in diamond,” [arXiv:2610.26413](https://arxiv.org/abs/2610.26413), Oct. 2026. [P]
[969] H. P. Bartling *et al.*, “Universal high-fidelity quantum gates for spin qubits in diamond,” *Phys. Rev. Appl.*, vol. 23, no. 3, Art. no. 034052, Mar. 2025, doi: [10.1103/PhysRevApplied.23.034052](https://doi.org/10.1103/PhysRevApplied.23.034052). [arXiv:2403.10633](https://arxiv.org/abs/2403.10633). [D]
[970] H. K. C. Beukers *et al.*, “Control of solid-state nuclear spin qubits using an electron spin-1/2,” *Phys. Rev. X*, vol. 15, Art. no. 021011, Apr. 2025, doi: [10.1103/PhysRevX.15.021011](https://doi.org/10.1103/PhysRevX.15.021011). [arXiv:2409.08977](https://arxiv.org/abs/2409.08977). [D]
[971] M. van Riggelen, J. Yun, H. B. van Ommen, and T. H. Taminiau, “High-fidelity two-qubit gates in a 7-qubit register for quantum networks,” [arXiv:2606.14847](https://arxiv.org/abs/2606.14847), Jun. 2026. [P]

