---
id: cx_switch
name: Photonic switching / routing (EO, feed-forward)
layer: 4 Connectivity / transport
status: demonstrated
since: 2015
one_line: Electro-optic and MEMS switches route photons between waveguides on a real-time heralding decision, the loss-dominated transport layer every photonic architecture shares.
verdict: Best published in-line switch loss is 100 mdB (PsiQuantum BTO), ~14x the ~7 mdB fault-tolerance budget as of 4 Sep 2026; non-volatile devices fix static power, not loss.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An electro-optic or mechanical element inside a Mach–Zehnder interferometer sets its splitting ratio, so a mesh implements any unitary and, driven by an earlier heralding click, routes photons in real time. The lineage is Carolan's six-mode, 15-MZI chip of 2015 [D][12] — thermo-optic, reconfigurable "in seconds", the opposite end of the speed and power axis from what fusion needs. Everything since has tried to keep that programmability while stripping its loss and static power.
- b/e: switching in ns–µs (10⁻⁶·⁰ s), electro-optic, room-temperature drivers; not itself entangling.
- d/g: flying photons routed in photonic-IC waveguides; every stage taxes the loss budget.

## Physics & limits
Loss is multiplicative, so the architecture fixes a per-stage budget the device meets or the machine does not exist: against a total photon budget of order 0.5 dB across a fusion network's depth, the per-switch allowance is ≈7 mdB [D][1]. Fusion-based fault tolerance tolerates 2.7% per-photon loss with six-ring resource states, 17% only with 168-qubit states nobody can build [D][16]. The families trade differently: thermo-optic shifters are low-loss but dissipate milliwatts each and switch in µs, unusable at 2 K across 10⁴ channels; barium titanate and thin-film lithium niobate switch in ns at low power but add material and transition loss. The second failure mode is finite extinction: amplitude leaked to the wrong port is an unheralded error, not a loss. Moving the floor needs higher electro-optic coefficients (barium titanate's effective r is ~30× lithium niobate's, so shifters shorten and lose less), lower-loss material transitions and non-volatility.

## Engineering state of the art
Best published in-line switch: PsiQuantum's barium titanate at 100 mdB insertion, with 52(12) mdB fibre-to-chip coupling at ~2 K [D][3][G:PSIQ-OMEGA-METRICS-2025]. Aurora is the only system-scale figure: 35 chips, 0.19 dB per MZI, ~14 dB total loss, no error-corrected computation [D][1]. The 2026 non-volatile barium-titanate array switches in 80 ns at 1.48 dB per cell with zero static power once set [D][2] — a static-power result, not a loss one. Dominant error: cumulative insertion loss, then coupling.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-01 | 0.19 dB/MZI; ~14 dB system loss; ≈7 mdB requirement | Xanadu | [D][1] |
| 2025-02 | BTO switch 100 mdB; fibre-to-chip 52(12) mdB | PsiQuantum | [D][3] |
| 2026-06 | Non-volatile BTO cell: 80 ns, 1.48 dB, zero static power | UPV iTEAM | [D][2] |
| 2026-08 | Foundry-compatible MEMS switch, <1.5 dB, >30 dB extinction, ~20 nW | UC Berkeley | [P][11] |

