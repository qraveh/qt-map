---
id: fab_optics
name: Optical / mechanical assembly (lasers, vacuum, objectives)
layer: "10 Manufacturing"
tier: 2
status: demonstrated
since: 2016
one_line: The laser, ultra-high-vacuum and imaging-optics stack that traps, cools, addresses and reads out both trapped-ion and neutral-atom qubits — infrastructure, not a qubit.
verdict: The only manufacturing tier serving two platform families at once, so its vendors are modality-agnostic; laser supply is concentrated in one German firm and beam-steering in two AOD houses, and free-space delivery is the wall past ~10⁴ sites.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The shared laser, ultra-high-vacuum and imaging-optics infrastructure under trapped ions (Quantinuum, AQT, IonQ) and neutral-atom tweezer arrays (Harvard with QuEra, Pasqal, Atom Computing, Infleqtion, Google). It holds no qubit and performs no gate: it supplies cooling and addressing light, vacuum confinement, high-NA objectives and the beam-steering that places atoms. It became a separate discipline with dedicated vendors from about 2016.
Coordinates: no carrier, no entangling time, no readout channel and no mobility of its own — the physical layer other nodes ride on.
Manufacturing category optics and mechanical assembly; the error it contributes downstream is coherent — drift, vibration, pointing and frequency noise, not stochastic Pauli noise.

## Physics & limits
Laser frequency and intensity noise convert into coherent dephasing on every gate driven by that light. Background-gas pressure sets atom lifetime, and in tweezer arrays the resulting loss is over 80% of all leakage events — detectable, therefore erasure-convertible, which turns a vacuum specification into a code-level asset [D][5]. Objective numerical aperture sets tweezer pitch and crosstalk; beam-steering bandwidth sets rearrangement speed, and the main report puts ~10 MHz refresh as insufficient above ~10⁴ qubits — an assessment, not a measurement. The harder scaling term is power: Rydberg and Raman light is divided among sites, so an array becomes power-limited before it becomes optics-limited. What moves the floor is photonic integration and higher-bandwidth deflectors; neither removes the vacuum or the objective.

## Engineering state of the art
Continuous operation is the headline result: two optical-lattice conveyor belts carry atom reservoirs into the science region, atoms are extracted into tweezers at 300,000 per second, and from that flux the system creates over 30,000 initialised qubits per second, enough to hold an array of more than 3,000 atoms for over two hours without disturbing stored coherence [D][2]. Both rates are correct and differently scoped. Elsewhere: 11,000 atoms in 18,225 metasurface tweezers with no gates [D][4], and 6,100 atoms with 12.6 s coherence [D][3]. Pasqal quotes 3 kW average power and 2,500 kg for a room-temperature Orion Gamma rack [C][1] — a brochure figure, not an audited one.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-03 | 6,100-atom tweezer array, 12.6 s coherence | Caltech | [D][3] |
| 2025-11 | 3 kW average power, 2,500 kg, room temperature | Pasqal Orion Gamma | [C][1] |
| 2025-11 | 300,000 atoms/s into tweezers, 30,000 initialised qubits/s, >3,000 atoms held >2 h | Harvard with QuEra | [D][2] |
| 2026-06 | 11,000 atoms in 18,225 metasurface tweezers, no gates | Tsinghua | [D][4] |

## Manufacturing, materials & supply chain
Lasers concentrate hardest: TOPTICA Photonics (Munich) states EUR 140 M revenue and 600 staff and calls quantum technology its founding market [C][6], and is named the principal supplier to ion builders alongside MOGLabs, Menlo Systems, Coherent, Thorlabs and NKT [P][8]. Beam steering is a duopoly in practice: only two deflector houses appear across the sourced neutral-atom literature — AA Opto-Electronic, whose crossed DTSX-400 AODs sit in the 448-atom system beside Hamamatsu modulators, Spectrum Instrumentation waveform generators and Rohde & Schwarz sources, and Gooch & Housego, in the 3,000- and 6,100-atom papers [P][9]. Vacuum is more diversified (Pfeiffer, Edwards and Leybold under Atlas Copco, Agilent, Kurt J. Lesker, VACOM) but consolidating, with a Universal Quantum–Atlas Copco MoU in December 2025 [P][7]. Export exposure is oblique: the 2024-09-06 BIS rule controls assembled quantum computers under ECCN 4A906, but no ECCN names ion traps, atom-array vacuum or tweezer optics [G][18] — subsystems ship freely, the finished machine does not.

## Control, readout & I/O burden
This tier imposes I/O rather than bearing it. Helios needs at least seven wavelengths against 1,228 trap electrodes [D][11]; a tweezer array needs one deflector order or hologram per addressed site. At 10³ sites, addressing optics and power splitting are already the dominant integration cost; at 10⁴, refresh bandwidth and optical power bind; at 10⁶, free-space delivery is not credible — which is why photonic-integrated delivery is the watched path.

