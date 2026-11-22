---
id: fab_scd
name: ייצור אלקטרוניקה ספרתית מוליכת-על (תהליכי ניוביום רב-שכבתיים, לוגיקת SFQ/AQFP)
layer: "10 ייצור"
status: demonstrated
since: 2010
one_line: "תהליכי ניוביום רב-שכבתיים מושטחים ללוגיקה ספרתית מוליכת-על: עד שמונה שכבות חיווט Nb עם צמתים של 10 kA/cm² על פרוסות של 200 mm, או שתי שכבות צמתים בערמה אחת; החברים הקטנים במשפחה, בני שלוש עד שש שכבות ב-250 A/cm² עד 1 kA/cm², מייצרים את פיסות הבקרה SFQ ואת ה-DAC-שטף שעל השבב במעבדים קוונטיים מוליכי-על."
verdict: "משפחת תהליכים תעשייתית שהודגמה בחומרה קוונטית דרך מחשבי ההרפיה של D-Wave, שהקיוביטים, ה-DAC-שטף והקריאה שלהם חולקים ערמה רב-שכבתית אחת; למכונות של מודל השערים היא עדיין מתהווה — פיסות ה-SFQ שהניעו קיוביטים באו מתהליכי מחקר בני שלוש שכבות וממודול אחד של חברה, בן חמישה קיוביטים, וצמתי התהליך בני שמונה השכבות בנו מעגלים קלאסיים בלבד. לאשר בפיסת בקרה SFQ מצומת תהליך רב-שכבתי המניעה יותר מעשרים קיוביטים של מודל השערים; להוריד בדרגה את תפקידה במודל השערים אם עד 2029 לא תהיה פיסה כזו."
updated: 2026-11-22
---

SFQ = קוונט שטף בודד; RSFQ / ERSFQ = לוגיקת SFQ מהירה / מהירה וחסכונית באנרגיה; AQFP = פרמטרון שטף קוונטי אדיאבטי; QFP = פרמטרון שטף קוונטי; J_c = צפיפות הזרם הקריטי של הצומת; I_c = הזרם הקריטי של הצומת; MCM = מודול מרובה-שבבים; CMP = השטחה כימית-מכנית; DAC = ממיר ספרתי-אנלוגי; MIT LL = MIT Lincoln Laboratory; AIST = National Institute of Advanced Industrial Science and Technology (יפן); SIMIT = Shanghai Institute of Microsystem and Information Technology (Chinese Academy of Sciences); NIST = US National Institute of Standards and Technology; PECVD = שיקוע כימי מאדים בסיוע פלזמה; QPU = יחידת עיבוד קוונטית; IARPA = US Intelligence Advanced Research Projects Activity; BIS = US Bureau of Industry and Security; ECCN = מספר סיווג לפיקוח על יצוא; CMOS = מתכת–תחמוצת–מוליך למחצה משלים.

## זהות ומוצא

