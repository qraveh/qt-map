---
id: g_lointer
name: אינטרפרומטר אופטי-ליניארי ניתן לתכנות (ללא פרימיטיב שזירה)
layer: "3 מנגנון השער"
status: demonstrated
since: 2020
one_line: "אוניטרי פסיבי ניתן לתכנות על N אופנים אופטיים — רשת של מפצלי אלומה ומזיזי פאזה או לולאות סיב במשבצות זמן — המפזר אור סחוט או פוטונים בודדים אל גלאים לצורך דגימה, ללא שער שזירה וללא הזנה קדימה."
verdict: "דוגם פועל, לא שער: 8,176 אופנים ועד 3,050 פוטונים שגולו (Jiuzhang 4.0, 2026). דוגם קלאסי שפורסם השתווה לכל טענת יתרון מוקדמת יותר על אמות המידה שלה עצמה; נכון ל-2026-09-26 לא נמצא דוגם כזה עבור Jiuzhang 4.0, ו-ORCA אינה מפרסמת נתון של אופנים, אובדן או שעון עבור PT-2."
updated: 2026-09-30
---

GBS = דגימת בוזונים גאוסית; MZI = אינטרפרומטר מאך–צנדר; EOM = מאפנן אלקטרו-אופטי; PNR = מבחין במספר הפוטונים; SNSPD = גלאי פוטון בודד מננו-תיל מוליך-על; TES = חיישן קצה-מעבר; MPS = מצב מכפלת מטריצות (רשת טנזורים); USTC = University of Science and Technology of China; NQCC = UK National Quantum Computing Centre; G1–G7 = מחלקות היעדים של הדוח (G1: סימולציה אנלוגית ו-NISQ).

## זהות ומוצא
רשת פסיבית ממפה אופני קלט לאופני פלט, a†ᵢ → Σⱼ Uⱼᵢ a†ⱼ, כאשר U אוניטרי N×N. Reck ועמיתיו פירקו כל U ל-N(N−1)/2 זוגות של מפצל אלומה ומזיז פאזה [G][452]; Clements ועמיתיו הקטינו את השטח בחצי ואיזנו את האובדן [G][453]; לולאות משתמשות מחדש בנקודת התאבכות אחת בכל משבצת זמן [G][454]. שבב של שישה אופנים ו-15 MZI מימש 100 אוניטריים אקראיים לפי מידת האר בנאמנות של 0.999 ± 0.001 [D][455]. מכונות על טכנולוגיה זו משתמשות ברשת לדגימה בלבד — פוטונים בודדים בעקבות Aaronson ו-Arkhipov [G][456], אור סחוט בעקבות Hamilton ועמיתיו [G][268]. תכונות: נושא מעופף, אין זמן שער ואין סיווג דטרמיניזם, שגיאה שבה שולט האובדן, בקרה אלקטרו-אופטית בטמפרטורת החדר, ייצור באופטיקה נפחית או במעגלים פוטוניים משולבים.

## פיזיקה וגבולות
הסתברויות הפלט הן פרמננטות של תת-מטריצות n×n של U; דגימה קלאסית מדויקת בזמן פולינומי הייתה ממוטטת את ההיררכיה הפולינומית, והקושי של הדגימה המקורבת נשען על שתי השערות [G][456]. עם קלט סחוט הן הפניאנים, גם הם #P-קשים [G][268]. הרשת שוזרת אופנים כשמזינים אותה באור סחוט [D][270], אך אין לה שער שזירה על קיוביטים מקודדים: אופטיקה ליניארית ללא פוטוני עזר מבחינה במצבי בל בהסתברות של 50% לכל היותר [G][457], והאוניברסליות דורשת הזנה קדימה מהגלאים [G][337]. הגבולות הם האובדן והניתנות להבחנה. העבירות מצטברת עם העומק: ב-0.99 לכל MZI, רשת Clements של 100 אופנים מעבירה ~0.37 [S][453]. GBS רועשת ניתנת לסימולציה יעילה ברגע שהסחיטה, העבירות ואיכות הגלאים מקיימות אי-שוויון מסוים [S][269]; רשתות טנזורים כנראה יעילות כאשר מספר הפוטונים השורדים גדל כמו √N עבור N אופני קלט [S][458]; בניתנות חלקית קבועה להבחנה, עלות הסימולציה גדלה רק באופן פולינומי עם מספר הפוטונים [S][459].

