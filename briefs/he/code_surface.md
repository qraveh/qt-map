---
id: code_surface
name: קוד המשטח המסובב (+ גרסאות רתומות)
layer: 7 קוד
status: demonstrated
since: 2023
one_line: קוד מייצב מסוג CSS במשקל 4 על סריג ריבועי; הקוד היחיד עם נתוני חומרה מתחת לסף בשלוש פלטפורמות, והיקר ביותר.
verdict: קוד ברירת המחדל משום שאינו צריך דבר מלבד סריג סטטי מדרגה 4; ב-Λ ≈ 2 הוא עולה 600–1,500 פיזיים ללוגי. להוריד בדרגה אם זיכרון qLDPC יגבר עליו בחומרה לפני סוף 2027.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

קוד מייצב מסוג CSS: פלאקטים (plaquettes) של X ושל Z במשקל 4 על סריג ריבועי, ובמשקל 2 על השפה. הפריסה המסובבת — זו שכולם בונים — מציבה קיוביט לוגי אחד ב-d² קיוביטי נתונים ו-d²−1 קיוביטי מדידה: טלאי במרחק 7 הוא 97 קיוביטים פיזיים. שגיאות מופיעות כזוגות של פגמי סינדרום, שמפענח מזווג על פני גרף זיווג תלת-ממדי (שני ממדי מרחב, d סבבים) לכדי מסגרת פאולי. מוצא: קוד הטורוס של Kitaev (1997) [S][649]; הזיכרון המישורי והסף שלו אצל Dennis, Kitaev, Landahl ו-Preskill (2002) [S][650]; הפריסה המסובבת של d² קיוביטים אצל Bombín ו-Martín-Delgado (2007) [S][651]; ניתוח סריג (lattice surgery) אצל Horsman et al. (2011) [S][652]; הקאנון ההנדסי אצל Fowler et al. (2012) [S][653]; הרתימה (yoking) אצל Gidney et al. (2023) [S][654].

תכונות מגרף הטכנולוגיות (a זיקה; b זמן; c קריאה; d ניידות; e בקרה @ מיקום; f מבנה השגיאה כפי שהקוד רואה אותו; g ייצור): a = 0.5, אדיש לנושא הקיוביט — פריסה, לא התקן, כש-b ו-c ירושים מהמארח ו-e, g אינם קיימים משלו; d = סטטי, הטלאים זזים רק בניתוח סריג; f = פאולי, ההנחה המגדירה והחולשה המגדירה, שכן כל מה שאינו היפוך X/Z — דליפה, אובדן, הטיה, מחיקה — הוא מידע מושלך או נזק לא ממודל. דירוג 7 מתוך 111; משותף למשפחות מוליכי-העל, האטומים הניטרליים והספינים.

## פיזיקה וגבולות

הקוד הופך שיעור שגיאות פיזי p לשיעור לוגי היורד אקספוננציאלית ב-d, כל עוד p נמצא מתחת לסף. Λ, המקדם שבו יורדת השגיאה הלוגית לכל שני צעדי מרחק, הוא הכלכלה כולה: ב-Λ = 2.14 הפחתה פי עשרה בשגיאה הלוגית עולה שלושה גורמים של Λ (log 10 / log 2.14 ≈ 3.0), כלומר הגדלה של d בכ-6 — מ-d = 7 זה ~3.5× קיוביטים, שכן טלאי דורש 2d²−1. הסף תלוי במפענח וברעש: 0.937% תחת רעש דה-פולריזציה אחיד ברמת המעגל [S][8], אך 0.55% למפענח החומרה הלא-משוקלל של Riverlane לעומת 0.7% לזיווג משוקלל תחת דליפה [D][238]. כל Λ שמצוטט מתאר מפענח לא פחות משהוא מתאר שבב.

