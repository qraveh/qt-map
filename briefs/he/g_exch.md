---
id: g_exch
name: שער חילוף (ספינים; כולל CZ בספינים מוסעים)
layer: "3 מנגנון השער"
status: demonstrated
since: 2018
one_line: חילוף הייזנברג בפולסי מתח בין ספינים שכנים או מוסעים, בנקודות המוגדרות באלקטרודות שער או בדונורים — מנגנון השזירה היחיד שאינו צריך דבר מלבד אלקטרודות שער של CMOS.
verdict: ה-CNOT הטוב ביותר בחילוף הוא 9×10⁻⁴ (HRL, 18 קיוביטים), וזוגות בהתקני בית יציקה עומדים על 99.0–99.6%, אך ~80% מהשגיאה הדו-קיוביטית הם כיול ולא פיזיקה, ואף התקן של יותר משמונה קיוביטים אינו מפרסם נאמנות לכל הזוגות.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
פולס מתח מנמיך את מחסום המנהור בין שני ספינים שכנים של נקודות קוונטיות או של דונורים, ומפעיל חילוף הייזנברג J לזמן קצוב כדי לממש שער שזירה ממשפחת SWAP; דבר אינו מוקרן, ולכן אין צורך באנטנה, בלייזר או במהוד. Loss ו-DiVincenzo הציעו ב-1998 קיוביטי ספין המבוססים עליו; DiVincenzo, Bacon, Kempe, Burkard ו-Whaley הראו ב-2000 שהחילוף לבדו אוניברסלי, במחיר של ~3× יותר קיוביטים ו-~10× יותר פעולות דו-קיוביטיות — הקידוד ש-HRL בונה עליו [S][416]. הגרסה המוסעת מזיזה אלקטרון אחד דרך פוטנציאל מסוע אל טווח החילוף עם שותף מרוחק.
תכונות: נושא מיוצר לחלוטין; שזירה דטרמיניסטית ב-≈10⁻⁷ s (~100 ns), וכברירת מחדל צימוד סטטי בין שכנים קרובים.
בקרת מתח בפס בסיס, בטמפרטורת החדר אך בדרך לשלב הקריוגני; שגיאה קוהרנטית, פאולי, דליפה; הייצור הוא CMOS.

## פיזיקה וגבולות
J עולה באופן מעריכי ככל שהמחסום מונמך, וניתן לכוונון חשמלי מקרוב לאפס ועד עשרות MHz; זמן השער מתנהג כ-1/J, ולכן השערים הנמדדים נוחתים ב-58–500 ns עבור חילוף של 10–90 MHz. המעריכיות היא נקודת התורפה: אותו מנוף שהופך את J למהיר מגדיל את δJ/J תחת רעש מתח השער ורעש מלכודות המטען, ולכן יש נקודת עבודה ולא מקסימום — מעלים את J, ורעש המטען גורם לדה-פאזה של השער; מורידים אותו, והפולס הארוך יותר עושה זאת. מכאן הממצא של HRL שכ-80% מהשגיאה הדו-קיוביטית הם בקרה וכיול חיצוניים, לא דה-קוהרנטיות [D][190]. מתחת לזה נמצאים אמבט ה-²⁹Si השיורי, רעש מטען 1/f בממשק התחמוצת ופיצול עמקים קטן, ההופך את הדליפה לשגיאה מדרגה ראשונה. הזזת הרצפה דורשת העשרת ²⁸Si, ממשקים טובים יותר ובקר שמרחיק רעש 1/f מאלקטרודות המחסום.

## מצב ההנדסה העדכני
שער החילוף הטוב ביותר: ה-CNOT בחילוף בלבד של HRL — 9×10⁻⁴ כטוב ביותר הניתן לשחזור ו-3×10⁻³ בממוצע על פני 18 קיוביטים הבנויים מ-54 נקודות, שגיאה חד-קיוביטית ממוצעת של 2×10⁻⁴ — בתזמון של בקר ב-4 K בטכנולוגיית RF CMOS מסחרית של 130 nm [D][190]. בקנה מידה של בית יציקה, Diraq ו-imec מדווחות על 99.04–99.56% דו-קיוביטי ו-99.9% SPAM על SiMOS של 300 mm [D][189]. הגרסה המוסעת מוסיפה בדיקת זוגיות ממשקל ארבע ב-97.7% לכל הלוך-ושוב של 1.2 µm, והתנועה וזמן הסרק תורמים כרבע מהשגיאה שלה [D][349]. התקן הדונורים של SQC בן 11 הקיוביטים שונה במהותו: ספינים גרעיניים המצומדים בצימוד על-דק לאלקטרון משותף, ואוגרים המקושרים בחילוף [D][192]. שום התקן מעבר לשמונה קיוביטים אינו מפרסם נאמנות לכל הזוגות.

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2025-09 | דו-קיוביטי 99.04–99.56%, בית יציקה של 300 mm | Diraq עם imec | [D][189] |
| 2025-12 | 11 קיוביטים דונוריים, אוגרים המקושרים בחילוף | Silicon Quantum Computing | [D][192] |
| 2026-05 | CZ בספינים מוסעים, 98.86% ב-58 ns | QuTech | [D][193] |
| 2026-07 | CNOT בחילוף בלבד, 9×10⁻⁴ במיטבו, 18 קיוביטים | HRL Laboratories | [D][190] |

