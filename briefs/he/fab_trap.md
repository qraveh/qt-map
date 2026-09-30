---
id: fab_trap
name: מיקרו-ייצור של מלכודות יונים באלקטרודות משטח
layer: "10 ייצור"
status: demonstrated
since: 2006
one_line: שבבי אלקטרודות RF/DC מישוריים הכולאים יונים ומסיעים אותם, הבנויים בקווי MEMS או, יותר ויותר, על פרוסות של בתי יציקה מסחריים למוליכים למחצה.
verdict: ניתן להפרכה — אם עד סוף 2027 אף ספק לא יפרסם נתוני חימום או שיעור תקינות ברמת הפרוסה, ייצור המלכודות יישאר מלאכת יד, וסיכון לוח הזמנים של Sol/Apollo יימצא במספר האותות ובאריזה, לא בפיזיקת השערים.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
מלכודת אלקטרודות משטח פורשת את מלכודת פאול על מישור ליתוגרפי אחד — האלקטרודות זו לצד זו, והיון מוחזק עשרות מיקרומטרים מעליהן — וכך גאומטריית המלכודת הופכת לפריסת מסכה. NIST הדגים אותה ב-2006, כשהחזיק ²⁴Mg⁺ כ-40 µm מעל זהב מישורי ומדד ישירות את קצב החימום [D][806]. לצדה שורדת המלכודת התלת-ממדית בעיבוד שבבי: מלכודת Pine של AQT בנויה מארבע אלקטרודות להב ומשתי אלקטרודות קצה, בעיבוד שבבי מטיטניום מצופה זהב, על מחזיק אלומינה; הלהבים מרוחקים 0.57 mm מציר המלכודת [D][253]. זוהי השכבה שמתחת לנושא הקיוביט היוני: היא קובעת את מספר האלקטרודות, את גאומטריית האזורים והצמתים ואת כימיית פני השטח שמעליה.
תכונות: זיקת הנושא a = 0.0, טבעית — הנושא שהיא משרתת הוא היון; המלכודת עצמה מיוצרת, אך ייצור מלכודות ב-MEMS הוא ברירת המחדל של הנושאים הטבעיים, ולכן הטכנולוגיה ממוקמת במחצית הטבעית של המפה. ייצור g = ליתוגרפיית MEMS העוברת לקווי ייצור מסחריים של מוליכים למחצה בפרוסות של 6–12 אינץ' [C][320].

## פיזיקה וגבולות
הרצפה היא רעש שדה אנומלי מפני האלקטרודות, לא הרזולוציה הליתוגרפית. בגובהי יון של 30–3,000 µm הוא יורד בקירוב כ-d⁻⁴ [D][807]: הקטנת הגובה בחצי כדי לדחוס אזורים עולה ~16× בחימום. החימום הופך לשגיאת שער, שכן שערי השזירה נשענים על אופן תנועה משותף במשך עשרות עד מאות מיקרו-שניות, והוא מחייב קירור מחדש בין שלבי ההובלה. הרעש הוא שכבה של מולקולות נספחות, לא תכונה נפחית: קירור מלכודות זהב ל-6 K דיכא את החימום ב-~7 סדרי גודל [D][808]; הפצצה ביוני ארגון הפחיתה אותו פי 100 במלכודת שכבר הייתה נקייה [D][809]. מבנה השגיאה שהקוד רואה הוא קוהרנטי ומתואם — מטען תועה על מרווחים דיאלקטריים יוצר מיקרו-תנועה וסחיפת פאזה המשותפות לאזור שלם, ואלקטרודה מנותקת אחת משביתה את האזור. מה מזיז את הרצפה: אלקטרודות ניוביום, ניקוי בתוך הוואקום, דיאלקטרי ממוגן, וקריוגניקה כברירת מחדל.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2006 | ²⁴Mg⁺ ~40 µm מעל זהב מישורי; החימום נמדד לראשונה | NIST | [D][806] |
| 2012 | הפחתה של 100× ברעש השדה, ניקוי באתרו ביוני ארגון | NIST | [D][809] |
| 2025-10 | שגיאת שער דו-קיוביטי 8.4×10⁻⁵, ללא לייזר, שבב ממפעל מסחרי | Oxford Ionics | [D][102] |
| 2025-11 | 1,228 אלקטרודות, 273 אותות בלתי תלויים, 8 אזורים | Quantinuum | [D][97] |

