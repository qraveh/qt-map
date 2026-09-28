---
id: ct_ionaod
name: Free-space laser addressing of ions (AOM/AOD beams)
layer: "5 Control"
status: demonstrated
since: 2016
one_line: "Gate light from a room-temperature optical bench is switched and steered onto individual ions of one chain by multi-channel acousto-optic modulators or acousto-optic deflectors and focused through bulk optics above the trap."
verdict: "The most common ion control in the register, published to 40 addressed ions per chain with neighbour crosstalk of 10⁻³–10⁻²; no per-pair benchmark of a longer free-space-addressed chain was found as of 2026-09-26, and IonQ's roadmap past Tempo rests on chips and photonic links."
updated: 2026-09-26
---

AOM = acousto-optic modulator; AOD = acousto-optic deflector; MS = Mølmer–Sørensen gate; DRB = direct randomized benchmarking; ε = the neighbour's Rabi frequency over the target's; QV = quantum volume; G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An optical bench sends gate light through viewports and a high-aperture objective; acousto-optics set which ion is lit and the light's amplitude, frequency and phase. A multi-channel AOM gives one RF channel per fixed beam — 32 at 355 nm in the 2016 five-qubit Maryland machine, the technology's origin [D][585]; an AOD maps RF frequency to angle, so a steered beam reaches any ion [D][100]. Hyperfine qubits take a Raman pair — 355 nm for ¹⁷¹Yb⁺ [D][586], 532 nm for ¹³³Ba⁺ [D][109]; ⁴⁰Ca⁺ optical qubits take one 729 nm beam [D][253].
Attributes: optical control at room temperature; coherent errors; bulk optics; one assembly per chain.

## Physics & limits
Crosstalk. A Gaussian field falls as exp(−d²/w²) — ~10⁻¹² at EURIQA's 0.85 µm waist and 4.43 µm pitch [S] — yet the neighbour sees up to 2.5% of the target's Rabi frequency [D][254]: aberration and scatter set the floor. Published neighbour figures, in differing measures, fall from <4% in 2016 [D][585] to <9×10⁻⁴ [D][587]. For a Rabi ratio ε, a spectator rotated by εθ loses ≈(εθ/2)², 2.5×10⁻⁴ at ε = 10⁻² for a π pulse [S]; being coherent, the error compensates — intensity-scaling light-shift pulses cut the AQT demonstrator's 0.5% neighbour figure to 1.3×10⁻⁴ [D][253].
Pointing and phase. Jitter δx shifts the Rabi rate by ~(δx/w)² [S]; Forte sizes its 1.5 µm waist against pointing noise [D][100]. At 355 nm, 56 nm of path between counter-propagating arms is 1 rad of gate phase [S]; Forte configures two of its four paths for phase-insensitive single-qubit gates [D][100].
The AOD. θ = λf/v; resolution is aperture time × bandwidth; thermal drift needs in-situ angle calibration [G][588]. Duke's UV AOD deflects 6 mrad over a 100 MHz band [D][587], i.e. v ≈ 5.9 km/s [S]. The RF also shifts the optical frequency with position; AQT's crossed AODs cancel it [D][253]. ~50 beam diameters of steering [D][587] span 25–50 ions at 3–4 µm spacing [S]. Pairs are served in sequence [D][109]: 15 disjoint pairs at Forte's median 672 µs MS gate take ~10 ms [S]. Field of view and serialisation hold a chain near 30–40 ions [S].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2016-08 | 5 ¹⁷¹Yb⁺; 32-channel UV AOM; crosstalk <4%; XX gate 235 µs | Univ. of Maryland | [D][585] |
| 2019-11 | 11 qubits in 13 ions; global + addressed 355 nm beams; 2Q 97.5% | IonQ | [D][586] |
| 2021-06 | Crossed AODs, 729 nm; neighbour crosstalk 0.5%; 24-ion GHZ 54.4(7)% | Innsbruck / AQT | [D][253] |
| 2021-10 | 32 beams, 0.85 µm waist; 13 qubits in 15 ions; 2Q 98.5–99.3% | EURIQA (Maryland/Duke) | [D][254] |
| 2023-08 | 4 AODs; 30 qubits in 36 ions; 2Q DRB median 4.64×10⁻³ | IonQ Forte | [D][100] |
| 2026-01 | AOD module <1 ft²; crosstalk <9×10⁻⁴; 30-ion chain; 240 ns switching | Duke | [D][587] |
| 2026-06 | 40 ¹³³Ba⁺; AOD-steered 532 nm Raman beams | IonQ | [D][109] |

