---
id: cx_qccd
name: הסעת יונים (QCCD, צמתים, מלכודות רשת)
layer: "4 קישוריות והובלה"
status: demonstrated
since: 2002
one_line: הזזת יונים לכודים בין אזורים דרך צמתים או מלכודות רשת, כך שגביש קטן שאפשר להפעיל עליו שערים יורש קישוריות של כל-לכל.
verdict: מיון, פיצול וקירור מחדש — לא ההזזה ולא השער — קובעים את שעון היונים (~55 ms לשכבה ברוחב מלא ב-Helios). בלי קיצוץ של 10x עד 2028, QCCD של יונים יישאר בעל נאמנות גבוהה ותפוקה נמוכה.
updated: 2026-09-04
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
QCCD, שהוצע בידי Kielpinski, Monroe ו-Wineland ב-2002 [D][499], מחלק את האוגר לאזורים ומשתמש במתחי אלקטרודות משתנים בזמן כדי להזיז יונים בין אזורי זיכרון לאזורי אינטראקציה, כך שאף שרשרת אינה צריכה להיות גם ארוכה וגם כזאת שאפשר להפעיל עליה שערים — ניתוב הנקנה בשטח מלכודת. צמתים הופכים אותו לדו-ממדי; מלכודות רשת מחליפות את מקומות היונים כמו בפאזל של אריחים מחליקים.

ניידות וזמן: הנושא עצמו נע, ב-1.7–4 m/s שנמדדו [D][114], [117], ולכן הקישוריות היא לוח זמנים, לא מפת מצמדים; הזזה ועוד קירור מחדש ~2 ms, ושאלת הדטרמיניזם של השזירה אינה ישימה. שגיאה וייצור: עירור תנועתי קוהרנטי ועוד אובדן יונים, הנראים כאי-נאמנות דו-קיוביטית מוגברת וכדליפה; שבבי אלקטרודות משטח ברמת MEMS המופעלים בצורות גל DC.

## פיזיקה וגבולות
שינוי הדרגתי של מתחי מקטעים שכנים גורר באר פוטנציאל, ואת היון שבה, לאורך הציר — וההזזה אינה חייבת להיות איטית: ב-NIST הוזז ⁹Be⁺ לאורך 370 µm ב-8 µs, כשהעירור מגיע לשיא של 1.6 קוונטים וחוזר ל-0.2 בזכות תכנון צורת הגל [D][500]. לכן העלות ברמת המילישניות אינה ההזזה עצמה, אלא פיצול גבישים ואיחודם מחדש (שני יונים שפוצלו ב-55 µs שמרו ~2 קוונטים כל אחד [D][500]) וקירור פס הצד המשקם את אופני השער.

בצומת, האפס של שדה ה-RF אינו רציף: היון חוצה גבשושית בפסאודו-פוטנציאל עם מיקרו-תנועה עודפת, והיא שקובעת את מהירות המעבר ואת החימום. מתחת לכך נמצא החימום האנומלי מרעש פני האלקטרודות, החריף ככל שהיון מתקרב לפני השטח, ולכן כליאה הדוקה יותר אינה יכולה לקנות אדיאבטיות. מה שמזיז את הרצפה הוא שער הסובל גביש חם: השער האלקטרוני הגיע לשגיאה של 8.4×10⁻⁵ ללא קירור למצב היסוד [D][102], ומוחק את איבר הקירור מחדש במקום לכווץ אותו.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2022-06 | הלוך ושוב דרך צומת X, ממוצע 4 m/s, 0.013(1)–0.030(2) קוונטים | Quantinuum | [D][114] |
| 2023-02 | קישור חומר משבב לשבב, 2,424 העברות/s, אי-נאמנות של אובדן < 7×10⁻⁸ | Universal Quantum | [D][117] |
| 2024-03 | החלפת יונים במלכודת רשת ב-2.5 kHz | Quantinuum | [D][113] |
| 2025-11 | 55 ms לשכבה ברוחב מלא, 98 יונים, 8 אזורים | Quantinuum | [D][97] |

הפער בין הפרימיטיב למוצר הוא הממצא: שער דו-קיוביטי ב-Helios אורך ~70 µs לעומת ~55 ms לשכבה, וב-H2 ההובלה היוותה ~60% מזמן הריצה [D][97], [110]. האיבר השולט הוא לוח הזמנים — מיון, פיצול/איחוד, קירור מחדש, ביצוע סדרתי על פני שמונה אזורים.

