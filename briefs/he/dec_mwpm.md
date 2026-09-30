---
id: dec_mwpm
name: MWPM / Sparse Blossom (+התאמה מתואמת)
layer: "8 מפענח"
status: demonstrated
since: 2015
one_line: מפענח התאמה בגרף, ההופך סבב סינדרום לשרשרת שגיאות הפאולי הסבירה ביותר; נקודת הייחוס לדיוק, והמפענח בזמן אמת שכבר מסופק בפועל לקודי המשטח.
verdict: ההתאמה נשארת ברירת המחדל של קוד המשטח לאורך 2026 — גם הריצה של Google עצמה מתחת לסף מפוענחת ב-Sparse Blossom. להוריד בדרגה אם עד סוף 2027 מבחן בזמן אמת על החומרה עצמה, על אותם סינדרומים, יראה מפענח שאינו מבוסס התאמה גובר עליה בדיוק ובהשהיה גם יחד.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
MWPM (התאמה מושלמת במשקל מינימלי, minimum-weight perfect matching) הופך כל מייצב מופר לקודקוד בגרף משוקלל שקשתותיו הן השגיאות המהפכות שני גלאים; הזיווג בעל המשקל הנמוך ביותר המסביר את הקבוצה כולה הוא שרשרת השגיאות הבודדת הסבירה ביותר תחת שגיאות בלתי תלויות — ולא פענוח הסבירות המרבית, הסוכם על כל השרשראות שבמחלקה, ושאותו מקרבים מפענחי רשתות הטנזורים והמפענחים מבוססי התפשטות האמונה (belief propagation, BP). Dennis, Kitaev, Landahl ו-Preskill הציגו אותו (2002) [D][650]; Fowler הראה ב-2015 שמתחת לסף אפשר לפתור אותו במדויק בזמן מקבילי ממוצע של O(1) לסבב — על מערך דו-ממדי של מעבדים קלאסיים, שכל אחד מהם משרת מספר קבוע של קיוביטים — ללא תלות בגודל הסריג [D][725]. התאמה מתואמת משקללת מחדש את הקשתות כך ששגיאת Y אינה נספרת פעמיים. המנוע הוא Sparse Blossom של Higgott ו-Gidney (*Quantum* 9, 1600, 2025-01-20) [D][726], ניסוח מחדש דליל של אלגוריתם ה-blossom של Edmonds מ-1965, המופץ כ-PyMatching v2.
a = 0.5 — עיבוד-המשך קלאסי, ללא נושא; b, c, d, e אינם ישימים [graph].
f = שרשרת פאולי על גרף התאמה; g = אין — תוכנה, ללא ייצור [graph].

## פיזיקה וגבולות
התפוקה חייבת לעלות על קצב ייצור הסינדרומים, אחרת הפיגור מתבדר והמכונה נעצרת: Sparse Blossom מעבד ~10⁶ שגיאות לליבה-שנייה, פחות מ-1 µs לסבב ב-d=17 [D][726], בתוך מחזור ה-1.1 µs של Willow [D][1]. ההשהיה מגבילה רק היכן שמדידה לוגית מתנה את הפעולה הבאה: 63 µs ב-d=5 הם ~57 מחזורים של זמן מת [D][1]. רצפת הדיוק מבנית: ההתאמה מוצאת את השרשרת הבודדת הסבירה ביותר רק כאשר כל שגיאה מהפכת לכל היותר שני גלאים, והיא לעולם אינה סוכמת על השרשראות של מחלקה אחת כפי שעושה מפענח סבירות מרבית, ולכן יש להטיל היפר-קשתות (שגיאות Y, שגיאות מדידה מתואמות, דליפה, אובדן) על גרף הניתן להתאמה. ההטלה הזאת היא כל הפער מול מפענח הממדל אותן — Λ = 2.04 ± 0.02 להתאמה לעומת 2.14 ± 0.02 למפענח הנוירוני על הסינדרומים של Willow [D][1], ו-AlphaQubit טוב בכ-25% ב-d=11 בסימולציה [D][657]. מה שמזיז את הרצפה הוא הגרף: משקלי קשתות שנאמדו מהנתונים, קריאה רכה (soft readout), קשתות דליפה.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2023-03 | <1 µs/סבב ב-d=17, ~10⁶ שגיאות/ליבה-שנייה, בסימולציה | Google Quantum AI | [D][726] |
| 2024-12 | השהיה של 63 µs בזמן אמת ב-d=5 לאורך 10⁶ מחזורים | Google Quantum AI | [D][1][G:WILLOW-QEC-2024-12] |
| 2025-03 | השהיית FPGA של 0.8 µs ב-d=13, p=0.1%, 62 MHz | Yale University | [D][727][G:MICROBLOSSOM-2026] |

