---
id: code_erasure
name: קודים מותאמי-מחיקה
layer: 7 קוד
status: emerging
since: 2025
one_line: קודי משטח וקודי בלוקים המפוענחים עם דגלים של שגיאות ממוקמות; ספים של 4–10% ו-Λ ≈ 27 בסימולציה, רווחים של 1.7–1.9× בחומרה.
verdict: התאוריה מבטיחה Λ ≈ 27 וספים של 4–10%; החומרה מראה רק 1.7–1.9× ממידע המחיקה, ואף קוד מוליך-על לא פוענח עם דגלי מחיקה. לאשר אם זיכרון d=3→5 המפוענח עם דגלי מחיקה ידווח על Λ ≥ 3 עד סוף 2027; להוריד בדרגה אחרת.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

קוד מותאם-מחיקה הוא קוד מייצב שהמפענח שלו מקבל, נוסף לסינדרום, דגל לכל קיוביט האומר "הקיוביט הזה אבד או יצא ממרחב הקוד כאן", ושהפריסה ולוח הזמנים שלו נבחרו לערוץ שבו שגיאות ממוקמות שולטות. שגיאה ממוקמת מסלקת את שאלת *היכן* ומשאירה רק את *מה*, ולכן קוד המשטח נכשל רק כאשר המחיקות מחלחלות דרכו — סף של 50% במודל קיבולת הקוד, הנקבע בידי פרקולציית קשרים בסריג ריבועי [S][679], לעומת 18.9(3)% לרעש דה-פולריזציה [S][334] — והמרחק שלו כנגד מחיקות הוא d ולא ⌈d/2⌉. פענוח מחיקות בסבירות מרבית הוא קילוף בזמן ליניארי על יער פורש [S][680]; Union-Find מרחיב אותו לשגיאות פאולי ב-O(n α(n)) [S][681]. המפנה לחומרה הגיע ב-2022: 98% משגיאות ¹⁷¹Yb ניתנות להמרה, מה שמעלה את סף קוד המשטח ברמת המעגל מ-0.937% ל-4.15% [S][8], וטרנסמונים במסילה כפולה, שבהם במחיקה של 1% הקוד סובל שגיאת פאולי של 0.51%, 5.2× מהנתון הסטנדרטי [S][334]; מחזור מלא ראשון של תיקון אובדן רץ על חמישה יונים לכודים כבר ב-2020 [D][682]. הדגלים שייכים לתקציר *בדיקת מחיקה באמצע המעגל* (שכבה 6); התקציר הזה עוסק במה שהקוד עושה איתם.

תכונות (רשומת הגרף; מקרא: a זיקה טבעי↔מיוצר; b זמן, שזירה דטרמיניסטית/מבושרת; c קריאה; d ניידות; e בקרה @ מיקום; f מבנה השגיאה; g ייצור):
- a = 0.5 — אדיש לנושא הקיוביט; מפענח אחד משרת אטומים וטרנסמונים.
- b = אין זמן או שזירה משלו.
- c = אין — הוא צורך את דגל הבדיקה.
- d = סטטי.
- e = אין אופן בקרה, אין מיקום.
- f = מחיקה — אובדן ממוקם שולט, שארית פאולי קטנה.
- g = אין — פריסה ותוכנה.
דירוג 3 מתוך 111; משותף למשפחות האטומים הניטרליים והמעגלים מוליכי-העל; הוא מצמיד נושא קיוביט מיוצר למבנה שגיאה של מחיקה.

## פיזיקה וגבולות

