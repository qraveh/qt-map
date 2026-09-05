# Quantum Technology Map

**Edition 2026.09** · published at [qodeh.com/qt-map](https://qodeh.com/qt-map) · archived on Zenodo, DOI [10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX) · CC BY 4.0 · bilingual EN / RU

Every quantum-computing platform compared by the goal it serves; a technology graph of 96 self-contained technologies across ten stack layers, seven design coordinates and five edge types; a brief on each technology; every figure tagged and traced to a dated source. This repository holds the data, the briefs and the build that renders the single interactive document.

## About the map — the five questions

**Why a Quantum Technology Map.** Quantum computing has no universally best technology, because it has no single goal. Every platform presents a computation with an error channel, a clock (its error-correction cycle time), a qubit count and a scaling path, and every goal weighs the four differently: a cryptanalytic machine is a fast clock on ~10³ logical qubits; a lattice-gauge simulator wants many qubits, rich connectivity and high-dimensional local degrees of freedom, and tolerates a slow clock; a network node cannot be built from superconducting qubits at all — the only carrier that leaves the cryostat is a photon. Comparisons are nevertheless made at the level of *platforms* — superconducting versus ions versus atoms — although a platform is an assembly of separable technologies, and the decisions that matter (what to research, what to build, whom to partner with, what to buy) are made one technology at a time. The material that exists today comes in three kinds, each blind in its own way: vendor roadmaps (intentions, not results), market monitors (money, not physics) and academic reviews (physics, not economics, and dated on arrival). The map exists so that every technology in the quantum-computing stack can be read on the same coordinates, against dated evidence, with its conflicts and its economics in one place — and so that the picture is refreshed several times a year rather than once.

**What it is.** A living reference in four connected parts. A goal-oriented comparison of platforms: a criteria set that is technology-agnostic by construction, every major platform graded separately on *demonstrated* results and on *justified* intentions, platforms mapped to goals — and only then the directions that look most promising. A technology graph: 96 self-contained technologies across ten stack layers, each placed on seven design coordinates and connected by five kinds of edge, with platforms drawn as paths through the layers. A brief on every technology, with the same section skeleton from physics to economics. And an evidence system: every claim tagged by its standing, every figure traced to a dated, linked source, conflicts stated rather than averaged, open verification items listed. It is published as one interactive document in dated editions (2026.09), each archived with its own DOI — the concept DOI resolves to the latest; the data and the build live on GitHub.

**Who should use it.** Researchers choosing where to put the next years of work — the graph shows hubs, empty slots and unresolved conflicts, which is where leverage is. Architects and engineers designing a system — a platform is a path through the layers, and every station on it comes with what it requires, what it can be swapped for, and what it collides with, priced. Investors and analysts — each brief carries the actors, the dated money, the supply chain and the roadmap-versus-delivery record of one technology, not of a company. Programme and policy staff — who is where, which suppliers are single points of failure, which export rules apply. Newcomers — the map is a structured entry into a field whose literature is not. Vendors — to see how their claims read when tagged and dated. It is not a market-sizing exercise and not a ranking of companies.

**What makes an entry.** A technology becomes a node of the graph if it is *self-contained* — it can be replaced without redesigning the rest of the stack; *principled* — it rests on a distinct physical or mathematical mechanism, not on a product, a vendor or a parameter choice; and it belongs to exactly one layer. It must be locatable on all seven coordinates: carrier affinity (natural ↔ fabricated), characteristic time and deterministic or heralded entangling, readout mechanism with its time, destructiveness and mid-circuit capability, mobility and connectivity, control modality and placement, dominant error structure as an error-correcting code sees it, and manufacturing technology. A demonstrated node needs at least one dated, sourced record; emerging or theoretical nodes are admitted when a platform path needs the slot, and slots with no technology at all are drawn as empty. Platforms, companies and devices are never nodes: platforms are paths, companies are actors, devices are records. Every node carries its coordinates (design space, stable), its dated records (evaluation space), its actors and goals (annotation space), its edges, and its brief.

**How it is organised.** Ten layers run left to right — carrier, encoding, gate mechanism, connectivity and transport, control, readout, code, decoder, interconnect, manufacturing; the vertical position is carrier affinity, natural at the top and fabricated at the bottom, so the natural/fabricated diagonal is visible and every technology that breaks it is hatched. Stations are technologies; coloured lines are platform paths through one station per layer; a station on several lines is a transfer hub. Five edge types connect stations: *requires/provides* between layers; *alternatives* within a layer; *conflicts*, each with its mechanism, its measured price, its mitigation and a status; *transfers*, derived from the paths; *defines*, dated records with sources. Lenses recolour every station by one coordinate, and the legend doubles as a filter. Hubs, off-diagonal technologies, empty slots and each path's clock are derived from the data, not asserted. The briefs follow one skeleton — identity and lineage, physics and limits, engineering state of the art, manufacturing and supply chain, role in the stack, verification, actors and economics, outlook, sources, open items — at a depth set by the technology's importance in the graph.

## Repository layout

| Path | What it is |
|---|---|
| `data/graph_data.py` | **Source of truth for the graph**: layers, coordinate vocabularies, 96 nodes (coordinates, bilingual descriptions, dated `defines` records with sources), 14 platform paths, edges (requires / alternatives / conflicts with mechanism–price–mitigation–status), derivations (transfers, hubs, off-diagonal, empty slots, derived clock, validity check). Running it writes `data/graph.json`. |
| `data/graph.json` | Generated machine-readable graph (nodes, edges, paths, vocabularies, validity). Use this if you build on the data. |
| `data/records.json` | **Standard records** — dated, sourced numbers per node (T1/T2, 1Q gate time, reset, SPAM, feed-forward latency, syndrome-circuit depth, code rate, acceptance, decode latency, transport per layer, yield, spread…); nulls mark quantities that are not published. Feeds the derived clocks (syndrome round, reaction time, operations per coherence). |
| `data/ranking.json` | Importance score, rank and depth tier of every node (drives brief depth). |
| `data/facts.json` | Shared dated facts (funding, programmes, M&A, key device facts) behind the linked `[G]` chips in the briefs. |
| `briefs/en/*.md`, `briefs/ru/*.md` | One brief per technology, YAML front matter + fixed section skeleton; Russian mirrors English section by section. |
| `report/report_EN.md`, `report/report_RU.md` | The main report (§0–§8). §7 (the graph section) is **generated** from `data/graph_data.py` by the build — edit the graph, not §7. |
| `build/` | Build scripts (Python 3.11+, `markdown` package) and the vendored D3 v7 (ISC licence). `python3 build/build.py` regenerates everything into `dist/`. |
| `dist/` | The single self-contained HTML document of the current edition (the release artefact). |
| `CHANGELOG.md` | Editions (generated from `build/editions.py`). |

## Build

```bash
pip install markdown
python3 build/build.py          # → data/graph.json, report §7, dist/Quantum-Technology-Map-<edition>.html, CHANGELOG.md
```

The document is one HTML file with no runtime dependencies except Google Fonts (optional; system fonts are the fallback). Open `dist/…html` locally or publish it as-is.

## Editions and citation

Editions use calendar versioning (`YYYY.MM`, `.N` for a re-issue within the month) and are cut when the graph changes structurally, a verdict changes or a headline number is corrected — otherwise roughly quarterly (3–6 per year). Each edition is a git tag and a Zenodo version with its own DOI; the concept DOI always resolves to the newest edition. Cite the edition you read:

> Neeman, R. (2026). *Quantum Technology Map* (Edition 2026.09). Qodeh. https://doi.org/10.5281/zenodo.XXXXXXX

A `CITATION.cff` is included for GitHub's "Cite this repository" and for reference managers.

## Contributing

Corrections and new dated records are welcome as issues or pull requests. What is open to contribution: records (a new result with its date and primary source), source corrections, actor and money facts, translations. What stays editorial: node admission, coordinates, edges and their prices, verdicts — propose them in an issue with evidence; the rules are stated in the About section and in §7.1 of the report. Every number needs a dated primary source; every claim gets an evidence tag (`[D]` measured / peer-reviewed · `[C]` company claim · `[R]` roadmap · `[S]` simulation or estimate · `[G]` established fact · `[P]` preprint or trade press). Preview your change by running the build; the HTML in `dist/` is the review artefact.

## Licence

Content (report, graph data, briefs, the rendered document): [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) — see `LICENSE`. Build scripts in `build/`: MIT — see `LICENSE-CODE`. Vendored D3: ISC (`build/vendor/D3-LICENSE`). Quoted figures remain the property of their cited sources.

## Provenance

Research and drafting with Claude (Anthropic) under the author's direction and review; every figure traces to a dated, linked primary source; conflicts between sources are stated, not averaged; open verification items are listed at the end of each brief.
