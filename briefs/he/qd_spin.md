---
id: qd_spin
name: ספין בנקודה קוונטית המוגדרת באלקטרודות שער (Si/SiGe, Si-MOS, Ge)
layer: "1 נושא הקיוביט"
status: demonstrated
since: 2012
one_line: "ספין של אלקטרון או של חור בנקודה שאלקטרודות השער שלה מוגדרות בליתוגרפיה; החילוף נותן שערים דו-קיוביטיים דטרמיניסטיים בסדר גודל של ns על פיסת CMOS."
verdict: "הנושא היחיד המיוצר בקנה מידה על קו של 300 mm, אך הנאמנות הדו-קיוביטית תקועה זה שנה על 99.0-99.6% בהתקני בית יציקה, ואף מערך של יותר מ-12 קיוביטים לא פרסם נתונים לכל הזוגות."
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

אלקטרון או חור לכודים בבור אלקטרוסטטי שקוטרו ~50 nm, הנוצר בידי אלקטרודות שער מתכתיות מעל בור קוונטי של Si/SiGe, שכבת היפוך של Si-MOS או גז חורים של Ge/SiGe. הספין הוא דרגת החופש החישובית; המחסום בין נקודות שכנות קובע צימוד חילוף J, ופולס של J למשך ħπ/J נותן שער שזירה דטרמיניסטי. Loss ו-DiVincenzo הציעו את הארכיטקטורה ב-1998; קיוביטי הספין היחיד והסינגלט–טריפלט הראשונים בסיליקון הופיעו ב-2010–2012, וזהו תאריך השושלת שבו משתמשים כאן.

תכונות, כפי שרשומת הגרף רושמת אותן:
- **a — זיקה:** 1.0, מיוצר לחלוטין; כל נקודה היא תוצר של ליתוגרפיה.
- **b — זמן אופייני:** ~50 ns לפעולה, שזירה **דטרמיניסטית** דרך החילוף, לא מבושרת.
- **c — קריאה:** המרת ספין-למטען בחיישן מטען rf, ~6 µs, לא הרסנית, אפשרית באמצע המעגל.
- **d — ניידות:** סטטי, אלא אם מופעל מנגנון הסעה נפרד.
- **e — בקרה:** מתחי שער בפס בסיס ועוד הנעת מיקרוגל או EDSR, והאלקטרוניקה בדרך כלל בטמפרטורת החדר.
- **f — מבנה השגיאה כפי שהקוד רואה אותו:** קוהרנטית, פאולי, ודליפה למצבי עמק או מטען.
- **g — ייצור:** CMOS.

## פיזיקה וגבולות

שלושה סולמות אנרגיה שולטים בכול. פיצול זימן (~10–100 µeV ב-0.3–1 T) מגדיר את הקיוביט; החילוף J, הניתן לכוונון בטווח 10–100 MHz, מגדיר את השער; פיצול העמקים בסיליקון (0.1–0.3 meV, לא אחיד משום שהוא עוקב אחר חספוס הממשק) מגדיר את רצפת הדליפה. בנקודות חורים ב-Ge אין ניוון עמקים ואין צורך במיקרו-מגנט, אך צימוד הספין–מסלול שלהן הופך רעש חשמלי ישירות לדה-פאזה.

שני אמבטים קובעים את רצפת הקוהרנטיות. את הספינים הגרעיניים אפשר לדכא: העשרת ²⁸Si נותנת T2 בהד האן של 1.31(4) ms בחומר של בית יציקה ו-T2* בניסוי ראמזי של 41(2) µs [D][197]. את רעש המטען אי אפשר — מקורות תנודות 1/f בתחמוצת מצטמדים דרך החילוף, ולכן הנאמנות יורדת בדיוק כאשר J פועל: אינטראקציית השזירה היא גם ערוץ הרעש השולט. השגיאות מגיעות לקוד כסיבוב-יתר/סיבוב-חסר קוהרנטי, כדה-פאזה מסוג פאולי וכדליפה שקודי חזרה וקודי משטח מחמיצים בלי יחידות להפחתת דליפה. הפירוק של HRL הוא האמירה היחידה המועילה ביותר על מקומה של השגיאה: כ-**80% משגיאת ה-CNOT שלה חיצוניים — בקרה וכיול, לא פיזיקה** [D][190]. הזזת הרצפה מחייבת דיאלקטריקים שקטים יותר, פיצול עמקים אחיד יותר וכיול טוב יותר — בסדר הזה של קושי, ובסדר ההפוך של עלות.

