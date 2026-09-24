---
id: fab_sc
name: Superconducting-qubit lithography (Nb/Al JJ, 300 mm)
layer: "10 Manufacturing"
status: demonstrated
since: 2007
one_line: "300 mm junction lithography and post-fab trimming set the frequency spread every superconducting path inherits."
verdict: "Real: 300 mm optical lithography yields 393/400 qubits at ~8% junction-resistance spread; trimming lands 97.4% on target. Anderon is an LOI — demote if no non-IBM wafer ships by end-2027."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A Josephson junction is two superconductors across a ~1–2 nm oxide barrier whose area and oxidation fix the critical current and hence the qubit frequency. This node is the process patterning those junctions and their niobium wiring at wafer scale — not a qubit. Lineage: e-beam Dolan-bridge Al/AlOx/Al junctions from the 2007 transmon (Koch et al., Yale), then 193 nm immersion lithography and etch on CMOS lines [D][1].

Attributes. **Carrier affinity 1.0** — fully fabricated: the manufacturing step itself, with no carrier, mobility, readout or control. **Manufacturing** — Nb wiring and Al/AlOx junctions on 200→300 mm silicon or sapphire; the error passed downstream is coherent (frequency offset, collision), not stochastic.

## Physics & limits

Ambegaokar–Baratoff ties critical current to normal-state resistance, and $f_{01}\approx(\sqrt{8E_JE_C}-E_C)/h$, so $R_n$ spread reaches frequency at half weight. imec measured ~8% RSD in junction resistance across a 300 mm wafer (7,872 test structures), ~4% within a die, and 5–7% RSD in qubit frequency [D][1]. That is a lattice problem, not a device problem: fixed-frequency neighbours must clear collision windows tens of MHz wide on a ~5 GHz qubit, so 5% spread (≈250 MHz, 1σ) leaves no collision-free yield at lattice scale. Trimming is a precondition, not an optimisation — alternating-bias assisted annealing moves junction resistance >70% and lands 97.4% of junctions on target [D][2].

The second floor is dielectric loss: amorphous AlOx and interface oxides host two-level systems capping $T_1$ in the tens-to-low-hundreds of µs. imec's 300 mm devices give median $T_1$ 75 µs, best 161 µs, best $T_{2e}$ 245 µs, over a 42–113 µs centre-to-edge gradient that is a process signature, not scatter [D][1]. TLS drift hourly, and quasiparticle bursts set a floor lithography cannot touch [D][G:WILLOW-QEC-2024-12]. What moves it: epitaxial barriers, Ta/Nb base metal, tuneable couplers.

## Engineering state of the art

Best on a genuine 300 mm CMOS line: 393 of 400 qubits functional [D][1] — but at the frequency spread above, so trimming or tuneability is still required downstream.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-08 | ABAA trimming: 97.4% targeting success, >70% tuning range | Rigetti | [D][2] |
| 2024-09 | 300 mm optical-litho transmons: 393/400 functional, median $T_1$ 75 µs, 8% RSD $R_n$ | imec | [D][1] |
| 2025-11 | Loon on 300 mm Albany: c-couplers, multilayer low-loss routing | IBM | [C][3] |
| 2026-02 | Wafer-scale package: >500 qubits per 3-inch sapphire die, readout 97.5% median (n=54) | OQC | [P][4] |
| 2026-05 | Anderon, pure-play 300 mm quantum foundry: $1 B CHIPS + $1 B IBM | IBM / US DoC | [G][5] |

Dominant error term: coherent frequency error — spread, collisions, drift. TLS-limited $T_1$ is what the process cannot remove.

## Manufacturing, materials & supply chain

Dolan-bridge shadow evaporation still produces most published qubits; the CMOS route means 193i patterning, RIE, Nb wiring, TSVs, bump bonds. Its advantage is statistics and throughput, not coherence: imec's median $T_1$ matches e-beam devices, its metrology does not. Trade press claims ~30× device output versus 200 mm; IBM's release states no multiple [P][6]. Tooling is unremarkable, so the scarce asset is recipe and trimming capability; single points of failure are refrigerator capacity, high-resistivity silicon and sapphire, and Nb etch expertise shared with the SFQ chain. Cost per wafer is not quotable. Export exposure is indirect: the BIS rule of 2024-09-06 controls cryogenic wafer probers (3B904), sub-4.5 K cryogenic electronics (3A901) and ≥34-qubit machines (4A906), but no ECCN names junction lithography [G][7].

