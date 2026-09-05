---
id: ct_eo
name: Electro-optic drive + feed-forward electronics (RT)
layer: "5 Control"
tier: 3
status: demonstrated
since: 2020
one_line: "Room-temperature modulators driven from detector outcomes inside one optical clock cycle — the feed-forward layer every photonic architecture needs."
verdict: "Loop latency reached 150–196 ns in 2026 against an 80 ns switch: electronics sit ~2× above the component floor, not orders of magnitude. Demote if no system-scale sub-µs loop by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
The 300 K layer that drives photonic qubits and closes the measurement loop: pump lasers, thin-film lithium-niobate (TFLN) or barium-titanate (BTO) modulators, and electronics turning a detector click or homodyne quadrature into a drive voltage before the next photon arrives. Alone among control nodes it has no cryogenic variant: electronics at 300 K read detectors near 2 K, so every loop crosses that boundary twice. Coordinates: no carrier of its own, immobile, loss-dominated error; electro-optic modality at room temperature, photonic-IC fabrication.

## Physics & limits
Modulator bandwidth is not the constraint. What binds is detector rise, discrimination, decision and driver settling, which must fit inside optical delay you can afford. Holding a photon 100 ns in silicon nitride costs ~15 m of waveguide; at PsiQuantum's measured 1.8 ± 0.2 dB/m single-mode SiN loss that is ~27 dB against a per-photon budget near 0.5 dB. The same delay in fibre costs ~4 mdB plus two fibre-to-chip transitions at 52 ± 12 mdB [D][2]. Feed-forward delay must live off-chip; its loss price is packaging, not waveguide [S]. Past ~1 GHz the wall becomes SNSPD dead time.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-01 | Feed-forward in one 1 MHz cycle, 35 chips | Xanadu | [D][1] |
| 2026-06-02 | ~150 ns detector-in to settled drive | QuiX Quantum | [C][4] |
| 2026-06-02 | 196 ns continuous-variable loop | Duggan et al. | [P][5] |
| 2026-06-04 | Non-volatile BTO array, 80 ns | Lumiphase | [D][3] |

June 2026 reset the arithmetic: 80 ns against a 1 µs cycle is ~12×, and rack electronics at 150–196 ns cut it to ~2×. That array's zero static power costs 1.48 dB per cell, ~15× PsiQuantum's 100 mdB in-line switch [D][2][3] — routing plane, not fusion plane.

## Manufacturing, materials & supply chain
TFLN comes from two merchant vendors, HyperLight and Lightium [P][6]; volume BTO only from PsiQuantum's 300 mm GlobalFoundries flow [D][2] and Lumiphase's pilot [D][3]; Xanadu's 0.085 dB/facet coupling used Corning and DISCO [C][9]. No cost per channel is public. I/O burden is this node: a driver and DAC per modulator, a coax and discriminator per detector. QuiX's unit is 32×32 [C][4], so 10³ modes is ~30 racks; at 10⁴ the wall is inter-rack clock skew, at 10⁶ nothing scales. The machine falls under BIS ECCN 4A906 [G:BIS-QUANTUM-2024].

## Role in the stack
A hub, not a path choice: it drives the fusion path (PsiQuantum, Quandela, QuiX) and the continuous-variable/GKP path (Xanadu) identically, and sets the derived clock wherever fusions or homodyne measurements iterate — 1.0 MHz at system scale, 5–7 MHz at unit scale. Verification: the figures sit at three reference planes. QuiX's ~150 ns is detector-to-drive [C][4]; 196 ns a full CV loop [P][5]; Aurora's 1 MHz a cycle time, not a latency [D][1].

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Xanadu | developer | CA | Only system-scale single-cycle feed-forward | [D][1] |
| PsiQuantum | developer | US | 300 mm BTO switches, DARPA V&V | [D][2] |
| QuiX Quantum | developer | NL | Rack feed-forward unit, ~150 ns | [C][4] |
| Lumiphase | supplier | CH | Non-volatile BTO array | [D][3] |