השבב של Helios הוא המלכודת הגדולה ביותר שהוצבה בשטח; רוב הקבוצות עדיין מפעילות מלכודות בהתאמה אישית של עשרות עד ~100 אלקטרודות. איש אינו מפרסם שיעור תקינות, שיעור פגמים או עלות למלכודת, ולכן לשכבה אין מדד איכות ציבורי, והשגיאה הנמדדת נשארת נשלטת בידי חימום, מיקרו-תנועה ועומס כיול, לא בידי פגמים ליתוגרפיים.

## ייצור, חומרים ושרשרת האספקה
שתי שושלות. קווי MEMS מחקריים (מתחם MESA של Sandia, GTRI, חדרים נקיים באוניברסיטאות) מניחים זהב או ניוביום על ספיר, על סיליקה מותכת או על סיליקון מחומצן, בהיקפים של יחידות בודדות [G][501]. השינוי המתרחש כעת הוא המעבר לייצור במפעלים מסחריים: פלטפורמת Villach של Infineon מריצה פרוסות של 6–12 אינץ' עם הצמדה אנודית עבור Oxford Ionics, eleQtron [C][129], Innsbruck ו-ETH Zurich; אלקטרודות הדור השלישי שלה, מחוץ למישור, מגבירות לפי הטענה את הכליאה ~10×, ולא פורסם עבורן קצב חימום [C][320]. Honeywell מייצרת את המלכודות של Quantinuum בייצור פנימי, כולל מלכודת הרשת של Sol [R][118]; IonQ סגרה את עסקת SkyWater ב-2026-07-31, לשם תכנון, ייצור ואריזה בקווים אמריקאיים [C][19]. Infineon היא נקודת הכשל היחידה: מפעל מסחרי אחד, כמה ספקים, ואף מקור שני לא נזכר. החשיפה לפיקוח על יצוא מתונה — התקנה של BIS מ-2024-09-06 מונה מחשבים קוונטיים (4A906) ואלקטרוניקה לטמפרטורות מתחת ל-4.5 K (3A901), אך אף ECCN אינו נוקב במלכודות [G][301].

## בקרה, קריאה ועומס הקלט-פלט
המלכודת קובעת את רצפת החיווט עוד לפני שקיים קו אופטי או קו מיקרוגל כלשהו: 273 אותות בלתי תלויים עבור 98 יונים, 2.8 לקיוביט, לכליאה ולהובלה בלבד [D][97], וכל אחד מהם הוא ערוץ DAC, מסנן ומעבר ואקום. ביחס הזה 10³ יונים דורשים ~3,000 קווי DC, מעבר למספר מעברי הוואקום המעשי, ו-10⁶ אינם אפשריים בלי מיתוג מתחת למלכודת. המוצא שפורסם הוא מיתוג על השבב: WISE של Oxford Ionics מפעילה 1,000 יונים בקישוריות מלאה מ-~200 מקורות, בלי ששבב נבנה ובלי תקציב פיזור הספק [S][325].

