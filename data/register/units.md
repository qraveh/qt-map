# The units of a machine type — `units_built`, `units_in_service`, `units_evidence` (the register's fields since 6 Nov 2026)

The editor's decision D5 of 6 Nov 2026 (`00_admin/handoffs/GRILL_20261106_atlas-update-and-architecture-course.md`): the register counts the
physical instances of each built machine type beside the type's row.

- **Unit.** One physically separate machine with a named backend (a cloud name such as `ibm_fez`, `Advantage2_system4`) or a named site
  (Cleveland Clinic, PSNC Poznań). A chip design, a processor family or a cloud route is not a unit; two cloud routes to one machine are one unit.
- **`units_built`.** The number of units built, as far as the sources show: an integer when the sources name every unit, "≥N" when they name
  N and the owner says or implies more (a lower bound, never an estimate). Retired units count — the field is a history, not a fleet.
- **`units_in_service`.** The units in operation at the field's date (cloud backends online or paused for maintenance; on-premises systems
  reported operating); "≥N" when only N are confirmed; "0" when every unit is retired; "?" when the sources say nothing.
- **Ordered, not delivered.** A unit sold, ordered, delivered-but-not-assembled or scheduled is **not** counted in either field; it is named
  in `units_evidence` with its date, so that the next count can move it.
- **`units_evidence`.** The URLs and the verbatim words the count rests on, one unit or one list per source; "the register's row: one
  machine" for a type whose only unit is the row itself (a laboratory or national system with nothing suggesting a second).
- **Scope.** Built types only (DEPLOYED, DEMONSTRATED, RETIRED): 133 rows at `main` 820ed57; PLANNED, ANNOUNCED and CONTESTED rows have no units yet.
  Three installation rows are folded into their types (fraunhofer-ehningen → ibm-falcon; basq-system-two → ibm-heron-r2; it4i-vlq → iqm-star-24).
- **Date.** The count of 6 Nov 2026 (three Opus agents in the cloud) with the memory-sourced items re-read at the owners' pages on 6 Nov 2026
  by the local session (`handoffs/HANDOFF_20261106_T1-research_rev1_local.md`): IBM's retired and live lists, IBM's and the customers'
  releases for the on-premises systems, Quantinuum's Reimei release, IonQ's systems and Aria pages, Google's Cirq devices, D-Wave's solver
  page, ORCA's, AQT's, OQC's, Pasqal's and SaxonQ's news pages. What those pages do not show is not counted; the count's memory items that
  they contradict are named in the `note` column and, where they touch a register cell, in the change ledger as `doubt` items.
