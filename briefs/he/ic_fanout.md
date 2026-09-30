---
id: ic_fanout
name: פיצול אותות קריוגני למערכי ספינים (פיסת נתב, חיווט תלת-ממדי מוערם)
layer: "9 חיבור בין-מודולי"
status: emerging
since: 2025
one_line: "פיסת נתב בטמפרטורת מיליקלווין, מרבב על הפיסה או חיווט תלת-ממדי מוערם, ההופכים קווי כניסה קרים ספורים לעשרות עד אלפי מתחי השער שמערך של קיוביטי ספין צריך."
verdict: "הרכיבים קיימים — Pando Tree של Intel עם 64 הדקים, השבב המרובב של Quantum Motion עם 1,024 נקודות, מפריד הריבוב של Delft ל-648 התקנים — אך נכון ל-2026-09-26 לא פורסמה נאמנות שער שנמדדה דרך נתב בטמפרטורת מיליקלווין, ובהספק של Delft, ~1.25 µW לכל מתח שנוצר, מיליוואט של קירור בשלב המיליקלווין מחזיק ~800 מתחים: 10³ קיוביטים רק בבקרה משותפת."
updated: 2026-09-30
---

MXC = תא הערבוב, השלב הקר ביותר של המקרר; SET = טרנזיסטור חד-אלקטרוני (single-electron transistor); DRAM = זיכרון דינמי בגישה אקראית (dynamic random-access memory); FinFET = טרנזיסטור אפקט שדה בעל סנפיר (fin field-effect transistor); 22FDX = תהליך הסיליקון-על-מבודד המדולדל לחלוטין של GlobalFoundries ב-22 nm; PDK = ערכת תכנון תהליך (process design kit); חוק רנט T = t·g^p (T — מספר ההדקים, g — מספר הרכיבים, t — הדקים לרכיב, p — מעריך רנט); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
כל אלקטרודת שער של קיוביט ספין היא קו. הפיצול מנתב את הקווים המעטים שמקרר מוביל אל אלקטרודות השער האלה: פיסת נתב ב-MXC (Intel), מרבבים על פיסת הקיוביטים (Quantum Motion, Equal1), או שבב קיוביטים ואלקטרוניקת בקרה המוערמים אנכית (Hitachi). Vandersypen ועמיתיו (2017) העריכו שחיווט של ~10⁸ קיוביטים הפועלים מתחת ל-100 mK אל טמפרטורת החדר "אינו מעשי", והציבו את האלקטרוניקה לצד הקיוביטים [D][761]. Li ועמיתיו שיתפו את הקווים — "קווי הבקרה מגדירים את רשת הקיוביטים" [D][762]; Schaal ועמיתיו ו-Paquelet Wuetz ועמיתיו הציבו מתגי CMOS בטמפרטורת מיליקלווין [D][763][D][764]. Intel תיארה את Pando Tree ב-2024-06-20 [C][272]; רשומת הפיצול המתוארכת הראשונה במרשם היא מ-2025.
תכונות: חיבור סטטי; אותות בתדר נמוך בשלבי ה-mK וה-4 K; שגיאה קוהרנטית; ייצור CMOS.

