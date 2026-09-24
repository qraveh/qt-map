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
Attributes: natural trapped-ion carrier; deterministic entangling at ≈10⁻⁴·² s (≈63 µs) over a shared motional bus.
Optical control from room temperature; error coherent, leakage, Pauli; manufacturing is optical assembly.

## Physics & limits
Gate duration follows the detuning δ from the addressed sideband — one closed loop takes 2π/δ — and δ cannot be opened freely, because the beat note must stay clear of every spectator mode. In an N-ion chain the axial spectrum crowds, δ shrinks and the pulse lengthens: 1.6 µs on a pair [D][1] against a 672 µs median on one 30-ion chain [D][2], roughly 400× for 15× the ions. Two floors remain. Off-resonant Raman scattering is incoherent, no pulse shape cancels it, and it falls only as the Raman detuning is pushed past the fine-structure splitting. Laser noise and motional heating supply the rest: a 2026 perturbative model weights noise spectral density by a position-dependent sensitivity function and finds distant pairs ~10× more sensitive at ~25 kHz than neighbours, while ~1 kHz noise costs percent-level infidelity independently of position [S][3]. The residue is coherent and leakage-like, not depolarising, so averaged benchmarks understate what a code sees.

## Engineering state of the art
Best demonstrated: 99.8% at 1.6 µs on a ⁴³Ca⁺ pair, entanglement still generated at 480 ns — under one motional oscillation period (Oxford, 2018) [D][1], still the fastest published laser gate. At scale, Helios logs 7.9×10⁻⁴ error in ≈70 µs across 98 Ba⁺ in eight zones [D][4]; IonQ's single 30-ion chain, benchmarked over all 435 pairs, gives 550–883 µs, median 672 µs [D][2].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2018 | 99.8% at 1.6 µs; entanglement at 480 ns | Oxford (Schäfer et al.) | [D][1] |
| 2023-08 | 550–883 µs, median 672 µs, 30-ion chain | IonQ Forte | [D][2] |
| 2025-11 | 7.9×10⁻⁴ error in ≈70 µs, 98 ions | Quantinuum Helios | [D][4] |
| 2026-05 | Quantum volume 32,768, gate undisclosed | Alpine Quantum Technologies | [C][5] |

## Manufacturing, materials & supply chain
Nothing here is fabricated into the trap: the gate is delivered by stabilised lasers, acousto- and electro-optic modulators and beam optics, covered as its own node. Helios needs at least seven wavelengths against 1,228 trap electrodes [D][4] — the optical half is the larger bill of materials. Traps by contrast are merchant goods (Infineon, Villach); Honeywell makes Quantinuum's in-house [C][6]. Export exposure is at system level — the 2024-09-06 BIS rule created ECCN 4A906 for quantum computers above qubit-count and error-rate thresholds, but no ECCN names ion traps or beam optics [G][7].

## Control, readout & I/O burden
The two global tones do not scale with ion count; individual addressing does, at ~one modulator channel and beam path per ion. The pulse is the cheap part of the cycle: a full-width Helios layer runs ≈55 ms once sorting, transport and re-cooling are counted — three orders above the 70 µs gate — transport alone was ~60% of runtime on H2 [D][4]. At 10³ ions, power and crosstalk trade addressing quality against zone count; at 10⁴–10⁶, gate time growing with chain length makes any single-bus design trade throughput for connectivity, which is why every roadmap subdivides the trap.

## Role in the stack
Entangling mechanism for the laser-gate QCCD path (Quantinuum, Alpine Quantum Technologies) and the historical one for lines migrating to electronic control (IonQ with Oxford Ionics, eleQtron, Quantum Art). It requires a trapped-ion carrier and a laser subsystem delivering phase-stable bichromatic beams to a chosen pair, and provides the entangling layer zoned architectures assume. Its substitute is the near-field electronic gate at 8.4×10⁻⁵ [D][8]; switching writes off the optics stack but deletes photon scattering and laser noise. It conflicts with any single-bus design. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 9.7 ms, transport 9.0 ms of it, against a measured ~55 ms full-width layer [D][4]. No neighbouring empty slot is flagged.

## Verification (QCVV)
Headline numbers are benchmarking averages over a zone or chain; no vendor publishes pair-resolved error against chain position, and the ~10× neighbour-versus-distant gap remains theory [S][3]. Quantum-volume claims need the same care: AQT's 32,768 is 2¹⁵ against 2²⁵ published for Quantinuum's 56-qubit H2 [C][9] — a record inside the rack-mounted class, not at the frontier. Neither 7.9×10⁻⁴ nor 8.4×10⁻⁵ has an independent replication as of 2026-09-04.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US-UK | Helios: 98 ions, eight zones | [D][4] |
| IonQ | developer | US | Forte's 30-ion chain, 550–883 µs | [D][2] |
| Oxford Ionics (IonQ) | developer | UK | Laser-free electronic gate, the substitute | [D][8] |
| Alpine Quantum Technologies | developer | Austria | Rack-mounted LYNX, noise-desensitised variant | [C][5] |
| Leibniz Supercomputing Centre | user | Germany | 20-qubit AQT system, the only public price | [C][10] |
| DARPA | regulator | US | QBI Stage B funds both large roadmaps | [G:QBI-STAGEB-2025-11] |

**Money.**
- 2023-12-05 · Alpine Quantum Technologies · sale to Leibniz Supercomputing Centre · ≈EUR 9.8 M, 20 qubits · closed [C][10]
- 2025-09-04 · Quantinuum · equity · USD 600 M at USD 10 B pre-money · NVentures, Quanta, QED · closed [C][11]
- 2025-09-17 · IonQ · M&A, Oxford Ionics · USD 1.075 B · closed [C][12]
- 2026-06-03 · Quantinuum · IPO · USD 1.68 B gross, Nasdaq QNT · closed [C][13]

