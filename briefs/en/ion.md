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

Attributes (technology graph): carrier affinity 0.0 — wholly natural, every ion identical by physical law, no fabrication variance to calibrate out; entangling time 10⁻⁴·² s (≈ 63 µs), deterministic, no heralding; readout by fluorescence on a cycling transition, ≈ 10 µs, non-destructive, mid-circuit capable; mobility by physical transport — ions are shuttled, not wired; control optical, at room temperature; error structure as the code sees it coherent, leakage, Pauli; manufacturing MEMS-class surface-electrode traps.

## Physics & limits

Trap frequencies of a few MHz set the clock. Spin–motion coupling scales with the Lamb–Dicke parameter times the drive, so a gate much faster than a motional period either excites the wrong modes or needs optical power that reintroduces scattering; µs-to-hundreds-of-µs gates are a physical compromise, not an engineering lapse. Memory is the opposite: in magnetically insensitive clock states one ion holds coherence beyond an hour [D][98], five to six orders longer than a superconducting qubit. Idle error is nearly free; idle time is what costs.

The floor belongs to the drive, not the carrier: laser gates carry an irreducible spontaneous-emission floor, and 8.4(7)×10⁻⁵ two-qubit error at Doppler temperature without ground-state cooling [D][96] shows it is removable. What remains is anomalous heating from electrode surfaces, mode crowding as chains lengthen, and background-gas collisions that reorder or eject a chain. That last is the architectural problem: a decoder built for stochastic Pauli noise instead sees ions leak into metastable manifolds or vanish. Leakage is small enough to quote — 1.1×10⁻⁵ per Clifford on Helios [D][91] — but quoted separately because it is not Pauli. Cryogenic traps, sympathetic cooling, metastable erasure encodings and better vacuum would move the floor.

## Engineering state of the art

Best-demonstrated and typical-at-scale have converged unusually far: Helios runs 98 Ba⁺ qubits at 7.9×10⁻⁴ two-qubit error with all-to-all connectivity, within an order of magnitude of the record. The gap is speed — the gate is ≈ 70 µs, but a full-width layer takes ≈ 55 ms once sorting, transport and re-cooling are counted; transport was ~60% of runtime on H2 [D][91], [104].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-07 | All-electronic control, 10 qubits / 7 zones: 2Q 99.97(1)% | Oxford Ionics | [D][248][G:OXIONICS-ALLELEC-2024-07] |
| 2025-10 | 2Q error 8.4(7)×10⁻⁵, no ground-state cooling | Oxford Ionics / IonQ | [D][96][G:ELECGATE-9999-2025-10] |
| 2025-11 | Helios 98 Ba⁺: 2Q 7.9×10⁻⁴, SPAM 3.3–4.8×10⁻⁴, leakage 1.1×10⁻⁵/Clifford | Quantinuum | [D][91] |
| 2026-02 | 48 corrected logical qubits ([[80,48,4]]), logical gate infidelity 1.0–1.2×10⁻⁴ | Quantinuum | [D][99][G:HELIOS-ICEBERG-2026-02] |
| 2026-05 | Quantum volume 32,768, rack-mounted LYNX | AQT | [C][115] |
| 2026-06 | qLDPC memory break-even: [[18,4,3]] 3.95 ± 0.68 s vs 3.3 ± 0.9 s | IonQ | [D][103][G:IONQ-QLDPC-BREAKEVEN-2026-06] |

The dominant error term at scale is not the gate: it is the cost of moving ions — transport excitation, re-cooling, re-ordering — plus leakage the decoder cannot absorb. High-rate code demonstrations discard 75–97% of shots at depth [D][99].

## Manufacturing, materials & supply chain

