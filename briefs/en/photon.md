---
id: photon
name: Single photon (discrete variable)
layer: "1 Carrier"
tier: 1
status: demonstrated
since: 2001
one_line: "A qubit carried by one optical quantum in path, time-bin or polarisation modes; entangling is probabilistic and the only error is loss."
verdict: "Best component metrics of any platform, worst system result: no photonic logical qubit exists as of 2026-09-03 and loss sits 20–24× above threshold."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A discrete-variable photonic qubit encodes one bit in which of two optical modes a single quantum occupies — two waveguides (path/dual-rail), two time slots, or two polarisations. Nothing in it decoheres: at 1550 nm the quantum carries 0.8 eV, four orders above room-temperature thermal energy, so there is no T1 and no T2. The photon either arrives intact or does not, so the error model is erasure with known location and the problem is transport, not isolation. Dual-rail as an error-suppressing encoding dates to Chuang and Yamamoto (1995); the platform starts with Knill, Laflamme and Milburn (2001), who proved linear optics, single-photon detection and feed-forward universal — at the price of making every two-qubit interaction probabilistic [D][1][G:DUALRAIL-LINEAGE].

Coordinates, from the graph record:
- **a — affinity:** 0.25, near the fabricated end; the photon is natural, the mode defining the qubit is lithography.
- **b — time, entangling:** 10⁻⁷ s per layer, heralded — fusion succeeds with probability ≤ 1/2 unless boosted.
- **c — readout:** single-photon detection, ~10⁻⁸ s, destructive, no mid-circuit measurement.
- **d — mobility:** flying; transport is free, standing still is what costs.
- **e — control:** electro-optic, driven from room temperature though the chip sits near 2 K.
- **f — error structure:** loss, seen by the code as erasure.
- **g — manufacturing:** photonic integrated circuit.

## Physics & limits

Two indistinguishable photons meeting on a beamsplitter bunch, and detecting the right output pattern projects the remaining modes into an entangled state. Because the projection succeeds only sometimes, a fusion network must over-attempt and repair failures with redundancy in the resource state.

The floor is a loss budget and every element spends against it. In Omega: fibre-to-chip 52 ± 12 mdB, splitter 0.5 ± 0.2 mdB, barium-titanate switch 100 mdB insertion, single-mode SiN 1.8 ± 0.2 dB/m (0.5 dB/m multimode) [D][3][G:PSIQ-OMEGA-METRICS-2025]. Theory tolerates 2.7% per-photon loss with 6-ring resource states, up to 17% with 168-qubit states nobody can build [S][15]. A photon crossing thirty switches has spent 3 dB — half of itself. Xanadu, on the continuous-variable side but with the same optics, quantifies the gap: 24.1× above threshold in 2026, targeting 1.0× in 2030 [C][16][G:XANADU-SPAC-2026-03].

The standard fix for probabilistic sources costs the budget it protects: four-wave mixing must run at ~1% heralding probability to suppress multi-photon events, so near-determinism needs multiplexing depth around ten — ten times the switches at 100 mdB each. Deterministic quantum-dot sources break that circle, which is why 71.2% system efficiency, first above the 2/3 loss-tolerance threshold, is the most consequential source number on record [D][2]. Secondary failure modes: distinguishability (mismatch degrades HOM visibility and appears as Pauli rather than erasure error), multi-photon contamination, dark counts, and feed-forward latency — the photon waits in delay while a classical decision is made, and delay is loss.

## Engineering state of the art

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-11 | QD source system efficiency 71.2% — first above the 2/3 threshold | USTC (Ding et al.) | [D][2] |
| 2025-02 | Omega: purity 99.5%, HOM 99.5%, fusion Bell 99.22 ± 0.12%, chip-to-chip Bell 99.72 ± 0.04% over 42 m, on-chip SNSPD median efficiency 93.4%, ~2 K, 300 mm | PsiQuantum / GlobalFoundries | [D][3] |
| 2025 | Commercial QD source S1: 55.3% system efficiency, 26.2 MHz detected rate | Sparrow Quantum | [D][4] |
| 2025-10 | 12-qubit Belenos/Lucy delivered to CEA TGCC | Quandela | [C][7] |
| 2026 | QD source S3: raw HOM visibility 97.1 ± 0.1%, purity 99.9 ± 0.1% | Sparrow Quantum | [D][4] |
| 2026-05 | Gaussian boson sampling, 3,050 photon clicks | USTC (Jiuzhang 4.0) | [D][5] |
| 2026-07 | 8-qubit universal MBQC subsystem (Carina) delivered to DLR QCI | QuiX Quantum | [C][8] |

