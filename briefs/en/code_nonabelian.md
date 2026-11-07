---
id: code_nonabelian
name: Non-Abelian topological order (quantum double models): anyon braiding and fusion
layer: "7 Code"
status: emerging
since: 2023
one_line: Information stored in the fusion space of non-Abelian anyons prepared on ordinary qubits, with gates by braiding and by fusion or charge measurement; made on ions and transmons, corrected nowhere.
verdict: Four groups have prepared and moved non-Abelian anyons on hardware, but no run suppresses a logical error or runs a decoder; it stays a code-layer experiment, not an error-correcting code, until a lattice larger than 3 × 3 shows a logical lifetime.
updated: 2026-11-07
---

TO = topological order; D(G) = the quantum double model of a finite group G (D₄ of order 8, S₃ of order 6); QCCD = the ion-transport architecture; G1–G7 = the report's goal classes.

## Identity & lineage

The toric code is the quantum double of the group Z₂: its excitations are Abelian anyons, and moving one around another multiplies the wavefunction by a phase, nothing more. Replace Z₂ by a non-Abelian group and the excitations carry a fusion space — a degenerate manifold that braiding rotates with a matrix rather than a phase. The idea is Kitaev's of 2003; what is new is that the states are prepared on ordinary qubits by circuits, with mid-circuit measurement and feed-forward or by a deep unitary, instead of being sought in a material. Google braided Ising anyons as graph vertices on a planar superconducting lattice and entangled three logical qubits by braiding alone (Nature 618, 264, 2023) [D][901]. Quantinuum and Harvard prepared the ground state of D₄ order on a 27-qubit kagome lattice of the H2 processor at a per-site fidelity above 98.4%, detected a non-Abelian braiding process by anyon interferometry and reached all 22 ground states of the torus by moving anyons (Nature 626, 505, 2024) [D][902]. Zhejiang and Tsinghua realised Fibonacci string-net states on a superconducting processor and braided two pairs of Fibonacci anyons (Nature Physics 20, 1469, 2024) [D][903]; IBM condensed the Fibonacci string-net dynamically and read the golden ratio from a braid at 98% average accuracy under error mitigation (Nature Communications 16, 6225, 2025) [D][904]; Quantinuum added a Z₃ qutrit toric code on 24 qutrits with parafermion defects (Nature Communications 16, 6301, 2025) [D][905]. The 2026 result that makes this a code-layer technology rather than a physics demonstration is S₃ order on 54 qubits of H2: logical qutrits in the fusion space of non-Abelian fluxes, an entangling braiding gate, read-out by charge measurement and a topologically prepared magic state — a universal gate set (Nature 655, 591, 2026) [D][906].

Attributes (technology graph): carrier affinity 0.5 — a code layer, run on ions and on transmons. Characteristic time: none of its own; entangling neither deterministic nor heralded here. Readout: none of its own — it consumes mid-circuit measurement with feed-forward for the adaptive preparation and for the charge measurements. Mobility: static nearest-neighbour wiring suffices for a planar patch (Google); the torus experiments used the all-to-all of ion transport. Control modality: none. Error structure as the code sees it: Pauli. Manufacturing: none.

## Physics & limits

A quantum double D(G) assigns a group element to every edge of a lattice and enforces two kinds of local constraint — flux through a face, charge at a vertex — whose violations are the anyons. For a non-Abelian G the flux anyons come in conjugacy classes with internal states, and two fluxes can fuse into several outcomes: that multiplicity is the fusion space in which the logical information lives, invisible to any local operator. Braiding permutes and rotates it. The limit is in the group: for the smallest non-Abelian orders the braid group's image is finite, so, in the authors' words, "their braiding operations do not provide a universal set of quantum gates" [D][906]. The S₃ work closes the gap by treating fusion as a computational primitive — three primitives, "pull-through gate, Z-basis measurement, and X-basis measurement", constitute a universal gate set on the logical qutrits — and by preparing a magic state heralded on a fusion outcome [D][906].