האיבר השולט: גרף הפענוח — משקלים שכוילו שלא כהלכה, דליפה שאינה מיוצגת — ולא אלגוריתם ההתאמה [D][1].

## ייצור, חומרים ושרשרת האספקה
ללא ייצור: תוכנה ברישיון MIT [728] על חומרת מחשוב כללית, וההאצה היא השכבה שמשלמים עליה, והיא ממקור יחיד. כל מפענח תיקון שגיאות בזמן אמת שפורסם רץ על לוגיקה של AMD/Xilinx — זה של Riverlane על VU19P, ב-≈6% מטבלאות החיפוש (LUT) עבור d≤17 [D][238], Micro Blossom על Versal VMK180 [D][727], המפענח הנוירוני מ-Shenzhen על Kintex-7 [D][729], Relay-BP של IBM על רכיבי AMD [P][48] — ופענוח ב-GPU הוא של NVIDIA בלבד. אין ASIC ל-MWPM (4 בספטמבר 2026). החשיפה לפיקוח על יצוא יושבת בחומרה הזאת: תקנת BIS מ-2024-09-06 מפקחת על מחשבים קוונטיים (4A906) ועל מעגלים משולבים לבקרה הפועלים מתחת ל-4.5 K (3A901.a) [G][301]; קוד מקור מפורסם של מפענחים נמצא מחוץ ל-EAR לפי 15 CFR §734.7.

## בקרה, קריאה ועומס הקלט-פלט
ב-10³ קיוביטים ליבה אחת מספיקה. ב-10⁴ האיבר המגביל הוא רוחב הפס של הסינדרום, לא החישוב — d² גלאים לכל קיוביט לוגי בכל 1.1 µs — ומכאן הצורך בדחיסה מקדימה קריוגנית: נטען להפחתה של עד 3,780× בהספק של פחות מ-0.56 mW ב-4 K, אך המעגל לא יוצר [S][G:PINBALL-2025-12]. ב-10⁶ הקישור מכריע: זמן ההלוך-ושוב של NVQLink, 3.84 µs [C][324], ארוך ממחזור של טרנסמון, ולכן התאמה ב-GPU רצה שם בחלונות.

## תפקיד במחסנית
מפענח ברירת המחדל בזמן אמת לזיכרונות של קוד המשטח ושל קוד הצבע, משותף לחמש משפחות [graph]: כל שלוש הארכיטקטורות של מוליכי-על, כל שלוש הארכיטקטורות של יונים לכודים, שני מערכי הפינצטות של רידברג, הארכיטקטורות הפוטוניות מבוססות-ההיתוך ובמשתנים רציפים, ושתי ארכיטקטורות הספין — ראשי בשש מתוך שתים-עשרה (קיוביטי חתול ו-GKP, מסילה כפולה, מלכודת פאול הליניארית, פוטוניקת היתוך, ספינים בנקודות קוונטיות וספינים דונוריים), חלופי בשאר; הוא צריך את הגרף הכמעט-מישורי שסריג סטטי של שכנים קרובים מספק בחינם. הוא מחליף מפענחים נוירוניים ומפענחי התפשטות אמונה, הגוברים עליו ברגע שהבדיקות חדלות להיות ניתנות להתאמה; המעבר אינו סימטרי — עזיבה עולה מימוש בחומרה וסיפור אימות חדש, חזרה אינה עולה דבר. תרומה לשעון: ≈1.0 µs לסבב ב-d=17 [D][726], לעומת שעון נגזר של 0.65 µs לארכיטקטורת הטרנסמונים עם קוד המשטח (שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס עבור הארכיטקטורה). משבצת ריקה סמוכה: שום מפענח התאמה בזמן אמת אינו צורך קריאה רכה או דגלי דליפה.