## ייצור, חומרים ושרשרת האספקה
המלכודות הן שבבים של אלקטרודות מקוטעות. Honeywell היא המפעל הפנימי של Quantinuum, והיא שייצרה את שבב הרשת הדו-ממדי של Sol, הנמצא בתיקוף נכון לרבעון השני של 2026 [C][124]. Infineon Villach היא הקו המסחרי — פרוסות של 6–12 אינץ', אלקטרודות מחוץ למישור מהדור השלישי, שלפי הטענה מגבירות את הכליאה ~10× — המשרת בו-זמנית את Oxford Ionics, eleQtron, Innsbruck ו-ETH [C][320]. IonQ שברה את הדואופול הזה ברכישת SkyWater תמורת ~$1.8 B, שנסגרה ב-2026-07-31: ספקית היונים הראשונה המחזיקה בייצור משלה [G][19]. MESA של Sandia נשאר מחקרי בלבד [G][501]. אין נתון פומבי על שיעור תקינות; המחיר היחיד הוא EUR 9.8 M למערכת של 20 קיוביטים של AQT המוכנה להפעלה, ≈ EUR 0.5 M לקיוביט [C][323]. נקודות כשל יחידות: הקו היחיד של Infineon, ולייזרי UV, שבהם שולטת TOPTICA ושבהם ה-369 nm עבור Yb⁺ מוגבל [P][322]. אף ECCN אינו נוקב במלכודות יונים, אך מכונה מוגמרת נופלת תחת 4A906, בתוקף מ-2024-09-06 [G][301].

## בקרה, קריאה ועומס הקלט-פלט
הזזה היא צורת גל DC מסונכרנת על פני עשרות אלקטרודות בקצב עדכון של µs, ולאחריה קירור, ובשערי לייזר — גם מיעון מחדש של האלומות. Helios נושא 1,228 אלקטרודות עבור 98 יונים [D][97]: מספר האלקטרודות הוא מה שגדל, והעדכונים נכנסים בשלושה סדרי גודל בתוך השכבה של 55 ms, ולכן האלקטרוניקה אינה הקיר. ב-10³ יונים מדובר ב-~10⁴ ערוצי DC מסוננים, ש-Oxford Ionics הייתה מצמצמת ל-~200 מקורות חיצוניים בהצבת אלקטרוניקת מיתוג על השבב — מחקר תכנון, שום שבב לא נבנה [S][325]. ב-10⁴–10⁶ האילוץ הוא ניתוב אור הקירור ואור השערים לאזורים רבים בבת אחת (Helios צריך ≥7 אורכי גל): אף מערכת אינה מפעילה יותר מכמה עשרות אזורים בו-זמנית.

## תפקיד במחסנית
ההסעה משרתת שתיים משלוש הארכיטקטורות של יונים לכודים — QCCD (Quantinuum), שבה היא הטכנולוגיה הראשית, ובקרה אלקטרונית של הקיוביט (IonQ/Oxford Ionics, eleQtron), שבה היא החלופית — ומספקת את הקישוריות בין כל זוג שרירותי שזיכרונות qLDPC מסוג bivariate bicycle וקודים טרנסוורסליים בעלי קצב גבוה מניחים: ההדגמה של Quantinuum עם [[80,48,4]] משלמת עליה בהובלה, בעוד שנקודת האיזון של IonQ עם qLDPC הושגה על שרשרת סטטית של 40 יונים, בלעדיה. היא מחליפה את השרשרת הארוכה הסטטית, שספקטרום האופנים שלה מצטופף ככל שמוסיפים יונים; המחיר הוא שהקישוריות הופכת לתזמון, והשעון עובר מהשער אל ההזזה — שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס ≈ 9.7 ms, מהם 9.0 ms הובלה, לעומת שכבה ברוחב מלא שנמדדה ב-~55 ms [D][97]. משבצת ריקה סמוכה: יותר משני מודולים מקושרים — הקישור בין שני מודולים קיים [D][117], שום דבר גדול יותר.

