---
id: ro_erasure
name: בדיקת מחיקה באמצע המעגל
layer: 6 קריאה
status: demonstrated
since: 2023
one_line: בדיקה, באמצעות קיוביט עזר או פלואורנות, האם קיוביט עודנו במרחב הקוד שלו; היא מסמנת דעיכה או דליפה כמחיקה ממוקמת בלי לקרוא את המצב הלוגי.
verdict: הבדיקה פתורה בטרנסמונים (384 ns, שארית 6×10⁻⁴); לא פתורים שיעור המחיקות תחת שערים דו-קיוביטיים, השליליים השגויים ומס זמן המחזור. להוריד בדרגה אם עד סוף 2027 אף מערכת מחיקה לא תציג Λ > 2 לוגי.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

בדיקת מחיקה באמצע המעגל שואלת "האם הקיוביט הזה עדיין בתוך מרחב הקוד שלו?" ומחזירה בישור של ביט אחד, עם מיקומו של הקיוביט, בלי להפריע למצב הלוגי. היא זקוקה לקידוד שהדעיכה השולטת בו יוצאת ממרחב הקוד: מסילה כפולה (עירור אחד בשני טרנסמונים או בשני מהודים; האובדן משאיר ואקום שניתן לגלות) או קיוביט אטומי מטא-יציב (³P₀ ב-¹⁷¹Yb, D₅/₂ ב-⁴⁰Ca⁺), שהדעיכה שלו למצב היסוד פולטת פלואורנות תחת אלומה שהקיוביט אינו רואה. הצעות: Princeton/Yale, 2022-01 — 98% משגיאות ה-¹⁷¹Yb ניתנות להמרה, סף קוד המשטח 0.937%→4.15% [S][8]; טרנסמוני מסילה כפולה של AWS, 2022-08 [S][334]; מהודים של Yale, 2022-12 [S][399]. הדגמות: ¹⁷¹Yb ב-Princeton [D][141] ו-⁸⁸Sr ב-Caltech [D][143] ב-2023-05; טרנסמונים ב-AWS [D][400] ומהודים ב-Yale [D][401] ב-2023-07.

תכונות מגרף הטכנולוגיות (מקרא: a זיקה טבעי↔מיוצר; b זמן, דטרמיניסטי/מבושר; c מנגנון הקריאה, זמן, הרסני?, באמצע המעגל?; d ניידות; e בקרה @ מיקום; f מבנה השגיאה; g ייצור):
- a = 0.5, אדיש לנושא הקיוביט.
- b = לא ישים.
- c = בדיקת מחיקה בקיוביט עזר, 10⁻⁶·⁴ s ≈400 ns, לא הרסנית, באמצע המעגל — השיא בטרנסמונים [D][85], לא 20 µs של האטומים [D][141].
- d = אין.
- e = מיקרוגל @ טמפרטורת החדר (אטומים: אופטי).
- f = ניתן להמרה למחיקה (אובדן ממוקם ומבושר).
- g = אין (פרוטוקול, לא עצם).
דירוג 1 מתוך 111; משותף למשפחות מוליכי-העל והאטומים הניטרליים.

## פיזיקה וגבולות

בזוג טרנסמונים במסילה כפולה המצבים הלוגיים הם |10⟩ ו-|01⟩, ולכן רלקסציית T₁ של כל אחד מהטרנסמונים נוחתת ב-|00⟩. הבדיקה היא קריאה דיספרסיבית משותפת, המכוונת כך ששני המצבים הלוגיים מושכים את המהוד המשותף במידה שווה ואילו הוואקום מושך אותו אחרת; AWS מגיעה לפיצול לוגי שיורי של −0.7(5) kHz לעומת הסטה דיספרסיבית של −4.25 MHz [D][85]. בזוג מהודים קיוביט עזר הרגיש למספר הפוטונים הכולל עושה את אותה עבודה ב-1.82 µs [D][404]. באטומים, דעיכה מ-³P₀ ל-¹S₀ נתפסת ב-20 µs של פלואורנות על המעבר ¹S₀–¹P₁, הבלתי נראה לקיוביט המטא-יציב, ולכן השורדים צוברים פחות מ-10⁻⁵ שגיאה לכל בדיקה [D][141].

