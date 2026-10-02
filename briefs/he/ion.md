---
id: ion
name: יון אטומי לכוד
layer: "1 נושא הקיוביט"
status: demonstrated
since: 1995
one_line: "יונים בודדים של Yb⁺/Ba⁺/Ca⁺ במלכודות RF, הנשזרים דרך אופני תנועה משותפים; הקיוביט בעל הנאמנות הגבוהה ביותר והאיטי ביותר בשירות מסחרי."
verdict: "מובילת הנאמנות והפלטפורמה היחידה המריצה עשרות קיוביטים לוגיים מתוקנים, אך התפוקה נקבעת בידי ההובלה והקירור, לא בידי השערים; ההגדלה הדו-ממדית לא תוכח עד Sol (2027)."
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

קיוביט של יון לכוד הוא יון אטומי בודד — איטרביום, בריום, סידן או סטרונציום — הכלוא בשדות RF ובשדות סטטיים מעל אלקטרודות במיקרו-ייצור, והלוגיקה שלו מקודדת ברמות על-דקות, ברמות זימן או ברמות אופטיות. יונים בשרשרת דוחים זה את זה, ולכן הם חולקים אופני תנועה מקוונטטים; כוח התלוי בספין הפועל על אופנים אלה הופך את התנועה לאפיק השוזר כל זוג. Cirac ו-Zoller הציעו זאת ב-1995; הקבוצה של Wineland ב-NIST הדגימה שער דו-קיוביטי באותה שנה. כל מה שמסחרי כיום הוא הרעיון הזה ועוד מיקרו-ייצור של אלקטרודות משטח.

תכונות (גרף הטכנולוגיות): זיקת הנושא 0.0 — טבעי לחלוטין, כל היונים זהים מכוח חוקי הפיזיקה, אין שונות ייצור שיש לכייל; זמן שזירה 10⁻⁴·² s (≈ 63 µs), דטרמיניסטית, ללא בישור; קריאה בפלואורנות על מעבר מחזורי, ≈ 10 µs, לא-הורסת, ניתנת לביצוע באמצע המעגל; ניידות בהובלה פיזית — היונים מוסעים, לא מחווטים; בקרה אופטית, בטמפרטורת החדר; מבנה השגיאה כפי שהקוד רואה אותו: קוהרנטית, דליפה, פאולי; ייצור: מלכודות אלקטרודות משטח ברמת MEMS.

## פיזיקה וגבולות

תדרי מלכודת של כמה MHz קובעים את השעון. צימוד ספין–תנועה גדל עם פרמטר למב–דיקה כפול עוצמת ההנעה, ולכן שער מהיר בהרבה ממחזור תנועה אחד מעורר את האופנים הלא נכונים או דורש הספק אופטי שמחזיר את הפיזור; שערים של µs עד מאות µs הם פשרה פיזיקלית, לא כשל הנדסי. הזיכרון הוא ההפך: במצבי שעון שאינם רגישים לשדה מגנטי, יון אחד שומר על קוהרנטיות יותר משעה [D][104], חמישה עד שישה סדרי גודל יותר מקיוביט מוליך-על. שגיאת הסרק כמעט חינמית; זמן הסרק הוא מה שעולה.

הרצפה שייכת להנעה, לא לנושא: שערי לייזר נושאים רצפה בלתי ניתנת להפחתה של פליטה ספונטנית, ושגיאת שער דו-קיוביטי של 8.4(7)×10⁻⁵ בטמפרטורת דופלר ללא קירור למצב היסוד [D][102] מראה שאפשר להסיר אותה. מה שנותר הוא חימום אנומלי מפני האלקטרודות, צפיפות אופנים ככל שהשרשראות מתארכות, והתנגשויות עם גז הרקע שמשנות את סדר השרשרת או פולטות ממנה יונים. האחרונה היא הבעיה הארכיטקטונית: מפענח שנבנה לרעש פאולי סטוכסטי רואה במקום זאת יונים שדולפים למכלולים מטא-יציבים או נעלמים. הדליפה קטנה דיה כדי לצטט אותה — 1.1×10⁻⁵ לכל קליפורד ב-Helios [D][97] — אך היא מצוטטת בנפרד משום שאינה פאולי. מלכודות קריוגניות, קירור סימפתטי, קידודי מחיקה מטא-יציבים וואקום טוב יותר היו מזיזים את הרצפה.

