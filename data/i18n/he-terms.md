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
| quantum annealers | מחשבי הרפיה קוונטית | family ANNEAL; annealing = הרפיה (fem.: הרפיה קוונטית, הרפיה חטופה, ההרפיה נמשכת) — the slow heat treatment, as in metallurgy and the Academy's dental dictionary (הַרְפָּיָה, 1991); not חישול, which is forging (fast and sharp) — the editor, 2 Oct 2026; the Academy's physics term רִפּוּי (1993) is avoided because "ריפוי קוונטי" is the pseudo-scientific "quantum healing"; the Hebrew CS habit "חישול מדומה / קוונטי" is a mistranslation and is named once, as an alias, in the glossary entry (the reader's tooltip on the first הרפיה of a page); simulated annealing = הרפיה מדומה; quantum annealer (machine) = מחשב הרפיה; the construct form is הרפיית (הרפיית הצמתים = junction annealing) |
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
| T1 relaxation / relaxation time / energy relaxation | דעיכת T1 / זמן הדעיכה / דעיכת האנרגיה | never הרפיה, which the Atlas reserves for annealing (2 Oct 2026); dephasing = דה-פאזה; resonator decay = דעיכת המהוד |
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
| Who / Money / Market & supply chain / IP & standards / Roadmaps & track record / Strategic reading (the briefs' run-in labels of "Actors & economics") | מי / כספים / שוק ושרשרת אספקה / קניין רוחני ותקנים / מפות דרכים ועמידה בהבטחות / פרשנות אסטרטגית | bold, with the full stop inside: **פרשנות אסטרטגית.** |
| Confirm / Demote (the briefs' next-test labels) | לאשר / להוריד בדרגה | |
| Records timeline (the briefs' table) | ציר הזמן של השיאים | |
| eponyms in running text (Rydberg, Josephson, Pauli, Clifford, Majorana, Bell, Cooper, Hamiltonian) | רידברג, ג'וזפסון, פאולי, קליפורד, מיורנה, בל, קופר, המילטוניאן | transliterated, as the finished briefs do; an eponym inside a Latin identifier or a product name stays Latin |
| abstract (of a paper) | תמצית | never תקציר, which is "brief" |
| randomized benchmarking (RB) / interleaved RB / cycle benchmarking | מדידת ביצועים אקראית / מדידת ביצועים אקראית משולבת / מדידת ביצועים מחזורית | never השוואת ביצועים |
| decoherence | דה-קוהרנטיות | matches קוהרנטיות; never דה-קוהרנציה |
| detuning / local detuning | היסט (מתהודה) / היסט מקומי | never ההסטה |
| funding round "closed" | נסגר | never הושלם |
| post-selected / heralded / heralding | בבחירה בדיעבד / מבושר / בישור | |
| ancilla (qubit) | קיוביט עזר | |
| break-even / sweet spot / prior art | נקודת האיזון / נקודת האופטימום / אמנות קודמת | |
| crosstalk / whitepaper / preprint / testbed | הפרעה הדדית / מסמך טכני / טרום-פרסום / מצע ניסוי | |
| gap ledger / the money ledger / the forecast ledger | פנקס הפערים / פנקס הכספים / פנקס התחזיות | |
| moat (competitive) / lock-out | חפיר תחרותי / נעילת מתחרים | |
| Tag+key (the timeline column) | תג+מפתח | |
| roadmap status: pending / on track; deal status: undelivered / active | תלוי ועומד / לפי התוכנית; לא סופק / פעיל | |
| gate-set / transport-set (clock) | נקבע בידי השערים / נקבע בידי ההובלה | |
| erasure excision / erasure flag | השמטת מחיקות / דגל מחיקה | |
| quench (of a Hamiltonian) | שינוי פתאומי (quench) | |
| false positive / false negative | חיובי כוזב / שלילי כוזב | |
| sequencer / demultiplexer / chiplet / interposer / bump bond | מתזמן / מפריד ריבוב / שבבון / אינטרפוזר / חיבור בליטות | |
| matrix-product state / bond dimension / Mach–Zehnder / PNR (number-resolving) detector | מצב מכפלת מטריצות / ממד הקשר / מאך–צנדר / גלאי המבחין במספר הפוטונים | |
| further eponyms | ראבי (Rabi), ראמאן (Raman), ראמזי (Ramsey), זימן (Zeeman), דופלר (Doppler), שטארק (Stark), פרסטר (Förster), ואן דר ואלס (van der Waals), מולמר–סורנסן (Mølmer–Sørensen), הייזנברג (Heisenberg), איזינג (Ising), טאנר (Tanner), רנט (Rent), ג'ונסון (Johnson) | people cited as authors stay in Latin (Loss–DiVincenzo, Cirac/Zoller as names; the gate שער סירק–צולר) |
| Best case 2029: / Best case by 2029: / Worst case: (Outlook labels) | התרחיש הטוב ביותר ל-2029: / התרחיש הטוב ביותר עד 2029: / התרחיש הגרוע ביותר: | |
| Confirm/demote in 12–24 months: | לאשר/להוריד בדרגה בתוך 12–24 חודשים: | verbs; no spaces around the slash |
| Open: / Open questions: / Verification: / Attributes: / Register: (run-in labels) | פתוח: / שאלות פתוחות: / אימות: / תכונות: / המרשם: | |
| What exactly they do with this technology (Who-table column) | מה בדיוק הם עושים בטכנולוגיה זו | |
| Who roles: developer / research / supplier / user / investor / funder / regulator / evaluator | מפתח / מחקר / ספק / משתמש / משקיע / מממן / רגולטור / מעריך | DARPA = מממן |
| (X group) | (הקבוצה של X) | |
| captive / merchant (fab, foundry, supplier) | פנימי / מסחרי | never שבוי, never בבעלות הלקוח |
| G1–G7 (goal names in the briefs) | סימולציה אנלוגית · תועלת עם מיתון שגיאות · עמידות מוקדמת לתקלות · עמידות לתקלות בקנה מידה גדול · אופטימיזציה · רישות · מערכות הניתנות לפריסה | |
| derived clock (sum of the syndrome round) / readout-set | שעון נגזר / נקבע בידי הקריאה | |
| dominant term / floor / ceiling / wall | האיבר השולט / רצפה / תקרה / חומה | "moves the floor" = מזיז את הרצפה |
| fault tolerance / fault-tolerant / threshold / logical error rate / overhead / footprint / throughput | עמידות לתקלות / עמיד לתקלות / סף / שיעור שגיאה לוגית / תקורה / טביעת רגל / תפוקה | |
| yield (fabrication) / efficiency (a measured ratio) | שיעור תקינות / נצילות | יעילות only in the economic sense |
| wafer / die / chip / package / packaging / flip-chip | פרוסה / פיסה / שבב / מארז / אריזה / שבב הפוך | |
| coupler / tunable coupler / resonator / junction | מצמד / מצמד בר-כוונון / מהוד / צומת | צומת ג'וזפסון |
| two-level systems (TLS) | מערכות דו-רמתיות | |
| shuttling / conveyor / zone / latency / feed-forward / real-time | הסעה / מסוע / אזור / השהיה / הזנה קדימה / בזמן אמת | |
| magic state / distillation / cultivation / code switching / lattice surgery / yoked | מצב קסם / זיקוק / טיפוח / החלפת קוד / ניתוח סריג / רתום | |
| stabilizer / repetition code / dephasing / bit-flip / phase-flip / bias-preserving | מייצב / קוד חזרה / דה-פאזה / היפוך ביט / היפוך פאזה / משמר-הטיה | |
| loss (photons, atoms) / loss (dB: insertion, coupling) | אובדן / הפסד | |
| hyperfine / metastable / clock state / tweezer / reloading | על-דק / מטא-יציב / מצב שעון / פינצטה / טעינה מחדש | |
| fusion / resource state / cluster state / time-bin / squeezing / homodyne detection | היתוך / מצב משאב / מצב אשכול / תא זמן / סחיטה / גילוי הומודיני | |
| multiplexing / demultiplexing / fan-out | ריבוב / פירוק ריבוב / פיצול | |
| transducer / remote entanglement / Purcell filter / quantum-limited amplifier | מתמר / שזירה מרוחקת / מסנן פרסל / מגבר בגבול הקוונטי | |
| loss-aware / erasure-aware decoding | פענוח מודע-אובדן / פענוח מודע-למחיקות | |
| coherent quench (annealer) | הרפיה חטופה קוהרנטית | a quench of a Hamiltonian elsewhere = שינוי פתאומי (quench) |
| IPO / Series B extension / non-binding / gross / cumulative / lead (investor) | הנפקה ראשונה לציבור / הרחבת סבב B / לא מחייב / ברוטו / במצטבר / בהובלת X | |
| undisclosed (Money lines) / missed (roadmap outcome) / delivered / met / unmet / pending | לא פורסם / הוחמץ / סופק / הושג / לא הושג / תלוי ועומד | |
| export control / patent family / standards body | פיקוח על יצוא / משפחת פטנטים / גוף תקינה | |
| trade press / press release / peer-reviewed / company-reported | העיתונות המקצועית / הודעה לעיתונות / שעבר ביקורת עמיתים / מדווח בידי הספק | |
| independent replication / headline figure / single-shot | שחזור בלתי תלוי / נתון הכותרת / בהרצה יחידה | |
| microsecond / nanosecond (in words) | מיקרו-שנייה / ננו-שנייה | the unit symbols µs / ns stay |
