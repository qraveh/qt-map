---
id: ic_transducer
name: Microwave–optical transducer (useful efficiency)
layer: "9 Interconnect"
status: empty slot
since: "—"
one_line: "A quantum-coherent microwave-to-telecom converter good enough to entangle superconducting processors in separate refrigerators; nothing in 2026 comes close."
verdict: "No device combines efficiency above 50%, added noise well below one photon and MHz repetition; IBM's analysis puts the gap at three orders of magnitude on all three axes at once."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

The slot is a device converting an itinerant microwave photon at a transmon's frequency (4–10 GHz) into a telecom photon near 194 THz with the quantum state intact, and back, so two dilution refrigerators can be entangled over ordinary fibre instead of a cryogenic coaxial bridge. Three mechanisms compete, all parametric beam-splitter interactions driven by a strong optical pump: electro-optic in lithium niobate, piezo-optomechanical via a GHz phonon, and magneto-optic via a magnon in yttrium iron garnet. One quantity governs all three: cooperativity C = 4g²/κ₁κ₂ [1] — efficiency rises with C, input-referred added noise falls as N_add ∝ n_th/C. The line runs from cavity optomechanics of 2010–2013 to the first *quantum-enabled* microwave–optical interface, an electro-optic device at 60 mK with sub-photon added noise (2022, IST Austria) [D][1].

Attributes. **Carrier affinity:** fully fabricated — a lithographic cavity. **Characteristic time and determinism:** no gate time defined; entanglement through the link is heralded, never deterministic. **Readout:** none of its own. **Mobility:** flying — the carrier leaves the refrigerator. **Control at placement:** electro-optic, pumped optically at millikelvin. **Dominant error as the code sees it:** loss — heralded photon loss (erasure), plus pump-induced thermal photons creating false heralds. **Manufacturing:** photonic integrated circuit on superconducting resonators.

## Physics & limits

Everything hard here follows from one ratio: an optical photon is about 2×10⁴ times more energetic than a microwave one. A 1,550 nm photon carries 0.80 eV — roughly 9,300 K — and must be delivered in quantity to a stage whose cooling budget is a few hundred microwatts at 20 mK. Absorbed pump light breaks Cooper pairs and heats the phonon bath, and that heat reappears as thermal occupation in the mode carrying the qubit signal. Push the pump and efficiency rises together with added noise; back off and the device is quantum-limited but converts almost nothing. The trade shows up as duty cycle: the highest-efficiency electro-opto-mechanical device in the literature ran at 5,000 µs repetition and 0.22 kHz bandwidth [D][2].

The useful condition is η > 1/2 with N_add ≪ 1 [S][1], and the asymmetry matters: loss can be heralded away at the cost of rate, excess noise cannot be removed at all. The code therefore sees erasure plus a rate penalty when the device is good, and irreducible infidelity when it is not. What would move the floor: more nonlinearity per watt dissipated, superconductors tolerating pump light, and protocols that stop demanding determinism — the QphoX/IST claim that heralding plus distillation reaches >99% Bell fidelity with transducers that already exist [S][2], against IBM's calculation that 99.7% remote gates at MHz rates need "3 orders of magnitude in added noise, efficiency, and repetition rates" [S][3]. That disagreement is the live question.

## Engineering state of the art

Each record belongs to a different device; no two can be had at once.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018 | Total efficiency 47%, added noise far above one photon | Higginbotham et al., NIST/JILA | [D][1] |
| 2022 | Internal efficiency 99.5%, total 15%, added noise 0.16 photons at 60 mK, pulsed | Sahu et al., IST Austria | [D][1] |
| 2022 | Efficiency 0.38 at 5,000 µs repetition, 2.2×10⁻⁴ MHz bandwidth | Brubaker et al., JILA | [D][2] |
| 2024 | Total efficiency 3×10⁻⁶, ~10 µs repetition, 15 MHz bandwidth, 6 added photons | Weaver et al., QphoX | [D][2] |
| 2025-02 | Optical readout of a superconducting qubit through a transducer | QphoX, Rigetti, Qblox | [C][4] |
| 2025 | Added noise 0.12 photons at 30 MHz bandwidth (thin-film LiNbO₃) | Warner et al. | [D][1] |