לוגיקה ספרתית מוליכת-על מאחסנת ביט כקוונט שטף אחד וממתגת אותו בצמתי ג'וזפסון עם נגד מקביל; התהליך שלה הוא ערמה מושטחת של שכבות חיווט מניוביום, שכבת צמתים אחת או שתיים של Nb/Al–AlOx/Nb, נגדים ותחמוצת — ההפך מן הערמה המינימלית שעליה מיוצרים רוב הקיוביטים (`fab_sc`), ניגוד שהמסמך הטכני של D-Wave מ-2026 משרטט בעצמו [C][316]. צמתי התהליך של MIT LL הם נקודת הייחוס: SFQ4ee, שמונה שכבות מוליכות-על ב-0.5 µm, ו-SFQ5ee, שמונה שכבות חיווט Nb ב-350 nm ועוד שכבת השראות קינטית מ-MoNx, כל אחד מהם עם שכבה אחת של צמתים של 10 kA/cm² (700 nm לכל הפחות) ושכבות מעגל מושטחות לחלוטין על פרוסות של 200 mm [D][953]. הקו של AIST משתרע מ-ADP2 בן תשע השכבות אל תהליך מושטח של 10 kA/cm² ושתי גרסאות בעלות J_c נמוך למעגלי ממשק לקיוביטים — 250 A/cm², וה-1KP של 1 kA/cm² מ-2025 [D][571]; לוגיקת ה-AQFP של Yokohama National University נבנתה ב-2017 בתהליך של AIST עם שתי שכבות פעילות סביב מישור הארקה אחד [D][954]. SIMIT-Nb08 (אוקטובר 2026) מכניס שתי שכבות צמתים ושני מישורי הארקה לתהליך ניוביום בן שמונה שכבות [D][955]. SEEQC, שנפרדה מ-Hypres ב-2019, היא הבעלים של מפעל ייצור רב-שכבתי מסחרי ב-Elmsford, New York [C][572]; imec ייצרה צמתים וחיווט מ-NbTiN בתוך תקציב תרמי של 420 °C של השלבים האחוריים (back-end) בקו CMOS, על פרוסות של 300 mm (דצמבר 2024) [C][956].

הקשר הקוונטי קודם לעבודה במודל השערים. ב-2010 תכנתה D-Wave תא של שמונה קיוביטים דרך מפלג SFQ על השבב ו-64 DAC-שטף שיוצרו בתהליך ארבע שכבות ה-Nb של הקיוביטים עצמם, וקראה 128 קיוביטים דרך תפסני QFP [D][957], [608]; Johnson ועמיתיו מצטטים ניסויים מוקדמים יותר של בקרת SFQ על קיוביטי שטף, שמקורותיהם לא הושגו כאן. הבקרה במודל השערים — לפי עדות המחברים המאוחרים, השערים הראשונים שהונעו ב-SFQ — החלה ב-2019 במעגל הנעה SFQ שיוצר יחד עם הקיוביט על שבב טרנסמון (שלוש שכבות Nb, כ-1 kA/cm²) [D][566], עברה ב-2023 לפיסה נפרדת שיוצרה ב-NIST Boulder (שלוש שכבות מוליכות-על, 1 kA/cm²) וחוברה בחיבור בליטות לשני טרנסמונים [D][249], והגיעה ב-2026, ב-SEEQC, למודול של חמישה קיוביטים בשיטת השבב ההפוך בטמפרטורת מיליקלווין, ששבב הנשא של ה-SFQ שלו יוצר במפעל הייצור של SEEQC עצמה, בתהליך צמתי ניוביום של 1 kA/cm² עם שכבה בעלת השראות קינטית גבוהה ועם שכבות נוספות של חיווט ניוביום ושל מישורי הארקה [D][304]. שום פיסת SFQ שהניעה קיוביט אינה מפורסמת כמוצר של צומת תהליך בן שמונה שכבות; צמתי התהליך האלה מופיעים דרך תכנונים — ספריית התאים של DigiQ, שכוילה מול SFQ5ee, וזו של QECOOL, שנבנתה על הספרייה של AIST ל-10 kA/cm² [S][958], [745].

תכונות (גרף הטכנולוגיות): זיקה לנושא 1.0, מיוצר. זמן אופייני: אין. קריאה: אין משלה. ניידות: אין. אופן הבקרה: אין; מוצריה יושבים ב-4 K או בטמפרטורת מיליקלווין. מבנה השגיאה: קוהרנטי — פיזור הזרם הקריטי וההשראות, שהמעגלים סופגים כמרווח או בכיול. ייצור: ליתוגרפיה של מוליכי-על, ניוביום רב-שכבתי על צורן של 200 mm; NbTiN על קווי CMOS של 300 mm, בפיתוח.

## פיזיקה וגבולות

