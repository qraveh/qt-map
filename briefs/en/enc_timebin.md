---
id: enc_timebin
name: Time-bin / path photonic encoding
layer: "2 Encoding"
status: demonstrated
since: 2001
one_line: "Photonic dual-rail qubit in arrival-time bins or waveguide path; loss is the error and it is heralded rather than stochastic."
verdict: "The two halves have diverged: path encoding won on chip (PsiQuantum Omega), time-bin survives in fibre, because an on-chip delay costs 0.27 dB per ns. No fusion logical qubit by 2028 leaves it a communication encoding."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
One photon, two orthogonal modes: two arrival-time bins, or two waveguides. Nothing continuous decoheres, so the only error is loss — and a lost photon fails to herald, detectable where it happens. Time-bin entanglement came from Brendel, Gisin, Tittel and Zbinden at Geneva in 1999, built for telecom fibre [D][1]; path encoding is the on-chip descendant, and Omega says so plainly — "a path-encoded qubit using a heralded photon and two-mode interferometers" [D][2]. Coordinates: no mobility, no control modality, no fabrication of its own; pure-loss error.

## Physics & limits
The floor is a loss budget, not an infidelity: every interferometer, coupler and switch removes amplitude, and the two halves of this node price it differently. A 1 ns time bin needs ~0.15 m of on-chip delay at group index 2, which at PsiQuantum's measured 1.8 ± 0.2 dB/m SiN loss [D][2] costs ~0.27 dB — over half a ~0.5 dB per-photon budget, against ~0.04 mdB in fibre. That is why chips are path-encoded and fibres time-bin encoded — one node only in the abstract. The erasure advantage needs a trusted herald: Omega's median on-chip detector efficiency is 93.4% [D][2], so about one heralded event in fifteen is an unflagged loss entering the code as ordinary error.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02 | Fusion Bell fidelity 99.22 ± 0.12%, chip-to-chip 99.72 ± 0.04% | PsiQuantum | [D][2] |
| 2025-02 | Single-mode SiN loss 1.8 ± 0.2 dB/m; on-chip SNSPD 93.4% | PsiQuantum | [D][2] |
| 2026-06-26 | Unencoded 6-ring loss threshold 0.38–0.82% | Löbl et al. | [S][4] |

No logical qubit exists in this encoding, and the threshold it must meet is disputed: 2.7% per photon for a boosted 6-ring and 17.4% for a {7,4}-encoded state [S][3] against 0.38–0.82% unencoded [S][4] — an order of magnitude apart, unreconciled [G:FBQC-THRESHOLD-CONFLICT-2026].

## Manufacturing, materials & supply chain
No fabrication step of its own: the encoding rides its host — PsiQuantum's 300 mm silicon nitride, Quandela's III–V quantum dots, QuiX's SiN meshes. Control is inherited: no per-qubit drive line, but every interferometer needs a phase shifter and every output a detector — thousands of cryogenic channels and their fan-out at 10³–10⁴ qubits. Chokepoints are the detector vendors (Single Quantum, ID Quantique, Photon Spot) and the III–V and SiN foundries [P][G:SNSPD-VENDORS-2026]; ECCN 4A906 applies [G:BIS-QUANTUM-2024].

## Role in the stack
The encoding under the fusion-based discrete-variable path (PsiQuantum, Quandela, QuiX); it needs only a single-photon source and has no rival there. Swapping path for time-bin trades interferometer phase stability for delay-line loss, unaffordable on chip. It also caps fusion: passive linear-optical Bell measurement on a dual-rail qubit succeeds at 50%, at least 75% with unentangled ancillae [S][5]. Verification: no group has run a syndrome cycle using heralded loss as an erasure flag, so the advantage is a design argument, not a measurement.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US | Path-encoded qubits on Omega | [D][2] |
| Quandela | developer | FR | Photonic QPUs on quantum-dot sources | [C][G:QUANDELA-LUCY-HPC-2026-04] |
| QuiX Quantum | developer | NL | Carina core delivered to DLR | [C][7] |
| Sparrow Quantum | supplier | DK | Only merchant single-photon source vendor | [P][8] |

**Money.**
2025-04-10 · Sparrow Quantum · Series A · EUR 21.5 M · lead undisclosed · closed [P][8]
2025-09-10 · PsiQuantum · Series E · USD 1 B at USD 7 B · BlackRock, Temasek · closed [C][G:PSIQ-1B-2025-09]
2026-07-22 · PsiQuantum · DARPA QBI Stage C expansion · USD 125 M · DARPA · announced [P][G:PSIQ-QBI-C-2026-07]