## פיזיקה וגבולות
קווים. ב-2019 כל פלטפורמה חיווטה כל קיוביט ישירות, p = 1, לעומת 0.36 במעבדי ה-x86 של Intel; בדוגמה של Franke ועמיתיו כל קיוביט ספין נוסף עולה שתי אלקטרודות שער, t = 2 [D][765] — 2×10⁶ קווים ב-g = 10⁶. מערך crossbar נותן T = 6√g − 1 — כלומר 23 הדקים ל-16 נקודות [D][520], ו-~6×10³ ב-10⁶ [S]. בפסיעת שערים של 90 nm [D][197] הניתוב חייב להתבצע על הפיסה או לצידה.
חום. מקררי דילול גדולים מספקים "מעבר ל-1 mW ב-100 mK" [D][761]. Delft יצרה 96 מתחים ופירקה אותם בריבוב אל 648 התקנים ב-66 mK, בפחות מ-120 µW [D][552]: ~1.25 µW למתח, ולכן מיליוואט מחזיק ~800 מתחים — ~400 קיוביטים בחיווט ישיר או ~1.8×10⁴ נקודות crossbar [S]. עלות המיתוג ∝ C·V²·f: מיתוג מחזורי של מרבבים מסחריים ב-8 kHz העלה שלב של 50 mK ל-130 mK [D][764]. מפריד ריבוב פוקד את ההדקים בזה אחר זה, וכל הדק מחזיק בינתיים מטען — התא של Schaal אוגר אותו על אלקטרודת השער של הנקודה, כמו תא DRAM של טרנזיסטור אחד וקבל אחד [D][763] — ולכן קצב הרענון הוא פשרה בין צניחת המתח לבין החום [S].

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2020-05-19 | מרבבי CMOS מסחריים ב-50 mK: 16 ערוצים × 6 קווים | QuTech / Intel | [D][764] |
| 2023-08-28 | מערך crossbar של 16 נקודות בגרמניום, 23 הדקים | QuTech | [D][520] |
| 2024-05-01 | מתקן בדיקת פרוסות קריוגני (cryoprober) ל-300 mm: 232 מערכים של שתים-עשרה נקודות, טמפרטורת אלקטרונים 1.6 ± 0.2 K | Intel | [D][766] |
| 2024-06-20 | Pando Tree: ממתח ופולסים ל-64 הדקים, 10–20 mK | Intel | [C][272] |
| 2025-01-03 | 1,024 נקודות על מרבב אחד על השבב, 22FDX, <1 K, מופו בפחות מ-10 דקות | Quantum Motion | [D][767] |
| 2025-03-16 | Bell-1, ששמה שונה ל-RacQ ב-2026: שישה קיוביטים ובקרה במסד אחד, 0.3 K, 1,600 W | Equal1 | [C][768] [G:EQUAL1-RACQ-ESA-2026-07] |
| 2025-07 | 648 התקנים מ-96 מתחים, 66 mK, <120 µW, FinFET של 22 nm | TU Delft / Intel | [D][552] |

אף שורה אינה מדידת ביצועים של שער דרך נתב: Pando Tree חולק לוח מעגלים עם שבב Tunnel Falls [C][272], ונכון ל-2026-09-26 לא נמצאה נאמנות שנמדדה דרכו. הקרוב ביותר: שבב פולסים של 32 תאים בטמפרטורת מיליקלווין, שמחירו ~0.07% מהנאמנות החד-קיוביטית [D][551] — יצירה, לא ניתוב. האיבר השולט: החום לכל מתח ממוען.

## ייצור, חומרים ושרשרת האספקה
פיסות נתב הן CMOS של בית יציקה המופעל בקור: FinFET של 22 nm מ-Intel עבור Delft [D][552], 22FDX עבור Quantum Motion [D][767] ועבור Equal1 [C][273], ו-Intel 18A עבור ערכת תכנון התהליך הקוונטית של Hitachi, "הממשק הראשון מסוגו לתהליך ממחלקת 1.8nm" [P][769]. Tunnel Falls מיוצר בקו של 300 mm בליתוגרפיית אולטרה-סגול קיצוני [D][199]. שלושה מסלולים מתחרים: פיסת נתב נפרדת (Intel), מרבבים מונוליתיים (Quantum Motion, Equal1), ו"הערמה אנכית של שבבי קיוביטים ושל אלקטרוניקת בקרה" (Hitachi) [P][769]. בדיקת פרוסות בקור מתנה את שלושתם — מתקן בדיקת הפרוסות הקריוגני של Intel הוא המקרה שפורסם [D][766] — וקו הייצור הניסיוני SPINS של imec מוסיף הרצות של קיוביטי ספין על 300 mm, ערכות תכנון תהליך ו-CMOS קריוגני [C][770]. שיעורי התקינות של הנתבים ושל החיבורים לא פורסמו, נכון ל-2026-09-26.