## ייצור, חומרים ושרשרת האספקה
הוא צריך רק אלקטרודות שער ופולסי מתח, ולכן הוא נשען על קווי ייצור קיימים: EUV של 300 mm ב-Intel (>24,000 התקנים לפרוסה [D][199]; 96% הצלחה בכוונון ב-232 התקנים בפרוסה אחת [D][766]), 300 mm ב-imec, 22FDX של GlobalFoundries, FD-SOI של STMicroelectronics. שני ריכוזים חשובים — GlobalFoundries קיבצה את הפלטפורמה ביחידה עסקית אחת, שמאחוריה מכתב כוונות של CHIPS בסך USD 375 M [C][353], ומחסנית הבקרה של Quantum Machines עומדת בבסיס העבודה של Diraq, HRL, imec, Equal1, Sandia וה-NQCC הבריטי [C][449]. החשיפה לפיקוח על יצוא ישירה: תקנת BIS מ-2024-09-06 יצרה את ECCN 3A901.a למעגלי CMOS *המתוכננים* לפעול ב-4.5 K או מתחת לכך — מבחן של כוונת התכנון, ולכן קובץ תכנון של בקר CMOS קריוגני מהסוג של HRL מפוקח כשלעצמו [G][301].

## בקרה, קריאה ועומס הקלט-פלט
נקודה כפולה צריכה בערך 4–6 ערוצי פס בסיס, ולכן בבקרה מטמפרטורת החדר החיווט גדל מהר יותר ממספר הקיוביטים; התשובה של HRL היא 296 קווים ו-366 DAC בתוך המקרר ב-≤3.5 W, בלי לולאת זמן אמת בטמפרטורת החדר [D][190]. הקריאה, לא השער, קובעת את המחזור: 1–100 µs לעומת שער של 58–500 ns. ב-10³ קיוביטים פריסת הקווים (fan-out) מטמפרטורת החדר אינה מעשית בלי אינטגרציה קריוגנית; ב-10⁴–10⁶ שיטות ה-crossbar המקטינות את מספר החוטים מתנגשות בצורך לכייל כל זוג חילוף בנפרד — ההתנגשות הארכיטקטונית הלא פתורה של המנגנון הזה.

## תפקיד במחסנית
הוא שוזר שתי משפחות: ספינים בנקודות קוונטיות בסיליקון ובגרמניום (Intel, Diraq, Quantum Motion, HRL בבעלות IBM, Quobly, Equal1) וספינים דונוריים (SQC). הוא דורש נקודה המוגדרת באלקטרודות שער או דונור, ועוד בקרה בפס בסיס, ומספק את שכבת השזירה ששתי המשפחות בונות עליה קודים — ב-HRL קוד חזרה במרחק 5 עם Λ(5/3) = 4.7 לאורך 200 סבבים, המגלה היפוכי ביט בלבד ולכן אינו תוצאה מתחת לסף עבור קוד מלא, ועוד [[4,2,2]] בבחירה בדיעבד בנאמנות לוגית של 0.95 [D][190]. הוא מתנגש במיעון crossbar, משום שהכיול נעשה לכל זוג בנפרד. הסבב הנגזר הוא 8.5 µs בספיני נקודות ו-7.7 µs בדונורים, מוגבל בידי הקריאה, לעומת ~100–300 µs שמריצים בדרך כלל: השער אינו צוואר הבקבוק. משבצת ריקה שכנה: תוצאה לכל הזוגות, על אותו שבב, מעבר לשמונה קיוביטים.

