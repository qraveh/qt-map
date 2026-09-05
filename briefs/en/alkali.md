---
id: alkali
name: Alkali atom (Rb/Cs) in optical tweezer
layer: "1 Carrier"
tier: 1
status: demonstrated
since: 2016
one_line: "Hyperfine ground-state qubit in a single rubidium or caesium atom held by a far-detuned optical tweezer, moved on demand."
verdict: "Identical, free, transportable qubits with second-scale coherence; the binding constraints are trap-laser watts, millisecond imaging and atom loss — not fabrication."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A single neutral ⁸⁷Rb or ¹³³Cs atom in a far-off-resonant dipole trap of ~1 µm waist, the qubit encoded in two hyperfine ground states split by 6.83 GHz (Rb) or 9.19 GHz (Cs). The trap, order 1 mK deep, confines but does not define the qubit, so every carrier is the same object to the precision of atomic physics. Single-atom trapping dates to 2001 (Institut d'Optique); the platform begins with the 2016 demonstrations of deterministic defect-free arrays assembled by moving tweezers (Harvard; Institut d'Optique).

Coordinates. *Carrier affinity:* fully natural — nothing fabricated, nothing to bin. *Characteristic time:* ~0.25 µs entangling interaction, deterministic, not heralded. *Readout:* fluorescence imaging, ~0.5 ms, non-destructive, mid-circuit capable. *Mobility:* the atom is physically transported by moving tweezers, so connectivity is reconfigured mid-circuit. *Control:* optical, room-temperature, outside the vacuum. *Error structure as the code sees it:* atom loss and leakage first, coherent error second — loss is detectable at imaging, hence erasure-convertible. *Manufacturing:* optical assembly, not lithography.

## Physics & limits

The trap sets the scaling law. Holding a laser-cooled atom costs roughly 0.5–1 mW of 850–1064 nm light: Tsinghua's 18,225-site array took 33 W incident and 12.2 W effective trapping power, ~0.67 mW per site [D][1]. Trap light grows strictly linearly with qubit count: a 10⁶-atom array is a kilowatt-class optical plant, not a larger version of today's machine.

Coherence is not the constraint. Hyperfine clock states are first-order magnetically insensitive: T₂ = 12.6(1) s in a 6,100-atom Cs array [D][3]; T₂ = 1.09(3) s in Rb *while a magneto-optical trap ran 0.5 m away*, against a shielded 1.34(4) s [D][2]. Against a millisecond cycle both are enormous.

The floor is atom loss. Background-gas collisions and photon-scattering heating give a tweezer-limited lifetime near 60 s in a room-temperature cell [D][2]; loss runs ~0.09% per two-qubit gate [D][5], and over 80% of leakage in a logical circuit is loss [D][4]. That is the defining asymmetry: the dominant error announces itself. Moving the floor takes cryogenic vacuum, reloading during computation (300,000 atoms/s into tweezers, >30,000 initialised qubits/s [D][2]) or a species change — alkalis buy the simplest laser system and the best-characterised Rydberg structure but lack the manifolds that make erasure conversion and loss-free imaging native in Sr/Yb.

## Engineering state of the art

**Records timeline.**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-03 → 2025-07 | 6,100 Cs atoms in ~12,000 sites; T₂ 12.6(1) s; imaging survival 99.98952(1)% | Caltech | [D][3] |
| 2025-09-15 | 3,217 Rb atoms in one shot, >3,000 held >2 h; 300,000 atoms/s loaded; ~60 s lifetime | Harvard/MIT | [D][2] |
| 2025-11-10 | 448 atoms under fault-tolerant control; 2.14(13)× below threshold, four rounds | Harvard/MIT/QuEra | [D][G:HARVARD-LOSS-QEC-2025] |
| 2026-06-01 | 11,022 Rb atoms in 18,225 metasurface tweezers, 60.5% filling, no gates | Tsinghua/Qosmos | [D][1] |

Typical at scale trails the records: QuEra's shipping Gemini is 260 physical qubits at 1 shot/s, SPAM 99.7% [C][G:QUERA-GEMINI-SPEC-2026-09]. The gap between 11,022 trapped and 448 under logical control is the field's honest position as of 3 September 2026, and atom loss dominates the budget in every regime. The carrier-quality bound set by the best entangling gate — 0.087(5)% atom loss per CZ [D][G:HARVARD-CZ-2026-04] — is a loss figure, not a coherence figure.

