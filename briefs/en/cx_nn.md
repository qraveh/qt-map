---
id: cx_nn
name: Static nearest-neighbour lattice
layer: "4 Connectivity / transport"
status: demonstrated
since: 2014
one_line: A coupling graph fixed at mask level in which each qubit interacts only with lithographic neighbours; the default topology under every fielded superconducting and spin processor.
verdict: Not a design choice but the residue of planar lithography. It caps codes at the surface/colour family by geometry, and every announced escape from it is roadmap, not hardware.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A connectivity primitive, not a qubit type: the interaction graph is frozen at mask level, each site coupling only to lithographic neighbours, because capacitive/inductive and exchange couplings decay over microns and nanometres. The anchor is Barends et al. (Google/UCSB, 2014-02): five Xmon qubits in a linear nearest-neighbour array, 2Q up to 99.4%, at the surface-code threshold [D][1]. IBM's heavy-hex arrived in 2019 as a *code* construction — a surface/Bacon–Shor hybrid with flag qubits, cutting fixed-frequency collisions "by several orders of magnitude" at the cost of coordination number [S][9]; the flagship has since returned to a square lattice [C][5].
Coordinates: fully fabricated affinity; no time constant, readout or control of its own — a topology, not a device; static, lithographic, coherent error: "heavy-hex (degree 2.3) or square lattice (degree 3.5–3.6) with on-chip couplers; ZZ crosstalk is the tax" (graph record).

## Physics & limits
The floor is not a coherence floor. Always-on coupling leaves residual ZZ; tunable couplers null the static part but add a flux line, a leakage path and flux-noise susceptibility [S][9]. In the only published full error budget at code scale — Google's d=7 run on Willow — CZ crosstalk contributes 5.5×10⁻⁴ [D][2]. The binding constraint is geometric: a stabiliser code with 2D-local checks obeys the Bravyi–Poulin–Terhal bound kd² ≲ n, so this topology hosts only the surface/colour family at order 2d² physical qubits per logical one — a rate no better qubit can raise. The second tax is routing: an arbitrary interaction on a degree-2.3–3.6 graph costs SWAP depth scaling with lattice diameter. Only breaking 2D locality moves the floor.

## Engineering state of the art
Best demonstrated is an isolated pair: IQM's flux-tunable-coupler CZ at 99.93% over 40 hours, with 99.98% 1Q and >99.94% simultaneous readout on the same device [D][3]. Typical at scale is IBM's fleet error per layered gate, 3.7×10⁻³ typical and 1.9×10⁻³ best (July 2026), measured full-width [D][8]. That ≈5× gap between a characterised pair and a full-width layer is the lattice tax; inside it the two-qubit gate dominates, about 40% of Google's colour-code budget [D][10]. Foundry spin arrays sit a generation behind, 2Q 99.04–99.56% [D][4].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2014-02 | Five-qubit linear array, 2Q up to 99.4% | Google/UCSB | [D][1] |
| 2024-12 | d=7 surface code, 105 q, Λ=2.14; CZ crosstalk 5.5×10⁻⁴ | Google Quantum AI | [D][2] |
| 2025-11 | Nighthawk: 120 q, 218 couplers, 5,000 2Q gates per circuit | IBM | [C][5] |
| 2026-04 | Twelve chiplets tiled into 108 q, median 2Q 99.1% (99.5% at 36 q) | Rigetti | [C][6] |

## Manufacturing, materials & supply chain
Superconducting lattices are Nb/Al junction films patterned by DUV or e-beam; EUV is not required and no fielded transmon lattice uses it — IBM runs 300 mm at Albany, Google in-house. Spin dot arrays are foundry-native and EUV-dependent: Intel 300 mm, >24,000 devices per wafer at 96% tune-up yield [D][7]; GlobalFoundries 22FDX for Quantum Motion; STMicroelectronics FD-SOI for Quobly [C][G:QUOBLY-115M-2026-06]. Uniformity, not peak fidelity, limits that branch: imec's eight-qubit device had a validated two-qubit gate on one of four pairs [D][11]. Export exposure attaches to the machine, not the topology (ECCN 4A906, 3A904, 3A901.a) [G][14].

