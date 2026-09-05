---
id: enc_gkp
name: GKP grid encoding
layer: "2 Encoding"
tier: 2
status: emerging
since: 2020
one_line: A qubit encoded in periodic grid states of one bosonic mode — microwave cavity or optical — correcting small quadrature shifts and handing the decoder an analogue syndrome.
verdict: The only encoding whose syndrome is continuous, and the only one whose every headline number is still post-selected. Unconditional logical error remains unpublished on both branches.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Gottesman, Kitaev and Preskill (Phys. Rev. A 64, 012310, 2001) encode a qubit in a comb of position/momentum grid states of one oscillator: the stabilisers are commuting displacements, and shifts below half the lattice spacing are correctable [S][1]. Ideal grid states need infinite energy, so every device approximates them at finite squeezing. The graph record's 2020 date is Campagne-Ibarcq et al. (Yale, Nature 584, 2020-08-19): square and hexagonal GKP states in a superconducting microwave cavity, logical errors suppressed by feedback on non-destructive measurement rather than post-selection [D][2].
Coordinates: partly fabricated (0.75) — a continuous-variable mode inside a fabricated cavity or photonic circuit; no control channel, readout or transport of its own; Gaussian error structure. "Grid states in a bosonic (microwave cavity) or optical mode; corrects small shifts; needs ~10 dB squeezing" (graph record).

## Physics & limits
The syndrome is analogue: measuring each quadrature modulo the lattice period returns a real number, so the decoder receives the size of the shift, not a bit. That soft information is GKP's architectural argument, and why concatenating GKP under an outer code beats concatenating a bare qubit. The floor is squeezing: finite squeezing broadens each comb tooth, and once the shift distribution has weight beyond half the lattice spacing the correction applies the wrong displacement and the error becomes logical. The graph record's ~10 dB is the working requirement, architecture-dependent rather than a constant, and loss is what spends it. What moves the floor: higher-Q cavities, lower-loss photonics, state breeding to raise effective above physical squeezing, and an outer code that relaxes the per-mode requirement.

## Engineering state of the art
Best demonstrated is a memory, not a computation. The largest coherence gain from any bosonic code remains Yale's 2.27(7), on a GKP qubit with reinforcement-learning-tuned real-time correction [D][3]; the qudit extension gives 1.82(3) for a qutrit and 1.87(3) for a ququart, cavity T₁ = 631 µs [D][4]. Nord Quantique's single-mode grid qubit reaches 0.0081(2) logical error per round and SPAM 7(7)×10⁻⁴ on cardinal states, but only on shots surviving an all-agree post-selection, 0.24 in preparation × 0.39 in measurement [D][6]. Nothing here resembles Λ scaling, and the dominant budget term is acceptance, not the conditional error rate quoted.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-03 | Real-time GKP correction beyond break-even, gain 2.27(7) | Yale | [D][3] |
| 2025-05 | GKP qudits beyond break-even: qutrit 1.82(3), ququart 1.87(3) | UCSB/Google Quantum AI | [D][4] |
| 2025-06 | GKP state on an integrated SiN chip at room temperature, 0.62 dB effective squeezing | Xanadu | [D][5] |
| 2026-07 | Single-mode grid qubit: 0.0081(2)/round, survival 0.24×0.39 | Nord Quantique | [D][6] |

## Manufacturing, materials & supply chain
The two branches share no supply chain. Microwave GKP is machined, not lithographed: aluminium or niobium 3D cavities — Nord Quantique's is a double-post design — plus an ancilla transmon and readout chain per mode, and a refrigerator whose volume, not wafer area, sets the qubit count [D][6]. Optical GKP is a 300 mm silicon-nitride process at room temperature, with squeezed-light generation, photon-number-resolving detection and packaging as cost drivers; Xanadu reports 0.085 dB edge-coupling loss per facet, with Corning and DISCO [C][G:XANADU-PACKAGING-2026-06]. No GKP-specific export control exists; the microwave branch inherits ECCN 3A904 [G][11].

