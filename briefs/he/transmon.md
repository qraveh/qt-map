---
id: transmon
name: טרנסמון
layer: 1 נושא הקיוביט
status: demonstrated
since: 2007
one_line: צומת ג'וזפסון המחובר במקביל לקבל (Koch 2007); נושא הקיוביט של Willow, Heron/Nighthawk ו-Zuchongzhi, עם השער הדטרמיניסטי ומחזור תיקון השגיאות המהירים ביותר מכל קיוביט שהודגם.
verdict: הנושא הממומן ביותר והמהיר ביותר, המוגבל בקנה מידה גדול בשגיאות של ~10⁻³ בשער הדו-קיוביטי ושל ~10⁻² בקריאה, ובפרצי שגיאות מתואמים מדי שעה. לאשר אם סריג של ≥100 קיוביטים יציג Λ ≥ 3 עם שגיאת שער דו-קיוביטי חציונית < 10⁻³ עד 2028; אחרת להוריד למעמד של רכיב.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

טרנסמון הוא צומת ג'וזפסון מסוג Al/AlOx/Al המחובר במקביל לקבל גדול, כך ש-E_J/E_C ≈ 50–100 [D][282]. דיספרסיית המטען דועכת באופן מעריכי ב-√(8E_J/E_C), וכך מסולק רעש המטען מסוג 1/f, במחיר של אנהרמוניות חלשה α ≈ −E_C ≈ −200 עד −300 MHz; הקיוביט הוא שתי הרמות הנמוכות ביותר של מתנד בתדר 4–6 GHz [D][282]. Koch ועמיתיו הציעו אותו ב-2007 [D][282]; הטרנסמון התלת-ממדי (2011) [D][283] וה-Xmon של UCSB/Google (2014) [D][284] קיבעו את שתי השושלות שעדיין בשימוש: תדר קבוע (IBM) ותדר הניתן לכוונון בשטף (Google, IQM, USTC).

תכונות (גרף הטכנולוגיות):
- a: זיקה 1.0, מיוצר (אין מקבילה טבעית).
- b: זמן אופייני 10⁻⁸ s, שזירה דטרמיניסטית; חסם הדליפה 1/α מציב את רצפת משך הפולס סביב 10 ns.
- c: קריאה דיספרסיבית במיקרוגל, 10⁻⁶·⁵ s (≈ 320 ns), לא-הורסת, ניתנת לביצוע באמצע המעגל.
- d: ניידות סטטית, חיווט בין שכנים קרובים.
- e: בקרה במיקרוגל מאלקטרוניקה בטמפרטורת החדר; גרסאות בשלב הקר (CMOS קריוגני או SFQ) ב-≤ 5 קיוביטים.
- f: מבנה השגיאה: דליפה + פאולי סטוכסטית + פרצים מתואמים + קוהרנטית/כיול.
- g: ייצור: ליתוגרפיה של מוליכי-על.

## פיזיקה וגבולות

האוכלוסייה התרמית השיורית (0.1% ב-35 mK בטרנסמון תלת-ממדי [D][285], ≈ 1% ב-40–60 mK לקיוביט של 5 GHz [S][285]) הופכת את האיפוס ואת הקריאה לרצפת ה-SPAM. האנהרמוניות חוסמת שערים חד-קיוביטיים ב-10–25 ns ושער CZ עם מצמד בר-כוונון ב-25–50 ns [D][1], [37][P][286]; שער התהודה הצולבת אורך ≈ 200–500 ns [D][287].

הרצפה היא דה-קוהרנטיות לאורך זמן השער: עם T1 ממוצע = 68 µs ב-Willow [D][1], שער CZ של 40 ns נושא ≈ 6×10⁻⁴ שגיאה לא-קוהרנטית [S][1]; עם T1 השיא = 1.68 ms בטרנסמון ניסוי יחיד של Ta על Si [D][288], היא יורדת מתחת ל-5×10⁻⁵ [S][288]. ההפסד נשלט בידי מערכות דו-רמתיות (TLS) בתחמוצות אמורפיות בממשקים [D][288], ומתחתיהן קוואזי-חלקיקים, דעיכת פרסל ורעש שטף.

