---
id: ct_sfq
name: SFQ digital control (millikelvin)
layer: "5 Control"
status: emerging
since: 2026
one_line: "Quantised flux pulses from a niobium digital chip flip-chipped onto the qubit die drive gates at millikelvin, replacing per-qubit microwave coax."
verdict: "Real: one five-qubit module at 1Q > 99%. Unproven: two-qubit gates, readout, flux bias, quasiparticle immunity beyond five qubits. Demote if no >20-qubit SFQ module by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

Single-flux-quantum logic holds a bit as one flux quantum Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb in a superconducting loop; a junction undergoing a 2π phase slip emits a pulse of quantised area Φ₀, about 1 mV for 2 ps. RSFQ (Likharev & Semenov, 1991) was built for classical computing at 4 K. The control use is younger: a pulse train locked to a multiple of the qubit period adds coherently into a Rabi rotation — proposed by McDermott and Vavilov in 2014 [S][1], first shown on a transmon at ≈ 95% by Leonard et al. [D][2]. The 2026 node is not merely cold classical logic: the control instrument sits on the mixing-chamber plate, flip-chipped to the qubits, so synthesis, timing and fan-out happen at 10 mK, not 300 K [D][3]. This brief covers the qubit-control node only; the wider family — RSFQ, ERSFQ/eSFQ, RQL, AQFP, DSFQ, their foundries, design flows and non-quantum markets — is tracked in the author's Superconductor Electronics Monitor [P][4].

Attributes. **Carrier affinity:** fully fabricated — a control layer bonded to a carrier, not a carrier. **Time / entangling:** not applicable. **Readout:** none demonstrated [C][5]. **Mobility:** none, bump-bonded. **Control modality @ placement:** microwave drive synthesised digitally *at millikelvin*, the defining attribute. **Error structure as the code sees it:** Pauli plus a correlated non-Pauli component from photon-mediated quasiparticle poisoning [D][6]. **Manufacturing:** multi-layer niobium lithography.

## Physics & limits

A Φ₀ kick delivers a fixed, calibration-free phase increment, so gate amplitude is set by pulse *count*, not analogue amplitude — hence immunity to the drift and IQ imbalance of room-temperature chains. Each switching event costs of order I_cΦ₀ ≈ 10⁻¹⁹ J, and resistively shunted RSFQ also burns static bias power; the mixing-chamber budget is tens of µW at 20 mK (a KIDE-class platform quotes > 3 mW only at 100 mK) [C][G:BLUEFORS-KIDE], so switching energy is not binding — bias distribution and the Josephson transmission lines are.

The floor is pair-breaking. A switching junction radiates photons above the gap (2Δ ≈ 90 GHz in aluminium); these break Cooper pairs in the qubit film, giving T₁ decay and correlated bursts no Pauli-channel decoder models. Liu et al. quantified it: with the driver on a separate chip joined by indium bumps, error per Clifford was 1.2(1)%, of which 0.96(2)% was incoherent and attributed to photon-mediated quasiparticle poisoning through the module's resonant millimetre-wave antenna modes [D][6]. Their fix is unexotic — limit the driver's pulse bandwidth — projecting 0.1% for resonant and 0.01% for complex sequences [D][6]. What moves the floor: gap engineering, quasiparticle traps, millimetre-wave absorbers, and bias-resistor-free families (ERSFQ/eSFQ, adiabatic quantum-flux-parametron).

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: SEEQC's five-qubit processor with SFQ control in the same flip-chip module at 10 mK, single-qubit fidelity above 99% with peaks at 99.9%, one digital input demultiplexed to several qubits [D][3][C][5]. There is no "typical at scale": every SFQ result is ≤ 5 qubits, and none has driven a two-qubit gate or run a QEC cycle.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2014 | Resonant SFQ pulse-train control proposed | McDermott & Vavilov | [S][1] |
| 2014 | 4,544 on-chip flux DACs for 512 qubits via 56 wires | D-Wave | [D][7] |
| 2019 | First SFQ single-qubit gate on a transmon, ≈ 95% | Wisconsin / Syracuse | [D][2] |
| 2023 | Separate-die driver: 1.2(1)% error/Clifford, 0.96(2)% from poisoning | Wisconsin, Syracuse, NIST | [D][6] |
| 2024 | Multiplexed adiabatic-logic controller at 4.2 K, ~1,000× signals per cable | AIST, Yokohama NU, NEC | [C][8] |
| 2026-03 | Five qubits + SFQ control at 10 mK; 1Q > 99%, peak 99.9% | SEEQC | [D][3] |
| 2026-03 | Fluxon time-delay readout in a Josephson transmission line | preprint | [S][9] |

Dominant error term: quasiparticle poisoning at ~80% of the 2023 module's total; in SEEQC's module, undisclosed — the paper reports fidelity, not a decomposition.