כל בדיקה עולה חשיפה אחת ל-T₁: AWS מודדת מחיקה של 2.54(1)×10⁻² לכל בדיקה של 384 ns לעומת שגיאה שיורית בלתי מגולה של 6.0(2)×10⁻⁴; היחס ביניהן, הטיית המחיקה של 42(1), הוא מה שמעניין קוד [D][85].

שלוש רצפות הן מהותיות. שליליים שגויים חוזרים אל הקוד כדליפה: שיעור השליליים השגויים של Yale, 3.7%, כפול שיעור המחיקה שלה נותן שיעור מחיקות מוחמצות של 9.0(5)×10⁻⁴ [D][404]; אצל AWS הם שגיאת ההפרדה של הקריאה, ≈0.8% [D][85]. פעולה חוזרת (back-action): אי-התאמה שיורית ב-χ גורמת לדה-פאזה של הקיוביט ב-8(3)×10⁻⁵ לכל בדיקה, וטון הקריאה מקצר את זמן חיי המחיקה למחצית כל עוד הוא פועל [D][85]. זמן: באטומים בדיקת 20 µs מתארכת ל-420 µs כאשר אוכלוסיית רידברג חייבת לדעוך לפני הדימות — ומכאן 56(4)% משגיאות השער החד-קיוביטי אך רק ≈33% משגיאות השער הדו-קיוביטי מומרות [D][141]. הקוד רואה מחיקה ממוקמת p_e, שארית פאולי ≈p_e/40 וזנב דליפה לא מבושר ≈FN×p_e; תחת ערוץ זה סף קוד המשטח הוא 4.15% [S][8], וקודים למחיקה מוטה מגיעים ל-8.2–10.3% [S][643]. הרצפה זזה עם T₁ ארוך יותר, קריאה חזקה יותר, ובאטומים — גילוי מהיר יותר של דליפת רידברג.

## מצב ההנדסה העדכני

המיטב שהודגם: קיוביט טרנסמון יחיד במסילה כפולה שנבדק ב-384 ns עם שארית של 6×10⁻⁴ (2026-04) [D][85]; CZ במהודים עם 0.5% מחיקה ו-0.03% שגיאת פאולי (2026-08) [D][84]. הטיפוסי בקנה מידה (3 בספטמבר 2026): שום דבר מעל עשרה קיוביטי מחיקה, למעט OQC GENESIS, 16 אתרי מסילה כפולה עם קריאה מגלה-שגיאות — ארבעת טרנסמוני המסילה הכפולה של SUSTech בנאמנות מצב בל לוגי של 98.8% (2025-04) [D][406], ו-Seeker בן 8 הקיוביטים של Quantum Circuits (2024-11) [C][86]. באטומים, בלוקי ה-[[4,2,2]] של Princeton [D][142] ומצב ה-GHZ של 20 אטומים ב-JILA [D][644] (2025-06) הם המעגלים הגדולים ביותר עם בדיקת מחיקה; 24 הקיוביטים הלוגיים של Microsoft/Atom Computing משתמשים בדימות אובדן בסוף הסבב, לא בבדיקות באמצע המעגל [D][149].

| שנה | נתון | מי | תג | מקור |
|---|---|---|---|---|
| 2023-05 | בדיקה של 20 µs בנאמנות גילוי 0.986; 56(4)% משגיאות ה-1Q מומרות | Princeton ¹⁷¹Yb | [D] | [141] |
| 2023-07 | מחיקה 2.19(2)×10⁻³ לשער, שארית נמוכה ≈40×, דה-פאזה <0.1% לבדיקה | טרנסמונים של AWS | [D] | [400] |
| 2024-06 | בדיקה באמצע המעגל של 1.82 µs, חיוביים שגויים (FP) 0.51%, שליליים שגויים (FN) 3.7% | מהודים של Yale | [D] | [404] |
| 2024-11 | מצב בל ב-⁴⁰Ca⁺ 98.56→99.14% עם השמטת מחיקות; בדיקה של 1 ms | Oregon | [D] | [393] |
| 2025-06 | CZ מגלה-שגיאות ב-¹⁷¹Yb 99.78(4)%, גילוי >90% של דעיכת רידברג | JILA | [D] | [644] |
| 2025-06 | טלפורטציה ב-[[4,2,2]] 0.771→0.802 עם קיוביטי עזר שנבררו לפי מחיקה | Princeton | [D] | [142] |
| 2026-04 | בדיקה של 384 ns, שארית 6.0(2)×10⁻⁴, הטיה 42(1) | AWS | [D] | [85] |
| 2026-08 | CZ במסילה כפולה 500 ns, מחיקה ≈0.5% לשער, פאולי 0.029(6)%, היפוך ביט 2.8(4)×10⁻⁶ | Quantum Circuits | [D] | [84] |

