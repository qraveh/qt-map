---
id: enc_spin_ld
name: Single-spin (Loss–DiVincenzo) / nuclear-spin encoding
layer: "2 Encoding"
tier: 3
status: demonstrated
since: 1998
one_line: One qubit per spin-1/2 — a confined electron, hole or nucleus — with no encoded subspace, giving the smallest footprint and no leakage channel.
verdict: The default encoding on every silicon, germanium, donor and defect platform; it buys minimum area and a clean Pauli error model at the cost of a resonant drive per qubit.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
One physical spin-1/2 is one qubit: an electron or hole in a gate-defined dot, or a nucleus bound to a donor or defect. Loss and DiVincenzo set it out in 1998 — dot-confined electron spins, rotations by a local resonant field, two-qubit gates by pulsed exchange [D][1]. The nuclear variant drives a ³¹P or defect nucleus by radio frequency through hyperfine coupling to an electron, trading speed for coherence: nuclei as data, electrons as ancillas.  Coordinates: affinity — a near-natural carrier with no composite structure; error — coherent dephasing plus Pauli error, no leakage subspace, no control modality or fabrication of its own.

## Physics & limits
The computational space is the whole two-level system: nothing leaks out, so every error is Pauli or coherent as the codes assume — and nothing is filtered out either. T2* is set by residual ²⁹Si hyperfine coupling and by charge noise turned into a frequency shift through the g-factor or a micromagnet; ²⁸Si purification removes the first term. Coherence is not the limit today: QuTech's microwave-free array bounds its hopping gate at ≥99.50(6)% [D][2] and foundry two-qubit gates sit at 99.04–99.56% [D][3] — a calibration-limited plateau, not a T2 limit. Deeper purification, baseband control and cold calibration move the floor.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2025-07-01 | ≥99.50(6)% hopping gate (lower bound), no microwave, 2×2 array | QuTech/TU Delft | [D][2] |
| 2025-09-24 | 99.04–99.56% two-qubit on 300 mm foundry SiMOS | Diraq | [D][3] |
| 2025-12-17 | 11-qubit donor register, 9 nuclear plus 2 electron, 99.10–99.99% | Silicon Quantum Computing | [D][4] |

Dominant term: calibration drift across the array; no device above 12 qubits publishes all-pairs fidelities.

## Manufacturing, materials & supply chain
The encoding adds no structure — one dot or donor per qubit, about a third of the dots an exchange-only qubit needs — and inherits the carrier's process: Intel's 300 mm EUV line at >24,000 devices per wafer and 96% tune-up yield [D][5], plus 22FDX, FD-SOI and imec 300 mm. The burden it imposes is control: one resonant drive per qubit frequency, so at 10³ qubits the wall is frequency crowding and microwave power at millikelvin, at 10⁴–10⁶ the count of addressable tones.

## Role in the stack
The base encoding for the silicon and germanium quantum-dot path, the donor path and defect-spin network nodes. It is replaced in some designs by exchange-only encoding — the central fork: microwave hardware for minimum footprint and no leakage, against extra dots for baseband-only control and a leakage channel. It adds nothing to derived clock = max(gate, readout, transport), which on silicon stays readout-dominated at ~1.0×10⁻⁵ s. Verification: the 99.50(6)% is a lower bound and the accompanying ~49 µs Hahn-echo a maximum, both routinely requoted as point estimates [D][2]; the main report's "99.90% donor nuclear CZ" conflicts with the published SQC range [D][4]; and HRL's 2×10⁻⁴ single-qubit error belongs to exchange-only encoding, not this one [D][6].

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Intel | developer | USA | 300 mm EUV single-spin devices | [D][5] |
| Diraq | developer | Australia | Electron spins on 300 mm imec SiMOS | [D][3] |
| QuTech/TU Delft | research | Netherlands | Microwave-free baseband control | [D][2] |
| Silicon Quantum Computing | developer | Australia | Nuclear-spin encoding on donors | [D][4] |
| Quobly | developer | France | Single spins on STMicroelectronics FD-SOI | [C][G:QUOBLY-115M-2026-06] |

**Money.** 2026-06-03 · Quobly · Series A · €115 M · Bpifrance, SEALSQ, STMicroelectronics · €134 M cumulative · closed [C][G:QUOBLY-115M-2026-06]. 2026-06 · SQC · NRFC · A$60 M · Australia's National Reconstruction Fund · closed [G:SQC-NRFC-2026].

**Market & supply chain.** No supplier is specific to this encoding — it is a layout and pulse-sequence choice on shared CMOS lines — and its one distinctive demand, a resonant drive per qubit, is what the control-electronics duopoly sells. Pays into G2, G3 and G6.

**IP & standards.** The 1998 proposal is prior art long out of patent term [D][1]; no dated patent family for single-spin encoding found in a named database as of 4 Sep 2026.

**Roadmaps & track record.** Intel (2026-01-06 · 12 qubits at Argonne, "scale to hundreds of dots" · no successor chip, no dated roadmap) [G:INTEL-2026]. Diraq (2026-08-27 · 150 k physical, 1 k logical by 2029 · its 2026-07-09 release said "thousands by 2029") [R][G:DIRAQ-FUNDING]. Both are orders of magnitude beyond any demonstrated device.

**Strategic reading.** Every spin team can fall back on it, so it differentiates nobody: value accrues to the fab and the control stack. If baseband control matures the microwave vendors lose their strongest claim; if encoded qubits win, area matters less than wafer economics.

*Open niche:* no published protocol separates encoding-specific coherent error from calibration drift across an array, and the field's one quantitative split is self-reported, from a different encoding — an opening for independent characterisation.

## Outlook & open questions
Confirm or demote in 12–24 months: all-pairs fidelities above 12 qubits; baseband control beyond a 2×2 array. Best case 2029: baseband plus 1 K operation removes most microwave I/O at >99.5% two-qubit fidelity. Worst case: the plateau holds. Open: (1) whether hopping-gate control scales past four qubits; (2) whether the calibration-limited diagnosis generalises; (3) which platform shows a below-threshold logical qubit.

## Sources
[1] D. Loss, D. P. DiVincenzo · "Quantum computation with quantum dots" · Physical Review A 57, 120 · 1998-01 · https://journals.aps.org/pra/abstract/10.1103/PhysRevA.57.120 [D]
[2] I. Unseld, B. Undseth, R. Raymenants et al. (QuTech/TU Delft) · "Baseband control of single-electron silicon spin qubits in two dimensions" · Nature Communications · 2025-07-01 · https://www.nature.com/articles/s41467-025-60351-x [D]
[3] Diraq and imec · 300 mm SiMOS two-qubit fidelity and SPAM · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9 [D]
[4] H. Edlbauer, Y. Wang, S. Huq et al. (Silicon Quantum Computing) · 11-qubit donor processor in silicon · Nature 648, 569–575 · 2025-12-17 · https://www.nature.com/articles/s41586-025-09827-w [D]
[5] Intel · 300 mm spin-qubit process statistics, >24,000 devices per wafer · arXiv:2410.16583 · 2024-10 · https://arxiv.org/abs/2410.16583 [D]
[6] HRL Laboratories · 18 exchange-only qubits, mean single-qubit error 2×10⁻⁴ · arXiv:2604.16216 · 2026-07-29 · https://arxiv.org/abs/2604.16216 [D]

## Open verification items
The "99.90% donor nuclear CZ" quoted in the main report is not isolable in the SQC abstract and conflicts with the published range 99.10–99.99%. Intel's "scale to hundreds of dots" statement carries no date or milestone.