## מצב ההנדסה העדכני

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2015-05 | שבב אוניברסלי של שישה אופנים, נאמנות 0.999 ± 0.001 | Carolan ועמיתיו | [D][455] |
| 2020-12 | 50 מצבים סחוטים, 100 אופנים, עד 76 אירועי גילוי | USTC, Jiuzhang 1.0 | [D][460] |
| 2021-09 | דוגמים על תחנת עבודה עוקפים את Jiuzhang 1.0/2.0 במרחקי התפלגויות שוליות | Google Quantum AI | [S][461] |
| 2022-06-01 | 216 אופנים במשבצות זמן, שלוש לולאות, עד 219 פוטונים, עבירות ~33% | Xanadu, Borealis | [D][270] |
| 2023-10-10 | עד 255 אירועי גילוי; 1.27 µs לדגימה לעומת ~600 שנה על Frontier | USTC, Jiuzhang 3.0 | [D][462] |
| 2024-06-25 | דוגם MPS עוקף את Jiuzhang 2.0/3.0 ואת Borealis במתאמים; 288 GPU, ~72 min ל-10⁷ דגימות | Univ. of Chicago / Argonne | [S][463] |
| 2026-05-13 | 1,024 מצבים סחוטים, 8,176 אופנים, עד 3,050 פוטונים, 25.6 µs לדגימה | USTC, Jiuzhang 4.0 | [D][175] |

Jiuzhang 4.0 עונה למתקפת ה-MPS בנצילות — 92% במקור, 51% מקצה לקצה — שלפי הערכת המחברים דורשת ממד קשר מעל 8×10²¹, יותר מ-10⁴² שנה על El Capitan [S][175]; התיקוף נעשה על תת-מערכות, עם מרווח הגדל עם הגודל, ולא בקנה מידה מלא [D][175].

## ייצור, חומרים ושרשרת האספקה
Borealis בנויה מסיבים ומאופטיקה נפחית: שלושה קווי השהיה עם מפצלי אלומה משתנים המונעים ב-EOM של QUBIG GmbH, ו-16 גלאי TES ב-95% מאחורי מפלג של 1 ל-16 [D][270]. Jiuzhang 4.0 משרשרת שלושה אינטרפרומטרים של 16 אופנים דרך שני מערכים של לולאות השהיה אל 16 SNSPD ב-93% [D][175]. ORCA בונה מערכות במסד בטמפרטורת החדר מרכיבי סיב בדרגת תקשורת [C][464]. רק הגלאים קריוגניים. לא פורסם אובדן לרכיב של רשת דגימה המוצבת בשטח נכון ל-2026-09-26; העבירות של 99.8% ויחס ההכחדה של >40 dB המצוטטים עבור Jiuzhang 4.0 שייכים למסנן האור הסחוט שלה [D][175].

## בקרה, קריאה ועומס הקלט-פלט
Borealis מכוונת כל מפצל אלומה בלולאה לכל משבצת זמן של 167 ns, ודוגמת ב-10 kHz בין ייצובי הלולאות [D][270]. Jiuzhang 4.0 מכווננת את הרשתות שלה תרמית ואת פאזות הלולאות במותחי פיאזו; לא מדווחת הגדרה אלקטרו-אופטית לכל משבצת זמן [D][175], ולכן התכונה האלקטרו-אופטית של הטכנולוגיה מתאימה בעיקר ל-Borealis. הקריאה סופית; דבר אינו מוזן קדימה. ריבוב בזמן מנתק את הגלאים מהאופנים: 16 גלאים קוראים 216 או 8,176 אופנים [D][175], [270]. הקלט-פלט הכבד הוא קלאסי: בדיקה מדויקת של דגימה פירושה חישוב הפניאנים [G][268].

