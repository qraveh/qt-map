---
id: ro_spd
name: גילוי פוטון בודד (SNSPD / TES)
layer: "6 קריאה"
status: demonstrated
since: 2001
one_line: "גלאים קריוגניים מוליכי-על ההורסים פוטון כדי לרשום אותו; איבר הקריאה המשותף של כל פלטפורמה פוטונית ושל כל פלטפורמה המקושרת בפוטונים."
verdict: "הנצילות פתורה במעבדה (99.73% על השבב) אך לא בקנה מידה של פרוסה (חציון של 93.4% ב-Omega); מספר הערוצים והקריוגניקה, לא הפיזיקה, מכריעים אם סבילות לתקלות פוטונית ניתנת לבנייה."
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

ננו-תיל מוליך-על בממתח זרם בולע פוטון אחד, יוצר נקודה חמה התנגדותית ופולט פולס מתח; חיישן קצה-מעבר (TES) מודד במקום זאת את האנרגיה הנבלעת קלורימטרית, וכך מבחין במספר הפוטונים. הקבוצה של Gol'tsman ב-Moscow State Pedagogical University הדגימה את התקן ה-NbN הראשון ב-2001 [D][626]; ה-TES בממתח מתח מתוארך ל-Irwin (1995) [D][627]. Scontel, שעודנה ב-Moscow, יורשת ישירה של אותה קבוצה ראשונה.

תכונות. זיקת הנושא: מיוצרת — שכבה דקה ליתוגרפית, לא מערכת קוונטית טבעית. זמן אופייני ושזירה: לא ישים; הטכנולוגיה אינה מארחת קיוביט ואינה מבצעת פעולת שזירה. קריאה: גילוי פוטון בודד, ~1.0×10⁻⁸ s לאירוע כולל איפוס, **הורסת**, לא באמצע המעגל — הפוטון נצרך. ניידות: אין; נקודת קצה קבועה. אופן הבקרה ומיקומה: ממתח והגברה אלקטרו-אופטיים בשלב ה-1–4 K. מבנה השגיאה השולט כפי שהקוד רואה אותו: אובדן — גילוי שהוחמץ הוא מחיקה במיקום ידוע, וספירת חושך היא חיובי שגוי שהמפענח אינו יכול להבחין בינו לבין קליק אמיתי. ייצור: תהליך של מעגלים פוטוניים משולבים, יותר ויותר אותו תהליך הנושא את מוליכי הגל.

## פיזיקה וגבולות

פוטון של 1550 nm נושא 0.80 eV מול פער NbN של כמה meV, ולכן הבליעה שוברת כ-10³ זוגות קופר; האות עצום ביחס לפער, ולכן הסתברות הגילוי הפנימית רוויה קרוב לאחד (99.99% בממתח של 5.5 µA [D][628]). הנצילות היא לפיכך בעיה של אופטיקה, לא של מוליכות-על: היא מתפרקת לצימוד סיב × בליעה × הסתברות פנימית, והאמנות היא סילוק האיבר הראשון (שילוב במוליך גל) או הנדוס השני (מראות דיאלקטריות [D][618]). הרצפות האמיתיות הן תזמון וקצב: האיפוס הוא השראות קינטית חלקי עומס, כ-10 ns, המגביל את הקצב לפיקסל לעשרות Mcps, ואילו לריצוד יש רצפת פאנו מסטטיסטיקת הנקודה החמה ועוד איבר גאומטרי לאורך החוט — ולכן 2.7 ± 0.2 ps FWHM ב-400 nm מידרדר ל-4.6 ± 0.2 ps ב-1550 nm [D][629]. TES מוותר על שניהם: הבחנה במספר הפוטונים תמורת התאוששות של ~µs ב-~100 mK, מקרר דילול ולא ראש קר של 2–4 K.

במטבע שבו משתמשת הסבילות לתקלות הפוטונית, 1% של אי-נצילות עולה 0.044 dB. הנצילות החציונית על השבב של PsiQuantum, 93.4% [D][169], עולה **0.30 dB** מול תקציב מיזוג לפוטון הקרוב ל-0.5 dB, ואי-הנצילות שלה, 6.6%, היא לבדה פי 2.4 מסף האובדן של 2.7% בסכמות מיזוג של טבעת-6 [S][179]. שום דבר אחר כאן אינו חשוב כמו החשבון הזה.

## מצב ההנדסה העדכני

