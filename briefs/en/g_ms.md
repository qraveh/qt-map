---
id: g_ms
name: Mølmer–Sørensen / light-shift laser gate
layer: "3 Gate mechanism"
status: demonstrated
since: 2003
one_line: Bichromatic-laser spin-dependent force that entangles trapped ions through a geometric phase on a shared motional mode, leaving no population in it.
verdict: Still the entangling mechanism under every deployed laser-gate ion system, but gate time scales with chain length (1.6 µs on a pair, 672 µs median on 30 ions) and its floor is laser noise plus photon scattering — the two terms electronic gates delete.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Two laser tones detuned symmetrically about a motional sideband drive a spin-dependent force; the pair traces a closed loop in the phase space of a shared vibrational mode and acquires a geometric phase set by the enclosed area, so the spins entangle and the motion returns to its start. The phase depends on loop area, not mode occupation, so a hot bus is tolerated — why this, not Cirac–Zoller, became the production mechanism. Mølmer and Sørensen proposed it in 1999–2000; the light-shift variant, one field detuned against the differential Stark shift, shares the error budget and dates the deployed line to about 2003.
Coordinates: natural trapped-ion carrier; deterministic entangling at ≈10⁻⁴·² s (≈63 µs) over a shared motional bus.
Optical control from room temperature; error coherent, leakage, Pauli; manufacturing is optical assembly.

## Physics & limits
Gate duration follows the detuning δ from the addressed sideband — one closed loop takes 2π/δ — and δ cannot be opened freely, because the beat note must stay clear of every spectator mode. In an N-ion chain the axial spectrum crowds, δ shrinks and the pulse lengthens: 1.6 µs on a pair [D][3] against a 672 µs median on one 30-ion chain [D][2], roughly 400× for 15× the ions. Two floors remain. Off-resonant Raman scattering is incoherent, no pulse shape cancels it, and it falls only as the Raman detuning is pushed past the fine-structure splitting. Laser noise and motional heating supply the rest: a 2026 perturbative model weights noise spectral density by a position-dependent sensitivity function and finds distant pairs ~10× more sensitive at ~25 kHz than neighbours, while ~1 kHz noise costs percent-level infidelity independently of position [S][6]. The residue is coherent and leakage-like, not depolarising, so averaged benchmarks understate what a code sees.

## Engineering state of the art
Best demonstrated: 99.8% at 1.6 µs on a ⁴³Ca⁺ pair, entanglement still generated at 480 ns — under one motional oscillation period (Oxford, 2018) [D][3], still the fastest published laser gate. At scale, Helios logs 7.9×10⁻⁴ error in ≈70 µs across 98 Ba⁺ in eight zones [D][1]; IonQ's single 30-ion chain, benchmarked over all 435 pairs, gives 550–883 µs, median 672 µs [D][2].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018 | 99.8% at 1.6 µs; entanglement at 480 ns | Oxford (Schäfer et al.) | [D][3] |
| 2023-08 | 550–883 µs, median 672 µs, 30-ion chain | IonQ Forte | [D][2] |
| 2025-11 | 7.9×10⁻⁴ error in ≈70 µs, 98 ions | Quantinuum Helios | [D][1] |
| 2026-05 | Quantum volume 32,768, gate undisclosed | Alpine Quantum Technologies | [C][7] |

## Manufacturing, materials & supply chain
Nothing here is fabricated into the trap: the gate is delivered by stabilised lasers, acousto- and electro-optic modulators and beam optics, covered as its own node. Helios needs at least seven wavelengths against 1,228 trap electrodes [D][1] — the optical half is the larger bill of materials. Traps by contrast are merchant goods (Infineon, Villach); Honeywell makes Quantinuum's in-house [C][20]. Export exposure is at system level — the 2024-09-06 BIS rule created ECCN 4A906 for quantum computers above qubit-count and error-rate thresholds, but no ECCN names ion traps or beam optics [G][19].

## Control, readout & I/O burden
The two global tones do not scale with ion count; individual addressing does, at ~one modulator channel and beam path per ion. The pulse is the cheap part of the cycle: a full-width Helios layer runs ≈55 ms once sorting, transport and re-cooling are counted — three orders above the 70 µs gate — transport alone was ~60% of runtime on H2 [D][1]. At 10³ ions, power and crosstalk trade addressing quality against zone count; at 10⁴–10⁶, gate time growing with chain length makes any single-bus design trade throughput for connectivity, which is why every roadmap subdivides the trap.

## Role in the stack
Entangling mechanism for the laser-gate QCCD path (Quantinuum, Alpine Quantum Technologies) and the historical one for lines migrating to electronic control (IonQ with Oxford Ionics, eleQtron, Quantum Art). It requires a trapped-ion carrier and a laser subsystem delivering phase-stable bichromatic beams to a chosen pair, and provides the entangling layer zoned architectures assume. Its substitute is the near-field electronic gate at 8.4×10⁻⁵ [D][5]; switching writes off the optics stack but deletes photon scattering and laser noise. It conflicts with any single-bus design. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 9.7 ms, transport 9.0 ms of it, against a measured ~55 ms full-width layer [D][1]. No neighbouring empty slot is flagged.

