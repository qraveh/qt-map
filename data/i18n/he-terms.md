# Hebrew terminology of the Quantum Technology Atlas — the binding list for every translation (29 Sep 2026)

Rules. Formal written Hebrew (לשון כתובה תקנית), the register of a scientific review — not journalese. Terms below are fixed:
use them everywhere, in the same form; a term that is not here is translated once, consistently, and reported for this
list. Latin identifiers (`transmon`, `cx_nn`, machine and product names, organisation names, arXiv ids, DOIs, URLs),
numbers, units (µs, mK, GHz), citation marks ([D], [C], [R], [S], [P], [G], [S12], [1]), section marks (§7.3), Markdown
(** *, `, |, #, links), `{{placeholders}}` and `{python expressions}` are kept exactly as they are. Product and machine names
stay in their original script (IBM Heron, Helios, Zuchongzhi 3.0). Do not transliterate organisation names; do not translate
them. Numbers keep the decimal point and the thousands comma as in English (1,024 · 4.5 × 10⁻³). Dates: 26 בספטמבר 2026.
Sentences keep the Atlas's voice: short, declarative, no marketing words, no "notably/importantly"; say a thing once.

| English | עברית | note |
|---|---|---|
| Quantum Technology Atlas | אטלס הטכנולוגיות הקוונטיות | the work's name; "the Atlas" = האטלס |
| technology map / the map | מפת הטכנולוגיות / המפה | |
| technology (the map's unit) | טכנולוגיה | never "station"/"node" in reader text |
| node (graph mathematics of §7 only) | צומת | |
| edge | קשת | requires = דורש, alternatives = חלופות, conflicts = מתנגש, defines = מגדיר |
| architecture (a platform path) | ארכיטקטורה | |
| platform | פלטפורמה | |
| family (qubit platform family) | משפחה | |
| layer | שכבה | the ten layers = עשר השכבות |
| the stack | המחסנית | "ten layers read from the qubit up" |
| qubit carrier | נושא הקיוביט | layer 1 |
| encoding | קידוד | layer 2 |
| gate mechanism | מנגנון השער | layer 3; gate = שער, entangling gate = שער שזירה |
| connectivity and transport | קישוריות והובלה | layer 4 |
| control | בקרה | layer 5 |
| readout | קריאה | layer 6; mid-circuit readout = קריאה באמצע המעגל |
| code (error-correcting code) | קוד | layer 7; error correction = תיקון שגיאות |
| decoder | מפענח | layer 8; decoding in the loop = פענוח בלולאה |
| interconnect (between modules) | חיבור בין-מודולי | layer 9; link = קישור, module = מודול |
| manufacturing | ייצור | layer 10; foundry = בית יציקה (CMOS foundry = מפעל CMOS) |
| superconducting circuits | מעגלים מוליכי-על | family SC; transmon = טרנסמון (masc.) |
| trapped ions | יונים לכודים | family ION; ion trap = מלכודת יונים |
| neutral atoms | אטומים ניטרליים | family ATOM; tweezer array = מערך פינצטות (אופטיות) |
| photonics | פוטוניקה | family PHOTON; photon = פוטון |
| semiconductor spins | ספינים במוליכים למחצה | family SPIN; quantum dot = נקודה קוונטית; donor = דונור (donor spin = ספין דונורי) |
| defect spins | ספיני פגם | family DEFECT; colour centre = מרכז צבע; NV centre = מרכז NV |
| topological | טופולוגי | family TOPO; Majorana = מיורנה |
| quantum annealers | מחשבי חישול קוונטי | family ANNEAL; annealing = חישול |
| natural / fabricated (carrier) | טבעי / מיוצר | the natural–fabricated divide = החלוקה טבעי–מיוצר |
| crossing technology | טכנולוגיה חוצה | hatched on the map = מקווקוות |
| empty slot | משבצת ריקה | |
| primary / alternate (technology of an architecture) | ראשית / חלופית | |
| attribute (the seven design attributes) | תכונה | |
| lens | עדשה | |
| card (a technology's, machine's, architecture's) | כרטיס | |
| brief (technology brief) | תקציר | the technology briefs = תקצירי הטכנולוגיות |
| record page | דף רשומה | |
| machine / quantum machine / quantum computer | מכונה / מכונה קוונטית / מחשב קוונטי | as in the English: "quantum machine" at entry points, "quantum computer" only for gate-capable devices |
| the register (of machines) | המרשם | the Quantum Machines Register = מרשם המכונות הקוונטיות |
| device (hardware that exists) | התקן | |
| deployed / demonstrated / retired / announced / planned | בהפעלה / הודגם / הוצא משימוש / הוכרז / מתוכנן | status words |
| gate-capable device | התקן בעל שערים | |
| evidence cell | תא ראיות | |
| verified (✅) / unverified (🔎) | מאומת / לא מאומת | |
| evidence grade | דרגת הראיות | |
| verdict | פסק | supported = נתמכת; partly supported = נתמכת חלקית; not supported = אינה נתמכת |
| hypothesis | השערה | H1–H8 stay H1–H8 |
| forecast / the forecast ledger | תחזית / פנקס התחזיות | F1–F6 stay |
| roadmap | מפת דרכים | |
| cohort | קוהורט | |
| edition | מהדורה | |
| data cut-off | תאריך הקפאת הנתונים | "data cut-off: 26 September 2026" = הקפאת נתונים: 26 בספטמבר 2026 |
| physical qubit / logical qubit | קיוביט פיזי / קיוביט לוגי | |
| two-qubit error / gate error | שגיאת שער דו-קיוביטי / שגיאת שער | |
| fidelity | נאמנות | |
| coherence / T1 / T2 | קוהרנטיות / T1 / T2 | |
| syndrome round / QEC cycle | סבב סינדרום / מחזור תיקון שגיאות | |
| surface code / colour code / qLDPC code | קוד המשטח / קוד הצבע / קוד qLDPC | |
| erasure / erasure conversion | מחיקה / המרה למחיקה | erasure check = בדיקת מחיקה |
| leakage | דליפה | |
| dual-rail | מסילה כפולה | dual-rail encoding = קידוד מסילה כפולה |
| cat qubit / GKP | קיוביט חתול / GKP | bosonic = בוזוני |
| cryogenic / cryostat / dilution refrigerator | קריוגני / קריוסטט / מקרר דילול | |
| room temperature | טמפרטורת החדר | |
| wiring / I/O | חיווט / קלט-פלט | |
| cloud access / on-premises | גישה בענן / באתר הלקוח | |
| Find (the search window) | חיפוש | "Find in the Atlas" = חיפוש באטלס |
| whole word / substring; case-sensitive / case-insensitive | מילה שלמה / מחרוזת חלקית; תלוי רישיות / לא תלוי רישיות | |
| all languages | כל השפות | |
| contents (table of) | תוכן העניינים | |
| about the Atlas | על האטלס | |
| takeaways | עיקרי הדברים | §0 |
| references (§9, the briefs' lists) | מקורות | the section title; "reference" (a cited work) = מקור |
| glossary | מילון מונחים | |
| method / confidence | שיטה / מידת הביטחון | |
| known conflicts (between sources) | סתירות ידועות | |
| the next test / expectations | המבחן הבא / ציפיות | |
| the bet (an architecture's) | ההימור | |
| goal (G1–G7) | יעד | |
| score / scoreboard | ציון / לוח הציונים | |
| fit matrix | מטריצת ההתאמה | |
| most promising directions | הכיוונים המבטיחים ביותר | |
| open verification items | פריטי אימות פתוחים | |
| identity & lineage / physics & limits / engineering state of the art / manufacturing, materials & supply chain / control, readout & I/O burden / role in the stack / evidence — how the numbers were measured / actors & economics / outlook & open questions | זהות ומוצא / פיזיקה וגבולות / מצב ההנדסה העדכני / ייצור, חומרים ושרשרת האספקה / בקרה, קריאה ועומס הקלט-פלט / תפקיד במחסנית / ראיות — כיצד נמדדו המספרים / שחקנים וכלכלה / תחזית ושאלות פתוחות | the briefs' section names |
| actors & goals | שחקנים ויעדים | the card block |
| organisation | ארגון | |
| author / publisher / published by | מחבר / מוציא לאור / בהוצאת | |
| English / Russian / Hebrew (language names, native) | English / Русский / עברית | the language switch shows native names |
