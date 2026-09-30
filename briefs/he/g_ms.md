---
id: g_ms
name: שער לייזר מולמר–סורנסן / הסטת אור
layer: "3 מנגנון השער"
status: demonstrated
since: 2003
one_line: כוח תלוי-ספין של לייזר דו-כרומטי, השוזר יונים לכודים דרך פאזה גאומטרית על אופן תנועה משותף, בלי להשאיר בו אכלוס.
verdict: עדיין מנגנון השזירה שביסוד כל מערכת יונים עם שערי לייזר שבהפעלה, אך זמן השער גדל עם אורך השרשרת (1.6 µs על זוג, חציון של 672 µs על 30 יונים), והרצפה שלו היא רעש הלייזר ועוד פיזור פוטונים — שני האיברים שהשערים האלקטרוניים מוחקים.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
שני תדרי לייזר המוסטים באופן סימטרי סביב פס צד תנועתי מניעים כוח תלוי-ספין; הזוג משרטט לולאה סגורה במרחב הפאזה של אופן תנודה משותף ורוכש פאזה גאומטרית שנקבעת לפי השטח הכלוא, ולכן הספינים נשזרים והתנועה חוזרת לנקודת ההתחלה שלה. הפאזה תלויה בשטח הלולאה ולא באכלוס האופן, ולכן אפיק חם נסבל — וזו הסיבה שמנגנון זה, ולא זה של Cirac–Zoller, הפך למנגנון שבשימוש בפועל. Mølmer ו-Sørensen הציעו אותו ב-1999–2000; גרסת הסטת האור, שבה שדה אחד מוסט כנגד הזזת שטארק הדיפרנציאלית, חולקת את אותו תקציב שגיאה, והיא שמתארכת את הקו שבהפעלה לסביבות 2003.
תכונות: נושא טבעי של יון לכוד; שזירה דטרמיניסטית ב-≈10⁻⁴·² s (≈63 µs) דרך אפיק תנועתי משותף.
בקרה אופטית מטמפרטורת החדר; השגיאה קוהרנטית, דליפה, פאולי; הייצור הוא הרכבה אופטית.

## פיזיקה וגבולות
משך השער נקבע לפי ההיסט δ מפס הצד הממוען — לולאה סגורה אחת אורכת 2π/δ — ואי אפשר להגדיל את δ בחופשיות, משום שתדר הפעימה חייב להתרחק מכל אופן צופה. בשרשרת של N יונים הספקטרום הצירי מצטופף, δ קטן והפולס מתארך: 1.6 µs על זוג [D][441] לעומת חציון של 672 µs על שרשרת אחת של 30 יונים [D][100], בערך 400× עבור 15× יונים. נותרות שתי רצפות. פיזור ראמאן מחוץ לתהודה אינו קוהרנטי, שום צורת פולס אינה מבטלת אותו, והוא יורד רק כשהיסט ראמאן נדחק מעבר לפיצול המבנה הדק. רעש הלייזר והחימום התנועתי משלימים את השאר: מודל פרטורבטיבי מ-2026 שוקל את צפיפות הספקטרום של הרעש בפונקציית רגישות התלויה במיקום, ומוצא שזוגות מרוחקים רגישים ~10× יותר משכנים ב-~25 kHz, בעוד שרעש של ~1 kHz עולה אי-נאמנות ברמת האחוזים ללא תלות במיקום [S][442]. השארית קוהרנטית ודמוית-דליפה, לא דה-פולריזציה, ולכן מדדי ביצועים ממוצעים מעריכים בחסר את מה שהקוד רואה.

## מצב ההנדסה העדכני
המיטב שהודגם: 99.8% ב-1.6 µs על זוג ⁴³Ca⁺, ושזירה שעדיין נוצרת ב-480 ns — פחות ממחזור תנודה תנועתי אחד (Oxford, 2018) [D][441], ועדיין שער הלייזר המהיר ביותר שפורסם. בקנה מידה, Helios רושם שגיאה של 7.9×10⁻⁴ ב-≈70 µs על פני 98 יוני Ba⁺ בשמונה אזורים [D][97]; השרשרת היחידה של IonQ בת 30 היונים, שנמדדה על כל 435 הזוגות, נותנת 550–883 µs, חציון 672 µs [D][100].

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2018 | 99.8% ב-1.6 µs; שזירה ב-480 ns | Oxford (Schäfer et al.) | [D][441] |
| 2023-08 | 550–883 µs, חציון 672 µs, שרשרת של 30 יונים | IonQ Forte | [D][100] |
| 2025-11 | שגיאה של 7.9×10⁻⁴ ב-≈70 µs, 98 יונים | Quantinuum Helios | [D][97] |
| 2026-05 | נפח קוונטי 32,768, השער לא נחשף | Alpine Quantum Technologies | [C][128] |

