---
id: ae_atom
name: אטום אלקלי-עפרורי או דומה לו (Yb/Sr) — מחיקה מובנית
layer: "1 נושא הקיוביט"
status: demonstrated
since: 2019
one_line: קיוביטי איטרביום/סטרונציום במלקחיים אופטיים, שמכלול השעון המטא-יציב שלהם הופך דעיכה ואובדן לניתנים לגילוי אופטי, וממיר שגיאות פיזיות למחיקות מבושרות במקום לשגיאות פאולי שקטות.
verdict: ההמרה למחיקה ממשית ועקבית פנימית (דיכוי דעיכה בלתי מותנה של 1.9(4)×), אך הקידוד המטא-יציב עולה ~6× בשגיאת CZ ולא שוחזר מחוץ ל-Princeton ול-Caltech.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
ל-¹⁷¹Yb ול-⁸⁷Sr יש שני אלקטרוני ערכיות: טריפלט מטא-יציב ³P₀/³P₂ בעל זמן חיים של שניות מעל סינגלט היסוד ¹S₀, על קו שעון צר (578 nm ל-Yb, 698 nm ל-Sr). אלומת דימות של מכלול היסוד חשוכה לקיוביט במכלול המטא-יציב, ולכן דעיכה ואובדן מפזרים פוטונים בזמן שמרחב הקוד נשאר שקט — שיטת "omg" (אופטי–מטא-יציב–יסוד), מתוך תוכנית אב למלכודות יונים מ-2021 [D][333]. השגיאות מגיעות אז כשהן ממוקמות, כמחיקות, ולא כהיפוכי פאולי שקטים. הודגם ב-Yb (Princeton) וב-Sr (Caltech), במאי 2023 [D][141], [143].
תכונות: נושא טבעי; שזירה דטרמיניסטית בחסימת רידברג ~250 ns; קריאה בפלואורסצנציה ~0.5 ms, לא-הורסת, ניתנת לביצוע באמצע המעגל.
בקרה אופטית מטמפרטורת החדר; מבנה השגיאה: מחיקה ואובדן, לא פאולי מטבעו; ייצור בהרכבה אופטית, לא בליתוגרפיה.

## פיזיקה וגבולות
ההמרה למחיקה מתייגת את השגיאה מחדש במקום להקטין אותה; התמורה נמצאת במפענח — ב-1% מחיקה, קוד המשטח המודע למחיקות סובל שגיאת פאולי עד 0.51%, 5.2× לעומת הפרוטוקול הסטנדרטי [D][334]. רצפת השער נמצאת במקום אחר: CZ בחסימת רידברג פועל בכמה מאות ננו-שניות מול דעיכה ספונטנית של רמת רידברג ועוד דעיכה מקרינת גוף שחור (0.05–0.1%), רעש פאזה של הלייזר (0.1–0.2%) ותנועה תרמית (~0.1%), שלטענת סקירה מ-2026 מגבילים את השיטה הסטנדרטית לסביבות 99.9% בהיעדר מנגנון שער חדש [P][140]. אובדן אטומים הוא יותר מ-80% מאירועי הדליפה [D][4] — בדיוק מה ש-omg רואה. הזזת הרצפה דורשת מעטפת קריוגנית נגד דעיכת רידברג המונעת בקרינת גוף שחור, פחות פיזור של אור הלכידה אל מחוץ למכלול המטא-יציב (הוא קובע את מרווח הבדיקות), ודימות שחוסך באתרים השכנים.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג/מפתח |
|---|---|---|---|
| 2023-05 | 56% משגיאות השער החד-קיוביטי → מחיקות, ¹⁷¹Yb (תקרה של 98%) | Princeton | [D][141] |
| 2024-07 | CZ של Sr: 99.71% | Caltech | [D][136] |
| 2024-11 | CZ של Yb: 99.72% בבחירה בדיעבד / 99.40% גולמי | Atom Computing | [D][135] |
| 2026-06 | שגיאת CZ מטא-יציב 0.016(1), 38(6)% מסומנות; דעיכת [[4,2,2]] איטית 1.9(4)× | Princeton | [D][142][G:PRINCETON-ERASURE-V2-2026-06] |
| 2026-08 | דימות ב-17.6 µs, הבחנה 99.89(5)%, הישרדות 98.80(44)%, ¹⁷⁴Yb | Kyoto/Yaqumo | [P][261][G:KYOTO-FASTIMG-2026-08] |