**Money.**
2024-09 · HyperLight · Series B · USD 37 M · Summit Partners · closed [P][6]
2025-07-10 · QuiX · Series A · EUR 15 M · Invest-NL, EIC · closed [C][G:QUIX-SERIESA-2025-07]
2026-05-21 · GlobalFoundries · CHIPS LOI · USD 375 M · US Commerce [G:CHIPS-LOI-2026-05]
2026-07-22 · PsiQuantum · QBI Stage C, BTO-switch V&V · USD 125 M · DARPA [P][7]

**Market & supply chain.** Two TFLN vendors, one volume BTO line, and no merchant vendor of low-latency feed-forward at all — each firm builds its own. The scarce input is the deterministic sub-200 ns detector-to-driver path, not the modulator. Pays for G3/G4, G6.

**IP & standards.** No feed-forward patent family surfaced from a dated database as of 2026-09-04; the BTO gate array is the dated advance [D][3].

**Roadmaps & track record.** Xanadu 1 MHz (delivered 2025-01, unimproved) [D][1]; QuiX named fast feed-forward a 2026 blocker in 2025-07 and installed the unit 2026-06-02 [C][4]; PsiQuantum published no 2026 hardware result [P][7]. QuiX alone shipped what it named.

**Strategic reading.** If sub-200 ns loops generalise, the bottleneck migrates to detector dead time and the fibre delay lines holding photons during the decision — favouring owners of packaging and detector supply over FPGA vendors. A merchant feed-forward box would commoditise a layer three firms treat as differentiation.

*Open niche:* load-tested closed-loop latency measurement at a stated reference plane is an unclaimed QCVV service, precisely because 1 MHz, 150 ns and 196 ns are quoted at incompatible planes.

## Outlook & open questions
Confirm by 2027: a loop under 200 ns above 32 channels, or a system cycle faster than 1 MHz; demote if Aurora's 1 MHz still stands in 2028. Best case 2029: ~10 MHz rack-scale. Worst case: unit latency never couples to scale. Open: does 150 ns hold under 32-channel load; does non-volatile BTO reach usable in-line loss.

## Sources
[1] Xanadu, "Scaling and networking a modular photonic quantum computer" (Aurora), Nature 638, 2025-01 [D] — https://www.nature.com/articles/s41586-024-08406-9
[2] PsiQuantum, "A manufacturable platform for photonic quantum computing" (Omega), Nature, 2025-02 [D] — https://www.nature.com/articles/s41586-025-08820-7
[3] UPV iTEAM with Lumiphase and CEA-Leti, non-volatile barium-titanate photonic gate array, Nature Photonics, 2026-06-04 [D] — https://www.nature.com/articles/s41566-026-01934-y
[4] QuiX Quantum, "QuiX Quantum Installs Real-Time Control Component for Universal Photonic Quantum Computer," 2026-06-02 [C] — https://www.quixquantum.com/news/quix-quantum-installs-real-time-control-component-for-universal-photonic-quantum-computer
[5] Duggan, Filgis, Bregnsbo, Saalmüller, Neergaard-Nielsen, Wintermantel, Andersen, "FPGA Based Feedforward System for Photonic Quantum Computing Applications," arXiv:2606.03500, 2026-06-02 (v2 2026-06-25) [P] — https://arxiv.org/abs/2606.03500
[6] optics.org, "Lithium niobate in vogue as thin-film developers raise cash," 2024-09 [P] — https://optics.org/news/lithium-niobate-in-vogue-as-thin-film-developers-raise-cash
[7] Quantum Computing Report, "PsiQuantum Secures $125 Million Expanded Agreement with DARPA under QBI," 2026-07-22 [P] — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/
[8] Xanadu, "Xanadu Charts Path to Over 1,000 Logical Qubits by 2031," GlobeNewswire, 2026-08-31 [C] — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html
[9] PR Newswire, "Xanadu Sets New Industry Benchmark in Photonic Chip Packaging," 2026-06-10 [C] — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html

## Open verification items
Institutional affiliations for arXiv:2606.03500 are not on the retrievable abstract page; the author list points to the DTU group but is unconfirmed. The three 2026 latency figures sit at different reference planes and no source reconciles them. The 27 dB on-chip versus 4 mdB in-fibre delay comparison is derived here from published loss figures, not measured. No cost per modulator or feed-forward channel is public.
