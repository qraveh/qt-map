---
id: ro_img
name: דימות פלואורסצנציה של מערכי אטומים
layer: "6 קריאה"
status: demonstrated
since: 2016
one_line: גילוי בפלואורסצנציה של אטומים ניטרליים באמצעות מצלמה — לא-הורס, באמצע המעגל, מילישנייה כברירת מחדל, מיקרושנייה בהדגמות של קבוצה יחידה.
verdict: קובעת את סבב תיקון השגיאות של האטומים הניטרליים על ~1 ms; אלא אם דימות מתחת ל-100 µs בעל אובדן נמוך יגיע לחומרה מסופקת עד 2028, היא נשארת העלות הקבועה הגדולה ביותר במחזור.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
אטום במעבר מחזורי סגור מפזר פוטונים אל אובייקטיב בעל מפתח מספרי (NA) גבוה ומשם אל מצלמה; סף של ספירת פוטונים לכל אתר מכריע על תפוסה או על מצב. סטנדרט במערכי מלקחיים אופטיים מאז 2016 בערך, והקריאה שעליה בנויה כל ארכיטקטורה של אטומים ניטרליים.
דימות פלואורסצנציה במצלמה, ~0.5–1 ms, לא-הורס, ניתן לביצוע באמצע המעגל.
בקרה אופטית בטמפרטורת החדר; אופטיקה של שולחן במרחב חופשי; מבנה השגיאה הוא אובדן.

## פיזיקה וגבולות
האות הוא הזווית המרחבית של האיסוף כפול הנצילות הקוונטית כפול קצב הפיזור כפול זמן האינטגרציה, ושגיאת הסף יורדת מעריכית במספר הפוטונים שנאספו: ההבחנה זולה. המחיר הוא הרתיעה: כל פוטון מפוזר מחמם את האטום, ומעבר לכמה אלפים הוא עוזב את המלכודת, ולכן אופן הכשל הוא אובדן — היפוך ביט של 0.46% לעומת אובדן של 0.24% ב-448 אטומים [D][4]. בדיקות קצרות יותר משפרות את ההישרדות: שתי תוצאות המיקרושנייה מ-2026 מדווחות על אובדן הנמוך בסדר גודל מקו הבסיס של המילישנייה. המפתח המספרי והנצילות הקוונטית יושבים קרוב לתקרתם המעשית, ומה שנותר הוא קירור מחדש במהלך הבדיקה, מעברים בהירים יותר ואזורים מקבילים. ארכיטקטונית, הסבב הוא שחשוב: שערי CZ אורכים 270 ns בעוד סבב תיקון שגיאות אורך 1–4.5 ms, הדימות 0.5–1 ms ממנו וההובלה את השאר [D][4].

## מצב ההנדסה העדכני
| תאריך | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2025-11 | 0.5–1 ms, היפוך ביט 0.46%, אובדן 0.24%, מערך סובלני לתקלות של 448 אטומים | Harvard/MIT/QuEra | [D][4] |
| 2026-08 | 17.6 µs, הבחנה 99.89(5)%, הישרדות 98.80(44)%, ¹⁷⁴Yb חסר ספין | Kyoto/Yaqumo | [P][261] |
| 2026-08 | בדיקה של 15 µs על תת-מערך של 25 אתרים, אי-נאמנות 4.1×10⁻⁵, אובדן 2.1×10⁻⁴ | USTC | [P][623] |

השגיאה השולטת: אובדן מושרה-דימות, לא שיוך שגוי.

## ייצור, חומרים ושרשרת האספקה
ללא ייצור: אובייקטיב, מראות דיכרואיות ומצלמה על שולחן. ה-qCMOS מסוג ORCA-Quest של Hamamatsu הוא החיישן הנקוב לאורך כל קו Harvard/QuEra, ללא מקור שני ברגישות זו [P][329]; האובייקטיבים הם אופטיקת מיקרוסקופ סחורתית. הדימות יושב בתוך מחזור תיקון השגיאות, ולכן עלותה היא לכל סבב, לא לכל הרצה. ב-10³ אטומים תמונה אחת מכסה את המערך; ב-10⁴–10⁶ מספר הפיקסלים, קצב התמונות והספק ההארה כופים אזורים מקבילים עם מצלמה לכל אחד — המשטר שבו גם היגוי האלומות חדל להתרחב בהתקן יחיד: מסיט מבחין במספר נקודות השווה למכפלת רוחב הפס שלו בתדר הרדיו בזמן מעבר הגל האקוסטי דרך האלומה, ואותו זמן מגביל את מהירות ההכוונה מחדש של מלכודת, ואילו מאפנני גביש נוזלי מחליפים תמונה רק בקצב של עשרות הרץ. החשיפה לפיקוח על יצוא עקיפה: 4A906 כובל את המכונה רק כאשר מספר הקיוביטים ושגיאת ה-C-NOT שלה נופלים באותה רצועה, מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך [G:BIS-3A901A-CRYOCMOS]; שום דבר אינו נוקב באופטיקת מלקחיים או במצלמות [G][301].

