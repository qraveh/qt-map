# Quantum Computing Technologies — A Goal-Oriented Comparison
## Achievements, justified intentions, and the most promising directions (status: 4 September 2026)



> **Thesis.** There is no universally best qubit technology, because there is no single goal. Every platform presents the computation with an error channel, a clock, a count, and a scaling path — and every goal weighs these four differently. A machine that is fatal for RSA-2048 may be ideal for lattice-gauge simulation. This document therefore does three things: (1) fixes a criteria set that is technology-agnostic by construction, (2) grades every major platform on *demonstrated* results and on *justified* intentions separately, and (3) maps platforms to goals — and only then names the directions that look most promising.

---

## About the map

**Why a Quantum Technology Map.** Quantum computing has no universally best technology, because it has no single goal: a machine that is fatal for RSA-2048 may be the wrong machine for lattice-gauge simulation. Comparisons are nevertheless made at the level of *platforms* — superconducting versus ions versus atoms — although a platform is an assembly of separable technologies, and the decisions that matter (what to research, what to build, whom to partner with, what to buy) are made one technology at a time. The material that exists today comes in three kinds, each blind in its own way: vendor roadmaps (intentions, not results), market monitors (money, not physics) and academic reviews (physics, not economics, and dated on arrival). The map exists so that every technology in the quantum-computing stack can be read on the same coordinates, against dated evidence, with its conflicts and its economics in one place — and so that the picture is refreshed several times a year rather than once.

**What it is.** A living, open (CC BY 4.0), bilingual reference in four connected parts: a goal-oriented comparison of platforms — what each has demonstrated, what it credibly intends, and which directions look most promising; a technology graph — 96 self-contained technologies across ten stack layers, each placed on seven design coordinates and connected by five kinds of edge, with platforms drawn as paths through the layers; a brief on every technology, with the same section skeleton from physics to economics; and an evidence system — every claim tagged by its standing, every figure traced to a dated, linked source, conflicts stated rather than averaged, open verification items listed. It is published as one interactive document; editions are archived with a DOI; the data and the build are open on GitHub.

**Who should use it.** Researchers choosing where to put the next years of work — the graph shows hubs, empty slots and unresolved conflicts, which is where leverage is. Architects and engineers designing a system — a platform is a path through the layers, and every station on it comes with what it requires, what it can be swapped for, and what it collides with, priced. Investors and analysts — each brief carries the actors, the dated money, the supply chain and the roadmap-versus-delivery record of one technology, not of a company. Programme and policy staff — who is where, which suppliers are single points of failure, which export rules apply. Newcomers — the map is a structured entry into a field whose literature is not. Vendors — to see how their claims read when tagged and dated. It is not a market-sizing exercise and not a ranking of companies.

**What makes an entry.** A technology becomes a node of the graph if it is *self-contained* — it can be replaced without redesigning the rest of the stack; *principled* — it rests on a distinct physical or mathematical mechanism, not on a product, a vendor or a parameter choice; and it belongs to exactly one layer. It must be locatable on all seven coordinates: carrier affinity (natural ↔ fabricated), characteristic time and deterministic or heralded entangling, readout mechanism with its time, destructiveness and mid-circuit capability, mobility and connectivity, control modality and placement, dominant error structure as an error-correcting code sees it, and manufacturing technology. A demonstrated node needs at least one dated, sourced record; emerging or theoretical nodes are admitted when a platform path needs the slot, and slots with no technology at all are drawn as empty. Platforms, companies and devices are never nodes: platforms are paths, companies are actors, devices are records. Every node carries its coordinates (design space, stable), its dated records (evaluation space), its actors and goals (annotation space), its edges, and its brief.

**How it is organised.** Ten layers run left to right — carrier, encoding, gate mechanism, connectivity and transport, control, readout, code, decoder, interconnect, manufacturing; the vertical position is carrier affinity, natural at the top and fabricated at the bottom, so the natural/fabricated diagonal is visible and every technology that breaks it is hatched. Stations are technologies; coloured lines are platform paths through one station per layer; a station on several lines is a transfer hub. Five edge types connect stations: *requires/provides* between layers; *alternatives* within a layer; *conflicts*, each with its mechanism, its measured price, its mitigation and a status; *transfers*, derived from the paths; *defines*, dated records with sources. Lenses recolour every station by one coordinate, and the legend doubles as a filter. Hubs, off-diagonal technologies, empty slots and each path's clock are derived from the data, not asserted. The briefs follow one skeleton — identity and lineage, physics and limits, engineering state of the art, manufacturing and supply chain, role in the stack, verification, actors and economics, outlook, sources, open items — at a depth set by the technology's importance in the graph. Editions are named by date (2026.09) and archived with a DOI; the concept DOI always resolves to the latest edition.

---

## 0. Executive summary

1. **Three platforms have demonstrated fault-tolerance primitives at the level of "the physics works": superconducting circuits, trapped ions, and neutral atoms.** They have complementary profiles: superconducting = fast clock ($\sim 1\ \mu$s QEC cycle), mediocre channel at scale ($\sim 10^{-3}$ two-qubit error, $10^{-2}$ readout); ions = best channel at scale ($7.9\times10^{-4}$ two-qubit, $4.8\times10^{-4}$ SPAM over 98 qubits; $8.4\times10^{-5}$ record) but a millisecond-class logical clock; neutral atoms = largest qubit counts with quality (448 atoms under full logical control; 3,000–6,100 held with second-scale coherence; 11,000 trapped) and reconfigurable connectivity, also with a millisecond clock.
2. **The only platform with a demonstrated *scaling* of error suppression in memory ($\Lambda=2.14$ across d=3→5→7, plus a $10^6$-cycle real-time-decoded run at d=5) is superconducting** (Google; best d=7 logical error $7.7\times10^{-4}$/cycle, July 2026). Neutral atoms and ions lead on the *number* of logical qubits (96 d=4 blocks at Harvard/QuEra; 48 error-corrected logical qubits on Quantinuum Helios with $10^{-4}$ logical gate error) and on logical *operations* (transversal gates, teleportation, magic-state distillation on logical qubits).
3. **Speed is the decisive discriminator for large-scale fault tolerance and nearly irrelevant for everything else.** Resource estimates for chemistry and cryptanalysis change runtime by $\sim10^{3}$ between nanosecond- and microsecond-class gates; a millisecond QEC cycle adds another $10^{3}$. Ions and atoms must buy this back with encoding rate, transversal logic and parallelism — plausible for $10^{2}$–$10^{3}$ logical qubits, unproven for $10^{9}$-gate algorithms.
4. **The most important cross-cutting direction is error-structure engineering, not error-rate reduction:** erasure conversion (dual-rail, metastable Yb/Sr, photon loss), noise bias (cats), leakage removal, and real-time decoding. The surface-code threshold roughly quadruples ($0.94\%\to4.15\%$) when errors become erasures. This is the lever every major vendor is now reaching for.
5. **Revealed preferences of the majors are a better roadmap filter than press releases.** Google added a neutral-atom track (March 2026) next to superconducting; IBM bought HRL (silicon spin qubits, cryo-CMOS control, July 2026) next to its transmon program; Microsoft sells neutral-atom machines with Atom Computing while its own topological program still has no qubit; D-Wave bought Quantum Circuits (dual-rail erasure) as annealing revenue collapsed; IonQ bought Oxford Ionics (electronic gates) and a foundry. Every major now hedges across exactly two families: one fast (superconducting) and one dense (atoms or spins).
6. **Verdict (ranked by expected contribution to a utility-scale fault-tolerant machine by ~2033):** (i) superconducting transmons with engineered error structure, qLDPC codes and cryo-integrated control; (ii) neutral atoms with zoned architectures, transversal/algorithmic fault tolerance and erasure conversion; (iii) trapped ions with laser-free electronic gates on 2D chip traps; (iv) silicon spin qubits as the long-horizon manufacturability bet; (v) photonics as the interconnect layer of every modular architecture and a high-variance compute bet; (vi) topological qubits — not yet a qubit; (vii) annealing — commercially eroding. Bosonic codes (cats, GKP, dual-rail) are a *direction* that the superconducting mainstream will absorb, not a separate winner.

---

## 1. Criteria — chosen for the task, not for popularity

### 1.1 Why not fidelity

A two-qubit fidelity is an average-case, context-dependent, gate-set-dependent number. It hides error *structure* (coherent vs. stochastic vs. leakage vs. erasure), it is measured in isolation rather than under full parallel load, and it says nothing about time. Cross-technology comparison in fidelity space is meaningless: an ion "99.99%" and a transmon "99.9%" differ by $10^{3}$ in gate duration and by $10^{3}$–$10^{5}$ in QEC cycle time. The invariant object is the **error channel per operation plus its duration**, decomposed by the classes a code treats differently:

| Error class | Cost to fault tolerance | Where it dominates |
|---|---|---|
| Stochastic Pauli | linear, threshold $\sim1\%$ | all platforms after twirling |
| Coherent | accumulates $\sim n^2$; worst-case $\sim\sqrt{r}$ | ions (laser phase), spins (calibration), transmons (ZZ) |
| Undetected leakage | non-Pauli, spreads; needs leakage-removal units | transmons $\lvert2\rangle$, Rydberg decay, valley states |
| **Erasure (detected loss/leakage)** | **cheap: threshold $\sim4\%$ vs $\sim1\%$** | photons (loss), Yb/Sr atoms, dual-rail SC, metastable ions |
| Correlated bursts | catastrophic beyond code distance | transmon quasiparticle bursts (~hourly on Willow), global laser/field noise on ions/atoms |

### 1.2 The six axes (each scored 1–5 with fixed anchors)

| Axis | What it measures | 5 | 3 | 1 |
|---|---|---|---|---|
| **A. Channel quality at scale** | 2Q error and SPAM error *under full-width parallel operation*, plus error-class structure | $\le10^{-4}$ at $\ge50$ qubits | $10^{-3}$–$5\times10^{-3}$ | not shown beyond a few qubits |
| **B. Logical clock** | QEC-cycle time including measurement, reset, transport | $\le1\ \mu$s | $\sim100\ \mu$s | $\ge10$ ms or undefined |
| **C. Scale with quality** | number of qubits that simultaneously meet axis-A quality; connectivity | $\ge1{,}000$ | 50–100 | $<10$ |
| **D. Fault-tolerance progress** | what has been *demonstrated*: break-even, $\Lambda$, logical gates, magic states, decoding | sustained $\Lambda>2$ + logical gates + magic states | many logical qubits beyond break-even (short circuits / detection codes) | none |
| **E. Scaling path** | fab, I/O, cryogenics, modularity — credibility of a route to $10^5$–$10^6$ physical qubits | foundry-proven + modularity demonstrated | foundry-compatible, modularity on paper | bespoke materials, no replication |
| **F. Roadmap credibility** | track record (hits vs. slips), external validation (DARPA QBI stage), funding runway | consistent delivery, Stage B/C, multi-year runway | mixed record | repeated slips / no validation |

Two scores are given where they differ: **[D]** = demonstrated as of Sep 2026, **[R]** = what the roadmap would deliver by ~2029 *if* held. The sum of the six axes is a *maturity index*, not a ranking of usefulness — usefulness is decided in §4 by goal.

### 1.3 The goals

| Goal | What it needs (dominant → secondary) | Scale/time |
|---|---|---|
| **G1 Analog & NISQ many-body simulation** (physics: gauge theories, spin glasses, thermalization) | count × native connectivity × coherence; no QEC | $10^2$–$10^4$ physical, now |
| **G2 Error-mitigated utility circuits** (100–150 qubits, $10^3$–$10^4$ 2Q gates; "advantage candidates", certified randomness) | channel quality at scale, shot throughput | 100–150 physical, now–2027 |
| **G3 Early fault tolerance** ($10^2$–$10^3$ logical qubits, $10^5$–$10^6$ Toffolis: Hubbard models, small catalysts) | logical-qubit count × fidelity; clock secondary | $10^4$–$10^5$ physical, 2027–2031 |
| **G4 Large-scale fault tolerance** ($\ge10^3$ logical, $10^9$–$10^{10}$ Toffolis: RSA-2048, FeMoco, P450) | **clock** × fidelity × count × connectivity | $10^5$–$10^7$ physical, 2030s |
| **G5 Heuristic optimization / annealing** | — (no proven advantage) | now, contested |
| **G6 Networking / distributed QC** (quantum-internet nodes, inter-module links) | photonic interface rate × fidelity × memory | now–2030 |
| **G7 Deployable / sovereign / HPC-embedded systems** (racks, no dilution fridge, on-prem) | footprint, power, integration | now |

Resource anchors for G3/G4 (latest credible estimates): RSA-2048 with $<10^6$ noisy qubits in $<1$ week at $10^{-3}$ error and $1\ \mu$s cycles (Gidney, May 2025); FeMoco/P450 $\sim0.5$–$7\times10^6$ physical qubits and days-to-months at $\mu$s cycles — becoming *years to centuries* at millisecond cycles unless offset by parallelism; 8×8 Hubbard $\sim1.3\times10^{2}$ logical qubits and $\sim3\times10^{5}$ physical, hours (Kivlichan 2020). **2026 updates:** ECDLP-256 in *minutes* with fewer than 0.5 M physical qubits on a planar lattice at $10^{-3}$ (Google, Mar 2026 — ~20× below Litinski 2023) [X11]; RSA-2048 with fewer than 100,000 physical qubits using qLDPC codes at $10^{-3}$, 1 µs cycles (Iceberg Quantum 'Pinnacle', Feb 2026) [X12]; on reconfigurable neutral atoms, Shor for P-256 in days with 10,000 atoms minimum (26,000 in the time-efficient variant), with RSA-2048 one to two orders of magnitude longer on the same architecture (Cain et al., Mar 2026); the RSA-2048 point on that trade curve is 5.6 days on 19 M qubits at a 1 ms cycle (ISCA 2025) [X13] — the count is no longer the barrier; the clock is. See sources [X1]–[X4].

*Cost and energy are not a separate axis here* (system power spans 3 kW for a room-temperature atom machine to 12.5 kW for an annealer and tens of kW for a large dilution-refrigerator installation; $/qubit is quoted only as a Diraq roadmap target of < $1); they enter through G7 and axis E. A reader pricing a deployment should add them explicitly.

---

## 2. Platform profiles — demonstrated vs. intended

Legend: **[D]** demonstrated/published · **[C]** company claim without peer-reviewed data · **[R]** roadmap. Scores follow §1.2 anchors; "[D]/[R]" gives demonstrated / roadmap-if-held.

### 2.1 Superconducting circuits (transmons, fluxonium)

**Demonstrated [D].**
- *Channel at scale:* Google Willow (105 q): mean 1Q 99.97%, 2Q 99.88%, readout 99.5%, mean $T_1$ 68 µs, QEC cycle 1.1 µs [S1][S2]. IBM fleet EPLG (error per layered gate, full-width) $3.7\times10^{-3}$ typical, best $1.9\times10^{-3}$ on ibm_boston (July 2026) [S3][S4]. Zuchongzhi 3.0 (105 q): 2Q 99.62%, readout 99.13% [S5]. Rigetti Cepheus-1-108Q (12 chiplets): median 2Q 99.1% [C] [S6]. Records: IQM tunable-coupler CZ 99.93% over 40 h and Toshiba double-transmon coupler CZ 99.90% in 48 ns [S7]; fluxonium 2Q record **CNOT 99.94% in 60 ns** (Manucharyan group, PRX Quantum 6, 010349), above MIT's 99.922%, which is an RL-optimised mean [S8]. Dominant errors: 2Q gates (~40% of the colour-code budget), leakage, TLS drift, quasiparticle bursts about hourly on Willow [S9].
- *Fault tolerance:* d=7 surface code, $\Lambda=2.14$, memory 2.4× best physical, real-time decoding 63 µs latency at d=5 [S2]; colour code $\Lambda_{3/5}=1.56$, lattice-surgery teleportation, magic injection >99% [S9]; magic-state cultivation fidelity 0.9999(1) with 8% acceptance [S10]; RL-steered calibration during QEC, **record d=7 logical error $7.72\times10^{-4}$/cycle** (July 2026) [S11]. China: USTC 107-qubit processor (reported as Zuchongzhi 3.2; the PRL does not name it) d=7 below threshold, $\Lambda=1.40$ [S12]; USTC logical CNOT between d=3 patches (fidelity 0.643, no post-selection) [S13]; Zhejiang 125-q lattice surgery [S14]. IBM: 70 "logical" qubits in an error-*detecting* spacetime code, 468 T gates (July 2026) — a mitigation-class result, not fault tolerance [S15]; Relay-BP decoder for the [[144,12,12]] gross code on FPGA <1 µs/cycle (simulation) [S16].
- *Scale/modularity:* Nighthawk 120 q square lattice, 5,000 2Q gates per circuit [S17]; IBM Loon (c-couplers, multilayer routing) fabricated and two coupled cryogenic cells (Aug 2026) [C] [S18]; Rigetti's chiplet tiling is the only shipped multi-chip system and shows the fidelity cost of tiling (99.6%→99.1%) [S6]; Fujitsu/RIKEN 256 q with 3D-stacked cells [S19]. Cryo-integrated control: SEEQC SFQ digital control of qubits at millikelvin temperature, 1Q fidelities >99% and up to 99.9% (Nature Electronics, Mar 2026); the 5-qubit / nW-per-qubit / no-quasiparticle-poisoning details are from SEEQC's press coverage [C] [S20]; SEEQC–IBM SFQ integration under QBI (announced June 2025) [S21]; Google absorbed Atlantic Quantum for its cold-stage control stack [S22].
- *Commercial:* IBM $10 B commitment (June 2026) [S23]; IQM Nasdaq listing, 23 systems sold [S24]; OQC £260 M Series C [S25]; Rigetti ~$570 M cash [S26]; Google Willow by proposal only [S27]. **DARPA QBI Stage B: IBM is the only transmon vendor**; Google (which joined Stage A only in Sept 2025), Rigetti and Atlantic Quantum were not on the Nov-2025 Stage-B list — DARPA says further teams may still enter [S28].

**Justified intentions [R].** IBM: Kookaburra (first qLDPC memory + logic module) 2026 — slipped one year from the 2023 roadmap; Cockatoo (L-couplers between modules) 2027; **Starling 2029: 200 logical qubits, $10^8$ gates; Blue Jay 2033: 2,000 logical, $10^9$ gates** [S29]. Track record: Heron r3, Nighthawk r1 and the decoder came on or ahead of time; the "quantum advantage by end-2026" claim rests on IBM's own definition. Google: six-milestone roadmap, next is the "long-lived logical qubit" ($10^{-6}$); "commercially relevant" by end of decade [S1]. Rigetti: 108 q at 99.5% slipped from end-2025 to "later 2026" [S30]. IQM: 150-q Halocene at 99.7% (late 2026), FT 2030 [S31]. Fujitsu: 1,000 q in 2026 (unconfirmed), 250 logical FY2030 [S19].

**Bottlenecks.** $\Lambda\approx1.4$–$2.1$ is too small: from $7.7\times10^{-4}$ at d=7 with $\Lambda\approx2$, reaching $10^{-6}$ requires d≈25 and $>10^{3}$ physical qubits per logical qubit unless physical errors fall well below $10^{-3}$. Readout ($\sim10^{-2}$ at scale) is the weakest link. Logical two-qubit gates exist only at d=3. No qLDPC memory has run on hardware — as of 3 Sep 2026 Kookaburra is not delivered and no gross-code/bivariate-bicycle result exists on IBM hardware (the only BB-code hardware runs are IonQ's 4-logical-in-18-ion memory, reported as [[18,4,3]], and Zhejiang's 32-qubit [[18,4,4]] at 8.9%/cycle) [S32]. Google has published no successor to Willow and no multi-chip result; the July-2026 record paper reports no Λ for the d=7 run [S33]. Fujitsu's 1,000-qubit machine is scheduled for fiscal 2026 (Apr 2026–Mar 2027), not yet launched [S34]. Per-qubit coax/flex wiring persists; cryo-CMOS/SFQ demos are ≤5 qubits. No cross-module QEC anywhere.

**Scores.** A 3 · B **5** · C 4 · D **4** · E 4 · F 4 → **24/30 [D]**; [R] adds mainly on A (0.1%→0.05% targets) and C (modules).

### 2.2 Bosonic superconducting codes: cat, GKP, dual-rail erasure

