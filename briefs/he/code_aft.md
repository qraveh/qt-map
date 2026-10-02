---
id: code_aft
name: סבילות תקלות אלגוריתמית / ארכיטקטורות טרנסוורסליות
layer: "7 קוד"
status: emerging
since: 2025
one_line: החלפת O(d) סבבי חילוץ סינדרום לכל שער לוגי במספר קבוע, באמצעות שערים טרנסוורסליים בין בלוקים ופענוח מתואם.
verdict: המחצית הטרנסוורסלית נמדדה על אטומים ועל יונים; מחצית הפענוח המתואם היא הוכחה ועוד סימולציה. אף ריצה לא סגרה שער טרנסוורסלי, פענוח מתואם והזנה קדימה בזמן אמת.
updated: 2026-09-04
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
סבילות תקלות אלגוריתמית, שהציגו Zhou, Bluvstein, Kubica, Lukin ועמיתיהם כקדם-פרסום ביוני 2024 ופורסמה ב-Nature ב-2025 [D][152], מריצה שערים לוגיים טרנסוורסלית בין בלוקי קוד ומפענחת את היסטוריית הסינדרום של האלגוריתם כולה במשותף, כך ששער לוגי עולה מספר קבוע של סבבי חילוץ ולא את ה-O(d) שניתוח סריג דורשת.

ניידות: היא מניחה מכונה שיכולה להצמיד כל שני בלוקים זה לזה — הובלה במלקחיים אופטיים או הסעת יונים — לא סריג קבוע. מבנה השגיאה: אין ערוץ חדש — רעש פאולי והמחיקה של הקוד עצמו, כשאובדן אטומים שולט, ותקורת המחזורים הפיזיים מוחלפת בתקורת פענוח קלאסית.

## פיזיקה וגבולות
כלל d הסבבים קיים משום שסבב אחד אינו יכול להבחין בין שגיאת מדידה לשגיאת נתונים; חזרה על מעגל הסינדרום d פעמים משווה את מרחק המרחב-זמן של גרף הגלאים למרחק הקוד. היתירות הזאת נחוצה רק כאשר כל בלוק מפוענח לבדו: CNOT טרנסוורסלי ממפה תקלה בבלוק אחד אל בת זוגה בבלוק האחר, ולכן לגרף המשותף על פני הבלוקים והזמן עדיין יש מרחק d אחרי O(1) סבבים — אם המפענח משתמש בו. ההוכחה חוסמת את הסטייה מהתפלגות המדידה הלוגית האידאלית כקטנה מעריכית [D][152].

העלות עוברת לצד הקלאסי, באופן מבני. הגרף המשותף אינו מתפרק לגורמים, ולכן החלון הנע ששומר את הפענוח לכל בלוק מקומי בזמן אינו מדויק עוד: המפענח משתרע על פני כמה שערים לוגיים, אינו יכול לסגור את חלונו עד נקודת ההזנה קדימה הבאה, ועבודתו גדלה עם מספר הבלוקים שנשזרו מאז המדידה האחרונה, לא עם d.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2024-06 | O(d) → O(1) סבבים לכל שער לוגי, הפחתה של >10× במרחב-זמן (הוכחה, סימולציה) | Harvard/QuEra | [D][152] |
| 2025-05 | RSA-2048 ב-5.6 ימים על 19 M אטומים במחזור של 1 ms, ~50× מהר יותר מהמקבילים | Harvard/QuEra | [S][31] |
| 2025-11 | 448 אטומים: שערי CNOT טרנסוורסליים, מאות טלפורטציות, 96 קיוביטים לוגיים | Harvard/QuEra | [D][4] |
| 2026-03 | אלגוריתם שור עם 10,000 אטומים (26,000 למהירות): P-256 בימים, RSA-2048 ארוך בהרבה | Harvard/Caltech | [S][30] |
| 2026-06 | קוד tesseract [[16,6,4]], שערי קליפורד לוגיים טרנסוורסליים, על יונים לכודים | Quantinuum | [D][667] |

