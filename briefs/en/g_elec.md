---
id: g_elec
name: Electronic near-field microwave gate (ions, laser-free)
layer: "3 Gate mechanism"
status: demonstrated
since: 2024
one_line: Currents in a microfabricated trap chip entangle ions through microwave field gradients, with no laser and no ground-state cooling.
verdict: Holds the highest two-qubit fidelity measured on any modality (8.4×10⁻⁵ error) but only on chips of ≤10 qubits; demote if no ≥50-qubit device publishes gate time, heating and crosstalk by end-2027.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage

An entangling gate on hyperfine ion qubits driven entirely by currents in the trap chip. Oscillating currents in electrodes tens of micrometres from the ion produce a microwave field whose *gradient*, not its amplitude, couples spin to the shared motional mode; a state-dependent force closes a loop in phase space and imprints a geometric phase, as a Mølmer–Sørensen gate does, with a ~10 GHz field replacing two laser beams. Demonstrated at NIST Boulder in 2011 (76(3)%, 20 ns single-qubit pulses) [D][5], brought to useful fidelity at Oxford in 2016 with dynamically decoupled ⁴³Ca⁺ clock qubits [D][4], industrialised by Oxford Ionics — the Ballance/Harty spin-out of that group, part of IonQ since 2025 — as Electronic Qubit Control [C][6]. A parallel lineage at Sussex (Hensinger), its spin-out Universal Quantum, and eleQtron's MAGIC drives global microwave fields across a *static* gradient [P][9][10]; the near-field variant here holds the records.

Coordinates (technology graph):
- Carrier affinity: fully natural — the qubit is an atomic ion; only the trap is fabricated.
- Characteristic time: 2×10⁻⁴ s per entangling operation, deterministic, not heralded.
- Readout: not defined by this node; it inherits the host ion's fluorescence detection.
- Mobility: shared motional bus within a zone, ions transported between zones.
- Control modality and placement: microwave, sources at room temperature.
- Error structure as the code sees it: Pauli plus a coherent component.
- Manufacturing: microfabricated surface trap with buried current traces.

## Physics & limits

Gate rate is set by the microwave gradient at the ion and the Lamb–Dicke parameter; both are geometric. Halving the ion–electrode distance roughly doubles the gradient but raises anomalous heating steeply (surface noise near d⁻⁴), so speed is bought against motional decoherence — hence durations of 120–226 µs, not sub-microsecond. There is no photon-scattering floor, the dominant fundamental error of laser gates, which is why the achievable ceiling is higher [D][1].

What replaces it is a.c. Zeeman shift from the field's non-gradient component, magnetic-field noise, and residual spin–motion entanglement at finite temperature. The first two are attacked with clock qubits and dynamical decoupling [D][4]; the third bound everything until the 2025 "smooth gate", which ramps the gate detuning to adiabatically eliminate spin–motion entanglement and tolerate a hot mode — it ran at mean phonon number n̄ = 9.4(3), above the Doppler limit, with error ≲5×10⁻⁴ even hotter [D][1]. The residual error is largely coherent — miscalibrated phase and gradient amplitude — which a code sees as correlated rather than depolarising noise, so logical extrapolations assuming Pauli noise run optimistic. Moving the floor further needs lower trap-surface noise and better microwave amplitude and phase stability, not new physics.

## Engineering state of the art

Best demonstrated: two-qubit error 8.4(7)×10⁻⁵ (2025-10) on a laboratory chip [D][1]. Typical at scale: nothing above ten qubits is published — the 2024 device giving 99.97(1)% two-qubit and 99.99916(7)% single-qubit fidelity is a seven-zone chip controlling up to ten qubits [D][2]. That gap is the most important fact about this node.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2011 | First near-field microwave two-qubit gate, 76(3)% | NIST Boulder (Ospelkaus, Leibfried, Wineland) | [D][5] |
| 2016 | 99.7(1)% two-qubit, ⁴³Ca⁺ clock qubits, dynamically decoupled | Oxford (Harty, Lucas) | [D][4] |
| 2024-07 | 99.97(1)% two-qubit, 99.99916(7)% single-qubit, seven-zone chip, ≤10 qubits | Oxford Ionics | [D][2] |
| 2024-12 | Single-qubit error 1.5(4)×10⁻⁷ per Clifford, chip-integrated microwave resonator | Oxford (Lucas group) | [D][3] |
| 2025-10 | Two-qubit error 8.4(7)×10⁻⁵ at n̄ = 9.4(3), no ground-state cooling | Oxford Ionics / IonQ | [D][1] |