שלוש רצפות הן מהותיות. שטח וזמן: קיוביט לוגי הוא 2d²−1 קיוביטים פיזיים ופעולה לוגית עולה d סבבים, ולכן מ-7.72×10⁻⁴ ב-d=7 עם Λ ≈ 2 [D][2], הגעה ל-10⁻⁶ דורשת d ≈ 25 ויותר מ-1,200 פיזיים ללוגי, אלא אם p יורד מתחת ל-10⁻³; ב-p = 10⁻³ טביעת הרגל של מכונת teraquop (טריליון פעולות לוגיות) היא כ-1,500 פיזיים ללוגי בקוד הפשוט, 800 עם רתמות חד-ממדיות ו-600 עם רתמות דו-ממדיות [S][654], או כ-650 בקוד הפשוט עם זיווג מתואם [S][655]. שגיאות שאינן פאולי: דליפה מייצרת סינדרומים שהזיווג אינו יכול להסביר, ואובדן אטומים ניתן לטיפול רק אם המפענח מקבל הודעה היכן אירע. פרצים מתואמים: Google רואה אירועים בערך מדי שעה, המקבעים רצפה סמוך ל-10⁻¹⁰ ללא תלות ב-d [D][1]. מה שמזיז את הרצפה הוא הנדסת מבנה השגיאה — הטיה, מחיקה, סילוק דליפה — בדיוק מה שהקוד הזה משליך; הרתמות מזיזות רק את הקבוע.

## מצב ההנדסה העדכני

המיטב שהודגם נכון ל-3 בספטמבר 2026: זיכרון במרחק 7 עם שגיאה לוגית של 7.72×10⁻⁴ למחזור על Willow של Google בן 105 הקיוביטים, עם כיול בלמידת חיזוק בתוך לולאת תיקון השגיאות [D][2]. הטיפוסי בקנה מידה: אין. אף ספק אינו מוכר קיוביט לוגי של קוד המשטח; שערים לוגיים דו-קיוביטיים קיימים רק ב-d=3 [D][43]; באטומים הקוד רץ על 448 אטומים לאורך ארבעה סבבים [D][4].

| שנה | נתון | מי | תג | מקור |
|---|---|---|---|---|
| 2023-02 | d=5 ב-2.914(16)%/מחזור לעומת ממוצע d=3 של 3.028(23)% | Google | [D] | [602] |
| 2024-12 | Λ = 2.14 ± 0.02 (d=3→5→7); d=7 ב-0.143(3)%/מחזור; 2.4(3)× מהקיוביט הפיזי הטוב ביותר; 10⁶ מחזורים ב-d=5 | Google (Willow) | [D] | [1] |
| 2025-11 | 448 אטומים: 2.14(13)× על פני d=3→5 בארבעה סבבים; פענוח בלמידת מכונה מודע-אובדן שווה 1.73(13)× | Harvard/MIT/QuEra | [D] | [4] |
| 2025-12 | Local Clustering Decoder בפחות מ-1 µs/סבב על FPGA עד d=17; חיסכון של 4× בקיוביטים (d=33→17) תחת דליפה | Riverlane | [D] | [238] |
| 2025-12 | התקן של 107 קיוביטים מתחת לסף ב-d=7, Λ = 1.40(6) | USTC | [D] | [3] |
| 2026-07 | CNOT לוגי בין שני טלאים ב-d=3, נאמנות 0.643, ללא בחירה בדיעבד | USTC | [D] | [43] |

האיבר השולט: שגיאת השער הדו-קיוביטי, כ-40% מתקציב קוד הצבע המקביל על אותו שבב [D][41], אחריה דליפה וקריאה, ואחריהן פרצים ששום d גדול יותר אינו מסלק [D][1].

## ייצור, חומרים ושרשרת האספקה

