---
id: dec_gpu
name: GPU decoding via NVQLink
layer: "8 Decoder"
tier: 2
status: demonstrated
since: 2025
one_line: "RoCE link putting a GPU inside the QEC feedback loop at 3.84 µs mean round trip, so decoding runs as CUDA software on GH200-class hardware instead of a fixed FPGA bitstream."
verdict: "The round trip is bounded (3.96 µs max over 1,000 samples) and the decoder is software, but the only published decode is BP+OSD on Quantinuum's Helios at 67 µs median; no head-to-head against an FPGA decoder on identical syndromes exists as of 2026-09-04."
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A low-latency RDMA-over-Converged-Ethernet path between a QPU's control electronics and a GPU, with an open-source FPGA core on the quantum side, so decoding and in-loop calibration run as CUDA software rather than a bitstream. NVIDIA announced it on 2025-10-28, naming 17 quantum-computer builders, five control-electronics vendors and nine US national laboratories [C][1]; the numbers followed on 2025-11-17 [C][2]. Coordinates: d = platform-agnostic, reaching superconducting, trapped-ion QCCD and neutral-atom paths; e/f/g = no control modality, corrects Pauli syndrome errors, no fabrication — commodity GPU and Ethernet hardware (graph record).

## Physics & limits
Two budgets, and the mistake is to add them. Transport is bounded: 3.84 µs mean, 0.035 µs standard deviation, 3.96 µs maximum over 1,000 samples [C][2] — the tightness matters more than the mean, because a feedback loop is sized by its tail. Decode is not: BP+OSD on a GH200 against Quantinuum's Helios gives a 67 µs *median* for Bring's code, taking an 8-logical-qubit memory from 4.95 ± 0.67% to 0.925 ± 0.38% error, a 5.4× gain [C][2].

Whether 67 µs is slow depends on which clock it must meet. For memory the requirement is throughput, not per-cycle latency: Google sustained 10⁶ cycles at d=5 on a 1.1 µs cycle with a real-time decoder of 63 µs *mean latency* [D][6] — the same order as the GPU figure — because a sliding window pipelines cycles instead of decoding each within one. Reaction time is the hard constraint, and it binds only where an operation is conditioned on a decode: magic-state injection, feed-forward, lattice surgery. That distinction, not the raw microseconds, decides where this layer is usable. GPU decoding is therefore comfortable on millisecond-cycle ion and atom platforms, adequate for superconducting memory, and unproven on the reaction-limited path. What moves the floor: kernels exploiting GPU parallelism rather than ports of serial algorithms.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-11 | RoCE round trip 3.84 µs mean, 0.035 µs SD, 3.96 µs max over 1,000 samples | NVIDIA | [C][2][G:NVQLINK-QUANTINUUM-2025-11] |
| 2025-11 | BP+OSD on GH200, Bring's code on Helios: 67 µs median, 4.95%→0.925% logical error | Quantinuum | [C][2] |
| 2026-03 | Real-time QEC demonstrator over NVQLink, under 4 µs end-to-end | IQM | [P][3][G:NVQLINK-2025] |

GPU decode time dominates at ~17× the network hop, so the interconnect is not what has to shrink. No published result runs GPU BP+OSD and an FPGA decoder on identical traces.

## Manufacturing, materials & supply chain
No fabrication process. The GPU side is NVIDIA silicon — GH200 for Helios, RTX PRO 6000 Blackwell Max-Q for the networking demonstration [C][2] — with no AMD or Intel equivalent as of 2026-09-04. The network side is deliberately unlocked: RoCE is a standard and NVIDIA published an open-source FPGA core for the QPU endpoint [C][2], which let five control-electronics vendors integrate it [C][1]. The asymmetry is the commercial design — give away the interface, sell the accelerator. Nothing is priced; it ships as a reference architecture with a sign-up page [C][1]. Export exposure is inherited from US controls on advanced GPUs, not from a quantum ECCN.

