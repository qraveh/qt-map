---
id: cx_qccd
name: Ion shuttling (QCCD, junctions, grid traps)
layer: "4 Connectivity / transport"
status: demonstrated
since: 2002
one_line: Moving trapped ions between zones through junctions or grid traps so a small gate-able crystal inherits all-to-all connectivity.
verdict: Sorting, splitting and re-cooling — not the hop, not the gate — set the ion clock (~55 ms per full-width layer on Helios). Without a 10x cut by 2028 ion QCCD stays high-fidelity and low-throughput.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
QCCD, proposed by Kielpinski, Monroe and Wineland in 2002 [D][1], splits the register into zones and uses time-varying electrode voltages to move ions between memory and interaction zones, so no chain need be both long and gate-able — routing bought with trap area. Junctions make it two-dimensional; grid traps permute ions like a sliding-tile puzzle.

Mobility and time: the carrier itself moves, at 1.7–4 m/s measured [D][2], [3], so connectivity is a schedule, not a coupler map; move-plus-re-cool ~2 ms, entangling determinism inapplicable. Error and fabrication: coherent motional excitation plus ion loss, seen as raised two-qubit infidelity and leakage; MEMS surface-electrode chips on DC waveforms.

## Physics & limits
Ramping neighbouring segment voltages drags a potential well, and its ion, along the axis — and the move need not be slow: NIST moved ⁹Be⁺ 370 µm in 8 µs, excitation peaking at 1.6 quanta and returning to 0.2 by waveform design [D][4]. The millisecond cost is therefore not the hop but splitting and recombining crystals (two ions split in 55 µs kept ~2 quanta each [D][4]) and the sideband cooling that restores the gate modes.

At a junction the RF null is discontinuous: the ion crosses a pseudopotential bump with excess micromotion, which sets transit speed and heating. Beneath that is anomalous heating from electrode-surface noise, steep as the ion nears the surface, so tighter confinement cannot buy adiabaticity. What moves the floor is a gate tolerant of a warm crystal: the electronic gate reached 8.4×10⁻⁵ error without ground-state cooling [D][5], deleting the re-cool term rather than shrinking it.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2022-06 | X-junction round trip, 4 m/s average, 0.013(1)–0.030(2) quanta | Quantinuum | [D][2] |
| 2023-02 | Chip-to-chip matter link, 2,424 transfers/s, loss infidelity < 7×10⁻⁸ | Universal Quantum | [D][3] |
| 2024-03 | Grid-trap ion exchange at 2.5 kHz | Quantinuum | [D][6] |
| 2025-11 | 55 ms per full-width layer, 98 ions, 8 zones | Quantinuum | [D][7] |

The gap between primitive and product is the finding: a Helios two-qubit gate takes ~70 µs against ~55 ms per layer, and on H2 transport was ~60% of runtime [D][7], [8]. The dominant term is the schedule — sorting, split/merge, re-cooling, serialisation across eight zones.

## Manufacturing, materials & supply chain
Traps are segmented-electrode chips. Honeywell is Quantinuum's captive fab and made Sol's 2D grid chip, in validation as of Q2 2026 [C][9]. Infineon Villach is the merchant line — 6–12 inch wafers, Generation-3 out-of-plane electrodes claimed to raise confinement ~10× — serving Oxford Ionics, eleQtron, Innsbruck and ETH at once [C][10]. IonQ broke that duopoly by buying SkyWater for ~$1.8 B, closed 2026-07-31: the first ion vendor to own fabrication [G][11]. Sandia's MESA stays research-only [G][12]. No yield figure is public; the only price is AQT's EUR 9.8 M 20-qubit turnkey system, ≈ EUR 0.5 M per qubit [C][13]. Single points of failure: Infineon's one line, and UV lasers, where TOPTICA dominates and 369 nm for Yb⁺ is constrained [P][14]. No ECCN names ion traps, but a finished machine falls under 4A906, effective 2024-09-06 [G][15].

## Control, readout & I/O burden
A move is a synchronised DC waveform across tens of electrodes at µs update, then cooling and, for laser gates, beam re-addressing. Helios carries 1,228 electrodes for 98 ions [D][7]: electrode count is what scales, and updates fit three orders inside the 55 ms layer, so electronics is not the wall. At 10³ ions it is ~10⁴ filtered DC channels, which Oxford Ionics would cut to ~200 external sources by putting switching electronics on-chip — a design study, no chip built [S][16]. At 10⁴–10⁶ the constraint is routing cooling and gate light to many zones at once (Helios needs ≥7 wavelengths): none drives more than a few dozen concurrently.

