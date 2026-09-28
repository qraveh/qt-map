---
id: ro_reset
name: Fast unconditional / dissipative qubit reset
layer: "6 Readout"
status: demonstrated
since: 2018
one_line: "Returning a superconducting qubit to |0⟩ in ~100–500 ns by handing its excitation to a lossy mode, usually the readout resonator, instead of waiting for T1 or measuring and flipping."
verdict: "Demonstrated since 2018 and inside production error-correction rounds (Google's 160 ns step in a 921 ns round; USTC's all-microwave ancilla reset). IBM's dissipative gadget on Nighthawk r2 is company-reported only: no reset duration or absolute residual population published as of 2026-09-26."
updated: 2026-09-26
---

T1 = energy-relaxation time; κ = energy-decay rate of the lossy mode; LRU = leakage-reduction unit; DQLR = data-qubit leakage removal; MLR = multi-level reset; Λ = error-suppression factor per code-distance step; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Reset returns a qubit to |0⟩ before a shot and, in error correction, every measure qubit once per syndrome round. Unconditional reset — this technology — hands the excitation to a lossy mode with no classical decision, unlike waiting for T1 or measuring and flipping. It began with the all-microwave "f0g1" scheme: a drive couples |f,0⟩ to |g,1⟩ of the transmon–resonator pair (g, f = ground and second excited states; 0, 1 = resonator photons) and the photon leaks out, leaving 0.2% residual excitation in under 500 ns without feedback [D][596]. It sits in the readout layer because the lossy mode is usually the readout resonator and feedline [D][597][D][598]. Attributes: on-chip, superconducting lithography, driven from room temperature, no transport; error class leakage.

## Physics & limits
Passive relaxation is too slow: even with no thermal floor, 10⁻³ at T1 = 200 µs takes ln(10³)·T1 ≈ 1.4 ms [S]. The floor matters too: a 5 GHz transmon at 50 mK effective temperature holds ~0.8% excitation [S], so reset must cool — with engineered rate Γ_r ≫ Γ_q the residual tends to (Γ_q·n_q + Γ_r·n_r)/(Γ_q + Γ_r), the colder bath's occupation [S]. Speed is set by the lossy mode: an excitation swapped into a mode of decay rate κ leaves no faster than the critically damped κ/2, so 10⁻³ takes ≈ 21/κ, 170–340 ns for κ/2π = 20–10 MHz [S] — the 100–500 ns band. A 34 ns flux swap thus becomes 284 ns once the resonator must be emptied [D][599]; a broadband metamaterial bath escapes the single-mode bound [D][600]. A switchable dissipator decouples reset rate from idle T1: IBM's moves effective T1 from ~200 µs to ~25 ns [C][601], an on/off ratio of ~8×10³ [S]. Leakage is the companion problem: a conditional X acts only on |0⟩↔|1⟩, so |2⟩ stays leaked [S]; MLR empties |1⟩–|3⟩ at one setting [D][597].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018-08-07 | f0g1: 0.2% residual in <500 ns | Magnard et al. | [D][596] |
| 2021-03-19 | MLR of \|1⟩–\|3⟩ in ~250 ns, >99% (readout-limited) | Google | [D][597] |
| 2021-10-11 | Flux swap: 0.08% ± 0.08% in 34 ns; 284 ns with depletion | Zhou et al. | [D][599] |
| 2023-02-22 | 160 ns reset + 500 ns measurement in a 921 ns round | Google, Sycamore | [D][602] |
| 2024-09-25 | Reset + leakage reduction in 83 ns, fixed-frequency, >99% | Chen et al. | [D][598] |
| 2024-11-05 | Reset error <0.13% (\|1⟩), 0.16% (\|2⟩) in 88 ns; \|2⟩-only LRU 44 ns | Kim et al. | [D][600] |
| 2025-12-22 | Microwave LRUs + ancilla reset: leakage ÷72 to 6.4×10⁻⁴; d = 7, Λ = 1.40 ± 0.06 | USTC, Zuchongzhi 3.2 | [P][603] |
| 2026-08-31 | 120 reset elements; initialization error ÷25 | IBM, Nighthawk r2 | [C][601] |