## Control, readout & I/O burden

No control or readout of its own; it sets the ceiling others hit, through escape density and frequency targeting. OQC's package is the current bound: >500 qubits on one die, out-of-plane coax, no wire bonds, 56 nine-to-one readout multiplexing cells — and no per-qubit control lines as measured [P][4], so it is a packaging result, not a processor. At 10³ per die the constraint is collisions; at 10⁴ escape density and routing, what Loon targets [C][3]; at 10⁶ no fabricated design exists.

## Role in the stack

Root node of the superconducting family: it requires nothing upstream and provides for transmon, fluxonium and the rf-SQUID flux qubit, plus long-range c-couplers, millikelvin SFQ control, flux-DAC multiplexing, multi-chip modules with l-couplers, and cryogenic microwave links. Paths served: transmon, bosonic cat/GKP, dual-rail erasure, annealing. It replaces 3D integration in the planar-versus-stacked trade. Fan-in is zero, so it is no hub, yet its fan-out is the family's widest and every downstream node inherits its spread and yield. It adds nothing to the derived clock (derived clock = sum of the syndrome round: gate layers + transport + readout + reset, 0.65 µs on the superconducting path) but bounds how many qubits reach it.

## Verification (QCVV)

Frequency is predicted from junction resistance via Ambegaokar–Baratoff, then confirmed spectroscopically after packaging, so the statistic that matters is $R_n$ RSD — published by nobody except imec [D][1]. RB, XEB and cycle benchmarking measure a calibrated lattice, blind to dies discarded and pre-trim collision rates. ABAA's 97.4% is a targeting-success rate from an optimised study, not a worst-case bound [D][2]. OQC's numbers are sub-sampled: readout over 54 of >500 sites, 105/108 operational on the characterised subset [P][4]. Conflict: the quoted "~100 µs median" resolves to $T_1$ ~97 µs and $T_{2e}$ ~129 µs, reported separately.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Anderon | supplier | US | Proposed pure-play 300 mm quantum wafer foundry | [G][5] |
| IBM | developer | US | Fabricates Nighthawk and Loon on 300 mm Albany | [C][3] |
| imec | research | BE | 300 mm optical-litho transmons, published yield | [D][1] |
| Rigetti | developer | US | ABAA junction trimming on its own line | [D][2] |
| OQC | developer | UK | Wafer-scale package, >500 qubits per die | [P][4] |
| GlobalFoundries | supplier | US | $375 M CHIPS LOI, multi-modality foundry | [G][8] |
| US Dept of Commerce | regulator | US | CHIPS letters of intent, $2.013 B | [G][8] |

**Money.**
- 2026-05-21 · Anderon · CHIPS LOI plus IBM equity · $1 B CHIPS + $1 B IBM cash and IP · US Dept of Commerce · within $2.013 B across nine firms · LOI, unexecuted [G][5][G:CHIPS-LOI-2026-05]
- 2026-05-21 · GlobalFoundries · CHIPS LOI, multi-modality foundry · $375 M · US Dept of Commerce · — · LOI [G][8]
- 2026-06-02 · IBM · commitment, quantum overall · >$10 B / 5 yr · — · announced [C][9]
- 2026-08-26 · IBM · HRL acquisition completed, naming an Anderon collaboration · undisclosed · — · completed [C][10]

**Market & supply chain.** No merchant superconducting-qubit foundry operates as of 4 Sep 2026: every 300 mm line with published qubit data is captive (IBM Albany, Google Santa Barbara [P][11]) or a research pilot (imec), and the proposed merchant line is funded by its prospective customers' largest competitor. Binding scarcities are refrigerator capacity and process know-how, not tools; unit economics are not quotable. G3 and G4 pay directly, G7 indirectly; G1, G2, G5, G6 fund nothing.

**IP & standards.** PatSnap counts to 2026-06-30 give IBM 783 and Google 357 families in superconducting devices (IPC H10N 60) [P][G:PATSNAP-2026-06][12]. No patent family specific to 300 mm junction lithography carries a named assignee and year; no standards body governs these processes.