Above 40 ions only claims exist: Tempo's page lists 100 "target" qubits and 99.9% "target fidelity", with no addressing method [C][101]. Tsinghua's 512-ion crystal runs global 411 nm beams — free space without addressing [D][121].

## Manufacturing, materials & supply chain
An assembly, not a wafer: a pulsed UV laser (EURIQA: Coherent Paladin 355-4000) [D][254], acousto-optics — fused silica in the UV, TeO₂ in the visible [G][588] — objectives and RF synthesis; Duke's module uses a Brimrose AOD [D][587]. Gooch & Housego and AA Opto Electronic are also named [P][322]; G&H deflectors steer 3,000- and 6,100-atom tweezer arrays too [C][504], a supply shared with cx_aod. AQT fits 12 qubits in two 19-inch racks, 2 m², <2 kW [C][382].

## Control, readout & I/O burden
A multi-channel AOM needs one RF channel per ion at fixed pitch — EURIQA idles two end ions to keep the spacing uniform [D][254]; Forte's four AODs, each behind an AOM that sets amplitude, frequency and phase, reach any of 40 ions and free the trapping potential [D][100]. Switching (~240 ns) [D][587] is negligible; serialisation is the latency — Ba-testbed code cycles take 35–86 ms, all ions shelved to D₅/₂ during mid-circuit readout [D][109]. At 10³ ions: ~25 benches plus photonic links [S].

## Role in the stack
Slot 5 of "Trapped ions — linear Paul trap with individual laser addressing" and "Trapped ions — QCCD (transport between zones)". It **requires** fab_optics (bulk optics above the trap), **provides** the free-space fields g_ms requires, and is **replaced** by ct_ionlaser (integrated delivery) and ct_ionmw (electronic gates, two-qubit error 8.4(7)×10⁻⁵ [D][102]). Nine register machines carry it, all primary: IonQ Aria, Forte, Tempo and the 40-ion Ba testbed; AQT IBEX Q1; Qudoor AbaQ; Tsinghua; Innsbruck; Maryland/Duke. Five ✅ cells cite addressing hardware; Aria's ✅ rests on its 2019 predecessor [D][586]; Tsinghua's shows global beams; Tempo is 🔎; Qudoor's control is undisclosed. AQT and Innsbruck are profiled as hyperfine; their cited papers use ⁴⁰Ca⁺ optical qubits [D][253][D][255]. Gap G-ionaod is closed, with ion_chain in place of the proposed ion_elec.

## Evidence — how the numbers were measured
Crosstalk is quoted as Rabi ratio, intensity ratio (ε²) or spectator error — Duke calls a Rabi ratio "intensity crosstalk" [D][587] — and measured by moving one ion through the beam [D][253], by flag ions [D][254] or by simultaneous benchmarks [D][109]. Forte's 435-pair DRB finds no significant dependence on ion distance but significant out-of-model errors [D][100]. Of the vendor pages opened, only AQT's specifies crosstalk, neighbour <1.8×10⁻², as of 2026-09-26 [C][382].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IonQ | developer | US | AOD addressing on Forte and the 40-ion Ba testbed | [D][100][D][109] |
| Alpine Quantum Technologies | developer | AT | Crossed-AOD 729 nm addressing, rack systems | [D][253][C][382] |
| University of Innsbruck | research | AT | Steerable 729 nm beams, 16 ions | [D][255] |
| Univ. of Maryland / Duke | research | US | 32-channel AOM; compact AOD module | [D][254][D][587] |
| Tsinghua University | research | CN | 512-ion crystal, global beams | [D][121] |
| Qudoor | developer | CN | In-house lasers and control; addressing undisclosed | [P][302] |
| Gooch & Housego | supplier | UK | AODs, AOMs | [C][504] |