**Demonstrated [D].**
- *Cats:* bit-flip times of 430 s (Alice & Bob Boson 4), mean 44 min on the 12-cat "Helium 2" chip (preliminary, Sept 2025), 22 s for a squeezed cat [B1][B2]; AWS Ocelot: 5 cat + 4 ancilla + 5 buffers, repetition code d=3 1.75% at $|\alpha|^2=1$ → d=5 1.65% at $|\alpha|^2=1.5$ per 2.8-µs cycle — two points at different mean photon numbers, not a distance scan, because the **phase-flip is $9.6(4)\times10^{-2}$ per CX at $\bar n=2$** (bit-flip $3.5(4)\times10^{-3}$) and the bias is only >25 under the gate, >30 idle [B3]. No cat–cat CNOT has been demonstrated (AWS's July 2026 CNOT is theory) [B4].
- *GKP:* Nord Quantique single-mode GKP: $T_1=360$ µs, logical error $8.1\times10^{-3}$/round, SPAM $<10^{-3}$ **with survival 0.24×0.39** (heavy post-selection) [B5]; Yale/Google GKP qudits beyond break-even (gain 1.8–1.9) [B6]. Best bosonic memory gain anywhere ≈2.3 — nothing resembling $\Lambda$ scaling.
- *Dual-rail erasure:* Yale/QCI (now D-Wave) cavity dual-rail CZ ~500 ns, **erasure 0.53%/gate, remaining post-selected Pauli error <0.1% (0.12% bound at depth)**, bit-flips $\sim10^{-6}$, SPAM ~0.02% (Nature, Aug 2026) — gate-level erasure fraction ≈80% [B7]; AWS transmon dual-rail: 384-ns erasure check, residual $6\times10^{-4}$, bias 42 [B8]; 8-qubit Aqumen Seeker shipped (2024) [B9].
- *Commercial:* Alice & Bob Series B extension with NVentures, French GENCI bought the first "Helium" (June 2026) — **no logical-qubit performance data published for the 18-cat system**; **not selected for QBI Stage B** [B10][B11]. Nord Quantique: QBI Stage B, $1.4 B valuation (May 2026) [B12]. D-Wave acquired QCI for $550 M (Jan 2026) [B13].

**Justified intentions [R].** Alice & Bob: Graphene 2030 — 2,000 cats / 100 logical / $10^{-6}$, requiring ≥13-min bit-flip *during CNOT* [B14]. Nord Quantique: 100+ logical by 2029, "1:1 physical:logical" [B15]. D-Wave/QCI: 17 qubits 2026, 181 in 2028, 10 logical 2030, 100 logical 2032, target $\Lambda=10$ [B16].

**Bottlenecks — are the "100–1000× fewer qubits" claims holding?** No, not yet. The headline estimates (126,133 cats for ECC-256 in 9 h; 758 cats for 100 logical qubits) assume $0.1\%$ phase-flip per cycle at $\bar n\approx19$; measured phase-flip per cycle is $\sim10^{-1}$ — two orders of magnitude off. Bias-preserving cat–cat gates: undemonstrated. Erasure qubits are the credible part of this family: 82–90% erasure fraction with $10^{-3}$ residual Pauli is a good channel, but false-negative rates (1.5–8%) and ancilla transmons dominate the budget, and the marketed "99.9%" is post-selected.

**Scores.** A 2 · B **5** · C 1 · D 2 · E 3 · F 2 → **15/30 [D]**; [R] if phase-flip falls 100×: A→4, D→4.

### 2.3 Trapped ions

**Demonstrated [D].**
- *Channel at scale:* **Quantinuum Helios (98 Ba⁺): 1Q $2.5\times10^{-5}$, 2Q $7.9\times10^{-4}$, SPAM $3.3$–$4.8\times10^{-4}$, leakage $1.1\times10^{-5}$/Clifford**, all-to-all via ring + junction, 8 zones [I1]. H2 (56 q): QV $2^{25}$ [I2]. IonQ Forte (36 q): 2Q 0.4%, SPAM 0.5% [C] [I3]; its laser (MS) gates take **550–883 µs (median 672 µs)** on 30+-ion chains, 1Q 110 µs [I27]; Tempo publishes only '99.9% fidelity' and #AQ 64 with no gate times [C]. Oxford Ionics' electronic gate lasts 225.8 µs (2025) / ≈120 µs (2024) [I4]. Records: **2Q $8.4\times10^{-5}$ with electronic (laser-free) gates, no ground-state cooling** (IonQ/Oxford Ionics, Oct 2025) [I4]; 1Q $1.5\times10^{-7}$ (Oxford) [I5]; hour-scale memory [I6].
- *Fault tolerance:* Helios: **48 error-corrected logical qubits ([[80,48,4]]) with logical gate error $\sim1\times10^{-4}$ vs $8\times10^{-4}$ physical, logical SPAM $<8\times10^{-6}$**, 94 error-detected qubits in a GHZ state, 64-logical-qubit XY simulation (3.2% acceptance at depth) [I7]; logical teleportation 99.82% [I8]; magic states in [[6,2,2]] at $7\times10^{-5}$ infidelity [I9]; FT QAOA/HHL with a Steane-code T gate at $2.6\times10^{-3}$ [I10]. IonQ: nine codes on 40 ions, including a **bivariate-bicycle qLDPC memory of 4 logical qubits in 18 ions (reported as [[18,4,3]]; the abstract gives no code notation) at break-even (3.95 ± 0.68 s vs 3.3 ± 0.9 s physical), with leakage post-selection** [I11]. No $\Lambda$-type distance scaling on any ion system.
- *Speed:* Helios 2Q gate ~70 µs but **~55 ms per full-width layer** (sorting, transport, cooling dominate); transport ≈60% of runtime on H2 [I1][I12]; IonQ assumes 1–5 ms syndrome cycles [I13].
- *Scale/modularity:* Quantinuum grid trap with 2.5 kHz ion exchange; junction transport at 4 m/s [I14]; Oxford distributed QC over a 2-m photonic link: remote Bell 96.9% at 9.7 s⁻¹, teleported CZ 86% [I15]; 250 s⁻¹ (Duke/Maryland) [I16]. Tsinghua 512-ion 2D crystal (analog) [I17].
- *Commercial:* Quantinuum $600 M at $10 B (Sep 2025), **IPO June 2026 ($1.68 B, Nasdaq QNT)**, cash $2.1 B, four Helios systems [I18][I19]; IonQ $3 B equity raised in 2025, acquisitions of Oxford Ionics ($1.075 B), Lightsynq, ID Quantique, Vector Atomic, **SkyWater foundry ($1.8 B, announced Jan 2026, closed July 2026)** [I20][I21]; Quantum Art $140 M Series A (Israel) [I22]; eleQtron €57 M; AQT rack-mounted, QV 32,768 [I23]. **QBI Stage B: Quantinuum and IonQ** [S28].

**Justified intentions [R].** Quantinuum: Sol 2027 (192 physical, ~100 logical, 2D grid trap fabricated by Honeywell, in validation) → **Apollo 2029 (thousands physical, hundreds logical, $10^{-6}$–$10^{-10}$)** [I24]; "near five-nines logical fidelity with a novel code family" claimed on the Q2-2026 call, paper not yet public [I25]. Track record: strong — QV 10×/year promise met, Helios launched on schedule. IonQ: 256 q at 99.99% (slipped to H1 2027), 10,000 on one chip 2027, **2 M physical / 40–80 k logical by 2030** [I26]. Track record: the 2020 roadmap promised 4,000 qubits by 2026 (missed ~40×); the 99.99% gate is real, the 100→10,000 jump has no published 2D-trap heating, gate-time or interconnect data.

**Bottlenecks.** Clock: $10^{3}$–$10^{5}$× slower than superconducting per layer; transport and cooling, not gates, set throughput. High-rate code demos discard 75–97% of shots at depth. 2D scaling unproven at product scale (Sol is the first test). Interconnects at 10–250 s⁻¹ vs $\sim10^{4}$ s⁻¹ needed. Optical complexity (Helios ≥7 laser wavelengths, 1,228 electrodes) — electronic gates remove lasers but have no published gate time at scale.

**Scores.** A **5** · B 2 · C 3 · D **4** · E 3 · F 3 (Quantinuum 4 / IonQ 2) → **20/30 [D]**; [R] Sol/Apollo would lift C→4, B→3 (2× speed-ups per generation).

### 2.4 Neutral atoms (Rydberg tweezer arrays)

**Demonstrated [D].**
- *Channel:* CZ **99.854% raw / 99.941% loss-post-selected** stable over 10 h (Harvard, Apr 2026) [N1]; 99.72/99.40% (Atom Computing, Yb) [N2]; 99.71% (Caltech, Sr) [N3]; QuEra Gemini spec 2Q 99.2% global [N4]. Non-destructive readout 0.46% bit-flip + 0.24% loss [N5]; hyperfine $T_2$ 1.3 s, 12.6 s in a 6,100-atom Cs array [N6]. Dominant error: **atom loss (>80% of leakage events) — detectable, hence erasure-convertible**; Rydberg decay 0.05–0.1%; a 2026 review argues the standard CZ scheme saturates near 99.9% without new gate physics [N7]. Erasure conversion demonstrated in metastable Yb (Princeton) and Sr (Caltech), with [[4,2,2]] logical teleportation under erasure-biased noise (Nature Physics, June 2026) [N8][N9].
- *Scale:* **448 atoms under full fault-tolerant control** [N5]; **>3,000 qubits maintained >2 h with continuous reloading** (300,000 atoms/s reloaded into tweezers, 30,000 initialised qubits/s) [N10]; 6,100-atom Cs array with 12.6-s coherence [N6]; 11,000 Rb atoms trapped in 18,225 metasurface tweezers (Tsinghua, June 2026; no gates) [N11]; Atom Computing 1,225-site Yb array; Pasqal 1,024 atoms [C].
- *Fault tolerance:* Harvard/MIT/QuEra 448-atom architecture (Nature, Nov 2025): surface codes d=3→5 with **2.14× suppression in a 4-round circuit** (not long memory), [[7,1,3]], [[15,1,3]] with transversal T, [[16,6,4]] with **up to 96 logical qubits active**, hundreds of logical teleportations, mid-circuit qubit reuse [N5]; **logical magic-state distillation** (5-to-1, d=3 and d=5 colour codes) [N12]; Atom/Microsoft toric code: $\Lambda_Z\approx1.9$ but $\Lambda_X\approx1.2$ (average 1.30) over 4 cycles, **90 rounds sustained with reloading — but suppression vanished once reloading was included** (0.63% vs 0.64%/cycle) [N13]; Microsoft/Atom 24 entangled logical qubits, 28 running Bernstein–Vazirani better than physical (2024) [N14]; Infleqtion 12 logical qubits with loss correction, Shor N=15 [N15].
- *Speed:* CZ 270 ns, but imaging ~0.5–1 ms and transport ~100s µs give **QEC rounds of ~1–4.5 ms** [N5][N16]; transversal + correlated decoding (algorithmic fault tolerance: constant syndrome rounds per logical gate) is the compensating theory [N17]; RSA-2048 estimate for a transversal atom architecture: 19 M atoms, 5.6 days at 1 ms cycles [N16].
- *Commercial:* QuEra $230 M+ Series B expansion, closed 9 Sept 2025 (Google, SoftBank Vision Fund 2, NVentures) [N18]; **Atom Computing $300 M+ incl. $100 M US DoC LOI (June 2026)** [N19]; Infleqtion NYSE listing Feb 2026 (>$550 M) + $100 M DoC LOI [N20]; Pasqal SPAC closed Aug 2026 (~$360 M cash, €16.5 M 2025 revenue) [N21]; QuNorth ordered "Magne" (1,225 physical / 50 logical, €80 M) from Atom/Microsoft [N22]; **Google opened a neutral-atom hardware track under Adam Kaufman (March 2026)** [N23]. **QBI Stage B: Atom Computing and QuEra** [S28].

**Justified intentions [R].** QuEra: Jan-2024 roadmap promised 100 logical qubits in 2026 → now **"Libra" 2028 (>256 logical, $10^{-6}$, on Braket) and a gigaquop system 2028–29** (>1,000 logical, >20,000 physical per core) — a two-year slip [N24]. Atom/Microsoft: Magne 50 logical qubits at turn of 2026/27, being installed [N22]. Pasqal: 10,000 physical slipped 2026→2028; 100 logical 2029 [N25]. Infleqtion: 30 logical 2026, >50 logical Illinois system 2027, 1,000 by 2030 [N15]. Google: QEC-focused, no commercial date.

**Bottlenecks.** The millisecond cycle ($10^{3}$× slower than superconducting) is the single structural disadvantage; decoders must keep up in real time. Below-threshold operation shown only in short circuits — no long-memory $\Lambda>2$ with reloading yet. Scale-with-quality gap: 11,000 trapped vs 448 with logical control. Laser power, SLM/AOD bandwidth (10 MHz refresh insufficient above ~$10^4$ qubits), multi-core interconnects unproven.

**Scores.** A 4 · B 2 · C 4 · D **4** · E 4 · F 3 → **21/30 [D]**; [R] Libra/Magne would lift D→5, C→5.

### 2.5 Photonic (linear-optical / fusion-based / continuous-variable)

**Demonstrated [D].**
- *Components (excellent):* PsiQuantum Omega (300-mm GlobalFoundries): purity 99.5%, HOM 99.5%, **fusion Bell fidelity 99.22%**, chip-to-chip Bell 99.72% over 42 m, waveguide loss 0.5 dB/m, 2 K [P1]; USTC quantum-dot source 71.2% system efficiency — first above the 2/3 loss-tolerance threshold [P2]; Xanadu edge-coupling 0.085 dB/facet (June 2026) [C] [P3].
- *Systems:* Xanadu Aurora — 35 chips, 12 modes per 1 MHz cycle, a 12×N cluster state generated for 2 h, **at ~14 dB total loss, no error-corrected computation** [P4]; on-chip GKP state at 0.62 dB effective squeezing vs ~10 dB needed [P5]; Jiuzhang 4.0 boson sampling, 3,050 photon clicks (Nature, May 2026) — non-universal, contested by loss-exploiting classical algorithms [P6]; Quandela 12-qubit Belenos/Lucy delivered to CEA (Oct 2025) [P7]; QuiX 8-qubit universal MBQC subsystems delivered to DLR (July 2026), commissioning pending [P8].
- *Fault tolerance:* **no photonic logical qubit exists.** Xanadu states its loss is 24× above threshold in 2026, targets 1× in 2030 [P9]. Theory: fusion-based QC tolerates 2.7% per-photon loss with 6-ring resource states, up to 17% with 168-qubit resource states nobody can make [P10].
- *Commercial:* PsiQuantum $1 B Series E at $7 B (Sep 2025) [P11], **DARPA QBI Stage C via US2QC: $31.8 M + $125 M expanded (July 2026) for validation of BTO switches, packaging and cryogenics** [P12]; Brisbane site changed and groundbreaking slipped to June 2026, cryoplant 2H 2027 — the "useful by end-2027" target is at risk; CEO change Feb 2026 [P13]. Xanadu SPAC closed Mar 2026 (~$302 M, 40% below plan), CAD 195 M Canadian factory funding (Aug 2026), first quantified roadmap 31 Aug 2026: FT milestone 2028–29, up to 200 logical qubits by 2029, 500 by 2030, 1,000+ by 2031 [P9][P14]. Photonic Inc $200 M at $2 B (T-centres, spin-photon) [P15]; **QBI Stage B: Xanadu, Photonic Inc**; Quandela Stage A (June 2026) [S28][P16].

**Justified intentions [R].** PsiQuantum "before 2033" utility scale; Xanadu 1,000+ logical by 2031; Quandela 50 logical by 2028 (its 2025 first-logical-qubit milestone was missed); ORCA PT-3 (2026) not delivered.

**Bottlenecks.** Loss is the whole game: every switch costs 0.1–0.2 dB against a total budget of ~0.5 dB; GKP squeezing is 9 dB short; sources are probabilistic, forcing multiplexing depth ~10; thousands of cryogenic detector channels and MHz–GHz feed-forward are unproven at system level. PsiQuantum has published no 2026 hardware demonstration — its progress is visible only through DARPA V&V contracts.

**Scores.** A 2 (component-level) · B — (design 4) · C 1 · D 1 · E 3 · F 2 → **9/30 [D]** (13 with design-level clock); [R] if loss falls 20×: D→3–4, C→4.

### 2.6 Semiconductor spin qubits (Si/SiGe, Si-MOS, Ge, donors) and solid-state defects

**Demonstrated [D].**
- *Channel:* 1Q up to 99.97% (Diraq/imec 300 mm), $2\times10^{-4}$ mean over 18 exchange-only qubits (HRL) [Q1][Q2]; **2Q 99.04–99.56% on foundry 300-mm devices** (Diraq/imec, Nature Sep 2025) [Q1]; 99.90% donor nuclear-spin CZ (SQC) [Q3]; CZ between *moving* spins 98.86% (Delft, May 2026) [Q4]; 1 K operation at 98.9% 2Q [Q5]. Readout 1–100 µs; no erasure channel. Dominant errors: residual ²⁹Si, charge noise, and — per HRL — **~80% of CNOT error is extrinsic control/calibration** [Q2].
- *Scale:* 18-qubit Ge array at identical voltages (Groove/QuTech), 18 EO qubits from 54 dots (HRL), 12 (Intel Tunnel Falls), 10-qubit 2D Ge lattice; conveyor-mode shuttling 10 µm at 99.5% [Q6]; 8-qubit imec device with exchange working in only 1 of 4 pairs [Q7].
- *Fault tolerance:* **HRL: d=5 repetition code, 200 rounds, $\Lambda_{5/3}=4.7$, [[4,2,2]] logical fidelity 0.95 (post-selected), all sequenced by a 4-K cryo-CMOS controller with no room-temperature real-time electronics** (Nature, July 2026) [Q2]; donor [[4,2,2]] universal gate set (SUSTech) [Q8]. No below-threshold logical memory on any spin platform.
- *Manufacturing:* Intel 300 mm EUV (>24,000 devices/wafer, 96% tune-up yield) [Q9]; GlobalFoundries 22FDX (Quantum Motion: 1,024 dots characterised in 5 min; full-stack system at UK NQCC) [Q10]; STMicro FD-SOI (Quobly); mK cryo-CMOS co-located with qubits (UNSW/Diraq, Nature 2025) [Q11].
- *Commercial:* **IBM acquired HRL Laboratories (announced July 2026) to add spin qubits, cryo-CMOS control and packaging to its roadmap** [Q12]; Quantum Motion $160 M Series C; Quobly €115 M; Diraq >$100 M + $38 M CHIPS LOI; SQC A$60 M; **QBI Stage B: Diraq, Quantum Motion, SQC, Photonic** — four of eleven [S28]. Intel: no new chip since Tunnel Falls; a 12-qubit processor was deployed at Argonne under Q-NEXT (Jan 2026) with Intel stating it will 'scale to hundreds of dots' — the program is alive but without a dated roadmap [Q15].
- *Defect qubits (NV/SiV/SnV/T-centre):* gate errors <0.1% (Fujitsu/QuTech NV); SiV entanglement over 35 km deployed fibre at ~1 Hz (Harvard); T-centre teleported CNOT between cryostats — **network nodes, not processors** [Q13].

**Justified intentions [R].** Diraq: 150 k physical / 1 k logical by 2029, >2 M physical by 2031 at <$1/qubit — but six weeks earlier its release said "thousands by 2029" (inconsistent messaging) [Q14]. Quobly: millions of qubits 2032. SQC: commercial scale 2033. Quantum Motion: "commercially useful this decade", NQCC delivery on schedule.

**Bottlenecks.** No device >12 qubits has published all-pairs 2Q fidelities; 2Q plateau at 99–99.6% in foundry devices; readout is slow and sensor-hungry (cycle ~100s of µs); hot operation costs ~1% fidelity; roadmaps are >100× beyond any demonstrated device. The 2026 signal is nonetheless real: HRL's self-sequenced QEC and IBM's acquisition are the first evidence that the CMOS argument is being taken seriously by a hyperscaler.

**Scores.** A 2 · B 3 · C 2 · D 2 · E 3 (ceiling 5) · F 3 → **15/30 [D]**; [R] is the widest spread of any platform.

### 2.7 Topological (Majorana) qubits

**Demonstrated [D].** Single-shot *parity* readout of one InAs–Al nanowire: 1% assignment error, ms dwell times (Nature, Feb 2025) — with an editor's note that the results do not by themselves establish Majorana zero modes in the devices [T1][T2]. Tetron Z-loop parity lifetime 12.4 ms vs **X-loop 14.5 µs (~1000× shorter)**, preprint July 2025 — other tunings in the same preprint give ~9.3 ms and ~4 µs, so the ~10³ ratio is robust but the point values are not, and the paper attributes the gap to the X loop's larger quasiparticle-capture cross-section, not to flux noise [T3]. **"Majorana 2" (arXiv:2606.03884, June 2026): InAs–Pb, ~20-s parity switching time in one wire of one tetron — a parity switching time, not a qubit lifetime; no braiding, no joint-parity/X measurement, no two-qubit operation, no entanglement, no Bell test, no qubit $T_1/T_2$** [T4]. Microsoft's blog calls the 20 s a "qubit lifetime" and re-states a 2029 fault-tolerant target [T5]. Independent: QuTech "poor man's" Kitaev-chain parity readout >1 ms and a coherent minimal-Kitaev-chain parity qubit with "only limited protection" (2026) [T6][T7]; Legg's critique became a Nature Matters Arising (June 2026); Microsoft's multi-author reply concedes nothing [T8]. DARPA: US2QC final phase (Feb 2025), not in QBI Stage B [T9].

**Justified intentions [R].** "Years not decades" (2025) → "2029" (2026). Given the 2018 retraction, the contested TGP protocol and the absence of any two-qubit result, the roadmap has no demonstrated base.

**Assessment.** No topological qubit has been demonstrated. What exists is high-fidelity single-wire parity readout in a better material, whose topological origin is contested and untestable until X/Z-comparable lifetimes, two-qubit operations, or independent replication appear.

**Scores.** A 1 · B — · C 1 · D 1 · E 1 · F 1 → **5/30 [D]**.

### 2.8 Quantum annealing and analog machines

**Demonstrated [D].** D-Wave Advantage2 GA (May 2025): 4,400+ qubits, Zephyr 20-way connectivity, 12.5 kW [A1]. "Beyond-classical" spin-glass dynamics (Science, Mar 2025) was substantially eroded within weeks by belief-propagation tensor networks (Tindall et al., Science May 2026) and t-VMC (Mauron & Carleo); D-Wave maintains that its largest/most-frustrated instances remain unmatched — unresolved but the classical frontier moved [A2][A3]. Finances: FY2025 revenue $24.6 M; **H1-2026 revenue $5.9 M (−67% YoY)**, CFO resigned Aug 2026 [A4]; pivot to gate model via QCI (§2.2). Analog simulators: Google 69-q analog-digital simulator (beyond-classical only for XEB-style benchmarking) [A5]; QuEra Aquila (256 atoms, on Braket) string-breaking in a gauge theory — no advantage claim [A6]; Quantinuum digital magnetism (Nature 2026) — heuristic claim [A7].

**Sober view.** No analog machine has solved a scientifically posed problem demonstrably beyond classical reach with an unchallenged claim; the value of analog platforms is as physics instruments (G1) and as stepping stones (QuEra/Pasqal analog → digital).

**Scores.** Not comparable on A–D (no gate channel); E 4 (mature manufacturing), F 2. Roadmap: 20,000 qubits 2029, 100,000 in 2031 [A4].

---

## 3. Scoreboards

### 3.1 Criteria scores (demonstrated, Sep 2026)

| Platform | A Channel at scale | B Logical clock | C Scale w/ quality | D FT progress | E Scaling path | F Roadmap credibility | **Maturity index** |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Superconducting | 3 | **5** | 4 | **4** | 4 | 4 | **24** |
| Neutral atoms | 4 | 2 | 4 | **4** | 4 | 3 | **21** |
| Trapped ions | **5** | 2 | 3 | **4** | 3 | 3 | **20** |
| Bosonic (cat/GKP/dual-rail) | 2 | **5** | 1 | 2 | 3 | 2 | 15 |
| Spin qubits (Si/Ge) | 2 | 3 | 2 | 2 | 3 | 3 | 15 |
| Photonic | 2 | (4 design) | 1 | 1 | 3 | 2 | 9 (13) |
| Topological | 1 | — | 1 | 1 | 1 | 1 | 5 |
| Annealing | n/a | n/a | n/a | n/a | 4 | 2 | n/a |

The index measures *how much of the fault-tolerance stack has been shown to work*, not usefulness. Read it together with §3.3 and §4.

*Sensitivity.* Each cell is a judgment with ±1 uncertainty. The superconducting lead (24) survives any single ±1 change; the neutral-atom/trapped-ion order (21 vs 20) does not — it flips if axis C or F moves one step either way, so treat those two as tied. Axis F mixes vendors inside a platform (Quantinuum ≈ 4, IonQ ≈ 2; QuEra/Pasqal ≈ 2–3 after two-year slips, Atom/Infleqtion ≈ 3–4): read F per leading vendor, not per platform. Every number behind these scores carries a [D]/[C]/[R] tag in §2; a score built mainly on [C] figures (bosonic F, photonic E) inherits that weakness.

### 3.2 Fault-tolerance primitives — who has shown what

| Primitive | Superconducting | Trapped ions | Neutral atoms | Bosonic | Photonic | Spin |
|---|---|---|---|---|---|---|
| Below-threshold scaling ($\Lambda$) | **$\Lambda=2.14$ (d=3→5→7); separate $10^6$-cycle real-time-decoded run at d=5; d=7 at $7.7\times10^{-4}$** | none (concatenation instead) | 2.14× (d=3→5, 4 rounds); $\Lambda_Z\approx1.9$ / avg 1.3 (4 cycles), lost with reloading | repetition-cat "flat" below threshold | none | repetition d=5 $\Lambda=4.7$ (bit-flip only) |
| Most logical qubits beyond break-even | 1–2 | **48 corrected / 94 detected** | **96 (d=4 blocks) / 28 in algorithm** | 1 | 0 | 0 |
| Logical 2Q gates | d=3 lattice surgery (CNOT 0.64); colour-code teleportation | transversal + lattice surgery (0.85–0.98), teleportation 99.8% | **transversal CNOTs, hundreds of teleportations** | — | — | — |
| Magic states on logical qubits | **cultivation 0.9999** (8% accept) | code-switching $5\times10^{-4}$; [[6,2,2]] $7\times10^{-5}$ | **5-to-1 distillation** on d=3/5 colour codes | — | — | — |
| Real-time decoding | 63 µs at d=5; FPGA <1 µs/round (sim); RL calibration in-loop | in-loop (teleportation); GPU on Helios | offline ML (1.7× gain) | — | detection only | self-sequenced by cryo-CMOS |
| qLDPC on hardware | components (Loon); gross code pending | **BB memory at break-even, 4 logical in 18 ions (reported as [[18,4,3]]; leakage post-selected)** | theory: $10^{-13}$/round at $p=10^{-3}$ | — | SHYPS codes (theory) | — |
| QEC cycle | **1.1 µs** | ~1–5 ms (55 ms/full layer) | ~1–4.5 ms | 2.8 µs | MHz by design | ~100s µs |

### 3.3 Revealed preferences — how the majors hedge (2025–26)

| Actor | Primary bet | Second bet | Signal |
|---|---|---|---|
| Google | superconducting (Willow, next: long-lived logical qubit) | **neutral atoms** — new hardware track, Mar 2026 | "superconducting scales in time, atoms scale in space" (Neven) |
| IBM | superconducting + qLDPC (Starling 2029), $10 B | **silicon spin** — HRL acquisition, Jul 2026 | wants CMOS density + cryo-CMOS control |
| Microsoft | topological (no qubit yet) | **neutral atoms** — sells Magne with Atom Computing | revenue comes from the hedge |
| AWS | cat qubits (Ocelot), dual-rail erasure | **neutral atoms / ions / SC via Braket**, QuEra co-design | hardware-efficient QEC as research, everything else as marketplace |
| NVIDIA | none | NVQLink + investments in Quantinuum, QuEra, Alice & Bob, others | the decoding/control layer is platform-agnostic |
| IonQ | trapped ions | **electronic gates (Oxford Ionics) + foundry (SkyWater) + photonic networking (Lightsynq)** | vertical integration, ion-only |
| D-Wave | annealing (revenue −67%) | **dual-rail erasure SC** (QCI, $550 M) | annealing is being abandoned as the growth story |
| DARPA QBI Stage B (11) | atoms ×2, ions ×2, SC ×1, bosonic ×1, spin ×3, spin-photon ×1, photonic ×1 | Stage C: PsiQuantum, Microsoft (via US2QC) | Google, Rigetti, Alice & Bob, Oxford Ionics were **not** on the Nov-2025 list (DARPA: more teams may still enter) |

The pattern is unambiguous: every deep-pocketed actor pairs one **fast** platform (superconducting, in some form) with one **dense** platform (atoms or spins). Nobody pairs two slow platforms. That is the market's estimate of §1.3: speed matters for G4, density for G3.

---

## 4. Goals × technologies — fit matrix

●●● best fit · ●● good · ● marginal · ○ unsuitable. Left symbol = demonstrated (2026), right = credible trajectory (~2029) where different.

| Goal | Superconducting | Trapped ions | Neutral atoms | Bosonic SC | Photonic | Spin | Topological | Annealing |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **G1** Analog / NISQ many-body physics | ●●● | ●● | ●●● | ○ | ● | ○ | ○ | ●● |
| **G2** Error-mitigated utility (100–150 q) | ●●● | ●●● | ●● → ●●● | ○ | ● | ○ | ○ | ○ |
| **G3** Early FT ($10^2$–$10^3$ logical) | ●● → ●●● | ●●● | ●●● | ● → ●● | ○ → ● | ○ → ● | ○ | ○ |
| **G4** Large-scale FT (RSA-2048, FeMoco) | ●● → ●●● | ● | ● → ●● | ● → ●● | ○ → ●● | ○ → ●● | ○ → ? | ○ |
| **G5** Heuristic optimization | ● | ● | ● | ○ | ○ | ○ | ○ | ●● (contested) |
| **G6** Networking / distributed QC | ● | ●●● | ●● | ● | ●●● | ●●● (defects) | ○ | ○ |
| **G7** Deployable / on-prem / HPC-embedded | ●● | ●●● | ●●● | ● | ●● | ●● | ○ | ●● |

**Why the cells are what they are.**

- **G1.** Atoms (Aquila 256, 6,100-atom Cs, gauge-theory string breaking) and superconducting (Google's 69-q analog-digital simulator, Quantinuum's digital magnetism on ions as the runner-up) are the instruments physicists actually use; annealers do genuine spin-glass dynamics but every "beyond classical" claim is under active erosion.
- **G2.** Superconducting wins on throughput (IBM Nighthawk: 5,000–7,500 2Q gates per circuit, 100 kHz-class shot rates; Q-CTRL 120 q with $10^4$ gates) and ions win on per-shot quality (Helios; certified randomness) but lose on shots/s (~18/s at full width). The 2026 "advantage candidates" (IBM 70-q doped-Clifford, Qedma 74-q Floquet cross-checked on Helios, Google OTOC) all live here.
- **G3.** This is the ions' and atoms' window: 48 corrected logical qubits today (Helios), 50 (Magne) at the turn of the year, ~100 (Sol) in 2027, >256 (Libra) in 2028 — all with transversal or high-rate codes that superconducting nearest-neighbour lattices cannot use. Superconducting reaches the same count only via qLDPC modules (Kookaburra → Starling 2029). Hubbard-class problems ($\sim10^5$–$10^6$ Toffolis, hours at µs cycles) tolerate a slow clock: at 1 ms cycles they take days-to-weeks, which is acceptable.
- **G4.** Only the microsecond-class platforms can run $10^{9}$–$10^{10}$-Toffoli algorithms in days rather than decades. Superconducting is the only fast platform with demonstrated $\Lambda$; bosonic codes, photonics and spins are fast *by design* but have not shown a logical qubit (photonic, spin) or a working phase-flip budget (cats). Atoms can partially compensate through transversal architectures (19 M atoms, 5.6 days for RSA-2048 in one estimate) — plausible, unproven. Ions at 1–5 ms syndrome cycles with $10^{4}$-qubit chips that do not yet exist cannot be placed above ● today.
- **G5.** No platform has a credible optimization advantage: Grover-type speedups are useless on early FT hardware, DQI's advantage is on a contrived problem, QAOA evidence is noiseless simulation ≤40 qubits. Annealing gets ●● only for being deployed and occasionally useful as a heuristic.
- **G6.** Photonics is the interconnect no matter who wins compute; ions (Oxford's distributed CZ) and defect spins (SiV over 35 km, T-centres) are the demonstrated network nodes; atoms are joining (Atom Computing–Nu Quantum/Cisco); superconducting lacks a microwave-to-optical transducer of useful efficiency.
- **G7.** Room-temperature racks (AQT, IonQ Tempo, Equal1, ORCA, Quandela) and <4 kW atom systems (Pasqal) versus dilution-refrigerator superconducting — though IQM's 23 delivered systems show on-prem superconducting is a real market.

---

## 5. Most promising directions

Ranked by expected contribution to a utility-scale fault-tolerant computer by ~2033, weighting demonstrated physics ×2, scaling path ×1, roadmap credibility ×1. "Direction" is deliberately narrower than "platform": within each platform, one specific line of work carries the promise.

**1. Superconducting transmons with engineered error structure, qLDPC codes and cold-stage control.**
The only platform with demonstrated $\Lambda$ scaling in long memory, a microsecond clock, a 300-mm fab line, modular cryogenics, and a $10 B balance sheet behind a dated roadmap. The specific direction that matters is *not* "better transmons": it is (a) converting the error channel — dual-rail erasure (D-Wave/QCI, AWS), leakage removal, bias — so that the effective threshold rises 3–4×; (b) qLDPC memory modules (Kookaburra 2026 is the test); (c) real-time decoding and in-loop RL calibration (Google's 3.5× drift robustness); (d) moving control into the cold stage — SFQ (SEEQC at millikelvin temperature, IBM–SEEQC under QBI) and cryo-CMOS (Google/Atlantic Quantum, HRL/IBM) — because the I/O wall, not the qubit, caps the count. Risks: $\Lambda\approx2$ implies $>10^{3}$ physical per logical; readout at $10^{-2}$; no logical 2Q gate beyond d=3; no cross-module QEC.

**2. Neutral atoms with zoned architectures, transversal/algorithmic fault tolerance, and erasure conversion.**
The best "space" scaling (Neven's phrase): thousands of atoms with second-scale coherence, all-to-all connectivity by transport, the richest logical-operation demonstrations (96 logical blocks, magic-state distillation, hundreds of teleportations), continuous reloading, and an erasure-convertible dominant error (loss). Google's new track, Microsoft/Atom's commercial machines, AWS–QuEra co-design and two QBI Stage-B slots make this the consensus second bet. The direction that matters: erasure-native isotopes (Yb, Sr), transversal + correlated decoding to amortise the millisecond cycle, high-rate qLDPC (rate >1/2 simulated at $10^{-13}$/round), and sub-ms imaging/transport. Risks: no sustained $\Lambda>2$ with reloading; the $10^{3}$× clock gap; roadmaps have slipped two years at QuEra and Pasqal.

**3. Trapped ions with laser-free electronic gates on 2D chip traps (and QCCD as the near-term product).**
Highest channel quality at scale (Helios) and the most convincing *logical-qubit* results today (48 corrected qubits at $10^{-4}$ logical gate error; a qLDPC memory at break-even at IonQ). The direction with a real scaling story is Oxford Ionics'/IonQ's electronic gates at $8.4\times10^{-5}$ without ground-state cooling on foundry chips — removing lasers, the historic scaling blocker — plus SkyWater as an in-house fab, and photonic interconnects. Quantinuum's Sol (2027) is the first product-scale 2D trap. Risks: speed ($10^{3}$–$10^{5}$× per layer), 75–97% post-selection in high-rate demos, interconnect rates $10^{2}$× short, and IonQ's roadmap (2 M qubits by 2030) has no published 2D-heating or gate-time data.

**4. Silicon/germanium spin qubits as the long-horizon manufacturability bet.**
2026 was the year the CMOS argument acquired evidence: 2Q >99% on 300-mm imec wafers, HRL's self-sequenced d=5 repetition code ($\Lambda=4.7$) under a 4-K cryo-CMOS controller, 18-qubit arrays at identical voltages, spin shuttling at 99.5%, IBM's acquisition of HRL, and four of eleven QBI Stage-B slots. The ceiling (transistor density, $<\$1$/qubit) is the highest of any platform; the floor (no device >12 qubits with all-pairs 2Q data; readout-limited ~100-µs cycles) is the lowest of the top four. Direction: 2×N tileable cells with shuttling buses, cryo-CMOS co-integration, and isotopically purified 300-mm processes.

**5. Photonics: certain as interconnect, high-variance as compute.**
Component metrics are superb (fusion 99.22%, foundry-scale SiN + BTO + SNSPDs, 300-mm), the money is real ($1 B, QBI Stage C V&V), and modularity for every other platform will run on photonic links. But no photonic logical qubit exists, loss is 10–25× above threshold, GKP squeezing is 9 dB short, and PsiQuantum's 2027 "useful" target is already at risk. Treat as a 2030s option with a binary outcome; watch for the first multi-photon resource state / fusion network demonstration, which would move it two places up.

**6. Bosonic codes (cats, GKP, dual-rail) — a direction, not a winner.**
The erasure half of this family (dual-rail transmons and cavities: 82–90% erasure fraction, $10^{-3}$ residual Pauli) is being absorbed by the superconducting mainstream and belongs in direction 1. The cat half has solved bit-flips (hours) and not phase-flips ($10^{-1}$/cycle vs the $10^{-3}$ the resource estimates assume); until a bias-preserving cat–cat CNOT exists, the "100× fewer qubits" claim is a projection. GKP remains post-selected. Nord Quantique's QBI Stage-B slot is the one external validation.

**7. Topological qubits — not a qubit yet.**
Long parity lifetimes in a better material are progress in materials science; without an X-measurement lifetime comparable to Z, a two-qubit operation, or independent replication, there is no basis to rank the platform. Microsoft's own commercial position (selling neutral atoms) is the tell.

**8. Quantum annealing — commercially eroding.**
Classical belief-propagation tensor networks closed most of the 2025 gap; revenue fell 67% in H1 2026; the company bought a gate-model platform. Analog atom/ion/superconducting simulators keep the *physics* value of G1 without the annealing form factor.

### 5.1 Cross-cutting directions (technology-agnostic value)

1. **Error-structure engineering** — erasure conversion, noise bias, leakage removal: the one lever that raises thresholds 3–4× without touching gate physics. Every top-four platform now has an erasure program.
2. **Real-time decoding and in-loop calibration** — FPGA/GPU/on-chip decoders at <1 µs/round (Riverlane, IBM Relay-BP, IQM–Zurich Instruments <4 µs end-to-end), RL calibration during QEC (Google), self-sequencing controllers (HRL). NVIDIA's NVQLink makes this a platform-agnostic layer.
3. **qLDPC and transversal/algorithmic fault tolerance** — the overhead reduction from $\sim10^{3}$ to $\sim10^{2}$ physical per logical qubit. qLDPC (bivariate-bicycle) hardware runs: IonQ (4 logical in 18 ions, break-even) and Zhejiang ([[18,4,4]], not break-even). High-rate transversal block codes: Quantinuum and Harvard/QuEra (tesseract [[16,6,4]]). IBM's gross code is the 2026–27 test.
4. **Cold-stage control integration** — SFQ and cryo-CMOS: the I/O wall is the binding constraint for superconducting and spin platforms at $10^{4}$+ qubits; 2026 delivered peer-reviewed millikelvin SFQ qubit control and the first 4-K cryo-CMOS-sequenced QEC.
5. **Verification and benchmarking at scale (QCVV)** — the 2026 "advantage" claims are all *candidate* claims explicitly open to classical challenge; certified-randomness, cross-platform cross-checks (Qedma on Heron + Helios), and layer-fidelity-class metrics under full load are what separates a result from a press release.
6. **Photonic interconnects** — for every modular architecture; current rates (10–250 Bell pairs/s) are $10^{2}$–$10^{4}$× short of logical clock rates.

### 5.2 Falsifiable watch-list for the next 12–18 months

| Direction | Milestone that would confirm | Milestone that would demote |
|---|---|---|
| Superconducting | sustained $\Lambda\ge3$ at d≥9 with a logical 2Q gate; a gross-code memory on Kookaburra; SFQ/cryo-CMOS control of ≥50 qubits | Kookaburra slips again; readout stuck at $10^{-2}$; Google's next milestone missed |
| Neutral atoms | $\Lambda>2$ in a ≥100-round memory *with* reloading; Magne delivers 50 logical qubits; sub-ms QEC round | Libra slips past 2028; CZ plateau at 99.9% confirmed with no new gate scheme |
| Trapped ions | Sol at 192 q with electronic or ≤99.9% gates in 2D; IonQ 256-q chip at 99.99% commissioned; $\Lambda$-type scaling on any ion code | 256-q system slips beyond 2027; Sol heating/transport data disappoint |
| Bosonic | cat phase-flip ≤$10^{-2}$/cycle at $\bar n\approx10$ with a bias-preserving CNOT; dual-rail 17-qubit system with logical error 2× below physical | Helium ships without logical data through 2027 |
| Photonic | a fusion network / multi-photon resource state beyond Bell pairs; loss within 10× of threshold | PsiQuantum 2027 target formally moved; Stage C V&V negative |
| Spin | >20 qubits with all-pairs 2Q ≥99.5% on 300 mm; µs-class readout | Diraq's 2029 numbers revised down again |
| Topological | X-lifetime ≈ Z-lifetime; any two-qubit entanglement | none of the above by end-2027 |
| External | DARPA QBI Stage C selections (expected Q4 2026) | — |

---

---

## 6. Method, confidence and known conflicts

- **Method.** Web research on 2 Sep 2026 across primary sources (arXiv, Nature/Science/PRX/PRL, company newsrooms and roadmap pages, DARPA), with trade press (Quantum Computing Report, The Quantum Insider, HPCwire, PostQuantum) used to locate primaries. Every number in §2–§3 carries a source key; scores in §3.1 and the matrix in §4 are the author's judgment under the §1.2 anchors.
- **High confidence:** peer-reviewed physical and logical numbers for Google, IBM, USTC/Zhejiang, Quantinuum, IonQ/Oxford Ionics, Harvard/QuEra, Atom/Microsoft, Caltech, AWS, Yale/QCI, PsiQuantum, Xanadu, Diraq/imec, HRL; DARPA QBI rosters; funding events from primary releases.
- **Medium confidence:** Alice & Bob hour-scale bit-flips (company-labelled preliminary, no paper); Nord Quantique tesseract result (press release only); Quantinuum's "near five-nines logical" claim (earnings call, paper not yet public); IBM Heron r3 medians (dashboard snapshot); Origin Wukong-180 figures (company only); Magne commissioning date (end-2026 vs early 2027).
- **Known conflicts:** Helios SPAM $4.8\times10^{-4}$ (arXiv) vs $3.3\times10^{-4}$ (Nature); Ocelot d=3 1.72% (blog) vs 1.75% (paper); Google surface-code $\Lambda$ 2.14 (paper) vs 2.31 (blog); Harvard 448-atom "2.14× below threshold" (Nature abstract) vs an early press summary of the arXiv version; Majorana 2 parity time "20 s mean" (Microsoft) vs "characteristic ~20 s" (paper) vs 22 ± 1 s (analysis); Diraq "thousands by 2029" (July 2026) vs "150 k by 2029" (August 2026); Quantinuum IPO valuation $14–17.6 B across sources.

### 6.1 Open questions checked (status 3 September 2026)

| Question | Finding | Status |
|---|---|---|
| Google successor to Willow / multi-chip result | None published as of 3 Sep 2026: Google's Oct-2025 and Mar-2026 posts still describe Willow (105 q) as the current chip; the July-2026 QEC paper runs on Willow; no inter-fridge or multi-chip result [S33] | closed — negative |
| Λ for the July-2026 record (7.72×10⁻⁴ at d=7) | Not reported: the paper (arXiv:2511.08493 → Nature 655, 879) gives the d=7 LER with AlphaQubit2, the d=5 colour-code LER 8.19×10⁻³, ~20% RL gain and 3.5× drift robustness, but no numeric Λ and no d=3/d=5 surface-code LERs [S33] | closed — value does not exist |
| Kookaburra / Loon hardware in 2026 | Kookaburra not delivered; roadmap page still lists it for 2026; Loon 'demonstrates all key components' with **no performance numbers**; Nighthawk r2 expected at 25× Heron throughput (future tense); no gross-code hardware result [S32] | closed — pending |
| Fujitsu 1,000-qubit launch | Scheduled for fiscal 2026 (Apr 2026–Mar 2027) at Fujitsu Technology Park; no architecture or fidelity disclosed; not launched [S34] | closed — pending |
| IQM / OQC in DARPA QBI | Neither appears on any DARPA Stage A/B roster nor in the 2026 QBIT selections [X14] | closed — negative |
| IonQ laser-gate durations, Tempo fidelities | Forte: MS gates 550–883 µs (median 672 µs), 1Q 110 µs, SPAM 0.5% [I27]; Tempo: '99.9% fidelity', #AQ 64 in a 64-ion chain, no gate times; Oxford Ionics electronic gate 225.8 µs (2025), ≈120 µs (2024) [I4] | closed |
| planqc 2025–26 metrics | No hardware-metric release since the Oct-2024 1,200-atom register; DLR 100-qubit system targeted spring 2027, LRZ 1,000-qubit (2×500) 'circa 2027'; €2.3 M grant Mar 2026, no equity round [N26] | closed — slipped |
| Intel posture | Program alive without a roadmap: 12-qubit Tunnel Falls deployed at Argonne (Jan 2026), 'scale to hundreds of dots'; quantum page unchanged since Aug 2025; no successor chip, no exit statement [Q15] | closed |
| 18th QBI Stage-A company | DARPA's page still reads '17 of the 18 companies have been announced; one is still in negotiation'; the 18th has never been named. Stage A roster: 15 on 3 Apr 2025 + QuEra (29 Apr) + Google (9 Sep 2025); DARPA counts '20 companies evaluated' incl. Microsoft and PsiQuantum (US2QC) [X14] | closed — unnamed by DARPA |
| Gidney RSA-2048 update in 2026 | No revision by Gidney/Ekerå; three other 2026 estimates: Pinnacle (qLDPC) < 100 k physical qubits [X12]; Google ECDLP-256 < 0.5 M qubits in minutes [X11]; neutral-atom Shor with ~10⁴–2.6×10⁴ reconfigurable atoms (P-256 in days, RSA-2048 1–2 orders longer) [X13] | closed — superseded by three papers |
| DARPA QBI Stage C selections | None as of 3 Sep 2026 beyond the two US2QC performers (PsiQuantum, Microsoft). Stage B is 'yearlong' from Nov 2025; DARPA's 2025 Q&A gives Stage B ≈ 12 months and Stage C ≈ 36 months, implying decisions in late 2026 / early 2027; no official date [X14] | closed — pending |
| Quantinuum 'near five-nines logical' paper | Still no arXiv preprint; the Q2-2026 release restates the claim and gives Helios 2Q 99.921% [I25] | open (company claim) |

---

## 7. The technology graph — nodes, coordinates, edges, and what the graph says on its own
### 7.1 Construction rules

**Nodes are technologies, not platforms.** A technology enters the graph if it is *self-contained* (replaceable without touching the rest of the stack) and *principled* (its replacement shifts at least one of the four outputs — error channel, clock, count-with-quality, scaling path — by an order of magnitude). A platform is a *path*: one node per layer through the ten-layer stack (carrier → encoding → gate mechanism → connectivity/transport → control → readout → code → decoder → interconnect → manufacturing). Alternates within a slot are listed; the first is the primary.

**Seven coordinates per node (design space, stable):** (a) carrier-nature affinity on the natural ↔ fabricated spectrum (photon = natural particle in engineered modes; donor/defect = intermediate; carrier-agnostic = neutral); (b) the characteristic time the node imposes (log-scale) with the entangling flag deterministic / probabilistic-heralded; (c) measurement mechanism with time bound, destructiveness and mid-circuit capability; (d) mobility/connectivity mechanism; (e) control modality and placement (room temperature / 4 K / millikelvin / in-vacuum); (f) dominant error structure *as the code sees it*; (g) manufacturing technology. A coordinate is a property that does not move as records improve; anything that moves with records (fidelity, Λ, counts, cycle times, QBI stage, funding) is an **evaluation-space attribute** — dated, sourced, attached to the node, never used for position. Actors and goals are **annotations** on paths.

**Five edge types:** *requires/provides* (inter-layer dependency; either-or dependencies are flagged and only count where realised in a path), *alternatives* (two technologies that can fill the same slot of a layer; the relation is symmetric and does not mean exclusion — a platform may combine both across modules or hierarchy levels, e.g. surface-code processing with gross-code memory), *conflicts* (the two work together only with a mitigating element or a change in a third layer; every conflict edge carries the mechanism, the measured price, the mitigation, a status — open / mitigated / bypassed — and a dated source, see 7.10), *transfers* (the same node in several platform paths), *defines* (node → one of the four outputs, each carrying a source, a date and a number).

**Clock is not a coordinate.** Per path it is derived as max(gate time, readout time, transport time) from three different nodes; the measured QEC cycle is shown next to it as a check.

**Off-diagonal test.** Along the natural–fabricated axis, coordinates correlate: natural carriers default to optical room-temperature control, transport connectivity, loss-type errors, slow fluorescence readout, optical/MEMS assembly; fabricated carriers default to microwave/electrical room-temperature control, static nearest-neighbour wiring, Pauli/leakage errors, fast dispersive/charge readout, lithography. A node is *off-diagonal* when, in the path that uses it, it breaks that correlation: natural carrier + microwave control; fabricated + far connectivity; fabricated + erasure; fabricated + cold-stage control or decoding; solid-state carrier + photonic interconnect; natural + sub-µs gate; natural + ≤ 30 µs readout; natural + semiconductor/photonic-chip fabrication. **Hubs** are nodes whose dependency reach (own paths plus paths of nodes that require them) spans ≥ 3 carrier families, or ≥ 2 families for a technology that reached hardware in 2023 or later. **Empty slots** are nodes with no demonstrated technology, or path slots with nothing in them.

**Validity criterion.** The graph must *reproduce* the promising directions of §5 as the set S = off-diagonal ∪ hubs ∪ empty slots — it does not receive them as input. The test is only as independent as the off-diagonal patterns, which encode the natural/fabricated correlation; its real information is in the residuals: prose claims the graph does not support, and graph findings the prose missed (§7.8).
### 7.2 Node table (96 technologies × 7 coordinates)
| # | Layer | Technology | (a) carrier affinity | (b) time · entangling | (c) readout | (d) mobility | (e) control · placement | (f) error structure | (g) manufacturing | status · since |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 Carrier | **Bosonic cavity mode** `cavity` | fabricated | 316 ns; deterministic | dispersive microwave; 1 µs; destructive=no; mid-circuit=yes | shared bus (motional / cavity) | microwave @ room temperature | loss (erasure), biased | 3D machined cavities | demonstrated · 2013 |
| 2 | 1 Carrier | **Fluxonium** `fluxonium` | fabricated | 50.1 ns; deterministic | dispersive microwave; 316 ns; destructive=no; mid-circuit=yes | static NN wiring | low-frequency electrical @ room temperature | stochastic Pauli, coherent / calibration | superconducting lithography | demonstrated · 2009 |
| 3 | 1 Carrier | **rf-SQUID flux qubit (annealer)** `fluxq` | fabricated | 3.16 ns; n/a | dispersive microwave; 1 µs; destructive=no; mid-circuit=no | long-range static couplers | low-frequency electrical @ millikelvin stage | stochastic Pauli, coherent / calibration | superconducting lithography | demonstrated · 2011 |
| 4 | 1 Carrier | **Majorana parity (InAs–Pb tetron)** `majorana` | fabricated | 1 µs; deterministic | rf quantum capacitance (parity); 100 µs; destructive=no; mid-circuit=yes | static NN wiring | low-frequency electrical @ room temperature | unknown / contested | III-V MBE heterostructures | emerging · 2025 |
| 5 | 1 Carrier | **Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge)** `qd_spin` | fabricated | 50.1 ns; deterministic | spin-to-charge + rf reflectometry; 6.31 µs; destructive=no; mid-circuit=yes | static NN wiring | low-frequency electrical @ room temperature | coherent / calibration, stochastic Pauli, leakage | CMOS foundry 300 mm | demonstrated · 2012 |
| 6 | 1 Carrier | **Transmon** `transmon` | fabricated | 10 ns; deterministic | dispersive microwave; 316 ns; destructive=no; mid-circuit=yes | static NN wiring | microwave @ room temperature | leakage, stochastic Pauli, correlated bursts, coherent / calibration | superconducting lithography | demonstrated · 2007 |
| 7 | 1 Carrier | **Colour-centre / defect spin (NV, SiV, SnV, T)** `defect` | intermediate / carrier-agnostic | 1 µs; deterministic | fluorescence (PMT/SNSPD); 100 µs; destructive=no; mid-circuit=yes | flying qubits (photons) | optical @ room temperature | stochastic Pauli, loss (erasure) | diamond growth / implantation | demonstrated · 2004 |
| 8 | 1 Carrier | **Donor spin (P in ²⁸Si)** `donor` | intermediate / carrier-agnostic | 1 µs; deterministic | spin-to-charge + rf reflectometry; 10 µs; destructive=no; mid-circuit=yes | static NN wiring | low-frequency electrical @ room temperature | stochastic Pauli | STM hydrogen lithography | demonstrated · 2012 |
| 9 | 1 Carrier | **Single photon (discrete variable)** `photon` | photon (natural particle, engineered modes) | 100 ns; probabilistic / heralded | single-photon detection; 10 ns; destructive=yes; mid-circuit=no | flying qubits (photons) | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | demonstrated · 2001 |
| 10 | 1 Carrier | **Squeezed light mode (CV)** `squeezed` | photon (natural particle, engineered modes) | 1 µs; probabilistic / heralded | single-photon detection; 10 ns; destructive=yes; mid-circuit=no | flying qubits (photons) | electro-optic @ room temperature | Gaussian (small-shift), loss (erasure) | photonic IC foundry | demonstrated · 2012 |
| 11 | 1 Carrier | **Alkaline-earth atom (Yb/Sr) — erasure-native** `ae_atom` | natural | 251 ns; deterministic | fluorescence imaging (camera); 501 µs; destructive=no; mid-circuit=yes | physical transport | optical @ room temperature | erasure-convertible, loss (erasure) | optical / mechanical assembly | demonstrated · 2019 |
| 12 | 1 Carrier | **Alkali atom (Rb/Cs) in tweezer** `alkali` | natural | 251 ns; deterministic | fluorescence imaging (camera); 501 µs; destructive=no; mid-circuit=yes | physical transport | optical @ room temperature | loss (erasure), leakage, coherent / calibration | optical / mechanical assembly | demonstrated · 2016 |
| 13 | 1 Carrier | **Trapped atomic ion** `ion` | natural | 63.1 µs; deterministic | fluorescence (PMT/SNSPD); 10 µs; destructive=no; mid-circuit=yes | physical transport | optical @ room temperature | coherent / calibration, leakage, stochastic Pauli | MEMS / surface-electrode traps | demonstrated · 1995 |
| 14 | 2 Encoding | **Bare two-level subspace** `enc_bare` | fabricated | — | — | — | — | leakage | — | demonstrated · 2007 |
| 15 | 2 Encoding | **Cat-code encoding (biased noise)** `enc_cat` | fabricated | — | — | — | — | biased | — | demonstrated · 2020 |
| 16 | 2 Encoding | **Exchange-only / singlet-triplet spin encoding** `enc_eo` | fabricated | — | — | — | — | leakage, coherent / calibration | — | demonstrated · 2013 |
| 17 | 2 Encoding | **Fermion-parity encoding (tetron)** `enc_parity` | fabricated | — | — | — | — | unknown / contested | — | theory / design only · 2025 |
| 18 | 2 Encoding | **GKP grid encoding** `enc_gkp` | hybrid (fabricated host) | — | — | — | — | Gaussian (small-shift) | — | emerging · 2020 |
| 19 | 2 Encoding | **Single-spin (Loss–DiVincenzo) / nuclear-spin encoding** `enc_spin_ld` | hybrid (fabricated host) | — | — | — | — | coherent / calibration, stochastic Pauli | — | demonstrated · 1998 |
| 20 | 2 Encoding | **Dual-rail (erasure) encoding** `enc_dualrail` | photon (natural particle, engineered modes) | — | — | — | — | erasure-convertible | — | demonstrated · 2023 |
| 21 | 2 Encoding | **Time-bin / path photonic encoding** `enc_timebin` | photon (natural particle, engineered modes) | — | — | — | — | loss (erasure) | — | demonstrated · 1999 |
| 22 | 2 Encoding | **Hyperfine / clock-state qubit** `enc_hf` | natural | — | — | — | — | stochastic Pauli, leakage | — | demonstrated · 1995 |
| 23 | 2 Encoding | **Metastable ('omg') erasure encoding** `enc_omg` | natural | — | — | — | — | erasure-convertible | — | emerging · 2023 |
| 24 | 3 Gate mechanism | **Analog annealing evolution** `g_anneal` | fabricated | 3.98 ns; n/a | — | long-range static couplers | low-frequency electrical @ millikelvin stage | coherent / calibration, stochastic Pauli | superconducting lithography | demonstrated · 2011 |
| 25 | 3 Gate mechanism | **Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter)** `g_bos` | fabricated | 501 ns; deterministic | — | shared bus (motional / cavity) | microwave @ room temperature | erasure-convertible, biased, stochastic Pauli | 3D machined cavities | demonstrated · 2018 |
| 26 | 3 Gate mechanism | **Bias-preserving cat–cat CNOT** `g_catcnot` | fabricated | —; deterministic | — | shared bus (motional / cavity) | microwave @ room temperature | biased | superconducting lithography | empty slot — no technology yet · — |
| 27 | 3 Gate mechanism | **Cross-resonance (fixed-frequency, all-microwave)** `g_cr` | fabricated | 316 ns; deterministic | — | static NN wiring | microwave @ room temperature | coherent / calibration, stochastic Pauli | superconducting lithography | demonstrated · 2011 |
| 28 | 3 Gate mechanism | **Electronic near-field microwave gate (ions, laser-free)** `g_elec` | fabricated | 200 µs; deterministic | — | shared bus (motional / cavity) | microwave @ room temperature | stochastic Pauli, coherent / calibration | MEMS / surface-electrode traps | demonstrated · 2024 |
| 29 | 3 Gate mechanism | **Exchange gate (spins; incl. shuttled-spin CZ)** `g_exch` | fabricated | 100 ns; deterministic | — | static NN wiring | low-frequency electrical @ room temperature | coherent / calibration, stochastic Pauli, leakage | CMOS foundry 300 mm | demonstrated · 2018 |
| 30 | 3 Gate mechanism | **Measurement-based Majorana gate** `g_mbq` | fabricated | —; deterministic | — | static NN wiring | low-frequency electrical @ room temperature | unknown / contested | III-V MBE heterostructures | empty slot — no technology yet · — |
| 31 | 3 Gate mechanism | **Tunable-coupler CZ / iSWAP** `g_tc` | fabricated | 39.8 ns; deterministic | — | static NN wiring | microwave @ room temperature | coherent / calibration, leakage, stochastic Pauli | superconducting lithography | demonstrated · 2014 |
| 32 | 3 Gate mechanism | **Microwave / optical spin gates (defect centres, 1Q spins)** `g_mwspin` | intermediate / carrier-agnostic | 1 µs; deterministic | — | static NN wiring | microwave @ room temperature | stochastic Pauli, coherent / calibration | diamond growth / implantation | demonstrated · 2004 |
| 33 | 3 Gate mechanism | **CV Gaussian gates + GKP-assisted non-Gaussian ops** `g_cv` | photon (natural particle, engineered modes) | 1 µs; deterministic | — | flying qubits (photons) | electro-optic @ room temperature | Gaussian (small-shift), loss (erasure) | photonic IC foundry | demonstrated · 2020 |
| 34 | 3 Gate mechanism | **Linear-optical fusion (heralded)** `g_fusion` | photon (natural particle, engineered modes) | 100 ns; probabilistic / heralded | — | flying qubits (photons) | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | demonstrated · 2005 |
| 35 | 3 Gate mechanism | **Multi-photon resource-state factory (6-ring etc.)** `src_resource` | photon (natural particle, engineered modes) | —; probabilistic / heralded | — | flying qubits (photons) | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | empty slot — no technology yet · — |
| 36 | 3 Gate mechanism | **Mølmer–Sørensen / light-shift laser gate** `g_ms` | natural | 63.1 µs; deterministic | — | shared bus (motional / cavity) | optical @ room temperature | coherent / calibration, leakage, stochastic Pauli | optical / mechanical assembly | demonstrated · 2003 |
| 37 | 3 Gate mechanism | **Rydberg-blockade CZ** `g_ryd` | natural | 251 ns; deterministic | — | physical transport | optical @ room temperature | loss (erasure), leakage, coherent / calibration | optical / mechanical assembly | demonstrated · 2010 |
| 38 | 4 Connectivity / transport | **Crossbar shared-line control (spins)** `cx_crossbar` | fabricated | — | — | shared-line crossbar | low-frequency electrical @ room temperature | coherent / calibration | CMOS foundry 300 mm | emerging · 2023 |
| 39 | 4 Connectivity / transport | **Long-range on-chip couplers (c-couplers, mm-scale)** `cx_lr` | fabricated | — | — | long-range static couplers | — | coherent / calibration | superconducting lithography | emerging · 2023 |
| 40 | 4 Connectivity / transport | **Static nearest-neighbour lattice** `cx_nn` | fabricated | — | — | static NN wiring | — | coherent / calibration | superconducting lithography | demonstrated · 2014 |
| 41 | 4 Connectivity / transport | **Spin shuttling (conveyor mode)** `cx_shuttle` | fabricated | 200 ns; n/a | — | physical transport | — | coherent / calibration | CMOS foundry 300 mm | emerging · 2025 |
| 42 | 4 Connectivity / transport | **Photonic switching / routing (EO, feed-forward)** `cx_switch` | photon (natural particle, engineered modes) | 1 µs; n/a | — | flying qubits (photons) | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | demonstrated · 2015 |
| 43 | 4 Connectivity / transport | **Atom transport by AOD tweezers (zoned architecture)** `cx_aod` | natural | 1 ms; n/a | — | physical transport | — | loss (erasure) | optical / mechanical assembly | demonstrated · 2022 |
| 44 | 4 Connectivity / transport | **Ion-chain motional bus (all-to-all in chain)** `cx_bus` | natural | — | — | shared bus (motional / cavity) | — | coherent / calibration | MEMS / surface-electrode traps | demonstrated · 2003 |
| 45 | 4 Connectivity / transport | **Ion shuttling (QCCD, junctions, grid traps)** `cx_qccd` | natural | 2 ms; n/a | — | physical transport | — | coherent / calibration | MEMS / surface-electrode traps | demonstrated · 2002 |
| 46 | 5 Control | **Baseband electrical control (spins, Majorana)** `ct_base` | fabricated | — | — | — | low-frequency electrical @ room temperature | coherent / calibration | CMOS foundry 300 mm | demonstrated · 2012 |
| 47 | 5 Control | **Cryo-CMOS controller (4 K / mK)** `ct_cryocmos` | fabricated | — | — | — | microwave @ 4 K stage | coherent / calibration | CMOS foundry 300 mm | demonstrated · 2024 |
| 48 | 5 Control | **On-chip flux-DAC multiplexing** `ct_fluxdac` | fabricated | — | — | — | low-frequency electrical @ millikelvin stage | coherent / calibration | superconducting lithography | demonstrated · 2026 |
| 49 | 5 Control | **Chip-integrated microwave control (ions)** `ct_ionmw` | fabricated | — | — | — | microwave @ room temperature | stochastic Pauli | MEMS / surface-electrode traps | demonstrated · 2024 |
| 50 | 5 Control | **Room-temperature electronics + per-qubit coax/flex** `ct_rt` | fabricated | — | — | — | microwave @ room temperature | coherent / calibration | superconducting lithography | demonstrated · 2007 |
| 51 | 5 Control | **SFQ digital control (millikelvin)** `ct_sfq` | fabricated | — | — | — | microwave @ millikelvin stage | stochastic Pauli | superconducting lithography | emerging · 2026 |
| 52 | 5 Control | **Electro-optic drive + feed-forward electronics (RT)** `ct_eo` | photon (natural particle, engineered modes) | — | — | — | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | demonstrated · 2020 |
| 53 | 5 Control | **PIC-generated tweezers / integrated optics for atoms** `ct_pic_trap` | photon (natural particle, engineered modes) | — | — | — | optical @ room temperature | coherent / calibration | photonic IC foundry | emerging · 2026 |
| 54 | 5 Control | **Laser control with integrated photonics (ions)** `ct_ionlaser` | natural | — | — | — | optical @ in-vacuum integrated | coherent / calibration | photonic IC foundry | demonstrated · 2020 |
| 55 | 5 Control | **Laser + AOD/SLM optical control (atoms)** `ct_laser` | natural | — | — | — | optical @ room temperature | coherent / calibration | optical / mechanical assembly | demonstrated · 2016 |
| 56 | 6 Readout | **Dispersive microwave readout (+TWPA, Purcell)** `ro_disp` | fabricated | — | dispersive microwave; 282 ns; destructive=no; mid-circuit=yes | — | microwave @ room temperature | leakage | superconducting lithography | demonstrated · 2005 |
| 57 | 6 Readout | **rf quantum-capacitance parity readout** `ro_qcap` | fabricated | — | rf quantum capacitance (parity); 100 µs; destructive=no; mid-circuit=yes | — | low-frequency electrical @ room temperature | unknown / contested | III-V MBE heterostructures | emerging · 2025 |
| 58 | 6 Readout | **Spin-to-charge conversion + rf reflectometry** `ro_s2c` | fabricated | — | spin-to-charge + rf reflectometry; 6.31 µs; destructive=no; mid-circuit=yes | — | low-frequency electrical @ room temperature | coherent / calibration | CMOS foundry 300 mm | demonstrated · 2004 |
| 59 | 6 Readout | **Mid-circuit erasure check** `ro_erasure` | intermediate / carrier-agnostic | — | ancilla erasure check; 398 ns; destructive=no; mid-circuit=yes | — | microwave @ room temperature | erasure-convertible | — | demonstrated · 2023 |
| 60 | 6 Readout | **Single-photon detection (SNSPD / TES)** `ro_spd` | photon (natural particle, engineered modes) | — | single-photon detection; 10 ns; destructive=yes; mid-circuit=no | — | electro-optic @ 4 K stage | loss (erasure) | photonic IC foundry | demonstrated · 2001 |
| 61 | 6 Readout | **Fluorescence state detection (ions)** `ro_fluor` | natural | — | fluorescence (PMT/SNSPD); 100 µs; destructive=no; mid-circuit=yes | — | optical @ room temperature | stochastic Pauli | optical / mechanical assembly | demonstrated · 1995 |
| 62 | 6 Readout | **Fluorescence imaging of atom arrays** `ro_img` | natural | — | fluorescence imaging (camera); 501 µs; destructive=no; mid-circuit=yes | — | optical @ room temperature | loss (erasure) | optical / mechanical assembly | demonstrated · 2016 |
| 63 | 6 Readout | **Fast (≤ 20 µs) atom-array readout** `ro_imgfast` | natural | — | fluorescence imaging (camera); 17.8 µs; destructive=no; mid-circuit=yes | — | optical @ room temperature | loss (erasure) | optical / mechanical assembly | emerging · 2026 |
| 64 | 7 Code | **Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC)** `code_bosonic` | hybrid (fabricated host) | — | — | static NN wiring | — | biased, Gaussian (small-shift) | — | emerging · 2024 |
| 65 | 7 Code | **Colour code (transversal Cliffords)** `code_color` | intermediate / carrier-agnostic | — | — | static NN wiring | — | stochastic Pauli | — | demonstrated · 2024 |
| 66 | 7 Code | **Erasure-adapted codes** `code_erasure` | intermediate / carrier-agnostic | — | — | static NN wiring | — | erasure-convertible | — | emerging · 2025 |
| 67 | 7 Code | **Magic-state factory (cultivation / distillation / code switching)** `code_magic` | intermediate / carrier-agnostic | — | — | static NN wiring | — | stochastic Pauli | — | demonstrated · 2025 |
| 68 | 7 Code | **Non-local qLDPC codes (bivariate-bicycle, 'gross')** `code_qldpc` | intermediate / carrier-agnostic | — | — | long-range static couplers | — | stochastic Pauli | — | emerging · 2025 |
| 69 | 7 Code | **Rotated surface code (+ yoked variants)** `code_surface` | intermediate / carrier-agnostic | — | — | static NN wiring | — | stochastic Pauli | — | demonstrated · 2023 |
| 70 | 7 Code | **Fusion-based fault tolerance** `code_fusion` | photon (natural particle, engineered modes) | — | — | flying qubits (photons) | — | loss (erasure) | — | theory / design only · — |
| 71 | 7 Code | **Algorithmic FT / transversal architectures** `code_aft` | natural | — | — | physical transport | — | stochastic Pauli | — | emerging · 2025 |
| 72 | 7 Code | **High-rate concatenated codes with transversal gates** `code_highrate` | natural | — | — | physical transport | — | stochastic Pauli | — | demonstrated · 2024 |
| 73 | 8 Decoder | **Cryogenic / on-chip decoder (SFQ, cryo-CMOS)** `dec_cryo` | fabricated | — | — | — | microwave @ millikelvin stage | stochastic Pauli | superconducting lithography | empty slot — no technology yet · — |
| 74 | 8 Decoder | **In-loop RL calibration / decoder steering** `dec_rl` | fabricated | — | — | — | — | coherent / calibration | — | demonstrated · 2026 |
| 75 | 8 Decoder | **FPGA real-time decoders (LCD, Deltaflow)** `dec_fpga` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | — | demonstrated · 2025 |
| 76 | 8 Decoder | **GPU decoding via NVQLink** `dec_gpu` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | — | demonstrated · 2025 |
| 77 | 8 Decoder | **MWPM / Sparse Blossom (+correlated matching)** `dec_mwpm` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | — | demonstrated · 2015 |
| 78 | 8 Decoder | **Neural decoders (AlphaQubit2, CNN, transformers)** `dec_nn` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | — | demonstrated · 2024 |
| 79 | 8 Decoder | **Relay-BP for qLDPC (FPGA)** `dec_relaybp` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | — | demonstrated · 2025 |
| 80 | 8 Decoder | **Correlated / loss-aware decoding (transversal, atom loss)** `dec_corr` | natural | — | — | — | — | loss (erasure), erasure-convertible | — | demonstrated · 2025 |
| 81 | 9 Interconnect | **Cryogenic microwave link between refrigerators** `ic_cryolink` | fabricated | — | — | long-range static couplers | microwave @ millikelvin stage | loss (erasure), coherent / calibration | superconducting lithography | emerging · 2020 |
| 82 | 9 Interconnect | **Multi-chip modules / l-couplers (same cryostat)** `ic_mcm` | fabricated | — | — | long-range static couplers | microwave @ millikelvin stage | coherent / calibration | superconducting lithography | emerging · 2025 |
| 83 | 9 Interconnect | **Microwave–optical transducer (useful efficiency)** `ic_transducer` | fabricated | — | — | flying qubits (photons) | electro-optic @ millikelvin stage | loss (erasure) | photonic IC foundry | empty slot — no technology yet · — |
| 84 | 9 Interconnect | **Spin–photon solid-state link (SiV, NV, T-centre)** `ic_spinphoton` | intermediate / carrier-agnostic | — | — | flying qubits (photons) | optical @ room temperature | loss (erasure) | diamond growth / implantation | demonstrated · 2013 |
| 85 | 9 Interconnect | **Fibre links between photonic modules** `ic_fibre` | photon (natural particle, engineered modes) | — | — | flying qubits (photons) | electro-optic @ room temperature | loss (erasure) | photonic IC foundry | demonstrated · 2025 |
| 86 | 9 Interconnect | **Atom–photon cavity interface** `ic_atomcavity` | natural | — | — | flying qubits (photons) | optical @ room temperature | loss (erasure) | optical / mechanical assembly | emerging · 2024 |
| 87 | 9 Interconnect | **Ion–photon photonic link** `ic_ionphoton` | natural | — | — | flying qubits (photons) | optical @ room temperature | loss (erasure) | optical / mechanical assembly | demonstrated · 2007 |
| 88 | 10 Manufacturing | **3D machined superconducting cavities** `fab_3d` | fabricated | — | — | — | — | loss (erasure) | 3D machined cavities | demonstrated · 2013 |
| 89 | 10 Manufacturing | **300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)** `fab_cmos` | fabricated | — | — | — | — | coherent / calibration | CMOS foundry 300 mm | demonstrated · 2022 |
| 90 | 10 Manufacturing | **Superconducting-qubit lithography (Nb/Al JJ, 300 mm)** `fab_sc` | fabricated | — | — | — | — | coherent / calibration | superconducting lithography | demonstrated · 2007 |
| 91 | 10 Manufacturing | **III-V MBE heterostructures (InAs–Pb wires, QD sources)** `fab_mbe` | hybrid (fabricated host) | — | — | — | — | unknown / contested | III-V MBE heterostructures | demonstrated · 2018 |
| 92 | 10 Manufacturing | **Diamond growth / implantation (NV, SiV, SnV)** `fab_diamond` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | diamond growth / implantation | demonstrated · 2010 |
| 93 | 10 Manufacturing | **STM hydrogen lithography (donors)** `fab_stm` | intermediate / carrier-agnostic | — | — | — | — | stochastic Pauli | STM hydrogen lithography | demonstrated · 2012 |
| 94 | 10 Manufacturing | **Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm)** `fab_pic` | photon (natural particle, engineered modes) | — | — | — | — | loss (erasure) | photonic IC foundry | demonstrated · 2015 |
| 95 | 10 Manufacturing | **Optical / mechanical assembly (lasers, vacuum, objectives)** `fab_optics` | natural | — | — | — | — | coherent / calibration | optical / mechanical assembly | demonstrated · 2016 |
| 96 | 10 Manufacturing | **Surface-electrode ion-trap microfabrication** `fab_trap` | natural | — | — | — | — | coherent / calibration | MEMS / surface-electrode traps | demonstrated · 2006 |

