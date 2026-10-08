---
id: fab_optics
name: Optical / mechanical assembly (lasers, vacuum, objectives)
layer: "10 Manufacturing"
status: demonstrated
since: 2016
one_line: The laser, ultra-high-vacuum and imaging-optics stack that traps, cools, addresses and reads out both trapped-ion and neutral-atom qubits — infrastructure, not a qubit.
verdict: Serves two platform families, ions and atoms — the photonic-IC and CMOS foundries serve more — so its vendors are modality-agnostic; supply concentrates in beam steering, two AOD houses, while lasers have a leader (TOPTICA) among six named vendors, and free-space delivery is the wall past ~10⁴ sites.
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The shared laser, ultra-high-vacuum and imaging-optics infrastructure under trapped ions (Quantinuum, AQT, IonQ) and neutral-atom tweezer arrays (Harvard with QuEra, Pasqal, Atom Computing, Infleqtion, Google). It holds no qubit and performs no gate: it supplies cooling and addressing light, vacuum confinement, high-NA objectives and the beam-steering that places atoms. It became a separate discipline with dedicated vendors from about 2016.
Attributes: no carrier, no entangling time, no readout channel and no mobility of its own — the physical layer other nodes ride on.
Manufacturing category optics and mechanical assembly; the error it contributes downstream is coherent — drift, vibration, pointing and frequency noise, not stochastic Pauli noise.

## Physics & limits
Laser frequency and intensity noise convert into coherent dephasing on every gate driven by that light. Background-gas pressure sets the atom lifetime — one source of atom loss beside gates and imaging — and in the 448-atom system loss makes up over 80% of all leakage: detectable, therefore erasure-convertible, which turns loss control, the vacuum included, into a code-level asset [D][4]. Objective numerical aperture sets tweezer pitch and crosstalk. Beam steering sets rearrangement speed under two limits that pull against each other — a deflector resolves as many spots as its rf bandwidth times the acoustic transit across the beam, and that transit bounds how fast a trap is re-pointed — while liquid-crystal modulators reframe only at tens of hertz. The harder scaling term is power: Rydberg and Raman light is divided among sites, so an array becomes power-limited before it becomes optics-limited. What moves the floor is photonic integration and higher-bandwidth deflectors; neither removes the vacuum or the objective.

## Engineering state of the art
Continuous operation is the headline result: two optical-lattice conveyor belts carry atom reservoirs into the science region, atoms are extracted into tweezers at 300,000 per second, and from that flux the system creates over 30,000 initialised qubits per second, enough to hold an array of more than 3,000 atoms for over two hours while stored qubits keep T2 above a second — 1.34 s undisturbed, 1.15 s while the magneto-optical trap loads new atoms, 1.09 s during imaging and sorting [D][144]. Both rates are correct and differently scoped. Elsewhere: 11,000 atoms in 18,225 metasurface tweezers with no gates [D][145], and 6,100 atoms with 12.6 s coherence [D][138]. Pasqal quotes 3 kW average power and 2,500 kg for a room-temperature Orion Gamma rack [C][438] — a brochure figure, not an audited one.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-03 | 6,100-atom tweezer array, 12.6 s coherence | Caltech | [D][138] |
| 2025-11 | 3 kW average power, 2,500 kg, room temperature | Pasqal Orion Gamma | [C][438] |
| 2025-09 | 300,000 atoms/s into tweezers, 30,000 initialised qubits/s, >3,000 atoms held >2 h | Harvard with QuEra | [D][144] |
| 2026-06 | 11,000 atoms in 18,225 metasurface tweezers, no gates | Tsinghua | [D][145] |

