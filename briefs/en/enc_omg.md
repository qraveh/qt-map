---
id: enc_omg
name: Metastable ("omg") erasure encoding
layer: "2 Encoding"
status: emerging
since: 2023
one_line: "Qubit lives in a metastable manifold so its dominant decay leaves the subspace detectably, converting Pauli errors into located erasures."
verdict: "Physics confirmed on atoms and ions, but measured conversion is 38–50%, not the 98% theory assumed, and no vendor ships it. Demote unless a >70%-conversion gate appears by end-2027."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An omg encoding places the computational basis inside a long-lived *metastable* manifold, chosen so the dominant decay takes the atom or ion *out* of the qubit subspace into a state a cycling transition lights up. The error is then not a Pauli flip on an unknown qubit but a heralded, located loss — an erasure.

The name is the ion-side blueprint: *optical–metastable–ground*, three manifolds in one species so one ion serves as qubit, ancilla and coolant (Allcock, Campbell, Chiaverini, Chuang, Hudson, Wineland and colleagues, 2021) [D][1]. Wu, Kolkowitz, Puri and Thompson made it quantitative for neutral atoms: 98% of ¹⁷¹Yb errors convertible, threshold rising from 0.937% under Pauli noise to 4.15% under erasure noise [S][2]. Kang, Campbell and Brown carried it to ions [S][3]. First hardware: Princeton, 2023 [D][4].

Attributes (technology graph): **a** carrier affinity 0.0, natural carriers. **b** no characteristic time, no entangling mechanism of its own. **c** no readout of its own; it delegates to the mid-circuit erasure check it enables. **d** no mobility. **e** no control modality or placement. **f** error structure as the code sees it: **erasure**. **g** no manufacturing. A hub in the strict sense, reaching both host families.

## Physics & limits

The mechanism is a hierarchy of lifetimes. In ¹⁷¹Yb the qubit is the nuclear spin of the 6s6p ³P₀ clock state; in ⁴⁰Ca⁺ two Zeeman sublevels of D₅/₂. Both live long against circuit duration and decay to the ground manifold, which scatters photons on a strong transition while the metastable one does not. A short fluorescence check therefore reports *which site* left the code space without touching those that stayed — Princeton measured the induced error on survivors below 10⁻⁵ [D][4].

The floor is set by errors that stay inside the manifold — Raman scattering back into the qubit subspace, magnetic dephasing across small Zeeman splittings, off-resonant coupling between the computational sublevels — all un-heralded Pauli noise. Oregon measured the split: ~94% of spontaneous Raman scattering and nearly all decay events detected, but only half the *total* error budget converted [D][5]; Princeton's [[4,2,2]] run converted 38(6)% [D][6]. Erasure buys more per unit rate — at 1% erasure the surface code tolerates 0.51% Pauli error, 5.2× the standard protocol [S][7][G:KUBICA-ERASURE-THRESH-2022] — but the gain scales with conversion fraction, so the residual is a floor only better gate physics removes.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: a two-qubit gate at 99.16% after erasure subtraction on ⁴⁰Ca⁺ [D][5], and a [[4,2,2]] block whose decay slows 1.9(4)× with erasure information [D][6]. Typical at scale: nothing — every shipped machine uses ground-manifold qubits.


**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2022-01 | 98% of ¹⁷¹Yb errors convertible; threshold 0.937% → 4.15% | Princeton | [S][2] |
| 2023-10 | Metastable ¹⁷¹Yb: 1Q 0.9990(1), CZ 0.980(1), check error <10⁻⁵ | Princeton | [D][4] |
| 2023-10 | ⁸⁸Sr Bell ≥0.9971 after erasure excision | Caltech | [D][8] |
| 2024-11 | ⁴⁰Ca⁺ Bell 97.73% raw → 99.16% erasure-subtracted, ≈400 µs | Oregon | [D][5] |
| 2026-06 | [[4,2,2]]: CZ 0.984(1), 38(6)% erasures, decay 1.9(4)× slower | Princeton | [D][6] |
| 2026-08 | Mid-circuit ground-state cooling and ancilla readout | Oregon | [D][9] |

The dominant term is the unconverted residual: half the ≈1.4% raw ⁴⁰Ca⁺ gate error survives the check [D][5], as does 62(6)% of a 1.6(1)% CZ error on ¹⁷¹Yb [D][6] — far worse than 99.854% raw on Harvard's Rb array [D][10] or 7.9×10⁻⁴ on Helios [D][11].

## Manufacturing, materials & supply chain