ב-4.2 K צומת לוגי צריך I_c של 100–300 µA כדי שאנרגיית ג'וזפסון שלו תגמד את האנרגיה התרמית, ומכאן צמתי תהליך ספרתיים סביב 10 kA/cm²; ב-10 mK מספיק I_c ≳ 0.4 µA, ולכן AIST בחר ב-1 kA/cm² לצומת מינימלי של 10 µA [D][571]. המחיר הוא שטח המשרנים: כ-2 nH לצומת של 1 µA [D][571]. שטח המשרנים מגביל גם ב-4.2 K: SFQ5ee הוסיף שכבת השראות קינטית, ביעד של 8 pH/sq, למשרני הממתח של ~100 pH במעגלי ERSFQ [D][953]. ב-1KP, לוגיקת RSFQ מפזרת 3.2% מן ההספק של RSFQ רגילה, ומחולל פולסים לבקרת קיוביטים היה יורד מ-51.7 µW ל-1.65 µW [S][571], לעומת כ-10 µW של כושר קירור ב-10 mK, כפי שהמחברים מצטטים [D][571].

אלקטרוניקה מוליכת-על משלבת 1–10 מיליון צמתים לכל cm², לעומת יותר מ-10 מיליארד טרנזיסטורים לכל cm² ב-CMOS מתקדם, כפי שמצטטים Papanikolaou ועמיתיו [D][897]. שכבת צמתים שנייה תוקפת את גודש הניתוב: עבור אוגר הזזה מנותב של 320 תאים, בחינת הביצועים של SIMIT לאחר הניתוב (post-route) מעריכה שטח קטן ב-32.2%, תדר מרבי גבוה ב-25.0% והספק נמוך ב-65.3% לעומת תהליך ה-Nb03 שלו [S][955]. מימן המומס בניוביום מזיז את ה-I_c של הצמתים בעד כ-10% [D][953]; הצמתים הקטנים ביותר של ה-1KP מפוזרים ב-5.17% ב-4.2 K, והגדולים בפחות מ-1% [D][571].

אצל הקיוביט, התהליך קובע כמה דיסיפציה מגיעה אליו. כשיוצר על אותו שבב, מעגל ההנעה של 2019 צימד לטרנסמון 1.6(2) × 10⁻³ קוואזי-חלקיקים לכל החלקת פאזה, והחזיק שערים סביב 95% [D][566]; על פיסה נפרדת, מעבר לבליטות אינדיום, הצימוד ירד פי 43 ל-3.7(5) × 10⁻⁵, ונותרה הרעלה בתיווך פוטונים דרך אופני אנטנה בתחום הגלים המילימטריים [D][249]. תהליך בעל J_c נמוך, המותאם לטמפרטורת מיליקלווין, צפוי לקצץ את יצירת הקוואזי-חלקיקים פי 100 בקירוב, שכן הדיסיפציה לכל החלקת פאזה גדלה עם I_c [S][566].

## מצב ההנדסה העדכני

המיטב שהודגם נכון ל-22 בנובמבר 2026: ערמת מחשב ההרפיה הרב-שכבתית של D-Wave, עם 4,608 DAC-שטף מבוססי SFQ על השבב ל-512 קיוביטים על 56 קווים (2014) [D][430]; בבקרה במודל השערים — פיסת SFQ מתוצרת NIST על מודול של שני טרנסמונים, שגיאה של 1.2(1)% לקליפורד בקיוביט שנבחן בבחינת ביצועים [D][249], והמודול של SEEQC בן חמשת הקיוביטים, נאמנויות X/2 של 99.69–99.75% על פני חמשת הקיוביטים, ארבעה מהם מונעים דרך מפלג 1:4 [D][304]. הטיפוסי בקנה מידה: אף מוצר של מודל השערים אינו משתמש בפיסת בקרה SFQ.

