---
id: code_surface
name: Rotated surface code (+ yoked variants)
layer: 7 Code
status: demonstrated
since: 2023
one_line: Weight-4 CSS stabilizer code on a square lattice; the only code with below-threshold hardware data on three platforms, and the most expensive.
verdict: The default code because it needs nothing but a static degree-4 lattice; at Λ ≈ 2 it costs 600–1,500 physical per logical. Demote if a qLDPC memory beats it on hardware before end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

A CSS stabilizer code: weight-4 X and Z plaquettes on a square lattice, weight-2 on the boundary. The rotated layout — the one everybody builds — puts one logical qubit in d² data and d²−1 measure qubits: a distance-7 patch is 97 physical qubits. Errors show up as pairs of syndrome defects, which a decoder pairs across a three-dimensional matching graph (two space dimensions, d rounds) into a Pauli frame. Lineage: Kitaev's toric code (1997) [S][487]; the planar memory and its threshold in Dennis, Kitaev, Landahl and Preskill (2002) [S][488]; the rotated d²-qubit layout in Bombín and Martín-Delgado (2007) [S][489]; lattice surgery in Horsman et al. (2011) [S][490]; the engineering canon in Fowler et al. (2012) [S][491]; yoking in Gidney et al. (2023) [S][492].

Attributes from the technology graph (a affinity; b time; c readout; d mobility; e control @ placement; f error structure as the code sees it; g manufacturing): a = 0.5, carrier-agnostic — a layout, not a device, with b and c inherited from the host and e, g none of its own; d = static, patches moving only by lattice surgery; f = Pauli, the defining assumption and the defining weakness, since whatever is not an X/Z flip — leakage, loss, bias, erasure — is discarded information or unmodelled damage. Rank 7 of 96; a hub reaching superconducting, neutral-atom and spin families.

## Physics & limits

The code turns a physical error rate p into a logical rate falling exponentially in d, while p sits below a threshold. Λ, the factor by which logical error drops per two distance steps, is the whole economics: at Λ = 2.14 a decade of logical fidelity costs seven distance steps, an order of magnitude in qubits. The threshold is decoder- and noise-dependent: 0.937% under uniform circuit-level depolarizing noise [S][8], but 0.55% for Riverlane's unweighted hardware decoder against 0.7% for weighted matching under leakage [D][199]. Every quoted Λ describes a decoder as much as a chip.

Three floors are intrinsic. Area and time: a logical qubit is 2d²−1 physical qubits and a logical operation costs d rounds, so from 7.72×10⁻⁴ at d=7 with Λ ≈ 2 [D][2], reaching 10⁻⁶ needs d ≈ 25 and over 1,200 physical per logical unless p falls below 10⁻³; at p = 10⁻³ the teraquop footprint is about 1,500 physical per logical plain, 800 with one-dimensional and 600 with two-dimensional yokes [S][492], or about 650 plain with correlated matching [S][493]. Non-Pauli errors: leakage produces syndromes matching cannot explain, and atom loss is tractable only if the decoder is told where it happened. Correlated bursts: Google sees events roughly hourly pinning a floor near 10⁻¹⁰ irrespective of d [D][1]. What moves the floor is error-structure engineering — bias, erasure, leakage removal — exactly what this code discards; yokes move only the constant.

## Engineering state of the art

Best demonstrated as of 3 Sep 2026: distance-7 memory at 7.72×10⁻⁴ logical error per cycle on Google's 105-qubit Willow, with reinforcement-learning calibration inside the QEC loop [D][2]. Typical at scale: nothing. No vendor sells a surface-code logical qubit; logical two-qubit gates exist only at d=3 [D][42]; on atoms the code ran on 448 atoms for four rounds [D][4].

