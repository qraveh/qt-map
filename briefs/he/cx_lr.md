---
id: cx_lr
name: מצמדים לטווח ארוך על השבב (מצמדי c, בסדר גודל של mm)
layer: 4 קישוריות והובלה
status: emerging
since: 2023
one_line: מצמדים ברי-כוונון המוארכים במוליך גל או במהוד, השוזרים קיוביטים מוליכי-על נייחים המרוחקים מילימטרים זה מזה, וקונים את הגרפים מדרגה 6 שקודי qLDPC צריכים.
verdict: CZ אחד על פני 2 mm ב-99.81% (IQM, 2023) ורכיבי Loon של IBM ללא מספרים; להוריד בדרגה אם עד סוף 2027 אף מצמד של ≥ 5 mm לא ידווח על CZ של ≥ 99.5% עם פסי שגיאה.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

מצמד לטווח ארוך על השבב הוא רכיב מיקרוגל — קבל מוארך, מקטע של קו תמסורת, מהוד או שרשרת שלהם, בדרך כלל עם טרנסמון או SQUID בר-כוונון בשטף באמצע — המתווך אינטראקציית חילוף או ZZ בין קיוביטים מוליכי-על שאינם שכנים בסריג, המרוחקים מילימטרים זה מזה, באמצעות חילוף פוטונים וירטואליים דרך האופן המוסט של המבנה. אפיק המהוד של Yale מ-2007-09 העביר אינפורמציה קוונטית בין קיוביטים "בצדדים מנוגדים של שבב" דרך מהוד "באורך של כמה מילימטרים" [D][477]; האטומים הענקיים של MIT, המצומדים למוליך גל אחד בכמה נקודות, העניקו ב-2020-07 לקיוביטים מרוחקים חילוף חסין דה-קוהרנטיות [D][478]; אפיק המטא-חומר של Caltech העניק ב-2023 לעשרה קיוביטים טווח דילוג בר-כוונון [D][479]. רשומת הגרף מתארכת את הטכנולוגיה ל-2023, כאשר IQM פרסמה CZ של 99.81 ± 0.02% בין טרנסמונים המרוחקים 1.96 mm זה מזה, דרך מצמד טרנסמון צף ששני "מאריכי מוליך הגל" שלו נושאים הן את הצימוד קיוביט–מצמד והן את הצימוד הישיר קיוביט–קיוביט [D][480]. ה"מצמד c" (c-coupler) של IBM (מינוח מ-2025-06; "מצמדי l" מקשרים בין שבבים [C][481]) הוא אותו עצם, שנבנה עבור קוד, ו-Loon (2025-11) הוא השבב הראשון הטוען לסריג שלהם [C][49].

תכונות (מקרא: a = זיקה טבעי↔מיוצר; b = זמן, דטרמיניסטי/מבושר; c = קריאה; d = ניידות; e = בקרה @ מיקום; f = מבנה השגיאות; g = ייצור), בציטוט מרשומת הגרף:
- a = 1.0: נושא מיוצר לחלוטין.
- b = אין זמן אופייני, הדטרמיניזם אינו ישים: הקישור אינו קובע שעון; ה-CZ שהוא מארח דטרמיניסטי, 33 ns בהתקן השיא [D][480].
- c = אין פונקציית קריאה.
- d = טווח ארוך: קישוריות מעבר לשכן הקרוב בלי להזיז את הקיוביט.
- e = אין אופן בקרה ואין מיקום בקרה: קו השטף נזקף לחשבון הקיוביטים המחוברים.
- f = קוהרנטית: ZZ שיורי, כיול שגוי של הפאזה, הפרעה הדדית.
- g = ליתוגרפיה של מוליכי-על.
דירוג 2 מתוך 111; משותף לארכיטקטורות מוליכי-העל והריפוי; הוא מצרף נושא מיוצר לניידות לטווח רחוק.

## פיזיקה וגבולות

