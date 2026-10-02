---
id: enc_hf
name: קיוביט על-דק / קיוביט מצב-שעון
layer: "2 קידוד"
status: demonstrated
since: 1995
one_line: שתי תת-רמות על-דקות, או תת-רמות של ספין גרעיני, של מצב היסוד בנקודת שעון שאינה רגישה לשדה; קיוביט ברירת המחדל של כל ספק של יונים לכודים ושל אטומים ניטרליים.
verdict: השכבה המבדלת פחות מכול במחסנית היונים והאטומים — אוניברסלית, ולכן אין בה לא חפיר תחרותי ולא נעילת מתחרים; התחרות מתנהלת שכבה אחת מעליה, באופן שבו מניעים את הקיוביט.
updated: 2026-09-03
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
שתי תת-רמות על-דקות (או תת-רמות של ספין גרעיני) של מצב היסוד, בעוצמת שדה מגנטי שבה הסטת זימן מסדר ראשון מתאפסת ונשאר רק האיבר הריבועי: קוהרנטיות של שניות עד שעות, וזיכרונות של יון בודד מגיעים לסדר גודל של שעה [104]. השושלת היא שושלת התחום עצמו: שער הלוגיקה הראשון במלכודת יונים, ב-NIST, אחסן קיוביט במצבים הפנימיים של יון יחיד מקורר-לייזר (Monroe, Meekhof, King, Itano, Wineland, PRL 75, 4714, 1995) [374], ומאז זו ברירת המחדל ליונים, ובהמשך גם לאטומים.
f = פאולי + דליפה — דליפה לתת-רמות שכנות, שאינה נראית למפענח המניח רעש פאולי; היקף: ארבע ארכיטקטורות — יונים ב-QCCD ויונים בשערים אלקטרוניים, אטומים אלקליים ואטומים אלקליים-עפרוריים [graph].

## פיזיקה וגבולות
נקודת השעון מבטלת את הרגישות לשדה מסדר ראשון; מה שנשאר הוא איבר זימן הריבועי ועוד *גרדיאנטים* של השדה לרוחב האוגר, ולכן הזיכרון מידרדר עם גודל האוגר, ולא רק עם הזמן. הזיכרון אינו הגבול — ההנעה היא הגבול. שערי ראמאן נושאים שגיאת פיזור ספונטני שיורדת רק כ-~1/Δ, והפוטון המפוזר נוחת בדרך כלל מחוץ למכלול הקיוביט: דליפה, לא שגיאת פאולי. סילוק הלייזר מסלק את האיבר הזה — 2Q 99.97(1)%, 1Q 99.99916(7)% במלכודת של עשרה קיוביטים ושבעה אזורים [D][G:OXIONICS-ALLELEC-2024-07], ו-8.4×10⁻⁵ ללא קירור למצב היסוד [D][102]. אופן הבקרה הוא שמזיז את הרצפה, לא הקידוד.

## מצב ההנדסה העדכני
| תאריך | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2024-12-05 | קיוביט שעון של ⁴³Ca⁺, מהוד מיקרוגל על השבב, טמפרטורת החדר, ללא מיגון: 1.5(4)×10⁻⁷ לכל קליפורד, T₂ ≈ 70 s | Oxford | [D][103][G:OXFORD-1Q-1E-7-2024-12] |
| 2025-11 | צי Helios (98 Ba⁺): 1Q 2.5×10⁻⁵, 2Q 7.9×10⁻⁴, דליפה 1.1×10⁻⁵ לכל קליפורד | Quantinuum | [D][97] |

באטומים: T₂ על-דק של Cs = 12.6 s במערך של 6,100 אטומים [D][138]. האיבר ברמת הצי: דליפה בשער הדו-קיוביטי, ~10⁻⁵ לכל קליפורד ביונים, לעומת ~10⁻⁴ לאטום לכל שער במערכים.

## ייצור, חומרים ושרשרת האספקה
אין תהליך ייעודי; הקידוד נשען על כל מה שמקיף את המין האטומי (Ba⁺, Yb⁺, Ca⁺, Cs, Rb, Sr). שתי משפחות בקרה, שתי שרשראות אספקה: שערי ראמאן דורשים את מערכת האופטיקה כולה — Helios מפעיל שבעה אורכי גל ויותר על פני 1,228 אלקטרודות — בעוד שפסי מיקרוגל על השבב מסלקים אותה ומעבירים את העומס לייצור המלכודות, ש-IonQ הפנימה ברכישת SkyWater [C][19]; eleQtron מוכרת את אותו רעיון בשם MAGIC [C][129]. ¹³⁷Ba ו-¹⁷¹Yb מועשרים הם צוואר הבקבוק הסביר, אך לא נמצאה עובדה מתוארכת על ספק; אין ECCN ייחודי.