## תפקיד במחסנית
שכבה זו נמצאת בבסיס כל שלוש ארכיטקטורות היונים הלכודים — QCCD (Quantinuum), מלכודת פאול ליניארית עם מיעון לייזר (IonQ, AQT, Quantum Art [P][125]) ושערים אלקטרוניים עם בקרה על השבב (IonQ/Oxford Ionics, eleQtron) — ומספקת את המלכודת לנושא הקיוביט, את גאומטריית הצמתים והרשת, ואת הפסים המוליכים לבקרת מיקרוגל משולבת בשבב. היא מחליפה MEMS בהתאמה אישית בייצור בבית יציקה, והמחיר משולם בהסמכה לכללי התכנון ול-UHV ובמדידה חוזרת של החימום, לא בפיזיקה. תרומתה לשעון עקיפה וגדולה: שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס, וההובלה היא 9.0 ms מתוך הסבב של 9.7 ms שנגזר עבור QCCD, לעומת שער של ~70 µs [D][97]; במדידה על H2 ההובלה לקחה בממוצע 60% מזמן המעגל [D][110] — ולכן מספר האזורים ואיכות הצמתים קונים יותר שעון ממהירות השער. אין משבצת ריקה סמוכה בגרף הטכנולוגיות.

## ראיות — כיצד נמדדו המספרים
מספרי האלקטרודות והאותות מדווחים בידי הספקים ולא עברו ביקורת. החימום מתפרסם לכל מלכודת בנקודת פעולה אחת, אף פעם לא כהתפלגות על פני פרוסה או אצווה, ואף ספק אינו חושף שיעור תקינות. השער של 8.4×10⁻⁵ הוא מדידה בשני יונים ללא קירור למצב היסוד, לא ממוצע על פני צי מכונות, ונכון ל-4 בספטמבר 2026 לא שוחזר בידי גורם חיצוני [D][102]. לא נמצאה מחלוקת מתוארכת בין ספקים על טענות ייצור.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| IonQ | מפתח | ארה״ב | בעלים של בית תכנון מלכודות ושל בית יציקה אמריקאי | [C][19] |
| Oxford Ionics | מפתח | בריטניה | שבבי מלכודות לשערים אלקטרוניים בקווי ייצור מסחריים | [D][102] |
| Infineon Technologies | ספק | אוסטריה | מפעל מסחרי למלכודות, Villach, פרוסות של 6–12 אינץ' | [C][320] |
| SkyWater Technology | ספק | ארה״ב | בית יציקה אמריקאי, שמונה התקשרויות עם חברות מחשוב קוונטי ב-2025, בבעלות IonQ מאז 2026-07-31 | [G][576][C][19] |
| Quantinuum | מפתח | ארה״ב | מפעילה בשטח את המלכודת בת 1,228 האלקטרודות; Sol בתיקוף | [D][97] |

**כספים.**
- 2025-09-17 · IonQ · מיזוג ורכישה (Oxford Ionics) · $1.075 B · — · נסגר [G:IONQ-OXIONICS-2025]
- 2026-07-31 · IonQ · מיזוג ורכישה (SkyWater) · ~$1.8 B ($15.00 במזומן + 0.4883 מניות IonQ לכל מניה) · — · נסגר [C][19][G:IONQ-SKYWATER-2026]
- 2026-02-25 · SkyWater · תוצאות שנת הכספים 2025 (שהסתיימה ב-2025-12-28) · הכנסות $442.1 M, שולי רווח גולמי GAAP של 19.7%, הכנסות מלקוחות קוונטיים +30% משנה לשנה · הוגש [G][576]
- 2025-11-06 · DARPA · QBI שלב B (IonQ ו-Quantinuum, מתוך אחת-עשרה) · ≤$15 M לכל אחת · הוכרז [G][65][G:QBI-STAGEB-2025-11]

**שוק ושרשרת אספקה.** הציוד המאפשר הוא ציוד הון רגיל של תעשיית המוליכים למחצה ועוד רכיבי UHV, ואף אחד מהם אינו מרוכז; הריכוזיות יושבת במפעל — Infineon כמפעל מסחרי, Honeywell כמפעל פנימי, Sandia למחקר בלבד, ובנוסף מזכר הבנות (MOU) לתכנון משותף בין IonQ ל-Sandia מ-2026-08-04 [C][584]. כלכלת היחידה של המלכודות אינה מפורסמת; המספר הקרוב ביותר הוא שולי הרווח הגולמי (GAAP) של SkyWater, 19.7% על הכנסות של $442.1 M בשנת הכספים 2025 [G][576]. G3 ו-G4 משלמים על שכבה זו, ו-G7 על מודולים להרכבה במסד.