האיבר השולט כיום: בטרנסמונים — המחיקה במצב סרק במהלך הבדיקה (T₁ ≈25 µs); במהודים — הדה-קוהרנטיות של קיוביט העזר; באטומים — שגיאות דו-קיוביטיות שאינן ניתנות לגילוי וזמן המת של רידברג.

## ייצור, חומרים ושרשרת האספקה

מסילה כפולה בטרנסמונים משתמשת בליתוגרפיה הרגילה של מוליכי-על, אך הזוג חייב להיות בר-כוונון בשטף כדי למצוא נקודה שבה χ מותאם ולחמוק ממערכות דו-רמתיות, ושני הטרנסמונים חייבים להיות טובים — בעיית שיעור תקינות בריבוע; הדגימות של AWS לאורך חמישה ימים מתנודדות עם מערכות דו-רמתיות (TLS) קרובות לתהודה [D][85]. מסילה כפולה במהודים צריכה שני מהודים בעיבוד שבבי בעלי Q גבוה ועוד קיוביט עזר לכל קיוביט, בהרכבה ידנית — ומכאן התוכנית של Quantum Circuits, 8 → 17 → 49 → 181 קיוביטים לאורך 2024–2028 [R][94]. הבדיקה האטומית צריכה רק אלומת דימות ומצלמה. עלות ואנרגיה לכל קיוביט נבדק לא פורסמו. הבדיקה בטרנסמונים יורשת את שרשרת הקריאה הדיספרסיבית, שהמגברים והמקררים שלה הם הפריטים המרוכזים. החשיפה לפיקוח על יצוא: תקנת BIS מ-2024-09-06 [G][301] [G:BIS-QUANTUM-2024] מונה מגברים פרמטריים ו-CMOS קריוגני (3A901), מקררים של ≥600 µW ב-≤0.1 K (3A904) ומחשבים קוונטיים (4A906) — רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT שלהם נופלים באותה רצועה, מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך [G:BIS-3A901A-CRYOCMOS]; התקנה אינה אומרת אם קיוביט מסילה כפולה נספר כאחד או כשניים.

## בקרה, קריאה ועומס הקלט-פלט

מוליכי-על: מהוד קריאה אחד לכל קיוביט מסילה כפולה על קו הזנה מרובב, שני קווי שטף לכל קיוביט, TWPA אחד לכל קו — כפליים מהקלט-פלט של טרנסמון. החלפת קיוביט שנמחק בתוך המחזור דורשת הזנה קדימה של כמה מאות ns. ב-10³ קיוביטים החיווט הוא חומת הטרנסמונים כפול שניים; ב-10⁴ עובדים רק ריבוב קר או CMOS קריוגני, בעזרת הדגל בן הביט האחד; ב-10⁶ 384 ns למחזור ו-2×10⁶ טרנסמונים הם מחיר ההטיה של 40×. אטומים: פולס גלובלי אחד של 20 µs ופריים מצלמה אחד לכל בדיקה — הקווים אינם גדלים עם N, אך קריאת המצלמה והעיבוד (0.1–1 ms) קובעים את השהיית הלולאה, ופריימים מהירים עולים בהישרדות (98.80(44)% בדימות ה-¹⁷⁴Yb של Kyoto ב-17.6 µs [D][261]); החומה מעבר ל-10⁴ אטומים היא תקציב הפריימים.

## תפקיד במחסנית