## Manufacturing, materials & supply chain
Lasers have a leader, not a monopoly: TOPTICA Photonics (Munich) states EUR 140 M revenue and 600 staff and calls quantum technology its founding market [C][815], and is named the principal supplier to ion builders alongside MOGLabs, Menlo Systems, Coherent, Thorlabs and NKT [P][322]. Beam steering is where supply concentrates, a duopoly in practice: only two deflector houses appear across the sourced neutral-atom literature — AA Opto-Electronic, whose crossed DTSX-400 AODs sit in the 448-atom system beside a Hamamatsu modulator and camera, Spectrum Instrumentation waveform generators, a Rohde & Schwarz source and a 0.65-NA Special Optics objective [D][4], and Gooch & Housego, in the 3,000- and 6,100-atom papers [P][504]. Vacuum is more diversified (Pfeiffer, Edwards and Leybold under Atlas Copco, Agilent, Kurt J. Lesker, VACOM) but consolidating, with a Universal Quantum–Atlas Copco MoU in December 2025 [P][502]. Export exposure is oblique: the 2024-09-06 BIS rule controls assembled quantum computers under ECCN 4A906 only when qubit count and two-qubit (C-NOT) error fall in the same band — from 34–99 qubits at ≤ 10⁻⁴ to any error at 2,000 qubits and more — and no ECCN names ion traps, atom-array vacuum or tweezer optics [G][301]: no quantum-specific entry reaches the subsystems, and a finished machine is caught only inside those bands.

## Control, readout & I/O burden
This tier imposes I/O rather than bearing it. Helios needs at least seven wavelengths — its paper names six, from 369 to 1762 nm, and loads both barium and ytterbium by photoionisation — against 1,228 trap electrodes [D][97]; a tweezer array needs one deflector order or hologram per addressed site. At 10³ sites, addressing optics and power splitting are already the dominant integration cost; at 10⁴, steering bandwidth and optical power bind; at 10⁶, free-space delivery is not credible — which is why photonic-integrated delivery is the watched path.

## Role in the stack
It sits under six architectures — as the primary assembly under alkali and alkaline-earth tweezer arrays and the neutral-atom analogue simulator, and as an alternate under all three trapped-ion architectures (QCCD, the linear Paul trap with laser addressing, electronic gates) — providing lasers and vacuum to ions, tweezers to both atom families, clock lasers to alkaline earths and cavities to the atom–photon link. It requires nothing upstream, replaces nothing and conflicts with nothing: shared in economic terms, invisible in architectural ones. It sets no derived clock but bounds every architecture's through laser-lock, imaging and rearrangement time — imaging alone is 0.5–1 ms of a 1–4.5 ms atom cycle. No empty slot is flagged.

## Evidence — how the numbers were measured
Pasqal's power and mass carry a company-claim tag, not a measurement tag [C][438]. TOPTICA's revenue and headcount are corroborated by its own page [C][815]; "dominant supplier" rests on one secondary source [P][322].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| TOPTICA Photonics | supplier | Germany | Lasers for ion and atom platforms; EUR 140 M revenue, 600 staff | [C][815] |
| AA Opto-Electronic | supplier | France | Crossed DTSX-400 AODs in the 448-atom system | [D][4] |
| Gooch & Housego | supplier | UK | Deflectors in the 3,000- and 6,100-atom papers | [P][504] |
| Atlas Copco (Edwards, Leybold) | supplier | Sweden | MoU to industrialise high-vacuum systems | [P][502] |
| Pasqal | user | France | Orion Gamma rack: 3 kW, 2,500 kg, room temperature | [C][438] |
| Harvard with QuEra | user | US | Conveyor reload holding >3,000 atoms >2 h | [D][144] |
| Quantinuum | user | US-UK | Helios: ≥7 wavelengths over 1,228 electrodes | [D][97] |

**Money.**
- 2022-11-02 · Universal Quantum · government contract · EUR 67 M · DLR · closed [P][328]
- 2023-12-05 · Alpine Quantum Technologies · system sale to Leibniz Supercomputing Centre · ≈EUR 9.8 M for 20 qubits · closed [C][323]
- 2026-06 · Atom Computing · equity plus CHIPS letter of intent · >USD 300 M incl. USD 100 M LOI · closed [C][154]
- 2026-08-28 · Pasqal · SPAC completion · ~USD 360 M cash, EUR 16.5 M 2025 revenue · closed [P][156]

**Market & supply chain.** It serves two platform families, ions and atoms, so its vendors are indifferent to which wins. Unit economics differ about 7.5-fold between the two ends: QuNorth ordered the 1,225-physical, 50-logical Magne system from Atom Computing and Microsoft for EUR 80 M, ~EUR 65 k per atom [P][12], while AQT delivered 20 trapped ions for EUR 9.8 M, ~EUR 0.5 M per ion [C][323]. Tweezer optics amortise across thousands of sites; ion optics scale closer to per-ion. All of G1–G7 pays for this tier.

