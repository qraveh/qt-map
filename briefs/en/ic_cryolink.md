---
id: ic_cryolink
name: Cryogenic microwave link between refrigerators
layer: "9 Interconnect"
status: emerging
since: 2020
one_line: "Superconducting waveguide held below 50 mK along its whole length, carrying itinerant 5–7 GHz photons or squeezed states between two independently cooled dilution refrigerators."
verdict: "One group (ETH Zürich) owns every headline: 30 m, Bell fidelity 80.4% at 12.5 kHz, loophole-free. Loss sits in the demountable joints, not the waveguide, and no architecture puts this on a fault-tolerance critical path."
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A superconducting waveguide cooled below the aluminium gap along its whole length, carrying itinerant ~5–7 GHz photons between two *separately* cooled dilution refrigerators — not between chips in one cryostat. Wallraff's group at ETH Zürich introduced it in 2020: 5 m, state transfer 85.8%, remote Bell pairs 79.5% [D][3]. The 30 m successor carried the first loophole-free superconducting Bell test in 2023 [D][1]; the 2026 paper documents it as a reproducible modular assembly [D][2]. TU Munich with VTT runs the only independent second line, sending *squeezed* Gaussian states over 6.6 m [D][4]. Coordinates: d = long-range inter-cryostat connectivity, the only layer entry spanning separate refrigerators; e/f/g = millikelvin microwave drive at both fridges, loss and coherent phase rather than Pauli errors, superconducting lithography with demountable interfaces (graph record).

## Physics & limits
The waveguide is not the limit: attenuation is α < 1 dB/km, under 0.03 dB across the full 30 m — the *same* figure in the 2023 and 2026 papers [D][1][2]. End-to-end photon transfer loss is nonetheless 0.55–0.65 dB (12–14%), which the 2026 paper attributes to the interfaces between modules, not the line [D][2]: every one of the 26 demountable joints costs transmission.

Second, thermal occupation. At 5.6 GHz a photon is worth 0.27 K, so a 50 mK channel holds 4.6×10⁻³ residual photons, while the 1 K channel centre at which Munich/VTT still resolved entanglement holds ≈3.3 [D][4]. Fock transfer degrades roughly linearly in that occupation; Gaussian squeezed states tolerate it, so squeezing is the cheaper carrier to lengthen. Third, phase: two mechanically independent cryostats need a common reference, and no source quantifies the residual phase noise — the term that would bound a repeatered link. What moves the floor: welded or bump-bonded joints replacing demountable flanges.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-05 | 30 m link, Bell fidelity 80.4% at 12.5 kHz, CHSH S = 2.0747 ± 0.0033 | ETH Zürich | [D][1] |
| 2025-05 | 6.6 m squeezed link, 2.10 ± 0.02 dB squeezing, negativity 0.501 ± 0.011 | TU Munich | [D][4][G:MUNICH-VTT-CRYOLINK-2025] |
| 2026-04 | 30 m modular assembly, 26 modules, 6.5 d cooldown, 0.55–0.65 dB transfer loss | ETH Zürich | [D][2] |

Interface loss dominates, ~20× the waveguide's own contribution [D][2]; no chained (≥3-fridge) link, no link run during gate execution, and no independent 30 m replication as of 2026-09-04.

## Manufacturing, materials & supply chain
Every link is bespoke. The ETH 30 m assembly is 26 modules plus two nodes and a central cooling unit, holding the 4 K stage under 6 K across the span; the 6.5-day cooldown, not fidelity, is what makes iteration slow, and simulation puts one cooling unit per ~15 m out to 120 m [D][2][S][2]. Base cryostats come from a concentrated market: Bluefors closed its Cryomech acquisition (pulse-tube and Gifford-McMahon cryocoolers) on 2023-03-28, giving ~600 staff and revenue above EUR 160 M [C][8]; ULVAC is a Japanese third source built with IBM input [C][5][G:ULVAC-IBM-REFRIG-2025]. Export exposure is inherited: ECCN 3A904 (BIS, 2024-09-06) covers refrigerators sustaining ≥600 µW at 0.1 K for 48 h; no ECCN names a link [G][9][G:BIS-QUANTUM-2024].

