---
id: dec_tn
name: Tensor-network maximum-likelihood decoders (offline)
layer: "8 Decoder"
status: emerging
since: 2023
one_line: "Decoders that contract a tensor network to sum the probabilities of all errors in each logical class — near-optimal maximum-likelihood decoding, run offline on recorded data, never in real time; they decoded Google's first distance-5 memory to beat distance 3 (2.914% vs 3.028% per cycle)."
verdict: "The accuracy reference of surface-code experiments since 2023, used on transmon data by two groups and always after the run; it enters the machine only if a per-shot time or a hardware implementation approaches a syndrome cycle, and is demoted if learned or ensembled decoders replace it as the offline yardstick, as AlphaQubit did on Sycamore data."
updated: 2026-11-22
---

ML = maximum likelihood; TN = tensor network; MPS = matrix product state; χ = bond dimension, how much of the network a truncated contraction keeps; MWPM = minimum-weight perfect matching; RBIM = random-bond Ising model; d = code distance; CNOT = controlled-NOT gate; CPU / GPU = central / graphics processing unit; FPGA = field-programmable gate array; ASIC = application-specific integrated circuit; qLDPC = quantum low-density parity-check (code).

## Identity & lineage

A matching decoder finds the single likeliest error chain; a maximum-likelihood decoder finds the likeliest logical class, by summing the probabilities of every error consistent with the syndrome in each class. Dennis, Kitaev, Landahl and Preskill showed that this sum is the partition function of a disordered Ising-like model; Bravyi, Suchara and Vargo (IBM, 2014) contracted it as a tensor network on the code's grid, column by column, as an MPS truncated to bond dimension χ, in time O(nχ³) for n qubits. At χ = 6 the decoder was virtually indistinguishable from exact ML under bit-flip noise, and its depolarizing threshold lay between 17% and 18.5% against 15–16% for matching (simulation, perfect syndromes) [S][933]. Chubb generalised the contraction to any two-dimensional code, O(n log n + nχ³), reaching 18.81(3)% for the surface code against an optimal bound of 18.9(3)% [S][934]; Piveteau, Chubb and Renes (ETH Zürich) carried it to three dimensions — repeated noisy rounds and circuit-level noise, the problem a memory experiment poses [S][935].

Maximum likelihood reached hardware data before that without a tensor network: IBM decoded a distance-3 heavy-hexagon code on a 27-qubit Falcon processor by building the full error distribution — a method its authors call optimal but non-scalable, limited to four rounds [D][722]. The first tensor-network decoder on hardware data found is Google Quantum AI's, for the 72-qubit Sycamore surface-code memory published in February 2023: both class likelihoods were contracted approximately as an MPS evolution and checked for convergence, giving a decoder nearly optimal for its error priors but considerably slower [D][602] — hence `since` 2023. In 2026 Zhejiang University and HKUST (Guangzhou) decoded two distance-7 codes on a 125-qubit processor with a TN-ML decoder, and ran a TN-Bayesian decoder built on a random eight-vertex model, which reduces to the RBIM for bit-flip noise, on the transition data of distances 2, 4 and 6 [D][936]. Every hardware use so far is post-processing after the run.

Attributes (technology graph): carrier affinity 0.5 — classical inference, no carrier. Characteristic time: none; it is not in the loop. Readout: none. Mobility: none. Control modality: none, placed at no cryogenic stage — general-purpose computers after the experiment. Error structure: Pauli priors on an error hypergraph, hyperedges and Y errors included. Manufacturing: none — software.

## Physics & limits

The ceiling is exact maximum likelihood, #P-complete in general — as Chubb notes, citing Iyer and Poulin [G][934]; only the truncation of χ is heuristic [S][935]. In two dimensions — one perfect syndrome, as in code-capacity simulation or single-shot data — truncation is benign: the exact ML threshold under bit-flip noise, 10.9–11%, sits on the Nishimori point of the RBIM against about 10.31% for matching, and the MPS decoder reproduces exact ML at χ = 6–8; at d = 25 under depolarizing noise it cut the logical error probability by more than two orders of magnitude, because matching ignores X–Z correlations [S][933]. Repeated noisy rounds make the network three-dimensional and its approximate contraction far less well-behaved: circuit-level networks of the rotated surface code hold 245, 1,799 and 6,351 tensors at d = 3, 5 and 7, the gain over matching shrinks to a threshold of about 0.8% against 0.78% — at small distances and against PyMatching, not belief-matching — and on three-dimensional surface codes the decoder runs into numerical problems around d = 11 [S][935]. The cost of contracting Google's network exactly grows exponentially in d², that of its approximation as χ³ [D][602].

