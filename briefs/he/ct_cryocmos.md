---
id: ct_cryocmos
name: בקר CMOS קריוגני (4 K / mK)
layer: 5 בקרה
status: demonstrated
since: 2024
one_line: רכיבי ASIC מסחריים ב-CMOS בתוך הקריוסטט, המסנתזים את צורות הגל לבקרת הקיוביטים ואת מתחי הממתח לצד הקיוביטים, ומחליפים את המסדים בטמפרטורת החדר ואת הקווים הקואקסיאליים שלהם.
verdict: הוכח מקצה לקצה על 18 קיוביטי ספין, ובשוויון עם טמפרטורת החדר על 156 טרנסמונים — לשטף בלבד; האילוץ המחייב הוא מיליוואטים לקיוביט מול מתקן קירור של 2 W ב-4 K. להוריד בדרגה אם עד סוף 2027 שום בקר לא יפעיל >50 קיוביטים מקצה לקצה.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

בקר CMOS קריוגני הוא רכיב ASIC מצורן על לוח קר בתוך המקרר, המחולל צורות גל של מיקרוגל, של שטף ושל ממתח אלקטרודות השער לצד הקיוביטים. שום דבר קוונטי אינו מתרחש בו: הרווח תרמי וטופולוגי. הוא הפך לחומרה עם Horse Ridge (Intel/QuTech, FinFET של 22 nm, 4 K, 2019–2020) [C][548] ועם Gooseberry (Microsoft/Sydney, 100 mK) [D][549].

תכונות (a זיקה; b זמן; c קריאה; d ניידות; e בקרה @ מיקום; f מבנה השגיאה; g ייצור):
- a = 1.0, מיוצר לחלוטין; רכיב של מפעל ייצור, לא נושא קיוביט.
- b = אין; הוא אינו מחזיק מצב קוונטי.
- c = אין; הוא משרת את הקריאה של המארח.
- d = אין; מקובע ללוח קר.
- e = מיקרוגל @ 4 K; המיקום הוא הטכנולוגיה.
- f = קוהרנטית: משרעת, פאזה, תזמון, הפרעה הדדית.
- g = CMOS, מ-130 nm עד 14 nm.

דירוג 5 מתוך 111; משותף לארכיטקטורות מוליכי-העל והספינים.

## פיזיקה וגבולות

הרצפה היא תקציב חום, לא זמן קוהרנטיות. מתקני הקירור קטנים: 2 W ב-4 K (Bluefors XLD1000sl), 24 W (הרעיון Goldeneye של IBM), 200 W (Colossus של Fermilab) [S][550]. ההספק היחיד שקשור לשער דו-קיוביטי פועל הוא 23 mW לקיוביט של IBM [D][296]; המקרה האופטימי של אותה סקירה הוא 5 mW, וההדגמות הנמוכות ביותר בה — מתחת ל-2 mW [S][550]. מתקן של 2 W מכיל אפוא ~87 קיוביטים ב-23 mW, ו-~1,000 ב-2 mW.

בטמפרטורת מיליקלווין המשטר משתנה במהותו: תאים בפס בסיס, הפועלים במחזור עבודה חלקי, שמחזיקים מתח על אלקטרודת שער ומרעננים אותו — 18 nW לתא לפולסים של 100 mV ב-100 mK [D][549], ~20 nW MHz⁻¹ לתא ב-7 mK [D][551].

הכשל קוהרנטי: סחיפה וקוונטיזציה הופכות לשגיאה בזווית הסיבוב — ממיר של Delft נסחף בקצב של 60 µV/s עד 18 mV/s [C][552] — ריצוד (jitter) הופך לסיבוב-יתר, ובידוד סופי — להפרעה הדדית. הערוץ הסטוכסטי הוא הפעולה החוזרת (back-action), השווה ל-0.07% מהנאמנות החד-קיוביטית [D][551]. הרצפה זזה עם תהליך שאופיין בקור [C][553], או עם לוגיקה מוליכת-על ב-~1.6 µW לקיוביט [S][550].

## מצב ההנדסה העדכני