## מצב ההנדסה העדכני

המיטבי שהודגם והטיפוסי בקנה מידה התקרבו זה לזה במידה יוצאת דופן: Helios מריץ 98 קיוביטים של Ba⁺ בשגיאת שער דו-קיוביטי של 7.9×10⁻⁴ עם קישוריות של כל-לכל, בתוך סדר גודל אחד מהשיא. הפער הוא מהירות — השער ≈ 70 µs, אך שכבה ברוחב מלא אורכת ≈ 55 ms כשמביאים בחשבון מיון, הובלה וקירור מחדש; ההובלה היוותה ~60% מזמן הריצה ב-H2 [D][97], [110].

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2024-07 | בקרה אלקטרונית מלאה, 10 קיוביטים / 7 אזורים: שער דו-קיוביטי 99.97(1)% | Oxford Ionics | [D][257][G:OXIONICS-ALLELEC-2024-07] |
| 2025-10 | שגיאת שער דו-קיוביטי 8.4(7)×10⁻⁵, ללא קירור למצב היסוד | Oxford Ionics / IonQ | [D][102][G:ELECGATE-9999-2025-10] |
| 2025-11 | Helios, 98 Ba⁺: שער דו-קיוביטי 7.9×10⁻⁴, SPAM 3.3–4.8×10⁻⁴, דליפה 1.1×10⁻⁵/קליפורד | Quantinuum | [D][97] |
| 2026-02 | 48 קיוביטים לוגיים מתוקנים ([[80,48,4]]), אי-נאמנות שער לוגי 1.0–1.2×10⁻⁴ | Quantinuum | [D][105][G:HELIOS-ICEBERG-2026-02] |
| 2026-05 | נפח קוונטי 32,768, LYNX בהרכבה במסד | AQT | [C][128] |
| 2026-06 | זיכרון qLDPC בנקודת האיזון בתחום השגיאה: 3.95 ± 0.68 s (קוד אחד) לעומת 3.84 ± 0.48 s פיזי (עודכן בספטמבר 2026) | IonQ | [D][109][G:IONQ-QLDPC-BREAKEVEN-2026-06] |

איבר השגיאה השולט בקנה מידה אינו השער: זו עלות הזזת היונים — עירור בהובלה, קירור מחדש, סידור מחדש — ועוד דליפה שהמפענח אינו יכול לספוג. הדגמות של קודים בקצב גבוה משליכות 75–97% מהריצות בעומק [D][105].

## ייצור, חומרים ושרשרת האספקה

המלכודות הן רכיבי צורן ברמת MEMS, לא ליתוגרפיה המגדירה את הקיוביט: היון מושלם, ולכן השונות בין פרוסות מתבטאת בגאומטריית האלקטרודות ובאיכות פני השטח, ולעולם לא בפיזור בין קיוביט לקיוביט. שני מפעלי ייצור חשובים. Infineon מפעילה פלטפורמת QPU ייעודית ב-Villach על פרוסות של 6 עד 12 אינץ' עם הצמדה אנודית של פרוסות; מלכודות הדור השלישי שלה מוסיפות אלקטרודות מחוץ למישור, שלפי הטענה מגבירות את הכליאה ~10×, ובין המשתמשים הנזכרים eleQtron (שלושה דורות), Oxford Ionics, Innsbruck ו-ETH Zurich [C][320]. Honeywell מייצרת את המלכודות של Quantinuum בתוך הבית — Helios נושא 1,228 אלקטרודות [D][97] — ומלכודת הרשת של Sol חזרה מהייצור ונמצאת בתיקוף [C][123]; בנפרד, Infineon נכנסה לשותפות עם Quantinuum על מלכודות הדור הבא ב-2024-11 [C][321]. Infineon היא נקודת כשל יחידה עבור IonQ/Oxford Ionics, eleQtron ו-Universal Quantum בבת אחת [P][322] — וממנה בדיוק IonQ קונה את דרכה החוצה ברכישת SkyWater תמורת ≈ $1.8 B (נסגרה 2026-07-31) [C][19].