כל רווח שדווח הוא סימולציה או פענוח לא-מקוון של סינדרומים שמורים: אף ריצה שפורסמה אינה סוגרת את הלולאה — שער טרנסוורסלי, פענוח מתואם, הזנה קדימה — בזמן אמת.

## ייצור, חומרים ושרשרת האספקה
ארכיטקטורה ושכבת פענוח ללא תהליך, ניצולת או עלות יחידה. החשיפה שלה לשרשרת האספקה היא מיד שנייה אך ספציפית: מסיטים אקוסטו-אופטיים מוצלבים, ש-AA Opto-Electronic ו-Gooch & Housego הם הספקים היחידים הנקובים בעבודת 448 האטומים [D][4], והחומרה הקלאסית שמריצה את הפענוח. NVQLink של NVIDIA קובע את קנה המידה ב-3.84 µs הלוך-ושוב ו-67 µs חציון לפענוח BP-OSD — על הבעיה הקלה בהרבה של בלוק בודד [C][324].

## בקרה, קריאה ועומס הקלט-פלט
אין לייזר, קו בקרה או גלאי חדשים; העומס קלאסי ובזמן אמת. מפענח מתואם חייב לקלוט סינדרומים מכל בלוק ששער טרנסוורסלי נגע בו ולהחזיר תיקון לפני נקודת ההזנה קדימה הבאה — בתוך מילישניות באטומים, על גרף גדול 10²–10³× מבעיית הבלוק הבודד שמעבדי GPU מטפלים בה כיום. ב-10³ קיוביטים לוגיים הראיות הן סימולציה; ב-10⁴–10⁶ לא פורסם מודל השהיה, ושתי הערכות המשאבים מניחות שהפענוח עומד בקצב [S][31][S][30]. ההנחה הזאת, לא מספר האטומים, היא המקום שבו זה נכשל, אם זה נכשל.

## תפקיד במחסנית
היא חלה על כל ארכיטקטורה שיכולה להזיז קיוביטים: מערך המלקחיים האופטיים לאטומי רידברג אלקליים (QuEra, Pasqal, Infleqtion) וגם — אף שרשומת הגרף ממדלת אותה על המערך הזה בלבד — המערכים האלקליים-עפרוריים של Atom Computing וארכיטקטורת ה-QCCD של יונים לכודים, שבה Quantinuum מריצה את אותו קוד [[16,6,4]] טרנסוורסלית [D][667]. היא דורשת הובלה ועוד פענוח מתואם ומודע-אובדן, ומתנגשת עם סריגים קבועים של שכנים קרובים, שאינם יכולים לזווג בלוקים שרירותיים בלי שכבת ניתוב. היא אינה מוסיפה איבר לשעון הנגזר אלא מכפילה אותו, ומקצצת את מספר הסבבים לכל שער לוגי מ-~d (ב-d = 7 על אטומים, ~9 ms לשער) ל-O(1). משבצת ריקה סמוכה: מפענח מתואם בזמן אמת.

