---
id: ion
name: Trapped atomic ion
layer: "1 Carrier"
status: demonstrated
since: 1995
one_line: "Single Yb⁺/Ba⁺/Ca⁺ ions in RF traps, entangled through shared motional modes; the highest-fidelity and slowest qubit in commercial service."
verdict: "Fidelity leader and the only platform running dozens of corrected logical qubits, but throughput is set by transport and cooling, not gates; 2D scaling unproven until Sol (2027)."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A trapped-ion qubit is a single atomic ion — ytterbium, barium, calcium or strontium — confined by RF and static fields above micro-fabricated electrodes, with logic in hyperfine, Zeeman or optical levels. Ions in a chain repel, so they share quantised motional modes; a spin-dependent force on those modes turns motion into a bus that entangles any pair. Cirac and Zoller proposed it in 1995; Wineland's NIST group demonstrated a two-qubit gate the same year. Everything commercial today is that idea plus surface-electrode microfabrication.

Coordinates (technology graph): carrier affinity 0.0 — wholly natural, every ion identical by physical law, no fabrication variance to calibrate out; entangling time 10⁻⁴·² s (≈ 63 µs), deterministic, no heralding; readout by fluorescence on a cycling transition, ≈ 10 µs, non-destructive, mid-circuit capable; mobility by physical transport — ions are shuttled, not wired; control optical, at room temperature; error structure as the code sees it coherent, leakage, Pauli; manufacturing MEMS-class surface-electrode traps.

## Physics & limits

Trap frequencies of a few MHz set the clock. Spin–motion coupling scales with the Lamb–Dicke parameter times the drive, so a gate much faster than a motional period either excites the wrong modes or needs optical power that reintroduces scattering; µs-to-hundreds-of-µs gates are a physical compromise, not an engineering lapse. Memory is the opposite: in magnetically insensitive clock states one ion holds coherence beyond an hour [D][6], five to six orders longer than a superconducting qubit. Idle error is nearly free; idle time is what costs.

The floor belongs to the drive, not the carrier: laser gates carry an irreducible spontaneous-emission floor, and 8.4(7)×10⁻⁵ two-qubit error at Doppler temperature without ground-state cooling [D][4] shows it is removable. What remains is anomalous heating from electrode surfaces, mode crowding as chains lengthen, and background-gas collisions that reorder or eject a chain. That last is the architectural problem: a decoder built for stochastic Pauli noise instead sees ions leak into metastable manifolds or vanish. Leakage is small enough to quote — 1.1×10⁻⁵ per Clifford on Helios [D][1] — but quoted separately because it is not Pauli. Cryogenic traps, sympathetic cooling, metastable erasure encodings and better vacuum would move the floor.

## Engineering state of the art

Best-demonstrated and typical-at-scale have converged unusually far: Helios runs 98 Ba⁺ qubits at 7.9×10⁻⁴ two-qubit error with all-to-all connectivity, within an order of magnitude of the record. The gap is speed — the gate is ≈ 70 µs, but a full-width layer takes ≈ 55 ms once sorting, transport and re-cooling are counted; transport was ~60% of runtime on H2 [D][1][12].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-07 | All-electronic control, 10 qubits / 7 zones: 2Q 99.97(1)% | Oxford Ionics | [D][32][G:OXIONICS-ALLELEC-2024-07] |
| 2025-10 | 2Q error 8.4(7)×10⁻⁵, no ground-state cooling | Oxford Ionics / IonQ | [D][4][G:ELECGATE-9999-2025-10] |
| 2025-11 | Helios 98 Ba⁺: 2Q 7.9×10⁻⁴, SPAM 3.3–4.8×10⁻⁴, leakage 1.1×10⁻⁵/Clifford | Quantinuum | [D][1] |
| 2026-02 | 48 corrected logical qubits ([[80,48,4]]), logical gate infidelity 1.0–1.2×10⁻⁴ | Quantinuum | [D][7][G:HELIOS-ICEBERG-2026-02] |
| 2026-05 | Quantum volume 32,768, rack-mounted LYNX | AQT | [C][23] |
| 2026-06 | qLDPC memory break-even: [[18,4,3]] 3.95 ± 0.68 s vs 3.3 ± 0.9 s | IonQ | [D][11][G:IONQ-QLDPC-BREAKEVEN-2026-06] |