ההדגמה הטובה ביותר היא זוג מוליכי גל בטור בנצילות של 99.73% על השבב, 1.5 K, NbN, ברוחב 100 nm ובעובי 5 nm [D][628]. הטיפוסי בקנה מידה גדול שונה: חציון של 93.4% על השבב על פני פרוסות ה-Omega של PsiQuantum ב-300 mm ב-~2 K [D][169], ומערכות קטלוג המצטטות רק ">90% סמוך ל-1550 nm" עם ריצוד מתחת ל-100 ps [C][630], [631]. הפער בין התקן שיא לחציון של פרוסה הוא הבעיה ההנדסית. האיבר השולט היום הוא אי-נצילות הכרוכה באובדן במוליכי הגל ובמתגים; במכונת רשת אלה ספירות החושך והריצוד מול חלון צירוף המקרים.

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2001 | גלאי הפוטון הבודד הראשון מננו-תיל NbN | Moscow State Pedagogical University | [D][626] |
| 2008 | TES בנצילות של 95% ב-1556 nm, מבחין במספר הפוטונים | NIST Boulder | [D][632] |
| 2020-11 | נצילות גילוי מערכתית 98.0 ± 0.5% ב-1550 nm, מצומד לסיב | NIST | [D][618] |
| 2020 | ריצוד תזמון 2.7 ± 0.2 ps FWHM ב-400 nm; 4.6 ± 0.2 ps ב-1550 nm | JPL | [D][629] |
| 2023-10 | מצלמה של 400,000 פיקסלים, 4 × 2.5 mm, קריאת שורה–עמודה תרמית | NIST Boulder | [D][339] |
| 2025-02 | נצילות חציונית על השבב 93.4% ב-~2 K, קו מפעל ייצור של 300 mm | PsiQuantum | [D][169] |
| 2025-10 | נצילות על השבב 99.73% בטור (97.33% יחיד), 1.5 K | Nanjing University | [D][628] |

## ייצור, חומרים ושרשרת האספקה

ארבע מערכות חומרים מתחרות: NbN ו-NbTiN (מהירים, 2–4 K, ברירת המחדל המסחרית), WSi אמורפי (הנצילות הגבוהה ביותר, ~1 K, בחירתה של NIST לשיאים) ו-MoSi. שכבות אמורפיות אחידות יותר על פני פרוסה, וזה מה שקו של 300 mm צריך; NbN רב-גבישי מהיר יותר. שילוב הגלאים של PsiQuantum בזרימת 300 mm של GlobalFoundries לצד מוליכי גל מ-SiN ומתגים מבריום-טיטנאט הוא נקודת הנתונים היחידה בקנה מידה של פרוסה, והחציון שפרסמה — לא הפיסה הטובה ביותר שלה — הוא הצהרת התקינות הכנה [D][169].

שרשרת האספקה קצרה ומרוכזת. הספקים העצמאיים הם Single Quantum (Delft), ID Quantique (Geneva, בבעלות IonQ מאז 2025), Photon Spot (Monrovia, CA), Quantum Opus (Michigan) ו-Scontel (Moscow); NIST ו-JPL קובעות את השיאים אך אינן מוכרות דבר. כל אחד מהם משווק בתוך קריוסטט במחזור סגור, ולכן נקודת הכשל היחידה נמצאת במעלה הזרם: ראשים קרים מסוג Gifford-McMahon וצינור פולסים מקומץ יצרנים (Sumitomo Heavy Industries, Cryomech, ומשלבים כמו Bluefors), ועוד הליום-4, כבלים קואקסיאליים קריוגניים ומעברי סיב. Photon Spot מפחיתה זאת במכירת קריוסטטים Cryospot משלה [C][630].

החשיפה לפיקוח על יצוא יושבת על הקריוגניקה, לא על הגלאי. כלל הביניים הסופי של BIS מ-2024-09-06 יצר את ECCN 3A904 לקירור קריוגני מתחת ל-4.5 K, עם 3A901.b למגברים בגבול הקוונטי [G:BIS-3A901A-CRYOCMOS][301]; גלאי פוטון בודד אינם נקובים, אך הקופסה שהם חיים בה מפוקחת. מיקומה של Scontel ב-Moscow הופך אותה לבלתי זמינה בפועל לתוכניות מערביות אחרי 2022 — שיפוט, לא עובדה ממקור.

## בקרה, קריאה ועומס הקלט-פלט