### 7.3 Platform paths through the stack (primary node per layer; alternates in brackets)
| Path | 1 Carrier | 2 Encoding | 3 Gate mechanism | 4 Connectivity / transport | 5 Control | 6 Readout | 7 Code | 8 Decoder | 9 Interconnect | 10 Manufacturing |
|---|---|---|---|---|---|---|---|---|---|---|
| **Superconducting transmon** — Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu | Transmon (Fluxonium) | Bare two-level subspace | Tunable-coupler CZ / iSWAP (Cross-resonance (fixed-frequency, all-microwave)) | Static nearest-neighbour lattice (Long-range on-chip couplers (c-couplers, mm-scale)) | Room-temperature electronics + per-qubit coax/flex (Cryo-CMOS controller (4 K / mK); SFQ digital control (millikelvin)) | Dispersive microwave readout (+TWPA, Purcell) | Rotated surface code (+ yoked variants) (Colour code (transversal Cliffords); Non-local qLDPC codes (bivariate-bicycle, 'gross'); Magic-state factory (cultivation / distillation / code switching)) | Neural decoders (AlphaQubit2, CNN, transformers) (MWPM / Sparse Blossom (+correlated matching); FPGA real-time decoders (LCD, Deltaflow); Relay-BP for qLDPC (FPGA); In-loop RL calibration / decoder steering; GPU decoding via NVQLink) | Multi-chip modules / l-couplers (same cryostat) (Cryogenic microwave link between refrigerators; Microwave–optical transducer (useful efficiency)) | Superconducting-qubit lithography (Nb/Al JJ, 300 mm) (300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)) |
| **Superconducting bosonic (cat / GKP)** — Alice & Bob, AWS, Nord Quantique | Bosonic cavity mode | Cat-code encoding (biased noise) (GKP grid encoding) | Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) (Bias-preserving cat–cat CNOT) | Static nearest-neighbour lattice | Room-temperature electronics + per-qubit coax/flex | Dispersive microwave readout (+TWPA, Purcell) | Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | MWPM / Sparse Blossom (+correlated matching) | Multi-chip modules / l-couplers (same cryostat) | Superconducting-qubit lithography (Nb/Al JJ, 300 mm) (3D machined superconducting cavities) |
| **Superconducting dual-rail erasure** — D-Wave/QCI, AWS, SUSTech | Bosonic cavity mode (Transmon) | Dual-rail (erasure) encoding | Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) | Static nearest-neighbour lattice | Room-temperature electronics + per-qubit coax/flex | Mid-circuit erasure check (Dispersive microwave readout (+TWPA, Purcell)) | Erasure-adapted codes | MWPM / Sparse Blossom (+correlated matching) | Multi-chip modules / l-couplers (same cryostat) | 3D machined superconducting cavities (Superconducting-qubit lithography (Nb/Al JJ, 300 mm)) |
| **Trapped ions — QCCD, laser gates** — Quantinuum, AQT | Trapped atomic ion | Hyperfine / clock-state qubit | Mølmer–Sørensen / light-shift laser gate | Ion shuttling (QCCD, junctions, grid traps) | Laser control with integrated photonics (ions) | Fluorescence state detection (ions) | High-rate concatenated codes with transversal gates (Colour code (transversal Cliffords); Magic-state factory (cultivation / distillation / code switching)) | GPU decoding via NVQLink (MWPM / Sparse Blossom (+correlated matching)) | Ion–photon photonic link | Surface-electrode ion-trap microfabrication (Optical / mechanical assembly (lasers, vacuum, objectives)) |
| **Trapped ions — electronic gates, chip control** — IonQ / Oxford Ionics, eleQtron, Quantum Art | Trapped atomic ion | Hyperfine / clock-state qubit (Metastable ('omg') erasure encoding) | Electronic near-field microwave gate (ions, laser-free) (Mølmer–Sørensen / light-shift laser gate) | Ion-chain motional bus (all-to-all in chain) (Ion shuttling (QCCD, junctions, grid traps)) | Chip-integrated microwave control (ions) | Fluorescence state detection (ions) | Non-local qLDPC codes (bivariate-bicycle, 'gross') (High-rate concatenated codes with transversal gates) | Relay-BP for qLDPC (FPGA) (MWPM / Sparse Blossom (+correlated matching)) | Ion–photon photonic link | Surface-electrode ion-trap microfabrication (300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)) |
| **Neutral atoms — alkali (Rb/Cs)** — Harvard/MIT, QuEra, Pasqal, Infleqtion, Google (2026) | Alkali atom (Rb/Cs) in tweezer | Hyperfine / clock-state qubit | Rydberg-blockade CZ | Atom transport by AOD tweezers (zoned architecture) | Laser + AOD/SLM optical control (atoms) (PIC-generated tweezers / integrated optics for atoms) | Fluorescence imaging of atom arrays (Fast (≤ 20 µs) atom-array readout) | High-rate concatenated codes with transversal gates (Rotated surface code (+ yoked variants); Colour code (transversal Cliffords); Algorithmic FT / transversal architectures; Magic-state factory (cultivation / distillation / code switching)) | Correlated / loss-aware decoding (transversal, atom loss) (Neural decoders (AlphaQubit2, CNN, transformers); GPU decoding via NVQLink) | Atom–photon cavity interface | Optical / mechanical assembly (lasers, vacuum, objectives) |
| **Neutral atoms — alkaline-earth (Yb/Sr), erasure-native** — Atom Computing/Microsoft, Princeton, Caltech | Alkaline-earth atom (Yb/Sr) — erasure-native | Metastable ('omg') erasure encoding (Hyperfine / clock-state qubit) | Rydberg-blockade CZ | Atom transport by AOD tweezers (zoned architecture) | Laser + AOD/SLM optical control (atoms) | Fluorescence imaging of atom arrays (Mid-circuit erasure check; Fast (≤ 20 µs) atom-array readout) | Erasure-adapted codes (Rotated surface code (+ yoked variants)) | Correlated / loss-aware decoding (transversal, atom loss) | Atom–photon cavity interface | Optical / mechanical assembly (lasers, vacuum, objectives) |
| **Photonic — fusion-based (DV)** — PsiQuantum, Quandela, QuiX | Single photon (discrete variable) | Time-bin / path photonic encoding (Dual-rail (erasure) encoding) | Linear-optical fusion (heralded) (Multi-photon resource-state factory (6-ring etc.)) | Photonic switching / routing (EO, feed-forward) | Electro-optic drive + feed-forward electronics (RT) | Single-photon detection (SNSPD / TES) | Fusion-based fault tolerance | MWPM / Sparse Blossom (+correlated matching) | Fibre links between photonic modules | Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) |
| **Photonic — continuous-variable / GKP** — Xanadu | Squeezed light mode (CV) | GKP grid encoding | CV Gaussian gates + GKP-assisted non-Gaussian ops (Linear-optical fusion (heralded)) | Photonic switching / routing (EO, feed-forward) | Electro-optic drive + feed-forward electronics (RT) | Single-photon detection (SNSPD / TES) | Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | Relay-BP for qLDPC (FPGA) (MWPM / Sparse Blossom (+correlated matching)) | Fibre links between photonic modules | Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) |
| **Silicon / germanium quantum-dot spins** — Intel, Diraq, Quantum Motion, HRL→IBM, QuTech/Groove, Quobly, Equal1 | Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | Exchange-only / singlet-triplet spin encoding (Single-spin (Loss–DiVincenzo) / nuclear-spin encoding) | Exchange gate (spins; incl. shuttled-spin CZ) | Static nearest-neighbour lattice (Spin shuttling (conveyor mode); Crossbar shared-line control (spins)) | Baseband electrical control (spins, Majorana) (Cryo-CMOS controller (4 K / mK)) | Spin-to-charge conversion + rf reflectometry | Rotated surface code (+ yoked variants) | MWPM / Sparse Blossom (+correlated matching) | **∅** | 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) |
| **Donor spins in silicon** — SQC | Donor spin (P in ²⁸Si) | Single-spin (Loss–DiVincenzo) / nuclear-spin encoding | Exchange gate (spins; incl. shuttled-spin CZ) | Static nearest-neighbour lattice | Baseband electrical control (spins, Majorana) | Spin-to-charge conversion + rf reflectometry | Rotated surface code (+ yoked variants) | MWPM / Sparse Blossom (+correlated matching) | **∅** | STM hydrogen lithography (donors) |
| **Defect-spin network nodes (NV/SiV/T)** — QuTech/Fujitsu, Harvard, Photonic Inc, Quantum Brilliance | Colour-centre / defect spin (NV, SiV, SnV, T) | Single-spin (Loss–DiVincenzo) / nuclear-spin encoding | Microwave / optical spin gates (defect centres, 1Q spins) | Static nearest-neighbour lattice | Baseband electrical control (spins, Majorana) | Fluorescence state detection (ions) | **∅** | **∅** | Spin–photon solid-state link (SiV, NV, T-centre) | Diamond growth / implantation (NV, SiV, SnV) |
| **Topological (Majorana)** — Microsoft | Majorana parity (InAs–Pb tetron) | Fermion-parity encoding (tetron) | Measurement-based Majorana gate ✗ | Static nearest-neighbour lattice | Baseband electrical control (spins, Majorana) | rf quantum-capacitance parity readout | **∅** | **∅** | **∅** | III-V MBE heterostructures (InAs–Pb wires, QD sources) |
| **Quantum annealing** — D-Wave | rf-SQUID flux qubit (annealer) | **∅** | Analog annealing evolution | Long-range on-chip couplers (c-couplers, mm-scale) | On-chip flux-DAC multiplexing | Dispersive microwave readout (+TWPA, Purcell) | **∅** | **∅** | **∅** | Superconducting-qubit lithography (Nb/Al JJ, 300 mm) |

