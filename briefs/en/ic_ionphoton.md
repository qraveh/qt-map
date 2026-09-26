---
id: ic_ionphoton
name: Ion–photon photonic link
layer: "9 Interconnect"
status: demonstrated
since: 2007
one_line: "Heralded ion–photon entanglement over fibre links separate ion traps into one machine; best published rate 250 s⁻¹ against a ~10⁴ s⁻¹ need."
verdict: "Real: remote Bell pairs at 9.7–250 s⁻¹, 94–97% fidelity, teleported CZ 86%. Unverified: IonQ's networked-systems claim carries no rate or fidelity. Demote if nothing exceeds 10³ s⁻¹ by 2028."
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An ion decaying from an excited state emits a photon entangled with its qubit state; interfere two such photons from two traps on a beamsplitter and a coincident detection projects the distant ions into a Bell pair — heralded and probabilistic, unlike an in-trap gate, and the only mechanism coupling ions in separate vacuum systems. First shown in 2007 by Monroe's group (Michigan, later Maryland/Duke) — the lineage that holds today's rate record, not the Wineland/NIST line.

Attributes. **Mobility: flying** — the photon, not the ion, carries entanglement. **Control modality @ placement: optical, room temperature** — collection, interference and detection sit outside the trap's vacuum envelope.

## Physics & limits

The rate is the whole problem. Success probability per attempt goes as η², where η is collection solid angle × branching ratio × fibre coupling × detector efficiency, since both photons must survive; two in η is four in rate. With free-space objectives η sits in the low per cent, so published rates are 9.7 s⁻¹ over a 2-m link [D][108] and 250 s⁻¹ at the record [D][109] against the ~10⁴ s⁻¹ a QEC cycle would consume — 40× at best, closing quadratically through collection, not electronics.

Fidelity is the healthier budget: two-photon interference visibility, detector dark counts and jitter, and residual ion motion cap heralded fidelity at 94–97% [D][108], [109]. Because failures are heralded, the error the code sees is loss, so low η costs throughput, not infidelity — an erasure channel at the interconnect layer. What moves the floor: cavity (Purcell) enhancement, waveguide-integrated collection in photonic-chip traps, telecom frequency conversion, emitter multiplexing per module, and quantum memories that let attempts accumulate rather than retry in lockstep.

## Engineering state of the art

Best demonstrated is a distributed computation, not just a Bell pair: Oxford ran a teleported CZ at 86.2(9)% and a distributed Grover search across a 2-m link [D][108].

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024 | Remote entanglement rate record, 250 s⁻¹ at fidelity >94% | Duke/Maryland | [D][109] |
| 2025-02 | 2-m link: remote Bell 96.89(8)% at 9.7 s⁻¹, teleported CZ 86.2(9)% | Oxford | [D][108] |
| 2025-06 | Lightsynq (photonic interconnect + quantum memory, >20 patents and applications) acquired | IonQ | [C][566] |
| 2026-04 | Two commercial ion systems linked; no rate, fidelity or distance disclosed | IonQ | [C][567] |

Dominant gap: throughput. Every published rate is two to three orders below what a networked QEC cycle needs; fidelity is not the blocker.

## Manufacturing, materials & supply chain

No fab and no wafer statistic — the "yield" is optical collection efficiency, an alignment and numerical-aperture figure. A link is a high-NA objective or in-vacuum cavity, single-mode fibre and polarisation control, a Bell-state-measurement station with two single-photon detectors, and coincidence logic. Traps come from elsewhere: Infineon is the merchant trap foundry for IonQ/Oxford Ionics, eleQtron and Universal Quantum, Honeywell fabricates Quantinuum's in house [C][G:INFINEON-IONTRAP-FAB-2026]. The concentrated input is detectors — the merchant SNSPD base is Single Quantum, ID Quantique, Photon Spot and Quantum Opus, and IonQ owns ID Quantique [P][G:SNSPD-VENDORS-2026]. Cost per link is not quotable. Export exposure is indirect: the BIS rule of 2024-09-06 names no interconnect optics, only ≥34-qubit machines (4A906) [G][225].

