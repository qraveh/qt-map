---
id: ct_ionlaser
name: Laser control with integrated photonics (ions)
layer: "5 Control"
status: demonstrated
since: 2020
one_line: On-chip waveguides route cooling, gate and readout light to trapped ions, replacing free-space beams with lithographically fixed optical paths.
verdict: Proven in laboratory chips (two-ion entanglement at > 99.3% fidelity, 2020) but in no product: Helios still delivers its ≥7 wavelengths to 8 zones as free-space beams, and the best laser gate at scale (7.9×10⁻⁴) is an order of magnitude behind the laser-free electronic gate it competes with.
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Light for cooling, state preparation, gates and readout runs in single-mode waveguides fabricated into or beside the trap chip, exiting at the ion through grating couplers instead of free-space beams aligned through vacuum viewports. ETH Zürich demonstrated waveguide-delivered multi-ion logic above 99.3% two-qubit fidelity in October 2020 [D][583]. No product uses it yet: Quantinuum's Helios (≥7 wavelengths, 8 zones) delivers its light as focused free-space beams running parallel to the chip surface [D][97], while Sandia's MESA complex designs and tests integrated-photonics components with Quantinuum for possible inclusion in future platforms, under a CRADA in force for four years and renewed in May 2026 [G][501].
Attributes: optical control modality on a natural ion carrier, delivered inside the vacuum system; no intrinsic gate or readout channel.
Dominant error is coherent — crosstalk, stray-light shifts, phase noise; fabrication is a photonic-IC foundry process (SiN, BTO or thin-film lithium niobate).

## Physics & limits
The gate physics is untouched — MS and light-shift gates run identically whether the beam arrives from a mirror or a waveguide, so gate times stay microsecond-scale. Optical power per site is capped by waveguide loss and coupler efficiency, and since gate rate scales with intensity, a loss budget becomes a gate-time budget. Stray light from the photonic layer ac-Stark-shifts and heats neighbouring zones — a coherent channel free-space delivery lacks, traded against the alignment drift it has. And the binding material constraint is the shortest wavelength in the set: Helios's Ba⁺ qubits run on visible and infrared lines (gates at 515 nm), but its Yb⁺ coolant ions are cooled at 369 nm [D][97], where waveguide loss and photodarkening are worst and where the supply chain's constrained laser wavelength sits [P][322] — the choice of species, coolant included, and photonic integrability are one decision. Moving the floor needs UV-transparent waveguide materials, better couplers, denser multiplexing, and on-chip modulators.

## Engineering state of the art
| Year | Figure | Who | Tag/key |
|---|---|---|---|
| 2020-10 | Waveguide-delivered multi-ion 2Q gate > 99.3% | ETH Zürich | [D][583] |
| 2024-07 | All-electronic 7-zone trap, 2Q 99.97(1)%, 10 qubits — no gate lasers | Oxford Ionics | [D][257][G:OXIONICS-ALLELEC-2024-07] |
| 2025-10 | Electronic 2Q error 8.4×10⁻⁵, no ground-state cooling | IonQ/Oxford Ionics | [D][102] |
| 2025-11-05 | Helios: 98 Ba⁺, 8 zones, ≥7 wavelengths, all free-space; 2Q 7.9(2)×10⁻⁴, 1Q 2.5(1)×10⁻⁵, SPAM 4.8(6)×10⁻⁴ | Quantinuum | [D][97] |

The uncomfortable comparison: the best laser gate at scale sits at 7.9×10⁻⁴ while the laser-free electronic gate reaches 8.4×10⁻⁵ [D][97], [102]. Integrated photonics competes on stability, zone count and manufacturability, not fidelity; no vendor publishes a metric for the photonic layer itself.

## Manufacturing, materials & supply chain
Waveguides (SiN or thin-film lithium niobate) come from photonic-IC foundries, and co-integrating them with trap electrodes is not confined to Sandia's MESA research complex: LioniX International, a merchant photonics foundry, built ETH Zürich's 2020 traps with electrodes, waveguides and couplers on one chip [C][882], and MIT Lincoln Laboratory's chip of the same year delivered every wavelength a Sr⁺ qubit needs [D][883]. The volume merchant trap fab is Infineon's Villach line (6–12 inch, anodic bonding, Gen-3 out-of-plane electrodes), serving Oxford Ionics/IonQ, eleQtron and Universal Quantum, while Honeywell fabricates Quantinuum's traps in-house [C][320][G:INFINEON-IONTRAP-FAB-2026]. Sandia is therefore a process-development partner, not a supply bottleneck: the genuine single points of failure are UV laser supply (TOPTICA) and Infineon's fab [P][322]. No ECCN names ion traps or ion-control photonics [G][301][G:BIS-QUANTUM-ECCN-2024-09]; only the finished machine can be caught, under 4A906, and only when its qubit count and C-NOT error fall in the same band, from 34–99 qubits at ≤ 10⁻⁴ to any error from 2,000 qubits [G:BIS-3A901A-CRYOCMOS].