## מצב ההנדסה העדכני

המיטב שהודגם נכון ל-3 בספטמבר 2026: נאמנות דו-קיוביטית של 99.04–99.56% בהתקן Si-MOS מבית יציקה של 300 mm [D][189]; 18 קיוביטים במערך אחד, פעמיים, על חומרים שונים [D][190][D][195]. הטיפוסי בקנה מידה גרוע יותר, והפער הוא העיקר — ההתקן של imec בן שמונת הקיוביטים על 300 mm אימת שער דו-קיוביטי **באחד מתוך ארבעה** זוגות של נקודות כפולות [D][197]. אף התקן של יותר מ-12 קיוביטים בפלטפורמה זו לא פרסם נאמנויות דו-קיוביטיות לכל הזוגות.

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2022-01 | 2Q 99.5% (טומוגרפיית ערכת שערים), Si/SiGe — החצייה הראשונה של סף קוד המשטח | QuTech/TU Delft | [D][346] |
| 2024-03 | 2Q 98.9% בטמפרטורת פעולה של 1 K | Diraq/UNSW | [D][194] |
| 2025-09 | 2Q 99.04–99.56%, SPAM 99.9%, על Si-MOS מבית יציקה של 300 mm | Diraq + imec | [D][189] |
| 2026-04 | מערך Ge של 2×N בן 18 קיוביטים; 1Q ממוצע 99.8%, חציון 99.9% | Groove Quantum + QuTech | [D][195] |
| 2026-05 | CZ בין שני ספינים *נעים*, 98.86 ± 0.29%, 58 ns | QuTech/TU Delft | [D][193] |
| 2026-07 | התקן 300 mm בן 8 קיוביטים; T2 בהד האן 1.31 ms; 2Q ב-1 מתוך 4 זוגות | imec + Diraq | [D][197] |
| 2026-07 | 18 קיוביטים בחילוף בלבד מ-54 נקודות; 1Q 2×10⁻⁴, CNOT 3×10⁻³; קוד חזרה ב-d=5, 200 סבבים, Λ₅/₃ = 4.7 | HRL Laboratories | [D][190] |

איבר השגיאה השולט כיום אינו דה-קוהרנטיות, אלא סחיפת כיול: 54 נקודות דורשות מאות מתחים התלויים זה בזה, ומרחב הכוונון — לא T2 — הוא שמגביל את גודל המערך.

## ייצור, חומרים ושרשרת האספקה

הטענה המבדלת היא ייצור בקווי CMOS שלא שונו — Intel מדווחת על >24,000 התקנים לפרוסת EUV של 300 mm [D][199] ועל 96% הצלחה בכוונון ב-232 התקנים בני שתים-עשרה נקודות בפרוסה אחת [D][766], ו-Quantum Motion אפיינה 1,024 נקודות בחמש דקות על 22FDX של GlobalFoundries [C][200]. פרטי התהליך שייכים לתקציר על מפעל CMOS של 300 mm; סטטיסטיקה בקנה מידה של פרוסה קיימת כאן, ואינה קיימת לאף נושא אחר.

החומרים הם נקודת החשיפה. ²⁸Si מועשר הוא נקודת כשל יחידה של ממש: **ASP Isotopes החלה בייצור מסחרי של סיליקון-28 מועשר במתקן השני שלה ב-Pretoria ב-2025-03-27**, עם שני לקוחות אמריקאים שזהותם לא נמסרה [C][347]. ב-2026-07-16 הודיע ה-US DOE Office of Isotope R&D and Production כי ORNL ו-PNNL מייצרות כעת סילאן ב-99.9999% ²⁸Si וגרמאן עם Ge-73 מתחת ל-1 ppm, מדולדל "לפחות 100×" יותר מכל חומר מסחרי — החזרה מכוונת של הייצור לארה״ב [G][348]. הטרו-מבנים של Ge/SiGe מגיעים מקומץ כורי גידול אקדמיים (הקבוצה של Scappucci ב-Delft) — צוואר בקבוק צר יותר מן המפעל. החשיפה לפיקוח יצוא עקיפה: הפיסות הן CMOS רגיל, אך איזוטופים מועשרים ומקררי דילול כפופים למגבלות הקוונטים הרב-צדדיות של 2024 (US ECCN 3A901/3A904).

