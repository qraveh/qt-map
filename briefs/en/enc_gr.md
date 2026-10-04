---
id: enc_gr
name: Ground–Rydberg analog qubit
layer: "2 Encoding"
status: demonstrated
since: 2017
one_line: "A two-level qubit formed by an atomic ground state |g⟩ and a Rydberg state |r⟩, driven globally under an Ising-type Hamiltonian: the computational basis of analog Rydberg simulators, not an error-suppressing code."
verdict: "Its ceiling is the black-body-limited Rydberg lifetime (~150 µs for Rb 70S at 300 K), but its working window is set by Doppler and laser-phase dephasing (T2* ≈ 5–6 µs), which caps Aquila programs at 4 µs. As of 2026-09-26 it has no memory and no code, and both vendors' gate-model lines use the hyperfine basis instead."
updated: 2026-09-26
---

Ω = Rabi frequency; Δ = detuning; C6 = van der Waals coefficient; R_b = blockade radius; T2* = Ramsey dephasing time; T2echo = spin-echo coherence time; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The qubit is a level pair inside one atom: |g⟩ in the 5S₁/₂ ground manifold and |r⟩ = |70S₁/₂⟩ in QuEra's ⁸⁷Rb machine Aquila, reached by a two-photon 420 nm + 1013 nm drive via 6P₃/₂ [C][262]. "Encoding" names the computational basis of an analog machine, not a code: the program is a Hamiltonian, the output a g/r pattern. The line starts with the 51-atom Harvard–MIT Ising-type simulator of 2017 [D][384], co-authored by QuEra's CEO Alexander Keesling [C][262]; Pasqal's architecture paper calls it the analog level, "programming Hamiltonian sequences" [C][385]. Attributes: natural carrier, nothing fabricated; no step time, control modality or placement of its own; loss and coherent errors.

## Physics & limits
Aquila runs H(t) = (Ω/2)Σᵢ(e^{iφ}|gᵢ⟩⟨rᵢ| + h.c.) − ΔΣᵢnᵢ + Σ_{i<j} C6/|xᵢ−xⱼ|⁶ nᵢnⱼ, nᵢ = |rᵢ⟩⟨rᵢ|, with C6 = 5.42×10⁶ rad µm⁶ µs⁻¹ for 70S, |Ω| ≤ 15.8 rad/µs, |Δ| ≤ 125 rad/µs [C][262]; Pulser uses the same convention for Pasqal's "ground-rydberg" basis [C][386]. Blockade forbids two excitations within R_b = (C6/Ω)^{1/6} ≈ 8.4 µm at full drive [S][262].

Three limits act on |r⟩. Decay: Rb 70S lives 410 µs at 0 K but 152 µs at 300 K (60S: 104 µs) [S][387], black-body radiation carrying ~63% of the rate — the ceiling, and a loss channel. Doppler: for counter-propagating beams (k_eff ≈ 8.8 µm⁻¹) at 10 µK, a detuning spread σ ≈ 0.27 rad/µs gives a Ramsey 1/e time ≈ 5 µs [S][262], matching the measured T2* = 4.5(1) µs [D][388]. Phase noise and scattering: echo leaves T2 = 32(6) µs; T1 = 51(6) µs combines the 146 µs Rydberg lifetime with ~80 µs of 6P3/2 scattering [D][388]. The 12.6(1) s hyperfine T2 of a Cs tweezer array [D][138] does not apply: |r⟩ cannot be shelved, so there is no memory.

## Engineering state of the art

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2017-07-13 | 51-atom programmable Ising-type model on g–r qubits | Harvard/MIT | [D][384] |
| 2018-05 | g–r Rabi damping traced to several few-percent effects | Browaeys–Lahaye group | [D][389] |
| 2018-09 | T2* 4.5(1) µs, T2echo 32(6) µs, Bell fidelity 0.97(3) | Harvard/MIT | [D][388] |
| 2023-06-20 | Aquila: 256 sites, T2* 5.8 µs, T2echo 11.4 µs, 4 µs cap | QuEra | [C][262] |
| 2023-10-11 | Sr g–r Bell fidelity ≥0.9971 after erasure excision | Caltech | [D][143] |
| 2024-10-21 | (2+1)D string breaking, kagome array, local-detuning quench | QuEra, Zoller, Lukin | [D][226] |

The window has barely moved: T2* rose from 4.5 to 5.8 µs, and Aquila stops programs at 4 µs, the "approximate timescale of coherent evolution" [C][262].