הריכוזיות השנייה אופטית: TOPTICA (הכנסות > €140 M, ~600 עובדים) מספקת את רוב ניסויי היונים הגדולים, והקצה העל-סגול — 369 nm עבור Yb⁺ — הוא החלק המוגבל [P][322]. חומרת הוואקום ומקורות האטומים הם סחורה; קישורים פוטוניים בין מודולים מחזירים תלות קריוגנית דרך גלאי SNSPD [P][322][G:SNSPD-VENDORS-2026]. כלכלת היחידה: AQT סיפקה מסד של 20 קיוביטים ל-LRZ / Munich Quantum Valley תמורת ≈ €9.8 M (2023-12-05, Bavarian Hightech Agenda) [C][323] — ≈ €0.5 M לקיוביט, מערכת מוכנה להפעלה. החשיפה לפיקוח על יצוא עוברת דרך סיווגי ה-ECCN הקוונטיים של ארה״ב מספטמבר 2024; הסיווג של שבב מלכודת חשוף לא אומת כאן.

## בקרה, קריאה ועומס הקלט-פלט

המיעון האופטי לכל יון הוא מה שנכשל בהגדלה ליניארית: Helios דורש לפחות שבעה אורכי גל של לייזר לצד 1,228 ערוצי הנעה של אלקטרודות [D][97]. הקריאה זולה — פלואורנות אל PMT או מצלמה בתוך ≈ 10 µs, לא-הורסת ומתאימה מטבעה לביצוע באמצע המעגל. דרישות ההשהיה מתונות: IonQ מניחה מחזורי סינדרום של 1–5 ms [D][111], בתוך זמני הלוך-ושוב ברמת NVQLink [C][324][G:NVQLINK-2025].

החומה זזה עם N. ב-10³ היא מספר מקורות ההנעה ושטח השולחן האופטי; מחקר WISE טוען שמכונה של 1,000 יונים בקישוריות מלאה יכולה לפעול מ-~200 מקורות עם אלקטרוניקת מיתוג בתוך המלכודת, ב-40–2,600 שכבות שערים בשנייה [S][325][G:WISE-ARCH-2023] — תכנון על הנייר, לא נבנה שבב. ב-10⁴ היא בין-מודולית: שזירה מרוחקת עומדת על 9.7 s⁻¹ על פני 2 m (נאמנות בל 96.9%) [D][115] ועל 250 s⁻¹ במעבדה [D][116], לעומת ~10⁴ s⁻¹ הנדרשים. ב-10⁶ היא שיעור התקינות והספק הלייזר. יצירת השערים ובקרת המיקרוגל שייכות לתקצירים הסמוכים.

## תפקיד במחסנית

