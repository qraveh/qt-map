# The intake run — how the Atlas takes the digest's news

The digest (qnews, on the editor's laptop) delivers an issue every second day and then writes its proposals into
`C:\MyDrive\QT-Map\qnews-intake\` (papers: technology records, gaps, station amendments, works; the industry stream since
6 Oct 2026: one field of one register machine, a new machine, an organisation event — each with the owner's own words and
a source class A owner feed · B SEC filing · C catalogue page · D press). This runbook is what a cloud session does with
them, unattended, once a day. Policy: `build/intake.py` (`python3 build/intake.py status --rules`). Ledger:
`data/intake/decisions.json` — every proposal gets exactly one final decision, so a row is never read twice.

The run is a C session (core). It never opens E material, never pushes, never asks a question (nobody is watching): it
takes the conservative reading, says which in its report, and stops at anything that is the editor's. No browser or
desktop-control tools (any tool whose name contains `computer_`, `Claude_Browser` or `claude-in-chrome`): a sleeping
laptop wedges them. No call blocks over ~2 min; the build runs in the background.

## 1. Is there anything to do? (≤ 2 min)

```
cd /home/claude && git clone --filter=blob:none https://github.com/qraveh/qt-map.git && cd qt-map
pip install -q -r requirements.txt
python3 build/intake.py status          # decided so far; the last run's manifest_updated is in data/intake/decisions.json `runs`
```
Through the device bridge (`device_bash`, folders `C:\MyDrive\QT-Map` and `C:\Users\raveh\Downloads`):
- `qnews-intake/landed-manifest.json` → its `updated`;
- `00_admin/HANDOFF.md` → the cloud's open ticket, if any;
- `00_admin/intake/decisions/*.json` → the editor's answers that sessions wrote since the last run (a file is consumed
  once: after recording, rename it to `*.json.recorded` with `mv`).

Stop with a one-line report («intake: nothing new since <updated>») when the manifest's `updated` equals the last run's
and there is no new decisions file. If the cloud's open ticket is not an intake ticket (a core session's work is waiting
for the local side), do steps 2–4 only, write the packet (§6) and stop: the next run applies.

## 2. Bring the intake in

`device_stage_files` the seven data files of `qnews-intake/data/` (`register-amendment-candidates.csv`,
`machine-candidates.csv`, `org-event-candidates.csv`, `amendment-candidates.csv`, `map-gaps-candidates.csv`,
`records-candidates.csv`, `works-candidates.csv`) → `/mnt/user-data/uploads/QT-Map/qnews-intake/data/`. Never edit
the intake: qnews owns it and stops writing on a foreign edit.

If an intake ticket of an earlier run is still open, stage its bundle from Downloads, `git fetch <bundle> <branch>`,
check out that branch and continue on it: the new ticket supersedes it (rev + 1), so there is one intake ticket at a time.

```
python3 build/intake.py decide --from <each new decisions file> --intake <dir>     # the editor's answers first
python3 build/intake.py triage --intake <dir> --out $SP/intake-<date>             # triage.json, verify.json, packet.md
```

## 3. Verify at the source (the budget: 25 fetches; the rest wait for the next run)

For each entry of `verify.json`, open its `url` with WebFetch, asking for the verbatim passage that contains the quote
(its numbers and the product name). The quote must be there in substance — same numbers, same subject. Class C pages are
catalogue pages: the table row is the quote. SEC filings: the EDGAR document. Routing per the cloud manual §6
(arXiv abs pages, not the API; one try at nature.com / aps.org, then the arXiv version). Write `verified.json`:
`[{row_key, url, quote_found: true|false, checked: <date>, note}]` — `note` says what the page shows when the quote is
absent. A row you could not fetch is left out (it stays undecided), never marked false.

## 4. Plan and apply what is the run's to apply

```
python3 build/intake.py plan --triage $SP/intake-<date>/triage.json --verified $SP/intake-<date>/verified.json --out $SP/intake-<date>
```
`plan.json` holds the register patch, the change-ledger items, the decisions, and `manual` (approved rows a session writes
by hand). Before applying the register patch, write each `text_twin` (the register's prose column beside a number:
`physical_qubits` beside `physical_qubits_num`) in the register's style — «36 (IonQ systems page, Oct 2026)» — into the
same row's `fields`. Then:
```
python3 build/register_patch.py $SP/intake-<date>/register_patch.json      # data/register/, idempotent
# append plan.json `change_items` to data/changes/<date>.json (create it with date and source "digest intake <issues>")
python3 build/intake.py record --plan $SP/intake-<date>/plan.json --manifest-updated <updated> --ticket <ticket>
python3 build/machines_json.py && python3 build/audit/edges_check.py && python3 build/audit/records_check.py \
  && python3 build/audit/machines_json_check.py && python3 build/audit/propagate.py --check && python3 build/intake.py check
(nohup python3 build/build.py > $SP/build.log 2>&1 &)    # 3–4 min; poll with sleep ≤ 110
python3 build/audit/text_lint.py && python3 build/audit/links_check.py --records
```
`manual` rows (approved new machines, technologies, technology descriptors) are written only when the run has the budget
for the full job (a new machine: cells per layer with evidence, references, the organisation — cloud manual §5.2);
otherwise they stay approved-and-pending and the report says so. If `propagate --check` names hand-written text that
mentions a changed subject (a brief that calls a retired machine current), fix it in English, Russian and Hebrew in the
same commit, or revert that row and record it `deferred` with `until: core session`.

Nothing applied → skip to §6.

## 5. Hand over

Commit as the editor (`git -c user.name="Raveh Neeman" -c user.email="raveh@qodeh.com" commit`, the subject «intake
<date>: …», the trailers), then the cloud manual §7: `build/audit/handoff.py --ticket <YYYYMMDD-N> --out $SP/ho --note
handoffs/HANDOFF_<date>_intake.md`, the bundle to Downloads with `device_commit_files`, the note and its ACCEPTANCE block,
the ticket row in `HANDOFF.md` (one line: «intake <date>: N register changes, M organisation events, K records — from
digest issues …»), the `channel/cloud.md` entry (newest first). The class of an intake ticket is `data`; it carries no
generator or UI change, so the local side's checks are the data row of the matrix.

## 6. Report

The editor's packet: `packet.md` of the triage, with the plan's outcome on top (applied rows with their Atlas links, the
deferred ones with the reason). Create it as a Google Doc «Atlas intake <date>» in `QT-Map/00_admin/intake/` (Drive
connector, `text/markdown`, converted), and write the same markdown to `00_admin/intake/PACKET_<date>.md` through the
bridge. The run's final message — what reaches the editor's phone — in plain words: what changed in the Atlas (one line
per machine or organisation), what is his to decide (count, and the doc's name), what waits (holds for WP2, the weekly
brief notes), the ticket for the local side. Answers he gives in any session are written by that session as
`00_admin/intake/decisions/<date>-<n>.json` (`[{row_key, decision: approved|rejected|deferred, reason, until}]`) and
taken by the next run.