## בקרה, קריאה ועומס הקלט-פלט

מתחים בפס בסיס ועוד הנעת מיקרוגל או EDSR לכל קיוביט, וחיישן רפלקטומטריית rf אחד לכל נקודה אחת עד כמה נקודות. אין לייזרים — בעיית הקלט-פלט היא מספר הקווים והחום. הבקר של HRL ב-4 K (≤3.5 W באופן טיפוסי, 366 DAC, 296 קווים) תזמן ניסוי QEC מלא של 18 קיוביטים בלי אלקטרוניקת זמן אמת בטמפרטורת החדר [D][190]; UNSW/Diraq הראו CMOS קריוגני ב-mK לצד הקיוביטים [D][203]. הבקרים האלה הם נושאו של התקציר על בקרת CMOS קריוגני.

הקיר הוא הקריאה, לא השערים. עם ~6 µs של המרת ספין-למטען ועוד זמן התייצבות, המחזור מגיע למאות מיקרו-שניות — שלושה סדרי גודל איטי יותר מן השער של 50 ns, ולכן סבב הסינדרום קובע את השעון הלוגי. ב-10³ קיוביטים אפשר לשרוד את מספר הקווים רק במיעון crossbar בקווים משותפים; ב-10⁴ שולטים מספר החיישנים ופיזור החום; ב-10⁶ לא שורדים לא קווים ייעודיים ולא חיישנים לכל קיוביט.

## תפקיד במחסנית

הטכנולוגיה יושבת על ארכיטקטורה אחת, **ספינים בנקודות קוונטיות בסיליקון / גרמניום**. היא דורשת מפעל CMOS של 300 mm; היא מספקת את הנקודות שצורכים שערי החילוף, קידוד החילוף-בלבד והסינגלט–טריפלט, הסעת הספינים במצב מסוע, בקרת ה-crossbar בקווים משותפים וקריאת הספין-למטען. היא מחליפה ספינים דונוריים (הזרחן הממוקם בדיוק של SQC), הקונים שערים של 99.10–99.99% על 11 קיוביטים [D][192] במחיר של היעדר מסלול לבית יציקה — מחיר המעבר בשורה אחת.

השעון הנגזר של הארכיטקטורה = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס = **8.5 µs**, מהם 6.3 µs קריאה ו-1 µs איפוס. כל מה שהטכנולוגיה מאפשרת נמצא במורד הזרם ממנה, ולכן לכשל כאן אין חלופה במקום אחר. המשבצת הריקה השכנה היא קריאה מהירה ללא חיישן — חסימת ספין פאולי מתחת ל-1 µs, בנאמנות >99.9%; דבר בגרף אינו ממלא אותה.

## ראיות — כיצד נמדדו המספרים

המספרים הדו-קיוביטיים שבכותרות מגיעים ממדידת ביצועים אקראית משולבת (interleaved RB) או מטומוגרפיית ערכת שערים על הזוג הטוב ביותר בפיסה — פרוטוקול לגיטימי המדווח סיכום לא לגיטימי, שאינו לוכד לא הפרעה הדדית ולא סחיפת כיול. קוד החזרה של HRL ב-d=5 לאורך 200 סבבים הוא תוצאת הספין היחידה המודדת שגיאה *באתרה*, תחת פעולה רציפה, וה-Λ₅/₃ = 4.7 שלו [D][190] נוגע להיפוך ביט בלבד, ואינו זיכרון לוגי מתחת לסף — דבר שאף פלטפורמת ספין לא הראתה.