הנושא מזין שלוש ארכיטקטורות, כנושא הראשי של כל אחת מהן: *יונים לכודים — QCCD (הובלה בין אזורים)* (Quantinuum, Universal Quantum), *יונים לכודים — מלכודת פאול ליניארית עם מיעון לייזר פרטני* (Aria, Forte ו-Tempo של IonQ; AQT; Qudoor; Quantum Art) ו-*יונים לכודים — בקרה אלקטרונית של הקיוביט (שערי מיקרוגל / RF)* (IonQ/Oxford Ionics, eleQtron, QUDORA). הוא דורש מיקרו-ייצור של מלכודות אלקטרודות משטח והרכבה אופטית/מכנית, והוא התשתית לשער מולמר–סורנסן, לשער המיקרוגל האלקטרוני בשדה הקרוב, לקידוד המחיקה המטא-יציב "omg", להסעה, לגילוי בפלואורנות ולקישור יון–פוטון. הוא אינו מחליף שום דבר ואינו מתנגש בשום דבר: היונים הם עמודה סגורה בפני עצמה, ולכן מעבר ממנה הוא מוחלט — מעל הנושא לא שורד דבר מלבד המהדר.

שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס. בארכיטקטורת QCCD ההובלה שולטת: ≈ 9.7×10⁻³ s לסבב, מתוכם 9.0 ms הובלה, לעומת ≈ 5.5×10⁻² s לשכבה ברוחב מלא [D][97], [110]. בארכיטקטורת השערים האלקטרוניים הסבב ≈ 1.5×10⁻³ s, ונקבע בידי שכבות השערים [D][102]. הפער הזה, פי שישה, הוא המספר המגדיר של הפלטפורמה. משבצת ריקה סמוכה: שכבת הנעה קריוגנית המשולבת בשבב למלכודות יונים — המקבילה ל-SFQ/CMOS קריוגני — אין לה עדיין מאכלס ברמת מוצר.

## ראיות — כיצד נמדדו המספרים

המספרים הדו-קיוביטיים הבולטים מגיעים מגרסאות של בחינת ביצועים אקראית. שיא ה-8.4(7)×10⁻⁵ הוא RB עם דליפה לתת-מרחב על זוג יונים אחד בטמפרטורת דופלר, לא נתון של ההתקן כולו, והטקסט הזמין אינו מציין משך שער [D][102]. הנתון 7.9×10⁻⁴ של Helios הוא נתון ממוצע של ההתקן, העקבי עם הניסוח בדוח הרווחים, "99.921%" [C][123]. נפח קוונטי ו-#AQ הם מדדים מורכבים שהגדירו הספקים, ללא פרוטוקול שחזור [C][98], [99]. יתרה מזו, RB רץ במצב סטטי, ולכן הסעה וקירור מחדש אינם נראים בשגיאות השער המצוטטות. התוצאות הלוגיות כוללות שיעור קבלה (0.62(2) [D][105]), ונקודת האיזון של IonQ נמדדה בבחירה בדיעבד של דליפה [D][109]; אף אחת מהן אינה בלתי מותנית. אף פלטפורמת יונים לא פרסמה הגדלה במרחק מהסוג של Λ.

סתירות. משך השער האלקטרוני הוא 225.8 µs (2025) או ≈ 120 µs (2024) בגרף הטכנולוגיות, ואינו מצוין בתמצית של 2025 — לא אומת. הטענה של Quantinuum ל"נאמנות לוגית של כמעט חמש תשיעיות עם משפחה חדשה של קודים לתיקון שגיאות" [C][123] מקדימה את אי-נאמנות השער הלוגי שפורסמה, 1.0–1.2×10⁻⁴ [D][105]; משפחת הקודים לא פורסמה, ולכן ערך ה-[D] עומד בעינו. Tempo של IonQ משווק ב-"99.9%" וב-#AQ 64 ללא זמני שער שפורסמו [C][99], [326].

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב/בריטניה | שערי לייזר ב-QCCD; Helios, 98 קיוביטים, 48 קיוביטים לוגיים; Sol, Apollo | [D][105] |
| IonQ | מפתח | ארה״ב | שרשראות ארוכות ועוד השערים האלקטרוניים של Oxford Ionics; נקודת איזון ב-qLDPC; בעלת SkyWater | [D][109] |
| Honeywell | ספק | ארה״ב | ייצור MEMS עצמי של מלכודות Quantinuum; בעלת מניות עוגן | [C][122] |
| Infineon Technologies | ספק | אוסטריה/גרמניה | מפעל ייצור מסחרי למלכודות יונים, Villach, 6–12″, מלכודות דור 3 | [C][320] |
| AQT | מפתח | אוסטריה | מערכות יונים בהרכבה במסד 19″; QV 32,768; התקנה ב-LRZ | [C][323] |
| eleQtron | מפתח | גרמניה | בקרת יונים במיקרוגל; המדגים QSea I של DLR; צבר הזמנות €54 M | [G][327] |
| Quantum Art | מפתח | ישראל | ארכיטקטורת יונים לכודים מרובת ליבות; סבב A בסך $140 M | [P][125] |
| Universal Quantum | מפתח | בריטניה | מכונת מלכודות מודולרית במסגרת חוזה DLR בסך €67 M; לא סופק דבר | [P][328] |
| Tsinghua University | מחקר | סין | סימולציה אנלוגית בגביש דו-ממדי של 512 יונים; זיכרון בסדר גודל של שעה | [D][121] |
| Qudoor | מפתח | סין | מערכות מלכודות יונים AbaQ וענן; 32+ פטנטים לפי טענתה | [P][302] |