שתי ארכיטקטורות: מחיקה במסילה כפולה במוליכי-על ואטומים ניטרליים אלקליים-עפרוריים. היא דורשת קידוד שבו מחיקה ניתנת לגילוי — מסילה כפולה, או הקידוד המטא-יציב "omg" (אופטי–מטא-יציב–יסוד) — ומספקת את הדגלים שקידודי המסילה הכפולה והקודים המותאמים למחיקה צורכים. היא דוחקת את סילוק הדליפה ואת הבחירה בדיעבד בטרנסמונים חשופים. מחיר המעבר הוא 2× טרנסמונים ועוד בדיקה בכל מחזור; באטומים המכלול המטא-יציב עולה בנאמנות חד-קיוביטית (99.12(4)% ב-³P₀ לעומת 99.968(3)% במצב היסוד של התקן ה-omg של JILA [D][645]). הזיווג "נושא מיוצר עם מבנה שגיאה של מחיקה" אמיתי; "נושא טבעי עם קריאה של ≤10 µs" ירוש מזמן הטרנסמון, ולא הושג בידי הבדיקה האטומית של 20 µs. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס: ארכיטקטורת המסילה הכפולה 2.8 µs, נקבע בידי שכבות השערים, כשהבדיקה של 0.40 µs היא שביעית ממנו; ארכיטקטורת האטומים 1.3 ms, נקבע בידי ההובלה, כשהבדיקה ≈1.5% ממנו. משבצות ריקות סמוכות: המפענח בשלב הקר (צרכן טבעי של בישורים בני ביט אחד) והמתמר מיקרוגל–אופטי.

## ראיות — כיצד נמדדו המספרים

החיוביים השגויים והשליליים השגויים (FP/FN) מתקבלים מהכנת |0_L⟩, |1_L⟩ והמצב המחוק ומחזרה על הבדיקה; AWS מצטטת FP ≈ FN ≈0.8% וגוזרת את השארית ואת ההטיה מרצפי בדיקות חוזרות ומרצפים משולבים תחת גילוי רציף [D][85]. שיעורי המחיקות ברמת השער הם סטטיסטיקה של דגלים, ושגיאת הפאולי השיורית היא התאמה ליניארית בעומק נמוך [D][84]. שיעורי ההמרה האטומיים נשענים על נאמנות הגילוי 0.986 [D][141]; נאמנות מצב בל ≥0.9971 של Caltech היא חסם לאחר השמטת המחיקות, מתוקן ל-SPAM [D][143].

מה שאינו נלכד: ההישרדות (כל נאמנות בולטת מותנית ב"אין מחיקה"; ב-2.5% לבדיקה, ארבעים בדיקות מקטינות את המדגם למחצית); שליליים שגויים, הנראים רק כדליפה בקוד רב-סבבי; דה-פאזה של קיוביטים צופים על קווי הזנה משותפים, שלא נמדדה מעבר לארבעה קיוביטים; סחיפה (תנודות מונעות-TLS לאורך 5–18 ימים [D][85]); מס הזמן. שחזורים בלתי תלויים: AWS (2023, 2026) [D][85], [400], Yale (2023, 2024) [D][401], [404], Quantum Circuits (2026) [D][84], SUSTech (2025) [D][406], UMass (2026) [D][405]; Princeton (2023, 2025) [D][141], [142], Caltech (2023) [D][143], JILA (2025) [D][644]; Oregon (2024) [D][393].