## Control, readout & I/O burden
Each attempt needs a flux-tunable coupler at both ends and microwave sources phase-locked across two cryostats. The 2023 Bell test carries this report's hardest real-time constraint: 32.824 m of separation leaves a 109 ns window in which basis choice, gate, readout and record must all complete [D][1]. The 12.5 kHz repetition rate — 80 µs per attempt — is set by reset and pulse shaping, not time of flight. Nothing is published at 10³–10⁶ qubits; the binding quantities are cryoplant count and independent phase references.

## Role in the stack
The only path is superconducting transmon (Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu); it requires superconducting-qubit lithography. It competes with same-fridge modularity — IBM coupled two cryogenic cells in 2026-08, l-couplers at "one meter scale", with no qubits and no fidelity reported [C][6][G:IBM-MODCRYO-2026-08] — and with microwave-optical transduction, best total efficiency 47% and nothing at η > ½ with sub-unity added noise [P][10][G:TRANSDUCER-GAP-2026]. Derived clock: 80 µs per entanglement attempt (2 s.f.) against a 1.1 µs surface-code cycle — four orders adrift. Adjacent empty slot: a cryogenic microwave switch, absent which N fridges need N(N−1)/2 waveguides.

## Verification (QCVV)
A loophole-free CHSH violation with space-like separated measurements is device-independent, not tomographic — unusually strong verification for this layer [D][1]. Munich rests on homodyne tomography [D][4]; the two are not comparable, neither replicated, and both ran with local processors idle. Conflict: the graph record's 75–79% transfer efficiency is not what 0.55–0.65 dB implies alone (86–88%).

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| ETH Zürich | Research | Switzerland | Built the 5 m, 30 m and modular links; owns every headline | [D][1][2][3] |
| TU Munich | Research | Germany | 6.6 m squeezed-state link, the independent second line | [D][4] |
| Bluefors | Supplier | Finland | Refrigerator and cryocooler vendor; KIDE is the rival path | [C][7][G:BLUEFORS-KIDE] |
| ULVAC Cryogenics | Supplier | Japan | ~10 mK refrigerator with IBM input, tested at Poughkeepsie | [C][5][G:ULVAC-IBM-REFRIG-2025] |
| IBM | Developer | USA | Runs the competing intra-fridge modular-cryogenics line | [C][6][G:IBM-MODCRYO-2026-08] |

**Money.** 2023-03-28 · Bluefors · M&A (Cryomech) · undisclosed · combined revenue > EUR 160 M · closed [C][8]. 2024-09-06 · US BIS · ECCN 3A904 rule · n/a · in force [G][9]. 2025-03-21 · ULVAC · ~10 mK refrigerator programme with IBM · undisclosed · "early 2026", unconfirmed [C][5]. No round, grant or acquisition specific to an inter-fridge link exists as of 2026-09-04.

**Market & supply chain.** There is no link market, only a refrigerator market in which a link consumes two units instead of one; Oxford Instruments is the second merchant source [C][5]. Bluefors plus Cryomech supplies the dilution stage and the pulse tubes beneath it with no alternative at that volume [C][8]. G6 (networking) pays directly; G4 pays only once a cryostat's line budget runs out, which KIDE's >4,000 RF lines are designed to postpone [C][7][G:BLUEFORS-KIDE].

**IP & standards.** No patent family specific to cross-cryostat microwave links in any named database and no standards body addressing cryogenic microwave interfaces — no dated fact found; module geometry is published openly [D][2].

**Roadmaps & track record.** ETH Zürich: (2023-05 · 30 m Bell test · delivered); (2026-04 · 120 m via cooling units per ~15 m · simulated only) [S][2]. ULVAC/IBM: (2025-03 · refrigerator "early 2026" · unconfirmed) [C][5]. IBM: (2026-08 · two coupled cells · delivered, no qubits in them) [C][6]. ETH has met every milestone it announced; both vendor timelines are unverified.

**Strategic reading.** If this works the cryostat suppliers capture the value, not the QPU vendor. If it fails nothing breaks — every published superconducting roadmap scales inside one cryostat first. Substitution runs both ways: l-couplers remove the need below ~1,000 qubits per cell [C][6], transduction removes the distance limit above it. No independent link vendor exists to bargain with.