**IP & standards.** No dated patent-family fact specific to laser, vacuum or objective IP was found as of 2026-09-04. No standards body covers this tier; vacuum-flange, laser-safety and optical-mount standards predate quantum computing — the components are commodity, the integration is not.

**Roadmaps & track record.** Universal Quantum (promised 2022-11 · two computers for DLR within four years, so by 2026-11 · no delivery announced as of 2026-09-30) [P][328] — at risk, not yet overdue. Pasqal (promised 2024-03 · 10,000 physical in 2026 · slipped to 2028) [R][166]. QuEra (promised 2024-01 · 100 logical in 2026 · replaced by Libra in 2028) [R][162]. The supplier side publishes no checkable roadmap.

**Strategic reading.** Suppliers here hold bargaining power no carrier- or gate-specific vendor has: a bet on TOPTICA or Atlas Copco is a bet on both ions and atoms. The threat is not a competitor but a change of form factor — if photonic-integrated delivery arrives, value migrates to PIC foundries and the AOD duopoly is the exposed link. Builders integrating optics in-house trade cost for control; outsourcers trade control for a supplier's industrialisation budget.

## Outlook & open questions
Falsifiable in 12–24 months: confirm/demote that Universal Quantum and Atlas Copco ship a vacuum system past MoU stage; that a second laser vendor is named in a production ion system; that any free-space array rearranges beyond ~10⁴ sites at the pace of error correction. Best case by 2029: photonic-integrated delivery removes pointing sensitivity and per-site optics cost falls. Worst case: supply stays concentrated and this tier's coherent error stays the dominant infidelity term. Open: does anyone displace TOPTICA; does an objective vendor beyond Special Optics appear in the literature; does the ion-versus-atom unit-cost gap persist.

## References
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[12] M. Abdel-Kareem, “Denmark's QuNorth to Acquire 50-Logical-Qubit Magne Quantum Computer from Atom Computing and Microsoft,” Quantum Computing Report, Jul. 17, 2025. [Online]. Available: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ [P]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[138] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[144] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[145] Y. Wang *et al.*, “Trapping 11,000 Atoms in a Tweezer Array Generated by a Single Metasurface,” [arXiv:2606.02715](https://arxiv.org/abs/2606.02715), Jun. 2026. [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[156] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[166] Pasqal, “Pasqal Releases 2025 Roadmap Showcasing Upgradable Platform from Today's Quantum Solutions to Tomorrow's Fault-Tolerant Systems,” Jun. 12, 2025. [Online]. Available: https://www.pasqal.com/newsroom/pasqal-releases-2025-roadmap/ [R]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[328] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]
[438] Pasqal and O. Q.-C. P. brochure, “The Power of Neutral Atom Quantum Processors by Pasqal — Unlock Quantum Computing for Real-World Solutions,” Pasqal, product brochure (PDF). [Online]. Available: https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf [C]
[502] M. Abdel-Kareem, “Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers,” Quantum Computing Report, Dec. 18, 2025. [Online]. Available: https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ [P]
[504] Gooch & Housego (G&H), “G&H Acousto-Optic Deflectors Referenced in Nature Papers Demonstrating 3,000 & 6,100 Qubit Quantum Systems,” G&H, Mar. 2026. [Online]. Available: https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [P]
[815] TOPTICA Photonics, “About the TOPTICA Group.” [Online]. Available: https://www.toptica.com/company [C]

## Open verification items
The ~10 MHz SLM/AOD refresh ceiling above ~10⁴ qubits sometimes quoted cannot be attributed to a device or a measurement, so it is not used here. TOPTICA's "dominant supplier" position rests on one secondary source [322], though its revenue and headcount are now confirmed on the company's own page [815]. Special Optics, for the 448-atom system's 0.65-NA objective, is the only objective vendor named in the sourced literature; none was found for an ion system. The AOD supplier list is verified by absence — only two vendors appear across the sourced literature, which is not the same as only two existing.