## Control, readout & I/O burden
Helios sends several free-space beams to each of its 8 zones [D][97]; the same trap carries 1,228 electrodes, so the electrical interface is already an order of magnitude larger — optical delivery is not today's binding I/O. Gate-loop latency is unchanged — microsecond-scale, set by the ion-light interaction — so the gain is reliability, not speed. At 10³ ions, beyond Helios's 8 zones, integrated delivery is a candidate for future platforms [G][501]; at 10⁴ routing that many low-crosstalk channels is unproven, and neither Sandia partnership names a channel count — both cite scalability as their purpose [G][501], [584]; at 10⁶ no path exists, and optical power per waveguide, not channel count, would bind.

## Role in the stack
This node is the alternate light delivery of two trapped-ion architectures, "Trapped ions — QCCD (transport between zones)" (Quantinuum) and "Trapped ions — linear Paul trap with individual laser addressing"; it requires photonic-IC fabrication and feeds the Mølmer–Sørensen / light-shift gate. It replaces microwave and electronic ion control, and the switching cost is not a component swap but a fork: an entire laser system against an entire electrode system, with trap geometry, species and error budget downstream. IonQ owns both sides. The node shares the fabrication constraint of natural-carrier platforms needing photonic integration. Delivery does not enter the derived clock: Helios's 2Q gate is ~70 µs but the round is 9.66 ms and the measured full-width layer ~55 ms, dominated by transport, sorting and cooling.

## Evidence — how the numbers were measured
The 2020 two-qubit figure is the fidelity of the entangled state the waveguide-delivered gate prepares [D][583], not a benchmarked gate error; a paired comparison with free-space delivery on one trap is possible, but none is published. No vendor reports the photonic layer's crosstalk, stray-light heating or phase-noise contribution; Helios's numbers are system-level and free-space [D][97], and Sandia's August 2026 announcement carries none [G][501]. No independent replication of the 2020 ETH result was found. Reading caveat: AQT's "QV record" of 32,768 is 2¹⁵ against 2²⁵ for Quantinuum's H2 — a record within the rack-mounted class, with no gate time or fidelity disclosed [C][128][G:AQT-LYNX-QV-CONTEXT-2026].

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK | Develops integrated photonics with Sandia for future platforms; Helios's 8 zones still take free-space beams | [D][97], [G][501] |
| Sandia National Laboratories | research | US | MESA designs and tests integrated photonics for future trapped-ion platforms; CRADA with Quantinuum, MOU with IonQ | [G][501], [584] |
| IonQ | developer | US | Sandia MOU on photonics; owns Oxford Ionics and SkyWater | [C][19], [584] |
| Infineon Technologies | supplier | AT | Merchant ion-trap fab at Villach | [C][320] |
| TOPTICA Photonics | supplier | DE | Dominant laser supplier; UV is the constrained input | [P][322] |

**Money.**
2025-09-17 · IonQ · M&A, Oxford Ionics (electronic gates) · $1.075 B · closed [C][G:IONQ-OXIONICS-2025]
2026-06-03 · Quantinuum · IPO, Nasdaq QNT · $1.68 B gross; Q2-2026 revenue $8.0 M, cash $2.1 B · closed [C][123][G:QTM-IPO-2026-06]
2026-07-31 · IonQ · M&A, SkyWater Technology (captive US fab) · ~$1.8 B · closed [C][19][G:IONQ-SKYWATER-2026]
2026-08-04 · IonQ / Sandia · MOU, quantum co-design for US security work · undisclosed · signed [C][584][G:IONQ-SANDIA-MOU-2026-08]

**Market & supply chain.** Two upstream markets feed this node, both thin: PIC fabrication co-integrated with trap electrodes, shown at MESA, MIT Lincoln Laboratory and one merchant foundry, LioniX, with PIXEurope the only open-access capacity being built [G][582], and UV-capable lasers, dominated by TOPTICA [P][322]. No $/unit or $/channel figure is disclosed. G3 and G4 pay for this node — multi-zone delivery is what QCCD scaling requires — plus G7 for replacing field alignment with a fab step.