ב-4 GHz על צורן אורך הגל המונחה הוא כ-30 mm, ולכן מאריכי ה-2 mm של IQM הם קבלים קצרים חשמלית; נקודת הסרק של המצמד היא 3.195 GHz, מתחת לקיוביטים שב-4.10 וב-3.89 GHz, עם צימודי קיוביט–מצמד של 51.5 ו-53.9 MHz לעומת צימוד ישיר של 3.7 MHz, והחילוף נטו הוא ההפרש ביניהם [D][480]. השער הוא סטיית שטף של המצמד, המפעילה את האינטראקציה |11⟩↔|20⟩ למשך 22 ns ועוד 11 ns של סרק; ההפרדה גם מורידה את הצימוד לשכן השני אל מתחת ל-30 kHz [D][480]. מעבר לכמה מילימטרים, אופני הגל העומד של המאריך עצמו נכנסים לתחום התדרים של הקיוביטים (קו חצי-גל של 1 cm מהדהד סביב 6 GHz), ולכן הצימוד חייב לבוא מאופן היברידי של מהוד–טרנסמון: המצמד של 1 cm של Nanjing מודד 23.5 MHz של צימוד XX ועד 100 MHz של ZZ, הניתנים למיתוג ביחס של יותר מ-10² ו-10⁴, בהתאמה [D][482]. קישורים של 1 cm עד 0.5 m קיימים רק בסימולציה [S][483]–[485].

ארבע רצפות. אובדן: אופן מצמד עם T₁ > 40 µs [D][480] עולה לכל היותר 33 ns/40 µs ≈ 8×10⁻⁴ לשער, ו-~10⁻⁵ בהשתתפות דיספרסיבית — מתחת ל-1.9 ± 0.2 ×10⁻³ של השיא, המיוחס "בעיקר" לירידת ה-T₁ של קיוביט אחד ל-14 µs במהלך סטיית השטף [D][480]. צפיפות: כל אופן נוסף הוא התנגשות תדרים, וצומת מדרגה 6 מחזיק שישה מצמדים מחוץ לתהודה בבת אחת. שגיאה קוהרנטית: ZZ שיורי של פחות מ-2 kHz [D][480] הוא 0.013 rad של פאזה מותנית לכל מיקרושנייה של סרק לכל זוג, מתואם ולא סטוכסטי. גאומטריה: דרגה מעל ארבע מחייבת הצלבות, ולכן שכבות ניתוב; גרף טאנר של קוד bivariate bicycle הוא "גרף מדרגה 6 המורכב משני תת-גרפים מישוריים זרים בקשתות" [D][248], ולכן מבחינה טופולוגית שתי שכבות מספיקות. הרצפה זזה עם שכבות ניתוב בעלות הפסדים נמוכים יותר — Loon טוען ל"שכבות ניתוב מרובות, איכותיות ובעלות הפסדים נמוכים" [C][49] — ועם קיוביטים שה-T₁ שלהם שורד כוונון שטף.

## מצב ההנדסה העדכני

המיטב שהודגם: CZ של 99.81(2)% על פני 1.96 mm ב-33 ns (IQM, פורסם 2023-02) [D][480]. הטיפוסי בקנה מידה, נכון ל-3 בספטמבר 2026: אין — אף מעבד רב-קיוביטי עם מצמדים בסדר גודל של mm לא פרסם נאמנויות שער; Loon מציג "חיבורי קיוביטים שישה-כיווניים" ללא מספרים [C][49], [486], והתקני Star של IQM, בעלי רכזת מהוד, מגיעים ל"מעל 99.3%" ברצף MOVE–CZ–MOVE [C][487].

| שנה | נתון | מי | תג | מקור |
|---|---|---|---|---|
| 2007-09 | שני קיוביטים בצדדים מנוגדים של שבב, המצומדים דרך אפיק מהוד באורך כמה mm | Yale | [D] | [477] |
| 2023-02 | CZ 99.81(2)% על פני 1.96 mm, 33 ns, ZZ < 2 kHz | IQM | [D] | [480] |
| 2025-03 | מהוד כוכב של 6 קיוביטים: שגיאה לוגית של [[4,2,2]] למחזור 0.25(2)–0.91(3)% | IQM | [D] | [488] |
| 2025-05-20 | Advantage2 בזמינות כללית, 4,400+ קיוביטים בדרגה 20 (16 מצמדים פנימיים + 2 חיצוניים + 2 מסוג odd) | D-Wave | [C] | [489] [G:DWAVE-FIN-2026] |
| 2025-06 | מצמד אופן היברידי של 1 cm, XX 23.5 MHz, ניגודיות ZZ > 10⁴, ללא שער | Nanjing | [D] | [482] |
| 2025-11-12 | Loon: חיבורים שישה-כיווניים, מצמדים ארוכים יותר, ניתוב רב-שכבתי, ללא מספרים | IBM | [C] | [49], [486] |

איבר השגיאה השולט כיום: רלקסציית הקיוביט במהלך סטיית השטף (T₁,eff של 14 µs בקיוביט אחד ו-43 µs בשני) [D][480]; לסריגים מדרגה 6 התקציב לא פורסם.