סתירות. D-Wave אומרת שהקיוביטים שלה מגלים "כ-90% מהשגיאות" [C][94]; ברמת השער השיעור הוא 83–94%, תלוי אם שארית הפאולי היא החסם <0.1% או ההתאמה 0.029% [D][84]. ההמרה הדו-קיוביטית באטומים היא 33–38% [D][141], [142] לעומת 98% שבהצעה [S][8]. הרווח של ה-[[4,2,2]] ממידע המחיקה הוא 1.9(4)× בטקסט ה-arXiv מ-2025-06 [D][142] אך 3.6× כפי שנישא בגרף מגרסת Nature Physics מ-2026-06 [D][142]; בשימוש ערך ה-arXiv, עד שיתקבל הטקסט המפורסם.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הוא עושה בבדיקה | ראיות |
|---|---|---|---|---|
| Quantum Circuits Inc. | מפתח | ארה״ב | קיוביטי מסילה כפולה במהודים; Seeker בן 8 קיוביטים; מערכת של 17 קיוביטים צפויה ב-2026; יחידה של D-Wave מאז 2026-01 | [D][84] [C][86] [G:DWAVE-QCI-2026-01] |
| AWS Center for Quantum Computing | מפתח | ארה״ב | בדיקה בטרנסמונים עם χ מותאם ב-384 ns | [D][85], [400] |
| Yale University | מחקר | ארה״ב | מקור המסילה הכפולה במהודים; בדיקה בקיוביט עזר | [D][401], [403], [404] |
| SUSTech (Shenzhen) | מחקר | סין | ארבעה קיוביטי טרנסמון במסילה כפולה | [D][406] |
| Princeton University | מחקר | ארה״ב | המרה מטא-יציבה ב-¹⁷¹Yb; [[4,2,2]] | [D][141], [142] |
| Google Quantum AI | מפתח | ארה״ב | מסלול אטומים בראשות Kaufman (לשעבר JILA, omg ב-¹⁷¹Yb), 2026-03 | [G:GOOGLE-ATOMS-2026-03] [P][158] [D][644], [645] |
| Atom Computing | מפתח | ארה״ב | מערכות של 1,225 אטומי ¹⁷¹Yb; גילוי אובדן בדימות; Magne עם Microsoft | [D][149] [G:MAGNE-2025-07] |

**כספים.**
- 2024-05 · Quantum Circuits · הרחבת סבב B · $26.5 M · Sequoia · ≈$84 M במצטבר · נסגר [P][646] [G:QCI-FUNDING]
- 2024-08-15 · Quantum Circuits · סגירת סבב B · >$60 M · ARCH, F-Prime, Sequoia, Hither Creek · חופף להרחבה · נסגר [C][647] [G:QCI-FUNDING]
- 2025-07-17 · QuNorth · הזמנת Magne, 50 קיוביטים לוגיים · €80 M · Atom Computing/Microsoft · הוזמן [G:MAGNE-2025-07]
- 2025-11-06 · DARPA QBI, שלב B · עד $15 M לכל אחד · אחד-עשר צוותים, אף לא ספק מסילה כפולה אחד · רשמי [G][65] [G:QBI-STAGEB-2025-11]
- 2026-01-07 · D-Wave · רוכשת את Quantum Circuits · $550 M ($300 M במניות + $250 M במזומן) · נסגרה 2026-01-19/20 [C][14], [648] [G:DWAVE-QCI-2026-01]
- 2026-05-21 · D-Wave; Atom Computing · מכתבי כוונות של CHIPS מטעם US DoC · $100 M לכל אחת · מכתב כוונות [G:CHIPS-LOI-2026-05]
- 2026-06-16 · Atom Computing · סבב C · $100 M · Third Point Ventures · >$300 M במצטבר · נסגר [C][154] [G:ATOM-300M-2026-06]
- 2026-08-06 · D-Wave · תוצאות המחצית הראשונה של 2026 · הכנסות $5.9 M (−67% לעומת אשתקד), מזומנים $546.2 M · דווח [G:DWAVE-FIN-2026]

**שוק ושרשרת אספקה.** איש אינו מוכר בדיקת מחיקה; היא רוכבת על המגברים והמקררים של הקריאה הדיספרסיבית (מרוכזים, ברשימת BIS [G][301]). כלכלת היחידה לא פורסמה; העלות המבנית היא 2× טרנסמונים או שני מהודים ועוד קיוביט עזר לכל קיוביט, לעומת הטענה של Quantum Circuits ל-10–20 פיזיים ללוגי במקום ~200 [C][86]. רק G3 ו-G4 משלמים, וזאת כאשר קודים ירוצו 10⁵–10⁶ סבבים.

**קניין רוחני ותקנים.** Amazon Technologies: US 11,748,652 B1, "Heralding of amplitude damping decay noise for quantum error correction" (Kubica, Retzker; הוגש 2021-12-10, הוענק 2023-09-05): דעיכה מבושרת דרך רמה שמחוץ למרחב הקוד, ובכלל זה מסילה כפולה [G][336]. Yale: US 12,288,135, קיוביט עזר עם ערוץ שגיאה אסימטרי (הוגש 2019-06-28, הוענק 2025-04-29) [G][408]. משפחות המהודים של Yale/Quantum Circuits נמצאות כעת בידי D-Wave. אין תקן; ההוראה HERALDED_ERASE של Stim [P][397] הופכת את צד הפענוח לסחורה.