### 7.4 Derived clock per path — max(gate, readout, transport) vs measured cycle
| Path | gate | readout | transport | derived lower bound | limiter | measured cycle |
|---|---|---|---|---|---|---|
| Superconducting transmon | 39.8 ns | 282 ns | — | **282 ns** | readout | 1.1 µs (Willow QEC cycle) |
| Superconducting bosonic (cat / GKP) | 501 ns | 282 ns | — | **501 ns** | gate | 2.8 µs (Ocelot cycle) |
| Superconducting dual-rail erasure | 501 ns | 398 ns | — | **501 ns** | gate | ~2 µs (CZ 500 ns + 384 ns check) |
| Trapped ions — QCCD, laser gates | 63.1 µs | 100 µs | 2 ms | **2 ms** | transport | ~1–5 ms syndrome cycle; 55 ms per full layer (Helios) |
| Trapped ions — electronic gates, chip control | 200 µs | 100 µs | — | **200 µs** | gate | ~1–5 ms (IonQ decoder assumption) |
| Neutral atoms — alkali (Rb/Cs) | 251 ns | 501 µs | 1 ms | **1 ms** | transport | ~1–4.5 ms per QEC round |
| Neutral atoms — alkaline-earth (Yb/Sr), erasure-native | 251 ns | 501 µs | 1 ms | **1 ms** | transport | ~1–4 ms |
| Photonic — fusion-based (DV) | 100 ns | 10 ns | — | **100 ns** | gate | MHz–GHz by design; no logical cycle |
| Photonic — continuous-variable / GKP | 1 µs | 10 ns | — | **1 µs** | gate | 1 MHz clock (Aurora); no logical cycle |
| Silicon / germanium quantum-dot spins | 100 ns | 6.31 µs | — | **6.31 µs** | readout | ~100 µs – 300 µs (readout-limited) |
| Donor spins in silicon | 100 ns | 6.31 µs | — | **6.31 µs** | readout | ~ms (nuclear-spin gates µs, readout 100 µs) |
| Defect-spin network nodes (NV/SiV/T) | 1 µs | 100 µs | — | **100 µs** | readout | n/a (network node) |
| Topological (Majorana) | — | 100 µs | — | **100 µs** | readout | n/a (no qubit) |
| Quantum annealing | 3.98 ns | 282 ns | — | **282 ns** | readout | µs–ms anneal; 3.6–27 ns quenches |