Best-demonstrated and typical-at-scale are further apart here than on any other platform: component fidelities are excellent, the largest fielded universal DV machine is twelve qubits [C][7], and no photonic logical qubit exists as of 2026-09-03. The dominant error term is not a fidelity but per-photon survival through the switch network.

## Manufacturing, materials & supply chain

Foundry detail belongs to the photonic-IC brief; specific to the carrier is that two incompatible source technologies compete. **SFWM** in SiN or Si rings is monolithic with the circuit, CMOS-compatible, III-V-free and runs at 2 K beside the detectors, but is probabilistic and buys determinism with multiplexing switches (PsiQuantum, Xanadu, QuiX). **Quantum dots** (InAs/GaAs in photonic-crystal waveguides) are near-deterministic — 71.2% in the lab [D][2], 55.3% shipped, 20–35% typical [D][4] — but need ~4 K, emit near 900–950 nm rather than telecom, grow at random positions and energies (a yield problem), and must be heterogeneously integrated (Quandela, Sparrow).

Single points of failure: one 300 mm line of record [C][G:GF-QTS-2026-05]; one merchant deterministic-source vendor [D][4]; a switch base on two small thin-film-lithium-niobate suppliers [P][G:TFLN-FUNDING-2024-09]. No vendor publishes a per-qubit cost or system price. Export exposure runs through the September 2024 US quantum controls and the EU dual-use list; the exact classification of single-photon sources is unverified.

## Control, readout & I/O burden

Drivers are room-temperature electro-optics and the chip sits at ~2 K, where a cryoplant has roughly a thousand times the cooling capacity available at 10 mK — the platform's real scaling advantage. The wall is channel count and latency, not power. Every operation ends in destructive detection, so channels scale with mode count: 10³ modes is ordinary cryogenic wiring, 10⁴ needs multiplexed readout, 10⁶ needs something like the row-column architecture behind the 400,000-pixel SNSPD camera [D][18] plus decision logic inside the cryostat. At 0.5 dB/m multimode SiN, holding a photon 100 ns costs ~20 m of waveguide and 10 dB, so feed-forward must be nanosecond-class. QuiX names fast feed-forward, with sources, as the two problems its 2026 system must solve [C][11].

## Role in the stack