לקוד אין ייצור משלו; הוא כופה ייצור — סריג סטטי מדרגה 4, קיוביט מדידה בין כל זוג קיוביטי נתונים, קריאה לא הרסנית באמצע המעגל בכל קיוביט עזר, ואחידות, משום שכל 2d²−1 הקיוביטים חייבים לעבוד. זו בעיית שיעור תקינות ב-d², והסיבה לכך ש-Google רשמה פטנט על גרסאות הסובלות קיוביטים מתים [G][656]. שרשרת האספקה האמיתית שלו היא שרשרת הפענוח: המפענח של Riverlane תופס כ-6% מהלוגיקה של Xilinx VU19P ב-d=17 [D][238], ומשפחת ה-FPGA הזאת היא ממקור יחיד (AMD), וכך גם חלופת ה-GPU (NVIDIA, זמן הלוך-ושוב של 3.84 µs על NVQLink [G:NVQLINK-2025]). העלות לקיוביט לוגי לא פורסמה. החשיפה לפיקוח על יצוא: תקנת BIS האמריקנית מ-2024-09-06 [G:BIS-QUANTUM-2024] מפקחת על מקררים (3A904), ועל מחשבים קוונטיים (4A906) רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT שלהם נופלים באותה רצועה, מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך [G:BIS-3A901A-CRYOCMOS]; טלאי במרחק 5, 49 קיוביטים, נתפס רק בשגיאת C-NOT של 10⁻⁴ או טובה ממנה.

## בקרה, קריאה ועומס הקלט-פלט

כל מחזור מודד ומאפס כל קיוביט עזר: ב-Willow, 48 ביטי מדידה בכל 1.1 µs לטלאי במרחק 7, בערך 44 Mbit/s של סינדרום לכל קיוביט לוגי [D][1]. המפענח חייב לצרוך את הזרם הזה מהר יותר משהוא מגיע, אחרת הפיגור מתבדר — פחות ממיקרו-שנייה לסבב במארג FPGA [D][238] לעומת השהיה ממוצעת של 63 µs ב-d=5 אצל Google ב-2024 [D][1]. ב-10³ קיוביטים החומה היא החיווט לכל קיוביט; ב-10⁴ היא רוחב הפס של הסינדרום אל מחוץ למקרר — הטיעון בעד פענוח מקדים בשלב הקר (מחקר על CMOS קריוגני טוען להפחתה של 3,780× בהספק של 0.56 mW ב-4 K [S][G:PINBALL-2025-12]); ב-10⁶ הפענוח הוא בעיית הזרמה בקנה מידה של מרכז נתונים, שגודלה נקבע לפי קצב הסינדרום, לא לפי מספר הקיוביטים.

## תפקיד במחסנית

חמש ארכיטקטורות נושאות אותו: טרנסמונים מוליכי-על, אטומים ניטרליים אלקליים, אטומים אלקליים-עפרוריים עם מחיקה מובנית, ספינים בנקודות קוונטיות בצורן/גרמניום וספיני תורמים בצורן. הוא דורש רק סריג סטטי של שכנים קרובים — הסיבה לכך שהוא ברירת המחדל — מארח מפעלי מצבי קסם (טיפוח מצבי קסם מגיע ל-0.9999(1) בשיעור קבלה של 8% [D][42]) ומזין מפענחי FPGA ומפענחים עצביים [D][238], [657]. הוא מוחלף בידי קוד הצבע (שערים טובים יותר, שיפוע גרוע יותר: Λ₃/₅ = 1.56 על אותו שבב [D][41]), בידי קודי qLDPC מסוג bivariate bicycle (288 פיזיים ל-12 לוגיים לעומת כ-3,000 קיוביטים של קוד המשטח [D][248]) ובידי קודים טרנסוורסליים בעלי קצב גבוה על אטומים ניידים — ואינו מורכב איתם. הוא מתנגש עם קיוביטי חתול (קוד לא מוטה מבזבז את ההטיה), עם קידודי מסילה כפולה (הזיווג משליך את דגלי המחיקה) ועם גילוי הרסני. עלויות המעבר פועלות לשני הכיוונים: עזיבה קונה קיצוץ של 3–10× בתקורה ודורשת קישוריות שאין לחומרה; הישארות עולה 600–1,500 פיזיים ללוגי [S][654]. זו הטכנולוגיה היחידה בשכבת הקוד שהיא באמת אדישה לפלטפורמה, ולכן חברת מפענחים יכולה להתקיים. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס: 0.65 µs נגזר על סריג הטרנסמונים לעומת מחזור נמדד של 1.1 µs, כשהקריאה והאיפוס הם שני שלישים ממנו ולא השערים של 25–40 ns [D][1]; 1.31 ms באטומים, נקבע בידי ההובלה. משבצות ריקות סמוכות: מפענח בתוך המקרר, וטלאים חוצי-מודולים — שום קוד לא רץ על פני שני מודולים.

