---
id: g_mwspin
name: Microwave / optical spin gates (defect centres, 1Q spins)
layer: "3 Gate mechanism"
tier: 3
status: demonstrated
since: 2004
one_line: Resonant microwave rotation of a defect electron spin, hyperfine-conditional rotation of its neighbouring nuclei, and optical pulses for initialisation and readout.
verdict: Sub-0.1% single-node gate error, but the optical cycles that initialise and read the spin are also its dominant decoherence source, and no benchmark in use separates the two.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Resonant microwave drive rotates a colour centre's electron spin between ground-state sublevels — 2.87 GHz at zero field for NV, a Zeeman-split pair for the group-IV centres. Hyperfine coupling to ¹³C or ¹⁴N neighbours makes them addressable by conditional rotations — a register from one defect. Optical pulses do the initialisation and readout microwaves cannot. Coherent single-defect Rabi driving dates to 2004; the benchmark is Fujitsu/QuTech gate-set tomography below 0.1% [P][1].
Coordinates: engineered placement of a natural defect, static, entangling near 1 µs (electron) and milliseconds (nuclear); microwave plus optical control; Pauli and coherent error.

## Physics & limits
Two rates set the architecture: megahertz electron Rabi gives gates of tens to hundreds of nanoseconds, while hyperfine-conditional nuclear gates run at kilohertz — three orders slower, so the long-lived memory is the slow one. The floor is optical duty cycle, not microwave power: every initialisation or readout pulse drives the defect through an excited state that can ionise it and shifts the local charge environment, so the error of the *next* gate depends on how many photons the last one scattered. Isotopic ¹²C purity lengthens T₂ but does nothing about that; only fewer optical cycles per operation move the floor, which is why Delft's ~10× collection gain is a gate result as much as a link result [D][2].

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2025-03-28 | NV 1Q and 2Q gate error below 0.1% by gate-set tomography | Fujitsu with QuTech | [P][1] |
| 2026-01-15 | resonant photon collection ~0.05% → ~0.5%, echo coherence above 100 µs kept | QuTech | [D][2] |
| 2026-05-26 | unconditional teleported CNOT between cryostats, 63(4)% | QuTech | [D][3] |

Dominant term: optically induced charge instability, not microwave control.

## Manufacturing, materials & supply chain
The gate inherits diamond's constraints: CVD growth from Element Six, implanted defects, per-device nanophotonics. Nothing in the drive chain multiplexes: each addressed defect needs its own resonant laser line, microwave feed and detector channel, so hardware scales linearly with sites — the opposite of a shared microwave plant. Control latency is set by the link, not the gate: the teleported CNOT needed feed-forward inside the memory lifetime [D][3]. At 10³ sites the wall is laser count and optical fan-out, with no published plan. No export rule names colour centres.

## Role in the stack
Requires the colour-centre carrier and provides the gate the defect-node path uses. Its clock contribution never binds: ~10⁻⁷–10⁻⁶ s electron gates against ~100 µs readout and links six to nine orders slower; no code runs on the defect path, so sum of the syndrome round: gate layers + transport + readout + reset has no value here and the link rate is the clock. Verification: the sub-0.1% figure is one collaboration, published through a press release, and gate-set tomography as applied does not separate microwave error from optically induced charge-state error — a composite that will not transfer to another readout duty cycle. The teleported CNOT is unconditional, unlike the post-selected T-centre result at Bell 0.60(8) [P][7].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| QuTech | developer | Netherlands | Cavity NV control, remote gate | [D][2][3] |
| Fujitsu | user | Japan | Joint NV gate programme | [P][1] |
| Quantum Brilliance | developer | Australia | Room-temperature units | [P][6] |
| Photonic Inc. | developer | Canada | T-centre spin control | [P][7] |
| Element Six | supplier | UK | Merchant CVD diamond | [P][4] |