## תפקיד במחסנית
היא הקריאה של שלוש ארכיטקטורות האטומים הניטרליים: מערכי מלקחיים אופטיים רידברג של אלקליים (Rb/Cs) ושל אלקליים-עפרוריים (Yb/Sr) והסימולטור האנלוגי של אטומים ניטרליים. דורשת אטום אלקלי או אלקלי-עפרורי עם מעבר מחזורי; מספקת את המדידה הלא-הורסת באמצע המעגל שפענוח בזמן אמת צריך, והופכת אובדן אטום למחיקה ניתנת לגילוי, לא לשגיאת פאולי שקטה. שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס ≈ 1.3×10⁻³ s, ההובלה ראשונה והקריאה הזאת שנייה ב-501 µs, לא השער של 270 ns — פי ~10³ מסבב של מוליכי-על. אימות: שתי תוצאות המיקרושנייה הן של קבוצה יחידה ושל מין יחיד; זו של Kyoto משתמשת ב-¹⁷⁴Yb חסר ספין, ולכן היא מבססת הבחנת תפוסה, לא קריאה של מצב על-דק, וה-15 µs של USTC ממוצע על פני תת-מערך של 25 אתרים. אף אחת מהן לא רצה בתוך זיכרון לוגי.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Harvard/MIT | מחקר | ארה״ב | קו הבסיס הסובלני לתקלות של 448 אטומים | [D][4] |
| QuEra Computing | מפתח | ארה״ב | מספקת קריאה זו במפת הדרכים שלה | [C][153] |
| Atom Computing | מפתח | ארה״ב | מערכי Yb; Magne עם Microsoft | [C][154] |
| Kyoto Univ./Yaqumo | מחקר | יפן | הדגמת דימות Yb ב-17.6 µs | [P][261] |
| Hamamatsu Photonics | ספק | יפן | חיישן qCMOS, ללא מקור שני | [P][329] |

**כספים.** 2025-09-09 · QuEra · סבב B · $230 M+ USD · Google, SoftBank VF2, NVentures [C][153]. 2025-11-06 · DARPA · שלב B של QBI · ≤$15 M לכל אחת · Atom ו-QuEra בין אחת-עשרה [G][65]. 2026-02 · Infleqtion · רישום למסחר ב-NYSE · >$550 M USD, ועוד מכתב כוונות של DoC על $100 M [C][155]. 2026-06 · Atom Computing · גיוס · $300 M+ USD כולל מכתב כוונות של Commerce על $100 M [C][154]. 2026 · QuNorth · הזמנת Magne, 50 לוגיים · €80 M · Atom/Microsoft [P][12].

**שוק ושרשרת אספקה.** חיישן של ספק אחד יושב בנתיב הקריטי של כל מערך מוביל, והשאר אופטיקה סחורתית — סיכון ריכוזיות חד. היא משלמת אל G3 ו-G4: אין דימות באמצע המעגל, אין פענוח בזמן אמת.

**קניין רוחני ותקנים.** אין משפחת פטנטים מתוארכת או תקן הייחודיים לדימות מערכי אטומים.

**מפות דרכים ועמידה בהבטחות.** (2026-08 · דימות מהיר הוצג בנפרד · לא שולב בריצה לוגית); (2028–29 · יעדי Libra של QuEra ו-Magne · מניחים שהמחזור ממשיך להתכווץ) [R][153]. מפות הדרכים של הספקים מגלמות האצה שהוצגה רק על תת-מערכים.

**פרשנות אסטרטגית.** מי שיספק ראשון דימות מתחת ל-100 µs בעל אובדן נמוך יקריס את העלות הקבועה הגדולה ביותר במחזור האטומים הניטרליים וירוויח פי כמה בשעון האפקטיבי, החולשה המבנית האחת של הפלטפורמה. ספקי המצלמות מחזיקים מנוף גדול מכפי שהכנסותיהם מרמזות; לספקי האטומים אין עליהם שום מנוף.

## תחזית ושאלות פתוחות
לאשר אם תוצאת מיקרושנייה תשולב בריצת זיכרון לוגי עד 2028; להוריד בדרגה אם תישאר קריאה בלבד. התרחיש הטוב ביותר ל-2029: דימות מתחת ל-50 µs הוא סטנדרט וסבבי תיקון השגיאות יורדים מתחת ל-0.5 ms. התרחיש הגרוע ביותר: דימות מילישנייה נשאר ברירת המחדל ומגביל את המחזור סביב 1 ms. פתוח: האם דימות מהיר מחזיק על פני מערך מלא, והאם הוא משנה את התמהיל אובדן-לעומת-פאולי שהמפענחים מניחים?

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[12] M. Abdel-Kareem, “Denmark's QuNorth to Acquire 50-Logical-Qubit Magne Quantum Computer from Atom Computing and Microsoft,” Quantum Computing Report, Jul. 17, 2025. [Online]. Available: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ [P]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[153] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[155] L. Roady, “Infleqtion Becomes First Neutral-Atom Quantum Company to Go Public,” Infleqtion, Feb. 17, 2026. [Online]. Available: https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [C]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[329] M. Ivezic, “The Tweezer Array's Hidden Supply Chain: Who Really Wins If Neutral-Atom Quantum Computing Wins,” PostQuantum.com, Nov. 17, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/neutral-atom-quantum-ecosystem/ [P]
[623] Xu-Zhao-Qiu Zeng *et al.*, “Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor,” [arXiv:2608.17189](https://arxiv.org/abs/2608.17189), Aug. 2026. [P]

## פריטי אימות פתוחים
תוצאת ה-17.6 µs של Kyoto/Yaqumo היא על ¹⁷⁴Yb חסר ספין, שאין לו קיוביט על-דק — הבחנת תפוסה, לא קריאת מצב; לא נמצא שחזור בלתי תלוי. ה-15 µs של USTC הוא זמן בדיקה ממוצע על פני תת-מערך של 25 אתרים; הנתון המקביל למערך מלא של 100 אתרים אינו מצוין. המצלמה ששימשה בהדגמה של Kyoto אינה מזוהה במקורות שנמצאו, ולכן לא נעשה לה ייחוס חיישן. אין עלות ליחידה הניתנת לציטוט לערוץ קריאה של מצלמה ועוד אובייקטיב. הזמנת Magne של QuNorth ב-€80 M מקורה בעיתונות המקצועית; לא נמצאה הודעה של הספק.
