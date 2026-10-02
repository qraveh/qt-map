---
id: ct_ionlaser
name: בקרת לייזר בפוטוניקה משולבת (יונים)
layer: "5 בקרה"
status: demonstrated
since: 2020
one_line: מוליכי גל על השבב מנתבים אור קירור, שער וקריאה אל יונים לכודים, ומחליפים אלומות במרחב חופשי בנתיבים אופטיים הקבועים בליתוגרפיה.
verdict: הוכחה בשבבי מעבדה (שזירה של שני יונים בנאמנות מעל 99.3%, 2020), אך לא בשום מוצר: Helios עדיין מוליך את ≥7 אורכי הגל שלו אל 8 אזורים כאלומות במרחב חופשי, ושער הלייזר הטוב ביותר בקנה מידה (7.9×10⁻⁴) מפגר בסדר גודל אחרי השער האלקטרוני ללא לייזר שעמו הוא מתחרה.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
האור לקירור, להכנת מצב, לשערים ולקריאה עובר במוליכי גל חד-אופניים המיוצרים בתוך שבב המלכודת או לצדו, ויוצא אל היון דרך מצמדי סריג עקיפה, במקום אלומות במרחב חופשי המיושרות דרך חלונות הוואקום. ETH Zürich הדגימה לוגיקה רב-יונית באור המועבר במוליכי גל, בנאמנות דו-קיוביטית של יותר מ-99.3%, באוקטובר 2020 [D][583]. אף מוצר עדיין אינו משתמש בה: Helios של Quantinuum (≥7 אורכי גל, 8 אזורים) מוליך את האור שלו כאלומות ממוקדות במרחב חופשי, המתקדמות במקביל לפני השבב [D][97], ומתחם MESA של Sandia מתכנן ובודק יחד עם Quantinuum רכיבי פוטוניקה משולבת לשילוב אפשרי בפלטפורמות עתידיות, במסגרת הסכם מו״פ שיתופי (CRADA) שבתוקף זה ארבע שנים וחודש במאי 2026 [G][501].
תכונות: אופן בקרה אופטי על נושא יוני טבעי, המועבר בתוך מערכת הוואקום; ללא ערוץ שער או ערוץ קריאה משלו.
השגיאה השולטת קוהרנטית — הפרעה הדדית, הסטות מאור תועה, רעש פאזה; הייצור הוא תהליך של מפעל ייצור למעגלים פוטוניים משולבים (SiN, BTO או ליתיום ניובט בשכבה דקה).

## פיזיקה וגבולות
הפיזיקה של השער אינה משתנה — שערי MS (מולמר–סורנסן) ושערי הסטת אור פועלים באופן זהה בין שהאלומה מגיעה ממראה ובין שהיא מגיעה ממוליך גל, ולכן זמני השער נשארים בסקאלה של מיקרו-שניות. ההספק האופטי לכל אתר מוגבל בהפסדי מוליך הגל ובנצילות המצמד, ומאחר שקצב השער גדל עם העוצמה, תקציב ההפסדים הופך לתקציב של זמן שער. אור תועה מהשכבה הפוטונית גורם להזזות שטארק AC ולחימום של אזורים שכנים — ערוץ קוהרנטי שאין בהולכה במרחב החופשי, בתמורה לסחיפת היישור שיש בה. ואילוץ החומרים המכריע הוא אורך הגל הקצר ביותר מבין אלה שבשימוש: קיוביטי ה-Ba⁺ של Helios פועלים בקווים נראים ואינפרא-אדומים (שערים ב-515 nm), אך יוני הקירור מסוג Yb⁺ שלו מקוררים ב-369 nm [D][97], שם הפסדי מוליכי הגל וההתכהות המושרית-אור חמורים ביותר, ושם נמצא אורך הגל של הלייזר המוגבל בשרשרת האספקה [P][322] — בחירת המינים, כולל מין הקירור, ויכולת השילוב הפוטוני הן החלטה אחת. הזזת הרצפה דורשת חומרי מוליכי גל שקופים לעל-סגול, מצמדים טובים יותר, ריבוב צפוף יותר ומאפננים על השבב.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג/מפתח |
|---|---|---|---|
| 2020-10 | שער דו-קיוביטי רב-יוני באור המועבר במוליכי גל > 99.3% | ETH Zürich | [D][583] |
| 2024-07 | מלכודת אלקטרונית לחלוטין בת 7 אזורים, שער דו-קיוביטי 99.97(1)%, 10 קיוביטים — ללא לייזרי שער | Oxford Ionics | [D][257][G:OXIONICS-ALLELEC-2024-07] |
| 2025-10 | שגיאת שער דו-קיוביטי אלקטרוני 8.4×10⁻⁵, ללא קירור למצב היסוד | IonQ/Oxford Ionics | [D][102] |
| 2025-11-05 | Helios: 98 Ba⁺, 8 אזורים, ≥7 אורכי גל, כולם במרחב חופשי; שער דו-קיוביטי 7.9(2)×10⁻⁴, שער חד-קיוביטי 2.5(1)×10⁻⁵, SPAM 4.8(6)×10⁻⁴ | Quantinuum | [D][97] |

