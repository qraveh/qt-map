---
id: fab_cmos
name: מפעל CMOS של 300 mm (ספינים, CMOS קריוגני, חיווט מוליך-על)
layer: 10 ייצור
status: demonstrated
since: 2022
one_line: קווי CMOS תעשייתיים של 300 mm המייצרים קיוביטי ספין בנקודות קוונטיות, בקרי CMOS קריוגני וחיווט מוליך-על; מסלול ייצור הקיוביטים היחיד שיש לו סטטיסטיקה של שיעורי תקינות בקנה מידה של פרוסה.
verdict: האחידות הוכחה (96% תקינות התקנים, ממד קריטי תת-ננומטרי); הנאמנות עדיין אינה תוצר שמפעל ייצור מספק. להוריד בדרגה אם עד סוף 2027 לא יופיע התקן של 300 mm עם >20 קיוביטים ונאמנות דו-קיוביטית (2Q) ≥ 99.5% לכל הזוגות.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

טכנולוגיה זו היא משטר ייצור, לא קיוביט: קווי ייצור CMOS של 300 mm המייצרים מערכי נקודות קוונטיות המוגדרות באלקטרודות שער (Si/SiGe, SiMOS, Ge), את רכיבי ה-ASIC שלהם ב-CMOS קריוגני, ושכבות מוליכות-על של קיוביטים ושל חיווט. נקודה קוונטית היא טרנזיסטור במשטר הצטברות, באכלוס של אלקטרון בודד; בפסיעה של 45–100 nm מפעל הייצור מספק אחידות, איכות ממשק ובקרה איזוטופית, לא רזולוציה, על פני עשרות אלפי התקנים לפרוסה, עם בדיקה קריוגנית ברמת הפרוסה.

CEA-Leti פתחה את המסלול ב-2016 בקיוביט ספין בזרימת תהליך FD-SOI של 28 nm [D][793]. Intel ו-QuTech ייצרו במרץ 2022 את הקיוביטים הראשונים על 300 mm שכל תבניותיהם עוצבו בליתוגרפיה אופטית [D][794], ומכאן *מאז 2022*; ב-2024 הוסיפה Intel מערכים שיוצרו ב-EUV וסטטיסטיקה ברמת הפרוסה ב-1.6 K [D][199], [766]. imec ייצרה טרנסמונים על 300 mm ב-2024 [D][293], ויחד עם Diraq — תאי יחידה מעל 99% ב-2025 [D][189]. 22FDX של GlobalFoundries הפך ב-2025 לאפשרות של מפעל ייצור מסחרי [D][767], ST החלה בדצמבר 2025 באצוות FD-SOI על 28Si [P][795], ובמאי 2026 באו מכתבי הכוונות של US CHIPS [G][300].

תכונות (גרף הטכנולוגיות):
a, זיקה לנושא: מיוצר, 1.0; הטכנולוגיה היא הייצור עצמו.
b, זמן אופייני: אין; אין זמן שער ואין אופן שזירה.
c, קריאה: אין.
d, ניידות וקישוריות: אין.
e, אופן הבקרה: אין.
f, מבנה השגיאה: קוהרנטית; השונות בין התקן להתקן נקראת כשגיאת כיול.
g, ייצור: CMOS.

## פיזיקה וגבולות

מנגנון. המפעל קובע ארבעה גדלים שעוברים בירושה: אחידות גאומטרית — ממד קריטי (CD) שסטייתו בתוך 0.5 nm, בפסיעה של 45–100 nm [D][199]; אי-סדר אלקטרוסטטי — פיזור אקראי של 59 mV במתח הסף ב-Si/SiGe של Intel [D][766]; טוהר איזוטופי — 800 ppm של 29Si שיורי ב-Intel [D][199] ו-400 ppm ב-imec [D][189]; ואיכות הממשק, הקובעת את רעש המטען, וב-Si/SiGe גם את התפלגות פיצול העמקים.

סדרי גודל. T2*/T2echo מגיעים ל-5/205 µs ב-Si/SiGe על 28Si, לעומת 0.6/98 µs בצורן טבעי [D][766]; T2 בהד האן מגיע ל-1.31 ms ב-SiMOS של imec [D][197].

רצפה. בספינים היא חומרית: 29Si שיורי, רעש מטען בממשק וזנב התפלגות פיצול העמקים ב-Si/SiGe, ההופך חלק מהנקודות למוקדי דליפה. בטרנסמונים היא פגיעת הצמתים ביעד: על פני פרוסה של 300 mm תדרי הקיוביטים מפוזרים ב-5–7%, כלומר 10–14% בהתנגדות בגודלי הצמתים של קיוביטים (הפיזור של ~8% הוא של צמתים גדולים) [D][293], סדר גודל מעל מה שסריג נטול התנגשויות צריך; ריפוי בממתח מתחלף (97.4% פגיעה ביעד [D][294]) הוא שלב שלאחר הייצור, לא תכונה של מפעל הייצור.

