---
id: majorana
name: Majorana parity (InAs–Pb tetron)
layer: "1 Carrier"
status: emerging
since: 2025
one_line: "Fermion parity stored non-locally in a gate-defined semiconductor–superconductor wire pair; only single-wire parity readout has been measured."
verdict: "No topological qubit exists as of 2026-09-03: one measured basis, no X-basis lifetime, no two-qubit operation, no independent replication of the topological claim."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

The carrier is the total fermion parity of two hybrid semiconductor–superconductor nanowires (a "tetron"), intended to be held non-locally in Majorana zero modes at the wire ends and so inaccessible to local perturbation. Kitaev proposed the one-dimensional p-wave chain in 2001; the Lutchyn/Oreg proximitised-nanowire recipe (2010) is what every device since has tried to realise; Microsoft's measurement-based architecture, where logic is parity measurement rather than braiding, is what these devices serve. Nothing in the record establishes that the measured parity is topologically protected.

Attributes (technology graph):
- a — affinity: fully fabricated (1.0); the object does not exist until an MBE stack and a gate pattern create it.
- b — characteristic time ≈ 1 µs; entangling operation deterministic (measurement-based, not heralded).
- c — readout: rf quantum-capacitance parity detection, ~100 µs, non-destructive, mid-circuit capable.
- d — mobility: static; the carrier is not transported.
- e — control: low-frequency gate voltages, electronics at room temperature.
- f — dominant error structure: unknown as the code sees it; no error model measured on a working qubit.
- g — manufacturing: molecular-beam epitaxy of III–V heterostructures.

## Physics & limits

The intended floor is exponential: a parity error requires a quasiparticle to cross between Majorana modes separated by many coherence lengths, so the rate should fall as exp(−L/ξ). That is the argument, not the demonstration. Two scales govern the devices: the induced gap, which sets the thermal quasiparticle population and is why lead replaced aluminium; and the hybridisation splitting, resolved on InAs–Pb to µeV precision from h/2e-periodic quantum-capacitance shifts [C][1].

Failure modes divide into quasiparticle poisoning — one unpaired fermion entering the island flips parity, which is what the ~20 s figure bounds — and dephasing between parity states, which is what an X-loop measures. The published asymmetry is the whole story: Z-loop 12.4 ms against X-loop 14.5 µs, roughly 1000× shorter [D][2]. Long Z with short X is equally consistent with a well-isolated charge island and says nothing about topology. With no X-loop re-measured on InAs–Pb, the physics that would move the floor — larger gap, lower disorder, longer wires — stays untested against the only discriminating observable.

## Engineering state of the art

Best demonstrated, 2026-06-02: a characteristic parity switching time of ~20 s, "with some instances reaching minute-scale", by interferometric single-shot parity measurement on **one hybrid nanowire of one tetron** in a multi-tetron array, InAs–Pb [C][1]. Typical at scale does not exist: no array yield, no assignment error, no X-loop lifetime, no two-qubit operation, no entanglement, no Bell test, no qubit T₁/T₂ [C][1][G:MSFT-MAJORANA-2026]. Microsoft's blog calls the 20 s a "qubit lifetime"; the preprint claims a parity lifetime in one wire [C][3].

**Records timeline**

| Date | Figure | Who | Tag+key |
|---|---|---|---|
| 2018-03-28, retracted 2021-03-08 | quantised 2e²/h Majorana conductance; recalibration moved plateaus 8%, points fell outside 2σ | Zhang et al. (Delft, Eindhoven, Microsoft) | [D][4] |
| 2023-03-01 | e/4 interference with the predicted even–odd effect at ν=5/2 and ν=7/2 | Nokia Bell Labs, PRX 13, 011028 | [D][5] |
| 2025-02 | single-shot parity readout, 1% assignment error, ms dwell times, InAs–Al | Microsoft, Nature | [D][6] |
| 2025-07 | tetron Z-loop 12.4 ms vs X-loop 14.5 µs | Microsoft, preprint | [D][2] |
| 2026 | Kitaev-chain parity readout > 1 ms | QuTech, Nature | [D][7] |
| 2026-06-02 | ~20 s parity switching, one wire of one InAs–Pb tetron | Microsoft, preprint | [C][1] |
| 2026-07-10 | coherent parity oscillations in coupled minimal Kitaev chains, "limited protection" | QuTech, preprint | [D][8] |