*Open niche:* no demonstration characterises link fidelity, phase stability or crosstalk while both endpoints run live gates; every result assumes a quiet fridge at each end. Independent phase-noise and interface-loss metrology, and a protocol certifying a link separately from its nodes, is an open QCVV niche.

## Outlook & open questions
Falsifiable (12–24 months): confirm if any group publishes a three-cryostat chained link, or a 30 m link run while both processors execute gates, by end-2027; demote if interface loss is not below 0.3 dB by then. Best case 2029: per-hop efficiency above 90% and an architecture that needs two fridges. Worst case: intra-cryostat modularity absorbs all growth through 2030 and this stays a Bell-test instrument. Open questions: residual inter-cryostat phase noise; whether joints can be non-demountable and still serviceable; whether anyone builds a cryogenic microwave switch. Watch: ETH follow-ons, IBM's first coupled cells with qubits in them.

## Sources
[1] Storz, S., Schär, J., Kulikov, A., Magnard, P., Kurpiers, P., … Wallraff, A. (ETH Zürich) · "Loophole-free Bell inequality violation with superconducting circuits" · Nature 617, 265 · 2023-05-10 — https://www.nature.com/articles/s41586-023-05885-0
[2] Schär, J.D., Storz, S., Magnard, P., Kurpiers, P., Lütolf, J., Gehrig, M., Besse, J.-C., Kulikov, A., Wallraff, A. (ETH Zürich) · "A modular cryogenic link for microwave quantum communication over distances of tens of meters" · arXiv:2604.15971 · 2026-04 — https://arxiv.org/html/2604.15971v1
[3] Magnard, P., Storz, S., Kurpiers, P., et al. (ETH Zürich) · "Microwave quantum link between superconducting circuits housed in spatially separated cryogenic systems" · Phys. Rev. Lett. 125, 260502 (arXiv:2008.01642) · 2020-12 — https://arxiv.org/abs/2008.01642
[4] Yam, W.K., Renger, M., Gandorfer, S., et al. (MCQST / TU Munich; VTT, Finland) · "Cryogenic microwave link for quantum local area networks" · npj Quantum Information 11, 87 · 2025-05-31 — https://www.nature.com/articles/s41534-025-01046-5
[5] ULVAC, Inc. [C] · "ULVAC developing next-generation dilution refrigerator for quantum computing" · press release · 2025-03-21 — https://www.nasdaq.com/press-release/ulvac-developing-next-generation-dilution-refrigerator-quantum-computing-2026-2025-03
[6] IBM Quantum [C] · "A new modular architecture for cryogenic systems" · IBM Quantum blog · 2026-08-19 — https://www.ibm.com/quantum/blog/modular-cryogenics
[7] Bluefors [C] · "KIDE cryogenic platform" · product page, revised 2026-06-16 — https://bluefors.com/products/kide-cryogenic-platform/
[8] Bluefors [C] · "Bluefors closes the acquisition of Cryomech" · press release · 2023-03-28 — https://bluefors.com/press-releases/bluefors-closes-the-acquisition-of-cryomech/
[9] US Bureau of Industry and Security [G] · "Commerce Control List additions and revisions: controls on advanced technologies" (ECCN 3A904, dilution refrigerators) · Federal Register interim final rule · 2024-09-06 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies
[10] Microwave-optical transduction state-of-the-art review [P] · arXiv:2605.26976 · 2026-05 — https://arxiv.org/html/2605.26976

## Open verification items
The graph record's "transfer efficiency 75–79%" for the 2026 link is not implied by the measured 0.55–0.65 dB channel loss (86–88% transmission); no source reconciles the two, and the residue is presumed to be node emission/absorption efficiency.
Residual phase noise between the two cryostats is not quantified in any source reviewed.
No independent replication of either the ETH 30 m or the Munich/VTT 6.6 m headline figure as of 2026-09-04.
ULVAC/IBM refrigerator shipment status unconfirmed beyond the "early 2026" target stated in 2025-03.
The arXiv HTML for [2] shows a 2026-08-24 revision date against an April-2026 identifier; the graph record's 2026-04 date is used here.