ההשוואה הלא נוחה: שער הלייזר הטוב ביותר בקנה מידה עומד על 7.9×10⁻⁴, בעוד שהשער האלקטרוני ללא לייזר מגיע ל-8.4×10⁻⁵ [D][97], [102]. הפוטוניקה המשולבת מתחרה ביציבות, במספר האזורים ובאפשרות הייצור, לא בנאמנות; אף ספק אינו מפרסם מדד לשכבה הפוטונית עצמה.

## ייצור, חומרים ושרשרת האספקה
מוליכי הגל (SiN או ליתיום ניובט בשכבה דקה) מגיעים ממפעלי ייצור למעגלים פוטוניים משולבים, ושילובם יחד עם אלקטרודות המלכודת אינו מוגבל למתחם המחקר MESA של Sandia: LioniX International, מפעל ייצור פוטוני מסחרי, ייצרה את המלכודות של ETH Zürich מ-2020 עם אלקטרודות, מוליכי גל ומצמדים על שבב אחד [C][882], והשבב של MIT Lincoln Laboratory מאותה שנה הוליך את כל אורכי הגל שקיוביט Sr⁺ צריך [D][883]. מפעל המלכודות המסחרי לייצור סדרתי הוא קו Villach של Infineon (6–12 אינץ', הצמדה אנודית, אלקטרודות דור 3 מחוץ למישור), המשרת את Oxford Ionics/IonQ, eleQtron ו-Universal Quantum, בעוד ש-Honeywell מייצרת את המלכודות של Quantinuum בתוך הבית [C][320][G:INFINEON-IONTRAP-FAB-2026]. לכן Sandia היא שותפה בפיתוח התהליך, לא צוואר בקבוק באספקה: נקודות הכשל היחידות של ממש הן אספקת הלייזרים העל-סגולים (TOPTICA) ומפעל הייצור של Infineon [P][322]. שום ECCN אינו נוקב במלכודות יונים או בפוטוניקה לבקרת יונים [G][301][G:BIS-QUANTUM-ECCN-2024-09]; רק המכונה המוגמרת עשויה להיתפס, תחת 4A906, ורק כאשר מספר הקיוביטים ושגיאת ה-C-NOT שלה נופלים באותה רצועה — מ-34–99 קיוביטים ב-≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ואילך [G:BIS-3A901A-CRYOCMOS].

## בקרה, קריאה ועומס הקלט-פלט
Helios שולח כמה אלומות במרחב חופשי לכל אחד מ-8 האזורים שלו [D][97]; אותה מלכודת נושאת 1,228 אלקטרודות, ולכן הממשק החשמלי גדול כבר בסדר גודל — ההולכה האופטית אינה הקלט-פלט המגביל של היום. השהיית לולאת השער אינה משתנה — בסקאלה של מיקרו-שניות, ונקבעת בידי האינטראקציה יון–אור — ולכן הרווח הוא אמינות, לא מהירות. ב-10³ יונים, מעבר ל-8 האזורים של Helios, הולכה משולבת היא מועמדת לפלטפורמות עתידיות [G][501]; ב-10⁴ ניתוב של מספר כזה של ערוצים בעלי הפרעה הדדית נמוכה לא הוכח, ואף אחת משתי השותפויות של Sandia אינה נוקבת במספר ערוצים — שתיהן מציגות את יכולת ההגדלה כתכליתן [G][501], [584]; ב-10⁶ אין מסלול, וההספק האופטי לכל מוליך גל, לא מספר הערוצים, יהיה המגבלה.

## תפקיד במחסנית
טכנולוגיה זו היא הולכת האור החלופית של שתי ארכיטקטורות של יונים לכודים, "יונים לכודים — QCCD (הובלה בין אזורים)" (Quantinuum) ו"יונים לכודים — מלכודת פאול ליניארית עם מיעון לייזר פרטני"; היא דורשת ייצור של מעגלים פוטוניים משולבים ומזינה את שער הלייזר מולמר–סורנסן / הסטת אור. היא מחליפה את בקרת היונים במיקרוגל ובאמצעים אלקטרוניים, ומחיר המעבר אינו החלפת רכיב אלא פיצול דרכים: מערכת לייזרים שלמה מול מערכת אלקטרודות שלמה, וגאומטריית המלכודת, המין ותקציב השגיאה נגזרים מכך. IonQ מחזיקה בשני הצדדים. הטכנולוגיה חולקת את אילוץ הייצור של פלטפורמות הנושא הטבעי הזקוקות לשילוב פוטוני. ההולכה אינה נכנסת לשעון הנגזר: השער הדו-קיוביטי של Helios הוא ~70 µs, אך הסבב הוא 9.66 ms והשכבה ברוחב מלא שנמדדה ~55 ms, והם נשלטים בידי הובלה, מיון וקירור.

## ראיות — כיצד נמדדו המספרים
הנתון הדו-קיוביטי מ-2020 הוא נאמנות המצב השזור שהשער באור המועבר במוליכי גל מכין [D][583], לא שגיאת שער שנמדדה בבחינת ביצועים אקראית; השוואה זוגית מול הולכה במרחב חופשי על מלכודת אחת אפשרית, אך אף השוואה כזאת לא פורסמה. אף ספק אינו מדווח את תרומת השכבה הפוטונית להפרעה ההדדית, לחימום מאור תועה או לרעש הפאזה; המספרים של Helios הם ברמת המערכת ובהולכה במרחב חופשי [D][97], וההודעה של Sandia מאוגוסט 2026 אינה כוללת אף אחד מהם [G][501]. לא נמצא שחזור עצמאי של תוצאת ETH מ-2020. הסתייגות לקריאה: "שיא ה-QV" של AQT, 32,768, הוא 2¹⁵, לעומת 2²⁵ ב-H2 של Quantinuum — שיא בתוך קטגוריית המערכות בהרכבה במסד, בלי שנחשפו זמן שער או נאמנות [C][128][G:AQT-LYNX-QV-CONTEXT-2026].

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב/בריטניה | מפתחת עם Sandia פוטוניקה משולבת לפלטפורמות עתידיות; 8 האזורים של Helios עדיין מקבלים אלומות במרחב חופשי | [D][97], [G][501] |
| Sandia National Laboratories | מחקר | ארה״ב | MESA מתכנן ובודק פוטוניקה משולבת לפלטפורמות עתידיות של יונים לכודים; CRADA עם Quantinuum, מזכר הבנות עם IonQ | [G][501], [584] |
| IonQ | מפתח | ארה״ב | מזכר הבנות עם Sandia על פוטוניקה; בעלת Oxford Ionics ו-SkyWater | [C][19], [584] |
| Infineon Technologies | ספק | אוסטריה | מפעל מסחרי למלכודות יונים ב-Villach | [C][320] |
| TOPTICA Photonics | ספק | גרמניה | ספק הלייזרים הדומיננטי; העל-סגול הוא התשומה המוגבלת | [P][322] |

**כספים.**
2025-09-17 · IonQ · מיזוג ורכישה, Oxford Ionics (שערים אלקטרוניים) · $1.075 B · נסגר [C][G:IONQ-OXIONICS-2025]
2026-06-03 · Quantinuum · הנפקה ראשונית לציבור, Nasdaq QNT · $1.68 B ברוטו; הכנסות הרבעון השני של 2026 $8.0 M, מזומנים $2.1 B · נסגרה [C][123][G:QTM-IPO-2026-06]
2026-07-31 · IonQ · מיזוג ורכישה, SkyWater Technology (מפעל ייצור אמריקאי פנימי) · ~$1.8 B · נסגר [C][19][G:IONQ-SKYWATER-2026]
2026-08-04 · IonQ / Sandia · מזכר הבנות (MOU), תכנון משותף קוונטי לעבודות ביטחון של ארה״ב · לא נחשף · נחתם [C][584][G:IONQ-SANDIA-MOU-2026-08]

**שוק ושרשרת אספקה.** שני שווקים במעלה הזרם מזינים טכנולוגיה זו, ושניהם דלילים: ייצור PIC המשולב יחד עם אלקטרודות המלכודת, שהוצג ב-MESA, ב-MIT Lincoln Laboratory ובמפעל ייצור מסחרי אחד, LioniX, ו-PIXEurope הוא כושר הייצור היחיד בגישה פתוחה הנמצא בהקמה [G][582], ולייזרים המסוגלים לפעול בעל-סגול, שבהם שולטת TOPTICA [P][322]. לא נחשף נתון של $ ליחידה או $ לערוץ. G3 ו-G4 משלמים על הטכנולוגיה — הולכה רב-אזורית היא מה שהגדלת QCCD דורשת — ועוד G7, על החלפת יישור בשטח בשלב ייצור.

**קניין רוחני ותקנים.** לא נמצאה משפחת פטנטים מתוארכת הייחודית לפוטוניקה משולבת לבקרת יונים. ניתוח של PatSnap מ-2026 מציב את IonQ במקום הראשון בין בעלי הפטנטים ביונים לכודים, עם 9+ בקשות על טכניקות של שערים ושל גאומטריית אלומות [P][375]. לא זוהתה פעילות תקינה.

**מפות דרכים ועמידה בהבטחות.** Quantinuum: Helios (הובטח 2024-09 · ל-2025 · סופק 2025-11-05), Sol (2027, מלכודת רשת דו-ממדית, בתיקוף), Apollo (2029) [R][118]; ההתחייבות ל-QV של 10× בשנה קוימה. IonQ: 4,000 קיוביטים (הובטח ב-2020 · ל-2026 · החטאה של ~40×), 256 קיוביטים ב-99.99% נדחו למחצית הראשונה של 2027; שתי ההתחייבויות בפוטוניקה צעירות משלושה חודשים נכון ל-4 בספטמבר 2026, ואין להן תוצאה שפורסמה.

**פרשנות אסטרטגית.** היריב כאן אינו ספק פוטוניקה אחר אלא סילוק הלייזרים מהשער כליל. השער האלקטרוני מוביל בנאמנות בסדר גודל, והולכת הלייזר — במספר האזורים שהודגם; מי שיסגור ראשון את הפער שלו ייקח את הארכיטקטורה. IonQ קנתה את שני הצדדים ויכולה להמתין. Quantinuum אינה יכולה: היא מחויבת ללייזרים, והפוטוניקה המשולבת שלה מפותחת במעבדה לאומית המשרתת גם את המתחרה העיקרית שלה. חומרת היישור במרחב החופשי תוצא מהתכנון בכל מקרה; TOPTICA ו-Infineon ישמרו על כוח המיקוח שלהן בכל תרחיש.

## תחזית ושאלות פתוחות
אבני דרך (12–24 חודשים): Sol מסופק עם הולכה משולבת באזוריו וללא נסיגה בנאמנות (לאשר); Sandia או Quantinuum מפרסמות מדד של השכבה הפוטונית (לאשר); שגיאת השער הדו-קיוביטי באור המועבר במוליכי גל מגיעה לסדר הגודל של 10⁻⁴ (לאשר) — או ש-Sol מסופק על אלומות במרחב חופשי, כמו Helios (להוריד בדרגה). התרחיש הטוב ביותר ל-2029: הולכה משולבת היא ברירת המחדל בכל פלטפורמות שערי הלייזר בקנה מידה של 10³ אזורים, עם הפרעה הדדית מתחת לתקציב שגיאת השער; התרחיש הגרוע ביותר: היא נשארת בשבבי מעבדה, בעוד שהשערים האלקטרוניים לוקחים את מפת הדרכים של היונים הלכודים. פתוח: תרומת השגיאה המבודדת של השכבה הפוטונית; האם קיימת פלטפורמת מוליכי גל המתאימה לעל-סגול עבור Yb⁺; האם התהליך של MESA עובר למפעל ייצור. במעקב: אספקת Sol ב-2027, הפרסום הראשון של Sandia–IonQ.

## מקורות
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[118] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[123] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [C]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[257] C. Löschnauer *et al.*, “Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits,” *PRX Quantum*, vol. 6, no. 4, Art. no. 040313, Oct. 2025, doi: [10.1103/h4wk-v31j](https://doi.org/10.1103/h4wk-v31j). [arXiv:2407.07694](https://arxiv.org/abs/2407.07694). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[501] T. Rummler, “In the Mountain West, a quantum computing collaboration announces major results,” Sandia Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/ [G]
[582] imec, “The European Commission and Chips JU select the PIXEurope consortium to lead the European Pilot Line on Advanced Photonic Integrated Circuits,” Nov. 24, 2024. [Online]. Available: https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line [G]
[583] K. K. Mehta *et al.*, “Integrated optical multi-ion quantum logic,” *Nature*, vol. 586, no. 7830, pp. 533–537, Oct. 2020, doi: [10.1038/s41586-020-2823-6](https://doi.org/10.1038/s41586-020-2823-6). [D]
[584] IonQ, “IonQ and Sandia National Laboratories Sign MOU to Accelerate Quantum Co-Design for National Security Applications,” Aug. 4, 2026. [Online]. Available: https://www.ionq.com/news/ionq-and-sandia-national-laboratories-sign-mou-to-accelerate-quantum-co-design-for-national-security-applications [C]
[882] LioniX International, “A photonic integrated ion trap for scalable quantum computing,” Nov. 20, 2020. [Online]. Available: https://www.lionix-international.com/about-us/blog/a-photonic-integrated-ion-trap-for-scalable-quantum-computing/ [C]
[883] R. J. Niffenegger *et al.*, “Integrated multi-wavelength control of an ion qubit,” *Nature*, vol. 586, no. 7830, pp. 538–542, Oct. 2020, doi: [10.1038/s41586-020-2811-x](https://doi.org/10.1038/s41586-020-2811-x). [arXiv:2001.05052](https://arxiv.org/abs/2001.05052). [D]

## פריטי אימות פתוחים
לא נמצא נתון נאמנות, הפסד או הפרעה הדדית הייחודי לתהליך הפוטוניקה המשולבת של MESA ב-Sandia; ההודעה של Sandia מאוגוסט 2026 אינה נותנת אף אחד מהם. איזו מערכת של Quantinuum תהיה הראשונה עם הולכה משולבת — לא נמסר: ההודעה של Sandia נוקבת רק ב"פלטפורמות עתידיות", והמאמר על Helios מתאר אלומות במרחב חופשי. לא נמצאה משפחת פטנטים מתוארכת הייחודית לפוטוניקה משולבת לבקרת יונים, ושום ECCN אינו נוקב במלכודות יונים או בפוטוניקה לבקרת יונים. אם SkyWater תייצר פוטוניקה ליונים לכודים, ובאיזה לוח זמנים — לא נמסר. הטיעון בדבר אורכי הגל של Ba⁺ לעומת Yb⁺ הוא הסקה הנדסית מעובדות המין ושרשרת האספקה שבמקורות, לא טענה מצוטטת.