## Control, readout & I/O burden
The lattice buys no wiring saving. Nighthawk carries 218 tunable couplers for 120 qubits: the coupler count — roughly 1.8 flux lines per qubit above drive and readout — sets the harness [C][5]. At 10³ the harness is buildable; at 10⁴ it binds on cryostat area and heat load, which IBM's 0.53 m² wiring area and 2.75 m³ vacuum volume per modular cell are sized against [C][12]; at 10⁶ nothing at room temperature closes. Both mitigations sit far below lattice scale: SEEQC's millikelvin SFQ control flip-chip-integrated with qubits, 1Q up to 99.9% [D][13], and HRL's 4-K cryo-CMOS sequencer running 18 qubits with no room-temperature real-time electronics [D][15].

## Role in the stack
It underlies the transmon path (IBM, Google, Rigetti, IQM, Fujitsu), the bosonic and dual-rail superconducting paths, the silicon and germanium spin paths (Intel, Diraq, Quantum Motion, HRL→IBM) and defect-spin nodes. It provides the 2D-local checks the rotated surface and colour codes need, and is the alternative to long-range on-chip couplers, shuttled spins and shared-line crossbars; switching costs a mask redesign. It conflicts with degree-≥6 qLDPC codes, all-to-all high-rate codes, transversal-permutation schemes and cm-scale 3D cavities. Having no transport step it adds zero to the transport term of the derived clock (= sum of the syndrome round: gate layers + transport + readout + reset); its cost hides in the gate term as SWAP depth. The neighbouring empty slot is a degree-≥6 static lattice at parity fidelity with degree-3.5.

## Verification (QCVV)
Crosstalk and coupler figures come from randomised or cross-entropy benchmarking on pairs or small subsets. The 5.5×10⁻⁴ CZ crosstalk is a fitted component of Google's device-wide error budget, not an independent measurement; no vendor publishes full-lattice simultaneous crosstalk. Error per layered gate is the only full-width metric in fleet use and only IBM reports it, so cross-vendor comparison of the lattice tax is impossible today. Rigetti's 99.5%→99.1% median drop across its 36→108-qubit tiling is unattributed [C][6].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| IBM | Developer | US | Heavy-hex then square lattices; Nighthawk 120 q | [C][5] |
| Google | Developer | US | Square lattices; d=7 code on 105 qubits | [D][2] |
| Rigetti | Developer | US | Tiles chiplets into 108 qubits | [C][6] |
| IQM | Developer | FI | Transmon line; isolated-pair CZ 99.93% | [D][3] |
| GlobalFoundries | Supplier | US | 22FDX spin-dot wafers | [C][G:GF-QTS-2026-05] |