## בקרה, קריאה ועומס הקלט-פלט
Pando Tree מספק "גם ממתח במתח קבוע וגם פולסי מתח מהירים לעד 64 הדקי קיוביטים" מתשעה אותות ספרתיים ומקו אחד מבקר Horse Ridge II שב-4 K [C][272]: עשרה קווים ל-32 קיוביטים, בשני הדקים לכל קיוביט (t = 2), כ-0.3 קווים לקיוביט [S]. הערך של המרשם, 0.0156 קווים לקיוביט, סופר רק את הקו האנלוגי וקורא הדקים כקיוביטים [S]. ה"כ-20 כבלים" של Intel למיליון קיוביטים [C][272] אינם מלווים בתקציב חום או רוחב פס, נכון ל-2026-09-26. גם הקריאה מתכנסת (fan-in): Diraq קוראת שמונה קיוביטים דרך שני SET [D][197]. ב-1.25 µW למתח ובשני הדקים לקיוביט [S], 10³ קיוביטים צריכים ~2.5 mW בחיווט ישיר ו-~0.2 mW ב-crossbar; 10⁶ צריכים ~2.5 W, או ~7.5 mW בקווים משותפים — רק השילוב מתקרב לתקציב של מקרר אחד.

## תפקיד במחסנית
משבצת 9 — הטכנולוגיה היחידה בשכבה 9 — של "ספינים בנקודות קוונטיות בסיליקון / גרמניום". היא **דורשת** את fab_cmos (מפעל CMOS) — "פיסת נתב CMOS בטמפרטורה קריוגנית" — ואת ct_cryocmos (בקרת CMOS קריוגנית), המייצרת את מה שהטכנולוגיה הזו מנתבת; cx_crossbar (שכבה 4) משתפת קווים בתוך המערך. לא נרשמה קשת **מספקת**. ic_mcm (מודולים מרובי-שבבים מצומדים) **מחליפה** אותה; נכון ל-2026-09-26 לאף אחת משתי ארכיטקטורות הספין אין קישור בין-מודולי. {{N_T_IC_FANOUT_MACH_CAP}} במרשם נושאות אותה ({{N_T_IC_FANOUT_PRIMARY}} כטכנולוגיה ראשית): Tunnel Falls, Hitachi × Intel 18A, RacQ (Bell-1) ו-QM-One — אלה שיצרניהן נוקבים ברכיב מוחשי. התא של Tunnel Falls מסומן ✅, על סמך מפריד הריבוב Pando Tree; האחרות מוסקות ומסומנות 🔎. הפער G-spinl9, תשובה חלקית: משבצת 9 של ארכיטקטורת הנקודות הקוונטיות מחזיקה כעת את הטכנולוגיה הזו, ה-ic_router המוצע; משבצת 9 של ארכיטקטורת הספינים הדונוריים עדיין ריקה.

## ראיות — כיצד נמדדו המספרים
מדדי הטיב — ערוצים לפיסה, חום לקו ב-MXC, צניחת מתח בהחזקה, קצב רענון, הפרעה הדדית במיתוג — אינם מופיעים באף תא של המרשם. התיעוד הוא ברמת הרכיב: המתחים המוחזקים של Delft נסחפים בקצב של 60 µV/s עד 18 mV/s [D][552], שגיאה קוהרנטית איטית שמדידת ביצועים אקראית ממצעת ומעלימה [S]; מתקן בדיקת הפרוסות הקריוגני והשבב בן 1,024 הנקודות מודדים התקנים, לא שערים [D][766][D][767]. הדף של Equal1 מציג נאמנות דו-קיוביטית ממוצעת של 99.3% [C][273], והמרשם מביא אותה לצד 98.4% מסקירה בעיתונות; אף אחד מהם אינו נוקב בפיצול שמאחוריה. חסרים, נכון ל-2026-09-26: מדידת ביצועים דרך נתב בטמפרטורת מיליקלווין, ופיזור ההספק של Pando Tree.

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Intel | מפתח | ארה״ב | הנתב Pando Tree; מתקן בדיקת פרוסות קריוגני ל-300 mm | [C][272][D][766] |
| Hitachi | מפתח | יפן | שבבי קיוביטים ובקרה בהערמה אנכית; ערכת תכנון תהליך ל-18A | [P][769] |
| Quantum Motion | מפתח | בריטניה | מרבב 1:1,024 על השבב; אריחים עם בקרה וקריאה על השבב | [D][767][C][200] |
| Equal1 | מפתח | אירלנד | קיוביטים ואלקטרוניקת בקרה ב-22FDX ב-0.3 K | [C][273] |
| TU Delft / QuTech | מחקר | הולנד | פירוק ריבוב בטמפרטורת מיליקלווין; crossbar בגרמניום | [D][552][D][520] |

