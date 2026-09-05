---
id: code_magic
name: Magic-state factory (cultivation / distillation / code switching)
layer: "7 Code"
tier: 1
status: demonstrated
since: 2025
one_line: The subsystem that manufactures non-Clifford resource states so a code with transversal Cliffords can run universal circuits.
verdict: Three routes are demonstrated on three carriers, but every headline number is a post-selected stand-alone state; no factory has yet fed a real algorithm.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A magic-state factory manufactures the non-Clifford resource states — |T⟩, |H⟩, |CCZ⟩ — that gate teleportation injects to supply the rotation a host code cannot perform transversally. Eastin–Knill forbids a transversal universal gate set on any code with distance, so universality must be bought with space-time volume, and the factory is where that purchase is made. Bravyi and Kitaev showed in 2004–05 that Cliffords plus noisy ancillas give universality, and that ancillas polarised beyond roughly 65% along a magic direction purify asymptotically [S][1]. Three families exist: distillation, code switching, and cultivation — grow and verify one state in place (Gidney, Shutty, Jones, 2024-09) [S][2].

Coordinates. **a — carrier affinity** 0.5: a code-layer construct inheriting whatever carrier hosts it. **b**: no characteristic time of its own, entangling not applicable; it runs at the host's cycle. **c — readout**: none of its own, it consumes the host's mid-circuit measurement. **d — mobility**: static, a fixed tile region. **e — control**: no modality, no placement — compiled, not wired. **f — error structure as the code sees it**: Pauli. **g — manufacturing**: none.

## Physics & limits

The factory converts fidelity into volume at a rate set by the protocol's suppression exponent. Fifteen-to-one distillation on the quantum Reed–Muller code suppresses input error cubically, so 10⁻⁹ from a 10⁻³ injected state needs two concatenated levels and the footprint that dominated the field's resource estimates. Cultivation changes the price rather than the exponent: a |T⟩ is grown in a small patch, checked fault-tolerantly, then escaped to a large one, reaching 2×10⁻⁹ under 10⁻³ uniform depolarising circuit noise and 4×10⁻¹¹ at 5×10⁻⁴, with about the gate count of a lattice-surgery CNOT of equal reliability and an order of magnitude fewer qubit-rounds than distillation [S][2].

Two quantities set the floor. The host's physical error rate fixes achievable output error; the acceptance rate fixes throughput and has no analogue in code memory. All three routes are heralded, so a factory is a yield problem: Google retained 8% of attempts [D][3], the [[6,2,2]] route discarded 14.8% [D][5], code switching succeeded 82.58% of the time [D][4]. The dangerous failure is the undetected one — a coherent logical fault entering the algorithm where no later correction helps — so required output error is roughly the inverse T-count: IBM's 10⁸-gate Starling target implies ~10⁻⁹ per state, exactly cultivation's theoretical figure. Erasure conversion, noise bias or faster cycles move the floor; a code with a transversal non-Clifford gate would delete the node.

## Engineering state of the art

Best demonstrated is Google's cultivation run: 0.9999(1) fidelity at 8% retention, 40× error reduction, including code-switching into a surface code and a purpose-built fault-tolerant protocol to bound the fidelity [D][3]. Typical at scale is nothing — as of 3 September 2026 no factory has run inside an algorithm anywhere, and every result is stand-alone and post-selected. Demonstrated (10⁻⁴) sits five orders above required (10⁻⁹), and acceptance looks harder to close than fidelity.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2005 | Purification threshold ≈65% polarisation along a magic direction | Bravyi, Kitaev | [S][1] |
| 2025-06-17 | Magic-state infidelity 7×10⁻⁵ at 14.8% discard; logical controlled-Hadamard ≤2.3×10⁻⁴, [[6,2,2]] on 8 qubits | Quantinuum | [D][5] |
| 2025-07-14 | First logical-level 5-to-1 distillation, d=3 and d=5 colour codes, neutral atoms | QuEra, Harvard, MIT | [D][7] |
| 2025-10-15 | Code switching [[15,1,3]]→[[7,1,3]]: ≤5.1(2.7)×10⁻⁴ at 82.58% success | Quantinuum | [D][4] |
| 2025-12-15 | Cultivation on a superconducting processor: 0.9999(1), 8% acceptance, 40× | Google Quantum AI | [D][3] |

The dominant budget term is the escape step, where the state enters a large patch and loses post-selection; below it sit host two-qubit errors, mean 1.2×10⁻³ on the leading transmon system [C][17].

