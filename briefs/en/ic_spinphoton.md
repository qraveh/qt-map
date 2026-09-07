---
id: ic_spinphoton
name: Spin–photon solid-state link (SiV, NV, T-centre)
layer: "9 Interconnect"
status: demonstrated
since: 2013
one_line: Heralded photonic entanglement between separated solid-state spin registers — diamond NV and SiV centres, silicon T centres — through deployed telecom fibre.
verdict: Inter-cryostat gates exist on both hosts, unconditionally on NV (63–64%) and only post-selected on T centres. Rates of 0.0075–1 Hz sit 10⁵–10⁷ below the 200 kHz vendors promise; loss, not coherence, is why.
updated: 2026-09-04
---

"Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics)."

## Identity & lineage
Each node is a spin qubit in a solid — a nitrogen-vacancy or silicon-vacancy centre in diamond, or a silicon T centre — whose optical transition emits a photon entangled with the spin. Photons from two nodes interfere on a beamsplitter; a detection pattern heralds spin–spin entanglement without trusting the channel, so loss costs attempts, not fidelity.  Delft demonstrated the first heralded solid-state version across 3 m in 2013 [D][10]; everything since has pushed that protocol into deployed telecom fibre.
- Mobility: the carrier flies (a photon in fibre); both spins stay fixed.
- Error structure: loss-dominated; conditional fidelity and unconditional rate must be quoted together.

## Physics & limits
The floor is the product of collection, conversion and transmission efficiencies, entering the rate quadratically for two-photon protocols and linearly for the single-photon protocol Delft uses at metropolitan scale [D][2]. Only a small fraction of an emitter's photons land in the coherent zero-phonon line, and a 35 km deployed urban loop costs a further 17 dB [D][1]. Wavelength decides whether conversion is needed — NV at 637 nm and SiV at 737.2 nm require it (Harvard converts to 1,350 nm), while a T centre emits natively near 1,326 nm, skipping that stage but paying with a weaker transition [P][5]. Spin coherence is not the constraint: nuclear memories hold entanglement beyond 2 s [D][1], far longer than the 0.25–0.35 ms fibre round trip. The one lever that moves the floor is cavity enhancement — a fibre microcavity around one NV raised resonant collection roughly tenfold, ~0.05% to ~0.5%, keeping echo coherence above 100 µs [D][G:QUTECH-NV-CAVITY-2026-01]; two more such steps reach the trapped-ion regime.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-04 | NV, nodes 10 km apart over 25 km deployed fibre with telecom L-band conversion: F = 0.534 at 0.022 s⁻¹ | QuTech/Delft | [D][2] |
| 2024-05 | SiV: F = 0.69(7) between nuclear memories over a 35 km deployed Boston loop; 0.86(3) electron–electron at 20 m, ≤1 Hz | Harvard | [D][1] |
| 2024-06 | T centre, two modules in separate cryostats over ~40 m fibre: Bell F = 0.60(8), ~7.5 mHz; teleported-CNOT sequence post-selected, no gate fidelity | Photonic Inc. | [P][5] |
| 2026-05 | Unconditional teleported CNOT between NV registers in separate cryostats: 4-qubit GHZ 64(4)%, CNOT-mediated state 63(4)% | QuTech/Delft | [D][G:QUTECH-NV-TELEPORT-CNOT-2026-05] |

The dominant term is collection and heralding efficiency, not spin coherence or in-node gate error.

## Manufacturing, materials & supply chain
Diamond nodes need quantum-grade CVD material, for which Element Six (UK) is the reference supplier [P][G:NV-DIAMOND-ACTORS-2026-07], plus nanophotonic cavities whose yield is the blocker: a 2026 Delft tin-vacancy study fabricated 327 devices across two chips and found two with coherent cooperativity above 1 [D][G:QUTECH-SNV-FUNDING-2026] — the number to quote against any 10²-node proposal. Silicon T centres trade emitter quality for process maturity: implantation into enriched ²⁸Si on a CMOS line at ~1.5–4 K, not millikelvin [P][6]. Both ends depend on nanowire detectors from a five-vendor merchant base [P][G:SNSPD-VENDORS-2026]. No export-control classification names spin–photon links.

## Control, readout & I/O burden
Per node: a cryostat, microwave spin control, resonant lasers for initialisation and readout, a conversion stage unless the emitter is already telecom, phase-stabilised fibre to the midpoint, and detectors. The binding burden is duty cycle, not latency: at 0.022 s⁻¹ one link spends 45 s per Bell pair while stabilisation loops run continuously. Ten nodes are an experiment; 10² at sub-Hz cannot serve a distributed processor, and 10³ needs multiplexed emitters and detector arrays nobody has fielded.

