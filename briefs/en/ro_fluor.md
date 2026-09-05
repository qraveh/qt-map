---
id: ro_fluor
name: Fluorescence state detection (ions)
layer: "6 Readout"
tier: 2
status: demonstrated
since: 1995
one_line: State-dependent resonance fluorescence, counted on a PMT, EMCCD, SNSPD or trap-integrated photodiode, is the default non-destructive mid-circuit readout for trapped ions.
verdict: Readout is no longer the weakest link on the best ion system; falsifiable if any published SPAM figure on a production ion system exceeds that system's two-qubit gate error.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A closed cycling transition scatters photons only when the qubit sits in one logical state; counting them collapses the measurement onto a classical bit. Detectors are photomultipliers, EMCCD cameras, superconducting-nanowire single-photon detectors (SNSPDs) or, recently, avalanche photodiodes built into the trap. In use since the earliest trapped-ion demonstrations (1995), unchanged in principle. Coordinates: c = fluorescence readout, non-destructive, mid-circuit capable, ~10⁻⁴ s — 11 µs at 99.931(6)% on ¹⁷¹Yb⁺ with SNSPDs [D][1]; e = optical control, detection hardware at room temperature unlike the ion.

## Physics & limits
The mechanism is photon counting against a dark-count and stray-light background, so the signal is set entirely by how many scattered photons reach a detector: collection numerical aperture (a few percent of 4π), UV transmission, detector quantum efficiency. That last term is where the platform hurts — the cycling transitions are ultraviolet (369.5 nm for Yb⁺), where PMT efficiency is tens of percent and where the 98% system detection efficiencies quoted for SNSPDs do not apply, those being telecom-band figures [D][14]. The 2019 record worked because a molybdenum-silicide SNSPD was built specifically for 369.5 nm, letting the experiment stop on a single detection event [D][1]. The floor is geometry and efficiency, not atomic physics. Errors are Pauli-like misclassification, except when the dark state leaks out of the cycling transition — a loss channel standard SPAM folds into one number. What moves the floor: higher-NA collection, UV-optimised detectors, and moving the detector onto the trap die.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2019-08-21 | 11 µs mean detection at 99.931(6)%, crosstalk ~2×10⁻⁵ at 370 µm, MoSi SNSPD on ¹⁷¹Yb⁺ | Duke University | [D][1] |
| 2022-09-02 | 99.92(1)% in 450 µs with room-temperature trap-integrated avalanche photodiodes, Sr⁺ | MIT Lincoln Laboratory | [D][4] |
| 2025-11 | Helios (98 Ba⁺): SPAM 3.3–4.8×10⁻⁴, leakage 1.1×10⁻⁵/Clifford | Quantinuum | [D][2] |
| 2026 | Forte (36-ion chain): SPAM 0.5% | IonQ | [C][3] |

The reversal matters: on Helios, SPAM sits below the two-qubit gate error (7.9×10⁻⁴) [D][2], and logical SPAM in the [[80,48,4]] code is below 8×10⁻⁶ [D][6]. Readout dominated ion error budgets a decade ago; not now.

## Manufacturing, materials & supply chain
Optical assembly, not a fab layer — high-NA objectives, UV viewports, a detector — aligned per system, so detector variation is a calibration cost, not a yield loss. PMTs and EMCCD/qCMOS cameras come from Hamamatsu and Andor (Oxford Instruments), Hamamatsu the only named vendor for single-photon-sensitivity cameras in this class [C][12]. SNSPDs come from a five-vendor merchant base — Single Quantum, ID Quantique, Photon Spot, Quantum Opus, Scontel — none of which has disclosed funding or revenue [P][13], each carrying a closed-cycle cryostat that PMT and camera channels do not. Upstream, the single points of failure are shared with the rest of the ion stack: UV lasers (TOPTICA) and Infineon's merchant trap fab [P][14]. No ion-readout ECCN exists; the 2024 BIS rule reaches computers and refrigerators, not detectors.

## Control, readout & I/O burden
One collection channel per readout zone, not per qubit — Quantinuum's QCCD shuttles ions into dedicated zones, so channel count scales with zones [D][2]. That is why this layer has not yet hit a wall: at 10³ qubits, zone readout is demonstrated at 98 ions across 8 zones. At 10⁴ a free-space objective per zone stops being buildable and the answer must be integration — trap-integrated photodiodes [D][4] or multiplexed SNSPD arrays, for which a 400,000-pixel row-column camera is the existence proof, at a cost in timing resolution [D][15]. At 10⁶ nothing is published. Mid-circuit readout must also keep up with real-time decoding; at 11–100 µs it does.

