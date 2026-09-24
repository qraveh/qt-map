---
id: ro_fluor
name: Fluorescence state detection (ions)
layer: "6 Readout"
status: demonstrated
since: 1995
one_line: State-dependent resonance fluorescence, counted on a PMT, EMCCD, SNSPD or trap-integrated photodiode, is the default non-destructive mid-circuit readout for trapped ions.
verdict: Readout is no longer the weakest link on the best ion system; falsifiable if any published SPAM figure on a production ion system exceeds that system's two-qubit gate error.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A closed cycling transition scatters photons only when the qubit sits in one logical state; counting them collapses the measurement onto a classical bit. Detectors are photomultipliers, EMCCD cameras, superconducting-nanowire single-photon detectors (SNSPDs) or, recently, avalanche photodiodes built into the trap. In use since the earliest trapped-ion demonstrations (1995), unchanged in principle. Attributes: c = fluorescence readout, non-destructive, mid-circuit capable, ~10⁻⁴ s — 11 µs at 99.931(6)% on ¹⁷¹Yb⁺ with SNSPDs [D][1]; e = optical control, detection hardware at room temperature unlike the ion.

## Physics & limits
The mechanism is photon counting against a dark-count and stray-light background, so the signal is set entirely by how many scattered photons reach a detector: collection numerical aperture (a few percent of 4π), UV transmission, detector quantum efficiency. That last term is where the platform hurts — the cycling transitions are ultraviolet (369.5 nm for Yb⁺), where PMT efficiency is tens of percent and where the 98% system detection efficiencies quoted for SNSPDs do not apply, those being telecom-band figures [D][2]. The 2019 record worked because a molybdenum-silicide SNSPD was built specifically for 369.5 nm, letting the experiment stop on a single detection event [D][1]. The floor is geometry and efficiency, not atomic physics. Errors are Pauli-like misclassification, except when the dark state leaks out of the cycling transition — a loss channel standard SPAM folds into one number. What moves the floor: higher-NA collection, UV-optimised detectors, and moving the detector onto the trap die.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2019-08-21 | 11 µs mean detection at 99.931(6)%, crosstalk ~2×10⁻⁵ at 370 µm, MoSi SNSPD on ¹⁷¹Yb⁺ | Duke University | [D][1] |
| 2022-09-02 | 99.92(1)% in 450 µs with room-temperature trap-integrated avalanche photodiodes, Sr⁺ | MIT Lincoln Laboratory | [D][3] |
| 2025-11 | Helios (98 Ba⁺): SPAM 3.3–4.8×10⁻⁴, leakage 1.1×10⁻⁵/Clifford | Quantinuum | [D][4] |
| 2026 | Forte (36-ion chain): SPAM 0.5% | IonQ | [C][5] |

The reversal matters: on Helios, SPAM sits below the two-qubit gate error (7.9×10⁻⁴) [D][4], and logical SPAM in the [[80,48,4]] code is below 8×10⁻⁶ [D][6]. Readout dominated ion error budgets a decade ago; not now.

## Manufacturing, materials & supply chain
Optical assembly, not a fab layer — high-NA objectives, UV viewports, a detector — aligned per system, so detector variation is a calibration cost, not a yield loss. PMTs and EMCCD/qCMOS cameras come from Hamamatsu and Andor (Oxford Instruments), Hamamatsu the only named vendor for single-photon-sensitivity cameras in this class [C][7]. SNSPDs come from a five-vendor merchant base — Single Quantum, ID Quantique, Photon Spot, Quantum Opus, Scontel — none of which has disclosed funding or revenue [P][8], each carrying a closed-cycle cryostat that PMT and camera channels do not. Upstream, the single points of failure are shared with the rest of the ion stack: UV lasers (TOPTICA) and Infineon's merchant trap fab [P][2]. No ion-readout ECCN exists; the 2024 BIS rule reaches computers and refrigerators, not detectors.

## Control, readout & I/O burden
One collection channel per readout zone, not per qubit — Quantinuum's QCCD shuttles ions into dedicated zones, so channel count scales with zones [D][4]. That is why this layer has not yet hit a wall: at 10³ qubits, zone readout is demonstrated at 98 ions across 8 zones. At 10⁴ a free-space objective per zone stops being buildable and the answer must be integration — trap-integrated photodiodes [D][3] or multiplexed SNSPD arrays, for which a 400,000-pixel row-column camera is the existence proof, at a cost in timing resolution [D][9]. At 10⁶ nothing is published. Mid-circuit readout must also keep up with real-time decoding; at 11–100 µs it does.

