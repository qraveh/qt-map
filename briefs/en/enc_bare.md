---
id: enc_bare
name: Bare two-level subspace
layer: 2 Encoding
status: demonstrated
since: 2007
one_line: The {|0⟩,|1⟩} subspace of a weakly anharmonic Josephson oscillator used directly as the qubit, with no bosonic, erasure or bias structure on top.
verdict: The default of every mainstream superconducting vendor as of 2026-09-04; its structural cost is leakage plus an unbiased error model, which caps measured Λ at 1.4–2.1 where erasure encodings simulate an order of magnitude higher.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Using the lowest two levels of a Josephson circuit directly as a qubit is as old as the Cooper-pair box (Nakamura, 1999); the transmon (Koch et al., 2007) made it the default by buying charge insensitivity with lower anharmonicity — which is what creates the leakage problem.
Attributes: it adds no characteristic time, readout, mobility, control or fabrication of its own — each is the carrier's.
Error structure as the code sees it: unbiased Pauli plus leakage out of the subspace.

## Physics & limits
The scale that matters is α ≈ −E_C ≈ 2π × 200–300 MHz: it sets the minimum gate time and the leakage per gate, which DRAG suppresses but cannot remove. Raising α costs charge dispersion, which grows as exp(−√(8E_J/E_C)); that trade is the floor here. Leakage persists where a Pauli fault does not: the second excited state survives tens of QEC cycles at Willow's 1.1 µs [D][1], feeding the decoder correlated wrong syndromes. Hence dedicated removal: USTC's all-microwave scheme suppresses leakage 72×, to a residual 6.4(5)×10⁻⁴ after 40 cycles [D][3]. What moves the floor is leakage-aware decoding and faster multi-level reset.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2024-12-09 | d=7 surface code, Λ = 2.14 ± 0.02 | Google (Willow) | [D][1] |
| 2025-12-22 | Leakage suppressed 72×, Λ = 1.40(6) at d=7 | USTC | [D][3] |
| 2026-07-08 | d=7 logical error 7.72×10⁻⁴ per cycle | Google | [D][2] |

Best in class is one characterised IQM pair, CZ 99.93% over 40 h [D][37]; typical at scale is IBM's fleet EPLG 3.7×10⁻³, best 1.9×10⁻³ [D][33], and Rigetti's 108-qubit median 99.1% [C][35].

## Manufacturing, materials & supply chain
Nothing of its own: it inherits the carrier's 300 mm Nb/Al lithography, yield spread and one drive plus one readout line per qubit. That is the whole commercial argument — dual-rail erasure adds a rail and a check per qubit (384 ns, 2.54×10⁻² erasure [D][80]), cat codes a pump and buffer mode. The I/O wall is the carrier's: coax per qubit, ~10³ qubits per fridge. What this encoding adds at 10⁴–10⁶ is leakage removal inside every 1.1 µs cycle and the decoder bandwidth to use it. Export exposure is the carrier's (US EAR ECCN 3A901).

## Role in the stack
The default Layer-2 encoding on every mainstream transmon path (IBM, Google, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu). Dual-rail erasure or cat encoding replaces it when a vendor trades control complexity for a friendlier error structure: Alice & Bob, AWS and D-Wave/Quantum Circuits have, IBM and Google have not. The price is quantifiable: measured dual-rail gate errors simulate to Λ ≈ 27 against 14 for 0.1% depolarising noise [S][79], where this encoding measures 2.14 and 1.40(6) [D][1], [3]. It adds nothing to the derived clock, which stays the carrier's 0.65 µs round inside its measured 1.1 µs cycle. Verification: the 72× is one unreplicated USTC device, and leakage is self-reported with no cross-vendor protocol.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| IBM | developer | US | Whole fleet and the Starling roadmap on bare transmons | [D][33] |
| Google | developer | US | Willow QEC and the d=7 logical-error record | [D][1] |
| USTC | research | CN | Below-threshold d=7 via leakage suppression | [D][3] |

**Money.**
2026-06-02 · IBM · investment commitment · > $10 B over five years · announced [G][55][G:IBM-10B-2026-06]
2026-07-02 · IQM · Nasdaq and Helsinki listing · pro-forma cash €337 M · closed [C][56][G:IQM-LISTING-2026-07]

**Market & supply chain.** No supply chain of its own; concentration sits one layer down, in Nb/Al lithography and dilution refrigerators. Being free, it is what every G1–G4 budget on this path buys.

**IP & standards.** No dated patent family found for bare-subspace leakage mitigation as of 2026-09-04; PatSnap's 2026-06-30 counts are not encoding-specific [P][G:PATSNAP-2026-06].

**Roadmaps & track record.** IBM (2025-06-10 · Starling, 200 logical / 10⁸ gates in 2029 · Nighthawk on plan, Kookaburra slipped a year [G:IBM-ROADMAP]). Google (2025 · long-lived logical qubit at 10⁻⁶ · no successor to Willow). Neither publishes a leakage target.

**Strategic reading.** Its edge is that it is free, so the fork is capital allocation: money spent switching to erasure is not spent scaling the bare fleet. If Λ stays near 2, erasure encodings win on physical qubits per logical; otherwise incumbents keep the field.

*Open niche:* vendors quote per-gate leakage, per-cycle residual population, or nothing. A vendor-neutral benchmark — population versus QEC round with removal running — would be comparable across IBM, Google, IQM and USTC hardware.

## Outlook & open questions
Confirm by end-2027: ≥ 50× leakage suppression in a below-threshold code outside USTC, or leakage published as a line item in a vendor's logical error budget; otherwise demote it to a single-device claim. Best case 2029: leakage falls under the correlated-event floor (≈10⁻¹⁰, hourly bursts on Willow [D][1]); worst case, Λ stays near 2 and physical-per-logical above 10³. Does leakage or 2Q error dominate at 10⁴ qubits? Can removal keep up at 10⁶? Does erasure conversion ever cross over commercially?

## Sources
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[33] IBM Quantum, “What's new at IBM Quantum - Q2 2026.” [Online]. Available: https://www.ibm.com/quantum/blog/whats-new-q2-2026 [D]
[35] Rigetti Computing, Inc., “Rigetti Announces General Availability of 108-Qubit System,” Apr. 7, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system [C]
[37] F. Marxer *et al.*, “Above 99.9% Fidelity Single-Qubit Gates, Two-Qubit Gates, and Readout in a Single Superconducting Quantum Device,” *PRX Quantum*, vol. 7, Art. no. 020333, 2026, doi: [10.1103/n86s-2b88](https://doi.org/10.1103/n86s-2b88). [arXiv:2508.16437](https://arxiv.org/abs/2508.16437). [D]
[55] IBM Quantum, “Why IBM is investing $10 billion into quantum computing,” Jun. 2, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/10-billion-investment-faq [G]
[56] IQM Quantum Computers, “IQM Quantum Computers Becomes First European Quantum Computing Company Listed on a Major U.S. Exchange,” Jul. 2, 2026. [Online]. Available: https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ [C]
[79] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [S]
[80] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026. [D]

## Open verification items
The 72× leakage suppression and 6.4(5)×10⁻⁴ residual come from one USTC device; no independent replication was found as of 2026-09-04.
The PRL does not name the processor; the report's "Zuchongzhi 3.2" label is external to the paper.
No leakage figure is published for IBM's fleet; EPLG aggregates all error mechanisms.
