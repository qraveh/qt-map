---
id: ct_sfq
name: SFQ digital control (millikelvin)
layer: "5 Control"
status: emerging
since: 2026
one_line: "Quantised flux pulses from a niobium digital chip flip-chipped onto the qubit die drive gates at millikelvin, replacing per-qubit microwave coax."
verdict: "Real: one five-qubit module at 1Q > 99%. Unproven: two-qubit gates, readout, flux bias, quasiparticle immunity beyond five qubits. Demote if no >20-qubit SFQ module by 2028."
updated: 2026-09-30
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

Single-flux-quantum (SFQ) logic stores a bit as one flux quantum Φ₀ = h/2e in a superconducting loop; a switching junction emits a pulse of area Φ₀, about 1 mV for 2 ps. Its rapid form (RSFQ; Likharev & Semenov, 1991) was built for classical computing at 4 K. For qubit control, a pulse train locked to the qubit period adds coherently into a Rabi rotation [S][565]. In the 2026 form the controller is flip-chipped to the qubits at 10 mK [D][304]. The wider superconductor-electronics field is tracked in the Superconductor Electronics Monitor [P][56].

Attributes. **Carrier affinity:** fully fabricated control layer. **Time / entangling:** not applicable. **Readout:** none demonstrated [C][53]. **Mobility:** none, bump-bonded. **Control modality @ placement:** microwave drive synthesised digitally *at millikelvin*. **Error structure as the code sees it:** Pauli plus correlated poisoning bursts [D][249]. **Manufacturing:** multi-layer niobium lithography.

## Physics & limits

Each Φ₀ pulse gives the qubit a fixed phase kick, so gate angle is set by pulse *count*, not analogue amplitude. Switching costs only ~I_cΦ₀ ≈ 10⁻¹⁹ J per event; within a mixing-chamber budget of tens of µW at 20 mK, RSFQ's static bias power and bias distribution bind first.

The floor is pair-breaking: switching junctions radiate photons above the aluminium gap (2Δ ≈ 90 GHz) that break Cooper pairs in the qubit film — quasiparticle poisoning — causing T₁ decay and correlated bursts. Limiting the driver's pulse bandwidth is projected to remove it, bringing gate error toward 0.1% for resonant sequences [D][249]. Other levers: quasiparticle traps, gap engineering, millimetre-wave absorbers.

## Engineering state of the art

Best demonstrated (3 Sep 2026): SEEQC's five-qubit module at 10 mK, single-qubit fidelity above 99%, one digital input demultiplexed to several qubits [D][304][C][53]. No SFQ result exceeds five qubits or includes a two-qubit gate or a QEC cycle.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2014 | 4,544 on-chip flux DACs for 512 qubits via 56 wires | D-Wave | [D][430] |
| 2019 | First SFQ gate on a transmon, ≈ 95% | Wisconsin / Syracuse | [D][566] |
| 2023 | Separate-die driver: 1.2(1)% error/Clifford, 0.96(2)% from poisoning | Wisconsin, Syracuse, NIST | [D][249] |
| 2026-03 | Five qubits, SFQ control at 10 mK; 1Q > 99%, peak 99.9% | SEEQC | [D][304] |
| 2026-03 | Fluxon time-delay readout, no fidelity reported | preprint | [S][568] |

Dominant error term: quasiparticle poisoning in the 2023 module [D][249]; undisclosed for SEEQC's.

## Manufacturing, materials & supply chain

The control die is multi-layer Nb/AlOx/Nb — eight or more planarised niobium layers, 10⁴–10⁶ junctions — unlike the aluminium qubit process [D][569]. Foundries are few: MIT Lincoln Laboratory (SFQ5ee line, SQUILL qubit foundry) [C][570], AIST's niobium process and cell libraries [D][571], and SEEQC's commercial foundry in Elmsford, NY [C][572]. Yield needs critical-current spreads of a few per cent across thousands of junctions. Export exposure (BIS rule of 2024-09-06): ECCNs 3A904, 3B904 and 4A906; 3A901.a, read literally, covers cryogenic CMOS only [G][301]. Single points of failure: dilution refrigerators, indium-bump bonding, niobium sputter and CMP tools.

## Control, readout & I/O burden