The derived value is a lower bound (one operation of each kind); a real QEC round stacks several gate layers plus reset, so measured cycles sit 2–5× above it on the fast platforms and inside the stated range on the slow ones. The limiter column is the point: superconducting and spin paths are readout-limited, atom paths are transport-limited, laser-gate ion paths are transport-limited and electronic-gate ion paths are gate-limited.

### 7.5 Hubs — nodes with high cross-platform reach (the 'transfers' out-degree)
| Node | Layer | Families reached | Paths | Since | Reading |
|---|---|---|---|---|---|
| **Static nearest-neighbour lattice** `cx_nn` | 4 | atoms, defects, ions, superconducting, spins, topological | 7 | 2014 | universal backbone (commodity) |
| **Single-photon detection (SNSPD / TES)** `ro_spd` | 6 | defects, ions, photonics, superconducting | 2 | 2001 | single-photon detection behind every photonic interconnect |
| **MWPM / Sparse Blossom (+correlated matching)** `dec_mwpm` | 8 | ions, photonics, superconducting, spins | 9 | 2015 | universal backbone (commodity) |
| **Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm)** `fab_pic` | 10 | atoms, ions, photonics, superconducting | 2 | 2015 | photonic-chip foundry pulled into ion traps, atom tweezers and transducers |
| **Baseband electrical control (spins, Majorana)** `ct_base` | 5 | defects, spins, topological | 4 | 2012 | shared by all solid-state spin-like carriers |
| **300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)** `fab_cmos` | 10 | ions, superconducting, spins | 3 | 2022 | CMOS foundry: spins, cryo-CMOS, standard-fab ion traps, SC wiring |
| **Mid-circuit erasure check** `ro_erasure` | 6 | atoms, photonics, superconducting | 2 | 2023 | erasure detection transferring from atoms/photons into superconducting circuits |
| **Rotated surface code (+ yoked variants)** `code_surface` | 7 | atoms, superconducting, spins | 5 | 2023 | baseline code on three families |
| **Colour code (transversal Cliffords)** `code_color` | 7 | atoms, ions, superconducting | 3 | 2024 | transversal Cliffords + distillation on three families — a direction the prose under-weighted |
| **Non-local qLDPC codes (bivariate-bicycle, 'gross')** `code_qldpc` | 7 | ions, photonics, superconducting | 2 | 2025 | overhead reduction spreading from theory to ions/SC/photonics |
| **Magic-state factory (cultivation / distillation / code switching)** `code_magic` | 7 | atoms, ions, superconducting | 3 | 2025 | non-Clifford resource on three families |
| **Relay-BP for qLDPC (FPGA)** `dec_relaybp` | 8 | ions, photonics, superconducting | 3 | 2025 | qLDPC decoder shared by SC, ions, photonics |
| **GPU decoding via NVQLink** `dec_gpu` | 8 | atoms, ions, superconducting | 3 | 2025 | platform-agnostic decoding layer (NVQLink) |
| **GKP grid encoding** `enc_gkp` | 2 | photonics, superconducting | 2 | 2020 | grid encoding shared by microwave and optical modes |
| **Metastable ('omg') erasure encoding** `enc_omg` | 2 | atoms, ions | 2 | 2023 | metastable erasure encoding on atoms and ions |
| **Dual-rail (erasure) encoding** `enc_dualrail` | 2 | photonics, superconducting | 2 | 2023 | erasure encoding shared by photonics and SC |
| **Long-range on-chip couplers (c-couplers, mm-scale)** `cx_lr` | 4 | annealing, superconducting | 2 | 2023 | long-range couplers on SC and annealers |
| **Cryo-CMOS controller (4 K / mK)** `ct_cryocmos` | 5 | superconducting, spins | 2 | 2024 | cold-stage control spreading from spins to SC (IBM/HRL) |
| **High-rate concatenated codes with transversal gates** `code_highrate` | 7 | atoms, ions | 3 | 2024 | high-rate transversal codes on atoms and ions |
| **Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC)** `code_bosonic` | 7 | photonics, superconducting | 2 | 2024 | bosonic concatenation spanning SC and photonics |
| **Neural decoders (AlphaQubit2, CNN, transformers)** `dec_nn` | 8 | atoms, superconducting | 2 | 2024 | neural decoders on SC and atoms |
| **Erasure-adapted codes** `code_erasure` | 7 | atoms, superconducting | 2 | 2025 | erasure-adapted codes on atoms and SC |
| **Correlated / loss-aware decoding (transversal, atom loss)** `dec_corr` | 8 | atoms, superconducting | 2 | 2025 |  |

### 7.6 Off-diagonal nodes — where the natural/fabricated correlation breaks
| Node | Layer | Pattern | In paths | Why it matters |
|---|---|---|---|---|
| **Dual-rail (erasure) encoding** `enc_dualrail` | 2 | fabricated carrier + erasure error structure | Superconducting dual-rail erasure | erasure — a natural-world error class — engineered into a fabricated carrier; threshold ×4 |
| **Rydberg-blockade CZ** `g_ryd` | 3 | natural carrier + sub-microsecond gate | Neutral atoms — alkaline-earth (Yb/Sr), erasure-native, Neutral atoms — alkali (Rb/Cs) | a natural carrier with a 270 ns gate: the reason atoms compete at all |
| **Electronic near-field microwave gate (ions, laser-free)** `g_elec` | 3 | natural carrier + microwave/electronic control | Trapped ions — electronic gates, chip control | removes lasers, the historic scaling blocker of ions; 8.4×10⁻⁵ |
| **Long-range on-chip couplers (c-couplers, mm-scale)** `cx_lr` | 4 | fabricated carrier + far connectivity (transport / long-range) | Quantum annealing, Superconducting transmon | gives 2D lattices the degree-6 connectivity qLDPC needs |
| **Spin shuttling (conveyor mode)** `cx_shuttle` | 4 | fabricated carrier + far connectivity (transport / long-range) | Silicon / germanium quantum-dot spins | transport connectivity for a fabricated carrier — the spin route to non-local codes |
| **Cryo-CMOS controller (4 K / mK)** `ct_cryocmos` | 5 | fabricated carrier + control/decoding in the cold stage | Superconducting transmon, Silicon / germanium quantum-dot spins | control moves into the fridge: the I/O wall is the binding constraint at 10⁴ qubits |
| **SFQ digital control (millikelvin)** `ct_sfq` | 5 | fabricated carrier + control/decoding in the cold stage | Superconducting transmon | same, at millikelvin with nW/qubit; QP poisoning is the risk |
| **On-chip flux-DAC multiplexing** `ct_fluxdac` | 5 | fabricated carrier + control/decoding in the cold stage | Quantum annealing | annealer heritage: 10⁴ qubits on 200–300 lines (D-Wave's own figures disagree) |
| **PIC-generated tweezers / integrated optics for atoms** `ct_pic_trap` | 5 | natural carrier + semiconductor / photonic-chip fabrication | Neutral atoms — alkali (Rb/Cs) | optics of the fabricated world for a natural carrier; footprint ÷50 claimed |
| **Laser control with integrated photonics (ions)** `ct_ionlaser` | 5 | natural carrier + semiconductor / photonic-chip fabrication | Trapped ions — QCCD, laser gates | integrated photonics in the trap — the ion analogue of the same move |
| **Chip-integrated microwave control (ions)** `ct_ionmw` | 5 | natural carrier + microwave/electronic control | Trapped ions — electronic gates, chip control | ~200 electronic sources for 1,000 ions instead of laser beams |
| **Mid-circuit erasure check** `ro_erasure` | 6 | fabricated carrier + erasure error structure; natural carrier + ≤ 10 µs readout | Neutral atoms — alkaline-earth (Yb/Sr), erasure-native, Superconducting dual-rail erasure | the readout primitive behind every erasure code; 384 ns on transmons |
| **Erasure-adapted codes** `code_erasure` | 7 | fabricated carrier + erasure error structure | Superconducting dual-rail erasure | threshold 0.94% → 4.15%; the largest single lever on overhead |
| **Multi-chip modules / l-couplers (same cryostat)** `ic_mcm` | 9 | fabricated carrier + far connectivity (transport / long-range) | Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure, Superconducting transmon | fabricated carriers reaching beyond one chip (chiplets, l-couplers) |
| **Cryogenic microwave link between refrigerators** `ic_cryolink` | 9 | fabricated carrier + far connectivity (transport / long-range) | Superconducting transmon | 30 m between fridges at 80% Bell — the microwave route to modularity |
| **Spin–photon solid-state link (SiV, NV, T-centre)** `ic_spinphoton` | 9 | fabricated/solid-state carrier + photonic interconnect | Defect-spin network nodes (NV/SiV/T) | solid-state spins reaching the network via photons |
| **Microwave–optical transducer (useful efficiency)** `ic_transducer` | 9 | fabricated/solid-state carrier + photonic interconnect | Superconducting transmon | the missing link for optical modularity of superconducting machines — empty |
| **300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)** `fab_cmos` | 10 | natural carrier + semiconductor / photonic-chip fabrication | Trapped ions — electronic gates, chip control | ion traps from standard semiconductor fabs (Oxford Ionics, SkyWater) |
| **Fast (≤ 20 µs) atom-array readout** `ro_imgfast` | 6 | natural carrier + ≤ 10 µs readout | Neutral atoms — alkaline-earth (Yb/Sr), erasure-native, Neutral atoms — alkali (Rb/Cs) | 17.6 µs atom readout cuts the imaging term 30–50×, but the whole QEC round only ~2× |

### 7.7 Empty slots — where a technology does not exist yet
| Slot | Status | What would fill it | Best today vs needed |
|---|---|---|---|
| **Microwave–optical transducer (useful efficiency)** `ic_transducer` (9) | empty slot — no technology yet | Best: η_tot 15%, N_add 0.16 (EO); useful regime needs η > 1/2 and N_add ≪ 1; ~3 orders of magnitude short (IBM analysis). | η_tot 15%, N_add 0.16 vs η > 1/2, N_add ≪ 1; ~3 orders of magnitude (IBM) |
| **Cryogenic / on-chip decoder (SFQ, cryo-CMOS)** `dec_cryo` (8) | empty slot — no technology yet | Designs only: NISQ+ (≤ 20 ns, SFQ), QECOOL (2.8 µW), Pinball/CryoZip (4 K predecoders) — no fabricated decoder chip. | designs only (NISQ+ 20 ns, QECOOL 2.8 µW); no fabricated decoder chip |
| **Bias-preserving cat–cat CNOT** `g_catcnot` (3) | empty slot — no technology yet | Required by every cat-qubit resource estimate; only a July-2026 theory proposal exists. | theory proposal Jul 2026; every cat resource estimate assumes it |
| **Multi-photon resource-state factory (6-ring etc.)** `src_resource` (3) | empty slot — no technology yet | Fusion-based FT needs 24–168-photon encoded resource states at high rate; largest fused deterministic-emitter graph states are 8 photons at < 1 Hz. | 8-photon states at < 1 Hz vs 24–168-photon encoded resource states at MHz |
| **Measurement-based Majorana gate** `g_mbq` (3) | empty slot — no technology yet | Braiding by sequences of parity measurements — nothing demonstrated; single-wire readout only. | single-wire parity readout only; no X-lifetime ≈ Z, no two-qubit operation |
| Silicon / germanium quantum-dot spins — Interconnect | ∅ | an interconnect for quantum-dot spins (spin–photon in dots is lab-only) | — |
| Donor spins in silicon — Interconnect | ∅ | interconnect for donor spins | — |
| Defect-spin network nodes (NV/SiV/T) — Code | ∅ | a code for network nodes (memory/repeater codes are theory) | — |
| Defect-spin network nodes (NV/SiV/T) — Decoder | ∅ | — | — |
| Topological (Majorana) — Code | ∅ | Floquet / measurement-based codes on a demonstrated qubit | — |
| Topological (Majorana) — Decoder | ∅ | — | — |
| Topological (Majorana) — Interconnect | ∅ | — | — |
| Quantum annealing — Encoding | ∅ | no encoding — analog Hamiltonian, not a qubit register | — |
| Quantum annealing — Code | ∅ | no error correction in annealing | — |
| Quantum annealing — Decoder | ∅ | — | — |
| Quantum annealing — Interconnect | ∅ | — | — |

Numeric gaps on existing nodes (attribute-level, not empty slots): ion–photon links at 10–250 s⁻¹ vs ≥ 10⁴ s⁻¹ needed; photonic switch loss 100–190 mdB vs ~7 mdB; optical GKP effective squeezing 0.62 dB vs 9.75 dB; cat phase-flip ~10⁻¹ per CX vs 10⁻³ assumed; spin readout 6 µs at 99.2% vs sub-µs at 99.9% for a µs-class cycle; atom imaging 0.5–1 ms typical vs 17.6 µs emerging.

### 7.8 Validity check — does the graph reproduce §5 on its own?
| Direction (from §5) | Defining nodes | In S | Missing | Coverage |
|---|---|---|---|---|
| D1 superconducting + engineered error structure + qLDPC + cold-stage control | 12 | `enc_dualrail`, `ro_erasure`, `code_erasure`, `code_qldpc`, `cx_lr`, `ct_cryocmos`, `ct_sfq`, `ct_fluxdac`, `ic_mcm`, `ic_cryolink`, `dec_relaybp`, `dec_nn` | — | **1.00** |
| D2 neutral atoms + zoned + transversal/algorithmic FT + erasure conversion | 7 | `g_ryd`, `enc_omg`, `ro_erasure`, `code_erasure`, `code_highrate`, `ro_imgfast`, `ct_pic_trap` | — | **1.00** |
| D3 trapped ions + electronic gates + chip traps | 4 | `g_elec`, `ct_ionmw`, `fab_cmos`, `ct_ionlaser` | — | **1.00** |
| D4 silicon spins + CMOS manufacturability | 3 | `fab_cmos`, `ct_cryocmos`, `cx_shuttle` | — | **1.00** |
| D5 photonics as interconnect | 4 | `fab_pic`, `ro_spd`, `ic_transducer`, `ic_spinphoton` | — | **1.00** |
| D6 bosonic codes as a direction | 4 | `enc_dualrail`, `enc_gkp`, `code_bosonic`, `g_catcnot` | — | **1.00** |
| X1 erasure engineering (cross-cutting) | 4 | `enc_dualrail`, `enc_omg`, `ro_erasure`, `code_erasure` | — | **1.00** |
| X2 real-time decoding (cross-cutting) | 4 | `dec_nn`, `dec_relaybp`, `dec_gpu`, `dec_cryo` | — | **1.00** |
| X3 qLDPC / transversal FT (cross-cutting) | 3 | `code_qldpc`, `code_highrate`, `code_magic` | — | **1.00** |
| X4 cold-stage control (cross-cutting) | 3 | `ct_sfq`, `ct_cryocmos`, `ct_fluxdac` | — | **1.00** |
| X5 photonic interconnect (cross-cutting) | 3 | `fab_pic`, `ro_spd`, `ic_transducer` | — | **1.00** |