רוב הערוץ לאחר סחרור הוא פאולי סטוכסטי, ולכן Λ = 2.14 של Willow [D][1] תואם את התאוריה. דליפה ל-|2⟩ מצטברת תחת תיקון שגיאות אם אינה מוסרת בכל מחזור (האיפוס המיקרוגלי המלא של USTC הפחית אותה 72×, ל-6.4×10⁻⁴, על 107 קיוביטים [D][3]). שגיאות קוהרנטיות (ZZ שיורי, סחיפת TLS) חייבו כיול מחדש באמצעות למידת חיזוק בתוך ריצת תיקון השגיאות של Google מ-2026-07 [D][2]. פרצים מתואמים (חלקיקים מייננים המציפים את השבב בקוואזי-חלקיקים) פוגעים בכל הקיוביטים בבת אחת — בערך אחד לכל 10 s ב-Sycamore ב-2021 [D][289], בערך אחד לשעה ב-Willow לאחר הנדסת פער [D][1], [290] — ולכן ריצות זיכרון ארוכות נקטעות בגלל הפרצים, לא בגלל המרחק. הזזת הרצפה פירושה חומרים חדשים (Ta, Nb מכומס), אנהרמוניות בסדר הגודל של פלוקסוניום, ניהול קרינה או המרה למחיקה (מסילה כפולה).

## מצב ההנדסה העדכני

ההתקנים המבודדים הטובים ביותר: T1 1.68 ms, Q 2.5×10⁷, שער חד-קיוביטי 99.994% [D][288]; CZ 99.93% וקריאה של 280 ns ב-99.94% על שבב דו-קיוביטי של IQM [D][38]; מצמד הטרנסמון הכפול של Toshiba: CZ 99.90% ב-48 ns [D][37].

ערכים טיפוסיים ב-≥ 100 קיוביטים: Willow, 105 קיוביטים — T1 ממוצע 68 µs, שגיאת CZ 0.33%, קריאה 99.5%, מחזור תיקון שגיאות 1.1 µs [D][1][C][32]; צי המכונות של IBM: שגיאה לכל שער בשכבה 3.7×10⁻³ טיפוסית, 1.9×10⁻³ במיטבה (2026-07) [C][34]; Zuchongzhi 3.0, 105 קיוביטים — דו-קיוביטי 99.62%, קריאה 99.13% [D][35]; Rigetti Cepheus-1-108Q, שנים-עשר שבבונים בני 9 קיוביטים [C][36] — דו-קיוביטי חציוני 99.1% [C][G:RIGETTI-FIN-2026].

| שנה | נתון | מי | ראיות |
|---|---|---|---|
| 2019 | Sycamore, 53 קיוביטים, שגיאת שער דו-קיוביטי בפעולה בו-זמנית 0.62% | Google | [D][291] |
| 2023 | Condor, 1,121 קיוביטים על שבב אחד | IBM | [C][292] |
| 2024 | Willow, 105 קיוביטים, Λ = 2.14 | Google | [D][1] |
| 2025 | טרנסמון דו-ממדי, T1 1.68 ms | Princeton | [D][288] |
| 2026 | שגיאה לוגית ב-d=7: 7.72×10⁻⁴ למחזור | Google | [D][2] |

בקנה מידה גדול, השער הדו-קיוביטי הוא איבר השגיאה הגדול ביותר (~40% מתקציב קוד הצבע של Google) [D][41], ואחריו הקריאה (~10⁻² בציי מכונות [C][34]) והדליפה; זנב ההתפלגות בסריג חשוב יותר מהחציון.

## ייצור, חומרים ושרשרת האספקה

תהליך: Nb או Ta על Si בעל התנגדות סגולית גבוהה או על ספיר; צמתי Al/AlOx/Al באידוי צל; אינטגרציה תלת-ממדית בשיטת השבב ההפוך. על ציוד CMOS של 300 mm דיווחו imec/KU Leuven על 393 טרנסמונים תקינים מתוך 400 (98.25%), עם T1 חציוני ≈ 75 µs (42–113 µs) [D][293][G:IMEC-300MM-2025]: אחידות, לא קוהרנטיות. סריגים בתדר קבוע חייבים גם לפגוע ביעדי התדר (פיזור הצמתים הופך להתנגשויות תדר), באמצעות ריפוי בלייזר (IBM), ריפוי בממתח מתחלף (Rigetti, הצלחה של 97.4%) [D][294] או מצמדים ברי-כוונון.

עלות ואנרגיה: אף ספק אינו מפרסם $/קיוביט; נתוני הקירוב הם חוזה LUMI של IQM בסך €33 M [P][295] ובקר קריוגני של IBM בטכנולוגיית 14 nm הצורך 23 mW לקיוביט ב-4 K [D][296] — עשרות ואטים ב-10³ קיוביטים; בקרת SFQ טוענת ל-nW לקיוביט [C][54].