Dominant term of the error budget: unquantified. The only channel with a measured rate is the Z-basis parity flip; no budget attributing the X/Z ratio to disorder, hybridisation or readout back-action has been published.

## Manufacturing, materials & supply chain

The stack is MBE-grown InAs with an in-situ superconductor — now lead — patterned into tetrons by electrostatic gates. It is the least manufacturable process in the carrier layer: MBE throughput is wafers per day; the semiconductor–superconductor interface determines yield and has no published in-line metric; and the device is defined by gate tuning, so "yield" means the fraction of gate settings passing a screen — the contested Topological Gap Protocol [9].

No yield, uniformity, cost- or energy-per-qubit figure has been published for any Majorana device as of 2026-09-03. Microsoft moved fabrication capacity to Lyngby, Denmark, where the November 2025 opening was reported as enabling "the full fabrication of the Majorana chip core in Denmark", against cumulative Danish quantum-infrastructure investment above DKK 1 bn (≈ USD 156 M) [P][10]. GlobalFoundries lists topological among the modalities its Quantum Technology Solutions unit serves, with Microsoft Quantum named, but gives no wafer size, node or fab [C][11][G:GF-QTS-2026-05] — a captive research fab, not a foundry flow. Single points of failure: MBE tool supply, III–V source material, and the concentration of tetron know-how in one company and two university groups. No ECCN specific to Majorana devices was found.

## Control, readout & I/O burden

Control is DC-to-low-frequency gate voltages from room-temperature electronics plus rf readout lines; no per-qubit microwave drive, no laser — the architecture's genuine advantage. Readout is the gate operation: parity is inferred from an h/2e-periodic shift in the quantum capacitance of a dot coupled to the wire ends, non-destructively and mid-circuit, at ~100 µs (graph record). I/O scales with gates and resonators per tetron, both of order ten, so at 10³ tetrons the burden resembles a large spin-qubit array, addressable in principle by cryo-CMOS multiplexing. At 10⁴ and 10⁶ nothing can be said: no multiplexed Majorana-array readout is published, and no error model exists to set a latency requirement.

## Role in the stack

The node sits on one platform path, Topological (Majorana), with no off-diagonal reach: it requires III–V MBE heterostructures and provides the physical layer for the measurement-based Majorana gate, the fermion-parity (tetron) encoding and rf quantum-capacitance parity readout. It replaces and conflicts with nothing, because nothing depends on it. That isolation is the strategic fact: failure strands the branch with no partial credit — readout and MBE know-how transfer to hybrid-device physics, the encoding, gate set and error model nowhere.

Derived clock for the path = sum of the syndrome round: gate layers + transport + readout + reset: no code runs here, so only the ~100 µs parity-measurement term is defined and reset is unpublished, since logic *is* measurement and transport is absent — a design figure, not a demonstrated round. Neighbouring empty slots: a two-tetron joint-parity (X-type) measurement, and any decoder for a measured Majorana error model.

## Verification (QCVV)

The headline 20 s is a switching-time fit to a telegraph signal in one wire, not a randomised-benchmarking number, and has no companion in the conjugate basis: parity lifetime and qubit coherence are different quantities, and only the former was measured [C][1]. The February 2025 Nature paper carries an editor's note stating the results do not by themselves establish the presence of Majorana zero modes in the devices [D][6], [12].

Independent work does not replicate the claim. QuTech has shown Kitaev-chain parity readout beyond 1 ms [D][7] and, in July 2026, coherent parity oscillations in coupled minimal Kitaev chains while stating that "poor man's" Majoranas carry only limited protection [D][8]: replication of the technique, explicit non-replication of the protection.