Dominant terms today: temperature-dependent residual spin–motion entanglement and coherent control error. The headline is an estimate from subspace-leakage randomized benchmarking, not tomography [D][1]. Gate duration is 225.8 µs in 2025 and ≈120 µs (two 60 µs pulses) in 2024 [D][1][2].

## Manufacturing, materials & supply chain

The trap is a surface-electrode chip with buried current-carrying traces and local tuning electrodes in a standard semiconductor process; IonQ's framing is that control lives on "classical semiconductor chips" built in "existing semiconductor fabs" [C][6]. That claim is now vertically integrated: IonQ closed the SkyWater Technology acquisition (~$1.8 B, announced 2026-01-26, closed 2026-07-31) [C][G:IONQ-SKYWATER-2026][12], giving it a US 200 mm trusted foundry instead of a merchant relationship. Packaging is the named weak point: Oxford Ionics uses Bay Photonics for the electrical, photonic and electrostatically shielded packaging of high-density trap devices [C][7]. No yield, uniformity, defect-density or per-qubit cost figure is published by any actor as of 3 Sep 2026. Export exposure runs through the US BIS interim final rule of 2024-09-06, which created ECCN 4A906 for quantum computers (34-qubit floor with error-rate tiers) plus 3A904/3B904 for enabling equipment [G:BIS-QUANTUM-2024][19]: a ≥34-qubit electronic-gate system meeting the error tiers falls inside it, and the UK-design/US-parent structure makes licensing a design constraint.

## Control, readout & I/O burden

A laser-gate machine of comparable ambition needs many wavelengths and per-zone optical addressing — Helios uses at least seven laser wavelengths and 1,228 electrodes [D][18]. The electronic gate deletes the gate lasers, leaving light only for cooling, state preparation and readout, and substitutes room-temperature microwave sources plus d.c. electrode drivers. Per-qubit I/O becomes a mixed-signal ASIC problem — coherent microwave channels and many d.c. lines — a familiar scaling exercise rather than an optical one.

The wall moves rather than disappears. At 10³ qubits it is the count of independent microwave channels and their phase coherence, since amplitude and phase errors are the leading coherent term. At 10⁴ it is routing current-carrying traces, with on-chip dissipation and zone-to-zone crosstalk; no actor has published a crosstalk or heating figure for a 2D array. At 10⁶ nothing in the public record connects this gate to a demonstrated 2D trap. Control-loop latency demands are modest — millisecond-class syndrome cycles suffice.

## Role in the stack

The node sits on the path "Trapped ions — electronic gates, chip control" (IonQ/Oxford Ionics, eleQtron, Quantum Art). It requires a trapped atomic ion as carrier and chip-integrated microwave control as signal source; it provides nothing downstream that the laser gate does not, and directly replaces the laser Mølmer–Sørensen gate. The switching price is one-directional: buried traces and electrode geometry are co-designed with the gate, so an electronic-gate machine cannot fall back to lasers, while a laser machine can in principle add microwave electrodes. The off-diagonal reading is a natural, unfabricated carrier steered by purely electronic control — a semiconductor supply chain driving an atomic qubit. Contribution to the derived clock: 2.3×10⁻⁴ s per entangling gate. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset for the path ≈1.5×10⁻³ s, gate layers 1.4 ms of it; on a multi-zone machine transport dominates instead (Helios ~55 ms per full-width layer [D][18]), so the gate's speed advantage is invisible at product scale. The neighbouring empty slot is the cryogenic version: nothing published combines electronic gates with a cryogenic trap, which is where the heating-versus-gradient trade would be won.

## Verification (QCVV)