## ראיות — כיצד נמדדו המספרים

Λ הוא התאמה של השגיאה הלוגית למחזור מול d, ושלושה דברים הופכים אותו לרך. תלוי במפענח: אותם נתוני Sycamore נותנים 3.028% בפענוח ברשת טנזורים ו-2.901% ב-AlphaQubit ב-d=3 [D][602], [657]. תלוי בתת-הקבוצה: טלאי d=7 מוסיף קיוביטים גרועים יותר לקבוצת ה-d=5. תלוי במשך: מעגלים של ארבעה סבבים [D][4] לעולם אינם רואים את פיזיקת הסחיפה והפרצים שריצה של 10⁶ מחזורים רואה [D][1]. מה שאינו נלכד: אוכלוסיות דליפה, פרצים, הטיית הישרדות בטעינה מחדש, כשל מפענח בזמן אמת. שוחזר באופן בלתי תלוי — Google [D][1], [2], USTC [D][3], Harvard/MIT/QuEra [D][4].

סתירות. Λ לכל שני צעדי מרחק: 2.14 ± 0.02 (Google, d=3→7) [D][1] לעומת 1.40(6) (USTC) [D][3] לעומת 2.14(13)× (אטומים, ארבעה סבבים, אבד בטעינה מחדש) [D][4] — רעש שונה, לא קודים שונים, ורק זה של Google שורד מיליון מחזורים. סף: 0.937% [S][8] לעומת 0.55–0.7% תחת דליפה [D][238]; יש לתקצב לפי השני.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Google Quantum AI | מפתח | ארה״ב | זיכרון Willow עד d=7, השיא ב-d=7, AlphaQubit, תאוריית הקודים הרתומים | [D][1], [2], [657] [S][654] |
| IBM | מפתח | ארה״ב | הריצה גרסאות heavy-hex של קוד המשטח על Falcon; מפת הדרכים נוטשת אותן לטובת qLDPC מסוג bivariate bicycle מטעמי תקורה | [D][248] [G:IBM-ROADMAP] |
| Riverlane | ספק | בריטניה | ספק תיקון השגיאות הייעודי היחיד; Local Clustering Decoder, פחות מ-µs לסבב על FPGA | [D][238] [C][658] |
| Harvard/MIT + QuEra | מחקר + מפתח | ארה״ב | קוד המשטח על 448 אטומים עם פענוח בלמידת מכונה מודע-אובדן | [D][4] [G:QUERA-230M-2025] |
| USTC, Zhejiang University | מחקר | סין | d=7 מתחת לסף; CNOT לוגי ב-d=3; ניתוח סריג ב-125 קיוביטים | [D][3], [43], [44] |
| NVIDIA, Qblox | ספקים | ארה״ב, הולנד | NVQLink ומערכי בקרה הסוגרים את לולאת הפענוח בזמן אמת | [G:NVQLINK-2025] [C][659] |

**כספים.** איש אינו מממן קוד; אלה תוצרים הנקובים ביחידות של קוד המשטח.
- 2024-05-01 · Riverlane · מענק EIC Transition של Horizon Europe (SkyTALE, עם Qblox) · £2.1 M · הוענק [C][660]
- 2024-08-06 · Riverlane · סבב C · $75 M · Planet First Partners מובילה, עם ETF Partners, EDBI, Cambridge Innovation Capital, Amadeus · נסגר [C][661]
- 2025-11-06 · DARPA · QBI, שלב B · עד $15 M לכל אחד, אחד-עשר צוותים; IBM ספקית הטרנסמונים היחידה, ותוכניתה qLDPC [G:QBI-STAGEB-2025-11]
- 2026-03-12 · Riverlane · הודעת מפת הדרכים טוענת לגיוס של $120 M+ ולסבב C של "$85 M" · סותר את ההודעה מ-2024 [C][658]
- 2026-06-02 · IBM · התחייבות לקוונטים · >$10 B על פני חמש שנים · הוכרז [G:IBM-10B-2026-06]