## תפקיד במחסנית
ארכיטקטורות: הקידוד הראשי של כל שלוש ארכיטקטורות היונים הלכודים (QCCD; מלכודת פאול ליניארית עם מיעון לייזר פרטני; בקרה אלקטרונית של הקיוביט) ושל מערך המלקחיים האופטיים לאטומי רידברג אלקליים, והקידוד החלופי במערך המלקחיים האופטיים האלקלי-עפרורי. אינו דורש דבר — קידוד הבסיס, הטכנולוגיה החוזרת בשימוש יותר מכל אחרת בעץ. קשת ה"מחליף" שלו אל omg היא הרחבה: omg שומר על מצבי היסוד האלה ומוסיף מכלול מטא-יציב, כך שמין אחד מספק את הקיוביט, את קיוביט העזר ואת הקירור [G:OMG-BLUEPRINT-2021]. הוא אינו מוסיף דבר לשעון הנגזר, שבארכיטקטורת ה-QCCD נקבע בידי ההובלה — סבב של 9.66 ms, לעומת שכבה ברוחב מלא של ~55 ms שנמדדה (≈18 שכבות/s) ושער של 70 µs. אימות: ה-1.5(4)×10⁻⁷ של Oxford הוא קיוביט אחד במערכת ייעודית, וה-2.5×10⁻⁵ של Quantinuum הוא ממוצע צי של 98 יונים — שלושה סדרי גודל ביניהם; רק נתון הצי הוא קלט ארכיטקטוני.

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק | ראיות |
|---|---|---|---|---|
| Quantinuum | מפתח | ארה״ב | Helios, 98 קיוביטי Ba⁺ | [D][97] |
| IonQ | מפתח | ארה״ב | שערים אלקטרוניים, מפעל ייצור מלכודות משלה | [D][102][C][19] |
| University of Oxford | מחקר | בריטניה | שיא השער החד-קיוביטי ב-⁴³Ca⁺ | [D][103] |
| Atom Computing | מפתח | ארה״ב | קיוביטי שעון בספין הגרעיני של Yb | [C][154] |

**כספים.**
2026-06-03 · Quantinuum · הנפקה ראשונית לציבור, Nasdaq QNT, אחרי סבב מספטמבר 2025 לפי שווי של $10 B לפני הכסף · $1.68 B ברוטו · נסגרה [C][G:QTM-IPO-2026-06][G:QTM-600M-2025-09]
2026-07-31 · IonQ · רכישת SkyWater נסגרה · ~$1.8 B [C][G:IONQ-SKYWATER-2026]

**שוק ושרשרת אספקה.** שום דבר אינו נמכר בתור "קידוד על-דק": הכסף נמצא בהנעה — שרשראות לייזר מול מלכודות מיקרוגל. הריכוזיות נמוכה באופטיקה ועולה במלכודות, עכשיו כש-IonQ מחזיקה מפעל ייצור. היעדים המשלמים: G3/G4/G7 — המצע שמתחת לכמעט כל קיוביט לוגי שהודגם עד כה.

**קניין רוחני ותקנים.** PatSnap Eureka (2026) מדרגת את IonQ במקום הראשון בין בעלי הזכויות הנקובים בשמם, עם 9+ רשומות (5 JP, 2 EP, 2 IL בבחינה) על פולסי שערים ועל אופני תנועה; הספירה מערבבת פטנטים עם מאמרים [P][375].

**מפות דרכים ועמידה בהבטחות.** Quantinuum: Sol ב-2027, Apollo ב-2029 (הובטח 2024-09-10); Helios הגיע בזמן, 2025-11-05, וקצב של 10× בשנה בנפח הקוונטי נשמר. IonQ: 256 קיוביטים ב-99.99% נדחו למחצית הראשונה של 2027, ו-4,000 קיוביטים עד 2026 (הובטח ב-2020) הוחמצו בפער של ~40×. Quantinuum עומדת בתאריכים, IonQ — בפיזיקה.

**פרשנות אסטרטגית.** האוניברסליות היא העיקר: כולם משתמשים בו, ולכן אין בו לא חפיר תחרותי ולא נעילת מתחרים. התחרות היא על ההנעה. אם בקרה אלקטרונית מלאה תגדל מעבר לעשרה קיוביטים, שרשרת הלייזרים תהפוך לנטל עבור Quantinuum ועבור כל ספק אטומים; אם לא, IonQ קנתה מפעל ייצור בשביל תוצאת מעבדה.