The headline 8.4(7)×10⁻⁵ comes from subspace-leakage randomized benchmarking at Doppler temperature, not from tomography or interleaved RB against an independent reference [D][1]. Two-qubit RB twirls coherent errors into an effective depolarising rate, understating the coherent residual, and says nothing about crosstalk to spectator ions — the term that will decide performance at scale. No independent group has replicated the electronic gate above 99.9%: the 2016 Oxford [D][4] and 2011 NIST [D][5] results are the only non-Oxford-Ionics near-field microwave gates on record, and neither eleQtron nor Universal Quantum has published a comparable fidelity as of 3 Sep 2026. The company line "99.99% two-qubit gate fidelity" [C][6] rounds the preprint's 1 − 8.4(7)×10⁻⁵ — consistent, but with no error bar and no width.

## Actors & economics

**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| IonQ | developer | US | Owns Oxford Ionics and its Electronic Qubit Control line; holds the gate record | [D][1] [C][6] |
| Oxford Ionics | developer | UK | Designs the trap chips and ran both record experiments | [D][1][2] |
| eleQtron | developer | DE | MAGIC static-gradient microwave ion control; €57 M Series A, >€54 M backlog | [P][G:ELEQTRON-57M-2026-05][8][9] |
| Universal Quantum | developer | UK | Sussex spin-out; modular microwave machines under a German state contract | [P][10] |
| University of Oxford | research | UK | Lucas group: single-qubit 1.5(4)×10⁻⁷ with a chip-integrated microwave resonator | [D][3] |
| NIST Boulder | research | US | Originated the near-field microwave gate in 2011 | [D][5] |
| NQCC | user | UK | Hosts the Oxford Ionics "Quartet" system; 2D trap upgrade | [C][7] |
| Innovate UK | funder | UK | Quantum Missions Pilot award for the 2D trap upgrade, value undisclosed | [C][7] |
| SkyWater Technology | supplier | US | 200 mm US foundry, acquired by IonQ to fabricate trap chips in-house | [C][G:IONQ-SKYWATER-2026][12] |
| Bay Photonics | supplier | UK | Packaging of high-density trap devices | [C][7] |
| DARPA | evaluator | US | QBI: Oxford Ionics in Stage A, IonQ carried into Stage B | [G:QBI-STAGEA-2025-04][14] [G:QBI-STAGEB-2025-11][15] |

**Money.**
- 2022-11-02 · Universal Quantum · contract · €67 M · German Aerospace Center (DLR); two machines in four years, multi-chip system up to 100 qubits · — · announced [P][10]
- 2025-03-11 · Oxford Ionics · programme award (Quantum Missions Pilot, "Q-Surge") · undisclosed · DSIT and Innovate UK · — · announced [C][7]
- 2025-04-03 · Oxford Ionics · DARPA QBI Stage A selection · — · DARPA · — · selected [G:QBI-STAGEA-2025-04][14]
- 2025-09-17 · IonQ · M&A, Oxford Ionics (announced 2025-06-09) · $1.075 B · — · — · closed [C][G:IONQ-OXIONICS-2025][11]
- 2025-10-12 · IonQ · equity · $2.0 B at $93/share, after $1.0 B on 2025-07-08 · — · cash $3.0 B · closed [C][G:IONQ-EQUITY-2025][13]
- 2025-11-06 · IonQ · DARPA QBI Stage B selection, up to $15 M each · — · DARPA · — · selected [G:QBI-STAGEB-2025-11][15]
- 2026-04-27 · Quantum Art · Series A extension · $140 M, from $100 M on 2025-12-10 · — · — · closed [P][G:QART-140M-2026-04][17]
- 2026-05-05 · eleQtron · Series A · €57 M · Schwarz Digits lead, with EIC Fund, Earlybird, Ankaa Ventures, Precitec, NRW.BANK · backlog >€54 M · closed [P][G:ELEQTRON-57M-2026-05][8][9]
- 2026-07-31 · IonQ · M&A, SkyWater (announced 2026-01-26) · ~$1.8 B · — · — · closed [C][G:IONQ-SKYWATER-2026][12]
- 2026-Q2 · IonQ · revenue · $80.1 M, +287% YoY; FY guidance $280–290 M · — · cash $3.0 B · reported [C][G:IONQ-EQUITY-2025][13]