S has 40 nodes. All eleven directions are reproduced with coverage 1.00. **Residuals:** (i) the prose also called *diagonal* enablers promising — atom transport, algorithmic FT, correlated decoding, Yb/Sr atoms, QCCD, MEMS traps, ion–photon links (§7.1 lists them as `diagonal_enablers`); the graph classifies these as native strengths of a family, not cross-platform directions — a useful distinction the prose blurred. (ii) The graph flags nodes the prose did not name as directions: `code_color`, `code_surface`, `ct_base`, `cx_nn`, `dec_corr`, `dec_mwpm`, `g_mbq`, `src_resource` — the colour code (transversal Cliffords + distillation on three families), the surface-code/NN-lattice/MWPM/baseband backbone (commodities every family shares; not a direction, but the graph's honest picture of where the stack is standardised), and two empty slots (Majorana measurement-based gate; multi-photon resource-state factory) that belong on the watch-list. (iii) The photonic-interconnect direction is reproduced through its *dependencies* (PIC foundry, single-photon detectors, transducer), not through photonic-link nodes themselves — i.e. the prose's claim 'photonics is the interconnect for everyone' is, in graph terms, 'every family now depends on the photonic supply chain'.

### 7.9 How a 7-coordinate, 5-edge-type graph is best shown — and why the map is dynamic
Options weighed: a force-directed layout (rejected — it destroys the layer semantics and makes the stack unreadable); an adjacency matrix (right for the dense *requires* relation but wrong for a narrative reader — kept as a table); a chord diagram (rejected — no layers); 3D (rejected — occlusion). The chosen form is a **layered map in the metro-map idiom**: the ten layers are columns; the vertical position inside a column is the node's carrier-nature affinity, so the natural/fabricated *diagonal* becomes literally visible and off-diagonal nodes sit where a warm path dips into the cool half or vice versa; platform paths are coloured lines through their stations; a station on several lines is an interchange — the *transfers* degree at a glance; empty slots are hollow dashed stations. Coordinates cannot all be painted at once (one hue channel is all a reader has), so the map carries a **lens** that recolours every station by one coordinate at a time, and a **parallel-coordinates strip** shows the full seven-vector of every node as a polyline; a **node inspector** keeps the three spaces physically apart — design coordinates, dated evaluation attributes, actors/goals. Edges of type *requires / alternatives / conflicts* are drawn only on focus (degree-of-interest), because 96 nodes × 160 edges is a hairball; *defines* edges live in the inspector as dated rows, not lines. **Dynamic is necessary, static is mandatory:** the resting frame is a complete readable map (all paths, all stations) that prints and thumbnails; the interaction adds lenses, focus and filters without which five edge types cannot be read. The equivalent static artefacts — the tables of §7.2–9.8 — are the print fallback.

### 7.10 Edge list
**requires / provides**

| From | To | Note |
|---|---|---|
| `g_tc` Tunable-coupler CZ / iSWAP | `transmon` Transmon | flux-tunable coupler between transmons |
| `g_cr` Cross-resonance (fixed-frequency, all-microwave) | `transmon` Transmon | fixed-frequency transmons |
| `g_ryd` Rydberg-blockade CZ | `alkali` Alkali atom (Rb/Cs) in tweezer | Rydberg excitation of the atom *(one-of)* |
| `g_ryd` Rydberg-blockade CZ | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | Rydberg excitation of the atom *(one-of)* |
| `g_ryd` Rydberg-blockade CZ | `ct_laser` Laser + AOD/SLM optical control (atoms) | Rydberg lasers, global pulses |
| `g_ms` Mølmer–Sørensen / light-shift laser gate | `ion` Trapped atomic ion | spin–motion coupling |
| `g_ms` Mølmer–Sørensen / light-shift laser gate | `ct_ionlaser` Laser control with integrated photonics (ions) | laser fields |
| `g_elec` Electronic near-field microwave gate (ions, laser-free) | `ion` Trapped atomic ion | chip currents act on the ion |
| `g_elec` Electronic near-field microwave gate (ions, laser-free) | `ct_ionmw` Chip-integrated microwave control (ions) | electronic signal sources |
| `g_exch` Exchange gate (spins; incl. shuttled-spin CZ) | `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | exchange between dots *(one-of)* |
| `g_exch` Exchange gate (spins; incl. shuttled-spin CZ) | `donor` Donor spin (P in ²⁸Si) | exchange between donors *(one-of)* |
| `g_exch` Exchange gate (spins; incl. shuttled-spin CZ) | `ct_base` Baseband electrical control (spins, Majorana) | voltage pulses on gates |
| `g_fusion` Linear-optical fusion (heralded) | `photon` Single photon (discrete variable) | photons to fuse |
| `g_fusion` Linear-optical fusion (heralded) | `ro_spd` Single-photon detection (SNSPD / TES) | heralding detection |
| `g_fusion` Linear-optical fusion (heralded) | `cx_switch` Photonic switching / routing (EO, feed-forward) | feed-forward routing |
| `g_cv` CV Gaussian gates + GKP-assisted non-Gaussian ops | `squeezed` Squeezed light mode (CV) | squeezed modes |
| `g_cv` CV Gaussian gates + GKP-assisted non-Gaussian ops | `ct_eo` Electro-optic drive + feed-forward electronics (RT) | homodyne feed-forward |
| `g_bos` Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) | `cavity` Bosonic cavity mode | bosonic modes |
| `g_bos` Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) | `transmon` Transmon | ancilla transmon *(one-of)* |
| `g_catcnot` Bias-preserving cat–cat CNOT | `enc_cat` Cat-code encoding (biased noise) | two cat qubits |
| `g_mbq` Measurement-based Majorana gate | `majorana` Majorana parity (InAs–Pb tetron) | Majorana wires |
| `g_mbq` Measurement-based Majorana gate | `ro_qcap` rf quantum-capacitance parity readout | measurement-based |
| `g_mwspin` Microwave / optical spin gates (defect centres, 1Q spins) | `defect` Colour-centre / defect spin (NV, SiV, SnV, T) | spin register |
| `src_resource` Multi-photon resource-state factory (6-ring etc.) | `g_fusion` Linear-optical fusion (heralded) | fusions build the resource state |
| `src_resource` Multi-photon resource-state factory (6-ring etc.) | `photon` Single photon (discrete variable) | deterministic or multiplexed photons |
| `enc_cat` Cat-code encoding (biased noise) | `cavity` Bosonic cavity mode | two-photon dissipation on a mode |
| `enc_gkp` GKP grid encoding | `cavity` Bosonic cavity mode | microwave GKP *(one-of)* |
| `enc_gkp` GKP grid encoding | `squeezed` Squeezed light mode (CV) | optical GKP needs ~10 dB squeezing *(one-of)* |
| `enc_dualrail` Dual-rail (erasure) encoding | `ro_erasure` Mid-circuit erasure check | erasure check |
| `enc_omg` Metastable ('omg') erasure encoding | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | metastable manifold *(one-of)* |
| `enc_omg` Metastable ('omg') erasure encoding | `ion` Trapped atomic ion | metastable ion levels *(one-of)* |
| `enc_eo` Exchange-only / singlet-triplet spin encoding | `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | three-dot encoded qubit |
| `enc_timebin` Time-bin / path photonic encoding | `photon` Single photon (discrete variable) | photonic modes |
| `enc_parity` Fermion-parity encoding (tetron) | `majorana` Majorana parity (InAs–Pb tetron) | two wires per tetron |
| `enc_bare` Bare two-level subspace | `transmon` Transmon | anharmonic subspace |
| `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | `ion` Trapped atomic ion | ions to move |
| `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | `fab_trap` Surface-electrode ion-trap microfabrication | junction / grid traps |
| `cx_aod` Atom transport by AOD tweezers (zoned architecture) | `ct_laser` Laser + AOD/SLM optical control (atoms) | AOD deflectors |
| `cx_shuttle` Spin shuttling (conveyor mode) | `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | spins to move |
| `cx_shuttle` Spin shuttling (conveyor mode) | `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | uniform conveyor gates |
| `cx_lr` Long-range on-chip couplers (c-couplers, mm-scale) | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | multilayer routing |
| `cx_switch` Photonic switching / routing (EO, feed-forward) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | low-loss switches |
| `cx_crossbar` Crossbar shared-line control (spins) | `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | dot array |
| `ct_sfq` SFQ digital control (millikelvin) | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | flip-chip SFQ MCM |
| `ct_cryocmos` Cryo-CMOS controller (4 K / mK) | `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | cryo ASIC |
| `ct_fluxdac` On-chip flux-DAC multiplexing | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | on-chip SFQ DACs |
| `ct_pic_trap` PIC-generated tweezers / integrated optics for atoms | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | photonic chip |
| `ct_ionlaser` Laser control with integrated photonics (ions) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | integrated waveguides |
| `ct_ionmw` Chip-integrated microwave control (ions) | `fab_trap` Surface-electrode ion-trap microfabrication | current traces in the trap |
| `ct_eo` Electro-optic drive + feed-forward electronics (RT) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | modulators |
| `ro_disp` Dispersive microwave readout (+TWPA, Purcell) | `transmon` Transmon | dispersive shift *(one-of)* |
| `ro_disp` Dispersive microwave readout (+TWPA, Purcell) | `cavity` Bosonic cavity mode | ancilla-mediated readout *(one-of)* |
| `ro_fluor` Fluorescence state detection (ions) | `ion` Trapped atomic ion | cycling transition *(one-of)* |
| `ro_fluor` Fluorescence state detection (ions) | `defect` Colour-centre / defect spin (NV, SiV, SnV, T) | optical readout of the spin *(one-of)* |
| `ro_img` Fluorescence imaging of atom arrays | `alkali` Alkali atom (Rb/Cs) in tweezer | imaging transition *(one-of)* |
| `ro_img` Fluorescence imaging of atom arrays | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | imaging transition *(one-of)* |
| `ro_imgfast` Fast (≤ 20 µs) atom-array readout | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | Yb fast imaging |
| `ro_s2c` Spin-to-charge conversion + rf reflectometry | `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | charge sensor *(one-of)* |
| `ro_s2c` Spin-to-charge conversion + rf reflectometry | `donor` Donor spin (P in ²⁸Si) | charge sensor *(one-of)* |
| `ro_spd` Single-photon detection (SNSPD / TES) | `photon` Single photon (discrete variable) | detection |
| `ro_qcap` rf quantum-capacitance parity readout | `majorana` Majorana parity (InAs–Pb tetron) | quantum capacitance |
| `ro_erasure` Mid-circuit erasure check | `enc_dualrail` Dual-rail (erasure) encoding | erasure-detectable encoding *(one-of)* |
| `ro_erasure` Mid-circuit erasure check | `enc_omg` Metastable ('omg') erasure encoding | erasure-detectable encoding *(one-of)* |
| `code_surface` Rotated surface code (+ yoked variants) | `cx_nn` Static nearest-neighbour lattice | 2D nearest-neighbour checks |
| `code_color` Colour code (transversal Cliffords) | `cx_nn` Static nearest-neighbour lattice | 2D checks |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `cx_lr` Long-range on-chip couplers (c-couplers, mm-scale) | degree-6 long-range checks *(one-of)* |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | long-range via transport *(one-of)* |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `cx_bus` Ion-chain motional bus (all-to-all in chain) | all-to-all in chain *(one-of)* |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `cx_aod` Atom transport by AOD tweezers (zoned architecture) | long-range via transport *(one-of)* |
| `code_highrate` High-rate concatenated codes with transversal gates | `cx_aod` Atom transport by AOD tweezers (zoned architecture) | transversal blocks by transport *(one-of)* |
| `code_highrate` High-rate concatenated codes with transversal gates | `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | all-to-all via QCCD *(one-of)* |
| `code_highrate` High-rate concatenated codes with transversal gates | `cx_bus` Ion-chain motional bus (all-to-all in chain) | all-to-all in chain *(one-of)* |
| `code_erasure` Erasure-adapted codes | `ro_erasure` Mid-circuit erasure check | erasure flags |
| `code_erasure` Erasure-adapted codes | `dec_corr` Correlated / loss-aware decoding (transversal, atom loss) | erasure-/loss-aware decoding (flags are useless to a plain matcher) |
| `code_bosonic` Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | `enc_cat` Cat-code encoding (biased noise) | biased inner qubit *(one-of)* |
| `code_bosonic` Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | `enc_gkp` GKP grid encoding | GKP inner qubit *(one-of)* |
| `code_fusion` Fusion-based fault tolerance | `g_fusion` Linear-optical fusion (heralded) | fusion measurements |
| `code_fusion` Fusion-based fault tolerance | `src_resource` Multi-photon resource-state factory (6-ring etc.) | resource states |
| `code_aft` Algorithmic FT / transversal architectures | `cx_aod` Atom transport by AOD tweezers (zoned architecture) | transversal gates by transport *(one-of)* |
| `code_aft` Algorithmic FT / transversal architectures | `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | transversal gates by ion shuttling (Quantinuum tesseract on ions) *(one-of)* |
| `code_aft` Algorithmic FT / transversal architectures | `dec_corr` Correlated / loss-aware decoding (transversal, atom loss) | correlated decoding |
| `code_magic` Magic-state factory (cultivation / distillation / code switching) | `code_surface` Rotated surface code (+ yoked variants) | host code *(one-of)* |
| `code_magic` Magic-state factory (cultivation / distillation / code switching) | `code_color` Colour code (transversal Cliffords) | host code *(one-of)* |
| `dec_relaybp` Relay-BP for qLDPC (FPGA) | `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | qLDPC syndromes |
| `dec_corr` Correlated / loss-aware decoding (transversal, atom loss) | `code_highrate` High-rate concatenated codes with transversal gates | transversal circuits |
| `dec_rl` In-loop RL calibration / decoder steering | `dec_nn` Neural decoders (AlphaQubit2, CNN, transformers) | decoder in the loop |
| `dec_cryo` Cryogenic / on-chip decoder (SFQ, cryo-CMOS) | `ct_sfq` SFQ digital control (millikelvin) | cold digital logic *(one-of)* |
| `dec_cryo` Cryogenic / on-chip decoder (SFQ, cryo-CMOS) | `ct_cryocmos` Cryo-CMOS controller (4 K / mK) | cold digital logic *(one-of)* |
| `dec_fpga` FPGA real-time decoders (LCD, Deltaflow) | `code_surface` Rotated surface code (+ yoked variants) | matching/clustering on surface syndromes *(one-of)* |
| `dec_nn` Neural decoders (AlphaQubit2, CNN, transformers) | `code_surface` Rotated surface code (+ yoked variants) | trained on surface-code syndromes *(one-of)* |
| `ic_mcm` Multi-chip modules / l-couplers (same cryostat) | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | chiplets, couplers |
| `ic_cryolink` Cryogenic microwave link between refrigerators | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | superconducting waveguide |
| `ic_ionphoton` Ion–photon photonic link | `ion` Trapped atomic ion | ion–photon entanglement |
| `ic_ionphoton` Ion–photon photonic link | `ro_spd` Single-photon detection (SNSPD / TES) | photon detection |
| `ic_atomcavity` Atom–photon cavity interface | `alkali` Alkali atom (Rb/Cs) in tweezer | cavity-coupled atoms *(one-of)* |
| `ic_atomcavity` Atom–photon cavity interface | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | cavity-coupled atoms *(one-of)* |
| `ic_atomcavity` Atom–photon cavity interface | `fab_optics` Optical / mechanical assembly (lasers, vacuum, objectives) | cavities |
| `ic_spinphoton` Spin–photon solid-state link (SiV, NV, T-centre) | `defect` Colour-centre / defect spin (NV, SiV, SnV, T) | spin–photon interface |
| `ic_spinphoton` Spin–photon solid-state link (SiV, NV, T-centre) | `ro_spd` Single-photon detection (SNSPD / TES) | photon detection |
| `ic_transducer` Microwave–optical transducer (useful efficiency) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | electro-optic / optomechanical chip |
| `ic_transducer` Microwave–optical transducer (useful efficiency) | `ro_spd` Single-photon detection (SNSPD / TES) | heralded entanglement through the transducer needs single-photon detection |
| `ic_transducer` Microwave–optical transducer (useful efficiency) | `transmon` Transmon | microwave qubit |
| `ic_fibre` Fibre links between photonic modules | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | chip-to-fibre coupling |
| `transmon` Transmon | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | JJ lithography |
| `fluxonium` Fluxonium | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | JJ arrays |
| `cavity` Bosonic cavity mode | `fab_3d` 3D machined superconducting cavities | machined cavities *(one-of)* |
| `fluxq` rf-SQUID flux qubit (annealer) | `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | annealer fab |
| `ion` Trapped atomic ion | `fab_trap` Surface-electrode ion-trap microfabrication | surface-electrode trap |
| `ion` Trapped atomic ion | `fab_optics` Optical / mechanical assembly (lasers, vacuum, objectives) | lasers, vacuum |
| `alkali` Alkali atom (Rb/Cs) in tweezer | `fab_optics` Optical / mechanical assembly (lasers, vacuum, objectives) | tweezers, vacuum |
| `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | `fab_optics` Optical / mechanical assembly (lasers, vacuum, objectives) | tweezers, clock lasers |
| `photon` Single photon (discrete variable) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | sources, waveguides |
| `squeezed` Squeezed light mode (CV) | `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | squeezers |
| `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | 300 mm dots |
| `donor` Donor spin (P in ²⁸Si) | `fab_stm` STM hydrogen lithography (donors) | STM placement |
| `defect` Colour-centre / defect spin (NV, SiV, SnV, T) | `fab_diamond` Diamond growth / implantation (NV, SiV, SnV) | host crystal |
| `majorana` Majorana parity (InAs–Pb tetron) | `fab_mbe` III-V MBE heterostructures (InAs–Pb wires, QD sources) | InAs–Pb stack |

**alternatives (within layer)**

| From | To | Note |
|---|---|---|
| `transmon` Transmon | `fluxonium` Fluxonium | alternative superconducting carriers |
| `alkali` Alkali atom (Rb/Cs) in tweezer | `ae_atom` Alkaline-earth atom (Yb/Sr) — erasure-native | alternative atomic species |
| `photon` Single photon (discrete variable) | `squeezed` Squeezed light mode (CV) | DV vs CV photonics |
| `qd_spin` Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge) | `donor` Donor spin (P in ²⁸Si) | dot vs donor spins |
| `enc_bare` Bare two-level subspace | `enc_dualrail` Dual-rail (erasure) encoding | bare vs erasure encoding |
| `enc_bare` Bare two-level subspace | `enc_cat` Cat-code encoding (biased noise) | bare vs cat |
| `enc_cat` Cat-code encoding (biased noise) | `enc_gkp` GKP grid encoding | cat vs GKP |
| `enc_hf` Hyperfine / clock-state qubit | `enc_omg` Metastable ('omg') erasure encoding | ground vs metastable manifold |
| `enc_eo` Exchange-only / singlet-triplet spin encoding | `enc_spin_ld` Single-spin (Loss–DiVincenzo) / nuclear-spin encoding | encoded vs bare spin |
| `g_tc` Tunable-coupler CZ / iSWAP | `g_cr` Cross-resonance (fixed-frequency, all-microwave) | tunable vs fixed-frequency |
| `g_ms` Mølmer–Sørensen / light-shift laser gate | `g_elec` Electronic near-field microwave gate (ions, laser-free) | laser vs electronic gates |
| `g_fusion` Linear-optical fusion (heralded) | `g_cv` CV Gaussian gates + GKP-assisted non-Gaussian ops | DV fusion vs CV Gaussian |
| `g_bos` Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) | `g_catcnot` Bias-preserving cat–cat CNOT | ancilla-mediated vs direct cat CNOT |
| `cx_nn` Static nearest-neighbour lattice | `cx_lr` Long-range on-chip couplers (c-couplers, mm-scale) | NN vs long-range couplers |
| `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | `cx_bus` Ion-chain motional bus (all-to-all in chain) | shuttling vs chain bus |
| `cx_nn` Static nearest-neighbour lattice | `cx_shuttle` Spin shuttling (conveyor mode) | static vs shuttled spins |
| `cx_nn` Static nearest-neighbour lattice | `cx_crossbar` Crossbar shared-line control (spins) | individual vs shared lines |
| `ct_rt` Room-temperature electronics + per-qubit coax/flex | `ct_cryocmos` Cryo-CMOS controller (4 K / mK) | RT vs 4 K control |
| `ct_rt` Room-temperature electronics + per-qubit coax/flex | `ct_sfq` SFQ digital control (millikelvin) | RT vs mK SFQ |
| `ct_cryocmos` Cryo-CMOS controller (4 K / mK) | `ct_sfq` SFQ digital control (millikelvin) | cryo-CMOS vs SFQ |
| `ct_rt` Room-temperature electronics + per-qubit coax/flex | `ct_fluxdac` On-chip flux-DAC multiplexing | RT lines vs on-chip DACs |
| `ct_laser` Laser + AOD/SLM optical control (atoms) | `ct_pic_trap` PIC-generated tweezers / integrated optics for atoms | free-space vs PIC optics |
| `ct_ionlaser` Laser control with integrated photonics (ions) | `ct_ionmw` Chip-integrated microwave control (ions) | laser vs microwave ion control |
| `ro_img` Fluorescence imaging of atom arrays | `ro_imgfast` Fast (≤ 20 µs) atom-array readout | ms vs µs imaging |
| `code_surface` Rotated surface code (+ yoked variants) | `code_color` Colour code (transversal Cliffords) | surface vs colour |
| `code_surface` Rotated surface code (+ yoked variants) | `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | local (surface) vs non-local constant-rate qLDPC — alternatives for the same slot, combinable hierarchically (surface/LPU processing + gross memory) |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `code_highrate` High-rate concatenated codes with transversal gates | non-local BB memory (gross) vs high-rate transversal blocks ([[16,6,4]] tesseract, [[16,4,2,4]]) |
| `code_surface` Rotated surface code (+ yoked variants) | `code_highrate` High-rate concatenated codes with transversal gates | 2D vs high-rate transversal |
| `code_surface` Rotated surface code (+ yoked variants) | `code_erasure` Erasure-adapted codes | Pauli vs erasure-adapted |
| `code_fusion` Fusion-based fault tolerance | `code_bosonic` Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | DV fusion FT vs GKP concatenation |
| `dec_mwpm` MWPM / Sparse Blossom (+correlated matching) | `dec_nn` Neural decoders (AlphaQubit2, CNN, transformers) | matching vs neural |
| `dec_mwpm` MWPM / Sparse Blossom (+correlated matching) | `dec_relaybp` Relay-BP for qLDPC (FPGA) | matching vs BP |
| `dec_fpga` FPGA real-time decoders (LCD, Deltaflow) | `dec_gpu` GPU decoding via NVQLink | FPGA vs GPU |
| `dec_fpga` FPGA real-time decoders (LCD, Deltaflow) | `dec_cryo` Cryogenic / on-chip decoder (SFQ, cryo-CMOS) | RT FPGA vs cryo decoder |
| `ic_mcm` Multi-chip modules / l-couplers (same cryostat) | `ic_cryolink` Cryogenic microwave link between refrigerators | same-fridge vs inter-fridge |
| `ic_cryolink` Cryogenic microwave link between refrigerators | `ic_transducer` Microwave–optical transducer (useful efficiency) | microwave link vs optical link |
| `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | `fab_3d` 3D machined superconducting cavities | planar vs 3D |
| `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | `fab_stm` STM hydrogen lithography (donors) | foundry vs STM |
| `fab_trap` Surface-electrode ion-trap microfabrication | `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | MEMS vs standard CMOS fab for traps |

**conflicts**

| From | To | Mechanism | Measured price | Mitigation | Status · source |
|---|---|---|---|---|---|
| `code_highrate` High-rate concatenated codes with transversal gates | `cx_nn` Static nearest-neighbour lattice | needs all-to-all connectivity | no nearest-neighbour device has run a high-rate code; on a static lattice the non-local checks need SWAP networks whose depth grows with the check span, and errors accumulate with it | long-range on-chip couplers (IBM c-couplers, Loon 2025-11) or physical transport (atoms, ions) | open — no mitigation shown at scale · [2025-06](https://arxiv.org/abs/2506.03094) |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | `cx_nn` Static nearest-neighbour lattice | needs degree ≥ 6; heavy-hex insufficient without c-couplers | bivariate-bicycle codes need a degree-6 Tanner graph — two long-range connections per qubit — which heavy-hex (degree 2–3) cannot provide; without c-couplers no gross code runs | c-couplers (Loon), then Kookaburra module; measured coupler fidelity and length not yet published | open — no mitigation shown at scale · [2024-03](https://www.nature.com/articles/s41586-024-07107-7) |
| `code_aft` Algorithmic FT / transversal architectures | `cx_nn` Static nearest-neighbour lattice | transversal permutations need transport | transversal gates between logical blocks need block-to-block qubit permutations; on a static lattice that is O(d) SWAP depth per logical gate, which erases the constant-depth advantage | physical transport (AOD tweezers, ion shuttling) — the reason the architecture is atom/ion-native | bypassed by a different node in a third layer · [2025-09](https://www.nature.com/articles/s41586-025-09543-5) |
| `enc_cat` Cat-code encoding (biased noise) | `code_surface` Rotated surface code (+ yoked variants) | unbiased code wastes the bias — needs repetition/XZZX/elevator codes | a CSS surface code corrects X and Z symmetrically, so a bias > 25 (Ocelot, 2025) buys nothing; the ~10× qubit saving of cat architectures exists only with bias-tailored codes | repetition (Ocelot), XZZX, elevator or LDPC-cat codes instead of the plain surface code | bypassed by a different node in a third layer · [2025-02](https://www.nature.com/articles/s41586-025-08642-7) |
| `enc_dualrail` Dual-rail (erasure) encoding | `code_surface` Rotated surface code (+ yoked variants) | plain surface code discards erasure flags | a matching decoder that ignores erasure flags sees a threshold of 0.937% instead of 4.15% — the erasure advantage is lost entirely | erasure-aware decoding (heralded-loss matching) — a decoder change, not a hardware change | mitigated at small scale · [2022-01](https://arxiv.org/abs/2201.03540) |
| `ro_spd` Single-photon detection (SNSPD / TES) | `code_surface` Rotated surface code (+ yoked variants) | destructive detection precludes repeated syndrome extraction on the same photon | a detected photon is gone: no repeated syndrome extraction on the same carrier, so a surface-code memory cycle cannot be run on flying qubits | fusion-based / measurement-based fault tolerance, where every photon is measured exactly once by design | bypassed by a different node in a third layer · [2023-02](https://www.nature.com/articles/s41467-023-36493-1) |
| `g_ms` Mølmer–Sørensen / light-shift laser gate | `cx_bus` Ion-chain motional bus (all-to-all in chain) | gate time grows with chain length (median 672 µs on Forte's 30-ion chain) | spectral crowding of the motional modes makes the gate slower and less faithful as the chain grows: median 672 µs on Forte's 30-ion chain vs ~10–30 µs on short chains | short chains in zoned QCCD traps (Quantinuum), amplitude/phase-modulated gates, or electronic gates on ≤ 4-ion segments | open — no mitigation shown at scale · [2025](https://www.ionq.com/quantum-systems/forte) |
| `fab_3d` 3D machined superconducting cavities | `cx_nn` Static nearest-neighbour lattice | cm-scale cavities cannot tile dense 2D lattices | cm-scale machined cavities give ~1 mode per cm²; a dense 2D lattice of them is impossible, so 3D bosonic qubits stop at a few tens of modes per module | mm-scale coaxial λ/4 and double-post cavities, or planar bosonic modes; density still an order below transmon lattices | open — no mitigation shown at scale · [2026-07](https://arxiv.org/abs/2607.06718) |
| `cx_crossbar` Crossbar shared-line control (spins) | `g_exch` Exchange gate (spins; incl. shuttled-spin CZ) | shared lines vs per-pair exchange calibration | one shared line drives many exchange gates at once, but J varies dot-to-dot with disorder; the 2024 16-dot crossbar showed no coherent qubit operation | 300 mm uniformity (~1% device-to-device), local floating-gate trims, or a semi-shared scheme with per-qubit correction lines | open — no mitigation shown at scale · [2024-07](https://www.nature.com/articles/s41467-024-50355-4) |
| `ct_sfq` SFQ digital control (millikelvin) | `transmon` Transmon | SFQ switching photons cause quasiparticle poisoning unless shielded (0.96% error source in 2023 MCM) | photons emitted by switching junctions lie above the aluminium gap (2Δ ≈ 90 GHz) and break Cooper pairs in the qubit film: T₁ decay plus correlated, non-Pauli bursts; 0.96(2)% of the 1.2(1)% error per Clifford in the 2023 multi-chip module | driver on a separate die, pulse-bandwidth limiting (projected 0.1%), quasiparticle traps / gap engineering, mm-wave shielding; SEEQC 2026 reports no detectable poisoning at 5 qubits | mitigated at small scale · [2023-09](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310) |
| `code_color` Colour code (transversal Cliffords) | `dec_mwpm` MWPM / Sparse Blossom (+correlated matching) | colour-code syndromes contain three-body (hyperedge) events that pairwise matching cannot decode | weight-6 checks produce detection events that fire in triples; a plain matcher is not applicable, and the decoders that are (restriction, Möbius, Chromobius) lose accuracy — Google's d=5 colour memory reached 8.19(14)×10⁻³ per cycle with the search-based Tesseract decoder, worse than its d=5 surface code | hyperedge-capable decoders: Chromobius / restriction decoders, Tesseract (search), neural decoders; hook-free one-ancilla circuits (2026) reduce the hyperedge burden | mitigated at small scale · [2026-07](https://www.nature.com/articles/s41586-026-10759-2) |
| `dec_gpu` GPU decoding via NVQLink | `transmon` Transmon | GPU decoding over NVQLink adds a ~4 µs round trip to a ~1 µs surface-code cycle | NVQLink's measured round trip is 3.84 µs mean / 3.96 µs max, i.e. 3–4 surface-code cycles of a Willow-class transmon (~1.1 µs): syndromes queue faster than any single-cycle reaction, so real-time feed-forward (non-Clifford, teleportation) must wait | windowed / streaming decoding with an FPGA pre-decoder at the fridge, deferring only the reaction-critical decisions; slower carriers (atoms, ions: ms cycles) do not see the conflict | open — no mitigation shown at scale · [2025-11](https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/) |

**transfers (node → additional platform paths)**

| Node | Paths |
|---|---|
| `transmon` Transmon | Superconducting transmon, Superconducting dual-rail erasure |
| `cavity` Bosonic cavity mode | Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure |
| `ion` Trapped atomic ion | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control |
| `enc_hf` Hyperfine / clock-state qubit | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control, Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `enc_omg` Metastable ('omg') erasure encoding | Trapped ions — electronic gates, chip control, Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `enc_dualrail` Dual-rail (erasure) encoding | Superconducting dual-rail erasure, Photonic — fusion-based (DV) |
| `enc_gkp` GKP grid encoding | Superconducting bosonic (cat / GKP), Photonic — continuous-variable / GKP |
| `g_ryd` Rydberg-blockade CZ | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `g_ms` Mølmer–Sørensen / light-shift laser gate | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control |
| `g_exch` Exchange gate (spins; incl. shuttled-spin CZ) | Silicon / germanium quantum-dot spins, Donor spins in silicon |
| `g_fusion` Linear-optical fusion (heralded) | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `g_bos` Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter) | Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure |
| `cx_nn` Static nearest-neighbour lattice | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure, Silicon / germanium quantum-dot spins, Donor spins in silicon, Defect-spin network nodes (NV/SiV/T), Topological (Majorana) |
| `cx_lr` Long-range on-chip couplers (c-couplers, mm-scale) | Superconducting transmon, Quantum annealing |
| `cx_qccd` Ion shuttling (QCCD, junctions, grid traps) | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control |
| `cx_aod` Atom transport by AOD tweezers (zoned architecture) | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `cx_switch` Photonic switching / routing (EO, feed-forward) | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `ct_rt` Room-temperature electronics + per-qubit coax/flex | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure |
| `ct_cryocmos` Cryo-CMOS controller (4 K / mK) | Superconducting transmon, Silicon / germanium quantum-dot spins |
| `ct_laser` Laser + AOD/SLM optical control (atoms) | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `ct_base` Baseband electrical control (spins, Majorana) | Silicon / germanium quantum-dot spins, Donor spins in silicon, Defect-spin network nodes (NV/SiV/T), Topological (Majorana) |
| `ro_disp` Dispersive microwave readout (+TWPA, Purcell) | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure, Quantum annealing |
| `ro_fluor` Fluorescence state detection (ions) | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control, Defect-spin network nodes (NV/SiV/T) |
| `ro_img` Fluorescence imaging of atom arrays | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `ro_s2c` Spin-to-charge conversion + rf reflectometry | Silicon / germanium quantum-dot spins, Donor spins in silicon |
| `ro_spd` Single-photon detection (SNSPD / TES) | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `ro_erasure` Mid-circuit erasure check | Superconducting dual-rail erasure, Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `code_surface` Rotated surface code (+ yoked variants) | Superconducting transmon, Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native, Silicon / germanium quantum-dot spins, Donor spins in silicon |
| `code_color` Colour code (transversal Cliffords) | Superconducting transmon, Trapped ions — QCCD, laser gates, Neutral atoms — alkali (Rb/Cs) |
| `code_qldpc` Non-local qLDPC codes (bivariate-bicycle, 'gross') | Superconducting transmon, Trapped ions — electronic gates, chip control |
| `code_highrate` High-rate concatenated codes with transversal gates | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control, Neutral atoms — alkali (Rb/Cs) |
| `code_erasure` Erasure-adapted codes | Superconducting dual-rail erasure, Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `code_bosonic` Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC) | Superconducting bosonic (cat / GKP), Photonic — continuous-variable / GKP |
| `code_magic` Magic-state factory (cultivation / distillation / code switching) | Superconducting transmon, Trapped ions — QCCD, laser gates, Neutral atoms — alkali (Rb/Cs) |
| `dec_mwpm` MWPM / Sparse Blossom (+correlated matching) | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure, Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control, Photonic — fusion-based (DV), Photonic — continuous-variable / GKP, Silicon / germanium quantum-dot spins, Donor spins in silicon |
| `dec_nn` Neural decoders (AlphaQubit2, CNN, transformers) | Superconducting transmon, Neutral atoms — alkali (Rb/Cs) |
| `dec_relaybp` Relay-BP for qLDPC (FPGA) | Superconducting transmon, Trapped ions — electronic gates, chip control, Photonic — continuous-variable / GKP |
| `dec_gpu` GPU decoding via NVQLink | Superconducting transmon, Trapped ions — QCCD, laser gates, Neutral atoms — alkali (Rb/Cs) |
| `dec_corr` Correlated / loss-aware decoding (transversal, atom loss) | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `ic_mcm` Multi-chip modules / l-couplers (same cryostat) | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure |
| `ic_ionphoton` Ion–photon photonic link | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control |
| `ic_atomcavity` Atom–photon cavity interface | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `ic_fibre` Fibre links between photonic modules | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `fab_cmos` 300 mm CMOS foundry (spins, cryo-CMOS, SC wiring) | Superconducting transmon, Trapped ions — electronic gates, chip control, Silicon / germanium quantum-dot spins |
| `fab_sc` Superconducting-qubit lithography (Nb/Al JJ, 300 mm) | Superconducting transmon, Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure, Quantum annealing |
| `fab_3d` 3D machined superconducting cavities | Superconducting bosonic (cat / GKP), Superconducting dual-rail erasure |
| `fab_trap` Surface-electrode ion-trap microfabrication | Trapped ions — QCCD, laser gates, Trapped ions — electronic gates, chip control |
| `fab_pic` Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm) | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `fab_optics` Optical / mechanical assembly (lasers, vacuum, objectives) | Trapped ions — QCCD, laser gates, Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |
| `enc_spin_ld` Single-spin (Loss–DiVincenzo) / nuclear-spin encoding | Silicon / germanium quantum-dot spins, Donor spins in silicon, Defect-spin network nodes (NV/SiV/T) |
| `ct_eo` Electro-optic drive + feed-forward electronics (RT) | Photonic — fusion-based (DV), Photonic — continuous-variable / GKP |
| `ro_imgfast` Fast (≤ 20 µs) atom-array readout | Neutral atoms — alkali (Rb/Cs), Neutral atoms — alkaline-earth (Yb/Sr), erasure-native |

**defines (node → output; every row carries a source, a date and a number)**

| Node | Output | Metric | Value | Date | Source |
|---|---|---|---|---|---|
| `transmon` | error channel | Willow mean T1 / 2Q error | 68 µs / 0.33% CZ (QEC chip) | 2024-12 | https://www.nature.com/articles/s41586-024-08449-y |
| `transmon` | error channel | correlated burst rate | ~1 per hour on 101-qubit Willow | 2024-12 | https://arxiv.org/abs/2408.13687 |
| `fluxonium` | error channel | record 2Q (CNOT, Manucharyan group) | 99.94% in 60 ns, > 99.9% over 24 days | 2024-07 | https://arxiv.org/abs/2407.15783 |
| `fluxonium` | error channel | MIT FTF CZ (RL-optimised mean) | 99.922% | 2023-09 | https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035 |
| `cavity` | error channel | cavity single-photon lifetime (Al, Yale) | 10 ms | 2013 | https://arxiv.org/abs/1302.4408 |
| `cavity` | error channel | cavity-qubit coherence (Weizmann) | T1 25.6 ms / T2 34 ms | 2023-09 | https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030336 |
| `ion` | error channel | Helios (98 q) 2Q / SPAM | 7.9×10⁻⁴ / 4.8×10⁻⁴ | 2025-11 | https://arxiv.org/abs/2511.05465 |
| `ion` | error channel | memory | > 1 hour single-qubit coherence | 2021 | https://arxiv.org/abs/2008.00251 |
| `alkali` | count with quality | atoms with coherence | 6,100 Cs atoms, T2 12.6 s (Caltech) | 2025-09 | https://arxiv.org/abs/2403.12021 |
| `alkali` | count with quality | continuous operation | > 3,000 qubits held > 2 h; 300,000 atoms/s reloaded into tweezers, 30,000 initialised qubits/s | 2025-09 | https://www.nature.com/articles/s41586-025-09596-6 |
| `alkali` | count with quality | trapped (no gates) | 11,022 Rb atoms in 18,225 metasurface tweezers | 2026-06 | https://arxiv.org/abs/2606.02715 |
| `ae_atom` | error channel | erasure conversion demonstrated | 56% of 1Q errors → erasures (Yb-171) | 2023-05 | https://arxiv.org/abs/2305.05493 |
| `ae_atom` | error channel | Yb CZ | 99.72% post-selected / 99.40% raw | 2024-11 | https://arxiv.org/abs/2411.11708 |
| `photon` | error channel | source purity / HOM (Omega) | 99.5% / 99.5% | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `photon` | error channel | QD source system efficiency | 71.2% (first above 2/3 loss threshold) | 2023-11 | https://arxiv.org/abs/2311.08347 |
| `squeezed` | error channel | on-chip GKP effective squeezing (Xanadu) | 0.62 dB vs ~9.75 dB required | 2025-06 | https://www.nature.com/articles/s41586-025-09044-5 |
| `squeezed` | error channel | on-chip raw squeezing (poled TFLN) | 1.4 dB measured (> 10 dB loss-corrected) | 2025-08 | https://arxiv.org/abs/2508.08599 |
| `qd_spin` | error channel | 2Q on 300 mm foundry wafer | 99.04–99.56% (Diraq/imec) | 2025-09 | https://www.nature.com/articles/s41586-025-09531-9 |
| `qd_spin` | count with quality | largest arrays | 18 qubits (Groove/QuTech Ge; HRL EO) | 2026-04 | https://arxiv.org/abs/2604.01063 |
| `donor` | error channel | nuclear-spin gates (range reported) | 99.5–99.99%; Bell > 99% (single 99.90(4)% CZ not isolable in the abstract) | 2025-12 | https://www.nature.com/articles/s41586-025-09827-w |
| `defect` | error channel | NV gate errors (GST) | < 0.1% [P] — press release only, no primary paper | 2025-03 | https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ |
| `majorana` | error channel | single-nanowire parity switching time | ~20 s in one wire of one tetron (not a qubit lifetime), Z only; X loop 14.5 µs (2025) | 2026-06 | https://arxiv.org/abs/2606.03884 |
| `fluxq` | count with quality | Advantage2 | 4,400+ qubits, degree 20 | 2025-05 | https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/ |
| `enc_bare` | error channel | leakage suppression | 72× (all-microwave reset), residual 6.4×10⁻⁴ after 40 cycles | 2025-12 | https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31 |
| `enc_hf` | error channel | leakage per 1Q Clifford (Helios) | 1.1×10⁻⁵ | 2025-11 | https://arxiv.org/abs/2511.05465 |
| `enc_omg` | error channel | erasure fraction (theory) | 98% of errors convertible (Yb-171) | 2022-01 | https://arxiv.org/abs/2201.03540 |
| `enc_omg` | error channel | [[4,2,2]] with erasure info | logical decay 1.9(4)× slower (unconditional decoding) | 2026-06 | https://arxiv.org/abs/2506.13724 |
| `enc_dualrail` | error channel | cavity dual-rail CZ | erasure 0.53%/gate, residual Pauli < 0.1%, 500 ns | 2026-08 | https://www.nature.com/articles/s41586-026-10822-y |
| `enc_dualrail` | error channel | transmon dual-rail | erasure 2.5×10⁻²/check, residual 6×10⁻⁴, bias 42 | 2026-04 | https://arxiv.org/abs/2604.16292 |
| `enc_cat` | error channel | bit-flip time | 44 min mean (12-cat chip, preliminary); 22 s squeezed cat | 2025-09 | https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record |
| `enc_cat` | error channel | phase-flip per CX (Ocelot) | 9.6(4)×10⁻² at n̄=2 (bit-flip 3.5(4)×10⁻³); bias > 25 under the gate, > 30 idle | 2025-02 | https://www.nature.com/articles/s41586-025-08642-7 |
| `enc_gkp` | error channel | single-mode GKP logical error | 8.1×10⁻³/round (survival 0.24×0.39) | 2026-07 | https://arxiv.org/abs/2607.06718 |
| `enc_gkp` | error channel | GKP qudit gain beyond break-even (UCSB + Google) | 1.82–1.87 | 2025-05 | https://www.nature.com/articles/s41586-025-08899-y |
| `enc_gkp` | error channel | best bosonic memory gain (GKP, Yale) | 2.27(7) | 2023-03 | https://www.nature.com/articles/s41586-023-05782-6 |
| `enc_eo` | error channel | EO 1Q error (18 qubits) | 2×10⁻⁴ mean | 2026-07 | https://arxiv.org/abs/2604.16216 |
| `enc_parity` | error channel | Z / X parity lifetimes | 12.4 ms / 14.5 µs in the quoted tuning (~9.3 ms / ~4 µs in others; the ~10³ ratio is robust, the point values are not) | 2025-07 | https://arxiv.org/abs/2507.08795 |
| `g_tc` | error channel | record CZ (tunable coupler, IQM) | 99.93% over 40 h | 2025-08 | https://arxiv.org/abs/2508.16437 |
| `g_tc` | error channel | record CZ (double-transmon coupler) | 99.90% in 48 ns | 2024-11 | https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050 |
| `g_tc` | clock (cycle time) | gate time (Willow) | ~30 ns CZ | 2024-12 | https://www.nature.com/articles/s41586-024-08449-y |
| `g_tc` | error channel | fleet EPLG (full width) | best 0.19% (ibm_boston), typical 0.37% | 2026-07 | https://www.ibm.com/quantum/blog/whats-new-q2-2026 |
| `g_cr` | error channel | CR CNOT with intrinsic static-ZZ suppression (Kandala) | 99.77(2)% in a single 180 ns pulse | 2021 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501 |
| `g_ryd` | error channel | record CZ | 99.854% raw / 99.941% loss-post-selected | 2026-04 | https://arxiv.org/abs/2604.25987 |
| `g_ryd` | clock (cycle time) | gate time | 270 ns | 2025-06 | https://arxiv.org/abs/2506.20661 |
| `g_ms` | error channel | Helios 2Q | 7.9×10⁻⁴ in ~70 µs | 2025-11 | https://arxiv.org/abs/2511.05465 |
| `g_ms` | clock (cycle time) | IonQ Forte MS duration (30-ion chain, all 435 pairs) | 550–883 µs (median 672 µs) | 2023-08 | https://arxiv.org/abs/2308.05071 |
| `g_ms` | clock (cycle time) | fastest laser gate (Schäfer et al., Oxford) | 99.8% at 1.6 µs | 2018 | https://arxiv.org/abs/1709.06952 |
| `g_elec` | error channel | record 2Q | 8.4×10⁻⁵ without ground-state cooling | 2025-10 | https://arxiv.org/abs/2510.17286 |
| `g_elec` | clock (cycle time) | gate duration | 225.8 µs (2025); ≈120 µs in 2024 (two 60 µs pulses, arXiv:2407.07694) | 2025-10 | https://arxiv.org/html/2510.17286 |
| `g_exch` | error channel | foundry CZ | 99.04–99.56% (300 mm) | 2025-09 | https://www.nature.com/articles/s41586-025-09531-9 |
| `g_exch` | error channel | EO CNOT best / mean | 9×10⁻⁴ / 3×10⁻³ | 2026-07 | https://arxiv.org/abs/2604.16216 |
| `g_exch` | clock (cycle time) | mobile-spin CZ | 98.86% in 58 ns | 2026-05 | https://www.nature.com/articles/s41586-026-10423-9 |
| `g_fusion` | error channel | fusion Bell fidelity | 99.22% | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `g_bos` | error channel | dual-rail cavity CZ | post-selected infidelity 0.029% (bound 0.12%), 500 ns | 2026-08 | https://www.nature.com/articles/s41586-026-10822-y |
| `g_bos` | error channel | cavity beam-splitter (DC-SQUID coupler) | > 99.98%, ~100 ns swaps | 2023-03 | https://arxiv.org/abs/2303.00959 |
| `g_mbq` | error channel | status | no two-qubit operation, no entanglement | 2026-06 | https://arxiv.org/abs/2606.03884 |
| `g_anneal` | clock (cycle time) | coherent quench | 3.6–27 ns | 2025-03 | https://arxiv.org/abs/2403.00910 |
| `cx_nn` | count with quality | Nighthawk | 120 q, 218 couplers, 5,000 2Q gates/circuit | 2025-11 | https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance |
| `cx_nn` | error channel | CZ crosstalk (fitted budget term, Willow d=7) | 5.5×10⁻⁴ | 2024-08 | https://arxiv.org/abs/2408.13687 |
| `cx_lr` | scaling path | long-range CZ | 99.81% over ≥ 2 mm | 2023 | https://arxiv.org/abs/2208.09460 |
| `cx_lr` | scaling path | IBM Loon | c-couplers + multilayer routing shown, no performance numbers | 2025-11 | https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance |
| `cx_qccd` | clock (cycle time) | time per full-width layer (Helios) | ~55 ms | 2025-11 | https://arxiv.org/html/2511.05465v1 |
| `cx_qccd` | scaling path | junction transport | 4 m/s, 0.013–0.03 quanta/round trip | 2022 | https://arxiv.org/abs/2206.11888 |
| `cx_qccd` | scaling path | grid-trap ion exchange | 2.5 kHz | 2024-03 | https://arxiv.org/abs/2403.00756 |
| `cx_qccd` | scaling path | two-module matter link (Universal Quantum) | 2,424 transfers/s, loss infidelity < 7×10⁻⁸ | 2023-02 | https://www.nature.com/articles/s41467-022-35285-3 |
| `cx_bus` | count with quality | independently benchmarked chain (Forte) | 30 ions, all 435 pairs | 2023-08 | https://arxiv.org/abs/2308.05071 |
| `cx_bus` | count with quality | largest claimed chain (Tempo) | 100 ions, #AQ 64 [C] — a company claim, no per-pair data | 2025-10 | https://ionq.com/quantum-systems/tempo |
| `cx_aod` | clock (cycle time) | move time | 610 µm in 1.6 ms at 99.95%; 270 µm in 400 µs at 99.8% | 2025-09 | https://arxiv.org/abs/2403.12021 |
| `cx_aod` | count with quality | zoned FT processor | 448 atoms, 256 in entangling zone | 2025-11 | https://www.nature.com/articles/s41586-025-09848-5 |
| `cx_shuttle` | scaling path | conveyor shuttling | 10 µm, 99.54%, up to 64 m/s | 2025-06 | https://www.nature.com/articles/s41565-025-01920-5 |
| `cx_shuttle` | scaling path | weight-4 parity via shuttled ancilla | 97.7% per shuttle | 2026-07 | https://www.nature.com/articles/s41586-026-10766-3 |
| `cx_switch` | error channel | best in-line switch (PsiQuantum BTO) | 100 mdB insertion; 52(12) mdB fibre-to-chip | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `cx_switch` | error channel | system-scale switch loss (Aurora) | 0.19 dB/MZI; requirement ≈ 7 mdB | 2025-01 | https://www.nature.com/articles/s41586-024-08406-9 |
| `cx_switch` | error channel | BTO phase shifter | 0.33 dB·V | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `cx_crossbar` | scaling path | control lines vs dots (no coherent qubit operation) | 23 lines for 16 dots | 2024-01 | https://www.nature.com/articles/s41565-023-01491-3 |
| `ct_rt` | scaling path | I/O wall | > 4,000 high-density RF lines per fridge | 2026 | https://bluefors.com/ |
| `ct_rt` | count with quality | largest single-fridge chip | 1,121 qubits (Condor) | 2023-12 | https://www.ibm.com/quantum/blog/quantum-roadmap-2033 |
| `ct_cryocmos` | scaling path | HRL 4 K controller sequencing QEC | ≤ 3.5 W, 366 DACs; d=5 *bit-flip-only* repetition code Λ=4.7 without room-temperature real-time electronics (arXiv Apr–May 2026, Nature Jul 2026) | 2026-07 | https://arxiv.org/abs/2604.16216 |
| `ct_cryocmos` | scaling path | IBM 14 nm at 4 K | 23 mW/qubit; 1Q 8×10⁻⁴ | 2024-02 | https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326 |
| `ct_cryocmos` | scaling path | mK CMOS next to spin qubits | ~20 nW/MHz per cell; fidelity impact 0.07% | 2025-06 | https://www.nature.com/articles/s41586-025-09157-x |
| `ct_sfq` | scaling path | SEEQC mK SFQ control | 1Q > 99%, up to 99.9% (Nature Electronics) | 2026-03 | https://www.nature.com/articles/s41928-026-01576-6 |
| `ct_sfq` | scaling path | QP-poisoning-limited SFQ MCM | 1.2% error/Clifford, 0.96% from photon-mediated QP | 2023-07 | https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310 |
| `ct_fluxdac` | scaling path | bias lines per qubits | 200 bias wires (press release 2026-01-06) vs ~300 bias lines (whitepaper 2026-01-23) for the same annealer scheme — unreconciled; fluxonium MCM at 10 mK | 2026-01 | https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf |
| `ct_laser` | count with quality | SLM array | ~12,000 sites, 6,100 atoms | 2025-09 | https://arxiv.org/abs/2403.12021 |
| `ct_laser` | scaling path | metasurface tweezers | 18,225 traps from 33 W | 2026-06 | https://arxiv.org/abs/2606.02715 |
| `ct_pic_trap` | scaling path | on-chip traps | 4 Rb atoms, 27.5 s lifetime | 2026-08 | https://www.pasqal.com/newsroom/pasqal-brings-qubit-control-on-chip/ |
| `ct_ionlaser` | scaling path | waveguide-delivered 2Q gate | > 99.3% | 2020-10 | https://www.nature.com/articles/s41586-020-2823-6 |
| `ct_ionmw` | error channel | chip-integrated microwave 1Q | 1.5×10⁻⁷ error per Clifford | 2024-12 | https://arxiv.org/abs/2412.04421 |
| `ct_ionmw` | scaling path | WISE architecture | 1,000 ions with ~200 signal sources (design) | 2023 | https://arxiv.org/abs/2305.12773 |
| `ct_base` | error channel | extrinsic control share of CNOT error | ~80% (HRL) | 2026-07 | https://arxiv.org/abs/2604.16216 |
| `ro_disp` | clock (cycle time) | readout pulse / fidelity (IQM) | 240 ns pulse (≈280 ns full window) / 99.94% simultaneous assignment; QNDness 99.3% | 2025-09 | https://arxiv.org/abs/2508.16437 |
| `ro_disp` | error channel | at-scale readout error | ~1×10⁻² (fleet) | 2025-08 | https://www.ibm.com/quantum/hardware |
| `ro_fluor` | clock (cycle time) | fastest ion readout | 11 µs at 99.931% (¹⁷¹Yb⁺, MoSi SNSPD) | 2019 | https://www.nature.com/articles/s42005-019-0195-8 |
| `ro_fluor` | error channel | Helios SPAM | 4.8×10⁻⁴ | 2025-11 | https://arxiv.org/abs/2511.05465 |
| `ro_img` | clock (cycle time) | typical mid-circuit readout | ~0.5–1 ms; 0.46% bit-flip, 0.24% loss | 2025-11 | https://www.nature.com/articles/s41586-025-09848-5 |
| `ro_img` | clock (cycle time) | fast imaging (emerging) | 17.6 µs, 99.89% discrimination, 98.8% survival — neutral ¹⁷⁴Yb, spinless (not qubit-state-resolved) | 2026-08 | https://arxiv.org/html/2605.24175 |
| `ro_s2c` | clock (cycle time) | fast readout (Oakes et al., Quantum Motion; rf single-electron box) | 99.2% in < 6 µs | 2023-02 | https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.011023 |
| `ro_s2c` | error channel | best SPAM | 99.9% (100 µs integration) | 2025-09 | https://www.nature.com/articles/s41586-025-09531-9 |
| `ro_spd` | error channel | wafer-scale median on-chip efficiency (PsiQuantum Omega, 300 mm) | 93.4% at ~2 K | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `ro_spd` | error channel | best on-chip efficiency (laboratory device) | 99.73% | 2025-10 | https://www.nature.com/articles/s41377-025-02031-5 |
| `ro_qcap` | clock (cycle time) | readout | 1% error; SNR 1 in 3.6 µs | 2025-02 | https://www.nature.com/articles/s41586-024-08445-2 |
| `ro_qcap` | clock (cycle time) | independent replication (QuTech, InSb Kitaev chain) | ~1.85 ms dwell, SNR ~1.93 | 2026-02 | https://www.nature.com/articles/s41586-025-09927-7 |
| `ro_erasure` | clock (cycle time) | transmon dual-rail check | 384 ns, false-negative ~0.8% | 2026-04 | https://arxiv.org/abs/2604.16292 |
| `ro_erasure` | clock (cycle time) | cavity dual-rail check | 1.8 µs, FP 0.51% / FN 3.7% | 2025-01 | https://www.nature.com/articles/s41534-024-00944-4 |
| `ro_erasure` | clock (cycle time) | Yb erasure detection | 20 µs (1Q) / 420 µs (2Q) | 2023-05 | https://arxiv.org/abs/2305.05493 |
| `code_surface` | error channel | Λ (Willow, d=3→7) | 2.14 ± 0.02; d=7 record 7.72×10⁻⁴/cycle (Jul 2026) | 2026-07 | https://www.nature.com/articles/s41586-026-10759-2 |
| `code_surface` | error channel | Λ (USTC 107 q, d=7) | 1.40(6) | 2025-12 | https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31 |
| `code_surface` | error channel | neutral-atom d=3→5 | 2.14(13)× in 4-round circuit | 2025-11 | https://www.nature.com/articles/s41586-025-09848-5 |
| `code_surface` | count with quality | teraquop footprint, plain patches (p=10⁻³) | ~1,500 physical/logical (800 with 1D yokes, 600 with 2D yokes) | 2023-12 | https://arxiv.org/abs/2312.04522 |
| `code_surface` | count with quality | teraquop footprint with correlated matching (p=10⁻³) | ~650 physical/logical | 2023-12 | https://arxiv.org/abs/2312.08813 |
| `code_color` | error channel | Λ₃/₅ (Google) | 1.56(4); logical Clifford 0.0027 | 2025-05 | https://www.nature.com/articles/s41586-025-09061-4 |
| `code_color` | error channel | 5-to-1 distillation on logical qubits | d=3: 95.1%→99.4%; d=5: 92.5%→98.6% | 2025-07 | https://www.nature.com/articles/s41586-025-09367-3 |
| `code_qldpc` | count with quality | gross code overhead | 288 physical for 12 logical (~24/logical) vs ~3,000 surface | 2024-03 | https://arxiv.org/abs/2308.07915 |
| `code_qldpc` | error channel | IonQ memory: 4 logical in 18 ions (reported as [[18,4,3]]) | 3.95 ± 0.68 s vs 3.3 ± 0.9 s physical (leakage post-selected) | 2026-06 | https://arxiv.org/abs/2606.06455 |
| `code_qldpc` | error channel | Zhejiang [[18,4,4]] on 32 SC qubits | 8.91%/logical/cycle (not break-even) | 2025-05 | https://arxiv.org/html/2505.09684 |
| `code_qldpc` | count with quality | RSA-2048 with qLDPC (Pinnacle) | < 100,000 physical qubits at 10⁻³, 1 µs cycle | 2026-02 | https://arxiv.org/abs/2602.11457 |
| `code_highrate` | count with quality | Helios [[80,48,4]] | 48 corrected logical qubits; logical gate error 1.0–1.2×10⁻⁴ | 2026-02 | https://arxiv.org/abs/2602.22211 |
| `code_highrate` | count with quality | Harvard tesseract [[16,6,4]] | up to 96 d=4 logical qubits active | 2025-11 | https://www.nature.com/articles/s41586-025-09848-5 |
| `code_highrate` | count with quality | Quantinuum tesseract [[16,6,4]] on ions | transversal logical Clifford group in depth-one circuits, 12 addressable logical CZ pairs | 2026-06 | https://www.nature.com/articles/s41586-026-10628-y |
| `code_erasure` | error channel | threshold with 98% erasure | 4.15% vs 0.937% | 2022-01 | https://arxiv.org/abs/2201.03540 |
| `code_erasure` | error channel | [[4,2,2]] erasure teleportation (atoms) | logical decay 1.9(4)× slower with erasure info in unconditional decoding | 2026-06 | https://arxiv.org/abs/2506.13724 |
| `code_bosonic` | error channel | repetition-cat (Ocelot) | d=3 1.75% at |α|²=1 → d=5 1.65% at |α|²=1.5 per 2.8 µs cycle — different n̄, not a distance scan | 2025-02 | https://www.nature.com/articles/s41586-025-08642-7 |
| `code_bosonic` | count with quality | LDPC-cat estimate | 758 cats → 100 logical at 10⁻⁸ (assumes 0.1% phase-flip) | 2024-01 | https://arxiv.org/abs/2401.09541 |
| `code_bosonic` | count with quality | repetition-cat estimate (Gouzien et al.) | 126,133 cats for a 256-bit elliptic-curve logarithm in 9 h | 2023-02 | https://arxiv.org/abs/2302.06639 |
| `code_fusion` | error channel | loss threshold | 2.7% per photon (boosted 6-ring); 17.4% ({7,4}-encoded resource state) | 2025-06 | https://arxiv.org/abs/2506.11975 |
| `code_aft` | clock (cycle time) | rounds per logical gate | O(d) → O(1) | 2024-06 | https://arxiv.org/abs/2406.17653 |
| `code_aft` | count with quality | Shor / P-256 on reconfigurable atoms | 10,000 atoms minimum (26,000 time-efficient); P-256 in days, RSA-2048 one to two orders longer | 2026-03 | https://arxiv.org/abs/2603.28627 |
| `code_aft` | count with quality | RSA-2048 on reconfigurable atoms (ISCA 2025) | 5.6 days on 19 M qubits at a 1 ms cycle | 2025-05 | https://arxiv.org/abs/2505.15907 |
| `code_magic` | error channel | cultivation (Google) | 0.9999(1), 8% acceptance, 40× error reduction | 2025-12 | https://arxiv.org/abs/2512.13908 |
| `code_magic` | error channel | code switching (Quantinuum) | ≤ 5.1×10⁻⁴ at 82.6% acceptance | 2025-06 | https://arxiv.org/abs/2506.14169 |
| `dec_mwpm` | clock (cycle time) | PyMatching v2 throughput | < 1 µs/round at d=17, p=0.1% | 2023-03 | https://arxiv.org/abs/2303.15933 |
| `dec_mwpm` | clock (cycle time) | Micro Blossom FPGA (ASPLOS 2025) | 0.8 µs average latency at d=13, p=0.1% | 2025-02 | https://arxiv.org/abs/2502.14787 |
| `dec_nn` | error channel | Willow d=7 with AlphaQubit2 | 7.72×10⁻⁴/cycle | 2026-07 | https://www.nature.com/articles/s41586-026-10759-2 |
| `dec_nn` | clock (cycle time) | FPGA NN decoder | 124 ns decode, 550 ns closed loop (d=3) | 2026-05 | https://arxiv.org/abs/2605.04892 |
| `dec_relaybp` | clock (cycle time) | FPGA Relay-BP | average < 1 µs per cycle at p < 3×10⁻³ (simulated syndromes) | 2025-10 | https://arxiv.org/abs/2510.21600 |
| `dec_fpga` | clock (cycle time) | Riverlane LCD | < 1 µs/round to d=17 | 2025-12 | https://www.nature.com/articles/s41467-025-66773-x |
| `dec_fpga` | clock (cycle time) | Google real-time at d=5 | 63 µs latency, Λ=2.0 | 2024-08 | https://arxiv.org/abs/2408.13687 |
| `dec_gpu` | clock (cycle time) | NVQLink RoCE round trip | 3.84 µs mean | 2025-10 | https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ |
| `dec_corr` | error channel | loss-aware ML decoding gain | 1.73(13)× | 2025-11 | https://www.nature.com/articles/s41586-025-09848-5 |
| `dec_rl` | error channel | RL-steered QEC | 20% LER cut, 3.5× stability vs drift | 2026-07 | https://arxiv.org/abs/2511.08493 |
| `dec_cryo` | clock (cycle time) | QECOOL on-line SFQ decoder (simulation) | 2.78 µW at 2 GHz | 2021-03 | https://arxiv.org/abs/2103.14209 |
| `dec_cryo` | clock (cycle time) | NISQ+ approximate SFQ decoder (design) | ≤ 20 ns latency | 2020-04 | https://arxiv.org/abs/2004.04794 |
| `dec_cryo` | scaling path | cryo-CMOS predecoder (design) | 3,780× syndrome-bandwidth reduction at < 0.56 mW | 2025-12 | https://arxiv.org/abs/2512.09807 |
| `ic_mcm` | count with quality | chiplet tiling | 108 q from 12 chiplets, median 2Q 99.1% (vs 99.5% at 36 q) | 2026-04 | https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system |
| `ic_mcm` | scaling path | coupled cryogenic cells | two cells coupled; 0.53 m² wiring area each | 2026-08 | https://www.ibm.com/quantum/blog/modular-cryogenics |
| `ic_cryolink` | error channel | 30 m link Bell fidelity / rate | 80.4% / 12.5 kHz | 2023-05 | https://www.nature.com/articles/s41586-023-05885-0 |
| `ic_cryolink` | scaling path | 2026 modular link | waveguide loss < 0.03 dB/30 m; end-to-end transfer loss 0.55–0.65 dB, i.e. 86–88% transmission | 2026-04 | https://arxiv.org/html/2604.15971v1 |
| `ic_ionphoton` | error channel | distributed CZ (Oxford) | remote Bell 96.9% at 9.7 s⁻¹; teleported CZ 86.2% | 2025-02 | https://www.nature.com/articles/s41586-024-08404-x |
| `ic_ionphoton` | clock (cycle time) | entanglement rate record | 250 s⁻¹ at F > 94% | 2024 | https://arxiv.org/abs/2404.16167 |
| `ic_atomcavity` | error channel | atom–photon efficiency (MPQ, Science 385, 179) | ~90% generation-to-detection | 2024-07 | https://arxiv.org/abs/2407.09109 |
| `ic_spinphoton` | error channel | SiV over 35 km | F = 0.69, ≤ 1 Hz | 2024-05 | https://www.nature.com/articles/s41586-024-07252-z |
| `ic_spinphoton` | error channel | NV Delft–The Hague 25 km | F = 0.534, 0.022 s⁻¹ | 2024-04 | https://arxiv.org/html/2404.03723 |
| `ic_spinphoton` | error channel | T-centre inter-cryostat link (Photonic Inc.) | Bell F = 0.60(8) at 7.5 mHz; teleported-CNOT sequence post-selected, no gate fidelity | 2024-06 | https://arxiv.org/html/2406.01704v1 |
| `ic_spinphoton` | error channel | NV unconditional teleported CNOT (QuTech) | 63(4)% (4-qubit GHZ 64(4)%), real-time feed-forward, no post-selection | 2026-05 | https://www.nature.com/articles/s41467-026-72818-6 |
| `ic_transducer` | error channel | state of the art (review) | η_int 99.5%, η_tot 15%, N_add 0.16 (EO, 60 mK) | 2026-05 | https://arxiv.org/html/2605.26976 |
| `ic_transducer` | scaling path | gap to useful | 3 orders of magnitude (noise, η, rate) for 99.7% remote gates at MHz | 2025-03 | https://arxiv.org/abs/2503.10842 |
| `ic_fibre` | error channel | chip-to-chip Bell fidelity | 99.72% over 42 m, conditional on heralded events (channel loss excluded) | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `fab_cmos` | scaling path | wafer-scale statistics | > 24,000 devices/wafer, 96% single-electron tune-up, CD < 0.5 nm | 2024-10 | https://arxiv.org/abs/2410.16583 |
| `fab_cmos` | scaling path | multi-modality foundry LOI | GlobalFoundries $375 M (SC, ion, photonic, topological, spin) | 2026-05 | https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion |
| `fab_sc` | scaling path | junction frequency targeting (ABAA) | 97.4% success, 0.9 ± 2.4% of prediction | 2024-08 | https://www.nature.com/articles/s43246-024-00596-z |
| `fab_sc` | count with quality | wafer-scale package (OQC) | > 500 qubits on one 3-inch sapphire die; T1 ~97 µs, T2e ~129 µs; no per-qubit control lines in the measured configuration | 2026-02 | https://arxiv.org/abs/2602.12773 |
| `fab_sc` | scaling path | Anderon foundry | $1 B CHIPS + $1 B IBM; SC wiring/TSV/bump; 30× device output vs 200 mm | 2026-05 | https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding |
| `fab_3d` | error channel | cavity Q (Al, Yale) | > 0.5×10⁹, single-photon lifetime 10 ms | 2013 | https://arxiv.org/abs/1302.4408 |
| `fab_trap` | scaling path | Helios trap | 1,228 electrodes, 273 independent signals (2.8 per qubit) | 2025-11 | https://arxiv.org/html/2511.05465 |
| `fab_trap` | scaling path | standard-fab traps | 99.99% 2Q on chips from standard semiconductor fabs | 2025-10 | https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing |
| `fab_pic` | error channel | SiN waveguide loss (multimode) | 0.5 dB/m | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `fab_pic` | error channel | SiN waveguide loss (single-mode) | 1.8(2) dB/m | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `fab_pic` | error channel | wafer-scale median on-chip SNSPD efficiency | 93.4% at ~2 K, 300 mm | 2025-02 | https://www.nature.com/articles/s41586-025-08820-7 |
| `fab_optics` | scaling path | system power / mass | 3 kW avg, 2,500 kg (Orion Gamma) | 2025-11 | https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf |
| `fab_optics` | scaling path | continuous reload hardware | 300,000 atoms/s reloaded into tweezers; 30,000 initialised qubits/s | 2025-09 | https://www.nature.com/articles/s41586-025-09596-6 |
| `fab_mbe` | scaling path | replication | no independent replication of the InAs–Pb stack | 2026-06 | https://www.nature.com/articles/s41586-026-10567-8 |
| `fab_stm` | count with quality | register size | 11 qubits | 2025-12 | https://www.nature.com/articles/s41586-025-09827-w |
| `fab_diamond` | scaling path | device yield | 327 devices, cooperativity > 1 | 2026-06 | https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/ |
| `g_cv` | clock (cycle time) | Aurora clock | 1 MHz, 12 modes per cycle | 2025-01 | https://www.nature.com/articles/s41586-024-08406-9 |
| `g_mwspin` | error channel | NV 1Q/2Q (GST) | < 0.1% [P] — press release only, no primary paper | 2025-03 | https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ |
| `g_catcnot` | error channel | status | no experimental bias-preserving cat–cat CNOT | 2026-07 | https://arxiv.org/abs/2607.22852 |
| `src_resource` | count with quality | largest emitter-fused graph state | 8 qubits, 0.4–2.3 coincidences/min | 2024-05 | https://www.nature.com/articles/s41586-024-07357-5 |
| `src_resource` | count with quality | independent emitter graph states (C2N Paris-Saclay) | reconfigurable 4-photon graph states from one quantum dot, ~0.5 Hz | 2025-05 | https://www.nature.com/articles/s41467-025-59693-3 |
| `ct_eo` | clock (cycle time) | single-clock-cycle feed-forward | 1 MHz (Aurora) | 2025-01 | https://www.nature.com/articles/s41586-024-08406-9 |
| `ro_imgfast` | clock (cycle time) | fast imaging | 17.6 µs, 99.89%, survival 98.8% — neutral ¹⁷⁴Yb, spinless | 2026-08 | https://arxiv.org/html/2605.24175 |

---

## 8. Sources

**Superconducting [S]**
[S1] Google Quantum AI, Willow fidelities / verifiable advantage (Oct 2025) — https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ · [S2] "Quantum error correction below the surface code threshold", Nature (2024/25) — https://www.nature.com/articles/s41586-024-08449-y · [S3] IBM Quantum hardware page — https://www.ibm.com/quantum/hardware · [S4] IBM, What's new Q2 2026 — https://www.ibm.com/quantum/blog/whats-new-q2-2026 · [S5] Zuchongzhi 3.0, PRL 134, 090601 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.090601 · [S6] Rigetti Cepheus-1-108Q GA (Apr 2026) — https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system · [S7] Toshiba double-transmon coupler, PRX 14, 041050 — https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050 ; IQM CZ 99.93% / readout 99.94% — https://arxiv.org/abs/2508.16437 · [S8] Fluxonium CNOT 99.94% in 60 ns (Manucharyan group), PRX Quantum 6, 010349 — https://arxiv.org/abs/2407.15783 ; MIT fluxonium CZ 99.922%, PRX 13, 031035 — https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035 · [S9] Google colour code, Nature (May 2025) — https://www.nature.com/articles/s41586-025-09061-4 · [S10] Magic-state cultivation — https://arxiv.org/abs/2512.13908 · [S11] Google RL-steered QEC, Nature (Jul 2026) — https://www.nature.com/articles/s41586-026-10759-2 · [S12] Zuchongzhi 3.2 below threshold, PRL (Dec 2025) — https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31 · [S13] USTC logical CNOT — https://arxiv.org/abs/2607.01473 · [S14] Zhejiang lattice surgery — https://arxiv.org/abs/2606.06598 · [S15] IBM "trusted quantum advantage" — https://www.ibm.com/quantum/blog/quantum-advantage ; https://arxiv.org/abs/2607.25941 · [S16] Relay-BP FPGA decoder — https://arxiv.org/abs/2510.21600 · [S17] IBM Nighthawk/Loon (Nov 2025) — https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance · [S18] IBM modular cryogenics (Aug 2026) — https://www.ibm.com/quantum/blog/modular-cryogenics · [S19] Fujitsu/RIKEN 256 q — https://info.archives.global.fujitsu/global/about/resources/news/press-releases/2025/0422-01.html ; 10,000-qubit plan — https://quantumcomputingreport.com/fujitsu-to-develop-10000-plus-qubit-superconducting-quantum-computer-for-2030/ · [S20] SEEQC mK SFQ control (Nature Electronics, Mar 2026) — https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ · [S21] SEEQC–IBM SFQ under QBI — https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ · [S22] Atlantic Quantum joins Google — https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/ · [S23] IBM $10 B — https://www.ibm.com/quantum/blog/10-billion-investment-faq · [S24] IQM Nasdaq listing — https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ · [S25] OQC Series C — https://oqc.tech/company/newsroom/series-c · [S26] Rigetti Q1 2026 — https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-first-quarter-2026-financial-results · [S27] Willow early access — https://quantumcomputingreport.com/google-quantum-ai-is-now-accepting-proposals-for-early-access-to-their-willow-quantum-processor/ · [S28] DARPA QBI Stage B — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection ; https://quantumcomputingreport.com/darpas-quantum-benchmarking-initiative-qbi-advances-with-eleven-teams-moving-to-stage-b/ · [S29] IBM Starling/Blue Jay — https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center ; 2023 roadmap — https://quantumcomputingreport.com/ibm-extends-roadmap-up-to-4158-qubits-using-multiprocessing-and-advanced-software/ · [S30] Rigetti 108-q update — https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-provides-update-108-qubit-system · [S31] IQM roadmap — https://iqm.tech/technology/roadmap ; https://iqm.tech/press-releases/iqm-to-deliver-world-leading-300-qubit-quantum-computer-to-finland/

**Bosonic [B]**
[B1] Alice & Bob bit-flip record — https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record · [B2] Squeezed cat — https://alice-bob.com/newsroom/squeezed-cat-qubit/ ; https://arxiv.org/abs/2502.07892 · [B3] AWS Ocelot, Nature — https://www.nature.com/articles/s41586-025-08642-7 · [B4] AWS cat–cat CNOT proposal — https://arxiv.org/abs/2607.22852 · [B5] Nord Quantique GKP SPAM — https://arxiv.org/abs/2607.06718 · [B6] GKP qudits beyond break-even, Nature — https://www.nature.com/articles/s41586-025-08899-y · [B7] Dual-rail cavity CZ, Nature (Aug 2026) — https://www.nature.com/articles/s41586-026-10822-y ; https://arxiv.org/abs/2503.10935 · [B8] AWS transmon erasure check — https://arxiv.org/abs/2604.16292 · [B9] Aqumen Seeker — https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/ · [B10] Alice & Bob Helium — https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/ ; Series B extension — https://alice-bob.com/newsroom/alice-bob-announces-series-b-extension/ · [B11] see [S28] · [B12] Nord Quantique valuation — https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment ; QBI Stage B — https://www.hpcwire.com/off-the-wire/canadas-nord-quantique-selected-for-2nd-phase-of-darpa-quantum-benchmarking-initiative/ · [B13] D-Wave acquires QCI — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ · [B14] Alice & Bob roadmap — https://alice-bob.com/roadmap.md · [B15] Nord Quantique — https://www.nordquantique.com/ · [B16] D-Wave gate-model roadmap — https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/ · [B17] Gouzien et al., cat-qubit ECC estimate — https://arxiv.org/abs/2302.06639 · [B18] LDPC-cat estimate — https://arxiv.org/abs/2401.09541

**Trapped ions [I]**
[I1] Helios — https://arxiv.org/abs/2511.05465 ; Nature (Jun 2026) — https://www.nature.com/articles/s41586-026-10676-4 · [I2] Quantinuum QV — https://www.quantinuum.com/glossary-item/quantum-volume · [I3] IonQ Forte — https://www.ionq.com/quantum-systems/forte · [I4] 99.99% electronic 2Q gate — https://arxiv.org/abs/2510.17286 · [I5] Oxford 1Q record — https://arxiv.org/abs/2412.04421 · [I6] Hour-scale memory — https://arxiv.org/abs/2008.00251 · [I7] Helios logical qubits — https://arxiv.org/abs/2602.22211 · [I8] Logical teleportation — https://www.quantinuum.com/blog/teleporting-to-new-heights · [I9] Magic states [[6,2,2]] — https://arxiv.org/abs/2506.14688 · [I10] FT QAOA/HHL — https://arxiv.org/abs/2603.04584 · [I11] IonQ qLDPC break-even — https://arxiv.org/abs/2606.06455 · [I12] H2 — https://arxiv.org/abs/2305.03828 · [I13] IonQ decoder — https://arxiv.org/abs/2608.25027 · [I14] Grid trap — https://arxiv.org/abs/2403.00756 ; junction transport — https://arxiv.org/abs/2206.11888 · [I15] Oxford distributed QC, Nature — https://www.nature.com/articles/s41586-024-08404-x · [I16] Duke/Maryland remote entanglement — https://arxiv.org/abs/2404.16167 · [I17] Tsinghua 512-ion — https://www.nature.com/articles/s41586-024-07459-0 · [I18] Honeywell/Quantinuum $600 M — https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale · [I19] Quantinuum IPO — https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering ; Q2 2026 — https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results · [I20] IonQ–Oxford Ionics — https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum · [I21] IonQ–SkyWater — https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology · [I22] Quantum Art — https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ · [I23] AQT LYNX — https://www.aqt.eu/lynx-quantum-volume-record/ ; eleQtron — https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ · [I24] Quantinuum roadmap — https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 · [I25] see [I19] · [I26] IonQ roadmap — https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality ; 2020 roadmap record — https://postquantum.com/quantum-computing-companies/ionq/

**Neutral atoms [N]**
[N1] Harvard CZ record — https://arxiv.org/abs/2604.25987 · [N2] Atom Computing Yb CZ — https://arxiv.org/abs/2411.11708 · [N3] Caltech Sr CZ — https://arxiv.org/abs/2407.20184 · [N4] QuEra Gemini — https://www.quera.com/gemini · [N5] Harvard 448-atom architecture — https://arxiv.org/abs/2506.20661 ; Nature — https://www.nature.com/articles/s41586-025-09848-5 · [N6] Caltech 6,100 atoms — https://arxiv.org/abs/2403.12021 ; https://www.caltech.edu/about/news/caltech-team-sets-record-with-6100-qubit-array · [N7] Rydberg gate review (Aug 2026) — https://arxiv.org/abs/2608.05010 · [N8] Princeton erasure conversion — https://arxiv.org/abs/2305.05493 ; Nature Physics (Jun 2026) — https://www.nature.com/articles/s41567-026-03309-0 · [N9] Caltech erasure excision — https://arxiv.org/abs/2305.03406 · [N10] Continuous operation, Nature — https://www.nature.com/articles/s41586-025-09596-6 · [N11] Tsinghua 11,000 atoms — https://arxiv.org/abs/2606.02715 · [N12] Logical magic-state distillation, Nature — https://www.nature.com/articles/s41586-025-09367-3 · [N13] Atom Computing toric code — https://arxiv.org/abs/2606.04079 · [N14] Microsoft/Atom logical qubits — https://arxiv.org/abs/2411.11822 · [N15] Infleqtion roadmap — https://infleqtion.com/infleqtion-unveils-new-architecture-to-accelerate-its-quantum-computing-roadmap-to-achieve-1000-logical-qubits-by-2030/ · [N16] Neutral-atom FT architecture study — https://arxiv.org/abs/2505.15907 · [N17] Algorithmic fault tolerance — https://arxiv.org/abs/2406.17653 · [N18] QuEra $230 M — https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing · [N19] Atom Computing $300 M+ — https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html · [N20] Infleqtion NYSE — https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ · [N21] Pasqal SPAC — https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ · [N22] Magne — https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ ; https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ · [N23] Google neutral-atom track — https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/ · [N24] QuEra Libra — https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws ; 2024 roadmap — https://quantumzeitgeist.com/quera-computing-roadmap-100-logical-qubits/ · [N25] Pasqal roadmap 2025 — https://www.pasqal.com/newsroom/pasqal-releases-2025-roadmap/ ; 2024 — https://www.hpcwire.com/2024/03/13/pasqal-issues-roadmap-to-10000-qubits-in-2026-and-fault-tolerance-in-2028/

**Photonic [P]**
[P1] PsiQuantum Omega, Nature — https://www.nature.com/articles/s41586-025-08820-7 · [P2] USTC quantum-dot source — https://arxiv.org/abs/2311.08347 · [P3] Xanadu packaging — https://www.prnewswire.com/news-releases/xanadu-sets-new-industry-benchmark-in-photonic-chip-packaging-302796562.html · [P4] Aurora, Nature — https://www.nature.com/articles/s41586-024-08406-9 · [P5] On-chip GKP, Nature — https://www.nature.com/articles/s41586-025-09044-5 · [P6] Jiuzhang 4.0 — https://arxiv.org/abs/2508.09092 ; Nature — https://www.nature.com/articles/s41586-026-10523-6 · [P7] Quandela Lucy — https://www.quandela.com/about-us/newsroom/quandela-delivers-lucy-the-most-advanced-photonic-quantum-computer-worldwide-to-eurohpc-and-genci-at-ceas-tgcc/ · [P8] QuiX Carina — https://www.quixquantum.com/news/quix-quantum-delivers-carina-core-hardware-platformto-dlr-qci · [P9] Xanadu roadmap (31 Aug 2026) — https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html · [P10] FBQC thresholds — https://www.nature.com/articles/s41467-023-36493-1 ; loss-tolerant schemes — https://arxiv.org/abs/2506.11975 · [P11] PsiQuantum newsroom (Series E, CEO change, Griffith lab) — https://www.psiquantum.com/news-import · [P12] PsiQuantum DARPA Stage C — https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/ · [P13] Brisbane site — https://www.forbes.com.au/news/innovation/psiquantums-stalled-quantum-plant-to-break-ground-after-location-switch/ · [P14] Xanadu listing — https://quantumcomputingreport.com/xanadu-to-list-on-nasdaq-and-tsx-following-shareholder-merger-approval/ · [P15] Photonic Inc — https://quantumcomputingreport.com/photonic-inc-reaches-2b-valuation-with-200m-final-close/ · [P16] Quandela QBI Stage A — https://thequantuminsider.com/2026/06/16/darpa-selects-quandela-for-stage-a-of-the-quantum-benchmarking-initiative/

**Spin and defect qubits [Q]**
[Q1] Diraq/imec 300 mm, Nature — https://www.nature.com/articles/s41586-025-09531-9 · [Q2] HRL self-sequenced QPU — https://arxiv.org/abs/2604.16216 ; https://www.hrl.com/news/2026/07/29/hrl-demonstrates-a-silicon-quantum-processor-that-runs-itself · [Q3] SQC donor qubits — https://arxiv.org/abs/2506.03567 · [Q4] Delft mobile-spin CZ, Nature — https://www.nature.com/articles/s41586-026-10423-9 · [Q5] Diraq 1 K operation, Nature — https://www.nature.com/articles/s41586-024-07160-2 · [Q6] Groove/QuTech 18-qubit Ge — https://arxiv.org/abs/2604.01063 ; conveyor shuttling — https://www.nature.com/articles/s41565-025-01920-5 · [Q7] imec 8-qubit — https://www.nature.com/articles/s41467-026-74597-6 · [Q8] SUSTech donor [[4,2,2]] — https://www.nature.com/articles/s41565-026-02140-1 · [Q9] Intel 300 mm statistics — https://arxiv.org/abs/2410.16583 · [Q10] Quantum Motion NQCC — https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ · [Q11] UNSW mK cryo-CMOS — https://www.unsw.edu.au/newsroom/news/2025/06/unsw-engineers-crack-challenge-scaling-quantum-computers · [Q12] IBM acquires HRL — https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum · [Q13] Fujitsu/QuTech NV gates — https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/ ; Harvard SiV 35 km — https://www.nature.com/articles/s41586-024-07252-z · [Q14] Diraq roadmap — https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip ; July release — https://thequantuminsider.com/2026/07/09/diraq-demonstrates-scaled-foundry-fabricated-silicon-based-qubit-array-made-at-imec/

**Topological [T]**
[T1] Microsoft parity readout, Nature (Feb 2025) — https://www.nature.com/articles/s41586-024-08445-2 · [T2] APS Physics coverage — https://physics.aps.org/articles/v18/57 · [T3] Tetron Z/X lifetimes — https://arxiv.org/abs/2507.08795 · [T4] "Majorana 2" — https://arxiv.org/abs/2606.03884 · [T5] Microsoft blog — https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor · [T6] QuTech Kitaev-chain parity readout, Nature — https://www.nature.com/articles/s41586-025-09927-7 · [T7] QuTech coherent parity qubit — https://arxiv.org/abs/2607.09511 · [T8] Legg critique — https://arxiv.org/abs/2503.08944 ; Matters Arising — https://www.nature.com/articles/s41586-026-10567-8 ; Microsoft reply — https://www.nature.com/articles/s41586-026-10568-7 · [T9] DARPA US2QC — https://www.darpa.mil/news/2025/quantum-computing-approaches

**Annealing / analog [A]**
[A1] Advantage2 GA — https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/ · [A2] D-Wave beyond-classical — https://arxiv.org/abs/2403.00910 ; Tindall et al. — https://arxiv.org/abs/2503.05693 ; Mauron & Carleo — https://arxiv.org/abs/2503.08247 · [A3] D-Wave rebuttal — https://arxiv.org/abs/2508.15759 · [A4] D-Wave Q2 2026 — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ ; FY2025 — https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-fourth-quarter-and-year-end-2025-results/ · [A5] Google analog-digital simulator, Nature — https://www.nature.com/articles/s41586-024-08460-3 · [A6] QuEra Aquila string breaking, Nature — https://www.nature.com/articles/s41586-025-09051-6 · [A7] Quantinuum digital magnetism — https://arxiv.org/abs/2503.20870

**Cross-cutting [X]**
[X1] Gidney, RSA-2048 with <1 M qubits (May 2025) — https://arxiv.org/abs/2505.15917 · [X2] Microsoft resource-estimation model (ns vs µs gates) — https://arxiv.org/abs/2211.07629 · [X3] P450 estimate — https://arxiv.org/abs/2202.01244 ; FeMoco THC — https://arxiv.org/abs/2011.03494 · [X4] Hubbard estimates — https://arxiv.org/abs/1902.10673 · [X5] Litinski ECC-256 — https://arxiv.org/abs/2306.08585 · [X6] Optimization speedups (Babbush et al.) — https://arxiv.org/abs/2011.04149 ; DQI — https://arxiv.org/abs/2408.08292 · [X7] Google OTOC "Quantum Echoes", Nature — https://www.nature.com/articles/s41586-025-09526-6 ; certified randomness, Nature — https://www.nature.com/articles/s41586-025-08737-1 ; Q-CTRL — https://arxiv.org/abs/2605.04025 ; Qedma cross-platform — https://arxiv.org/abs/2607.24937 · [X8] Erasure-conversion threshold (Wu et al.) — https://arxiv.org/abs/2201.03540 · [X9] Riverlane FPGA decoder, Nat. Commun. — https://www.nature.com/articles/s41467-025-66773-x ; IQM real-time QEC — https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/ · [X10] UK NQCC testbeds — https://www.nqcc.ac.uk/quantum-computing-testbeds-in-the-uk/



[S32] IBM roadmap page (Kookaburra 2026, not delivered as of Sep 2026) — https://www.ibm.com/roadmaps/quantum/ ; IBM hardware metrics (Nighthawk r2 expected) — https://www.ibm.com/quantum/blog/hardware-metrics-2026 ; Zhejiang [[18,4,4]] BB code — https://arxiv.org/html/2505.09684 · [S33] Google RL-controlled QEC, arXiv version — https://arxiv.org/abs/2511.08493 ; Google neutral-atom track — https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ · [S34] Fujitsu quantum research page (1,000-qubit machine, fiscal 2026) — https://global.fujitsu/en-global/technology/research/quantum ; 10,000-qubit programme — https://global.fujitsu/en-global/pr/news/2025/08/01-01-en · [I27] IonQ Forte benchmarking (gate durations) — https://arxiv.org/abs/2308.05071 ; Tempo page — https://ionq.com/quantum-systems/tempo · [N26] planqc news — https://planqc.eu/news ; profile — https://postquantum.com/quantum-computing-companies/planqc/ · [Q15] Argonne–Intel 12-qubit deployment — https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel · [X11] Google ECDLP-256 estimate — https://arxiv.org/abs/2603.28846 · [X12] Iceberg Quantum Pinnacle architecture — https://arxiv.org/abs/2602.11457 · [X13] Shor with ~10,000 reconfigurable atoms — https://arxiv.org/abs/2603.28627 ; neutral-atom RSA-2048 architecture — https://arxiv.org/abs/2505.15907 · [X14] DARPA QBI Stage A page ('17 of 18 announced') — https://www.darpa.mil/news/2025/companies-targeting-quantum-computers ; QBIT Stage A — https://www.darpa.mil/news/2026/qbi-stage-a-qbit ; QBI Q&A (stage durations) — https://www.darpa.mil/sites/default/files/attachment/2025-04/darpa-qbi-q-a-2025.pdf

**Technology-graph sources (§7)** — every 'defines' row in §7.10 carries its own URL; the graph JSON (`graph.json`) is the machine-readable source list.

*End of English edition.*
