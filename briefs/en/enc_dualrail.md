---
id: enc_dualrail
name: Dual-rail (erasure) encoding
layer: 2 Encoding
tier: 1
status: demonstrated
since: 2023
one_line: One excitation shared between two modes; loss leaves the code space and is heralded as a located erasure, not an unknown Pauli.
verdict: The cleanest error channel in superconducting hardware (≈0.5% erasure, 0.03% residual Pauli per CZ), bought with 2× the modes; unproven above eight qubits. Demote if no dual-rail device shows a coded Λ > 2 by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A dual-rail qubit is one quantum of excitation shared between two modes: |0_L⟩ = |10⟩, |1_L⟩ = |01⟩. The dominant hardware error — cavity photon loss, transmon T₁ decay, waveguide absorption — is the annihilation operator on either rail, and it sends both logical states to |00⟩, outside the code space. A total-excitation measurement therefore commutes with the logical operators: decay is caught and *located* without disturbing the encoded state, turning the largest error term from unknown Pauli into heralded erasure. What remains is differential dephasing between two rails never quite identical.

Dual-rail is the native photonic qubit: Chuang and Yamamoto (1995) called it "a simple form of error correction" [S][1]; Knill, Laflamme and Milburn built linear optics on it in 2000 [S][2]. The superconducting transfer was deliberate — AWS proposed transmon pairs (2022-08) [S][3], Yale cavities (2022-12) [S][4], both demonstrated July 2023 [D][5][6].

Coordinates from the technology graph (a affinity; b time; c readout; d mobility; e control @ placement; f errors; g manufacturing):
- a = 0.25, fabricated — engineered modes, not natural levels.
- b = n/a; no gate time of its own.
- c = none; the check is a separate primitive.
- d = none.
- e = none @ none.
- f = erasure: located, heralded loss.
- g = none; a wiring choice, not an object.
Rank 6 of 96; a hub across photonics and superconductors.

## Physics & limits

The energy scale is one quantum — a 6 GHz microwave or 1.5 µm optical photon — and the time scale is the single-excitation lifetime of the worse rail. Either rail can decay, so the erasure rate is roughly twice the single-mode loss rate: the qubit *fails more often* than a bare one, and wins only if the code eats located errors more cheaply. It does — erasure locations lift the surface-code threshold to 50% in the ideal limit against ≈19% for depolarising noise, and at 1% erasure the tolerable Pauli rate rises 5.2× [S][13][3].

The measured hierarchy is the point: a Yale double-post cavity gave erasure at 3.981(3) ms⁻¹ against in-code-space dephasing below 0.17 ms⁻¹ [D][7]; AWS's transmon pair, erasure 2.19(2)×10⁻³ per single-qubit gate with residual ~40× lower and millisecond code-space coherence from far shorter-lived transmons [D][5].

Four floors are intrinsic: rail asymmetry, whose differential frequency shift dephases the code space and does not improve with lifetime; false negatives, re-entering as invisible leakage (3.7% [D][8], 6–8% in the qutrit variant [D][14]); heating out of the single-excitation manifold; and the check's own exposure. Only longer lifetimes, matched shifts and faster checks move them.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: a cavity dual-rail CZ in ~500 ns at ≈0.5% erasure per gate and 0.029(6)% post-selected Pauli error [D][11]. Typical at scale: nothing beyond eight qubits — Quantum Circuits' 8-qubit Aqumen Seeker (2024-11) [C][20], SUSTech's four dual-rail transmons (2025-04) [D][9].

**Records timeline**

