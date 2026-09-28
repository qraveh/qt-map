---
id: enc_opt
name: Optical narrow-line qubit (ion S–D, atom clock)
layer: "2 Encoding"
status: demonstrated
since: 2003
one_line: "A qubit split between a ground level and a metastable level one optical photon above it — the S₁/₂–D₅/₂ quadrupole line of ⁴⁰Ca⁺ or ⁸⁸Sr⁺, or the ¹S₀–³P₀ clock line of neutral Sr/Yb — with one narrow-line laser driving every gate."
verdict: "Proven on both carriers — ⁴⁰Ca⁺ in AQT's shipped machines, ⁸⁸Sr clock qubits at 99.62(3) % entangling fidelity in the laboratory — but coherence is set by the laser and the magnetic field, not the atom: 90(30) ms against a 1.168(7) s D₅/₂ lifetime in AQT's demonstrator. As of 2026-09-26 planqc, the register's only company on the atomic clock qubit, publishes no gate error or coherence time of its own."
updated: 2026-09-26
---

T₂ = Ramsey phase-coherence time; MS = Mølmer–Sørensen gate; CZ = controlled-Z gate; SPAM = state preparation and measurement; QV = quantum volume; TRL = technology readiness level; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The ion realisation stores |1⟩ in |4S₁/₂, m = −1/2⟩ and |0⟩ in |3D₅/₂, m = −1/2⟩ of ⁴⁰Ca⁺, coupled by the 729 nm electric-quadrupole line [D][253]. Innsbruck ran the Cirac–Zoller CNOT on two such ions in 2003 [D][376]; the encoding carried its fault-tolerant universal gate set of 2022 [D][255] and AQT's products. ⁸⁸Sr⁺ at 674 nm is the sister ion, its D₅/₂ lifetime measured on a single ion at NPL [D][377]. The atom realisation uses ¹S₀ and ³P₀ of neutral strontium, the lattice-clock line, run in tweezers since 2019 [D][378], with alkaline-earth Rydberg entanglement from 2020 [D][379]. Attributes: natural carrier; no time, mobility or control of its own; errors Pauli plus leakage.

## Physics & limits
Three ceilings. Lifetime: τ(D₅/₂, ⁴⁰Ca⁺) = 1.168(7) s [D][253], so T₂ ≤ 2τ ≈ 2.3 s; decay from m = −1/2 may land in S₁/₂, m = +1/2, outside the qubit pair — leakage [G]. The Sr ³P₀ level outlives the >3 s atomic coherence measured in a tweezer clock [D][378]. Field: ⁴⁰Ca⁺ has no hyperfine structure, hence no field-insensitive line; with g(D₅/₂) = 6/5 and g(S₁/₂) ≈ 2.002 the qubit line moves 0.40 μ_B B ≈ 5.6 kHz per µT, so 0.1 µT of noise shifts it 560 Hz, a radian in 0.3 ms [S]. Mitigations: shielding, mains feed-forward, dynamical decoupling, decoherence-free pairs. The J = 0 → J = 0 clock line has no first-order electronic Zeeman shift [G]. Laser: every gate references the laser phase, so T₂ is the laser's coherence over the circuit. AQT measured Ramsey T₂ = 90(30) ms on the optical qubit against 18(1) ms on the ground-state Zeeman qubit, naming magnetic noise from mains and neighbouring magnets beyond 25 ms [D][253] — 26× below the lifetime bound [S].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2003-03 | Cirac–Zoller CNOT on two ⁴⁰Ca⁺ S–D qubits | Innsbruck | [D][376] |
| 2019 | Sr tweezer clock, >3 s coherence, duty cycle up to 96 % | JILA | [D][378] |
| 2021-06 | τ(D₅/₂) 1.168(7) s; T₂ 90(30) ms; 24-ion GHZ fidelity 0.544(7) | AQT/Innsbruck | [D][253] |
| 2022-08 | Sr clock-qubit Bell state 92.8(2.0) % SPAM-corrected; Bell coherence 4.2(6) s | JILA | [D][380] |
| 2024-10 | ⁸⁸Sr clock-qubit entangling gate 99.62(3) %; ancilla readout | Caltech | [D][381] |
| 2026-05 | LYNX QV 32,768; first units Q4 2026 | AQT | [C][128] |

The shipped figure: IBEX Q1, 12 qubits, 1Q 99.97(1) %, 2Q 98.7(3) % over all pairs, QV 128 [C][382]; MARMOT, 20 qubits, 2Q (98.47 ± 0.3) % on an 11-qubit register [C][383]. Atoms lead on fidelity, ions on deployment.