האיבר השולט הוא השער, לא מנגנון המחיקה: שגיאת ה-CZ המטא-יציב של Princeton, 0.016(1), גדולה ~6× משגיאת ה-CZ הגולמית של Atom Computing במצב היסוד של Yb, 0.0060 [D][135], [142], ורק ~38% ממנה חוזרים כדגלים. שיא ה-17.6 µs הוא של ¹⁷⁴Yb חסר ספין, לא קריאה של ¹⁷¹Yb, ולכן 0.5 ms נשאר המחזור הכן.

## ייצור, חומרים ושרשרת האספקה
אין שבב ליתוגרפי: ה"מפעל" הוא תא UHV, אובייקטיב בעל NA גבוה, היגוי SLM/AOD ולייזרי שעון, רידברג, דימות ואחסון; שיעור התקינות הוא הסתברות הטעינה לכל אתר ועוד אי-אחידות של המלכודות בגלל אברציות ה-SLM. האופטיקה היא מניע העלות — המערכת של Fraunhofer ILT מ-2026 יוצרת 2,000 מלקחיים אופטיים לאטומי רידברג ניתנים לבקרה מארבע אלומות בהספק כולל של 20 W [D][G:FRAUNHOFER-TWEEZER-2026-07], כ-10 mW לאתר, ולכן 10⁴ אתרים הם בעיית לייזר ברמת 100 W [S]. הנקודות הדקות אינן מפעלי ייצור: בכל הספרות מופיעים רק שני ספקים של AOD מוצלבים (AA Opto-Electronic, Gooch & Housego) [D][G:AOD-VENDORS-2026], ולקו ה-SLM והמצלמות של Hamamatsu לא זוהתה חלופה [P][G:HAMAMATSU-CAMERA-CONC-2026]. החשיפה לפיקוח על יצוא היא ברמת המערכת: ECCN 4A906 מפקח על מחשבים קוונטיים מעל סף של מספר קיוביטים ושיעור שגיאות (בתוקף מ-2024-09-06, עם חריגת הרישוי IEC לשותפות); אף ECCN אינו נוקב באופטיקת מלקחיים, ב-AOD או בתאי UHV [G][301][G:BIS-QUANTUM-ECCN-2024-09].

## בקרה, קריאה ועומס הקלט-פלט
המיעון נעשה במלקחי AOD/SLM ועוד אלומות שעון ורידברג גלובליות; הקריאה היא דימות ב-0.5–1 ms. בדיקת מחיקה באמצע המעגל חייבת להיות בררנית למכלול, ואסור לה לחמם את השכנים שהיא מאירה — זה האילוץ שמחזיק את ההמרה שהודגמה ב-38–56% ולא בתקרה של 98% [D][141], [142]. אלומות גלובליות ועוד מיעון AOD מספיקים ב-10³ אתרים; ב-10⁴ היגוי האלומות הופך לצוואר בקבוק לפעולות מקומיות מקבילות — מסיט מבחין במספר נקודות השווה למכפלת רוחב הפס שלו בתדר הרדיו בזמן מעבר הגל האקוסטי דרך האלומה, ואותו זמן מגביל את מהירות ההכוונה מחדש, ואילו מאפנני גביש נוזלי מחליפים תמונה רק בקצב של עשרות הרץ — והספק הלכידה עובר 100 W; ב-10⁶ אין מסלול, אלא באמצעות מטא-משטח או הולכה פוטונית.