Cost binds. Chubb's threshold studies took about 35,000 CPU-hours each [S][934]; AlphaQubit's authors call the TN decoder one "which takes orders of magnitude longer to run" than their network [D][657]; none of the papers read gives a decode time per shot. The prior binds too: the decoder is optimal only for the noise model it is handed, and leakage, crosstalk and analogue readout lie outside a Pauli hypergraph; a decoder trained on the experimental data itself overtook it on the same syndromes [D][657].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: for a repeated-round memory, Google's distance-5 Sycamore experiment over 25 cycles, decoded at χ = 30: 2.914(16)% logical error per cycle against 3.028(23)% at distance 3 [D][602]; for size, two distance-7 surface codes (98 qubits) on Zhejiang University's 125-qubit processor, single-shot data decoded offline: logical error 0.014(1) before and 0.025(3) after teleportation [D][936]. Typical at scale: none — no tensor-network decoder runs in a control loop.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2014-05 | MPS approximate ML decoder, O(nχ³); depolarizing threshold 17–18.5% at χ = 6 vs 15–16% for matching (simulation) | IBM | [S][933] |
| 2021-01 | General 2D TN decoder; surface code 18.81(3)% under depolarizing noise vs bound 18.9(3)% (simulation) | Université de Sherbrooke / ETH Zürich | [S][934] |
| 2022-03 | Antecedent without a TN: exact ML by enumeration, d = 3 heavy-hexagon code, ~0.035 vs ~0.04 per round for matching (leakage post-selected) | IBM | [D][722] |
| 2023-02 | First TN decoder on hardware data found: Sycamore d = 3 and 5 memory, χ = 30, 2.914(16)% vs 3.028(23)% per cycle | Google Quantum AI | [D][602] |
| 2023-10 | Circuit-level 3D TN decoder beats matching on the rotated surface code (≈0.8% vs ≈0.78% threshold, small distances, against PyMatching) | ETH Zürich | [S][935] |
| 2024-11 | TN beaten on its own data: AlphaQubit 2.748(15)% vs TN 2.915(16)% per round at d = 5 | Google DeepMind / Google Quantum AI | [D][657][G:ALPHAQUBIT-2024-11] |
| 2026-10 | Two d = 7 codes (98 qubits) decoded offline by a TN-ML decoder, logical error 0.014(1) / 0.025(3); TN-Bayesian and matching decoders on the d = 2, 4, 6 transition data | Zhejiang University / HKUST (Guangzhou) | [D][936] |

Dominant error term: the prior, not the contraction — Google's decoder converged at χ = 30 [D][602], yet a decoder that learned the noise from data made about 6% fewer errors on the same syndromes [D][657].

## Manufacturing, materials & supply chain

Nothing is fabricated: the decoders are research code on CPU clusters — Google's on the open-source library quimb [D][602], Chubb's as the Julia package SweepContractor.jl [S][934], the three-dimensional one as tndecoder3d [S][935]. No FPGA, GPU or ASIC implementation was located and no vendor sells one; supply-chain exposure is that of commodity computing. The September 2024 export rule names quantum computers, cryogenic electronics and related software [G:BIS-QUANTUM-ECCN-2024-09]; all three decoders are open source.

## Control, readout & I/O burden

Offline means the decoder never touches the control stack: detection events or bitstrings go to storage and the contraction runs afterwards. Google judged in 2023 that the TN decoder would likely be too slow to keep up with a surface-code processor's throughput, and cut a distance-3 cross-check short because of the network's computational cost [D][602]. The Zhejiang processor had no feedback operation yet, so CNOT layers replaced teleportation's classical communication and the logical outcome was recovered in post-processing [D][936]. A live transmon decoder must clear a round within the 1.1 µs cycle [G:WILLOW-QEC-2024-12]; the three-dimensional decoder pre-compresses a network of thousands of tensors (bond dimension 16, truncated to 8), and its authors set runtime aside to pursue accuracy [S][935]. The burden is compute and storage, not lines or bandwidth.

## Role in the stack