הטוב ביותר שהודגם: הבקר של HRL ב-RF CMOS של 130 nm ב-4 K — ≤3.5 W, 366 DAC, מתזמן של 250 MHz — המפעיל 54 נקודות כ-18 קיוביטים בחילוף בלבד, בשגיאה חד-קיוביטית ממוצעת של 2×10⁻⁴ ו-CNOT ממוצע של 3×10⁻³ (הטוב ביותר הניתן לשחזור: 9×10⁻⁴), וסוגר את הלולאה של קוד חזרה במרחק 5 ב-5.0×10⁻³ לאורך 200 סבבים, Λ₅/₃ = 4.7, בלי שום רכיב חם בלולאה [D][190] [G:HRL-2026]. IBM הפעילה רכיבי ASIC לממתח שטף של 14 nm על Heron R2 בן 156 קיוביטים, בשגיאה דו-קיוביטית חציונית של ≈2.3×10⁻³ — שוויון עם אלקטרוניקה חמה על אותו מעבד [C][527]. הטיפוסי בקנה מידה: אין — כל השאר מעל ~10 קיוביטים פועל ממסדים חמים [D][G:SEEQC-2026].

| שנה | נתון | מי | תג | מקור |
|---|---|---|---|---|
| 2021-01-25 | 100 mK, 18 nW לתא, פולסים של 100 mV | Microsoft | [D] | [549] |
| 2024-02-14 | שער מ-4 K: 23 mW לקיוביט, חד-קיוביטי 8×10⁻⁴ | IBM | [D] | [296] |
| 2025-06-25 | 7 mK, ~20 nW MHz⁻¹ לתא, מחיר של 0.07% בנאמנות | Sydney | [D] | [551] |
| 2026-03-16 | רכיבי ASIC לשטף, 156 קיוביטים, דו-קיוביטי חציוני 2.3×10⁻³ | IBM | [C] | [527] |
| 2026-07-29 | ≤3.5 W, 366 DAC, 18 קיוביטים, Λ₅/₃ = 4.7 | HRL | [D] | [190] |

האיבר השולט: אי-אחידות בין ערוץ לערוץ — CNOT ממוצע של 3×10⁻³ לעומת 9×10⁻⁴ כטוב ביותר הניתן לשחזור, וכ-80% מהשגיאה חיצוניים, מהבקרה ומהכיול [D][190].

## ייצור, חומרים ושרשרת האספקה

אין תהליך אקזוטי; הקושי הוא תהליך ייצור מסחרי המופעל 300 K מחוץ לתחום שבו הוסמך: RF CMOS של 130 nm (HRL) [D][190], FinFET של 14 nm (IBM) [D][296], FinFET של 22 nm (Horse Ridge, הממירים של Delft) [C][548], [552], FDSOI של 28 nm (Gooseberry, Sydney) [D][549], [551], 22FDX (Equal1) [C][273]. המשאב הנדיר הוא המודל, לא הפרוסה: ערכות התכנון נעצרות ב-−40 °C, ולכן השחקנים מחזיקים מודלים קריוגניים פרטיים או קונים תהליך שעבר אופטימיזציה לקור — SemiQon מצטטת שיפוע תת-סף של 0.32 mV/dec ב-420 mK, לעומת ~60 mV/dec ב-300 K [C][553]. שיעור התקינות והעלות לערוץ לא פורסמו. הריכוזיות יושבת במפעלי ייצור המוכנים להריץ פינות תהליך שלא הוסמכו, ובמקררי דילול [C][G:BLUEFORS-KIDE]. החשיפה לפיקוח על יצוא ישירה: תקנת BIS מ-2024-09-06 יצרה את ECCN 3A901.a למעגלי CMOS "המתוכננים לפעול בטמפרטורת סביבה השווה ל-4.5 K או נמוכה (טובה) ממנה", ולוכדת את הטכנולוגיה הזו לפי כוונת התכנון ולא לפי הביצועים, לצד פיקוח על מקררים ועל מערכות קריוגניות לבדיקת פרוסות [G][301] [G:BIS-QUANTUM-2024]. הפריט המפוקח יכול אפוא להיות קובץ תכנון.