## תפקיד במחסנית
נושא זה מגדיר את הארכיטקטורה "מערך מלקחיים אופטיים לאטומי רידברג — אלקליים-עפרוריים (Yb/Sr), מחיקה מובנית" (Atom Computing/Microsoft, Princeton, Caltech, planqc, Yaqumo), והוא הנושא החלופי של "סימולטור אנלוגי של אטומים ניטרליים (מערכי רידברג, גזי סריג)" (QUIONE של ICFO, גז סריג של ⁸⁴Sr): הרכבה אופטית בלבד, ללא מפעל ייצור וללא קריוסטט, ולכן ללא חומת הון בסגנון CHIPS. הוא מזין את שער ה-CZ בחסימת רידברג, את קידוד omg, את הקריאה בדימות, את הקריאה המהירה (≤20 µs) של המערך ואת ממשק אטום–פוטון במהוד. הוא מחליף מינים אלקליים; עלות המעבר של שחקן ותיק מבוסס Rb היא מערכת לייזרים ודימות חדשה. השעון הנגזר במערך מלקחיים אופטיים אלקלי-עפרורי = סכום סבב הסינדרום (שערים 1 µs, הובלה 800 µs, שער חד-קיוביטי 0.34 µs, קריאה 501 µs) = 1.3 ms, מוגבל בהובלה, לעומת סבב שנמדד של ~1–4 ms. המשבצת הריקה הבולטת היא מפענח בזמן אמת המודע למחיקות, המוזן בסינדרומים חיים מהמערך.

## ראיות — כיצד נמדדו המספרים
השיעורים מגיעים מפלואורסצנציה בררנית-מצב לאחר השערים; נאמנות ה-CZ — מבחינת ביצועים אקראית או מטומוגרפיה, ומדווחת גולמית ובבחירה בדיעבד לפי הדגל. קוד מוציא מחזור תיקון על כל מחיקה מבושרת, ולכן המספרים הגולמיים הם שקובעים את העלות. הסתירה בין 1.9(4)× ל-3.6× נפתרת בתוך arXiv:2506.13724v2: שני הנתונים מופיעים במאמר זה ומתארים גדלים שונים — הדעיכה איטית 3.6(1)× במהלך ההחזקה עבור הקיוביט הלוגי שנבחר בדיעבד, ואיטית 1.9(4)× תחת פענוח בלתי מותנה עם מידע המחיקה [D][142]. רק ל-1.9(4)× יש משמעות ארכיטקטונית; הטקסט ב-Nature Physics נמצא מאחורי חומת תשלום [142]. הנתונים 56% (שער חד-קיוביטי, 2023) ו-38(6)% (CZ, 2026) הם מדדים שונים, ואין למצע אותם. לא נמצא שחזור עצמאי.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Atom Computing | מפתח | ארה״ב | מספקת מערכי ¹⁷¹Yb; Magne עם 1,225 אתרים | [C][154] |
| Princeton University | מחקר | ארה״ב | יזמה את ההמרה למחיקה ב-Yb; קיוביט לוגי [[4,2,2]] | [D][141], [142] |
| Caltech | מחקר | ארה״ב | השמטת מחיקות ב-Sr; CZ של 99.71% | [D][136], [143] |
| Microsoft | מפתח | ארה״ב | משווקת את Magne במשותף; מחסנית תיקון שגיאות ומפענח | [C][11] |
| Hamamatsu Photonics | ספק | יפן | SLM ומצלמות; המקור היחיד שזוהה | [P][335] |
| US Dept of Commerce | מאסדר | ארה״ב | מכתב כוונות של CHIPS; ECCN 4A906 | [G][300], [301] |

**כספים.**
2025-07-17 · QuNorth · הזמנת "Magne" — 1,225 פיזיים / 50 לוגיים — מ-Atom Computing/Microsoft · €80 M · EIFO + Novo Nordisk Foundation · הוזמן [C][11][G:MAGNE-2025-07]
2025-11-06 · Atom Computing · שלב B של DARPA QBI · עד $15 M · DARPA · הוענק [G][65][G:QBI-STAGEB-2025-11]
2026-05-21 · Atom Computing · מכתב כוונות של CHIPS · $100 M · US DoC, חבילה של $2.013 B · מכתב כוונות [G][300][G:CHIPS-LOI-2026-05]
2026-06-16 · Atom Computing · סבב C · $100 M · Third Point · במצטבר > $300 M · נסגר [C][154][G:ATOM-300M-2026-06]

