---
id: enc_eo
name: Exchange-only / singlet-triplet spin encoding
layer: "2 Encoding"
status: demonstrated
since: 2013
one_line: One logical qubit in the total-spin subspace of two or three exchange-coupled dots, driven entirely by baseband voltage pulses, with leakage as the price of removing microwave control.
verdict: The only spin encoding that has run error correction with no room-temperature real-time electronics; it costs three dots per qubit and a leakage channel, and its headline code result is bit-flip only.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two or three spins in adjacent dots encode one qubit in a subspace of fixed total spin, every gate a pulse of Heisenberg exchange — baseband voltage, never a microwave tone. The basis is DiVincenzo, Bacon, Kempe, Burkard and Whaley, Nature 408, 339 (2000): exchange alone implements any circuit, so local single-qubit drive disappears [S][1]. Scaled three-dot demonstrations date from about 2013. Attributes: affinity — fully composite, the opposite pole from the bare spin; error — leakage plus coherent exchange error, no control modality or fabrication of its own.

## Physics & limits
Three spins span eight states and the qubit uses two, so population leaks into the spin-3/2 manifold, invisible to a Pauli-frame decoder unless converted into detectable error. That is the encoding-specific floor: 0.015% per Clifford for always-on two-exchange operation against a 0.029% single-exchange average [D][2]. In return it is a decoherence-free subspace against uniform field noise, but exchange depends exponentially on barrier voltage, so charge noise enters the gate. Neither term dominates: HRL attributes roughly 80% of its CNOT error to extrinsic control and calibration [D][3]. Sweet-spot operation, always-on pulsing (1.9 versus 2.7 pulses per Clifford [D][2]) and cold calibration move it.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2026-04-03 | 99.86% Clifford (blind randomised benchmarking), leakage 0.015%/Clifford, always-on | UCLA | [D][2] |
| 2026-07-29 | 18 qubits from 54 dots; 1Q 2×10⁻⁴, CNOT 3×10⁻³; distance-5 repetition code, Λ₅/₃ = 4.7 over 200 rounds | HRL | [D][3] |

Dominant term: extrinsic control and calibration, then leakage; best reproducible CNOT 9×10⁻⁴ [D][3].

## Manufacturing, materials & supply chain
Three dots per qubit — two for singlet–triplet — triples gate-stack density per logical unit on the hosting 300 mm process, with no encoding-specific step.  The win is control: purely baseband, no microwave lines or micromagnets, the sequencer inside a 4 K controller in commercial 130 nm RF CMOS — 366 DACs, 296 lines, ≤3.5 W, no room-temperature real-time electronics [D][3] — the first sign a control rack can become a cold ASIC. That sets the wall: ≤3.5 W for 18 qubits is ≈0.2 W per qubit, so 10³ qubits need hundreds of watts at 4 K, one to two orders beyond a standard pulse-tube stage [S][3]. Power per qubit, not line count, is the scaling problem.

## Role in the stack
Requires a gate-defined quantum-dot carrier at three dots per qubit, in the silicon and germanium quantum-dot spin path; replaces single-spin encoding, the central fork. Exchange pulses are nanoseconds, but a Clifford costs about two, so the encoding multiplies gate count, not gate time; readout still sets derived clock = sum of the syndrome round: gate layers + transport + readout + reset at 8.5×10⁻⁶ s, 6.3 µs of it readout. Verification: Λ₅/₃ = 4.7 and the 5.0×10⁻³ logical error come from a distance-5 repetition code, bit-flip only, not below-threshold operation of a full code; the [[4,2,2]] fidelity of 0.95 is post-selected [D][3]. The UCLA 99.86% is single-qubit blind benchmarking, not device-wide [D][2]; neither result is replicated.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| HRL Laboratories | developer | USA | 18 exchange-only qubits, 4 K controller | [D][3] |
| IBM | developer | USA | Acquired HRL; no spin milestone on its roadmap | [C][G:IBM-HRL-CLOSED-2026-08] |
| UCLA | research | USA | Always-on two-exchange qubit | [D][2] |
| Quantum Machines | supplier | Israel | Named control-stack supplier to HRL | [C][G:QM-SPINCONTROL-2026] |


**Money.** 2026-06-02 · IBM · quantum programme commitment · >$10 B over five years · announced [C][G:IBM-10B-2026-06]. 2026-08-26 · IBM · HRL acquisition completed · undisclosed · closed [C][G:IBM-HRL-CLOSED-2026-08].

**Market & supply chain.** No encoding-specific supply chain exists; the distinctive asset is HRL's cryogenic controller, now IBM property. Removing microwave generation shrinks the rack vendors' share of the bill — the only spin encoding threatening the control duopoly. Pays into G3.

**IP & standards.** The 2000 exchange-universality result is prior art out of patent term [S][1]; IBM's HRL purchase is the clearest IP consolidation, terms undisclosed [C][G:IBM-HRL-CLOSED-2026-08]. No dated patent family for the encoding is in a named database as of 4 Sep 2026.

**Roadmaps & track record.** IBM and HRL (2026-08-26 · acquisition completed · no dated qubit-count milestone, no spin entry on Starling 2029 or Blue Jay) [C][G:IBM-HRL-CLOSED-2026-08]. The July 2026 paper is a physics demonstration, not a scaling promise.

**Strategic reading.** If leakage holds near 10⁻⁴ per Clifford at scale, three dots per qubit buys away the microwave subsystem and the rack — a system win for IBM and any fab printing dense arrays. If single-spin encoding closes the calibration gap, the overhead is pure area cost and the rack vendors keep their position.

*Open niche:* the claim that ~80% of CNOT error is extrinsic is self-reported by the group that set the record; leakage benchmarking, leakage-reduction verification and honest repetition-versus-full-code accounting are what an independent group supplies.

## Outlook & open questions
Confirm or demote in 12–24 months: a second laboratory reproducing the 18-qubit result; a full code below threshold; a dated IBM milestone. Best case 2029: IBM folds the cold sequencer into a foundry-scale device with unconditional performance. Worst case: a single-laboratory result. Open: (1) whether controller power per qubit falls two orders; (2) whether leakage stays flat as arrays grow; (3) whether always-on pulsing becomes the standard.

## Sources
[1] D. P. DiVincenzo, D. Bacon, J. Kempe, G. Burkard, and K. B. Whaley, “Universal quantum computation with the exchange interaction,” *Nature*, vol. 408, no. 6810, pp. 339–342, 2000, doi: [10.1038/35042541](https://doi.org/10.1038/35042541). [arXiv:quant-ph/0005116](https://arxiv.org/abs/quant-ph/0005116). [S]
[2] J. D. Broz, J. C. Hoke, E. Acuna, and J. R. Petta, “Demonstration of an always-on exchange-only spin qubit,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 4794, Apr. 2026, doi: [10.1038/s41467-026-70943-w](https://doi.org/10.1038/s41467-026-70943-w). [D]
[3] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]

## Open verification items
The 0.2 W per qubit figure is arithmetic on HRL's published controller power and qubit count, not a scaling number the paper states. HRL's ~80% extrinsic-error attribution is self-reported and unreplicated. Neither the UCLA nor the HRL result has an independent replication, and no exchange-only device has published all-pairs two-qubit fidelities.
