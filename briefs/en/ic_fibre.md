---
id: ic_fibre
name: Fibre links between photonic modules
layer: "9 Interconnect"
tier: 3
status: demonstrated
since: 2025
one_line: "Telecom fibre carrying heralded entanglement between photonic chips and racks — priced per connector, not per metre, and with no published rate."
verdict: "Real: 99.72% chip-to-chip Bell fidelity over 42 m (PsiQuantum, 2025), the fibre span itself costing ~8 mdB. Unproven: any inter-module entanglement rate. Demote if none is published by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Commodity telecom single-mode fibre carrying single photons or heralded entangled pairs between photonic chips, racks or modules. PsiQuantum published chip-to-chip Bell fidelity 99.72 ± 0.04% over 42 m in Omega [D][2]; Aurora networks 35 chips over fibre at ~14 dB total loss [D][1]. The same physics underwrites metropolitan entanglement distribution, where rates are published. Coordinates: flying photons, no deterministic timing, loss-dominated error; room-temperature electro-optic interfaces, photonic-IC fibre coupling.

## Physics & limits
Attenuation is not the binding term at machine scale. Forty-two metres at 0.2 dB/km is ~8 mdB, while the two fibre-to-chip transitions bracketing it cost 52 ± 12 mdB each [D][2] — ~104 mdB, a fifth of a ~0.5 dB per-photon budget, spent on connectors rather than span. Modularity here is priced per interface, unlike matter-qubit links. What distance costs is time: 42 m is ~206 ns one way at group index 1.47, longer than the best 2026 feed-forward electronics, so separation eats the decision budget before the loss budget. Rate is the term no computing vendor publishes, and its exchange against loss is brutal: 0.7 coincidences/s through 66 dB of metropolitan fibre versus 132/s on the 93 km leg [P][3]. At rack-scale loss the ceiling reverts to source brightness and multiplexing depth.

## Engineering state of the art

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-01 | 35 chips networked over fibre, ~14 dB total loss | Xanadu | [D][1] |
| 2025-02 | Chip-to-chip Bell fidelity 99.72 ± 0.04% over 42 m | PsiQuantum | [D][2] |
| 2025-02 | Fibre-to-chip coupling 52 ± 12 mdB | PsiQuantum | [D][2] |
| 2026-06-10 | Edge coupling 0.085 dB/facet, claimed a benchmark | Xanadu | [C][5] |

The 2026 benchmark claim does not survive comparison: PsiQuantum's 52 mdB is ~39% lower at the same interface a year earlier [D][2][C][5]. Fidelity is past 99.7%; the missing number is throughput.

## Manufacturing, materials & supply chain
No new fabrication: fibre, connectors and edge-coupled arrays are commodity telecom, with Corning fibre arrays and DISCO singulation behind Xanadu's coupling figure [C][5]. The scaling variable is attachment count: every module boundary is two attachments, each a yield event and a 52 mdB loss event, so at 10³ modules packaging throughput sets the build rate; at 10⁴ bundle volume and timing calibration bind; nothing addresses 10⁶. I/O burden sits upstream, in the source and the fusion measurement. The machine falls under BIS ECCN 4A906 [G:BIS-QUANTUM-2024].

## Role in the stack
Both photonic paths depend on it — fusion (PsiQuantum, Quandela, QuiX) and continuous-variable/GKP (Xanadu) — to scale past one chip's mode count, contributing ~0.21 µs per 42 m to the derived clock, comparable to the whole feed-forward term. Verification: the 99.72% is a conditional Bell fidelity on heralded events, channel loss excluded [D][2], so it says nothing about link efficiency, and it is single-source as of 2026-09-04.

## Actors & economics
**Who.**

| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US | Highest published chip-to-chip Bell fidelity over 42 m | [D][2] |
| Xanadu | developer | CA | 35-chip fibre-networked system; coupling benchmark | [D][1] |
| Quandela | developer | FR | Fielded 12-qubit Lucy coupled to Joliot-Curie HPC | [C][8] |
| Corning | supplier | US | Fibre arrays for photonic chip packaging | [C][5] |