No fabrication step: the manufacturing attribute is "none" and the encoding rides whatever trap the host uses. What it changes is optics — a shelving/clock laser (578 nm for ¹⁷¹Yb, 674 nm for Ca⁺, 1762 nm for Ba⁺), repumps out of the manifold, and in Oregon's case a Raman pair at 976 nm detuned −43 THz, bought with power [D][5]. Suppliers are the field's usual set: Toptica, M Squared, Menlo Systems and NKT Photonics for sources; Stable Laser Systems for ultra-low-expansion cavities; Hamamatsu and Andor for check cameras. Single points of failure: the ULE cavity and the clock laser, both sub-ten-vendor markets. Export-control exposure runs through the lasers, not the encoding — Wassenaar Category 6 controls and the US BIS quantum rule of 2024-09-06 apply whichever manifold carries the qubit.

## Control, readout & I/O burden

Per-qubit line count is unchanged — the encoding's main commercial attraction. What grows is wavelength count and calibration: extra state preparation, a shelving fidelity, and a check whose false-positive rate feeds the decoder. The check's cost against the clock is the decisive number, and it is favourable on both hosts. Atom arrays already pay 0.5–1 ms imaging inside a 1–4.5 ms round [D][10][S][12], so a check that *is* the imaging is nearly free; ion machines run ~55 ms per layer [D][11], making a few-hundred-µs fluorescence check ~1% of it. Yale and AWS showed erasure qubits win only when check time is short against the cycle [S][13][G:YALE-IMPERFECT-CHECKS-2025] — here it is. The wall at 10³–10⁶ qubits is decoder bandwidth, not I/O: erasure flags roughly double the syndrome payload.

## Role in the stack

Two paths carry it: *Neutral atoms — alkaline-earth (Yb/Sr), erasure-native* (Atom Computing with Microsoft, Princeton, Caltech) and *Trapped ions — electronic gates, chip control* (IonQ with Oxford Ionics, eleQtron, Quantum Art). It **requires** an alkaline-earth atom or a trapped ion with an accessible metastable manifold; it **provides** the detectable-decay structure a mid-circuit erasure check consumes; it **replaces** ground-manifold hyperfine encoding. Switching costs a re-calibrated preparation and readout chain plus one or two lasers. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: **1.5×10⁻³ s** on the ion path (gate-set), where the encoding adds ≈1%, and **1.3×10⁻³ s** on the atom path (transport-set), where it adds nothing. A rare Layer-2 node with no clock penalty, so conversion fraction, not speed, is what to watch. Empty neighbouring slots: no erasure-native encoding for fabricated carriers, and no sub-100-µs erasure check for ions [D][9].

## Verification (QCVV)

Headline numbers come from Bell-state and randomised-benchmarking estimators with post-selection: shots where the check fired are discarded, so the "erasure-subtracted" fidelity is conditional — legitimate for a channel, illegitimate as a system figure of merit. Princeton's [[4,2,2]] result is the honest form: 1.9(4)× is logical, with erasure information actually used [D][6]. Not captured: the check's false-positive and false-negative rates, which can halve effective distance [S][13], and correlated leakage.

Conflicts. (i) The graph record records the [[4,2,2]] improvement as **3.6×**; arXiv:2506.13724 v1 and v2 both state **1.9(4)×**, which we use, treating 3.6× as superseded [G:PRINCETON-ERASURE-V2-2026-06]. (ii) Oregon's Bell fidelities read 98.56%/99.14% in the arXiv HTML and 98.61%/99.16% in Physical Review A, detuning −43 vs −44 THz; journal values used [D][5]. (iii) The 98% conversion figure [S][2] is an upper bound on an idealised error inventory, not a missed target.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Princeton | research | US | Originated Yb-171 metastable erasure conversion; [[4,2,2]] demo | [D][2], [4], [6] |
| University of Oregon | research | US | Only metastable-ion gate with erasure conversion; omg mid-circuit cooling | [D][5], [9] |
| Caltech | research | US | Sr Rydberg erasure excision | [D][8] |
| UCLA | research | US | omg blueprint co-author; metastable ion theory | [D][1], [3] |
| MIT Lincoln Laboratory | research | US | Blueprint co-author; single-ion spin-cat correction | [D][1], [14] |
| Duke | research | US | Surface-code comparison, ground vs metastable ions | [S][3] |
| Atom Computing | developer | US | ¹⁷¹Yb arrays, adoptable without changing species; QBI Stage B | [G:QBI-STAGEB-2025-11] |
| QuEra | developer | US | Rb arrays using atom loss, not metastable erasure | [C][G:QUERA-LIBRA-2026] |
| Infleqtion | developer | US | Sr/Rb arrays, 12 logical qubits with loss correction | [G:INFLEQTION-NYSE-2026-02] |
| IonQ | developer | US | Laser-free gates remove the error omg heralds | [D][15][G:IONQ-OXIONICS-2025] |
| Quantinuum | developer | US | Ba⁺ Helios; natural omg host, no metastable programme | [D][11] |
| Microsoft | user | US | Sells Magne with Atom Computing; erasure-aware decoding | [G:MAGNE-2025-07] |