Traps are MEMS-class silicon parts, not qubit-defining lithography: the ion is perfect, so wafer variance shows up as electrode geometry and surface quality, never as qubit-to-qubit spread. Two fabs matter. Infineon runs a dedicated QPU platform in Villach on 6- to 12-inch wafers with anodic wafer bonding; its Generation-3 traps add out-of-plane electrodes claimed to raise confinement ~10×, with eleQtron (three generations), Oxford Ionics, Innsbruck and ETH Zurich as named users [C][249]. Honeywell fabricates Quantinuum's traps in-house — Helios carries 1,228 electrodes [D][91] — and the Sol grid trap is back from fabrication and in validation [C][112]; Infineon separately partnered with Quantinuum on next-generation traps in 2024-11 [C][250]. Infineon is a single point of failure for IonQ/Oxford Ionics, eleQtron and Universal Quantum at once [P][251] — which is what IonQ's ≈ $1.8 B purchase of SkyWater (closed 2026-07-31) buys its way out of [C][18].

The second concentration is optical: TOPTICA (> €140 M revenue, ~600 staff) supplies most major ion experiments, and the UV end — 369 nm for Yb⁺ — is the constrained part [P][251]. Vacuum hardware and atomic sources are commodity; photonic interconnects re-import a cryogenic dependency through SNSPDs [P][251][G:SNSPD-VENDORS-2026]. Unit economics: AQT delivered a 20-qubit rack to LRZ / Munich Quantum Valley for ≈ €9.8 M (2023-12-05, Bavarian Hightech Agenda) [C][252] — ≈ €0.5 M per qubit, turnkey. Export exposure runs through the September-2024 US quantum ECCNs; a bare trap chip's classification is unverified here.

## Control, readout & I/O burden

Per-ion optical addressing is what fails to scale linearly: Helios needs at least seven laser wavelengths alongside 1,228 electrode drives [D][91]. Readout is cheap — fluorescence onto a PMT or camera in ≈ 10 µs, non-destructive and natively mid-circuit. Latency demands are mild: IonQ assumes 1–5 ms syndrome cycles [D][105], inside NVQLink-class round trips [C][253][G:NVQLINK-2025].

The wall moves with N. At 10³ it is drive-source count and optical-table area; the WISE study argues a fully connected 1,000-ion machine could run from ~200 sources with in-trap switching electronics, at 40–2,600 gate layers per second [S][254][G:WISE-ARCH-2023] — paper design, no chip built. At 10⁴ it is inter-module: remote entanglement stands at 9.7 s⁻¹ over 2 m (Bell 96.9%) [D][108] and 250 s⁻¹ in a lab [D][109] against ~10⁴ s⁻¹ needed. At 10⁶ it is yield and laser power. Gate generation and microwave control belong to the sibling briefs.

## Role in the stack

The carrier feeds two named paths: *Trapped ions — QCCD, laser gates* (Quantinuum, AQT) and *Trapped ions — electronic gates, chip control* (IonQ/Oxford Ionics, eleQtron, Quantum Art). It requires surface-electrode trap microfabrication and optical/mechanical assembly, and is the substrate for the Mølmer–Sørensen gate, the electronic near-field microwave gate, metastable "omg" erasure encoding, shuttling, fluorescence detection and the ion–photon link. It replaces and conflicts with nothing: ions are a self-contained column, which is why switching away is total — nothing above the carrier survives but the compiler.

Derived clock = sum of the syndrome round: gate layers + transport + readout + reset. On the QCCD path transport dominates: ≈ 9.7×10⁻³ s per round, 9.0 ms of it transport, against a ≈ 5.5×10⁻² s full-width layer [D][91], [104]. On the electronic-gate path the round is ≈ 1.5×10⁻³ s, set by the gate layers [D][96]. That six-fold gap is the platform's defining number. Neighbouring empty slot: a cryogenic chip-integrated drive layer for ion traps — the SFQ/cryo-CMOS analogue — has no product-scale occupant.

## Verification (QCVV)

