---
id: code_bosonic
name: Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC)
layer: "7 Code"
tier: 2
status: emerging
since: 2024
one_line: A discrete outer code — repetition or qLDPC — wrapped around a bosonic inner qubit whose noise is already shaped, so the outer code corrects only one residual channel.
verdict: The whole family rests on one number, the phase-flip rate under a gate. Measured hardware is two orders of magnitude away from every published resource estimate.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The construction shapes the inner qubit's noise so the outer code has less to do. A cat qubit stabilised by two-photon dissipation suppresses bit-flips exponentially in photon number while phase-flips grow only linearly, so a 1D repetition code suffices: distance d costs d cats, not d². A GKP inner qubit instead hands up an analogue shift syndrome that a qLDPC outer code decodes with soft information. Theory came first and is precise. Gouzien et al. (PRL 131, 040602, 2023) size a repetition-cat machine at 126,133 cats, 19 photons each, for a 256-bit elliptic-curve logarithm in 9 hours at an assumed loss ratio of 10⁻⁵ [S][1]; Ruiz et al. then gave 2D-local LDPC-cat codes, 758 cats for 100 logical qubits at ≤10⁻⁸ per cycle, assuming ~0.1% phase-flip [S][2].
Coordinates: partly fabricated (0.75); static, no control channel or readout of its own; biased plus Gaussian error — "Outer code exploits inner bias/shift correction; Ocelot d=3→5 nearly flat; LDPC-cat assumes 0.1% phase-flip (measured ~10%)" (graph record).

## Physics & limits
The family trades one error channel against another, and the exchange rate is the noise bias. Photon number buys exponential bit-flip suppression and pays linearly in phase-flips, so an architecture picks the point where bit-flips fall below the outer code's reach and lives with the rate left — assumed near 10⁻³. Hardware is not there: in Ocelot's CX at |α|² = 2 the phase-flip is 9.6(4)×10⁻² and the bit-flip 3.5(4)×10⁻³, a bias above 25 under the gate and above 30 idle [D][3] — a per-CX figure, not per cycle. The deeper limit: bias belongs to the idle manifold and a dissipative CX degrades the asymmetry the code is built on, so the open problem is a bias-preserving gate, not a better memory. What moves the floor: a larger ratio of two-photon dissipation to single-photon loss, and unitary rather than dissipative gates.

## Engineering state of the art
One hardware result carries the family: Ocelot (Putterman et al., AWS and Caltech, Nature 638, 927, 2025-02-26), a repetition code over five cat qubits with four ancilla transmons and five buffer modes — logical error 1.75(2)% at distance 3 and 1.65(3)% at distance 5, per 2.8 µs cycle [D][3]. These are not the same operating point (d=3 at |α|² = 1, d=5 at |α|² = 1.5), so the repeated "flat below threshold" mixes a distance step with a photon-number step and scaling is not isolated. No bias-preserving cat–cat CNOT exists — the AWS-affiliated proposal is unitary and simulated [S][5] — and no GKP-plus-qLDPC hardware exists.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-01 | LDPC-cat, 2D-local: 758 cats → 100 logical at ≤10⁻⁸/cycle, assumes 0.1% phase-flip | Ruiz et al. | [S][2] |
| 2025-02 | Ocelot: 1.75(2)% at d=3 (\|α\|²=1) → 1.65(3)% at d=5 (\|α\|²=1.5), 2.8 µs cycle | AWS/Caltech | [D][3] |
| 2026-07 | Unitary bias-preserving cat–cat CNOT; d=7 repetition of 13 cats below 10⁻⁶, simulated | AWS-affiliated | [S][5] |

## Manufacturing, materials & supply chain
No process step of its own: this is an architecture and a decoder, and the graph record leaves fabrication unset. It inherits the cat or GKP host — Nb/Al circuits with parametric elements, buffer modes, high-Q storage, an ancilla transmon per data qubit, a refrigerator. The accounting worth keeping is Ocelot's fourteen engineered elements for five data cats — the real denominator behind any "fewer qubits" comparison [D][3]. Helium draws about 40 kW for a logical qubit using as few as 18 cats [C][4]. No code-specific export control exists; ECCN 3A904 applies to the host [G][11].