לרווח שלושה חלקים, ועל כל אחד מוטל מס. הסף: החלק המומר קובע אותו. ה-4.15% של Wu מניחים המרה של 98% [S][8]; החלקים שנמדדו הם 56(4)% מהשגיאות החד-קיוביטיות ו-≈33% מהשגיאות הדו-קיוביטיות ב-¹⁷¹Yb [D][141] ו-38(6)% משגיאת ה-CZ של Princeton [D][142], ולכן הסף בפועל יושב בין גבול פאולי לגבול המחיקה; קודי XZZX למחיקה מוטה מעלים את התקרה ל-8.2%, והיתוך היברידי — ל-10.3% [S][643]. הבדיקות אינן חינם: כל אחת חושפת את הקיוביט ל-T₁, וקיוביטי מחיקה מנצחים רק כאשר הבדיקה קצרה ביחס למחזור [S][683]; עם חיוביים שגויים ושליליים שגויים הסף נשאר לפחות כפול מערך פאולי והמרחק האפקטיבי בערך מוכפל [S][395]. מחיקות מתפשטות דרך שערים, ומחיקה שהוחמצה חוזרת כדליפה, השגיאה שקוד המשטח מטפל בה הכי גרוע [S][684]. התקרה האידאלית היא הסימולציה של Quantum Circuits: מחיקת קיוביט עזר 0.4%, מחיקת קיוביט נתונים 0.1%, דה-פאזה 0.04/0.01/0.01% ובדיקות מושלמות הנדחות לסוף כל סבב נותנות Λ ≈ 27 לכל צעד במרחק לעומת Λ ≈ 14 לרעש דה-פולריזציה של 0.1% [S][84]; קוד המשטח בחומרה של Google עומד על Λ = 2.14(2) [D][1]. ההטיה שמאחורי מספרים כאלה היא ≈40:1 — 6×10⁻³ מחיקה לעומת 1.6×10⁻⁴ פאולי לכל פעולה [S][334] — תואמת את ה-42(1) שמדדה AWS [D][85] [G:AWS-ERASURE-2026-04]. מה שמזיז את הרצפה: ההמרה תחת שערים דו-קיוביטיים, שיעור השליליים השגויים, זמן הבדיקה, ומפענחים המשתמשים במידע אובדן מושהה כך שאין צורך בבדיקה באמצע המעגל [S][508].

## מצב ההנדסה העדכני

הטוב ביותר שהודגם, אטומים: קוד המשטח של Harvard/MIT/QuEra על עד 448 אטומים, 2.14(13)× מתחת לסף במעגל אפיון של ארבעה סבבים, כשמידע אובדן בתוספת פענוח בלמידת מכונה נותן 1.73(13)× לעומת פענוח רגיל [D][4]; בלוק ה-[[4,2,2]] של Princeton, שהדעיכה הלוגית שלו מואטת 1.9(4)× עם דגלי מחיקה במפענח [D][142]; 24 הקיוביטים הלוגיים של Microsoft/Atom Computing ב-48 אטומים, עם 1.8 אטומים אבודים מתוקנים לריצה [D][149]. מוליכי-על: אף קוד המפוענח עם דגלי מחיקה לא רץ על חומרת מסילה כפולה נכון ל-3 בספטמבר 2026; המעגלים הגדולים ביותר בקידוד מחיקה הם ארבעת הטרנסמונים במסילה כפולה של SUSTech, עם מצב GHZ לוגי של שלושה קיוביטים בנאמנות 93.9% (גרסת Nature Physics) [D][406] [G:SUSTECH-DUALRAIL-2025] ו-Seeker של Quantum Circuits עם 8 קיוביטים, גילוי שגיאות בלבד [C][86] [G:QCI-SEEKER-2024-11]. טיפוסי בקנה מידה: רק המכונות של Harvard ושל Microsoft מפענחות עם דגלי אובדן מעל 100 אטומים.

| שנה | נתון | מי | תג | מקור |
|---|---|---|---|---|
| 2009 | סף אובדן של 50% (פרקולציית קשרים) | Stace/Barrett/Doherty | [S] | [679] |
| 2022-01 | סף 0.937% → 4.15% בהמרה של 98% | Princeton/Yale | [S] | [8] |
| 2022-08 | מסילה כפולה: 0.51% פאולי נסבל במחיקה של 1%, 5.2× | AWS | [S] | [334] |
| 2023-02 | מחיקה מוטה ב-XZZX 8.2%; היתוך היברידי 10.3% | Yale/Princeton | [S] | [643] |
| 2024-11 | 24 לוגיים ב-48 אטומים; 1.8 אטומים אבודים מתוקנים לריצה | Microsoft/Atom | [D] | [149] |
| 2025-06 | דעיכת [[4,2,2]] איטית 1.9(4)× עם דגלי מחיקה | Princeton | [D] | [142] |
| 2025-06 | 2.14(13)× מתחת לסף; מידע אובדן + למידת מכונה 1.73(13)× | Harvard/QuEra | [D] | [4] |
| 2026-08 | Λ ≈ 27 לעומת 14, רעש מסילה כפולה מובנה, בדיקות מושלמות | QCI/D-Wave | [S] | [84] |