**כספים.**
- 2022-11-02 · Universal Quantum · חוזה DLR · €67 M · הוכרז [P][328][G:UQ-DLR-67M-2022-11]
- 2023-12-05 · AQT · חוזה, מערכת של 20 קיוביטים עבור LRZ · ≈ €9.8 M · Bavarian StMWK/StMWi · נסגר [C][323]
- 2025-11-06 · IonQ, Quantinuum · שלב B של DARPA QBI · עד $15 M לכל אחת · נבחרו [G][65][G:QBI-STAGEB-2025-11]
- 2025-10-12 · IonQ · הון מניות · $1.0 B + $2.0 B לפי $93/מניה · נסגר [G:IONQ-EQUITY-2025]
- 2025-09-04 · Quantinuum · סבב גיוס · $600 M לפי שווי של $10 B לפני הכסף · NVentures, Quanta, QED, JPMorgan · נסגר [G][122][G:QTM-600M-2025-09]
- 2025-09-17 · IonQ · מיזוג ורכישה של Oxford Ionics · $1.075 B · נסגר [C][18][G:IONQ-OXIONICS-2025]
- 2026-04-27 · Quantum Art · הרחבת סבב A · $100 M → $140 M · נסגר [P][125][G:QART-140M-2026-04]
- 2026-05-05 · eleQtron · סבב A · €57 M · צבר הזמנות €54 M · נסגר [C][128][G:ELEQTRON-57M-2026-05]
- 2026-06-03 · Quantinuum · הנפקה ראשונית לציבור, Nasdaq QNT · $1.68 B ברוטו לפי $60/מניה · נסגרה [G][123][G:QTM-IPO-2026-06]
- 2026-07-31 · IonQ · מיזוג ורכישה של SkyWater · ≈ $1.8 B · נסגר [C][19][G:IONQ-SKYWATER-2026]
- 2026-06-30 · הכנסות הרבעון השני של שנת הכספים 2026 · Quantinuum: $8.0 M, מזומנים $2.1 B, תחזית החברה $28–32 M; IonQ: $80.1 M, מזומנים $3.0 B, תחזית החברה $280–290 M [C][123], [326]

**שוק ושרשרת אספקה.** כסף הציוד נמצא אצל TOPTICA, Infineon וספקי ואקום סחורתיים; סיכון הריכוזיות ממשי בשני מקומות בלבד — לייזרים על-סגולים ומפעל הייצור של Infineon, שעליו נשענים שלושה מפתחים שאחרת אינם תלויים זה בזה [P][322]. לעומת ≈ €9.8 M למסד של 20 קיוביטים [C][323], הכנסות מגזר היונים הן בערך מערכת גדולה אחת לרבעון ועוד גישה בענן. יעדים משלמים: G1 (הסימולטור של Tsinghua), G2 ו-G5 (ענן), G3 (הקיוביטים הלוגיים של Helios, זיכרון ה-qLDPC של IonQ), G7 (המסדים של AQT, צבר ההזמנות של eleQtron), G6 באב-טיפוס. G4 ממומן בידי שוקי ההון ו-DARPA, לא בידי לקוחות.