## Manufacturing, materials & supply chain

Nothing is fabricated: the bill of materials is host-code patches, mid-circuit measurement and classical compute, and the unit of cost is qubit-rounds. An attempt escaping to distance 15 implies a working region of order 10³ physical qubits per concurrent attempt, against a teraquop memory footprint of 650 physical per logical at 0.1% noise [S][13] — a handful of logical qubits per factory, not the hundreds implied by two-level distillation. The supply chain is classical: real-time decoders (Riverlane, NVIDIA, Zurich Instruments), the accept/reject interconnect, and the tooling that certifies output; the verification stack is the single point of failure. Export-control exposure is inherited — controls attach to the host machine under the 2024 US quantum-computer rules, not to a code.

## Control, readout & I/O burden

The factory adds no wires and one hard latency requirement: each attempt ends in an accept/reject verdict that must reach the scheduler before the state decays, so it rides the memory's real-time decode path and competes for its bandwidth. On a 1.1 µs superconducting cycle [D][16] a distance-15 escape is about 17 µs per attempt, and at 8% acceptance the attempt rate must be ~12× consumption. On QCCD ion and neutral-atom hosts the cycle is 1–5 ms, the same attempt costs 15–75 ms, and throughput binds rather than fidelity. Measured decode latency is 63 µs at d=5 [D][16], above the per-attempt budget; Riverlane's sub-microsecond-per-round FPGA decoder [D][11] and NVQLink's 3.84 µs mean round trip [P][15] are what make pipelining possible. The wall: at 10³ qubits factory and algorithm do not coexist; at 10⁴ one or two fit; at 10⁶ the problem is scheduling tens of factories, each with its own decoder stream.

## Role in the stack