**שוק ושרשרת אספקה.** המוצר היחיד שאפשר למכור כאן הוא המפענח ושילובו; Riverlane היא הספק הייעודי היחיד, הטוענת ליותר מ-20 שותפויות עם יצרנים ומעבדות לאומיות [C][658]; NVIDIA הופכת את מסלול ה-GPU לסחורה. סיכון הריכוזיות נמצא במעלה השרשרת (AMD/Xilinx, NVIDIA, שוק מקררים של שני ספקים); כלכלת היחידה לא פורסמה מעבר ל-600–1,500 הפיזיים ללוגי שכל קונה משלם [S][654]. רק G3 ו-G4 משלמים עליו.

**קניין רוחני ותקנים.** Google LLC, US 12,518,194, "Surface codes with densely packed gauge operators" (הוענק 2026-01-06) [G][656]; Riverlane Ltd, GB 2641501 A, "Quantum decoder" (פורסם 2025-12-10) [G][662]. הקוד הוא ידע קודם מ-1997–2007 שאינו ניתן לרישום כפטנט [S][649], [651], ולכן המאבק הוא על מפענחים ועל פריסות. אין תקן; הממשקים הם קוד פתוח — Stim, PyMatching, Deltakit [P][397].

**מפות דרכים ועמידה בהבטחות.**
- Google: הובטח 2023-02 · אבן דרך 3, "קיוביט לוגי ארוך-חיים" ב-10⁻⁶ · לא הושג; המיטב 7.72×10⁻⁴ ב-d=7 [D][2] [C][32].
- IBM: הובטח 2025-06-10 · Kookaburra, המודול הראשון של זיכרון qLDPC עם לוגיקה, ב-2026 · לא סופק נכון ל-2026-09-03 [G:IBM-ROADMAP].
- Riverlane: הובטח 2026-03-12 · megaquop לפני סוף העשור, gigaquop בתחילת שנות ה-2030, teraquop מ-2033 · תלוי ועומד [C][658].
אמינות: Google סיפקה כל אבן דרך שהכריזה עליה, באיחור אך באמת, והיא היחידה שיש לה מספרים השורדים מיליון מחזורים; IBM מבצעת אך נטשה את הקוד הזה; Riverlane מספקת חומרה שעברה ביקורת עמיתים; למחנה האטומים יש סיפור התקורה הטוב ביותר ונתוני המשך החלשים ביותר [G:QUERA-LIBRA-2026].

**פרשנות אסטרטגית.** אם קוד המשטח יישאר סוס העבודה, המנצחים יהיו מי שיהפכו את הקיוביטים הפיזיים לזולים ואת המחזורים למהירים — מחנה מוליכי-העל — ועוד שרשרת אספקה של מפענחים המוכרת לכל פלטפורמה. המפסידים הם כל מי שטיעונו הניח 10² פיזיים ללוגי: ב-600–1,500, מכונה של 200 קיוביטים לוגיים היא מכונה של 10⁵ קיוביטים — הסיבה המוצהרת של IBM לעזיבה [D][248]. איומי התחליף מתוארכים: qLDPC בנקודת האיזון ביונים לכודים, קודים טרנסוורסליים על אטומים ניידים, קודים מותאמים למחיקה. כוח המיקוח נמצא בידי ספקי הפלטפורמות, למעט בפענוח בזמן אמת, שרובם מעדיפים לקנות ולא לבנות.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם: קבוצה כלשהי תדווח על Λ ≥ 3 לאורך ≥10⁵ מחזורים; שער לוגי דו-קיוביטי ב-d ≥ 5 יגיע ל-99% ללא בחירה בדיעבד; טלאי ירוץ על פני שני מודולים; טלאים רתומים יופיעו בחומרה. להוריד בדרגה אם זיכרון qLDPC יגבר על טלאי של קוד המשטח במספר קיוביטים שווה לפני סוף 2027. התרחיש הטוב ביותר עד 2029: כמה מאות קיוביטים לוגיים ב-10⁻⁶ על 10⁵–10⁶ קיוביטים פיזיים, והפענוח סחורה — מה ש-Starling ו-Libra מניחים. התרחיש הגרוע ביותר: Λ נשאר סמוך ל-2, d ≈ 25 נשאר מחירו של 10⁻⁶, והקוד שורד רק כמדד ביצועים. שאלות פתוחות: (1) האם Λ מחזיק מעל 10³ קיוביטים פיזיים, שם ההפרעה ההדדית והסחיפה גדלות אחרת? (2) האם הרתימה יכולה לרוץ בחומרה, או שפענוח הקוד החיצוני מכשיל את תקציב הזמן האמת? (3) כמה מהשיא של 2026 הוא כיול ולא פיזיקה, בהינתן שהיגוי בלמידת חיזוק לבדו הזיז את d=7 מ-1.43×10⁻³ ל-7.72×10⁻⁴? לעקוב: צעד המרחק הבא של Google ו-Kookaburra של IBM.