The dominant error term at scale is not the gate: it is the cost of moving ions — transport excitation, re-cooling, re-ordering — plus leakage the decoder cannot absorb. High-rate code demonstrations discard 75–97% of shots at depth [D][7].

## Manufacturing, materials & supply chain

Traps are MEMS-class silicon parts, not qubit-defining lithography: the ion is perfect, so wafer variance shows up as electrode geometry and surface quality, never as qubit-to-qubit spread. Two fabs matter. Infineon runs a dedicated QPU platform in Villach on 6- to 12-inch wafers with anodic wafer bonding; its Generation-3 traps add out-of-plane electrodes claimed to raise confinement ~10×, with eleQtron (three generations), Oxford Ionics, Innsbruck and ETH Zurich as named users [C][27]. Honeywell fabricates Quantinuum's traps in-house — Helios carries 1,228 electrodes [D][1] — and the Sol grid trap is back from fabrication and in validation [C][19]; Infineon separately partnered with Quantinuum on next-generation traps in 2024-11 [C][28]. Infineon is a single point of failure for IonQ/Oxford Ionics, eleQtron and Universal Quantum at once [P][30] — which is what IonQ's ≈ $1.8 B purchase of SkyWater (closed 2026-07-31) buys its way out of [C][21].

The second concentration is optical: TOPTICA (> €140 M revenue, ~600 staff) supplies most major ion experiments, and the UV end — 369 nm for Yb⁺ — is the constrained part [P][30]. Vacuum hardware and atomic sources are commodity; photonic interconnects re-import a cryogenic dependency through SNSPDs [P][30][G:SNSPD-VENDORS-2026]. Unit economics: AQT delivered a 20-qubit rack to LRZ / Munich Quantum Valley for ≈ €9.8 M (2023-12-05, Bavarian Hightech Agenda) [C][29] — ≈ €0.5 M per qubit, turnkey. Export exposure runs through the September-2024 US quantum ECCNs; a bare trap chip's classification is unverified here.

## Control, readout & I/O burden

Per-ion optical addressing is what fails to scale linearly: Helios needs at least seven laser wavelengths alongside 1,228 electrode drives [D][1]. Readout is cheap — fluorescence onto a PMT or camera in ≈ 10 µs, non-destructive and natively mid-circuit. Latency demands are mild: IonQ assumes 1–5 ms syndrome cycles [D][13], inside NVQLink-class round trips [C][38][G:NVQLINK-2025].

The wall moves with N. At 10³ it is drive-source count and optical-table area; the WISE study argues a fully connected 1,000-ion machine could run from ~200 sources with in-trap switching electronics, at 40–2,600 gate layers per second [S][33][G:WISE-ARCH-2023] — paper design, no chip built. At 10⁴ it is inter-module: remote entanglement stands at 9.7 s⁻¹ over 2 m (Bell 96.9%) [D][15] and 250 s⁻¹ in a lab [D][16] against ~10⁴ s⁻¹ needed. At 10⁶ it is yield and laser power. Gate generation and microwave control belong to the sibling briefs.

## Role in the stack

The carrier feeds two named paths: *Trapped ions — QCCD, laser gates* (Quantinuum, AQT) and *Trapped ions — electronic gates, chip control* (IonQ/Oxford Ionics, eleQtron, Quantum Art). It requires surface-electrode trap microfabrication and optical/mechanical assembly, and is the substrate for the Mølmer–Sørensen gate, the electronic near-field microwave gate, metastable "omg" erasure encoding, shuttling, fluorescence detection and the ion–photon link. It replaces and conflicts with nothing: ions are a self-contained column, which is why switching away is total — nothing above the carrier survives but the compiler.

Derived clock = sum of the syndrome round: gate layers + transport + readout + reset. On the QCCD path transport dominates: ≈ 9.7×10⁻³ s per round, 9.0 ms of it transport, against a ≈ 5.5×10⁻² s full-width layer [D][1][12]. On the electronic-gate path the round is ≈ 1.5×10⁻³ s, set by the gate layers [D][4]. That six-fold gap is the platform's defining number. Neighbouring empty slot: a cryogenic chip-integrated drive layer for ion traps — the SFQ/cryo-CMOS analogue — has no product-scale occupant.

## Verification (QCVV)