## Manufacturing, materials & supply chain
Silicon nitride or thin-film lithium niobate waveguides, barium titanate for the active element, superconducting nanowire detectors on the same 300-mm wafer; PsiQuantum's runs at GlobalFoundries, which launched a quantum manufacturing unit on 2026-05-21 against a $375M CHIPS letter of intent [C][10]. Barium titanate on silicon is a deposition few lines can do; the merchant thin-film-lithium-niobate base is two venture-scale suppliers, HyperLight and Lightium [P][13]. Packaging is the second chokepoint: Xanadu's coupling result needed Corning fibre arrays and DISCO singulation [C][4]. No yield figure is public; no export-control category names photonic switches, the 2024 BIS rule reaching them only via ECCN 4A906 [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden
Feed-forward means the photon waits in a delay line while a cryogenic detector click is classified and the switch driven, which couples latency to loss — brutally on chip. At silicon-nitride propagation loss one nanosecond of on-chip delay costs a few tenths of a dB, more than the whole per-stage budget, while the same nanosecond in fibre at ≈0.2 dB/km is free: feed-forward lives in fibre and must resolve in nanoseconds. QuiX names feed-forward electronics as one of two problems its 2026 system must solve [C][5]. I/O scales with network depth, not qubit count; at 10⁴–10⁶ modes the binding constraints are detector channel count and the cryogenic power holding each switch in state.

## Role in the stack
Transport for both photonic families: fusion-based discrete-variable machines (PsiQuantum, Quandela, QuiX) and the continuous-variable/GKP path (Xanadu). It requires a photonic-IC foundry process and provides the routing that turns heralded fusion outcomes into a cluster state; nothing substitutes for it. Not a hub by reach, but every actor in the branch depends on the same number, making it the branch's single point of failure. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset — undefined here, the fusion architecture running no syndrome round; the ~1 µs floor is set by feed-forward and detector recovery, not the switch. Empty neighbouring slot: a sub-10 mdB non-volatile switch.

## Verification (QCVV)
Switch loss and extinction come from direct insertion-loss characterisation against on-chip reference paths — harder numbers than gate fidelities, and the least comparable, each vendor quoting a different boundary. Aurora's 0.19 dB is per MZI including interconnect; PsiQuantum's 100 mdB is the switch element alone; Xanadu's 0.085 dB/facet is fibre-to-chip, marketed as an industry benchmark [C][4] though PsiQuantum published 52(12) mdB for that interface a year earlier [D][3]. None should be summed or ranked without a common protocol, and none is replicated outside its originating group. System verification is a loss budget, not a logical-fidelity witness.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| PsiQuantum | developer | USA | BTO switches at 100 mdB, under DARPA V&V | [D][3] |
| Xanadu | developer | Canada | Aurora switch network; coupling and packaging | [D][1] |
| QuiX Quantum | developer | Netherlands | Feed-forward hardware; Carina at DLR | [C][5] |
| Quandela | developer | France | 12-qubit switched system at CEA | [C][6] |
| GlobalFoundries | supplier | USA | 300-mm line; $375M CHIPS letter of intent | [C][10] |
| DARPA | investor | USA | Stage C money buys BTO switch validation | [P][8] |

**Money.**
| Date | Actor | Event | Amount | Programme / lead | Status |
|---|---|---|---|---|---|
| 2025-09-10 | PsiQuantum | Series E | $1B at $7B | BlackRock, Temasek | closed [C][15] |
| 2026-03-26 | Xanadu | SPAC merger | ~$302M, 40% below plan | Crane Harbor | closed [C][9] |
| 2026-05-21 | US Commerce | CHIPS letters of intent | $375M, $100M | GlobalFoundries, PsiQuantum | LOI [G:CHIPS-LOI-2026-05] |
| 2026-07-22 | PsiQuantum | QBI Stage C expanded | $125M after $31.8M | DARPA | official [P][8] |
| 2026-08-28 | Xanadu | Toronto factory funding | CAD 195M | Government of Canada | closed [C][9] |

**Market & supply chain.** The enabling equipment is not quantum: 300-mm CMOS (GlobalFoundries), fibre-array assembly (Corning), wafer singulation (DISCO), a thin-film-lithium-niobate base of two small suppliers [P][13]. Concentration sits in mainstream chains where a photonic quantum company has no bargaining power and no second source for fibre-array attach. G3 and G4 pay for this component — no photonic logical qubit exists without closing the loss gap — G1/G5 do not.

**IP & standards.** No patent family specific to quantum photonic switching surfaced; the nearest adjacent grant is ORCA Computing's US 12,437,225 on linear-optical encoded GHZ measurements (2025-10-07) [G:ORCA-DUALRAIL-PATENT-2025]. Classical MZI-switch IP is extensive and non-quantum; PatSnap's counts are not disaggregated to this layer [P][G:PATSNAP-2026-06]. No standards body, no litigation, no shared feed-forward interface.

**Roadmaps & track record.** PsiQuantum (2024-04, for a useful machine by end-2027) — as of 4 Sep 2026 groundbreaking only in June 2026 after a site change [P][14], cryoplant targeted 2H 2027, no 2026 hardware publication; strong components, unevidenced system. Xanadu (2026-08-31, for 1.0× threshold loss in 2030 from 24.1×) — the field's first quantified roadmap, naming this component's gap. QuiX (2025-07, for a 2026 universal system) — Carina delivered July 2026, commissioning pending. Quandela — Lucy delivered, 2025 logical-qubit milestone missed.

**Strategic reading.** Whoever first ships a non-volatile sub-10 mdB switch owns the chokepoint for both photonic architectures at once, the requirement being encoding-agnostic; hence DARPA's Stage C buys validation of switches, packaging and cryogenics, not an algorithm. If the gap fails to close the branch loses together — no photonic fallback avoids switching — while matter-based modalities face no equivalent single-number gate. Leverage sits with GlobalFoundries, Corning and DISCO.

*Open niche:* A small QCVV house could define and run the missing common protocol for optical-fabric metrology: insertion loss, extinction and drift to a stated reference plane, per switch, per facet, per stage. The field quotes 0.19 dB, 100 mdB, 85 mdB and 1.48 dB as if comparable; no buyer can rank vendors without that normalisation.

## Outlook & open questions
Confirm/demote in 12–24 months: a sub-50 mdB non-volatile switch; independent replication of the 100 mdB figure; PsiQuantum's Brisbane cryoplant energised in 2H 2027; a feed-forward loop published under 100 ns. Best case 2029: single-digit-mdB non-volatile switching, Xanadu's 24.1× closing as promised. Worst case: loss plateaus near 100 mdB and photonic fault tolerance slips past 2031 for the whole branch. Open: does barium titanate yield at 300 mm; can fibre-array attach be second-sourced; does extinction bind once loss falls. Watch Xanadu's 2027 loss number.

## Sources
[1] Xanadu · Scaling and networking a modular photonic quantum computer (Aurora) · Nature · 2025-01 · https://www.nature.com/articles/s41586-024-08406-9
[2] Universitat Politècnica de València iTEAM, Lumiphase AG, CEA-Leti · Non-volatile barium-titanate photonic gate array · Nature Photonics · 2026-06-04 · https://www.nature.com/articles/s41566-026-01934-y
[3] PsiQuantum · A manufacturable platform for photonic quantum computing (Omega) · Nature · 2025-02 · https://www.nature.com/articles/s41586-025-08820-7
[4] Xanadu · Photonic chip packaging benchmark, 0.085 dB/facet, with Corning and DISCO · PR Newswire · 2026-06-10 · https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html [C]
[5] QuiX Quantum · Carina core hardware platform delivered to DLR QCI · company newsroom · 2026-07-14 · https://www.quixquantum.com/news/quix-quantum-delivers-carina-core-hardware-platformto-dlr-qci [C]
[6] Quandela · Lucy delivered to EuroHPC and GENCI at CEA's TGCC · company newsroom · 2025-10-23 · https://www.quandela.com/about-us/newsroom/quandela-delivers-lucy-the-most-advanced-photonic-quantum-computer-worldwide-to-eurohpc-and-genci-at-ceas-tgcc/ [C]
[7] QuiX Quantum · €15M Series A (Invest-NL, EIC Fund, PhotonVentures) · company newsroom · 2025-07-10 · https://www.quixquantum.com/news/quix-quantum-series-a [C]
[8] Quantum Computing Report · PsiQuantum secures $125M expanded DARPA agreement under QBI · 2026-07-22 · https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/ [P]
[9] Xanadu · Roadmap to over 1,000 logical qubits by 2031; SPAC and Canadian funding · GlobeNewswire · 2026-08-31 · https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html [C]
[10] GlobalFoundries · Launch of Quantum Technology Solutions; $375M CHIPS letter of intent · company press release · 2026-05-21 · https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ [C]
[11] Roy, Klawson, Luo, Zhi, Tang, Wu · Zero-change foundry-compatible silicon photonics MEMS optical switch · arXiv:2608.03146 · 2026-08-04 · https://arxiv.org/abs/2608.03146 [P]
[12] Carolan et al. · Universal linear optics (six modes, 15 MZIs, 30 thermo-optic shifters) · arXiv:1505.01182 · 2015 · https://arxiv.org/abs/1505.01182
[13] optics.org · Thin-film lithium niobate suppliers raise: HyperLight $37M Series B, Lightium $7M seed · 2024-09 · https://optics.org/news/lithium-niobate-in-vogue-as-thin-film-developers-raise-cash [P]
[14] Forbes Australia · PsiQuantum's stalled quantum plant to break ground after location switch (A$940M) · 2026-06 · https://www.forbes.com.au/news/innovation/psiquantums-stalled-quantum-plant-to-break-ground-after-location-switch/ [P]
[15] PsiQuantum · $1B Series E at $7B valuation; CEO change · company newsroom · 2025-09-10 · https://www.psiquantum.com/news-import/psiquantum-1b-fundraise [C]
[16] Bartolucci et al. · Fusion-based quantum computation (loss thresholds 2.7% and 17%) · Nature Communications 14, 912 · 2023-02-17 · https://www.nature.com/articles/s41467-023-36493-1

## Open verification items
The graph record's "recent 30 mdB" switch figure could not be traced to any publication; the best located in-line figure is 100 mdB (PsiQuantum) and the most recent device is a 1.5 dB MEMS switch. Whether 0.19 dB/MZI (switch plus interconnect), 100 mdB (switch element) and 85 or 52 mdB (fibre-to-chip) share a reference plane — no source reconciles them. The main report's "waveguide loss 0.5 dB/m" for Omega conflicts with the paper's single-mode silicon-nitride figure of 1.8(2) dB/m [G:PSIQ-OMEGA-METRICS-2025]; I use neither as a switch number. Institutional affiliation for the MEMS switch authors was not returned by the arXiv abstract page.