## Control, readout & I/O burden
The loop is control electronics → RoCE → GPU → back, at 3.84 µs plus decode. Helios is 98 physical qubits [D][8], so nothing at 10³ has run end-to-end. At 10⁴–10⁶ the question is whether decode time grows with code size faster than throughput grows per GPU generation, and whether batching across logical blocks keeps the budget flat; no source states either. The offsetting argument, unquantified: one GPU cluster can serve several QPUs, which an FPGA bolted to one rack cannot.

## Role in the stack
It requires nothing upstream and replaces FPGA-based real-time decoding, trading a fixed bitstream for software changeable between shots; the graph record marks it a hub across the superconducting, trapped-ion QCCD and neutral-atom paths — the broadest reach here. Derived clock contribution: ~71 µs per decode round trip (2 s.f.), 1–7% of a 1–5 ms ion or atom cycle but ~65 cycles of a 1.1 µs superconducting one [D][6]. Switching cost is a rack and a software stack, not a code change — the opposite of the qLDPC decoders. Adjacent empty slot: an independent cross-vendor benchmark.

## Verification (QCVV)
Both headline numbers come from NVIDIA's own blog, co-developed with Quantinuum, and are not peer-reviewed [C][2]. The 5.4× carries uncertainties — better practice than most vendor claims — but it is one code on one machine, and the IQM demonstrator is trade press [P][3]. No comparison exists against Relay-BP [D][4] or Riverlane's decoder [D][5] on the same syndromes, so "GPUs are slower than FPGAs" compares numbers from different codes and machines.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| NVIDIA | Developer | USA | Built NVQLink and the nv-qldpc-decoder; supplies the GPUs | [C][1][2] |
| Quantinuum | User | USA/UK | Only published deployment: Helios plus GH200 running BP+OSD | [C][2][G:NVQLINK-QUANTINUUM-2025-11] |
| IQM | User | Finland | Real-time QEC demonstrator over NVQLink under 4 µs end-to-end | [P][3][G:NVQLINK-2025] |
| Zurich Instruments | Supplier | Switzerland | Control electronics carrying the NVQLink endpoint | [C][1] |
| DARPA | Regulator | USA | QBI Stage B funds several of the named QPU builders | [G][10][G:QBI-STAGEB-2025-11] |

**Money.** 2025-10-28 · NVIDIA · launch, 17 builders / 5 control vendors / 9 labs · no financing disclosed · announced [C][1]. 2025-09-04 · Quantinuum · $600 M at $10 B pre-money, NVentures participating · closed [C][G:QTM-600M-2025-09]. 2026-05-22 · Alice & Bob · Series B extension with NVentures · closed [C][G:AB-SERIESB-2025-01]. 2026-07-26 quarter · NVIDIA · revenue $96.2 B, Data Center $89.0 B, +106% y/y, quantum unmentioned · reported [G][7] — the economics of this layer in one line.

**Market & supply chain.** No market yet — no price, SKU or licence terms disclosed [C][1]. The chain splits: open interface, single-sourced accelerator, so concentration risk is the decoder host, not the link. Goal exposure is broader than any FPGA decoder — G3/G4 as a decoder, G2 because the same path serves mitigation and calibration, G7 because national-lab deployments are procurement-shaped.

**IP & standards.** No patent family specific to NVQLink was found in any named database. The standards posture is the interesting part: RoCE is an existing Ethernet standard and the QPU-side core is open source [C][2], so NVIDIA standardises the boundary it does not sell. Third parties build against CUDA-Q QEC [P][G:QXLABS-QECCT-2026-07].

**Roadmaps & track record.** NVIDIA: (2025-10 · launch with 17 builders · delivered, one published deployment three weeks later) [C][1][2]; (2025-11 · partners to deploy on future processors · only Helios confirmed) [C][2]. IQM: (2026-03 · demonstrator · delivered) [P][3]. Launch-to-first-deployment was effectively zero; the gap between 17 announced builders and one published deployment is the number to watch.