איבר השגיאה השולט כיום: באטומים השגיאה הדו-קיוביטית הלא-מומרת, ≈62–67% משגיאת ה-CZ [D][141], [142]; במסילה כפולה מחיקת קיוביט העזר לכל CZ, 0.400(4)%, והזמן המת של הבדיקה [D][84] [G:DUALRAIL-CZ-2026-08]; בשניהם, זנב של שליליים שגויים שאיש לא ספר לאורך סבבים רבים.

## ייצור, חומרים ושרשרת האספקה

דבר אינו מיוצר עבור הקוד; העומס שלו נופל על החומרה שהוא בוחר. מסילה כפולה דורשת שני טרנסמונים טובים או שני מהודים לכל אתר — בעיה של ניצולת בריבוע — ועוד קיוביט עזר לכל זוג מהודים [S][399], ומכאן תוכנית 8 → 17 → 49 → 181 של Quantum Circuits, בהרכבה ידנית [R][94] [G:DWAVE-QCI-2026-01]. אטומים אלקליים-עפרוריים אינם מוסיפים חומרה, אך עולים בנאמנות חד-קיוביטית במכלול המטא-יציב, 99.12(4)% לעומת 99.968(3)% במצב היסוד בהתקן של JILA [D][645]. המפענח הוא התוצר היחיד של הקוד: Union-Find על Xilinx VCU129 מפענח d = 21 ב-11.5 ns לסבב תחת רעש פנומנולוגי של 0.1% [D][685]; קלט מחיקה טבוע ב-Union-Find [S][681], אך לא פורסם מדד ביצועים ב-FPGA עם דגלי מחיקה; Stim חושף את HERALDED_ERASE [P][397]. עלות יחידה: 2× קיוביטים פיזיים לכל אתר במסילה כפולה, לעומת טענת Quantum Circuits ל-10–20 פיזיים לכל לוגי במקום ≈200 [C][86]. פיקוח על יצוא: הכלל של BIS מ-2024-09-06 [G][301] [G:BIS-QUANTUM-2024] מפקח על מחשבים קוונטיים (4A906: רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT נופלים באותה רצועה — מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך [G:BIS-3A901A-CRYOCMOS]), על תוכנה "המתוכננת במיוחד" לפיתוח או לייצור של התקני קיוביטים והתקני בקרה מפוקחים (4D906) ועל הטכנולוגיה הקשורה (4E906); מפענח הנשלח כקושחה למערכת בקרה מפוקחת נופל בתוך 4D906.

## בקרה, קריאה ועומס הקלט-פלט

הקוד מוסיף לזרם הסינדרום ביט אחד לכל קיוביט בכל מחזור, ועוד הכרעה: לאפס ולשזור מחדש את הקיוביט המחוק לפני הסבב הבא, או לדחות. במסילה כפולה זו הזנה קדימה בתוך ≈1 µs (שער 0.50 µs, בדיקה 0.38 µs) [D][84], [85]; באטומים — פריים מצלמה וטעינה מחדש, ≈1 ms [D][4]. פענוח מחיקה מושהה [S][508] ובדיקות-על (superchecks) [D][4] מסירים את ההסתעפות באמצע המעגל במחיר של פענוח מתואם. קירות: ב-10³ הקיר הוא של החומרה; ב-10⁴ המפענח חייב לקלוט ≈10⁴ דגלים ועוד סינדרומים בכל מיקרושנייה — 10 Gbit/s, בהישג ידו של FPGA [D][685] אך לא נבדק עם מחיקות; ב-10⁶ מסילה כפולה פירושה 2×10⁶ טרנסמונים, ובאטומים תקציב הפריימים של תקציר *בדיקת מחיקה באמצע המעגל* חל ללא שינוי.

## תפקיד במחסנית