כפי שהקוד רואה זאת: שגיאה קוהרנטית הניתנת לכיול (HRL מייחסת כ-80% משגיאת ה-CNOT במערך 54 הנקודות שלה לבקרה ולכיול [D][190]), ועוד דליפה וסחיפה איטית; דבר אינו ניתן להמרה למחיקה; גרדיאנטים על פני הפרוסה [D][293] הופכים לשגיאה מתואמת במרחב. הזזת הרצפה מחייבת 28Si ממחלקת 10 ppm, פיצול עמקים מהונדס (בסימולציה בלבד [S][796]), חורים ב-Ge/SiGe, או גיזום צמתים בתוך זרימת התהליך.

## מצב ההנדסה העדכני

המיטב שהודגם: ארבעה תאי יחידה של Diraq/imec, כל פעולה בהם מעל 99% (1Q 99.97%, CZ 99.04–99.56%, SPAM 99.95% ב-100 µs), בטומוגרפיית ערכת שערים, ספטמבר 2025 [D][189][G:IMEC-300MM-2025]. הטיפוסי בקנה מידה: 232 ההתקנים של Intel, בני שתים-עשרה נקודות כל אחד, על פרוסה אחת נתנו שיעור תקינות של 99.8% לנקודות ו-96% להתקנים שלמים, מאי 2024 [D][766]; 22FDX שלא שונה נתן שיעור של 28–40% "נקודות טובות" על פני 1,024 נקודות, ינואר 2025 [D][767]; מערך שמונת הקיוביטים של imec אימת זוג אחד מתוך ארבעה, יולי 2026 [D][197].

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2016 | קיוביט ספין בזרימת תהליך FD-SOI של 28 nm על 300 mm | CEA-Leti | [D][793] |
| 2022-03 | >10,000 מערכי נקודות לפרוסה; 1Q 99.0–99.1% | Intel/QuTech | [D][794] |
| 2024-09 | טרנסמונים על 300 mm: T1 חציוני 75 µs, שיעור תקינות 98.25% | imec/KU Leuven | [D][293] |
| 2024-12 | >24,000 התקנים לפרוסה, CD < 0.5 nm (EUV) | Intel | [D][199] |
| 2025-01 | 1,024 נקודות על 22FDX, מרבב CMOS קריוגני 1:1,024, < 10 min | Quantum Motion/GF | [D][767] |
| 2025-09 | CZ 99.04–99.56% על SiMOS של 300 mm, 4 מתוך 4 התקנים > 99% | Diraq/imec | [D][189] |
| 2026-04 | בקר CMOS ב-4 K (366 DAC, ≤ 3.5 W) מריץ קוד חזרה ב-d=5, Λ = 4.7 | HRL | [D][190][G:HRL-2026] |

איבר השגיאה השולט: המישור שבו נתקעה נאמנות ה-2Q, 99.0–99.6%, נובע מרעש מטען ומכיול החילוף [D][189], [190]; קריאה של 100 µs לשם SPAM ממחלקת 99.9% [D][189] קובעת מחזור של 100–300 µs; אף התקן של 300 mm עם יותר משנים-עשר קיוביטים לא פרסם 2Q לכל הזוגות; בטרנסמונים המגבלה היא פיזור הצמתים, לא הקוהרנטיות [D][293].

## ייצור, חומרים ושרשרת האספקה

פלטפורמות. Intel D1: בורות קוונטיים של Si/SiGe, ליתוגרפיית טבילה ו-EUV, סינון במתקני בדיקת פרוסות קריוגניים [D][199], [766]. imec: SiMOS עם אלקטרודות שער חופפות מצורן רב-גבישי בפסיעה של פחות מ-100 nm, על 28Si של 400 ppm [D][189], ועוד זרימת תהליך לטרנסמונים עם צמתי חפיפה באיכול יבש [D][293]. FD-SOI: 22FDX של GlobalFoundries (Quantum Motion [D][767]; Equal1 [C][797]) ו-28 nm של ST ב-Crolles על מצעי 28Si של Soitec, והאצוות הראשונות בדצמבר 2025 [P][795]. HRL ו-SkyWater עובדות על 200 mm [D][190][C][19].

שיעור תקינות. 96% תקינות התקנים בזרימת תהליך שעברה אופטימיזציה לקוונטים [D][766], לעומת 28–40% בזרימת תהליך מסחרית [D][767] — זהו המספר המרכזי של הטכנולוגיה.

