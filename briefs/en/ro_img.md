---
id: ro_img
name: Fluorescence imaging of atom arrays
layer: "6 Readout"
status: demonstrated
since: 2016
one_line: Camera-based fluorescence detection of neutral atoms — non-destructive, mid-circuit, millisecond by default, microsecond in single-group demos.
verdict: Sets the neutral-atom QEC round at ~1 ms; unless sub-100 µs low-loss imaging reaches shipped hardware by 2028 it stays the largest fixed cost in the cycle.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An atom on a closed cycling transition scatters photons into a high-NA objective and onto a camera; a photon-count threshold per site decides occupancy or state. Standard on tweezer arrays since about 2016, and the readout every neutral-atom architecture builds on.
Camera fluorescence imaging, ~0.5–1 ms, non-destructive, mid-circuit capable.
Optical control at room temperature; free-space bench optics; error structure is loss.

## Physics & limits
Signal is collection solid angle times quantum efficiency times scattering rate times integration time, and threshold error falls exponentially in collected photons: discrimination is cheap. The cost is recoil: every scattered photon heats the atom, and past a few thousand it leaves the trap, so the failure mode is loss — 0.46% bit-flip against 0.24% loss at 448 atoms [D][4]. Shorter probes improve survival: both 2026 microsecond results report loss an order below the millisecond baseline. NA and quantum efficiency sit near their practical ceiling, leaving recooling during the probe, brighter transitions and parallel zones. Architecturally the round matters: CZ gates take 270 ns while a QEC round takes 1–4.5 ms, imaging 0.5–1 ms of it and transport the rest [D][4].

## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-11 | 0.5–1 ms, 0.46% bit-flip, 0.24% loss, 448-atom FT array | Harvard/MIT/QuEra | [D][4] |
| 2026-08 | 17.6 µs, 99.89(5)% discrimination, 98.80(44)% survival, spinless ¹⁷⁴Yb | Kyoto/Yaqumo | [P][264] |
| 2026-08 | 15 µs probe on a 25-site subarray, 4.1×10⁻⁵ infidelity, 2.1×10⁻⁴ loss | USTC | [P][469] |

Dominant error: imaging-induced loss, not misassignment.

## Manufacturing, materials & supply chain
No fab: an objective, dichroics and a camera on a bench. Hamamatsu's ORCA-Quest qCMOS is the named sensor across the Harvard/QuEra line, with no second source at this sensitivity [P][258]; objectives are commodity microscope optics. Imaging sits inside the QEC cycle, so its cost is per round, not per shot. At 10³ atoms one frame covers the array; at 10⁴–10⁶ pixel count, frame rate and illumination power force parallel zones with a camera each — the regime where SLM/AOD refresh near 10 MHz also stops scaling. Export exposure is indirect: 4A906 binds the machine by qubit count, nothing names tweezer optics or cameras [G][225].

## Role in the stack
Requires an alkali or alkaline-earth atom with a cycling transition; provides the non-destructive mid-circuit measurement real-time decoding needs, and turns atom loss into detectable erasure, not silent Pauli error. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 1.3×10⁻³ s, transport first and this readout second at 501 µs, not the 270 ns gate — ~10³× a superconducting round. Verification: both microsecond results are single-group and single-species; Kyoto's uses spinless ¹⁷⁴Yb, so it establishes occupancy discrimination, not hyperfine state readout, and USTC's 15 µs averages over a 25-site subarray. Neither has run inside a logical memory.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Harvard/MIT | research | US | 448-atom fault-tolerant baseline | [D][4] |
| QuEra Computing | developer | US | Ships this readout in its roadmap | [C][137] |
| Atom Computing | developer | US | Yb arrays; Magne with Microsoft | [C][138] |
| Kyoto Univ./Yaqumo | research | Japan | 17.6 µs Yb imaging demo | [P][264] |
| Hamamatsu Photonics | supplier | Japan | qCMOS sensor, no second source | [P][258] |

**Money.** 2025-09-09 · QuEra · Series B · $230 M+ USD · Google, SoftBank VF2, NVentures [C][137]. 2025-11-06 · DARPA · QBI Stage B · ≤$15 M each · Atom and QuEra among eleven [G][60]. 2026-02 · Infleqtion · NYSE listing · >$550 M USD, plus $100 M DoC LOI [C][139]. 2026-06 · Atom Computing · raise · $300 M+ USD incl. $100 M Commerce LOI [C][138]. 2026 · QuNorth · Magne order, 50 logical · €80 M · Atom/Microsoft [P][12].

**Market & supply chain.** One vendor's sensor sits in the critical path of every leading array, the rest being commodity optics — sharp concentration risk. It pays into G3 and G4: no mid-circuit imaging, no real-time decoding.

**IP & standards.** No dated patent family or standard specific to atom-array imaging.

**Roadmaps & track record.** (2026-08 · fast imaging shown standalone · not folded into a logical run); (2028–29 · QuEra Libra and Magne targets · assume the cycle keeps shrinking) [R][137]. Vendor roadmaps price in a speed-up shown only on subarrays.

**Strategic reading.** Whoever ships sub-100 µs low-loss imaging first collapses the largest fixed cost in the neutral-atom cycle taking a factor of several in effective clock, the platform's one structural weakness. Camera suppliers hold more leverage than their revenue implies; atom vendors none over them.

*Open niche:* Imaging-loss statistics are decoder inputs; independent validation of discrimination and survival claims — the gap both 2026 papers share — needs no atom array.

## Outlook & open questions
Confirm if a microsecond result is folded into a logical memory run by 2028; demote if it stays readout-only. Best case 2029: sub-50 µs imaging is standard and QEC rounds fall below 0.5 ms. Worst case: millisecond imaging stays the default and caps the cycle near 1 ms. Open: does fast imaging hold across a full array, and does it shift the loss-versus-Pauli mix decoders assume?

## Sources
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[12] M. Abdel-Kareem, “Denmark's QuNorth to Acquire 50-Logical-Qubit Magne Quantum Computer from Atom Computing and Microsoft,” Quantum Computing Report, Jul. 17, 2025. [Online]. Available: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ [P]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[137] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[138] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[139] L. Roady, “Infleqtion Becomes First Neutral-Atom Quantum Company to Go Public,” Infleqtion, Feb. 17, 2026. [Online]. Available: https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [C]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[258] M. Ivezic, “The Tweezer Array's Hidden Supply Chain: Who Really Wins If Neutral-Atom Quantum Computing Wins,” PostQuantum.com, Nov. 17, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/neutral-atom-quantum-ecosystem/ [P]
[264] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[469] Xu-Zhao-Qiu Zeng *et al.*, “Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor,” [arXiv:2608.17189](https://arxiv.org/abs/2608.17189), Aug. 2026. [P]

## Open verification items
The Kyoto/Yaqumo 17.6 µs result is on spinless ¹⁷⁴Yb, which has no hyperfine qubit — occupancy discrimination, not state readout; no independent replication found. USTC's 15 µs is an average probe time over a 25-site subarray; the corresponding figure for a full 100-site array is not stated. The camera used in the Kyoto demonstration is not identified in the sources found, so no sensor attribution is made for it. No quotable unit cost per readout channel for camera plus objective. QuNorth's €80 M Magne order is trade-press sourced; no vendor release found.