**ציר הזמן של השיאים**

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2010-04 | מפלג SFQ ו-64 DAC-שטף לשמונה קיוביטים, בתהליך ארבע שכבות ה-Nb של הקיוביטים עצמם | D-Wave | [D][957] |
| 2014-01 | שש שכבות מתכת מוליכות-על, ערמת צמתים תלת-שכבתית אחת של 250 A/cm²; 4,608 DAC-שטף על 512 קיוביטים | D-Wave | [D][430] |
| 2015-09 | SFQ5ee: שמונה שכבות חיווט Nb ב-350 nm, 10 kA/cm², 200 mm | MIT LL | [D][953] |
| 2017-06 | AQFP בתהליך עם שתי שכבות פעילות סביב מישור הארקה אחד | AIST / Yokohama National University | [D][954] |
| 2019-01 | מעגל הנעה SFQ שיוצר יחד עם טרנסמון: שערים סביב 95% | Wisconsin / Syracuse | [D][566] |
| 2023-07 | פיסת SFQ נפרדת מתוצרת NIST על שני טרנסמונים: 1.2(1)% לקליפורד | Wisconsin / Syracuse / NIST | [D][249] |
| 2025-11 | 1KP, 1 kA/cm²: תאי RSFQ ו-AQFP ב-4.2 K לממשקי קיוביטים | AIST / Yokohama National University | [D][571] |
| 2026-03 | חמישה טרנסמונים המונעים בלוגיקת SFQ בטמפרטורת מיליקלווין ב-MCM בשיטת השבב ההפוך; שבב הנשא בתהליך ה-Nb של SEEQC ב-1 kA/cm²; X/2 של 99.69–99.75%, ארבעה קיוביטים דרך מפלג 1:4 | SEEQC | [D][304] |
| 2026-10 | SIMIT-Nb08: שתי שכבות צמתים ב-6.15 / 6.26 kA/cm²; מחלק תדר מעל 100 GHz | SIMIT | [D][955] |

איבר השגיאה השולט: במודולים של מודל השערים — הרעלת קוואזי-חלקיקים מפיסת ה-SFQ, שגיאה לא-קוהרנטית של 0.96(2)% לקליפורד ב-2023 [D][249]; בתהליך — פיזור הזרם הקריטי של הצמתים [D][953].

## ייצור, חומרים ושרשרת האספקה

ערכת הכלים של MIT LL היא קו CMOS מדור 248 nm: מערכת ריסוס רב-תאית, תחמוצת PECVD ב-150 °C, מכונת ליתוגרפיה צעדית (stepper), איכול בפלזמה ו-CMP על צורן של 200 mm [D][953]. הפיסות שהניעו קיוביטים באו מקווים קטנים יותר: פרוסות של שלושה אינץ' ב-NIST Boulder [D][249], תהליך i-line ב-Wisconsin [D][566] ומפעל הייצור של SEEQC [D][304]. ה-1KP של AIST הוא ערמה של ארבע שכבות Nb המיוצרת במתקן Qufab שלו, עם נגדי Ti/Pd/Ti, משום שהם נשארים התנגדותיים ב-10 mK — בחירה שנעשתה לראשונה בהתקני ההרפיה הקוונטית של AIST [D][571]. imec מחליפה את הניוביום ב-NbTiN כדי לגדול ל-300 mm [C][956]; הקדם-פרסום שלה מ-2023 מציע 16 שכבות NbTiN ל-400 מיליון צמתים לכל cm², כשהפיתוח עמד אז על שתי שכבות מתכת [S][959].

