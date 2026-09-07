---
id: fab_stm
name: STM hydrogen lithography (donors)
layer: "10 Manufacturing"
status: demonstrated
since: 2012
one_line: A scanning-tunnelling tip desorbs hydrogen from passivated Si(100) to open single sites, phosphine dopes them, and epitaxial silicon buries the donors — atom-precise, serial, and without a foundry equivalent.
verdict: Eleven qubits at atom precision prove the physics; with one practitioner, no merchant tool and no published parallel-write scheme, this stays a boutique process whatever the 2033 target says.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A hydrogen-terminated Si(100) surface is the resist. The tip removes hydrogen from selected dimers by electron-stimulated desorption; phosphine adsorbs only on the bare silicon; an anneal incorporates phosphorus substitutionally; low-temperature epitaxy buries the result. Hydrogen-resist patterning predates its qubit use by two decades; UNSW's Simmons group made a single-atom transistor in 2012 [D][1] and SQC — branding the flow PAQMan — an 11-qubit processor in 2025 [D][2].
Coordinates: engineered placement of a natural dopant, no mobility and no control step, Pauli error once fabricated, a fabrication class with no CMOS analogue.

## Physics & limits
Throughput is the floor, structurally: one tip visits one site at a time, so the process scales as O(N) in qubits where photolithography scales as O(1) in wafers. In-plane registration inside the desorption window is near a lattice constant, but the donor's final position carries ~3 nm of uncertainty from segregation and diffusion during incorporation and encapsulation: the limiting step is thermal, not lithographic. Encapsulation temperature is the real trade: hot enough for good epitaxy moves donors, cold enough to freeze them leaves defects that dephase the electron. Only parallel exposure changes the scaling law.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2012 | first single-atom transistor from a deterministically placed donor | UNSW | [D][1] |
| 2025-12-17 | 11 qubits (9 nuclear, 2 electron ancilla), gates 99.10–99.99%, Bell to 99.5%, GHZ over eight nuclei | SQC | [D][2][G:SQC-11Q-2025-12] |

Dominant term: device count. Every STM-donor device is fabricated individually; no parallel process exists at any scale and no placement-yield distribution is published.

## Manufacturing, materials & supply chain
No vendor sells a turnkey donor-placement tool: the equipment (UHV STM, phosphine handling, epitaxy) is merchant, the recipe is not, so no second source can be procured. Feedstock is no longer scarce: enriched ²⁸Si from ASP Isotopes and, from 2026-07-16, US DOE silane at 99.9999% ²⁸Si [P][8]. SkyWater supplies US resonators and packaging (2025-11-20) [C][4], and IonQ, a competing platform vendor, closed its ~USD 1.8 B acquisition of SkyWater on 2026-07-31 [G][5] — the sharpest supply risk here. Export control does not bite: no ECCN covers STM lithography and 4A906 starts at 34 qubits [G][7]. Burden at scale is unknown — no device beyond eleven qubits exists.

## Role in the stack
Provides the donor-spin carrier and, through it, hyperfine-gated registers and spin-to-charge readout; it substitutes for foundry CMOS at placement, trading wafer throughput for unmatched precision. Nothing else in the stack requires it — the strategic weakness: a defect here cannot be routed around, and no other node gains from progress on it. Verification: the 11-qubit fidelities come from one paper by the only group practising the process [D][2] — no second fabricator, and three fidelity framings across preprint, journal and main report.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| SQC | developer | Australia | Sole practitioner of STM donor placement | [D][2] |
| SkyWater Technology | supplier | USA | Resonators and packaging | [C][4] |
| IonQ | supplier | USA | Owns SkyWater since 2026-07-31 | [G][5] |
| NVIDIA | supplier | USA | NVQLink interconnect, SQC among 17 builders | [C][6] |

**Money.** 2025-11-06 · SQC · QBI Stage B · up to USD 15 M · DARPA · awarded [G:QBI-STAGEB-2025-11]. 2026-03-24 and 2026-06-11 · SQC · equity · A$60 M combined · Australia's NRFC · closed [G:SQC-NRFC-2026]. 2026-06-11 · SQC · investment · undisclosed · Firgun Ventures · announced [C][3]. 2026-07-31 · IonQ · acquisition of supplier SkyWater · ~USD 1.8 B · closed [G][5].