**כספים.**
- 2026-01-15 · Equal1 · סבב בהובלת Ireland Strategic Investment Fund, מערכת "על שבב יחיד" · USD 60 M · הוכרז [C][771]
- 2026-03-18 · Rhonexum · סבב טרום-סיד (pre-seed) בהובלת QDNL Participations · USD 1 M · הוכרז [P][560]
- 2026-04-03 · קונסורציום בהובלת imec · קו הייצור הניסיוני SPINS, מימון משותף של EU Chips Joint Undertaking · EUR 50 M · הושק [C][770]
- 2026-05-07 · Quantum Motion · סבב C, הפיצול אינו מוזכר · USD 160 M · הוכרז [C][355]

**שוק ושרשרת אספקה.** הפיצול נקנה יחד עם פיסת הקיוביטים; הספקית העצמאית החדשה היחידה שנמצאה, Rhonexum מ-Lausanne, עומדת בשלב טרום-סיד [P][560]. התשומות הנדירות — מודלים של התקנים בקור, בדיקת פרוסות בקור, חלונות ייצור בבתי יציקה — משותפות עם ct_cryocmos. היא משרתת את G4 ואת G7 בארכיטקטורת הנקודות הקוונטיות.

**קניין רוחני ותקנים.** נכון ל-2026-09-26 אין ספירת פטנטים על פיצול ממאגר נתונים מזוהה, ואין תקן ממשק; התוצרים הקרובים ביותר הם ערכות תכנון תהליך — זו של SPINS [C][770] והערכה ל-18A שמתכננת Hitachi [P][769].

**מפות דרכים ועמידה בהבטחות.** Intel: ~20 כבלים למיליון קיוביטים, ללא תאריך [C][272]; אין נתוני קיוביטים דרך Pando Tree מאז 2024-06-20, נכון ל-2026-09-26. Hitachi: גישה בענן בשנת הכספים 2027, 100 קיוביטים בשנת הכספים 2028, 1,000 בשנת הכספים 2030 [P][769]. Diraq: 150,000 קיוביטים פיזיים עד 2029, יותר מ-2 מיליון עד 2031, הפיצול אינו מפורט [R][211]. מועדה של אף אבן דרך של פיצול טרם הגיע; עדיין אין מה להעריך.