## Control, readout & I/O burden

Per link: one collection channel per ion, two detectors, a phase-stable optical path, a coincidence gate. Heralding latency is sub-µs, so the electronics limit nothing — the attempt rate does. At ~10 modules a handful of point-to-point links works; at 10⁴ any-to-any needs a switch fabric plus enough pair generation to feed inter-module lattice surgery, and no published design states a link count. Quantinuum's in-trap alternative exchanges ions at 2.5 kHz and transports through junctions at 4 m/s [D][106] — an order faster than the best photonic link, which is why QCCD vendors have not adopted this node.

## Role in the stack

It requires the trapped atomic ion and single-photon detection (SNSPD/TES) and provides for nothing downstream: a terminal capability, the exit from single-trap scaling. Paths served: QCCD laser-gate ions (Quantinuum, AQT) and electronic-gate, chip-controlled ions (IonQ/Oxford Ionics, eleQtron, Quantum Art). The graph lists no replacement or conflict, but in-trap transport is the functional rival and currently wins. Derived-clock contribution: dominant where used — at 250 s⁻¹ one inter-module pair costs 4.0×10⁻³ s, comparable to a full-width ion layer; at 9.7 s⁻¹ it is 1.0×10⁻¹ s.

## Verification (QCVV)

Heralded fidelity is tomography or parity oscillation conditioned on a successful click, so 94–97% describes the links that happened, not the channel including loss; the honest figure of merit is rate × fidelity, which nobody reports. Published rates come from different species, distances and collection geometries and are not directly comparable. The weakest evidence is commercial: IonQ's release states it "validated the generation, transmission, and detection of photons used to enable quantum entanglement" — wording that stops short of reporting a measured Bell state, with no rate, fidelity or distance and no replication [C][567]. Among peer-reviewed results there is no conflict.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| University of Oxford | research | UK | 2-m link, teleported CZ and distributed Grover | [D][108] |
| Duke University | research | US | Co-holder of the 250 s⁻¹ record | [D][109] |
| IonQ | developer | US | Networked two systems; owns Lightsynq and ID Quantique | [C][567] |
| Quantinuum | developer | US | Scales by in-trap transport; no photonic commitment | [D][106] |
| ID Quantique | supplier | CH | SNSPD vendor, acquired by IonQ | [P][G:SNSPD-VENDORS-2026] |
| Single Quantum | supplier | NL | Merchant SNSPD supplier, independent | [P][G:SNSPD-VENDORS-2026] |
| AFRL | user | US | Partner on IonQ's April-2026 milestone | [C][567] |
| DARPA | investor | US | QBI Stage B funds both ion vendors | [G][60] |

**Money.**
- 2025-05-06 · IonQ · M&A, ID Quantique (single-photon detectors) · undisclosed · — · closed [P][G:SNSPD-VENDORS-2026]
- 2025-06-03 · IonQ · M&A, Lightsynq (interconnect, quantum memory, >20 patents) · undisclosed · Harvard/AWS founders · closed [C][566]
- 2025-09-17 · IonQ · M&A, Oxford Ionics · $1.075 B · — · closed [C][17]
- 2025-11-06 · DARPA · QBI Stage B · up to $15 M each · IonQ and Quantinuum among eleven [G][60]
- 2026-06-03 · Quantinuum · IPO, Nasdaq QNT · $1.68 B gross · — · closed [G][112]
- 2026-07-31 · IonQ · M&A, SkyWater Technology · ~$1.8 B · — · closed [C][18]

**Market & supply chain.** There is no market yet — four merchant detector houses and a few optics suppliers — and the largest natural customer owns one of the four. IonQ has bought the vertical: Lightsynq for interconnect and memory, ID Quantique for detectors, Oxford Ionics for gates, SkyWater for fabrication. Unit economics are not quotable. G6 pays directly; G4 pays as the way past single-trap ceilings; the rest do not.

