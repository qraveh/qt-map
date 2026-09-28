---
id: ic_fanout
name: Cryogenic signal fan-out for spin arrays (router die, 3-D stacked wiring)
layer: "9 Interconnect"
status: emerging
since: 2025
one_line: "A millikelvin router die, an on-die multiplexer or 3-D stacked wiring that turns a few cold input lines into the tens to thousands of gate voltages a spin-qubit array needs."
verdict: "The parts exist — Intel's 64-terminal Pando Tree, Quantum Motion's 1,024-dot multiplexed chip, Delft's 648-device demultiplexer — but no gate fidelity measured through a millikelvin router has been published as of 2026-09-26, and at Delft's ~1.25 µW per generated voltage a milliwatt of millikelvin cooling holds ~800 voltages: 10³ qubits only with shared control."
updated: 2026-09-26
---

MXC = mixing chamber, the coldest refrigerator stage; SET = single-electron transistor; DRAM = dynamic random-access memory; FinFET = fin field-effect transistor; 22FDX = GlobalFoundries' 22 nm fully depleted silicon-on-insulator process; PDK = process design kit; Rent's rule T = t·g^p (T terminals, g components, t terminals per component, p the Rent exponent); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Every gate of a spin qubit is a line. Fan-out routes the few lines a refrigerator carries to those gates: a router die at the MXC (Intel), multiplexers on the qubit die (Quantum Motion, Equal1), or qubit chip and control electronics stacked vertically (Hitachi). Vandersypen et al. (2017) judged wiring ~10⁸ sub-100 mK qubits to room temperature "impractical" and put electronics beside the qubits [D][761]. Li et al. shared the lines — "the control lines define the qubit grid" [D][762]; Schaal et al. and Paquelet Wuetz et al. put CMOS switches at millikelvin [D][763][D][764]. Intel described Pando Tree on 2024-06-20 [C][272]; the register's first dated fan-out record is from 2025.
Attributes: static interconnect; low-frequency signals at mK and 4 K; coherent error; CMOS fabrication.

## Physics & limits
Lines. In 2019 every platform wired each qubit directly, p = 1, against 0.36 for Intel's x86 processors; in Franke et al.'s example an added spin qubit costs two gates, t = 2 [D][765] — 2×10⁶ lines at g = 10⁶. A crossbar gives T = 6√g − 1, 23 terminals for 16 dots [D][520], ~6×10³ at 10⁶ [S]. At a 90 nm gate pitch [D][197] routing must happen on or beside the die.
Heat. Large dilution refrigerators give "beyond 1 mW at 100 mK" [D][761]. Delft generated and demultiplexed 96 voltages onto 648 devices at 66 mK for under 120 µW [D][552]: ~1.25 µW per voltage, so a milliwatt holds ~800 — ~400 directly wired qubits or ~1.8×10⁴ crossbar dots [S]. Switching costs ∝ C·V²·f: strobing commercial multiplexers at 8 kHz lifted a 50 mK stage to 130 mK [D][764]. A demultiplexer visits terminals in turn, each holding charge meanwhile — Schaal's cell stores it on the dot gate like a one-transistor–one-capacitor DRAM cell [D][763] — so refresh rate trades droop against heat [S].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2020-05-19 | Commercial CMOS multiplexers at 50 mK: 16 channels × 6 lines | QuTech / Intel | [D][764] |
| 2023-08-28 | 16-dot germanium crossbar, 23 terminals | QuTech | [D][520] |
| 2024-05-01 | 300 mm cryoprober: 232 twelve-dot arrays, electron temperature 1.6 ± 0.2 K | Intel | [D][766] |
| 2024-06-20 | Pando Tree: bias and pulses to 64 terminals, 10–20 mK | Intel | [C][272] |
| 2025-01-03 | 1,024 dots on one on-chip multiplexer, 22FDX, <1 K, mapped in <10 min | Quantum Motion | [D][767] |
| 2025-03-16 | Bell-1: six qubits and control in one rack, 0.3 K, 1,600 W | Equal1 | [C][768] |
| 2025-07 | 648 devices from 96 voltages, 66 mK, <120 µW, 22 nm FinFET | TU Delft / Intel | [D][552] |

No row is a gate benchmark through a router: Pando Tree shares a circuit board with a Tunnel Falls chip [C][272], with no fidelity measured through it found, as of 2026-09-26. Nearest: a 32-cell millikelvin pulse chip costing ~0.07% single-qubit fidelity [D][551] — generation, not routing. Dominant term: heat per addressed voltage.