עלות ואנרגיה. אף מפעל ייצור אינו מפרסם מחיר לפרוסה קוונטית; היעד של Diraq, < $1 לקיוביט [R][211], וטענות הספקים ברמת המסד [C][200], [355], [771] לא עברו ביקורת.

שרשרת אספקה. קווים: Intel (פנימי); imec, המתאמת של קו הייצור הניסיוני SPINS של האיחוד האירופי [G][770]; יחידת Quantum Technology Solutions של GlobalFoundries [C][353]; IBM Albany, ההופך ל-Anderon — קו לחיווט מוליך-על, למעברים דרך הצורן (TSV) ולבליטות [C][798]; SkyWater, קו של 200 mm, בבעלות IonQ מאז 2026-07-31 [C][19]. חומרים: 28Si מועשר, שמקורו ההיסטורי ברוסיה, וכיום גם מ-ASP Isotopes בפרטוריה (ייצור מסחרי מאז 2025-03-27) [C][347] ומ-ORNL ו-PNNL כסילאן של 99.9999% 28Si (US DOE, הוכרז ב-2026-07-16) [G][348]; Silex השלימה ביוני 2026 מפעל לעד 20 kg בשנה, עם הפעלה ראשונית בסוף 2026, עבור SQC [C][799]. ציוד: מתקני בדיקת פרוסות קריוגניים מ-Bluefors/Afore (< 2 K, 300 mm, 768 קווי DC, 48 קווי RF) [C][800] ומ-FormFactor [C][801]. נקודות כשל יחידות: נקודות ב-EUV רק ב-Intel וב-imec; דואופול של מתקני בדיקת הפרוסות; 28Si מקומץ מפעלי העשרה.

פיקוח על יצוא. התקנה של BIS מ-2024-09-06 מפקחת על מעגלי CMOS משולבים קריוגניים ל-≤ 4.5 K (ECCN 3A901), על מערכות קריוגניות של ≥ 600 µW ב-≤ 0.1 K (3A904), על מתקני בדיקת פרוסות קריוגניים (3B904) ועל מחשבים קוונטיים לפי מספר הקיוביטים ושגיאת ה-C-NOT יחד, מ-34 קיוביטים בשגיאה של ≤ 10⁻⁴ ועד כל שגיאה שהיא החל מ-2,000 קיוביטים (4A906) [G:BIS-3A901A-CRYOCMOS], עם חריגת הרישוי IEC לבעלות ברית [G][301][G:BIS-QUANTUM-2024]; הרשימות של האיחוד האירופי ושל בריטניה תואמות. אותה תקנה מפקחת על צורן וגרמניום המועשרים מעבר לשיעורים איזוטופיים שנקבעו — שכבות אפיטקסיאליות, הידרידים כגון סילאן, חומר בתפזורת ותחמוצות (3C907–3C909) [G][301].

## בקרה, קריאה ועומס הקלט-פלט

הריבוב עובר אל הפיסה או אל המארז: מרבב CMOS קריוגני של 1:1,024 על 13 קווים [D][767]; המרבב של imec, המנתב פולסים של טרנסמונים מתחת ל-15 mK תוך שמירה על 1Q > 99.9% [D][802]; שבב FD-SOI של 28 nm עם 32 תאים ב-7 mK, ~20 nW/MHz לתא [D][551]; הבקר של HRL ב-4 K, עם 366 DAC ב-≤ 3.5 W (~10 mW לערוץ), המריץ קוד חזרה [D][190]; הבקר של IBM ב-4 K, ב-23 mW לקיוביט [D][296]. שיתוף קווים במערך crossbar דורש T = 6√g − 1 קווים למערך ריבועי של g נקודות (23 עבור 16) [D][520].

חומות. 10³: די בקווים לכל קיוביט; העומס הוא זמן הכוונון. 10⁴: ב-23 mW לקיוביט של IBM [D][296] העומס ב-4 K הוא 230 W, וב-3.5 W ל-18 קיוביטים של HRL [D][190] — כ-2 kW: יותר מפי מאה משלב ה-4 K של 2 W ב-Bluefors XLD1000sl, ומעל 200 W של Colossus ב-Fermilab, המתקן הגדול ביותר בסקירת המשאבים [S][550] — ולכן נדרש ריבוב של ≥ 10:1 או תאים בטמפרטורת מיליקלווין ממחלקת ה-nW. 10⁶: רק שיתוף קווים ב-crossbar (~6,000 קווים [D][520]) יחד עם CMOS בטמפרטורת מיליקלווין או SFQ סוגר את החשבון; השאלה אם בקרה משותפת שומרת את השגיאה הקוהרנטית מתחת לסף עדיין פתוחה. השהיה: מחזורי הספין מוגבלים בידי הקריאה, באינטגרציה של 100 µs [D][189].