## Control, readout & I/O burden
The decoder is the cheap part: a 1D repetition syndrome stream is simpler than 2D matching and, at 2.8 µs, inside existing FPGA decoders. The cost moved into analogue stabilisation — each cat needs a two-photon dissipation drive, a buffer pump, an ancilla transmon and readout, so lines per data qubit exceed a bare transmon's. The saving is in code distance, not wiring: at 10³ cats the cryostat resembles a 10³-transmon machine with extra pumps. The cycle is also 2.5× slower than a 1.1 µs surface-code cycle [D][7].

## Role in the stack
The code requires a biased cat or a GKP inner qubit; as the terminal outer layer it has no dependents, and it replaces fusion-based discrete-variable fault tolerance. It sits on the superconducting bosonic path (Alice & Bob, AWS, Nord Quantique) and the photonic path, where Xanadu concatenates GKP under qLDPC [C][G:XANADU-LIQUIDITY-2026-06]. Switching inner qubits is no re-parameterisation: the cat branch buys a 1D outer code and owes a bias-preserving gate; the GKP branch buys an analogue syndrome and owes ~10 dB of squeezing. Its derived-clock contribution (= sum of the syndrome round: gate layers + transport + readout + reset) is d₂ = 2 gate layers, a 1.44 µs round against the measured 2.8 µs cycle [D][3]. The neighbouring empty slot is an LDPC-cat memory on hardware — unbuilt as of 4 Sep 2026.

## Verification (QCVV)
The "100–1000× fewer qubits" claim is a resource estimate, not a measurement, and both papers state the assumption plainly: ~0.1% phase-flip [S][1][2]; hardware is at 9.6×10⁻² per CX [D][3]. No protocol captures gate-level bias preservation under load, because the gate does not exist; Ocelot has no independent replication and mixes operating points across its distance comparison. Helium is sold but publishes no logical-performance data, and the roadmap quotes a September 2025 *peak* bit-flip time of 252 minutes against a 44-minute mean for the same run [C][6].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| AWS | Developer | US | Ocelot repetition-cat hardware; cat–cat CNOT proposal | [D][3] |
| Alice & Bob | Developer | FR | Cat hardware; Graphene repetition-cat roadmap | [C][6] |
| Nord Quantique | Developer | CA | GKP inner qubits for an outer code | [D][10] |
| Xanadu | Developer | CA | Optical GKP under qLDPC, roadmap stage | [R][G:XANADU-SPAC-2026-03] |
| D-Wave | Developer | US | Bosonic gate-model roadmap after buying Quantum Circuits | [C][G:DWAVE-QCI-2026-01] |

**Money.**
- 2025-01-28 · Alice & Bob · Series B · €100 M · NVentures extension 2026-05-22, undisclosed · closed [C][G:AB-SERIESB-2025-01]
- 2025-11-06 · DARPA · QBI Stage B: Nord Quantique and Xanadu in, Alice & Bob not · ≤$15 M each · closed [G:QBI-STAGEB-2025-11]
- 2026-01-20 · D-Wave · acquisition of Quantum Circuits · $550 M ($300 M stock, $250 M cash) · closed [C][G:DWAVE-QCI-2026-01]
- 2026-05-18 · Nord Quantique · growth equity · $30 M at a $1.4 B valuation · closed [C][G:NQ-1.4B-2026-05]

**Market & supply chain.** Nobody sells this layer; it is bundled into machines with a superconducting bill of materials, so concentration risk sits with amplifier and refrigerator vendors, not foundries. G3 and G4 pay for it indirectly: what customers buy is the qubit-count claim, which is why GENCI's June 2026 Helium purchase precedes any published logical-performance number [C][G:AB-SERIESB-2025-01].

**IP & standards.** No dated, code-specific patent-family count was found in any named database. The constructions are academic and openly published, so defensible IP sits in the stabilisation circuits — buffer design, two-photon dissipation, bias-preserving gates — not the codes. No standards activity found.