## Role in the stack
Shuttling serves both ion paths — laser-gate QCCD (Quantinuum, AQT) and electronic gates with chip control (IonQ/Oxford Ionics, eleQtron) — providing the arbitrary-pair connectivity that bivariate-bicycle qLDPC memories and high-rate transversal codes assume: Quantinuum's [[80,48,4]] demonstration and IonQ's qLDPC break-even both pay for it in transport. It replaces the static long chain, whose mode spectrum crowds as ions are added; the price is that connectivity becomes scheduling and the clock moves from gate to move — derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 9.7 ms, transport 9.0 ms of it, against the measured ~55 ms full-width layer [D][7]. Neighbouring empty slot: more than two linked modules — the two-module link exists [D][3], nothing larger.

## Verification (QCVV)
Transport has no stand-alone benchmark. It is inferred from sideband thermometry around a move — the 0.013(1)–0.030(2) quanta figures [D][2] — and from two-qubit fidelity after a transport sequence, which folds transport into gate error. Neither captures cumulative heating over a deep circuit, junction loss at scale, or zone cross-talk. The 55 ms layer and 2.5 kHz exchange rate are vendor-reported and externally unreplicated as of 2026-09-04; AQT's quantum volume 32,768 is not a transport measurement and discloses no timing [C][17].

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do here | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK | Ring-junction QCCD, grid trap for Sol | [D][7] |
| Honeywell | supplier | US | Captive fab, made Sol's chip | [C][9] |
| IonQ | developer | US | Junction traps, owns SkyWater | [G][11] |
| Infineon | supplier | AT | Merchant trap foundry, Gen-3 | [C][10] |
| Universal Quantum | developer | UK | Only chip-to-chip matter link | [D][3] |
| AQT | developer | AT | LYNX module, units Q4 2026 | [C][17] |
| Quantum Art | developer | IL | Optical ion-array reconfiguration | [P][18] |

**Money.** 2022-11-02 · Universal Quantum · DLR contract · EUR 67 M · undelivered [P][19]. 2025-09-04 · Quantinuum · round · $600 M at $10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G][20]. 2025-11-06 · Quantinuum and IonQ · QBI Stage B · ≤$15 M each · active [G:QBI-STAGEB-2025-11]. 2026-05-05 · eleQtron · Series A · EUR 57 M [G][21]. 2026-06-03 · Quantinuum · IPO · $1.68 B gross, Nasdaq QNT, cash $2.1 B [G][9]. 2026-07-31 · IonQ · SkyWater M&A · ~$1.8 B, after Oxford Ionics at $1.075 B [G][11], [22].

**Market & supply chain.** Trap fabrication was one captive plus one merchant line; SkyWater adds a vertically integrated third — the year's most consequential supply-chain event [C][10][G][11]. UV lasers stay the harder chokepoint [P][14]. Shuttling is paid for by G2 and is prerequisite to G3 and G4.

**IP & standards.** No shuttling-specific family count is published. Nearest dated: IonQ filed 9+ trapped-ion families across JP/EP/IL in 2025–26; Quantum Art holds two pending IL/KR patents on optical reconfiguration of ion arrays [P][23]. No open-source shuttling stack exists.

**Roadmaps & track record.** Quantinuum: Helios (promised 2024-09-10, launched 2025-11-05 — met); Sol (2027, chip in validation Q2 2026 — on track); Apollo (2029 — unscored) [R][24][C][9]; credible. IonQ: 10,000 physical on one chip by 2027, 2 M by 2030, no published 2D-trap heating or transport data, and a 2020 roadmap that missed 4,000 qubits by ~40× — intent, not plan [R][25]. Universal Quantum has delivered nothing since 2022 [P][26].

**Strategic reading.** Cut layer time 10× and ions convert a fidelity lead into throughput-competitive fault tolerance; fail, and they win logical-qubit headlines while losing on shots per second. Winners either way: Infineon and Honeywell, who sell the scarce object. Substitution threat: neutral-atom tweezers and superconducting long-range couplers — connectivity with no transport.