סתירות. המסרים של Diraq סותרים זה את זה בעניין קנה המידה: הודעה מ-2026-07-09 אמרה "אלפי קיוביטים עד 2029", ומפת הדרכים מ-2026-08-27 אומרת 150,000 פיזיים ו-1,000 לוגיים עד 2029 [R][211][G:DIRAQ-FUNDING]; יש לקבל את מפת הדרכים כעמדת החברה, ואת הפער כראיה על החברה. אין שחזור של התוצאה הדו-קיוביטית על 300 mm מחוץ לקו של imec.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים | ראיות |
|---|---|---|---|---|
| Diraq | מפתח | אוסטרליה | קיוביטי Si-MOS על 300 mm של imec; 2Q 99.04–99.56%; פעולה ב-1 K | [D][189][D][194] |
| HRL Laboratories | מפתח | ארה״ב | SiGe בחילוף בלבד, 18 קיוביטים, QEC ב-d=5 בתזמון עצמי | [D][190] |
| IBM | משקיע | ארה״ב | רכשה את HRL; מוסיפה ספינים למפת דרכים של מוליכי-על | [C][204] |
| Intel | מפתח | ארה״ב | התקני ספין ב-EUV על 300 mm; Tunnel Falls בן 12 קיוביטים ב-Argonne | [D][199][P][207] |
| Quantum Motion | מפתח | בריטניה | נקודות ב-22FDX; מערכת CMOS שלמה, בכל שכבותיה, סופקה ל-NQCC | [C][200] |
| QuTech (TU Delft) | מחקר | הולנד | שערים בספינים מוסעים, בדיקות זוגיות, הטרו-מבנים של Ge | [D][193][D][349] |
| Groove Quantum | מפתח | הולנד | מערך Ge בן 18 קיוביטים; יצאה מתוכנית ה-Ge של Delft | [D][195] |
| Quobly | מפתח | צרפת | אצוות FD-SOI של ²⁸Si ב-ST Crolles מאז 2025-12 | [C][350] |
| Equal1 | מפתח | אירלנד | יחידת מסד בת שישה קיוביטים, שנמכרה בשם Bell-1 ומאז מאי 2026 בשם RacQ; הותקנה ב-ESA Frascati ביולי 2026 | [C][351] [G:ESA-BELL1-2026-07] [G:EQUAL1-RACQ-ESA-2026-07] |
| SemiQon | ספק | פינלנד | חברה שיצאה מ-VTT; שבבי CMOS קריוגני המיוצרים ב-Espoo | [P][352] |
| GlobalFoundries | ספק | ארה״ב | יחידת Quantum Technology Solutions; פרוסות 22FDX | [C][353] |

**כספים.**

- 2025-02-24 · SemiQon · סבב · €17.5 M (€15 M הון + €2.5 M מענק) · European Innovation Council · נסגר [P][354]
- 2025-11-06 · Diraq, Quantum Motion, SQC · שלב B של DARPA QBI · עד $15 M לכל אחת · DARPA · שלוש מתוך אחת-עשרה · הוכרז [G:QBI-STAGEB-2025-11][65]
- 2026-01-15 · Equal1 · סבב · $60 M · ISIF · >$85 M במצטבר · נסגר [C][G:EQUAL1-60M-2026-01][351]
- 2026-04-30 · Groove Quantum · סבב · €16 M · לא נמסר · €26 M במצטבר · נסגר [P][G:GROOVE-2026]
- 2026-05-07 · Quantum Motion · סבב C · $160 M · DCVC, Kembara · נסגר [C][355]
- 2026-05-21 · Diraq · מכתב כוונות של US CHIPS · עד $38 M · Dept of Commerce · LOI [G][300]
- 2026-05-21 · GlobalFoundries · LOI של US CHIPS, בית יציקה קוונטי רב-מודאלי · $375 M · Dept of Commerce · LOI [G][300][C][353]
- 2026-06-03 · Quobly · סבב A · €115 M · Bpifrance, SEALSQ, STMicroelectronics · €134 M במצטבר · נסגר [C][350]
- 2026-06 · Silicon Quantum Computing · NRFC (מסלול הדונורים) · A$60 M · Australia NRFC · נסגר [G:SQC-NRFC-2026]
- 2026-07-03 · SemiQon · השקעה אסטרטגית · לא נמסר · PostScriptum · נסגר [P][352]
- 2026-08-26 · IBM / HRL · מיזוג ורכישה **הושלמו** (הוכרזו ב-2026-07-23) · התנאים לא נמסרו · המוכרות Boeing ו-General Motors, שעדיין שותפות ליישומים · סופי [C][204]