## Manufacturing, materials & supply chain
No fabricated part; the item is the narrow-line laser — 729 nm (Ca⁺), 674 nm (Sr⁺), 698 nm (Sr) — locked to a high-finesse reference cavity [G]. AQT's demonstrator uses seven wavelengths (375, 397, 423, 515, 729, 854, 866 nm); the 854 nm quench laser exists only because the qubit level is metastable [D][253]. IBEX Q1 fills two 19-inch racks, 2 m², <2 kW, at (22.0 ± 1.5) °C [C][382].

## Control, readout & I/O burden
One phase-stable laser per species, split into individually addressed 729 nm beams on the ion chain [D][255]; fibre and modulator phase noise lands directly on the qubit [S]. Readout is electron shelving — D₅/₂ stays dark on the 397 nm cycling line — by camera or photodiode, ~99.9 % in 300 µs [D][253]; atoms add ancilla-based read-out with non-destructive conditional reset [D][381].

## Role in the stack
Slot 2 of Trapped ions — linear Paul trap with individual laser addressing, and of Rydberg tweezer array — alkaline-earth (Yb/Sr), erasure-native, beside enc_hf and enc_omg. It **requires** either ion (S–D quadrupole transition) or ae_atom (¹S₀–³P₀ of Sr/Yb). It is **replaced** by enc_hf, whose field-insensitive ground-state pair trades the one-laser drive for Raman or microwave control. It **provides** single-laser universality and shelving readout, and the metastable manifold that the omg erasure scheme reuses [S][333]; it **defines** the channel metric τ(D₅/₂) = 1.17 s. Register: aqt-ibex-q1 ✅ and uibk-innsbruck-ion ✅; psnc-piast-q 🔎 (20 AQT qubits, species unnamed — consistent with MARMOT); planqc-maqcs 🔎. Gap G-enc-clock is answered: the ledger's 10–100 ms is planqc's range in a press profile [P][247], 30–300× below published clock-qubit arrays [D][380], so it measures a laser, not the encoding.

## Evidence — how the numbers were measured
AQT's 98.7(3) % is an all-pairs product average [C][382]; a secondary 97.7 % in the register stays unreconciled. The demonstrator's 0.997(6) is a two-ion Bell-state fidelity, not randomised benchmarking [D][253]. Caltech's 99.62(3) % is averaged over symmetric input states [D][381]. LYNX publishes QV without qubit count or fidelity [C][128]. No vendor reports T₂ beside τ, as of 2026-09-26.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| AQT | developer | Austria | IBEX Q1, MARMOT, LYNX on ⁴⁰Ca⁺ | [C][383] |
| University of Innsbruck | research | Austria | Origin; fault-tolerant gates on ⁴⁰Ca⁺ | [D][255] |
| planqc | developer | Germany | Sr clock-transition qubits; MAQCS at LRZ | [P][247] |
| JILA / Kaufman group | research | US | Sr clock-qubit Bell states | [D][380] |
| Caltech / Endres group | research | US | ⁸⁸Sr clock-qubit gates, ancilla readout | [D][381] |

**Money.**
- 2024-07 · planqc · Series A · €50 M · closed [P][247]
- 2026-09-09 · planqc / LRZ · MAQCS, first hardware delivered · almost €20 M (BMFTR) · under construction [C][161]

**Market & supply chain.** One ultrastable laser and cavity per species is the concentration point. Pays into G2, G3 and G7.

**IP & standards.** No patent search was run; no standard defines reporting of laser-limited T₂, as of 2026-09-26.

**Roadmaps & track record.** (AQT · LYNX first units · Q4 2026) [C][128]; (planqc · MAQCS co-processor · end-2027, TRL 5 today, 6–7 targeted) [R][161].

**Strategic reading.** On ions the encoding is AQT's legacy, its depth capped by τ; on atoms it is the best-gated clock qubit, and a clock-grade laser on a processor is the prize.

## Outlook & open questions
Confirm the atomic branch if planqc publishes clock-qubit T₂ and CZ fidelity on MAQCS hardware by 2027-12-31; demote it to metrology if not. Confirm the ion branch if LYNX ships in Q4 2026 with per-pair 2Q figures. Open questions. (1) What laser linewidth would bring ⁴⁰Ca⁺ T₂ to its 2.3 s bound? (2) Is planqc's 10–100 ms the lattice, the laser or the field? (3) How much D₅/₂ decay leaks versus flips? (4) Will AQT move to a hyperfine or omg species? (5) Can one clock laser serve 10³ sites?

## Sources