**Strategic reading.** If GPU decoding wins, every fault-tolerant machine becomes a recurring GPU customer and decoding stops differentiating QPU vendors — good for builders without FPGA engineering, bad for Riverlane and IBM's in-house route. NVIDIA loses little if it fails: quantum does not appear in a $96.2 B quarter [G][7], so this is a cheap option on the classical half of a future stack. The substitution threat is a decoder ASIC nobody sells. Bargaining power sits with NVIDIA on the accelerator and the control vendors on the endpoint.

*Open niche:* nobody has run GPU and FPGA decoders against identical recorded syndrome traces; the vendor numbers are medians and means from different codes on different machines. An independent benchmark — common traces, published latency distributions, accuracy under real noise — would settle a comparison the layer argues by press release, and has no incumbent.

## Outlook & open questions
Falsifiable (12–24 months): confirm if a second QPU vendor publishes an NVQLink decode loop with numbers by end-2027; demote if published deployments still number one. Best case 2029: GPU decoding is the default on ion, atom and superconducting memory, reaction-limited operations handed to a small local FPGA. Worst case: 17 builders yield two deployments and dedicated hardware keeps the loop. Open questions: how decode time scales with code size and block count; whether anyone reports tail rather than median latency; whether AMD or Intel field a rival host. Watch: a second deployment and any independent benchmark.

## Sources
[1] NVIDIA [C] · "NVIDIA introduces NVQLink — connecting quantum and GPU computing for 17 quantum builders and nine scientific labs" · NVIDIA Newsroom · 2025-10-28 — https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing
[2] NVIDIA [C] · "NVIDIA NVQLink architecture integrates accelerated computing with quantum processors" · NVIDIA Developer Blog · 2025-11-17 — https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
[3] Quantum Computing Report [P] · "IQM and Zurich Instruments develop real-time QEC via NVIDIA NVQLink" · 2026-03 — https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/
[4] Maurer, T., Bühler, M., Kröner, M., Haverkamp, F., Müller, T., Vandeth, D., Johnson, B.R. (IBM) · "Real-time decoding of the gross code memory with FPGAs" · arXiv:2510.21600 · 2025-10-24 — https://arxiv.org/abs/2510.21600
[5] Ziad, Zalawadiya, Topal, Camps, Gehér, Stafford, Turner (Riverlane) · "Local clustering decoder as a fast and adaptive hardware decoder for the surface code" · Nature Communications 16, 11048 · 2025-12-17 — https://www.nature.com/articles/s41467-025-66773-x
[6] Google Quantum AI · "Quantum error correction below the surface code threshold" · Nature 638, 920 · 2024-12-09 — https://www.nature.com/articles/s41586-024-08449-y
[7] NVIDIA [G] · "NVIDIA announces financial results for second quarter fiscal 2027" (quarter ended 2026-07-26) · 2026-08 — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[8] Quantinuum · "Computing with many encoded logical qubits beyond break-even" (Helios, 98 qubits) · arXiv:2602.22211 · 2026-02 — https://arxiv.org/abs/2602.22211
[9] Quantinuum [C] · IPO pricing, 28,000,000 shares at $60, Nasdaq QNT · 2026-06-03 — https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering
[10] DARPA [G] · Quantum Benchmarking Initiative, Stage B selection · 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection

## Open verification items
No independent (non-NVIDIA, non-Quantinuum) confirmation of the 3.84 µs or 67 µs figures as of 2026-09-04.
No head-to-head benchmark of GPU against FPGA decoding on identical syndrome traces.
Whether GPU decode time scales with code size or logical-block count at 10⁴–10⁶ qubits is stated nowhere reviewed.
NVentures investment amounts in Quantinuum, QuEra and Alice & Bob are not separately disclosed; only the round totals are public.
The launch release's headline counts (17 builders, nine labs) and the enumerated names retrieved from it do not tally exactly; the headline counts are used here.