Headline two-qubit numbers come from randomized-benchmarking variants. The 8.4(7)×10⁻⁵ record is a subspace-leakage RB on one ion pair at Doppler temperature, not a device-wide figure, and the retrievable text gives no gate duration [D][4]. Helios's 7.9×10⁻⁴ is an averaged device figure, consistent with the earnings language "99.921%" [C][19]. Quantum volume and #AQ are vendor-defined composites with no replication protocol [C][2][3]. RB also runs statically, so shuttling and re-cooling are invisible to quoted gate errors. Logical results carry an acceptance fraction (0.62(2) [D][7]) and IonQ's break-even is leakage-post-selected [D][11]; neither is unconditional. No ion platform has published Λ-type distance scaling.

Conflicts. The electronic gate's duration is 225.8 µs (2025) or ≈ 120 µs (2024) in the technology graph and unstated in the 2025 abstract — unverified. Quantinuum's "near five-nines logical fidelity with a novel QEC code family" [C][19] outruns the published 1.0–1.2×10⁻⁴ logical gate infidelity [D][7]; the code family is unpublished, so the [D] value stands. IonQ's Tempo is marketed at "99.9%" and #AQ 64 with no published gate times [C][3][26].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK | QCCD laser gates; Helios 98 q, 48 logical qubits; Sol, Apollo | [D][7] |
| IonQ | developer | US | Long chains plus Oxford Ionics electronic gates; qLDPC break-even; owns SkyWater | [D][11] |
| Honeywell | supplier | US | In-house MEMS fabrication of Quantinuum traps; anchor shareholder | [C][18] |
| Infineon Technologies | supplier | AT/DE | Merchant ion-trap foundry, Villach, 6–12″, Gen-3 traps | [C][27] |
| AQT | developer | AT | Rack-mounted 19″ ion systems; QV 32,768; LRZ installation | [C][29] |
| eleQtron | developer | DE | Microwave ion control; DLR QSea I demonstrator; €54 M backlog | [G][35] |
| Quantum Art | developer | IL | Multi-core trapped-ion architecture; $140 M Series A | [P][22] |
| Universal Quantum | developer | UK | Modular trap machine under a €67 M DLR contract; nothing delivered | [P][34] |
| Tsinghua University | research | CN | 512-ion 2D crystal analog simulation; hour-scale memory | [D][17] |
| Qudoor | developer | CN | AbaQ ion-trap systems and cloud; 32+ claimed patents | [P][37] |

**Money.**
- 2022-11-02 · Universal Quantum · DLR contract · €67 M · announced [P][34][G:UQ-DLR-67M-2022-11]
- 2023-12-05 · AQT · contract, 20-qubit system for LRZ · ≈ €9.8 M · Bavarian StMWK/StMWi · closed [C][29]
- 2025-11-06 · IonQ, Quantinuum · DARPA QBI Stage B · up to $15 M each · selected [G][31][G:QBI-STAGEB-2025-11]
- 2025-10-12 · IonQ · equity · $1.0 B + $2.0 B at $93/share · closed [G:IONQ-EQUITY-2025]
- 2025-09-04 · Quantinuum · round · $600 M at $10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G][18][G:QTM-600M-2025-09]
- 2025-09-17 · IonQ · M&A Oxford Ionics · $1.075 B · closed [C][20][G:IONQ-OXIONICS-2025]
- 2026-04-27 · Quantum Art · Series A extension · $100 M → $140 M · closed [P][22][G:QART-140M-2026-04]
- 2026-05-05 · eleQtron · Series A · €57 M · backlog €54 M · closed [C][23][G:ELEQTRON-57M-2026-05]
- 2026-06-03 · Quantinuum · IPO, Nasdaq QNT · $1.68 B gross at $60/share · closed [G][19][G:QTM-IPO-2026-06]
- 2026-07-31 · IonQ · M&A SkyWater · ≈ $1.8 B · closed [C][21][G:IONQ-SKYWATER-2026]
- 2026-06-30 · Q2 FY26 revenue · Quantinuum $8.0 M, cash $2.1 B, guidance $28–32 M; IonQ $80.1 M, cash $3.0 B, guidance $280–290 M [C][19][26]

**Market & supply chain.** Equipment money sits with TOPTICA, Infineon and commodity vacuum vendors; concentration risk is real in two places only — UV lasers and Infineon's fab, which underpins three otherwise-independent developers [P][30]. Against ≈ €9.8 M for a 20-qubit rack [C][29], sector ion revenue is about one large system per quarter plus cloud access. Goals that pay: G1 (Tsinghua's simulator), G2 and G5 (cloud), G3 (Helios logical qubits, IonQ's qLDPC memory), G7 (AQT racks, eleQtron's backlog), G6 in prototype. G4 is funded by capital markets and DARPA, not customers.