## בקרה, קריאה ועומס הקלט-פלט

HRL ביטלה את יצירת צורות הגל בחום, אך מספר הכבלים לא ירד: 296 קווים ל-18 קיוביטים, ~16 לכל אחד — הרווח היה המסד, לא החיווט [D][190]. הרווח בחיווט הוא רווח של שלב המיליקלווין, שבו פירוק ריבוב הופך N הדקים ל-~log N כניסות: 64 ההדקים של Pando Tree ב-10–20 mK [C][272], ו-648 ההתקנים של Delft מ-96 מתחים, מתחת ל-120 µW [C][552]. ההשהיה היא הטיעון השני: 200 סבבי קוד נסגרו בלי שום רכיב חם בלולאה [D][190], לעומת הלוך-ושוב ממוצע של 3.84 µs בקישור GPU חם [G:NVQLINK-2025]. החומות הולכות אחר תקציב החום: 10³ קיוביטים דורשים את המחלקה של מתחת ל-2 mW על מתקן של 2 W; 10⁴ דורשים קירור ברמת Goldeneye או Colossus ב-≤5 mW לקיוביט; 10⁶ פירושם ~90 מודולים של 10,000 קיוביטים, שכל אחד מהם מפזר 50 W ב-4 K — מחוץ לכל מה שנמכר ב-2026 [S][550].

## תפקיד במחסנית

שתי ארכיטקטורות: טרנסמונים מוליכי-על (IBM, Google, IQM) וספינים בנקודות קוונטיות בצורן או בגרמניום (Intel, Diraq, Quantum Motion, HRL, Quobly, Equal1). הוא דורש מפעל CMOS של 300 mm — תלות שהספינים כבר נושאים, ולכן הם מקבלים CMOS קריוגני כתוצר לוואי, ואילו ספקי מוליכי-העל מממנים אותו בנפרד. הוא מספק את המצע הספרתי הקר שמפענח קריוגני צריך: מפענח מקדים ב-4 K שעלותו הוערכה בפחות מ-0.56 mW, עבור הפחתה של 3,780× ברוחב הפס של הסינדרום [S][G:PINBALL-2025-12]. הוא מחליף את הבקרה בטמפרטורת החדר, החלק היחיד בשכבה הזו שיש לו הכנסות, ומתחרה בבקרת קוונט שטף בודד (SFQ), שפורסמה מעל 99% בטמפרטורת מיליקלווין [D][G:SEEQC-2026]; המעבר קונה צורן קר במחזור מסירה לייצור (tape-out) של 18–24 חודשים, ומשולם בתקציב קירור שאחרת היה קונה קיוביטים. הטכנולוגיה הזו היא עצם לא-קוונטי, שהתכונה המבדלת היחידה שלו היא המיקום ב-4 K. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס; הטכנולוגיה הזו אינה מגבילה אותו — רזולוציית מתזמן של 4.0 ns [D][190] מול סבב של 0.65 µs, שהאיבר הגדול ביותר בו הוא 282 ns של קריאה. משבצות ריקות סמוכות: דוגם ספרתי (digitiser) קריוגני לקריאה, וממשק ספרתי קר תקני.

## ראיות — כיצד נמדדו המספרים

כל מספר בולט נמדד דרך הקיוביט, לעולם לא על הבקר: מידוד אקראי משולב (interleaved RB), שה-1.71 וה-17.51 פקודות לכל קליפורד שלו (חד-קיוביטי ודו-קיוביטי) חייבים ללוות כל השוואה [D][296]; הגדילה של Λ בקוד חזרה בין המרחקים 3 ו-5 אצל HRL [D][190]; ובתוצאת השטף של IBM מ-2026 — השוואת A/B מול אלקטרוניקה חמה על אותו מעבד: התכנון הנכון, והנדיר ביותר.

מידוד אקראי ממצע על פני פעולות קליפורד ועיוור לסחיפה קוהרנטית איטית, ולכן סחיפת הממירים [C][552] אינה מופיעה באף מספר RB; פעולה חוזרת, תופעות מעבר של מחזור העבודה, אי-אחידות ערוצים ואמינות בקור דורשים מדידות ייעודיות [D][551]. השחזור סביר ב-4 K (IBM, HRL) ובטמפרטורת מיליקלווין (Microsoft, Sydney, Delft, QuTech [C][554]).