**Roadmaps & track record.** Anderon (promised 2026-05-21 · foundry serving vendors worldwide · status 2026-09-03: LOI only, yet IBM's 2026-08-26 release calls it "its quantum wafer foundry") [G][5][C][10]. Rigetti/ABAA (2024-08 · production frequency targeting · in use under the 108-qubit product, whose 99.5% two-qubit target slipped to "later 2026") [D][2][C][13]. IBM's fabrication milestones land on schedule; its merchant-access promise has no record.

**Strategic reading.** If 300 mm superconducting fab scales, IBM wins twice — vertically integrated, and landlord to everyone else's capacity. Fabless vendors win only with a neutral foundry, which does not exist. Losers are vendors whose differentiator is fabrication skill, not architecture. The threat is capture, not substitution: every superconducting path needs this node, and equipment suppliers have no bargaining power against its owner.

*Open niche:* a small QCVV/SFQ research company can plug in at the measurement nobody publishes — cross-line frequency targeting and collision statistics. Verifying ABAA-class claims and comparing $R_n$ RSD across foundries needs metrology, not fab access.

## Outlook & open questions

Confirm by end-2027 if Anderon executes definitive CHIPS documents and fabricates for a named non-IBM customer; demote the merchant-foundry framing if only IBM designs emerge. Best case by 2029: two or more independent 300 mm lines with published cross-foundry uniformity and post-trim residuals below 1% frequency RSD. Worst case: Anderon stays captive. Open questions: does any line publish post-trim collision yield; can epitaxial barriers lift median $T_1$ above 200 µs; does a merchant European or Asian line emerge?

## Sources

[1] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[2] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[3] IBM, “IBM Delivers New Quantum Processors, Software, and Algorithm Breakthroughs on Path to Advantage and Fault Tolerance,” Nov. 12, 2025. [Online]. Available: https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance [C]
[4] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [P]
[5] IBM, “IBM and U.S. Department of Commerce Announce America's First Purpose-Built Quantum Foundry, Supported by Proposed $1 Billion CHIPS Award,” May 21, 2026. [Online]. Available: https://newsroom.ibm.com/ibm-and-u-s-department-of-commerce-announce-americas-first-purpose-built-quantum-foundry [G]
[6] L. James, “IBM spins off America's first quantum chip foundry with $2 billion in federal and private funding — newly-minted 'Anderon' foundry to offer 300mm quantum wafer fab and manufacturing services,” Tom's Hardware, May 26, 2026. [Online]. Available: https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding [P]
[7] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[8] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[9] IBM Quantum, “Why IBM is investing $10 billion into quantum computing,” Jun. 2, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/10-billion-investment-faq [C]
[10] IBM, “IBM Completes Acquisition of HRL Laboratories to Accelerate the Future of Quantum,” Aug. 26, 2026. [Online]. Available: https://newsroom.ibm.com/2026-08-26-ibm-completes-acquisition-of-hrl-laboratories-to-accelerate-the-future-of-quantum [C]
[11] I. Hamm, “Google Buys 83,000-Square-Foot Campus in Goleta for $32.5M,” The Santa Barbara Independent, Aug. 24, 2026. [Online]. Available: https://www.independent.com/2026/08/24/google-buys-83000-square-foot-campus-in-goleta-for-32-5m/ [P]
[12] PatSnap, “Quantum Error Correction Technology Landscape 2026,” Apr. 22, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/articles/quantum-error-correction-patent-landscape-2026/ [P]
[13] Rigetti Computing, Inc., “Rigetti Announces General Availability of 108-Qubit System,” Apr. 7, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system [C]

## Open verification items

- Anderon's contractual status: IBM's 2026-05-21 release states an LOI subject to execution of definitive documents; no execution confirmed by 4 Sep 2026, yet IBM's 2026-08-26 HRL release already calls Anderon "its quantum wafer foundry".
- "≈30× device output versus 200 mm" appears only in trade press [6]; IBM's own release states no multiple.
- No per-wafer or per-qubit cost figure exists for any 300 mm superconducting-qubit line.
- No dated patent family specific to Nb/Al junction lithography at 300 mm was found; the PatSnap H10N 60 counts are portfolio-wide and carried by no public URL of their own.
- Google's Goleta purchase is not stated to be fab capacity; the fab reading is inferential.
- imec's 300 mm devices use Al/AlOx/Al overlap junctions; whether that line's Nb wiring stack matches IBM's approach is not established by the sources consulted.