**מפות דרכים ועמידה בהבטחות.**
- D-Wave: הובטח 2026-01-07 · מערכת מסילה כפולה ראשונית זמינה ב-2026 · לא סופק נכון ל-2026-09-03 [C][14].
- D-Wave: הובטח 2026-06-01 · 17 קיוביטים עם שגיאה לוגית נמוכה 2× מהפיזית (2026), 49 / 20× (2027), 181 / 2,000× (2028), 10 לוגיים (2030), 100 לוגיים (2032), Λ = 10 · תלוי ועומד, אין נתונים לוגיים [R][94] [G:DWAVE-QCI-2026-01].
אמינות: Quantum Circuits/D-Wave גבוהה בפיזיקה, לא מוכחת בתאריכים; AWS מפרסמת תוצאות ואינה מבטיחה מוצר; Princeton סיפקה את המחצית החד-קיוביטית של הצעתה מ-2022 [S][8] [D][141]; Atom Computing לפי לוח הזמנים, ללא התחייבות לבדיקות באמצע המעגל.

**פרשנות אסטרטגית.** אם בדיקות המחיקה יגדלו בקנה מידה, המנצחים יהיו מי שמחזיקים בייצור בעל T₁ גבוה ובשרשרת הקריאה — D-Wave, AWS והמחנה האלקלי-עפרורי (Atom Computing, Google); המפסידות יהיו מפות הדרכים של טרנסמונים חשופים, הקונות סף ב-Λ בלבד. איומי התחליף: קיוביטי מחיקה על קוטריטים [D][405] מסלקים את התקורה של 2×; דימות Yb מהיר [D][261] ופענוח מודע-אובדן שוחקים את הטיעון בעד קידודים מטא-יציבים. כוח המיקוח נשאר בידי ספקי הפלטפורמות, לא בידי הספקים.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם: D-Wave תספק את מערכת 17 הקיוביטים עם שגיאה לוגית מפורסמת הנמוכה 2× מהפיזית עד אמצע 2027 [R][94]; קבוצה כלשהי תריץ ≥10 סבבים של קוד במרחק 3 על קיוביטי מסילה כפולה ותדווח על ההישרדות; ההמרה הדו-קיוביטית באטומים תגיע ל-≥70% עם בדיקה של ≤50 µs; בדיקה עם χ מותאם תגיע ל-≤250 ns עם שארית ≤3×10⁻⁴. להוריד בדרגה אם עד סוף 2027 אף מערכת מחיקה לא תדווח על Λ >2 בנתונים לא מותנים. התרחיש הטוב ביותר עד 2029: 100–200 קיוביטי מסילה כפולה ב-Λ ≈4–10 עם מחזורים של 2 µs, ומכונות Yb המריצות קודים מודעי-מחיקה. התרחיש הגרוע ביותר: המחיקה נשארת מוצג ראווה של שני קיוביטים, בעוד טרנסמונים חשופים מגיעים ל-10⁻³ ול-Λ ≈3 בלעדיה.

שאלות פתוחות: (1) האם ההטיה של 40× שורדת בדיקות מקביליות על קיוביטים החולקים קווי הזנה? (2) האם אפשר להפוך דליפת רידברג לבהירה בתוך מיקרו-שניות? (3) מה עושה מפענח עם שליליים שגויים ב-10⁻³ כשהדליפה מצטברת? לעקוב: האספקה של D-Wave ב-2026, המאמר הרב-קיוביטי הבא של AWS, תוצאות ה-Yb של Google/Kaufman.