שרשרת אספקה: מקררי דילול מ-Bluefors (פינלנד), Oxford Instruments (בריטניה), FormFactor ו-Maybell (ארה״ב); ³He מדעיכת טריטיום במלאי ממשלתי (ארה״ב: NNSA [G][297]), ללא יצרן מסחרי; מגברי HEMT ל-4 K — למעשה ספק אחד (Low Noise Factory, שוודיה); אלקטרוניקת הבקרה תחרותית (Quantum Machines, Qblox, Zurich Instruments); יחידות QPU מסחריות מ-QuantWare (הולנד) [P][298]; מפעלי ייצור: Anderon (חברה שהופרדה מ-IBM Albany, 2026-05; מכתב כוונות של CHIPS על $1 B, ו-$1 B במזומן מ-IBM שצוינו בנפרד) [P][299][G][300] ו-GlobalFoundries (מכתב כוונות על $375 M) [G][300].

פיקוח על יצוא: התקנה הסופית-הזמנית של BIS מ-2024-09-06 חלה על מקררי דילול ≥ 600 µW ב-0.1 K למשך 48 h (3A904), על מערכות קריוגניות לבדיקת פרוסות (3B904), על מגברים פרמטריים (3A901.b), ועל מחשבים קוונטיים (4A906) רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT נופלים באותה רצועה — 34–99 קיוביטים ב-≤ 10⁻⁴, 100–199 ב-≤ 10⁻³, התקרה עולה עד 6 × 10⁻³ מתחת ל-2,000 קיוביטים, וכל שגיאה שהיא מ-2,000 ואילך [G][301][G:BIS-QUANTUM-2024]; לכן ספקים סיניים בונים מקררי 10 mK בייצור מקומי (2026-05-15) [P][302].

## בקרה, קריאה ועומס הקלט-פלט

סריג בר-כוונון דורש קו XY אחד וקו Z אחד לכל קיוביט, ועוד קו לכל מצמד (Sycamore: ≈ 3.6 קווי בקרה לקיוביט, לפני הקריאה [D][291]); הקריאה מרבבת ≈ 6–10 קיוביטים לכל קו הזנה [D][1]; כל קו הוא ערוץ DAC ועוד כבל קואקסיאלי מונחת, ולכן העלות והחום גדלים עם N.

השהיה: מחזור תיקון השגיאות הוא 1.1 µs; המפענח בזמן אמת של Google פעל בהשהיה ממוצעת של 63 µs עבור d=5 [D][1]; Relay-BP של IBM מכוון בסימולציה ל-< 1 µs למחזור [S][48] עבור קוד ה-gross (קוד ה-qLDPC של IBM מסוג bivariate bicycle, [[144,12,12]]: 12 קיוביטים לוגיים ב-288 פיזיים [D][248]).

חומות: 10³ הושג (Condor, 1,121 קיוביטים [C][292]); KIDE של Bluefors (> 4,000 קווי RF, > 1,000 קיוביטים; דף מוצר, 2026-06) [C][303] היא התקרה של קריוסטט אחד. 10⁴ דורש CMOS קריוגני ב-4 K (HRL: קוד חזרה d=5 מבקר של ≤ 3.5 W [D][190][G:HRL-2026]) או SFQ בטמפרטורת מיליקלווין (SEEQC: שער חד-קיוביטי עד 99.9% על ≤ 5 קיוביטים [D][304][G:SEEQC-2026]), ועוד מודולים מרובי קריוסטטים (IBM צימדה שני תאים, 2026-08 [C][50]). ל-10⁶ אין תכנון סגור: DAC שטף על השבב, פענוח קריוגני וקישורים בין מקררים (ETH: 30 m בנאמנות בל של 80.4% [D][305]) עדיין מתחת לקנה המידה הנדרש.

## תפקיד במחסנית

ארכיטקטורות: סריג הטרנסמונים עם מצמדים ברי-כוונון, וארכיטקטורת המחיקה במסילה כפולה (הטרנסמון כקיוביט עזר או כאחת המסילות). דורש ליתוגרפיה של מוליכי-על; מספק את נושא הקיוביט לשערים עם מצמד בר-כוונון ולשערי תהודה צולבת, את קיוביט העזר לשערי מהוד בוזוני, את תת-המרחב של הקיוביט החשוף, את ההסטה הדיספרסיבית לקריאה במיקרוגל ואת הצד המיקרוגלי של המתמר האופטי. מוחלף בידי הפלוקסוניום, הקונה אנהרמוניות ו-T1 במחיר של ממתח שטף לכל קיוביט, בקרה בתדר מתחת ל-GHz וקריאה בתכנון מחודש. מתנגש עם בקרת SFQ: פוטוני המיתוג הרעילו את הקיוביטים בקוואזי-חלקיקים במודול מרובה השבבים של 2023 (0.96 מתוך 1.2% שגיאה לכל קליפורד) [D][249]; SEEQC טוענת שפתרה זאת בתכנון הנדסי [C][54], ולכן ההתנגשות עומדת בעינה עד לבדיקה עצמאית בקנה מידה של סריג. השעון הנגזר של ארכיטקטורת סריג הטרנסמונים ≈ 6.5×10⁻⁷ s (651 ns; שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס בארכיטקטורה), מתוכו 282 ns קריאה, וקריאה ועוד איפוס — שני שלישים, לעומת מחזור של 1.1 µs שנמדד ב-Willow [D][1] — הארכיטקטורה המהירה ביותר שהודגמה, ועבורה משלם היעד G4 (סבילות לתקלות בקנה מידה גדול). משבצות ריקות סמוכות: המתמר מיקרוגל–אופטי (≈ 3 סדרי גודל מתחת לנדרש לשערים מרוחקים [S][306]) ופענוח קריוגני.