## Role in the stack
Serves both ion paths — QCCD with laser gates and chip-controlled electronic gates — and is reused by defect-spin network nodes for optical spin readout. It requires a cycling transition; no competing readout mechanism exists for ions at product scale, dispersive readout being superconducting-specific. The only real choice is detector type, whose switching price is a redesign of the collection optics, not of the processor. In the derived clock — sum of the syndrome round: gate layers + transport + readout + reset — readout has large slack: 100 µs of a 9.7 ms round against 9.0 ms of transport, and a full-width layer is ~55 ms because sorting, transport and cooling dominate [D][4], so faster readout buys nothing today. Multiplexed many-zone readout without a linear cost in channels and cryostats remains an empty slot.

## Verification (QCVV)
SPAM is measured by preparing known bright and dark states and counting misclassification; Helios's 3.3–4.8×10⁻⁴ is a per-zone range, not one number [D][4]. Standard SPAM conflates preparation with measurement and rarely separates leakage or loss from misclassification — quoting discrimination and survival separately, as a 2026 neutral-ytterbium imaging study does (99.89% and 98.80%, not an ion result), is uncommon here [P][10]. The headline numbers are also not commensurable: three species, three detectors, three machines. IonQ's Forte SPAM of 0.5% [C][5] is an order of magnitude worse than Helios's — plausibly a real architecture difference, long chains on a camera versus zoned detection, but it is a specification page against a preprint.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | USA/UK | Zoned fluorescence readout on Helios, SPAM 3.3–4.8×10⁻⁴ | [D][4] |
| IonQ | developer | USA | Camera readout on Forte chains; owns SNSPD maker ID Quantique | [C][5] |
| ID Quantique | supplier | Switzerland | SNSPD detection systems; IonQ-owned since 2025-05-06 | [P][11] |
| Hamamatsu Photonics | supplier | Japan | PMTs and the only named single-photon-sensitivity cameras here | [C][7] |
| Single Quantum | supplier | Netherlands | Merchant SNSPDs, the main non-IonQ alternative | [P][8] |
| MIT Lincoln Laboratory | research | USA | Trap-integrated avalanche photodiodes, 99.92% | [D][3] |

**Money.**
2025-03-03 · IonQ · M&A, ID Quantique (SNSPD detectors) · undisclosed · closed 2025-05-06 [P][11]
2025-09-04 · Quantinuum · private round · USD 600 M at USD 10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G][12]
2026-06-03 · Quantinuum · IPO, Nasdaq QNT · USD 1.68 B gross · cash USD 2.1 B · closed [G][13]
2026-07 · IonQ · M&A, SkyWater Technology foundry · USD 1.8 B · closed [G][14]

**Market & supply chain.** Small money attached to large money. IonQ's purchase of ID Quantique gave one of the two QBI Stage-B ion vendors in-house SNSPD supply that Quantinuum, eleQtron and Quantum Art must buy on the merchant market [P][11][P][8] — the sharpest concentration event here, though its weight is limited while PMTs and cameras remain adequate. No per-channel price is public. Pays for G2 and G3: every ion error-correction result, Helios's 48 logical qubits included, rests on it. It also gates G6, since photonic interconnects need the same detectors at far higher rates.

**IP & standards.** No dated patent-family count specific to ion fluorescence readout was found in a named database — no dated fact found. Photon-number-resolving SNSPD operation is covered by US 11,274,962 B2, licensed exclusively to Quantum Opus [C][8]. No consortium standard governs ion readout.

**Roadmaps & track record.** No vendor publishes a standalone readout roadmap; it rides inside system roadmaps — Quantinuum Sol 2027 and Apollo 2029 [R][4], IonQ 256 qubits at 99.99% slipped from 2026 to H1 2027 [R][15]. Quantinuum delivered Helios on schedule with the SPAM figure it promised; IonQ has published nothing peer-reviewed behind its 0.5% specification, and its detector acquisition has produced no published readout result.