## Role in the stack
It sits under three paths — trapped ions with laser gates, alkali tweezer arrays and alkaline-earth arrays — providing lasers and vacuum to ions, tweezers to both atom families, clock lasers to alkaline earths and cavities to the atom–photon link. It requires nothing upstream, replaces nothing and conflicts with nothing: a hub in economic terms, invisible in architectural ones. It sets no derived clock but bounds every path's through laser-lock, imaging and rearrangement time — imaging alone is 0.5–1 ms of a 1–4.5 ms atom cycle. No empty slot is flagged.

## Verification (QCVV)
The reload-rate conflict is resolved above; the graph's bare "300,000 atoms/s" is right but mislabelled [D][2]. Pasqal's power and mass carry a company-claim tag, not a measurement tag [C][1]. TOPTICA's revenue and headcount are corroborated by its own page [C][6]; "dominant supplier" rests on one secondary source [P][8].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| TOPTICA Photonics | supplier | Germany | Lasers for ion and atom platforms; EUR 140 M revenue, 600 staff | [C][6] |
| AA Opto-Electronic | supplier | France | Crossed DTSX-400 AODs in the 448-atom system | [P][9] |
| Gooch & Housego | supplier | UK | Deflectors in the 3,000- and 6,100-atom papers | [P][9] |
| Atlas Copco (Edwards, Leybold) | supplier | Sweden | MoU to industrialise high-vacuum systems | [P][7] |
| Pasqal | user | France | Orion Gamma rack: 3 kW, 2,500 kg, room temperature | [C][1] |
| Harvard with QuEra | user | US | Conveyor reload holding >3,000 atoms >2 h | [D][2] |
| Quantinuum | user | US-UK | Helios: ≥7 wavelengths over 1,228 electrodes | [D][11] |

**Money.**
- 2022-11-02 · Universal Quantum · government contract · EUR 67 M · DLR · closed [P][17]
- 2023-12-05 · Alpine Quantum Technologies · system sale to Leibniz Supercomputing Centre · ≈EUR 9.8 M for 20 qubits · closed [C][13]
- 2026-06 · Atom Computing · equity plus CHIPS letter of intent · >USD 300 M incl. USD 100 M LOI · closed [C][15]
- 2026-08-28 · Pasqal · SPAC completion · ~USD 360 M cash, EUR 16.5 M 2025 revenue · closed [P][10]

**Market & supply chain.** The only manufacturing tier serving two platform families, so its vendors are indifferent to which wins. Unit economics differ by two orders at the two ends: QuNorth ordered the 1,225-physical, 50-logical Magne system from Atom Computing and Microsoft for EUR 80 M, ~EUR 65 k per atom [P][16], while AQT delivered 20 trapped ions for EUR 9.8 M, ~EUR 0.5 M per ion [C][13]. Tweezer optics amortise across thousands of sites; ion optics scale closer to per-ion. All of G1–G7 pays for this tier.

**IP & standards.** No dated patent-family fact specific to laser, vacuum or objective IP was found as of 2026-09-04. No standards body covers this tier; vacuum-flange, laser-safety and optical-mount standards predate quantum computing — the components are commodity, the integration is not.

**Roadmaps & track record.** Universal Quantum (promised 2022-11 · two computers for DLR within four years · no delivery as of 2026-09-04) [P][17] — weak. Pasqal (promised 2024-03 · 10,000 physical in 2026 · slipped to 2028) [R][20]. QuEra (promised 2024-01 · 100 logical in 2026 · replaced by Libra in 2028) [R][19]. The supplier side publishes no checkable roadmap.

**Strategic reading.** Suppliers here hold bargaining power no carrier- or gate-specific vendor has: a bet on TOPTICA or Atlas Copco is a bet on both ions and atoms. The threat is not a competitor but a change of form factor — if photonic-integrated delivery arrives, value migrates to PIC foundries and the AOD duopoly is the exposed link. Builders integrating optics in-house trade cost for control; outsourcers trade control for a supplier's industrialisation budget.

*Open niche:* a small QCVV house could quantify this tier's coherent-error contribution — laser drift, pointing noise, pressure fluctuation — as a transfer function into gate infidelity across vendor combinations, which nobody currently publishes.

## Outlook & open questions
Falsifiable in 12–24 months: confirm/demote that Universal Quantum and Atlas Copco ship a vacuum system past MoU stage; that a second laser vendor is named in a production ion system; that any array beats the ~10 MHz rearrangement assessment. Best case by 2029: photonic-integrated delivery removes pointing sensitivity and per-site optics cost falls. Worst case: supply stays concentrated and this tier's coherent error stays the dominant infidelity term. Open: does anyone displace TOPTICA; do objectives get a named merchant vendor; does the ion-versus-atom unit-cost gap persist.