Legg argues the Topological Gap Protocol can label the same region gapped or gapless depending on analysis choices such as field range and junction transparency, and that the conductance data show no clear gap [9]; it became a Nature Matters Arising in June 2026 with a multi-author Microsoft reply that concedes nothing [9], [13]. History is load-bearing: the 2018 "quantized Majorana conductance" Letter was retracted on 2021-03-08 after undisclosed charge-jump corrections, a mislabelled axis, and a recalibration moving plateau values by 8% that left points outside 2σ [D][4]. Only one group reports the headline numbers, so no value conflict arises.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| Microsoft Quantum | developer | US | Sole source of tetron devices and of every headline number; measurement-based architecture; 2029 fault-tolerance target | [C][1], [3][G:MSFT-MAJORANA-2026] |
| Microsoft Quantum Lab Lyngby | supplier (captive fab) | DK | Fabrication of the Majorana chip core; opened 2025-11-13 | [P][10] |
| QuTech | research | NL | Minimal Kitaev chains; independent parity readout and a coherent parity qubit with explicitly limited protection | [D][7], [8] |
| TU Eindhoven | supplier (materials) | NL | InSb/InAs nanowire growth feeding the Kitaev-chain devices | [D][8] |
| Nokia Bell Labs | developer | US | ν=5/2 fractional quantum Hall in GaAs, ~15×15 µm devices; target end-2026 for a topological qubit in superposition | [D][5][C][14][P][15] |
| DARPA | funder | US | Microsoft in the final US2QC phase since 2025-02; absent from QBI Stage B | [G][16][G:QBI-STAGEC-2026] |
| GlobalFoundries | supplier | US | Quantum Technology Solutions covers the topological modality; Microsoft Quantum a named partner | [C][11][G:GF-QTS-2026-05] |
| Atom Computing | partner (hedge) | US | Neutral-atom hardware for Microsoft's Magne logical-qubit machine — not topological | [G:MAGNE-2025-07] |
| QuNorth | user | DK | Bought Magne for €80 M, funded by EIFO and the Novo Nordisk Foundation | [G:MAGNE-2025-07] |
| H. F. Legg | critic | — | Matters Arising challenging the Topological Gap Protocol | [9] |

**Money.**
- 2025-02 · Microsoft · DARPA US2QC final phase (with PsiQuantum only) · amount not disclosed · DARPA · in progress [G][16][G:QBI-STAGEC-2026]
- 2025-07-17 · QuNorth · order for "Magne", 1,225 physical / 50 logical qubits · €80 M · EIFO + Novo Nordisk Foundation · ordered, delivery around the turn of 2026/27 [G:MAGNE-2025-07]
- 2025-11-06 · Microsoft · **not** selected for DARPA QBI Stage B (11 companies, up to $15 M each) · n/a · DARPA · confirmed absent [G:QBI-STAGEB-2025-11]
- 2025-11-13 · Microsoft · Lyngby lab opening; cumulative Danish quantum-infrastructure investment above DKK 1 bn (≈ USD 156 M) · announced [P][10]
- 2026-01-23 · Microsoft · Quantum Pioneers Program 2026, academic grants up to USD 200,000 per proposal, decisions 2026-03-15 · announced [P][17]
- 2026-05-12 · Microsoft · returning investor in Photonic Inc.'s $200 M round at a $2 B valuation · closed [G:PHOTONIC-200M-2026-05]
- 2026-05-21 · GlobalFoundries · CHIPS letter of intent covering a unit that lists topological · $375 M · US Dept of Commerce · LOI [C][11][G:GF-QTS-2026-05]
- Microsoft's topological R&D spend, headcount and Lyngby capex: not disclosed anywhere found.

**Market & supply chain.** Nobody sells equipment specific to this technology; inputs are general MBE tools, III–V substrates and standard dilution refrigerators. Concentration risk is total: one vendor, one captive fab, no merchant supply. Unit economics are unquotable — no device sold, no cloud access, no attributable revenue. Only G3 and G4 (early and large-scale fault tolerance) would pay for it; G1, G2, G5 and G7 are served by machines Microsoft buys from others, which the Magne order documents [G:MAGNE-2025-07].

**IP & standards.** No topological-specific patent count from a named database was found; the only dated figure is PatSnap's 1,175 Microsoft quantum patent families to 2026-06-30 [P][G:PATSNAP-2026-06], spanning all modalities. No litigation over Majorana device IP was found, and there is no standards body; the only openly published aligned stack is Microsoft's Q#/Azure Quantum Development Kit, whose instruction model presumes the architecture rather than validating it.

