---
id: ro_erasure
name: Mid-circuit erasure check
layer: 6 Readout
status: demonstrated
since: 2023
one_line: Ancilla- or fluorescence-based test of whether a qubit is still in its code space, flagging decay/leakage as a located erasure without reading the logical state.
verdict: The check is solved on transmons (384 ns, residual 6×10⁻⁴); unsolved are erasure fraction under two-qubit gates, false negatives and the cycle-time tax. Demote if no erasure system shows logical Λ > 2 by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A mid-circuit erasure check asks "is this qubit still inside its code space?" and returns a one-bit herald with the qubit's location without disturbing the logical state. It needs an encoding whose dominant decay leaves the code space: dual-rail (one excitation in two transmons or two cavities; loss leaves the detectable vacuum) or a metastable atomic qubit (³P₀ in ¹⁷¹Yb, D₅/₂ in ⁴⁰Ca⁺) whose ground-state decay fluoresces under a beam the qubit does not see. Proposals: Princeton/Yale, 2022-01 — 98% of ¹⁷¹Yb errors convertible, surface-code threshold 0.937%→4.15% [S][8]; AWS dual-rail transmons, 2022-08 [S][263]; Yale cavities, 2022-12 [S][315]. Demonstrations: Princeton ¹⁷¹Yb [D][127] and Caltech ⁸⁸Sr [D][129] in 2023-05; AWS transmons [D][316] and Yale cavities [D][317] in 2023-07.

Attributes from the technology graph (legend: a affinity natural↔fabricated; b time, deterministic/heralded; c readout mechanism, time, destructive?, mid-circuit?; d mobility; e control @ placement; f error structure; g manufacturing):
- a = 0.5, carrier-agnostic.
- b = n/a.
- c = ancilla erasure check, 10⁻⁶·⁴ s ≈400 ns, non-destructive, mid-circuit — the transmon record [D][80], not the atomic 20 µs [D][127].
- d = none.
- e = microwave @ room temperature (atoms: optical).
- f = erasure-convertible (located, heralded loss).
- g = none (a protocol, not an object).
Rank 1 of 96; a hub.

## Physics & limits

In a transmon dual-rail pair the logical states are |10⟩ and |01⟩, so a T₁ decay of either transmon lands in |00⟩. The check is a joint dispersive readout tuned so that both logical states pull the shared resonator equally while the vacuum pulls it differently; AWS reaches a residual logical splitting of −0.7(5) kHz against a −4.25 MHz dispersive shift [D][80]. In a cavity pair an ancilla sensitive to the total photon number does the same job in 1.82 µs [D][320]. For atoms a decay from ³P₀ to ¹S₀ is caught by 20 µs of fluorescence on ¹S₀–¹P₁, invisible to the metastable qubit, so survivors pick up less than 10⁻⁵ error per check [D][127].

Each check costs one exposure to T₁: AWS measures 2.54(1)×10⁻² erasure per 384 ns check against a residual undetected error of 6.0(2)×10⁻⁴; their ratio, the erasure bias of 42(1), is what a code cares about [D][80].

Three floors are intrinsic. False negatives re-enter the code as leakage: Yale's 3.7% false-negative rate times its erasure rate gives a missed-erasure fraction of 9.0(5)×10⁻⁴ [D][320]; AWS's are the readout's ≈0.8% separation error [D][80]. Back-action: residual χ mismatch dephases the qubit by 8(3)×10⁻⁵ per check and the readout tone halves the erasure lifetime while on [D][80]. Time: in atoms the 20 µs check stretches to 420 µs when Rydberg population must decay before imaging — hence 56(4)% of single-qubit but only ≈33% of two-qubit errors are converted [D][127]. The code sees a located erasure p_e, a Pauli residual ≈p_e/40 and an unheralded leakage tail ≈FN×p_e; under that channel the surface-code threshold is 4.15% [S][8] and biased-erasure codes reach 8.2–10.3% [S][481]. The floor moves with longer T₁, stronger readout and, for atoms, faster Rydberg-leakage detection.

## Engineering state of the art