Room-temperature control needs about one drive coax and one flux line per transmon, so fridge cross-section and heat load set its limit; a KIDE-class platform offers > 4,000 RF lines for "over 1000 qubits" [C][G:BLUEFORS-KIDE]. SFQ control needs a clock plus a low-rate instruction stream [D][304]. SFQ readout exists only as a preprint scheme [S][568]; SEEQC lists flux bias as future work [C][53].

## Role in the stack

Architecture: the superconducting transmon lattice. It requires superconducting-qubit lithography and flip-chip modules; it provides cold digital logic for a cryogenic decoder and D-Wave's flux DACs [D][430]. The cold routes for control are cryo-CMOS or SFQ: cryo-CMOS reuses commercial foundries and design tools; SFQ needs a niobium ecosystem whose commercial tools stop at physical verification. The conflict with the transmon — switching photons poisoning the qubit — is open: its mitigation is projected [D][249], and SEEQC's 2026 report of no detectable poisoning is press coverage [C][53]. Contribution to the derived clock: neutral — the syndrome round stays at **0.65 µs** against the measured **1.1 µs** QEC cycle [D][1]. Neighbouring empty slots: SFQ flux bias, SFQ readout.

## Evidence — how the numbers were measured

Every headline number is a randomised-benchmarking (RB) Clifford average [D][566][D][249][D][304]. RB assumes Markovian, gate-independent errors, so rare correlated bursts average into a slightly worse mean, and a module can pass at 99.9% yet emit correlated errors that decoders do not model. SEEQC's "absence of detectable quasiparticle poisoning" is reported only in press [C][53]. Not reported: charge parity under continuous clocking, T₁ with the clock on and off. No independent replication: the 2026 authors are all from SEEQC [D][304]. Conflicts: "exceeding 99%" in the abstract [D][304] against "exceeding 99.5%" in press [C][53]; "nanowatts per qubit" [C][53] against ~1.6 µW per qubit in a 2026 estimate [S][550][G:CRYOCMOS-POWER-CONFLICT].

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| SEEQC | developer / foundry | US | mK SFQ control module; commercial Nb foundry | [D][304][C][572] |
| IBM | integrator | US | SFQ integration with SEEQC (QBI); own cryo-CMOS control | [P][54][C][527] |
| Wisconsin–Madison, Syracuse, NIST Boulder | research | US | Resonant SFQ control; poisoning study | [S][565][D][249] |
| MIT Lincoln Laboratory | foundry | US | SFQ5ee process; SQUILL qubit foundry | [C][570] |
| D-Wave | developer (adjacent) | CA | On-chip SFQ flux DACs in annealers | [D][430] |
| AIST, NEC | research / foundry | JP | Nb cell libraries; 4.2 K multiplexed controller | [D][571][C][567] |

**Money.**
- 2020-09-16 · SEEQC · Series A · $22.4 M · EQT Ventures (lead) · closed [C][572]
- 2025-01-16 · SEEQC · growth round · $30 M · SIP Global and others · closed [P][573]
- 2025-06-12 · SEEQC + IBM · SFQ integration under DARPA QBI, IBM the performer [G][65] · undisclosed · announced [P][54][G:SEEQC-2026]
- 2026-06-29 · SEEQC · S-1 for a Nasdaq IPO, alongside an Allegro Merger Corp SPAC agreement ($1 B enterprise value) · filed [C][556][G:SEEQC-S1-2026-07]
- 2026-08-25 · SEEQC / Allegro · SPAC merger ended by settlement: Allegro gets $6 M in stock at a $1.3 B pre-money valuation on a future IPO, sale or ≥ $100 M raise · terminated [G][574]

**Market & supply chain.** No SFQ control market exists yet: one vendor, one demonstration. SkyWater, the merchant foundry named in D-Wave's 10-K filings [G][492], has belonged to IonQ since July 2026 [C][19]. G3 and G4 pay for it; G7 secondarily.

**IP & standards.** SEEQC holds the Hypres RSFQ and niobium-process patents, transferred at its 2019 spin-out [C][572]. No SFQ-control standards exist; shared design bases are AIST's cell library [D][571] and MIT-LL's kits [C][570].

