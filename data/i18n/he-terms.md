# Hebrew terminology of the Quantum Technology Atlas — the binding list for every translation (29 Sep 2026; revised 2 Oct 2026 — every term checked against the dictionaries of the Academy of the Hebrew Language and Israeli academic usage, and the terms of quantum mechanics and quantum information against the Hebrew quantum literature itself — Hebrew Wikipedia's quantum articles, the Davidson Institute, university teaching, the quantum press — which outranks the Academy's general dictionaries for them; the authority is given in the note)

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
| manufacturing | ייצור | layer 10; foundry = מפעל ייצור (pl. מפעלי ייצור; CMOS foundry = מפעל CMOS; photonic IC foundry = מפעל ייצור למעגלים פוטוניים משולבים) — never בית יציקה, which is metal casting (Academy Building 1972) |
| superconducting circuits | מעגלים מוליכי-על | family SC; transmon = טרנסמון (masc.) |
| trapped ions | יונים לכודים | family ION; ion trap = מלכודת יונים |
| neutral atoms | אטומים ניטרליים | family ATOM; tweezer array = מערך מלקחיים אופטיים (see tweezer below) |
| photonics | פוטוניקה | family PHOTON; photon = פוטון |
| semiconductor spins | ספינים במוליכים למחצה | family SPIN; quantum dot = נקודה קוונטית; donor = אטום תורם / תורם (Academy Modern Physics 1993: donor atom = אטום תורם, donor impurity = אלח תורם; never דונור); donor spin = ספין של אטום תורם, donor spins = ספיני תורמים, bare "donors" = אטומים תורמים where תורמים alone would read as contributors; silicon = צורן (Academy Electronics 1981, Microelectronics; its סיליקון is silicone); polysilicon = צורן רב-גבישי; Si / SiGe / SOI / SiN stay Latin |
| defect spins | ספיני פגם | family DEFECT; colour centre = מרכז צבע; NV centre = מרכז NV |
| topological | טופולוגי | family TOPO; Majorana = מיורנה |
| quantum annealers | מחשבי הרפיה קוונטית | family ANNEAL. Two words for the English "annealing", by what it names: QUANTUM annealing (the technique, the machine, the run, the coherent quench, simulated annealing as its classical sibling) = הרפיה, f. (הרפיה קוונטית, הרפיה חטופה, ההרפיה נמשכת; construct הרפיית) — the term of the Hebrew quantum literature (Hayadan 2013: "הרפיה קוונטית"), physically a relaxation toward the ground state (the editor, 2 Oct 2026); MATERIALS annealing (the heat treatment in fabrication: laser annealing, ABAA, 1150 °C, NV formation, STM phosphorus incorporation) = ריפוי, m. — the Academy's term (Modern Physics 1993, Chemical Engineering 1989, Technique 1946; its AI dictionary 1997 has ריפוי מודמה for simulated annealing, not followed: the Atlas keeps the quantum family together under הרפיה). Never חישול (= forging; the Hebrew CS habit "חישול מדומה / קוונטי" is a mistranslation, named once as an alias in the glossary entry). quantum annealer (machine) = מחשב הרפיה |
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
| cohort | עוקבה | f. (העוקבה, עוקבות); Academy: five dictionaries 1987–2022; TAU usage מחקר עוקבה; never קוהורט |
| edition | מהדורה | |
| data cut-off | תאריך הקפאת הנתונים | "data cut-off: 26 September 2026" = הקפאת נתונים: 26 בספטמבר 2026 |
| physical qubit / logical qubit | קיוביט פיזי / קיוביט לוגי | |
| two-qubit error / gate error | שגיאת שער דו-קיוביטי / שגיאת שער | |
| fidelity | נאמנות | |
| coherence / T1 / T2 | קוהרנטיות / T1 / T2 | |
| T1 relaxation / relaxation time / energy relaxation | רלקסציית T1 / זמן הרלקסציה / רלקסציית האנרגיה | the Hebrew quantum/physics literature's term (HUJI NMR teaching: "זמן רלקסציה אורכי – T1"; Hebrew Wikipedia's physics article רלקסציה (תפוגה); Academy Modern Physics 1993: תפוגה / רלקסציה); never הרפיה (the Atlas's quantum annealing; Hayadan once writes הרפיית ספין) and never דעיכה, which is decay (resonator decay = דעיכת המהוד, Purcell decay, κ); dephasing = דה-פאזה |
| imaging / fluorescence imaging | דימות / דימות פלואורנות | imaging = דימות, m. (Academy IT 2010, general dictionary 1971–2025; its הדמיה is simulation; Technion/Weizmann usage); never הדמיה |
| fluorescence / fluorescent | פלואורסצנציה / פלואורסצנטי | the field's word: Hebrew Wikipedia's title and its quantum-dot and spectroscopy articles (63 articles vs 5 for the Academy's פלואורנות), university usage (Bar-Ilan EE), the Davidson Institute's own explainer (which spells פלורסנציה); the Academy's פלואורנות (Modern Physics 1993 and seven more) appears in one Davidson quantum-spin article and is recorded here, not used. The Hebrew quantum literature itself (ion, atom and NV readout: Weizmann, HUJI, Technion, the press) names no fluorescence word at all — it writes פיזור האור, פולט פוטונים, גלאי פוטונים בודדים (checked 2 Oct 2026, 22:30) |
| time evolution / Hamiltonian evolution / annealing evolution | התפתחות (בזמן) / התפתחות המילטוניאנית / התפתחות ריפוי אנלוגית | Hebrew quantum-mechanics teaching (TAU): התפתחות בזמן; never אבולוציה |
| matching (graph; MWPM) / matching decoder | זיווג (זיווג מושלם במשקל מינימלי) / מפענח זיווג | Hebrew graph theory (TAU, Technion); fit stays התאמה (מטריצת ההתאמה) |
| neural network / neural decoder | רשת עצבית / מפענח מבוסס רשת עצבית | Academy IT 1997–2010; Technion course names; never נוירוני (a neuron itself stays נוירון) |
| objective (microscope) / coaxial cable / latch | אובייקטיב / כבל קואקסיאלי / תפסן | objective = אובייקטיב (Academy Optics 1977; never עדשה אובייקטיבית; the adjective אובייקטיבי = impartial stays); coax = כבל קואקסיאלי (Academy IT 2002; never the clipping קואקס; the device name קואקסמון stays); latch = תפסן (digital-logic teaching), flux latch = תפסן שטף |
| checked against the Academy and KEPT (2 Oct 2026) | — | decoder מפענח (not פענח, IT 1989); junction צומת (not מצמת); spin ספין (not סחריר); bus אפיק (not פס, IT 2007 — teaching usage); link קישור (not מקשר, Electronics 2007); rail מסילה (EE usage מסילת מתח); dilution refrigerator מקרר דילול (not מיהול, Chemistry 1985 — no usage); vacuum ואקום for apparatus (ריק is the physical vacuum); hyperfine על-דק; throughput תפוקה; crosstalk הפרעה הדדית; sequencer מתזמן; near field שדה קרוב (not שדה-קרבה, Acoustics 1985); crystal growth גידול (the Academy's גדילה is also alive); quadrature קוודרטורה; crossbar in Latin letters (not שתי-וערב, 1970); Mach–Zehnder מאך–צנדר (Swiss German z = צ; the Wikipedia זנדר is an anglicism); confidence (the Atlas's rating) מידת הביטחון (סמך is the statistical confidence) |
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
| whole word / substring; case-sensitive / case-insensitive | מילה שלמה / תת-מחרוזת; תלוי רישיות / לא תלוי רישיות | substring = תת-מחרוזת (Academy Programming Languages 2015) |
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
| randomized benchmarking (RB) / interleaved RB / cycle benchmarking / benchmarking | בחינת ביצועים אקראית / בחינת ביצועים אקראית משולבת / בחינת ביצועים מחזורית / בחינת ביצועים | f.; the Hebrew quantum literature's term (Hebrew Wikipedia, "בחינת ביצועים של מחשבים קוונטיים": "בחינת ביצועים אקראית (Randomized Benchmarking, RB)"); logical RB = בחינת ביצועים אקראית לוגית; direct RB = … ישירה; blind RB = … עיוורת; the English stays in parentheses at a file's first mention; never מדידת ביצועים, never השוואת ביצועים; the Academy's general מידוד (2004) is management usage, not the field's |
| decoherence | דה-קוהרנטיות | matches קוהרנטיות; never דה-קוהרנציה |
| detuning / local detuning | היסט (מתהודה) / היסט מקומי | never ההסטה |
| funding round "closed" | נסגר | never הושלם |
| post-selected / heralded / heralding | בבחירה בדיעבד / מבושר / בישור | |
| ancilla (qubit) | קיוביט עזר | |
| break-even / sweet spot / prior art | נקודת האיזון / נקודת האופטימום / ידע קודם | prior art (patents) = ידע קודם, as Israeli patent practice writes it; never אמנות קודמת |
| crosstalk / whitepaper / preprint / testbed | הפרעה הדדית / מסמך טכני / קדם-פרסום / סביבת ניסוי | preprint = קדם-פרסום (Academy Librarianship 2003; the Wikipedia title); testbed = סביבת ניסוי (מצע is the substrate — Academy Microelectronics 1981 — so never מצע ניסוי); crosstalk keeps הפרעה הדדית (the Academy's ערב דיבור, 1957/1970, is telephony and not in academic use) |
| gap ledger / the money ledger / the forecast ledger | פנקס הפערים / פנקס הכספים / פנקס התחזיות | |
| moat (competitive) / lock-out | חפיר תחרותי / נעילת מתחרים | |
| Tag+key (the timeline column) | תג+מפתח | |
| roadmap status: pending / on track; deal status: undelivered / active | תלוי ועומד / לפי התוכנית; לא סופק / פעיל | |
| gate-set / transport-set (clock) | נקבע בידי השערים / נקבע בידי ההובלה | |
| erasure excision / erasure flag | השמטת מחיקות / דגל מחיקה | |
| quench (of a Hamiltonian) | שינוי פתאומי (quench) | |
| false positive / false negative | חיובי שגוי / שלילי שגוי | Academy Epidemiology 2021: תוצאה חיובית שגויה; never כוזב (a false claim is still טענה כוזבת) |
| sequencer / demultiplexer / chiplet / interposer / bump bond | מתזמן / מפלג / שבבון / אינטרפוזר / חיבור בליטות | demultiplexer = מפלג, multiplexer = מרבב (Israeli digital-logic teaching; the Academy's נוטל ריבוב, 2007, is not in use); demultiplexing as a process stays פירוק ריבוב |
| matrix-product state / bond dimension / Mach–Zehnder / PNR (number-resolving) detector | מצב מכפלת מטריצות / ממד הקשר / מאך–צנדר / גלאי המבחין במספר הפוטונים | |
| further eponyms | ראבי (Rabi), ראמאן (Raman), ראמזי (Ramsey), זימן (Zeeman), דופלר (Doppler), שטארק (Stark), פרסטר (Förster), ואן דר ואלס (van der Waals), מולמר–סורנסן (Mølmer–Sørensen), הייזנברג (Heisenberg), איזינג (Ising), טאנר (Tanner), רנט (Rent), ג'ונסון (Johnson) | people cited as authors stay in Latin (Loss–DiVincenzo, Cirac/Zoller as names; the gate שער סירק–צולר) |
| Best case 2029: / Best case by 2029: / Worst case: (Outlook labels) | התרחיש הטוב ביותר ל-2029: / התרחיש הטוב ביותר עד 2029: / התרחיש הגרוע ביותר: | |
| Confirm/demote in 12–24 months: | לאשר/להוריד בדרגה בתוך 12–24 חודשים: | verbs; no spaces around the slash |
| Open: / Open questions: / Verification: / Attributes: / Register: (run-in labels) | פתוח: / שאלות פתוחות: / אימות: / תכונות: / המרשם: | |
| What exactly they do with this technology (Who-table column) | מה בדיוק הם עושים בטכנולוגיה זו | |
| Who roles: developer / research / supplier / user / investor / funder / regulator / evaluator | מפתח / מחקר / ספק / משתמש / משקיע / מממן / מאסדר / מעריך | DARPA = מממן; regulator = מאסדר (Academy Civil Law 2019, Insurance 2016, Banking 2006; רגולציה stays) |
| (X group) | (הקבוצה של X) | |
| captive / merchant (fab, foundry, supplier) | פנימי / מסחרי | never שבוי, never בבעלות הלקוח |
| G1–G7 (goal names in the briefs) | סימולציה אנלוגית · תועלת עם הפחתת שגיאות · סבילות מוקדמת לתקלות · סבילות לתקלות בקנה מידה גדול · אופטימיזציה · רישות · מערכות הניתנות לפריסה | error mitigation = הפחתת שגיאות, f. (the Hebrew quantum press on Qedma's error mitigation; the Academy's אפחות, 2007–2022, is public-health and environmental usage; never מיתון); mitigated = מופחת; mitigates = מפחית; fault tolerance = סבילות לתקלות (below) |
| derived clock (sum of the syndrome round) / readout-set | שעון נגזר / נקבע בידי הקריאה | |
| dominant term / floor / ceiling / wall | האיבר השולט / רצפה / תקרה / חומה | "moves the floor" = מזיז את הרצפה |
| fault tolerance / fault-tolerant / threshold / logical error rate / overhead / footprint / throughput | סבילות לתקלות / סובלני לתקלות / סף / שיעור שגיאות לוגיות / תקורה / טביעת רגל / תפוקה | fault tolerance = סבילות לתקלות (the Hebrew quantum literature: Hebrew Wikipedia's Majorana article "סבילות לתקלות", Hayadan "סובלני לתקלות (fault-tolerant)", also "חסין תקלות"; the Academy's IT dictionaries 1992–2004 agree with סבילות/סבולת תקלות); fault-tolerant = סובלני לתקלות, סובלנית לתקלות, סובלניים לתקלות (Hayadan's form); early FT = סבילות מוקדמת לתקלות; algorithmic FT = סבילות תקלות אלגוריתמית; never עמידות לתקלות (עמידות keeps other senses: עמידות לרעש); threshold = סף (Davidson: סף השגיאות); error rate = שיעור שגיאות (plural; Hebrew Wikipedia's benchmarking article writes שיעורי השגיאה); throughput keeps תפוקה |
| yield (fabrication) / efficiency (a measured ratio) | שיעור תקינות / נצילות | יעילות only in the economic sense |
| wafer / die / chip / package / packaging / flip-chip | פרוסה / פיסה / שבב / מארז / זיווד / שבב הפוך | packaging (electronic) = זיווד (Academy Microelectronics 1981; the engineers' society of electronic packaging), m.; the package itself = מארז; never אריזה for electronics |
| coupler / tunable coupler / resonator / junction / cavity | מצמד / מצמד בר-כוונון / מהוד / צומת / מהוד | צומת ג'וזפסון (the Academy's מצמת is not in use); cavity (a resonator: 3D superconducting, optical, cat/GKP, nanocavity, cavity QED) = מהוד (Academy: resonator = מהוד, Physics 1976/1993; cavity resonator = מהוד מחילה, Electronics 1970; Weizmann: מהוד אופטי) — a 3D cavity beside a readout resonator is המהוד התלת-ממדי / מהוד הקריאה; חלל only for outer space and a void |
| two-level systems (TLS) | מערכות דו-רמתיות | |
| shuttling / conveyor / zone / latency / feed-forward / real-time | הסעה / מסוע / אזור / השהיה / הזנה קדימה / בזמן אמת | |
| magic state / distillation / cultivation / code switching / lattice surgery / yoked | מצב קסם / זיקוק / טיפוח / החלפת קוד / ניתוח סריג / רתום | |
| stabilizer / repetition code / dephasing / bit-flip / phase-flip / bias-preserving | מייצב / קוד חזרה / דה-פאזה / היפוך ביט / היפוך פאזה / משמר-הטיה | |
| loss (photons, atoms) / loss (dB: insertion, coupling) | אובדן / הפסד | |
| hyperfine / metastable / clock state / tweezer / reloading | על-דק / מטא-יציב / מצב שעון / מלקחיים אופטיים / טעינה מחדש | optical tweezers = מלקחיים אופטיים (m. pl.; Davidson Institute, Hebrew Wikipedia; the Academy has only the hand tool מלקטת, 1965); tweezer array = מערך מלקחיים אופטיים; construct מלקחי AOD; never פינצטה; hyperfine keeps על-דק (the Academy's על-דקיק, 1993, is not taught) |
| fusion / resource state / cluster state / time-bin / squeezing / homodyne detection | היתוך / מצב משאב / מצב אשכול / משבצת זמן / סחיטה / גילוי הומודיני | fusion (the photonic fusion gate, fusion-based QC, fusion network) = היתוך, m. — the field's word for a fusion that combines: היתוך גרעיני (Hebrew Wikipedia 163 articles vs 6 for the Academy's מיזוג גרעיני), היתוך חיישנים / היתוך מידע (sensor and data fusion in Israeli engineering: Systematics/MathWorks, Calcalist, Techtime), ניסויים בהיתוך על ידי לייזר (Wikipedia's optical-tweezers article); the Academy's מיזוג (Modern Physics 1993, with the note that היתוך is melting) has no living use and is recorded here, not used; no Hebrew quantum text names the photonic fusion gate at all (checked 2 Oct 2026, 22:30). מיזוג stays for a merge (מיזוג/פיצול of ion crystals or code patches) and a merger (מיזוג SPAC); time bin = משבצת זמן (Academy Data Communications 2002: time slot), f.; never תא זמן |
| multiplexing / demultiplexing / fan-out | ריבוב / פירוק ריבוב / פיצול | |
| transducer / remote entanglement / Purcell filter / quantum-limited amplifier | מתמר / שזירה מרוחקת / מסנן פרסל / מגבר בגבול הקוונטי | |
| loss-aware / erasure-aware decoding | פענוח מודע-אובדן / פענוח מודע-למחיקות | |
| coherent quench (annealer) | הרפיה חטופה קוהרנטית | a quench of a Hamiltonian elsewhere = שינוי פתאומי (quench); the metallurgical quench (rapid cooling) is חיסום, which is not this |
| IPO / Series B extension / non-binding / gross / cumulative / lead (investor) | הנפקה ראשונית לציבור / הרחבת סבב B / לא מחייב / ברוטו / במצטבר / בהובלת X | IPO = הנפקה ראשונית לציבור (Academy Banking 2006), never ראשונה |
| undisclosed (Money lines) / missed (roadmap outcome) / delivered / met / unmet / pending | לא פורסם / הוחמץ / סופק / הושג / לא הושג / תלוי ועומד | |
| export control / patent family / standards body | פיקוח על יצוא / משפחת פטנטים / גוף תקינה | |
| trade press / press release / peer-reviewed / company-reported | העיתונות המקצועית / הודעה לעיתונות / שעבר ביקורת עמיתים / מדווח בידי הספק | |
| independent replication / headline figure / single-shot | שחזור בלתי תלוי / נתון הכותרת / בהרצה יחידה | |
| microsecond / nanosecond (in words) | מיקרו-שנייה / ננו-שנייה | the unit symbols µs / ns stay |
| resource-state generator (RSG) (the photonic FBQC term; 4 Oct 2026 — the English pass replaced "factory") | מחולל מצבי משאב | the PsiQuantum term; "factory" stays only for magic states |
| SiMOS; AlphaQubit 2; bivariate bicycle (English spellings fixed 4 Oct 2026) | SiMOS; AlphaQubit 2; bivariate bicycle | Latin tokens as the English edition writes them |