## ייצור, חומרים ושרשרת האספקה
דבר כאן אינו מיוצר לתוך המלכודת: השער מסופק בידי לייזרים מיוצבים, מאפננים אקוסטו-אופטיים ואלקטרו-אופטיים ואופטיקת אלומות, המכוסים כטכנולוגיה נפרדת. Helios דורש לפחות שבעה אורכי גל לעומת 1,228 אלקטרודות מלכודת [D][97] — המחצית האופטית היא רשימת הרכיבים הגדולה יותר. המלכודות, לעומת זאת, הן סחורה מסחרית (Infineon, Villach); Honeywell מייצרת את אלה של Quantinuum בתוך הבית [C][320]. החשיפה לפיקוח על יצוא היא ברמת המערכת — התקנה של BIS מ-2024-09-06 יצרה את ECCN 4A906 למחשבים קוונטיים שמעל ספי מספר קיוביטים ושיעור שגיאה, אך שום ECCN אינו נוקב במלכודות יונים או באופטיקת אלומות [G][301].

## בקרה, קריאה ועומס הקלט-פלט
שני התדרים הגלובליים אינם גדלים עם מספר היונים; המיעון הפרטני גדל, בערך ערוץ מאפנן אחד ונתיב אלומה אחד לכל יון. הפולס הוא החלק הזול של המחזור: שכבה ברוחב מלא ב-Helios אורכת ≈55 ms כשמביאים בחשבון מיון, הובלה וקירור מחדש — שלושה סדרי גודל מעל השער של 70 µs — וההובלה לבדה היוותה ~60% מזמן הריצה ב-H2 [D][97]. ב-10³ יונים, ההספק וההפרעה ההדדית מחליפים איכות מיעון במספר אזורים; ב-10⁴–10⁶, זמן שער הגדל עם אורך השרשרת מאלץ כל תכנון של אפיק יחיד להחליף תפוקה בקישוריות, ולכן כל מפת דרכים מחלקת את המלכודת.

## תפקיד במחסנית
מנגנון השזירה של שתי ארכיטקטורות של יונים לכודים — QCCD (Quantinuum) ומלכודת פאול ליניארית עם מיעון לייזר פרטני (Aria, Forte ו-Tempo של IonQ, Alpine Quantum Technologies, Qudoor, Quantum Art) — והמנגנון ההיסטורי של הקווים העוברים לבקרה אלקטרונית (IonQ עם Oxford Ionics, eleQtron). הוא דורש נושא של יון לכוד ותת-מערכת לייזר המספקת אלומות דו-כרומטיות יציבות-פאזה לזוג נבחר, ומספק את שכבת השזירה שהארכיטקטורות המחולקות לאזורים מניחות. התחליף שלו הוא השער האלקטרוני בשדה קרוב, ב-8.4×10⁻⁵ [D][102]; המעבר הופך את מערך האופטיקה להשקעה אבודה, אך מוחק את פיזור הפוטונים ואת רעש הלייזר. הוא מתנגש עם כל תכנון של אפיק יחיד. שעון נגזר בארכיטקטורת QCCD = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס ≈ 9.7 ms, מהם 9.0 ms הובלה, לעומת שכבה ברוחב מלא שנמדדה ב-~55 ms [D][97]. לא סומנה משבצת ריקה סמוכה.

