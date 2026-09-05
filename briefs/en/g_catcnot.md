---
id: g_catcnot
name: Bias-preserving cat–cat CNOT
layer: 3 Gate mechanism
tier: 3
status: empty slot
since: 2030
one_line: A direct entangling gate between two dissipative cat qubits that keeps the exponential bit-flip suppression intact through the interaction — theory only.
verdict: Undemonstrated as of 2026-09-04; demote every cat-code qubit-count estimate if no two-cat gate shows measured bias preservation by 2028.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An entangling gate acting directly between two dissipative cat qubits, no transmon ancilla in the middle, preserving the bit-flip/phase-flip asymmetry through the interaction. Every cat CX in hardware is cat–transmon; the cat–cat version is what cat-code resource estimates silently assume. The first coherent (unitary) scheme, a "vacuum-conditional beam-splitter", was posted 2026-07-24 by Ye et al. (AWS Center for Quantum Computing / Caltech) [S][1]. Entangling is intended deterministic, gate time unmeasured; control is room-temperature microwave, bus connectivity.

## Physics & limits
The difficulty is geometric: a cat CNOT rotates the target's coherent amplitude through π conditioned on the control, briefly leaving the stabilised two-lobe manifold; any non-adiabatic drive term then leaks population between lobes as plain bit-flips, no longer exponentially suppressed in photon number. Dissipative schemes pin the state but pay in gate-induced phase-flips. The unitary scheme drops the dissipator and claims logical memory below 10⁻⁶ from a distance-7 repetition code of 13 cats — from assumed lifetimes and nonlinearity precision, not measurement [S][1]. The floor is structural: one residual bias-breaking term turns the exponential into a polynomial and takes the qubit-count case with it [S][7].

## Engineering state of the art
No cat–cat entangling gate exists in hardware as of 2026-09-04.

| Date | Figure | Who | Tag |
|---|---|---|---|
| 2025-02 | Cat–transmon CX at n̄ = 2: bit-flip 3.5(4)×10⁻³, phase-flip 9.6(4)×10⁻² → bias > 25 under the gate, > 30 idle | AWS/Caltech (Ocelot) | [D][2] |
| 2026-07 | Unitary cat–cat CNOT proposed; <10⁻⁶ logical memory claimed, distance 7 / 13 cats | Ye et al. | [S][1] |
| 2030 | 2,000 cats → 100 logical at 10⁻⁶, requiring ≥13-min bit-flip during a CNOT | Alice & Bob | [R][3] |

The neighbour shows the budget's shape: Ocelot's 2.8 µs cycle moved logical error only from 1.75(2)% at distance 3 to 1.65(3)% at distance 5, because per-CX phase-flip is already ~10⁻¹ [D][2].

## Manufacturing, materials & supply chain
No dedicated process: the gate reuses existing cavity bodies, junction lithography and room-temperature microwave stacks. Dropping the ancilla removes one transmon and readout chain per gate pair — Ocelot spends four ancillas on five cats — but adds a parametric tone per cat: lines per qubit are re-allocated, not reduced. At 10³ cats the wall is coax density and pump crosstalk in one dilution unit; at 10⁴–10⁶ it is the generic microwave wiring wall, no cryogenic-CMOS multiplexing of cat pump tones having been demonstrated.

## Role in the stack
On the superconducting bosonic (cat/GKP) path; requires two cat-encoded qubits and provides nothing downstream until it exists. It replaces the ancilla-mediated bosonic CX, trading a non-bias-preserving transmon channel for an unproven direct interaction; not switching leaves the ancilla's bit-flips setting the code floor. It does not move the derived clock, 2.8 µs here, set by CX plus dispersive ancilla readout [D][2]. Verification: the sole evidence is a proposal — no replication, no hardware attempt, and <10⁻⁶ is a code-level projection, not a measured fidelity [S][1].

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| AWS | developer | US | Authored the unitary scheme; owns the cat CX hardware | [S][1] |
| Alice & Bob | developer | FR | 2030 rung, 2,000 cats → 100 logical, presumes it | [R][3] |
| DARPA | investor | US | Stage B funds Nord Quantique, not Alice & Bob | [G:QBI-STAGEB-2025-11] |

