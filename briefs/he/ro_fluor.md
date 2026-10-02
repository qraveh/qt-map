---
id: ro_fluor
name: גילוי מצב בפלואורסצנציה (יונים, פגמים)
layer: "6 קריאה"
status: demonstrated
since: 1995
one_line: פלואורסצנציה תהודה תלוית-מצב, הנספרת ב-PMT, ב-EMCCD, ב-SNSPD או בפוטודיודה המשולבת במלכודת, היא קריאת ברירת המחדל הלא-הורסת באמצע המעגל של יונים לכודים.
verdict: הקריאה אינה עוד החוליה החלשה במערכת היונים הטובה ביותר; ניתן להפרכה אם נתון SPAM כלשהו שפורסם על מערכת יונים מסחרית יעלה על שגיאת השער הדו-קיוביטי של אותה מערכת.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
מעבר מחזורי סגור מפזר פוטונים רק כשהקיוביט יושב במצב לוגי אחד; ספירתם מקריסה את המדידה אל ביט קלאסי. הגלאים הם מכפילי פוטונים (PMT), מצלמות EMCCD, גלאי פוטון בודד מננו-תיל מוליך-על (SNSPD) או, לאחרונה, פוטודיודות מפולת הבנויות בתוך המלכודת. בשימוש מאז ההדגמות הראשונות של יונים לכודים (1995), ללא שינוי עקרוני. תכונות: c = קריאה בפלואורסצנציה, לא-הורסת, ניתנת לביצוע באמצע המעגל, ~10⁻⁴ s — 11 µs ב-99.931(6)% על ¹⁷¹Yb⁺ עם SNSPD [D][617]; e = בקרה אופטית, חומרת הגילוי בטמפרטורת החדר, שלא כמו היון.

## פיזיקה וגבולות
המנגנון הוא מניית פוטונים על רקע של ספירות חושך ואור תועה, ולכן האות נקבע כולו לפי מספר הפוטונים המפוזרים המגיעים אל גלאי: המפתח המספרי (NA) של האיסוף (אחוזים ספורים מ-4π), תמסורת העל-סגול, הנצילות הקוונטית של הגלאי. האיבר האחרון הוא המקום שבו הפלטפורמה סובלת — המעברים המחזוריים הם בעל-סגול (369.5 nm ל-Yb⁺), שם נצילות ה-PMT היא עשרות אחוזים, ונצילויות הגילוי המערכתיות של 98% המצוטטות ל-SNSPD אינן חלות, בהיותן נתונים בתחום הטלקום [D][618]. השיא של 2019 עבד משום ש-SNSPD ממוליבדן-סיליציד נבנה במיוחד ל-369.5 nm, מה שאפשר לניסוי לעצור באירוע גילוי יחיד [D][617]. הרצפה היא גאומטריה ונצילות, לא פיזיקה אטומית. השגיאות הן סיווג שגוי דמוי-פאולי, למעט כשהמצב החשוך דולף אל מחוץ למעבר המחזורי — ערוץ אובדן ש-SPAM תקני מקפל לתוך מספר אחד. מה שמזיז את הרצפה: איסוף במפתח מספרי גבוה יותר, גלאים הממוטבים לעל-סגול, והעברת הגלאי אל פיסת המלכודת.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2019-08-21 | גילוי ממוצע של 11 µs ב-99.931(6)%, הפרעה הדדית ~2×10⁻⁵ ב-370 µm, SNSPD מ-MoSi על ¹⁷¹Yb⁺ | Duke University | [D][617] |
| 2022-09-02 | 99.92(1)% ב-450 µs עם פוטודיודות מפולת בטמפרטורת החדר המשולבות במלכודת, Sr⁺ | MIT Lincoln Laboratory | [D][619] |
| 2025-11 | Helios (98 Ba⁺): SPAM 3.3–4.8×10⁻⁴, דליפה 1.1×10⁻⁵ לשער קליפורד | Quantinuum | [D][97] |
| 2026 | Forte (שרשרת של 36 יונים): SPAM 0.5% | IonQ | [C][99] |

ההיפוך חשוב: ב-Helios ה-SPAM יושב מתחת לשגיאת השער הדו-קיוביטי (7.9×10⁻⁴) [D][97], וה-SPAM הלוגי בקוד [[80,48,4]] נמוך מ-8×10⁻⁶ [D][105]. לפני עשור הקריאה שלטה בתקציבי השגיאה של היונים; לא עכשיו.