סתירות: 23 mW לקיוביט של IBM [D][296] לעומת 5 mW ופחות מ-2 mW [S][550] הם גדלים שונים — פעיל לעומת סרק, הנעה בלבד לעומת השרשרת המלאה — ללא הגדרה משותפת; 23 mW משמש כאן כנתון היחיד הקשור לשער פועל. נתוני הנאמנות של Equal1 הם טענות מדף מוצר [C][273], מול התקן של שישה קיוביטים ב-0.3 K שפורסם [G:EQUAL1-60M-2026-01].

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בה | ראיות |
|---|---|---|---|---|
| HRL Laboratories | מפתח | ארה״ב | בקר ב-4 K המתזמן 18 קיוביטים | [D][190] [G:HRL-2026] |
| IBM Quantum | מפתח | ארה״ב | רכיבי ASIC לשטף של 14 nm; רכשה את HRL | [D][296] [C][10], [527] [G:IBM-HRL-CLOSED-2026-08] |
| Intel | מפתח | ארה״ב | Horse Ridge, Pando Tree | [C][272] [G:INTEL-2026] |
| Microsoft | מחקר | ארה״ב | Gooseberry ב-100 mK; פטנט נעילת המטען (charge-lock) | [D][549] [G][555] |
| University of Sydney | מחקר | אוסטרליה | CMOS ב-mK המניע את הספינים של Diraq | [D][551] |
| Equal1 | מפתח | אירלנד | קיוביטים ובקרה על פיסה אחת | [C][273] [G:EQUAL1-60M-2026-01] |
| Quantum Machines | ספק | ישראל | מסדים חמים שהטכנולוגיה הזו דוחקת | [C][528] |

**כספים.**
- 2025-02-25 · Quantum Machines · סבב C · $170 M · PSG Equity · $280 M במצטבר [C][528]
- 2025-11-06 · DARPA QBI שלב B · עד $15 M לכל אחד · אחד-עשר צוותים, ובהם IBM ו-Diraq [G:QBI-STAGEB-2025-11]
- 2026-05-21 · GlobalFoundries; Diraq · מכתבי כוונות של CHIPS · $375 M; $38 M · מכתב כוונות [G:CHIPS-LOI-2026-05]
- 2026-06-29 · SEEQC · S-1 ל-Nasdaq לצד מיזוג עם Allegro · שווי פעילות (EV) של $1 B, PIPE של $65 M [C][556] [P][557]; מיזוג ה-SPAC בוטל ב-2026-08-25, וה-S-1 ממשיך; ההנפקה לא תומחרה עד 30 בספטמבר 2026 [G:SEEQC-SPAC-TERMINATED-2026-08]
- 2026-07-23 · IBM · רוכשת את HRL Laboratories · לא פורסם · העסקה נסגרה ב-2026-08-26 [C][10] [G:IBM-HRL-2026-07][G:IBM-HRL-CLOSED-2026-08]

**שוק ושרשרת אספקה.** נכון ל-3 בספטמבר 2026 איש אינו מוכר בקר CMOS קריוגני; ההכנסות של השכבה הן ממסדים חמים של Quantum Machines, Zurich Instruments, Keysight ו-QBLOX, ו-Quantum Machines לבדה גייסה $280 M [C][528], [558]. ה-CMOS הקריוגני עצמו הוא מו״פ פנימי; ההצעות המסחריות עדיין ללא הכנסות: SemiQon, FrostByte (€1.3 M) ו-Rhonexum ($1 M) [C][553], [559] [P][560]. G3, G4 ו-G7 משלמים עליו; G1, G2 ו-G5 לא.

