---
id: ct_laser
name: Laser + AOD/SLM optical control (atoms)
layer: 5 Control
tier: 2
status: demonstrated
since: 2016
one_line: Free-space lasers, holographic modulators and acousto-optic deflectors generate, move, image and drive the optical-tweezer arrays that hold neutral-atom qubits.
verdict: This layer, not the 270 ns gate, sets the neutral-atom clock: imaging plus transport keep the QEC round at 1-4.5 ms as of 4 Sep 2026, and trap power scales linearly at ~0.67 mW per site.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A holographic modulator splits one beam into a static lattice of tweezer foci; crossed acousto-optic deflectors, driven by multi-tone RF, steer individual traps; further lasers cool, image and drive the hyperfine and Rydberg transitions. Modulators frame at tens of hertz, static within a shot, so fast motion belongs to the deflectors or to optical-lattice conveyors. Endres set the pattern in 2016 — real-time control of 100 tweezers building defect-free arrays of over 50 atoms in under 400 ms [D][1] — and that measure-decide-move-verify loop is still the clock.
- e/f: entirely optical, room temperature, outside the vacuum cell; errors are coherent — pointing, hologram phase, RF intermodulation.
- d/g: connectivity comes from deflector transport, built of free-space optics.

## Physics & limits
Two hard laws govern this layer. Trap power is linear in site count: Tsinghua's 18,225-site array takes 33 W incident, 12.2 W effective, ~0.67 mW per trap [D][2], so 10⁶ sites implies about a kilowatt of trapping light before any imaging or Rydberg beam. And a deflector's resolvable-spot count is its RF bandwidth times the acoustic transit across the beam, while that transit lower-bounds how fast a trap is re-pointed: more sites and faster moves pull against each other in one device. Neither is a "refresh rate"; the report's 10 MHz figure is a proxy. The consequence is the clock: imaging at 0.5–1 ms and transport at hundreds of µs give QEC rounds of 1–4.5 ms against 270 ns gates [D][3]. Failure modes are systematic: trap-depth non-uniformity, pointing drift, tone intermodulation. Faster imaging moves the floor — 17.6 µs readout at 99.89(5)% discrimination on ytterbium [P][6], ~50× off the dominant term.

## Engineering state of the art
Largest array: 11,022 rubidium atoms in an 18,225-site grid from a 19.8 mm metasurface outside the vacuum cell — no gates, no coherence, 60.5% filling before rearrangement [D][2]. Best sustained operation: 3,217 atoms at 99.3% filling beyond two hours, reloading 300,000 atoms per second for 30,000 initialised qubits per second, moved by optical-lattice conveyors, not deflectors [D][4]. Typical at scale is far smaller: the 448-atom architecture, where imaging and transport set a 1–4.5 ms round [D][3]. Dominant limit: measurement and motion latency, not trap count or power.

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2025-09 | 3,217 atoms, >2 h, 30,000 initialised qubits/s | Harvard | [D][4] |
| 2026-06 | 18,225 metasurface traps, 11,022 atoms, 0.67 mW/site | Tsinghua | [D][2] |
| 2026-07 | 2,000 tweezers from 20 W, 3.5 µm pitch, sub-100 nm | Fraunhofer ILT | [P][5] |
| 2026-08 | 17.6 µs imaging, 99.89(5)% discrimination, 98.80(44)% survival | Kyoto | [P][6] |

## Manufacturing, materials & supply chain
No wafer: commodity and semi-custom free-space optics integrated by hand — yet the concentration is severe. Only two deflector vendors appear in the sourced literature, AA Opto-Electronic (DTSX-400, in the 448-atom system) and Gooch & Housego [D][G:AOD-VENDORS-2026], and Hamamatsu supplies both modulator and camera with no alternative identified [C][G:HAMAMATSU-CAMERA-CONC-2026] — the two real single points of failure. A June-2026 alliance of Hamamatsu, NKT Photonics and Yaqumo is the first attempt to industrialise the tier, aimed at a sensing market projected at $3.5–7.9B [P][7]. Tsinghua's metasurface points the other way: a lithographic element replacing the objective is the one step that could become semiconductor manufacturing [D][2]. No export-control category names tweezer optics; exposure runs via ECCN 4A906 [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden
One optics chain serves the whole array, so the burden is bandwidth and optical power, not lines per qubit — the inverse of the superconducting problem, and why atom counts scale while clocks do not. At 10³ sites full fault-tolerant loops run today [D][3]. At 10⁴ the binding constraint is the measure-rearrange-verify cycle: 11,022 atoms trapped against 448 under logical control. Nothing exists at 10⁶. The only end-to-end control-loop figure a vendor publishes is QuEra's Gemini repetition rate: one shot per second at 260 qubits [C][8].