## Sources
[1] Pasqal, Orion quantum-computing processor brochure (Orion Gamma: 3 kW average, 2,500 kg) · company brochure · 2025-11 · https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf — [C]
[2] Chiu, Ji, Bluvstein et al. (Harvard, MIT, QuEra), "Continuous operation of a coherent 3,000-qubit system" · Nature · 2025 · https://www.nature.com/articles/s41586-025-09596-6 — [D]
[3] Caltech, 6,100-atom tweezer array with 12.6 s coherence · arXiv:2403.12021 · 2024-03 · https://arxiv.org/abs/2403.12021 — [D]
[4] Tsinghua, 11,000 atoms in 18,225 metasurface tweezers · arXiv:2606.02715 · 2026-06 · https://arxiv.org/abs/2606.02715 — [D]
[5] Bluvstein et al. (Harvard, MIT, QuEra), 448-atom fault-tolerant architecture with atom-loss detection · Nature · 2025-11 · https://www.nature.com/articles/s41586-025-09848-5 — [D]
[6] TOPTICA Photonics, company page (EUR 140 M revenue, 600 employees, quantum technology as founding market) · company page · accessed 2026-09-04 · https://www.toptica.com/company — [C]
[7] Quantum Computing Report, "Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers" · trade press · 2025-12-18 · https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ — [P]
[8] postquantum.com, "The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins" · trade analysis · 2026 · https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ — [P]
[9] Gooch & Housego, acousto-optic deflectors in the Nature neutral-atom papers (with AA Opto-Electronic DTSX-400 crossed AODs in the 448-atom system) · company news · 2026 · https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers — [P]
[10] The Quantum Insider, "Pasqal Completes SPAC Merger with $360 Million in Cash" · trade press · 2026-08-28 · https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ — [P]
[11] Quantinuum, "Helios" 98-qubit trapped-ion processor · arXiv:2511.05465 · 2025-11 · https://arxiv.org/abs/2511.05465 — [D]
[12] Infineon Technologies, trapped-ion QPU platform (Villach, 6–12-inch traps) · product page · accessed 2026-09-04 · https://www.infineon.com/promo/trapped-ions — [C]
[13] Alpine Quantum Technologies, "AQT lands million-euro contract" — 20-qubit system for the Leibniz Supercomputing Centre, ≈EUR 9.8 M · company newsroom · 2023-12-05 · https://www.aqt.eu/aqt-lands-million-euro-contract/ — [C]
[14] Infleqtion, "Infleqtion Becomes First Neutral Atom Quantum Company to Go Public" · press release · 2026-02 · https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ — [C]
[15] Atom Computing, "Atom Computing Raises More Than $300 Million" · press release · 2026-06 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html — [C]
[16] Quantum Computing Report, "Denmark's QuNorth to Acquire 50 Logical Qubit Magne Quantum Computer from Atom Computing and Microsoft" · trade press · 2026 · https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ — [P]
[17] University of Sussex, Universal Quantum DLR contract announcement (EUR 67 M) · university newsroom · 2022-11-02 · https://www.sussex.ac.uk/broadcast/read/59206 — [P]
[18] US Bureau of Industry and Security, "Implementation of Additional Export Controls: Certain Advanced Computing Items; Quantum Computing Items" (ECCN 4A906) · Federal Register interim final rule · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and — [G]
[19] QuEra, "QuEra Announces 2028 Fault-Tolerant Quantum Computer" (Libra) · press release · 2026 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws — [R]
[20] Pasqal, 2025 roadmap release (10,000 physical qubits slipped from 2026 to 2028) · company newsroom · 2025 · https://www.pasqal.com/newsroom/pasqal-releases-2025-roadmap/ — [R]

## Open verification items
The 30,000-versus-300,000 atoms/s discrepancy is resolved: the abstract of [2] states a reloading rate of 300,000 atoms into tweezers per second, from which over 30,000 initialised qubits per second are created, sustaining an array of over 3,000 atoms for more than two hours; the graph's node description should read "reload 300,000 atoms/s into tweezers, 30,000 initialised qubits/s", and the transport is by two optical-lattice conveyor belts, not AODs. The ~10 MHz SLM/AOD refresh ceiling above ~10⁴ qubits is carried from the main report's bottleneck assessment; no primary measurement was located. TOPTICA's "dominant supplier" position rests on one secondary source [8], though its revenue and headcount are now confirmed on the company's own page [6]. No dated fact naming a high-numerical-aperture objective vendor for either platform family was found. The AOD supplier list is verified by absence — only two vendors appear across the sourced literature, which is not the same as only two existing.