Best demonstrated: one dual-rail transmon qubit checked in 384 ns with a 6×10⁻⁴ residual (2026-04) [D][80]; a cavity CZ with 0.5% erasure and 0.03% Pauli error (2026-08) [D][79]. Typical at scale (3 Sep 2026): nothing above ten erasure qubits — SUSTech's four dual-rail transmons at 98.8% logical Bell fidelity (2025-04) [D][322], Quantum Circuits' 8-qubit Seeker (2024-11) [C][81]. On atoms, Princeton's [[4,2,2]] blocks [D][128] and JILA's 20-atom GHZ state [D][482] (2025-06) are the largest erasure-checked circuits; Microsoft/Atom Computing's 24 logical qubits use end-of-round loss imaging, not mid-circuit checks [D][134].

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2023-05 | 20 µs check at 0.986 detection fidelity; 56(4)% of 1Q errors converted | Princeton ¹⁷¹Yb | [D] | [127] |
| 2023-07 | Erasure 2.19(2)×10⁻³ per gate, residual ≈40× lower, <0.1% dephasing per check | AWS transmons | [D] | [316] |
| 2024-06 | 1.82 µs mid-circuit check, FP 0.51%, FN 3.7% | Yale cavities | [D] | [320] |
| 2024-11 | ⁴⁰Ca⁺ Bell 98.56→99.14% with erasure excision; 1 ms check | Oregon | [D] | [309] |
| 2025-06 | ¹⁷¹Yb error-detected CZ 99.78(4)%, >90% Rydberg-decay detection | JILA | [D] | [482] |
| 2025-06 | [[4,2,2]] teleportation 0.771→0.802 with erasure-selected ancillas | Princeton | [D] | [128] |
| 2026-04 | 384 ns check, residual 6.0(2)×10⁻⁴, bias 42(1) | AWS | [D] | [80] |
| 2026-08 | Dual-rail CZ 500 ns, erasure ≈0.5% per gate, Pauli 0.029(6)%, bit-flip 2.8(4)×10⁻⁶ | Quantum Circuits | [D] | [79] |

Dominant term today: on transmons the idling erasure during the check (T₁ ≈25 µs); on cavities the ancilla's decoherence; on atoms undetectable two-qubit errors and the Rydberg dead time.

## Manufacturing, materials & supply chain

Transmon dual-rail uses standard superconducting lithography, but the pair must be flux-tunable to find a χ-matched point and dodge two-level systems, and both must be good — a yield-squared problem; AWS's five-day samples fluctuate with near-resonant TLSs [D][80]. Cavity dual-rail needs two machined high-Q cavities plus an ancilla per qubit, hand-assembled — hence Quantum Circuits' plan of 8 → 17 → 49 → 181 qubits over 2024–2028 [R][88]. The atomic check needs only an imaging beam and a camera. Cost and energy per checked qubit are unpublished. The transmon check inherits the dispersive-readout chain, whose amplifiers and refrigerators are the concentrated items. Export exposure: the BIS rule of 2024-09-06 [G][225] [G:BIS-QUANTUM-2024] lists parametric amplifiers and cryo-CMOS (3A901), refrigerators of ≥600 µW at ≤0.1 K (3A904) and computers with ≥34 physical qubits (4A906), a floor no erasure system reaches; the rule does not say whether a dual-rail qubit counts as one or two.

## Control, readout & I/O burden

Superconducting: one readout resonator per dual-rail qubit on a multiplexed feedline, two flux lines per qubit, one TWPA per line — twice a transmon's I/O. Replacing an erased qubit within the cycle needs feed-forward of a few hundred ns. At 10³ qubits the wiring is the transmon wall doubled; at 10⁴ only cold multiplexing or cryo-CMOS works, helped by the one-bit flag; at 10⁶ the 384 ns per cycle and 2×10⁶ transmons are the price of the 40× bias. Atoms: one global 20 µs pulse and one camera frame per check — lines do not grow with N, but camera read-out and processing (0.1–1 ms) set the loop latency, and fast frames cost survival (98.80(44)% for Kyoto's 17.6 µs ¹⁷⁴Yb imaging [D][264]); the wall beyond 10⁴ atoms is frame budget.