## Role in the stack
This layer underlies both neutral-atom paths — alkali (QuEra, Pasqal, Infleqtion, Google) and alkaline-earth (Atom Computing/Microsoft, Caltech) — supplying the Rydberg drive and deflector transport that the gate and zoned-connectivity mechanisms consume. It replaces photonic-integrated trap control, trading chip-scale integration for free-space flexibility. Not a hub by reach, but nearly every neutral-atom mechanism sits on it. Derived clock = sum of the syndrome round: gate layers + transport + readout + reset ≈ 1.31 ms, transport 0.80 ms of it, against a measured 1–4.5 ms round — set entirely here. Empty neighbouring slot: an integrated optical control plane keeping deflector flexibility.

## Verification (QCVV)
Trap counts and filling come from direct fluorescence imaging and are not disputed, but they are compared across incompatible boundaries: 11,022 trapped atoms and 448 qubits under fault-tolerant control measure different things, and filling is quoted before rearrangement (60.5% [D][2]) or after (99.3% [D][4]) unlabelled. Latency figures are architectural, measured inside one group's system and never reproduced, and the metasurface and 2,000-tweezer results are each single-group.

## Actors & economics
**Who.**
| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| QuEra Computing | developer | USA | Sells Gemini: 260 atoms, one shot per second | [C][8] |
| Atom Computing | developer | USA | Ytterbium platform; builds Magne with Microsoft | [C][10] |
| Pasqal | developer | France | Rydberg tweezer systems; SPAC-listed Aug 2026 | [P][16] |
| Hamamatsu Photonics | supplier | Japan | Modulators and qCMOS cameras | [P][7] |
| AA Opto-Electronic | supplier | France | Crossed AODs for tweezer transport | [D][G:AOD-VENDORS-2026] |

**Money.**
| Date | Actor | Event | Amount | Programme / lead | Status |
|---|---|---|---|---|---|
| 2025-07-17 | QuNorth | Magne order, 1,225 physical | €80M | Atom Computing, Microsoft | ordered [C][G:MAGNE-2025-07] |
| 2025-09-09 | QuEra | financing round | $230M+ | Google, SoftBank Vision Fund 2 | closed [C][9] |
| 2025-11-06 | DARPA | QBI Stage B: Atom Computing, QuEra | ≤$15M | QBI | official [G:QBI-STAGEB-2025-11] |
| 2026-06-16 | Atom Computing | Series C plus CHIPS LOI | $100M + $100M | Third Point; US Commerce | closed+LOI [C][10] |
| 2026-08-28 | Pasqal | SPAC close | ~$360M cash, 2025 revenue €16.5M | — | closed [P][16] |

**Market & supply chain.** Two deflector vendors and one camera-and-modulator vendor against a laser field with real alternatives (NKT, TOPTICA, Coherent): the concentration sits in deflectors and cameras, small unlisted businesses under four venture-funded platforms. Unit economics are quotable at system level — QuNorth's €80M for 1,225 atoms is ~€65k per atom, two orders below a trapped-ion delivery per ion [P][G:ATOM-OPTICS-UNIT-COST-2026], because tweezer optics amortise across sites. It pays for G1, is a prerequisite for G3, blocks G4 until the millisecond cycle falls.

**IP & standards.** No patent family specific to tweezer control surfaced: the technique descends from open literature and the entrants are spin-outs of the groups that published it. Vendor IP sits in the deflector and modulator products, not quantum-specific; PatSnap's counts are not disaggregated here [P][G:PATSNAP-2026-06]. No litigation, no standards body.

**Roadmaps & track record.** QuEra (2024, for 100 logical in 2026) — retargeted to "Libra" in 2028, a two-year slip, no control-hardware change announced. Atom Computing with Microsoft (2025-07, for 50 logical in Magne at the turn of 2026/27) — installing as of 4 Sep 2026, the field's only firm delivery date. Pasqal (2024, for 10,000 physical in 2026) — slipped to 2028, now funded. Infleqtion (2025-09, for 1,000 logical by 2030) — capitalised, no latency figure. Google (2026-03) — staffed, no milestone.

**Strategic reading.** If this layer industrialises the winner is whoever consolidates the optics tier, not a platform company: a supplier owning deflectors, modulators and cameras prices against every neutral-atom vendor at once, which is what the Hamamatsu alliance is positioned to become. The platforms' counter is integration — metasurfaces and trap chips pulling optics onto a wafer. If the millisecond cycle holds they lose together: atom counts already exceed what anyone can control, so latency is the differentiator, and superconducting rivals hold three orders on clock.

