---
id: enc_hf
name: Hyperfine / clock-state qubit
layer: "2 Encoding"
tier: 3
status: demonstrated
since: 1995
one_line: Two ground-state hyperfine or nuclear-spin sublevels at a field-insensitive clock point, the default qubit for every trapped-ion and neutral-atom vendor.
verdict: The least differentiating layer in the ion/atom stack — universal, so no moat and no lock-out; the contest is one layer up, in how the qubit is driven.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two hyperfine (or nuclear-spin) ground-state sublevels at a bias field where the first-order Zeeman shift vanishes, leaving only the quadratic term: coherence in seconds to hours, with single-ion memories reaching hour scale [2]. The lineage is the field's own: NIST's first ion-trap logic gate stored a qubit in the internal states of one laser-cooled ion (Monroe, Meekhof, King, Itano, Wineland, PRL 75, 4714, 1995) [1], the default for ions and later atoms ever since.
f = Pauli + leakage — leakage into neighbouring sublevels, invisible to a Pauli decoder; reach: four paths, QCCD and electronic-gate ions, alkali and alkaline-earth atoms [graph].

## Physics & limits
The clock point kills first-order field sensitivity; what remains is the quadratic Zeeman term plus field *gradients* across the register, so memory degrades with register size, not only time. The memory is not the limit — the drive is. Raman gates carry a spontaneous-scattering error falling only as ~1/Δ, and the scattered photon usually lands outside the qubit manifold: leakage, not Pauli error. Deleting the laser deletes that term — 2Q 99.97(1)%, 1Q 99.99916(7)% on a ten-qubit seven-zone trap [D][G:OXIONICS-ALLELEC-2024-07], 8.4×10⁻⁵ without ground-state cooling [D][4]. The control modality moves the floor, not the encoding.

## Engineering state of the art
| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-12-05 | ⁴³Ca⁺ clock qubit, chip microwave resonator, room temperature, unshielded: 1.5(4)×10⁻⁷ per Clifford, T₂ ≈ 70 s | Oxford | [D][3][G:OXFORD-1Q-1E-7-2024-12] |
| 2025-11 | Helios fleet (98 Ba⁺): 1Q 2.5×10⁻⁵, 2Q 7.9×10⁻⁴, leakage 1.1×10⁻⁵ per Clifford | Quantinuum | [D][5] |

On atoms, Cs hyperfine T₂ = 12.6 s in a 6,100-atom array [D][6]. Fleet-scale term: two-qubit-gate leakage, ~10⁻⁵ per Clifford on ions against ~10⁻⁴ per atom per gate on arrays.

## Manufacturing, materials & supply chain
No dedicated process; the encoding rides whatever surrounds the species (Ba⁺, Yb⁺, Ca⁺, Cs, Rb, Sr). Two control families, two supply chains: Raman gates need the optical stack — Helios runs seven-plus wavelengths across 1,228 electrodes — while chip microwave traces delete it and move the burden to trap fabrication, internalised by IonQ's SkyWater purchase [C][7]; eleQtron sells the same idea as MAGIC [C][8]. Enriched ¹³⁷Ba and ¹⁷¹Yb are the plausible chokepoint, but no dated supplier fact was found; no specific ECCN.

## Role in the stack
Requires nothing — the base encoding, the most reused node in the tree. Its "replaces" edge to omg is an extension: omg keeps these ground states and adds a metastable manifold so one species supplies qubit, ancilla and coolant [G:OMG-BLUEPRINT-2021]. It adds nothing to the derived clock, set on the QCCD path by transport — a 9.66 ms round against the measured ~55 ms full-width layer (≈18 layers/s) and a 70 µs gate. Verification: Oxford's 1.5(4)×10⁻⁷ is one qubit in a dedicated apparatus, Quantinuum's 2.5×10⁻⁵ a 98-ion fleet average — three orders apart; only the fleet number is an architectural input.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US | Helios, 98 Ba⁺ qubits | [D][5] |
| IonQ | developer | US | Electronic gates, own trap fab | [D][4][C][7] |
| University of Oxford | research | UK | ⁴³Ca⁺ single-qubit record | [D][3] |
| Atom Computing | developer | US | Yb nuclear-spin clock qubits | [C][9] |

**Money.**
2026-06-03 · Quantinuum · IPO, Nasdaq QNT, after a Sep-2025 round at $10 B pre-money · $1.68 B gross · closed [C][G:QTM-IPO-2026-06][G:QTM-600M-2025-09]
2026-07-31 · IonQ · SkyWater acquisition closed · ~$1.8 B [C][G:IONQ-SKYWATER-2026]

**Market & supply chain.** Nothing is sold as "hyperfine encoding": the money is in the drive, laser chains against microwave traps. Concentration is low in optics, rising in traps now IonQ owns a fab. Pays G3/G4/G7, the substrate under nearly every logical qubit yet demonstrated.

**IP & standards.** PatSnap Eureka (2026) ranks IonQ first among named assignees, 9+ records (5 JP, 2 EP, 2 IL pending) on gate pulses and motional modes; the count mixes patents with papers [P][10].