**שוק ושרשרת אספקה.** איש אינו מוכר קיוביטי ספין; הסחורות הנמכרות הן הרצות בבית יציקה, איזוטופים מועשרים ואלקטרוניקה קריוגנית. גישה לבית יציקה נקנית מ-imec, מ-GlobalFoundries ומ-STMicroelectronics, כאשר GF הפכה אותה ב-2026 למוצר של יחידה עסקית ומונה את Diraq, Equal1 ו-Quantum Motion כלקוחות [C][353]. אספקת האיזוטופים היא הסיכון המרוכז — יצרן מסחרי אחד בקנה מידה, ועוד יכולת מחודשת של המעבדות הלאומיות בארה״ב [C][347][G][348]. ה-"<$1 לקיוביט בשני מיליון קיוביטים" של Diraq [R][211] הוא תחזית, לא מחיר. מה שמשלם כיום הוא G3 (עבודת ה-QEC של HRL, שלב B של QBI) ו-G7 (Quantum Motion ב-NQCC, Equal1 ב-ESA); דבר כאן אינו נקנה עבור G1, G2 או G5.

**קניין רוחני ותקנים.** המבט המתוארך היחיד ממאגר נתונים שזמין — ניתוח של PatSnap מ-2026-06-02, שעודכן ב-2026-08-21 — דל: ~60 רשומות בשנים 2005–2026, ו-NewSouth Innovations (UNSW, שורש הרישוי של Diraq) היא הגדולה, עם חמש בקשות, לפני SIAT/SIMIT, MIT, Intel ו-SQC [P][356]. קטן מכדי להיות מפקד. לא נרשמה התדיינות משפטית, אין גוף תקינה ייעודי לספינים, והקניין הרוחני של הבקר של HRL אינו מתפרסם עוד, בתוך IBM.

**מפות דרכים ועמידה בהבטחות.** Diraq (הובטח 2026-08-27 · ל-2029 · 150 k פיזיים / 1 k לוגיים, >2 M עד 2031) — שישה שבועות קודם לכן אמרה "אלפים עד 2029" [R][211]: לקבל את הנאמנויות, ולייחס משקל מופחת לספירות. Quobly (2026-06 · ל-2032 · מיליוני קיוביטים) — ממומנת ומייצרת ב-ST, אך ללא התקן מרובה קיוביטים שפורסם: כוונה. SQC (ל-2033 · קנה מידה מסחרי) — תוצאת דונורים אמיתית של 11 קיוביטים [D][192], שאינה ניתנת להפרכה עד 2030. Quantum Motion — השחקן היחיד שסיפק מערכת ללקוח בזמן [C][200]. Intel — 12 קיוביטים ב-Argonne, ללא שבב ממשיך וללא מפת דרכים מתוארכת נכון ל-3 בספטמבר 2026 [P][207]: חיה, אך ללא הכוונה. IBM/HRL — עדיין אין אבן דרך של ספינים ב-Starling (2029) או ב-Blue Jay (אמצע שנות ה-2030) [C][204].

**פרשנות אסטרטגית.** אם הפלטפורמה תצליח, המנצחים יהיו בתי היציקה וספקי האיזוטופים, לא מתכנני הקיוביטים: קיוביט Si-MOS הוא מתכון תהליך, ומשהוסמך, הפיסה השולית זולה והבידול עובר לתוכנת הכיול. לכן רכשה IBM את HRL — לא בשביל 18 קיוביטים, אלא בשביל מערך בקרה של CMOS קריוגני ואריזה הניתנים לשימוש חוזר בכל סוגי הקיוביטים: רכישת ספק בתחפושת של הימור על פלטפורמה. המפסידות הן חברות הזנק העוסקות בספינים בלבד, שכוח המיקוח שלהן מול בית יציקה שזה עתה הפך ייצור קוונטי למוצר הולך ונחלש. יכולת הייצור היא הטיעון היחיד של הפלטפורמה שניתן להגן עליו, ואם נאמנות ה-2Q תעמוד עדיין על 99.0–99.6% לאורך 2027, עם מערכים של פחות מ-20 קיוביטים, היא תחדל להספיק.

## תחזית ושאלות פתוחות