## ראיות — כיצד נמדדו המספרים
נתוני התפוקה של Sparse Blossom באים מזרמי Stim מדומים [D][726]. הנתון היחיד המשולב בחומרה, ה-63 µs של Willow ב-d=5, התקבל בגרסה מקבילית ייעודית של Sparse Blossom שבנתה Google, ולא ב-PyMatching המקורי [D][1]. ה-0.8 µs של Micro Blossom ב-d=13 עבר ביקורת עמיתים (ASPLOS 2025), אך הוא מפענח סינדרומים מוקלטים המוזנים מחדש [D][727]; ה-367 ns שבמאגר הקוד אינו מופיע בשום מאמר [C][G:MICROBLOSSOM-2026]. פיזור הספים המצוטט לעתים קרובות אינו סתירה: 0.7% (PyMatching), 0.65% ו-0.55% (מפענחי האשכול של Riverlane בתוכנה ובחומרה) באים מהשוואה אחת תחת מודל רעש אחד [D][238]. כל מתחרה מפרסם את MWPM כקו בסיס; אף אחד אינו משחזר את מהירותו.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Google Quantum AI | מפתח/משתמש | ארה״ב | שותפה לחיבור Sparse Blossom; מריצה אותו ב-Willow | [D][1], [726] |
| Riverlane | ספק | בריטניה | מוכרת את חומרת תיקון השגיאות Deltaflow; מצטטת את MWPM כנקודת ייחוס | [C][G:RIVERLANE-DELTAFLOW-PAGE-2026-05] |
| Yale University | מחקר | ארה״ב | Micro Blossom, מאיץ FPGA ל-MWPM מדויק | [D][727] |
| AMD | ספק | ארה״ב | רכיביה נושאים כל מפענח בזמן אמת שפורסם | [D][238], [727] |
| NVIDIA | ספק | ארה״ב | CUDA-Q QEC ואפיק ה-GPU–QPU של NVQLink | [C][324] |

**כספים.** 2024-08-06 · Riverlane · סבב C · $75 M (לפי מפת הדרכים שלה $85 M) · Planet First Partners מובילה · >$120 M במצטבר · נסגר [C][661]. 2025-11-17 · NVIDIA · השקת NVQLink · לא נמסר · Quantinuum היא שותפת ה-QPU הראשונה [C][G:NVQLINK-QUANTINUUM-2025-11]. 2026-07-24 · Quantum X Labs · תוצאה · לא נמסר סכום · NVIDIA, Quantum Machines/IQCC · לא כומתה [C][730]. אין מענק DARPA ייעודי למפענחים; במסגרת QBI ממומנים אחד-עשר צוותים בשלב B, וכל אחד מהם זקוק למפענח [G:QBI-STAGEB-2025-11]. לא אותר סבב מאוחר יותר של Riverlane נכון ל-4 בספטמבר 2026.

**שוק ושרשרת אספקה.** איש אינו מוכר MWPM: האלגוריתם חופשי ומימוש הייחוס ברישיון MIT [728], ולכן הערך נצבר אצל הקופסה שמריצה אותו — Deltaflow, CUDA-Q QEC/NVQLink, קושחה פנימית. הריכוזיות היא של ספק יחיד, פעמיים: AMD ללוגיקה, NVIDIA ל-GPU. נתון המשאבים הפומבי היחיד, ≈6% מ-VU19P עבור d≤17 [D][238], מרמז על ~16 טלאים לרכיב. תורם ל-G3 ול-G4.