**קניין רוחני ותקנים.** הסקירה של PatSnap מ-2026 מונה את משפחות הפטנטים של MIT Lincoln Laboratory למקורות מתח ולפוטוניקה המשולבים בשבב (2016, 2019) ואת האופטיקה הקריוגנית של ETH Zurich, המיוצרת באותו תהליך עם המלכודת (2020), כקניין הרוחני המרכזי של השילוב, בלי ספירה המבודדת לייצור מלכודות [P][375]. ארכיטקטורת החיווט המרכזית פורסמה ולא גודרה בפטנטים [S][325]; אין התדיינות משפטית ואין תקן קבלה.

**מפות דרכים ועמידה בהבטחות.** Quantinuum: Sol על מלכודת רשת שייצרה Honeywell (הובטח 2024-09-10 · ל-2027 · בתיקוף נכון ל-2026-09-03) [R][118]; Helios סופקה בזמן, ולכן האמינות בכל הנוגע לייצור טובה. IonQ: SkyWater (הובטח 2026-01-26 · לרבעונים השני–השלישי של 2026 · נסגר 2026-07-31) [C][19], אבל 10,000 יונים על שבב אחד ב-2027 אינם נשענים על שום נתון שפורסם על חימום או שיעור תקינות של מלכודות דו-ממדיות, ומפת הדרכים של 2020 החטיאה את היעד שלה ל-2026 ב-~40×.

**פרשנות אסטרטגית.** אם הייצור בבתי יציקה יעבוד, הגורם המבדל יעבור ממלאכת היד של המלכודות אל אלקטרוניקת הבקרה, האריזה והקודים. המנצחים: IonQ, שמסירה תלות במפעל ייצור; Quantinuum, שכבר מקבלת אספקה מייצור פנימי; Infineon, שזוכה בנפח של כל השאר. המפסידים: קווי המעבדות הלאומיות מאבדים את המונופול שלהם. איום התחליף אינו מלכודת מתחרה אלא השעון — הייצור אינו יכול לתקן זמן שכבה איטי 10³–10⁵× מזה של מוליכי-העל, אלא אם יכפיל את מספר האזורים. הכוח נמצא בידי המפעל; IonQ קנתה אחד, והיא נושאת את שולי הרווח הגולמי שלו, ~20%.

## תחזית ושאלות פתוחות
לאשר או להוריד בדרגה עד סוף 2027: האם מלכודת שיוצרה ב-SkyWater מחזיקה יונים במערכת שסופקה; האם Sol עוברת תיקוף בזמן עם 1,200+ אלקטרודות בדו-ממד; האם מישהו מפרסם שיעור תקינות או התפלגות חימום לכל פרוסה. התרחיש הטוב ביותר ל-2029: פרוסות מלכודות מסחריות עם נתוני קבלה שפורסמו, ומיתוג שמקטין פי חמישה את מספר האותות ליון. התרחיש הגרוע ביותר: מספרי האלקטרודות נתקעים סביב 10³, משום שמעברי הוואקום וערוצי ה-DAC הם החומה, וגאומטריה דו-ממדית צפופה יותר מעלה את החימום די כדי לדחות את Apollo. שאלות פתוחות: האם רשת דו-ממדית שומרת על קצב החימום של המלכודת הליניארית; האם המיתוג יכול לפעול ב-4 K בתוך תקציב פיזור הספק; האם Infineon תישאר מפעל מסחרי.