[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[161] planqc, “MAQCS takes shape as first quantum computing hardware arrives at LRZ,” Sep. 9, 2026. [Online]. Available: https://planqc.eu/news/maqcs-takes-shape-as-first-quantum-computing-hardware-arrives-at-lrz [C]
[247] M. Ivezic, “Planqc,” PostQuantum, May 22, 2025. [Online]. Available: https://postquantum.com/quantum-computing-companies/planqc/ [P]
[253] I. Pogorelov *et al.*, “Compact Ion-Trap Quantum Computing Demonstrator,” *PRX Quantum*, vol. 2, no. 2, Art. no. 020343, Jun. 2021, doi: [10.1103/PRXQuantum.2.020343](https://doi.org/10.1103/PRXQuantum.2.020343). [arXiv:2101.11390](https://arxiv.org/abs/2101.11390). [D]
[255] L. Postler *et al.*, “Demonstration of fault-tolerant universal quantum gate operations,” *Nature*, vol. 605, pp. 675–680, 2022, doi: [10.1038/s41586-022-04721-1](https://doi.org/10.1038/s41586-022-04721-1). [arXiv:2111.12654](https://arxiv.org/abs/2111.12654). [D]
[333] D. T. C. Allcock *et al.*, “omg blueprint for trapped ion quantum computing with metastable states,” *Appl. Phys. Lett.*, vol. 119, no. 21, Art. no. 214002, Nov. 2021, doi: [10.1063/5.0069544](https://doi.org/10.1063/5.0069544). [arXiv:2109.01272](https://arxiv.org/abs/2109.01272). [S]
[376] F. Schmidt-Kaler *et al.*, “Realization of the Cirac–Zoller controlled-NOT quantum gate,” *Nature*, vol. 422, pp. 408–411, Mar. 2003, doi: [10.1038/nature01494](https://doi.org/10.1038/nature01494). [D]
[377] V. Letchumanan, M. A. Wilson, P. Gill, and A. G. Sinclair, “Lifetime measurement of the metastable 4d ²D₅/₂ state in ⁸⁸Sr⁺ using a single trapped ion,” *Phys. Rev. A*, vol. 72, Art. no. 012509, Jul. 2005, doi: [10.1103/PhysRevA.72.012509](https://doi.org/10.1103/PhysRevA.72.012509). [D]
[378] M. A. Norcia *et al.*, “Seconds-scale coherence on an optical clock transition in a tweezer array,” *Science*, vol. 366, p. 93, 2019. [arXiv:1904.10934](https://arxiv.org/abs/1904.10934). [D]
[379] I. S. Madjarov *et al.*, “High-fidelity entanglement and detection of alkaline-earth Rydberg atoms,” *Nat. Phys.*, vol. 16, pp. 857–861, May 2020, doi: [10.1038/s41567-020-0903-z](https://doi.org/10.1038/s41567-020-0903-z). [arXiv:2001.04455](https://arxiv.org/abs/2001.04455). [D]
[380] N. Schine, A. W. Young, W. J. Eckner, M. J. Martin, and A. M. Kaufman, “Long-lived Bell states in an array of optical clock qubits,” *Nat. Phys.*, vol. 18, pp. 1067–1073, Aug. 2022, doi: [10.1038/s41567-022-01678-w](https://doi.org/10.1038/s41567-022-01678-w). [arXiv:2111.14653](https://arxiv.org/abs/2111.14653). [D]
[381] R. Finkelstein *et al.*, “Universal quantum operations and ancilla-based read-out for tweezer clocks,” *Nature*, vol. 634, pp. 321–327, Oct. 2024, doi: [10.1038/s41586-024-08005-8](https://doi.org/10.1038/s41586-024-08005-8). [D]
[382] Alpine Quantum Technologies, “19-inch rack-mounted quantum computer,” AQT. [Online]. Available: https://www.aqt.eu/products/ibex-q1/ [C]
[383] Alpine Quantum Technologies (AQT), “Quantum computer products built for performance,” AQT. [Online]. Available: https://www.aqt.eu/products/ [C]

## Open verification items
- 2026-09-26: arxiv.org (abstract of 2111.14653v2) and api.semanticscholar.org returned HTTP 429; Schine et al. read at nature.com instead.
- 2026-09-26: ⁸⁸Sr⁺ D₅/₂ lifetime (dossier: 0.39 s) not stated — Crossref elides the abstract, journals.aps.org returned 403.
- 2026-09-26: ⁸⁷Sr ³P₀ natural lifetime (~118 s) not verified; no source opened.
- 2026-09-26: planqc's own technology and LRZ pages name neither strontium nor the clock transition; PIAST-Q's species and product are unnamed on the pages in the register.
- 2026-09-26: arXiv:2111.12654 not re-opened (register ✅ relied on); Madjarov et al.'s fidelity number, Finkelstein et al.'s arXiv id and Norcia et al.'s author list and DOI (arXiv page showed only the abstract) not seen.