**לאשר** אם עד סוף 2027 קבוצה כלשהי תפרסם נאמנויות דו-קיוביטיות מעל 99% לכל הזוגות במערך של ≥16 קיוביטים, או שהתקן ספין יראה זיכרון לוגי מתחת לסף בקוד משטח במרחק 3 עד 5, או ש-IBM תציב אבן דרך מתוארכת של ספינים במפת הדרכים הפומבית שלה. **להוריד בדרגה** אם נאמנות השער הדו-קיוביטי בבית יציקה תעמוד עדיין על 99.0–99.6% באמצע 2027, אם Intel לא תפרסם הודעת ספין נוספת, או אם Diraq תתקן את נתון ה-2029 שלה כלפי מטה בפעם השנייה.

התרחיש הטוב ביותר עד 2029: כמה מאות קיוביטים פיזיים בתהליך 300 mm מוסמך, עם בקרה בקווים משותפים וזיכרון לוגי עובד — שני סדרי גודל מתחת ל-150 k של Diraq. התרחיש הגרוע ביותר: הפלטפורמה נשארת הדגמה של בית יציקה, חברות ההזנק מתאחדות לתוך IBM, GlobalFoundries ו-STMicroelectronics, וקיוביטי הספין הופכים לעסק של אלקטרוניקת בקרה שמוצמדים אליו קיוביטים.

שאלות פתוחות. (1) האם נאמנות דו-קיוביטית ברמה של 99.5% ניתנת לשחזור בכל הזוגות של פיסה, או רק בזוג שמצליחים לכוונן? (2) האם אפשר להפוך את פיצול העמקים לאחיד דיו כדי שהדליפה תחדל להיות הגרלה של כל התקן לעצמו? (3) האם הקריאה תרד מתחת ל-1 µs בלי חיישן מטען לכל קיוביט? (4) האם IBM קנתה קיוביט או מערך בקרה?