**Roadmaps & track record.** SEEQC: millikelvin SFQ control (promised 2021–22 · delivered 2026-03 at five qubits) [D][304]; on-die flux control and readout (announced 2026-03 · undated) [C][53].

**Strategic reading.** Niobium process capability sits with SEEQC and, via Lincoln Laboratory, the US government. Of the cold routes, cryo-CMOS or SFQ, cryo-CMOS has the stronger record: a QEC demonstration under a 4 K cryo-CMOS controller [D][190] and parity with warm electronics on an IBM processor [C][527]; SFQ has single-qubit gates on five qubits from one group [D][304].

## Outlook & open questions

Confirm if by end-2027 a group publishes an SFQ-driven two-qubit gate below 1% error, an SFQ-controlled device above ten qubits, or hours of charge-parity data free of clock-correlated bursts. Demote if by end-2028 no SFQ module exceeds twenty qubits, or a decomposition shows poisoning above 0.1% per Clifford. Open questions: does "no detectable poisoning" survive continuous clocking at QEC duty cycles? Can SFQ flux bias hold the DC stability transmons need?

## References
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[53] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [C]
[54] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [P]
[56] R. Neeman, “Superconductor Electronics Monitor,” Qodeh, 2026, doi: [10.5281/zenodo.21860767](https://doi.org/10.5281/zenodo.21860767). [Online]. Available: https://qodeh.com/publications/superconductor-electronics-monitor-2026/ [P]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[492] U.S. Securities and Exchange Commission, “EDGAR full-text search: ‘SkyWater’ in D-Wave Quantum Inc. 10-K filings,” SEC EDGAR Full-Text Search, Feb. 26, 2026. [Online]. Available: https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982 [G]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[556] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [C]
[565] R. McDermott and M. G. Vavilov, “Accurate Qubit Control with Single Flux Quantum Pulses,” *Phys. Rev. Appl.*, vol. 2, no. 1, Art. no. 014007, Jul. 2014, doi: [10.1103/PhysRevApplied.2.014007](https://doi.org/10.1103/PhysRevApplied.2.014007). [S]
[566] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[567] AIST; Yokohama National University; Tohoku University; NEC, “Successful demonstration of a superconducting circuit for qubit control within large-scale quantum computer systems,” NEC Press Releases, Jun. 3, 2024. [Online]. Available: https://www.nec.com/en/press/202406/global_20240603_02.html [C]
[568] S. Kamimura, A. Taguchi, M. Tanaka, and T. Yamamoto, “Fluxon Time-Delay Readout of a Superconducting Qubit Protected by a Spectral Gap in a Josephson Transmission Line,” [arXiv:2603.13175](https://arxiv.org/abs/2603.13175), Mar. 2026. [S]
[569] S. K. Tolpygo, “Superconductor Digital Electronics: Scalability and Energy Efficiency Issues,” [arXiv:1602.03546](https://arxiv.org/abs/1602.03546), Feb. 2016. [D]
[570] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[571] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[572] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[573] SIP Global Partners, “SIP Global Partners Participates in $30M Round for SEEQC, Developer of the World's First Full-Stack Processor for Quantum Computers,” PRWeb, Jan. 16, 2025. [Online]. Available: https://www.prweb.com/releases/sip-global-partners-participates-in-30m-round-for-seeqc-developer-of-the-worlds-first-full-stack-processor-for-quantum-computers-302352970.html [P]
[574] Allegro Merger Corp.; SeeQC, Inc., “Settlement, Termination and Release Agreement,” U.S. Securities and Exchange Commission (EDGAR), Aug. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1779977/000121390026095175/ea028847004ex2-2.htm [G]

## Open verification items

- Main text of [304] paywalled: five qubits, 10 mK and "nanowatts per qubit" come from press [53], not the abstract.
- MIT-LL SFQ5ee parameters not obtained; [570] covers the qubit foundry only.
- No dated 2025–26 Chinese SFQ qubit-control result found; no patent-family count.
- SEEQC's revenue and cash are in its S-1 filings — $4.2 M revenue in 2025, $18.1 M cash at 2026-06-30 [G:SEEQC-S1A-2026-08]; the offering size is still blank (S-1 amendment of 2026-09-11), and the enterprise value comes from trade press.
- SkyWater's superconducting capability inferred from D-Wave 10-K mentions [492].