**Money.** No financing event is earmarked for metastable encoding; this money buys the host platforms.
- 2025-09-17 · IonQ · M&A, Oxford Ionics · $1.075 B · announced 2025-06-09 · closed [G:IONQ-OXIONICS-2025]
- 2025-11-04 · US DOE · five National QIS Research Centers renewed · $625 M / five years · closed [G:DOE-NQISRC-2025-11]
- 2025-11-06 · DARPA · QBI Stage B, 11 teams incl. Atom Computing, QuEra, IonQ · ≤$15 M each · selected [G:QBI-STAGEB-2025-11]
- 2026-02-17 · Infleqtion · IPO, NYSE (INFQ) · >$550 M gross · closed [G:INFLEQTION-NYSE-2026-02]
- 2026-04-27 · Quantum Art · Series A extension · $140 M · closed [P][16]
- 2026-05-21 · US Dept of Commerce · CHIPS LOIs, Atom Computing $100 M, Infleqtion $100 M · $2.013 B total · non-binding [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · Series C plus DoC LOI · >$300 M cumulative · Third Point · closed + LOI [C][17][G:ATOM-300M-2026-06]
- 2026-06 · Quantinuum · IPO, Nasdaq (QNT) · $1.68 B · after $600 M at $10 B pre-money · closed [G][18]
- 2026-07 · IonQ · M&A, SkyWater Technology · $1.8 B · closed [G][19]
- 2026-08-28 · Pasqal · SPAC completion · ~$360 M cash · €16.5 M 2025 revenue · closed [P][20]

**Market & supply chain.** No one sells an omg product; the enabling lasers, cavities and cameras are already a dependency of every host platform, so adoption adds one or two laser channels against systems like Magne (€80 M, 50 logical) [G:MAGNE-2025-07]. Only **G3** and **G4** (early and large-scale fault tolerance) pay for it; **G1** benefits marginally via erasure excision in simulators [D][8]. G2 and G5–G7 do not.

**IP & standards.** No patent family specific to metastable erasure encoding was found in a named database as of 3 Sep 2026; nearest granted art is Amazon Technologies US 11,748,652 B1 on heralded amplitude-damping decay (2023-09-05) [G:AMZN-ERASURE-PATENT]. No litigation, no standards body; Stim models the encoding in software [C][21].

**Roadmaps & track record.** (2021 · omg blueprint · partly delivered — Oregon entanglement 2024 [D][5], mid-circuit cooling 2026 [D][9]; no product.) (2022-01 · 98% conversion · missed by 2.6×, 38(6)% measured [D][6].) (2028 · QuEra Libra >256 logical · on roadmap, no metastable commitment [G:QUERA-LIBRA-2026].) (2026/27 · Magne 50 logical · installing, ground-manifold Yb [G:MAGNE-2025-07].) The vendors made no omg promises to break.

**Strategic reading.** Winners would be alkaline-earth atom vendors and ion vendors still using laser gates; losers, decoder stacks tuned for Pauli noise. Substitution bites from both sides: atom loss is >80% of array leakage and Harvard detected it on ground-manifold Rb for 2.14(13)× below threshold [D][10], while laser-free ion gates at 8.4×10⁻⁵ delete the error omg catches [D][15].

*Open niche:* a small QCVV/SFQ research company plugs in at the check, not the qubit. Everything unmeasured here is metrology — false-positive and false-negative rates of the check, correlated leakage across sites, and the conversion fraction under a full circuit. A certified-interval estimator for it has no incumbent, and a cryogenic SFQ pre-decoder compressing erasure flags at the camera is a defensible niche.

## Outlook & open questions

**Confirm** if a gate reports >70% of total error converted with residual below 3×10⁻³, or a vendor announces a metastable product line. **Demote** if no conversion fraction above 50% is published by end-2027, or a laser-free ion gate below 10⁻⁴ ships at scale. Best case by 2029: an alkaline-earth array runs a distance-5 code with erasure-aware decoding and reports Λ above the loss-only baseline. Worst case: atom loss remains the only erasure anyone needs and this stays a two-laboratory programme.

Open questions. (1) Why is measured conversion 38–50% when the model says 98% — gate, check, or error inventory? (2) Does erasure information still help once false negatives are folded in at distance ≥5? (3) Is the residual Pauli error set by sublevel choice or by the gate laser? (4) Can a metastable ancilla be read non-destructively inside a 1 ms atom cycle? Watch the next Princeton follow-up, whether Atom Computing exposes the metastable manifold, and whether Quantinuum's unpublished "novel code family" is erasure-structured.


## Sources

[1] D. T. C. Allcock *et al.*, “omg blueprint for trapped ion quantum computing with metastable states,” *Appl. Phys. Lett.*, vol. 119, no. 21, Art. no. 214002, Nov. 2021, doi: [10.1063/5.0069544](https://doi.org/10.1063/5.0069544). [arXiv:2109.01272](https://arxiv.org/abs/2109.01272).
[2] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540).
[3] M. Kang, W. C. Campbell, and K. R. Brown, “Quantum Error Correction with Metastable States of Trapped Ions Using Erasure Conversion,” *PRX Quantum*, vol. 4, no. 2, Art. no. 020358, Jun. 2023, doi: [10.1103/PRXQuantum.4.020358](https://doi.org/10.1103/PRXQuantum.4.020358). [arXiv:2210.15024](https://arxiv.org/abs/2210.15024).
[4] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493).
[5] A. Quinn *et al.*, “High-fidelity entanglement of metastable trapped-ion qubits with integrated erasure conversion,” *Phys. Rev. A*, vol. 113, no. 4, Art. no. L040601, Apr. 2026, doi: [10.1103/p3cy-8yjk](https://doi.org/10.1103/p3cy-8yjk). [arXiv:2411.12727](https://arxiv.org/abs/2411.12727).
[6] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0).
[7] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461).
[8] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406).
[9] S. Brudney *et al.*, “Mid-circuit ground-state cooling and ancilla readout in the omg architecture,” [arXiv:2608.13181](https://arxiv.org/abs/2608.13181), Aug. 2026.
[10] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661).
[11] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465).
[12] H. Zhou *et al.*, “Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays,” *Proc. 52nd Annu. Int. Symp. Comput. Archit. (ISCA)*, 2025, doi: [10.1145/3695053.3731039](https://doi.org/10.1145/3695053.3731039). [arXiv:2505.15907](https://arxiv.org/abs/2505.15907).
[13] K. Chang *et al.*, “Surface Code with Imperfect Erasure Checks,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040355, Dec. 2025, doi: [10.1103/d1v7-nctj](https://doi.org/10.1103/d1v7-nctj).
[14] K. DeBry *et al.*, “Error correction of a logical qubit encoded in a single atomic ion,” *Nat. Phys.*, vol. 22, no. 9, pp. 1446–1452, Sep. 2026, doi: [10.1038/s41567-026-03315-2](https://doi.org/10.1038/s41567-026-03315-2).
[15] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025.
[16] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[17] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[18] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[20] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[21] Google Quantum AI, “Stim, heralded-erasure noise channels,” open source. [Online]. Available: https://github.com/quantumlib/Stim [C]

## Open verification items

- Exact Applied Physics Letters volume, page and month for the 2021 omg blueprint [1] — cited from a laboratory publications listing; the journal record itself was not consulted.
- Metastable-manifold lifetimes used as the physical premise (¹⁷¹Yb 6s6p ³P₀, ⁴⁰Ca⁺ D₅/₂) — stated qualitatively; no numeric lifetime verified here.
- Oregon Bell fidelities conflict: 98.56%/99.14% (arXiv HTML) vs 98.61%/99.16% (Physical Review A abstract), detuning −43 vs −44 THz; journal values used [5].
- Princeton [[4,2,2]] logical-decay improvement: graph record says 3.6×, arXiv v1 and v2 both say 1.9(4)×; 1.9(4)× used, Nature Physics main text not accessible to confirm [6].
- Erasure-check false-positive and false-negative rates for both the ¹⁷¹Yb and ⁴⁰Ca⁺ demonstrations — not published in the abstracts consulted.
- Duration and fidelity of Oregon's quantum-logic non-destructive metastable readout [9] — no timing given.
- Exact ECCN mapping of the US BIS quantum interim final rule of 2024-09-06 to metastable-qubit hardware — not verified.