## ראיות — כיצד נמדדו המספרים
להובלה אין מדד ביצועים עצמאי. מסיקים אותה מתרמומטריית פסי צד סביב הזזה — הנתונים של 0.013(1)–0.030(2) קוונטים [D][114] — ומנאמנות דו-קיוביטית לאחר רצף הובלה, המקפלת את ההובלה לתוך שגיאת השער. אף אחת מהן אינה לוכדת חימום מצטבר לאורך מעגל עמוק, אובדן בצמתים בקנה מידה, או הפרעה הדדית בין אזורים. השכבה של 55 ms וקצב ההחלפה של 2.5 kHz מדווחים בידי הספק ולא שוחזרו מבחוץ נכון ל-2026-09-04; הנפח הקוונטי של AQT, 32,768, אינו מדידת הובלה ואינו חושף שום תזמון [C][128].

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים כאן | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב/בריטניה | QCCD עם צומת טבעתי, מלכודת רשת ל-Sol | [D][97] |
| Honeywell | ספק | ארה״ב | מפעל פנימי, ייצר את השבב של Sol | [C][124] |
| IonQ | מפתח | ארה״ב | מלכודות עם צמתים, בעלת SkyWater | [G][19] |
| Infineon | ספק | אוסטריה | מפעל ייצור מסחרי למלכודות, דור 3 | [C][320] |
| Universal Quantum | מפתח | בריטניה | קישור החומר היחיד משבב לשבב | [D][117] |
| AQT | מפתח | אוסטריה | מודול LYNX, יחידות ברבעון הרביעי של 2026; הארכיטקטורה לא נחשפה | [C][128] |
| Quantum Art | מפתח | ישראל | ארגון מחדש אופטי של מערכי יונים | [P][125] |

**כספים.** 2022-11-02 · Universal Quantum · חוזה DLR · EUR 67 M · לא סופק [P][328]. 2025-09-04 · Quantinuum · סבב · $600 M לפי שווי של $10 B לפני הכסף · NVentures, Quanta, QED, JPMorgan · נסגר [G][122]. 2025-11-06 · Quantinuum ו-IonQ · שלב B של QBI · ≤$15 M לכל אחת · פעיל [G:QBI-STAGEB-2025-11]. 2026-05-05 · eleQtron · סבב A · EUR 57 M [G][129]. 2026-06-03 · Quantinuum · הנפקה ראשונית לציבור · $1.68 B ברוטו, Nasdaq QNT, מזומנים $2.1 B [G][124]. 2026-07-31 · IonQ · מיזוג ורכישה, SkyWater · ~$1.8 B, אחרי Oxford Ionics תמורת $1.075 B [G][18], [19].

**שוק ושרשרת אספקה.** ייצור המלכודות היה קו פנימי אחד ועוד קו מסחרי אחד; SkyWater מוסיפה קו שלישי משולב אנכית — האירוע המשמעותי ביותר של השנה בשרשרת האספקה [C][320][G][19]. לייזרי ה-UV נשארים צוואר הבקבוק הקשה יותר [P][322]. G2 משלם על ההסעה, והיא תנאי מוקדם ל-G3 ול-G4.

**קניין רוחני ותקנים.** לא פורסמה ספירת משפחות פטנטים ייחודית להסעה. הקרוב ביותר המתוארך: IonQ הגישה 9+ משפחות של יונים לכודים ב-JP/EP/IL בשנים 2025–26; ל-Quantum Art שני פטנטים תלויים ועומדים ב-IL/KR על ארגון מחדש אופטי של מערכי יונים [P][375]. אין מחסנית תוכנה בקוד פתוח להסעה.

**מפות דרכים ועמידה בהבטחות.** Quantinuum: Helios (הובטח 2024-09-10, הושק 2025-11-05 — קוים); Sol (2027, השבב בתיקוף ברבעון השני של 2026 — לפי התוכנית); Apollo (2029 — טרם הוערך) [R][118][C][124]; אמינה. IonQ: 10,000 פיזיים על שבב אחד עד 2027, 2 M עד 2030, ללא נתוני חימום או הובלה שפורסמו למלכודת דו-ממדית, ומפת דרכים מ-2020 שהחטיאה את 4,000 הקיוביטים ב-~40× — כוונה, לא תוכנית [R][132]. Universal Quantum לא סיפקה דבר מאז 2022 [P][502].

**פרשנות אסטרטגית.** קיצוץ של זמן השכבה ב-10× יאפשר ליונים להמיר יתרון בנאמנות לסבילות לתקלות תחרותית בתפוקה; כישלון — והם יזכו בכותרות על קיוביטים לוגיים אך יפסידו בריצות לשנייה. המנצחות בכל מקרה: Infineon ו-Honeywell, המוכרות את המשאב הנדיר. איום התחליף: מלקחיים אופטיים של אטומים ניטרליים ומצמדים לטווח ארוך במוליכי-על — קישוריות ללא הובלה.