**Market & supply chain.** There is no market: one operator, no merchant process. Cost per placed donor is unpublished, so unit economics cannot be checked against the 2033 target. Funds G2 and G3; G4 needs parallelisation that does not exist.

**IP & standards.** Foundational patents trace to the UNSW/Simmons line; no dated family count from a named database as of 4 Sep 2026, and no standard covers atom-precision placement.

**Roadmaps & track record.** SQC (2026-06 · commercial scale by 2033 [R][G:SQC-NRFC-2026] · unmet, eleven qubits published). "Continuous scaling" and "a million qubits" appear in company material with no published mechanism [C][3], so the target is unfalsifiable rather than ambitious.

**Strategic reading.** If a parallel-write scheme appears, a decade of recipe knowledge compounds into a real moat. Without one, the precision that makes the process attractive is what caps it, and value migrates to whoever puts donors in a foundry flow.

*Open niche:* at these device counts, per-device characterisation beats fleet statistics. Isolating the fabrication-error tail — placement scatter, incomplete desorption, encapsulation defects — from gate and readout error needs no fab.

## Outlook & open questions
Confirm/demote (12–24 months): a dated parallel-fabrication announcement or a device beyond eleven qubits confirms a path past boutique scale; neither by 2028 demotes this to a physics tool. Best case 2029: above fifty donors with published yield. Worst case: a single-laboratory capability. Open: (1) is multi-tip or templated exposure feasible; (2) does SkyWater's new owner keep the relationship; (3) does anyone publish a placement-yield distribution.

## Sources
[1] Fuechsle, Miwa, Mahapatra, Ryu, Lee, Warschkow, Hollenberg, Klimeck, Simmons (UNSW) · "A single-atom transistor" · Nature Nanotechnology 7, 242–246 · 2012 · https://www.nature.com/articles/nnano.2012.21 [D]
[2] Edlbauer, Wang, Huq et al. (SQC) · "An 11-qubit atom processor in silicon" · Nature 648, 569–575; preprint arXiv:2506.03567 · 2025-12-17 · https://www.nature.com/articles/s41586-025-09827-w [D]
[3] SQC · newsroom and technology pages (Bluefors 2025-09-29, AMD 2026-04-07, Firgun Ventures 2026-06-11, PAQMan process) · company pages · accessed 2026-09-04 · https://sqc.com/news/ [C]
[4] SQC · "SkyWater x SQC: Advancing Hybrid Quantum-Classical Computing" · company release · 2025-11-20 · https://sqc.com/news/skywater-and-sqc-advancing-hybrid-quantum-classical-computing [C]
[5] IonQ · "IonQ Completes Acquisition of SkyWater Technology" · company release · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[6] NVIDIA · "NVIDIA NVQLink connects quantum and GPU computing" (17 QPU builders incl. SQC) · newsroom · 2025-10-28 · https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing [C]
[7] US Bureau of Industry and Security · "Implementation of Additional Export Controls: Quantum Computing Items" (ECCN 4A906, 3A904) · Federal Register · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and [G]
[8] US DOE Office of Isotope R&D and Production, via HPCwire · "DOE Advances Domestic Supply of Silicon, Germanium Isotopes for Quantum Computing" · 2026-07-16 · https://www.hpcwire.com/off-the-wire/doe-advances-domestic-supply-of-silicon-germanium-isotopes-for-quantum-computing/ [P]

## Open verification items
- Placement precision: no primary measurement of the incorporated-donor position distribution was located, so ~3 nm is used and the underlying distribution is listed as unpublished.
- SQC's newsroom dates the NVIDIA announcement 2025-10-29; NVIDIA's own newsroom dates the NVQLink launch 2025-10-28. The NVIDIA date is used.
- No dollar amounts disclosed for the Firgun Ventures investment or the SkyWater and AMD agreements; the A$60 M NRFC total is not itemised by tranche on SQC's pages.
- No parallelisation scheme for STM donor placement has been published by SQC or any other group, and no SQC statement was found on IonQ's acquisition of SkyWater.
