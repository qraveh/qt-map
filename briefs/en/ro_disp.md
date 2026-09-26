---
id: ro_disp
name: Dispersive microwave readout (+TWPA, Purcell)
layer: "6 Readout"
status: demonstrated
since: 2005
one_line: The qubit state is read as a dispersive shift of a coupled resonator, Purcell-filtered on chip and amplified near the quantum limit before the HEMT.
verdict: Falsifiable — assignment fidelity is already 99.94%, so if fleet readout error stays near 1% through 2027 the binding term is measurement-induced leakage and QND violation, not amplifier noise.
updated: 2026-09-03
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
A resonator coupled off-resonantly (coupling g, detuning Δ ≫ g) acquires a state-dependent shift χ ≈ g²/Δ, so a probe tone carries the state in its phase without exchanging quanta with the qubit — non-demolition by construction. Wallraff and colleagues at Yale established it as circuit QED's readout channel [D][457]. Two additions make it usable: an on-chip Purcell filter, which passes the probe while blocking qubit emission into the same line, and a near-quantum-limited parametric amplifier before the HEMT.
Attributes: carrier affinity a = 1.0, fully fabricated. Readout ~10⁻⁶·⁵⁵ s (≈280 ns), non-destructive, mid-circuit capable.

## Physics & limits
Separation needs a fixed number of signal photons at the amplifier input, so readout time falls with probe power and rises with chain noise. A Josephson travelling-wave amplifier giving 12 dB across 4 GHz near the quantum limit [D][458] removes the HEMT's noise penalty, so the amplifier is not the floor. The floor is what hard probing does to the qubit: above a critical photon number the dressed system undergoes measurement-induced transitions out of the computational subspace, and the code inherits leakage — unheralded, sticky, correlated in time, not a Pauli flip. The IQM device shows the split: 99.94% simultaneous assignment fidelity with a 240 ns pulse and shelving into the second excited state, but 99.3% QNDness [D][37]. Assignment error is 6×10⁻⁴; the chance the qubit does not survive as measured is an order of magnitude larger — and that is what syndrome extraction consumes. The Purcell filter's linewidth buys speed but, widened, reopens the emission channel it exists to close. What moves the floor: shelving-free discrimination, on-chip isolation, and encodings that turn a failed measurement into a heralded erasure.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-12 | Willow, 105 q: readout 99.5%, 1.1 µs error-correction cycle | Google | [D][1] |
| 2025-08 | 99.94% simultaneous readout, 240 ns pulse, QNDness 99.3% | IQM | [D][37] |
| 2026-08 | Dual-rail cavity readout: SPAM ≈0.02%, erasure ≈0.5% per gate | Quantum Circuits | [D][79] |
| 2026-07 | Fleet readout error ~1×10⁻² | IBM | [C][32] |

The spread is the story: 6×10⁻⁴ on a characterised pair, 5×10⁻³ over 105 qubits, ~10⁻² across a fleet [D][37][D][1][C][32]; Zuchongzhi 3.0 reads out at 99.13% [D][34]. Readout is the largest single-channel error term at scale, larger than two-qubit gates, and the one whose fleet value has barely moved in two years.

## Manufacturing, materials & supply chain
On chip there is no extra process: resonator and Purcell filter are patterned in the qubit's own lithography, the cost being area and frequency planning: each qubit on a feedline needs a distinct resonator frequency in the amplifier's band. Off chip the chain — isolators, circulators, parametric amplifier, HEMT — is the fridge's bulkiest hardware and where a merchant market has appeared: Silent Waves (Grenoble) sells Argo, Carthago and Zephyr, the last launched 2026-03-13, to Rigetti, Alice & Bob, Qilimanjaro, QphoX and CEA [C][459]; QuantWare sells a Crescendo TWPA [C][460]; QuantumCore is developing one with the Institute for Quantum Computing [P][461]. Export exposure is direct: ECCN 3A901, effective 2024-09-06, covers sub-4.5 K electronics and names parametric amplifiers, so a TWPA is controlled in its own right [G][225].