מפעילים: MIT LL, שה-SFQ5ee שלה משרת מתכננים חיצוניים [P][897] ושמפעל הייצור הנפרד שלה, SQUILL, מייצר מעגלי קיוביטים ליותר מ-30 קבוצות [C][570]; AIST; SIMIT; SEEQC; NIST. דוח ה-10-K של D-Wave מתאר "תהליך של מעגלים משולבים רב-שכבתיים" [G:DWAVE-FAB-10K], המופעל על קו ש-SkyWater Technology Foundry מפעילה לפי הסכם להפעלת קו מוליכים למחצה (Semiconductor Line Operation Agreement) מדצמבר 2012, שתיקונו מ-2025 קובע את גודלי אצוות הפרוסות ואת החלפות ה-CMP לכל אצווה, אך אינו נוקב בחומרים [G][960]; SkyWater שייכת ל-IonQ מאז יולי 2026 [G:IONQ-SKYWATER-2026]. שיעור תקינות: כל 64 ה-DAC-שטף בתא של D-Wave מ-2010 פעלו, בפיזור צימוד של 1.2% על פני 121 DAC-שטף זהים בשבב של 16 תאים, אך הצימודים החטיאו את התכנון בעד 30% בהיעדר מידול מדויק של השראות תלת-ממדית [D][957]. תקנת BIS מ-2024 קבעה סיווגי ECCN לאלקטרוניקה קריוגנית, למקררים ולמתקני בדיקת פרוסות [G:BIS-QUANTUM-ECCN-2024-09]. נקודות כשל יחידות: קומץ קווים רב-שכבתיים מושטחים, הידע במחסומי הצמתים, ובדיקה קריוגנית.

## בקרה, קריאה ועומס הקלט-פלט

התהליך קובע את מספר הקווים: שישה קווי מיעון ושני קווי הספק ל-64 ה-DAC-שטף של D-Wave (2010) [D][957], 56 קווים ל-4,608 DAC-שטף במיעון XYZ (2014) [D][430], ו-2√N + 2 קווים לקריאת N קיוביטים [D][608]. ה-MCM של מודל השערים מ-2023 עדיין נזקק לקו ממתח שטף, לקו ממתח SFQ ולאות הדק (trigger) לכל קיוביט [D][249]. בתקציב של שלב ה-4 K, מכ-1 W (QECOOL) ועד כמה ואטים (DigiQ), התכנון החסכוני ביותר של DigiQ מגיע ליותר מ-42,000 קיוביטים ב-10 W [S][958], יחידת מפענח של QECOOL בת 3,177 צמתים הייתה צורכת 2.78 µW ב-2 GHz ב-ERSFQ [S][745], ומודול של NISQ+ היה צורך 13.08 µW במחזור של 163 ps [S][744]. אף אחד מהם לא יוצר.

## תפקיד במחסנית

ארכיטקטורות: סריג הטרנסמונים (`sc`), משבצת 10, לצד `fab_sc` ו-`fab_cmos`, ומחשב ההרפיה על קיוביטי שטף (`anneal`), משבצת 10, לצד `fab_sc`. היא מייצרת את פיסת הבקרה SFQ של `ct_sfq` (פיסת הקיוביטים היא `fab_sc`, והזוג המחובר בחיבור בליטות — `ic_multidie`), והייתה מייצרת מפענח קריוגני SFQ (`dec_cryo`). החלופה שלה לאותה לוגיקה קרה היא `fab_cmos`, המשרתת את `ct_cryocmos`; הטכנולוגיה המשלימה אותה היא `fab_sc`. מחשב ההרפיה (`anneal`) מיוצר במשפחה זו: `fluxq`, `ct_fluxdac` ו-`ro_fluxro` של D-Wave חולקים ערמה רב-שכבתית אחת — ארבע שכבות Nb ב-2010 ושש שכבות מתכת מוליכות-על ב-2014 [D][957], [430] — ומחברי imec מונים את התהליך של D-Wave מ-2010 בין תהליכי הניוביום המתקדמים ביותר למעגלים ספרתיים [P][959]. מודול הפלוקסוניום של D-Wave מ-2026 מחבר שבב קיוביטים בערמה מינימלית לשבב בקרה רב-שכבתי מעבר למרווח של ~7 µm — החלוקה `fab_sc` + `fab_scd` במכלול אחד [C][316]. התנגשות: ערמת SFQ על פיסת הקיוביטים מרעילה את הקיוביט; פיסה נפרדת מפחיתה את ההרעלה. התרומה לשעון הנגזר: אין.

## ראיות — כיצד נמדדו המספרים