| Year | Figure | Who | Tag | Src |
|---|---|---|---|---|
| 2023-02 | d=5 at 2.914(16)%/cycle vs d=3 average 3.028(23)% | Google | [D] | [494] |
| 2024-12 | Λ = 2.14 ± 0.02 (d=3→5→7); d=7 at 0.143(3)%/cycle; 2.4(3)× the best physical qubit; 10⁶ cycles at d=5 | Google (Willow) | [D] | [1] |
| 2025-11 | 448 atoms: 2.14(13)× over d=3→5 in four rounds; loss-aware ML decoding worth 1.73(13)× | Harvard/MIT/QuEra | [D] | [4] |
| 2025-12 | Local Clustering Decoder under 1 µs/round on FPGA to d=17; 4× qubit saving (d=33→17) under leakage | Riverlane | [D] | [199] |
| 2025-12 | 107-qubit device below threshold at d=7, Λ = 1.40(6) | USTC | [D] | [3] |
| 2026-07 | Logical CNOT between two d=3 patches, fidelity 0.643, no post-selection | USTC | [D] | [42] |

Dominant term: two-qubit gate error, about 40% of the comparable colour-code budget on the same chip [D][40], then leakage and readout, then bursts no larger d removes [D][1].

## Manufacturing, materials & supply chain

The code has no fabrication of its own; it imposes one — a static degree-4 lattice, a measure qubit between every data pair, non-destructive mid-circuit readout on every ancilla, and uniformity, because all 2d²−1 qubits must work. That is a yield problem in d², and why Google patented variants tolerating dead qubits [G][495]. Its real supply chain is the decoding chain: Riverlane's decoder takes about 6% of a Xilinx VU19P's logic at d=17 [D][199], and that FPGA family is single-source (AMD), as is the GPU alternative (NVIDIA, 3.84 µs round trip over NVQLink [G:NVQLINK-2025]). Cost per logical qubit is unpublished. Export exposure: the US BIS rule of 2024-09-06 [G:BIS-QUANTUM-2024] controls quantum computers at a 34-qubit floor with error-rate tiers (4A906) — a distance-5 patch, 49 qubits, clears it — and refrigerators (3A904).

## Control, readout & I/O burden

Every cycle measures and resets every ancilla: on Willow, 48 measurement bits per 1.1 µs for a distance-7 patch, roughly 44 Mbit/s of syndrome per logical qubit [D][1]. The decoder must consume that stream faster than it arrives or the backlog diverges — sub-microsecond per round in FPGA fabric [D][199] against Google's 63 µs mean latency at d=5 in 2024 [D][1]. At 10³ qubits the wall is per-qubit wiring; at 10⁴ it is syndrome bandwidth off the fridge, the case for cold-stage predecoding (a cryo-CMOS study claims 3,780× reduction under 0.56 mW at 4 K [S][G:PINBALL-2025-12]); at 10⁶ decoding is a datacentre-scale streaming problem sized by syndrome rate, not qubit count.

## Role in the stack

Five platform paths carry it: superconducting transmons, alkali neutral atoms, alkaline-earth erasure-native atoms, silicon/germanium quantum-dot spins and donor spins in silicon. It requires only a static nearest-neighbour lattice — the reason it is the default — hosts magic-state factories (cultivation reaches 0.9999(1) at 8% acceptance [D][41]) and feeds FPGA and neural decoders [D][199], [496]. It is replaced by, not composed with, the colour code (better gates, worse slope: Λ₃/₅ = 1.56 on the same chip [D][40]), bivariate-bicycle qLDPC codes (288 physical for 12 logical against roughly 3,000 surface-code qubits [D][227]) and high-rate transversal codes on movable atoms. It conflicts with cat qubits (an unbiased code wastes the bias), dual-rail encodings (matching discards erasure flags) and destructive detection. Switching costs run both ways: leaving buys a 3–10× overhead cut and demands connectivity the hardware lacks; staying costs 600–1,500 physical per logical [S][492]. Hub reading: the one genuinely platform-agnostic code-layer node, which is why a decoder company can exist. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset: 0.65 µs derived on the superconducting path against the measured 1.1 µs cycle, readout and reset two-thirds of it rather than the 25–40 ns gates [D][1]; 1.31 ms on atoms, set by transport. Neighbouring empty slots: a decoder inside the fridge, and cross-module patches — no code has run across two modules.

## Verification (QCVV)