## ראיות — כיצד נמדדו המספרים
המספרים הבולטים הם ממוצעי מדידת ביצועים על פני אזור או שרשרת; אף ספק אינו מפרסם שגיאה לפי זוג כפונקציה של המיקום בשרשרת, והפער של ~10× בין שכנים לזוגות מרוחקים נשאר תאוריה [S][442]. טענות נפח קוונטי דורשות אותה זהירות: ה-32,768 של AQT הוא 2¹⁵, לעומת 2²⁵ שפורסם ל-H2 בן 56 הקיוביטים של Quantinuum [C][98] — שיא בתוך קטגוריית ההרכבה במסד, לא בחזית. נכון ל-2026-09-04 אין שחזור בלתי תלוי לא ל-7.9×10⁻⁴ ולא ל-8.4×10⁻⁵.

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב-בריטניה | Helios: 98 יונים, שמונה אזורים | [D][97] |
| IonQ | מפתח | ארה״ב | שרשרת 30 היונים של Forte, 550–883 µs | [D][100] |
| Oxford Ionics (IonQ) | מפתח | בריטניה | שער אלקטרוני ללא לייזר — התחליף | [D][102] |
| Alpine Quantum Technologies | מפתח | אוסטריה | LYNX בהרכבה במסד, גרסה בעלת רגישות מופחתת לרעש | [C][128] |
| Leibniz Supercomputing Centre | משתמש | גרמניה | מערכת AQT של 20 קיוביטים, המחיר הפומבי היחיד | [C][323] |
| DARPA | מממן | ארה״ב | שלב B של QBI מממן את שתי מפות הדרכים הגדולות | [G:QBI-STAGEB-2025-11] |

**כספים.**
- 2023-12-05 · Alpine Quantum Technologies · מכירה ל-Leibniz Supercomputing Centre · ≈EUR 9.8 M, 20 קיוביטים · נסגר [C][323]
- 2025-09-04 · Quantinuum · הון מניות · USD 600 M לפי שווי של USD 10 B לפני הכסף · NVentures, Quanta, QED · נסגר [C][122]
- 2025-09-17 · IonQ · מיזוג ורכישה, Oxford Ionics · USD 1.075 B · נסגר [C][18]
- 2026-06-03 · Quantinuum · הנפקה ראשונה לציבור · USD 1.68 B ברוטו, Nasdaq QNT · נסגר [C][123]

**שוק ושרשרת אספקה.** האופטיקה משולבת בתוך הבית ב-Quantinuum וב-IonQ, ולכן לאף ספק חיצוני אין כוח תמחור; צוואר הבקבוק המסחרי היחיד בשרשרת האספקה של היונים הוא ייצור המלכודות, שהשער הזה אינו משתמש בו. Q-CTRL מוכרת כלים לאופטימיזציה של פולסים [C][443]. כלכלת היחידה: EUR 9.8 M למסד של 20 קיוביטים המוכן להפעלה ≈ EUR 0.5 M לקיוביט [C][323], המחיר היחיד של יונים לכודים שאפשר לצטט בפומבי נכון ל-2026-09-04. הכנסות הרבעון השני של 2026: USD 8.0 M ב-Quantinuum, USD 80.1 M ב-IonQ [C][123], [326]. G2 ו-G3 משלמים עליו; השכבה של ≈55 ms מנתבת את G4 למקום אחר.

**קניין רוחני ותקנים.** סקירת הנוף של PatSnap מ-2026 מונה 9+ משפחות של IonQ שהוגשו ב-JP/EP/IL בשנים 2025–2026, ובהן "universal gate pulse for two-qubit gates" (JP, 2025), ושתי בקשות תלויות ועומדות של Quantum Art (IL, KR) על ארגון מחדש של מערכי יונים [P][375] — לא הוצלבו במקור אחר. אין גוף תקינה המכסה את השער הזה.

**מפות דרכים ועמידה בהבטחות.** Quantinuum (הובטח 2024-09-10 · Helios ב-2025, Sol ב-2027, Apollo ב-2029 · Helios לפי לוח הזמנים, 2025-11-05) [R][118] — ההבטחה המתוארכת היחידה כאן שקוימה. IonQ (הובטח 2025-06-13 · 256 קיוביטים ב-99.99% ב-2026 · נדחה למחצית הראשונה של 2027); מפת הדרכים שלה מ-2020 החטיאה את יעד 4,000 הקיוביטים עד 2026 ב-~40× [R][132] — התאריכים מכווינים בלבד. AQT (הובטח 2026-05-05 · יחידות LYNX ברבעון הרביעי של 2026 · טרם הוערך) [C][128].