**קניין רוחני ותקנים.** משפחות מוכרות: בקרת הקיוביטים האלקטרונית של Oxford Ionics וארכיטקטורת המיתוג בתוך המלכודת WISE [S][325]; פטני הצמתים ומלכודות הרשת של Honeywell/Quantinuum ל-QCCD, העומדים מאחורי החלפת יונים ב-2.5 kHz והובלה ב-4 m/s [D][113]; תהליך האלקטרודות התלת-ממדיות בהצמדה אנודית של Infineon [C][320]; תיק הגלאים של ID Quantique, כיום בבעלות IonQ [C][19]. לא נמצאה ספירת פטנטים מתוארכת הייחודית ליונים ממאגר נתונים מזוהה; הסקירה של PatSnap שפורסמה ב-2026-06-30 מונה ל-IonQ 546 משפחות פטנטים קוונטיים, במקום השמיני בין בעלי הפטנטים, אך אינה מפרידה שורה ליונים לכודים [P][G:PATSNAP-2026-06]. אין תקן ייחודי ליונים.

**מפות דרכים ועמידה בהבטחות.** Quantinuum: Helios (הובטח 2024-09-10 · ל-2025 · הושק 2025-11-05) [G:QTM-ROADMAP]; Sol (הובטח 2024-09-10 · ל-2027 · שבב המלכודת יוצר ונמצא בתיקוף); Apollo (ל-2029 · "לפי לוח הזמנים", אבות-טיפוס בלבד) [C][123]. אמינות גבוהה — התאריכים שהובטחו עמדו — מלבד משפחת הקודים של חמש התשיעיות שלא פורסמה. IonQ: 4,000 קיוביטים (הובטח ב-2020 · ל-2026 · החטאה של ~40×) [P][132]; 256 קיוביטים ב-99.99% (הובטח 2025-06-13 · ל-2026 · נדחה למחצית הראשונה של 2027) [R][132]; 10,000 על שבב אחד (ל-2027 · לא פורסמו נתוני חימום או נתוני חיבור בין-מודולי של מלכודת דו-ממדית). אמינות מעורבת: הפיזיקה ניתנת לביקורת עמיתים, לוחות הזמנים לא. AQT מספקת את שיאי ה-QV שלה בזמן; Universal Quantum לא הכריזה על דבר במסגרת החוזה שלה מ-2022 [P][328].

**פרשנות אסטרטגית.** אם היונים ינצחו, Honeywell ו-Infineon ילכדו רנטה מבנית — האחת באמצעות אינטגרציה אנכית שאיש אינו יכול להעתיק, השנייה כמפעל הייצור המסחרי היחיד למלכודות — ו-TOPTICA תהפוך לצוואר הבקבוק. רכישת SkyWater בידי IonQ הופכת תלות בספק לנכס בבעלות: הימור על כך שייצור המלכודות, ולא הפיזיקה של הקיוביט, הוא המשאב הנדיר. איום התחליף אינו המעגלים מוליכי-העל (שעון מהיר יותר, נאמנות נמוכה יותר) אלא האטומים הניטרליים: אותו נושא טבעי, אותה הנדסה עתירת אופטיקה, כבר אלפי אתרים, ונאמנות ההולכת ומשתווה. כוח המיקוח עדיין בידי ספקי הפלטפורמות: יחידת הקוונטים של Infineon היא שגיאת עיגול בתוך חברה של €15 B [P][322], ואינה יכולה לתמחר כמונופול.