Λ is a fit of logical error per cycle against d, and three things make it soft. Decoder-conditioned: the same Sycamore data gives 3.028% under tensor-network decoding and 2.901% under AlphaQubit at d=3 [D][494], [496]. Subset-conditioned: a d=7 patch adds worse qubits to the d=5 set. Duration-conditioned: four-round circuits [D][4] never see the drift and burst physics a 10⁶-cycle run does [D][1]. Not captured: leakage populations, bursts, reload survival bias, decoder failure in real time. Replicated independently — Google [D][1], [2], USTC [D][3], Harvard/MIT/QuEra [D][4].

Conflicts. Λ per two distance steps: 2.14 ± 0.02 (Google, d=3→7) [D][1] versus 1.40(6) (USTC) [D][3] versus 2.14(13)× (atoms, four rounds, lost on reloading) [D][4] — different noise, not different codes, and only Google's survives a million cycles. Threshold: 0.937% [S][8] versus 0.55–0.7% under leakage [D][199]; budget against the second.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | Willow memory to d=7, the d=7 record, AlphaQubit, yoked-code theory | [D][1], [2], [496] [S][492] |
| IBM | developer | US | Ran surface codes on Heron; roadmap leaves them for bivariate-bicycle qLDPC on overhead grounds | [D][227] [G:IBM-ROADMAP] |
| Riverlane | supplier | UK | Only pure-play QEC vendor; Local Clustering Decoder, sub-µs per round on FPGA | [D][199] [C][497] |
| Harvard/MIT + QuEra | research + developer | US | Surface code on 448 atoms with loss-aware ML decoding | [D][4] [G:QUERA-230M-2025] |
| USTC, Zhejiang University | research | China | d=7 below threshold; logical CNOT at d=3; 125-qubit lattice surgery | [D][3], [42], [43] |
| NVIDIA, Qblox | suppliers | US, NL | NVQLink and control stacks that close the decode loop in real time | [G:NVQLINK-2025] [C][498] |

**Money.** Nobody funds a code; these are deliverables denominated in surface-code units.
- 2024-05-01 · Riverlane · Horizon Europe EIC Transition grant (SkyTALE, with Qblox) · £2.1 M · awarded [C][499]
- 2024-08-06 · Riverlane · Series C · $75 M · Planet First Partners lead, with ETF Partners, EDBI, Cambridge Innovation Capital, Amadeus · closed [C][500]
- 2025-11-06 · DARPA · QBI Stage B · up to $15 M each, eleven teams; IBM the only transmon vendor, its plan qLDPC [G:QBI-STAGEB-2025-11]
- 2026-03-12 · Riverlane · roadmap release claims $120 M+ raised and an "$85 M" Series C · conflicts with the 2024 release [C][497]
- 2026-06-02 · IBM · quantum commitment · >$10 B over five years · announced [G:IBM-10B-2026-06]

**Market & supply chain.** The only sellable artefact here is the decoder and its integration; Riverlane is the sole pure-play, claiming over 20 partnerships with makers and national labs [C][497]; NVIDIA commoditises the GPU path. Concentration risk is upstream (AMD/Xilinx, NVIDIA, a two-vendor refrigerator market); unit economics are unpublished beyond the 600–1,500 physical per logical every buyer pays [S][492]. Only G3 and G4 pay for it.

**IP & standards.** Google LLC, US 12,518,194, "Surface codes with densely packed gauge operators" (granted 2026-01-06) [G][495]; Riverlane Ltd, GB 2641501 A, "Quantum decoder" (published 2025-12-10) [G][501]. The code is unpatentable prior art from 1997–2007 [S][487], [489], so the fight is over decoders and layouts. No standard; the interfaces are open source — Stim, PyMatching, Deltakit [P][313].