## תפקיד במחסנית

שורש של שכבה 10: היא אינה דורשת דבר, ומספקת את מערכי הנקודות ואת רכיבי ה-ASIC הקריוגניים שארכיטקטורת הספינים בנקודות קוונטיות מניחה — הארכיטקטורה שבה היא ראשית; בסריג הטרנסמונים עם מצמדים ברי-כוונון, ביונים לכודים ב-QCCD וביונים לכודים עם שערים אלקטרוניים היא חלופית. היא מחליפה את ייצור התורמים בליתוגרפיית STM (אוגרים של 11 קיוביטים, ייצור טורי, ללא מסלול למפעל ייצור [D][192]); עבור מלכודות יונים היא החלופה למפעלי מלכודות MEMS, ומחיר המעבר הוא הסמכה מחדש ל-CMOS — מחיר ששילמה Oxford Ionics (חלק מ-IonQ מאז 2025-09-17), שהנאמנות הדו-קיוביטית שלה, 99.99% על שבבים ממפעלים סטנדרטיים, מדווחת בהודעה של IonQ [C][446][G:IONQ-OXIONICS-2025]. כאן נושאים טבעיים (יונים לכודים) יורשים את ייצור המוליכים למחצה. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס בארכיטקטורה; הטכנולוגיה הזו אינה מוסיפה לו איבר; הסבב הנגזר של ארכיטקטורת הספינים בנקודות קוונטיות הוא 8.5 µs ונקבע בידי הקריאה, לעומת מחזור מדוד של 100–300 µs [D][189]. הסעה במצב מסוע על פני 10 µm אפקטיביים (הלוך ושוב) ב-99.5% [D][196], שהודגמה בהתקן מתוצרת Delft, היא מה שאלקטרודות שער אחידות של 300 mm חייבות לשחזר. משבצות ריקות שכנות: אין חיבור בין-מודולי לספינים (פוטוניקה של 300 mm היא המועמדת, ולא הוכחה בטמפרטורת מיליקלווין) ואין מפענח קריוגני שיוצר בפועל; תכנון של מפענח מקדים ב-CMOS קריוגני טוען להפחתה של 3,780× ברוחב הפס של הסינדרום, מתחת ל-0.56 mW [S][733].

## ראיות — כיצד נמדדו המספרים

מספרי שיעור התקינות מגיעים ממתקני בדיקת פרוסות קריוגניים ב-1.6–1.7 K (כוונון אוטומטי, קריטריונים של הדלקה/צביטה ושל חישת מטען [D][199], [766]): סטטיסטיקה של טרנזיסטורים. הנאמנויות מגיעות מהתקנים ספורים במקררי דילול: טומוגרפיית ערכת שערים (12,263 רצפים) לתאי היחידה [D][189], בחינת ביצועים אקראית על Tunnel Falls [D][199], מפות T1/T2 על פני הפרוסה לטרנסמונים [D][293].

מה שאינו נלכד: (1) בדיקה ב-1.6 K אינה רואה פיצול עמקים, חילוף או קוהרנטיות, ולכן שיעור תקינות ההתקנים אינו אומר דבר על שיעור תקינות הקיוביטים; (2) ברירה: אופיינו 4 מתוך 20 התקנים של imec [D][189], וב-2022 קוררו 6 מתוך > 10,000 מערכים [D][794]; (3) קריטריונים: 28–40% ו-96% מגדירים "עובד" באופן שונה [D][766], [767]; (4) אין 2Q בו-זמני לכל הזוגות באף מערך של 300 mm [D][197]; (5) הזדקנות: סחיפה של 3.7% בצמתים במשך 146 ימים [D][293] נעדרת מטענות הנאמנות.