**שוק ושרשרת אספקה.** אופטיקה ייעודית, לא צורן: לייזרים צרי-קו, AOD מוצלבים (רק שני ספקים נזכרים בכלל), SLM ומצלמות (ספק אחד), תאי UHV. אין נתון $/קיוביט פומבי; €80 M של QuNorth עבור 1,225 פיזיים / 50 לוגיים מרמזים על ≈ €65 k לאתר ועל ≈ €1.6 M לקיוביט לוגי [C][11]. G3 משלם עבור הטכנולוגיה הזאת, G4 בתנאים מסוימים, ו-G1 משותף עם מערכי Rb.

**קניין רוחני ותקנים.** לא נמצאה משפחת פטנטים מתוארכת הייחודית לקידוד מחיקה אלקלי-עפרורי; הפטנט הקרוב ביותר שהוענק הוא US 11,748,652 B1 של Amazon (2023-09-05), בישור של דעיכת ריסון משרעת במימושים מוליכי-על במסילה כפולה, לא באטומים [G][336][G:AMZN-ERASURE-PATENT]. לא זוהתה פעילות תקינה.

**מפות דרכים ועמידה בהבטחות.** Magne — 50 לוגיים (הובטח 2025-07-17 · למפנה 2026/27 · אין הודעת השלמה נכון ל-4 בספטמבר 2026) [R][11]; QuEra — 100 לוגיים (2024-01 · ל-2026 · הפך ל-Libra, >256 לוגיים, 2028) [R][162]; Pasqal — 10,000 פיזיים (2024-03 · ל-2026 · נדחה ל-2028, במימון SPAC של ~$360 M) [R][156]. Princeton עוברת ביקורת עמיתים ועקבית בעצמה; Atom Computing מספקת חומרה, אך ראתה את הדיכוי נעלם ברגע שנכללה טעינה מחדש [D][148].

**פרשנות אסטרטגית.** אם הטיית המחיקה תחזיק במרחק קוד, Yb/Sr ירוויחו יתרון מבני בתקורה בדרך ל-G3/G4 על פני השחקנים הוותיקים מבוססי Rb, שיצטרכו להחליף לייזרים ודימות או להמציא בישור מובנה ל-Rb; המין האטומי ש-Google טרם הצהירה עליו הוא הסימן [C][9]. ספקי האופטיקה מנצחים בכל מקרה, ולכן הדואופולים של AOD ושל המצלמות מחזיקים בכוח המיקוח היציב. איום התחליף הוא מחיקה במסילה כפולה במוליכי-על, עם שעון של ~500 ns, ורכישת Quantum Circuits בידי D-Wave תמורת $550 M היא ההימור [C][G:DWAVE-QCI-2026-01].