לכל ערוץ: זרם ממתח, מגבר, קו קואקסיאלי מ-1–4 K לטמפרטורת החדר, וכניסה של מתייג זמן. נסבל ב-10¹–10² ערוצים — השוק המסחרי כולו — ומגביל מעליהם. ב-10³ עומס החום של הכבלים הקואקסיאליים ותקציב הקירור ב-2–4 K שולטים; KIDE של Bluefors, עם תשעה מקררי צינור פולסים ו"יותר מ-4,000 קווי RF" [C][G:BLUEFORS-KIDE][303], הוא בקירוב תקרת מה שניתן לשווק. ב-10⁴ החיווט חייב לפנות את מקומו לריבוב: סכמת השורה–עמודה התרמית של מצלמת 400,000 הפיקסלים [D][339] מראה שזה עובד כשאפשר להקריב את התזמון, אך רשתות מיזוג זקוקות להזנה קדימה ב-MHz–GHz מהקליק אל המתג ואינן יכולות להקריב אותו. ב-10⁶ הגלאי, המגבר ומפריד הריבוב חייבים להיות מונוליתיים בתהליך הפוטוני, ומתקן הקירור הופך לדרגת קילוואט ב-2–4 K; עבודת שלב C של PsiQuantum ב-DARPA מכסה במפורש זיווד ותיקוף קריוגניקה [P][G:PSIQ-QBI-C-2026-07][181], ואספקת מתקן הקירור של Linde לאתר שלה ב-Moreton Bay אינה צפויה לפני המחצית השנייה של 2027 [C][G:PSIQ-GROUNDBREAKING-2026-06].

## תפקיד במחסנית

הטכנולוגיה יושבת על ארכיטקטורת המשתנה הבדיד מבוססת-המיזוג (PsiQuantum, Quandela, QuiX), על ארכיטקטורת המשתנה הרציף/GKP (Xanadu) ועל דוגם הבוזונים. היא דורשת פוטונים בודדים ומספקת בישור למיזוג באופטיקה ליניארית ועוד גילוי פוטונים לחיבורים הבין-מודוליים יון–פוטון וספין–פוטון: חלק אחד הוא איבר הקריאה של שלוש מודאליות שאינן קשורות זו לזו בשום דבר אחר. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס — אין סבב כזה בארכיטקטורה פוטונית; הגלאי תורם ~1.0×10⁻⁸ s, ולכן הוא לעולם אינו האיבר האיטי בקישורי יונים או פגמים (קצבים של 10–250 s⁻¹ [D][115], [116]), ורק בשוליים כזה במיזוג, שבו השהיית ההזנה קדימה שולטת.

היא מתנגשת בקוד המשטח במיוחד: גילוי הורס שולל חילוץ סינדרום חוזר על אותו פוטון, ולכן תיקון שגיאות פוטוני חייב לחולל נושאים מחדש בין סבבים. המעבר ממנה אינו סימטרי — ארכיטקטורת המשתנה הרציף של Xanadu משתמשת בגילוי הומודיני בטמפרטורת החדר לרוב המדידות וזקוקה להבחנה במספר הפוטונים רק להכנת GKP [D][173], [174]. משבצות ריקות סמוכות: גלאי בטמפרטורת החדר המבחין במספר הפוטונים ב->99%, וכל מונה פוטונים לא-הורס בתחום הטלקום, שהיה ממוסס את ההתנגשות שלעיל.

## ראיות — כיצד נמדדו המספרים

נצילות הגילוי המערכתית נמדדת מול לייזר מונחת מאוד ומד הספק מכויל, שאת אי-הוודאות שלו מחברי Nanjing מעמידים על 2–5% [D][628] — בר-השוואה לפער בין הכותרות 98.0 ± 0.5% [D][618] ו-99.73% [D][628]. השתיים הן גם גדלים שונים: נצילות על השבב אינה כוללת צימוד סיב-לשבב, ולכן אסור לעולם לטבל שיאים משולבים במוליך גל לצד שיאים מצומדי-סיב ללא ההסתייגות הזאת. לא נלכד: פולסי המשך (afterpulsing), נעילה (latching), התקפות סנוור, וההתפלגות המשותפת של נצילות וריצוד על פני פרוסה, שהיא מה שמשלב צריך.