**Roadmaps & track record.** Alice & Bob (as of 2026-09-04): Helium, 12–18 cats and one logical qubit at 10⁻², current; then 48, 250 and finally 2,000 cats for 100 logical at 10⁻⁶ in 2030, with a stated 13-minute bit-flip requirement [R][6]. D-Wave (2026-06-01): 10 logical in 2030, 100 in 2032, Λ = 10 [R][G:DWAVE-QCI-2026-01]. Xanadu: fault tolerance 2028–29 [R][G:XANADU-LIQUIDITY-2026-06]. Every roadmap is in logical qubits while the demonstrated quantity is one at 10⁻²; AWS publishes no dated roadmap and holds the only scaling data.

**Strategic reading.** This family is the bosonic companies' only argument against better-funded transmon incumbents: close the phase-flip gap and they leapfrog on qubit count per dollar. Fail, and qLDPC-on-transmon or dual-rail erasure takes the slot without needing an unproven bias-preserving gate.

*Open niche:* a small QCVV/SFQ house can plug in at the gap: independent measurement of bias preservation under a two-qubit gate, protocols separating a distance step from a photon-number step, and decoder verification against measured rather than assumed phase-flip rates.

## Outlook & open questions
Confirm or demote within 12–24 months: a demonstrated bias-preserving cat–cat CNOT; a distance scan at fixed photon number; any LDPC-cat or GKP-plus-qLDPC hardware result. Best case by 2029: a repetition-cat logical qubit with isolated below-threshold scaling and a measured bias-preserving gate, making the 758-cat estimate arguable. Worst case: phase-flip stays near 10⁻¹ and the family survives as a research line. Open: whether bias survives any two-qubit gate.

## Sources
[1] Gouzien, Ruiz, Le Régent, Guillaud, Sangouard · "Performance analysis of a repetition cat code architecture: computing 256-bit elliptic curve logarithm in 9 hours with 126133 cat qubits" · Phys. Rev. Lett. 131, 040602 · 2023-02-13 · https://arxiv.org/abs/2302.06639
[2] Ruiz, Guillaud, Leverrier, Mirrahimi, Vuillot · "LDPC-cat codes for low-overhead quantum computing in 2D" · Nature Communications 16, 1040; arXiv:2401.09541 · 2024-01-17 · https://arxiv.org/abs/2401.09541
[3] Putterman et al. (AWS, Caltech) · "Hardware-efficient quantum error correction via concatenated bosonic qubits" (Ocelot) · Nature 638, 927 · 2025-02-26 · https://www.nature.com/articles/s41586-025-08642-7
[4] Alice & Bob · Helium system announcement [C] · 2026-06-10 · https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/
[5] Ye et al. (AWS-affiliated) · unitary bias-preserving cat–cat CNOT proposal · arXiv:2607.22852 · 2026-07-24 · https://arxiv.org/abs/2607.22852
[6] Alice & Bob · public roadmap (Boson 4 → Helium → Lithium → Beryllium → Graphene) [C] · retrieved 2026-09-04 · https://alice-bob.com/roadmap/
[7] Google Quantum AI · "Quantum error correction below the surface code threshold" (1.1 µs cycle) · Nature 638, 920 · 2024-12-09 · https://www.nature.com/articles/s41586-024-08449-y
[8] D-Wave · acquisition of Quantum Circuits Inc. [C] · 2026-01-07 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[9] Xanadu · roadmap to 1,000+ logical qubits by 2031 [C] · 2026-08-31 · https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html
[10] Turcotte et al. (Nord Quantique) · grid-state qubit with SPAM below 10⁻³ · arXiv:2607.06718 · 2026-07-07 · https://arxiv.org/abs/2607.06718
[11] US BIS · interim final rule, quantum ECCNs including 3A904 · Federal Register · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent

## Open verification items
No independent replication of the Ocelot result exists. Ocelot's d=3 and d=5 points were taken at different photon numbers, so no distance scan at fixed operating point has been published by anyone. No LDPC-cat or GKP-plus-qLDPC code has been run on hardware. Alice & Bob's Helium has no published logical-error measurement, and its roadmap quotes a peak rather than mean bit-flip time. No dated, code-specific patent-family count was found. AWS discloses no funding line for the Ocelot programme.