## מקורות
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[110] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828). [D]
[118] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[125] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[129] A. Cordes, “Quantum computing scale-up eleQtron secures €57 million in one of the largest Series A funding rounds worldwide,” eleQtron, May 5, 2026. [Online]. Available: https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[253] I. Pogorelov *et al.*, “Compact Ion-Trap Quantum Computing Demonstrator,” *PRX Quantum*, vol. 2, no. 2, Art. no. 020343, Jun. 2021, doi: [10.1103/PRXQuantum.2.020343](https://doi.org/10.1103/PRXQuantum.2.020343). [arXiv:2101.11390](https://arxiv.org/abs/2101.11390). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[325] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773). [S]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[501] T. Rummler, “In the Mountain West, a quantum computing collaboration announces major results,” Sandia Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/ [G]
[576] SkyWater Technology, “SkyWater Technology Reports Fourth Quarter and Full Fiscal Year 2025 Results,” U.S. Securities and Exchange Commission, Feb. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1819974/000181997426000005/skyt-20251228xex991.htm [G]
[584] IonQ, “IonQ and Sandia National Laboratories Sign MOU to Accelerate Quantum Co-Design for National Security Applications,” Aug. 4, 2026. [Online]. Available: https://www.ionq.com/news/ionq-and-sandia-national-laboratories-sign-mou-to-accelerate-quantum-co-design-for-national-security-applications [C]
[806] S. Seidelin *et al.*, “Microfabricated Surface-Electrode Ion Trap for Scalable Quantum Information Processing,” *Phys. Rev. Lett.*, vol. 96, no. 25, Art. no. 253003, Jun. 2006, doi: [10.1103/PhysRevLett.96.253003](https://doi.org/10.1103/PhysRevLett.96.253003). [arXiv:quant-ph/0601173](https://arxiv.org/abs/quant-ph/0601173). [D]
[807] M. Brownnutt, M. Kumph, P. Rabl, and R. Blatt, “Ion-trap measurements of electric-field noise near surfaces,” *Rev. Mod. Phys.*, vol. 87, no. 4, pp. 1419–1482, Dec. 2015, doi: [10.1103/RevModPhys.87.1419](https://doi.org/10.1103/RevModPhys.87.1419). [arXiv:1409.6572](https://arxiv.org/abs/1409.6572). [D]
[808] J. Labaziewicz *et al.*, “Suppression of Heating Rates in Cryogenic Surface-Electrode Ion Traps,” *Phys. Rev. Lett.*, vol. 100, no. 1, Art. no. 013001, Jan. 2008, doi: [10.1103/PhysRevLett.100.013001](https://doi.org/10.1103/PhysRevLett.100.013001). [arXiv:0706.3763](https://arxiv.org/abs/0706.3763). [D]
[809] D. A. Hite *et al.*, “100-Fold Reduction of Electric-Field Noise in an Ion Trap Cleaned with In Situ Argon-Ion-Beam Bombardment,” *Phys. Rev. Lett.*, vol. 109, no. 10, Art. no. 103001, Sep. 2012, doi: [10.1103/PhysRevLett.109.103001](https://doi.org/10.1103/PhysRevLett.109.103001). [arXiv:1112.5419](https://arxiv.org/abs/1112.5419). [D]

## פריטי אימות פתוחים
- שיעור התקינות של אלקטרודות המלכודות, שיעור הפגמים והעלות לכל מלכודת: לא פורסמו בידי IonQ, Quantinuum, Infineon, AQT או eleQtron נכון ל-2026-09-04.
- האם Infineon ייצרה את השבב המסוים שמאחורי התוצאה של 8.4×10⁻⁵: לא דף הפלטפורמה של Infineon ולא הטרום-פרסום אומרים זאת; הקשר Oxford Ionics–Infineon נטען ברמת החברה בלבד.
- לא פורסם קצב חימום לאלקטרודות מחוץ למישור מהדור השלישי של Infineon; נתון הכליאה של ~10× לא אומת במדידה.
- שחזור עצמאי של השער הדו-קיוביטי האלקטרוני של 8.4×10⁻⁵: לא נמצא נכון ל-2026-09-04.
- האם פיסת מלכודת יונים חשופה נופלת תחת ECCN 4A906 או מחוץ לקטגוריות המנויות: התקנה אינה נוקבת במלכודות, ולא נמצאה חוות דעת מייעצת של BIS.