השכבות, הממדים וה-J_c של MIT LL הם יעדי תהליך; פרמטרי התהליך נעקבים על כ-3,300 מבני בדיקה בטמפרטורת החדר לכל אתר, ו-J_c על 216 צמתים לכל פרוסה [D][953]; AIST מדד 1,248 A/cm² במערכים של 1,000 צמתים ב-4.2 K, כ-20% מעל היעד [D][571]. הנתונים של SIMIT-Nb08 לקוחים מן התמצית באתר המוציא לאור; הטקסט המלא לא הושג, ולכן שמונה השכבות שלו אינן מפורטות. שגיאות שערי ה-SFQ הן ממוצעים של בחינת ביצועים אקראית (randomised benchmarking), החלק הלא-קוהרנטי בא מבחינת ביצועים של טוהר (purity benchmarking), ומספרי הקוואזי-חלקיקים — מהתאמות להתאוששות T₁ [D][566], [249]. הנאמנויות של SEEQC הן נתוני בחינת ביצועים אקראית לכל קיוביט שנמדד לבדו, לא בו-זמנית, והתהליך של שבב הנשא שלה נקוב רק בחומר המשלים (supplementary) של המאמר — צמתי ניוביום של 1 kA/cm², שכבה בעלת השראות קינטית גבוהה, חיווט ומישורי הארקה מניוביום [D][304]; מספר השכבות אינו נמסר. הקשר בין D-Wave ל-SkyWater נשען על ההסכם ועל דוח ה-10-K; אף אחד מהם אינו נוקב בניוביום. לא פורסם בחומר שנקרא: שיעור תקינות של פיסת SFQ כלשהי לבקרת קיוביטים, מספר השכבות בתהליך של SEEQC, מדידה ב-10 mK של מעגלי ה-1KP של AIST.

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הם עושים בה | ראיות |
|---|---|---|---|---|
| MIT Lincoln Laboratory | מפעל ייצור / מחקר | ארה״ב | צמתי התהליך SFQ4ee ו-SFQ5ee; מפעל ייצור נפרד לקיוביטים, SQUILL | [D][953][C][570] |
| AIST / Yokohama National University | מפעל ייצור / מחקר | יפן | תהליך של 10 kA/cm², גרסאות בעלות J_c נמוך לממשקי קיוביטים; AQFP | [D][571], [954] |
| SIMIT | מפעל ייצור / מחקר | סין | Nb03, Nb04, Nb08; שתי שכבות צמתים | [D][955] |
| SEEQC | מפתח / מפעל ייצור | ארה״ב | מפעל ייצור רב-שכבתי מסחרי; מודול SFQ של חמישה קיוביטים שיוצר בתהליך ה-Nb שלה ב-1 kA/cm² | [C][572][D][304] |
| NIST Boulder; Wisconsin–Madison; Syracuse | מחקר | ארה״ב | פיסת SFQ ובקרת קיוביטים, 2019 ו-2023 | [D][566], [249] |
| D-Wave (הקו מופעל בידי SkyWater) | מפתח | קנדה / ארה״ב | יחידות QPU של מחשבי הרפיה עם DAC-שטף מבוססי SFQ על השבב | [D][430][G][960] |
| imec | מחקר | בלגיה | אבני בניין מ-NbTiN על 300 mm | [C][956] |

**כספים.** IARPA מימנה את SFQ4ee ואת SFQ5ee עבור תוכנית Cryogenic Computing Complexity שלה [D][953], ומימנה בחלקה את ייצור מעגל ההנעה SFQ של 2023 [D][249]. Hypres השקיעה יותר מ-$100 M במפעל הייצור ובקניין הרוחני שעברו ל-SEEQC [G:SEEQC-FUNDING], שסבב A שלה גייס $22.4 M בהובלת EQT Ventures [C][572]. לא פורסם נתון לקווים של AIST, של SIMIT או של imec.