**IP & standards.** Named families: Oxford Ionics' electronic qubit control and the WISE in-trap switching architecture [S][33]; Honeywell/Quantinuum QCCD junction and grid-trap patents behind 2.5 kHz ion exchange and 4 m/s transport [D][14]; Infineon's anodic-bonding 3D-electrode process [C][27]; ID Quantique's detector portfolio, now IonQ's [C][21]. No dated ion-specific patent count from a named database was found; the PatSnap 2026-06-30 cut carries no ion line [P][G:PATSNAP-2026-06]. No ion-specific standard exists.

**Roadmaps & track record.** Quantinuum: Helios (promised 2024-09-10 · for 2025 · launched 2025-11-05) [G:QTM-ROADMAP]; Sol (promised 2024-09-10 · for 2027 · trap chip fabricated, in validation); Apollo (for 2029 · "on schedule", prototypes only) [C][19]. Credibility high — promised dates met — except the unpublished five-nines code family. IonQ: 4,000 qubits (promised 2020 · for 2026 · missed ~40×) [P][25]; 256 qubits at 99.99% (promised 2025-06-13 · for 2026 · slipped to H1 2027) [R][25]; 10,000 on one chip (for 2027 · no published 2D-trap heating or interconnect data). Credibility mixed: the physics is peer-reviewable, the schedules are not. AQT delivers its QV records on time; Universal Quantum has announced nothing against its 2022 contract [P][34].

**Strategic reading.** If ions win, Honeywell and Infineon capture structural rent — one through vertical integration nobody can copy, the other as the only merchant trap fab — and TOPTICA becomes the choke point. IonQ's SkyWater purchase converts a supplier dependency into an owned asset: a bet that trap fabrication, not qubit physics, is the scarce input. The substitution threat is not superconducting circuits (faster clock, worse fidelity) but neutral atoms: same natural carrier, same optics-heavy engineering, thousands of sites already, fidelity closing. Bargaining power still sits with the platform vendors: Infineon's quantum unit is a rounding error inside a €15 B company [P][30] and cannot price like a monopolist.

*Open niche:* a small QCVV/SFQ house plugs in at three seams. First, transport-aware benchmarking: no published protocol charges shuttling and re-cooling to a gate-level figure of merit, yet those terms set the derived clock; a mirror-circuit variant reporting error per layer of a *moving* machine would be directly comparable across vendors. Second, acceptance- and leakage-corrected logical metrics: with post-selection discarding 62–97% of shots, a convention for unconditional logical error would settle several disputes above. Third, the empty cryogenic-drive slot: 4 K ion traps have no chip-integrated drive layer, making SFQ pulse generation inside the trap package an unclaimed question.

## Outlook & open questions

Confirm if: Sol ships in 2027 with ≥ 192 physical qubits on a 2D grid trap *and* a published layer time better than ≈ 55 ms; any ion vendor publishes Λ > 1 scaling across d = 3→5→7; remote entanglement passes 10³ s⁻¹. Demote if: IonQ has not shown 256 qubits at 99.99% by end-2027 (already slipped once); Sol leaves layer time unimproved; or the five-nines code family stays unpublished a year on.

Best case by 2029: Apollo lands with hundreds of logical qubits at 10⁻⁶–10⁻¹⁰ and ions own early fault tolerance, the clock deficit absorbed by depth-hungry algorithms. Worst case: 2D scaling multiplies transport cost instead of amortising it, layer time stays in tens of milliseconds, and ions become the high-fidelity low-throughput instrument for QEC research while neutral atoms and superconducting circuits take the volume.

Open questions: does grid-trap heating scale with zone count or electrode area? Can leakage be turned into erasure fast enough that decoders stop paying for it? What is the electronic gate's real duration at full width? Is 10⁴ s⁻¹ remote entanglement reachable at all? Who second-sources Infineon?

## Sources