| Quantity | Best demonstrated | Needed | Shortfall |
|---|---|---|---|
| Total efficiency | 15% pulsed [D][1]; 3×10⁻⁶ against a real qubit [D][2] | > 50% [S][1] | 3–5 orders |
| Added noise | 0.12–0.16 photons [D][1] | ≪ 1 | in isolation only |
| Repetition | 5.9–10 µs at low efficiency [D][2] | MHz, continuous | 1–3 orders |
| All three at once | none | — | 3 orders each [S][3] |

The dominant budget term is pump-induced heating — efficiency per microwatt of pump, the metric [2] argues should replace efficiency, because cooling capacity rather than conversion physics caps channel count.

## Manufacturing, materials & supply chain

Every published transducer is a single research die: no wafer-level yield or uniformity data for any platform as of 3 Sep 2026, and no foundry process of record. The candidate stacks — thin-film lithium niobate on insulator, silicon nitride, barium titanate, silicon optomechanical crystals — are the materials of the photonic-IC foundry slot this one requires, where 300-mm capability is proven for another purpose: PsiQuantum's Omega runs barium-titanate switches and superconducting nanowire detectors on GlobalFoundries 300 mm at median detector efficiency 93.4% [D][5]. Nobody has put a transducer on that route. Lithium-niobate substrates come from a small, largely Chinese supplier base, refrigerators with optical feedthroughs from Bluefors and Oxford Instruments; the binding constraint is cooling power at 20 mK, which nobody sells more of. Export exposure: the US Bureau of Industry and Security interim final rule of 2024-09-06 controls quantum computers, components and cryogenic equipment, but no ECCN names the transducer (mapping unverified below).

## Control, readout & I/O burden

Per channel: a pump fibre into the mixing chamber, a microwave line, a filter chain, and photon-counting or heterodyne detection. Fibre carries almost no static heat load — the load is the pump, tens of microwatts to milliwatts per channel against a few hundred microwatts of cooling at 20 mK. At 10³ channels that budget is exceeded by two to three orders unless efficiency per microwatt improves comparably; 10⁴ and 10⁶ are not discussable. Heralding needs a round trip to a mid-point detector at ~5 ns per metre, so a 10 m link costs ~100 ns against 6–10 µs repetition [D][2]: the transducer, not the speed of light, is the slow element.

## Role in the stack

The only path served is superconducting transmons (Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu). It requires the transmon and a photonic-IC foundry able to co-integrate electro-optic or optomechanical structures with superconducting resonators and detectors, and it replaces the cryogenic microwave link between refrigerators — competition, not complement: IBM has fabricated Loon with c-couplers and coupled two cryogenic cells (Aug 2026) [C][6] while its own researchers publish the analysis showing optical links are three orders away [S][3]. The off-diagonal reading: this cell sits where a superconducting-qubit row crosses a photonic-fabrication column, which is why no vendor owns it. Derived clock: transport dominates at about 1.0×10⁻⁵ s (the 6–10 µs repetition [D][2]) against 159 ns of gate layers and 282 ns readout, so derived clock = sum of the syndrome round: gate layers + transport + readout + reset runs ~16× the 0.65 µs on-chip round. Neighbouring empty slots: the cryogenic microwave link at multi-refrigerator scale, and the photonic-IC foundry line.

## Verification (QCVV)

