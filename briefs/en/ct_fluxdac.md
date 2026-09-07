---
id: ct_fluxdac
name: On-chip flux-DAC multiplexing
layer: "5 Control"
status: demonstrated
since: 2026
one_line: SFQ on-chip flux digital-to-analog converters that hold each qubit's or coupler's DC bias at the mK stage, replacing one room-temperature wire per bias with a multiplexed on-chip network.
verdict: Proven at 200–300 bias wires for a several-thousand-qubit annealer; the January 2026 fluxonium result is one device with coherence but no gate fidelity, no crosstalk matrix and no peer review.
updated: 2026-09-03
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
An on-chip flux DAC (Φ-DAC) is an SFQ circuit on the mK stage that latches the DC flux bias of one qubit or coupler. SFQ pulses push flux quanta (Φ₀ = h/2e) into a superconducting storage loop, which holds the bias indefinitely with no static dissipation and no room-temperature wire. D-Wave has shipped this in annealers for over a decade; the first gate-model application, a flip-chip fluxonium module, came in January 2026 [D][1][C][2].
Coordinates: fabricated control layer with no intrinsic gate or readout channel; low-frequency bias at the mK stage.
Error structure is coherent — bias-setting error, crosstalk, drift — not relaxation; fabrication is superconducting multilayer lithography.

## Physics & limits
The scaling argument is about duty cycle, not power efficiency. Each switching event dissipates ~I_cΦ₀, but a flux bias is reprogrammed on a calibration cadence, not a gate cadence, so thousands of latched channels sit quiescent inside a millikelvin budget that could not host one continuously driven line — unlike SFQ gate control, which pulses at circuit rates. A resource review puts SFQ control at ~1.6 µW/qubit against 2–23 mW/qubit for 4 K cryo-CMOS [S][11][G:CRYOCMOS-POWER-CONFLICT].
The floor is bias resolution and stability, not coherence. The least significant flux step fixes a residual detuning; thermal cycling and trapped vortices move the working point; and every stored quantum couples magnetically to its neighbours, which is where crosstalk originates. Moving the floor needs energy-efficient SFQ families (ERSFQ/eSFQ) without static bias resistors, finer quantization, and shielding that keeps the DAC network's fields off the qubit chip.

## Engineering state of the art
| Year | Figure | Who | Tag/key |
|---|---|---|---|
| 2025-05-20 | Advantage2 GA: 4,400+ qubits, Zephyr degree-20, 12.5 kW | D-Wave | [C][G:DWAVE-FIN-2026] |
| 2026-01-06 | "200 bias wires" for tens of thousands of qubits and couplers; parts made at NASA JPL | D-Wave | [C][2] |
| 2026-01-23 | Flip-chip fluxonium + Φ-DAC: T1 ≈ 200 µs, T2* ≈ 20 µs at 10 mK, no added decoherence resolved | D-Wave | [D][1] |
| 2026-03-10 | SFQ control co-integrated with qubits, 1Q > 99% (peak 99.9%) — gate, not flux, control | SEEQC | [D][4][G:SEEQC-MK-SFQ-2026-03] |
| 2026-03-16 | 14 nm cryo-CMOS flux-bias ASICs on 156-qubit Heron R2, 2Q error ≈ 2.3×10⁻³ (rival) | IBM | [C][5][G:IBM-CRYOCMOS-FLUX-2026-03] |

The annealer ratio is deployed; the gate-model result is one qubit, with coherence but no gate fidelity.

## Manufacturing, materials & supply chain
The package bump-bonds a "high-coherence, minimal fabrication" qubit chip to a multilayer control chip across a ~7 µm gap [D][1]. The supply chain is the exposure: key components were fabricated at NASA's Jet Propulsion Laboratory [C][2] — a government laboratory, not a merchant foundry. D-Wave's 10-Ks state fabrication at "existing third-party foundries" with a second source demonstrated; EDGAR search returns nine "SkyWater" hits in its 2023–2026 filings [G][12]. Export exposure is asymmetric and favours SFQ: ECCN 3A901.a controls CMOS ICs *designed* for ≤4.5 K — a design-intent test capturing a cryo-CMOS design file — while no ECCN names superconducting digital logic; only the finished ≥34-qubit machine is caught, under 4A906 [G][10][G:BIS-3A901A-CRYOCMOS].

## Control, readout & I/O burden
The node breaks the one-wire-per-bias law: 200–300 bias wires serve several thousand annealer qubits and tens of thousands of couplers [C][1][2]. Annealer biases are set per program and structurally homogeneous, whereas a gate-model processor retunes per-qubit and per-coupler biases against a drifting calibration. Line count is not the only I/O: bump-bond count, readout and microwave drive are untouched. SFQ pulses are picosecond-scale, so updates are fast; settling time and neighbour disturbance are unpublished. At 10³ D-Wave already operates; at 10⁴ the ~200–300 lines is an annealer ratio, not a fluxonium one; at 10⁶ no path is described and bond density, not wire count, binds.