**Money.**
- 2026-05-21 · US Dept of Commerce · CHIPS letters of intent, nine firms (IBM/Anderon $1 B, GlobalFoundries $375 M, Diraq ≤$38 M) · $2.013 B · LOI, non-binding [G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · five-year quantum commitment · >$10 B · announced [C][G:IBM-10B-2026-06]
- 2026-07-02 · IQM · Nasdaq/Helsinki listing · cash €337 M pro-forma · closed [C][G:IQM-LISTING-2026-07]
- 2026-08 · Rigetti · Q2-2026 results · revenue $5.1 M, cash $541.3 M · reported [C][G:RIGETTI-FIN-2026]

**Market & supply chain.** Transmon lattices consume DUV/e-beam tooling, flip-chip bonders, TWPA amplifiers and control racks; spin lattices consume ASML EUV inside Intel, GlobalFoundries and STMicroelectronics — a single point of failure the superconducting branch does not share. G1–G3 pay for the lattice; G4 is the goal it cannot reach unaided.

**IP & standards.** The IP is coupler-level: IBM US 11,727,297 B2 (granted 2023-08-15) claims an opposite-sign second coupling path cancelling coherent error [P][G:IBM-TCOUPLER-PATENT-2023]. Aggregate quantum families to 2026-06-30: IBM 4,388, Google 2,385 [P][16]. No topology standard exists.

**Roadmaps & track record.** IBM Nighthawk (promised 2025-06-10, for 2025, delivered 2025-12) [C][G:IBM-ROADMAP]; Kookaburra, the first step off pure nearest-neighbour connectivity (promised 2022-05-10 for 2025, redefined for 2026, undelivered as of 2026-09-04) [R][G:IBM-ROADMAP-2022]; Rigetti median 99.5% at 108 q (promised for end-2025, slipped to "later 2026", unmet) [R][G:RIGETTI-FIN-2026]. IBM ships the base lattice on time and misses every date beyond it.

**Strategic reading.** If this topology stays the only manufacturable one, the winners own 2D-local decoding and yield — IBM and Google in superconductors, CMOS foundries in spins — and the losers are high-rate-code startups betting on connectivity nobody can fabricate. If degree rises, leverage moves to coupler and packaging IP — what IBM's coupler patents and the HRL purchase buy.

*Open niche:* a small QCVV/SFQ house can plug in where none of the actors above publish: full-width simultaneous crosstalk as a vendor-neutral metric, coupling-map-aware decoder validation as coordination number changes, and verification of cryogenic control loops against the flux-line count a lattice degree implies.

## Outlook & open questions
Confirm or demote within 12–24 months: does Kookaburra ship a qLDPC memory on c-coupled hardware or slip again; does Rigetti reach median 99.5% at 108 qubits; does any vendor publish a full-lattice simultaneous-crosstalk number. Best case by 2029: degree-6 on-chip routing ships without a fidelity penalty and a planar lattice hosts a high-rate memory. Worst case: coordination stays near 3.5 and scale is bought with 2d² overhead. Open: whether the pair-to-full-width gap is intrinsic.

## Sources
[1] Barends, Kelly, Megrant et al. (Google/UCSB) · "Logic gates at the surface code threshold: superconducting qubits poised for fault-tolerant quantum computing" · Nature 508, 500 · 2014-02-19 · https://arxiv.org/abs/1402.4848
[2] Google Quantum AI · "Quantum error correction below the surface code threshold" · Nature 638, 920 · 2024-12-09 · https://www.nature.com/articles/s41586-024-08449-y
[3] Marxer, Vepsäläinen et al. (IQM) · "Above 99.9% fidelity single-qubit gates, two-qubit gates, and readout in a single superconducting quantum device" · arXiv:2508.16437 · 2025-08-22 · https://arxiv.org/abs/2508.16437
[4] Diraq with imec · 300 mm SiMOS two-qubit gates · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9
[5] IBM · "IBM delivers new quantum processors, software, and algorithm breakthroughs" (Nighthawk, Loon) [C] · IBM Newsroom · 2025-11-12 · https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance
[6] Rigetti · Cepheus-1-108Q general availability [C] · Rigetti Investor Relations · 2026-04-07 · https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system
[7] Intel · 300 mm quantum-dot device statistics · arXiv:2410.16583 · 2024-10 · https://arxiv.org/abs/2410.16583
[8] IBM · Quantum hardware page, error per layered gate [C] · 2026-07 · https://www.ibm.com/quantum/hardware
[9] Heavy-hexagon and heavy-square code construction (surface/Bacon–Shor hybrid with flag qubits) · arXiv:1907.09528 · 2019-07 · https://arxiv.org/abs/1907.09528
[10] Google Quantum AI · colour-code error budget on a square lattice · Nature · 2025-05 · https://www.nature.com/articles/s41586-025-09061-4
[11] imec with Diraq · eight-qubit 300 mm SiMOS device · Nature Communications 17, 5878 · 2026-07-09 · https://www.nature.com/articles/s41467-026-74597-6
[12] IBM · modular cryogenics, coupled cell prototypes [C] · IBM Quantum Blog · 2026-08-19 · https://www.ibm.com/quantum/blog/modular-cryogenics
[13] Jordan, Bernhardt, Rahamim, Kirichenko et al. (SEEQC) · "A quantum computer controlled by superconducting digital electronics at millikelvin temperature" · Nature Electronics · 2026-03-10 · https://www.nature.com/articles/s41928-026-01576-6
[14] US BIS · interim final rule, quantum ECCNs 4A906 / 3A904 / 3A901 · Federal Register · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[15] HRL Laboratories · self-sequenced silicon QPU, 18 exchange-only qubits · arXiv:2604.16216; Nature 2026-07-29 · https://arxiv.org/abs/2604.16216
[16] PatSnap · quantum patent-family counts to 2026-06-30 [P] · 2026-06-30 · (PatSnap report as cited in the main report's superconducting section)

## Open verification items
The title, authors and journal reference of arXiv:1907.09528 could not be retrieved from its abstract page; only the abstract text (heavy-hexagon / heavy-square construction, flag qubits, "several orders of magnitude" collision reduction) is quoted here. The 5.5×10⁻⁴ CZ-crosstalk figure is a component of Google's fitted device error budget, not an independently reported measurement. No full-lattice, simultaneously-gated crosstalk value exists for any vendor. The 40-basis-point median two-qubit drop across Rigetti's 36→108-qubit tiling is unattributed in both company releases. The PatSnap counts cited are secondary and are not independently confirmed against the database.