## ייצור, חומרים ושרשרת האספקה
הרכבה אופטית, לא שכבת ייצור — אובייקטיבים בעלי מפתח מספרי גבוה, חלונות ואקום לעל-סגול, גלאי — המיושרים לכל מערכת בנפרד, ולכן השונות בין גלאים היא עלות כיול, לא אובדן תקינות. PMT ומצלמות EMCCD/qCMOS מגיעים מ-Hamamatsu ומ-Andor (Oxford Instruments), ו-Hamamatsu היא הספקית הנקובה היחידה של מצלמות ברגישות של פוטון בודד במחלקה זו [C][620]. גלאי SNSPD מגיעים מבסיס של חמישה ספקים עצמאיים — Single Quantum, ID Quantique, Photon Spot, Quantum Opus, Scontel — שאף אחד מהם לא חשף מימון או הכנסות [P][621], וכל אחד מהם נושא קריוסטט במחזור סגור שערוצי PMT ומצלמה אינם צריכים. במעלה הזרם, נקודות הכשל היחידות משותפות לשאר מחסנית היונים: לייזרים לעל-סגול (TOPTICA) ומפעל הייצור העצמאי של Infineon למלכודות [P][322]. אין ECCN לקריאת יונים; כלל ה-BIS מ-2024 מגיע למחשבים ולמקררים, לא לגלאים.

## בקרה, קריאה ועומס הקלט-פלט
ערוץ איסוף אחד לכל אזור קריאה, לא לכל קיוביט — ה-QCCD של Quantinuum מובילה יונים אל אזורים ייעודיים, ולכן מספר הערוצים גדל עם מספר האזורים [D][97]. זו הסיבה שהשכבה הזאת טרם נתקלה בקיר: ב-10³ קיוביטים, קריאה לפי אזורים מודגמת ב-98 יונים על פני 8 אזורים. ב-10⁴ אובייקטיב במרחב חופשי לכל אזור חדל להיות ניתן לבנייה, והתשובה חייבת להיות שילוב — פוטודיודות המשולבות במלכודת [D][619] או מערכי SNSPD מרובבים, שמצלמת שורה-עמודה של 400,000 פיקסלים היא הוכחת הקיום שלהם, במחיר של רזולוציית תזמון [D][339]. ב-10⁶ לא פורסם דבר. קריאה באמצע המעגל חייבת גם לעמוד בקצב הפענוח בזמן אמת; ב-11–100 µs היא עומדת בו.

## תפקיד במחסנית
משרתת את שלוש ארכיטקטורות היונים הלכודים — QCCD, מלכודת פאול ליניארית עם מיעון לייזר פרטני, ובקרה אלקטרונית של הקיוביט — וצומתי הרשת של ספיני פגם משתמשים בה שוב לקריאה אופטית של הספין. היא דורשת מעבר מחזורי; אין ליונים מנגנון קריאה מתחרה בקנה מידה של מוצר, שכן קריאה דיספרסיבית ייחודית למוליכי-על. הבחירה האמיתית היחידה היא סוג הגלאי, שמחיר ההחלפה שלו הוא תכנון מחדש של אופטיקת האיסוף, לא של המעבד. בשעון הנגזר — סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס — לקריאה יש מרווח גדול: 100 µs מסבב של 9.7 ms לעומת 9.0 ms של הובלה, ושכבה ברוחב מלא היא ~55 ms משום שמיון, הובלה וקירור שולטים [D][97], ולכן קריאה מהירה יותר אינה קונה דבר היום. קריאה מרובבת של אזורים רבים ללא עלות ליניארית בערוצים ובקריוסטטים נותרת משבצת ריקה.