## תחזית ושאלות פתוחות
לאשר/להוריד בדרגה בתוך 12–24 חודשים: Sol יסופק ב-2027 עם זמן לשכבה שפורסם; ספק כלשהו יפרסם שכבה ברוחב מלא מתחת ל-10 ms; Universal Quantum תקשר יותר משני מודולים. התרחיש הטוב ביותר ל-2029: שכבות של פחות מ-10 ms מביאות את השעון הלוגי של היונים לטווח של ~10× ממוליכי-העל. התרחיש הגרוע ביותר: זמן השכבה נשאר בטווח של 2× מ-55 ms, והיונים נשארים פלטפורמה שמדגימה קודים ולא מריצה אלגוריתמים. פתוח: האם החימום האנומלי יכפה מלכודות קריוגניות ב-10⁴ יונים; האם אפשר להפוך פיצול/איחוד לנקיים מעירור קוונטים בבקרה אופטימלית; האם שערים הסובלים גביש חם מוחקים את הקירור מחדש; האם יופיע מפעל מסחרי שני. לעקוב: התיקוף של Sol, כושר הייצור של Infineon, המלכודת הראשונה של IonQ מ-SkyWater.

## מקורות
[18] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [G]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[110] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828). [D]
[113] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756). [D]
[114] W. C. Burton, B. Estey, I. M. Hoffman, A. R. Perry, C. Volin, and G. Price, “Transport of multispecies ion crystals through a junction in an RF Paul trap,” *Phys. Rev. Lett.*, vol. 130, Art. no. 173202, Apr. 2023, doi: [10.1103/PhysRevLett.130.173202](https://doi.org/10.1103/PhysRevLett.130.173202). [arXiv:2206.11888](https://arxiv.org/abs/2206.11888). [D]
[117] M. Akhtar *et al.*, “A high-fidelity quantum matter-link between ion-trap microchip modules,” *Nat. Commun.*, vol. 14, no. 1, Art. no. 531, Feb. 2023, doi: [10.1038/s41467-022-35285-3](https://doi.org/10.1038/s41467-022-35285-3). [D]
[118] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030 [R]
[122] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [G]
[124] Quantinuum, “Quantinuum Reports Second Quarter 2026 Results,” Aug. 11, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results [C]
[125] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[129] A. Cordes, “Quantum computing scale-up eleQtron secures €57 million in one of the largest Series A funding rounds worldwide,” eleQtron, May 5, 2026. [Online]. Available: https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [G]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[320] Infineon Technologies AG, “Trapped ion quantum computing.” [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[325] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773). [S]
[328] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[499] D. Kielpinski, C. Monroe, and D. J. Wineland, “Architecture for a large-scale ion-trap quantum computer,” *Nature*, vol. 417, no. 6890, pp. 709–711, Jun. 2002, doi: [10.1038/nature00784](https://doi.org/10.1038/nature00784). [D]
[500] R. Bowler *et al.*, “Coherent Diabatic Ion Transport and Separation in a Multi-Zone Trap Array,” *Phys. Rev. Lett.*, vol. 109, no. 8, Art. no. 080502, 2012, doi: [10.1103/PhysRevLett.109.080502](https://doi.org/10.1103/PhysRevLett.109.080502). [arXiv:1206.0780](https://arxiv.org/abs/1206.0780). [D]
[501] T. Rummler, “In the Mountain West, a quantum computing collaboration announces major results,” Sandia Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/ [G]
[502] M. Abdel-Kareem, “Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers,” Quantum Computing Report, Dec. 18, 2025. [Online]. Available: https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ [P]

## פריטי אימות פתוחים
- רשימת המחברים והכותרת המדויקת של מאמר מלכודת הרשת [113] לא אוחזרו מדף התמצית ב-arXiv; הייחוס ל-Quantinuum נשען על בדיקת העובדות של הדוח הראשי, והתמצית אינה מוסרת את מספר אתרי הרשת.
- אין שחזור בלתי תלוי (שאינו של הספק) לזמן השכבה ברוחב מלא של 55 ms או לקצב ההחלפה ברשת של 2.5 kHz.
- הארכיטקטורה של LYNX של AQT (עם צמתים או ליניארית בלבד) וזמני ההובלה והשער שלה לא נחשפו.
- אין נתון פומבי על שיעור תקינות, אחידות או עלות לפיסה עבור אף קו ייצור של מלכודות יונים; הנתון של EUR 0.5 M לקיוביט הוא מחיר של מערכת מוכנה להפעלה מ-2023, לא עלות שבב.
- לא נבדק מול ערכי הפרמטרים בנוסח התקנה אם סף מספר הקיוביטים ושיעור השגיאה של ECCN 4A906 חל על מערכות היונים המסחריות הנוכחיות.