## ייצור, חומרים ושרשרת האספקה

ליתוגרפיה סטנדרטית של צמתי ג'וזפסון מ-Nb/Al, ועוד ניתוב רב-שכבתי בעל הפסדים נמוכים כדי שמצמדים יוכלו לחצות שורות של קיוביטים. IBM בונה את Loon על פרוסות של 300 mm ב-Albany NanoTech, וזוקפת לזכות הקו "עלייה של פי עשרה" במורכבות השבב [C][49], [486]; דוח ה-10-K של D-Wave מתאר "תהליך של מעגלים משולבים רב-שכבתיים" [G][490]. כל מצמד בר-כוונון מוסיף צומת ג'וזפסון וקו שטף: מודול של קוד gross עם 288 קיוביטים בדרגה 6 [D][248] נושא 864 מצמדים אם כולם ברי-כוונון, שלושה לקיוביט לעומת 1.8 ב-Nighthawk (218 מצמדים, 120 קיוביטים) [C][49]. שיעור התקינות לכל מצמד לא פורסם.

שרשרת האספקה: IBM מייצרת בתוך הבית יחד עם NY CREATES [C][49]; IQM ב-Espoo [D][480]; D-Wave משתמשת ב"מפעלי ייצור קיימים של צד שלישי", הדגימה מקור שני עם ה-2000Q LN [G][491], ודוחות ה-10-K שלה מזכירים את SkyWater (תשעה אזכורים בחיפוש טקסט מלא, 2023–2026) [G][492] — מפעל ייצור שנמצא מאז 2026-07-31 בבעלות IonQ, מתחרה מפלטפורמה אחרת [C][493] [G:IONQ-SKYWATER-2026]. נקודות הכשל היחידות הן שלושה או ארבעה מפעלים בעלי תהליכים רב-שכבתיים מוסמכים בעלי הפסדים נמוכים. החשיפה לפיקוח על יצוא: התקנה של BIS מ-2024-09-06 [G][301] [G:BIS-QUANTUM-2024] מפקחת על מקררי דילול (3A904) ועל מחשבים קוונטיים רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT נופלים באותה רצועה — מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך (4A906) — לא על תכנוני מצמדים.

## בקרה, קריאה ועומס הקלט-פלט

מצמד בר-כוונון לטווח ארוך צריך קו שטף אחד ופולס שטף בסדר גודל של 22 ns [D][480]; רכזת מהוד קבועה אינה צריכה קו כזה, אך משלמת בפעולות MOVE [C][487], [494]. בדרגה 6 קווי השטף של המצמדים לבדם הם שלושה לקיוביט, מעבר להנעה, לשטף הקיוביט ולקריאה המרובבת — חמישה עד שישה קווים לקיוביט. ב-10³ קיוביטים מדובר ב-5,000–6,000 קווים ובריבוב בשלב הקר; ב-10⁴ — ב-40,000 הקווים ש-QuantWare מבטיחה ל-2028 [C][536] [G:QUANTWARE-VIO]; ב-10⁶ רק יצירת שטף על השבב (CMOS קריוגני או SFQ, כשבקרת ה-mK של SEEQC היא האינדיקציה שפורסמה [G:SEEQC-2026]) סוגרת את הפער. השהיית הלולאה אינה משתנה: סבב של קוד bivariate bicycle הוא "מעגל בעומק 7 המורכב משערי CNOT בין שכנים קרובים" [D][248]; מה שהמצמד מזיז הוא המפענח, שכן לקודי ה-bicycle חסרים מפענחי הזיווג השומרים על פענוח קוד המשטח בתוך מיקרושנייה.

## תפקיד במחסנית