[1] Quantinuum · Helios: a 98-qubit trapped-ion quantum computer · arXiv:2511.05465, and Nature · 2025-11, 2026-06 · https://arxiv.org/abs/2511.05465 · https://www.nature.com/articles/s41586-026-10676-4 [D]
[2] Quantinuum · Quantum Volume (glossary entry) · company website · 2026 · https://www.quantinuum.com/glossary-item/quantum-volume [C]
[3] IonQ · Forte system specifications · company website · 2026 · https://www.ionq.com/quantum-systems/forte [C]
[4] Hughes, Srinivas, Loschnauer, Knaack, Matt, Ballance, Malinowski, Harty, Sutherland (Oxford Ionics / IonQ) · Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling · arXiv:2510.17286 · 2025-10-20 · https://arxiv.org/abs/2510.17286 [D]
[5] Oxford (Lucas group) · Single-qubit gate error 1.5×10⁻⁷ · arXiv:2412.04421 · 2024-12 · https://arxiv.org/abs/2412.04421 [D]
[6] Wang, Zhang, Kim et al. (Tsinghua) · Single-ion qubit coherence beyond one hour · arXiv:2008.00251 · 2020-08 · https://arxiv.org/abs/2008.00251 [D]
[7] Quantinuum · Computing with many encoded logical qubits beyond break-even · arXiv:2602.22211 · 2026-02 · https://arxiv.org/abs/2602.22211 [D]
[8] Quantinuum · Teleporting to new heights (logical teleportation 99.82%) · company blog · 2025 · https://www.quantinuum.com/blog/teleporting-to-new-heights [C]
[9] Quantinuum · Magic states in the [[6,2,2]] code at 7×10⁻⁵ infidelity · arXiv:2506.14688 · 2025-06 · https://arxiv.org/abs/2506.14688 [D]
[10] Quantinuum · Fault-tolerant QAOA and HHL with a Steane-code T gate · arXiv:2603.04584 · 2026-03 · https://arxiv.org/abs/2603.04584 [D]
[11] Tham, Goldman, Debnath, Nielsen, Pisenti, Wright, Gamble, Delfosse (IonQ) · Breakeven demonstration of quantum low-density parity-check codes · arXiv:2606.06455 · 2026-06-04 · https://arxiv.org/abs/2606.06455 [D]
[12] Quantinuum · The H2 racetrack trapped-ion quantum processor · arXiv:2305.03828 · 2023-05 · https://arxiv.org/abs/2305.03828 [D]
[13] IonQ · Real-time decoding for trapped-ion QEC (1–5 ms syndrome cycles) · arXiv:2608.25027 · 2026-08 · https://arxiv.org/abs/2608.25027 [D]
[14] Quantinuum · Grid trap with 2.5 kHz ion exchange (arXiv:2403.00756) and junction transport at 4 m/s (arXiv:2206.11888) · 2024-03, 2022-06 · https://arxiv.org/abs/2403.00756 · https://arxiv.org/abs/2206.11888 [D]
[15] Main, Drmota, Nadlinger, Ainley, Agrawal, Nichol, Srinivas, Araneda, Lucas (Oxford) · Distributed quantum computing across an optical network link · Nature · 2025-02 · https://www.nature.com/articles/s41586-024-08404-x [D]
[16] Duke / University of Maryland · Remote ion–ion entanglement at 250 s⁻¹ · arXiv:2404.16167 · 2024-04 · https://arxiv.org/abs/2404.16167 [D]
[17] Guo, Ye, Kim et al. (Tsinghua) · Site-resolved two-dimensional quantum simulator with 512 ions · Nature · 2024-06 · https://www.nature.com/articles/s41586-024-07459-0 [D]
[18] Honeywell · $600 million capital raise for Quantinuum at $10 B pre-money valuation · press release · 2025-09-04 · https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [G]
[19] Quantinuum · Pricing of upsized IPO; Second quarter 2026 results · press releases · 2026-06-03, 2026-08 · https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering · https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results [G][C]
[20] IonQ · IonQ completes acquisition of Oxford Ionics · newsroom · 2025-09-17 · https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[21] IonQ · IonQ completes acquisition of SkyWater Technology · newsroom · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[22] Quantum Computing Report · Quantum Art extends Series A to $140 M to scale trapped-ion architecture · trade press · 2026-04-27 · https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[23] AQT · LYNX quantum volume record · company news · 2026-05 · https://www.aqt.eu/lynx-quantum-volume-record/ ; eleQtron · €57 million Series A · company news · 2026-05-05 · https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[24] Quantinuum · Accelerated roadmap to universal fault-tolerant quantum computing by 2030 · press release · 2024-09-10 · https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[25] IonQ · IonQ's accelerated roadmap · company blog · 2025-06-13 · https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality ; PostQuantum · IonQ company profile (2020 roadmap record) · 2026 · https://postquantum.com/quantum-computing-companies/ionq/ [R][P]
[26] IonQ · IonQ announces record second quarter 2026 revenues, growing 287% YoY · newsroom · 2026-08 · https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[27] Infineon Technologies · Trapped ion quantum computing (Villach QPU platform, 6–12″ wafers, Gen-3 traps, named partners) · product page · 2026 · https://www.infineon.com/promo/trapped-ions [C]
[28] Quantinuum and Infineon · Infineon and Quantinuum announce partnership to accelerate quantum computing · press release · 2024-11-19 · https://www.quantinuum.com/press-releases/infineon-and-quantinuum-announce-partnership-to-accelerate-quantum-computing-towards-meaningful-real-world-applications [C]
[29] AQT · AQT lands million euro contract (≈ €9.8 M, 20-qubit system for LRZ / Munich Quantum Valley) · company news · 2023-12-05 · https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[30] PostQuantum · The optical table's hidden supply chain: who really wins if trapped-ion quantum computing wins · analysis · 2026 · https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[31] DARPA · Quantum Benchmarking Initiative, Stage B selection · programme page · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[32] Loschnauer, Mosca Toba, Hughes, King, Weber, Srinivas, Matt, Nourshargh, Allcock, Ballance, Matthiesen, Malinowski, Harty · Scalable, high-fidelity all-electronic control of trapped-ion qubits · arXiv:2407.07694; PRX Quantum 6, 040313 · 2024-07-10, 2025 · https://arxiv.org/abs/2407.07694 [D]
[33] Malinowski, Allcock, Ballance (Oxford Ionics) · How to wire a 1000-qubit trapped ion quantum computer · PRX Quantum 4, 040313 (arXiv:2305.12773) · 2023-05-22 · https://arxiv.org/abs/2305.12773 [S]
[34] University of Sussex · Universal Quantum wins €67 M contract from the German Aerospace Center · newsroom · 2022-11-02 · https://www.sussex.ac.uk/broadcast/read/59206 [P]
[35] DLR Quantum Computing Initiative · QSea I (eleQtron MAGIC demonstrator with NXP and ParityQC, 2023-03-01 to 2027-02-28) · programme page · 2024-05-30 · https://qci.dlr.de/en/qsea-i/ [G][C]
[36] The Quantum Insider · Trapped-ion quantum computing: companies, technology and where it stands in 2026 · trade press · 2026-06-12 · https://thequantuminsider.com/2026/06/12/trapped-ion-quantum-computing-companies-technology-and-where-it-stands-in-2026/ [P]
[37] The Quantum Insider · Top Chinese quantum computing companies in 2026 · trade press · 2026-05-15 · https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[38] NVIDIA · NVQLink architecture integrates accelerated computing with quantum processors · developer blog · 2025-11 · https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]