## Manufacturing, materials & supply chain

The control die is multi-layer Nb/AlOx/Nb — eight or more planarised niobium layers, 10⁴–10⁶ junctions — a different flow from the two- or three-layer aluminium-on-silicon qubit process, so this node's supply chain is not the qubit supply chain [D][10]. Sources are few and mostly non-commercial: MIT Lincoln Laboratory's superconducting-digital line (SFQ5ee family) and its SQUILL qubit foundry, now on 200 mm wafers with > 400 devices delivered [C][11]; AIST's niobium node, whose RSFQ and adiabatic-logic cell libraries run at 1 kA/cm² [D][12]; and SEEQC, owner of one of the very few *commercial* multi-layer superconductor foundries, in Elmsford, New York, with sites in London and Naples [C][13]. Yield risk: margins need junction critical-current spreads of a few per cent across thousands of junctions. The only dated cryogenic figure is ~1.6 µW per qubit for SFQ against 23 mW/qubit for 4 K cryo-CMOS driving a two-qubit gate [S][14][G:CRYOCMOS-POWER-CONFLICT]. Export exposure is asymmetric: the BIS rule of 2024-09-06 created ECCN 3A901.a for **CMOS** circuits designed for ≤ 4.5 K, a design-intent test that captures cryo-CMOS design files but, read literally, not niobium SFQ — exposed instead through 3A904, 3B904 and 4A906 [G][15]. Single points of failure: dilution refrigerators, indium-bump bonding, niobium sputter and CMP tooling.

## Control, readout & I/O burden

Transmons run roughly one drive coax plus one flux line per qubit; a KIDE-class platform advertises > 4,000 RF lines for "over 1000 qubits" [C][G:BLUEFORS-KIDE], already the ceiling of coax-per-qubit. SFQ substitutes a clock plus a low-rate instruction stream [D][3]; D-Wave's flux DACs are the existence proof at the other end of the same idea — 4,544 on-chip converters programmed through 56 wires with zero static dissipation [D][7]. At 10³ qubits coax is workable; at 10⁴ it fails on fridge cross-section and heat load; at 10⁶ only in-fridge digital fan-out closes. Latency is the second prize: real-time decoding at d = 5 costs 63 µs round trip [D][16], and a co-located decoder removes the cable and the 300 K hop. SFQ does not yet touch readout — the fluxon scheme is a preprint with no reported fidelity [S][9] — nor flux bias, which SEEQC lists as future work [C][5].

## Role in the stack

Path: superconducting transmon (Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu). It requires superconducting-qubit lithography plus a flip-chip module flow, and provides the cold digital substrate a cryogenic on-chip decoder would sit on. D-Wave's on-chip flux DACs require it in the literal sense — each DAC is an SFQ flux-storage loop loaded one flux quantum at a time [D][7] — the node's only dependency from a second carrier family (annealing), and what makes it a transfer hub. It replaces room-temperature control racks and competes with 4 K cryo-CMOS — a substitution with a price, since cryo-CMOS reuses commercial foundries, EDA and verification whereas SFQ needs a niobium ecosystem whose design tools are commercial only at the physical-verification level (extraction, LVS, DRC) and academic above RTL — no licensable system-level flow exists. It conflicts with the transmon itself: the switching photons that make SFQ fast are the photons that poison the qubit. The off-diagonal reading is cold fabrication — a manufacturing answer to a control problem, which is why the leading actor is a foundry owner, not an instrument vendor. Contribution to the derived clock (sum of the syndrome round: gate layers + transport + readout + reset): neutral — gates stay at tens of nanoseconds, so the round stays at **0.65 µs**, readout its largest term, against the measured **1.1 µs** QEC cycle [D][16]. Neighbouring empty slots: SFQ flux bias for gate-model transmons (the annealer DAC exists), SFQ readout, a cryogenic decoder fed by SFQ syndrome traffic.

## Verification (QCVV)