## Role in the stack

Two platform paths: superconducting dual-rail erasure and alkaline-earth neutral atoms. It requires an erasure-detectable encoding — dual-rail, or the metastable "omg" (optical–metastable–ground) encoding — and provides the flags that dual-rail encodings and erasure-adapted codes consume. It displaces leakage removal and post-selection on bare transmons. The price of switching is 2× transmons plus a check every cycle; on atoms the metastable manifold costs single-qubit fidelity (99.12(4)% in ³P₀ against 99.968(3)% in the ground state of JILA's omg device [D][483]). Off-diagonal reading: "fabricated carrier with an erasure error structure" is genuine; "natural carrier with ≤10 µs readout" is inherited from the transmon time, not earned by the 20 µs atomic check. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: dual-rail path 2.8 µs, set by the gate layers, with the 0.40 µs check a seventh of it; atom path 1.3 ms, set by transport, the check ≈1.5% of it. Neighbouring empty slots: the cold-stage decoder (a natural consumer of one-bit heralds) and the microwave–optical transducer.

## Verification (QCVV)

FP/FN come from preparing |0_L⟩, |1_L⟩ and the erased state and repeating the check; AWS quotes FP ≈ FN ≈0.8% and derives residual and bias from repeated-check and interleaved sequences under continuous detection [D][80]. Gate-level erasure fractions are flag statistics and the residual Pauli error a low-depth linear fit [D][79]. Atomic conversion fractions rest on the 0.986 detection fidelity [D][127]; Caltech's ≥0.9971 Bell fidelity is a post-excision, SPAM-corrected bound [D][129].

Not captured: survival (every headline fidelity is conditioned on "no erasure"; at 2.5% per check, forty checks halve the sample); false negatives, visible only as leakage in a multi-round code; spectator dephasing on shared feedlines, unbenchmarked beyond four qubits; drift (TLS-driven swings over 5–18 days [D][80]); the time tax. Independent replications: AWS (2023, 2026) [D][80], [316], Yale (2023, 2024) [D][317], [320], Quantum Circuits (2026) [D][79], SUSTech (2025) [D][322], UMass (2026) [D][321]; Princeton (2023, 2025) [D][127], [128], Caltech (2023) [D][129], JILA (2025) [D][482]; Oregon (2024) [D][309].

Conflicts. D-Wave says its qubits detect "approximately 90% of errors" [C][88]; at gate level the fraction is 83–94% depending on whether the Pauli residual is the <0.1% bound or the 0.029% fit [D][79]. Atomic two-qubit conversion is 33–38% [D][127], [128] against the proposal's 98% [S][8]. The [[4,2,2]] gain from erasure information is 1.9(4)× in the 2025-06 arXiv text [D][128] but 3.6× as carried in the graph from the 2026-06 Nature Physics version [D][128]; the arXiv value is used pending the published text.

## Actors & economics

**Who.**

| Organisation | Role | Country | What it does with the check | Evidence |
|---|---|---|---|---|
| Quantum Circuits Inc. | developer | US | Cavity dual-rail qubits; 8-qubit Seeker; 17-qubit system due 2026; D-Wave unit since 2026-01 | [D][79] [C][81] [G:DWAVE-QCI-2026-01] |
| AWS Center for Quantum Computing | developer | US | 384 ns χ-matched transmon check | [D][80], [316] |
| Yale University | research | US | Cavity dual-rail origin; ancilla check | [D][317], [319], [320] |
| SUSTech (Shenzhen) | research | China | Four dual-rail transmon qubits | [D][322] |
| Princeton University | research | US | ¹⁷¹Yb metastable conversion; [[4,2,2]] | [D][127], [128] |
| Google Quantum AI | developer | US | Atom track under Kaufman (ex-JILA ¹⁷¹Yb omg), 2026-03 | [G:GOOGLE-ATOMS-2026-03] [P][141] [D][482], [483] |
| Atom Computing | developer | US | ¹⁷¹Yb 1,225-atom systems; loss by imaging; Magne with Microsoft | [D][134] [G:MAGNE-2025-07] |

**Money.**
- 2024-05 · Quantum Circuits · Series B extension · $26.5 M · Sequoia · cumulative ≈$84 M · closed [P][484] [G:QCI-FUNDING]
- 2024-08-15 · Quantum Circuits · Series B close · >$60 M · ARCH, F-Prime, Sequoia, Hither Creek · overlaps the extension · closed [C][485] [G:QCI-FUNDING]
- 2025-07-17 · QuNorth · Magne order, 50 logical qubits · €80 M · Atom Computing/Microsoft · ordered [G:MAGNE-2025-07]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each · eleven teams, no dual-rail vendor · official [G][60] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · acquires Quantum Circuits · $550 M ($300 M stock + $250 M cash) · closed 2026-01-19/20 [C][14], [486] [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; Atom Computing · US DoC CHIPS letters of intent · $100 M each · LOI [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · Series C · $100 M · Third Point Ventures · >$300 M cumulative · closed [C][138] [G:ATOM-300M-2026-06]
- 2026-08-06 · D-Wave · H1-2026 results · revenue $5.9 M (−67% YoY), cash $546.2 M · reported [G:DWAVE-FIN-2026]

**Market & supply chain.** Nobody sells an erasure check; it rides on the amplifiers and refrigerators of dispersive readout (concentrated, BIS-listed [G][225]). Unit economics are unpublished; the structural cost is 2× transmons or two cavities plus an ancilla per qubit, against Quantum Circuits' claim of 10–20 physical per logical instead of ~200 [C][81]. Only G3 and G4 pay, once codes run 10⁵–10⁶ rounds.

**IP & standards.** Amazon Technologies: US 11,748,652 B1, "Heralding of amplitude damping decay noise for quantum error correction" (Kubica, Retzker; filed 2021-12-10, granted 2023-09-05): heralded decay via a level outside the code space, dual-rail included [G][266]. Yale: US 12,288,135, ancilla with an asymmetric error channel (filed 2019-06-28, granted 2025-04-29) [G][324]. The Yale/Quantum Circuits cavity families now sit with D-Wave. No standard; Stim's HERALDED_ERASE instruction [P][313] commoditises the decoding side.

**Roadmaps & track record.**
- D-Wave: promised 2026-01-07 · initial dual-rail system available in 2026 · not delivered as of 2026-09-03 [C][14].
- D-Wave: promised 2026-06-01 · 17 qubits with logical error 2× below physical (2026), 49 / 20× (2027), 181 / 2,000× (2028), 10 logical (2030), 100 logical (2032), Λ = 10 · pending, no logical data [R][88] [G:DWAVE-QCI-2026-01].
Credibility: Quantum Circuits/D-Wave high on physics, unproven on dates; AWS publishes results and promises no product; Princeton delivered the single-qubit half of its 2022 proposal [S][8] [D][127]; Atom Computing on schedule, uncommitted to mid-circuit checks.

**Strategic reading.** If erasure checks scale, the winners own high-T₁ fabrication and the readout chain — D-Wave, AWS and the alkaline-earth camp (Atom Computing, Google); the losers are bare-transmon roadmaps buying threshold with Λ alone. Substitution threats: qutrit erasure qubits [D][321] remove the 2× overhead; fast Yb imaging [D][264] and loss-aware decoding erode the case for metastable encodings. Bargaining power stays with platform vendors, not suppliers.

*Open niche:* a small QCVV/SFQ company could own the missing benchmark — an "erasure-check tomography" reporting false positives, false negatives, spectator dephasing, survival-corrected fidelity and drift in one protocol; an SFQ cold-stage flag aggregator is the natural add-on.

## Outlook & open questions

Confirm within 12–24 months if: D-Wave ships the 17-qubit system with published logical error 2× below physical by mid-2027 [R][88]; any group runs ≥10 rounds of a distance-3 code on dual-rail qubits with survival reported; atomic two-qubit conversion reaches ≥70% with a check ≤50 µs; a χ-matched check reaches ≤250 ns with residual ≤3×10⁻⁴. Demote if by end-2027 no erasure system reports Λ >2 on unconditioned data. Best case by 2029: 100–200 dual-rail qubits at Λ ≈4–10 with 2 µs cycles, and Yb machines running erasure-aware codes. Worst case: erasure stays a two-qubit showpiece while bare transmons reach 10⁻³ and Λ ≈3 without it.

Open questions: (1) does the 40× bias survive parallel checks on qubits sharing feedlines? (2) can Rydberg leakage be made bright within microseconds? (3) what does a decoder do with false negatives at 10⁻³ as leakage accumulates? Watch: D-Wave's 2026 delivery, AWS's next multi-qubit paper, Google/Kaufman Yb results.

## Sources

[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[79] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [D]
[80] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026. [D]
[81] Quantum Circuits, “Quantum Circuits Makes Error-Detecting Qubits,” Nov. 19, 2024. [Online]. Available: https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/ [C]
[88] M. Swayne, “D-Wave's New Gate-Model Roadmap Puts Pin in 2032 For 100 Logical-Qubit System,” The Quantum Insider, Jun. 1, 2026. [Online]. Available: https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/ [R]
[127] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493). [D]
[128] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[129] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[134] B. W. Reichardt *et al.*, “Fault-tolerant quantum computation with a neutral atom processor,” [arXiv:2411.11822](https://arxiv.org/abs/2411.11822), Nov. 2024. [D]
[138] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[141] M. Swayne, “Google Paves a Two-Lane Quantum Roadmap by Adding Neutral Atom Systems,” The Quantum Insider, Mar. 24, 2026. [Online]. Available: https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/ [P]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[263] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461). [S]
[264] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [D]
[266] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]
[309] A. Quinn *et al.*, “High-fidelity entanglement of metastable trapped-ion qubits with integrated erasure conversion,” *Phys. Rev. A*, vol. 113, no. 4, Art. no. L040601, Apr. 2026, doi: [10.1103/p3cy-8yjk](https://doi.org/10.1103/p3cy-8yjk). [arXiv:2411.12727](https://arxiv.org/abs/2411.12727). [D]
[313] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[315] J. D. Teoh *et al.*, “Dual-rail encoding with superconducting cavities,” *Proc. Natl. Acad. Sci. USA*, vol. 120, no. 41, Art. no. e2221736120, Oct. 2023, doi: [10.1073/pnas.2221736120](https://doi.org/10.1073/pnas.2221736120). [arXiv:2212.12077](https://arxiv.org/abs/2212.12077). [S]
[316] H. Levine *et al.*, “Demonstrating a long-coherence dual-rail erasure qubit using tunable transmons,” *Phys. Rev. X*, vol. 14, no. 1, Art. no. 011051, Mar. 2024, doi: [10.1103/PhysRevX.14.011051](https://doi.org/10.1103/PhysRevX.14.011051). [arXiv:2307.08737](https://arxiv.org/abs/2307.08737). [D]
[317] K. S. Chou *et al.*, “Demonstrating a superconducting dual-rail cavity qubit with erasure-detected logical measurements,” [arXiv:2307.03169](https://arxiv.org/abs/2307.03169), Jul. 2023. [D]
[319] A. Koottandavida *et al.*, “Erasure Detection of a Dual-Rail Qubit Encoded in a Double-Post Superconducting Cavity,” *Phys. Rev. Lett.*, vol. 132, no. 18, Art. no. 180601, May 2024, doi: [10.1103/PhysRevLett.132.180601](https://doi.org/10.1103/PhysRevLett.132.180601). [arXiv:2311.04423](https://arxiv.org/abs/2311.04423). [D]
[320] S. J. de Graaf *et al.*, “A mid-circuit erasure check on a dual-rail cavity qubit using the joint-photon number-splitting regime of circuit QED,” *npj Quantum Inf.*, vol. 11, no. 1, Jan. 2025, doi: [10.1038/s41534-024-00944-4](https://doi.org/10.1038/s41534-024-00944-4). [arXiv:2406.14621](https://arxiv.org/abs/2406.14621). [D]
[321] B.-J. Liu *et al.*, “Hardware-Efficient Erasure Qubits With Superconducting Transmon Qutrits,” [arXiv:2604.08672](https://arxiv.org/abs/2604.08672), Apr. 2026. [D]
[322] W. Huang *et al.*, “Logical multi-qubit entanglement with dual-rail superconducting qubits,” *Nat. Phys.*, vol. 22, no. 4, pp. 591–597, Mar. 2026, doi: [10.1038/s41567-026-03211-9](https://doi.org/10.1038/s41567-026-03211-9). [arXiv:2504.12099](https://arxiv.org/abs/2504.12099). [D]
[324] Justia, “Shruti PURI Inventions, Patents and Patent Applications - Justia Patents Search.” [Online]. Available: https://patents.justia.com/inventor/shruti-puri [G]
[481] K. Sahay, J. Jin, J. Claes, J. D. Thompson, and S. Puri, “High-Threshold Codes for Neutral-Atom Qubits with Biased Erasure Errors,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041013, Oct. 2023, doi: [10.1103/PhysRevX.13.041013](https://doi.org/10.1103/PhysRevX.13.041013). [arXiv:2302.03063](https://arxiv.org/abs/2302.03063). [S]
[482] A. Senoo *et al.*, “High-fidelity entanglement and coherent multi-qubit mapping in an atom array,” [arXiv:2506.13632](https://arxiv.org/abs/2506.13632), Nov. 2025. [D]
[483] J. W. Lis *et al.*, “Mid-circuit operations using the omg-architecture in neutral atom arrays,” [arXiv:2305.19266](https://arxiv.org/abs/2305.19266), May 2023. [D]
[484] M. Swayne, “Quantum Circuits Inc. Quietly Raises $26.5 Million,” The Quantum Insider, May 29, 2024. [Online]. Available: https://thequantuminsider.com/2024/05/29/quantum-circuits-inc-quietly-raises-26-5-million/ [P]
[485] Quantum Circuits, Inc., “Quantum Circuits Secures More Than $60 Million in Series B Investment,” PR Newswire, Aug. 15, 2024. [Online]. Available: https://www.prnewswire.com/news-releases/quantum-circuits-secures-more-than-60-million-in-series-b-investment-302221428.html [C]
[486] D-Wave Quantum Inc., “D-Wave Completes Acquisition of Quantum Circuits Inc., Creating World's Leading Quantum Computing Company,” Business Wire, Jan. 19, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260119513563/en/D-Wave-Completes-Acquisition-of-Quantum-Circuits-Inc.-Creating-Worlds-Leading-Quantum-Computing-Company [C]

## Open verification items

- [[4,2,2]] erasure-information gain: 1.9(4)× in arXiv:2506.13724 v1 [D][128] versus 3.6× carried in the graph from the Nature Physics version [D][128]; the published main text could not be read (nature.com shows the abstract only; phys.org returned HTTP 429).
- Quantum Circuits' 2017 Series A amount (reported $18 M, Canaan/Sequoia) not verified from a primary source; omitted.
- Quantum Circuits' cumulative funding ≈ $84 M to May 2024 is a trade-press figure [P][484]; the company's release states no total.
- Whether Quantum Circuits was the unnamed 18th DARPA QBI Stage A company: DARPA names 17 of 18 [G:QBI-STAGEA-2025-04]; unresolved.
- Cost or energy per checked qubit: no actor publishes it.
- Patent counts for the Yale/Quantum Circuits dual-rail cavity families: not available from a named database; two individual patents cited.
- Oregon metastable-ion Bell fidelities: 98.61 → 99.16 % (abstract summaries) versus 98.56 → 99.14 % (arXiv v1 full text) [D][309]; the full text is used.
- AWS's spending on its dual-rail programme and the grants behind the Princeton, Caltech, Yale, Oregon and SUSTech groups: undisclosed or not attributable to this primitive.
- The atomic species of Google's neutral-atom track is not stated in accessible sources; not claimed.