*Open niche:* A small QCVV house could publish the number nobody reports: an end-to-end control-loop clock — image, decide, move, verify — with its variance, to a common protocol across vendors. The field offers one product figure and in-paper latencies never meant to be compared.

## Outlook & open questions
Confirm/demote in 12–24 months: a QEC round below 1 ms above 10³ sites; a second group replicating the metasurface array or the 17.6 µs imaging; Magne benchmarked at 50 logical qubits. Best case 2029: fast imaging and conveyor transport cut the round to ~100 µs, removing the clock disadvantage. Worst case: latency stays at milliseconds, arrays large, cheap and slow. Open: is the deflector bandwidth-transit trade engineering or a hard limit; can fast imaging survive at 10⁴ sites; will anyone second-source the deflectors. Watch Magne's acceptance tests.

## Sources
[1] Endres et al. (Caltech / Harvard) · Cold matter assembled atom-by-atom (100 real-time tweezers) · arXiv:1607.03044 · 2016-07-11 · https://arxiv.org/abs/1607.03044
[2] Wang, Zhang et al. (Tsinghua University, Qosmos) · Metasurface tweezer array, 18,225 sites, 11,022 atoms · arXiv:2606.02715 · 2026-06-01 · https://arxiv.org/abs/2606.02715
[3] Harvard / MIT / QuEra · 448-atom fault-tolerant architecture · Nature · 2025-11 · https://www.nature.com/articles/s41586-025-09848-5
[4] Chiu, Ji, Bluvstein et al. (Harvard / MIT / QuEra) · Continuous operation of a coherent 3,000-qubit system · Nature · 2025-09-15 · https://www.nature.com/articles/s41586-025-09596-6
[5] Fraunhofer ILT / University of Stuttgart · Laser-optical system for 2,000 Rydberg tweezers · The Quantum Insider · 2026-07-08 · https://thequantuminsider.com/2026/07/08/fraunhofer-ilt-develops-laser-system-for-2000-qubit-neutral-atom-quantum-computer/ [P]
[6] Yokoyama, Kashimoto, Shibata et al. (Kyoto University, Yaqumo) · 17.6 µs fluorescence imaging of ytterbium atoms · arXiv:2605.24175v2 · 2026-08-24 · https://arxiv.org/html/2605.24175 [P]
[7] Quantum Computing Report · Hamamatsu Photonics, NKT Photonics and Yaqumo alliance on cold-atom core components · 2026-06-04 · https://quantumcomputingreport.com/hamamatsu-photonics-nkt-photonics-and-yaqumo-form-alliance-to-industrialize-cold-atom-quantum-core-components/ [P]
[8] QuEra Computing · Gemini product page (260 qubits, 99.2% global 2Q, one shot per second) · company website · accessed 2026-09-03 · https://www.quera.com/gemini [C]
[9] QuEra Computing · $230M+ financing round · company press release · 2025-09-09 · https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[10] Atom Computing · Raises more than $300M including a $100M DoC letter of intent · PR Newswire · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[11] Caltech · 6,100-atom caesium array with 12.6 s coherence · arXiv:2403.12021 · 2025-09 · https://arxiv.org/abs/2403.12021
[12] Google · Neutral-atom quantum computers: a second hardware track · Google blog · 2026-03-24 · https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]
[13] Gooch & Housego · Acousto-optic deflectors in Nature neutral-atom papers · company page · accessed 2026-09-04 · https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [C]
[14] US Bureau of Industry and Security · Export controls on quantum computing items (ECCN 4A906) · Federal Register · 2024-09-06 · https://www.federalregister.gov/documents/2024/09/06/2024-19633/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and
[15] Infleqtion · First neutral-atom quantum company to go public (NYSE, >$550M gross) · company newsroom · 2026-02-17 · https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [C]
[16] The Quantum Insider · Pasqal completes SPAC merger with ~$360M in cash · 2026-08-28 · https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]

## Open verification items
The main report's "10 MHz refresh insufficient above ~10⁴ qubits" cannot be attributed to a device or a measurement in any source found; liquid-crystal modulators frame at tens of hertz and deflector reconfiguration is bounded by acoustic transit, so the figure is treated here as a proxy. Institutional affiliation for the 2016 lineage paper was not returned by the arXiv abstract page. Whether the Hamamatsu, NKT Photonics and Yaqumo alliance has signed named customers is undisclosed. Vacuum lifetime and any coherence measurement for the 18,225-site metasurface array are not reported. No cost breakdown exists below system level; the €65k-per-atom figure is derived from one order, not a price list.