Headline two-qubit numbers come from randomized-benchmarking variants. The 8.4(7)×10⁻⁵ record is a subspace-leakage RB on one ion pair at Doppler temperature, not a device-wide figure, and the retrievable text gives no gate duration [D][96]. Helios's 7.9×10⁻⁴ is an averaged device figure, consistent with the earnings language "99.921%" [C][112]. Quantum volume and #AQ are vendor-defined composites with no replication protocol [C][92], [93]. RB also runs statically, so shuttling and re-cooling are invisible to quoted gate errors. Logical results carry an acceptance fraction (0.62(2) [D][99]) and IonQ's break-even is leakage-post-selected [D][103]; neither is unconditional. No ion platform has published Λ-type distance scaling.

Conflicts. The electronic gate's duration is 225.8 µs (2025) or ≈ 120 µs (2024) in the technology graph and unstated in the 2025 abstract — unverified. Quantinuum's "near five-nines logical fidelity with a novel QEC code family" [C][112] outruns the published 1.0–1.2×10⁻⁴ logical gate infidelity [D][99]; the code family is unpublished, so the [D] value stands. IonQ's Tempo is marketed at "99.9%" and #AQ 64 with no published gate times [C][93], [255].

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK | QCCD laser gates; Helios 98 q, 48 logical qubits; Sol, Apollo | [D][99] |
| IonQ | developer | US | Long chains plus Oxford Ionics electronic gates; qLDPC break-even; owns SkyWater | [D][103] |
| Honeywell | supplier | US | In-house MEMS fabrication of Quantinuum traps; anchor shareholder | [C][111] |
| Infineon Technologies | supplier | AT/DE | Merchant ion-trap foundry, Villach, 6–12″, Gen-3 traps | [C][249] |
| AQT | developer | AT | Rack-mounted 19″ ion systems; QV 32,768; LRZ installation | [C][252] |
| eleQtron | developer | DE | Microwave ion control; DLR QSea I demonstrator; €54 M backlog | [G][256] |
| Quantum Art | developer | IL | Multi-core trapped-ion architecture; $140 M Series A | [P][114] |
| Universal Quantum | developer | UK | Modular trap machine under a €67 M DLR contract; nothing delivered | [P][257] |
| Tsinghua University | research | CN | 512-ion 2D crystal analog simulation; hour-scale memory | [D][110] |
| Qudoor | developer | CN | AbaQ ion-trap systems and cloud; 32+ claimed patents | [P][226] |

**Money.**
- 2022-11-02 · Universal Quantum · DLR contract · €67 M · announced [P][257][G:UQ-DLR-67M-2022-11]
- 2023-12-05 · AQT · contract, 20-qubit system for LRZ · ≈ €9.8 M · Bavarian StMWK/StMWi · closed [C][252]
- 2025-11-06 · IonQ, Quantinuum · DARPA QBI Stage B · up to $15 M each · selected [G][60][G:QBI-STAGEB-2025-11]
- 2025-10-12 · IonQ · equity · $1.0 B + $2.0 B at $93/share · closed [G:IONQ-EQUITY-2025]
- 2025-09-04 · Quantinuum · round · $600 M at $10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G][111][G:QTM-600M-2025-09]
- 2025-09-17 · IonQ · M&A Oxford Ionics · $1.075 B · closed [C][17][G:IONQ-OXIONICS-2025]
- 2026-04-27 · Quantum Art · Series A extension · $100 M → $140 M · closed [P][114][G:QART-140M-2026-04]
- 2026-05-05 · eleQtron · Series A · €57 M · backlog €54 M · closed [C][115][G:ELEQTRON-57M-2026-05]
- 2026-06-03 · Quantinuum · IPO, Nasdaq QNT · $1.68 B gross at $60/share · closed [G][112][G:QTM-IPO-2026-06]
- 2026-07-31 · IonQ · M&A SkyWater · ≈ $1.8 B · closed [C][18][G:IONQ-SKYWATER-2026]
- 2026-06-30 · Q2 FY26 revenue · Quantinuum $8.0 M, cash $2.1 B, guidance $28–32 M; IonQ $80.1 M, cash $3.0 B, guidance $280–290 M [C][112], [255]