Sycamore spent 660 of 921 ns (72%) measuring and resetting, and its authors name data-qubit idling during them a dominant error [D][602]. Willow runs MLR on measure qubits and DQLR on data qubits every 1.1 µs cycle [D][1], after DQLR cut data-qubit leakage tenfold, below 10⁻³ device-wide [D][604]. USTC's row is the press reading of its PRL [D][3]. IBM's gain is shot rate: 100,000 circuits per second, 25× Heron [C][601]. Dominant term: residual population, which production vendors do not publish.

## Manufacturing, materials & supply chain
Resonator-based reset adds no fabrication step [D][596]. The cost follows qubit type: flux-tunable transmons reuse their flux lines [D][597]; fixed-frequency ones use the microwave route, a tunable coupler [D][598] or a dedicated element per qubit [C][601]. A tunable element is in general one more control signal per qubit [S]; press coverage credits USTC's microwave-only route with avoiding Google's DC-pulse wiring [P][605].

## Control, readout & I/O burden
Unconditional reset is an open-loop pulse: no discrimination, decision or feed-forward. Conditional reset stacks readout, ring-down, a decision and a π pulse, floored by assignment error; IBM's earlier scheme flipped on |1⟩, then idled hundreds of microseconds between executions [C][601], an idle exposed as `rep_delay` that trades execution time against state-preparation error [C][606]. In a surface code the measurement happens anyway; what follows is a 160 ns step [D][602] or a feed-forward loop paid every round [S].

## Role in the stack
Slot 6 of the Transmon lattice with tunable couplers architecture, beside dispersive readout. It **requires** the transmon (the qubit to be reset) and ro_disp (the readout resonator as loss channel); no **provides**, **replaces** or conflicts edge exists as of 2026-09-26. The ro_disp edge is the common case, not a necessity: Nighthawk r2 couples each qubit to a cold environment through its own tunable coupler [C][601]. It answers gap G-reset with reset time and residual population as attributes; the Atlas's derived clock counts readout + reset as ≈ two-thirds of the superconducting round. The ledger's cat and dual-rail placements were not taken; atom re-initialisation or reloading has no lossy-mode step and is not this technology [G]. The sibling gap G-lru, data-qubit leakage removal, stays open. Register machines: google-sycamore-72, ibm-loon, ibm-nighthawk-r2 (primary), ustc-zuchongzhi-3.2 (alternate).

## Evidence — how the numbers were measured
Reset is checked by reading the qubit afterwards, so readout error bounds it: McEwen et al.'s ~10⁻³ was readout-limited [D][597]. Reported quantities do not compare — residual excitation, reset error, effective T1, an error ratio. All four register cells are verified ✅, but only Sycamore's has a figure locator (Fig. 1b); IBM's rest on blogs, Loon's naming "reset gadgets" without figures [C][486]; Zuchongzhi 3.2's has neither locator nor reset figure.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | 160 ns reset in Sycamore's round; MLR + DQLR every Willow cycle | [D][602][D][1] |
| IBM | developer | US | Conditional reset on Heron; 120 dissipative elements on Nighthawk r2; gadgets on Loon | [C][601][C][486] |
| USTC / Hefei National Laboratory | developer | CN | Microwave LRUs and in-cycle ancilla reset, Zuchongzhi 3.2 | [P][603] |

**Money.** No dated financial item is specific to qubit reset as of 2026-09-26.

**Market & supply chain.** No separate market: reset is bought as chip design and calibration and pays out as round time and shot rate, into G2–G4.

**IP & standards.** No standard defines a reset figure of merit; no dated patent count from a named database as of 2026-09-26.

**Roadmaps & track record.** IBM named reset gadgets on 2025-11-12 [C][486] and shipped them on Nighthawk r2 on 2026-08-31 [C][601]: delivered, with ratios rather than absolute figures.

**Strategic reading.** Reset is where fixed-frequency and tunable architectures part. If switchable dissipators keep their off-state T1 at scale, readout resonators can be optimised for readout alone.

## Outlook & open questions
Confirm if IBM or an independent group publishes Nighthawk r2's reset duration, absolute residual and mid-circuit use by 2027-06-30, and if a d ≥ 9 surface code brings readout + reset below half its round by 2027-12-31; demote the gadget to a throughput feature if figures cover only between-shot initialization.
Open questions. (1) What absolute residual does Nighthawk r2 reach? (2) What does a dissipator's off-state cost in T1 across 10³ qubits? (3) Can reset overlap ring-down to shrink the 660 ns term? (4) Do microwave-only resets match flux-based speed without crosstalk? (5) Which data-qubit leakage scheme closes G-lru without adding a round step?