## תחזית ושאלות פתוחות
אבני דרך (12–24 חודשים): Magne מציגה 50 קיוביטים לוגיים תחת פענוח מוטה-מחיקה בפעולה עצמה, לא בבחירה בדיעבד (לאשר); קבוצה חיצונית משחזרת המרה של >50% בשער חד-קיוביטי (לאשר); מפענח בזמן אמת צורך את דגלי המחיקה של המערך בתוך תקציב המחזור (לאשר) — או שההמרה נעלמת תחת טעינה מחדש כפי ש-Λ נעלם (להוריד בדרגה). התרחיש הטוב ביותר ל-2029: מערכים עם מחיקה מובנית עומדים בבסיס מכונה של >100 קיוביטים לוגיים עם הפחתת תקורה מתוקפת; התרחיש הגרוע ביותר: ההמרה נשארת אפקט של שער בודד, ומחזור המילישניות מכריע את גורל הפלטפורמה. שאלות פתוחות: האם ההמרה שורדת טעינה מחדש בסקאלה של ms; האם הקידוד המטא-יציב יכול להשלים את גירעון השער של 6×; האם הספק הלכידה או רוחב הפס של ה-AOD יגבילו ראשונים מעל 10⁴. לעקוב: קבלת Magne, בחירת המין האטומי של Google, השחזור הראשון שאינו של Princeton.

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[9] H. Neven, “Building superconducting and neutral atom quantum computers,” Google, Mar. 24, 2026. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ [C]
[11] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[135] J. A. Muniz *et al.*, “High-fidelity universal gates in the ¹⁷¹Yb ground state nuclear spin qubit,” [arXiv:2411.11708](https://arxiv.org/abs/2411.11708), Nov. 2024. [D]
[136] R. B.-S. Tsai, X. Sun, A. L. Shaw, R. Finkelstein, and M. Endres, “Benchmarking and linear response modeling of high-fidelity Rydberg gates,” [arXiv:2407.20184](https://arxiv.org/abs/2407.20184), Jul. 2024. [D]
[140] J. Wang, Z. Wang, L. Li, F. Wang, S. Liang, and K. Yan, “Neutral Atom Quantum Computing: Principles, Routes, Progress, and Challenges,” [arXiv:2608.05010](https://arxiv.org/abs/2608.05010), Aug. 2026. [P]
[141] S. Ma *et al.*, “High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit,” *Nature*, vol. 622, p. 279, 2023, doi: [10.1038/s41586-023-06438-1](https://doi.org/10.1038/s41586-023-06438-1). [arXiv:2305.05493](https://arxiv.org/abs/2305.05493). [D]
[142] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[143] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[156] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [R]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [P]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[333] D. T. C. Allcock *et al.*, “omg blueprint for trapped ion quantum computing with metastable states,” *Appl. Phys. Lett.*, vol. 119, no. 21, Art. no. 214002, Nov. 2021, doi: [10.1063/5.0069544](https://doi.org/10.1063/5.0069544). [arXiv:2109.01272](https://arxiv.org/abs/2109.01272). [D]
[334] A. Kubica *et al.*, “Erasure Qubits: Overcoming the T₁ Limit in Superconducting Circuits,” *Phys. Rev. X*, vol. 13, no. 4, Art. no. 041022, Nov. 2023, doi: [10.1103/PhysRevX.13.041022](https://doi.org/10.1103/PhysRevX.13.041022). [arXiv:2208.05461](https://arxiv.org/abs/2208.05461). [D]
[335] M. Abdel-Kareem, “Hamamatsu Photonics, NKT Photonics, and Yaqumo Form Alliance to Industrialize Cold-Atom Quantum Core Components,” Quantum Computing Report, Jun. 4, 2026. [Online]. Available: https://quantumcomputingreport.com/hamamatsu-photonics-nkt-photonics-and-yaqumo-form-alliance-to-industrialize-cold-atom-quantum-core-components/ [P]
[336] A. M. Kubica and A. Retzker, “Heralding of amplitude damping decay noise for quantum error correction,” Google Patents, Sep. 5, 2023. [Online]. Available: https://patents.google.com/patent/US11748652B1/en [G]

## פריטי אימות פתוחים
הגרסה שפורסמה ב-Nature Physics של תוצאת ה-[[4,2,2]] של Princeton לא נקראה (מאחורי חומת תשלום); יישוב הסתירה בין 1.9(4)× ל-3.6(1)× נשען על arXiv v2 [142], שבו שני המספרים מופיעים עם הגדרות נפרדות. לא נמצא שחזור עצמאי של שיעור ההמרה של 56% או של 38(6)%. מצב ההתקנה של Magne מעבר להודעת ההזמנה מ-2025-07-17 לא אושר. האקסטרפולציה של הספק הלכידה ≈10 mW/אתר ל-10⁴ אתרים נגזרת מנתוני Fraunhofer ולא נמדדה [S]. אף ECCN אינו נוקב באופטיקת מלקחיים, ב-AOD או בתאי UHV; רק המערכת המוגמרת נתונה לפיקוח.