**קניין רוחני ותקנים.** אין משפחת פטנטים על MWPM — המוצא הוא Edmonds (1965) דרך Dennis–Kitaev–Landahl–Preskill (2002) [D][650]; PyMatching ו-Micro Blossom הם ברישיון MIT [727], [728]. הקניין הרוחני יושב על מפענחי חומרה: Riverlane GB 2641501 A (פורסם 2025-12-10), Google US 12,518,194 (הוענק 2026-01-06) [G:SURFACE-CODE-PATENTS]. PatSnap מנתה 12 פטנטים על תיקון שגיאות קוונטי באפריל 2026 (Google 6, IBM 4, Tencent 2), ללא קבוצה של פטנטי מפענחים [P][668]. ממשקים בפועל: מודלי שגיאות-גלאים של Stim, NVQLink.

**מפות דרכים ועמידה בהבטחות.** Higgott ו-Gidney (2023-03 · פענוח תת-מיקרושנייתי בקנה מידה · הושג, ונמצא בתוך הלולאה של Willow) [D][726]. Yale (2025-03 · d=13 ב-0.8 µs על FPGA · הושג; ה-367 ns שבמאגר הקוד — לא) [D][727]. Riverlane (2026-03-12 · megaquop (10⁶ פעולות ללא שגיאה) לפני 2030, teraquop (10¹²) מ-2033 · אין אבן דרך ביניים שמועדה הגיע) [R][658]. הטענות של Google תואמות את מה שסופק, והן היחידות שנמדדו על חומרה פועלת; מפת הדרכים של Riverlane אינה ניתנת להפרכה לפני 2029.

**פרשנות אסטרטגית.** אם ההתאמה תחזיק מעמד, AMD וכל בוני קוד המשטח ינצחו: מימוש הייחוס נשאר חופשי, והבידול מצטמצם לקושחה. מפענח החומרה של Riverlane מקריב סף (0.55% לעומת 0.7%) לטובת השהיה ושטח [D][238], ולכן החפיר התחרותי שלו הוא "מתחת לזמן המחזור" — ואת זה Micro Blossom מציע כעת ל-MWPM מדויק, ברישיון MIT [D][727]. אם ההתאמה תפסיד, היא תפסיד להתפשטות אמונה על qLDPC: המפענח, הקוד והקישוריות יתחלפו יחד.

