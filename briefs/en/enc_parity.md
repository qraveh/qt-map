---
id: enc_parity
name: Fermion-parity encoding (tetron)
layer: "2 Encoding"
status: theory / design only
since: 2025
one_line: One logical qubit in the fermion parity of four Majorana modes on two wires; Z and X are parities of different mode pairs, both non-local.
verdict: Not a working encoding as of 4 Sep 2026 — its X channel lives ~1000× shorter than its Z channel; falsified as fault-tolerance-relevant unless that ratio falls below 10× by 2028.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Four Majorana modes on two wires joined by a superconducting backbone hold one qubit: Z is the parity of one wire's mode pair, X of a pair spanning both, so neither logical operator is local. Karzig et al. defined the tetron and hexon layouts in 2017, with Cliffords by measurement rather than braiding [S][1]. Only Z-type parity has been read with a stated fidelity; the X measurement the encoding requires has not [D][3].
a fabricated (1.0) · b not a gate · c no readout · d no transport
e no control · f asymmetric, poisoning-dominated · g inherits the wire fab

## Physics & limits
Protection is a length and a gap: parity splitting falls exponentially with length over coherence length, poisoning as the gap rises against temperature and quasiparticle density [S][1]. Neither is published. Published instead: 12.4 ms on the Z loop against 14.5 µs on the X loop in one device [D][2]. Both are fermion parities, so the ~1000× factor is geometric: the X loop encloses both wires and captures quasiparticles over a larger cross-section [D][2]. A code needs comparable rates on both bases, and this is not usable bias: the short basis is the one a measurement-based gate projects most. Moving the floor means a larger gap (lead replaced aluminium [D][3]), quasiparticle trapping and a smaller X loop.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2017 | Tetron and hexon layouts defined; measurement-only Cliffords | Microsoft | [S][1] |
| 2025-07 | Z loop 12.4 ms vs X loop 14.5 µs, one tetron | Microsoft Quantum | [D][2] |
| 2026-06 | One wire of one tetron in an array; no joint parity | Microsoft Quantum | [D][3] |
No logical state prepared, no X measurement, no coherence time or logical error rate for a tetron [D][3].

## Manufacturing, materials & supply chain
No process of its own; the encoding fixes a geometry. Two wires, a backbone and the dots closing each loop cost more area and steps than a bare wire, and the X loop's coupling elements are exactly what a Z-only measurement avoids. Bring-up is per device: the 2026 rf technique resolves wire-end-state splitting to µeV so array devices can be tuned at all [D][3]. Below it is in-house InAs–Pb epitaxy, unreplicated outside Microsoft; no export-control category specific to it.

## Role in the stack
It requires two wires per qubit and supplies the logical degree of freedom a measurement-based gate would act on; nothing else consumes it, and it sets no clock. Verification is one-sided: telegraph statistics on parity loops, no logical error per cycle, no Λ, no independent tetron. The dispute runs deeper: Legg's Matters Arising (2026-06-24) argues the regions read out in 2025 were disordered and gapless, making the encoded object trivial rather than protected; Microsoft's same-day reply concedes nothing [D][4]. QuTech's parity qubit in coupled Kitaev chains is an alternative encoding with limited protection, not a tetron replication [D][5].

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Microsoft Quantum | developer | US | Defined the tetron and holds the only Z/X data | [D][2] |
| DARPA | investor | US | US2QC final Validation & Co-Design stage since 2025-02-06 | [G:MSFT-US2QC-PARTNERS-2025-02] |
| QuTech | research | NL | Competing parity encoding in coupled Kitaev chains | [D][5] |
| Nokia Bell Labs | research | US | Fractional-quantum-Hall anyon route, a different encoding | [D][G:NOKIA-BELLLABS-TOPO-2026] |

**Money.** 2025-02-06 · Microsoft · US2QC final Validation & Co-Design stage · undisclosed · DARPA · announced [G:MSFT-US2QC-PARTNERS-2025-02]. 2026-01-23 · Microsoft · Quantum Pioneers Program, QEC an award topic · ≤ USD 200,000 per proposal · announced [P][G:MSFT-QUPP-2026-01].

**Market & supply chain.** Nothing is sold; it consumes wires and readout and pays back only in G4, after an X measurement exists.

**IP & standards.** The tetron layout is Microsoft's published lineage [S][1]; no dated patent count specific to it as of 4 Sep 2026.

**Roadmaps & track record.** (tetron as the fault-tolerance unit, promised 2017, restated for 2029 in 2026; status 4 Sep 2026: no X measurement, no logical qubit) [C][7]. Nine years from design to a one-wire measurement, with no interim milestone for the X/Z ratio.

**Strategic reading.** Every topological claim above sits on this ratio. If it closes, Microsoft's fabrication lead becomes a code; if not, the tetron gives way to a longer Kitaev chain and the wire stack loses its justification. Risk is single-vendor and single-design.

*Open niche:* Bounding how much of the ~1000× asymmetry is geometric versus intrinsic, from published loop geometries and lifetimes, is a modelling task with no hardware dependency.

## Outlook & open questions
Falsifiable in 12–24 months: any X-basis parity measurement with a stated assignment error; an X/Z ratio below 100×; a joint measurement across two tetrons. Confirm on the first two; demote to theory if none appears by end-2027. Best case, loop redesign and a larger gap bring X into milliseconds; worst case, X-loop poisoning is intrinsic and the design is abandoned. Open: is the asymmetry geometric or intrinsic; does anyone build a tetron outside Microsoft.

## Sources
[1] Karzig et al. — "Scalable designs for quasiparticle-poisoning-protected topological quantum computation with Majorana zero modes" — Phys. Rev. B 95, 235305 (arXiv:1610.05289) — 2017 — https://arxiv.org/abs/1610.05289
[2] Aghaee et al. (Microsoft Quantum) — tetron Z-loop / X-loop parity lifetimes — arXiv:2507.08795 — 2025-07 — https://arxiv.org/abs/2507.08795
[3] Aghaee et al. (Microsoft Quantum) — "20 Second Parity Lifetime in an InAs–Pb Tetron Device" — arXiv:2606.03884 — 2026-06-02 — https://arxiv.org/abs/2606.03884
[4] Legg — "On the robustness of topological gap detection via transport" — Nature, Matters Arising — 2026-06-24 (Microsoft reply same day) — https://www.nature.com/articles/s41586-026-10567-8
[5] Zatelli, Roovers, van Loo et al. (QuTech/TU Delft) — "Majorana parity qubit in coupled minimal Kitaev chains" — arXiv:2607.09511 — 2026-07-10 — https://arxiv.org/abs/2607.09511
[6] Microsoft Azure Quantum — "Interferometric single-shot parity measurement in InAs–Al hybrid devices" — Nature 638, 651–655 — 2025-02-19 — https://www.nature.com/articles/s41586-024-08445-2
[7] Microsoft — "Majorana 2: a scalable, error-corrected quantum processor" — Azure Quantum blog [C] — 2026-06 — https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor
[8] DARPA — "Quantum computing approaches" (US2QC) — DARPA news — 2025-02-06 — https://www.darpa.mil/news/2025/quantum-computing-approaches

## Open verification items
No Majorana splitting, wire length over coherence length, or quasiparticle density is published for a tetron, so the protection claim cannot be checked numerically. The arXiv text of [2] also gives X ~4 µs and Z ~9.3 ms for other tunings against the 14.5 µs / 12.4 ms used here. Whether the X/Z asymmetry is geometric or intrinsic is unresolved, and no non-Microsoft tetron exists to test it.