## Verification (QCVV)
Headline numbers are benchmarking averages over a zone or chain; no vendor publishes pair-resolved error against chain position, and the ~10× neighbour-versus-distant gap remains theory [S][6]. Quantum-volume claims need the same care: AQT's 32,768 is 2¹⁵ against 2²⁵ published for Quantinuum's 56-qubit H2 [C][18] — a record inside the rack-mounted class, not at the frontier. Neither 7.9×10⁻⁴ nor 8.4×10⁻⁵ has an independent replication as of 2026-09-04.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US-UK | Helios: 98 ions, eight zones | [D][1] |
| IonQ | developer | US | Forte's 30-ion chain, 550–883 µs | [D][2] |
| Oxford Ionics (IonQ) | developer | UK | Laser-free electronic gate, the substitute | [D][5] |
| Alpine Quantum Technologies | developer | Austria | Rack-mounted LYNX, noise-desensitised variant | [C][7] |
| Leibniz Supercomputing Centre | user | Germany | 20-qubit AQT system, the only public price | [C][8] |
| DARPA | regulator | US | QBI Stage B funds both large roadmaps | [G:QBI-STAGEB-2025-11] |

**Money.**
- 2023-12-05 · Alpine Quantum Technologies · sale to Leibniz Supercomputing Centre · ≈EUR 9.8 M, 20 qubits · closed [C][8]
- 2025-09-04 · Quantinuum · equity · USD 600 M at USD 10 B pre-money · NVentures, Quanta, QED · closed [C][10]
- 2025-09-17 · IonQ · M&A, Oxford Ionics · USD 1.075 B · closed [C][12]
- 2026-06-03 · Quantinuum · IPO · USD 1.68 B gross, Nasdaq QNT · closed [C][9]

**Market & supply chain.** Optics are integrated in-house at Quantinuum and IonQ, so no outside vendor holds pricing power; the ion stack's one merchant chokepoint is trap fabrication, which this gate does not use. Q-CTRL sells pulse-optimisation tooling [C][21]. Unit economics: EUR 9.8 M for a turnkey 20-qubit rack ≈ EUR 0.5 M per qubit [C][8], the only publicly quotable trapped-ion price as of 2026-09-04. Q2-2026 revenue: USD 8.0 M at Quantinuum, USD 80.1 M at IonQ [C][9][11]. G2 and G3 pay for it; the ≈55 ms layer routes G4 elsewhere.

**IP & standards.** PatSnap's 2026 landscape lists 9+ IonQ families filed across JP/EP/IL in 2025–2026, including "universal gate pulse for two-qubit gates" (JP, 2025), and two pending Quantum Art filings (IL, KR) on ion-array reconfiguration [P][14] — not cross-checked elsewhere. No standards body covers this gate.

**Roadmaps & track record.** Quantinuum (promised 2024-09-10 · Helios 2025, Sol 2027, Apollo 2029 · Helios on schedule 2025-11-05) [R][16] — the only met dated promise here. IonQ (promised 2025-06-13 · 256 qubits at 99.99% in 2026 · slipped to H1 2027); its 2020 roadmap missed 4,000 qubits by 2026 by ~40× [R][17] — dates are directional. AQT (promised 2026-05-05 · LYNX units Q4 2026 · unscored) [C][7].

**Strategic reading.** If laser gates hold, the vertically integrated optics teams win and no one buys an ion computer as components. If electronic gates win, IonQ with Oxford Ionics takes the cost curve and AQT and Quantum Art lose their optical differentiation. Exposure is asymmetric: Quantinuum, listed since June 2026, is the largest laser-gate incumbent, with Sol and Apollo still laser-driven — a laser-free gate at product scale is its biggest technical risk.

*Open niche:* the position-dependent noise sensitivity that decides whether averaged fidelities survive at scale is theory only; a small QCVV house could measure it — pair-resolved benchmarking against chain position under injected laser-noise spectra — and publish the first cross-vendor comparison of it.

## Outlook & open questions
Falsifiable in 12–24 months: confirm/demote that Sol ships in 2027 with laser gates; that a vendor publishes pair-resolved error against chain position; that AQT discloses LYNX gate time and fidelity at the Q4-2026 rollout. Best case by 2029: pulse engineering and zone subdivision hold laser gates at ≈10⁻⁴ with transport still the clock. Worst case: electronic gates reach product scale first and this becomes legacy. Open: does the AQT variant generalise beyond quantum-volume circuits; can scattering-limited error go below 10⁻⁴ at usable power; which binds first at 10⁴ ions, power or transport.