**IP & standards.** No dated patent family specific to integrated photonics for ion control was found. A 2026 PatSnap analysis puts IonQ first among trapped-ion assignees with 9+ filings on gate and beam-geometry techniques [P][375]. No standards activity identified.

**Roadmaps & track record.** Quantinuum: Helios (promised 2024-09 · for 2025 · delivered 2025-11-05), Sol (2027, 2D grid trap, in validation), Apollo (2029) [R][118]; the QV 10×/year commitment was met. IonQ: 4,000 qubits (promised 2020 · for 2026 · missed ~40×), 256 qubits at 99.99% slipped to H1 2027; both photonics commitments are under three months old as of 4 Sep 2026, with no published result.

**Strategic reading.** The rival here is not another photonics vendor but the removal of lasers from the gate entirely. The electronic gate leads on fidelity by an order of magnitude, laser delivery on demonstrated zone count; whichever closes its gap first takes the architecture. IonQ has bought both sides and can wait. Quantinuum cannot: it is committed to lasers, and its integrated photonics is being developed at a national laboratory that also serves its main competitor. Free-space alignment hardware is designed out either way; TOPTICA and Infineon keep bargaining power regardless.

## Outlook & open questions
Milestones (12–24 months): Sol ships with integrated delivery in its zones and no fidelity regression (confirm); Sandia or Quantinuum publishes a photonic-layer metric (confirm); waveguide-delivered 2Q error reaches the 10⁻⁴ decade (confirm) — or Sol ships on free-space beams like Helios (demote). Best case 2029: integrated delivery is default across laser-gate platforms at 10³-zone scale, crosstalk below the gate-error budget; worst case, it stays in laboratory chips while electronic gates take the trapped-ion roadmap. Open: the photonic layer's isolated error contribution; whether a UV-capable waveguide platform exists for Yb⁺; whether MESA's process transfers to a production fab. Watch: Sol's 2027 delivery, the first Sandia–IonQ publication.

## References
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[118] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[123] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[257] C. Löschnauer *et al.*, “Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040313, Oct. 2025, doi: [10.1103/h4wk-v31j](https://doi.org/10.1103/h4wk-v31j). [arXiv:2407.07694](https://arxiv.org/abs/2407.07694). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[501] T. Rummler, “In the Mountain West, a quantum computing collaboration announces major results,” Sandia Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/ [G]
[582] imec, “The European Commission and Chips JU select the PIXEurope consortium to lead the European Pilot Line on Advanced Photonic Integrated Circuits,” Nov. 24, 2024. [Online]. Available: https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line [G]
[583] K. K. Mehta *et al.*, “Integrated optical multi-ion quantum logic,” *Nature*, vol. 586, no. 7830, pp. 533–537, Oct. 2020, doi: [10.1038/s41586-020-2823-6](https://doi.org/10.1038/s41586-020-2823-6). [D]
[584] IonQ, “IonQ and Sandia National Laboratories Sign MOU to Accelerate Quantum Co-Design for National Security Applications,” Aug. 4, 2026. [Online]. Available: https://www.ionq.com/news/ionq-and-sandia-national-laboratories-sign-mou-to-accelerate-quantum-co-design-for-national-security-applications [C]
[882] LioniX International, “A photonic integrated ion trap for scalable quantum computing,” Nov. 20, 2020. [Online]. Available: https://www.lionix-international.com/about-us/blog/a-photonic-integrated-ion-trap-for-scalable-quantum-computing/ [C]
[883] R. J. Niffenegger *et al.*, “Integrated multi-wavelength control of an ion qubit,” *Nature*, vol. 586, no. 7830, pp. 538–542, Oct. 2020, doi: [10.1038/s41586-020-2811-x](https://doi.org/10.1038/s41586-020-2811-x). [arXiv:2001.05052](https://arxiv.org/abs/2001.05052). [D]

## Open verification items
No fidelity, loss or crosstalk figure specific to Sandia's MESA integrated-photonics process was found; the August 2026 Sandia announcement gives none. Which Quantinuum system will first carry integrated delivery is unstated: Sandia's release names only "future platforms", and the Helios paper describes free-space beams. No dated patent family specific to integrated photonics for ion control was found, and no ECCN names ion traps or ion-control photonics. Whether SkyWater will fabricate trapped-ion photonics, and on what timeline, is unstated. The Ba⁺-versus-Yb⁺ wavelength argument is engineering inference from the sourced species and supply-chain facts, not a quoted claim.