The node sits on the fusion-based photonic path (PsiQuantum, Quandela, QuiX). It requires the photonic-IC foundry for sources and waveguides, and provides photons to linear-optical fusion, the resource-state factory, time-bin and path encodings, and single-photon detection. It replaces continuous-variable squeezed light; switching costs the whole stack — different sources, homodyne rather than click detection, GKP rather than fusion codes. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: none is defined, the architecture being measurement-driven; the native 1.0×10⁻⁷ s clock stands instead, and multiplexing and fusion retries set the effective logical rate. Empty neighbouring slots are conspicuous: no deterministic photon–photon gate, no photonic memory good enough for multiplexing at scale (ORCA's rubidium hollow-core fibre is the only commercial attempt), no non-destructive mid-circuit measurement.

## Verification (QCVV)

HOM visibility, g²(0) by Hanbury Brown–Twiss, and fusion Bell fidelity by tomography on coincidence-post-selected data are the standard instruments. What they do not capture is loss: nearly every photonic fidelity is conditioned on the photons having been detected, so the error that dominates the machine is divided out of the number describing it. "Fusion Bell fidelity 99.22%" and "24× above the loss threshold" describe the same optics; treating the first as the platform's error rate mis-ranks it by two orders of magnitude.

Conflicts. (i) The main report's 0.5 dB/m is the multimode figure; single-mode SiN in Omega is 1.8 ± 0.2 dB/m [D][3][G:PSIQ-OMEGA-METRICS-2025] — both used here, labelled. (ii) QD efficiency 71.2% (lab) vs 55.3% (shipped) vs 20–35% (typical) is a lab-to-product gap; use the product figure [D][2][4]. (iii) Jiuzhang 4.0's advantage is contested by loss-exploiting classical spoofing [D][5]. (iv) Sparrow's "highest HOM visibility to date" is an unreplicated vendor claim [D][4]. Omega has never been independently reproduced.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | US / AU | Fusion-based DV on 300 mm GlobalFoundries; Omega chipset; Brisbane, Chicago | [D][3][G:PSIQ-QBI-C-2026-07] |
| Quandela | developer | FR | QD sources plus own processors; 12-qubit Lucy at CEA | [C][7][G:QBI-QBIT-2026] |
| QuiX Quantum | developer | NL | Universal MBQC photonic processors; Carina at DLR | [C][8][C][11] |
| ORCA Computing | developer | UK | Time-bin boson sampling with Rb memory; nine PT-1 units fielded | [P][9] |
| Xanadu | developer | CA | CV/squeezed route — the in-platform substitution threat | [C][16][G:XANADU-SPAC-2026-03] |
| Sparrow Quantum | supplier | DK | Merchant deterministic QD single-photon source chips | [D][4][P][13] |
| USTC (Pan group) | research | CN | Jiuzhang boson sampling; best QD source efficiency on record | [D][2][D][5] |
| Photonic Inc. | developer (adjacent) | CA | T-centres in silicon: spin-photon interface, telecom-band links | [P][19][G:PHOTONIC-200M-2026-05] |
| GlobalFoundries | supplier | US | 300 mm photonic quantum manufacturing, integrated SNSPD | [C][G:GF-QTS-2026-05] |
| DARPA | funder | US | QBI Stage A/B/C and US2QC validation money | [G:QBI-STAGEB-2025-11] |
| CEA/GENCI, DLR QCI | users | FR / DE | Buy and host photonic systems for HPC centres | [C][7][C][8] |

**Money.**
- 2023-11-07 · Quandela · round, €50 M · Serena, Crédit Mutuel Innovation, EIC Fund, Bpifrance, OMNES, Quantonation; France 2030 · closed [C][10]
- 2024-04 · PsiQuantum · Australian federal + Queensland commitment, A$940 M · definitive [P][14]
- 2025-04-10 · Sparrow Quantum · Series A, €21.5 M ($24 M) · lead undisclosed · closed [P][13]
- 2025-07-10 · QuiX Quantum · Series A, €15 M · Invest-NL and EIC Fund co-lead; PhotonVentures, Oost NL, FORWARD.one · closed [C][11]
- 2025-09-10 · PsiQuantum · Series E, $1 B at $7 B · BlackRock, Temasek, Baillie Gifford · closed [G:PSIQ-1B-2025-09]
- 2025-09 · PsiQuantum · DARPA QBI Stage C via US2QC, $31.8 M · announced [P][12]
- 2026-05-12 · Photonic Inc. · round, $200 M at $2 B, $350 M cumulative · Microsoft among returning investors · closed [P][19]
- 2026-05-21 · PsiQuantum · CHIPS letter of intent, $100 M · US Dept of Commerce · LOI, non-binding [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Quandela · DARPA QBI/QBIT Stage A selection · amount undisclosed · announced [G:QBI-QBIT-2026]
- 2026-06-19 · Sparrow Quantum · EuroHPC Grand Challenge (EU-SCALE), €300,000 · EuroHPC JU · in preparation [P][13]
- 2026-07-22 · PsiQuantum · DARPA QBI Stage C expanded agreement, $125 M · announced [G:PSIQ-QBI-C-2026-07]

**Market & supply chain.** The enabling layer is thin: one merchant 300 mm quantum-photonics offering [C][G:GF-QTS-2026-05], one merchant deterministic-source vendor [D][4], a switch base on two small TFLN suppliers [P][G:TFLN-FUNDING-2024-09], with open-access European capacity under PIXEurope (~EUR 400 M, 2024-11-24) [G:PIXEUROPE-2024-11]. Unit economics are unquotable: Quandela's machines for OVHcloud and CEA, QuiX's for DLR and the nine ORCA PT-1 units all sold at undisclosed value. G6 pays today, photons being the only carrier that moves; G1 and G5 pay marginally via sampling and optimisation demos; G4 is the whole PsiQuantum and Quandela thesis but is funded by governments, not customers; G3 pays photonics nothing, there being no logical qubit to sell.

**IP & standards.** The one dated grant surfaced is ORCA Computing US 12,437,225, "Linear-optical encoded GHZ measurements and fault-tolerant quantum computation and communication", filed 2023-10-16, granted 2025-10-07 [G:ORCA-DUALRAIL-PATENT-2025]. No dated patent count from a named database was obtained. Open-source stacks are vendor-led (Quandela's Perceval, Xanadu's PennyLane); no photonic interoperability standard exists.

**Roadmaps & track record.** PsiQuantum (promised 2024-04 · for end-2027 · commercially useful Brisbane machine; status: site moved to Moreton Bay Central, groundbreaking slipped to 2026-06, cryoplant 2H 2027, no 2026 hardware publication) — the money and DARPA validation are real, the date is not. Quandela (promised · for 2025 · first logical qubit; missed) and (promised · for 2028 · 50 logical qubits; pending) — ships machines on schedule, misses fault-tolerance milestones. QuiX (promised 2025-07 · for 2026 · first-generation universal computer; status: Carina delivered 2026-07, commissioning pending) — credible on delivery, unproven on universality. ORCA (promised · for 2026 · PT-3; undelivered) — ships units, but non-universal ones. Xanadu (promised 2026-08-31 · for 2028–31 · fault tolerance 2028–29, 1,000+ logical by 2031) — the only photonic roadmap publishing its distance from threshold.

**Strategic reading.** If DV photonics works, value migrates to the fab, the detector base and whoever owns the low-loss switch; the loser is the cryogenic-electronics complex around millikelvin qubits, because 2 K is cheap. Substitution threats sit inside photonics as much as outside: CV/GKP (Xanadu) and spin-photon hybrids (Photonic Inc.) both claim to sidestep probabilistic sources, while atoms and ions already have logical qubits — so photonics must win on manufacturing volume, not physics. Bargaining power sits with the foundry and the few firms able to make a deterministic source; no platform vendor gains leverage until one shows an encoded qubit.

*Open niche:* two entry points exist for a small QCVV/SFQ house. First, benchmarking: every photonic figure of merit is post-selected, and no accepted protocol reports a fusion-network fidelity together with its acceptance rate. Loss-inclusive metrics — acceptance-weighted fusion fidelity, a cross-chip multi-source indistinguishability test, resource-state certification that does not divide out loss — would be adopted quickly, because vendors currently cannot be compared. Second, single-flux-quantum logic is the natural classical partner: nanosecond feed-forward beside thousands of detector channels at 2–4 K is the acknowledged unproven system-level element, and a measured SFQ-driven feed-forward latency would be a new datum in a field that has none.

## Outlook & open questions

**Confirm** if PsiQuantum publishes a fusion-network result with measured end-to-end loss, or DARPA advances it past Stage C; if QuiX commissions Carina and runs a universal feed-forward MBQC circuit by mid-2027; if any group demonstrates an encoded photonic qubit with measured error suppression. **Demote** if there is no PsiQuantum hardware publication by end-2027 while Brisbane slips again; if Quandela reaches end-2027 without one logical qubit while holding a 50-logical-by-2028 target; if PT-3 stays undelivered through 2027.

Best case 2029: deterministic sources above 70% system efficiency on a foundry PIC, switch loss below 50 mdB, a first photonic logical qubit, a utility-scale machine in commissioning. Worst case 2029: loss within 3× of today, no logical qubit, the computing claim migrating to spin-photon hybrids while photonics consolidates into networking.

Open questions. (1) Can QD sources be integrated at foundry scale without breaking the 2 K budget or abandoning telecom wavelengths? (2) Is there a feed-forward technology whose optical delay costs less loss than the multiplexing it enables? (3) How much loss is heralded rather than silent? (4) Why has PsiQuantum published nothing since Omega? (5) Do resource-state factories scale sub-linearly in switch count?

## Sources

[1] Knill, Laflamme, Milburn — linear-optics universality, Nature 409, 46 (2001-01-04) — https://arxiv.org/abs/quant-ph/0006088
[2] Ding et al. (USTC) — QD source, 71.2% system efficiency, arXiv:2311.08347 (2023-11) — https://arxiv.org/abs/2311.08347
[3] PsiQuantum — Omega manufacturable photonic platform, Nature (2025-02) — https://www.nature.com/articles/s41586-025-08820-7
[4] Sparrow Quantum et al. — deterministic QD sources, specifications, arXiv:2511.23232 (device rows vendor data [C]) — https://arxiv.org/html/2511.23232v1
[5] USTC — Jiuzhang 4.0, Nature (2026-05); arXiv:2508.09092 — https://www.nature.com/articles/s41586-026-10523-6
[6] Xanadu — chip packaging, PRNewswire (2026-06) [C] — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html
[7] Quandela — Lucy delivered to EuroHPC/GENCI at CEA TGCC (2025-10) [C] — https://www.quandela.com/about-us/newsroom/quandela-delivers-lucy-the-most-advanced-photonic-quantum-computer-worldwide-to-eurohpc-and-genci-at-ceas-tgcc/
[8] QuiX Quantum — Carina delivered to DLR QCI (2026-07) [C] — https://www.quixquantum.com/news/quix-quantum-delivers-carina-core-hardware-platformto-dlr-qci
[9] postquantum.com — ORCA Computing profile, PT-1/PT-2, GXC acquisition (2026-09-03) [P] — https://postquantum.com/quantum-computing-companies/orca-computing/
[10] Quandela newsroom — €50 M round (2023-11-07) [C] — https://www.quandela.com/about-us/newsroom/quandela-secures-e50-million-to-support-international-expansion/
[11] QuiX Quantum newsroom — €15 M Series A (2025-07-10) [C] — https://www.quixquantum.com/news/quix-quantum-series-a
[12] Quantum Computing Report — PsiQuantum $125 M DARPA QBI expansion (2026-07-22) [P] — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/
[13] The Quantum Insider — Sparrow EuroHPC EU-SCALE (2026-08-26) [P]; Quantum Computing Report — Sparrow Series A (2025-04-10) [P] — https://thequantuminsider.com/2026/08/26/sparrow-quantum-eurohpc-quantum-grand-challenge-funding/ ; https://quantumcomputingreport.com/sparrow-quantum-secures-e21-5m-24m-usd-in-series-a-funding-to-advance-photonic-quantum-chip-production/
[14] Forbes Australia — PsiQuantum Brisbane site change, A$940 M (2026) [P] — https://www.forbes.com.au/news/innovation/psiquantums-stalled-quantum-plant-to-break-ground-after-location-switch/
[15] Bartolucci et al. — fusion-based quantum computation, Nature Communications 14, 912 (2023); arXiv:2506.11975 — https://www.nature.com/articles/s41467-023-36493-1
[16] Xanadu — roadmap to 1,000+ logical qubits (2026-08-31) [C] — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html
[17] PsiQuantum newsroom — Series E, CEO change [C] — https://www.psiquantum.com/news-import/psiquantum-1b-fundraise
[18] Oripov et al. (NIST/JPL) — 400,000-pixel SNSPD camera, Nature 622, 730 (2023-10-25) — https://www.nature.com/articles/s41586-023-06550-2
[19] Quantum Computing Report — Photonic Inc. $200 M at $2 B (2026-05-12) [P] — https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/
[20] DARPA — QBI Stage B selection (2025-11-06) [G] — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[21] NIST — CHIPS letters of intent (2026-05-21) [G] — https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[22] imec — PIXEurope pilot line selected (2024-11-24) [G] — https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line
[23] Xanadu — on-chip GKP states, Nature (2025) — https://www.nature.com/articles/s41586-025-09044-5
[24] Xanadu — Aurora, Nature (2025) — https://www.nature.com/articles/s41586-024-08406-9

## Open verification items

- Exact date and instrument mix (equity vs loan vs grant) of the A$940 M Australian commitment to PsiQuantum; source [14] gives only the total and the two governments.
- Sparrow Quantum Series A lead investor and cumulative funding — primary report paywalled; only date and amount confirmed.
- ORCA Computing funding history: only a secondary range (~£8–15 M Series A plus 2023–24 capital); no primary release, no cumulative total, no valuation.
- Export-control classification of single-photon sources and detectors under the September 2024 US quantum rule — ECCN not confirmed, deliberately not stated in the text.
- Quandela cumulative funding and any 2025–26 round; €50 M (2023-11-07) is the most recent primary release located.
- PsiQuantum's $31.8 M Stage C award is dated 2025-09 in some sources but framed inside a July 2026 package in others; the $125 M expansion date (2026-07-22) is firm.
- Xanadu's 2026 SPAC close (~$302 M) and CAD 195 M Toronto funding are omitted from the Money ledger here as continuous-variable events.
- Source conflicts carried forward: SiN loss 0.5 dB/m (multimode) vs 1.8 ± 0.2 dB/m (single-mode); QD efficiency 71.2% (lab) vs 55.3% (product) vs 20–35% (production); Jiuzhang 4.0 advantage contested by classical spoofing.