**Market & supply chain.** There is no merchant market for electronic ion gates. The enabling assets are trap-chip fabrication (in-house at IonQ via SkyWater), microwave sources and amplifiers (commodity RF, low concentration risk) and specialist packaging — Bay Photonics is a genuine single point of failure for the UK line. Concentration risk is corporate rather than industrial: one company holds the record, the patents and the fab. Unit economics are unquotable; nobody publishes cost or power per qubit. The goals that pay for it are G3 (early fault tolerance) and G7 (deployable systems): the case for deleting gate lasers is manufacturability and field-deployability, not speed. G6 is untouched — the node provides no photonic interface.

**IP & standards.** Oxford Ionics describes Electronic Qubit Control as patented [C][6], and the $1.075 B acquisition price is best read as a purchase of that portfolio plus the team; no patent family number, database-sourced count or litigation could be verified as of 3 Sep 2026 (Google Patents assignee search is robots-blocked). No standards body or consortium is specific to this gate.

**Roadmaps & track record.** (promised on · promised for · status as of 2026-09-03): IonQ, 2025-06-13 · 256 qubits at 99.99% in 2026 · slipped to commissioning in H1 2027 [R][G:IONQ-ROADMAP][16]. IonQ, 2025-06-13 · 10,000 physical qubits on one chip in 2027 and 2 M physical / 40–80 k logical by 2030 · no 2D-trap heating, gate-time or interconnect data published [R][G:IONQ-ROADMAP][16]. Universal Quantum, 2022-11-02 · two machines including up to 100 qubits within four years · no delivery announced as the term elapses [P][10]. Credibility: Oxford Ionics' physics claims have held and improved on schedule; IonQ's *scale* promises have not — the 2020 roadmap's 4,000 qubits by 2026 missed by roughly 40× — so read fidelity commitments as credible and qubit-count dates as aspirational.

**Strategic reading.** If the electronic gate scales, IonQ converts a physics lead into a manufacturing lead and the optical supply chain for ions loses its strongest customer class; Quantinuum's advantage narrows to systems engineering and error correction rather than gate quality. If it stalls at a few tens of ions, the record becomes a laboratory curiosity and laser gates with integrated photonics win on demonstrated width. Bargaining power sits with the platform vendor: nothing in the chain is scarce except packaging know-how, and IonQ has internalised the fab.

*Open niche:* the measurement gap here is a QCVV gap. The headline rests on randomized benchmarking that twirls away the coherent errors this gate carries, and no public protocol characterises microwave crosstalk to spectator ions in a multi-zone chip. A small group could supply coherent-error-sensitive benchmarking (cycle benchmarking, gate-set tomography on the two-qubit block) and could independently audit the 99.99% claim.

## Outlook & open questions

Confirm-or-demote milestones for 12–24 months: a device above ~30 electronic-gate qubits with published two-qubit fidelity, gate time and crosstalk (absent by end-2027, demote); IonQ's 256-qubit system commissioned in H1 2027 near 99.99%; any independent replication above 99.9%; a 2D trap running electronic gates with published heating rates. Best case by 2029: chip-trap machines of a few thousand ions, laser hardware reduced to cooling and readout, fidelity near 10⁻⁴, error correction limited by transport rather than gates. Worst case: fidelity degrades by an order of magnitude once hundreds of microwave channels share a die, and the platform reverts to laser gates for addressing.

Open questions: does the microwave gradient survive dense 2D routing without unacceptable crosstalk and dissipation? How much of the residual 8.4×10⁻⁵ is coherent, and what does that do to Λ? Does SkyWater's process yield trap chips at volume, or was the acquisition supply security rather than capability?

## Sources