## Sources

[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[486] R. Mandelbaum, “Scaling for quantum advantage and beyond,” IBM Quantum Computing Blog, Nov. 12, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/qdc-2025 [C]
[596] P. Magnard *et al.*, “Fast and Unconditional All-Microwave Reset of a Superconducting Qubit,” *Phys. Rev. Lett.*, vol. 121, no. 6, Art. no. 060502, Aug. 2018, doi: [10.1103/physrevlett.121.060502](https://doi.org/10.1103/physrevlett.121.060502). [arXiv:1801.07689](https://arxiv.org/abs/1801.07689). [D]
[597] M. McEwen *et al.*, “Removing leakage-induced correlated errors in superconducting quantum error correction,” *Nat. Commun.*, vol. 12, Art. no. 1761, Mar. 2021, doi: [10.1038/s41467-021-21982-y](https://doi.org/10.1038/s41467-021-21982-y). [arXiv:2102.06131](https://arxiv.org/abs/2102.06131). [D]
[598] L. Chen *et al.*, “Fast unconditional reset and leakage reduction in fixed-frequency transmon qubits,” [arXiv:2409.16748](https://arxiv.org/abs/2409.16748), Sep. 2024. [D]
[599] Y. Zhou *et al.*, “Rapid and unconditional parametric reset protocol for tunable superconducting qubits,” *Nat. Commun.*, vol. 12, Art. no. 5924, Oct. 2021, doi: [10.1038/s41467-021-26205-y](https://doi.org/10.1038/s41467-021-26205-y). [D]
[600] G. Kim *et al.*, “Fast Unconditional Reset and Leakage Reduction of a Tunable Superconducting Qubit via an Engineered Dissipative Bath,” [arXiv:2411.02950](https://arxiv.org/abs/2411.02950), Nov. 2024. [D]
[601] H. Haas, D. McKay, and R. Davis, “IBM Quantum Nighthawk r2—more circuits, faster,” IBM Quantum Computing Blog, Aug. 31, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/nighthawk-r2 [C]
[602] R. Acharya *et al.*, “Suppressing quantum errors by scaling a surface code logical qubit,” *Nature*, vol. 614, pp. 676–681, Feb. 2023, doi: [10.1038/s41586-022-05434-1](https://doi.org/10.1038/s41586-022-05434-1). [D]
[603] M. Ivezic, “China's Zuchongzhi 3.2 Crosses the Error Correction Threshold - and Takes a Different Path Than Google to Get There,” PostQuantum.com, Dec. 30, 2025. [Online]. Available: https://postquantum.com/quantum-research/zuchongzhi-3-2-belowthreshold/ [P]
[604] K. C. Miao *et al.*, “Overcoming leakage in quantum error correction,” *Nat. Phys.*, vol. 19, pp. 1780–1786, Oct. 2023, doi: [10.1038/s41567-023-02226-w](https://doi.org/10.1038/s41567-023-02226-w). [D]
[605] M. Swayne, “China Demonstrates Quantum Error Correction Using Microwaves, Narrowing Gap With Google,” The Quantum Insider, Dec. 26, 2025. [Online]. Available: https://thequantuminsider.com/2025/12/26/china-demonstrates-quantum-error-correction-using-microwaves-narrowing-gap-with-google/ [P]
[606] IBM, “Qubit initialization.” [Online]. Available: https://quantum.cloud.ibm.com/docs/en/guides/repetition-rate-execution [C]

## Open verification items
- Zuchongzhi 3.2 PRL (journals.aps.org) returned 403 on 2026-09-26; Europe PMC and phys.org were rate-limited (429). The 72×, 6.4×10⁻⁴, d = 7 and Λ figures come from press analysis; USTC's reset duration and residual were not found.
- Nighthawk r2 blog (opened 2026-09-26): effective T1, a 25× ratio, ~1 µs idle; no reset duration, absolute residual or paper. Loon's gadget figures unpublished as of 2026-09-26.
- Heron's conditional-reset duration and feed-forward latency: not in IBM's initialization guide, opened 2026-09-26.
- Willow's measurement and reset durations, and Miao et al.'s DQLR duration and arXiv id, not found in pages opened 2026-09-26 (Miao cited by DOI).
- Journal versions of arXiv:2409.16748 and arXiv:2411.02950 not opened; the 1.4 ms, 0.8%, ≈21/κ and 8×10³ figures are derived here.