**פרשנות אסטרטגית.** אם שערי הלייזר יחזיקו מעמד, צוותי האופטיקה המשולבים אנכית ינצחו, ואיש לא יקנה מחשב יונים כרכיבים. אם השערים האלקטרוניים ינצחו, IonQ עם Oxford Ionics תשלוט בעקומת העלות, ו-AQT ו-Quantum Art יאבדו את הבידול האופטי שלהן. החשיפה אסימטרית: Quantinuum, הנסחרת מאז יוני 2026, היא השחקנית הוותיקה הגדולה ביותר בשערי לייזר, ו-Sol ו-Apollo עדיין מונעים בלייזר — שער ללא לייזר בקנה מידה של מוצר הוא הסיכון הטכני הגדול ביותר שלה.

## תחזית ושאלות פתוחות
ניתן להפרכה בתוך 12–24 חודשים: לאשר / להוריד בדרגה — ש-Sol יסופק ב-2027 עם שערי לייזר; שספק יפרסם שגיאה לפי זוג כפונקציה של המיקום בשרשרת; ש-AQT תחשוף את זמן השער ואת הנאמנות של LYNX בהשקה ברבעון הרביעי של 2026. התרחיש הטוב ביותר עד 2029: הנדסת פולסים וחלוקה לאזורים מחזיקות את שערי הלייזר ב-≈10⁻⁴, וההובלה עדיין קובעת את השעון. התרחיש הגרוע ביותר: השערים האלקטרוניים מגיעים ראשונים לקנה מידה של מוצר, וזה הופך למורשת. פתוח: האם הגרסה של AQT תקפה גם מעבר למעגלי נפח קוונטי; האם שגיאה המוגבלת בפיזור יכולה לרדת מתחת ל-10⁻⁴ בהספק שמיש; מה יהפוך לאילוץ ראשון ב-10⁴ יונים, ההספק או ההובלה.

## מקורות
[18] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[98] Quantinuum, “Quantum Volume.” [Online]. Available: https://www.quantinuum.com/glossary-item/quantum-volume [C]
[100] J.-S. Chen *et al.*, “Benchmarking a trapped-ion quantum computer with 30 qubits,” *Quantum*, vol. 8, Art. no. 1516, Nov. 2024, doi: [10.22331/q-2024-11-07-1516](https://doi.org/10.22331/q-2024-11-07-1516). [arXiv:2308.05071](https://arxiv.org/abs/2308.05071). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[118] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[122] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [C]
[123] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[326] IonQ, “IonQ Announces Record Second Quarter 2026 Revenues, Growing 287% YoY,” Aug. 5, 2026. [Online]. Available: https://www.ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy [C]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[441] V. M. Schäfer *et al.*, “Fast quantum logic gates with trapped-ion qubits,” *Nature*, vol. 555, no. 7694, pp. 75–78, Feb. 2018, doi: [10.1038/nature25737](https://doi.org/10.1038/nature25737). [arXiv:1709.06952](https://arxiv.org/abs/1709.06952). [D]
[442] D. V. Donchenko, E. A. Anikin, O. Lakhmanskaya, and K. Lakhmanskiy, “Mølmer-Sørensen gates in trapped-ions chains in the presence of correlated noise,” [arXiv:2606.23951](https://arxiv.org/abs/2606.23951), Jun. 2026. [S]
[443] Q-CTRL, “Learn to optimize Mølmer–Sørensen gates for trapped ions.” [Online]. Available: https://docs.q-ctrl.com/boulder-opal/toolkit/apply/trapped-ion-quantum-computing/learn-to-optimize-molmer-sorensen-gates-for-trapped-ions [C]

## פריטי אימות פתוחים
תוצאת השזירה ב-480 ns ב-[441] מצוטטת בתמצית ללא נאמנות; רק הצמד 1.6 µs / 99.8% הוא מדד טיב שלם. זמן השער והנאמנות של LYNX של AQT, שמאחורי הנפח הקוונטי של 32,768, לא נחשפו, ולכן אי אפשר לבדוק את טענת הרגישות המופחתת לרעש מול מספר פיזיקלי. נכון ל-2026-09-04 לא נמצא שחזור בלתי תלוי, שאינו של הספק, ל-7.9×10⁻⁴ של Helios או ל-8.4×10⁻⁵ של IonQ/Oxford Ionics. פער הרגישות של ~10× התלוי במיקום [442] הוא תאוריה פרטורבטיבית, לא מדידה. ספירות המשפחות של PatSnap לא הוצלבו מול מאגר פטנטים שני. הטווח 550–883 µs לקוח מהטקסט המלא של [100]; התמצית מאשרת רק את השרשרת היחידה של 30 היונים ואת מדידת הביצועים על 435 הזוגות.