*Open niche:* No per-junction or per-move QCVV protocol is accepted. A small team could open-source one — quanta per junction crossing, loss per 10⁶ crossings, zone cross-talk, randomised benchmarking interleaving transport with a gate — which no vendor publishes and which would make the 55 ms number auditable.

## Outlook & open questions
Confirm/demote in 12–24 months: Sol ships in 2027 with a published per-layer time; any vendor publishes a full-width layer below 10 ms; Universal Quantum links more than two modules. Best case 2029: sub-10 ms layers put the ion logical clock within ~10× of superconducting. Worst case: layer time stays within 2× of 55 ms and ions stay a platform that demonstrates codes rather than running algorithms. Open: does anomalous heating force cryogenic traps at 10⁴ ions; can split/merge be made quanta-free by optimal control; do warm-crystal gates delete re-cooling; does a second merchant fab appear. Watch: Sol validation, Infineon capacity, IonQ's first SkyWater trap.

## Sources
[1] D. Kielpinski, C. Monroe, and D. J. Wineland, “Architecture for a large-scale ion-trap quantum computer,” *Nature*, vol. 417, no. 6890, pp. 709–711, Jun. 2002, doi: [10.1038/nature00784](https://doi.org/10.1038/nature00784).
[2] W. C. Burton, B. Estey, I. M. Hoffman, A. R. Perry, C. Volin, and G. Price, “Transport of multispecies ion crystals through a junction in an RF Paul trap,” *Phys. Rev. Lett.*, vol. 130, Art. no. 173202, Apr. 2023, doi: [10.1103/PhysRevLett.130.173202](https://doi.org/10.1103/PhysRevLett.130.173202). [arXiv:2206.11888](https://arxiv.org/abs/2206.11888).
[3] M. Akhtar *et al.*, “A high-fidelity quantum matter-link between ion-trap microchip modules,” *Nat. Commun.*, vol. 14, no. 1, Art. no. 531, Feb. 2023, doi: [10.1038/s41467-022-35285-3](https://doi.org/10.1038/s41467-022-35285-3).
[4] R. Bowler *et al.*, “Coherent Diabatic Ion Transport and Separation in a Multi-Zone Trap Array,” *Phys. Rev. Lett.*, vol. 109, Art. no. 080502, 2012, doi: [10.1103/PhysRevLett.109.080502](https://doi.org/10.1103/PhysRevLett.109.080502). [arXiv:1206.0780](https://arxiv.org/abs/1206.0780).
[5] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025.
[6] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756).
[7] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465).
[8] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828).
[9] Quantinuum, “Quantinuum Reports Second Quarter 2026 Results,” Aug. 11, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results [C]
[10] “Infineon Technologies, trapped-ion QPU platform (Villach), company page accessed 2026-09-03,” infineon.com, Sep. 4, 2026. [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[11] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[12] Sandia National Laboratories, “In the Mountain West, a quantum computing collaboration announces major results,” Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/
[13] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[14] “Trapped-ion ecosystem supply analysis, postquantum.com, 2026,” PostQuantum, Sep. 4, 2026. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[15] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies
[16] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773).
[17] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[18] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[19] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]
[20] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale
[21] A. Cordes, “Quantum computing scale-up eleQtron secures €57 million in one of the largest Series A funding rounds worldwide,” eleQtron, May 5, 2026. [Online]. Available: https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/
[22] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[23] PatSnap Eureka, “Trapped Ion Quantum Computing 2026,” patent landscape, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[24] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030
[25] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [C]
[26] M. Abdel-Kareem, “Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers,” Quantum Computing Report, Dec. 18, 2025. [Online]. Available: https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ [P]

## Open verification items
- The author list and exact title of the grid-trap paper [6] could not be retrieved from the arXiv abstract page; attribution to Quantinuum follows the main report's fact-check, and the abstract gives no grid-site count.
- No independent (non-vendor) replication exists for the 55 ms full-width-layer time or the 2.5 kHz grid-exchange rate.
- AQT's LYNX architecture (junction versus linear-only) and its transport and gate times are undisclosed.
- No yield, uniformity or per-die cost figure is public for any ion-trap fab line; the EUR 0.5 M per qubit figure is a 2023 turnkey system price, not a chip cost.
- Whether ECCN 4A906's qubit-count and error-rate threshold captures current commercial ion systems was not checked against the parameter values in the rule text.