| Year | Figure | Who | Evidence |
|---|---|---|---|
| 2023-07 | Erasure 2.19(2)×10⁻³ per 1Q gate, residual ~40× lower | AWS | [D][5] |
| 2025-04 | Four dual-rail transmons: logical Bell 98.8%, CNOT 96.2% | SUSTech | [D][9] |
| 2026-04 | 384 ns check; erasure 2.54(1)×10⁻², residual 6.0(2)×10⁻⁴, bias 42(1) | AWS | [D][10] |
| 2026-08 | CZ ~500 ns; erasure ≈0.5%/gate, Pauli 0.029(6)%, bit-flip 2.8(4)×10⁻⁶ | Quantum Circuits | [D][11] |
| 2025 | Photonic dual-rail: fusion Bell 99.22(12)%, SPAM 99.98(1)% | PsiQuantum | [D][12] |

Dominant term today: control-qubit dephasing during the gate in cavities, 3× the target's [D][11]; check exposure and false negatives in transmons [D][10]; loss in photonics.

## Manufacturing, materials & supply chain

Machined cavities (high-purity aluminium, sapphire-mounted ancillas) give the longest photon lifetimes and no foundry path — Quantum Circuits' line. Planar transmon pairs (AWS, SUSTech) inherit ordinary superconducting fabrication but take twice the die area per site and add a requirement bare transmons lack: the rails must be *matched* in frequency and coupling, so the frequency-collision problem that limits transmon yield now applies pairwise. No vendor publishes a dual-rail yield, cost or energy per qubit. Photonic dual-rail is the best case — path encoding is free in a waveguide — PsiQuantum's 300 mm silicon-nitride platform running 1.8(2) dB/m waveguide loss and 93.4% median detector efficiency at ~2 K [D][12].

Superconducting variants ride the export-controlled stack: refrigerators, amplifiers, microwave I/O (BIS ECCNs 3A904, 4A906, 3B904) [G][21] [G:BIS-QUANTUM-2024]. Photonics depends on a 300 mm CMOS-photonics foundry, barium-titanate switches and nanowire detectors — single-source risk at both.

## Control, readout & I/O burden

The encoding doubles control fan-out: two drive lines per qubit, or two cavities plus an ancilla transmon and its readout. AWS folds that back with one readout resonator coupled symmetrically to the pair, so the check is a single 384 ns pulse costing 8(3)×10⁻⁵ dephasing [D][10] [G:AWS-ERASURE-2026-04]; the cavity variant needs a number-splitting ancilla measurement, 1.82 µs standalone [D][8], now folded into the gate [D][11]. The system burden is the flag path: one bit per qubit per round must reach the decoder inside a syndrome cycle, against NVQLink's 3.84 µs round trip [G:NVQLINK-2025]. At 10³ qubits that is 2×10³ modes and 10³ flag channels; at 10⁴ the ~10 Gb/s flag bandwidth forces cold-stage aggregation; at 10⁶ only planar or photonic survives.

## Role in the stack

Dual-rail sits on two named paths: "Superconducting dual-rail erasure" (Quantum Circuits/D-Wave, AWS, SUSTech) and "Photonic — fusion-based (DV)" (PsiQuantum, Quandela, QuiX). It requires a mid-circuit erasure check and is what that check reads; without one it is merely a lossier qubit. It replaces bare encoding at 2× the modes and conflicts with the plain surface code, which discards heralds. Hence the fabrication↔erasure off-diagonal: buy error *structure* with area, not error *rate* with coherence.

Derived clock = max(gate, readout, transport): 5.0×10⁻⁷ s on the cavity route, set by the CZ [D][11]; 3.8×10⁻⁷ s on the transmon route, set by the check [D][10]. Switching away is cheap in hardware, expensive in software: decoder, calibration and benchmarks assume heralds. Neighbouring empty slots: a dual-rail *logical* memory over repeated rounds, and the erasure-biased code consuming heralds and bias.

## Verification (QCVV)

Every headline number here is post-selected: erasure rates come from heralded tomography or interleaved benchmarking with flagged shots discarded, so a "99.9% gate" is a conditional fidelity whose companion figure, the survival fraction, decides whether the device is useful. The protocols miss correlated two-rail loss, heating into |11⟩, rail-asymmetry drift, and the erasure fraction under *two-qubit gates in a repeated cycle* rather than idling. False negatives, the least-reported quantity, set the leakage floor the decoder never sees.