**Market & supply chain.** Sparrow is the only merchant source vendor, shipping 20–35% system efficiency against a 71.2% laboratory record [P][8], so every fusion architecture pays a multiplexing tax set by one supplier's yield. Pays for G1/G2, is PsiQuantum's G3–G4 substrate, and pays separately for G6 through QKD.

**IP & standards.** ORCA holds US 12,437,225 on linear-optical encoded GHZ measurements (granted 2025-10-07), the only photonic dual-rail family a dated search surfaced [G][6]; no computing-side standard exists.

**Roadmaps & track record.** PsiQuantum has published no hardware result since Omega, so 2026 progress is legible only through DARPA V&V [P][G:PSIQ-QBI-C-2026-07]. QuiX promised a universal machine for 2026 and delivered the core, not the machine [C][7]. Quandela missed its 2025 first-logical-qubit milestone, still targeting 50 by 2028 [R].

**Strategic reading.** Whoever cuts system-level loss wins the fusion race — likely whoever controls detector efficiency and source multiplexing, not whoever designs the encoding, which is free where its host is not. QKD monetises the same physics, so a fusion failure strands PsiQuantum and Quandela but not QKD.

*Open niche:* an erasure-aware benchmarking suite is a genuine gap — randomized benchmarking assumes Pauli noise, not flagged loss, and nothing published measures what fraction of a heralded-loss channel is actually flagged at a given detector efficiency [D][2].

## Outlook & open questions
Confirm by 2027: a hardware syndrome cycle consuming heralded loss as an erasure flag; absent that it stays theory. Best case 2029: a small fusion-based logical qubit; worst case, commercially real only in QKD. Open: does anyone reconcile the 0.38% and 2.7% thresholds; can detector efficiency reach herald-trust levels at scale.

## Sources
[1] Brendel, Gisin, Tittel, Zbinden (University of Geneva), "Pulsed energy-time entangled twin-photon source for quantum communication," Phys. Rev. Lett. 82, 2594, 1999 [D] — https://arxiv.org/abs/quant-ph/9809034
[2] PsiQuantum, "A manufacturable platform for photonic quantum computing" (Omega), Nature, 2025-02 [D] — https://www.nature.com/articles/s41586-025-08820-7
[3] Fusion-based quantum computation loss thresholds, Nature Communications, 2023 [S] — https://www.nature.com/articles/s41467-023-36493-1
[4] Löbl, Pettersson, Dragašević, Chen, Sandberg (Sparrow Quantum / Center for Hybrid Quantum Networks), "The subthreshold issue of fusion-based quantum computing," arXiv:2606.28490, 2026-06-26 [S] — https://arxiv.org/abs/2606.28490
[5] Ewert, van Loock, "3/4-efficient Bell measurement with passive linear optics and unentangled ancillae," Phys. Rev. Lett. 113, 140403, arXiv:1403.4841, 2014 [S] — https://arxiv.org/abs/1403.4841
[6] ORCA Computing Limited, US 12,437,225, "Linear-optical encoded GHZ measurements and fault-tolerant quantum computation and communication," granted 2025-10-07 [G] — https://patents.justia.com/patent/12437225
[7] QuiX Quantum, Series A announcement, 2025-07-10 [C] — https://www.quixquantum.com/news/quix-quantum-series-a
[8] Quantum Computing Report, "Sparrow Quantum Secures €21.5M Series A," 2025-04-10 [P] — https://quantumcomputingreport.com/sparrow-quantum-secures-e21-5m-24m-usd-in-series-a-funding-to-advance-photonic-quantum-chip-production/
[9] Toshiba Europe, quantum technology news (Orange Business 2025-06-11; Quantum Bridge 2026-03-16) [C] — https://www.toshiba.eu/quantum/news/

## Open verification items
The main report's "waveguide loss 0.5 dB/m" is not the Omega single-mode SiN figure; 1.8 ± 0.2 dB/m is used here and the discrepancy is unreconciled [G:PSIQ-OMEGA-METRICS-2025]. The arXiv abstract page for quant-ph/9809034 returned the abstract text but not the author list or journal reference; the attribution to Brendel, Gisin, Tittel and Zbinden rests on the identifier. Loss thresholds for 6-ring fusion differ by an order of magnitude between sources with no reconciliation [G:FBQC-THRESHOLD-CONFLICT-2026]. No syndrome-extraction-with-heralded-loss demonstration exists on any platform. Toshiba's public pages do not name "time-bin" for its 2025–26 deployments, so that attribution is not used here beyond the general QKD context [9]. The 0.27 dB per nanosecond of on-chip delay is derived from published loss figures, not measured.