**Roadmaps & track record.**
- Google: promised 2023-02 · milestone 3, a "long-lived logical qubit" at 10⁻⁶ · not reached; best 7.72×10⁻⁴ at d=7 [D][2] [C][31].
- IBM: promised 2025-06-10 · Kookaburra, first qLDPC memory-plus-logic module, in 2026 · not delivered as of 2026-09-03 [G:IBM-ROADMAP].
- Riverlane: promised 2026-03-12 · megaquop before end of decade, gigaquop early 2030s, teraquop from 2033 · pending [C][497].
Credibility: Google delivered every milestone it announced, late but real, and alone has numbers surviving a million cycles; IBM executes but has left this code; Riverlane ships peer-reviewed hardware; the atom camp has the best overhead story and the weakest duration data [G:QUERA-LIBRA-2026].

**Strategic reading.** If the surface code stays the workhorse the winners are whoever makes physical qubits cheap and cycles fast — the superconducting camp — plus a decoder supply chain selling to every platform. The losers are anyone whose case assumed 10² physical per logical: at 600–1,500, a 200-logical-qubit machine is a 10⁵-qubit machine — IBM's stated reason for leaving [D][227]. Substitution threats are dated: qLDPC at break-even on trapped ions, transversal codes on movable atoms, erasure-adapted codes. Bargaining power sits with platform vendors, except in real-time decoding, which most would rather buy than build.

*Open niche:* two entry points. A Λ-reporting standard: today's values are decoder-, subset- and duration-conditioned and not comparable across platforms, so a protocol fixing the decoder, the qubit-selection rule and a minimum run length would be adopted, because everyone must cite someone else's number. And cold-stage syndrome reduction — an SFQ predecoder clustering defects at 4 K and shipping only the residue up the fridge [S][G:PINBALL-2025-12].

## Outlook & open questions

Confirm within 12–24 months if: any group reports Λ ≥ 3 over ≥10⁵ cycles; a logical two-qubit gate at d ≥ 5 reaches 99% without post-selection; a patch runs across two modules; yoked patches appear on hardware. Demote if a qLDPC memory beats a surface-code patch at equal qubit count before end-2027. Best case by 2029: a few hundred logical qubits at 10⁻⁶ on 10⁵–10⁶ physical qubits, decoding a commodity — what Starling and Libra assume. Worst case: Λ stays near 2, d ≈ 25 stays the price of 10⁻⁶, and the code survives only as a benchmark. Open questions: (1) does Λ hold above 10³ physical qubits, where crosstalk and drift scale differently? (2) can yoking run on hardware, or does outer-code decoding defeat the real-time budget? (3) how much of the 2026 record is calibration rather than physics, given that RL steering alone moved d=7 from 1.43×10⁻³ to 7.72×10⁻⁴? Watch: Google's next distance step and IBM's Kookaburra.

## Sources