## תפקיד במחסנית
משבצת השער של ארכיטקטורת דוגם הבוזונים (ph_sampler, יעד G1). היא **דורשת** את photon (פוטונים בודדים או אור סחוט ברשת) ואת ct_eo (מזיזי פאזה ומתגים); היא אינה **מספקת** אף קשת — הפלט שלה הוא דגימה; היא אינה **מחליפה** דבר, ו-g_fusion מחליפה אותה (מיזוג מול אינטרפרומטר דגימה): אותה אופטיקה הופכת לשער רק כאשר תוצאות בל מבושרות (g_fusion) או תוצאות הומודיניות (g_cv) מוזנות קדימה. כך נסגר הפער G-lointer — לדוגמים הייתה שכבת שער שאין בה דבר הדומה לשער — בארכיטקטורה משלהם, ולא בטכנולוגיה שהוצעה ב-ph_cv וב-ph_fusion. מכונות המרשם, כולן ראשיות: Borealis (Xanadu, בהפעלה, 2022-06), Jiuzhang 4.0 (USTC, הודגם, 2026-05-13), PT-2 (ORCA, בהפעלה, 2024–2026). השעון הוא מחזור דגימה: 36 µs (Borealis), 25.6 µs (Jiuzhang 4.0) [D][175], [270].

## ראיות — כיצד נמדדו המספרים
אין שער שאפשר למדוד את ביצועיו; הדגימות מושוות להתפלגות האידיאלית, ואמות המידה שבהן נעשה שימוש — מתאמים מסדר נמוך, מרחקי התפלגויות שוליות — הושגו או נעקפו בדוגמים קלאסיים [S][461], [463]. תא ה-✅ של Borealis ותא ה-✅ של Jiuzhang 4.0 עומדים מול המאמרים שלהם, השני עם תיקון המסנן שתואר לעיל. PT-2 נשאר 🔎: דף הראיות שלו אינו נותן ארכיטקטורה [C][465]. התיאור היחיד שנמצא הוא של צד שלישי — מערך של לולאות השהיה בסיב עם מפצלי אלומה משתנים, המסוגל להפעיל שתי לולאות, בעוד המאמר ההוא מציב את המשטר הקשה קלאסית בשלוש, והדוגם מצבים סחוטים שמהם הופחת פוטון, עם גלאי PNR [P][271] — לא הפוטונים הבודדים שהמרשם רושם. מחקר על PT-1 ש-ORCA שותפה לכתיבתו השתמש בקו השהיה אחד [D][466].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| USTC | מפתח | סין | סדרת Jiuzhang; 4.0 מחברת רשתות של 16 אופנים עם מערכי לולאות השהיה, קריאה ב-SNSPD | [D][175] |
| Xanadu | מפתח | קנדה | Borealis: שלוש לולאות סיב המתוכנתות ב-EOM | [D][270] |
| ORCA Computing | מפתח | בריטניה | דוגמי לולאה במשבצות זמן מסדרת PT, במסד | [C][465] |
| QUBIG GmbH | ספק | גרמניה | רכיבי ה-EOM בלולאות של Borealis | [D][270] |
| Google Quantum AI; Univ. of Chicago / Argonne | מאתגרים קלאסיים | ארה״ב | דוגמים בהתאמת התפלגויות שוליות ודוגמי MPS | [S][461], [463] |

**כספים.**
- 2024-02-05 · NQCC · תחרות סביבות ניסוי בסך £30 M, ORCA אחת משבע הזוכות · הסכום לכל חברה לא פורסם · הוענק [G][467]
- 2024-06-05 · Montana State University · שתי מערכות PT-1, במימון US Air Force · לא פורסם · נחתם חוזה [C][468]
- 2025-06-11 · ORCA · סביבת הניסוי של NQCC הותקנה במסגרת היוזמה הבריטית בסך £121 M · לא פורסם · סופק [C][469]