## Role in the stack
It requires a colour-centre spin register and single-photon detection; without low-dark-count detectors heralding fails outright. It provides for nothing further and tops the defect-spin network path. On any distributed architecture it is the pacing term: no code runs on the defect path, so in place of a sum of the syndrome round: gate layers + transport + readout + reset the clock is 45 s at Delft's metropolitan rate and 1.0 s at Harvard's best. The comparison that matters is the competing interconnect: Oxford's trapped-ion link reached 96.89(8)% Bell fidelity at 9.7 s⁻¹ with an 86.2(9)% teleported CZ [D][G:OXFORD-DISTRIBUTEDQC-2025-02] — an order faster, 30 points better. Solid-state's counter-argument is manufacturability, not performance.

## Verification (QCVV)
The teleported-CNOT attribution resolves, and not as a mis-attribution: both results exist and differ in kind. Photonic Inc. entangled two T-centre modules in separate cryostats over ~40 m and ran a teleported-CNOT sequence, but forwent feed-forward and post-selected on a photon detection, reporting a truth table rather than a gate fidelity; still a 2024 preprint as of 4 Sep 2026 [P][5]. QuTech's 2026 result is unconditional — real-time feed-forward, no post-selection — at 63(4)% and 64(4)% [D][G:QUTECH-NV-TELEPORT-CNOT-2026-05]. Quoting the two together without that distinction overstates the T-centre platform. Elsewhere fidelities are conditional on a herald, and Harvard rejects ~23% of data on reflectance-contrast thresholds [D][1]. No result here has a second-group replication.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | Research | Netherlands | Metropolitan NV link; the only unconditional inter-cryostat gate | [D][G:QUTECH-NV-TELEPORT-CNOT-2026-05] |
| Photonic Inc. | Developer | Canada | Silicon T-centre modules, native telecom emission | [P][5] |
| Harvard University | Research | USA | SiV nanophotonic nodes over a 35 km deployed loop | [D][1] |
| Fujitsu | Funder | Japan | Funds the Delft modular-computer joint programme | [D][G:QUTECH-SNV-FUNDING-2026] |
| Microsoft | Investor, partner | USA | Networking collaboration since 2023; returning investor | [C][G:PHOTONIC-200M-2026-05] |
| Single Quantum | Supplier | Netherlands | Merchant nanowire detectors, the heralding dependency | [P][G:SNSPD-VENDORS-2026] |

**Money.** 2025-11-06 · Photonic Inc. · DARPA QBI Stage B, ~12 months · up to $15 M USD · programme [G:QBI-STAGEB-2025-11]. 2026-05-12 · Photonic Inc. · final close · $200 M USD at $2 B valuation, $350 M cumulative · Microsoft returning · closed [C][G:PHOTONIC-200M-2026-05]. Ongoing · QuTech · Fujitsu joint programme PPS2007, EU Quantum Internet Alliance grant 101080128, NWO Spinoza · not itemised · ongoing [D][G:QUTECH-SNV-FUNDING-2026].

**Market & supply chain.** No one sells a spin–photon link; the sold goods are detectors, diamond, enriched ²⁸Si, conversion modules and leased metro fibre. Detector supply is the shared bottleneck — five merchant vendors, one now owned by IonQ — and diamond is effectively single-sourced. It pays for G6 by definition and G7 where a modular machine needs inter-module links; not for G1–G5, which is why one company funds it today.

**IP & standards.** No patent family specific to spin–photon links was located in a named dated database as of 4 Sep 2026; Photonic Inc.'s T-centre position originates in Simon Fraser University work, but no assignee-and-date record was retrieved. No standards body governs heralding interfaces; the EU Quantum Internet Alliance is the nearest coordinating structure.

**Roadmaps & track record.** Photonic Inc. (promised 2023 · distributed fault tolerance "within five years", ~2028 · status 4 Sep 2026: no multi-node system, the 2024 link still post-selected), with a target of ~200 kHz at 99.8% [R][6] — seven orders of magnitude in rate and 40 points above its own published result, so an architecture target, not a roadmap. QuTech publishes no roadmap and delivers a Nature-class result roughly annually — credible on delivery, honest about rates.

**Strategic reading.** If this link matures the winners are modular architectures that cannot scale monolithically, and Microsoft gains optionality on a layer it need not build. Losers are monolithic roadmaps assuming on-chip scaling suffices. The substitution threat is ahead on points: trapped-ion links are faster and cleaner, and microwave-to-optical transduction targets the same slot. Bargaining power sits with detector and diamond suppliers.