Replication is real: transmon AWS 2023 → SUSTech 2025 → AWS 2026; cavity Yale 2023 → 2025 → Quantum Circuits 2026. Conflicts: the 2026 Nature gate is post-selected Pauli < 0.1% (0.12% at depth) with erasure fraction ≈80% in the main report, 0.029(6)% per gate cited from the same paper, "below 0.1%" in the arXiv abstract [D][11] — per-gate versus depth-extrapolated, quoted rather than merged. Second, PsiQuantum waveguide loss is 0.5 dB/m in the main report against 1.8(2) dB/m in Nature [D][12].

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with this encoding | Evidence |
|---|---|---|---|---|
| Quantum Circuits Inc. (D-Wave unit) | developer | US | Cavity dual-rail; Seeker; DR17–DR181 roadmap | [D][11] [C][20] [G:DWAVE-QCI-2026-01] |
| AWS Center for Quantum Computing | developer | US | Transmon dual-rail; symmetric-readout check | [D][5] [G:AWS-ERASURE-2026-04] |
| Yale University | research | US | Origin of the cavity encoding; C2QA | [D][4][6][7] [G:DOE-NQISRC-2025-11] |
| PsiQuantum | developer | US | Path-encoded dual-rail photonics, 300 mm | [D][12] [G:PSIQ-QBI-C-2026-07] |
| SUSTech | research | China | Four dual-rail transmons; logical Bell, CNOT | [D][9] [G:SUSTECH-DUALRAIL-2025] |
| Oxford Quantum Circuits | developer | UK | Industrial erasure-qubit review | [S][13] [G:OQC-SERIESC-2026-06] |
| UMass Amherst | research | US | Transmon-qutrit erasure qubit | [D][14] |
| ORCA Computing | developer | UK | Linear-optical dual-rail GHZ patents | [G][16] |