## Open verification items

- Electronic-gate duration on the 2025 record: the retrievable text of arXiv:2510.17286 states neither the 225.8 µs (2025) nor the ≈ 120 µs (2024) figure. Unverified.
- Quantinuum's "near five-nines logical fidelity with a novel QEC code family" (Q2-2026 call): no paper, no code family named as of 2026-09-03.
- IonQ Forte Mølmer–Sørensen gate times on 30+-ion chains (550–883 µs, median 672 µs; 1Q 110 µs) appear in the main report without a numbered source; not independently verified here.
- Export-control classification of a bare, un-populated ion-trap chip under the September-2024 US quantum ECCNs (4A906 family) and allied national controls — the rule text itself was not consulted here; unverified.
- Infineon press release infpss202604-080 ("Quantum chips: Infineon contributes industrialization", 2026-04) could not be retrieved (navigation-only page); wafer volumes and any new 2026 partners unconfirmed.
- Chinese trapped-ion commercial activity: Qudoor (AbaQ, 32+ claimed patents) is the only ion-trap vendor named in the surveyed 2026 sources; no funding amount, date, valuation or qubit count found.
- Universal Quantum: no delivery, milestone or fidelity result announced against the €67 M DLR contract as of 2026-09-03.
- AQT and QUDORA Technologies (Braunschweig; Tokyo subsidiary opened 2026-05): no equity funding round with a stated amount and date found.
- Quantinuum's Q2-2026 release discloses no bookings, backlog, Helios unit sales or customer names.