## Role in the stack
Serves both ion paths — QCCD with laser gates and chip-controlled electronic gates — and is reused by defect-spin network nodes for optical spin readout. It requires a cycling transition; no competing readout mechanism exists for ions at product scale, dispersive readout being superconducting-specific. The only real choice is detector type, whose switching price is a redesign of the collection optics, not of the processor. In the derived clock — max(gate, readout, transport) — readout has large slack: gates take ~70 µs and readout tens of µs, but a full-width layer is ~55 ms because sorting, transport and cooling dominate [D][2], so faster readout buys nothing today. Multiplexed many-zone readout without a linear cost in channels and cryostats remains an empty slot.

## Verification (QCVV)
SPAM is measured by preparing known bright and dark states and counting misclassification; Helios's 3.3–4.8×10⁻⁴ is a per-zone range, not one number [D][2]. Standard SPAM conflates preparation with measurement and rarely separates leakage or loss from misclassification — quoting discrimination and survival separately, as a 2026 neutral-ytterbium imaging study does (99.89% and 98.80%, not an ion result), is uncommon here [P][7]. The headline numbers are also not commensurable: three species, three detectors, three machines. IonQ's Forte SPAM of 0.5% [C][3] is an order of magnitude worse than Helios's — plausibly a real architecture difference, long chains on a camera versus zoned detection, but it is a specification page against a preprint.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | USA/UK | Zoned fluorescence readout on Helios, SPAM 3.3–4.8×10⁻⁴ | [D][2] |
| IonQ | developer | USA | Camera readout on Forte chains; owns SNSPD maker ID Quantique | [C][3] |
| ID Quantique | supplier | Switzerland | SNSPD detection systems; IonQ-owned since 2025-05-06 | [P][5] |
| Hamamatsu Photonics | supplier | Japan | PMTs and the only named single-photon-sensitivity cameras here | [C][12] |
| Single Quantum | supplier | Netherlands | Merchant SNSPDs, the main non-IonQ alternative | [P][13] |
| MIT Lincoln Laboratory | research | USA | Trap-integrated avalanche photodiodes, 99.92% | [D][4] |

**Money.**
2025-03-03 · IonQ · M&A, ID Quantique (SNSPD detectors) · undisclosed · closed 2025-05-06 [P][5]
2025-09-04 · Quantinuum · private round · USD 600 M at USD 10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G][9]
2026-06-03 · Quantinuum · IPO, Nasdaq QNT · USD 1.68 B gross · cash USD 2.1 B · closed [G][8]
2026-07 · IonQ · M&A, SkyWater Technology foundry · USD 1.8 B · closed [G][16]

**Market & supply chain.** Small money attached to large money. IonQ's purchase of ID Quantique gave one of the two QBI Stage-B ion vendors in-house SNSPD supply that Quantinuum, eleQtron and Quantum Art must buy on the merchant market [P][5][P][13] — the sharpest concentration event here, though its weight is limited while PMTs and cameras remain adequate. No per-channel price is public. Pays for G2 and G3: every ion error-correction result, Helios's 48 logical qubits included, rests on it. It also gates G6, since photonic interconnects need the same detectors at far higher rates.

**IP & standards.** No dated patent-family count specific to ion fluorescence readout was found in a named database — no dated fact found. Photon-number-resolving SNSPD operation is covered by US 11,274,962 B2, licensed exclusively to Quantum Opus [C][13]. No consortium standard governs ion readout.

**Roadmaps & track record.** No vendor publishes a standalone readout roadmap; it rides inside system roadmaps — Quantinuum Sol 2027 and Apollo 2029 [R][2], IonQ 256 qubits at 99.99% slipped from 2026 to H1 2027 [R][17]. Quantinuum delivered Helios on schedule with the SPAM figure it promised; IonQ has published nothing peer-reviewed behind its 0.5% specification, and its detector acquisition has produced no published readout result.

**Strategic reading.** If UV SNSPDs or trap-integrated photodiodes become standard at 10⁴ zones, IonQ's detector ownership plus its SkyWater fab is a real integration advantage and Hamamatsu loses a niche. If PMTs and cameras stay adequate — which Helios suggests — detector choice stays a commodity decision.

*Open niche:* the plug-in is independent SPAM characterisation that separates discrimination error from leakage and loss and reports per-zone spread rather than a best-zone number — a protocol gap ion papers routinely leave open, needing vendor system access but no proprietary trap hardware.

## Outlook & open questions
Confirm by end-2027 if IonQ publishes a peer-reviewed SPAM figure; demote the 0.5% claim if it stays a specification page. Best case by 2029: trap-integrated detectors or multiplexed SNSPD arrays make per-zone readout free at 10⁴ zones. Worst case: readout stays one free-space objective per zone and becomes the mechanical limit on zone count. Open questions: does IonQ's owned detector supply produce a measurable SPAM advantage; can UV SNSPD efficiency approach telecom-band figures; do trap-integrated photodiodes reach the tens of µs free-space detection already achieves.

