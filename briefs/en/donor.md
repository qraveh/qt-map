---
id: donor
name: Donor spin (P in ²⁸Si)
layer: 1 Carrier
status: demonstrated
since: 2012
one_line: Phosphorus donors placed by STM lithography in enriched silicon-28, the bound electron giving drive and readout, the ³¹P nucleus the long-lived qubit.
verdict: Highest published per-gate fidelities in silicon, but a serial atom-by-atom write process and a single practitioner cap the register at eleven qubits with no dated parallelisation scheme.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A single ³¹P donor placed atom-by-atom in enriched ²⁸Si: the bound electron gives drive and spin-to-charge readout, the spin-1/2 ³¹P nucleus the memory. Nuclear qubits inside a register are gated through their hyperfine coupling to a *shared* electron; registers are linked by electron exchange [D][1]. Kane proposed the architecture in 1998; UNSW's Simmons group built the first deterministically placed single-donor device in 2012 [D][2]; SQC, its 2017 spin-out, is the sole operator at device scale as of 4 Sep 2026.
Attributes: natural dopant at engineered placement, static, deterministic entangling near 1 µs; spin-to-charge readout ~10 µs, non-destructive and mid-circuit capable; Pauli error; STM fabrication, no foundry equivalent.

## Physics & limits
The qubit is a nucleus, not a confined electron: with no orbital degree of freedom there is no first-order charge-noise coupling — the term that plateaus gate-defined dots at 99.0–99.6%. But every operation routes through the one electron that does couple to charge noise, which is coupler, readout probe and dominant error source at once; the budget is set by electron dephasing during the hyperfine-conditional pulse, not by nuclear coherence. Residual ²⁹Si and the regrown STM interface set that electron's T₂. A sharper tip will not move the floor: exchange varies exponentially with separation, so a donor mis-sited by a few nm gives a dead register.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2012 | first deterministically placed single-donor device | UNSW | [D][2] |
| 2025-12-17 | 11 qubits (9 nuclear, 2 electron ancilla), gates 99.10–99.99%, Bell to 99.5%, GHZ over eight nuclei | SQC | [D][1] |

Dominant term: register size and the electron-mediated gate. The main report's single "99.90% donor nuclear CZ" is not isolable from this work [D][1].

## Manufacturing, materials & supply chain
Serial by construction: one tip, one site, so throughput is qubit-hours, not wafer-hours; no parallel exposure is published. Enriched ²⁸Si is dual-sourced as of 4 Sep 2026 — ASP Isotopes' Pretoria line since 2025-03, US DOE silane at 99.9999% ²⁸Si from 2026-07-16 [P][3] — so feedstock is not the constraint. Suppliers: SkyWater for US resonators [C][4], Bluefors for cryogenics [C][5]. The single point of failure moved in 2026: IonQ closed its ~USD 1.8 B purchase of SkyWater on 2026-07-31 [G][6], putting SQC's only named US manufacturing route inside a competitor. Export exposure is nil today — 4A906 bites only above 34 qubits [G][7]. Wiring is not the wall; the write step is.

## Role in the stack
Requires STM hydrogen lithography; provides the carrier for exchange links and spin-to-charge readout; substitutes for gate-defined dots at the cost of the whole process flow. Its clock contribution is not distinctive — µs gates and ~6 µs readout match dot spins, so sum of the syndrome round: gate layers + transport + readout + reset is 7.7 µs against their 8.5 µs, and the real bottleneck is a manufacturing quantity the clock cannot express. Verification: one group, one device, no replication, three inconsistent fidelity framings [D][1].

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do | Evidence |
|---|---|---|---|---|
| SQC | developer | Australia | Sole STM donor fabricator, 11-qubit processor | [D][1] |
| SkyWater Technology | supplier | USA | Resonators, packaging | [C][4] |
| IonQ | supplier | USA | Owns SkyWater since 2026-07-31 | [G][6] |

**Money.** 2025-11-06 · SQC · QBI Stage B award · up to USD 15 M · DARPA · awarded [G:QBI-STAGEB-2025-11]. 2026-03-24 and 2026-06-11 · SQC · equity · A$60 M combined · Australia's NRFC · closed [G:SQC-NRFC-2026]. 2026-07-31 · IonQ · acquisition of supplier SkyWater · ~USD 1.8 B · closed [G][6].

**Market & supply chain.** No merchant sells an STM placement tool: SQC's asset is know-how, so no second source can be bought. ²⁸Si is the one input with two suppliers [P][3]; cost per donor is unpublished. Pays into G2 and G3 on fidelity, not count.

**IP & standards.** Foundational patents trace to the UNSW/Simmons line; no dated family count from a named database as of 4 Sep 2026.

**Roadmaps & track record.** SQC (2026-06 · commercial scale by 2033 [R][G:SQC-NRFC-2026] · unmet; 11 qubits is the maximum published). It delivers what it publishes, but 2033 presumes a parallelisation scheme absent from the literature — unfalsifiable rather than aggressive.

**Strategic reading.** If donor spins win, they win as a precision register bolted onto a foundry dot array, and SQC captures little of it: it owns the write process, not the wafer. Acute risk: a competitor owns its US packaging supplier.

*Open niche:* SQC is the sole fabricator, so no second lab can cross-check its devices; independent QCVV separating placement variance from gate and readout error is a service only an outsider can supply.

## Outlook & open questions
Confirm/demote (12–24 months): a device beyond 11 qubits or a dated parallel-write scheme confirms; silence through 2028 demotes this to a physics testbed. Best case 2029: a few dozen donor qubits above 99.5%. Worst case: eleven remains the record. Open: (1) can hydrogen-resist patterning be parallelised; (2) does SkyWater's new owner keep the relationship; (3) does QBI Stage C fund SQC; (4) what is the placement-yield distribution.

## Sources
[1] H. Edlbauer *et al.*, “An 11-qubit atom processor in silicon,” [arXiv:2506.03567](https://arxiv.org/abs/2506.03567), Jun. 2025. [D]
[2] M. Fuechsle *et al.*, “A single-atom transistor,” *Nat. Nanotechnol.*, vol. 7, no. 4, pp. 242–246, Apr. 2012, doi: [10.1038/nnano.2012.21](https://doi.org/10.1038/nnano.2012.21). [D]
[3] U.S. Department of Energy, “DOE Advances Domestic Supply of Silicon, Germanium Isotopes for Quantum Computing,” HPCwire, Jul. 16, 2026. [Online]. Available: https://www.hpcwire.com/off-the-wire/doe-advances-domestic-supply-of-silicon-germanium-isotopes-for-quantum-computing/ [P]
[4] Silicon Quantum Computing, “SkyWater x SQC: Advancing Hybrid Quantum-Classical Computing,” Nov. 20, 2025. [Online]. Available: https://sqc.com/news/skywater-and-sqc-advancing-hybrid-quantum-classical-computing [C]
[5] Silicon Quantum Computing, “Silicon Quantum Computing — News,” sqc.com. [Online]. Available: https://sqc.com/news/ [C]
[6] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[7] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]

## Open verification items
- The main report's "99.90% donor nuclear-spin CZ" is not isolable from [1]; preprint (99.5–99.99%) and published (99.10–99.99%) framings also differ. Treated here as a range.
- No placement-yield or cost-per-donor figure published by any actor.
- Firgun Ventures' amount undisclosed; the A$60 M NRFC total's two tranches are not itemised on SQC's own pages.
- No SQC statement located on the consequences of IonQ acquiring SkyWater.