## ראיות — כיצד נמדדו המספרים
הנתונים הבולטים של HRL וחלוקת ה-80% לכיול מדווחים בידי הספק ולא שוחזרו [D][190]. ה-99.04–99.56% של Diraq ו-imec הוא סטטיסטיקה על אוכלוסיית התקני בית יציקה, לא תוצאה לכל הזוגות על אותו שבב; התקן שמונת הקיוביטים של imec מתקף חילוף בזוג אחד מתוך ארבעה [D][197]. הכתבה של Nature על קיוביטי ספין מיולי 2026 תוקנה ב-2026-08-04, ושיעורי השגיאה החד-קיוביטיים שיוחסו ל-HRL ול-QuTech עודכנו [P][450]. אין זיכרון לוגי מתחת לסף באף פלטפורמת ספין נכון ל-2026-09-04.

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Diraq | מפתח | אוסטרליה | שערים דו-קיוביטיים מבית יציקה של 300 mm, 99.04–99.56% | [D][189] |
| HRL Laboratories (IBM) | מפתח | ארה״ב | 18 קיוביטים בחילוף בלבד, בתזמון מ-4 K | [D][190] |
| QuTech | מחקר | הולנד | CZ בספינים מוסעים, בדיקות זוגיות עם קיוביט עזר נייד | [D][193] |
| Silicon Quantum Computing | מפתח | אוסטרליה | אוגרים דונוריים המקושרים בחילוף אלקטרונים | [D][192] |
| Quantum Motion | מפתח | בריטניה | מערכת מלאה (full-stack) על 22FDX ב-NQCC הבריטי | [C][355] |
| Quantum Machines | ספק | ישראל | מחסנית הבקרה שבבסיס רוב תוצאות הספין שפורסמו | [C][449] |

**כספים.**
- 2025-11-06 · DARPA · שלב B של QBI · ≤USD 15 M לכל אחת · Diraq, Quantum Motion, SQC מתוך אחת-עשרה · הוענק [G][65]
- 2026-05-07 · Quantum Motion · סבב C · USD 160 M · DCVC, Kembara · נסגר [C][355]
- 2026-05-21 · Diraq · מכתב כוונות של CHIPS · עד USD 38 M · US Commerce · מכתב כוונות, לא מענק [G][300]
- 2026-08-26 · IBM · מיזוג ורכישה, HRL Laboratories · התנאים לא פורסמו · נסגר [C][204]

**שוק ושרשרת אספקה.** אין לייזרים ואין ואקום: הציוד הוא קו CMOS ועוד אלקטרוניקת פס בסיס, ולכן שרשרת האספקה היא ארבעה קווי בית יציקה וספק בקרה אחד — טיעון עלות וסיכון ריכוזיות בבת אחת. ההבטחה של Diraq, "<USD 1 לקיוביט עד 2031", היא יעד, לא עלות [R][211]. כיום הוא מניע התקנים הנמכרים ל-G1 ול-G2; הרכישה של IBM היא הימור שהוא יגיע גם ל-G3 ול-G4.

**קניין רוחני ותקנים.** תוצאות היסוד — Loss–DiVincenzo מ-1998 והאוניברסליות של חילוף בלבד מ-2000 [S][416] — פורסמו ואינן קניין פרטי, ולכן הקניין הרוחני הניתן להגנה נמצא בגאומטריית ההתקן, בסיליקון של הבקרה הקריוגנית ובתוכנת הכיול. לא נמצאה ספירה מתוארכת של משפחות פטנטים הייחודית לשער הזה נכון ל-2026-09-04.

**מפות דרכים ועמידה בהבטחות.** Diraq (הובטח 2026-08-27 · 150 k פיזיים ו-1 k לוגיים עד 2029 · שישה שבועות קודם לכן אמרה אותה חברה "אלפים עד 2029") [R][211] — לא עקבי. Intel (הובטח 2026-01 · הגדלת Tunnel Falls ל"מאות נקודות" · אין המשך מתוארך) [C][207] — לא ניתן לדירוג. IBM (הובטח 2026-07-23 · סגירת רכישת HRL עד סוף הרבעון השלישי של 2026 · נסגרה 2026-08-26) [C][10], [204] — עמדה בהבטחה.

**פרשנות אסטרטגית.** אם שערי החילוף יגיעו לנאמנות של עמידות לתקלות, המנצחים יהיו בתי היציקה ומי שמחזיק בבקר הקריוגני — הקיוביט הופך לאפשרות בתהליך הייצור, לא למוצר — והמפסידים יהיו פלטפורמות שבסיס העלויות שלהן הוא אופטיקה וואקום. הרכישה של IBM הופכת את HRL לתוכנית הספין של ענקית ענן, ומאלצת את Diraq, Quantum Motion ו-Quobly להתחרות בכוח המאזן. אם נטל הכיול יימשך, הספינים יישארו קוריוז של G1/G2.