What the physics does not yet give is protection. A topological state on a 3 × 3 torus has a code distance of three; nobody has measured a logical error rate on it, extracted a syndrome round or run a decoder, so there is no threshold and no Λ. Errors on the physical qubits create anyon pairs; a stray anyon that braids with the logical ones is a logical error, and nothing in the present experiments detects it except post-selection: on H2 about 24% of the shots were discarded on the 3 × 3 lattice and about 13% on the 3 × 2 lattice, the adaptive preparation reaching a per-qudit bound between 0.930(8) and 0.978(2) against 0.970(5)–0.988(3) for the unitary one [D][906]. The worst failure mode is the same as for every code on these carriers — leakage and loss, which no anyon picture sees — and the cost specific to this family is depth: a non-Abelian state needs either measurement and feed-forward per site or a circuit whose depth grows with the lattice, and the 56-qubit budget of H2 bounded the lattice at 3 × 3.

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: S₃ order on 54 trapped-ion qubits with a universal logical gate set on qutrits — the pull-through braiding gate's non-local correlator rises to 0.86(3) against a theoretical 1, the X-basis vertex projector reads 0.84(4) for the logical zero against 0.06(3) for the logical one, and the Z-basis fusion measurement reads 0.32(4) against an expected 1/4 at the first site and 0.92(2) for vacuum annihilation at the second [D][906]. Typical at scale: nothing — the largest lattice is a 3 × 3 torus, and no superconducting run reports a per-site fidelity.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2023-05 | Ising anyons created and braided as graph vertices on a planar lattice; fusion rules verified; three logical qubits entangled by braiding | Google Quantum AI | [D][901] |
| 2024-02 | D₄ order on 27 qubits (kagome), per-site fidelity above 98.4%; non-Abelian braiding detected by interferometry; the 22 ground states of the torus | Quantinuum / Harvard | [D][902] |
| 2024-07 | Fibonacci string-net states; topological entanglement entropy; fusion rule and braiding of two anyon pairs | Zhejiang / Tsinghua | [D][903] |
| 2025 | Fibonacci string-net condensation; anyon charge certified at 94% average accuracy, braiding returns the golden ratio at 98% (error-mitigated) | IBM | [D][904] |
| 2025 | Z₃ toric code on 24 qutrits, 96.5(3)% per qutrit; parafermion defects fused | Quantinuum | [D][905] |
| 2026-07 | S₃ order on 54 qubits; per-qudit fidelity 0.970(5)–0.988(3) on 18 sites; logical qutrits; braiding gate; charge-measurement read-out; heralded magic state | Quantinuum / Harvard | [D][906] |

Dominant error term: not reported as a logical rate anywhere; the discarded-shot fraction and the gap between the correlator and unity are the only published measures of imperfection [D][906].

## Manufacturing, materials & supply chain

The technology has no fabrication of its own and places no new demand on the chip or the trap: every demonstration ran on a machine built for other codes — H2 for the ion results, planar transmon lattices for Google, Zhejiang and IBM. What it does demand is the ability to measure some qubits mid-circuit and act on the outcome within the coherence time of the rest (the adaptive preparation), or the depth budget for a unitary preparation; both are the properties of the host, listed under its readout and control technologies. Concentration risk is therefore the host's: the torus experiments exist on one vendor's processors, and the planar results on three organisations' superconducting lattices. Export-control exposure is the hardware's, not the mathematics' [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

The adaptive preparation of a non-Abelian state measures a subset of the sites and feeds the outcomes forward as corrections before the next layer; the S₃ paper notes the construction "admits a constant-depth adaptive preparation" while the reported ground state used a fully unitary circuit [D][906]. The charge measurements that serve as logical read-out and as the fusion primitive are projective measurements of vertex operators, i.e. the same mid-circuit measurement a stabiliser code needs. At the present scale the I/O burden is a handful of measurements per shot; at a scale where the family would be error-corrected it becomes a syndrome stream like any other code's, with the decoding problem — matching anyons of several types with non-trivial fusion — unsolved in practice. The paper's own outlook: "Scaling system sizes will allow for studies of logical error mechanisms and decoding strategies" [D][906].

## Role in the stack

Architectures: an alternate code-layer technology on two — trapped ions with QCCD transport (Quantinuum) and the transmon lattice with tunable couplers (Google, Zhejiang, IBM). It requires a connectivity route: nearest-neighbour gates on a planar lattice for Ising anyons (`cx_nn`), transport for the adaptive torus experiments (`cx_qccd`), or long-range couplers for the wraps (`cx_lr`). It is an alternative to the surface code (`code_surface`): Abelian toric order against non-Abelian order on the same qubits. It touches the magic-state factory (`code_magic`): the S₃ work's heralded topological magic state is a non-Clifford resource prepared by braiding and fusion rather than by cultivation, distillation or code switching — one group, not fault-tolerant. The topological architecture (`majorana`) seeks the same anyons as quasiparticles of a material; here they are prepared by circuits on any carrier, which is why the technology sits on the code layer and not the carrier layer. Price of switching: a decoder and a threshold, neither of which exists; what is gained is a universal gate set in which the non-Clifford element is topological rather than distilled.

## Evidence — how the numbers were measured

The per-qudit fidelities are bounds, not tomographic values: on the 18-site 3 × 3 lattice the ground-state overlap is bracketed as 0.970(5) ≤ ⟨gs|ρ|gs⟩^(1/18) ≤ 0.988(3) from the measured stabiliser-like projectors [D][906]. The braiding gate's quality is a non-local correlator (0.86(3) at the sixth step, theory 1), not a gate fidelity; the read-out's quality is the contrast between the projector values for the two logical states; the magic state is heralded on a fusion outcome whose theoretical probability the figure caption gives as 0.5, and no experimental success rate or state fidelity is quoted in the text read for this record. IBM's 94% and 98% are error-mitigated accuracies, not raw [D][904]; Google's paper reports no per-site fidelity in its abstract [D][901]. Value conflict: the register's H2 row carries the S₃ result as a best logical statement, which is right — it is a logical gate set — but it should not be read as a logical error rate, which no paper in this family publishes. Not published: a logical error per round, any decoder, the braiding gate's fidelity as a number, a lattice beyond 3 × 3.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| Quantinuum | developer | US/UK/DE | D₄, Z₃ and S₃ orders on H2; the only universal topological gate set | [D][902], [905], [906] |
| Harvard University | research | US | Theory and co-leadership of the H2 experiments (Verresen, Vishwanath, Tantivasadakarn) | [D][906] |
| Google Quantum AI | developer | US | Ising anyons braided on a planar superconducting lattice | [D][901] |
| Zhejiang University / Tsinghua University | research | CN | Fibonacci string-net states and braiding on a superconducting processor | [D][903] |
| IBM | developer | US | Fibonacci string-net condensation with error mitigation | [D][904] |