שתי ארכיטקטורות: טרנסמונים מוליכי-על וריפוי קוונטי. הוא דורש ליתוגרפיה של מוליכי-על עם ניתוב רב-שכבתי, ומספק את הבדיקות לטווח ארוך מדרגה 6 שקודי bivariate bicycle צורכים: 12 קיוביטים לוגיים ב-288 פיזיים, במקום שבו קוד משטח צריך "כמעט 3000" בשגיאה פיזית של 0.1% [D][248], ו-121 קיוביטים לוגיים ממערכת gross של 5,000 קיוביטים ב-p = 10⁻³ במחקר הארכיטקטורה של IBM, שדרגתה "אינה עולה על שבע" [S][496]. הוא מחליף את המצמדים לשכנים קרובים במחיר של צומת ג'וזפסון וקו שטף לכל קשת נוספת, שתי שכבות ניתוב או יותר, ומצמד שה-T₁ שלו והאופנים הטפיליים שלו נכנסים לתקציב — מחיר המשולם לכל תכנון, לא לכל שער. בהשוואה בין המשפחות: נושא מיוצר שקונה בליתוגרפיה את הניידות לטווח רחוק שאטומים ויונים מקבלים מתנועה. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס עבור הארכיטקטורה: בארכיטקטורת הטרנסמונים הסבב הוא 0.65 µs, והקריאה, 282 ns, היא האיבר הגדול בו; ה-CZ לטווח ארוך של 33 ns [D][480] הוא 5% מהסבב, ומגביל רק אם רצף MOVE–CZ–MOVE עולה על איבר הקריאה; בארכיטקטורת הריפוי, לוח הזמנים של הריפוי הוא השעון. משבצות ריקות סמוכות: מצמד ה-l משבב לשבב שהובטח ל-Cockatoo של IBM ב-2027 [R][481], וקישור המהוד לקיוביטי ספין, שבו Delft הראתה תנודות iSWAP בין ספינים המרוחקים 250 µm זה מזה [D][497] ללא נאמנות שער.

## ראיות — כיצד נמדדו המספרים

ה-99.81% הוא מידוד אקראי משולב (interleaved RB), ושגיאתו, 1.9(2)×10⁻³, פורקה בסימולציה לחלק המוגבל בקוהרנטיות, שבו שולט ה-T₁,eff של 14 µs של קיוביט אחד; ה-ZZ < 2 kHz נמדד בנקודת הסרק [D][480]. הנתונים של Nanjing הם צימודים ספקטרוסקופיים, לא שערים [D][482]. תוצאות הכוכב של IQM הן נאמנויות של מצבים לוגיים של קוד [[4,2,2]], הכוללות בתוכן את הקריאה והסרק [D][488]; ה"מעל 99.3%" שלה הוא נתון של החברה ללא פרוטוקול [C][487]. הטענות על Loon הן נוסח של הודעה לעיתונות [C][49], [486].

מה שאינו נמדד: הפרעה הדדית על מאריכים משותפים כשכמה מצמדים של אותו צומת פועלים יחד; ה-T₁ בנקודות השטף שכל מצמד כופה על הקיוביטים שלו; דליפה אל אופני המאריך; סחיפה של נקודת האיפוס של ה-ZZ. שחזורים בלתי תלויים של CZ בסדר גודל של mm עם פסי שגיאה: אין, נכון ל-3 בספטמבר 2026. סתירות: דרגה 6 [D][248] לעומת "אינה עולה על שבע" [S][496] — הקשת השביעית היא המתאם ליחידת הלוגיקה, ולכן שתיהן נכונות; ה-"≥ 2 mm" של רשומת הגרף הוא ה-1.96 mm של המאמר [D][480]; ה-99.3% של IQM (תא Constellation) וה-99.81% (זוג מבודד) הם פעולות שונות, לא נסיגה.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הוא עושה בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| IBM | מפתח | ארה״ב | מצמדי c ב-Loon; מודול qLDPC של Kookaburra (2026); Starling (2029) | [C][49], [481] [G:IBM-ROADMAP] |
| IQM Quantum Computers | מפתח | פינלנד | שיא המצמד של 2 mm; רכזות Star; Constellation ב-2030+ | [D][480] [C][70], [487], [494] |
| D-Wave Quantum | מפתח | ארה״ב | מחשבי ריפוי Zephyr מדרגה 20 | [C][489] [G:DWAVE-FIN-2026] |
| Nanjing University | מחקר | סין | מצמד אופן היברידי של 1 cm; תאוריה של ZZ לטווח ארוך | [D][482] [S][484] |
| QuTech | מחקר | הולנד | קישור מהוד בין ספינים המרוחקים 250 µm זה מזה | [D][497] |
| SkyWater Technology | ספק | ארה״ב | מפעל הייצור הנקוב בדוחות ה-10-K של D-Wave; בבעלות IonQ מאז 2026-07-31 | [G][492] [C][493] |
| QuantWare | ספק | הולנד | שבבים בניתוב תלת-ממדי; מפת הדרכים VIO-40K | [P][495] |
| DARPA | מממן | ארה״ב | שלב B של QBI כולל את IBM (עד $15 M) | [G][65] [G:QBI-STAGEB-2025-11] |