**פרשנות אסטרטגית.** הנתב הנפרד של Intel והפיסות המונוליתיות של Equal1 ושל Quantum Motion הם הימורים יריבים על המיליוואט של שלב המיליקלווין. אם הנתבים ירדו הרבה מתחת למיקרוואט למתח, הערך יעבור לבתי יציקה בעלי מודלים של התקנים בקור ולבדיקת פרוסות בקור; אם לא, הקיוביטים יפעלו חמים יותר — Equal1 ב-0.3 K [C][768] — או יתפצלו למודולים, ו-ic_mcm תתפוס את המשבצת [S].

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 מדידת ביצועים של שער בקיוביטי ספין, שעברה ביקורת עמיתים, תרוץ דרך נתב בטמפרטורת מיליקלווין או דרך מרבב על הפיסה ותדווח על החום לכל ערוץ; להוריד בדרגה אם אב-הטיפוס של Hitachi לשנת הכספים 2028 או המערכת של Diraq ל-2029 יסופקו עם קו לכל אלקטרודת שער מ-4 K או מטמפרטורת החדר. שאלות פתוחות. (1) כמה הספק מפזר Pando Tree לכל הדק ממותג? (2) איזו צניחת מתח בהחזקה סובלים שערי חילוף בין רענון לרענון? (3) האם פולסים בריבוב בזמן מגבילים את מקביליות השערים מתחת למה שסבב של קוד המשטח צריך? (4) האם שיתוף קווים בשיטת crossbar וניתוב בטמפרטורת מיליקלווין יכולים לחלוק פיסה אחת? (5) האם מודולי ספין (ic_mcm) יתפסו את המשבצת לפני שהנתבים יגיעו ל-10⁴ ערוצים?