**Money.**
2025-01-28 · Alice & Bob · Series B · €100 M · — · closed [G:AB-SERIESB-2025-01]
2026-05-22 · Alice & Bob · Series B extension · undisclosed · NVentures lead · closed [C][4]
2026-06-17 · GENCI · buys first "Helium" · undisclosed · French HPC agency · closed [C][8]
2025-11-06 · Nord Quantique · QBI Stage B · $5 M, up to $15 M · DARPA · announced [G][5]

**Market & supply chain.** No supplier is specific to this gate; it reuses cat vendors' fabrication and pays for G3 alone.

**IP & standards.** No dated patent family specific to a bias-preserving cat–cat gate was found as of 2026-09-04.

**Roadmaps & track record.** AWS: promised 2026-07, no experimental date [S][1]. Alice & Bob: promised on the live roadmap, for 2030 — Boson 4 (2024) and Helium (2026-06) landed, but every rung past Lithium (48 cats, 4 logical, 10⁻³) presumes this gate [R][3].

**Strategic reading.** If measured, cat codes keep their qubit-count argument and surface-code transmon vendors lose; if still theory past 2028, dual-rail erasure takes the hardware-efficient slot.

*Open niche:* the missing instrument is a bias-under-gate benchmark — bit-flip suppression measured *during* a two-qubit interaction, at stated photon number and ancilla state.

## Outlook & open questions
Confirm by 2028 if a measured two-cat gate holds bit-flip time within 10× of idle; demote if 2028 passes with only ancilla-mediated gates, since the 2030 rung and the 126,133-cat class of estimates lose their premise [S][7]. Best case 2029: bias above 10³ under drive. Worst case: cat logic runs through ancillas indefinitely. Open: does the scheme survive junction-nonlinearity spread; can the gate be characterised without ancilla contamination; who attempts hardware first? Watch Ocelot follow-ups and the Lithium chip.

## Sources
[1] Ye, Hann, Noh, Putterman, Belyansky, Grimsmo, Painter · "Bias-preserving cat-cat CNOT gate via vacuum-conditional beam-splitter" · arXiv:2607.22852 · 2026-07-24, rev. 2026-08-04 — https://arxiv.org/abs/2607.22852
[2] Putterman et al. (AWS/Caltech) · "Hardware-efficient quantum error correction using concatenated bosonic qubits" (Ocelot) · Nature 638, 927–934 · 2025-02-26 — https://www.nature.com/articles/s41586-025-08642-7
[3] Alice & Bob · public roadmap (Boson 4 / Helium / Lithium / Beryllium / Graphene) · retrieved 2026-09-04 [C] — https://alice-bob.com/roadmap/
[4] Alice & Bob · "Alice & Bob announces Series B extension" · newsroom · 2026-05-22 [C] — https://alice-bob.com/newsroom/alice-bob-announces-series-b-extension/
[5] DARPA · Quantum Benchmarking Initiative, Stage B selection · 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[6] Nord Quantique · "Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment" · BusinessWire · 2026-05-18 [C] — https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment
[7] Gouzien, Ruiz, Le Régent, Guillaud, Sangouard · cat-qubit resource estimate for elliptic-curve cryptanalysis · arXiv:2302.06639 · 2023-02-13 — https://arxiv.org/abs/2302.06639
[8] Alice & Bob · "Alice & Bob unveils first quantum system" (Helium) · newsroom · 2026-06-10 [C] — https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/

## Open verification items
The <10⁻⁶ logical-memory claim in [1] rests on assumed component lifetimes and nonlinearity precision; no independent replication and no measured gate exist as of 2026-09-04.
Roadmap page [3] attaches the "13 minutes" bit-flip requirement to the Graphene chip without saying whether it is idle or under-gate; the main report reads it as under-CNOT.
No public record was found of any experimental group attempting a cat–cat entangling gate.
Nord Quantique [6] appears in the ledger but not the Who table: its multimode route does not use this gate.