**Money.**
2025-09-10 · PsiQuantum · Series E · USD 1 B at USD 7 B · BlackRock, Temasek, Baillie Gifford · closed [C][G:PSIQ-1B-2025-09]
2026-03-26 · Xanadu · SPAC merger · ~USD 302 M gross, ~40% below plan · Crane Harbor · closed [C][G:XANADU-SPAC-2026-03]
2026-05-21 · PsiQuantum · CHIPS letter of intent · USD 100 M · US Commerce · LOI [G:CHIPS-LOI-2026-05]

**Market & supply chain.** Fibre and connectors are commodity; the concentrated input is precision fibre-array attachment, where Corning and a few packaging houses set loss and throughput alike. No cost per link is public. Pays for G3/G4, G6.

**IP & standards.** No dated patent family specific to inter-module photonic fibre linking surfaced as of 2026-09-04; ETSI QKD standards govern the physical layer, no computing-side interconnect standard exists.

**Roadmaps & track record.** PsiQuantum's 99.72% is unchanged since 2025-02, its 2026 progress visible only through DARPA V&V [D][2]. Xanadu marketed a coupling benchmark it does not hold [C][5]. No actor has published a dated inter-module rate target — a roadmap gap, not a slipped promise.

**Strategic reading.** While rate stays unpublished, every photonic logical-qubit roadmap rests on an unaudited number and buyers cannot compare vendors. Whoever publishes fidelity and rate together sets the benchmark; packaging houses, not chip designers, capture the margin, since loss and yield live at the connector.

*Open niche:* standardised measurement of inter-module entanglement rate at a declared loss reference plane, alongside fidelity, is an unclaimed QCVV service — the record holds fidelity without rate in computing, rate without computing in networking.

## Outlook & open questions
Confirm by 2028: a vendor publishing an inter-module rate with its fidelity; demote if the field still reports fidelity alone. Best case 2029: multiplexed links close a stated rate gap at rack scale. Worst case: rate stays unmeasured. Open: is 99.72% reproducible outside PsiQuantum; does multicore fibre help inside a machine.

## Sources
[1] Xanadu, "Scaling and networking a modular photonic quantum computer" (Aurora), Nature 638, 2025-01 [D] — https://www.nature.com/articles/s41586-024-08406-9
[2] PsiQuantum, "A manufacturable platform for photonic quantum computing" (Omega), Nature, 2025-02 [D] — https://www.nature.com/articles/s41586-025-08820-7
[3] "Entanglement distribution over 155 km metropolitan fiber using a CMOS-compatible silicon chip," arXiv:2409.17558, 2024-09 [P] — https://arxiv.org/abs/2409.17558
[4] "Chip-to-chip entanglement distribution over 80-km multicore fiber link," arXiv:2604.26791, 2026-04 [P] — https://arxiv.org/abs/2604.26791
[5] PR Newswire, "Xanadu Sets New Industry Benchmark in Photonic Chip Packaging," 2026-06-10 [C] — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html
[6] QuiX Quantum, Series A announcement, 2025-07-10 [C] — https://www.quixquantum.com/news/quix-quantum-series-a
[7] NIST, "Department of Commerce Announces Letters of Intent with 9 Companies," 2026-05-21 [G] — https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[8] The Quantum Insider, "Quandela Deploys Photonic Quantum Computer Integrated with HPC System," 2026-04-14 [P] — https://thequantuminsider.com/2026/04/14/quandela-photonic-quantum-hpc/

## Open verification items
The full text of arXiv:2604.26791 could not be consulted; its title is cited but none of its numbers are used. Authors and affiliations for arXiv:2409.17558 could not be confirmed; the deployment names NUS, SUTD and NTU links in Singapore. No photonic computing vendor publishes an inter-module entanglement-distribution rate, so the field's throughput ceiling is unverified. PsiQuantum's 99.72% chip-to-chip Bell fidelity has no independent replication. The ~206 ns per 42 m latency and the ~104 mdB two-interface cost are derived here from published figures, not measured.