## מקורות
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[189] P. Steinacker *et al.*, “Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity,” *Nature*, vol. 646, no. 8083, pp. 81–87, Sep. 2025, doi: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9). [D]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[192] H. Edlbauer *et al.*, “An 11-qubit atom processor in silicon,” *Nature*, vol. 648, no. 8094, pp. 569–575, Dec. 2025, doi: [10.1038/s41586-025-09827-w](https://doi.org/10.1038/s41586-025-09827-w). [arXiv:2506.03567](https://arxiv.org/abs/2506.03567). [D]
[193] Y. Matsumoto *et al.*, “Two-qubit logic and teleportation with mobile spin qubits in silicon,” *Nature*, vol. 653, no. 8114, pp. 391–397, May 2026, doi: [10.1038/s41586-026-10423-9](https://doi.org/10.1038/s41586-026-10423-9). [D]
[194] J. Y. Huang *et al.*, “High-fidelity spin qubit operation and algorithmic initialization above 1 K,” *Nature*, vol. 627, no. 8005, pp. 772–777, Mar. 2024, doi: [10.1038/s41586-024-07160-2](https://doi.org/10.1038/s41586-024-07160-2). [D]
[195] J. Dijkema *et al.*, “Simultaneous operation of an 18-qubit modular array in germanium,” [arXiv:2604.01063](https://arxiv.org/abs/2604.01063), Apr. 2026. [D]
[197] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[199] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[200] Quantum Motion, “Quantum Motion Delivers the Industry's First Full-Stack Silicon CMOS Quantum Computer,” Sep. 15, 2025. [Online]. Available: https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ [C]
[203] UNSW, “UNSW engineers help crack key challenge in scaling quantum computers,” Jun. 26, 2025. [Online]. Available: https://www.unsw.edu.au/newsroom/news/2025/06/unsw-engineers-crack-challenge-scaling-quantum-computers [D]
[204] IBM, “IBM Completes Acquisition of HRL Laboratories to Accelerate the Future of Quantum,” Aug. 26, 2026. [Online]. Available: https://newsroom.ibm.com/2026-08-26-ibm-completes-acquisition-of-hrl-laboratories-to-accelerate-the-future-of-quantum [C]
[207] L. Hesla, “Argonne launches silicon quantum processor collaboration with Intel,” Argonne National Laboratory, Jan. 6, 2026. [Online]. Available: https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel [P]
[211] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[346] X. Xue *et al.*, “Quantum logic with spin qubits crossing the surface code threshold,” *Nature*, vol. 601, no. 7893, pp. 343–347, Jan. 2022, doi: [10.1038/s41586-021-04273-w](https://doi.org/10.1038/s41586-021-04273-w). [arXiv:2107.00628](https://arxiv.org/abs/2107.00628). [D]
[347] ASP Isotopes Inc., “ASP Isotopes Inc. Commences Commercial Production of Enriched Silicon-28 at its Second Aerodynamic Separation Process (ASP) Enrichment Facility,” Mar. 27, 2025. [Online]. Available: https://ir.aspisotopes.com/news-events/press-releases/detail/56/asp-isotopes-inc-commences-commercial-production-of [C]
[348] U.S. Department of Energy, “DOE Advances Domestic Supply of Silicon, Germanium Isotopes for Quantum Computing,” HPCwire, Jul. 16, 2026. [Online]. Available: https://www.hpcwire.com/off-the-wire/doe-advances-domestic-supply-of-silicon-germanium-isotopes-for-quantum-computing/ [G]
[349] B. Undseth *et al.*, “Weight-four parity checks in a spin-shuttling architecture,” *Nature*, vol. 655, no. 8125, pp. 1160–1166, Jul. 2026, doi: [10.1038/s41586-026-10766-3](https://doi.org/10.1038/s41586-026-10766-3). [D]
[350] Quobly, “Quobly secures €115 million Series A to bring silicon-based quantum computers to market,” Jun. 3, 2026. [Online]. Available: https://www.quobly.io/press-releases/quobly-secures-e115-million-series-a-to-bring-silicon-based-quantum-computers-to-market [C]
[351] Equal1, “Equal1 raises $60M to accelerate quantum computing using existing semiconductor manufacturing,” Jan. 15, 2026. [Online]. Available: https://www.equal1.com/insights/equal1-raises-60m-to-accelerate-quantum-computing-using-existing-semiconductor-manufacturing [C]
[352] M. Swayne, “PostScriptum Invests in Quantum Hardware Developer SemiQon,” The Quantum Insider, Jul. 3, 2026. [Online]. Available: https://thequantuminsider.com/2026/07/03/postscriptum-invests-in-quantum-hardware-developer-semiqon/ [P]
[353] GlobalFoundries, “GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing,” May 21, 2026. [Online]. Available: https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ Also https://investors.gf.com/news-releases/news-release-details/globalfoundries-launches-quantum-technology-solutions-scale-us. [C]
[354] M. Abdel-Kareem, “SemiQon Secures €17.5M ($18.3M USD) to Develop Cryogenic CMOS Technology for Quantum Systems,” Quantum Computing Report, Feb. 24, 2025. [Online]. Available: https://quantumcomputingreport.com/semiqon-secures-e17-5m-18-3m-usd-to-develop-cryogenic-cmos-technology-for-quantum-systems/ [P]
[355] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[356] PatSnap, “Spin Qubit Silicon Quantum Dot Arrays 2026 — PatSnap Eureka,” Jun. 2, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/spin-qubit-silicon-quantum-dot-arrays-2026-patsnap-eureka/ [P]
[766] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]

## פריטי אימות פתוחים

- המימון המצטבר של SemiQon וסכום ההשקעה של PostScriptum לא נמסרו; נתון ה-€17.5 M מקורו בעיתונות מקצועית מאחורי חומת תשלום, וסוג הסבב לא צוין [P][354][P][352].
- ל-€16 M של Groove Quantum (2026-04-30) אין כתובת URL של מקור ראשוני; המשקיעים לא נקבו בשמם [P][G:GROOVE-2026].
- שווי העסקה בין IBM ל-HRL לא נמסר בשתי ההודעות; אין אבן דרך מתוארכת של ספינים במפת הדרכים של IBM [C][204].
- רמת ההעשרה, כושר הייצור והלקוחות של ASP Isotopes לא נמסרו; הכמויות והמימון של DOE לא צוינו [C][347][G][348].
- סתירה אצל Diraq בנוגע לקנה המידה של 2029: "אלפים" (2026-07-09) מול 150 k פיזיים / 1 k לוגיים (2026-08-27); נעשה שימוש בנתון מפת הדרכים [R][211].
- מערך הנתונים של PatSnap (~60 רשומות) משמיט את HRL, imec, Diraq ו-Quantum Motion; מטופל כמדגם, לא כמפקד [P][356].
- אין שחזור בלתי תלוי של טווח הנאמנות הדו-קיוביטית על 300 mm מחוץ לקו של imec [D][189].