## Manufacturing, materials & supply chain
Router dies are foundry CMOS run cold: 22 nm FinFET from Intel for Delft [D][552], 22FDX for Quantum Motion [D][767] and Equal1 [C][273], Intel 18A for Hitachi's quantum PDK, "the first such interface for a 1.8nm-class process" [P][769]. Tunnel Falls comes off a 300 mm line with extreme-ultraviolet lithography [D][199]. Three routes compete: a separate router die (Intel), monolithic multiplexers (Quantum Motion, Equal1), and "stacking qubit chips and control electronics vertically" (Hitachi) [P][769]. Cold wafer test gates all three — Intel's cryoprober is the published instance [D][766] — and imec's SPINS pilot line adds 300 mm spin-qubit runs, PDKs and cryo-CMOS [C][770]. Router and bond yields are unpublished as of 2026-09-26.

## Control, readout & I/O burden
Pando Tree delivers "both constant voltage bias and high-speed voltage pulsing for up to 64 qubit terminals" from nine digital signals and one line from the 4 K Horse Ridge II controller [C][272]: 0.3–0.8 lines per qubit at 2–5 terminals each [S]. The register's 0.0156 lines per qubit counts only the analogue line and reads terminals as qubits [S]. Intel's "approximately 20 cables" for a million qubits [C][272] carries no heat or bandwidth budget, as of 2026-09-26. Readout fans in too: Diraq reads eight qubits through two SETs [D][197]. At 1.25 µW per voltage and three terminals per qubit [S], 10³ qubits need ~4 mW wired directly, ~0.2 mW on a crossbar; 10⁶ need ~4 W, or ~7.5 mW shared — only the combination nears one refrigerator's budget.

## Role in the stack
Slot 9, the only layer-9 entry, of "Silicon / germanium quantum-dot spins" and "Donor spins in silicon". It **requires** fab_cmos (foundry CMOS) — "a CMOS router die at cryogenic temperature" — and ct_cryocmos (cryogenic CMOS control), which generates what this technology routes; cx_crossbar (layer 4) shares lines inside the array. No **provides** edge is recorded. ic_mcm (coupled multi-chip modules) **replaces** it; neither spin architecture has an inter-module link, as of 2026-09-26. Eight register machines carry it, all primary: Tunnel Falls, Hitachi × Intel 18A, Bell-1, QM-One, Diraq's eight-qubit array, Groove Quantum, Quobly and SQC's 11-qubit donor processor. All eight cells are inferred and 🔎 and record the missing slot, not a component; only Intel, Hitachi, Equal1 and Quantum Motion name an artefact, the rest drive gates from room temperature. Gap G-spinl9, answered: the slot is open on both architectures; the proposed ic_router is this technology.

## Evidence — how the numbers were measured
The figures of merit — channels per die, heat per line at the MXC, hold droop, refresh rate, switching crosstalk — sit in no register cell. The record is component-level: Delft's held voltages drift 60 µV/s to 18 mV/s [D][552], slow coherent error that randomized benchmarking averages away [S]; the cryoprober and the 1,024-dot chip measure devices, not gates [D][766][D][767]. Equal1's page lists 99.3% average two-qubit fidelity [C][273], the register 98.4%; neither names the fan-out behind it. Missing, as of 2026-09-26: a benchmark through a millikelvin router, and Pando Tree's dissipation.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| Intel | developer | US | Pando Tree router; 300 mm cryoprober | [C][272][D][766] |
| Hitachi | developer | JP | Qubit chips and control stacked vertically; 18A PDK | [P][769] |
| Quantum Motion | developer | UK | 1:1,024 on-chip multiplexer; tiles with on-chip control and readout | [D][767][C][200] |
| Equal1 | developer | IE | Qubits and control electronics in 22FDX at 0.3 K | [C][273] |
| TU Delft / QuTech | research | NL | Millikelvin demultiplexing; germanium crossbar | [D][552][D][520] |

**Money.**
- 2026-01-15 · Equal1 · round led by the Ireland Strategic Investment Fund, system "onto a single chip" · USD 60 M · announced [C][771]
- 2026-03-18 · Rhonexum · pre-seed led by QDNL Participations · USD 1 M · announced [P][560]
- 2026-04-03 · imec-led consortium · SPINS pilot line, EU Chips Joint Undertaking co-funding · EUR 50 M · launched [C][770]
- 2026-05-07 · Quantum Motion · Series C, fan-out not named · USD 160 M · announced [C][355]