## Manufacturing, materials & supply chain
Nothing is fabricated at this layer; fabrication sits in fab_optics. The demand is spectral: a Rydberg laser pair beside 780 nm tweezers [C][262] whose phase noise, not power, sets coherence; the 2018 gain came from reference-cavity filtering (FWHM ≈ 2π × 500 kHz) and injection locking [D][388]. A cold enclosure would move 70S from 152 µs toward 410 µs [S][387]; the register profiles the commercial machines as room-temperature.

## Control, readout & I/O burden
Aquila drives one global Ω(t), Δ(t), φ(t) set [C][262], so drive I/O is flat in atom number; local detuning, the first site-resolved knob, drove the string-breaking quench [D][226] and is promised for Pasqal's Vela [R][390]. Readout is destructive imaging with an asymmetric budget — Rydberg read as ground 0.08, ground as Rydberg 0.01, filling error 0.007 [C][262] — so r-populations are undercounted [S][262]. At under 10 shots per second [C][262], 10⁴ shots take over a quarter-hour.

## Role in the stack
On the architecture "Neutral-atom analog simulator (Rydberg arrays, lattice gases)" (atom_analog) the technology fills slot 2; slots 7–9 (code to interconnect) are empty. It **requires** an atom with a Rydberg level (alkali), **provides** the ground–Rydberg states g_rydanalog requires, and is **replaced** by enc_hf. Register machines: Aquila (primary, ✅), Fresnel / Fresnel 2 (primary, 🔎), Orion Alpha/Beta/Gamma (alternate, analog mode on atom_rb, 🔎 inferred). Gate-model lines use enc_hf: QuEra's Gemini is a 260-qubit digital machine [C][137]; the Harvard–MIT gate work encodes in |F=1,mF=0⟩, |F=2,mF=0⟩ and visits 53S1/2 only during gates [D][391]; Pasqal drives a separate "digital" basis |g⟩,|h⟩ by Raman channel [C][386]. The gap ledger stands: enc_hf does not describe analog machines. Its atom_rb/atom_ae placement became atom_analog; the alkaline-earth variant [D][143] has no register machine.

## Evidence — how the numbers were measured
Gate benchmarks do not apply; the figures are T2*, echo T2, Rabi damping, blockaded-pair coherence and readout asymmetry. Aquila publishes all of them (Rabi 7.5 µs, blockaded Rabi 8.9 µs) [C][262], none independently re-measured; beyond classical simulation, programs are checked against phase diagrams [D][226]. Grades: Aquila ✅; Fresnel 🔎, the paper's abstract confirming only the analog/digital split [C][385]; Orion 🔎, its cited blog naming neither analog mode nor encoding [C][390] — Pulser's basis definition is better evidence.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| QuEra Computing | developer | US | Aquila, 256-site g–r machine with public coherence budget | [C][262] |
| Pasqal | developer | France | Fresnel; "ground-rydberg" basis in Pulser | [C][385][C][386] |
| Harvard/MIT (Lukin group) | research | US | Origin of the g–r simulator and its coherence analysis | [D][384][D][388] |
| Caltech (Endres group) | research | US | Strontium g–r qubit with erasure detection | [D][143] |

**Money.** No dated financial item is specific to the ground–Rydberg encoding as of 2026-09-26.

**Market & supply chain.** Two commercial actors, both also selling gate-model machines; Pasqal lists five hosting clouds and five sites, mode unstated [C][390]. Concentration sits in Rydberg lasers and cavities. Pays into G1.

**IP & standards.** No standard for analog-qubit figures was found as of 2026-09-26; the shared Hamiltonian convention is the de facto interface [C][262][C][386].

**Roadmaps & track record.** Pasqal (2026-01-29): Vela in 2026, over 256 qubits with local detuning; measurable quantum advantage before mid-2026 [R][390] — not scored here. QuEra's next product is gate-model [C][137].

**Strategic reading.** Scale without per-qubit control, code or storage, bounded by a few-microsecond window. If analog results survive classical challenge, it keeps a G1 niche as a mode of digital machines; if not, both vendors already sell the hyperfine alternative.

## Outlook & open questions
Confirm if by 2027-12-31 a commercial analog machine publishes T2* above 20 µs; demote if Vela ships without coherence figures or no peer-reviewed analog-advantage result appears by 2027-06-30. Open questions. (1) Why is Aquila's echo time a third of the 2018 value? (2) How does T2* scale with register size? (3) Will erasure-detecting alkaline-earth g–r qubits reach a product? (4) Which Rydberg level and coherence do Fresnel and Orion run? (5) Does the readout asymmetry bias published phase diagrams?