**קניין רוחני ותקנים.** Microsoft Technology Licensing מחזיקה ב-US 11,838,022 על ממשק CMOS קריוגני לקיוביטים (הוענק ב-2023-12-05), ארכיטקטורת נעילת המטען שמאחורי Gooseberry [G][555]; MIT מחזיק ב-US 12,705,525 על פולסים בפס בסיס (2026-08-11) [G][561]; ההגשה של Intel על כיול בלולאה סגורה היא בקשה בלבד [G][562]. אף מאגר נתונים אינו מפרסם ספירה מתוארכת של משפחות פטנטים [P][563]. תקנים: אין, ואין הגדרה מוסכמת להספק לקיוביט.

**מפות דרכים ועמידה בהבטחות.**
- Intel: 2020-12-03 · Horse Ridge II למערכות ספין בקנה מידה גדול · אין ממשיך [G:INTEL-2026].
- Microsoft: 2021-01-27 · Gooseberry ל"אלפי קיוביטים" · לא סופק [C][564].
- IBM: 2024-02-14 · CMOS קריוגני כמסלול לבקרה הניתנת להגדלה · סופק חלקית, לשטף בלבד [D][296] [C][527].
- HRL: 2026-04-17 · מעבד ללא מחוללי צורות גל חמים · סופק [D][190].
אמינות: רק HRL נקבה בתוצר מתוארך וסיפקה אותו, ו-IBM קנתה אותה; IBM מפרסמת השוואות A/B, לא טענות כותרת; ל-Intel אין נאמנות שעברה ביקורת עמיתים על רכיב Horse Ridge; הקו של Microsoft רדום זה חמש שנים.

**פרשנות אסטרטגית.** המנצחים אם הבקרה הקרה תהפוך לתקן: בתי CMOS משולבים — IBM עם HRL, ו-Intel אם תחזור לתחום — וחברות ספין שהקיוביטים והבקרים שלהן חולקים קו ייצור. המפסידים: ספקי המסדים החמים, המוגנים רק כל עוד איש מתחת לאלף קיוביטים אינו זקוק ל-ASIC. המסלול הקר האחר, בקרת SFQ, צפוי לצרוך פחות הספק לקיוביט [S][550], ועדיין אין לו שער דו-קיוביטי; המפתחת שלו, SEEQC, הגישה בקשה לרישום ב-Nasdaq, וגודל ההנפקה לא פורסם [P][557]. כוח המיקוח נשאר בידי ספקי הפלטפורמות; הספק הנדיר הוא יצרן המקררים.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם IBM תפרסם, בביקורת עמיתים, שרשרת מלאה — הנעה, שטף וקריאה — על ≥100 קיוביטים מוליכי-על בשוויון עם מסדים חמים; אם הבקר של HRL יופיע מחדש בתוך IBM מעל 18 קיוביטים; אם מישהו ידווח על הספק מוגדר לקיוביט מתחת ל-5 mW ב-4 K תחת עומס. להוריד בדרגה אם עד סוף 2027 שום בקר לא יפעיל יותר מכחמישים קיוביטים מקצה לקצה בתוצאה שעברה ביקורת עמיתים, ומערכות ברמת Heron עדיין יסופקו עם מסדים חמים. התרחיש הטוב ביותר עד 2029: בקרה קרה כתקן במכונות ספין ובמסלול השטף של IBM, ומודול של 10,000 קיוביטים על מתקן 4 K אחד ב-≤5 mW לקיוביט. התרחיש הגרוע ביותר: התקציב נשאר מחייב, מכונות מוליכי-העל שומרות על מסדים חמים, וה-CMOS הקריוגני שורד רק כממתח בטמפרטורת מיליקלווין לספינים.

שאלות פתוחות: (1) הגדרה של הספק לקיוביט שאפשר להגן עליה? (2) האם מפעל ייצור יסמיך פינת תהליך קריוגנית? (3) האם סחיפת הבקר שולטת מתחת לשגיאת קיוביט של 10⁻⁴? (4) האם ההספק לקיוביט חייב לרדת, או שמתקן הקירור יכול לגדול פי עשרה? (5) האם IBM תשמור על התכנון של HRL ב-130 nm? לעקוב אחר ISSCC 2027, אחר הגילויים של IBM לאחר הרכישה, ואחר כל מתקן 4 K שישווק מעל 20 W.