**שוק ושרשרת אספקה.** אין שוק מסחרי לפיסות SFQ לבקרת קיוביטים: MIT LL ו-AIST מפעילים קווי מחקר, SEEQC — מפעל ייצור רב-שכבתי מסחרי, SkyWater — את הקו שהיא מפעילה עבור D-Wave; המסלול של imec ל-300 mm אינו נוקב בלקוח קוונטי.

**קניין רוחני ותקנים.** לא נעשה חיפוש פטנטים לרשומה זו. ספריות התאים הן התקנים בפועל, וביניהן ספריות ה-RSFQ וה-AQFP של AIST [D][571].

**מפות דרכים ועמידה בהבטחות.** MIT LL תכננה צמתי תהליך עתידיים עם מרווח מינימלי ורוחב נגד מינימלי של 0.35 µm, ואחר כך 0.25 µm (2015) [R][953]; הצעד הבא של AIST הוא בדיקת מעגלי 1KP ב-10 mK [R][571]; מפת הדרכים של SEEQC מציבה על הפיסה בקרת שטף ספרתית וקריאה [R][53]. הישגים מתועדים: מספר ה-DAC-שטף על השבב אצל D-Wave גדל פי 72 בין 2010 ל-2014.

**פרשנות אסטרטגית.** משפחת התהליכים יושבת לצד המחשוב הקוונטי במודל השערים, לא בתוכו: קווי הקיוביטים של המובילים הם ערמות מינימליות (`fab_sc`), והדגמות הבקרה הקרה הגדולות יותר הן CMOS קריוגני (`ct_cryocmos`). מעוזה הוא מחשב ההרפיה — מחלקת המעבדים שהקיוביטים והבקרה שלה חולקים ערמה רב-שכבתית — וגרסאות ה-J_c הנמוך (SEEQC, AIST, NIST) שנבנו לבקרה בטמפרטורת מיליקלווין. אם בקרת SFQ תגדל בקנה מידה, הנכס הנדיר יהיה צומת תהליך רב-שכבתי מוסמך בעל J_c נמוך, עם תהליך בליטות התואם קיוביטים.

## תחזית ושאלות פתוחות

לאשר בתוך 12–24 חודשים אם פיסת בקרה SFQ מצומת תהליך רב-שכבתי (מסוג SFQ5ee, ה-1KP של AIST, זה של SIMIT או זה של SEEQC) תניע יותר מעשרים קיוביטים או שער דו-קיוביטי, או אם יפורסמו מעגלי 1KP של AIST שנמדדו ב-10 mK. להוריד בדרגה אם בקרת SFQ במודל השערים תישאר על חמישה קיוביטים או פחות עד סוף 2028, בעוד CMOS קריוגני תופס את משבצת הבקרה הקרה. התרחיש הטוב ביותר עד 2029: צומת תהליך בעל J_c נמוך המספק פיסות בקרה ופיסות מפענח למודול של אלף קיוביטים; התרחיש הגרוע ביותר: המשפחה שורדת במחשוב הקוונטי רק בתוך מחשבי ההרפיה של D-Wave.

שאלות פתוחות: (1) כמה שכבות מונה התהליך של SEEQC ב-1 kA/cm², ובאיזה פיזור צמתים? (2) האם צמתים של 1 kA/cm² שומרים על פיזור I_c סביב 1% ב-10 mK? (3) כמה שכבות צמתים יש בערמה הנוכחית של D-Wave, והאם היא עדיין מיוצרת ב-SkyWater תחת IonQ? (4) האם לוגיקת NbTiN על 300 mm עומדת בתקציב הקוואזי-חלקיקים של קיוביט מעבר לחיבור בליטות?

## מקורות