ניתוח סריג המפוצל בין שני מעבדים המחוברים בקישור פוטוני אינו שומר מאליו על מרחק d בתפר: ממשק ישר של זוגות בל נותן d + 1 על תוצאת המיזוג, אך רק ⌊(d + 1)/2⌋ על הגודל הנצפה הניצב, חלוקה בזיגזג משיבה את d, ותפר היתוך של מצב אשכול ליניארי נותן 2d + 1 ו-d — מרחקים הסופרים רק תקלות בממשק [P][893].

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[32] Y. Chen and M. Devoret, “Our quantum hardware: the engine for verifiable quantum advantage,” Google Blog, Oct. 22, 2025. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ [C]
[41] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[42] E. Rosenfeld *et al.*, “Magic state cultivation on a superconducting quantum processor,” [arXiv:2512.13908](https://arxiv.org/abs/2512.13908), Dec. 2025. [D]
[43] W. Lin *et al.*, “Surface code logical operations on a superconducting quantum processor,” [arXiv:2607.01473](https://arxiv.org/abs/2607.01473), Jul. 2026. [D]
[44] Y. Wang *et al.*, “A superconducting surface-code processor with lattice-surgery logical operations,” [arXiv:2606.06598](https://arxiv.org/abs/2606.06598), Jun. 2026. [D]
[238] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[248] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[397] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[602] R. Acharya *et al.*, “Suppressing quantum errors by scaling a surface code logical qubit,” *Nature*, vol. 614, pp. 676–681, Feb. 2023, doi: [10.1038/s41586-022-05434-1](https://doi.org/10.1038/s41586-022-05434-1). [D]
[649] A. Y. Kitaev, “Fault-tolerant quantum computation by anyons,” *Annals of Physics*, vol. 303, no. 1, pp. 2–30, 2003, doi: [10.1016/S0003-4916(02)00018-0](https://doi.org/10.1016/S0003-4916(02)00018-0). [arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021). [S]
[650] E. Dennis, A. Kitaev, A. Landahl, and J. Preskill, “Topological quantum memory,” *Journal of Mathematical Physics*, vol. 43, no. 9, pp. 4452–4505, 2002, doi: [10.1063/1.1499754](https://doi.org/10.1063/1.1499754). [arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143). [S]
[651] H. Bombin and M. A. Martin-Delgado, “Optimal resources for topological two-dimensional stabilizer codes: Comparative study,” *Phys. Rev. A*, vol. 76, no. 1, Art. no. 012305, 2007, doi: [10.1103/PhysRevA.76.012305](https://doi.org/10.1103/PhysRevA.76.012305). [arXiv:quant-ph/0703272](https://arxiv.org/abs/quant-ph/0703272). [S]
[652] D. Horsman, A. G. Fowler, S. Devitt, and R. Van Meter, “Surface code quantum computing by lattice surgery,” *New Journal of Physics*, vol. 14, Art. no. 123011, Nov. 2011, doi: [10.1088/1367-2630/14/12/123011](https://doi.org/10.1088/1367-2630/14/12/123011). [arXiv:1111.4022](https://arxiv.org/abs/1111.4022). [S]
[653] A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland, “Surface codes: Towards practical large-scale quantum computation,” *Phys. Rev. A*, vol. 86, no. 3, Art. no. 032324, Sep. 2012, doi: [10.1103/PhysRevA.86.032324](https://doi.org/10.1103/PhysRevA.86.032324). [arXiv:1208.0928](https://arxiv.org/abs/1208.0928). [S]
[654] C. Gidney, M. Newman, P. Brooks, and C. Jones, “Yoked surface codes,” [arXiv:2312.04522](https://arxiv.org/abs/2312.04522), Dec. 2023. [S]
[655] C. Gidney and C. Jones, “New circuits and an open source decoder for the color code,” [arXiv:2312.08813](https://arxiv.org/abs/2312.08813), Dec. 2023. [S]
[656] Google LLC, “Surface codes with densely packed gauge operators,” U.S. Patent 12,518,194 B2, Jan. 6, 2026. [Online]. Available: https://patents.google.com/patent/US12518194B2/en Also https://patents.justia.com/search?q=%22surface+code%22+quantum+error+correction&company=google. [G]
[657] J. Bausch *et al.*, “Learning high-accuracy error decoding for quantum processors,” *Nature*, vol. 635, no. 8040, pp. 834–840, Nov. 2024, doi: [10.1038/s41586-024-08148-8](https://doi.org/10.1038/s41586-024-08148-8). [D]
[658] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [C]
[659] Qblox; Riverlane, “Qblox and Riverlane Demonstrate Integration Enabling Real-Time Quantum Error Correction,” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[660] Riverlane, “Riverlane awarded £2.1m by Horizon Europe to develop the next generation of its quantum error correction decoder,” May 1, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-awarded-2-1m-by-horizon-europe-to-develop-the-next-generation-of-its-quantum-error-correction-decoder [C]
[661] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[662] A. B. Ziad, A. Zalawadiya, B. Barber, and L. Skoric, “Quantum decoder,” Google Patents, Dec. 10, 2025. [Online]. Available: https://patents.google.com/patent/GB2641501A/en [G]
[893] F. Burt *et al.*, “Loss-tolerant distributed lattice surgery using fusion networks,” [arXiv:2610.01923](https://arxiv.org/abs/2610.01923), Oct. 2026. [P]

## פריטי אימות פתוחים

- סבב C של Riverlane: $75 M בהודעה מ-2024-08-06 [C][661] לעומת "$85 מיליון ב-2024" ו-"$120 מיליון+" במצטבר בהודעת מפת הדרכים מ-2026-03-12 [C][658]; שניהם מצוינים, ובשימוש הנתון הראשוני מ-2024.
- טביעות הרגל הרתומות (≈1,500 / ≈800 / ≈600 פיזיים ללוגי ב-p = 10⁻³) לקוחות מתיאור משני של arXiv:2312.04522 [S][654].
- Bombín ו-Martín-Delgado (2007) [S][651] מצוטטים עבור הפריסה המסובבת לפי הייחוס המקובל; דף התמצית ב-arXiv אינו נושא מטא-נתונים.
- רצפת השגיאה של ריצת 10⁶ המחזורים עצמה במאמר Willow [D][1] אינה מצוטטת כאן; מצוטטים רק d=7, Λ, היחס 2.4(3)× ורצפת הפרצים 10⁻¹⁰.
- עלות או אנרגיה לקיוביט לוגי: לא פורסמו. ההכנסות של Riverlane וערכי החוזים שלה: לא נמסרו.
- טרום-הפרסומים של USTC על CNOT לוגי ושל Zhejiang על ניתוח סריג [D][43], [44] לקוחים מהרשימה שעברה בדיקת עובדות של הדוח הראשי.