## ראיות — כיצד נמדדו המספרים
שערים טרנסוורסליים ו-96 קיוביטים לוגיים פעילים הם מדידות חומרה [D][4]; ההפחתה של >10× היא משפט ועוד סימולציה [D][152], שלא שוחזרו מחוץ לקבוצת המחברים. שתי הערכות המשאבים נבדלות בשלושה סדרי גודל במרחב — עקומת תמורה, לא סתירה: 19 M אטומים קונים RSA-2048 ב-5.6 ימים [S][31], בעוד 10,000–26,000 אטומים קונים P-256 בימים ו-RSA-2048 איטי בסדר גודל אחד או שניים [S][30]; "RSA-2048 עם 10,000 אטומים" הוא מה שאף אחד מהמאמרים אינו אומר. הראיה הנגדית החדה ביותר היא הקוד הטורי של Atom Computing ו-Microsoft: Λ_Z ≈ 1.9 אך Λ_X ≈ 1.2, ממוצע 1.30 על פני ארבעה מחזורים, ועם טעינה מחדש לאורך 90 סבבים הדיכוי נעלם (0.63% לעומת 0.64% למחזור) [D][148]. אטומים לא הראו זיכרון מתמשך מתחת לסף, וסבילות לתקלות במספר סבבים קבוע היא טענה על אלגוריתמים ארוכים.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים כאן | ראיות |
|---|---|---|---|---|
| Harvard | מחקר | ארה״ב | הגתה את הסכמה; הדגמה טרנסוורסלית של 448 אטומים | [D][4], [152] |
| QuEra | מפתח | ארה״ב | מחברת-שותפה וחומרה; Libra 2028 זקוקה לרווח הזה | [C][G:QUERA-LIBRA-2026] |
| Quantinuum | מפתח | ארה״ב/בריטניה | שערי קליפורד לוגיים טרנסוורסליים על יונים, אותו קוד | [D][667] |
| Atom Computing | מפתח | ארה״ב | הובלה בין אזורים; פרסמה את התוצאה הנגדית | [D][148] |
| Google Quantum AI | מפתח | ארה״ב | מסלול אטומים ניטרליים מאז 2026-03, ממוקד בתיקון שגיאות | [C][9] |
| Pasqal | מפתח | צרפת | ארכיטקטורת הובלה, 100 לוגיים עד 2029 | [C][G:PASQAL-SPAC-2026-08] |

**כספים.** 2025-09-09 · QuEra · סבב · $230 M+ · Google, SoftBank Vision Fund 2, NVentures · נסגר [G][153][G:QUERA-230M-2025]. 2025-11-06 · Atom Computing ו-QuEra · שלב B של QBI · ≤$15 M לכל אחת · פעיל [G][65][G:QBI-STAGEB-2025-11]. 2026-02-17 · Infleqtion · הנפקה ראשונית לציבור · >$550 M · NYSE INFQ [G][155]. 2026-05-21 · Atom Computing ו-Infleqtion · מכתב כוונות של CHIPS · $100 M לכל אחת · US Commerce · לא מחייב [G][300][G:CHIPS-LOI-2026-05]. 2026-06-16 · Atom Computing · סבב C · $100 M, Third Point [G][154][G:ATOM-300M-2026-06]. 2026-08-28 · Pasqal · SPAC · ~$360 M במזומן · Nasdaq PSQL [G][156][G:PASQAL-SPAC-2026-08].

**שוק ושרשרת אספקה.** דבר אינו נמכר תחת השם הזה; היא מכפילה את המכונה של מישהו אחר, ולכן הרנטה מצטברת אצל אופטיקת ההובלה ואצל מחסנית המפענחים. היא משלמת עבור G3, בקיצוץ מספר הקיוביטים הפיזיים לכל לוגי מ-~10³ לכיוון ~10², ועבור G4 אם תחזיק; דבר עבור G1 או G5.

**קניין רוחני ותקנים.** העבודה המייסדת עברה ביקורת עמיתים ב-Nature ופתוחה ב-arXiv, וכך גם ניתוח המשאבים מ-ISCA; לא נמצאה משפחת פטנטים הייחודית לסבילות תקלות אלגוריתמית או לפענוח מתואם נכון ל-2026-09-04.

**מפות דרכים ועמידה בהבטחות.** QuEra: Libra הובטחה ב-2026-06-15 ל-2028 (יותר מ-256 לוגיים, 10⁻⁶) אחרי הבטחה מינואר 2024 ל-100 קיוביטים לוגיים ב-2026 — דחייה של שנתיים, ולכן לוח הזמנים הנשען עכשיו על סבילות לתקלות במספר סבבים קבוע כבר אופס פעם אחת [R][162][G:QUERA-LIBRA-2026]. Pasqal: 10,000 פיזיים נדחו מ-2026 ל-2028 [R][G:PASQAL-SPAC-2026-08]. כל מפת דרכים של אטומים מעבר ל-2027 מתמחרת את הרווח הזה; אף אחת אינה מציינת אותו כתלות.