סתירה. נתון של "חציון 98.9% (PsiQuantum)" מצוטט במקום אחר; מאמר ה-Omega ורשומת העובדה המשותפת נותנים שניהם חציון של 93.4% על השבב [D][169][G:PSIQ-OMEGA-METRICS-2025]. נתון המקור הראשוני, 93.4%, הוא העומד בתוקף; ההבדל הוא 0.30 dB לעומת 0.05 dB לגילוי.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים | ראיות |
|---|---|---|---|---|
| PsiQuantum | מפתח | ארה״ב | SNSPD עצמיים מונוליתיים ב-Omega על 300 mm של GlobalFoundries, חציון 93.4% | [D][169] |
| Single Quantum | ספק | הולנד | מערכות SNSPD מוכנות להפעלה; המערכת ה-400 נשלחה ל-Q*Bird ב-2026-07 | [P][621] |
| ID Quantique | ספק | שווייץ | גלאי SNSPD ו-InGaAs ועוד QKD; נרכשה בידי IonQ ב-2025-05-06 | [P][633] |
| Photon Spot | ספק | ארה״ב | SNSPD ועוד קריוסטטים Cryospot משלה; נצילות קוונטית >90%, ריצוד מתחת ל-100 ps | [C][630] |
| Quantum Opus | ספק | ארה״ב | Opus One, ≥90% ב-1310/1550 nm, >2 K, הבחנה במספר הפוטונים ברישיון | [C][631] |
| Scontel | ספק | רוסיה | קווי SSPD בשטח גדול, ברעש נמוך במיוחד ובהבחנה במספר הפוטונים | [C][634] |
| NIST Boulder | מחקר | ארה״ב | שיא נצילות של 98.0%, שכבות WSi, מצלמה של 400 kpixel, כיול | [D][339], [618] |
| JPL | מחקר | ארה״ב | שיא ריצוד של 2.7 ps; מערכים לתקשורת אופטית בחלל העמוק | [D][629] |
| Nanjing University | מחקר | סין | נצילות של 99.73% על השבב בטור | [D][628] |
| Xanadu | משתמש | קנדה | ארכיטקטורת המשתנה הרציף נשענת על גילוי הומודיני; הבחנה במספר הפוטונים רק ל-GKP | [D][173] |
| Bluefors | ספק | פינלנד | פלטפורמות קריוגניות; KIDE, תשעה מקררי צינור פולסים, >4,000 קווי RF | [C][303] |

**כספים.**

- 2025-05-06 · IonQ / ID Quantique · מיזוג ורכישה · התמורה לא נחשפה בהודעות המצוטטות · — · נסגר [P][633]
- 2025-09-10 · PsiQuantum · סבב E · $1 B לפי שווי של $7 B · BlackRock, Temasek, Baillie Gifford · נסגר [G:PSIQ-1B-2025-09]
- 2025-11-06 · שלב B של DARPA QBI · תוכנית · עד $15 M לכל אחד, 11 מבצעים ובהם Xanadu, Photonic Inc. · DARPA · הוענק [G:QBI-STAGEB-2025-11][65]
- 2026-03-26 · Xanadu · סגירת SPAC · ~$302 M ברוטו, ~40% מתחת לתוכנית · Crane Harbor · נסגר [G:XANADU-SPAC-2026-03]
- 2026-05-21 · PsiQuantum · מכתב כוונות של CHIPS · $100 M · US Dept of Commerce · מכתב כוונות (לא מחייב) [G:CHIPS-LOI-2026-05][300]
- 2026-06-16 · Quandela · שלב A של DARPA QBIT · הסכום לא נחשף · DARPA · הוכרז [G:QBI-QBIT-2026]
- 2026-07-04 · Single Quantum · מערכת ה-SNSPD ה-400 סופקה · ההכנסות לא נחשפו · Q*Bird · דווח [P][621]
- 2026-07-22 · PsiQuantum · הרחבת שלב C של DARPA QBI (מתגים, זיווד, אימות ותיקוף קריוגניקה) · $125 M, אחרי $31.8 M ב-2025-09 · DARPA · הוכרז [P][G:PSIQ-QBI-C-2026-07][181]
- 2026-08-28 · Xanadu · מימון מפעל קנדי · CAD 195 M · תוכנית פדרלית · הוכרז [C][178]

אף ספק גלאים אינו מופיע בפנקס הזה עם סבב שנחשף: בסיס האספקה העצמאי פרטי, אטום, וקטן בסדר גודל מספקי הפלטפורמות התלויים בו.