[53] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [C]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [arXiv:2503.09879](https://arxiv.org/abs/2503.09879). [D]
[316] D-Wave Quantum Inc., “Digital control of a high-coherence fluxonium qubit,” D-Wave Quantum Inc., Jan. 2026. [Online]. Available: https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf [C]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[566] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[570] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[571] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[572] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[608] A. J. Berkley *et al.*, “A scalable readout system for a superconducting adiabatic quantum optimization system,” *Supercond. Sci. Technol.*, vol. 23, Art. no. 105014, 2010. [arXiv:0905.0891](https://arxiv.org/abs/0905.0891). [D]
[744] A. Holmes *et al.*, “NISQ+: Boosting quantum computing power by approximating quantum error correction,” [arXiv:2004.04794](https://arxiv.org/abs/2004.04794), Apr. 2020. [S]
[745] Y. Ueno, M. Kondo, M. Tanaka, Y. Suzuki, and Y. Tabuchi, “QECOOL: On-Line Quantum Error Correction with a Superconducting Decoder for Surface Code,” arXiv, Nov. 8, 2021. [Online]. Available: https://arxiv.org/abs/2103.14209 [S]
[897] P. Papanikolaou, A. Vanasse, H. Jin, G. Tzimpragos, and J. Volk, “Duplication-aware retiming and cell interface redesign for superconductor circuit minimization,” [arXiv:2610.02333](https://arxiv.org/abs/2610.02333), Oct. 2026. [D]
[953] S. K. Tolpygo *et al.*, “Advanced Fabrication Processes for Superconducting Very Large Scale Integrated Circuits,” *IEEE Trans. Appl. Supercond.*, 2016, doi: [10.1109/TASC.2016.2519388](https://doi.org/10.1109/TASC.2016.2519388). [arXiv:1509.05081](https://arxiv.org/abs/1509.05081). [D]
[954] T. Ando *et al.*, “Three-dimensional adiabatic quantum-flux-parametron fabricated using a double-active-layered niobium process,” *Supercond. Sci. Technol.*, vol. 30, no. 7, Art. no. 075003, Jun. 2017, doi: [10.1088/1361-6668/aa6ef4](https://doi.org/10.1088/1361-6668/aa6ef4). [D]
[955] M. Chen *et al.*, “A double-active-layer Nb-based fabrication process for superconducting digital integrated circuits,” *Supercond. Sci. Technol.*, vol. 39, no. 10, Art. no. 105024, Oct. 2026, doi: [10.1088/1361-6668/aeaeb2](https://doi.org/10.1088/1361-6668/aeaeb2). [D]
[956] imec, “Imec demonstrates core building blocks of a scalable, CMOS-fab compatible superconducting digital technology,” Dec. 10, 2024. [Online]. Available: https://www.imec-int.com/en/press/imec-demonstrates-core-building-blocks-scalable-cmos-fab-compatible-superconducting-digital [C]
[957] M. W. Johnson *et al.*, “A scalable control system for a superconducting adiabatic quantum optimization processor,” *Supercond. Sci. Technol.*, vol. 23, no. 6, Art. no. 065004, Apr. 2010, doi: [10.1088/0953-2048/23/6/065004](https://doi.org/10.1088/0953-2048/23/6/065004). [arXiv:0907.3757](https://arxiv.org/abs/0907.3757). [D]
[958] M. R. Jokar *et al.*, “DigiQ: A Scalable Digital Controller for Quantum Computers Using SFQ Logic,” arXiv, Apr. 2022. [Online]. Available: https://arxiv.org/abs/2202.01407 [S]
[959] A. Herr *et al.*, “Scaling NbTiN-based ac-powered Josephson digital to 400M devices/cm²,” [arXiv:2303.16792](https://arxiv.org/abs/2303.16792), Mar. 2023. [P]
[960] SkyWater Technology Foundry, Inc.; D-Wave Systems Inc., “Fifteenth Amendment to the Semiconductor Line Operation Agreement (Exhibit 10.23 to D-Wave Quantum Inc. Form 10-K for FY2025; agreement dated 2012-12-23, amendment effective 2025-01-14),” SEC EDGAR, Feb. 26, 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1907982/000190798226000026/exhibit1023-amendment15tod.htm [G]

