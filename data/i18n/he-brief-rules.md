# Translating a technology brief into Hebrew — the rules (29 Sep 2026)

Source: `briefs/en/<id>.md`. Target: `briefs/he/<id>.md` (create the folder if needed). The Russian twin `briefs/ru/<id>.md`
shows how a translation mirrors the English file; the terminology is `data/i18n/he-terms.md` (binding; report the terms you coin).

1. **Front matter** (between the `---` lines): keep every key and its order; translate the VALUES of `name`, `layer` (keep the
   layer number, translate the word: `1 Carrier` → `1 נושא הקיוביט`; the ten layer names are in `data/i18n/graph_he.json` → `layers`),
   `one_line`, `verdict`; leave `id`, `status`, `since`, `updated` exactly as they are.
2. **Section headings** — the eleven `## …` headings become exactly these Hebrew names, in the same order as the English:
   `## זהות ומוצא` (Identity & lineage) · `## פיזיקה וגבולות` (Physics & limits) · `## מצב ההנדסה העדכני` (Engineering state of the art) ·
   `## ייצור, חומרים ושרשרת האספקה` (Manufacturing, materials & supply chain) · `## בקרה, קריאה ועומס הקלט-פלט` (Control, readout & I/O burden) ·
   `## תפקיד במחסנית` (Role in the stack) · `## ראיות — כיצד נמדדו המספרים` (Evidence — how the numbers were measured) ·
   `## שחקנים וכלכלה` (Actors & economics) · `## תחזית ושאלות פתוחות` (Outlook & open questions) · `## מקורות` (References) ·
   `## פריטי אימות פתוחים` (Open verification items). A brief that lacks one of these sections keeps lacking it.
3. **The References section** (`## References` → `## מקורות`): its content is DATA — copy every line of it from the English file byte
   for byte (the numbered IEEE entries `[282] …`, the grade tags, the blank lines). Do not translate, reorder or renumber anything there.
4. **Everything else is translated** — the body prose, list items, table cells (keep the pipes and the `|---|` lines; the column headings
   translate), the "Attributes (technology graph):" block (its lines `- a: …` … `- g: …`), the Open verification items, the bold
   run-in labels (`**The idea.**` style); the standing marks `[D] [C] [P] [R] [S] [G]`, the citation numbers `[282]`, `[G:KEY]` tags,
   `§7.3`/`§8.3.4` references, ids in backticks, product/machine/organisation names, URLs, formulas, numbers, units (µs, mK, GHz, dB),
   dates in ISO form (2026-09-03), arrows and symbols stay exactly. Dates written in words become Hebrew (26 בספטמבר 2026).
5. **Structure mirrors the English one to one**: the same number of paragraphs, list items, table rows and headings, in the same
   order (the site keeps the reader's place across a language switch by paragraph rank; the checks count them).
6. **Voice**: formal written Hebrew of a scientific review; short declarative sentences; no marketing; the same term always the
   same word; Hebrew is right-to-left — write naturally, no bidi control characters, no transliteration of Latin names.
7. **Write with Python** (UTF-8, LF), file by file; after each file run this check and fix what it reports:

```python
import re, sys
def counts(t):
    L = t.split('\n')
    return (sum(1 for l in L if l.startswith('#')), sum(1 for l in L if l.startswith('|')), sum(1 for l in L if re.match(r'\s*[-*] ', l)),
            sorted(re.findall(r'\[(?:[A-Z]{1,2}\d{1,3}|\d{1,4}|[DCRSPG]|G:[A-Z0-9\-]+)\]', t)))
en = open('briefs/en/ID.md', encoding='utf-8').read(); he = open('briefs/he/ID.md', encoding='utf-8').read()
assert counts(en) == counts(he), 'structure or citations differ'
assert not re.search(r'[А-Яа-яЁё]', he), 'Cyrillic'
sec = lambda t, h: t.split('\n' + h + '\n', 1)[1].split('\n## ')[0]
assert sec(en, '## References') == sec(he, '## מקורות'), 'References not identical'
```
8. At the end run `cd /home/claude/qt-map && python3 build/brief_refs.py --check` — it must still say `brief references: OK`
   (if it reports the Hebrew lists, show the message). Do not run git; do not touch any file outside `briefs/he/`.