**IP & standards.** The only dated IP fact is IonQ's statement that Lightsynq brought "over 20 patents and patent applications" in photonic interconnect and quantum memory — a company count with no family, assignees or filing years [C][566]. No named patent family was found for ion–photon link hardware; no standards body governs it.

**Roadmaps & track record.** IonQ (promised 2025-06 · 2 M physical, 40–80 k logical by 2030 · status 2026-09-03: needs an interconnect two orders faster than any published rate) [R][118]; its 2020 roadmap missed 4,000 qubits by 2026 by ~40×. Quantinuum (promised 2024-09 · Sol 2027, Apollo 2029 · no dated photonic-interconnect commitment) [R][117]; Helios launched on schedule, so its dates carry weight.

**Strategic reading.** If heralded links reach production rates the single-trap ceiling stops mattering and every ion vendor becomes modular; IonQ wins that world because it owns each layer, and merchant detector vendors lose their largest customer to a competitor. If rates stay put, Quantinuum wins by ignoring the node — in-trap transport at 4 m/s is already faster. Supplier power is negligible today and would rise only if link counts grew with module counts.

*Open niche:* a small QCVV/SFQ research company could define and run the unconditional benchmark this field lacks — rate × fidelity including heralding loss — and apply it to commercial claims that publish neither.

## Outlook & open questions

Confirm by end-2027 if any group publishes above 10³ s⁻¹, or IonQ discloses rate, fidelity and distance. Demote the networking-ready framing if by end-2028 nothing exceeds roughly 10× the 250 s⁻¹ record. Best case by 2029: cavity or waveguide collection plus telecom conversion reaches 10³–10⁴ s⁻¹ and a three-node network appears. Worst case: rates stay at 10²–10³ s⁻¹ and modular ion machines use in-trap transport instead. Open questions: what did IonQ's link achieve; does cavity enhancement cost interference visibility; can frequency conversion survive the fidelity budget?

## Sources

[17] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[18] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[106] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756). [D]
[108] D. Main *et al.*, “Distributed quantum computing across an optical network link,” *Nature*, vol. 638, no. 8050, pp. 383–388, Feb. 2025, doi: [10.1038/s41586-024-08404-x](https://doi.org/10.1038/s41586-024-08404-x). [D]
[109] J. O'Reilly *et al.*, “Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking,” *Phys. Rev. Lett.*, vol. 133, Art. no. 090802, Aug. 2024, doi: [10.1103/PhysRevLett.133.090802](https://doi.org/10.1103/PhysRevLett.133.090802). [arXiv:2404.16167](https://arxiv.org/abs/2404.16167). [D]
[112] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G]
[117] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[118] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[566] IonQ, “IonQ Completes Acquisition of Lightsynq, Accelerating Quantum Computing and Networking Roadmap,” Jun. 3, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-lightsynq-accelerating-quantum-computing-and [C]
[567] IonQ, “IonQ Achieves Key Photonic Interconnect Milestone, Demonstrating Networked Quantum Systems Using Entanglement,” Apr. 14, 2026. [Online]. Available: https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement [C]

## Open verification items

- IonQ's April-2026 milestone [567] discloses no rate, fidelity or distance, and its wording ("validated the generation, transmission, and detection of photons used to enable quantum entanglement") does not state that a Bell pair was measured.
- The 2007 first remote ion–ion entanglement is attributed here to Monroe's group (Michigan) on the technology-graph record's first-demonstration date; the original paper is cited from the standard literature without a numbered source.
- Lightsynq deal terms are undisclosed; the ">20 patents and patent applications" figure is IonQ's own count with no family names, assignees or filing years.
- ID Quantique's acquisition close date (2025-05-06) comes from the shared fact record for SNSPD vendors and carries no numbered source.
- No source reports an unconditional link metric (rate combined with fidelity including heralding loss), so the 94–97% figures and the 250 s⁻¹ figure cannot be combined into one number.
- No published design states a link count or switch-fabric topology for a 10⁴-module ion machine.