## Control, readout & I/O burden
Microwave GKP is control-heavy per mode. Stabilisation needs conditional-displacement drives and feedback inside the cavity lifetime, and each mode carries an ancilla transmon whose errors propagate into it — the ancilla, not the cavity, is the practical limit at 360 µs–1 ms storage [D][4][6]. The I/O unit is a mode plus a full transmon control-and-readout chain, so at 10³ modes the wiring burden exceeds a bare transmon lattice; efficiency pays only once one mode replaces many physical qubits. Optical GKP substitutes homodyne detection per mode and GHz feed-forward across thousands of detector channels, unproven at system level [D][7].

## Role in the stack
GKP requires a bosonic cavity mode in the microwave branch and a roughly 10 dB squeezed mode in the optical one; it supplies the inner qubit for bosonic concatenation and is the direct alternative to cat encoding in that slot. It sits on the superconducting bosonic path (Nord Quantique; Alice & Bob and AWS on the cat variant) and the photonic continuous-variable path (Xanadu), whose architecture concatenates GKP under a qLDPC outer code [C][G:XANADU-LIQUIDITY-2026-06]. Switching from cat to GKP swaps a biased channel for an unbiased one with an analogue syndrome: the outer code must be redesigned. The graph record fixes no characteristic time, so its contribution to the derived clock (= sum of the syndrome round: gate layers + transport + readout + reset, 1.44 µs on the cat path) is a stabilisation round no actor publishes.

## Verification (QCVV)
Three quantities are reported as if commensurable. Gain is a ratio of decay rates against the best passive encoding [D][3][4]; logical error per round is conditional on survival [D][6]; effective squeezing is a state-quality measure [D][5]. None converts into another. Xanadu's 0.62 dB effective squeezing is not comparable with raw quadrature squeezing such as the 1.4 dB on periodically poled thin-film lithium niobate [D][8], and its "24.1× above threshold" is a system-loss metric [R][G:XANADU-SPAC-2026-03]. No independent replication of the Nord Quantique or UCSB/Google results exists as of 4 Sep 2026.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Nord Quantique | Developer | CA | Single-mode microwave grid qubits | [D][6] |
| Xanadu | Developer | CA | On-chip optical GKP sources; GKP-under-qLDPC architecture | [D][5] |
| Google Quantum AI | Research | US | Qudit GKP beyond break-even, with UCSB | [D][4] |
| Corning | Supplier | US | Fibre-array packaging for Xanadu's chips | [C][G:XANADU-PACKAGING-2026-06] |

**Money.**
- 2025-11-06 · Nord Quantique and Xanadu · DARPA QBI Stage B selections · $5 M initial, up to $15 M each · DARPA · closed [G:QBI-STAGEB-2025-11]
- 2026-03-26 · Xanadu · SPAC listing with Crane Harbor · ~$302 M gross, ~40% below plan · closed; ~US$686 M liquidity at 2026-06-30 [C][G:XANADU-LIQUIDITY-2026-06]
- 2026-05-18 · Nord Quantique · growth equity · $30 M at a $1.4 B valuation · closed [C][G:NQ-1.4B-2026-05]
- 2026-08-28 · Xanadu · Toronto factory funding · CAD 195 M · Government of Canada · announced [G:XANADU-SPAC-2026-03]

**Market & supply chain.** No one sells GKP; both branches buy their host platform's equipment — cavity machining, TWPA readout and refrigerators on one side, a narrow set of squeezed-light and photon-number-resolving detector suppliers plus specialist packaging on the other. G3 and G4 are the only goals that pay for GKP.

**IP & standards.** No dated GKP-specific patent-family count was found; aggregate sector figures (IBM 4,388, Google 2,385 families to 2026-06-30) do not break out continuous-variable encodings [P][9]. The 2001 construction is prior art, pushing defensible IP into state preparation, breeding and ancilla-control circuits. No standards activity found.

**Roadmaps & track record.** Xanadu (promised 2026-08-31): loss 24.1× above threshold in 2026 → 1.0× in 2030, 200 logical qubits by 2029, 1,000+ by 2031, on a GKP-plus-qLDPC architecture [R][G:XANADU-SPAC-2026-03]. Nord Quantique (company material): 100+ logical by 2029 at "1:1 physical to logical" [R][10]. Xanadu quantified its roadmap but raised ~40% below plan against a best published state of 0.62 dB; Nord Quantique's claim rests on a device whose combined survival is under 10%.