## מקורות
[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[84] N. Mehta *et al.*, “An entangling gate for dual-rail erasure qubits,” *Nature*, vol. 656, no. 8126, pp. 47–53, Aug. 2026, doi: [10.1038/s41586-026-10822-y](https://doi.org/10.1038/s41586-026-10822-y). [arXiv:2503.10935](https://arxiv.org/abs/2503.10935). [D]
[85] J. S.-C. Hung *et al.*, “Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout,” [arXiv:2604.16292](https://arxiv.org/abs/2604.16292), Apr. 2026. [D]
[86] Quantum Circuits, “Quantum Circuits Makes Error-Detecting Qubits,” Nov. 19, 2024. [Online]. Available: https://quantumcircuits.com/resources/quantum-circuits-make-error-detecting-qubits/ [C]
[94] M. Swayne, “D-Wave's New Gate-Model Roadmap Puts Pin in 2032 For 100 Logical-Qubit System,” The Quantum Insider, Jun. 1, 2026. [Online]. Available: https://thequantuminsider.com/2026/06/01/d-waves-new-gate-model-roadmap-puts-pin-in-2032-for-100-logical-qubit-system/ [R]
[141] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493). [D]
[142] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[143] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[149] B. W. Reichardt *et al.*, “Fault-tolerant quantum computation with a neutral atom processor,” [arXiv:2411.11822](https://arxiv.org/abs/2411.11822), Nov. 2024. [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[158] M. Swayne, “Google Paves a Two-Lane Quantum Roadmap by Adding Neutral Atom Systems,” The Quantum Insider, Mar. 24, 2026. [Online]. Available: https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/ [P]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[334] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461). [S]
[336] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]
[393] A. Quinn *et al.*, “High-fidelity entanglement of metastable trapped-ion qubits with integrated erasure conversion,” *Phys. Rev. A*, vol. 113, no. 4, Art. no. L040601, Apr. 2026, doi: [10.1103/p3cy-8yjk](https://doi.org/10.1103/p3cy-8yjk). [arXiv:2411.12727](https://arxiv.org/abs/2411.12727). [D]
[397] quantumlib, “Gates supported by Stim,” GitHub. [Online]. Available: https://github.com/quantumlib/Stim/blob/main/doc/gates.md [P]
[399] J. D. Teoh *et al.*, “Dual-rail encoding with superconducting cavities,” *Proc. Natl. Acad. Sci. USA*, vol. 120, no. 41, Art. no. e2221736120, Oct. 2023, doi: [10.1073/pnas.2221736120](https://doi.org/10.1073/pnas.2221736120). [arXiv:2212.12077](https://arxiv.org/abs/2212.12077). [S]
[400] H. Levine *et al.*, “Demonstrating a long-coherence dual-rail erasure qubit using tunable transmons,” *Phys. Rev. X*, vol. 14, no. 1, Art. no. 011051, Mar. 2024, doi: [10.1103/PhysRevX.14.011051](https://doi.org/10.1103/PhysRevX.14.011051). [arXiv:2307.08737](https://arxiv.org/abs/2307.08737). [D]
[401] K. S. Chou *et al.*, “Demonstrating a superconducting dual-rail cavity qubit with erasure-detected logical measurements,” [arXiv:2307.03169](https://arxiv.org/abs/2307.03169), Jul. 2023. [D]
[403] A. Koottandavida *et al.*, “Erasure Detection of a Dual-Rail Qubit Encoded in a Double-Post Superconducting Cavity,” *Phys. Rev. Lett.*, vol. 132, no. 18, Art. no. 180601, May 2024, doi: [10.1103/PhysRevLett.132.180601](https://doi.org/10.1103/PhysRevLett.132.180601). [arXiv:2311.04423](https://arxiv.org/abs/2311.04423). [D]
[404] S. J. de Graaf *et al.*, “A mid-circuit erasure check on a dual-rail cavity qubit using the joint-photon number-splitting regime of circuit QED,” *npj Quantum Inf.*, vol. 11, no. 1, Jan. 2025, doi: [10.1038/s41534-024-00944-4](https://doi.org/10.1038/s41534-024-00944-4). [arXiv:2406.14621](https://arxiv.org/abs/2406.14621). [D]
[405] B.-J. Liu *et al.*, “Hardware-Efficient Erasure Qubits With Superconducting Transmon Qutrits,” [arXiv:2604.08672](https://arxiv.org/abs/2604.08672), Apr. 2026. [D]
[406] W. Huang *et al.*, “Logical multi-qubit entanglement with dual-rail superconducting qubits,” *Nat. Phys.*, vol. 22, no. 4, pp. 591–597, Mar. 2026, doi: [10.1038/s41567-026-03211-9](https://doi.org/10.1038/s41567-026-03211-9). [arXiv:2504.12099](https://arxiv.org/abs/2504.12099). [D]
[408] Justia, “Shruti PURI Inventions, Patents and Patent Applications - Justia Patents Search.” [Online]. Available: https://patents.justia.com/inventor/shruti-puri [G]
[643] K. Sahay, J. Jin, J. Claes, J. D. Thompson, and S. Puri, “High-Threshold Codes for Neutral-Atom Qubits with Biased Erasure Errors,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041013, Oct. 2023, doi: [10.1103/PhysRevX.13.041013](https://doi.org/10.1103/PhysRevX.13.041013). [arXiv:2302.03063](https://arxiv.org/abs/2302.03063). [S]
[644] A. Senoo *et al.*, “High-fidelity entanglement and coherent multi-qubit mapping in an atom array,” [arXiv:2506.13632](https://arxiv.org/abs/2506.13632), Nov. 2025. [D]
[645] J. W. Lis *et al.*, “Mid-circuit operations using the omg-architecture in neutral atom arrays,” [arXiv:2305.19266](https://arxiv.org/abs/2305.19266), May 2023. [D]
[646] M. Swayne, “Quantum Circuits Inc. Quietly Raises $26.5 Million,” The Quantum Insider, May 29, 2024. [Online]. Available: https://thequantuminsider.com/2024/05/29/quantum-circuits-inc-quietly-raises-26-5-million/ [P]
[647] Quantum Circuits, Inc., “Quantum Circuits Secures More Than $60 Million in Series B Investment,” PR Newswire, Aug. 15, 2024. [Online]. Available: https://www.prnewswire.com/news-releases/quantum-circuits-secures-more-than-60-million-in-series-b-investment-302221428.html [C]
[648] D-Wave Quantum Inc., “D-Wave Completes Acquisition of Quantum Circuits Inc., Creating World's Leading Quantum Computing Company,” Business Wire, Jan. 19, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260119513563/en/D-Wave-Completes-Acquisition-of-Quantum-Circuits-Inc.-Creating-Worlds-Leading-Quantum-Computing-Company [C]

## פריטי אימות פתוחים

- הרווח של ה-[[4,2,2]] ממידע המחיקה: 1.9(4)× ב-arXiv:2506.13724 v1 [D][142] לעומת 3.6× שנישא בגרף מגרסת Nature Physics [D][142]; לא ניתן היה לקרוא את הטקסט הראשי המפורסם (nature.com מציג את התמצית בלבד; phys.org החזיר HTTP 429).
- סכום סבב A של Quantum Circuits מ-2017 (דווח $18 M, Canaan/Sequoia) לא אומת ממקור ראשוני; הושמט.
- המימון המצטבר של Quantum Circuits, ≈ $84 M עד מאי 2024, הוא נתון מהעיתונות המקצועית [P][646]; ההודעה של החברה אינה נוקבת בסך כולל.
- האם Quantum Circuits הייתה החברה ה-18, שלא נזכרה בשמה, בשלב A של DARPA QBI: DARPA נוקבת בשמן של 17 מתוך 18 [G:QBI-STAGEA-2025-04]; לא יושב.
- עלות או אנרגיה לכל קיוביט נבדק: אף שחקן אינו מפרסם אותן.
- ספירות פטנטים למשפחות המהודים במסילה כפולה של Yale/Quantum Circuits: לא זמינות ממאגר נקוב; מצוטטים שני פטנטים בודדים.
- נאמנויות מצב בל ביונים מטא-יציבים ב-Oregon: 98.61 → 99.16 % (סיכומי התמצית) לעומת 98.56 → 99.14 % (הטקסט המלא של arXiv v1) [D][393]; בשימוש הטקסט המלא.
- ההוצאה של AWS על תוכנית המסילה הכפולה שלה והמענקים שמאחורי הקבוצות ב-Princeton, ב-Caltech, ב-Yale, ב-Oregon וב-SUSTech: לא נמסרו, או שאינם ניתנים לייחוס לפרימיטיב זה.
- המין האטומי של מסלול האטומים הניטרליים של Google אינו מצוין במקורות נגישים; לא נטען.