## ראיות — כיצד נמדדו המספרים
SPAM נמדד בהכנת מצבים בהירים וחשוכים ידועים ובספירת הסיווגים השגויים; ה-3.3–4.8×10⁻⁴ של Helios הוא טווח לפי אזורים, לא מספר אחד [D][97]. SPAM תקני ממזג הכנה עם מדידה, ולעתים רחוקות מפריד דליפה או אובדן מסיווג שגוי — ציטוט נפרד של הבחנה ושל הישרדות, כפי שעושה מחקר דימות של איטרביום ניטרלי מ-2026 (99.89% ו-98.80%, לא תוצאה של יונים), אינו נפוץ כאן [P][261]. גם מספרי הכותרת אינם ניתנים להשוואה: שלושה מינים, שלושה גלאים, שלוש מכונות. ה-SPAM של Forte של IonQ, 0.5% [C][99], גרוע בסדר גודל מזה של Helios — ייתכן שזהו הבדל ארכיטקטוני אמיתי, שרשראות ארוכות על מצלמה לעומת גילוי לפי אזורים, אך זהו דף מפרט מול קדם-פרסום.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב/בריטניה | קריאה בפלואורסצנציה לפי אזורים ב-Helios, SPAM 3.3–4.8×10⁻⁴ | [D][97] |
| IonQ | מפתח | ארה״ב | קריאה במצלמה בשרשראות של Forte; בעלת יצרנית ה-SNSPD ID Quantique | [C][99] |
| ID Quantique | ספק | שווייץ | מערכות גילוי SNSPD; בבעלות IonQ מאז 2025-05-06 | [P][622] |
| Hamamatsu Photonics | ספק | יפן | PMT והמצלמות הנקובות היחידות כאן ברגישות של פוטון בודד | [C][620] |
| Single Quantum | ספק | הולנד | SNSPD ממקור עצמאי, החלופה העיקרית שאינה IonQ | [P][621] |
| MIT Lincoln Laboratory | מחקר | ארה״ב | פוטודיודות מפולת המשולבות במלכודת, 99.92% | [D][619] |

**כספים.**
2025-03-03 · IonQ · מיזוג ורכישה, ID Quantique (גלאי SNSPD) · לא נחשף · נסגר 2025-05-06 [P][622]
2025-09-04 · Quantinuum · סבב פרטי · USD 600 M לפי שווי של USD 10 B לפני הכסף · NVentures, Quanta, QED, JPMorgan · נסגר [G][122]
2026-06-03 · Quantinuum · הנפקה ראשונית לציבור (IPO), Nasdaq QNT · USD 1.68 B ברוטו · מזומנים USD 2.1 B · נסגר [G][123]
2026-07 · IonQ · מיזוג ורכישה, מפעל הייצור SkyWater Technology · USD 1.8 B · נסגר [G][19]

**שוק ושרשרת אספקה.** כסף קטן הצמוד לכסף גדול. רכישת ID Quantique בידי IonQ נתנה לאחד משני ספקי היונים בשלב B של QBI אספקת SNSPD עצמית, ש-Quantinuum, eleQtron ו-Quantum Art חייבות לקנות בשוק הספקים העצמאיים [P][622][P][621] — אירוע הריכוזיות החד ביותר כאן, אף שמשקלו מוגבל כל עוד PMT ומצלמות נותרים מספיקים. אין מחיר פומבי לערוץ. משלמת על G2 ו-G3: כל תוצאת תיקון שגיאות ביונים, כולל 48 הקיוביטים הלוגיים של Helios, נשענת עליה. היא גם מתנה את G6, שכן חיבורים בין-מודוליים פוטוניים זקוקים לאותם גלאים בקצבים גבוהים בהרבה.

**קניין רוחני ותקנים.** לא נמצאה במאגר נקוב ספירה מתוארכת של משפחות פטנטים הייחודית לקריאת יונים בפלואורסצנציה — לא נמצאה עובדה מתוארכת. הפעלת SNSPD המבחין במספר הפוטונים מכוסה בפטנט US 11,274,962 B2, ברישיון בלעדי ל-Quantum Opus [C][621]. אף תקן של קונסורציום אינו מסדיר קריאת יונים.

**מפות דרכים ועמידה בהבטחות.** אף ספק אינו מפרסם מפת דרכים עצמאית לקריאה; היא רוכבת בתוך מפות הדרכים של המערכות — Sol 2027 ו-Apollo 2029 של Quantinuum [R][97], 256 קיוביטים ב-99.99% של IonQ נדחו מ-2026 למחצית הראשונה של 2027 [R][132]. Quantinuum סיפקה את Helios בזמן עם נתון ה-SPAM שהבטיחה; IonQ לא פרסמה דבר שעבר ביקורת עמיתים מאחורי מפרט ה-0.5% שלה, ורכישת הגלאים שלה לא הניבה תוצאת קריאה שפורסמה.

**פרשנות אסטרטגית.** אם SNSPD לעל-סגול או פוטודיודות המשולבות במלכודת יהפכו לסטנדרט ב-10⁴ אזורים, הבעלות של IonQ על גלאים ועוד מפעל הייצור SkyWater שלה הם יתרון שילוב אמיתי, ו-Hamamatsu מאבדת נישה. אם PMT ומצלמות יישארו מספיקים — כפי ש-Helios מרמז — בחירת הגלאי נשארת החלטה סחורתית.