**Market & supply chain.** Fan-out is bought with the qubit die; the one merchant entrant found, Lausanne's Rhonexum, is at pre-seed [P][560]. Scarce inputs — cold device models, cold wafer test, foundry slots — are shared with ct_cryocmos. It serves G4 and G7 on the quantum-dot architecture, G7 on the donor architecture.

**IP & standards.** No fan-out patent count from a named database and no interface standard, as of 2026-09-26; the nearest artefacts are PDKs — SPINS' [C][770] and Hitachi's intended 18A kit [P][769].

**Roadmaps & track record.** Intel: ~20 cables per million qubits, undated [C][272]; no qubit data through Pando Tree since 2024-06-20, as of 2026-09-26. Hitachi: cloud access in fiscal 2027, 100 qubits in fiscal 2028, 1,000 in fiscal 2030 [P][769]. Diraq: 150,000 physical qubits by 2029, over 2 million by 2031, fan-out unstated [R][211]. No fan-out milestone has come due; nothing to score yet.

**Strategic reading.** Intel's separate router and the monolithic dies of Equal1 and Quantum Motion are rival bets on the millikelvin milliwatt. If routers fall well below a microwatt per voltage, value moves to foundries with cold device models and to cold wafer test; if not, qubits run hotter — Equal1 at 0.3 K [C][768] — or split into modules, and ic_mcm takes the slot [S].

## Outlook & open questions
Confirm if, by 2027-12-31, a peer-reviewed spin-qubit gate benchmark runs through a millikelvin router or on-die multiplexer and reports heat per channel; demote if Hitachi's fiscal-2028 prototype or Diraq's 2029 system ships with per-gate lines from 4 K or room temperature. Open questions. (1) What does Pando Tree dissipate per switched terminal? (2) What hold droop do exchange gates tolerate between refreshes? (3) Does time-multiplexed pulsing cap gate parallelism below what a surface-code round needs? (4) Can crossbar sharing and millikelvin routing share one die? (5) Will spin modules (ic_mcm) take the slot before routers reach 10⁴ channels?

## Sources