**Money.** No dated money is attached to this technology; it runs on machines funded for other codes. IBM's five-year commitment [G:IBM-10B-2026-06] and DARPA's Quantum Benchmarking Initiative, which funds Quantinuum, IBM and Google's competitors alike [G:QBI-STAGEB-2025-11], are the nearest budgets.

**Market & supply chain.** Nobody sells it and nobody has announced a machine that will use it; it is a research programme on three vendors' hardware. The supply chain is the hosts'.

**IP & standards.** No patent family naming quantum double models on circuit hardware was looked for here; the gate set is published. No standard exists.

**Roadmaps & track record.** No roadmap of Quantinuum, Google or IBM names non-Abelian topological order as a milestone; the record is a sequence of papers at roughly yearly intervals since 2023, each on a larger or richer order, none with error correction.

**Strategic reading.** If a non-Abelian state on a larger torus shows a logical lifetime that grows with size, the topological architecture's argument — that anyons must be found in materials — weakens, because the same physics is then available on any carrier with mid-circuit measurement. If it does not, the family remains what it is today: the most elegant demonstration of what a code could be, on hardware that runs other codes for its results.

## Outlook & open questions

Confirm within 12–24 months if a lattice larger than 3 × 3 reports a logical error per round below the physical error, if a decoder runs on anyon syndromes in the loop, or if a second group prepares S₃ or D₄ order on a different carrier. Demote if by 2028 nothing beyond state preparation and single braids has appeared. Best case by 2029: topological magic states as the non-Clifford resource of an ion or atom machine, cheaper than distillation. Worst case: a closed chapter of many-body physics, cited in code textbooks and run nowhere.

Open questions: (1) does the logical error of a quantum double state fall with lattice size on real hardware? (2) can anyon syndromes of several fusing types be decoded in real time? (3) is the heralded magic state's fidelity, once measured, better than a cultivated one at equal cost? (4) does the adaptive preparation hold its fidelity at hundreds of sites? (5) does any carrier other than ions reach the per-site fidelity the torus needs? Watch H2's successors and the first superconducting S₃ attempt.

## References

[901] T. I. Andersen *et al.*, “Non-Abelian braiding of graph vertices in a superconducting processor,” *Nature*, vol. 618, no. 7964, pp. 264–269, May 2023, doi: [10.1038/s41586-023-05954-4](https://doi.org/10.1038/s41586-023-05954-4). [arXiv:2210.10255](https://arxiv.org/abs/2210.10255). [D]
[902] M. Iqbal *et al.*, “Non-Abelian topological order and anyons on a trapped-ion processor,” *Nature*, vol. 626, no. 7999, pp. 505–511, Feb. 2024, doi: [10.1038/s41586-023-06934-4](https://doi.org/10.1038/s41586-023-06934-4). [arXiv:2305.03766](https://arxiv.org/abs/2305.03766). [D]
[903] S. Xu *et al.*, “Non-Abelian braiding of Fibonacci anyons with a superconducting processor,” *Nat. Phys.*, vol. 20, no. 9, pp. 1469–1475, Jul. 2024, doi: [10.1038/s41567-024-02529-6](https://doi.org/10.1038/s41567-024-02529-6). [arXiv:2404.00091](https://arxiv.org/abs/2404.00091). [D]
[904] Z. K. Minev *et al.*, “Realizing string-net condensation: Fibonacci anyon braiding for universal gates and sampling chromatic polynomials,” *Nat. Commun.*, vol. 16, Art. no. 6225, 2025, doi: [10.1038/s41467-025-61493-8](https://doi.org/10.1038/s41467-025-61493-8). [arXiv:2406.12820](https://arxiv.org/abs/2406.12820). [D]
[905] M. Iqbal *et al.*, “Qutrit toric code and parafermions in trapped ions,” *Nat. Commun.*, vol. 16, Art. no. 6301, 2025, doi: [10.1038/s41467-025-61391-z](https://doi.org/10.1038/s41467-025-61391-z). [arXiv:2411.04185](https://arxiv.org/abs/2411.04185). [D]
[906] C. F. B. Lo *et al.*, “Universal gates from braiding and fusing anyons on quantum hardware,” *Nature*, vol. 655, no. 8123, pp. 591–597, Jul. 2026, doi: [10.1038/s41586-026-10709-y](https://doi.org/10.1038/s41586-026-10709-y). [arXiv:2601.20956](https://arxiv.org/abs/2601.20956). [D]