## תחזית ושאלות פתוחות
לאשר עד סוף 2027 אם IonQ תפרסם נתון SPAM שעבר ביקורת עמיתים; להוריד את טענת ה-0.5% בדרגה אם תישאר דף מפרט. התרחיש הטוב ביותר עד 2029: גלאים המשולבים במלכודת או מערכי SNSPD מרובבים הופכים את הקריאה לכל אזור לחינמית ב-10⁴ אזורים. התרחיש הגרוע ביותר: הקריאה נשארת אובייקטיב אחד במרחב חופשי לכל אזור והופכת למגבלה המכנית על מספר האזורים. שאלות פתוחות: האם אספקת הגלאים שבבעלות IonQ מניבה יתרון SPAM מדיד; האם נצילות SNSPD לעל-סגול יכולה להתקרב לנתוני תחום הטלקום; האם פוטודיודות המשולבות במלכודת מגיעות לעשרות ה-µs שגילוי במרחב חופשי כבר משיג.

## מקורות
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [G]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[99] IonQ, “IonQ Forte: High-Performance Commercial Quantum Computer.” [Online]. Available: https://www.ionq.com/quantum-systems/forte [C]
[105] S. Dasu *et al.*, “Computing with many encoded logical qubits beyond break-even,” [arXiv:2602.22211](https://arxiv.org/abs/2602.22211), Feb. 2026. [D]
[122] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale [G]
[123] Quantinuum, “Quantinuum Announces Pricing of Upsized Initial Public Offering,” Jun. 3, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering [G]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[339] B. G. Oripov *et al.*, “A superconducting nanowire single-photon camera with 400,000 pixels,” *Nature*, vol. 622, no. 7984, pp. 730–734, Oct. 2023, doi: [10.1038/s41586-023-06550-2](https://doi.org/10.1038/s41586-023-06550-2). [D]
[617] S. Crain *et al.*, “High-speed low-crosstalk detection of a ¹⁷¹Yb⁺ qubit using superconducting nanowire single photon detectors,” *Commun. Phys.*, vol. 2, no. 1, Art. no. 97, Aug. 2019, doi: [10.1038/s42005-019-0195-8](https://doi.org/10.1038/s42005-019-0195-8). [D]
[618] D. V. Reddy, R. R. Nerem, S. W. Nam, R. P. Mirin, and V. B. Verma, “Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm,” *Optica*, vol. 7, no. 12, p. 1649, Dec. 2020, doi: [10.1364/OPTICA.400751](https://doi.org/10.1364/OPTICA.400751). [D]
[619] D. Reens *et al.*, “High-Fidelity Ion State Detection Using Trap-Integrated Avalanche Photodiodes,” *Phys. Rev. Lett.*, vol. 129, no. 10, Art. no. 100502, Sep. 2022, doi: [10.1103/PhysRevLett.129.100502](https://doi.org/10.1103/PhysRevLett.129.100502). [D]
[620] Hamamatsu Photonics, “APS DAMOP 2026,” Aug. 25, 2026. [Online]. Available: https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html [C]
[621] TipRanks, “Single Quantum Hits 400-System Milestone as It Deepens European Quantum Partnerships,” Jul. 4, 2026. [Online]. Available: https://www.tipranks.com/news/private-companies/single-quantum-hits-400-system-milestone-as-it-deepens-european-quantum-partnerships [P]
[622] startupticker.ch, “US-based company acquires ID Quantique,” Mar. 3, 2025. [Online]. Available: https://www.startupticker.ch/en/news/US-based-company-acquires-id-quantique [P]

## פריטי אימות פתוחים
מחיר רכישת ID Quantique לא נחשף, ולכן אי אפשר להעריך את שוויה של עמדת אספקת הגלאים. ל-SPAM של Forte של IonQ, 0.5%, אין מקבילה שעברה ביקורת עמיתים. אף ספק אינו מפרסם עלות גלאי לערוץ, ואי אפשר להפריד הכנסות המיוחסות לקריאת יונים בדיווחי Hamamatsu או Oxford Instruments. לא נמצאה נצילות גילוי מערכתית שפורסמה ל-SNSPD בעל-סגול (369–400 nm) להעמיד מול נתון ה-98% של תחום הטלקום. תוצאת הדימות של Kyoto/Yaqumo, 17.6 µs, היא מדידה של אטום איטרביום ניטרלי, לא קריאת יונים, ומצוטטת כאן רק כהשוואה מתודולוגית.