Architectures: the transmon lattice (`sc`) — both hardware decodes are transmon data; none on atom, ion or spin data was located. It requires the surface code (`code_surface`), the only code it has decoded on hardware; simulations extend it to colour and subsystem codes [S][934], none to the non-planar checks of `code_qldpc`. It is an alternative to matching (`dec_mwpm`), which keeps the likeliest chain where this sums the likeliest class, and to neural decoders (`dec_nn`), which learn the same posterior; on Sycamore data the order is learned, tensor network, belief-matching, correlated matching, PyMatching [D][657]. It grades the real-time decoders — `dec_fpga`, `dec_gpu`, `dec_relaybp` and the matcher in Google's loop [G:WILLOW-RTDECODER-2024] — and competes offline with the ensembled matcher Harmony, described as approaching tensor-network accuracy while being substantially faster and trivially parallel [P][937]. Derived clock (sum of the syndrome round: gate layers + transport + readout + reset): no contribution, since it never runs inside the round. Price of switching from matching: no live use and no published per-shot time; gained: the near-optimal number a hardware result is judged by. Neighbouring empty slot: a tensor-network decoder fast enough for the loop.

## Evidence — how the numbers were measured

Google's figures are memory experiments: logical error against cycle number fitted from cycle 3 to 25, 100,000 repetitions per point, averaged over the X and Z bases, with priors from detection-event correlations computed on the complementary half of the data; convergence was reached at χ = 30 on the distance-5, 25-round experiment [D][602]. Per basis the distance-5 decode gave 3.01(2)% (X) and 2.81(1)% (Z) per cycle against 3.16(2)% and 2.96(1)% for belief-matching [D][602]. Value conflict: the distance-5 figure is 2.914(16)% in Google's paper and 2.915(16)% in AlphaQubit's re-decode [D][657]; the Atlas quotes each with its own source.

The Zhejiang figures are not a repeated-round memory: the code is prepared by a linear-depth unitary circuit, entangled transversally with a second register and measured once; logical error is (1 − ⟨Z_L⟩)/2 from ⟨Z_L⟩ = 0.973(2) and 0.949(6) [D][936]. One round of bitstrings is a two-dimensional problem, where tensor networks are near exact. The decoders disagree on the transition, read from distances 2, 4 and 6: along X the ML pseudo-threshold is 0.122(2)π, MWPM's 0.116(2)π and the TN-Bayesian 0.107(1)π, against an asymptotic 0.1072128(2)π; along X + Z, 0.175(5)π, 0.164(2)π and 0.152(2)π against 0.1548014(3)π — the authors attribute the ML overestimate to extra Z-type syndrome information at even distances, and odd distances give the ML decoder 0.100(9)π along X [D][936]. A 2026 review generalises the point: different decoders run on the same experimental data can give strikingly different verdicts on the hardware [P][938]. Not published: a per-shot decode time, or the computer used, for any hardware dataset; the Zhejiang decoder's bond dimension; a tensor-network decode of a repeated-round memory beyond distance 5.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer, user | US | Earliest TN decoder on hardware data found (Sycamore, χ = 30) | [D][602] |
| Google DeepMind | developer | UK | AlphaQubit, which beat the TN decoder on the same data | [D][657] |
| Zhejiang University (H. Wang) | user | CN | 125-qubit processor; two d = 7 codes decoded offline | [D][936] |
| HKUST (Guangzhou) (G.-Y. Zhu) | developer | CN | TN-ML and TN-Bayesian decoders for the Zhejiang bitstrings | [D][936] |
| IBM | research | US | MPS decoder (2014); exact ML by enumeration on a Falcon processor | [S][933], [D][722] |
| ETH Zürich (Piveteau, Chubb, Renes) | research | CH | Three-dimensional and circuit-level TN decoding, open source | [S][935] |
| Université de Sherbrooke / ETH Zürich (Chubb) | research | CA / CH | General 2D TN decoder, SweepContractor.jl | [S][934] |

**Money.** No dated money is attached to tensor-network decoding; the acknowledged funding is academic — a Swiss National Science Foundation Sinergia grant for Chubb [S][934]; China's Quantum Science and Technology Major Project (2021ZD0300200) and the National Natural Science Foundation of China for the Zhejiang experiment [D][936].

**Market & supply chain.** None: free research code whose users are experimental groups needing an accuracy reference. Its value is evidentiary — it decides how good a logical qubit is said to be — and its cost is cluster time.

**IP & standards.** No patent search was made for this record. No standard; the de facto input is a Stim-style detector error model, used for Google's priors and for the three-dimensional decoder [D][602], [S][935].