[197] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[199] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[200] Quantum Motion, “Quantum Motion Delivers the Industry's First Full-Stack Silicon CMOS Quantum Computer,” Sep. 15, 2025. [Online]. Available: https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ [C]
[211] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[272] S. Subramanian and S. Pellerano, “Intel's Millikelvin Quantum Research Control Chip Provides Denser Integration with Qubits,” Intel Community, Jun. 20, 2024. [Online]. Available: https://community.intel.com/t5/Blogs/Tech-Innovation/Data-Center/Intel-s-Millikelvin-Quantum-Research-Control-Chip-Provides/post/1608558 [C]
[273] Equal1, “UnityQ.” [Online]. Available: https://www.equal1.com/technology [C]
[355] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[520] F. Borsoi *et al.*, “Shared control of a 16 semiconductor quantum dot crossbar array,” *Nat. Nanotechnol.*, vol. 19, no. 1, pp. 21–27, Jan. 2024, doi: [10.1038/s41565-023-01491-3](https://doi.org/10.1038/s41565-023-01491-3). [D]
[551] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[552] J. van Staveren *et al.*, “Cryo-CMOS Bias-Voltage Generation and Demultiplexing at mK Temperatures for Large-Scale Arrays of Quantum Devices,” *IEEE Trans. Quantum Eng.*, vol. 6, pp. 1–18, 2025, doi: [10.1109/TQE.2025.3580377](https://doi.org/10.1109/TQE.2025.3580377). [D]
[560] M. Abdel-Kareem, “Rhonexum Raises $1M Pre-Seed to Solve the Quantum Cabling Bottleneck via Cryo-CMOS,” Quantum Computing Report, Mar. 18, 2026. [Online]. Available: https://quantumcomputingreport.com/rhonexum-raises-1m-pre-seed-to-solve-the-quantum-cabling-bottleneck-via-cryo-cmos/ [P]
[761] L. M. K. Vandersypen *et al.*, “Interfacing spin qubits in quantum dots and donors—hot, dense, and coherent,” *npj Quantum Inf.*, vol. 3, Art. no. 34, Sep. 2017, doi: [10.1038/s41534-017-0038-y](https://doi.org/10.1038/s41534-017-0038-y). [D]
[762] R. Li *et al.*, “A Crossbar Network for Silicon Quantum Dot Qubits,” *Sci. Adv.*, vol. 4, Art. no. eaar3960, 2018, doi: [10.1126/sciadv.aar3960](https://doi.org/10.1126/sciadv.aar3960). [arXiv:1711.03807](https://arxiv.org/abs/1711.03807). [D]
[763] S. Schaal *et al.*, “A CMOS dynamic random access architecture for radio-frequency readout of quantum devices,” *Nat. Electron.*, vol. 2, no. 6, pp. 236–242, Jun. 2019, doi: [10.1038/s41928-019-0259-5](https://doi.org/10.1038/s41928-019-0259-5). [arXiv:1809.03894](https://arxiv.org/abs/1809.03894). [D]
[764] B. P. Wuetz *et al.*, “Multiplexed quantum transport using commercial off-the-shelf CMOS at sub-kelvin temperatures,” *npj Quantum Inf.*, vol. 6, Art. no. 43, May 2020, doi: [10.1038/s41534-020-0274-4](https://doi.org/10.1038/s41534-020-0274-4). [D]
[765] D. P. Franke, J. S. Clarke, L. M. K. Vandersypen, and M. Veldhorst, “Rent's rule and extensibility in quantum computing,” *Microprocess. Microsyst.*, vol. 67, pp. 1–7, 2019, doi: [10.1016/j.micpro.2019.02.006](https://doi.org/10.1016/j.micpro.2019.02.006). [D]
[766] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]
[767] E. J. Thomas *et al.*, “Rapid cryogenic characterization of 1,024 integrated silicon quantum dot devices,” *Nat. Electron.*, vol. 8, no. 1, pp. 75–83, Jan. 2025, doi: [10.1038/s41928-024-01304-y](https://doi.org/10.1038/s41928-024-01304-y). [D]
[768] Equal1, “Equal1 Launches Bell-1: The First Quantum System Purpose-Built for the HPC Era,” Mar. 16, 2025. [Online]. Available: https://www.equal1.com/post/equal1-launches-bell-1-the-first-quantum-system-purpose-built-for-the-hpc-era [C]
[769] M. Rutherford, “Silicon Spin Qubits Get Foundry Path: Hitachi Banks on Intel 18A Process,” Tech Times, Jul. 28, 2026. [Online]. Available: https://www.techtimes.com/articles/321867/20260728/hitachi-intel-18a-spin-qubit.htm [P]
[770] imec, “Quantum pilot line 'SPINS' launched with EU support,” Apr. 3, 2026. [Online]. Available: https://www.imec-int.com/en/press/semiconductor-based-quantum-pilot-line-spins-launched-eu-support [C]
[771] University College Dublin, “Equal1 Announces $60 million in Funding to Accelerate Quantum Computing using Existing Semiconductor Manufacturing,” UCD Innovation, Jan. 15, 2026. [Online]. Available: https://www.ucd.ie/innovation/news-and-events/2026/equal1-announces-funding-round/ [C]

## Open verification items
- "3–5 gate lines per qubit" and imec/Diraq back-end-of-line routing, both named in the brief request, were not found in a source opened; Franke et al.'s t = 2 and Diraq's 90 nm gate pitch are used instead (2026-09-26).
- arXiv abstract pages for Vandersypen et al. 2017, Franke et al. 2019 and Paquelet Wuetz et al. 2020 returned no metadata, then arxiv.org refused further fetches with HTTP 429 (2026-09-26); these works are cited by DOI and their arXiv ids are unconfirmed.
- Pando Tree: the 2024 VLSI Symposium paper was not opened; process node, dissipation and any qubit fidelity measured through it are absent from Intel's blog (2026-09-26).
- Fan-out plans of SQC, Quobly and Groove Quantum: none found in this pass; their register cells stay 🔎 (2026-09-26).
- Diraq's roadmap page shows "27 August" without a readable year (the Atlas's bibliography dates it 2026-08-27); the 2029 and 2031 targets are quoted from the page (2026-09-26).
- Schaal et al.'s record rests on the UCL Discovery entry and an arXiv listing, not the publisher page; no patent search specific to cryogenic fan-out was run (2026-09-26).