## תחזית ושאלות פתוחות
לאשר אם בקרה אלקטרונית מלאה תגיע לממוצע צי מתחת ל-10⁻⁵ עם דליפה מפורסמת, או אם קבוצה שנייה תשחזר את ה-8.4×10⁻⁵; להוריד בדרגה אם תישאר תוצאה של עשרה קיוביטים. התרחיש הטוב ביותר ל-2029: קיוביטים על-דקים המונעים במיקרוגל הם ברירת המחדל. התרחיש הגרוע ביותר: דליפה המוגבלת בגרדיאנטים של השדה עוצרת את היונים סביב 10⁻⁵, ו-omg תופס את מקומו כבסיס.

## מקורות
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[103] M. C. Smith, A. D. Leu, K. Miyanishi, M. F. Gely, and D. M. Lucas, “Single-qubit gates with errors at the 10⁻⁷ level,” *Phys. Rev. Lett.*, vol. 134, no. 23, Art. no. 230601, Jun. 2025, doi: [10.1103/42w2-6ccy](https://doi.org/10.1103/42w2-6ccy). [arXiv:2412.04421](https://arxiv.org/abs/2412.04421). [D]
[104] P. Wang *et al.*, “Single ion-qubit exceeding one hour coherence time,” *Nat. Commun.*, vol. 12, Art. no. 233, Jan. 2021, doi: [10.1038/s41467-020-20330-w](https://doi.org/10.1038/s41467-020-20330-w). [arXiv:2008.00251](https://arxiv.org/abs/2008.00251). [D]
[129] A. Cordes, “Quantum computing scale-up eleQtron secures €57 million in one of the largest Series A funding rounds worldwide,” eleQtron, May 5, 2026. [Online]. Available: https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/ [C]
[138] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[374] C. R. Monroe, D. M. Meekhof, B. E. King, W. M. Itano, and D. J. Wineland, “Demonstration of a Fundamental Quantum Logic Gate,” *Phys. Rev. Lett.*, vol. 75, no. 25, pp. 4714–4717, Dec. 1995, doi: [10.1103/PhysRevLett.75.4714](https://doi.org/10.1103/PhysRevLett.75.4714). [D]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[G] Smith, Leu, Miyanishi, Gely, Lucas (Oxford), "Single-qubit gates with errors at the 10^-7 level", arXiv:2412.04421 (2024-12-05, rev 2025-05-28): 43Ca+ hyperfine clock qubit in a mi… · 2024-12-05 · https://arxiv.org/abs/2412.04421
[G] Loschnauer, Mosca Toba, Hughes, King, Weber, Srinivas, Matt, Nourshargh, Allcock, Ballance, Matthiesen, Malinowski, Harty, "Scalable, high-fidelity all-electronic control of trappe… · 2024-07-10 · https://arxiv.org/abs/2407.07694
[G] Allcock, Campbell, Chiaverini, Chuang, Hudson, Moore, Ransford, Roman, Sage, Wineland, "omg blueprint for trapped ion quantum computing with metastable states", Applied Physics Let… · 2021 · https://cua.mit.edu/dev_site/publications/omg-blueprint-for-trapped-ion-quantum-computing-with-metastable-states
[G] Quantinuum raised $600 M at a $10 B pre-money valuation (NVentures, Quanta, QED, JPMorgan), 2025-09-04 · 2025-09-04 · https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale
[G] Quantinuum IPO priced 2026-06-03: 28,000,000 shares at $60 = $1.68 B gross, Nasdaq QNT; Q2-2026 revenue $8.0 M, cash $2.1 B, FY guidance $28–32 M · 2026-06-03 · https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering
[G] IonQ acquired SkyWater Technology: $15.00 cash + 0.4883 IonQ shares per share (~$1.8 B at announcement 2026-01-26), closed 2026-07-31 · 2026-07-31 · https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology
## פריטי אימות פתוחים
- תמצית ה-PRL מ-1995 אינה נוקבת במין האטומי או בתת-הרמות העל-דקות; הייחוס "מאז 1995" נשען על רשומת הגרף ועל קיוביט המצבים הפנימיים שבמאמר, לא על אמירה מפורשת על מבנה על-דק בתמצית.
- המקור לזיכרון בסדר גודל של שעה ב-Yb⁺ מדבר על "זיכרון של קיוביט ביון Yb בודד", בלי לציין בתמצית את האיזוטופ או את המעבר.
- ל-1.5(4)×10⁻⁷ של Oxford אין מקבילה מפורסמת של ממוצע צי רב-קיוביטי.
- הספירות של PatSnap מערבבות פטנטים ומאמרים, ולא אומתו מול הבקשות המקוריות.
- לא נמצאה עובדה מתוארכת על ספק של ¹³⁷Ba או של ¹⁷¹Yb בהעשרה איזוטופית; הטענה על צוואר הבקבוק לא אומתה.