Total efficiency is a calibrated scattering ratio between microwave and optical ports, so the number depends on where the reference planes sit — internal efficiency excludes coupling and is not what a link cares about. Added noise is input-referred with the pump running. The protocols miss duty cycle and thermal recovery time, routinely absent from headline claims, and end-to-end link fidelity with a real qubit at each end, never reported between two refrigerators. Conflicts: [1] lists 47% (2018) as the efficiency record while [2] tabulates 0.38 (2022) with the repetition time that makes it meaningful — both correct, incomparable; the figures reported alongside a duty cycle [2] are the ones to trust. The headline device in the technology-graph record (15% total, 0.16 photons) and the device used to read a qubit (3×10⁻⁶) differ by ~5×10⁴ [D][1][D][2].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QphoX | developer | Netherlands | Piezo-optomechanical "quantum modem"; optical readout of a Rigetti transmon; multi-channel programme at the NQCC | [C][7][C][8] |
| IST Austria (Fink) | research | Austria | Bulk-LiNbO₃ device holding the internal-efficiency and noise records; co-author of the optical-link architecture | [D][1][S][2] |
| Stanford (Safavi-Naeini) | research | USA | Piezo-optomechanical silicon crystals; 2023 and 2025 noise and bandwidth records | [D][1][D][2] |
| IBM | user / analyst | USA | Published the requirements analysis and a distillation protocol; building microwave links instead | [S][3][C][6] |
| Rigetti | user | USA | Supplies Novera QPUs as the microwave side of optical-readout experiments | [C][8] |
| NQCC | user / funder | UK | Hosts the multi-channel optical-readout system under an Innovate UK and RVO Eureka grant | [C][8] |
| Nu Quantum | adjacent developer | UK | Quantum Networking Unit for data centres; performs no microwave-optical conversion | [C][9] |
| Photonic Inc | substitution threat | Canada | Silicon T-centres emit telecom photons natively, bypassing transduction | [P][G:PHOTONIC-200M-2026-05][10] |
| Bluefors | supplier | Finland | Refrigerators with optical feedthroughs; cooling power caps channel count | [S][2] |

**Money.**

- 2024-01-17 · QphoX · Series A · €8 M · QDNL Participations (lead), EIC Fund, Quantonation, Speedinvest, High-Tech Gründerfonds, Delft Enterprises · cumulative €10 M with a €2 M 2021 seed · closed [C][7]
- 2025-05-06 · QphoX, Rigetti and NQCC · Eureka grant (RVO and Innovate UK), 33 months, multi-channel optical readout of a 9-qubit Novera at the NQCC · undisclosed · announced [C][8]
- 2025-11-06 · DARPA QBI Stage B · eleven teams, up to $15 M each — no transducer company listed, nor on Stage A · programme · announced [G:QBI-STAGEB-2025-11][11]
- 2025-12-10 · Nu Quantum · Series A · $60 M · National Grid Partners (lead), Gresham House, Morpheus, Amadeus, IQ Capital, Ahren, NSSIF, Sumitomo/Presidio · closed [C][9]
- 2026-05-12 · Photonic Inc · final close · $200 M at $2 B, $350 M total · Microsoft among returning investors · closed [P][G:PHOTONIC-200M-2026-05][10]
- 2025-06-10 · IBM · $10 B commitment and roadmap · modularity money goes to microwave couplers, not optics · announced [R][12]

The ledger is the finding: disclosed private capital in transduction as a product is about €10 M, at one company, closed two and a half years ago. Adjacent networking raised six times that in one round without touching conversion, and the largest benchmarking programme in the field funds no transducer team.

**Market & supply chain.** Nobody sells a transducer; QphoX's modem is a grant-funded research instrument. The enabling market is photonic — lithium-niobate substrates, silicon nitride and barium titanate foundry runs, nanowire detectors, cryogenic feedthroughs — with concentration risk highest in substrates and refrigerators. G6 networking pays first and G4 large-scale fault tolerance is the real prize, since multi-refrigerator scale-out is the only route past a few thousand transmons per fridge; G7 benefits indirectly as fibre replaces coax. G1, G2 and G5 do not pay for it at all, which is why venture money has not arrived.

**IP & standards.** No dated patent-family count from a named database was obtained (unverified below). No interoperability standard exists for a microwave-optical quantum link; the only fixed interface is the telecom fibre plant and the ITU wavelength grid, which is why serious designs target the C band.