שתי ארכיטקטורות: מחיקה במסילה כפולה במוליכי-על (D-Wave/Quantum Circuits, AWS, SUSTech) ואטומים ניטרליים אלקליים-עפרוריים (Atom Computing/Microsoft, Princeton, Caltech). הקוד דורש את הדגלים של בדיקת המחיקה באמצע המעגל, מספק קיוביטים לוגיים לשום דבר שנרשם עדיין במורד הזרם, ומחליף את קוד המשטח שפענוחו מבוסס-פאולי. מחיר המעבר הוא חומרה, לא תוכנה: 2× קיוביטים פיזיים ובדיקה בכל מחזור במסילה כפולה, מס הנאמנות המטא-יציב באטומים, ועוד מפענח שנותן לקשתות המחוקות משקל אפס. הוא אינו מתנגש עם דבר באופן פורמלי, אך מתחרה בזיכרון ה-qLDPC של IBM על אותו תקציב G4 [R][G:IBM-ROADMAP]. מחנה האטומים ומחנה מוליכי-העל חולקים תוצר אחד, המפענח. נושא קיוביט מיוצר עם מבנה שגיאה של מחיקה הוא אמיתי במסילה כפולה; האטומים מביאים את המחיקה כנושא קיוביט טבעי. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס בארכיטקטורה: 2.8 µs במסילה כפולה (מוגבל בשערים, ארבע שכבות של 0.5 µs מעל הבדיקה של 0.40 µs), 1.3 ms באטומים (הובלה); הקוד רוכב על ה-d₂ של הקוד המארח ואינו מוסיף איבר. משבצות סמוכות: קודי qLDPC מותאמי-מחיקה (לא נמצאה הדגמה), המפענח בשלב הקר, ובעמודה הסמוכה, חישוב פוטוני מבוסס-היתוך באובדן נסבל של 10.4% להיתוך [S][179], שבו Xanadu מדווחת ב-2026 על אובדן 24.1× מעל הסף [R][G:XANADU-SPAC-2026-03].

## ראיות — כיצד נמדדו המספרים

המספרים הבולטים הם קצבי דעיכה לוגית כתלות בזמן ההחזקה, מפוענחים עם דגלים ובלעדיהם (Princeton) [D][142], או יחסי שגיאות מגולות בין מרחקים במעגל של ארבעה סבבים (ה-2.14(13)× של Harvard) [D][4]; Λ מסומלץ מגיע מרעש מעגל בסגנון Stim עם הטיה מונחת [S][84]. מה שלא נלכד: בחירה בדיעבד — נאמנויות הטלפורטציה של Princeton, 0.771(9) → 0.802(8), מותנות בסינדרומים טריוויאליים ובדגל [D][142]; ארבעה סבבים אינם זיכרון לאורך 10⁵ סבבים; הסימולציה של Λ ≈ 27 מניחה בדיקות מושלמות, ללא שליליים שגויים וללא דה-פאזה מושרית-בדיקה [S][84]; איש אינו מדווח על הישרדות לצד Λ. שחזורים עצמאיים: Harvard/QuEra [D][4], Microsoft/Atom [D][149], Princeton [D][142]; תאוריה מ-AWS [S][334], [683], [684], Yale [S][395], [643], Duke [S][392]. סתירות: (i) הרווח של [[4,2,2]] הוא 1.9(4)× ב-arXiv v1 ו-v2 (2026-06-23) [D][142] אך 3.6× בגרף הטכנולוגיות מתוך הטקסט ב-Nature Physics [D][142] [G:PRINCETON-ERASURE-2026-06]; הטקסט שפורסם חסום בתשלום, ו-1.9(4)× הוא הערך שבשימוש. (ii) המרה של 98% [S][8] לעומת 38–56% שנמדדו [D][141], [142]. (iii) Λ ≈ 27 [S][84] לעומת Λ = 2.14(2) בחומרה הטובה ביותר שפענוחה מבוסס-פאולי [D][1] — פער בין סימולציה לחומרה.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הוא עושה עם קודים מותאמי-מחיקה | ראיות |
|---|---|---|---|---|
| Quantum Circuits (יחידה של D-Wave) | מפתח | ארה״ב | קיוביטי מהוד במסילה כפולה; סימולציית Λ ≈ 27; מערכת של 17 קיוביטים צפויה ב-2026 | [D][84] [C][15] |
| AWS Center for Quantum Computing | מפתח | ארה״ב | תאוריה וחומרה של טרנסמונים במסילה כפולה; אופטימיזציה של לוח זמני הבדיקות | [S][334], [683] [D][85] |
| Yale University | מחקר | ארה״ב | קודי XZZX למחיקה מוטה; תאוריה של בדיקות לא מושלמות; שותפה ב-C2QA | [S][395], [643] [G][686] |
| Princeton University | מחקר | ארה״ב | המרה למחיקה ב-¹⁷¹Yb; הקיוביט הלוגי הראשון שפוענח עם דגלי מחיקה | [S][8] [D][142] |
| Harvard University | מחקר | ארה״ב | פענוח מודע-אובדן של קוד משטח על 448 אטומים; מפענח מחיקה מושהה | [D][4] [S][508] |
| QuEra Computing | מפתח | ארה״ב | Libra 2028, יותר מ-256 לוגיים ב-10⁻⁶; שלב B של QBI | [R][162] [G:QBI-STAGEB-2025-11] |
| Atom Computing | מפתח | ארה״ב | מכונות ¹⁷¹Yb; תיקון אובדן עם המפענח של Microsoft; Magne | [D][149] [G:MAGNE-2025-07] |
| Google Quantum AI | מפתח | ארה״ב | HERALDED_ERASE ב-Stim; קו בסיס שפענוחו מבוסס-פאולי, Λ = 2.14; מסלול אטומים מאז 2026-03 | [P][397] [D][1] [G:GOOGLE-ATOMS-2026-03] |
| Caltech | מחקר | ארה״ב | המרה למחיקה ב-⁸⁸Sr; תאוריה של קודי מחיקה | [D][143] [S][684] |