## References
[137] QuEra Computing Inc., “Gemini-Class Gate-Model Quantum Computer.” [Online]. Available: https://www.quera.com/gemini [C]
[138] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[143] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[226] D. González-Cuadra *et al.*, “Observation of string breaking on a (2 + 1)D Rydberg quantum simulator,” *Nature*, vol. 642, no. 8067, pp. 321–326, Jun. 2025, doi: [10.1038/s41586-025-09051-6](https://doi.org/10.1038/s41586-025-09051-6). [D]
[262] J. Wurtz *et al.*, “Aquila: QuEra's 256-qubit neutral-atom quantum computer,” [arXiv:2306.11727](https://arxiv.org/abs/2306.11727), Jun. 2023. [C]
[384] H. Bernien *et al.*, “Probing many-body dynamics on a 51-atom quantum simulator,” *Nature*, vol. 551, pp. 579–584, Nov. 2017, doi: [10.1038/nature24622](https://doi.org/10.1038/nature24622). [arXiv:1707.04344](https://arxiv.org/abs/1707.04344). [D]
[385] L. Henriet *et al.*, “Quantum computing with neutral atoms,” *Quantum*, vol. 4, Art. no. 327, Sep. 2020, doi: [10.22331/q-2020-09-21-327](https://doi.org/10.22331/q-2020-09-21-327). [arXiv:2006.12326](https://arxiv.org/abs/2006.12326). [C]
[386] Pasqal (Pulser open-source project), “Conventions — Pulser 1.9.1 documentation,” Pulser documentation. [Online]. Available: https://pulser.readthedocs.io/en/stable/conventions.html [C]
[387] I. I. Beterov, I. I. Ryabtsev, D. B. Tretyakov, and V. M. Entin, “Quasiclassical calculations of blackbody-radiation-induced depopulation rates and effective lifetimes of Rydberg nS, nP, and nD alkali-metal atoms with n ≤ 80,” *Phys. Rev. A*, vol. 79, no. 5, Art. no. 052504, 2009, doi: [10.1103/PhysRevA.79.052504](https://doi.org/10.1103/PhysRevA.79.052504). [arXiv:0810.0339](https://arxiv.org/abs/0810.0339). [S]
[388] H. Levine *et al.*, “High-fidelity control and entanglement of Rydberg-atom qubits,” *Phys. Rev. Lett.*, vol. 121, no. 12, Art. no. 123603, Sep. 2018, doi: [10.1103/PhysRevLett.121.123603](https://doi.org/10.1103/PhysRevLett.121.123603). [arXiv:1806.04682](https://arxiv.org/abs/1806.04682). [D]
[389] S. de Léséleuc, D. Barredo, V. Lienhard, A. Browaeys, and T. Lahaye, “Analysis of imperfections in the coherent optical excitation of single atoms to Rydberg states,” *Phys. Rev. A*, vol. 97, no. 5, Art. no. 053803, May 2018, doi: [10.1103/PhysRevA.97.053803](https://doi.org/10.1103/PhysRevA.97.053803). [arXiv:1802.10424](https://arxiv.org/abs/1802.10424). [D]
[390] L. Garbini, “Inside Pasqal's 2026 Vision on Quantum for Industry and Research,” Pasqal, Jan. 29, 2026. [Online]. Available: https://www.pasqal.com/blog/inside-pasqals-2026-vision-on-quantum-for-industry-and-research/ [R]
[391] S. J. Evered *et al.*, “High-fidelity parallel entangling gates on a neutral-atom quantum computer,” *Nature*, vol. 622, no. 7982, pp. 268–272, Oct. 2023, doi: [10.1038/s41586-023-06481-y](https://doi.org/10.1038/s41586-023-06481-y). [arXiv:2304.05420](https://arxiv.org/abs/2304.05420). [D]

## Open verification items
- 2026-09-26: the arXiv page for 1802.10424 (v2) was refused by the fetch proxy (HTTP 429); its record rests on the v1 abstract and APS/ADS search results, authors after the first two unconfirmed.
- 2026-09-26: Fresnel and Orion Rydberg level, T2* and echo time not found in the Pasqal pages opened; Fig. 6b of arXiv:2006.12326 not opened, only its abstract.
- 2026-09-26: Gemini's product page names ⁸⁷Rb and digital mode, not the hyperfine pair; its enc_hf placement rests on the Harvard–MIT gate papers.
- 2026-09-26: the string-breaking abstract does not name Aquila; QuEra authorship suggests it, unconfirmed.
- 2026-09-26: whether Vela shipped and whether Pasqal's mid-2026 advantage objective was met were not checked.
- 2026-09-26: the Aquila text opened gives neither the beam geometry assumed in the Doppler estimate nor the F, mF sublevel of |g⟩ in analog mode.