**שוק ושרשרת אספקה.** אף ספק אינו מפרסם מחירים [C][630], [631], [634], ולכן כלכלת היחידה אינה ניתנת לאימות. הביקוש המשלם היום הוא רשתות G6 — QKD, שבו חיים 400 המערכות של Single Quantum וקו המוצרים של ID Quantique — ועוד עוגן לא-קוונטי במערכות G7 הניתנות לפריסה (תקשורת אופטית בחלל העמוק ולירח; NASA, NIST, Fermilab, Sandia ו-Argonne הם לקוחות נקובים [C][630], [631]). G3/G4 משלמים רק דרך PsiQuantum, Xanadu, Quandela, QuiX ו-Photonic Inc. סיכון הריכוזיות במעלה הזרם: ראשים קרים, הליום, כבלים קואקסיאליים קריוגניים.

**קניין רוחני ותקנים.** Quantum Opus מחזיקה ברישיון בלעדי ל-US 11,274,962 B2 להבחנה במספר הפוטונים [C][631]. נכון ל-2026-09-03 לא נמצא לטכנולוגיה זו נתון מתוארך של ספירת פטנטים ממאגר נקוב. אין תקן ייחודי ל-SNSPD; עקיבות הכיול היא בפועל של NIST [D][339], [618].

**מפות דרכים ועמידה בהבטחות.** PsiQuantum (מובטח מאז 2021 · מערכת שימושית עד סוף 2027 · בסיכון: הנחת אבן הפינה ב-Moreton Bay רק ב-2026-06, אספקת מתקן הקירור צפויה במחצית השנייה של 2027 [C][G:PSIQ-GROUNDBREAKING-2026-06], לא פורסמה הדגמת חומרה ב-2026) [P][181]. Xanadu (הובטח ב-2026-08-31 · אובדן פי 24.1 מעל הסף ב-2026 → פי 1.0 ב-2030, 1,000+ קיוביטים לוגיים עד 2031 · מפת דרכים על הנייר בלבד) [C][178]. Single Quantum (אין מפת דרכים פומבית; 400 מערכות שסופקו הן המדד המתוארך היחיד) [P][621]. אמינות: ספקי הגלאים מבטיחים פחות ומספקים; פיזיקת הגלאים של PsiQuantum אמינה ולוח הזמנים שלה לא; מפת הדרכים של Xanadu בת שלושה שבועות ולא נבחנה.

**פרשנות אסטרטגית.** אם חישוב פוטוני מבוסס-מיזוג יתרחב, מספר הגלאים למכונה יעלה מ-10² ל-10⁶, והספקים העצמאיים יצטרכו להפוך למעניקי רישיונות קניין רוחני המשולבים במפעלי ייצור או להידחק בידי גלאים מונוליתיים עצמיים — PsiQuantum כבר בחרה לעצמה בתוצאה השנייה. כוח המיקוח של הספקים חלש מול ספקי הפלטפורמות וחזק רק ב-QKD ובתקשורת חלל, שבהם הכמויות אמיתיות והשילוב לא. איום התחליף הוא גילוי הומודיני בארכיטקטורת המשתנה הרציף: זול ובטמפרטורת החדר. המנצח השקט בכל תרחיש הוא תעשיית המקררים הקריוגניים.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם מפת פרוסה שפורסמה תראה נצילות חציונית על השבב של >99% על פני קו של 300 mm; אם תודגם קריאה קריוגנית של >10³ ערוצים עם ריצוד לערוץ והשהיית הזנה קדימה; אם מתקן הקירור של PsiQuantum ב-Moreton Bay יסופק במחצית השנייה של 2027, כמובטח [C][G:PSIQ-GROUNDBREAKING-2026-06]. להוריד בדרגה אם PsiQuantum לא תפרסם נתוני גלאים עד סוף 2027, או אם חציוני הפרוסות יישארו מתחת ל-95% בעוד אובדני המתגים והצימוד יורדים. התרחיש הטוב ביותר עד 2029: גלאים משולבים במוליך גל מעל חציון של 99% עם אלפי ערוצים מרובבים על השבב. התרחיש הגרוע ביותר: שיאים ממשיכים להיקבע בהתקני מעבדה של שני גלאים, בעוד חציוני הפרוסות נתקעים סביב 93–95% וסף האובדן של 2.7% נשאר בלתי מושג.

