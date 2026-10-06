# `machine-codes.csv` — the machine × code table

One row per machine and quantum error-correcting code: the codes that have been run on the machine, and the codes its builder has designated for it. The key is (`machine_id`, `code_id`). Revised on 7 Oct 2026 by a machine-by-machine sweep against the primary sources; the sweep's full record, including the machines checked and found to have no code, is `30_working/QEC-SWEEP_2026-10-07.csv` in the QT-Map programme folder.

| Field | Meaning |
|---|---|
| `machine_id` | the machine's id in `machines.csv` |
| `code_id` | the code's id in the codes register (`qec-codes/data/qec-codes.csv` → `id`; the Error Correction Zoo id where the zoo has the code) |
| `status` | the code's state in the codes register: `in stage-1 register` for every row |
| `best_instance` | the most significant instance on this machine: parameters [[n,k,d]], distance, rounds, logical error or Λ, post-selection |
| `decoder` | the decoder as published, and whether it ran in real time or offline |
| `ref` | the register's source key (as in `machines.csv` → `refs`) for rows confirmed unchanged; empty otherwise — the source of every row is `url` |
| `use` | `demonstrated` — a published experiment encoded quantum information in the code on a device of this machine and measured its checks or verified the encoded state (third-party experiments over cloud access count); `planned` — the builder's own published architecture or roadmap designates the code for this machine. A builder's simulation study that does not name the machine is not a designation |
| `scope` | what was shown, `;`-separated: `prep` logical state prepared and verified (or a code state prepared as a many-body state, said in `note`) · `detect` error detection with post-selection · `memory` repeated syndrome cycles with decoding · `logic` logical gates, teleportation or lattice surgery between encoded qubits · `magic` magic-state preparation, distillation or cultivation in the code · `algo` an algorithm run on encoded qubits · `planned` for a designation |
| `device` | the chip, backend or system that ran it (`;`-separated); one machine's devices may run different codes |
| `by` | `builder` · `builder: <group>` · `builder with partners: <groups>` · `third party: <group>` |
| `year` | year of the first publication of the code on this machine |
| `url` | one primary source (arXiv abstract preferred) |
| `checked` | `yes` — the source was read and names the device and the code · `partial` — read, but the device or the code's variant is inferred (how, in `note`) · `no` — not re-read in the sweep |
| `note` | provenance, device mapping, caveats; further instances of the same code on the machine as `also <year>: …` |

A concatenated code is one row when a code id names the composite (`cat_repetition` for cats under a repetition code); its layers get rows of their own only when a layer was also run alone. The photon's native dual-rail qubit is the carrier encoding of a photonic machine, not a code row.