## Role in the stack
This Control-layer node underlies the quantum-annealing path (D-Wave) and requires superconducting Nb/Al junction lithography and SFQ digital logic at the mixing-chamber stage — the DAC is an SFQ flux-storage loop, so the node hangs off SFQ digital control (ct_sfq) and gives that node its second carrier family; off-diagonally it shares cold-stage fabrication capacity. It replaces room-temperature control lines. The switching cost is a second die, flip-chip bond yield as a new failure mode, and loss of arbitrary waveform shaping on the biased node — bandwidth traded for wire count. Flux biases are quasi-static, so this node adds no term to derived clock = sum of the syndrome round: gate layers + transport + readout + reset; the annealing path runs no syndrome round in any case, its cadence being calibration, not circuit, and no figure is quotable. Its empty downstream fan-out understates the case: every superconducting roadmap above ~10³ qubits meets this wall.

## Verification (QCVV)
T1 (relaxation) and T2* (Ramsey) were measured on the single Φ-DAC-controlled fluxonium against a conventional control-line baseline. The comparison has limited sensitivity: T2* ≈ 20 µs is already an order of magnitude below T1 ≈ 200 µs, so "no resolvable increase" bounds rather than measures the DAC's flux noise. Unpublished: any crosstalk matrix, bias drift across thermal cycles, or gate fidelity. The source is a company whitepaper, not peer-reviewed, and unreplicated. Value conflict: D-Wave says 200 bias wires (2026-01-06) [C][2] and ~300 (2026-01-23) [D][1]; the whitepaper's figure is tied to a described array.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| D-Wave | developer | CA | Originated Φ-DAC multiplexing; first fluxonium demo | [D][1][C][2] |
| NASA JPL | supplier | US | Fabricated key components of the module | [C][2] |
| SEEQC | developer | US | SFQ control chips; owns a multilayer superconductor foundry | [D][4] |
| IBM | developer | US | Rival 14 nm cryo-CMOS flux-bias ASIC on Heron R2 | [C][5] |
| US Dept of Commerce | regulator | US | $100 M CHIPS LOI to D-Wave; BIS sets 3A901.a and 4A906 | [G][9][10] |

**Money.**
2026-01-20 · D-Wave · M&A, Quantum Circuits Inc. · $550 M ($300 M stock + $250 M cash) · closed [C][7][G:DWAVE-QCI-2026-01]
2026-05-21 · D-Wave · CHIPS letter of intent · $100 M · US DoC, $2.013 B package · LOI [G][9][G:CHIPS-LOI-2026-05]
2026-05-26 · SEEQC · SPAC registration, Allegro Merger Corp. · $75 M offering + $65 M PIPE, ~$1 B EV · filed, not closed [G][8][G:SEEQC-S4-TERMS-2026-05]; SPAC merger terminated 2026-08-25 [G:SEEQC-SPAC-TERMINATED-2026-08]
2026-08-06 · D-Wave · H1-2026 revenue $5.9 M (−67% YoY), cash $546.2 M · reported [C][6][G:DWAVE-FIN-2026]

**Market & supply chain.** The scarce input is multilayer niobium capacity: SkyWater as merchant option (quantum ATS revenue +30% YoY on FY2025 revenue $442.1 M [G][13]), SEEQC's own Elmsford line, JPL as a government facility with no commercial throughput. No $/channel figure is disclosed. G7 pays most directly; G3/G4 only if the fluxonium route generalizes.

**IP & standards.** No dated patent family specific to on-chip flux-DAC circuits was found; D-Wave's annealer control IP predates this window. SEEQC's SFQ portfolio descends from over $100 M of prior Hypres investment [P][G:SEEQC-FUNDING]. No standards activity identified.

**Roadmaps & track record.** D-Wave gate model: 17 physical qubits (promised 2026-06-01 · for 2026 · reaffirmed 2026-08-06, undelivered as of 4 Sep 2026), then 49 (2027), 181 (2028), 100 logical (2032), Λ = 10 [R][7]. Advantage2 GA (promised for 2025 · delivered 2025-05-20) is the clean delivery [C][14]. Against that, H1-2026 revenue fell 67% and the CFO resigned 2026-08-25 [C][6]: the pivot runs on cash, not the business. SEEQC's 2026 listing is filed, not closed.