## תחזית ושאלות פתוחות

לאשר אם: Sol יסופק ב-2027 עם ≥ 192 קיוביטים פיזיים על מלכודת רשת דו-ממדית *וגם* זמן שכבה שפורסם טוב מ-≈ 55 ms; ספק יונים כלשהו מפרסם הגדלה עם Λ > 1 לאורך d = 3→5→7; השזירה המרוחקת עוברת את 10³ s⁻¹. להוריד בדרגה אם: IonQ לא הציגה 256 קיוביטים ב-99.99% עד סוף 2027 (כבר נדחה פעם אחת); Sol אינו משפר את זמן השכבה; או שמשפחת הקודים של חמש התשיעיות לא תפורסם גם כעבור שנה.

התרחיש הטוב ביותר עד 2029: Apollo מגיע עם מאות קיוביטים לוגיים ב-10⁻⁶–10⁻¹⁰ והיונים שולטים בסבילות המוקדמת לתקלות, וגירעון השעון נספג באלגוריתמים הזקוקים לעומק. התרחיש הגרוע ביותר: ההגדלה הדו-ממדית מכפילה את עלות ההובלה במקום לפזר אותה, זמן השכבה נשאר בעשרות מילישניות, והיונים הופכים למכשיר בעל נאמנות גבוהה ותפוקה נמוכה למחקר תיקון שגיאות, בזמן שהאטומים הניטרליים והמעגלים מוליכי-העל לוקחים את הנפח.

שאלות פתוחות: האם החימום במלכודת רשת גדל עם מספר האזורים או עם שטח האלקטרודות? האם אפשר להמיר דליפה למחיקה מהר מספיק כדי שהמפענחים יפסיקו לשלם עליה? מהו המשך האמיתי של השער האלקטרוני ברוחב מלא? האם שזירה מרוחקת של 10⁴ s⁻¹ ניתנת להשגה בכלל? מי יהיה מקור אספקה שני ל-Infineon?

