---
id: ct_fdm
name: Frequency-division-multiplexed gate drive (several qubits per line)
layer: "5 Control"
status: emerging
since: 2026
one_line: Polychromatic microwave pulses on one coaxial line, split by frequency at room-temperature band-pass filters, drive several qubits or couplers at once; a 1:4 ratio shown with no measurable fidelity penalty, one group.
verdict: The I/O wall's first measured answer at the gate level, but a 1:4 ratio on an unnamed device with room-temperature filters is a method, not a wiring plan; it holds its slot only if a 1:12 or better ratio appears on a processor of a hundred qubits or more, or a vendor adopts it.
updated: 2026-11-07
---

FDM = frequency-division multiplexing; AWG = arbitrary waveform generator; MXC = the mixing chamber, the coldest stage of a dilution refrigerator; FIR = finite impulse response (a digital filter).

## Identity & lineage

Every superconducting processor today runs one or more lines from room temperature to each qubit — a microwave drive, a flux line, often both — and the count of coaxial cables, their heat load and the connectors at each stage are the wall the room-temperature route (`ct_rt`) runs into somewhere between 10³ and 10⁴ qubits. Frequency-division multiplexing is the telecommunications answer: tones at different frequencies share one cable and are separated at the end by filters. Readout has done this for years — several resonators on one feedline, separated in frequency — but gate drive has not, because flux pulses are unipolar and broadband and because two-qubit gates were mostly driven by them. A proposal of December 2023 set out a scheme in which shared lines serve several qubits and couplers, with frequency multiplexing combined with individual tuning, and estimated a line-count reduction of one to two orders of magnitude [S][911]. In October 2026 the Hefei group of USTC and QuantumCTek demonstrated it: a "periodically extensible hybrid multiplexing framework" in which all gate operations are frequency-division multiplexed with polychromatic microwave pulses and band-pass filters, in a 1:4 ratio, with average errors of (6.4 ± 0.2)×10⁻³ for parallel FDM CZ gates and (10.6 ± 0.2)×10⁻⁴ for parallel FDM XY(π/2) gates and "no statistically significant multiplexing-induced degradation" [P][912].

Attributes (technology graph): carrier affinity 1.0 — fabricated. Characteristic time: none of its own. Readout: none. Mobility: none. Control modality: microwave, placed at room temperature — the filters sit outside the cryostat. Error structure: coherent (adjacent-tone crosstalk through finite filter isolation). Manufacturing: the chip's own superconducting lithography; nothing on it changes.

## Physics & limits

A coaxial line carries several gigahertz of bandwidth and a qubit drive occupies tens of megahertz, so in principle dozens of tones fit on one cable; the practice is bounded by four things. First, the output bandwidth of the electronics: the demonstration combined tones from a 2 GSa/s AWG with a 5.1 GHz source for the XY sidebands and was, by the authors' account, constrained by the processor's size and the electronics' bandwidth [P][912]. Second, filter isolation: adjacent tones leak through the skirts of each band-pass filter, and the paper puts the requirement at 50 dB or more at ±100 MHz for a tone spacing of 100 MHz to keep the crosstalk-induced infidelity near 10⁻⁴ [P][912]. Third, frequency allocation: every qubit and coupler on a shared line needs its own band, which is the frequency-crowding problem of fixed-frequency lattices in a new place. Fourth, gate physics: a microwave-driven two-qubit gate is longer than a flux-pulsed one and so more exposed to decoherence — the demonstration's CZ error of 6.4×10⁻³ is an order above the best flux-pulsed CZ of the lattice (`g_tc`) [P][912]. The filters' insertion loss and the filter-induced pulse distortion are corrected by a FIR pre-distortion kernel built from the measured response. The thermal argument is the point of the exercise: the passive conductive load on the mixing chamber falls from about 400 µW with dedicated lines to about 8.33 µW at a 1:48 ratio, by a manufacturer's reference value that excludes filters, switches and other parasitic loads [P][912].

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: a 1:4 ratio on four qubits and four couplers of an unnamed tunable-coupler transmon processor — parallel CZ error (6.4 ± 0.2)×10⁻³ against (6.53 ± 0.24)×10⁻³ with dedicated lines, parallel XY(π/2) error (10.6 ± 0.2)×10⁻⁴ against (10.38 ± 0.35)×10⁻⁴ without filters [P][912]. Typical at scale: none — no processor of more than a handful of qubits has been wired this way.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-12 | Proposal: shared lines for several qubits and couplers, line count down by one to two orders of magnitude | Beijing Academy of Quantum Information Sciences | [S][911] |
| 2026-10 | 1:4 FDM on transmons: CZ (6.4 ± 0.2)×10⁻³ vs (6.53 ± 0.24)×10⁻³ dedicated; XY(π/2) (10.6 ± 0.2)×10⁻⁴ vs (10.38 ± 0.35)×10⁻⁴ | USTC / QuantumCTek | [P][912] |
| 2026-10 | Projection: 381,000 physical qubits on 23,814 lines (1:48) against 1,143,000 dedicated; 1:12 at the measured parameters | USTC / QuantumCTek | [P][912] |