## Sources
[1] Crain, Cahall, Vrijsen, Wollman, Shaw, Verma, Nam, Kim (Duke University, JPL/Caltech, NIST), "High-speed low-crosstalk detection of a ¹⁷¹Yb⁺ qubit using superconducting nanowire single photon detectors", Communications Physics 2, 97, 2019-08-21 — https://www.nature.com/articles/s42005-019-0195-8 [D]
[2] Quantinuum, Helios (98 Ba⁺), arXiv:2511.05465, 2025-11; Nature, 2026-06 — https://arxiv.org/abs/2511.05465 [D]
[3] IonQ, Forte system page (SPAM 0.5%), accessed 2026-09 — https://www.ionq.com/quantum-systems/forte [C]
[4] Reens, Collins, Ciampi, Kharas, Aull, Donlon, Bruzewicz, Felton, Stuart, Niffenegger, Rich, Braje, Ryu, Chiaverini, McConnell (MIT Lincoln Laboratory), "High-fidelity ion state detection using trap-integrated avalanche photodiodes", Phys. Rev. Lett. 129, 100502, 2022-09-02 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.100502 [D]
[5] "US-based company acquires ID Quantique", startupticker.ch, 2025-03-03 — https://www.startupticker.ch/en/news/US-based-company-acquires-id-quantique [P] [G:IONQ-IDQUANTIQUE-2025-03]
[6] Quantinuum, "Computing with many encoded logical qubits beyond break-even" ([[80,48,4]] on Helios), arXiv:2602.22211, 2026-02 — https://arxiv.org/abs/2602.22211 [D] [G:HELIOS-ICEBERG-2026-02]
[7] Yokoyama, Kashimoto, Shibata et al. (Kyoto University with Yaqumo Inc.), 17.6 µs fluorescence imaging of neutral ¹⁷⁴Yb, arXiv:2605.24175v2, 2026-08-24 — https://arxiv.org/html/2605.24175 [P] [G:KYOTO-FASTIMG-2026-08]
[8] Quantinuum, IPO pricing, 2026-06-03 — https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G] [G:QTM-IPO-2026-06]
[9] Honeywell, "$600 million capital raise for Quantinuum at $10 B pre-money", 2025-09-04 — https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [G] [G:QTM-600M-2025-09]
[10] IonQ, "IonQ completes acquisition of Oxford Ionics" — https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [G]
[11] eleQtron, EUR 57 M Series A — https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[12] Hamamatsu Photonics, ORCA-Quest qCMOS single-photon-sensitivity camera, 2026-09 — https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html [C] [G:HAMAMATSU-CAMERA-CONC-2026]
[13] Merchant SNSPD supply base 2026 (Single Quantum, ID Quantique, Photon Spot, Quantum Opus, Scontel) — https://www.tipranks.com/news/private-companies/single-quantum-hits-400-system-milestone-as-it-deepens-european-quantum-partnerships [P] [G:SNSPD-VENDORS-2026]
[14] Reddy, Nerem, Nam, Mirin, Verma (NIST), 98.0 ± 0.5% fibre-coupled SNSPD system detection efficiency at 1550 nm, Optica 7(12), 2020-11-23 — https://www.nature.com/articles/s41377-025-02031-5 [D] [G:SNSPD-EFF-RECORDS]
[15] Oripov, Rampini, Allmaras, Shaw, Nam, Korzh, McCaughan (NIST, JPL), "A superconducting nanowire single-photon camera with 400,000 pixels", Nature 622, 730, 2023-10-25 — https://www.nature.com/articles/s41586-023-06550-2 [D] [G:SNSPD-CAMERA-400K]
[16] IonQ, "IonQ completes acquisition of SkyWater Technology", 2026-07 — https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[17] IonQ, accelerated roadmap, 2025-06-13 — https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R] [G:IONQ-ROADMAP]

## Open verification items
The ID Quantique purchase price is undisclosed, so no valuation can be put on the detector-supply position. IonQ's Forte SPAM of 0.5% has no peer-reviewed counterpart. No vendor publishes per-channel detector cost, and no revenue attributable to ion readout is separable in Hamamatsu's or Oxford Instruments' reporting. No published UV (369–400 nm) SNSPD system detection efficiency was found to set against the 98% telecom-band figure. The Kyoto/Yaqumo 17.6 µs imaging result is a neutral-ytterbium atom measurement, not ion readout, and is cited here only as a methodological comparison.