שאלות פתוחות. (1) מהי ההתפלגות המשותפת של נצילות וריצוד על פני פרוסה של 300 mm, ומהו קריטריון התקינות? (2) האם אפשר להשיג הבחנה במספר הפוטונים ב-2 K, או ש-GKP דורש לצמיתות TES סמוך ל-100 mK? (3) לאיזה הספק קירור לערוץ ב-2 K זקוקה מכונה של 10⁵ ערוצים, ומי בונה מתקן כזה? (4) האם סכמה לא-הורסת כלשהי מגיעה לאורכי גל של טלקום בנצילות שמישה? (5) האם לספקים העצמאיים יש מסלול תואם-מפעל-ייצור? יש לעקוב אחר מאמר החומרה הבא של PsiQuantum ואחר אבני הדרך של שלב C, ואחר כל סבב שייחשף ב-Single Quantum, ב-Photon Spot או ב-Quantum Opus — האות הראשון לכך שהביקוש עבר מעבר ל-QKD.

## מקורות
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[115] D. Main *et al.*, “Distributed quantum computing across an optical network link,” *Nature*, vol. 638, no. 8050, pp. 383–388, Feb. 2025, doi: [10.1038/s41586-024-08404-x](https://doi.org/10.1038/s41586-024-08404-x). [D]
[116] J. O'Reilly *et al.*, “Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking,” *Phys. Rev. Lett.*, vol. 133, Art. no. 090802, Aug. 2024, doi: [10.1103/PhysRevLett.133.090802](https://doi.org/10.1103/PhysRevLett.133.090802). [arXiv:2404.16167](https://arxiv.org/abs/2404.16167). [D]
[169] K. Alexander *et al.*, “A manufacturable platform for photonic quantum computing,” *Nature*, vol. 641, no. 8064, pp. 876–883, Feb. 2025, doi: [10.1038/s41586-025-08820-7](https://doi.org/10.1038/s41586-025-08820-7). [D]
[173] H. A. Rad *et al.*, “Scaling and networking a modular photonic quantum computer,” *Nature*, vol. 638, no. 8052, pp. 912–919, Jan. 2025, doi: [10.1038/s41586-024-08406-9](https://doi.org/10.1038/s41586-024-08406-9). [D]
[174] M. V. Larsen *et al.*, “Integrated photonic source of Gottesman–Kitaev–Preskill qubits,” *Nature*, vol. 642, no. 8068, pp. 587–591, Jun. 2025, doi: [10.1038/s41586-025-09044-5](https://doi.org/10.1038/s41586-025-09044-5). [D]
[178] Xanadu Quantum Technologies Limited, “Xanadu Charts Path to Over 1,000 Logical Qubits by 2031,” GlobeNewswire, Aug. 31, 2026. [Online]. Available: https://www.globenewswire.com/news-release/2026/08/31/3353211/0/en/xanadu-charts-path-to-over-1-000-logical-qubits-by-2031.html [C]
[179] S. Bartolucci *et al.*, “Fusion-based quantum computation,” *Nat. Commun.*, vol. 14, Art. no. 912, Feb. 2023, doi: [10.1038/s41467-023-36493-1](https://doi.org/10.1038/s41467-023-36493-1). [arXiv:2101.09310](https://arxiv.org/abs/2101.09310). [S]
[181] M. Abdel-Kareem, “PsiQuantum Secures $125 Million Expanded Agreement with DARPA under QBI Program,” Quantum Computing Report, Jul. 22, 2026. [Online]. Available: https://quantumcomputingreport.com/psiquantum-secures-125-million-expanded-agreement-with-darpa-under-qbi-program/ [P]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[303] Bluefors, “KIDE Cryogenic Platform — For Large-Scale Quantum Computing,” Jun. 16, 2026. [Online]. Available: https://bluefors.com/products/kide-cryogenic-platform/ [C]
[339] B. G. Oripov *et al.*, “A superconducting nanowire single-photon camera with 400,000 pixels,” *Nature*, vol. 622, no. 7984, pp. 730–734, Oct. 2023, doi: [10.1038/s41586-023-06550-2](https://doi.org/10.1038/s41586-023-06550-2). [D]
[618] D. V. Reddy, R. R. Nerem, S. W. Nam, R. P. Mirin, and V. B. Verma, “Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm,” *Optica*, vol. 7, no. 12, p. 1649, Dec. 2020, doi: [10.1364/OPTICA.400751](https://doi.org/10.1364/OPTICA.400751). [D]
[621] TipRanks, “Single Quantum Hits 400-System Milestone as It Deepens European Quantum Partnerships,” Jul. 4, 2026. [Online]. Available: https://www.tipranks.com/news/private-companies/single-quantum-hits-400-system-milestone-as-it-deepens-european-quantum-partnerships [P]
[626] G. N. Gol'tsman *et al.*, “Picosecond superconducting single-photon optical detector,” *Appl. Phys. Lett.*, vol. 79, no. 6, pp. 705–707, Aug. 2001, doi: [10.1063/1.1388868](https://doi.org/10.1063/1.1388868). [D]
[627] K. D. Irwin, “An application of electrothermal feedback for high resolution cryogenic particle detection,” *Appl. Phys. Lett.*, vol. 66, no. 15, pp. 1998–2000, Apr. 1995, doi: [10.1063/1.113674](https://doi.org/10.1063/1.113674). [D]
[628] Z.-G. Li *et al.*, “Surpassing 99% detection efficiency by cascading two superconducting nanowires on one waveguide with self-calibration,” *Light: Science & Applications*, vol. 14, no. 1, Art. no. 369, Oct. 2025, doi: [10.1038/s41377-025-02031-5](https://doi.org/10.1038/s41377-025-02031-5). [D]
[629] B. A. Korzh *et al.*, “Demonstration of sub-3 ps temporal resolution with a superconducting nanowire single-photon detector,” *Nat. Photon.*, vol. 14, no. 4, pp. 250–255, Mar. 2020, doi: [10.1038/s41566-020-0589-x](https://doi.org/10.1038/s41566-020-0589-x). [arXiv:1804.06839](https://arxiv.org/abs/1804.06839). [D]
[630] Photon Spot, “Photon Spot — Cryogenic & Quantum Detection Systems.” [Online]. Available: https://www.photonspot.com/ [C]
[631] Quantum Opus, “World-Class Photon Detection. Simplified.” [Online]. Available: https://www.quantumopus.com/ [C]
[632] A. E. Lita, A. J. Miller, and S. W. Nam, “Counting near-infrared single-photons with 95% efficiency,” *Optics Express*, vol. 16, no. 5, Art. no. 3032, 2008, doi: [10.1364/OE.16.003032](https://doi.org/10.1364/OE.16.003032). [D]
[633] IonQ, “IonQ Completes Acquisition of ID Quantique, Cementing Leadership in Quantum Networking and Secure Communications,” May 6, 2025. [Online]. Available: https://investors.ionq.com/news/news-details/2025/IonQ-Completes-Acquisition-of-ID-Quantique-Cementing-Leadership-in-Quantum-Networking-and-Secure-Communications/default.aspx [P]
[634] SCONTEL, “SCONTEL: SSPD SNSPD HEB CRYOGENICS – DETECT EVERYTHING YOU WANT.” [Online]. Available: https://www.scontel.ru/ [C]

## פריטי אימות פתוחים

- נצילות ה-TES של 95% (Lita/Miller/Nam, Optics Express 2008) וציטוטי השושלת של Gol'tsman 2001 ו-Irwin 1995 מצוטטים מהספרות המקובלת ללא מקור ממוספר.
- נתוני הריצוד של Korzh ועמיתיו באים מהתמצית ב-arXiv; טמפרטורת הפעולה ונצילות הגילוי של אותו התקן לא צוינו שם.
- התמורה ברכישת ID Quantique לא נחשפה בהודעות שהושגו; כתובת חדר החדשות של IonQ, שבה נעשה שימוש במקום אחר בדוח, החזירה 404, ולכן מצוטטת כתובת קשרי המשקיעים.
- Single Quantum, Photon Spot, Quantum Opus ו-Scontel אינן מפרסמות מחירי מערכות SNSPD או הכנסות; כלכלת היחידה אינה ניתנת לאימות.
- ריכוזיות ספקי הראשים הקרים (Sumitomo Heavy Industries, Cryomech) ואי-הזמינות של Scontel לתוכניות מערביות אחרי 2022 הם שיפוטים של אנליסט, לא עובדות ממקור.
- המפרטים של Scontel לכל מוצר (נצילות, ריצוד, ספירות חושך, מספרי ערוצים) נמצאים ב-PDF קטלוגי שלא אוחזר.