Every headline number is a randomised-benchmarking Clifford average [D][2][D][6][D][3]. RB is the wrong instrument for this node's characteristic failure: quasiparticle bursts are rare, correlated and non-Markovian, while RB assumes a Markovian gate-independent channel and averages bursts into a slightly worse mean — so a module can pass at 99.9% and still produce correlated multi-qubit errors that break a surface-code decoder. The 2023 paper separated coherent from incoherent error [D][6]; the 2026 claim of "absence of detectable quasiparticle poisoning" reaches us only through press coverage [C][5]. Missing everywhere: charge-parity monitoring under continuous clocking, T₁ with the clock on versus off, any QEC-level measurement. No independent replication exists — the 2026 author list is entirely Seeqc [D][3]. Conflicts: the abstract says "exceeding 99%" [D][3], press coverage "exceeding 99.5%" [C][5] (trust the abstract); and "nanowatts per qubit" [C][5] against ~1.6 µW/qubit [S][14], three orders apart.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| SEEQC | developer / supplier | US | The mK SFQ control module; owns a commercial Nb foundry | [D][3][C][13] |
| IBM | user / integrator | US | SFQ integration with SEEQC under QBI; also hedging with cryo-CMOS | [P][17][C][18] |
| Hypres | IP predecessor | US | SEEQC's 2019 spin-out parent; > $100 M of prior SFQ investment | [C][13] |
| Univ. of Wisconsin–Madison | research | US | Originated resonant SFQ control; leads poisoning studies | [S][1][D][6] |
| Syracuse University | research | US | Qubit fabrication and diagnostics for the multi-chip work | [D][6] |
| NIST Boulder | research / supplier | US | Niobium SFQ fabrication and metrology | [D][6] |
| MIT Lincoln Laboratory | supplier (foundry) | US | SFQ5ee digital process; SQUILL qubit foundry | [C][11] |
| D-Wave | developer (adjacent) | CA | On-chip flux DACs replacing control wires | [D][7] |
| AIST | research / foundry | JP | Nb RSFQ and adiabatic-logic cell libraries | [D][12] |
| NEC | research | JP | 4.2 K multiplexed qubit controller with AIST | [C][8] |
| DARPA | programme sponsor | US | QBI; SEEQC participates via IBM, not as a performer | [G][19] |
| IonQ | supplier (contested) | US | Owns SkyWater, named in D-Wave's 10-K filings | [C][20][G][21] |

**Money.**
- 2020-09-16 · SEEQC · Series A · $22.4 M · EQT Ventures (lead), FAM AB, M Ventures ($5 M) · cumulative > $29 M · closed [C][13]
- 2025-01-16 · SEEQC · growth round · $30 M · SIP Global, NordicNinja, Booz Allen Ventures, no named lead · closed [P][22]
- 2025-06-12 · SEEQC + IBM · SFQ integration under DARPA QBI · undisclosed · IBM the named performer · announced [P][17][G:SEEQC-2026]
- 2026-06-29 · SEEQC · S-1 for a conventional Nasdaq IPO (SEQC), filed in parallel with the Allegro Merger Corp SPAC agreement ($1 B enterprise value, $65 M PIPE) · offering size not set · filed [P][23][G:SEEQC-S1-2026-07]
- 2026-08-25 · SEEQC / Allegro Merger Corp · SPAC merger terminated by settlement; Allegro receives up to $2 M of expenses plus $6 M in stock at a $1.3 B pre-money valuation on a future IPO, acquisition or ≥ $100 M raise · terminated [G][24]
- 2026-07-31 · IonQ / SkyWater · M&A · ~$1.8 B · closed [C][20][G:IONQ-SKYWATER-2026]

**Market & supply chain.** No SFQ control market exists — one vendor, one demonstration, an IPO in registration. Concentration is upstream: niobium sputter and CMP tooling, indium-bump bonders, dilution refrigerators. Outside SEEQC's line, Western superconducting-digital capacity is essentially Lincoln Laboratory [C][11], and the merchant option most visible in SEC filings, SkyWater, now belongs to IonQ [C][20][G][21]. Only G3 and G4 pay for this; G7 is secondary, G1/G2/G5 pay nothing.

**IP & standards.** SEEQC's position rests on the Hypres portfolio of RSFQ circuit and niobium process patents transferred in 2019 [C][13]; no dated patent-family count was obtained. No SFQ-for-control standards exist; the nearest shared design base is AIST's cell library [D][12] and MIT-LL's design kits [C][11].

**Roadmaps & track record.** SEEQC: millikelvin SFQ control (promised 2021–22 · as chip-scale control · delivered 2026-03 at five qubits) [D][3]; on-die digital flux control and readout (promised 2026-03 · no date · not delivered) [C][5]; listing (promised 2026-06 · for 2026 · S-1 in registration; SPAC route abandoned 2026-08-25) [P][23]. It shipped the hard physics four to five years late and never at scale — take its fidelity claims seriously, its scaling claims sceptically. IBM: SFQ is a hedge beside cryo-CMOS, its control-electronics promises holding better than its module promises [G:IBM-ROADMAP-2022]. D-Wave: a decade of shipped on-chip digital control, for annealers [D][7].

**Strategic reading.** Winners: owners of niobium process capability — SEEQC and, via Lincoln Laboratory, the US government — plus whichever transmon vendor integrates first, most plausibly IBM. Losers: room-temperature control vendors, whose per-qubit revenue disappears into a bonded die. The substitution leads on evidence: cryo-CMOS has a full QEC demonstration [D][25] and fleet-scale parity data [C][18]; SFQ has five qubits and no two-qubit gate. Supplier power holds only while the supplier is also the only foundry.