**Roadmaps & track record.** QphoX (promised 2024-01 · optical readout of a commercial QPU · delivered, Nature Physics 2025-02 [C][4]). QphoX–Rigetti–NQCC (promised 2025-05 · multi-channel readout of nine Novera qubits in 33 months, due early 2028 · no public result as of 2026-09-03 [C][8]). Nu Quantum (promised · Networking Unit in 2025 · announced, no published rate or fidelity [C][9]). IBM (promised 2025-06 · module couplers with Cockatoo in 2027 · Loon and two coupled cryogenic cells fabricated 2026-08, on schedule [C][6][R][12]). QphoX has done the only thing a customer can inspect, on thin capital; IBM's analysis is credible precisely because IBM has no interest in an optimistic answer; Nu Quantum is well funded but solving the layer above. Nobody has published a dated roadmap to efficiency above one half with sub-photon noise, so 2030 in the technology graph is a placeholder.

**Strategic reading.** If the slot fills, superconducting vendors escape the single-refrigerator ceiling and microwave couplers become a stopgap; winners are photonic foundries, detector vendors and whoever owns the transducer IP, losers are cryogenic-cabling and very-large-refrigerator suppliers. If it stays empty, winners are the platforms whose carriers are already optical — trapped ions with frequency conversion, silicon T-centres, neutral atoms. Bargaining power sits with the QPU vendors: they have an alternative and the suppliers do not.

*Open niche:* the sharpest unoccupied position here is metrological. The field has no agreed acceptance test and its headline numbers are not comparable across groups; a QCVV house could define and run one — total efficiency end-to-end including fibre coupling and duty cycle, added noise referred to the qubit port, heralded Bell fidelity per attempt, and thermal recovery time after a pump pulse, reported as one tuple, with any national lab hosting a link as first customer. The second position is on the microwave side: heralded links need feed-forward inside the refrigerator, and millikelvin single-flux-quantum logic is now demonstrated for qubit control, so SFQ herald-and-switch logic closing the loop cold rather than at 300 K is an adjacent contribution.

## Outlook & open questions

**Confirm** if any group publishes one device measured at total efficiency ≥ 5%, added noise ≤ 0.2 photons and duty cycle ≥ 10% *simultaneously*; if the QphoX–Rigetti–NQCC programme shows ≥ 4 simultaneous optical readout channels; or if heralded entanglement between transmons in two separate refrigerators is measured above 90% Bell fidelity. **Demote** the slot to "bypassed" if by September 2028 no remote optical Bell pair between transmons exists and IBM's Cockatoo couplers have shipped. Best case by 2029: a four-to-eight-channel module at roughly 10% efficiency, ~0.1 added photons, a few hundred kHz herald rate [S][3][S][2]; worst case, single-channel laboratory demonstrations only and the slot still empty in 2030.

Open questions. (1) Does pump power per channel scale sub-linearly, or does the mixing chamber cap channel count at order ten? (2) Is η > 1/2 actually required, or does heralding plus distillation make η ≈ 10⁻² usable — the direct [3] versus [2] disagreement? (3) Which material wins, thin-film lithium niobate for bandwidth or silicon optomechanics for noise? (4) Who pays, given no transducer team in QBI and about €10 M of disclosed private capital? (5) Will a superconducting vendor acquire a transducer team or build in-house? Watch the NQCC multi-channel milestone and IBM's Cockatoo delivery in 2027.

## Sources