שחזור: מספרי ה-SiMOS של imec משתחזרים על פני ארבעה התקנים ושני מוסדות [D][189]; המספרים של Intel באים מיצרן אחד בלבד. סומנו: "המחשב הקוונטי הראשון מצורן ב-CMOS, מלא בכל שכבותיו" של Quantum Motion, ללא נאמנויות שפורסמו [C][200]; הנקודות של Equal1 בתהליך מסחרי, ללא מדדי קיוביט [C][797].

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Intel | מפתח; ספק פנימי | ארה״ב | מערכי Si/SiGe ב-EUV; סטטיסטיקה ברמת הפרוסה ממתקן בדיקה קריוגני; שבב של 12 קיוביטים ב-Argonne | [D][199], [766]; [G][207] |
| imec | מחקר; ספק | בלגיה | נקודות SiMOS על 300 mm, טרנסמונים, מרבב בטמפרטורת מיליקלווין; מתאמת SPINS | [D][189], [293], [802]; [G][770] |
| GlobalFoundries | ספק (מפעל ייצור מסחרי) | ארה״ב | נקודות ו-CMOS קריוגני על 22FDX; יחידת Quantum Technology Solutions; מכתב כוונות על $375 M | [C][353], [803]; [G][300] |
| IBM | מפתח; ספק | ארה״ב | Anderon: פרוסות מוליכות-על של 300 mm, TSV, בליטות; מכתב כוונות על $1 B | [C][10], [798]; [G][300] |
| Diraq | מפתח | אוסטרליה | תאי יחידה של SiMOS ב-imec; שלב B של QBI; מכתב כוונות של CHIPS עד $38 M | [D][189], [197]; [G][65], [300] |
| Quantum Motion | מפתח | בריטניה | מערכים של 1,024 נקודות על 22FDX; מערכת ב-NQCC; שלב B של QBI | [D][767]; [C][200]; [G][65] |

**כספים.**

| תאריך | שחקן | אירוע | סכום | משקיע מוביל או תוכנית | מצטבר | מצב |
|---|---|---|---|---|---|---|
| 2025-11-06 | Diraq; Quantum Motion; SQC | מענק | עד $15 M לכל אחת | DARPA QBI, שלב B | — | סופי [G][65][G:QBI-STAGEB-2025-11] |
| 2026-01-15 | Equal1 | סבב | $60 M | ISIF | > $85 M | נסגר [C][771][G:EQUAL1-60M-2026-01] |
| 2026-04-03 | imec + 25 שותפים | מענק | €50 M | קו הייצור הניסיוני SPINS של EU Chips JU | — | הוכרז [G][770] |
| 2026-05-07 | Quantum Motion | סבב C | $160 M | DCVC, Kembara | — | נסגר [C][355][G:QM-160M-2026-05] |
| 2026-05-21 | GlobalFoundries | מכתב כוונות של CHIPS | $375 M | US Commerce ($2.013 B בתשעה מכתבי כוונות) | — | מכתב כוונות, לא מחייב [G][300][C][353][G:CHIPS-LOI-2026-05] |
| 2026-05-21 | IBM (Anderon) | מכתב כוונות של CHIPS | $1 B + $1 B במזומן מ-IBM | US Commerce | — | מכתב כוונות, לא מחייב [G][300][C][798] |
| 2026-05-21 | Diraq | מכתב כוונות של CHIPS | עד $38 M | US Commerce | גויסו > $100 M [P][G:DIRAQ-FUNDING] | מכתב כוונות, טרם הוענק [G][300] |
| 2026-06-03 | Quobly | סבב A | €115 M | Bpifrance, SEALSQ, STMicroelectronics | €134 M | נסגר [P][804][G:QUOBLY-115M-2026-06] |
| 2026-06 | Silex Systems | הקמת מפעל Q-Si הושלמה | A$5.1 M + A$4.35 M | Defence Trailblazer; SQC | — | הפעלה ראשונית בסוף 2026 [C][799] |
| 2026-07-23 | IBM | מיזוג ורכישה: HRL Laboratories | לא נמסר | — | — | הוכרז; נסגר ב-2026-08-26; תוכניות אפשריות לקיוביטי ספין ב-Anderon [C][10][G:IBM-HRL-2026-07][G:IBM-HRL-CLOSED-2026-08] |
| 2026-07-31 | IonQ | מיזוג ורכישה: SkyWater | $15.00 + 0.4883 מניות IonQ לכל מניה (~$1.8 B) | — | — | נסגר [C][19][G:IONQ-SKYWATER-2026] |

**שוק ושרשרת אספקה.** חלקם של הקוונטים בהכנסות מפעלי הייצור זניח. ריכוזיות: שני קווי נקודות המסוגלים ל-EUV, אפשרות FD-SOI מסחרית אחת (ST נכנסת), דואופול של מתקני בדיקת פרוסות, קומץ מפעלי העשרה של 28Si. כלכלת היחידה: לא פורסמה, מלבד היעד של Diraq [R][211]. המשלמים: G4, עבור צפיפות CMOS של 10⁶ קיוביטים; G7, נכון ל-3 בספטמבר 2026, עבור מערכות ספין ברמת המסד; ספקי מוליכי-העל קונים חיווט מ-Anderon/GF עבור G2–G4; ספקי היונים קונים מלכודות ממפעלים סטנדרטיים עבור G2, G3, G7.