[1] A. C. Hughes, R. Srinivas, C. M. Löschnauer, H. M. Knaack, R. Matt, C. J. Ballance, M. Malinowski, T. P. Harty, R. T. Sutherland — "Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling" — arXiv:2510.17286 — 2025-10-20 — https://arxiv.org/abs/2510.17286
[2] C. M. Löschnauer, J. Mosca Toba, A. C. Hughes, S. A. King, M. A. Weber, R. Srinivas, R. Matt, R. Nourshargh, D. T. C. Allcock, C. J. Ballance, C. Matthiesen, M. Malinowski, T. P. Harty — "Scalable, high-fidelity all-electronic control of trapped-ion qubits" — arXiv:2407.07694 (2024-07-10); PRX Quantum 6, 040313 (2025) — https://arxiv.org/abs/2407.07694
[3] M. C. Smith, A. D. Leu, K. Miyanishi, M. F. Gely, D. M. Lucas — "Single-qubit gates with errors at the 10⁻⁷ level" — arXiv:2412.04421 — 2024-12-05 — https://arxiv.org/abs/2412.04421
[4] T. P. Harty, M. A. Sepiol, D. T. C. Allcock, C. J. Ballance, J. E. Tarlton, D. M. Lucas — "High-fidelity trapped-ion quantum logic using near-field microwaves" — Phys. Rev. Lett. 117, 140501 (arXiv:1606.08409) — 2016-06-27 — https://arxiv.org/abs/1606.08409
[5] C. Ospelkaus, U. Warring, Y. Colombe, K. R. Brown, J. M. Amini, D. Leibfried, D. J. Wineland — "Microwave quantum logic gates for trapped ions" — Nature 476, 181 (arXiv:1104.3573) — 2011 — https://arxiv.org/abs/1104.3573
[6] IonQ — "IonQ Achieves Landmark Result, Setting New World Record in Quantum Computing Performance" — IonQ newsroom [C] — 2025-10-21 — https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing
[7] Oxford Ionics — "Oxford Ionics selected for Quantum Missions Pilot to upgrade NQCC testbed with advanced 2D ion traps" [C] — 2025-03-11 — https://www.oxionics.com/announcements/oxford-ionics-selected-for-quantum-missions-pilot-to-upgrade-nqcc-testbed-with-advanced-2d-ion-traps/
[8] eleQtron — "eleQtron secures €57 million in one of the largest Series A funding rounds worldwide" [C] — 2026-05-05 — https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/
[9] Quantum Computing Report — "eleQtron Secures €57 Million Series A to Scale MAGIC Trapped-Ion Platform" [P] — 2026-05 — https://quantumcomputingreport.com/eleqtron-secures-e57-million-61-5m-usd-series-a-to-scale-ion-trap-systems/
[10] University of Sussex — "German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract" [P] — 2022-11-02 — https://www.sussex.ac.uk/broadcast/read/59206
[11] IonQ — "IonQ Completes Acquisition of Oxford Ionics" [C] — 2025-09-17 — https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum
[12] IonQ — "IonQ Completes Acquisition of SkyWater Technology" [C] — 2026-07-31 — https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
[13] IonQ — "IonQ Announces Record Second Quarter 2026 Revenues" [C] — 2026 — https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy
[14] DARPA — "Companies targeting quantum computers" (QBI Stage A roster) [G] — 2025-04-03 — https://www.darpa.mil/news/2025/companies-targeting-quantum-computers
[15] DARPA — QBI Stage B selection [G] — 2025-11-06 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[16] IonQ — "IonQ's accelerated roadmap" [R] — 2025-06-13 — https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality
[17] Quantum Computing Report — "Quantum Art extends Series A to $140M" [P] — 2026-04-27 — https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/
[18] Quantinuum — Helios — arXiv:2511.05465; Nature (2026-06) — https://arxiv.org/abs/2511.05465
[19] US Bureau of Industry and Security — interim final rule adding quantum ECCNs 4A906, 3A904, 3B904 [G] — 2024-09-06 — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent

## Open verification items
- Gate duration for the 2025 record (225.8 µs) is not stated in the abstract of arXiv:2510.17286 and could not be confirmed in the retrievable text; unverified.
- Ion species and trap zone count for arXiv:2510.17286 not stated in the retrievable text (the 2024 predecessor uses a seven-zone chip).
- No patent family number or database-sourced patent count for Oxford Ionics / IonQ Electronic Qubit Control: patents.google.com assignee search is blocked by robots.txt.
- Universal Quantum's €67 M DLR contract (four-year term from 2022-11) has no published delivery or milestone confirmation as of 2026-09-03.
- eleQtron publishes no ion species, qubit count, fidelity or gate time; MAGIC is described only qualitatively.
- Value of the Innovate UK / DSIT Quantum Missions Pilot award to Oxford Ionics is undisclosed.
- No crosstalk, heating-rate or on-chip dissipation figure has been published for any electronic-gate trap chip.