## מקורות
[197] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[199] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[200] Quantum Motion, “Quantum Motion Delivers the Industry's First Full-Stack Silicon CMOS Quantum Computer,” Sep. 15, 2025. [Online]. Available: https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ [C]
[211] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[272] S. Subramanian and S. Pellerano, “Intel's Millikelvin Quantum Research Control Chip Provides Denser Integration with Qubits,” Intel Community, Jun. 20, 2024. [Online]. Available: https://community.intel.com/t5/Blogs/Tech-Innovation/Data-Center/Intel-s-Millikelvin-Quantum-Research-Control-Chip-Provides/post/1608558 [C]
[273] Equal1, “UnityQ.” [Online]. Available: https://www.equal1.com/technology [C]
[355] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[520] F. Borsoi *et al.*, “Shared control of a 16 semiconductor quantum dot crossbar array,” *Nat. Nanotechnol.*, vol. 19, no. 1, pp. 21–27, Jan. 2024, doi: [10.1038/s41565-023-01491-3](https://doi.org/10.1038/s41565-023-01491-3). [D]
[551] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[552] J. van Staveren *et al.*, “Cryo-CMOS Bias-Voltage Generation and Demultiplexing at mK Temperatures for Large-Scale Arrays of Quantum Devices,” *IEEE Trans. Quantum Eng.*, vol. 6, pp. 1–18, 2025, doi: [10.1109/TQE.2025.3580377](https://doi.org/10.1109/TQE.2025.3580377). [D]
[560] M. Abdel-Kareem, “Rhonexum Raises $1M Pre-Seed to Solve the Quantum Cabling Bottleneck via Cryo-CMOS,” Quantum Computing Report, Mar. 18, 2026. [Online]. Available: https://quantumcomputingreport.com/rhonexum-raises-1m-pre-seed-to-solve-the-quantum-cabling-bottleneck-via-cryo-cmos/ [P]
[761] L. M. K. Vandersypen *et al.*, “Interfacing spin qubits in quantum dots and donors—hot, dense, and coherent,” *npj Quantum Inf.*, vol. 3, Art. no. 34, Sep. 2017, doi: [10.1038/s41534-017-0038-y](https://doi.org/10.1038/s41534-017-0038-y). [D]
[762] R. Li *et al.*, “A Crossbar Network for Silicon Quantum Dot Qubits,” *Sci. Adv.*, vol. 4, Art. no. eaar3960, 2018, doi: [10.1126/sciadv.aar3960](https://doi.org/10.1126/sciadv.aar3960). [arXiv:1711.03807](https://arxiv.org/abs/1711.03807). [D]
[763] S. Schaal *et al.*, “A CMOS dynamic random access architecture for radio-frequency readout of quantum devices,” *Nat. Electron.*, vol. 2, no. 6, pp. 236–242, Jun. 2019, doi: [10.1038/s41928-019-0259-5](https://doi.org/10.1038/s41928-019-0259-5). [arXiv:1809.03894](https://arxiv.org/abs/1809.03894). [D]
[764] B. P. Wuetz *et al.*, “Multiplexed quantum transport using commercial off-the-shelf CMOS at sub-kelvin temperatures,” *npj Quantum Inf.*, vol. 6, Art. no. 43, May 2020, doi: [10.1038/s41534-020-0274-4](https://doi.org/10.1038/s41534-020-0274-4). [D]
[765] D. P. Franke, J. S. Clarke, L. M. K. Vandersypen, and M. Veldhorst, “Rent's rule and extensibility in quantum computing,” *Microprocess. Microsyst.*, vol. 67, pp. 1–7, 2019, doi: [10.1016/j.micpro.2019.02.006](https://doi.org/10.1016/j.micpro.2019.02.006). [D]
[766] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]
[767] E. J. Thomas *et al.*, “Rapid cryogenic characterization of 1,024 integrated silicon quantum dot devices,” *Nat. Electron.*, vol. 8, no. 1, pp. 75–83, Jan. 2025, doi: [10.1038/s41928-024-01304-y](https://doi.org/10.1038/s41928-024-01304-y). [D]
[768] Equal1, “Equal1 Launches Bell-1: The First Quantum System Purpose-Built for the HPC Era,” Mar. 16, 2025. [Online]. Available: https://www.equal1.com/post/equal1-launches-bell-1-the-first-quantum-system-purpose-built-for-the-hpc-era [C]
[769] M. Rutherford, “Silicon Spin Qubits Get Foundry Path: Hitachi Banks on Intel 18A Process,” Tech Times, Jul. 28, 2026. [Online]. Available: https://www.techtimes.com/articles/321867/20260728/hitachi-intel-18a-spin-qubit.htm [P]
[770] imec, “Quantum pilot line 'SPINS' launched with EU support,” Apr. 3, 2026. [Online]. Available: https://www.imec-int.com/en/press/semiconductor-based-quantum-pilot-line-spins-launched-eu-support [C]
[771] University College Dublin, “Equal1 Announces $60 million in Funding to Accelerate Quantum Computing using Existing Semiconductor Manufacturing,” UCD Innovation, Jan. 15, 2026. [Online]. Available: https://www.ucd.ie/innovation/news-and-events/2026/equal1-announces-funding-round/ [C]

## פריטי אימות פתוחים
- "3–5 קווי שער לקיוביט" וניתוב בשכבות המתכת העליונות (back-end-of-line) של imec/Diraq, שניהם נזכרו בבקשה להכנת התקציר, לא נמצאו באף מקור שנפתח; במקומם נעשה שימוש ב-t = 2 של Franke ועמיתיו ובפסיעת השערים של 90 nm של Diraq (2026-09-26).
- דפי התמצית ב-arXiv של Vandersypen ועמיתיו (2017), Franke ועמיתיו (2019) ו-Paquelet Wuetz ועמיתיו (2020) לא החזירו מטא-נתונים, ולאחר מכן arxiv.org סירב לבקשות נוספות עם HTTP 429 (2026-09-26); עבודות אלה מצוטטות לפי DOI, ומזהי ה-arXiv שלהן לא אומתו.
- Pando Tree: המאמר מ-VLSI Symposium 2024 לא נפתח; דור התהליך, פיזור ההספק וכל נאמנות קיוביט שנמדדה דרכו אינם מופיעים בבלוג של Intel (2026-09-26).
- תוכניות הפיצול של SQC, Quobly ו-Groove Quantum: לא נמצאו בבדיקה זו; התאים שלהן במרשם נשארים 🔎 (2026-09-26).
- דף מפת הדרכים של Diraq מציג "27 באוגוסט" בלי שנה קריאה (הביבליוגרפיה של האטלס מתארכת אותו ל-2026-08-27); היעדים ל-2029 ול-2031 מצוטטים מהדף (2026-09-26).
- הרשומה של Schaal ועמיתיו נשענת על הרשומה ב-UCL Discovery ועל רישום ב-arXiv, לא על דף המוציא לאור; לא בוצע חיפוש פטנטים ייעודי לפיצול קריוגני (2026-09-26).
