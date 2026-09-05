---
id: cx_crossbar
name: Crossbar shared-line control (spins)
layer: "4 Connectivity / transport"
tier: 3
status: emerging
since: 2024
one_line: Row- and column-shared plunger and barrier lines address a two-dimensional dot array with line count scaling as the square root of dot count, trading wireability for addressing granularity.
verdict: Removes the wiring wall on paper and in a 1,058-site chip, but no crossbar array has published a two-qubit gate, a crosstalk figure or an independent replication.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
A crossbar shares gate lines across rows and columns of a dot array: an n×m grid needs O(n+m) lines, not O(nm), at the price that every pulse reaches every dot on the line. Selectivity comes from cross-capacitance compensation and the operating-point spread between tiles: addressing becomes calibration. Introduced for spin qubits by Borsoi et al. (Veldhorst group, QuTech/TU Delft): 16 germanium dots on 23 lines, published January 2024 [D][1]. Coordinates: connectivity — shared row/column addressing, carrier immobile; control and error — low-frequency drive from room temperature, coherent shared-line crosstalk over ordinary charge noise, CMOS fabrication.

## Physics & limits
Line count follows a Rent exponent near 0.5: T = 6√g − 1 terminals for g dots [D][1], and n+m+7 = 53 lines for the 23×23 QARPET array, capacity 1,058 sites at 2×10⁶ tiles/mm² [D][2]. The binding constraint is uniformity, not wiring: one shared voltage must land inside every tile's operating window at once, so threshold spread sets how many tiles a line serves. QARPET's 38-of-40 addressable tiles show T2* 4.43–5.75 µs and Hahn-echo T2 10.11–12.69 µs, comparable to individually wired germanium devices: sharing lines costs no coherence [D][2]. What it adds is coherent error correlated along a whole row or column, the structure decoders assume away. On-chip demultiplexing would move the floor.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2024-01 | 16 dots on 23 shared lines, odd occupancy in all sites | QuTech/TU Delft | [D][1] |
| 2026-02-12 | 53 lines, 23×23 tiles, 1,058-site capacity; 40 tiles measured, 38 addressable | QuTech/TU Delft | [D][2] |

Dominant term: addressing coverage. Neither device published a two-qubit gate on a shared line.

## Manufacturing, materials & supply chain
Both devices are Ge/SiGe heterostructures made in a university cleanroom, not on a 300 mm line, and no foundry has announced a crossbar process step as of 4 Sep 2026 — GlobalFoundries' Quantum Technology Solutions unit, with cryogenic control ICs and packaging, is the closest named capability [C][3]. Control burden is the whole point, and its cost reappears as sequencing: one row and one column select at a time, so at 10³ tiles parallel operation needs on-chip decoding, and at 10⁴–10⁶ the wall is addressing bandwidth, not connector count. No demultiplexer has been demonstrated inside an array.

## Role in the stack
Requires a gate-defined quantum-dot spin carrier; replaces one-line-per-electrode wiring; conflicts with per-pair exchange calibration, since a shared barrier cannot deliver an independently tuned pulse to every pair at once. Belongs to the silicon and germanium quantum-dot spin path. Its clock contribution is a sequencing multiplier on derived clock = max(gate, readout, transport), unquantified in any publication. Verification: 1,058 is a site capacity, not a qubit count, and no crossbar has published a two-qubit fidelity, a crosstalk figure or a replication. The "only some pairs work" result often cited here — one of four pairs gated on imec's eight-qubit 300 mm device [D][4] — is individually wired, not a crossbar.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| QuTech/TU Delft | research | Netherlands | Built both crossbar devices, including QARPET | [D][2] |
| Groove Quantum | developer | Netherlands | Commercialises the germanium dot platform | [G:GROOVE-2026] |
| GlobalFoundries | supplier | USA | Cryogenic control ICs and packaging | [C][3] |
| Quantum Machines | supplier | Israel | Sequencing hardware for shared-line addressing | [C][5] |

**Money.** 2026-04-30 · Groove Quantum · venture round · €16 M · investors undisclosed · €26 M cumulative · closed [G:GROOVE-2026]. 2026-05-21 · GlobalFoundries · CHIPS letter of intent · $375 M · US Commerce · non-binding [G:CHIPS-LOI-2026-05].

**Market & supply chain.** No crossbar-specific equipment vendor exists; the scheme sets how many fridge lines an array needs, making cryogenic control ICs the contested layer [C][3]. Pays into G3 and G4 only — below ~10³ dots individual wiring is cheaper and better characterised.

**IP & standards.** No dated crossbar patent family found in a named database as of 4 Sep 2026; the shared-line principle is commodity-memory word-line addressing, long out of patent.

**Roadmaps & track record.** QuTech (2026-02-12 · QARPET as a shared benchmarking chip · delivered, no scaling roadmap) [D][2]. Diraq's 2029 roadmap names no wiring scheme [R][G:DIRAQ-FUNDING]. The demonstrations are modest and honestly stated; no vendor has committed to a crossbar.

**Strategic reading.** If crossbars scale, leverage shifts from rack-electronics vendors to whichever foundry can put demultiplexers at millikelvin; if uniformity blocks them, per-qubit wiring with cold multiplexing — the HRL/IBM route — wins and the rack vendors keep their position.

*Open niche:* shared-line crosstalk has no published characterisation protocol; a benchmark separating row- and column-correlated coherent error from local charge noise on a QARPET-class chip is a small, well-defined QCVV product.

## Outlook & open questions
Confirm or demote in 12–24 months: two tiles gated independently through one shared line; a published crosstalk figure; a foundry crossbar step by 2027. Best case 2029: on-chip demultiplexing addresses >10⁴ dots with hundreds of lines. Worst case: crossbars stay a wireability demonstration while cold per-qubit multiplexing wins. Open: (1) what fraction of tiles stays addressable as arrays grow; (2) whether row-correlated error breaks decoder assumptions; (3) whether demultiplexers fit the millikelvin power budget.

## Sources
[1] F. Borsoi, N. W. Hendrickx, G. Scappucci, M. Veldhorst et al. (QuTech/TU Delft) · "Shared control of a 16 semiconductor quantum dot crossbar array" · Nature Nanotechnology · 2024-01 (online 2023-08-28) · https://www.nature.com/articles/s41565-023-01491-3 [D]
[2] M. Tosato, S. Elsayed, G. Scappucci et al. (QuTech/TU Delft) · "QARPET: crossbar chip for benchmarking semiconductor spin qubits" · Nature Electronics · 2026-02-12 · https://www.nature.com/articles/s41928-026-01569-5 [D]
[3] GlobalFoundries · "GlobalFoundries launches Quantum Technology Solutions" · press release · 2026-05-21 · https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ [C]
[4] R. Nickl, T. Dumoulin Stuyck, W. Steinacker et al. (Diraq/imec) · eight-qubit 300 mm SiMOS device, two-qubit gate on one of four pairs · Nature Communications 17, 5878 · 2026-07-09 · https://www.nature.com/articles/s41467-026-74597-6 [D]
[5] Quantum Machines · "Semiconductor spin qubits" — OPX1000, QDAC-II, QSwitch · company page · accessed 2026-09-04 · https://www.quantum-machines.co/qubit-types/semiconductor-spin-qubits/ [C]

## Open verification items
No crossbar publication gives a two-qubit fidelity or a shared-line crosstalk figure, so the conflict with per-pair exchange calibration is argued from the addressing scheme, not measured. Groove Quantum's investors and round label are not stated in any source consulted here. The QARPET 1,058 figure is a site capacity; the largest measured subset is 40 tiles.