## Control, readout & I/O burden
Each qubit consumes a resonator, a share of a feedline (eight to ten qubits multiplexed per line), a share of one amplifier's dynamic range, and a digitiser channel with real-time discrimination. The amplifier is the scaling constraint nobody has published a number for: TWPA saturation caps simultaneous tones per device, and each feedline needs its own isolator stack — volume, not silicon. Instrumentation has followed (over 1,000 channels per rack [C][410]), but the budget is set downstream: Google's real-time decoder ran at 63 µs latency for d=5 against a 1.1 µs cycle [D][1], so readout plus decode defines the loop. At 10⁶ the chain must move into the cold, and no cryogenic digitiser has been shown beyond a handful of qubits.

## Role in the stack
It serves every superconducting-family path: transmons, bosonic cat and GKP encodings, dual-rail erasure qubits, and the same chain in annealers. It requires the transmon's dispersive shift and, for bosonic codes, an ancilla mediating the cavity measurement, and provides the mid-circuit non-destructive measurement every error-correction scheme here assumes — no substitute exists inside the family. Its clock contribution is direct: derived clock = sum of the syndrome round: gate layers + transport + readout + reset is 0.65 µs, of which readout is 0.28 µs — the largest term, against ~0.048 µs per gate layer [D][1][D][37] — inside a measured 1.1 µs cycle. No neighbouring empty slot in the technology graph.

## Verification (QCVV)
Three quantities circulate as "readout fidelity" and are not interchangeable: assignment fidelity, QNDness (the qubit is left in the state reported), and SPAM. The 99.94% headline is simultaneous assignment fidelity with shelving; QNDness on the same device is 99.3% [D][37]. IBM's fleet ~10⁻² is undecomposed into amplifier noise, Purcell-limited decay and measurement-induced transitions [C][32]. Value conflict: the graph record quotes 280 ns readout, the preprint a 240 ns pulse, so ~280 ns should be read as the full window. No independent laboratory has replicated the 99.94% result.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IQM | developer | Finland | Readout record: 99.94% with shelving, QNDness 99.3% | [D][37] |
| Google | developer | US | 99.5% readout across 105 qubits in a 1.1 µs cycle | [D][1] |
| IBM | developer | US | Publishes the only at-scale fleet readout error, ~10⁻² | [C][32] |
| Silent Waves | supplier | France | Merchant TWPA maker, three shipping products | [C][459] |
| QuantumCore | supplier | Canada | TWPA development with IQC Waterloo | [P][461] |

**Money.**
- 2026-05-05 · QuantWare · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners · closed [C][462][G:QUANTWARE-SERIESB-2026-05]
- 2026-04-25 · QuantumCore · listing (CSE: QNCR, 2026-04-14) plus NSERC Alliance grant · $10.7 M raised, $1.7 M grant · NSERC/IQC · closed [P][461]
- 2026-01 · D-Wave · M&A (Quantum Circuits) · $550 M · — · announced [C][79]

**Market & supply chain.** The chain, not the chip, is what this node buys: isolators and circulators, HEMTs, the parametric amplifier. The TWPA market is thin — three small merchant suppliers against in-house builds at Google and IBM — so one exit matters more here than anywhere else, and the parts are export-controlled [G][225]. G2 and G3 pay for this node; G7 buys the instrumentation.

**IP & standards.** No TWPA or Purcell-filter patent family with a named assignee and grant year was found; Silent Waves' 2025 Nature Electronics amplifier-isolator is a published design, not a grant [C][459]. No litigation identified, and no standards body defines how readout fidelity is reported — hence three numbers quoted interchangeably.

**Roadmaps & track record.** Silent Waves: three products with named customers (Zephyr promised and launched 2026-03-13) [C][459], the most credible record here. QuantumCore: announced 2026-04-25, too recent to judge [P][461]. No platform vendor publishes a fleet-average readout target as distinct from best-device fidelity — a notable omission when readout is the largest fleet error term.

**Strategic reading.** This is a shared chokepoint: four paths depend on the same amplification and isolation hardware, so concentration risk is systemic in a way qubit-chip choices are not. If fleet readout stays near 10⁻², Λ stalls whatever gates do, since syndrome extraction inherits the measurement error — the case for erasure-style encodings that make a failed measurement heralded. Winners: merchant amplifier suppliers and whichever vendor solves QND rather than assignment. Bargaining power sits with the platform vendors, though export licensing gives regulators a lever.