**Roadmaps & track record.** (promised on · promised for · status 2026-09-03): 2018-03 · quantised Majorana conductance · retracted 2021-03-08 [D][4]. 2025-02 · topological qubit demonstrated · contested, with a Nature editor's note [D][6], [12]. 2025 · "years, not decades" · superseded [C][3]. 2026-06 · 2029 fault tolerance · no two-qubit operation exists [C][3]. Nokia: end-2025 · Pauli-X control result · no publication found; end-2026 · qubit in superposition · outstanding [P][15]. Microsoft delivers excellent measurements on schedule and labels them with claims they do not support — consistent from 2018 to 2026; a 2029 date resting on zero demonstrated two-qubit physics is an intention, not a forecast. QuTech's statements have matched its data. Nokia's roadmap is too thinly published to judge.

**Strategic reading.** If it works, Microsoft owns a carrier no competitor can match by engineering alone, devaluing the rival capital stack at the physical layer. If it fails — the base case on today's evidence — Microsoft loses little: its delivery vehicle is other people's hardware plus its own error correction, which is why it bought Magne and invested in Photonic. Substitution runs the other way, as qLDPC codes erode the overhead argument that made topological qubits necessary. Supplier bargaining power is nil; platform-vendor power depends on whether a two-qubit result appears.

*Open niche:* the exploitable gap is that this modality has no QCVV. Every published number is a single-parameter fit to a telegraph trace, and no protocol distinguishes a topologically protected parity from a well-isolated charge island. A small group could define a discrimination test — a joint X/Z lifetime-ratio benchmark, a parity-readout assignment-error protocol with SPAM separation, or a disorder-robust successor to the Topological Gap Protocol — from published data plus simulation alone. SFQ competence matters later: non-destructive mid-circuit readout at ~100 µs is where millikelvin digital control removes room-temperature line count, and nobody is doing that here.

## Outlook & open questions

Falsifiable within 12–24 months. Confirm: an X-loop or joint-parity lifetime on InAs–Pb within two orders of magnitude of the Z-loop 20 s; any two-tetron measurement-based operation with a reported fidelity; independent reproduction of the InAs–Pb parity lifetime; Nokia publishing a ν=5/2 qubit in superposition, promised for end-2026 [P][15]. Demote: another year of Z-basis single-wire numbers only, or a second Matters Arising surviving reply.

Best case 2029: a few tetrons with balanced X/Z lifetimes and a two-qubit parity gate — a research device, not the promised fault-tolerant machine. Worst case: the InAs–Pb signal proves to be trivial Andreev states and the branch closes.

Open questions: why no X-loop number exists for the lead generation; what fraction of tetrons pass screening; how parity lifetime scales with wire length, the measurement that tests exponential protection directly; whether US2QC's final phase can be satisfied by a Z-only result; and whether Nokia's route, with its peer-reviewed non-Abelian interference signature [D][5], is the better-evidenced bet.

## Sources