**Money.**
- 2024-08-15 · Quantum Circuits · Series B · > $60 M · ARCH, F-Prime, Sequoia · ≈$84 M cumulative [P] · closed [G:QCI-FUNDING]
- 2025-09-10 · PsiQuantum · Series E · $1 B at $7 B · BlackRock · closed [G:PSIQ-1B-2025-09]
- 2025-11-04 · US DOE · NQISRC renewal, C2QA · $125 M of $625 M · awarded [G:DOE-NQISRC-2025-11]
- 2025-11-06 · DARPA QBI Stage B · up to $15 M each, eleven teams, no dual-rail vendor [G][25] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · acquires Quantum Circuits · $550 M ($300 M stock + $250 M cash) · closed 2026-01-20 [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; PsiQuantum · US DoC CHIPS letters of intent · $100 M each · LOI [G:CHIPS-LOI-2026-05]
- 2026-06-03 · Oxford Quantum Circuits · Series C · £260 M · Bullhound · closed [C][17] [G:OQC-SERIESC-2026-06]
- 2026-07-22 · PsiQuantum · DARPA QBI Stage C expansion · $125 M · switch and cryogenics V&V [G:PSIQ-QBI-C-2026-07]
- 2026-08-06 · D-Wave · Q2-2026 · revenue $3.1 M, cash $546.2 M, $1.57 M NSF grant · reported [C][26] [G:DWAVE-Q2-2026-GATEMODEL]

**Market & supply chain.** Nobody sells the encoding; it is priced as hardware multiplicity — two modes plus an ancilla per site — plus the readout chain that reads the herald. On superconductors that is 2–3× die area or a machined cavity assembly with no foundry, so the suppliers that matter are the refrigerator and amplifier vendors under BIS control [G][21]. On photonics it is free, and the bill of materials is the foundry, the switch and the detector. G2 pays today for post-selected fidelity, which is what Seeker sells [C][20]; G3 and G4 pay once codes run 10⁵–10⁶ rounds; G6 pays on the photonic side; G1, G5 and G7 do not.

**IP & standards.** Amazon Technologies US 11,748,652 B1, heralded amplitude-damping decay for QEC (granted 2023-09-05), covers the transmon embodiment [G][23] [G:AMZN-ERASURE-PATENT]; Yale US 12,288,135, asymmetric-error-channel processing (granted 2025-04-29), sits with the cavity families that passed to D-Wave in January 2026 [G][24]; ORCA Computing holds US 12,437,225, linear-optical encoded GHZ measurements (2025-10-07) [G][16]. No dated patent-family count was obtainable from a named database; no standard exists, and Stim's HERALDED_ERASE is the de-facto decoder interface [P][22].

**Roadmaps & track record.**
- D-Wave/Quantum Circuits: promised 2026-06-01, restated 2026-08-06 · DR17 (17 qubits, 2× logical error reduction) 2026, DR49 at 20× 2027, DR181 at 2,000× 2028, 10 logical 2030, 100 logical 2032, Λ = 10 · undelivered as of 2026-09-03 [R][18] [G:DWAVE-QCI-2026-01].
- PsiQuantum: promised utility scale "before 2033" · Brisbane groundbreaking slipped to 2026-06-17 · at risk [G:PSIQ-1B-2025-09].
- AWS: no dual-rail product promised · three papers delivered 2022–2026 [D][5][10]. Oxford Quantum Circuits: TITAN announced with the Series C · no dated dual-rail target [C][17].
Credibility: Quantum Circuits/D-Wave publishes the field's best channel numbers and has never shipped a system; AWS publishes and promises nothing; PsiQuantum's components are the best-characterised anywhere, its systems slip.

**Strategic reading.** If dual-rail wins, the winners own long-lived modes and cheap area — cavity vendors and photonic foundries — and the losers are transmon roadmaps spending their whole budget on T₁, since the encoding makes T₁ a *detected* cost, not a fatal one. Substitution runs hard from inside the family: the transmon-qutrit erasure qubit needs one transmon and one ancilla, not two rails, at logical T₁ > 500 µs against a physical ~55 µs [D][14]; dual-rail cat codes add bias to the same structure [S][15]. Bargaining power sits with platform vendors.

*Open niche:* a small QCVV/SFQ research company could own the missing measurement — a dual-rail channel benchmark reporting erasure fraction, residual Pauli, bias, false-negative rate, survival and drift as one dated tuple, taken under two-qubit gates in a repeated cycle rather than idling; the SFQ angle is a cold-stage herald aggregator compressing one flag bit per qubit per round before it leaves the fridge.

## Outlook & open questions

Confirm if, within 12–24 months: DR17 ships with a *measured* 2× logical error reduction; any group runs a code on ≥ 10 dual-rail qubits with Λ > 2 and publishes the survival fraction; someone reports the erasure fraction under two-qubit gates in a repeated cycle. Demote if none lands by end-2027, or if the qutrit erasure qubit matches dual-rail's bias at half the hardware. Best case by 2029: a 181-qubit machine at the promised suppression. Worst case: doubled modes and check dead time eat the threshold gain, and the encoding survives only where it is free, in photonics.

Open questions. (1) Does the erasure fraction hold under two-qubit gates at depth? (2) What is a production check's false-negative rate, and does it scale? (3) Can planar dual-rail reach cavity-grade lifetimes? (4) Is there a regime where doubling modes beats doubling code distance? Watch D-Wave's quarterly disclosures and the first repeated-round dual-rail memory paper.

## Sources

[1] Chuang, I. L., Yamamoto, Y. · Simple quantum computer · Phys. Rev. A 52, 3489 (arXiv:quant-ph/9505011) · 1995 · https://arxiv.org/abs/quant-ph/9505011
[2] Knill, E., Laflamme, R., Milburn, G. · Efficient linear optics quantum computation · arXiv:quant-ph/0006088; Nature 409, 46 (2001) · 2000-06-20 · https://arxiv.org/abs/quant-ph/0006088
[3] Kubica, A., Haim, A., Vaknin, Y., Brandão, F., Retzker, A. (AWS) · Erasure qubits: overcoming the T1 limit in superconducting circuits · PRX 13, 041022 (arXiv:2208.05461) · 2022-08-10 · https://arxiv.org/abs/2208.05461
[4] Teoh, J. D. et al. (Yale) · Dual-rail encoding with superconducting cavities · PNAS 120 (arXiv:2212.12077) · 2022-12-22 · https://arxiv.org/abs/2212.12077
[5] Levine, H. et al. (AWS) · Demonstrating a long-coherence dual-rail erasure qubit using tunable transmons · PRX 14, 011051 (arXiv:2307.08737) · 2023-07-17 · https://arxiv.org/abs/2307.08737
[6] Chou, K. S. et al. (Yale) · Demonstrating a superconducting dual-rail cavity qubit with erasure-detected logical measurements · Nature Physics 20, 1454 (arXiv:2307.03169) · 2023-07-06 · https://arxiv.org/abs/2307.03169
[7] Koottandavida, A. et al. (Yale) · Erasure detection of a dual-rail qubit encoded in a double-post superconducting cavity · PRL 132, 180601 (arXiv:2311.04423) · 2023-11-08 · https://arxiv.org/abs/2311.04423
[8] de Graaf, S. J. et al. (Yale) · A mid-circuit erasure check on a dual-rail cavity qubit using the joint-photon number-splitting regime of circuit QED · npj Quantum Information 11, 1 (arXiv:2406.14621) · 2025-01-07 · https://www.nature.com/articles/s41534-024-00944-4
[9] Huang, W. et al. (SUSTech) · Logical multi-qubit entanglement with dual-rail superconducting qubits · arXiv:2504.12099; Nature Physics 2026, doi:10.1038/s41567-026-03211-9 · 2025-04-16 · https://arxiv.org/abs/2504.12099
[10] Hung, J. S.-C. et al. (AWS) · Fast, high-fidelity erasure detection of dual-rail qubits with symmetrically coupled readout · arXiv:2604.16292 · 2026-04-17 · https://arxiv.org/abs/2604.16292
[11] Quantum Circuits / D-Wave Quantum · An entangling gate for dual-rail erasure qubits (arXiv title: Bias-preserving and error-detectable entangling operations in a superconducting dual-rail system) · Nature 656, 47 (arXiv:2503.10935) · 2026-08-05 · https://www.nature.com/articles/s41586-026-10822-y
[12] Alexander, K. et al. (PsiQuantum) · A manufacturable platform for photonic quantum computing (Omega) · Nature · 2025 · https://www.nature.com/articles/s41586-025-08820-7
[13] Violaris, M., Henaut, L., Wills, J., Consani, G., Friel, J., Vlastakis, B. (Oxford Quantum Circuits) · Developments in superconducting erasure qubits for hardware-efficient quantum error correction · arXiv:2601.02183 · 2026-01-05 · https://arxiv.org/abs/2601.02183
[14] Liu, B.-J., Wang, Y.-Y., Wang, Y.-X., Badbaria, M., Puri, S., Wang, C. (UMass Amherst / Yale) · Hardware-efficient erasure qubits with superconducting transmon qutrits · arXiv:2604.08672 · 2026-04-09 · https://arxiv.org/abs/2604.08672
[15] Biswas, D., Sharma, N., Salvador, A., Wang, R., Granath, M., Udupa, A., Ferrini, G. · Bias-preserving gates and quantum error correction with dual-rail cat codes · arXiv:2607.00786 · 2026-07-01 · https://arxiv.org/abs/2607.00786
[16] [G] USPTO (via Justia Patents) · US 12,437,225, Linear-optical encoded GHZ measurements and fault-tolerant quantum computation and communication, ORCA Computing Limited (filed 2023-10-16); application US 2024/0256939 · granted 2025-10-07 · https://patents.justia.com/patent/12437225
[17] [C] Oxford Quantum Circuits · OQC Series C, £260 M led by Bullhound Capital · company newsroom · 2026-06-03 · https://oqc.tech/company/newsroom/series-c
[18] [P] Quantum Computing Report · D-Wave demonstrates two-qubit gate breakthrough for dual-rail erasure qubits in Nature (DR17 / DR49 / DR181 roadmap) · trade press · 2026-08-06 · https://quantumcomputingreport.com/d-wave-demonstrates-two-qubit-gate-breakthrough-for-dual-rail-erasure-qubits-in-nature/
[19] [C] Quantum Circuits · What are Quantum Circuits' dual-rail qubits and why are they a breakthrough? · company page · 2024-09-17 · https://quantumcircuits.com/dual-resonator-qubits-breakthrough/
[20] [C] Quantum Circuits · Quantum Circuits make error-detecting qubits (Aqumen Seeker, 8 dual-rail qubits) · company newsroom · 2024-11-19 · https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/
[21] [G] US Bureau of Industry and Security · Commerce Control List additions: controls on advanced technologies (ECCN 4A906, 3A904, 3B904) · Federal Register 2024-19633 · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[22] [P] quantumlib/Stim · Gate reference: HERALDED_ERASE · GitHub documentation · accessed 2026-09-03 · https://github.com/quantumlib/Stim/blob/main/doc/gates.md
[23] [G] USPTO (via Google Patents) · US 11,748,652 B1, Heralding of amplitude damping decay noise for quantum error correction, Amazon Technologies, Inc. (Kubica, Retzker; filed 2021-12-10) · granted 2023-09-05 · https://patents.google.com/patent/US11748652B1/en
[24] [G] USPTO (via Justia Patents) · US 12,288,135, Quantum information processing with an asymmetric error channel, Yale University (filed 2019-06-28) · granted 2025-04-29 · https://patents.justia.com/inventor/shruti-puri
[25] [G] DARPA · Quantum Benchmarking Initiative — Stage B selection · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[26] [C] D-Wave Quantum · D-Wave reports second quarter 2026 results · company press release · 2026-08-06 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/

## Open verification items

- Post-selected Pauli error of the 2026 dual-rail CZ: 0.029(6)% per gate (as cited from Nature 656, 47) versus "< 0.1%" in the arXiv abstract and "0.12% bound at depth" in the main report [D][11]; per-gate and depth-extrapolated figures, not reconciled in an accessible full text.
- Gate-level erasure fraction ≈80% for the cavity CZ is carried from the main report; the arXiv abstract states only ≈0.5% erasure per gate, so the fraction could not be re-derived from a primary source.
- PsiQuantum waveguide loss: 0.5 dB/m (main report) versus 1.8(2) dB/m for single-mode SiN (Nature) [D][12]; likely different waveguide classes, unresolved.
- Quandela's and QuiX's photonic qubit encoding is not stated on their public technology pages; both are path-encoded linear-optical by construction, but neither confirms "dual-rail" in a citable source, so no numbers are attributed to them.
- Quantum Circuits' claimed physical-to-logical overhead (reported elsewhere as 10–20 physical per logical) is not stated on the company's dual-rail explainer page [C][19]; no dated primary figure found.
- Dual-rail yield, cost per qubit and energy per qubit: not published by any actor, superconducting or photonic.
- Patent-family counts for dual-rail encodings: no named database gives a dated count; four individual patents or applications cited instead.
- OQC's erasure-qubit perspective [S][13] is a review by an industrial group, not a hardware commitment; OQC's Series C release names no dual-rail target [C][17].
- Cavity materials, quality factors and packaging for the 2026 Quantum Circuits device: not in the abstract; the full Nature text was not accessible.
- Funding attributable specifically to dual-rail programmes at AWS, SUSTech and Yale: undisclosed or not separable from the parent institution.