**Strategic reading.** GKP is the hardware-efficiency bet against surface-code brute force: if the squeezing and acceptance gaps close, one mode replaces the tens-to-hundreds of physical qubits an outer code needs. If they hold, both developers fall back on cat or discrete-variable encodings and lose the qubit-count argument behind their valuations, while surface-code incumbents lose nothing. Cat encoding is the substitution threat in the same slot.

*Open niche:* a small QCVV/SFQ house can plug in where the field is weakest: unconditional (non-post-selected) logical-error characterisation, protocols making gain, per-round error and effective squeezing mutually convertible, and independent replication of survival claims.

## Outlook & open questions
Confirm or demote within 12–24 months: does any GKP demonstration publish an unconditional logical error rate; does Nord Quantique lift combined survival above 10%; does an optical GKP state pass 1 dB effective squeezing. Best case by 2029: a multi-mode GKP logical qubit below break-even without post-selection, under a qLDPC outer code. Worst case: it stays a post-selected memory while cat and erasure encodings carry the bosonic path.

## Sources
[1] Gottesman, Kitaev, Preskill · "Encoding a qubit in an oscillator" · Phys. Rev. A 64, 012310 · 2001 · https://arxiv.org/abs/quant-ph/0008040
[2] Campagne-Ibarcq, Eickbusch, Touzard, Zalys-Geller, Frattini, Sivak et al. (Yale) · "Quantum error correction of a qubit encoded in grid states of an oscillator" · Nature 584, 368 · 2020-08-19 · https://www.nature.com/articles/s41586-020-2603-3
[3] Sivak, Eickbusch, Royer, Singh et al. (Yale) · "Real-time quantum error correction beyond break-even" · Nature 616 · 2023-03-22 · https://www.nature.com/articles/s41586-023-05782-6
[4] Brock, Singh, Eickbusch, Sivak, Ding, Frunzio, Girvin, Devoret (UC Santa Barbara and Google Quantum AI) · "Quantum error correction of qudits beyond break-even" · Nature 641, 612 · 2025-05-14 · https://www.nature.com/articles/s41586-025-08899-y
[5] Xanadu · "Integrated photonic source of Gottesman–Kitaev–Preskill qubits" · Nature · 2025-06-05 · https://www.nature.com/articles/s41586-025-09044-5
[6] Turcotte, St-Jean, Pessonneaux, Shillito, Kulchytskyy, Lachance-Quirion, Royer (Nord Quantique; Université de Sherbrooke) · "Quantum error correction of a grid-state qubit with state preparation and measurement errors below 10⁻³" · arXiv:2607.06718 · 2026-07-07 · https://arxiv.org/abs/2607.06718
[7] Xanadu · Aurora, 35 chips, 12 modes per 1 MHz cycle at ~14 dB total loss · Nature · 2025-01 · https://www.nature.com/articles/s41586-024-08406-9
[8] Shi, Baiju, Chen et al. · "Squeezed light generation in periodically poled thin-film lithium niobate waveguides" · arXiv:2508.08599; Nanophotonics · 2025-08-12 · https://arxiv.org/abs/2508.08599
[9] PatSnap · quantum patent-family counts to 2026-06-30 [P] · 2026-06-30 · (PatSnap report as cited in the main report's superconducting section)
[10] Nord Quantique · company roadmap statements [C] · 2026 · https://www.nordquantique.com/
[11] US BIS · interim final rule, quantum ECCNs including 3A904 (dilution refrigerators) · Federal Register · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent

## Open verification items
No unconditional (non-post-selected) logical error rate has been published for any GKP demonstration on either branch. The relationship between Xanadu's "24.1× above threshold" system-loss figure and its 0.62 dB effective squeezing is not derivable from the sources reviewed. The ~10 dB squeezing requirement is quoted from the graph record and is architecture-dependent; no single threshold paper is cited for it here. Nord Quantique's "100+ logical by 2029" is taken from company web material with no dated release located. No GKP-specific patent family or export-control category was found.