[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[31] Y. Chen and M. Devoret, “Our quantum hardware: the engine for verifiable quantum advantage,” Google Blog, Oct. 22, 2025. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ [C]
[40] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[41] E. Rosenfeld *et al.*, “Magic state cultivation on a superconducting quantum processor,” [arXiv:2512.13908](https://arxiv.org/abs/2512.13908), Dec. 2025. [D]
[42] W. Lin *et al.*, “Surface code logical operations on a superconducting quantum processor,” [arXiv:2607.01473](https://arxiv.org/abs/2607.01473), Jul. 2026. [D]
[43] Y. Wang *et al.*, “A superconducting surface-code processor with lattice-surgery logical operations,” [arXiv:2606.06598](https://arxiv.org/abs/2606.06598), Jun. 2026. [D]
[199] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[227] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[313] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[487] A. Y. Kitaev, “Fault-tolerant quantum computation by anyons,” *Annals of Physics*, vol. 303, no. 1, pp. 2–30, 2003, doi: [10.1016/S0003-4916(02)00018-0](https://doi.org/10.1016/S0003-4916(02)00018-0). [arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021). [S]
[488] E. Dennis, A. Kitaev, A. Landahl, and J. Preskill, “Topological quantum memory,” *Journal of Mathematical Physics*, vol. 43, no. 9, pp. 4452–4505, 2002, doi: [10.1063/1.1499754](https://doi.org/10.1063/1.1499754). [arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143). [S]
[489] H. Bombin and M. A. Martin-Delgado, “Optimal resources for topological two-dimensional stabilizer codes: Comparative study,” *Phys. Rev. A*, vol. 76, no. 1, Art. no. 012305, 2007, doi: [10.1103/PhysRevA.76.012305](https://doi.org/10.1103/PhysRevA.76.012305). [arXiv:quant-ph/0703272](https://arxiv.org/abs/quant-ph/0703272). [S]
[490] D. Horsman, A. G. Fowler, S. Devitt, and R. Van Meter, “Surface code quantum computing by lattice surgery,” *New Journal of Physics*, vol. 14, Art. no. 123011, Nov. 2011, doi: [10.1088/1367-2630/14/12/123011](https://doi.org/10.1088/1367-2630/14/12/123011). [arXiv:1111.4022](https://arxiv.org/abs/1111.4022). [S]
[491] A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland, “Surface codes: Towards practical large-scale quantum computation,” *Phys. Rev. A*, vol. 86, no. 3, Art. no. 032324, Sep. 2012, doi: [10.1103/PhysRevA.86.032324](https://doi.org/10.1103/PhysRevA.86.032324). [arXiv:1208.0928](https://arxiv.org/abs/1208.0928). [S]
[492] C. Gidney, M. Newman, P. Brooks, and C. Jones, “Yoked surface codes,” [arXiv:2312.04522](https://arxiv.org/abs/2312.04522), Dec. 2023. [S]
[493] C. Gidney and C. Jones, “New circuits and an open source decoder for the color code,” [arXiv:2312.08813](https://arxiv.org/abs/2312.08813), Dec. 2023. [S]
[494] R. Acharya *et al.*, “Suppressing quantum errors by scaling a surface code logical qubit,” *Nature*, vol. 614, pp. 676–681, Feb. 2023, doi: [10.1038/s41586-022-05434-1](https://doi.org/10.1038/s41586-022-05434-1). [D]
[495] Google LLC, “Surface codes with densely packed gauge operators,” U.S. Patent 12,518,194 B2, Jan. 6, 2026. [Online]. Available: https://patents.google.com/patent/US12518194B2/en Also https://patents.justia.com/search?q=%22surface+code%22+quantum+error+correction&company=google. [G]
[496] J. Bausch *et al.*, “Learning high-accuracy error decoding for quantum processors,” *Nature*, vol. 635, no. 8040, pp. 834–840, Nov. 2024, doi: [10.1038/s41586-024-08148-8](https://doi.org/10.1038/s41586-024-08148-8). [D]
[497] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [C]
[498] Qblox; Riverlane, “Qblox and Riverlane Demonstrate Integration Enabling Real-Time Quantum Error Correction,” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[499] Riverlane, “Riverlane awarded £2.1m by Horizon Europe to develop the next generation of its quantum error correction decoder,” May 1, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-awarded-2-1m-by-horizon-europe-to-develop-the-next-generation-of-its-quantum-error-correction-decoder [C]
[500] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[501] Z. A. Bracken, A. Zalawadiya, B. Barber, and L. Skoric, “Quantum decoder,” Google Patents, Dec. 10, 2025. [Online]. Available: https://patents.google.com/patent/GB2641501A/en [G]

## Open verification items

- Riverlane Series C: $75 M in the 2024-08-06 release [C][500] versus "$85 million in 2024" and "$120 million+" cumulative in the 2026-03-12 roadmap release [C][497]; both stated, the 2024 primary figure used.
- Yoked footprints (≈1,500 / ≈800 / ≈600 physical per logical at p = 10⁻³) come from a secondary rendering of arXiv:2312.04522 [S][492].
- Bombín and Martín-Delgado (2007) [S][489] is cited for the rotated layout on standard attribution; the arXiv abstract page carries no metadata.
- The 10⁶-cycle run's own error floor in the Willow paper [D][1] is not quoted here; only d=7, Λ, the 2.4(3)× ratio and the 10⁻¹⁰ burst floor are.
- Cost or energy per logical qubit: unpublished. Riverlane's revenue and contract values: undisclosed.
- The USTC logical-CNOT and Zhejiang lattice-surgery preprints [D][42], [43] come from the main report's fact-checked list.