**Roadmaps & track record.** No vendor roadmap names a tensor-network decoder. Google's 2023 forecast — too slow for real time, belief-matching the live candidate [D][602] — held: its live decoder is a matcher [G:WILLOW-RTDECODER-2024]. The ETH group's stated use case — an accurate but slow decoder to help demonstrate break-even error correction offline [S][935] — is the one that materialised. The Zhejiang group's stated next steps are mid-circuit measurement, reset and teleportation between distant modules [D][936].

**Strategic reading.** It certifies a logical qubit rather than running one. Learned decoders contest its accuracy from above, ensembled matchers from the side, and its cost keeps it out of the loop; its niche is experiments where accuracy is the result — threshold physics such as the teleportation transition — and the ground truth for grading fast decoders.

## Outlook & open questions

Confirm within 12–24 months if a tensor-network decoder decodes a repeated-round hardware memory at d ≥ 7, if a third group uses one for a headline result, or if a per-shot time is published that hardware could bring within a millisecond atom or ion cycle. Demote if every new d ≥ 7 hardware paper uses a learned or ensembled-matching decoder as its offline reference and none a tensor network. Best case by 2029: the standard certifier of logical error rates and thresholds up to d ≈ 11, with device-learned priors; worst case: a 2014–2026 benchmarking method displaced by learned decoders.

Open questions: (1) can three-dimensional contraction pass d = 11 without numerical breakdown? (2) what does one shot cost at d = 7 over 25 rounds? (3) can the prior absorb leakage and crosstalk and regain the lead a learned decoder took? (4) which threshold should be quoted when ML and Bayesian tensor-network decoders disagree on the same bitstrings? (5) will a colour or qLDPC code's hardware data be decoded this way?

## References

[602] R. Acharya *et al.*, “Suppressing quantum errors by scaling a surface code logical qubit,” *Nature*, vol. 614, pp. 676–681, Feb. 2023, doi: [10.1038/s41586-022-05434-1](https://doi.org/10.1038/s41586-022-05434-1). [D]
[657] J. Bausch *et al.*, “Learning high-accuracy error decoding for quantum processors,” *Nature*, vol. 635, no. 8040, pp. 834–840, Nov. 2024, doi: [10.1038/s41586-024-08148-8](https://doi.org/10.1038/s41586-024-08148-8). [D]
[722] N. Sundaresan *et al.*, “Demonstrating multi-round subsystem quantum error correction using matching and maximum likelihood decoders,” *Nat. Commun.*, vol. 14, Art. no. 2852, May 2023, doi: [10.1038/s41467-023-38247-5](https://doi.org/10.1038/s41467-023-38247-5). [D]
[933] S. Bravyi, M. Suchara, and A. Vargo, “Efficient Algorithms for Maximum Likelihood Decoding in the Surface Code,” *Phys. Rev. A*, vol. 90, Art. no. 032326, 2014, doi: [10.1103/PhysRevA.90.032326](https://doi.org/10.1103/PhysRevA.90.032326). [arXiv:1405.4883](https://arxiv.org/abs/1405.4883). [S]
[934] C. T. Chubb, “General tensor network decoding of 2D Pauli codes,” [arXiv:2101.04125](https://arxiv.org/abs/2101.04125), Jan. 2021. [S]
[935] C. Piveteau, C. T. Chubb, and J. M. Renes, “Tensor Network Decoding Beyond 2D,” *PRX Quantum*, vol. 5, Art. no. 040303, 2024, doi: [10.1103/PRXQuantum.5.040303](https://doi.org/10.1103/PRXQuantum.5.040303). [arXiv:2310.10722](https://arxiv.org/abs/2310.10722). [S]
[936] Y. Zou *et al.*, “Teleportation transition of surface codes on a superconducting quantum processor,” *Nat. Phys.*, Oct. 2026, doi: [10.1038/s41567-026-03484-0](https://doi.org/10.1038/s41567-026-03484-0). [arXiv:2602.21293](https://arxiv.org/abs/2602.21293). [D]
[937] K. Zhang *et al.*, “Learning to Decode in Parallel: Self-Coordinating Neural Network for Real-Time Quantum Error Correction,” [arXiv:2601.09921](https://arxiv.org/abs/2601.09921), Jan. 2026. [P]
[938] H. Cao, G. Yan, Y. Du, and F. Pan, “Maximum Likelihood Decoding of Quantum Error Correction Codes,” [arXiv:2605.17230](https://arxiv.org/abs/2605.17230), May 2026. [P]