**Strategic reading.** If UV SNSPDs or trap-integrated photodiodes become standard at 10⁴ zones, IonQ's detector ownership plus its SkyWater fab is a real integration advantage and Hamamatsu loses a niche. If PMTs and cameras stay adequate — which Helios suggests — detector choice stays a commodity decision.

*Open niche:* the plug-in is independent SPAM characterisation that separates discrimination error from leakage and loss and reports per-zone spread rather than a best-zone number — a protocol gap ion papers routinely leave open, needing vendor system access but no proprietary trap hardware.

## Outlook & open questions
Confirm by end-2027 if IonQ publishes a peer-reviewed SPAM figure; demote the 0.5% claim if it stays a specification page. Best case by 2029: trap-integrated detectors or multiplexed SNSPD arrays make per-zone readout free at 10⁴ zones. Worst case: readout stays one free-space objective per zone and becomes the mechanical limit on zone count. Open questions: does IonQ's owned detector supply produce a measurable SPAM advantage; can UV SNSPD efficiency approach telecom-band figures; do trap-integrated photodiodes reach the tens of µs free-space detection already achieves.

## Sources
[1] S. Crain *et al.*, “High-speed low-crosstalk detection of a ¹⁷¹Yb⁺ qubit using superconducting nanowire single photon detectors,” *Commun. Phys.*, vol. 2, no. 1, Art. no. 97, Aug. 2019, doi: [10.1038/s42005-019-0195-8](https://doi.org/10.1038/s42005-019-0195-8). [D]
[2] D. V. Reddy, R. R. Nerem, S. W. Nam, R. P. Mirin, and V. B. Verma, “Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm,” *Optica*, vol. 7, no. 12, p. 1649, Dec. 2020, doi: [10.1364/OPTICA.400751](https://doi.org/10.1364/OPTICA.400751). [D]
[3] D. Reens *et al.*, “High-Fidelity Ion State Detection Using Trap-Integrated Avalanche Photodiodes,” *Phys. Rev. Lett.*, vol. 129, no. 10, Art. no. 100502, Sep. 2022, doi: [10.1103/PhysRevLett.129.100502](https://doi.org/10.1103/PhysRevLett.129.100502). [D]
[4] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[5] IonQ, “IonQ Forte: High-Performance Commercial Quantum Computer.” [Online]. Available: https://www.ionq.com/quantum-systems/forte [C]
[6] S. Dasu *et al.*, “Computing with many encoded logical qubits beyond break-even,” [arXiv:2602.22211](https://arxiv.org/abs/2602.22211), Feb. 2026. [D]
[7] “Hamamatsu Photonics, ORCA-Quest qCMOS single-photon-sensitivity camera, 2026-09,” hamamatsu.com. [Online]. Available: https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html [C]
[8] “Merchant SNSPD supply base 2026 (Single Quantum, ID Quantique, Photon Spot, Quantum Opus, Scontel),” tipranks.com, Jul. 4, 2026. [Online]. Available: https://www.tipranks.com/news/private-companies/single-quantum-hits-400-system-milestone-as-it-deepens-european-quantum-partnerships [P]
[9] B. G. Oripov *et al.*, “A superconducting nanowire single-photon camera with 400,000 pixels,” *Nature*, vol. 622, no. 7984, pp. 730–734, Oct. 2023, doi: [10.1038/s41586-023-06550-2](https://doi.org/10.1038/s41586-023-06550-2). [D]
[10] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[11] “US-based company acquires ID Quantique,” startupticker.ch, Mar. 3, 2025. [Online]. Available: https://www.startupticker.ch/en/news/US-based-company-acquires-id-quantique [P]
[12] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [G]
[13] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G]
[14] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[15] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]

## Open verification items
The ID Quantique purchase price is undisclosed, so no valuation can be put on the detector-supply position. IonQ's Forte SPAM of 0.5% has no peer-reviewed counterpart. No vendor publishes per-channel detector cost, and no revenue attributable to ion readout is separable in Hamamatsu's or Oxford Instruments' reporting. No published UV (369–400 nm) SNSPD system detection efficiency was found to set against the 98% telecom-band figure. The Kyoto/Yaqumo 17.6 µs imaging result is a neutral-ytterbium atom measurement, not ion readout, and is cited here only as a methodological comparison.