[1] T. A. Aditto, J. S. Ifty, and K. Zahin, “Toward Scalable Heterogeneous Quantum Networks: Microwave-Optical Transduction Across Platforms,” [arXiv:2605.26976](https://arxiv.org/abs/2605.26976), May 2026.
[2] M. J. Weaver, G. Arnold, H. Weaver, S. Gröblacher, and R. Stockill, “Scalable Quantum Computing with Optical Links,” [arXiv:2505.00542](https://arxiv.org/abs/2505.00542), May 2025.
[3] N. Dirnegger *et al.*, “Distilled remote entanglement between superconducting qubits across optical channels,” [arXiv:2503.10842](https://arxiv.org/abs/2503.10842), Mar. 2025.
[4] Rigetti Computing, “Research from QphoX, Rigetti, and Qblox Demonstrating Optical Readout Technique for Superconducting Qubits Published in Nature Physics,” Rigetti Investor Relations, Feb. 11, 2025. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/research-qphox-rigetti-and-qblox-demonstrating-optical-readout [C]
[5] K. Alexander *et al.*, “A manufacturable platform for photonic quantum computing,” *Nature*, vol. 641, no. 8064, pp. 876–883, Feb. 2025, doi: [10.1038/s41586-025-08820-7](https://doi.org/10.1038/s41586-025-08820-7).
[6] C. Dundon, S. Hall, M. Hollister, and A. Lindler, “IBM's new modular architecture for cryogenic systems,” IBM Quantum Computing Blog, Aug. 19, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/modular-cryogenics [C]
[7] QphoX, “QphoX raises €8m to bring quantum modem technology to market, building towards the quantum internet,” Jan. 17, 2024. [Online]. Available: https://qphox.eu/news/qphox-raises-e8m-to-bring-quantum-modem-technology-to-market-building-towards-the-quantum-internet/ [C]
[8] Rigetti Computing, “QphoX, Rigetti and the NQCC Announce Collaboration on Multi-Channel Optical Readout of Quantum Processors,” Rigetti Investor Relations, May 6, 2025. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/qphox-rigetti-and-nqcc-announce-collaboration-multi-channel [C]
[9] Nu Quantum, “Nu Quantum Raises $60M Series A in Largest Financing Round for Quantum Computer Networking,” Dec. 10, 2025. [Online]. Available: https://www.nu-quantum.com/news/nu-quantum-raises-60m-series-a-in-largest-financing-round-for-quantum-computer-networking [C]
[10] M. Abdel-Kareem, “Photonic Inc. Reaches $2B Valuation with $200M Final Close,” Quantum Computing Report, May 12, 2026. [Online]. Available: https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ [P]
[11] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[12] IBM, “IBM Sets the Course to Build World's First Large-Scale, Fault-Tolerant Quantum Computer at New IBM Quantum Data Center,” Jun. 10, 2025. [Online]. Available: https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center [R]
[13] M. Abdel-Kareem, “QphoX, Rigetti, and Qblox Demonstrate Optical Readout Technique for Superconducting Qubits,” Quantum Computing Report, Feb. 14, 2025. [Online]. Available: https://quantumcomputingreport.com/qphox-rigetti-and-qblox-demonstrate-optical-readout-technique-for-superconducting-qubits/ [P]

## Open verification items

- Primary papers behind the per-platform records (Sahu 2022, Higginbotham 2018, Warner 2025, Sonar 2025) were not consulted directly; values come from the tables of review [1] and inherit its transcription risk. Review [1] is a preprint by authors with no experimental record in the field.
- Conflict: [1] reports 47% (2018) as the total-efficiency record; [2] tabulates 0.38 (2022) at 5,000 µs repetition. Both stand; [2] preferred because it reports duty cycle alongside efficiency.
- Conflict: the headline figures in the technology-graph record (total efficiency 15%, added noise 0.16) versus the integrated device used with a qubit (3×10⁻⁶) — a factor ~5×10⁴ [1], [2].
- Substantive conflict: [3] (IBM) requires three orders of improvement on noise, efficiency and repetition rate; [2] (QphoX/IST) claims >99% Bell fidelity with existing transducer performance via protocol design. Unresolved.
- The Nature Physics paper for the QphoX–Rigetti–Qblox optical readout: exact title, authors, publication date and measured readout fidelity not obtained ([13] paywalled, [4] not itemised).
- Export control: the specific ECCN applying to microwave-optical transducers under the BIS interim final rule of 2024-09-06 was not verified.
- No dated patent-family count from a named database was obtained for this slot.
- QphoX funding after 2024-01 and Nu Quantum cumulative funding are not disclosed by the sources used.
- No 2026 transduction record was found; the most recent primary device numbers date to 2025.