**Market & supply chain.** Equipment money sits with TOPTICA, Infineon and commodity vacuum vendors; concentration risk is real in two places only — UV lasers and Infineon's fab, which underpins three otherwise-independent developers [P][251]. Against ≈ €9.8 M for a 20-qubit rack [C][252], sector ion revenue is about one large system per quarter plus cloud access. Goals that pay: G1 (Tsinghua's simulator), G2 and G5 (cloud), G3 (Helios logical qubits, IonQ's qLDPC memory), G7 (AQT racks, eleQtron's backlog), G6 in prototype. G4 is funded by capital markets and DARPA, not customers.

**IP & standards.** Named families: Oxford Ionics' electronic qubit control and the WISE in-trap switching architecture [S][254]; Honeywell/Quantinuum QCCD junction and grid-trap patents behind 2.5 kHz ion exchange and 4 m/s transport [D][106]; Infineon's anodic-bonding 3D-electrode process [C][249]; ID Quantique's detector portfolio, now IonQ's [C][18]. No dated ion-specific patent count from a named database was found; the PatSnap 2026-06-30 cut carries no ion line [P][G:PATSNAP-2026-06]. No ion-specific standard exists.

**Roadmaps & track record.** Quantinuum: Helios (promised 2024-09-10 · for 2025 · launched 2025-11-05) [G:QTM-ROADMAP]; Sol (promised 2024-09-10 · for 2027 · trap chip fabricated, in validation); Apollo (for 2029 · "on schedule", prototypes only) [C][112]. Credibility high — promised dates met — except the unpublished five-nines code family. IonQ: 4,000 qubits (promised 2020 · for 2026 · missed ~40×) [P][118]; 256 qubits at 99.99% (promised 2025-06-13 · for 2026 · slipped to H1 2027) [R][118]; 10,000 on one chip (for 2027 · no published 2D-trap heating or interconnect data). Credibility mixed: the physics is peer-reviewable, the schedules are not. AQT delivers its QV records on time; Universal Quantum has announced nothing against its 2022 contract [P][257].

**Strategic reading.** If ions win, Honeywell and Infineon capture structural rent — one through vertical integration nobody can copy, the other as the only merchant trap fab — and TOPTICA becomes the choke point. IonQ's SkyWater purchase converts a supplier dependency into an owned asset: a bet that trap fabrication, not qubit physics, is the scarce input. The substitution threat is not superconducting circuits (faster clock, worse fidelity) but neutral atoms: same natural carrier, same optics-heavy engineering, thousands of sites already, fidelity closing. Bargaining power still sits with the platform vendors: Infineon's quantum unit is a rounding error inside a €15 B company [P][251] and cannot price like a monopolist.

*Open niche:* a small QCVV/SFQ house plugs in at three seams. First, transport-aware benchmarking: no published protocol charges shuttling and re-cooling to a gate-level figure of merit, yet those terms set the derived clock; a mirror-circuit variant reporting error per layer of a *moving* machine would be directly comparable across vendors. Second, acceptance- and leakage-corrected logical metrics: with post-selection discarding 62–97% of shots, a convention for unconditional logical error would settle several disputes above. Third, the empty cryogenic-drive slot: 4 K ion traps have no chip-integrated drive layer, making SFQ pulse generation inside the trap package an unclaimed question.

## Outlook & open questions

Confirm if: Sol ships in 2027 with ≥ 192 physical qubits on a 2D grid trap *and* a published layer time better than ≈ 55 ms; any ion vendor publishes Λ > 1 scaling across d = 3→5→7; remote entanglement passes 10³ s⁻¹. Demote if: IonQ has not shown 256 qubits at 99.99% by end-2027 (already slipped once); Sol leaves layer time unimproved; or the five-nines code family stays unpublished a year on.

Best case by 2029: Apollo lands with hundreds of logical qubits at 10⁻⁶–10⁻¹⁰ and ions own early fault tolerance, the clock deficit absorbed by depth-hungry algorithms. Worst case: 2D scaling multiplies transport cost instead of amortising it, layer time stays in tens of milliseconds, and ions become the high-fidelity low-throughput instrument for QEC research while neutral atoms and superconducting circuits take the volume.