**פרשנות אסטרטגית.** אם תחזיק בקנה מידה, תאריך הסבילות לתקלות של כל ספק בעל יכולת הובלה יוקדם בבת אחת, ומחזור המילישנייה של האטומים יחדל להיות פוסל — זה ההימור שמאחורי הארכיטקטורות המחולקות לאזורים. יונים מרוויחים באותה מידה ומתקדמים יותר בשערי קליפורד טרנסוורסליים, ולכן המנצח אינו חייב להיות חברת אטומים. המפסידים הם סריגי מוליכי-על קבועים של שכנים קרובים, שאינם יכולים לתבוע את ההנחה.

## תחזית ושאלות פתוחות
לאשר/להוריד בדרגה בתוך 12–24 חודשים: קבוצה תסגור שער טרנסוורסלי, פענוח מתואם והזנה קדימה בחומרה; מערכת אטומים תראה זיכרון מתמשך מתחת לסף עם טעינה מחדש; QuEra תנסח מחדש את Libra בלי הרווח הזה. התרחיש הטוב ביותר ל-2029: סבילות לתקלות במספר סבבים קבוע ב-10³ קיוביטים לוגיים, המכווצת כל מפת דרכים בעלת יכולת הובלה. התרחיש הגרוע ביותר: הפענוח המתואם נתקע בכמה עשרות בלוקים ונשאר כלי להערכת משאבים. פתוח: האם השהיית המפענח מתרחבת מעבר ל-10⁴ בלוקים; האם >10× שורד רעש עתיר-אובדן. לעקוב: אבני הדרך של Libra וכל הדגמה של מפענח מתואם בזמן אמת.

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[9] H. Neven, “Building superconducting and neutral atom quantum computers,” Google, Mar. 24, 2026. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]
[30] M. Cain *et al.*, “Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits,” [arXiv:2603.28627](https://arxiv.org/abs/2603.28627), Mar. 2026. [S]
[31] H. Zhou *et al.*, “Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays,” *Proc. 52nd Annu. Int. Symp. Comput. Archit. (ISCA)*, 2025, doi: [10.1145/3695053.3731039](https://doi.org/10.1145/3695053.3731039). [arXiv:2505.15907](https://arxiv.org/abs/2505.15907). [S]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[152] H. Zhou *et al.*, “Low-Overhead Transversal Fault Tolerance for Universal Quantum Computation,” *Nature*, vol. 646, no. 8084, pp. 303–308, 2025, doi: [10.1038/s41586-025-09543-5](https://doi.org/10.1038/s41586-025-09543-5). [arXiv:2406.17653](https://arxiv.org/abs/2406.17653). [D]
[153] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [G]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [G]
[155] L. Roady, “Infleqtion Becomes First Neutral-Atom Quantum Company to Go Public,” Infleqtion, Feb. 17, 2026. [Online]. Available: https://infleqtion.com/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public/ [G]
[156] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [G]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[324] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[667] A. Paetznick *et al.*, “Improved quantum processor logical error rates via correction and detection,” *Nature*, vol. 654, no. 8118, pp. 349–355, Jun. 2026, doi: [10.1038/s41586-026-10628-y](https://doi.org/10.1038/s41586-026-10628-y). [D]

## פריטי אימות פתוחים
- שיעור השגיאה הפיזי, מרחק הקוד ומודל המפענח שמאחורי ההערכות של 19 M אטומים / 5.6 ימים ושל 10,000 אטומים אינם באף אחת משתי התמציות; השתיים לא יושבו מול מערכת הנחות משותפת.
- לא קיים שחזור עצמאי של ההפחתה של >10× במרחב-זמן מחוץ לקבוצת המחברים החופפת של Harvard/QuEra/Caltech.
- אין נתון השהיה שפורסם למפענח מתואם בזמן אמת מעל כ-10² קיוביטים לוגיים; ההתרחבות מעבר לכך אינה מאומתת.
- שנת הכותרת ברשומת הגרף (2025) היא שנת הפרסום ב-Nature; הקדם-פרסום הוא מ-2024-06-25. שתיהן נשמרות ולא מיושבות.