**קניין רוחני ותקנים.** תיקי פטנטים: Intel, HRL, Diraq/UNSW, Quantum Motion/UCL, Quobly (רישיונות CEA/CNRS), Equal1; אין התדיינות משפטית פומבית; לא נמצאה ספירה מתוארכת של משפחות פטנטים ממאגר נתונים מזוהה. SPINS מבטיח ערכות תכנון תהליך (PDK) קוונטיות וגישה לפרוסות רב-פרויקטיות [G][770]; GF משווקת מודלים קריוגניים ל-FDX [C][353]; אין תקן פתוח למודלים של התקנים קריוגניים.

**מפות דרכים ועמידה בהבטחות.** Intel (הובטח 2022 · קיוביטים בקנה מידה של פרוסה · סופק 2024, Argonne 2026-01-06 [G][207][G:INTEL-2026]; אין ממשיך ואין מפת דרכים נכון ל-2026-09-03). Diraq (הובטח 2026-07-09 · "אלפים" עד 2029, נוסח מחדש ב-2026-08-27 כ-150,000 פיזיים · הוצגו שמונה קיוביטים [D][197][R][211][G:DIRAQ-FUNDING]). Quantum Motion (הובטח 2025-01 · מערכת ל-NQCC · סופקה 2025-09-15, ללא נאמנות שפורסמה [C][200], [803]). Quobly (הובטח 2025-12 · מדדים מאצוות ST ברבעון הראשון של 2026 [P][795] · לא נמצאו נכון ל-2026-09-03). GF, Anderon: לא הובטחו תאריכים לפרוסות [C][353], [798]. אמינות: imec/Diraq (פרסום בביקורת עמיתים, שחזור) ראשונות; Intel מייצרת בלי מסלול למוצר; Quantum Motion ו-Equal1 מספקות מערכות בלי מדדים שעברו ביקורת עמיתים (RacQ של Equal1, שנמכר בשם Bell-1 עד מאי 2026, מותקן במרכז של ESA בפרסקטי: ESA הודיעה על כך ב-2026-07-15 [G:ESA-BELL1-2026-07], ו-Equal1 ב-2026-07-31 [C][G:EQUAL1-RACQ-ESA-2026-07]), ו-Quobly עוד לא סיפקה אף מערכת; שקפי מפות הדרכים אחרונים.

**פרשנות אסטרטגית.** הצלחה תתגמל את מפעלי הייצור ואת הספקים (GF, imec, ST/Soitec, Bluefors), ואת ספקי הספינים שרשימת החומרים שלהם מצטמצמת לפרוסות ולמסדים; מסלולי הייצור הפרטניים (ליתוגרפיית STM, תהליכי lift-off במעבדות אוניברסיטאיות) ומפעלי מלכודות ה-MEMS יפסידו. כוח המיקוח של הספקים גבוה (קווים מעטים, הכנסה קוונטית זניחה), אך שלושה או ארבעה קווים חליפיים וכסף ממשלתי מגבילים את מה שמפעלי הייצור יכולים להפיק. איומי תחליף: חורים ב-Ge/SiGe, מפעלים לחיבורים פוטוניים, SFQ מול CMOS קריוגני.

## תחזית ושאלות פתוחות

אבני דרך, 12–24 חודשים: (1) התקן של 300 mm עם > 20 קיוביטים ו-2Q שפורסם לכל הזוגות ≥ 99.5% — מאשר; אם לא יופיע כזה עד סוף 2027 — מוריד בדרגה; (2) הרצות של פרוסות רב-פרויקטיות ב-SPINS עם ערכת תכנון תהליך קוונטית פומבית; (3) מכתב הכוונות של GF הופך לסופי, ומוצר קוונטי מוכרז בשמו על 22FDX; (4) אצוות קיוביטי ספין ב-Anderon מבית HRL, שבבעלות IBM מאז 2026-08-26; (5) Intel נוקבת בממשיך ל-Tunnel Falls, או יוצאת מהתחום.

התרחיש הטוב ביותר ל-2029: שני קווים מסחריים של 300 mm עם ערכות תכנון תהליך קוונטיות, מערכים של 10³ נקודות עם ריבוב על הפיסה, 2Q ≥ 99.5% כערך טיפוסי, זיכרון ספין מתחת לסף. הגרוע ביותר: שיעורי תקינות מסחריים של עשרות אחוזים, 2Q ב-99–99.6%, מפות דרכים שקוצצו שוב, והיחידה של GF מצטמצמת לזיווד עבור לקוחות של מוליכי-על ושל פוטוניקה.

שאלות פתוחות: האם אפשר להפוך את פיצול העמקים ואת רעש המטען לאחידים על פני הפרוסה, או שכל מערך יחייב בחירה בדיעבד? מהו שיעור התקינות מבחינת נאמנות הקיוביטים בזרימת תהליך של 300 mm? האם בקרה משותפת שומרת את השגיאה הקוהרנטית מתחת לסף? האם פגיעת הצמתים ביעד בתוך זרימת התהליך יכולה להגיע לדיוק של פחות מאחוז? לעקוב אחר מספר התקינות הראשון מבחינת נאמנות, אחר הפרוסה הרב-פרויקטית הראשונה של SPINS, אחר הענקות CHIPS סופיות, ואחר Intel.