**כספים.**
- 2024-08-15 · Quantum Circuits · סגירת סבב B · >$60 M · ARCH, F-Prime, Sequoia, Hither Creek · ≈$84 M מצטבר לפי העיתונות המקצועית · נסגר [G:QCI-FUNDING]
- 2025-11-04 · US DOE · חידוש NQISRC, C2QA (Brookhaven/Yale) · $125 M מתוך $625 M על פני עד חמש שנים · תוכנית · הוענק [G][474], [686]
- 2025-11-06 · שלב B של DARPA QBI · עד $15 M לכל אחד · Atom Computing, QuEra בין אחד-עשר; אף ספק של מסילה כפולה · רשמי [G][65] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · רוכשת את Quantum Circuits · $550 M ($300 M במניות + $250 M במזומן) · נסגר 2026-01-19/20 [C][14] [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; Atom Computing · מכתבי כוונות של CHIPS ממשרד המסחר האמריקאי · $100 M לכל אחת · מכתב כוונות [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · סבב C · $100 M · Third Point · >$300 M מצטבר · נסגר [G:ATOM-300M-2026-06]
- 2026-08-06 · D-Wave · תוצאות Q2-2026 · הכנסות $3.1 M, מזומן $546.2 M; מענק NSF של $1.57 M לעבודה על מודל השערים · דווח [C][15] [G:DWAVE-FIN-2026]

**שוק ושרשרת אספקה.** איש אינו מוכר קוד מותאם-מחיקה; המפענחים הם קוד פתוח (Stim, PyMatching, Union-Find) [P][397] ומימושי ה-FPGA אקדמיים [D][685], ולכן הכסף נמצא בתקורת החומרה: שני טרנסמונים או שני מהודים ועוד קיוביט עזר לכל אתר, או מכלול מטא-יציב ומצלמה. סיכון הריכוזיות הוא שרשרת הקריאה של המסילה הכפולה והמקררים, הרשומים אצל BIS [G][301]; באטומים — ערכת הלייזרים של ¹⁷¹Yb/⁸⁸Sr. G3 ו-G4 קונים את הקוד המלא; G2 ו-G1 משלמים כבר היום על *גילוי* מחיקות כבחירה בדיעבד (Seeker [C][86], סימולטור הרידברג של Caltech עם השמטת מחיקות [D][143]); G5–G7 אינם משלמים.

**קניין רוחני ותקנים.** Amazon Technologies, US 11,748,652 B1, דעיכת ריסון-משרעת מבושרת לתיקון שגיאות (Kubica, Retzker; הוענק 2023-09-05) [G][336] [G:AMZN-ERASURE-PATENT]; Yale, US 12,288,135, קיוביט עזר בעל ערוץ שגיאה אסימטרי (הוענק 2025-04-29) [G][408]; משפחות המהודים של Quantum Circuits נמצאות בידי D-Wave. אף פטנט מחיקה של Princeton או של Harvard לא עלה בחיפושים שנערכו; לא נמצאה ספירה במאגר. אין תקן; HERALDED_ERASE של Stim [P][397] הוא הממשק בפועל; D-Wave הכריזה על סימולטור עתידי של מודל השערים ל"תכנות מודע-שגיאות" [C][15].

**מפות דרכים ועמידה בהבטחות.**
- D-Wave: הובטח 2026-01-07 · מערכת מסילה כפולה ראשונה ב-2026 · לא סופקה נכון ל-2026-09-03; נוסחה מחדש ב-2026-08-06 כמערכת של 17 קיוביטים עם שגיאה לוגית 2× מתחת לפיזית ב-2026 [C][14], [15].
- D-Wave: הובטח 2026-06-01 · 49 קיוביטים / 20× (2027), 181 / 2,000× (2028), 10 לוגיים (2030), 100 לוגיים (2032), Λ = 10 · תלוי ועומד [R][94] [G:DWAVE-QCI-2026-01].
- QuEra: הובטח 2024-01 · 100 קיוביטים לוגיים ב-2026 · הוחמץ; נוסח מחדש ב-2026-06-15 כ-Libra, יותר מ-256 לוגיים ב-10⁻⁶ ב-2028 [R][162] [G:QUERA-LIBRA-2026].
- Atom Computing/Microsoft: הובטח 2025-07-17 · Magne, 50 קיוביטים לוגיים, אספקה סביב המעבר מ-2026 ל-2027 · תלוי ועומד [G:MAGNE-2025-07].
אמינות: Quantum Circuits/D-Wave מפרסמות את הפיזיקה ומחמיצות את התאריכים; Harvard/QuEra מספקות מאמרים בזמן, מפות דרכים באיחור; Microsoft/Atom בזמן, שותקות בעניין הקוד; AWS מפרסמת ואינה מבטיחה דבר; Princeton מספקת כל שלב בהצעתה מ-2022 [S][8], קטן מהמובטח.

**פרשנות אסטרטגית.** אם קודים מותאמי-מחיקה יגיעו ל-Λ ≥ 5 בחומרה, המנצחים הם בעלי קיוביטים עם מחיקה מובנית בקנה מידה — קו המהודים של D-Wave, זוגות הטרנסמונים של AWS, מחנה ה-¹⁷¹Yb (Atom Computing, מסלול האטומים של Google) — והמפענח הופך למצרך; המפסידים הם מפות דרכים של פאולי בלבד, הקונות Λ בנאמנות לבדה (קו מוליכי-העל של Google, ה-qLDPC של IBM), וספקי רובידיום ללא מכלול מטא-יציב. התחלופה פועלת לשני הכיוונים: פענוח מחיקה מושהה [S][508] ובדיקות-על [D][4] נותנים לאטומים את רוב הרווח בלי קיוביטים עם מחיקה מובנית; קידודי מחיקה בקיוטריטים היו מסירים מהטרנסמונים את התקורה של 2×. כוח המיקוח נמצא אצל ספקי הפלטפורמות; למחברי המפענחים אין כוח מיקוח.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם: קבוצה כלשהי תפענח זיכרון d = 3 → 5 עם דגלי מחיקה לאורך ≥ 10 סבבים ותדווח על Λ ≥ 3 עם הישרדות; מערכת 17 הקיוביטים של D-Wave תראה שגיאה לוגית 2× מתחת לפיזית עד אמצע 2027 [C][15]; סימולציה של מסילה כפולה עם שליליים שגויים נמדדים ודה-פאזה של הבדיקה עדיין תחזיר Λ ≥ 10; ההמרה באטומים תחת שערים דו-קיוביטיים תעבור 70%. להוריד בדרגה אם סוף 2027 יגיע כשפענוח מחיקה שווה < 2× בכל פלטפורמה. התרחיש הטוב ביותר עד 2029: זיכרונות במסילה כפולה ב-Λ ≈ 5–10 עם 100–200 קיוביטים, ומכונות Yb שמריצות קודים מודעי-אובדן כברירת מחדל. התרחיש הגרוע ביותר: אפשרות פענוח ששווה 1.7–1.9×, בעוד טרנסמונים שפענוחם מבוסס-פאולי מגיעים ל-Λ ≈ 3–4 בלעדיה.

שאלות פתוחות: (1) מהו Λ ברגע ששליליים שגויים מצטברים כדליפה לאורך 10³ סבבים? (2) האם ההטיה של 40:1 שורדת שערים מקביליים על קווי קריאה משותפים? (3) האם אפשר להסיר את מס הנאמנות המטא-יציב ב-Yb? (4) האם קוד qLDPC מותאם-מחיקה עם מפענח מהיר אפשרי? לעקוב: האספקה של D-Wave ב-2026, המאמר הרב-קיוביטי הבא של AWS, תוצאות ה-Yb של Google/Kaufman.

פענוח מודע-למחיקות פועל גם בממשק פוטוני בין מעבדי קוד המשטח: עם פעולות מקומיות אידיאליות, הסף לתוצאות היתוך שנמחקו מגיע לתקרת חלחול הקשתות של 50% בסריג הריבועי (ערך מותאם: 49.40–50.60% ב-d = 11–19), השקולה לאובדן פוטונים של 18.35% ללא היתוך מוגבר, והוא יורד בקירוב ליניארית עם שגיאת מצבי המשאב, ובקצב הולך וגובר ככל שרעש המעגל המקומי מתקרב לסף שלו עצמו [P][893]. התוצאה היא מסימולציה בלבד.

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[15] D-Wave Quantum Inc., “D-Wave Reports Second Quarter 2026 Results,” Aug. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[84] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [S]
[85] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026. [D]
[86] Quantum Circuits, “Quantum Circuits Makes Error-Detecting Qubits,” Nov. 19, 2024. [Online]. Available: https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/ [C]
[94] M. Swayne, “D-Wave's New Gate-Model Roadmap Puts Pin in 2032 For 100 Logical-Qubit System,” The Quantum Insider, Jun. 1, 2026. [Online]. Available: https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/ [R]
[141] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493). [D]
[142] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[143] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[149] B. W. Reichardt *et al.*, “Fault-tolerant quantum computation with a neutral atom processor,” [arXiv:2411.11822](https://arxiv.org/abs/2411.11822), Nov. 2024. [D]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[179] S. Bartolucci *et al.*, “Fusion-based quantum computation,” *Nat. Commun.*, vol. 14, Art. no. 912, Feb. 2023, doi: [10.1038/s41467-023-36493-1](https://doi.org/10.1038/s41467-023-36493-1). [arXiv:2101.09310](https://arxiv.org/abs/2101.09310). [S]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[334] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461). [S]
[336] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]
[392] M. Kang, W. C. Campbell, and K. R. Brown, “Quantum Error Correction with Metastable States of Trapped Ions Using Erasure Conversion,” *PRX Quantum*, vol. 4, no. 2, Art. no. 020358, Jun. 2023, doi: [10.1103/PRXQuantum.4.020358](https://doi.org/10.1103/PRXQuantum.4.020358). [arXiv:2210.15024](https://arxiv.org/abs/2210.15024). [S]
[395] K. Chang *et al.*, “Surface Code with Imperfect Erasure Checks,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040355, Dec. 2025, doi: [10.1103/d1v7-nctj](https://doi.org/10.1103/d1v7-nctj). [S]
[397] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[399] J. D. Teoh *et al.*, “Dual-rail encoding with superconducting cavities,” *Proc. Natl. Acad. Sci. USA*, vol. 120, no. 41, Art. no. e2221736120, Oct. 2023, doi: [10.1073/pnas.2221736120](https://doi.org/10.1073/pnas.2221736120). [arXiv:2212.12077](https://arxiv.org/abs/2212.12077). [S]
[406] W. Huang *et al.*, “Logical multi-qubit entanglement with dual-rail superconducting qubits,” *Nat. Phys.*, vol. 22, no. 4, pp. 591–597, Mar. 2026, doi: [10.1038/s41567-026-03211-9](https://doi.org/10.1038/s41567-026-03211-9). [arXiv:2504.12099](https://arxiv.org/abs/2504.12099). [D]
[408] Justia, “Shruti PURI Inventions, Patents and Patent Applications - Justia Patents Search.” [Online]. Available: https://patents.justia.com/inventor/shruti-puri [G]
[474] US Department of Energy, “Energy Department Announces $625 Million to Advance the Next Phase of National Quantum Information Science Research Centers,” Energy.gov, Nov. 4, 2025. [Online]. Available: https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information [G]
[508] G. Baranes *et al.*, “Leveraging Qubit Loss Detection in Fault-Tolerant Quantum Algorithms,” *Phys. Rev. X*, vol. 16, no. 1, Art. no. 011002, Jan. 2026, doi: [10.1103/ycwc-3myc](https://doi.org/10.1103/ycwc-3myc). [arXiv:2502.20558](https://arxiv.org/abs/2502.20558). [S]
[643] K. Sahay, J. Jin, J. Claes, J. D. Thompson, and S. Puri, “High-Threshold Codes for Neutral-Atom Qubits with Biased Erasure Errors,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041013, Oct. 2023, doi: [10.1103/PhysRevX.13.041013](https://doi.org/10.1103/PhysRevX.13.041013). [arXiv:2302.03063](https://arxiv.org/abs/2302.03063). [S]
[645] J. W. Lis *et al.*, “Mid-circuit operations using the omg-architecture in neutral atom arrays,” [arXiv:2305.19266](https://arxiv.org/abs/2305.19266), May 2023. [D]
[679] T. M. Stace, S. D. Barrett, and A. C. Doherty, “Thresholds for Topological Codes in the Presence of Loss,” *Phys. Rev. Lett.*, vol. 102, no. 20, Art. no. 200501, May 2009, doi: [10.1103/PhysRevLett.102.200501](https://doi.org/10.1103/PhysRevLett.102.200501). [arXiv:0904.3556](https://arxiv.org/abs/0904.3556). [S]
[680] N. Delfosse and G. Zémor, “Linear-time maximum likelihood decoding of surface codes over the quantum erasure channel,” *Phys. Rev. Res.*, vol. 2, no. 3, Art. no. 033042, Jul. 2020, doi: [10.1103/PhysRevResearch.2.033042](https://doi.org/10.1103/PhysRevResearch.2.033042). [arXiv:1703.01517](https://arxiv.org/abs/1703.01517). [S]
[681] N. Delfosse and N. H. Nickerson, “Almost-linear time decoding algorithm for topological codes,” *Quantum*, vol. 5, Art. no. 595, Dec. 2021, doi: [10.22331/q-2021-12-02-595](https://doi.org/10.22331/q-2021-12-02-595). [arXiv:1709.06218](https://arxiv.org/abs/1709.06218). [S]
[682] R. Stricker *et al.*, “Experimental deterministic correction of qubit loss,” *Nature*, vol. 585, no. 7824, pp. 207–210, Sep. 2020, doi: [10.1038/s41586-020-2667-0](https://doi.org/10.1038/s41586-020-2667-0). [arXiv:2002.09532](https://arxiv.org/abs/2002.09532). [D]
[683] S. Gu, Y. Vaknin, A. Retzker, and A. Kubica, “Optimizing Quantum Error-Correction Protocols with Erasure Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040354, Oct. 2025, doi: [10.1103/985g-58gd](https://doi.org/10.1103/985g-58gd). [S]
[684] S. Gu, A. Retzker, and A. Kubica, “Fault-tolerant quantum architectures based on erasure qubits,” *Phys. Rev. Res.*, vol. 7, no. 1, Art. no. 013249, Mar. 2025, doi: [10.1103/PhysRevResearch.7.013249](https://doi.org/10.1103/PhysRevResearch.7.013249). [arXiv:2312.14060](https://arxiv.org/abs/2312.14060). [S]
[685] N. Liyanage, Y. Wu, A. Deters, and L. Zhong, “Scalable Quantum Error Correction for Surface Codes using FPGA,” [arXiv:2301.08419](https://arxiv.org/abs/2301.08419), Jan. 2023. [D]
[686] Brookhaven National Laboratory, “DOE Renews Brookhaven Lab-led Quantum Research Center,” BNL Newsroom, Nov. 4, 2025. [Online]. Available: https://www.bnl.gov/newsroom/news.php?a=122687 [G]
[893] F. Burt *et al.*, “Loss-tolerant distributed lattice surgery using fusion networks,” [arXiv:2610.01923](https://arxiv.org/abs/2610.01923), Oct. 2026. [P]

## פריטי אימות פתוחים

- רווח מידע המחיקה של [[4,2,2]]: 1.9(4)× ב-arXiv:2506.13724 v1 ו-v2 (2026-06-23) [D][142] לעומת 3.6× בגרף הטכנולוגיות מתוך Nature Physics 22, 910 [D][142]; הטקסט שפורסם חסום בתשלום; 1.9(4)× בשימוש.
- Gu, Retzker, Kubica [S][684]: הספים פורסמו כמשטחים, לא כערכים בודדים; תוצאה איכותית בלבד.
- Kang, Campbell, Brown [S][392]: מספר המאמר ב-PRX Quantum 4 (2023) לא אושר.
- לא נמצאה משפחת פטנטים למחיקה של Princeton או של Harvard בשני חיפושי פטנטים; ההיעדר לא הוכח.
- מיני האטומים הניטרליים של planqc ושל Google לא אושרו ממקורות נגישים; אף אחד מהם אינו נטען.
- פענוח ב-FPGA עם דגלי מחיקה: אין מדד ביצועים שפורסם; 11.5 ns לסבב [D][685] הם לרעש פנומנולוגי.
- עלות או אנרגיה לכל קיוביט לוגי: לא פורסמו על ידי אף שחקן.
- הטענה של D-Wave על "$1.57 מיליון במימון NSF לפיתוח מודל השערים" [C][15]: המענק לא זוהה.