**כספים.**
- 2025-09-03 · IQM · סבב B · $320 M · נסגר [G:IQM-LISTING-2026-07]
- 2025-11-06 · DARPA QBI שלב B · IBM בין אחד-עשר הצוותים · עד $15 M לכל צוות · רשמי [G][65] [G:QBI-STAGEB-2025-11]
- 2026-05-21 · IBM/Anderon; D-Wave; GlobalFoundries · מכתבי כוונות של CHIPS מטעם US DoC · $1 B (+ $1 B במזומן מ-IBM); $100 M; $375 M · מכתבי כוונות, לא מחייבים [G][300] [G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · התחייבות להשקעה קוונטית · > $10 B על פני חמש שנים · הוכרזה [C][57] [G:IBM-10B-2026-06]
- 2026-07-02 · IQM · רישום למסחר ב-Nasdaq וב-Helsinki · מזומנים פרו-פורמה €337 M; הכנסות המחצית הראשונה של 2026 €8.9 M · נסגר [C][58] [G:IQM-LISTING-2026-07]
- 2026-07-31 · IonQ · רכישת SkyWater · ~$1.8 B · נסגרה [C][19] [G:IONQ-SKYWATER-2026]
- 2026-08-06 · D-Wave · תוצאות הרבעון השני של 2026 · הכנסות המחצית הראשונה $5.9 M (הרבעון השני $3.1 M), מזומנים $546.2 M · דווחו [C][15] [G:DWAVE-FIN-2026]

**שוק ושרשרת אספקה.** איש אינו מוכר מצמד לטווח ארוך; זהו רכיב תכנון בתוך השבב של ספק, והשוק הוא שלושה או ארבעה מפעלים שמסוגלים להדפיס אותו — Albany [C][49], המפעל של IQM עצמה [D][480], מפעלי הייצור של צד שלישי של D-Wave [G][491], [492], GlobalFoundries במסגרת מכתב הכוונות שלה [G:CHIPS-LOI-2026-05] — ועוד QuantWare, המוכרת המסחרית היחידה של שבבים בניתוב תלת-ממדי [P][495]. העלות המבנית היא 1.5–3 מצמדים נוספים לקיוביט, מול חיסכון של 10× בקיוביטים פיזיים לכל קיוביט לוגי [D][248]. מי משלם: G4 (Starling של IBM), G3 אם Kookaburra יפעל, G5 בארכיטקטורת הריפוי [C][489], G1/G2 באמצעות פחות פעולות SWAP ברכזות Star [C][494].

**קניין רוחני ותקנים.** IBM: US 12,517,856 (הוגש 2022-09-28, הוענק 2026-01-06) על רמות קישוריות מודולריות, US 12,587,192 (הוענק 2026-03-24) על שרשראות מהודים עם מצמדים השראתיים ברי-כוונון, US 2024/0169232 A1 (הוגש 2022-11-18) על צימוד לטווח ארוך של פלוקסוניום [G][498]. D-Wave: US 10,268,622 (הוענק 2019-04-23), US 11,507,871 ו-US 11,494,683 (שניהם 2022-11) על מצמדים לטווח ארוך [G][498]. לא נמצאה התדיינות משפטית; אין תקן. הסקירה של PatSnap שפורסמה ב-2026-06-30 מונה ל-IBM 4,388 משפחות פטנטים קוונטיות, 783 מהן בהתקני מוליכי-על [P][G:PATSNAP-2026-06]; אין ספירה למצמדים לטווח ארוך.

**מפות דרכים ועמידה בהבטחות.**
- IBM: הובטח 2025-06-10 · Loon ב-2025 עם מצמדי c · סופק 2025-11-12 כרכיבים ללא נתוני ביצועים [C][49], [481].
- IBM: הובטח 2025-06-10 · Kookaburra ב-2026, Cockatoo ב-2027 (מצמדי l), Starling ב-2029 (200 לוגיים, 10⁸ שערים) · Kookaburra לא סופק נכון ל-2026-09-03, והשאר תלויים ועומדים [R][481] [C][72] [G:IBM-ROADMAP].
- IQM: הובטח 2026-01-05 · נאמנות 2Q מעל 99.94% ב-2025–26; מדגימי qLDPC ב-2027–28; Constellation עם מצמדים לטווח ארוך ב-2030+ · תלוי ועומד [R][70].
- D-Wave: תואר 2021-09-22 · טופולוגיית Zephyr · סופקה עם הזמינות הכללית של Advantage2 ב-2025-05-20 [C][489] [G:DWAVE-FIN-2026].
אמינות: IBM מספקת את המעבד שהיא נוקבת בו בשנה שבה היא נוקבת (Nighthawk סופק 2025-12 [G:IBM-ROADMAP]), אך לא פרסמה אף נתון של מצמד עשרה חודשים אחרי Loon; IQM סיפקה את תוצאת הפיזיקה של 2023 ומספקת מערכות Star, עם מפת דרכים שאינה נוקבת במספרי קיוביטים; D-Wave סיפקה את הטופולוגיה שלה בקנה מידה, לריפוי בלבד.

**פרשנות אסטרטגית.** אם מצמדים בסדר גודל של mm יגיעו לנאמנות של שכנים קרובים בדרגה 6, מספר הקיוביטים הפיזיים לכל קיוביט לוגי יירד בסדר גודל [D][248]; המנצחים יהיו הספקים המחזיקים הן במצמד והן בקוד — IBM ובהמשך IQM — ועוד המפעלים המחזיקים בתהליכים רב-שכבתיים; המפסידות יהיו מפות הדרכים של קוד המשטח על סריגי שכנים קרובים, כולל זו של Google [G:GOOGLE-ATLANTIC-2025-10]. איומי תחליף: מצמדי l משבב לשבב [R][481]; אטומים ויונים, המקבלים קישוריות מתנועה; שערי שכנים קרובים טובים יותר עם רשתות SWAP. כוח המיקוח נמצא בידי ספקי הפלטפורמות בתכנון ובידי המפעלים המעטים בשכבות הניתוב; IonQ–SkyWater הוא המקרה הראשון של ספק פלטפורמה המחזיק במפעל הייצור הנקוב בשמו של מתחרה [G][492] [G:IONQ-SKYWATER-2026].

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם: IBM תפרסם נאמנויות CZ של מצמדי c של ≥ 99.5% עם פסי שגיאה ב-≥ 5 mm, וניסוי זיכרון של קוד gross על Kookaburra, עד סוף 2027 [G:IBM-ROADMAP]; קבוצה כלשהי תדגים CZ על השבב על פני ≥ 1 cm ב-≥ 99.5% [D][482]; IQM תציג תא Constellation ב-≥ 99.9% [C][487]. להוריד בדרגה אם עד סוף 2027 אף מצמד בסדר גודל של mm לא ידווח על ≥ 99.9%, או שאף קוד עם בדיקות לטווח ארוך על חומרת מוליכי-על לא ידווח על Λ > 1. התרחיש הטוב ביותר עד 2029: מודולים ברמת Starling של קודי gross בני 288 קיוביטים עם מצמדים ב-99.9% [D][248] [R][481]. התרחיש הגרוע ביותר: המצמדים נשארים ב-99.8% על זוגות מבודדים, קודי qLDPC נודדים לאטומים וליונים, והמכונה של IBM ל-2029 הופכת למכונת קוד משטח.

שאלות פתוחות: (1) האם ה-T₁ של קיוביט שורד את נקודות השטף ששישה מצמדים כופים עליו? (2) מהי ההפרעה ההדדית בשערים מקביליים בצומת שהמאריכים שלו חולקים שכבת ניתוב? (3) איזה מפענח מריץ קודי bicycle בתוך זמן המחזור? לעקוב: כל מאמר של IBM על מצמדים, מצבו של Kookaburra ב-2026, תאריך המוצר של Constellation של IQM, השער של 1 cm של Nanjing.

## מקורות
[15] D-Wave Quantum Inc., “D-Wave Reports Second Quarter 2026 Results,” Aug. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ [C]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[49] IBM, “IBM Delivers New Quantum Processors, Software, and Algorithm Breakthroughs on Path to Advantage and Fault Tolerance,” Nov. 12, 2025. [Online]. Available: https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance [C]
[57] IBM Quantum, “Why IBM is investing $10 billion into quantum computing,” Jun. 2, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/10-billion-investment-faq [C]
[58] IQM Quantum Computers, “IQM Quantum Computers Becomes First European Quantum Computing Company Listed on a Major U.S. Exchange,” Jul. 2, 2026. [Online]. Available: https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[70] IQM Quantum Computers, “Development Roadmap,” Jan. 5, 2026. [Online]. Available: https://iqm.tech/technology/roadmap [C]
[72] IBM, “Quantum Roadmap.” [Online]. Available: https://www.ibm.com/roadmaps/quantum/ [C]
[248] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[477] J. Majer *et al.*, “Coupling superconducting qubits via a cavity bus,” *Nature*, vol. 449, no. 7161, pp. 443–447, Sep. 2007, doi: [10.1038/nature06184](https://doi.org/10.1038/nature06184). [D]
[478] B. Kannan *et al.*, “Waveguide quantum electrodynamics with superconducting artificial giant atoms,” *Nature*, vol. 583, no. 7818, pp. 775–779, Jul. 2020, doi: [10.1038/s41586-020-2529-9](https://doi.org/10.1038/s41586-020-2529-9). [D]
[479] X. Zhang, E. Kim, D. K. Mark, S. Choi, and O. Painter, “A scalable superconducting quantum simulator with long-range connectivity based on a photonic bandgap metamaterial,” [arXiv:2206.12803](https://arxiv.org/abs/2206.12803), Jun. 2022. [D]
[480] F. Marxer *et al.*, “Long-Distance Transmon Coupler with cz-Gate Fidelity above 99.8%,” *PRX Quantum*, vol. 4, no. 1, Art. no. 010314, Feb. 2023, doi: [10.1103/PRXQuantum.4.010314](https://doi.org/10.1103/PRXQuantum.4.010314). [arXiv:2208.09460](https://arxiv.org/abs/2208.09460). [D]
[481] R. Mandelbaum *et al.*, “How IBM will build the world's first large-scale, fault-tolerant quantum computer,” IBM Quantum Computing Blog, Jun. 10, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/large-scale-ftqc [R]
[482] J. Xu *et al.*, “Tunable hybrid-mode coupler enabling strong interactions between transmons at centimeter-scale distance,” *Phys. Rev. Appl.*, vol. 25, no. 1, Art. no. 014016, Jan. 2026, doi: [10.1103/ls5b-279m](https://doi.org/10.1103/ls5b-279m). [arXiv:2506.14128](https://arxiv.org/abs/2506.14128). [D]
[483] P. Zhao, P. Xu, and Z.-Y. Xue, “Long-range tunable coupler for modular fluxonium quantum processors,” [arXiv:2604.12261](https://arxiv.org/abs/2604.12261), Apr. 2026. [S]
[484] X. Deng *et al.*, “Long-Range ZZ Interaction via Resonator-Induced Phase in Superconducting Qubits,” *Phys. Rev. Lett.*, vol. 134, no. 2, Art. no. 020801, Jan. 2025, doi: [10.1103/PhysRevLett.134.020801](https://doi.org/10.1103/PhysRevLett.134.020801). [arXiv:2408.16617](https://arxiv.org/abs/2408.16617). [S]
[485] P. Zhao, Y. Zhang, G. Xue, Y. Jin, and H. Yu, “Tunable coupling of widely separated superconducting qubits: A possible application towards a modular quantum device,” *Appl. Phys. Lett.*, doi: [10.1063/5.0097521](https://doi.org/10.1063/5.0097521). [arXiv:2201.03184](https://arxiv.org/abs/2201.03184). [S]
[486] R. Mandelbaum, “Scaling for quantum advantage and beyond,” IBM Quantum Computing Blog, Nov. 12, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/qdc-2025 [C]
[487] F. Vigneau, “IQM Constellation: A New Quantum Processor Architecture for Scalable Error Correction,” IQM Quantum Computers, Sep. 30, 2025. [Online]. Available: https://iqm.tech/blog/iqm-constellation-a-new-quantum-processor-architecture-for-scalable-error-correction/ [C]
[488] F. Vigneau *et al.*, “Quantum error detection in qubit-resonator star architecture,” [arXiv:2503.12869](https://arxiv.org/abs/2503.12869), Mar. 2025. [D]
[489] K. Boothby, A. D. King, and J. Raymond, “Zephyr Topology of D-Wave Quantum Processors,” D-Wave Systems Inc., Sep. 2021. [Online]. Available: https://www.dwavequantum.com/media/2uznec4s/14-1056a-a_zephyr_topology_of_d-wave_quantum_processors.pdf [C]
[490] D-Wave Quantum Inc., “Form 10-K for the fiscal year ended December 31, 2025,” U.S. Securities and Exchange Commission (EDGAR), Feb. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1907982/000190798226000026/qbts-20251231.htm [G]
[491] D-Wave Quantum Inc., “Form 10-K for fiscal year 2024,” SEC EDGAR, Mar. 14, 2025. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1907982/000190798225000060/qbts-20241231.htm Also https://www.sec.gov/Archives/edgar/data/1907982/000190798225000060/0001907982-25-000060-index.htm. [G]
[492] U.S. Securities and Exchange Commission, “EDGAR full-text search: ‘SkyWater’ in D-Wave Quantum Inc. 10-K filings,” SEC EDGAR Full-Text Search, Feb. 26, 2026. [Online]. Available: https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982 [G]
[493] IonQ, “IonQ to Acquire SkyWater Technology, Creating the Only Vertically Integrated Full-Stack Quantum Platform Company,” Jan. 26, 2026. [Online]. Available: https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/default.aspx [C]
[494] E. Stuart, “Jumping Off the Grid in Quantum Processor Innovation: Introducing IQM Star,” IQM Quantum Computers blog, Apr. 30, 2025. [Online]. Available: https://iqm.tech/blog/jumping-off-the-grid-in-quantum-processor-innovation-introducing-iqm-star/ [C]
[495] M. Abdel-Kareem, “QuantWare Debuts VIO-40K™ Architecture to Enable 10,000-Qubit Superconducting Processors,” Quantum Computing Report, Dec. 10, 2025. [Online]. Available: https://quantumcomputingreport.com/quantware-debuts-vio-40k-architecture-to-enable-10000-qubit-superconducting-processors/ [P]
[496] T. J. Yoder *et al.*, “Tour de gross: A modular quantum computer based on bivariate bicycle codes,” [arXiv:2506.03094](https://arxiv.org/abs/2506.03094), Jun. 2025. [S]
[497] J. Dijkema *et al.*, “Cavity-mediated iSWAP oscillations between distant spins,” *Nat. Phys.*, vol. 21, no. 1, pp. 168–174, Dec. 2024, doi: [10.1038/s41567-024-02694-8](https://doi.org/10.1038/s41567-024-02694-8). [arXiv:2310.16805](https://arxiv.org/abs/2310.16805). [D]
[498] Justia Patents, “Patent search: ‘long-range coupler’ qubit (results as of Sep. 3, 2026).” [Online]. Available: https://patents.justia.com/search?q=%22long-range+coupler%22+qubit Also https://patents.google.com/patent/US12517856B2/en. Also https://patents.google.com/patent/US12587192B2/en. [G]
[536] QuantWare, “QuantWare announces scaling breakthrough with VIO-40K™, delivering 10,000 qubit Quantum Processors for the first time,” Dec. 8, 2025. [Online]. Available: https://quantware.com/news/quantware-announces-scaling-breakthrough-with-vio-40k [C]

## פריטי אימות פתוחים

- IBM Loon: מספר הקיוביטים, אורך מצמד ה-c וכל נאמנות שער לא פורסמו נכון ל-2026-09-03 [C][49], [486]; לא נמצא מאמר של IBM מ-2026 על מצמדי c.
- הנוסח המדויק בדוח ה-10-K בדבר הסתמכותה של D-Wave על SkyWater: החיפוש בטקסט המלא ב-EDGAR מחזיר תשעה אזכורים [G][492], אך לא ניתן היה לחלץ את המשפטים מהדוחות שנבדקו; הטקסט של D-Wave עצמה אומר "מפעלי ייצור קיימים של צד שלישי", עם מקור שני שהודגם ב-2000Q LN [G][491].
- דרגה 6 [D][248] לעומת "אינה עולה על שבע" [S][496]: מיושבות כאן כזיכרון בלבד לעומת זיכרון ועוד יחידת לוגיקה; שיוך הקשת השביעית הוא הקריאה של תקציר זה, לא ניסוח המאמרים.
- IQM arXiv:2503.12869: רשימת המחברים ויום ההגשה המדויק לא חולצו (מצוטט שם הארגון); ל"מעל 99.3%" של Constellation אין פרוטוקול או פס שגיאה [C][487].
- המצמד של 1 cm של Nanjing: XX 23.5 MHz נמדד; ה-ZZ של 100 MHz מוצג בלי לומר אם נמדד או הודמה [D][482]; מטופל כערך תכנון.
- הקריאה של 282 ns ששימשה לשעון הנגזר היא ערך רשומת הגרף של ארכיטקטורת מוליכי-העל, לא נתון ייחודי למצמדים לטווח ארוך.
- עלות, אנרגיה ושיעור תקינות לכל מצמד: אף שחקן אינו מפרסם אותם.
- נתוני הפטנטים של [498] לקוחים מהאינדקס של Justia, לא מרשומות הטקסט המלא של USPTO; אין ספירת משפחות ייעודית למצמדים לטווח ארוך.
- אם מוצרי Crystal ש-IQM מספקת משתמשים במצמד המוארך של 2 mm מ-[480] — החברה אינה מציינת.