*Open niche:* a small QCVV/SFQ research company plugs in where this brief keeps returning — nobody measures SFQ-controlled qubits with protocols that see the failure mode. Concretely: charge-parity and correlated-error spectroscopy with the clock gated on and off; burst-aware benchmarking reporting the tail, not the RB mean; and an independent replication path. That needs a fridge, not a foundry, and yields what no vendor publishes: correlated error rate per unit clock time.

## Outlook & open questions

Confirm if by end-2027 a group publishes an SFQ-driven two-qubit gate below 1% error, an SFQ-controlled device above ten qubits, or a charge-parity measurement showing no clock-correlated bursts over hours. Demote if by end-2028 no SFQ module above twenty qubits exists, or a published decomposition shows poisoning above 0.1% per Clifford. Best case by 2029: SFQ control plus SFQ flux bias in an IBM or SEEQC module at the 10²-qubit scale, decoder co-located. Worst case: cryo-CMOS wins on ecosystem economics and SFQ survives only as D-Wave-style flux DACs. Open questions: (1) does "no detectable quasiparticle poisoning" survive continuous clocking at QEC duty cycles? (2) Can SFQ flux bias hold the DC stability transmons need? (3) Who fabricates SFQ wafers at volume if SEEQC's line saturates and SkyWater sits inside IonQ? Watch: SEEQC's S-1 disclosures, any two-qubit SFQ preprint, the next QBI roster.

## Sources

[1] R. McDermott and M. G. Vavilov, “Accurate Qubit Control with Single Flux Quantum Pulses,” *Phys. Rev. Appl.*, vol. 2, no. 1, Art. no. 014007, Jul. 2014, doi: [10.1103/PhysRevApplied.2.014007](https://doi.org/10.1103/PhysRevApplied.2.014007). [S]
[2] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[3] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[4] R. Neeman, “Superconductor Electronics Monitor 2026,” Qodeh, Sep. 2026, doi: [10.5281/zenodo.21860767](https://doi.org/10.5281/zenodo.21860767). [P]
[5] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [P]
[6] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[7] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[8] AIST; Yokohama National University; Tohoku University; NEC, “Successful demonstration of a superconducting circuit for qubit control within large-scale quantum computer systems,” NEC Press Releases, Jun. 3, 2024. [Online]. Available: https://www.nec.com/en/press/202406/global_20240603_02.html [C]
[9] S. Kamimura, A. Taguchi, M. Tanaka, and T. Yamamoto, “Fluxon Time-Delay Readout of a Superconducting Qubit Protected by a Spectral Gap in a Josephson Transmission Line,” [arXiv:2603.13175](https://arxiv.org/abs/2603.13175), Mar. 2026. [S]
[10] S. K. Tolpygo, “Superconductor Digital Electronics: Scalability and Energy Efficiency Issues,” [arXiv:1602.03546](https://arxiv.org/abs/1602.03546), Feb. 2016. [D]
[11] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[12] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[13] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[14] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[15] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[16] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[17] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [P]
[18] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[19] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[20] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[21] U.S. Securities and Exchange Commission, “EDGAR full-text search: ‘SkyWater’ in D-Wave Quantum Inc. 10-K filings,” SEC EDGAR Full-Text Search, Feb. 26, 2026. [Online]. Available: https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982 [G]
[22] SIP Global Partners, “SIP Global Partners Participates in $30M Round for SEEQC, Developer of the World's First Full-Stack Processor for Quantum Computers,” PRWeb, Jan. 16, 2025. [Online]. Available: https://www.prweb.com/releases/sip-global-partners-participates-in-30m-round-for-seeqc-developer-of-the-worlds-first-full-stack-processor-for-quantum-computers-302352970.html [P]
[23] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [P]
[24] Allegro Merger Corp.; SeeQC, Inc., “Settlement, Termination and Release Agreement,” U.S. Securities and Exchange Commission (EDGAR), Aug. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1779977/000121390026095175/ea028847004ex2-2.htm [G]
[25] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]

## Open verification items

- Fidelity conflict: abstract "exceeding 99%" [3] versus press "exceeding 99.5%" [5]; main text paywalled.
- Five-qubit count, 10 mK and "nanowatts per qubit" come from press coverage [5], not the abstract [3].
- Power conflict: nanowatts per qubit [5] versus ~1.6 µW/qubit [14].
- Reference [1] and Likharev & Semenov (1991) are cited from the standard literature.
- MIT-LL SFQ5ee process parameters not obtained; [11] covers the qubit foundry only.
- No dated 2025–26 Chinese SFQ qubit-control result surfaced; SIMIT and Nanjing activity unverified.
- No dated patent-family count for SFQ qubit control from a named database.
- SEEQC revenue, cash and offering size undisclosed in [23]; enterprise value from trade press.
- SkyWater's superconducting capability inferred from D-Wave 10-K mentions [21].