## מקורות
[18] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[98] Quantinuum, “Quantum Volume.” [Online]. Available: https://www.quantinuum.com/glossary-item/quantum-volume [C]
[99] IonQ, “IonQ Forte: High-Performance Commercial Quantum Computer.” [Online]. Available: https://www.ionq.com/quantum-systems/forte [C]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[104] P. Wang *et al.*, “Single ion-qubit exceeding one hour coherence time,” *Nat. Commun.*, vol. 12, Art. no. 233, Jan. 2021, doi: [10.1038/s41467-020-20330-w](https://doi.org/10.1038/s41467-020-20330-w). [arXiv:2008.00251](https://arxiv.org/abs/2008.00251). [D]
[105] S. Dasu *et al.*, “Computing with many encoded logical qubits beyond break-even,” [arXiv:2602.22211](https://arxiv.org/abs/2602.22211), Feb. 2026. [D]
[109] E. Tham *et al.*, “Breakeven demonstration of quantum low-density parity-check codes,” [arXiv:2606.06455](https://arxiv.org/abs/2606.06455), Jun. 2026. [D]
[110] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828). [D]
[111] M. Ye, A. Maksymov, and N. Delfosse, “Real-time decoder for a MegaQuOp quantum computer using a single CPU,” [arXiv:2608.25027](https://arxiv.org/abs/2608.25027), Aug. 2026. [D]
[113] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756). [D]
[115] D. Main *et al.*, “Distributed quantum computing across an optical network link,” *Nature*, vol. 638, no. 8050, pp. 383–388, Feb. 2025, doi: [10.1038/s41586-024-08404-x](https://doi.org/10.1038/s41586-024-08404-x). [D]
[116] J. O'Reilly *et al.*, “Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking,” *Phys. Rev. Lett.*, vol. 133, Art. no. 090802, Aug. 2024, doi: [10.1103/PhysRevLett.133.090802](https://doi.org/10.1103/PhysRevLett.133.090802). [arXiv:2404.16167](https://arxiv.org/abs/2404.16167). [D]
[121] S.-A. Guo *et al.*, “A site-resolved two-dimensional quantum simulator with hundreds of trapped ions,” *Nature*, vol. 630, no. 8017, pp. 613–618, May 2024, doi: [10.1038/s41586-024-07459-0](https://doi.org/10.1038/s41586-024-07459-0). [D]
[122] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [C]
[123] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[125] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [P]
[257] C. Löschnauer *et al.*, “Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040313, Oct. 2025, doi: [10.1103/h4wk-v31j](https://doi.org/10.1103/h4wk-v31j). [arXiv:2407.07694](https://arxiv.org/abs/2407.07694). [D]
[302] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[321] Quantinuum, “Infineon and Quantinuum announce partnership to accelerate quantum computing towards meaningful real-world applications,” Nov. 19, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/infineon-and-quantinuum-announce-partnership-to-accelerate-quantum-computing-towards-meaningful-real-world-applications [C]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[324] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[325] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773). [S]
[326] IonQ, “IonQ Announces Record Second Quarter 2026 Revenues, Growing 287% YoY,” Aug. 5, 2026. [Online]. Available: https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[327] German Aerospace Center (DLR), “QSea I – Quantum computer demonstrator with 10 ion trap qubits,” DLR Quantum Computing Initiative. [Online]. Available: https://qci.dlr.de/en/qsea-i/ [G]
[328] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]

## פריטי אימות פתוחים

- משך השער האלקטרוני בשיא של 2025: הטקסט הזמין של arXiv:2510.17286 אינו מציין לא את 225.8 µs (2025) ולא את ≈ 120 µs (2024). לא אומת.
- הטענה של Quantinuum ל"נאמנות לוגית של כמעט חמש תשיעיות עם משפחה חדשה של קודים לתיקון שגיאות" (שיחת הרבעון השני של 2026): נכון ל-2026-09-03 אין מאמר, ולא נקבה בשמה משפחת קודים.
- זמני שער מולמר–סורנסן של IonQ Forte בשרשראות של 30+ יונים (550–883 µs, חציון 672 µs; שער חד-קיוביטי 110 µs) מופיעים בדוח הראשי ללא מקור ממוספר; לא אומתו כאן באופן עצמאי.
- סיווג הפיקוח על יצוא של שבב מלכודת יונים חשוף ולא מאוכלס לפי סיווגי ה-ECCN הקוונטיים של ארה״ב מספטמבר 2024 (משפחת 4A906) ולפי הפיקוח הלאומי של בעלות הברית — נוסח התקנה עצמו לא נבדק כאן; לא אומת.
- הודעת העיתונות של Infineon infpss202604-080 ("Quantum chips: Infineon contributes industrialization", 2026-04) לא אוחזרה (דף ניווט בלבד); היקפי הפרוסות ושותפים חדשים ב-2026, אם יש, לא אושרו.
- פעילות מסחרית סינית ביונים לכודים: Qudoor (AbaQ, 32+ פטנטים לפי טענתה) היא ספקית מלכודות היונים היחידה הנזכרת במקורות 2026 שנסקרו; לא נמצאו סכום מימון, תאריך, שווי או מספר קיוביטים.
- Universal Quantum: נכון ל-2026-09-03 לא הוכרזו אספקה, אבן דרך או תוצאת נאמנות במסגרת חוזה ה-DLR בסך €67 M.
- AQT ו-QUDORA Technologies (Braunschweig; חברת בת בטוקיו נפתחה 2026-05): לא נמצא סבב גיוס הון עם סכום ותאריך מוצהרים.
- ההודעה של Quantinuum לרבעון השני של 2026 אינה חושפת הזמנות, צבר הזמנות, מכירות יחידות Helios או שמות לקוחות.