Open questions: does grid-trap heating scale with zone count or electrode area? Can leakage be turned into erasure fast enough that decoders stop paying for it? What is the electronic gate's real duration at full width? Is 10⁴ s⁻¹ remote entanglement reachable at all? Who second-sources Infineon?

## Sources

[17] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[18] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[91] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[92] Quantinuum, “Quantum Volume.” [Online]. Available: https://www.quantinuum.com/glossary-item/quantum-volume [C]
[93] IonQ, “IonQ Forte: High-Performance Commercial Quantum Computer.” [Online]. Available: https://www.ionq.com/quantum-systems/forte [C]
[96] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[98] P. Wang *et al.*, “Single ion-qubit exceeding one hour coherence time,” *Nat. Commun.*, vol. 12, Art. no. 233, Jan. 2021, doi: [10.1038/s41467-020-20330-w](https://doi.org/10.1038/s41467-020-20330-w). [arXiv:2008.00251](https://arxiv.org/abs/2008.00251). [D]
[99] S. Dasu *et al.*, “Computing with many encoded logical qubits beyond break-even,” [arXiv:2602.22211](https://arxiv.org/abs/2602.22211), Feb. 2026. [D]
[103] E. Tham *et al.*, “Breakeven demonstration of quantum low-density parity-check codes,” [arXiv:2606.06455](https://arxiv.org/abs/2606.06455), Jun. 2026. [D]
[104] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828). [D]
[105] M. Ye, A. Maksymov, and N. Delfosse, “Real-time decoder for a MegaQuOp quantum computer using a single CPU,” [arXiv:2608.25027](https://arxiv.org/abs/2608.25027), Aug. 2026. [D]
[106] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756). [D]
[108] D. Main *et al.*, “Distributed quantum computing across an optical network link,” *Nature*, vol. 638, no. 8050, pp. 383–388, Feb. 2025, doi: [10.1038/s41586-024-08404-x](https://doi.org/10.1038/s41586-024-08404-x). [D]
[109] J. O'Reilly *et al.*, “Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking,” *Phys. Rev. Lett.*, vol. 133, Art. no. 090802, Aug. 2024, doi: [10.1103/PhysRevLett.133.090802](https://doi.org/10.1103/PhysRevLett.133.090802). [arXiv:2404.16167](https://arxiv.org/abs/2404.16167). [D]
[110] S.-A. Guo *et al.*, “A site-resolved two-dimensional quantum simulator with hundreds of trapped ions,” *Nature*, vol. 630, no. 8017, pp. 613–618, May 2024, doi: [10.1038/s41586-024-07459-0](https://doi.org/10.1038/s41586-024-07459-0). [D]
[111] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [C]
[112] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[114] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[115] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[118] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [P]
[226] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[248] C. Löschnauer *et al.*, “Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040313, Oct. 2025, doi: [10.1103/h4wk-v31j](https://doi.org/10.1103/h4wk-v31j). [arXiv:2407.07694](https://arxiv.org/abs/2407.07694). [D]
[249] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[250] Quantinuum, “Infineon and Quantinuum announce partnership to accelerate quantum computing towards meaningful real-world applications,” Nov. 19, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/infineon-and-quantinuum-announce-partnership-to-accelerate-quantum-computing-towards-meaningful-real-world-applications [C]
[251] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Apr. 10, 2026. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[252] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[253] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[254] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773). [S]
[255] IonQ, “IonQ Announces Record Second Quarter 2026 Revenues, Growing 287% YoY,” Aug. 5, 2026. [Online]. Available: https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[256] German Aerospace Center (DLR), “QSea I – Quantum computer demonstrator with 10 ion trap qubits,” DLR Quantum Computing Initiative. [Online]. Available: https://qci.dlr.de/en/qsea-i/ [G]
[257] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]

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