Dominant error term: at 1:4, none attributable to multiplexing within the error bars; at higher ratios, adjacent-tone crosstalk through finite filter isolation and spectral overlap [P][912].

## Manufacturing, materials & supply chain

Nothing on the chip changes and nothing in the cryostat changes: the filters, splitters and sources are room-temperature microwave components, and the multiplexed line enters the fridge as a coaxial cable like any other [P][912]. That is the method's industrial virtue — it is a change in the control rack, bought from the microwave-component market — and its ceiling: the idealised 1:48 ratio assumes integrated filters and bias sources, at which point the technology becomes a cryogenic component question of the kind cryo-CMOS (`ct_cryocmos`) and on-chip flux DACs (`ct_fluxdac`) already pose. The paper's own closing sentence makes the dependence explicit: together with on-chip DC sources, the scheme completes "the last missing module of a scalable multiplexed-control architecture" [P][912]. Concentration risk is low on parts and high on know-how: one group holds the calibration and allocation method. Export-control exposure: the processor's and the cryogenic electronics' [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

This technology is the I/O burden's answer, so the burden is the figure of merit. With dedicated lines a tunable-coupler lattice needs about three lines per qubit (XY drive, qubit flux, coupler flux); at the measured gate parameters the paper's framework cuts the total to about one twelfth, at idealised parameters to one forty-eighth [P][912]. At 10³ qubits the saving is a rack and a cable tray; at 10⁴ it is the difference between one dilution refrigerator and several; at the paper's 381,000 qubits it is 23,814 lines against 1.1 million, a count no fridge wires. What it does not remove: the static DC flux bias per tunable element, unless on-chip DACs supply it; the readout feedlines, already multiplexed; and the control electronics' channel count, which falls only if one channel synthesises the polychromatic pulse — the 2 GSa/s AWG of the demonstration did. Readout is untouched.

## Role in the stack

Architectures: an alternate control technology on the transmon lattice with tunable couplers (`sc`). It requires the room-temperature route (`ct_rt`) — its sources and its filters are that route's — and is an alternative to it: one line per qubit against several qubits per line. It complements the cold-side routes rather than competing with them: cryo-CMOS (`ct_cryocmos`), SFQ control (`ct_sfq`) and on-chip flux DACs (`ct_fluxdac`) attack the same wall by moving the electronics into the fridge, and the paper's own architecture pairs frequency multiplexing with on-chip DC sources. It serves any all-microwave gate — cross-resonance (`g_cr`) and the resonator-induced phase gate (`g_rip`) have the frequency-separated drive channels it shares most easily — and the flux-pulsed CZ (`g_tc`) through its multiplexed coupler Z channel, the demonstration's harder half. Price of switching: a longer microwave two-qubit gate and a frequency plan for every shared line; gained: a line count that scales with the lattice's bandwidth, not its qubit count.

## Evidence — how the numbers were measured

The gate errors are randomised-benchmarking averages over the four parallel gates, compared with the same gates on the same device driven through dedicated lines (for CZ) or without filters (for XY) — a within-device comparison, which is why "no statistically significant degradation" is a defensible statement [P][912]. The device is not named and its qubit count is not stated; the ratio is four. The line-count projections are arithmetic on the measured gate parameters and on idealised ones, not measurements, and the thermal figure uses a manufacturer's reference value for a coaxial line's conductive load and excludes the filters, switches and other parasitic loads a real system would carry [P][912]. Value conflict: none within the paper; the gap worth noting is between the CZ error on this device, 6.4×10⁻³, and the errors of the lattice's best flux-pulsed gates, an order smaller — the multiplexing cost nothing, but the gates it multiplexed were not the field's best. Not published: the device, the filter insertion loss, a ratio above 1:4, a run on more than four pairs.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| University of Science and Technology of China / Hefei National Laboratory (Zhu, Pan) | research | CN | The 1:4 demonstration and the framework | [P][912] |
| QuantumCTek | developer | CN | Co-author of the demonstration; the control-electronics and processor vendor of the Tianyan machines in the register | [P][912] |
| Beijing Academy of Quantum Information Sciences | research | CN | The 2023 multiplexed-control proposal | [S][911] |
| D-Wave | developer | US/CA | The cold-side alternative: on-chip flux DACs behind a few hundred lines (`ct_fluxdac`) | — |

**Money.** No dated money is attached to this technology; the demonstration is university and national-laboratory work with a vendor co-author.

**Market & supply chain.** The parts are the microwave-component market's; the method is one group's. If adopted, it shifts value from cable and connector vendors to the makers of multi-tone sources and filter banks — and to whoever integrates the filters cold.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** No vendor's roadmap names frequency-multiplexed gate drive; QuantumCTek's co-authorship is the only industrial signal. The authors' own claim is an architecture statement — "frequency-multiplexed control as a viable scaling architecture" — made on four pairs [P][912].

**Strategic reading.** The I/O wall has been the standing argument for cold electronics. If multiplexed gate drive holds at 1:12 on a hundred-qubit lattice, the wiring count stops being that argument at 10⁴ qubits and the cold-side routes keep only the thermal and latency arguments; if it does not, the demonstration joins the list of methods that worked on four qubits. The work is Chinese and the vendor is QuantumCTek, so the first adopter, if any, is likely to be a Tianyan successor.

## Outlook & open questions

Confirm within 12–24 months if a processor of a hundred qubits or more is driven at 1:8 or better with gate errors equal to its dedicated-line baseline, or if a vendor's machine ships with multiplexed gate lines. Demote if nothing beyond the 1:4 paper appears by end-2027, or if the integrated filters the 1:48 ratio needs turn out to cost more fridge space than the cables they replace. Best case by 2029: a 10⁴-qubit cryostat wired with a few hundred lines; worst case: a control-rack option nobody specifies.

Open questions: (1) what filter isolation is achievable cold, and at what insertion loss? (2) does the frequency plan survive the frequency spread of a real lattice? (3) how does the scheme share a line between flux-pulsed gates, which are broadband, and microwave ones? (4) what is the real thermal budget with filters and switches counted? (5) does any vendor outside China pick it up?

## References

[911] P. Shi, J. Yuan, F. Yan, and H. Yu, “Multiplexed control scheme for scalable quantum information processing with superconducting qubits,” [arXiv:2312.06911](https://arxiv.org/abs/2312.06911), Dec. 2023. [S]
[912] D. Li *et al.*, “A control line multiplexing framework for scalable quantum computing,” [arXiv:2610.35227](https://arxiv.org/abs/2610.35227), Oct. 2026. [P]