## תחזית ושאלות פתוחות
לאשר/להוריד בדרגה בתוך 12–24 חודשים: השוואה של ההתאמה מול מתחרה על אותם קיוביטים ובאותו כיול (כל ההשוואות הקיימות הן בסימולציה, במצב לא מקוון או בשיפוט עצמי); מפענח התאמה ב-FPGA הסוגר לולאה חיה ב-d≥7. התרחיש הטוב ביותר ל-2029: ההתאמה נשארת ברירת המחדל מעבר ל-10⁴ קיוביטים פיזיים, וזמן התגובה יורד מ-63 µs ל-~1 µs. התרחיש הגרוע ביותר: זיכרונות qLDPC נושאים את המכונות, והתפשטות אמונה תופסת את מקומה. שאלות פתוחות: האם ההתאמה מתרחבת לסינדרומים של אטומים שבהם שולט האובדן; האם מישהו יממן ASIC למפענח כש-6% מ-FPGA מספיקים; האם שלב C של QBI יקבע מבחן ביצועים שאינו תלוי במפענח.

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[48] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [P]
[238] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[324] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[650] E. Dennis, A. Kitaev, A. Landahl, and J. Preskill, “Topological quantum memory,” *Journal of Mathematical Physics*, vol. 43, no. 9, pp. 4452–4505, 2002, doi: [10.1063/1.1499754](https://doi.org/10.1063/1.1499754). [arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143). [D]
[657] J. Bausch *et al.*, “Learning high-accuracy error decoding for quantum processors,” *Nature*, vol. 635, no. 8040, pp. 834–840, Nov. 2024, doi: [10.1038/s41586-024-08148-8](https://doi.org/10.1038/s41586-024-08148-8). [D]
[658] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [R]
[661] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[668] PatSnap, “Quantum Error Correction Technology Landscape 2026,” Apr. 22, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/articles/quantum-error-correction-patent-landscape-2026/ [P]
[725] A. G. Fowler, “Minimum weight perfect matching of fault-tolerant topological quantum error correction in average O(1) parallel time,” *Quantum Inf. Comput.*, vol. 15, no. 1&2, pp. 145–158, Jan. 2015, doi: [10.26421/QIC15.1-2-9](https://doi.org/10.26421/QIC15.1-2-9). [arXiv:1307.1740](https://arxiv.org/abs/1307.1740). [D]
[726] O. Higgott and C. Gidney, “Sparse Blossom: correcting a million errors per core second with minimum-weight matching,” *Quantum*, vol. 9, Art. no. 1600, Jan. 2025, doi: [10.22331/q-2025-01-20-1600](https://doi.org/10.22331/q-2025-01-20-1600). [arXiv:2303.15933](https://arxiv.org/abs/2303.15933). Also https://arxiv.org/abs/2303.15933. [D]
[727] Y. Wu, N. Liyanage, and L. Zhong, “Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction,” *Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems (ASPLOS '25)*, vol. 2, Mar. 2025, doi: [10.1145/3676641.3716005](https://doi.org/10.1145/3676641.3716005). [arXiv:2502.14787](https://arxiv.org/abs/2502.14787). Also https://github.com/yuewuo/micro-blossom. [D]
[728] O. Higgott, “PyMatching,” GitHub. [Online]. Available: https://github.com/oscarhiggott/PyMatching [G]
[729] X. Yang *et al.*, “Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder,” [arXiv:2605.04892](https://arxiv.org/abs/2605.04892), May 2026. Also https://arxiv.org/html/2605.04892. [D]
[730] Quantum X Labs, “Quantum X Labs Reports Meaningful Error Correction Decoder Results with NVIDIA CUDA-Q QEC,” GlobeNewswire, Jul. 24, 2026. [Online]. Available: https://www.globenewswire.com/news-release/2026/07/24/3332879/0/en/quantum-x-labs-reports-meaningful-error-correction-decoder-results-with-nvidia-cuda-q-qec.html [C]

## פריטי אימות פתוחים
Micro Blossom: הנתון שעבר ביקורת עמיתים הוא השהיה ממוצעת של 0.8 µs ב-d=13 (ASPLOS 2025) [727]; ה-367 ns וה-10⁶ סבבים/s שבמאגר הקוד אינם מופיעים בשום מאמר ואינם נושאים מרחק קוד מוצהר — טענה של מאגר הקוד, לא מדידה.
יש סתירה בסכום סבב C של Riverlane בין ההודעה שלה עצמה ($75 M, 2024-08-06) לבין מפת הדרכים שלה מ-2026 ($85 M) [G:RIVERLANE-FUNDING]; אין הודעה על הרחבה, ולא אותר סבב מאוחר יותר נכון ל-4 בספטמבר 2026.
הטענה של Quantum X Labs שמפענח הטרנספורמר שלה עולה על MWPM אינה נושאת נתון כמותי ולא עברה ביקורת עמיתים [730].
המפענח בזמן אמת של Willow מתואר רק כגרסה ייעודית של Sparse Blossom; לא אותרו עבורו פרסום נפרד, פלטפורמת חומרה או נתון משאבים, ולכן אי אפשר לייחס את ה-63 µs שלו לרכיב מסוים.