It sits on the superconducting transmon path (Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu), the QCCD trapped-ion path (Quantinuum, AQT) and the alkali neutral-atom path (Harvard/MIT, QuEra, Pasqal, Infleqtion, Google's 2026 atom track). It requires a host — the rotated surface code with its yoked variants, or the colour code — and provides the non-Clifford axis without which a stabiliser machine is classically simulable. Cultivation replaces multi-level distillation; the switching price is architectural, since cultivation is surface-code-native and post-selection-heavy while code switching needs a colour code. Hub reading: one primitive reaching all three leading carriers with no off-diagonal substitute, so its value lies entirely in what it unlocks. It does not set the derived clock but multiplies it — derived clock = max(gate, readout, transport) for the path, so 1.1 µs superconducting and 1.0–5.0 ms for QCCD ions, times escape depth and inverse acceptance. Empty neighbouring slots: no factory on bosonic, photonic or spin platforms, none on a qLDPC code.

## Verification (QCVV)

Every headline number is a post-selected stand-alone fidelity, measured on a state then discarded rather than used. Google reports a bound from a purpose-built fault-tolerant measurement protocol, not a tomographic estimate [D][3]; the 7×10⁻⁵ figure is quoted at a stated discard rate [D][5]; code switching's 5.1(2.7)×10⁻⁴ carries an uncertainty of the same order as the value [D][4]; the neutral-atom paper reports improvement over input rather than an absolute output infidelity [D][7]. Unmeasured everywhere: throughput under scheduling load, the cost of discards, factory-to-consumer correlations, and the loss channels post-selection removes. Independent checking is unusually strong — Wan, Zhong and Zapirain decompose d=5 cultivation circuits into about 8 Clifford ZX terms on average, over 10⁶× fewer than prior stabiliser decompositions [D][12]. No value conflicts were found among the sources used.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | Invented cultivation; first superconducting demonstration | [S][2] [D][3] |
| Quantinuum | developer | US/UK | Code switching and the [[6,2,2]] logical non-Clifford gate | [D][4][5] |
| QuEra Computing | developer | US | First logical-level 5-to-1 distillation on colour codes | [D][7] |
| Harvard University | research | US | 448-atom universal fault-tolerance architecture | [D][8] |
| IBM | developer | US | Starling budgets 10⁸ logical gates; nothing shown on IBM hardware | [R][9] |
| NVIDIA | supplier | US | NVQLink, the accept/reject path a pipelined factory needs | [P][15] |
| Riverlane | supplier | UK | Sub-microsecond decoding, the throughput gate on cultivation | [D][11] |
| DARPA | regulator | US | QBI Stage B funds IBM, Quantinuum, QuEra and eight others | [G:QBI-STAGEB-2025-11] |

**Money.**
- 2025-09-04 · Quantinuum · capital raise · $600 M at $10 B pre-money · NVentures, Quanta, QED, JPMorgan · closed [G:QTM-600M-2025-09]
- 2025-09-09 · QuEra · financing round · $230 M+ · Google, SoftBank Vision Fund 2, NVentures · closed [G:QUERA-230M-2025]
- 2025-11-06 · DARPA · QBI Stage B · up to $15 M each · eleven teams · announced [G:QBI-STAGEB-2025-11]
- 2026-06-03 · Quantinuum · IPO · $1.68 B gross, Nasdaq QNT; FY guidance $28–32 M · closed [G:QTM-IPO-2026-06]
- 2026-06 · IBM · corporate commitment · $10 B, US quantum manufacturing and R&D · announced [C][9]

**Market & supply chain.** Nobody sells a magic-state factory; it is bundled into a machine and given away in a compiler. The sellable adjacencies are real-time decoding and interconnect, resource estimation, and the host hardware. Concentration is extreme: Google, Quantinuum, and QuEra with Harvard and MIT hold every demonstrated result, and two of the three routes trace to one theory group. G3 and G4 pay for this directly, G6 indirectly; G1, G2 and G5 pay nothing, which is why a primitive on every fault-tolerance critical path carries almost no dedicated revenue.

**IP & standards.** No dated patent-family count specific to magic-state factories was found from a named database as of 3 September 2026; PatSnap's quantum totals to 2026-06-30 (IBM 4,388, Google 2,385, Microsoft 1,175 families) do not resolve to this node [P][G:PATSNAP-2026-06]. There is no interface standard; the de-facto portability layer is the Quantum Intermediate Representation used in the 2023 real-time demonstration [C][6], the verification layer open-source stabiliser and ZX simulation [D][12]. No litigation on record.

**Roadmaps & track record.** Google (2024-09-26, "as cheap as a CNOT"): demonstrated 2025-12-15 at 0.9999, fifteen months theory to silicon, still five orders above target. Quantinuum (2024-09-10, universal fault tolerance by 2029): two demonstrations, both on the 20-qubit H1-1, none yet on Helios. QuEra (2024-01, 100 logical qubits in 2026): distillation shown 2025-07, count not met, restated as Libra in 2028. IBM (2025-06-10, Starling 2029): no factory result, Kookaburra slipped a year. Credibility: Google highest, with theory, hardware and verification tooling in one place; Quantinuum high on primitives, unproven at scale; QuEra high on primitives, slipped roadmap; IBM unevidenced here.

**Strategic reading.** If cultivation holds at scale, the winner is whoever has the fastest cycle and the best sub-microsecond decoder — favouring superconducting over ions and atoms by two to three orders of magnitude in throughput; the loser is the distillation-dominated resource estimate that made fault tolerance look ten times dearer than it now appears, and any security timeline resting on it. Substitution threats are real but undemonstrated: transversal non-Clifford codes, algorithmic fault tolerance, Clifford-heavy redesign. Bargaining power sits with the platform vendor, since the factory is a compiler asset; the only supplier leverage is the accept/reject path.

*Open niche:* the measurement gap here is exactly a QCVV gap. Nobody reports an in-algorithm magic-state error rate, an acceptance rate under scheduling load, or factory-to-consumer correlations — a small company could define the factory-audit protocol Stage C verification will need, using public hardware access only. The SFQ angle is nearer: the accept/reject verdict is a small, latency-critical cold-stage decision, far smaller than a decoder, and millikelvin SFQ logic has now driven qubits above 99% single-qubit fidelity [P][14].

## Outlook & open questions

Confirm, within 12–24 months, if a cultivated state is consumed by a logical algorithm rather than measured in isolation, with end-to-end error below 10⁻⁶ by end-2027; if cultivation reaches a discard rate below 50%, against 92% today; if any magic-state result appears on IBM hardware before Starling, or any factory runs on a qLDPC code. Demote if Google's next processor cannot push cultivation below 10⁻⁵ while raising acceptance, or if the fidelity bound fails to survive consumption. Best case by 2029: in-line cultivation near 10⁻⁹ and factories a minority of the footprint, so T-count-limited algorithms become clock-limited. Worst case: acceptance stays near 10%, throughput binds, distillation returns as a second stage and the 10³-physical-per-logical estimates with it. Open questions: does the bound survive use rather than measurement; what does post-selection cost under real scheduling; can code switching be made deterministic; is a qLDPC-native factory possible; does erasure conversion raise this threshold as it raises the memory's. Watch Google's next cultivation paper, the first Helios magic-state numbers, IBM Kookaburra and QuEra Libra.

## Sources

[1] Bravyi, Kitaev — Universal quantum computation with ideal Clifford gates and noisy ancillas — Phys. Rev. A 71, 022316 — 2005 — https://arxiv.org/abs/quant-ph/0403025
[2] Gidney, Shutty, Jones — Magic state cultivation: growing T states as cheap as CNOT gates — arXiv — 2024-09-26 — https://arxiv.org/abs/2409.17595
[3] Rosenfeld, Gidney et al. (Google Quantum AI) — Magic state cultivation on a superconducting quantum processor — arXiv — 2025-12-15 — https://arxiv.org/abs/2512.13908
[4] Daguerre, Blume-Kohout, Brown, Hayes, Kim (Quantinuum) — High-fidelity logical magic states from code switching — Phys. Rev. X 15, 041008 — 2025-10-15 — https://arxiv.org/abs/2506.14169
[5] Dasu, Burton, Mayer et al. (Quantinuum) — Breaking even with magic: a high-fidelity logical non-Clifford gate — arXiv — 2025-06-17 — https://arxiv.org/abs/2506.14688
[6] Quantinuum with Microsoft Azure Quantum — Programming tools for real-time magic state distillation [C] — blog — 2023-10-24 — https://www.quantinuum.com/blog/a-quantinuum-led-team-has-built-the-quantum-programming-tools-for-real-time-magic-state-distillation-on-a-quantum-computer
[7] Cantú et al. (QuEra, Harvard, MIT) — Experimental demonstration of logical magic state distillation — Nature 645, 620–625 — 2025-07-14 — https://www.nature.com/articles/s41586-025-09367-3
[8] Bluvstein, Geim, Li et al. — Architectural mechanisms of a universal fault-tolerant quantum computer — arXiv — 2025-06-25 — https://arxiv.org/abs/2506.20661
[9] IBM — Starling 2029 / Blue Jay 2033 roadmap — newsroom — 2025-06-10 — https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center ; $10 B commitment FAQ [C] — 2026-06 — https://www.ibm.com/quantum/blog/10-billion-investment-faq
[10] Beverland et al. (Microsoft) — Assessing requirements to scale to practical quantum advantage — arXiv — 2022-11-14 — https://arxiv.org/abs/2211.07629
[11] Riverlane — Real-time FPGA surface-code decoder — Nature Communications — 2025 — https://www.nature.com/articles/s41467-025-66773-x
[12] Wan, Zhong, Zapirain — Simulating magic state cultivation with few Clifford terms — Quantum 10, 2134 — 2026-06-12 — https://quantum-journal.org/papers/q-2026-06-12-2134/
[13] Gidney, Jones (Google) — Teraquop surface-code footprint, 650 physical per logical at 0.1% noise — arXiv — 2023-12-14 — https://arxiv.org/abs/2312.08813
[14] SEEQC — Millikelvin SFQ qubit control logic, Nature Electronics [P] — Quantum Computing Report — 2026-03 — https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/
[15] NVIDIA — NVQLink architecture, 3.84 µs mean round trip [P] — developer blog — 2025-11 — https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
[16] Google Quantum AI — Quantum error correction below the surface code threshold — Nature — 2024-12 — https://www.nature.com/articles/s41586-024-08449-y
[17] Google Quantum AI — Willow fidelities, mean two-qubit 99.88% [C] — blog — 2025-10 — https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/

## Open verification items

- Google cultivation [3]: escape-stage code distance, physical-qubit count and cycle count are not in the abstract; only fidelity, acceptance and the 40× reduction verified.
- QuEra/Harvard/MIT distillation [7]: absolute output infidelity, atom count and acceptance rate not in the abstract — only improvement over input verified.
- Litinski's 15-to-1 factory footprints (arXiv:1808.02892) could not be extracted; the footprint comparison rests on [2] and [13].
- The distance-15 escape region of order 10³ qubits and ~17 µs per attempt are derived from [2] and [16], not quoted by a source.
- The ECCN for quantum computers under the 2024 US rule is not confirmed here from a primary source; no dated patent-family count specific to this node was found.