## ראיות — כיצד נמדדו המספרים

המספרים הבולטים מגיעים מ-RB/IRB של קליפורד, מ-XEB בו-זמני (Google), מנאמנות השכבה/EPLG של IBM וממטריצות השיוך של הקריאה; Λ הוא התאמה של השגיאה הלוגית מול המרחק תחת מפענח אחד. מה שחומק כאן: פעולה מבודדת מול פעולה בו-זמנית (שבבי השיא מבודדים); שגיאות קוהרנטיות הממוצעות לתוך מספר דה-פולריזציה יחיד; דליפה, שאינה נראית ל-RB ולעתים קרובות מסוננת בבחירה בדיעבד; סחיפה בין הכיול לשימוש; ומוסכמות דיווח (Rigetti מצטטת חציונים, IBM את ההתקן הטוב ביותר שלה, IQM שבב דו-קיוביטי). "70 הקיוביטים הלוגיים" של IBM מ-2026-07 הם תוצאה של גילוי שגיאות עם בחירה בדיעבד [D][46], לא סבילות לתקלות.

שחזור: הגדלה מתחת לסף שוחזרה בידי USTC על 107 קיוביטים עם Λ = 1.40 [D][3]. מחלוקות: דגימת העליונות של 2019 שוחזרה ברשתות טנזוריות [D][307]; ניסוי ה"תועלת" של IBM מ-2023 סומלץ באופן קלאסי בתוך שבועות [D][308], [309]; המאמר של Google מ-2026-07 אינו מדווח Λ עבור ריצת d=7 [D][2]. סתירת ערכים: T1 של imec ב-300 mm מצוטט לעתים קרובות כ-"> 100 µs"; החציון במאמר הוא ≈ 75 µs [D][293][G:IMEC-300MM-2025], והוא המשמש כאן.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | פעילות | ראיות |
|---|---|---|---|---|
| Google Quantum AI | מפתח | ארה״ב | Willow, 105 קיוביטים, Λ = 2.14; זיכרון d=7 | [D][1], [2] |
| IBM | מפתח | ארה״ב | צי Heron/Nighthawk; מפת הדרכים Starling; הפרדת Anderon | [C][34], [67][P][299] |
| Rigetti | מפתח | ארה״ב | שבבוני Cepheus-1-108Q; מפעל ייצור עצמי | [C][61] |
| IQM | מפתח | פינלנד | 26 מערכות נמכרו, 17 הותקנו | [C][58][G:IQM-LISTING-2026-07] |
| USTC | מחקר | סין | Zuchongzhi 3.x, 105 קיוביטים; Λ = 1.40 | [D][3], [35] |