**Roadmaps & track record.** Quantinuum: Sol 2027, Apollo 2029 (promised 2024-09-10); Helios on schedule 2025-11-05, 10×/year quantum volume held. IonQ: 256 qubits at 99.99% slipped to H1 2027, and 4,000 qubits by 2026 (promised 2020) missed ~40×. Quantinuum delivers dates, IonQ physics.

**Strategic reading.** Universality is the point: everyone uses it, so it is neither moat nor lock-out. The contest is the drive. If all-electronic control scales past ten qubits the laser chain becomes a liability for Quantinuum and every atom vendor; if not, IonQ bought a foundry for a lab result.

*Open niche:* leakage out of the manifold is the error this encoding contributes, invisible to standard randomised benchmarking and reported in non-comparable units — per Clifford by Quantinuum, per atom per gate by the atom groups. One definition serves all four paths, and no vendor will define it against itself.

## Outlook & open questions
Confirm if all-electronic control reaches a fleet average below 10⁻⁵ with published leakage, or a second group replicates 8.4×10⁻⁵; demote if it stays a ten-qubit result. Best case 2029: microwave-driven hyperfine qubits the default. Worst case: gradient-limited leakage caps ions near 10⁻⁵ and omg takes the base.

## Sources
[1] Monroe, Meekhof, King, Itano, Wineland (NIST Boulder), "Demonstration of a fundamental quantum logic gate", Phys. Rev. Lett. 75, 4714, 1995-12-18 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.75.4714
[2] Wang et al. (Tsinghua), "Single ion qubit with estimated coherence time exceeding one hour", arXiv:2008.00251, 2020-08 — https://arxiv.org/abs/2008.00251
[3] Smith, Leu, Miyanishi, Gely, Lucas (Oxford), "Single-qubit gates with errors at the 10⁻⁷ level", arXiv:2412.04421, 2024-12-05 — https://arxiv.org/abs/2412.04421
[4] IonQ / Oxford Ionics, two-qubit electronic gate at 8.4×10⁻⁵, arXiv:2510.17286, 2025-10 — https://arxiv.org/abs/2510.17286
[5] Quantinuum, "Helios", arXiv:2511.05465, 2025-11; Nature 2026-06 — https://arxiv.org/abs/2511.05465
[6] Caltech, 6,100-atom Cs array with 12.6 s hyperfine coherence, arXiv:2403.12021 — https://arxiv.org/abs/2403.12021
[7] IonQ, completion of the SkyWater Technology acquisition, 2026-07-31 [C] — https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
[8] eleQtron, €57 M Series A (MAGIC microwave ion control), 2026-05-05 [C] — https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/
[9] Atom Computing, raise of more than $300 M including a $100 M DoC letter of intent, 2026-06-16 [C] — https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[10] PatSnap Eureka, "Trapped ion quantum computing 2026" [P] — https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/
[G] Smith, Leu, Miyanishi, Gely, Lucas (Oxford), "Single-qubit gates with errors at the 10^-7 level", arXiv:2412.04421 (2024-12-05, rev 2025-05-28): 43Ca+ hyperfine clock qubit in a mi… · 2024-12-05 · https://arxiv.org/abs/2412.04421
[G] Loschnauer, Mosca Toba, Hughes, King, Weber, Srinivas, Matt, Nourshargh, Allcock, Ballance, Matthiesen, Malinowski, Harty, "Scalable, high-fidelity all-electronic control of trappe… · 2024-07-10 · https://arxiv.org/abs/2407.07694
[G] Allcock, Campbell, Chiaverini, Chuang, Hudson, Moore, Ransford, Roman, Sage, Wineland, "omg blueprint for trapped ion quantum computing with metastable states", Applied Physics Let… · 2021 · https://cua.mit.edu/dev_site/publications/omg-blueprint-for-trapped-ion-quantum-computing-with-metastable-states
[G] Quantinuum raised $600 M at a $10 B pre-money valuation (NVentures, Quanta, QED, JPMorgan), 2025-09-04 · 2025-09-04 · https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale
[G] Quantinuum IPO priced 2026-06-03: 28,000,000 shares at $60 = $1.68 B gross, Nasdaq QNT; Q2-2026 revenue $8.0 M, cash $2.1 B, FY guidance $28–32 M · 2026-06-03 · https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering
[G] IonQ acquired SkyWater Technology: $15.00 cash + 0.4883 IonQ shares per share (~$1.8 B at announcement 2026-01-26), closed 2026-07-31 · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
## Open verification items
- The 1995 PRL abstract does not name the species or the hyperfine sublevels; the "since 1995" attribution follows the graph record and the paper's internal-state qubit, not an explicit hyperfine statement in the abstract.
- The Yb⁺ hour-scale memory source names "a single Yb ion-qubit memory" without specifying the isotope or transition in the abstract.
- Oxford's 1.5(4)×10⁻⁷ has no published multi-qubit fleet-average equivalent.
- PatSnap counts mix patents and papers and are not verified against original filings.
- No dated supplier fact found for isotopically enriched ¹³⁷Ba or ¹⁷¹Yb; the chokepoint claim is unverified.