## Sources
[1] Quantinuum, "Helios" 98-qubit trapped-ion processor · arXiv:2511.05465 · 2025-11 · https://arxiv.org/abs/2511.05465 — [D]
[2] Chen, Nielsen, Ebert, Inlek, Wright, Chaplin, Maksymov, Páez, Poudel, Maunz, Gamble (IonQ), "Benchmarking a trapped-ion quantum computer with 30 qubits" · arXiv:2308.05071 · 2023-08-09, rev. 2024-11-02 · https://arxiv.org/abs/2308.05071 — [D]
[3] Schäfer, Ballance, Thirumalai, Stephenson, Ballance, Steane, Lucas (Oxford), "Fast quantum logic gates with trapped-ion qubits" · Nature 555 / arXiv:1709.06952 · 2018 · https://arxiv.org/abs/1709.06952 — [D]
[4] IonQ, "Forte" quantum systems page · product page · accessed 2026-09-04 · https://www.ionq.com/quantum-systems/forte — [C]
[5] IonQ / Oxford Ionics, laser-free electronic two-qubit gate at 8.4×10⁻⁵ · arXiv:2510.17286 · 2025-10 · https://arxiv.org/abs/2510.17286 — [D]
[6] Donchenko, Anikin, Lakhmanskaya, Lakhmanskiy (Russian Quantum Center / MEPhI), "Mølmer-Sørensen gates in trapped-ions chains in the presence of correlated noise" · arXiv:2606.23951, perturbative theory · 2026-06-22 · https://arxiv.org/abs/2606.23951 — [S]
[7] Alpine Quantum Technologies, "LYNX Sets a Quantum Volume Record" · company newsroom · 2026-05-05 · https://www.aqt.eu/lynx-quantum-volume-record/ — [C]
[8] Alpine Quantum Technologies, "AQT lands million-euro contract" — 20-qubit system for the Leibniz Supercomputing Centre, ≈EUR 9.8 M · company newsroom · 2023-12-05 · https://www.aqt.eu/aqt-lands-million-euro-contract/ — [C]
[9] Quantinuum, "Quantinuum Announces Pricing of Upsized Initial Public Offering" (with Q2-2026 results) · press release · 2026-06-03 · https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering — [C]
[10] Honeywell, "Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation" · press release · 2025-09-04 · https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale — [C]
[11] IonQ, "IonQ Announces Record Second Quarter 2026 Revenues" · press release · 2026-08 · https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy — [C]
[12] IonQ, "IonQ Completes Acquisition of Oxford Ionics" · press release · 2025-09-17 · https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum — [C]
[13] Quantum Computing Report, "Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture" · trade press · 2026-04-27 · https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ — [P]
[14] PatSnap Eureka, "Trapped Ion Quantum Computing 2026" · patent-database landscape · 2026 · https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ — [P]
[15] DARPA, "Quantum Benchmarking Initiative — Stage B Selection" · programme page · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection — [G]
[16] Quantinuum, "Quantinuum Unveils Accelerated Roadmap to Achieve Universal Fault-Tolerant Quantum Computing by 2030" · press release · 2024-09-10 · https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 — [R]
[17] IonQ, "IonQ's Accelerated Roadmap: Turning Quantum Ambition Into Reality" · company blog · 2025-06-13 · https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality — [R]
[18] Quantinuum, "Quantum Volume" glossary entry — H2, 56 qubits, QV 2²⁵ · company reference page · accessed 2026-09-04 · https://www.quantinuum.com/glossary-item/quantum-volume — [C]
[19] US Bureau of Industry and Security, "Implementation of Additional Export Controls: Certain Advanced Computing Items; Quantum Computing Items" · Federal Register interim final rule · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and — [G]
[20] Infineon Technologies, trapped-ion QPU platform, Villach, 6–12-inch traps · product page · accessed 2026-09-04 · https://www.infineon.com/promo/trapped-ions — [C]
[21] Q-CTRL, "Learn to Optimize Mølmer–Sørensen Gates for Trapped Ions" · Boulder Opal documentation · accessed 2026-09-04 · https://docs.q-ctrl.com/boulder-opal/toolkit/apply/trapped-ion-quantum-computing/learn-to-optimize-molmer-sorensen-gates-for-trapped-ions — [C]

## Open verification items
The 480 ns entangling result in [3] is quoted without a fidelity in the abstract; only the 1.6 µs / 99.8% pair is a complete figure of merit. AQT's LYNX gate time and fidelity behind quantum volume 32,768 are undisclosed, so the noise-desensitisation claim cannot be checked against a physical number. No independent, non-vendor replication of Helios's 7.9×10⁻⁴ or of the IonQ/Oxford Ionics 8.4×10⁻⁵ was found as of 2026-09-04. The ~10× position-dependent sensitivity gap [6] is perturbative theory, not measurement. PatSnap's family counts were not cross-checked against a second patent database. The 550–883 µs range comes from the full text of [2]; the abstract confirms only the single 30-ion chain and the 435-pair benchmark.