**כספים.**
- 2025-11-06 · DARPA · שלב B של QBI (עד $15 M לכל אחד) · IBM היא ספקית סריג הטרנסמונים היחידה מבין אחד-עשר; Google ו-Rigetti נשארו בשלב A [G][65][G:QBI-STAGEB-2025-11][G:QBI-STAGEA-2025-04]
- 2026-01-20 · D-Wave · מיזוג ורכישה, Quantum Circuits (מהודים במסילה כפולה על קיוביטי עזר טרנסמוניים) · $550 M (מניות + מזומן) · נסגרה [C][14][G:DWAVE-QCI-2026-01][G:DUALRAIL-CZ-2026-08]
- 2026-05-05 · QuantWare (יחידות QPU מסחריות; מפת הדרכים VIO-40K [R][G:QUANTWARE-VIO]) · סבב B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners (משקיעים חדשים, ללא משקיע מוביל) · > $210 M במצטבר · נסגר [P][298]
- 2026-05-18 · Nord Quantique · מימון הון צמיחה · $30 M לפי שווי של $1.4 B · נסגר [C][89][G:NQ-1.4B-2026-05]
- 2026-05-21 · US Dept of Commerce · מכתבי כוונות של CHIPS ($2.013 B, תשע חברות) · IBM/Anderon $1 B, GlobalFoundries $375 M, Rigetti ≤ $100 M, D-Wave $100 M · מכתב כוונות לא מחייב [G][300][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · התחייבות · > $10 B על פני חמש שנים, ו-$1 B במזומן ל-Anderon צוינו בנפרד · הוכרז [C][310][G:IBM-10B-2026-06]
- 2026-06-03 · OQC (מפתחת הקואקסמון [D][311]) · סבב C · £260 M (~$350 M) · בהובלת Bullhound · השווי לא פורסם · נסגר [C][60][G:OQC-SERIESC-2026-06]
- 2026-07-02 · IQM · רישום למסחר, Nasdaq ובורסת הלסינקי · מזומנים פרו-פורמה €337 M · נסגר [C][G:IQM-LISTING-2026-07]
- 2026-08-04 · IQM · תוצאות המחצית הראשונה של 2026 · הכנסות €8.9 M (+47%), מזומנים €309 M · דווח [P][295]
- 2026-08-06 · Rigetti · תוצאות הרבעון השני של 2026 · הכנסות $5.1 M, הפסד GAAP של $52.6 M, מזומנים $541.3 M · דווח [C][61]

**שוק ושרשרת אספקה.** ציוד התשתית ריכוזי יותר משוק ה-QPU. כלכלת היחידה אינה מפורסמת; חוזה IQM בסך €33 M [P][295] ומחיר Quantum Circuits בסך $550 M [C][G:DWAVE-QCI-2026-01] הם נקודות הייחוס היחידות שניתן לצטט. יעדים משלמים: G7 (מערכות הניתנות לפריסה) ו-G2 (תועלת עם הפחתת שגיאות) כבר היום; G3 (סבילות מוקדמת לתקלות) דרך תוכניות בסגנון QBI החל מ-2027 [G:QBI-STAGEC-2026]; G4 (סבילות לתקלות בקנה מידה גדול) אחרי 2029 [R][G:IBM-ROADMAP]; G1 (סימולציה אנלוגית), G5 (אופטימיזציה) ו-G6 (רישות) אינם מביאים הכנסות ייחודיות לטרנסמון.

**קניין רוחני ותקנים.** הסקירה של PatSnap שפורסמה ב-2026-06-30: IBM — 4,388 משפחות פטנטים קוונטיים, Google — 2,385, Microsoft — 1,175; בהתקנים מוליכי-על (H10N 60): IBM — 783, Google — 357 [P][312][G:PATSNAP-2026-06]. לא נמצאה התדיינות משפטית; לא אומתה משפחה ייחודית לטרנסמון. מחסניות תוכנה פתוחות הופכות את השכבה שמעל לסחורה: Qiskit (IBM טוענת ל-≈ 70% מהמפתחים [C][310]), Cirq/Stim, OpenQASM 3, NVQLink [C][G:NVQLINK-2025].

**מפות דרכים ועמידה בהבטחות.**
- IBM Kookaburra (2022-05-10 · 2025, כמעבד מרובה שבבים של 1,386 קיוביטים [C][313]; הובטח מחדש 2025-06-10 · 2026, כמודול ה-qLDPC הראשון [R][67] · לא סופק נכון ל-2026-09-03 [R][72][G:IBM-ROADMAP]).
- IBM Nighthawk (2025-06-10 · 2025 · סופק 2025-12) ו-Starling (2025-06-10 · 2029, 200 קיוביטים לוגיים / 10⁸ שערים · פתוח) [R][G:IBM-ROADMAP].
- Google, אבן דרך 3, שגיאה לוגית 10⁻⁶ (ללא תאריך · לא פורסם יורש ל-Willow; מסלול האטומים הניטרליים נפתח 2026-03-24) [R][2][G:GOOGLE-ATOMS-2026-03].
- Rigetti: 108 קיוביטים ב-99.5% (הובטח לסוף 2025 · זמינות כללית 2026-04-07 בחציון 99.1%; 99.5% נדחה ל"המשך 2026") [C][G:RIGETTI-FIN-2026].
- Fujitsu/RIKEN: 1,000 קיוביטים (הובטח 2025-04-22 · שנת הכספים 2026 · לא הושק נכון ל-2026-09-03) [R][75][G:FUJITSU-1000Q].
אמינות: IBM — גבוהה בקצב, חלשה במודול ה-qLDPC הראשון שלה ובטענות "יתרון"; Google — גבוהה בפיזיקה, אטומה בלוחות הזמנים; Rigetti — דחיות כרוניות; Fujitsu — לא הוכחה.

**פרשנות אסטרטגית.** אם הטרנסמונים ינצחו, בעלי מפעלי הייצור וספקי הקריוגניקה ינצחו בלי קשר לספק; חברות הזנק של טרנסמונים ללא מפעל ייצור יפסידו — ההתכנסות (Atlantic Quantum → Google, 2025-10-03 [P][55][G:GOOGLE-ATLANTIC-2025-10]; Quantum Circuits → D-Wave) כבר נראית. איומי תחליף: פלוקסוניום באותו מפעל ייצור, קידודי מסילה כפולה/בוזוניים המורידים את הטרנסמון למעמד של קיוביט עזר, ואטומים וספינים לטובת צפיפות. ספקי ³He, HEMT ומקררים מחזיקים בכוח מיקוח; ספקי הפלטפורמות נחלצים באמצעות אינטגרציה אנכית.

## תחזית ושאלות פתוחות

אבני דרך, 12–24 חודשים: (1) Kookaburra מריץ זיכרון על קוד ה-gross מתחת לנקודת האיזון — לאשר; היעדר תוצאה עד סוף 2027 מוריד בדרגה את תאריך 2029 של IBM [R][G:IBM-ROADMAP]. (2) Google מפרסמת Λ ≥ 3 או זיכרון לוגי של 10⁻⁶ ב-d ≥ 9 — לאשר; שנה שנייה בלי יורש ל-Willow מורידה בדרגה [D][2]. (3) שלב C של QBI (צפוי בסביבות הרבעון הרביעי של 2026 [G:QBI-STAGEC-2026][P][314]) מקדם ספק טרנסמונים. (4) CMOS קריוגני או SFQ מפעילים ≥ 50 טרנסמונים ללא פגיעה בנאמנות [D][190], [304]. התרחיש הטוב ביותר ל-2029: מכונה ברמת Starling עם 200 קיוביטים לוגיים [R][G:IBM-ROADMAP] וזיכרון של Google ב-d ≥ 11; התרחיש הגרוע ביותר: Λ סביב 2, קריאה ברמת 10⁻², הפרצים מגבילים את המרחק, הטרנסמון שורד רק כקיוביט עזר וההון עובר לאטומים ולספינים. שאלות פתוחות: האם קוהרנטיות של מילישניות ב-Ta/Si שורדת תהליך של 100 קיוביטים עם מצמדים; האם רצפת שגיאת השער הדו-קיוביטי בקנה מידה גדול קוהרנטית (כיול) או לא-קוהרנטית; האם הקריאה יכולה להגיע ל-10⁻³ ב-< 300 ns לרוחב סריג שלם. לעקוב: המאמר הבא של Google, Kookaburra, רשימת שלב C.

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[32] Y. Chen and M. Devoret, “Our quantum hardware: the engine for verifiable quantum advantage,” Google Blog, Oct. 22, 2025. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ [C]
[34] IBM Quantum, “What's new at IBM Quantum - Q2 2026.” [Online]. Available: https://www.ibm.com/quantum/blog/whats-new-q2-2026 [C]
[35] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[36] Rigetti Computing, Inc., “Rigetti Announces General Availability of 108-Qubit System,” Apr. 7, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system [C]
[37] R. Li, K. Kubo, Y. Ho, Z. Yan, Y. Nakamura, and H. Goto, “Realization of High-Fidelity CZ Gate Based on a Double-Transmon Coupler,” *Phys. Rev. X*, vol. 14, no. 4, Art. no. 041050, Nov. 2024, doi: [10.1103/PhysRevX.14.041050](https://doi.org/10.1103/PhysRevX.14.041050). [arXiv:2402.18926](https://arxiv.org/abs/2402.18926). [D]
[38] F. Marxer *et al.*, “Above 99.9% Fidelity Single-Qubit Gates, Two-Qubit Gates, and Readout in a Single Superconducting Quantum Device,” *PRX Quantum*, vol. 7, Art. no. 020333, 2026, doi: [10.1103/n86s-2b88](https://doi.org/10.1103/n86s-2b88). [arXiv:2508.16437](https://arxiv.org/abs/2508.16437). [D]
[41] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[46] S. Martiel *et al.*, “Sampling hard circuits with verifiably high fidelity,” [arXiv:2607.25941](https://arxiv.org/abs/2607.25941), Jul. 2026. [D]
[48] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[50] C. Dundon, S. Hall, M. Hollister, and A. Lindler, “IBM's new modular architecture for cryogenic systems,” IBM Quantum Computing Blog, Aug. 19, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/modular-cryogenics [C]
[54] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [C]
[55] M. Swayne, “Atlantic Quantum Joins Google Quantum AI,” The Quantum Insider, Oct. 3, 2025. [Online]. Available: https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/ [P]
[58] IQM Quantum Computers, “IQM Quantum Computers Becomes First European Quantum Computing Company Listed on a Major U.S. Exchange,” Jul. 2, 2026. [Online]. Available: https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ [C]
[60] A. Curbison, “OQC raises £260m in Europe's largest ever private quantum computing funding round,” OQC, Jun. 2, 2026. [Online]. Available: https://oqc.tech/company/newsroom/series-c [C]
[61] Rigetti Computing, “Rigetti Computing Reports Second Quarter 2026 Financial Results,” Rigetti Investor Relations, Aug. 6, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2026-financial-results [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[67] IBM, “IBM Sets the Course to Build World's First Large-Scale, Fault-Tolerant Quantum Computer at New IBM Quantum Data Center,” Jun. 10, 2025. [Online]. Available: https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center [C]
[72] IBM, “Quantum Roadmap.” [Online]. Available: https://www.ibm.com/roadmaps/quantum/ [R]
[75] Fujitsu, “Fujitsu Quantum.” [Online]. Available: https://global.fujitsu/en-global/technology/research/quantum [R]
[89] Nord Quantique, “Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment,” Business Wire, May 18, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment [C]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[248] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[282] J. Koch *et al.*, “Charge-insensitive qubit design derived from the Cooper pair box,” *Phys. Rev. A*, vol. 76, no. 4, Art. no. 042319, Oct. 2007, doi: [10.1103/PhysRevA.76.042319](https://doi.org/10.1103/PhysRevA.76.042319). [arXiv:cond-mat/0703002](https://arxiv.org/abs/cond-mat/0703002). [D]
[283] H. Paik *et al.*, “Observation of High Coherence in Josephson Junction Qubits Measured in a Three-Dimensional Circuit QED Architecture,” *Phys. Rev. Lett.*, vol. 107, no. 24, Art. no. 240501, Dec. 2011, doi: [10.1103/PhysRevLett.107.240501](https://doi.org/10.1103/PhysRevLett.107.240501). [arXiv:1105.4652](https://arxiv.org/abs/1105.4652). [D]
[284] R. Barends *et al.*, “Superconducting quantum circuits at the surface code threshold for fault tolerance,” *Nature*, vol. 508, no. 7497, pp. 500–503, Apr. 2014, doi: [10.1038/nature13171](https://doi.org/10.1038/nature13171). [arXiv:1402.4848](https://arxiv.org/abs/1402.4848). [D]
[285] X. Y. Jin *et al.*, “Thermal and Residual Excited-State Population in a 3D Transmon Qubit,” *Phys. Rev. Lett.*, vol. 114, no. 24, Art. no. 240501, Jun. 2015, doi: [10.1103/PhysRevLett.114.240501](https://doi.org/10.1103/PhysRevLett.114.240501). [arXiv:1412.2772](https://arxiv.org/abs/1412.2772). [D]
[286] C. Choucair, “Oxford Researchers Demonstrate Fast, 99.8% Fidelity Two-Qubit Gate Using Simplified Circuit Design,” The Quantum Insider, Mar. 26, 2025. [Online]. Available: https://thequantuminsider.com/2025/03/26/oxford-researchers-demonstrate-fast-99-8-fidelity-two-qubit-gate-using-simplified-circuit-design/ [P]
[287] A. Kandala *et al.*, “Demonstration of a High-Fidelity CNOT Gate for Fixed-Frequency Transmons with Engineered ZZ Suppression,” *Phys. Rev. Lett.*, vol. 127, no. 13, Art. no. 130501, Sep. 2021, doi: [10.1103/PhysRevLett.127.130501](https://doi.org/10.1103/PhysRevLett.127.130501). [D]
[288] M. P. Bland *et al.*, “2D transmons with lifetimes and coherence times exceeding 1 millisecond,” [arXiv:2503.14798](https://arxiv.org/abs/2503.14798), Mar. 2025. [D]
[289] M. McEwen *et al.*, “Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits,” *Nat. Phys.*, vol. 18, no. 1, pp. 107–111, Dec. 2021, doi: [10.1038/s41567-021-01432-8](https://doi.org/10.1038/s41567-021-01432-8). [arXiv:2104.05219](https://arxiv.org/abs/2104.05219). [D]
[290] M. McEwen *et al.*, “Resisting High-Energy Impact Events through Gap Engineering in Superconducting Qubit Arrays,” *Phys. Rev. Lett.*, vol. 133, no. 24, Art. no. 240601, Dec. 2024, doi: [10.1103/PhysRevLett.133.240601](https://doi.org/10.1103/PhysRevLett.133.240601). [arXiv:2402.15644](https://arxiv.org/abs/2402.15644). [D]
[291] F. Arute *et al.*, “Quantum supremacy using a programmable superconducting processor,” *Nature*, vol. 574, no. 7779, pp. 505–510, Oct. 2019, doi: [10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5). [D]
[292] J. Gambetta, “The hardware and software for the era of quantum utility is here,” IBM Quantum Computing Blog, Dec. 4, 2023. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-roadmap-2033 [C]
[293] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[294] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[295] Investing.com, “IQM Q2 2026 slides: backlog surges 52%, revenue up 47% in H1,” Aug. 4, 2026. [Online]. Available: https://www.investing.com/news/company-news/iqm-q2-2026-slides-backlog-surges-52-revenue-up-47-in-h1-93CH-4834587 [P]
[296] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[297] U.S. Government Accountability Office, “Managing Critical Isotopes: Weaknesses in DOE's Management of Helium-3 Delayed the Federal Response to a Critical Supply Shortage,” U.S. Government Accountability Office, May 2011. [Online]. Available: https://www.gao.gov/products/gao-11-472 [G]
[298] M. Ivezic, “QuantWare Raises $178M Series B — What It Means for Quantum Open Architecture,” PostQuantum.com, May 6, 2026. [Online]. Available: https://postquantum.com/industry-news/quantware-178m-series-b-qoa/ [P]
[299] L. James, “IBM spins off America's first quantum chip foundry with $2 billion in federal and private funding — newly-minted 'Anderon' foundry to offer 300mm quantum wafer fab and manufacturing services,” Tom's Hardware, May 26, 2026. [Online]. Available: https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding [P]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[302] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[303] Bluefors, “KIDE Cryogenic Platform — For Large-Scale Quantum Computing,” Jun. 16, 2026. [Online]. Available: https://bluefors.com/products/kide-cryogenic-platform/ [C]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[305] S. Storz *et al.*, “Loophole-free Bell inequality violation with superconducting circuits,” *Nature*, vol. 617, no. 7960, pp. 265–270, May 2023, doi: [10.1038/s41586-023-05885-0](https://doi.org/10.1038/s41586-023-05885-0). [D]
[306] N. Dirnegger *et al.*, “Distilled remote entanglement between superconducting qubits across optical channels,” [arXiv:2503.10842](https://arxiv.org/abs/2503.10842), Mar. 2025. [S]
[307] F. Pan, K. Chen, and P. Zhang, “Solving the Sampling Problem of the Sycamore Quantum Circuits,” *Phys. Rev. Lett.*, vol. 129, no. 9, Art. no. 090502, Aug. 2022, doi: [10.1103/PhysRevLett.129.090502](https://doi.org/10.1103/PhysRevLett.129.090502). [arXiv:2111.03011](https://arxiv.org/abs/2111.03011). [D]
[308] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[309] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[310] IBM, “IBM Commits More Than $10 Billion to Quantum Computing, Funding Its Roadmap from Today's Leading Systems to the World's First Fault-Tolerant Quantum Computers,” Jun. 2, 2026. [Online]. Available: https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers [C]
[311] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [D]
[312] PatSnap, “Quantum Computing Patent Landscape 2026,” Jun. 30, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape/ [P]
[313] J. Gambetta, “Expanding the IBM Quantum roadmap to anticipate the future of quantum-centric supercomputing,” IBM Quantum Blog, May 10, 2022. [Online]. Available: https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025 [C]
[314] Quantum Ledger, “DARPA QBI Tracker.” [Online]. Available: https://quantumledger.report/darpa-qbi [P]

## פריטי אימות פתוחים

- שווי השוק של IQM ≈ $2.6 B (2026-08): לא נמצא מקור ראשוני; הנתון אינו מובא.
- יעד 1,000 הקיוביטים / 99.9% של Rigetti ותאריכו: לא נמצא מקור לאף אחד מהם, ושניהם הושמטו.
- KIDE של Bluefors, "> 4,000 קווי RF / > 1,000 קיוביטים": דף המוצר עודכן ב-2026-06-16; לא נקבע תאריך השקה.
- IBM, "> $1.1 B בחוזי לקוחות מאז 2017" [C][310]: לא אומת באופן עצמאי; הנתון אינו מובא.
- זמן שער התהודה הצולבת ≈ 200–500 ns: טווח טיפוסי לצי המכונות, שהוסק ממאמר על התקן יחיד [287]; אין מקור ברמת הצי.
- שיעור התקינות של imec ב-300 mm — 393 מתוך 400 (98.25%): מצוטטת מול [293]; T1 החציוני באותה ריצה ≈ 75 µs.
- מקור [306] (arXiv:2503.10842): לא מובאת עבורו רשימת מחברים; פער ההתמרה של "≈ 3 סדרי גודל" מצוטט מהספרות.
- "מגברי HEMT ל-4 K — למעשה ספק אחד (Low Noise Factory)": תצפית שוק; אין מקור ממאגר נתונים.