**Strategic reading.** Three answers compete for one wiring wall: on-chip SFQ Φ-DACs (D-Wave), 4 K cryo-CMOS DACs (IBM, HRL), and needing fewer lines at all — the Shenzhen unified XY+Z architecture drives both through one room-temperature channel per fluxonium at 99.99% 1Q fidelity on eight devices [D][3]. That third route is the underrated threat: no cryogenic hardware, and it reports the gate metric the Φ-DAC work omits. If Φ-DACs generalize, D-Wave and Nb foundries gain and room-temperature rack vendors lose per-qubit channel revenue.

*Open niche:* the open gap is a vendor-neutral characterisation of a multiplexed Φ-DAC network — crosstalk matrix, settling time, drift across thermal cycles, gate fidelity — on a protocol that also runs against a cryo-CMOS DAC. No vendor publishes it; it needs SFQ design literacy rather than capital.

## Outlook & open questions
Milestones (12–24 months): D-Wave publishes a multi-qubit Φ-DAC result with a crosstalk matrix and gate fidelity (confirm); the 17-qubit 2026 gate-model target ships (confirm); an outside group replicates the coherence result on a second device (confirm) — or the fluxonium line stays a single-device whitepaper through 2027 (demote). Best case 2029: Φ-DAC control of hundreds of independently tuned gate-model qubits, crosstalk below the gate-error budget, adopted outside D-Wave; worst case, proven only for a homogeneous annealer array while cryo-CMOS or line-reduction takes the gate-model market. Open: crosstalk and drift at scale; whether bump-bond density becomes the real wall. Watch: D-Wave's next fluxonium publication, SEEQC's closing, an SFQ-vs-cryo-CMOS comparison.

## Sources
[1] D-Wave, "Digital Control of High-Coherence Fluxonium Qubits," technical whitepaper 14-1090A-A, 2026-01-23 [D] — https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf
[2] D-Wave, "D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits," press release, 2026-01-06 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/
[3] Pan, Wang, Zhou et al. (Quantum Science Center of Guangdong–Hong Kong–Macao Greater Bay Area, Shenzhen), "Unified Flux Control Architecture for Fluxonium Qubits," arXiv:2605.25948, 2026-05-26 [D] — https://arxiv.org/html/2605.25948v1
[4] Jordan, Bernhardt, Rahamim, Kirichenko et al. (SEEQC), "A quantum computer controlled by superconducting digital electronics at millikelvin temperature," Nature Electronics, 2026-03-10 [D] — https://www.nature.com/articles/s41928-026-01576-6
[5] IBM Research, "A cryo-CMOS control system for large-scale superconducting qubit quantum computing, Part 2," APS Global Physics Summit abstract, 2026-03-16 [C] — https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2
[6] D-Wave, "D-Wave Reports Second Quarter 2026 Results," 2026-08-06 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/
[7] D-Wave, "D-Wave to Acquire Quantum Circuits Inc.," press release, 2026-01-07 [C] — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[8] SEEQC / Allegro Merger Corp., SEC registration statement, filed 2026-05-26 [G] — https://www.sec.gov/Archives/edgar/data/1779977/000121390026061108/ea0278139-04.htm
[9] US Dept of Commerce / NIST, "Department of Commerce Announces Letters of Intent with 9 Companies," 2026-05-21 [G] — https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[10] US BIS, Commerce Control List additions implementing controls on quantum computing items (ECCNs 3A901, 3A904, 3B904, 4A906), Federal Register, effective 2024-09-06 [G] — https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies-consistent
[11] Kawabata et al., cryogenic control resource review, arXiv:2601.03922, 2026-01-08 [S] — https://arxiv.org/abs/2601.03922
[12] D-Wave, EDGAR full-text search for "SkyWater" in D-Wave 10-K filings 2023–2026 [G] — https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982
[13] SkyWater Technology, FY2025 results (fiscal year ended 2025-12-28), SEC exhibit 99.1, 2026-02-26 [G] — https://www.sec.gov/Archives/edgar/data/1819974/000181997426000005/skyt-20251228xex991.htm
[14] The Quantum Insider, "D-Wave Announces General Availability of Advantage2," 2025-05-20 [P] — https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/

## Open verification items
D-Wave states 200 bias wires (press release, 2026-01-06) and ~300 bias lines (whitepaper, 2026-01-23) for the same annealer control scheme; unreconciled. No crosstalk matrix, settling time, drift or gate fidelity has been published for the Φ-DAC-controlled fluxonium beyond the single-device T1/T2* comparison, and no independent replication was found. The SkyWater–D-Wave foundry relationship rests on an EDGAR full-text hit count, not a quoted sentence. JPL's role is described only as "key components," with no scope, capacity or contract terms disclosed. No ECCN names superconducting digital logic; whether an SFQ control die is caught by a catch-all is untested.