**Money.**
- 2023-12-05 · AQT · 20-qubit two-rack computer for LRZ and Munich Quantum Valley, Bavarian funding · ~EUR 9.8 M · contracted [C][323]
- 2025-09-17 · IonQ · acquisition of Oxford Ionics (chip-manufactured traps) · not stated in the release · closed [C][18]

**Market & supply chain.** Lasers, acousto-optics, objectives and RF are merchant parts; ytterbium's UV lines demand expensive, power-limited lasers [P][322]. Both architectures serve G2, G3, G6 and G7.

**IP & standards.** IonQ filings on compensating Raman beam-geometry errors (JP 2024, EP 2025) [P][375]; no crosstalk-reporting standard found as of 2026-09-26.

**Roadmaps & track record.** IonQ (2025-06-13): Tempo, 100 qubits, 2025; 10,000 on one chip, 2027; >2,000,000 by 2030, naming Oxford Ionics 2D traps and photonic links as the means [R][132]. Tempo's figures remain targets [C][101]; the 2026-04-14 two-system photonic link gave no rate or fidelity [C][589]. AQT's LYNX claims QV 32,768 and lower laser phase-noise sensitivity, no qubit count [C][128].

**Strategic reading.** The fastest route to a working 30–40-ion machine and the yardstick for integrated and electronic delivery, but not a scaling path; value moves to trap chips and links.

## Outlook & open questions
Confirm if, by 2027-12-31, IonQ publishes Tempo's per-pair gate times, fidelities and addressing method, or an addressed chain above 60 ions is benchmarked; demote if IonQ's next systems ship on electronic or integrated delivery. Open questions. (1) What sets the neighbour floor below 10⁻³ — aberration, scatter or RF intermodulation? (2) Can multi-tone AODs run parallel gates without stray beams? (3) How does pointing drift scale with RF duty cycle? (4) Does double-sided steering hold at 100 ions? (5) When does a photonic link beat a longer chain?

## Sources