[1] M. Aghaee *et al.*, “20 Second Parity Lifetime in an InAs–Pb Tetron Device,” [arXiv:2606.03884](https://arxiv.org/abs/2606.03884), Jun. 2026.
[2] M. Aghaee *et al.*, “Distinct Lifetimes for X and Z Loop Measurements in a Majorana Tetron Device,” [arXiv:2507.08795](https://arxiv.org/abs/2507.08795), Jul. 2025.
[3] C. Nayak, “Majorana 2 – Microsoft's Scalable Quantum Processor With Reliable, Long-Lasting Qubits,” Microsoft Quantum. [Online]. Available: https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor [C]
[4] H. Zhang *et al.*, “Quantized Majorana conductance,” *Nature*, vol. 556, no. 7699, pp. 74–79, Mar. 2018, doi: [10.1038/nature26142](https://doi.org/10.1038/nature26142). Retracted: *Nature*, vol. 591, p. E30, Mar. 2021, doi: [10.1038/s41586-021-03373-x](https://doi.org/10.1038/s41586-021-03373-x).
[5] R. L. Willett *et al.*, “Interference Measurements of Non-Abelian e/4 & Abelian e/2 Quasiparticle Braiding,” *Phys. Rev. X*, vol. 13, no. 1, Art. no. 011028, Mar. 2023, doi: [10.1103/PhysRevX.13.011028](https://doi.org/10.1103/PhysRevX.13.011028).
[6] Microsoft Azure Quantum, “Interferometric single-shot parity measurement in InAs–Al hybrid devices,” *Nature*, vol. 638, no. 8051, pp. 651–655, Feb. 2025, doi: [10.1038/s41586-024-08445-2](https://doi.org/10.1038/s41586-024-08445-2).
[7] N. van Loo *et al.*, “Single-shot parity readout of a minimal Kitaev chain,” *Nature*, vol. 650, no. 8101, pp. 334–339, Feb. 2026, doi: [10.1038/s41586-025-09927-7](https://doi.org/10.1038/s41586-025-09927-7).
[8] F. Zatelli *et al.*, “Majorana parity qubit in coupled minimal Kitaev chains,” [arXiv:2607.09511](https://arxiv.org/abs/2607.09511), Jul. 2026.
[9] H. F. Legg, “On the robustness of topological gap detection via transport,” *Nature*, vol. 654, no. 8120, pp. E22–E26, Jun. 2026, doi: [10.1038/s41586-026-10567-8](https://doi.org/10.1038/s41586-026-10567-8). [arXiv:2503.08944](https://arxiv.org/abs/2503.08944).
[10] M. Abdel-Kareem, “Microsoft Opens Largest Quantum Lab Globally in Denmark to Advance Topological Qubit Fabrication,” Quantum Computing Report, Nov. 13, 2025. [Online]. Available: https://quantumcomputingreport.com/microsoft-opens-largest-quantum-lab-globally-in-denmark-to-advance-topological-qubit-fabrication/ [P]
[11] GlobalFoundries, “GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing,” May 21, 2026. [Online]. Available: https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ [C]
[12] P. Ball, “Experts Weigh in on Microsoft's Topological Qubit Claim,” *Physics*, vol. 18, p. 57, 2025. [Online]. Available: https://physics.aps.org/articles/v18/57
[13] Microsoft Quantum, “Reply to: On the robustness of topological gap detection via transport,” *Nature*, vol. 654, no. 8120, pp. E27–E28, Jun. 2026, doi: [10.1038/s41586-026-10568-7](https://doi.org/10.1038/s41586-026-10568-7).
[14] Nokia Bell Labs, “Topological Quantum Computing,” Nokia.com, Feb. 24, 2025. [Online]. Available: https://www.nokia.com/bell-labs/research/air-lab/data-and-devices/topological-quantum-computing/ [C]
[15] J. Burt, “Bell Labs Takes A Topological Approach To Quantum 2.0,” The Next Platform, Jul. 21, 2025. [Online]. Available: https://www.nextplatform.com/2025/07/21/bell-labs-takes-a-topological-approach-to-quantum-2-0/ [P]
[16] DARPA, “DARPA selects two discrete utility-scale quantum computing approaches for evaluation,” Feb. 6, 2025. [Online]. Available: https://www.darpa.mil/news/2025/quantum-computing-approaches [G]
[17] M. U. Rehman, “Microsoft Opens 2026 Quantum Pioneers Program for Measurement-Based Topological Computing Research,” The Quantum Insider, Jan. 23, 2026. [Online]. Available: https://thequantuminsider.com/2026/01/23/microsoft-2026-quantum-pioneers-program-measurement-based-computing/ [P]
[18] P. R. Allison, “Bell Labs' Michael Eggleston on Nokia's research into topological quantum computing,” IT Pro, Apr. 28, 2026. [Online]. Available: https://www.itpro.com/technology/bell-labs-michael-eggleston-on-nokias-research-into-topological-quantum-computing [P]

## Open verification items
- Affiliation of H. F. Legg not confirmed in the arXiv text consulted; the Matters Arising author list and exact June 2026 day could not be established.
- The >1 ms figure for [7] is taken from the main report and is not verified against the paper.
- Assignment error, readout fidelity and device yield for the InAs–Pb generation: not reported in [1]; no source found.
- X-loop / joint-parity lifetime for InAs–Pb: no measurement published as of 2026-09-03.
- Microsoft topological R&D spend, Lyngby capex and headcount: not disclosed; the DKK 1 bn in [10] is total Danish quantum-infrastructure investment, not Microsoft's own outlay.
- DARPA US2QC contract value to Microsoft: not disclosed in [16].
- Export-control rules and ECCNs specific to Majorana or III–V superconducting hybrid devices: none identified.
- Nokia's claimed end-2025 Pauli-X control result: no publication or release found; [15], [18] are trade press.
- Nokia device size "15×15 µm" and the "hours to days" state stability come from [15] and [14], not from a peer-reviewed source.
- MBE tool vendor concentration asserted qualitatively; no dated market-share source consulted.