## מקורות
[10] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [C]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[189] P. Steinacker *et al.*, “Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity,” *Nature*, vol. 646, no. 8083, pp. 81–87, Sep. 2025, doi: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9). [D]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[192] H. Edlbauer *et al.*, “An 11-qubit atom processor in silicon,” *Nature*, vol. 648, no. 8094, pp. 569–575, Dec. 2025, doi: [10.1038/s41586-025-09827-w](https://doi.org/10.1038/s41586-025-09827-w). [arXiv:2506.03567](https://arxiv.org/abs/2506.03567). [D]
[196] M. De Smet *et al.*, “High-fidelity single-spin shuttling in silicon,” *Nat. Nanotechnol.*, vol. 20, no. 7, pp. 866–872, Jun. 2025, doi: [10.1038/s41565-025-01920-5](https://doi.org/10.1038/s41565-025-01920-5). [D]
[197] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[199] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[200] Quantum Motion, “Quantum Motion Delivers the Industry's First Full-Stack Silicon CMOS Quantum Computer,” Sep. 15, 2025. [Online]. Available: https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ [C]
[207] L. Hesla, “Argonne launches silicon quantum processor collaboration with Intel,” Argonne National Laboratory, Jan. 6, 2026. [Online]. Available: https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel [G]
[211] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[293] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[294] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[296] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[347] ASP Isotopes Inc., “ASP Isotopes Inc. Commences Commercial Production of Enriched Silicon-28 at its Second Aerodynamic Separation Process (ASP) Enrichment Facility,” Mar. 27, 2025. [Online]. Available: https://ir.aspisotopes.com/news-events/press-releases/detail/56/asp-isotopes-inc-commences-commercial-production-of [C]
[348] U.S. Department of Energy, “DOE Advances Domestic Supply of Silicon, Germanium Isotopes for Quantum Computing,” HPCwire, Jul. 16, 2026. [Online]. Available: https://www.hpcwire.com/off-the-wire/doe-advances-domestic-supply-of-silicon-germanium-isotopes-for-quantum-computing/ [G]
[353] GlobalFoundries, “GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing,” May 21, 2026. [Online]. Available: https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ Also https://investors.gf.com/news-releases/news-release-details/globalfoundries-launches-quantum-technology-solutions-scale-us. [C]
[355] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[446] IonQ, “IonQ Achieves Landmark Result, Setting New World Record in Quantum Computing Performance,” Oct. 21, 2025. [Online]. Available: https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing [C]
[520] F. Borsoi *et al.*, “Shared control of a 16 semiconductor quantum dot crossbar array,” *Nat. Nanotechnol.*, vol. 19, no. 1, pp. 21–27, Jan. 2024, doi: [10.1038/s41565-023-01491-3](https://doi.org/10.1038/s41565-023-01491-3). [D]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[551] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[733] A. Knapen *et al.*, “Pinball: A Cryogenic Predecoder for Surface Code Decoding Under Circuit-Level Noise,” [arXiv:2512.09807](https://arxiv.org/abs/2512.09807), Dec. 2025. [S]
[766] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]
[767] E. J. Thomas *et al.*, “Rapid cryogenic characterization of 1,024 integrated silicon quantum dot devices,” *Nat. Electron.*, vol. 8, no. 1, pp. 75–83, Jan. 2025, doi: [10.1038/s41928-024-01304-y](https://doi.org/10.1038/s41928-024-01304-y). [D]
[770] imec, “Quantum pilot line 'SPINS' launched with EU support,” Apr. 3, 2026. [Online]. Available: https://www.imec-int.com/en/press/semiconductor-based-quantum-pilot-line-spins-launched-eu-support [G]
[771] University College Dublin, “Equal1 Announces $60 million in Funding to Accelerate Quantum Computing using Existing Semiconductor Manufacturing,” UCD Innovation, Jan. 15, 2026. [Online]. Available: https://www.ucd.ie/innovation/news-and-events/2026/equal1-announces-funding-round/ [C]
[793] R. Maurand *et al.*, “A CMOS silicon spin qubit,” *Nat. Commun.*, vol. 7, Art. no. 13575, Nov. 2016, doi: [10.1038/ncomms13575](https://doi.org/10.1038/ncomms13575). [D]
[794] A.-M. Zwerver *et al.*, “Qubits made by advanced semiconductor manufacturing,” *Nat. Electron.*, vol. 5, no. 3, pp. 184–190, Mar. 2022, doi: [10.1038/s41928-022-00727-9](https://doi.org/10.1038/s41928-022-00727-9). [D]
[795] C. Knowles, “Quobly runs silicon-28 quantum wafers through ST fab,” IT Brief Asia, Dec. 12, 2025. [Online]. Available: https://itbrief.asia/story/quobly-runs-silicon-28-quantum-wafers-through-st-fab [P]
[796] M. P. Losert *et al.*, “Practical strategies for enhancing the valley splitting in Si/SiGe quantum wells,” *Phys. Rev. B*, vol. 108, no. 12, Art. no. 125405, Sep. 2023, doi: [10.1103/PhysRevB.108.125405](https://doi.org/10.1103/PhysRevB.108.125405). [S]
[797] Equal1, “Equal1 advances scalable quantum computing with CMOS-compatible silicon spin qubit technology,” Apr. 16, 2025. [Online]. Available: https://www.equal1.com/post/commercial_cmos_process [C]
[798] IBM, “IBM and U.S. Department of Commerce Announce America's First Purpose-Built Quantum Foundry, Supported by Proposed $1 Billion CHIPS Award,” May 21, 2026. [Online]. Available: https://newsroom.ibm.com/ibm-and-u-s-department-of-commerce-announce-americas-first-purpose-built-quantum-foundry [C]
[799] Silex Systems, “SILEX Quantum Silicon (Q-Si) Production for Quantum Computing,” silex.com.au. [Online]. Available: https://www.silex.com.au/silex-technology/silex-zs-si-production-for-quantum-computing/ [C]
[800] Bluefors Oy, “Cryogenic Wafer Prober — Under 2 K with 300 mm Wafers,” bluefors.com, Jun. 10, 2026. [Online]. Available: https://bluefors.com/products/cryogenic-wafer-prober/ [C]
[801] FormFactor, Inc., “HPD IQ3000 - 4 K Cryogenic Probe Station,” Jun. 9, 2026. [Online]. Available: https://www.formfactor.com/product/quantum-cryo/quantum-wafer-multi-chip-cryogenic/iq3000/ [C]
[802] R. Acharya *et al.*, “Multiplexed superconducting qubit control at millikelvin temperatures with a low-power cryo-CMOS multiplexer,” *Nat. Electron.*, vol. 6, no. 11, pp. 900–909, Nov. 2023, doi: [10.1038/s41928-023-01033-8](https://doi.org/10.1038/s41928-023-01033-8). [D]
[803] H. Bennie, “Quantum Motion Announces Record Integration of Quantum Devices and Partnership with Semiconductor Manufacturer, GlobalFoundries,” quantummotion.com, Jan. 6, 2025. [Online]. Available: https://quantummotion.com/partnership-with-globalfoundries/ [C]
[804] Quobly, “Quobly Raises €115M Series A to Industrialize Silicon Quantum Computing,” HPCwire, Jun. 3, 2026. [Online]. Available: https://www.hpcwire.com/off-the-wire/quobly-raises-e115m-series-a-to-industrialize-silicon-quantum-computing/ [P]

## פריטי אימות פתוחים

- SPAM של תאי היחידה של imec/Diraq: 99.95% ב-100 µs [189] (ערך מגרסה v1, נשמר), לעומת 99.9% שנרשם לקו ה-300 mm של imec (2025).
- נאמנות ההסעה [196]: גרסה v1 נתנה 99.54%; התמצית מציינת "99.5% בממוצע"; נעשה שימוש בערך שבתמצית.
- המימון של Silex (A$5.1 M מ-Defence Trailblazer, A$4.35 M מ-SQC): הסכומים אינם מתוארכים בדף של Silex [799]; השורה בפנקס הכספים מתוארכת לפי השלמת המפעל ביוני 2026.
- [796] Losert ועמיתיו: הפרטים הביבליוגרפיים מצוטטים מהספרות המקובלת, ולא אומתו מול דף המוציא לאור.
- הושמטו מגרסה v1 כלא מאומתים כאן: "אחזקת הון של ~1% בידי Commerce" במכתב הכוונות של CHIPS ל-GF (גרסה v1 ציטטה את [300], [353], [798] יחד) וטענת ה-30× של IBM לתפוקת ההתקנים של Anderon (מקורה בעיתונות המקצועית בלבד). כל נתוני שיעור התקינות של Intel באים מ-[766], על 232 התקנים בני שתים-עשרה נקודות בפרוסה אחת: 99.8% מהנקודות, 96% מההתקנים השלמים, 91% הצלחה בחישת מטען; [199] חוזר על ה-96% בהפניה ל-[766].