*Open niche:* the field reports conditional fidelity and unconditional rate in separate places, and one platform's headline gate is post-selected while another's is not. A small QCVV group could define one figure of merit — pairs per second above a stated fidelity threshold, selection fraction declared — and apply it across NV, SiV, T-centre and ion links. A benchmark, not an experiment, and unowned.

## Outlook & open questions
Confirm by 2028 if any group sustains > 1 Hz heralded entanglement above F = 0.8 over > 20 km of deployed fibre, or if Photonic Inc. publishes an unconditional inter-module gate with a fidelity; demote if T-centre results stay post-selected preprints. Best case 2029: cavity enhancement plus multiplexing reaches 10–100 Hz at metropolitan distance. Worst case: sub-Hz rates, fidelity near 0.7, ion-photon links taking the slot. Open questions: does native telecom emission beat conversion once T-centre photon yield is counted; can cavity yield rise from ~0.6% to what a 100-node network needs; does anyone multiplex across emitters.

## Sources
[1] Knaut, Suleymanzade, Wei, Assumpcao, Stas, Huan, Machielse, Bhaskar, Park, Lončar, Lukin (Harvard) · "Entanglement of nanophotonic quantum memory nodes in a telecom network" · Nature 629 · 2024-05-15 [D] — https://www.nature.com/articles/s41586-024-07252-z
[2] Stolk, van der Enden, Slater et al. (Hanson group, QuTech/Delft) · "Metropolitan-scale heralded entanglement of solid-state qubits" · arXiv:2404.03723; Science Advances 10, eadp6442 · 2024-04-04 [D] — https://arxiv.org/abs/2404.03723
[3] Fischer et al. (QuTech/Delft) · cavity-enhanced NV photon collection · Nature Communications · 2026-01-15 [D] — https://www.nature.com/articles/s41467-025-66722-8
[4] Hanson et al. (QuTech/Delft) · "Unconditionally teleported quantum gates between remote solid-state qubit registers" · Nature Communications · 2026-05-26 [D] — https://www.nature.com/articles/s41467-026-72818-6
[5] Photonic Inc. · "Distributed Quantum Computing in Silicon" · arXiv:2406.01704, preprint, no journal publication located · 2024-06-03 [P] — https://arxiv.org/html/2406.01704v1
[6] PostQuantum · Photonic Inc. company profile (Microsoft partnership Nov 2023, ~1.5–4 K operation, 200 kHz / 99.8% target) · accessed 2026-09-04 [P] — https://postquantum.com/quantum-computing-companies/photonic-inc/
[7] Photonic Inc. · "Entanglement First" technology page (silicon T centres, 1 K cryostat, integrated switches and detectors) · accessed 2026-09-04 [C] — https://photonic.com/technology/entanglement-first/
[8] Quantum Computing Report · Photonic Inc. $200 M final close at a $2 B valuation · 2026-05-12 [P] — https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/
[9] DARPA · QBI Stage B selection · 2025-11-06 [G] — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[10] Bernien, Hensen, Pfaff, Koolstra, Blok, Robledo, Taminiau, Markham, Twitchen, Childress, Hanson (Delft) · "Heralded entanglement between solid-state qubits separated by three metres" · Nature 497, 86–90 · 2013-04-24 [D] — https://www.nature.com/articles/nature12016
[11] Main, Drmota et al. (Oxford) · "Distributed quantum computing across an optical network link" · Nature 638, 383 · 2025-02-05 [D] — https://www.nature.com/articles/s41586-024-08404-x
[12] QuTech · SnV nanocavity yield study, 327 devices, two above cooperativity 1; Fujitsu PPS2007 and EU grant 101080128 named · 2026-06-25 [D] — https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/
[13] The Quantum Insider · survey of NV-centre/diamond actors, Element Six named as quantum-grade diamond supplier · 2026-07-10 [P] — https://thequantuminsider.com/2026/07/10/8-quantum-computing-companies-working-with-nv-centre-in-diamond-technology/

## Open verification items
Photonic Inc.'s teleported-CNOT sequence has no published gate fidelity and no journal publication; the tCNOT figure of merit is a truth table over a selected basis, post-selected on photon detection.
The 200 kHz / 99.8% Photonic target comes from a trade-press profile, not a company technical document; treated as an unverified architecture target.
No dated patent-family count exists for spin–photon links in any named database consulted.
The Fujitsu–QuTech "gate errors below 0.1%" figure circulating in trade press has no located peer-reviewed source and is omitted here.