## תחזית ושאלות פתוחות
ניתן להפרכה בתוך 12–24 חודשים: לאשר/להוריד בדרגה לפי השאלה אם התקן מבית יציקה יפרסם נאמנות לכל הזוגות מעבר לשמונה קיוביטים, ואם IBM תציב אבן דרך מתוארכת לספינים במפת דרכים פומבית. התרחיש הטוב ביותר עד 2029: שבב מבית יציקה, בתזמון קריוגני, מציג זיכרון לוגי מתחת לסף עם קוד מלא. התרחיש הגרוע ביותר: האחידות נתקעת מעבר לעשרה קיוביטים, ומפות הדרכים נשארות שני סדרי גודל לפני החומרה. פתוח: האם שגיאת הכיול יכולה לרדת בלי לייבא את תקציב השגיאה של הבקר עצמו; האם CZ מוסע ידחק את החילוף הסטטי; מה IBM תעשה בסיליקון של HRL.

## מקורות
[10] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [C]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[189] P. Steinacker *et al.*, “Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity,” *Nature*, vol. 646, no. 8083, pp. 81–87, Sep. 2025, doi: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9). [D]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[192] H. Edlbauer *et al.*, “An 11-qubit atom processor in silicon,” *Nature*, vol. 648, no. 8094, pp. 569–575, Dec. 2025, doi: [10.1038/s41586-025-09827-w](https://doi.org/10.1038/s41586-025-09827-w). [arXiv:2506.03567](https://arxiv.org/abs/2506.03567). [D]
[193] Y. Matsumoto *et al.*, “Two-qubit logic and teleportation with mobile spin qubits in silicon,” *Nature*, vol. 653, no. 8114, pp. 391–397, May 2026, doi: [10.1038/s41586-026-10423-9](https://doi.org/10.1038/s41586-026-10423-9). [D]
[197] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[199] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[204] IBM, “IBM Completes Acquisition of HRL Laboratories to Accelerate the Future of Quantum,” Aug. 26, 2026. [Online]. Available: https://newsroom.ibm.com/2026-08-26-ibm-completes-acquisition-of-hrl-laboratories-to-accelerate-the-future-of-quantum [C]
[207] L. Hesla, “Argonne launches silicon quantum processor collaboration with Intel,” Argonne National Laboratory, Jan. 6, 2026. [Online]. Available: https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel [C]
[211] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[349] B. Undseth *et al.*, “Weight-four parity checks in a spin-shuttling architecture,” *Nature*, vol. 655, no. 8125, pp. 1160–1166, Jul. 2026, doi: [10.1038/s41586-026-10766-3](https://doi.org/10.1038/s41586-026-10766-3). [D]
[353] GlobalFoundries, “GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing,” May 21, 2026. [Online]. Available: https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ Also https://investors.gf.com/news-releases/news-release-details/globalfoundries-launches-quantum-technology-solutions-scale-us. [C]
[355] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[416] D. P. DiVincenzo, D. Bacon, J. Kempe, G. Burkard, and K. B. Whaley, “Universal quantum computation with the exchange interaction,” *Nature*, vol. 408, no. 6810, pp. 339–342, 2000, doi: [10.1038/35042541](https://doi.org/10.1038/35042541). [arXiv:quant-ph/0005116](https://arxiv.org/abs/quant-ph/0005116). [S]
[449] Quantum Machines, “Semiconductor Spin Qubits,” Aug. 11, 2026. [Online]. Available: https://www.quantum-machines.co/qubit-types/semiconductor-spin-qubits/ [C]
[450] D. Garisto, “Underdog 'spin qubits' leap forward in race to a useful quantum computer,” *Nature*, vol. 656, no. 8127, pp. 280–281, Aug. 2026, doi: [10.1038/d41586-026-02357-z](https://doi.org/10.1038/d41586-026-02357-z). [P]
[766] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]

## פריטי אימות פתוחים
חלקו של הכיול, ~80% מהשגיאה הדו-קיוביטית, הוא בדיווח עצמי של HRL, מספק יחיד, ולא שוחזר נכון ל-2026-09-04. סתירה בטווח הנאמנויות של SQC: תמצית ה-arXiv של [192] מציינת את כל הנאמנויות ב-99.5–99.99% ומצבי בל מעל 99%, ואילו הגרסה שפורסמה ב-Nature נותנת 99.10–99.99% עם מצבי בל עד 99.5%, והדוח הראשי מצטט CZ גרעיני דונורי יחיד של 99.90% — שלושה ניסוחים שונים של אותו ניסוי, ואת ה-99.90% לא ניתן היה לאתר בתמצית. התנאים הכספיים של רכישת HRL בידי IBM לא נחשפו לא בהודעה על העסקה ולא בהודעה על סגירתה. הסכום הכולל שגייסה Diraq (">USD 100 M") מגיע מהעיתונות המקצועית, לא מהודעה של החברה. לא נמצאה ספירה מתוארכת של משפחות פטנטים הייחודית לשערי חילוף.