**Money.** 2026-05-12 · Photonic Inc. · equity · USD 200 M at USD 2 B · Microsoft returning · closed [C][G:PHOTONIC-200M-2026-05]. 2026-07 · QuantumDiamonds · EUR 91 M, EUR 76 M of it EU Chips Act · closed [P][4]. 2025-01 · Quantum Brilliance · Series A · USD 20 M · ~USD 58 M cumulative · closed [P][4]. No QBI stage names this gate mechanism.

**Market & supply chain.** One merchant diamond supplier and a thin detector base are the concentration risks; microwave hardware is shared with every modality. Pays into G6 and sensing; no G3 or G4 money reaches this gate.

**IP & standards.** No dated patent family from a named database as of 4 Sep 2026; no standards body covers defect-spin control.

**Roadmaps & track record.** Quantum Brilliance (units at three laboratories · delivered, sites undated) [P][6]. SaxonQ (QC2026 Dual Core · shipped) [P][4]. Photonic Inc. (fault tolerance "within five years" of 2023-11 · unmet). Credibility is inverted: the smallest actors ship, the best-funded promises.

**Strategic reading.** This gate wins only inside a networking or edge thesis, not the fault-tolerance budget. Suppliers hold leverage: no vendor sells an integrated defect-control stack.

*Open niche:* the open QCVV problem is separating optically induced charge-state error from microwave gate error, which benchmarking and tomography conflate. Sweeping readout duty cycle would give a number that transfers between labs.

## Outlook & open questions
Confirm/demote (12–24 months): a peer-reviewed sub-0.1% gate-set result with an explicit charge-state error term confirms; two more years of press-release fidelities demotes it. Best case 2029: a small error-detected multi-node register. Worst case: excellent gates that never enter a code. Open: (1) can optical addressing be multiplexed; (2) does anyone report nuclear-gate times with fidelities; (3) does a defect platform reach a logical qubit.

## Sources
[1] Fujitsu and QuTech · "Fujitsu and QuTech realize high-precision quantum gates" (NV gate-set tomography below 0.1%; no primary paper located) · The Quantum Insider · 2025-03-28 · https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ [P]
[2] Fischer et al. (QuTech, Delft) · cavity-enhanced NV photon collection · Nature Communications · 2026-01-15 · https://www.nature.com/articles/s41467-025-66722-8 [D]
[3] Hanson et al. (QuTech, Delft) · "Unconditionally teleported quantum gates between remote solid-state qubit registers" · Nature Communications · 2026-05-26 · https://www.nature.com/articles/s41467-026-72818-6 [D]
[4] The Quantum Insider · "Top Diamond NV-Centre Quantum Computing Companies in 2026" · 2026-07-10 · https://thequantuminsider.com/2026/07/10/8-quantum-computing-companies-working-with-nv-centre-in-diamond-technology/ [P]
[5] Knaut et al. (Harvard) · "Entanglement of nanophotonic quantum memory nodes in a telecom network" · Nature 629 · 2024-05-15 · https://www.nature.com/articles/s41586-024-07252-z [D]
[6] Quantum Brilliance · news and deployments (Oak Ridge, Fraunhofer IAF, Pawsey; dates not stated) · company page · accessed 2026-09-04 · https://quantumbrilliance.com/news [P]
[7] Photonic Inc. · "Distributed Quantum Computing in Silicon" · arXiv:2406.01704 · 2024-06-03 · https://arxiv.org/html/2406.01704v1 [P]

## Open verification items
- The below-0.1% NV gate-set-tomography figure rests on a joint Fujitsu/QuTech press release relayed by trade press [1]; no peer-reviewed publication with error bars or an error budget was located. Tagged [P] here, not [D] as in the main report and graph record.
- No source found that reports nuclear-spin gate durations alongside the NV fidelity numbers, so the kilohertz Rabi rate is stated as a mechanism, not a measured device figure.
- Quantum Brilliance's deployment sites are named without dates [6]; no 2025–2026 funding beyond the January 2025 Series A was found.
- No dated roadmap with qubit counts exists for any defect-gate actor.