**שוק ושרשרת אספקה.** מבין {{N_T_G_LOINTER_MACHINES}} המכונות במרשם, רק PT-1 ו-PT-2 של ORCA נמכרות כמערכות; USTC היא מוסד אקדמי, והמרשם מסמן את Borealis כמי שהוחלפה בידי Aurora. ORCA אינה מפרסמת את רוב גיוסי ההון שלה [P][470].

**קניין רוחני ותקנים.** לא נמצאו ספירת פטנטים ייחודית לדוגמים או תקן של אמות מידה נכון ל-2026-09-26.

**מפות דרכים ועמידה בהבטחות.** סביבות הניסוי של NQCC היו אמורות להיות מוכנות עד מרץ 2025 [G][467]; ORCA הודיעה על ההתקנה שלה ב-2025-06-11, רבעון מאוחר יותר [C][469]. PT-3 "צפויה לצאת בהמשך 2026" עם שלושה מודולים ניתנים למיתוג, ולפי הטענה תגבר על פותרים קלאסיים בבעיות של עד 25,000 משתנים [R][470].

**פרשנות אסטרטגית.** תחרות בין האובדן לסימולציה הקלאסית, לא דרך לחישוב; מה שנשאר הם הלולאות, מקורות הסחיטה והגלאים המבחינים במספר הפוטונים, שגם מכונות מיזוג ו-CV צריכות. אם PT-3 תגיע למשטר שלוש הלולאות עם אובדן שפורסם, ל-ORCA יהיה הדוגם המסחרי היחיד שמעבר לסימולציה קלה; אם לא, הטכנולוגיה תישאר אקדמית.

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 אף דוגם קלאסי לא ישתווה ל-Jiuzhang 4.0 באמות המידה של תת-המערכות שלה, ו-ORCA תפרסם את האופנים, הלולאות והאובדן של PT-3 עם השוואה קלאסית; להוריד בדרגה אם עד אז דוגם כזה ישתווה ל-Jiuzhang 4.0, או אם PT-3 תישלח ב-2026 בלי הנתונים האלה. שאלות פתוחות. (1) מהו האובדן לרכיב ברשתות הניתנות לתכנות של Jiuzhang 4.0? (2) האם התיקוף על תת-מערכות ניתן לאקסטרפולציה לקנה מידה מלא? (3) מה PT-2 מזריקה, ודרך כמה לולאות? (4) האם יישום GBS כלשהו שומר על האצה בעבירות של 33–51%? (5) האם דוגם לולאות יכול להפוך למכונת מיזוג בהוספת בישור והזנה קדימה?