**Market & supply chain.** Optics are integrated in-house at Quantinuum and IonQ, so no outside vendor holds pricing power; the ion stack's one merchant chokepoint is trap fabrication, which this gate does not use. Q-CTRL sells pulse-optimisation tooling [C][14]. Unit economics: EUR 9.8 M for a turnkey 20-qubit rack ≈ EUR 0.5 M per qubit [C][10], the only publicly quotable trapped-ion price as of 2026-09-04. Q2-2026 revenue: USD 8.0 M at Quantinuum, USD 80.1 M at IonQ [C][13], [15]. G2 and G3 pay for it; the ≈55 ms layer routes G4 elsewhere.

**IP & standards.** PatSnap's 2026 landscape lists 9+ IonQ families filed across JP/EP/IL in 2025–2026, including "universal gate pulse for two-qubit gates" (JP, 2025), and two pending Quantum Art filings (IL, KR) on ion-array reconfiguration [P][16] — not cross-checked elsewhere. No standards body covers this gate.

**Roadmaps & track record.** Quantinuum (promised 2024-09-10 · Helios 2025, Sol 2027, Apollo 2029 · Helios on schedule 2025-11-05) [R][17] — the only met dated promise here. IonQ (promised 2025-06-13 · 256 qubits at 99.99% in 2026 · slipped to H1 2027); its 2020 roadmap missed 4,000 qubits by 2026 by ~40× [R][18] — dates are directional. AQT (promised 2026-05-05 · LYNX units Q4 2026 · unscored) [C][5].

**Strategic reading.** If laser gates hold, the vertically integrated optics teams win and no one buys an ion computer as components. If electronic gates win, IonQ with Oxford Ionics takes the cost curve and AQT and Quantum Art lose their optical differentiation. Exposure is asymmetric: Quantinuum, listed since June 2026, is the largest laser-gate incumbent, with Sol and Apollo still laser-driven — a laser-free gate at product scale is its biggest technical risk.

*Open niche:* the position-dependent noise sensitivity that decides whether averaged fidelities survive at scale is theory only; a small QCVV house could measure it — pair-resolved benchmarking against chain position under injected laser-noise spectra — and publish the first cross-vendor comparison of it.

## Outlook & open questions
Falsifiable in 12–24 months: confirm/demote that Sol ships in 2027 with laser gates; that a vendor publishes pair-resolved error against chain position; that AQT discloses LYNX gate time and fidelity at the Q4-2026 rollout. Best case by 2029: pulse engineering and zone subdivision hold laser gates at ≈10⁻⁴ with transport still the clock. Worst case: electronic gates reach product scale first and this becomes legacy. Open: does the AQT variant generalise beyond quantum-volume circuits; can scattering-limited error go below 10⁻⁴ at usable power; which binds first at 10⁴ ions, power or transport.

## Sources
[1] V. M. Schäfer *et al.*, “Fast quantum logic gates with trapped-ion qubits,” *Nature*, vol. 555, no. 7694, pp. 75–78, Feb. 2018, doi: [10.1038/nature25737](https://doi.org/10.1038/nature25737). [arXiv:1709.06952](https://arxiv.org/abs/1709.06952). [D]
[2] J.-S. Chen *et al.*, “Benchmarking a trapped-ion quantum computer with 30 qubits,” *Quantum*, vol. 8, Art. no. 1516, Nov. 2024, doi: [10.22331/q-2024-11-07-1516](https://doi.org/10.22331/q-2024-11-07-1516). [arXiv:2308.05071](https://arxiv.org/abs/2308.05071). [D]
[3] D. V. Donchenko, E. A. Anikin, O. Lakhmanskaya, and K. Lakhmanskiy, “Mølmer-Sørensen gates in trapped-ions chains in the presence of correlated noise,” [arXiv:2606.23951](https://arxiv.org/abs/2606.23951), Jun. 2026. [S]
[4] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[5] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[6] “Infineon Technologies, trapped-ion QPU platform (Villach), company page accessed 2026-09-03,” infineon.com, Sep. 4, 2026. [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[7] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[8] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[9] Quantinuum, “Quantum Volume.” [Online]. Available: https://www.quantinuum.com/glossary-item/quantum-volume [C]
[10] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[11] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [C]
[12] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[13] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[14] Q-CTRL, “Learn to Optimize Mølmer–Sørensen Gates for Trapped Ions,” Boulder Opal documentation · accessed, Sep. 4, 2026. [Online]. Available: https://docs.q-ctrl.com/boulder-opal/toolkit/apply/trapped-ion-quantum-computing/learn-to-optimize-molmer-sorensen-gates-for-trapped-ions [C]
[15] IonQ, “Second-quarter 2026 results,” newsroom, Aug. 2026. [Online]. Available: https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[16] PatSnap Eureka, “Trapped Ion Quantum Computing 2026,” patent landscape, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[17] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[18] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]

## Open verification items
The 480 ns entangling result in [1] is quoted without a fidelity in the abstract; only the 1.6 µs / 99.8% pair is a complete figure of merit. AQT's LYNX gate time and fidelity behind quantum volume 32,768 are undisclosed, so the noise-desensitisation claim cannot be checked against a physical number. No independent, non-vendor replication of Helios's 7.9×10⁻⁴ or of the IonQ/Oxford Ionics 8.4×10⁻⁵ was found as of 2026-09-04. The ~10× position-dependent sensitivity gap [3] is perturbative theory, not measurement. PatSnap's family counts were not cross-checked against a second patent database. The 550–883 µs range comes from the full text of [2]; the abstract confirms only the single 30-ion chain and the 435-pair benchmark.