[18] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[100] J.-S. Chen *et al.*, “Benchmarking a trapped-ion quantum computer with 30 qubits,” *Quantum*, vol. 8, Art. no. 1516, Nov. 2024, doi: [10.22331/q-2024-11-07-1516](https://doi.org/10.22331/q-2024-11-07-1516). [arXiv:2308.05071](https://arxiv.org/abs/2308.05071). [D]
[101] IonQ, “IonQ Tempo: 100-Qubit Quantum Computer (#AQ 64).” [Online]. Available: https://ionq.com/quantum-systems/tempo [C]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[109] E. Tham *et al.*, “Breakeven demonstration of quantum low-density parity-check codes,” [arXiv:2606.06455](https://arxiv.org/abs/2606.06455), Jun. 2026. [D]
[121] S.-A. Guo *et al.*, “A site-resolved two-dimensional quantum simulator with hundreds of trapped ions,” *Nature*, vol. 630, no. 8017, pp. 613–618, May 2024, doi: [10.1038/s41586-024-07459-0](https://doi.org/10.1038/s41586-024-07459-0). [D]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[253] I. Pogorelov *et al.*, “Compact Ion-Trap Quantum Computing Demonstrator,” *PRX Quantum*, vol. 2, no. 2, Art. no. 020343, Jun. 2021, doi: [10.1103/PRXQuantum.2.020343](https://doi.org/10.1103/PRXQuantum.2.020343). [arXiv:2101.11390](https://arxiv.org/abs/2101.11390). [D]
[254] L. Egan *et al.*, “Fault-tolerant control of an error-corrected qubit,” *Nature*, vol. 598, no. 7880, pp. 281–286, Oct. 2021, doi: [10.1038/s41586-021-03928-y](https://doi.org/10.1038/s41586-021-03928-y). [arXiv:2009.11482](https://arxiv.org/abs/2009.11482). [D]
[255] L. Postler *et al.*, “Demonstration of fault-tolerant universal quantum gate operations,” *Nature*, vol. 605, pp. 675–680, 2022, doi: [10.1038/s41586-022-04721-1](https://doi.org/10.1038/s41586-022-04721-1). [arXiv:2111.12654](https://arxiv.org/abs/2111.12654). [D]
[302] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Apr. 10, 2026. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[382] Alpine Quantum Technologies, “19-inch rack-mounted quantum computer,” AQT. [Online]. Available: https://www.aqt.eu/products/ibex-q1/ [C]
[504] Gooch & Housego (G&H), “G&H Acousto-Optic Deflectors Referenced in Nature Papers Demonstrating 3,000 & 6,100 Qubit Quantum Systems,” G&H, Mar. 2026. [Online]. Available: https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [C]
[585] S. Debnath, N. M. Linke, C. Figgatt, K. A. Landsman, K. Wright, and C. Monroe, “Demonstration of a small programmable quantum computer with atomic qubits,” *Nature*, vol. 536, no. 7614, pp. 63–66, Aug. 2016, doi: [10.1038/nature18648](https://doi.org/10.1038/nature18648). [arXiv:1603.04512](https://arxiv.org/abs/1603.04512). [D]
[586] K. Wright *et al.*, “Benchmarking an 11-qubit quantum computer,” *Nat. Commun.*, vol. 10, Art. no. 5464, Nov. 2019, doi: [10.1038/s41467-019-13534-2](https://doi.org/10.1038/s41467-019-13534-2). [arXiv:1903.08181](https://arxiv.org/abs/1903.08181). [D]
[587] J. Yu *et al.*, “Design and Characterization of Compact Acousto-Optic-Deflector Individual Addressing System for Trapped-Ion Quantum Computing,” [arXiv:2601.01647](https://arxiv.org/abs/2601.01647), Jan. 2026. [D]
[588] R. Paschotta, “Acousto-optic Deflectors,” RP Photonics Encyclopedia. [Online]. Available: https://www.rp-photonics.com/acousto_optic_deflectors.html [G]
[589] IonQ, “IonQ Achieves Key Photonic Interconnect Milestone, Demonstrating Networked Quantum Systems Using Entanglement,” Apr. 14, 2026. [Online]. Available: https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement [C]

## Open verification items
- Fang et al., PRL 129, 240504 (2022), arXiv:2206.02703, on crosstalk suppression in individually addressed gates: not read, Crossref and PubMed rate-limited (2026-09-26); not cited.
- USTC double-sided AOD addressing (arXiv:2306.01307): neighbour Rabi crosstalk 1.19(5)×10⁻³ in the current abstract but 6.32×10⁻⁴ in the 2023 HTML version; published author list unconfirmed; not cited (2026-09-26).
- Tempo's species, gate time and addressing method, Aria's own architecture and Qudoor AbaQ's control are not disclosed in the sources opened (2026-09-26); these register cells are inferences.
- Register profiles give "hyperfine qubit" for AQT IBEX Q1 and Innsbruck, where the cited papers describe ⁴⁰Ca⁺ optical qubits at 729 nm; the IBEX Q1 page lists 2,000 gates per circuit against the register's 1,000 (2026-09-26).
- No quantitative source was opened for RF power per tone, multi-tone intermodulation or AOD thermal pointing drift in ion systems (2026-09-26).
- Postler et al.'s Nature publication date was not confirmed (Crossref rate-limited, 2026-09-26); the record carries the year.