## מקורות
[10] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [C]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[272] S. Subramanian and S. Pellerano, “Intel's Millikelvin Quantum Research Control Chip Provides Denser Integration with Qubits,” Intel Community, Jun. 20, 2024. [Online]. Available: https://community.intel.com/t5/Blogs/Tech-Innovation/Data-Center/Intel-s-Millikelvin-Quantum-Research-Control-Chip-Provides/post/1608558 [C]
[273] Equal1, “UnityQ.” [Online]. Available: https://www.equal1.com/technology [C]
[296] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[528] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[548] Intel Corporation, “Intel Debuts 2nd-Gen Horse Ridge Cryogenic Quantum Control Chip,” Dec. 3, 2020. [Online]. Available: https://www.intc.com/news-events/press-releases/detail/1429/intel-debuts-2nd-gen-horse-ridge-cryogenic-quantum-control [C]
[549] S. J. Pauka *et al.*, “A cryogenic CMOS chip for generating control signals for multiple qubits,” *Nat. Electron.*, vol. 4, no. 1, pp. 64–70, Jan. 2021, doi: [10.1038/s41928-020-00528-y](https://doi.org/10.1038/s41928-020-00528-y). [D]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[551] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[552] J. van Staveren *et al.*, “Cryo-CMOS Bias-Voltage Generation and Demultiplexing at mK Temperatures for Large-Scale Arrays of Quantum Devices,” *IEEE Trans. Quantum Eng.*, vol. 6, pp. 1–18, 2025, doi: [10.1109/TQE.2025.3580377](https://doi.org/10.1109/TQE.2025.3580377). [C]
[553] SemiQon, “SemiQon Cryo-CMOS™.” [Online]. Available: https://www.semiqon.com/technology/semiqon-cryo-cmos [C]
[554] QuTech, “Scalable diamond Quantum Computing with cryogenic chip integration,” Feb. 17, 2026. [Online]. Available: https://qutech.nl/2026/02/17/scalable-diamond-quantum-computing-with-cryogenic-chip-integration/ [C]
[555] Microsoft Technology Licensing, LLC, “Cryogenic-CMOS interface for controlling qubits,” USPTO, Dec. 2023. [Online]. Available: https://patents.justia.com/patent/11838022 [G]
[556] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [C]
[557] M. Abdel-Kareem, “SEEQC Files Form S-1 for Nasdaq IPO Parallel to Ongoing Allegro Merger Process,” Quantum Computing Report, Jul. 2, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-files-form-s-1-for-nasdaq-ipo-parallel-to-ongoing-allegro-merger-process/ [P]
[558] Quantum Machines, “Quantum Machines Makes Second European Acquisition in Six Weeks as Quantum Closes In on Real-World Advantage,” Jun. 17, 2026. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-acquisition-pcb-engineering/ [C]
[559] QuTech, “QuTech spinoff FrostByte raises €1.3 million for cryo-electronics for scalable quantum computers,” May 11, 2026. [Online]. Available: https://qutech.nl/2026/05/11/qutech-spinoff-frostbyte-raises-e1-3-million-for-cryo-electronics-for-scalable-quantum-computers/ [C]
[560] M. Abdel-Kareem, “Rhonexum Raises $1M Pre-Seed to Solve the Quantum Cabling Bottleneck via Cryo-CMOS,” Quantum Computing Report, Mar. 18, 2026. [Online]. Available: https://quantumcomputingreport.com/rhonexum-raises-1m-pre-seed-to-solve-the-quantum-cabling-bottleneck-via-cryo-cmos/ [P]
[561] W. D. Oliver and S. Gustavsson, “Scalable control of quantum bits using baseband pulsing,” USPTO, Aug. 2026. [Online]. Available: https://patents.justia.com/patent/12705525 [G]
[562] Intel Corporation, “Technologies for Closed-Loop Qubit Calibration,” USPTO, Jul. 2026. [Online]. Available: https://patents.justia.com/patent/20260187510 [G]
[563] PatSnap, “Cryogenic CMOS Circuit Technology Landscape 2026,” Apr. 20, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/articles/cryo-cmos-technology-landscape-2026/ [P]
[564] C. Nayak, “Full stack ahead: Pioneering quantum hardware allows for controlling up to thousands of qubits at cryogenic temperatures,” Microsoft Research Blog, Jan. 27, 2021. [Online]. Available: https://www.microsoft.com/en-us/research/blog/full-stack-ahead-pioneering-quantum-hardware-allows-for-controlling-up-to-thousands-of-qubits-at-cryogenic-temperatures/ [C]

## פריטי אימות פתוחים

- הספק לקיוביט ב-4 K: 23 mW שמדדה IBM תחת בקרה פעילה [D][296], לעומת "5 mW אופטימי" ו"מתחת ל-2 mW" בסקירת המשאבים [S][550]; ההגדרות שונות (פעיל לעומת סרק, הנעה בלבד לעומת השרשרת המלאה), ואף אחת מהן אינה מפורסמת. נעשה שימוש ב-23 mW.
- 18 nW לתא של Gooseberry [D][549] ו-~20 nW MHz⁻¹ לתא של השבב מ-Sydney [D][551] מצוטטים במקורות משניים כאילו היו שקולים; אלה גדלים שונים, שלא יושבו זה עם זה.
- הספקי הקירור של Bluefors XLD1000sl, של Goldeneye של IBM ושל Colossus של Fermilab לקוחים מסקירת המשאבים [S][550]; דף המוצר של Bluefors XLD החזיר HTTP 404 ב-2026-09-03, והמפרט הראשוני לא אושר.
- תוצאת השטף של IBM ב-CMOS קריוגני מ-2026 קיימת רק כתמציות של כנס [C][527]; אין קדם-פרסום או מאמר נכון ל-2026-09-03, והייחוס ל-FinFET של 14 nm נשען על טקסט התמצית. הבלוג של IBM על קריוגניקה מודולרית (2026-08) נותן את שטח החיווט של התא ואת נפח הוואקום, אך לא את הספק הקירור ב-4 K.
- הנאמנויות 99.9% / 99.3% / 99% של Equal1 ו"35 התאים הקוונטיים המונוליתיים" הן טענות מדף מוצר [C][273], ללא מאמר או הודעה מתוארכת.
- דור התהליך של SemiQon, מיקום מפעל הייצור שלה וגודל ההשקעה של PostScriptum בה מ-2026-07 לא פורסמו.
- ההכנסות והמזומנים של SEEQC מופיעים בטופסי ה-S-1 שלה, לא בהודעה על ההגשה ולא בסיכום בעיתונות המקצועית [C][556] [P][557]: הכנסות של $4.2 M ב-2025 ו-$18.1 M במזומן ב-2026-06-30 (תיקון ל-S-1 מ-2026-08-28) [G:SEEQC-S1A-2026-08]; גודל ההנפקה עדיין ריק, ושווי הפעילות של $1 B וה-PIPE של $65 M מתארים את המיזוג עם Allegro שבוטל.
- ההכנסות של Quantum Machines לא פורסמו, ונתח הלקוחות שלה, ">50% מהחברות המפתחות מחשבים קוונטיים", הוא טענה של החברה [C][528]; Zurich Instruments, Keysight ו-QBLOX אינן מפרסמות דבר דומה, ולכן אי אפשר להעריך את גודל שוק הבקרה החמה שהטכנולוגיה הזו הייתה דוחקת.
- ההספק, מספר הערוצים ודור התהליך של מאמר ה-CMOS הקריוגני ליהלום של QuTech/Fujitsu ב-ISSCC 2026 לא היו זמינים; רק ההודעה המוסדית [C][554].
- ספירות משפחות פטנטים של CMOS קריוגני: אף מאגר נתונים מזוהה אינו מפרסם ספירה מתוארכת; PatSnap נותנת רק ספירות אזוריות של "תוצאות מפתח", עם הסתייגות לגבי השלמות [P][563].
- עלות הבקר של HRL, לוח הזמנים של המסירה לייצור, והשאלה אם IBM תשמור על התכנון של 130 nm, אינם מצוינים בהודעת הרכישה [C][10]; הרכישה נסגרה ב-2026-08-26 [G:IBM-HRL-CLOSED-2026-08].