## מקורות
[175] H.-L. Liu *et al.*, “Gaussian boson sampling with 1,024 squeezed states in 8,176 modes,” *Nature*, vol. 653, no. 8115, pp. 687–692, May 2026, doi: [10.1038/s41586-026-10523-6](https://doi.org/10.1038/s41586-026-10523-6). [arXiv:2508.09092](https://arxiv.org/abs/2508.09092). [D]
[268] C. S. Hamilton *et al.*, “Gaussian Boson Sampling,” *Phys. Rev. Lett.*, vol. 119, no. 17, Art. no. 170501, Oct. 2017, doi: [10.1103/PhysRevLett.119.170501](https://doi.org/10.1103/PhysRevLett.119.170501). [arXiv:1612.01199](https://arxiv.org/abs/1612.01199). [G]
[269] H. Qi, D. J. Brod, N. Quesada, and R. García-Patrón, “Regimes of Classical Simulability for Noisy Gaussian Boson Sampling,” *Phys. Rev. Lett.*, vol. 124, no. 10, Art. no. 100502, Mar. 2020, doi: [10.1103/PhysRevLett.124.100502](https://doi.org/10.1103/PhysRevLett.124.100502). [arXiv:1905.12075](https://arxiv.org/abs/1905.12075). [S]
[270] L. S. Madsen *et al.*, “Quantum computational advantage with a programmable photonic processor,” *Nature*, vol. 606, no. 7912, pp. 75–81, Jun. 2022, doi: [10.1038/s41586-022-04725-x](https://doi.org/10.1038/s41586-022-04725-x). [D]
[271] J. Park, S. Stepney, and I. D'Amico, “Benchmarking the ORCA PT-2 Boson Sampler using Minimum Dominating Set Problems,” [arXiv:2605.30935](https://arxiv.org/abs/2605.30935), May 2026. [P]
[337] E. Knill, R. Laflamme, and G. Milburn, “Efficient Linear Optics Quantum Computation,” *Nature*, vol. 409, pp. 46–52, Jun. 2000, doi: [10.1038/35051009](https://doi.org/10.1038/35051009). [arXiv:quant-ph/0006088](https://arxiv.org/abs/quant-ph/0006088). [G]
[452] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, “Experimental realization of any discrete unitary operator,” *Phys. Rev. Lett.*, vol. 73, no. 1, pp. 58–61, Jul. 1994, doi: [10.1103/PhysRevLett.73.58](https://doi.org/10.1103/PhysRevLett.73.58). [G]
[453] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, “Optimal design for universal multiport interferometers,” *Optica*, vol. 3, no. 12, p. 1460, Dec. 2016, doi: [10.1364/OPTICA.3.001460](https://doi.org/10.1364/OPTICA.3.001460). [arXiv:1603.08788](https://arxiv.org/abs/1603.08788). [G]
[454] K. R. Motes, A. Gilchrist, J. P. Dowling, and P. P. Rohde, “Scalable Boson Sampling with Time-Bin Encoding Using a Loop-Based Architecture,” *Phys. Rev. Lett.*, vol. 113, no. 12, Art. no. 120501, Sep. 2014, doi: [10.1103/PhysRevLett.113.120501](https://doi.org/10.1103/PhysRevLett.113.120501). [arXiv:1403.4007](https://arxiv.org/abs/1403.4007). [G]
[455] J. Carolan *et al.*, “Universal Linear Optics,” [arXiv:1505.01182](https://arxiv.org/abs/1505.01182), May 2015. [D]
[456] S. Aaronson and A. Arkhipov, “The Computational Complexity of Linear Optics,” *Theory of Computing*, vol. 9, pp. 143–252, 2013, doi: [10.4086/toc.2013.v009a004](https://doi.org/10.4086/toc.2013.v009a004). [arXiv:1011.3245](https://arxiv.org/abs/1011.3245). [G]
[457] J. Calsamiglia and N. Lütkenhaus, “Maximum efficiency of a linear-optical Bell-state analyzer,” *Appl. Phys. B*, vol. 72, no. 1, pp. 67–71, Jan. 2001, doi: [10.1007/s003400000484](https://doi.org/10.1007/s003400000484). [arXiv:quant-ph/0007058](https://arxiv.org/abs/quant-ph/0007058). [G]
[458] M. Liu, C. Oh, J. Liu, L. Jiang, and Y. Alexeev, “Simulating lossy Gaussian boson sampling with matrix-product operators,” *Phys. Rev. A*, vol. 108, no. 5, Art. no. 052604, Nov. 2023, doi: [10.1103/PhysRevA.108.052604](https://doi.org/10.1103/PhysRevA.108.052604). [arXiv:2301.12814](https://arxiv.org/abs/2301.12814). [S]
[459] J. J. Renema *et al.*, “Efficient Classical Algorithm for Boson Sampling with Partially Distinguishable Photons,” *Phys. Rev. Lett.*, vol. 120, no. 22, Art. no. 220502, May 2018, doi: [10.1103/PhysRevLett.120.220502](https://doi.org/10.1103/PhysRevLett.120.220502). [arXiv:1707.02793](https://arxiv.org/abs/1707.02793). [S]
[460] H.-S. Zhong *et al.*, “Quantum computational advantage using photons,” *Science*, vol. 370, no. 6523, pp. 1460–1463, Dec. 2020, doi: [10.1126/science.abe8770](https://doi.org/10.1126/science.abe8770). [arXiv:2012.01625](https://arxiv.org/abs/2012.01625). [D]
[461] B. Villalonga *et al.*, “Efficient approximation of experimental Gaussian boson sampling,” [arXiv:2109.11525](https://arxiv.org/abs/2109.11525), Sep. 2021. [S]
[462] Y.-H. Deng *et al.*, “Gaussian Boson Sampling with Pseudo-Photon-Number-Resolving Detectors and Quantum Computational Advantage,” *Phys. Rev. Lett.*, vol. 131, no. 15, Art. no. 150601, Oct. 2023, doi: [10.1103/PhysRevLett.131.150601](https://doi.org/10.1103/PhysRevLett.131.150601). [arXiv:2304.12240](https://arxiv.org/abs/2304.12240). [D]
[463] C. Oh, M. Liu, Y. Alexeev, B. Fefferman, and L. Jiang, “Classical algorithm for simulating experimental Gaussian boson sampling,” *Nat. Phys.*, vol. 20, pp. 1461–1468, Jun. 2024, doi: [10.1038/s41567-024-02535-8](https://doi.org/10.1038/s41567-024-02535-8). [arXiv:2306.03709](https://arxiv.org/abs/2306.03709). [S]
[464] ORCA Computing, “Technology — ORCA Computing.” [Online]. Available: https://orcacomputing.com/technology/ [C]
[465] ORCA Computing, “ORCA PT-2 — ORCA Computing.” [Online]. Available: https://orcacomputing.com/orca-pt-2/ [C]
[466] A. Makarovskiy *et al.*, “A Binary Optimisation Algorithm for Near-Term Photonic Quantum Processors,” [arXiv:2510.08274](https://arxiv.org/abs/2510.08274), Oct. 2025. [D]
[467] National Quantum Computing Centre, “Science Minister Andrew Griffith announces the results of the £30m quantum computing testbed competition,” NQCC, Feb. 5, 2024. [Online]. Available: https://www.nqcc.ac.uk/updates/science-minister-andrew-griffith-announces-the-results-of-the-30m-quantum-computing-testbed-competition/ [G]
[468] ORCA Computing, “Montana State University Selects ORCA Computing to Advance Distributed Quantum Computing and Communications,” Jun. 5, 2024. [Online]. Available: https://orcacomputing.com/montana-state-university-selects-orca-computing/ [C]
[469] ORCA Computing, “ORCA Computing Delivers First Photonic Quantum Computing System to UK's National Quantum Computing Centre,” Jun. 11, 2025. [Online]. Available: https://orcacomputing.com/installation-marks-key-milestone-in-the-uks-121m-quantum-initiative-advancing-practical-quantum-research/ [C]
[470] Tech Journal UK, “ORCA aims to beat classical computers with PT-3 quantum system,” Jul. 1, 2026. [Online]. Available: https://www.techjournal.uk/p/orca-aims-to-beat-classical-computers [R]

## פריטי אימות פתוחים
- דפי התמצית ב-arXiv של 2605.30935 ושל 2109.11525 לא נטענו ב-2026-09-26; החודשים נלקחו מהמזהים, והכותרות והמחברים מגרסת ה-HTML של הטקסט המלא.
- דגם המערכת ב-NQCC: ההודעה של ORCA מ-2025-06-11 אומרת רק "PT Series"; דף ה-PT-2 מציין את סביבת הניסוי של NQCC כהצבה מ-2025 (נבדק 2026-09-26).
- מצב הקלט של PT-2: "מצבים סחוטים שמהם הופחת פוטון" של הצד השלישי סותר את "פוטונים בודדים (SPDC)" שבמרשם; אף מקור ראשוני של ORCA אינו מכריע בכך (חיפוש מ-2026-09-26).
- בחיפוש ב-2026-09-26 לא נמצאה הפרכה קלאסית של Jiuzhang 4.0; ייתכן שקיים קדם-פרסום שאינו מאונדקס.