## Manufacturing, materials & supply chain

There is no wafer. The process is an optical assembly: a UHV glass cell, an alkali dispenser, a high-NA objective — or, at Tsinghua, a 19.8 mm silicon-nitride metasurface 2.5 mm outside the cell replacing the objective entirely [D][1] — an SLM for the static array, crossed acousto-optic deflectors for movable tweezers, a scientific camera. Uniformity is a runtime property, not a yield: stochastic loading fills 50–60% of sites and rearrangement repairs the array every shot. Substituting sorting for yield is this carrier's structural advantage over every fabricated one.

The supply chain is optics, concentrated in Europe and Japan [P][9]. Lasers: TOPTICA (Munich), Exail (in Pasqal's racks), M Squared, and Menlo Systems and NKT — both Hamamatsu subsidiaries. SLMs: Meadowlark, Hamamatsu LCOS, Holoeye. Acousto-optics: AA Opto-Electronic, Gooch & Housego, Isomet. Cameras: Hamamatsu ORCA-Quest qCMOS, chosen for mid-circuit imaging in the Harvard/QuEra machine. Vacuum: Pfeiffer, Edwards, Kurt J. Lesker, VACOM. Over 90% of system size and cost is lasers and photonics [P][9]. There is no Bluefors-equivalent chokepoint, but Hamamatsu appears simultaneously in lasers, SLMs and cameras — the one name hard to route around. No vendor discloses a per-system price. Export exposure runs through tunable lasers and vacuum equipment under Wassenaar Categories 6 and 2 and the 2024 US BIS quantum rule; exact ECCNs are unverified below.

## Control, readout & I/O burden

The I/O burden does not scale with N: one SLM hologram makes the static array, one deflector pair addresses whichever subset is operated on. Wiring count — the wall for every solid-state carrier — is replaced by optical power and bandwidth. The cost lands in time: imaging 0.5–1 ms, transport 0.1–1 ms, correction cycle 1–4.5 ms, three orders slower than superconducting circuits, with the compensating benefit that a real-time decoder has an easy latency target (NVQLink 3.84 µs [C][22]).

At 10³ the platform is done. At 10⁴ the constraints are aggregate trap power (12 W at the atoms today), deflector bandwidth, rearrangement time and camera field of view. At 10⁶ nothing demonstrated applies: kilowatt trap light, no multi-core interconnect, no sorting scheme finishing inside a cycle. Photonic delivery is the proposed answer, and Pasqal's four chip-trapped Rb atoms, ~27.5 s lifetime (2026-08-10) [C][7], are three and a half orders from mattering.

## Role in the stack

One path: "Neutral atoms — alkali (Rb/Cs)". It requires optical/mechanical assembly and provides the carrier for Rydberg-blockade CZ, for fluorescence imaging of atom arrays, and for the atom–photon cavity interface a network layer would need. It replaces the alkaline-earth slot: switching costs a laser rebuild (narrow-line cooling and clock lasers at 689/698 nm) plus a decade of alkali Rydberg calibration, and buys native erasure conversion and non-destructive nuclear-spin readout. The field splits on that line — QuEra, Pasqal, Harvard, Tsinghua on alkalis; Atom Computing (Yb), Infleqtion, Caltech's gate work (Sr) on alkaline earths. Derived clock = max(gate 0.27 µs, readout ~0.5 ms, transport ~0.5 ms) ≈ **1.0 × 10⁻³ s**, set by readout and transport, never the gate. Neighbouring empty slots: no cavity interconnect at array scale, no cryogenic-vacuum array above 10³.

## Verification (QCVV)

The headline coherence is a dynamically decoupled, array-averaged T₂: it absorbs site-to-site trap-depth inhomogeneity into the pulse sequence rather than reporting it. Imaging survival of 99.98952(1)% is per image at a stated exposure and bounds nothing about loss during transport or Rydberg excitation. The 60.5% filling fraction is pre-rearrangement — "11,022 atoms" and "11,022 usable qubits" are different claims. No protocol here separates loss from depolarising error, so error-per-Clifford figures are not comparable to solid-state ones without the post-selection.

Conflicts. The Caltech abstract says "over 6,100 atoms in around 12,000 sites"; versions differ (v1 2024-03, v4 2025-07) and the 12.6 s figure belongs to v4, which I trust [D][3]. The review arguing a 99.9% blockade ceiling also tabulates a 2025 USTC CZ of 99.84% that no primary source corroborates [P][19].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuEra | developer | US | Rb arrays; Gemini 260 q shipping; Libra promised 2028 | [C][10][11] |
| Harvard/MIT | research | US | 448-atom architecture; 3,000-qubit continuous run; CZ record | [D][2][4] |
| Caltech | research | US | 6,100-atom Cs array; T₂ 12.6 s; record imaging survival | [D][3] |
| Pasqal | developer | FR | Rb machines; on-chip trapping; Nasdaq PSQL | [C][7][8] |
| Infleqtion | developer | US | Sqale line; NYSE INFQ; Illinois system 2027 | [G][6][15] |
| Tsinghua | research | CN | 11,022-atom metasurface array, largest trapped ensemble | [D][1] |
| Google Quantum AI | research | US | neutral-atom track opened 2026-03 under Adam Kaufman | [C][17] |
| Atom Computing | developer | US | Yb competitor; Magne with Microsoft; QBI Stage B | [G][21] |
| planqc | developer | DE | DLR and LRZ builds; 1,000 qubits at LRZ circa 2027 | [C][12] |
| TOPTICA | supplier | DE | dominant supplier of Rb/Cs cooling and trapping lasers | [P][9] |
| Hamamatsu | supplier | JP | LCOS-SLMs and qCMOS cameras; owns Menlo and NKT | [P][9] |

**Money.**

- 2022-05-04 / 2024-07-08 · planqc · DLR contract EUR 29 M; Series A EUR 50 M · DLR Quantum Computing Initiative; lead undisclosed · closed [C][12]
- 2025-07-17 · QuNorth · "Magne" order from Atom Computing/Microsoft · EUR 80 M · EIFO + Novo Nordisk Foundation · ordered [G:MAGNE-2025-07]
- 2025-09-09 · QuEra · financing round · > USD 230 M · Google, SoftBank Vision Fund 2, NVentures · closed [C][G:QUERA-230M-2025]
- 2025-11-06 · QuEra · DARPA QBI Stage B · up to USD 15 M · DARPA · selected [G:QBI-STAGEB-2025-11]
- 2026-02-17 · Infleqtion · NYSE listing (INFQ) · > USD 550 M gross · SPAC · closed [G:INFLEQTION-NYSE-2026-02]
- 2026-05-21 · Infleqtion · CHIPS letter of intent · USD 100 M · US Dept of Commerce · LOI (non-binding) [G:CHIPS-LOI-2026-05]
- 2026-06-15 · QuEra · Libra 2028 roadmap, expanded AWS Braket collaboration · undisclosed · AWS · roadmap [R][G:QUERA-LIBRA-2026]
- 2026-08-12 · Infleqtion · Q2 2026 results · revenue USD 12.6 M (+116% y/y), H1 USD 22.094 M, FY26 guidance ~USD 43 M, Q2 net loss USD 25.5 M, cash USD 582 M · reported [G][6]
- 2026-08-27 · Pasqal · SPAC completion, Nasdaq PSQL · ~USD 360 M cash; 2025 revenue EUR 16.5 M · Bleichroeder Acquisition Corp. II · closed [G:PASQAL-SPAC-2026-08]

**Market & supply chain.** The enabling equipment is sold by photonics firms that were profitable before quantum existed; concentration is real but diffuse, with over 90% of system cost in lasers and photonics [P][9]. Unit economics are undisclosed; the only quotable figure is 0.67 mW of trap light per tweezer [D][1]. G1 (analog simulation) is what alkali arrays are actually paid for today; G5 (optimisation) is what is marketed; G3 (early fault tolerance) is where every 2028 promise sits; G4 is the thesis behind the valuations. G6 is blocked on the cavity-interface slot.

**IP & standards.** The foundational tweezer-array and coherent-transport families come from Harvard/MIT, licensed into QuEra; the CNRS/Institut d'Optique lineage feeds Pasqal. Vertical integration is the visible move: Pasqal acquired Aeponyx for silicon-nitride photonics under 18 months before its August 2026 result [C][7]. Open-source stacks: Bloqade (QuEra), Pulser (Pasqal), both with analog-Hamiltonian front ends no other modality needs. No litigation found; no dated patent count from a named database.

**Roadmaps & track record.** QuEra (promised 2024-01 · for 2026 · 100 logical qubits undelivered as of 2026-09-03, replaced by Libra >256 logical in 2028 — a two-year slip). Pasqal (promised 2024-03 · for 2026 · 10,000 physical slipped to 2028; 100 logical now 2029). Infleqtion (reaffirmed 2026-08-12 · for 2026 · 30 logical qubits, unverified; >50 logical at Illinois 2027). planqc (promised 2024-11 · for ~2027 · 1,000 qubits at LRZ; no device metrics published since). Credibility: Harvard/MIT outrun every roadmap because they publish rather than promise; QuEra and Pasqal have each slipped a flagship number by two years and read as 2029 companies; Infleqtion alone reports audited revenue against its claims; planqc has contracts but no published metrics.

**Strategic reading.** If alkali arrays win, value accrues asymmetrically to component vendors — TOPTICA, Hamamatsu, Meadowlark — paid identically whichever developer prevails and facing no substitution risk from the alkaline-earth branch beyond a change of wavelength catalogue. The real threat to *this node* is internal: Sr/Yb carriers convert the dominant error into an erasure for free. Bargaining power sits with buyers — Infleqtion holds USD 582 M, Pasqal ~USD 360 M, against far smaller European vendors — and the response is acquisition rather than negotiation.

*Open niche:* the unclaimed QCVV ground here is loss-aware characterisation. No standard protocol separates atom loss from depolarising error, reports per-site rather than array-averaged coherence, or certifies that a rearranged array is defect-free before a circuit begins — yet loss is over 80% of the leakage budget and the erasure-conversion argument rests entirely on how well it is detected. Three deliverables are open: a loss-flagged randomised-benchmarking variant with a published estimator, a per-site T₂ and trap-depth mapping protocol for arrays above 10³, and a rearrangement-fidelity certificate. The millisecond cycle removes any latency argument for cryogenic single-flux-quantum control, so SFQ competence transfers here as measurement discipline, not hardware.

## Outlook & open questions

**Confirm** if a defect-free array above 2,000 atoms runs gates by end-2027; if Infleqtion demonstrates 30 logical qubits by 2026-12-31; if a chip-delivered tweezer array exceeds 100 traps by end-2027. **Demote** if no group shows Λ > 2 over more than 50 rounds *with* continuous reloading by end-2027 — Atom Computing's toric-code run lost its suppression precisely when reloading was included [D][20], and that, not gate fidelity, is the load-bearing question.

Best case by 2029: Libra-class systems above 256 logical qubits on cloud, chip or metasurface optics collapsing the footprint, loss handled as erasure end to end. Worst case: 10³-qubit analog simulators with a few dozen logical qubits, the millisecond cycle fatal outside simulation, alkalis losing fault tolerance to Sr/Yb.

Open questions. (1) Does continuous reloading survive contact with error correction, or does stray light impose a coherence tax growing with duty cycle? (2) Can rearrangement of >10⁴ sites finish inside a correction cycle, or does sorting become the clock? (3) Are metasurface and chip-based trap delivery compatible with the trap depths and beam quality high-fidelity gates require?

Watch: Infleqtion's Q4 2026 report against the 30-logical claim; a QuEra Libra milestone in 2027; Pasqal's chip channel count; Google's first neutral-atom paper; any vacuum-limited lifetime above 300 s at array scale.

## Sources

[1] Wang, Zhang et al. (Tsinghua University; Qosmos, Beijing) · Metasurface-generated tweezer array: 11,022 ⁸⁷Rb atoms in 18,225 sites · arXiv:2606.02715 · 2026-06-01 · https://arxiv.org/abs/2606.02715
[2] Harvard/MIT (Lukin, Greiner, Vuletić et al.) · Continuous operation of a 3,000-qubit atom array · Nature 646 (8087) · 2025-09-15 · https://www.nature.com/articles/s41586-025-09596-6
[3] Manetsch, Nomura, Bataille, Leung, Lv, Endres (Caltech) · A tweezer array with 6,100 highly coherent atomic qubits · arXiv:2403.12021 (v4, 2025-07-29) · https://arxiv.org/abs/2403.12021
[4] Bluvstein et al. (Harvard/MIT/QuEra) · A fault-tolerant neutral-atom architecture for universal quantum computation · Nature · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[5] Evered, Xu, Li et al. (Harvard/MIT) · High-fidelity entangling gates and nonlocal circuits with neutral atoms · arXiv:2604.25987 · 2026-04-28 · https://arxiv.org/abs/2604.25987
[6] Infleqtion, Inc. (INFQ) · Q2 2026 results: record revenue, raised 2026 outlook · investor-relations release · 2026-08-12 · [G] · https://ir.infleqtion.com/news-events/press-releases/detail/201/infleqtion-reports-record-q2-revenue-raises-2026-outlook-as-quantum-commercialization-accelerates
[7] Pasqal · Pasqal brings qubit control on-chip · newsroom · 2026-08-10 · [C] · https://www.pasqal.com/news/pasqal-brings-qubit-control-on-chip-advancing-the-path-to-fault-tolerant-quantum-computing-at-scale/
[8] Pasqal · Newsroom index (SPAC completion 2026-08-27; KACST collaboration 2026-08-31) · [C] · https://www.pasqal.com/newsroom/
[9] postquantum.com · The tweezer array's hidden supply chain: the neutral-atom quantum ecosystem · accessed 2026-09-03 · [P] · https://postquantum.com/quantum-ecosystem/neutral-atom-quantum-ecosystem/
[10] QuEra Computing · Gemini product specification · accessed 2026-09-03 · [C] · https://www.quera.com/gemini
[11] QuEra Computing · 2028 fault-tolerant computer and expanded AWS collaboration · 2026-06-15 · [C] · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[12] planqc · News index (DLR EUR 29 M 2022-05-04; Series A EUR 50 M 2024-07-08; LRZ 1,000 qubits 2024-11-13; EUR 2.3 M 2026-03-19) · [C] · https://planqc.eu/news
[13] DARPA · Quantum Benchmarking Initiative Stage B selection · 2025-11-06 · [G] · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[14] NIST / US Department of Commerce · Letters of intent with nine companies, USD 2.013 B · 2026-05-21 · [G] · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[15] Infleqtion · First neutral-atom quantum company to go public (NYSE, INFQ) · 2026-02-17 · [C] · https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/
[16] The Quantum Insider · Pasqal completes SPAC merger with USD 360 M in cash · 2026-08-28 · [P] · https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/
[17] Google · Neutral-atom quantum computers: a second hardware track · blog · 2026-03-24 · [C] · https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/
[18] QuEra Computing · USD 230 M+ financing round · 2025-09-09 · [C] · https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing
[19] Wang, Wang, Li, Wang, Liang, Yan · Neutral atom quantum computing: principles, routes, progress and challenges · arXiv:2608.05010 · 2026-08-05 · [P] · https://arxiv.org/html/2608.05010v1
[20] Atom Computing · Toric-code demonstration with continuous reloading · arXiv:2606.04079 · 2026-06 · https://arxiv.org/abs/2606.04079
[21] Novo Nordisk Foundation · QuNorth orders "Magne" from Atom Computing and Microsoft, EUR 80 M · 2025-07-17 · [C] · https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/
[22] NVIDIA · NVQLink architecture, 3.84 µs mean round trip · developer blog · 2025-11 · [C] · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/

## Open verification items

- The 2016 origin papers (Endres et al.; Barredo et al.) and the 2001 single-atom trapping result are cited from the standard literature without a numbered source.
- Export control: specific ECCNs for tunable lasers (6A005) and for quantum equipment under the 2024 BIS rule were not verified against a BIS or Wassenaar document; only general category exposure is asserted.
- Infleqtion's computing atom species (caesium) is not confirmed by any source consulted here.
- planqc's atom species (strontium) is not stated on its own news index; if strontium, planqc belongs to the alkaline-earth node rather than this one.
- Caltech array: the v4 abstract says "over 6,100 atoms in around 12,000 sites"; version drift between v1 (2024-03) and v4 (2025-07), the 12.6 s T₂ figure taken from v4.
- The Tsinghua metasurface paper does not state a vacuum-limited trap lifetime.
- No per-qubit or per-system capital cost was found for any tweezer machine, from any vendor or filing.
- arXiv:2608.05010 tabulates a 2025 USTC CZ of 99.84% with no corroborating primary source; not used.
- https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws returned HTTP 404 on 2026-09-03; no QuEra corporate events after 2026-06-15 were verified.
- Filling-fraction framing conflict: Tsinghua's "11,022 atoms" is a pre-rearrangement loading figure at 60.5%, not a defect-free usable-qubit count; the two are routinely conflated in secondary coverage.