*Open niche:* The gap is measurement, not hardware: nobody publishes a fleet QNDness, and the ~10⁻² fleet error is never decomposed into amplifier noise, Purcell-limited decay and measurement-induced leakage. A vendor-neutral protocol reporting all three across a whole chip is a low-capital QCVV service that also characterises amplifier chains for suppliers who publish no acceptance data.

## Outlook & open questions
Confirm or demote within 12–24 months: does any vendor publish a fleet-average QNDness; does fleet readout error fall below 5×10⁻³. Best case by 2029: shelving-free discrimination and on-chip isolation take fleet readout error toward 10⁻³ without slowing the cycle. Worst case: measurement-induced leakage holds QNDness near 99.3% whatever the amplifier does, and readout stays the term that caps Λ. Open questions: how the fleet 1% decomposes; how many tones one TWPA carries before compression.

## Sources
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[32] IBM, “IBM Quantum Computing — Hardware and roadmap.” [Online]. Available: https://www.ibm.com/quantum/hardware [C]
[34] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[37] F. Marxer *et al.*, “Above 99.9% Fidelity Single-Qubit Gates, Two-Qubit Gates, and Readout in a Single Superconducting Quantum Device,” *PRX Quantum*, vol. 7, Art. no. 020333, 2026, doi: [10.1103/n86s-2b88](https://doi.org/10.1103/n86s-2b88). [arXiv:2508.16437](https://arxiv.org/abs/2508.16437). [D]
[79] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [D]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[410] Zurich Instruments, “Zurich Instruments Launches the ZQCS Quantum Control System to Master the Long-Lived Logical Qubit Challenge,” Mar. 9, 2026. [Online]. Available: https://www.zhinst.com/americas/en/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/ [C]
[457] A. Wallraff *et al.*, “Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics,” *Nature*, vol. 431, no. 7005, pp. 162–167, Sep. 2004, doi: [10.1038/nature02851](https://doi.org/10.1038/nature02851). [arXiv:cond-mat/0407325](https://arxiv.org/abs/cond-mat/0407325). [D]
[458] T. C. White *et al.*, “Traveling wave parametric amplifier with Josephson junctions using minimal resonator phase matching,” [arXiv:1503.04364](https://arxiv.org/abs/1503.04364), Mar. 2015. [D]
[459] Silent Waves, “Silent Waves - Traveling-Wave Parametric Amplifiers (TWPAs),” Mar. 13, 2026. [Online]. Available: https://www.silent-waves.com/ [C]
[460] QuantWare, “Peripherals — Crescendo TWPA,” 2026. [Online]. Available: https://quantware.com/product/peripherals [C]
[461] D. Finke, “QuantumCore Secures $1.7M NSERC Grant to Advance Superconducting Amplifiers,” Quantum Computing Report, Apr. 25, 2026. [Online]. Available: https://quantumcomputingreport.com/quantumcore-partners-with-iqc-and-nserc-in-1-7m-traveling-wave-parametric-amplifier-twpa-development-initiative/ [P]
[462] QuantWare, “QuantWare Raises $178 Million to Build World’s Most Powerful Quantum Processors at an Industrial Scale,” May 5, 2026. [Online]. Available: https://quantware.com/news/quantware-raises-178-million [C]
General facts cited above: [G:QUANTWARE-SERIESB-2026-05], [G:IBM-10B-2026-06].

## Open verification items
- The graph record's 280 ns readout time versus the preprint's 240 ns readout pulse: the difference is unexplained in the source and may be a full-window versus pulse-length definition.
- Authors, institution and journal for the 2015 Josephson TWPA reference could not be established here; only the 12 dB gain over a 4 GHz span and near-quantum-limited noise are confirmed.
- No named TWPA or Purcell-filter patent family with assignee and grant year was found.
- No supplier publishes TWPA yield, unit cost, or the number of multiplexed tones one amplifier sustains before compression.
- No vendor publishes a fleet-average QNDness or a decomposition of the ~10⁻² fleet readout error.
