---
id: code_mitig
name: אפחות שגיאות במשבצת הקוד (ZNE, PEC) — אינו קוד
layer: "7 קוד"
status: demonstrated
since: 2017
one_line: "עיבוד קלאסי בדיעבד של ריצות רועשות רבות — אקסטרפולציה לרעש אפס, ביטול או הגברה הסתברותיים של שגיאות, סחרור הקריאה, היפוך הרעש ברשתות טנזורים — המסיר את ההטיה מערכי תוחלת בלי לקודד, לגלות או לתקן אף שגיאה אחת."
verdict: "הטיפול היחיד בשגיאות ברוב הניסויים במוליכי-על בקנה מידה של תועלת, ובהם שתיים משלוש טענות היתרון של IBM מיולי 2026; הוא קונה הפחתת הטיה בעלות יריות מעריכית במסת השגיאה של המעגל, ואינו מניב אף קיוביט לוגי, ולכן נכון ל-2026-09-26 הוא ממלא מקום של קוד, לא צעד לקראתו."
updated: 2026-09-30
---

ZNE = אקסטרפולציה לרעש אפס (zero-noise extrapolation); PEC = ביטול שגיאות הסתברותי (probabilistic error cancellation); PEA = הגברת שגיאות הסתברותית (probabilistic error amplification); TREX = הכחדת שגיאות קריאה בסחרור (twirled readout error extinction); TEM = אפחות שגיאות ברשתות טנזורים (tensor-network error mitigation); γ = הנורמה של התערובת בעלת המשקלים החיוביים והשליליים שהופכת את הרעש; P = סכום הסתברויות שגיאות הפאולי בחרוט האור האחורי של גודל נצפה (השערים שיכולים להשפיע עליו); CZ = שער Z מבוקר; G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
אפחות שגיאות מעריך את ערך התוחלת חסר הרעש של גודל נצפה מתוך ריצות רועשות רבות ועיבוד קלאסי בדיעבד; דבר אינו מקודד, שום סינדרום אינו נמדד ושום שגיאה אינה מתוקנת [G][693]. Temme, Bravyi ו-Gambetta הציעו ב-2016 אקסטרפולציה לרעש אפס בשיטת ריצ'רדסון וביטול בדגימה חוזרת לפי קוואזי-הסתברויות [D][694]; Li ו-Benjamin ביצעו, באופן בלתי תלוי, אקסטרפולציה לאפס של שגיאות מוגברות [D][695]. ZNE על חומרה הגיעה ב-2019 [D][696]; אחריה באו PEA, המגבירה מודל רעש נלמד בעזרת שגיאות פאולי מוזרקות [D][308], TREX לקריאה [C][693] ו-TEM, היפוך של הרעש הגלובלי ברשת טנזורים [S][697]. תכונות: אדיש לפלטפורמה, סטטי, ללא הובלה וללא אופן בקרה; מחלקת השגיאה היא פאולי לאחר סחרור.

## פיזיקה וגבולות
PEC כותב את הרעש ההופכי של כל שכבה כתערובת של פעולות ברות-מימוש במשקלים חיוביים ושליליים, בנורמה γ ≥ 1; האומדן חסר הטיה, אך מספר היריות גדל כ-γ², ו-γ גדל מעריכית עם העומק [C][693]. לרעש פאולי γ ≈ e^(2P), ולכן מספר היריות מוכפל פי ≈ e^(4P) [S]. בשגיאת CZ חציונית של 0.15% ב-Heron r3 [D][698], חרוט אור עם 1,000 שערי CZ נותן P ≈ 1.5 ומכפיל יריות של ≈ 400×, ו-7,500 שערים נותנים ~10¹⁹× [S]; תקציבי היום, 10²–10³×, מגבילים את P לסביבות 1.2–1.7 [S]. ZNE דוגמת ברעש מוגבר — כברירת מחדל בשלושה מקדמי הגברה, נומינלית ~3× [C][693] — ומבצעת אקסטרפולציה; היא מוטה בגלל התאמת העקומה שלה וחייבת להבחין באות שהונחת בגורם של עד e^(−2P), ולכן עלותה גדלה באופן דומה [S]. TEM טוען לשורש הריבועי של התקורה של PEC [S][697] — עדיין מעריכית [S]. המגבלה כללית: תחת רעש דה-פולריזציה מקומי, התקורה של כל פרוטוקול גדלה מעריכית עם העומק [D][699], כולל עיבוד בדיעבד לא-ליניארי [D][700], ואמידה במקרה הגרוע דורשת מספר דגימות על-פולינומי כבר בעומק רדוד [D][701]. רק שגיאה פיזית נמוכה יותר מזיזה את המעריך.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2019-03-27 | ZNE באמצעות פולסים מוארכים; כימיה ומגנטיות בשיטות וריאציוניות | IBM, Kandala et al. | [D][696] |
| 2023-05-08 | PEC עם מודל פאולי–לינדבלד דליל נלמד, כולל הפרעה הדדית, 20 קיוביטים | IBM, van den Berg et al. | [D][702] |
| 2023-06-14 | 127 קיוביטים, עד 60 שכבות, 2,880 שערי CNOT; ZNE עם PEA | IBM Eagle, Kim et al. | [D][308] |
| 2023-06/08 | שחזורים קלאסיים: רשת טנזורים מדויקת יותר מהחומרה; דינמיקת פאולי על ליבה אחת של מחשב נייד; התכנסות עד כדי <0.01 | Tindall et al.; Begušić, Chan; Begušić, Gray, Chan | [D][309][D][703][D][704] |
| 2025-11-12 | "samplomatic" מקצץ את תקורת הדגימה של PEC ב-100× | IBM | [C][486] |
| 2026-07-27 | QESEM (מבוסס PEC ו-ZNE) על Heron r3, 51–74 קיוביטים, עד 30 מחזורי פלוקה; רשתות טנזורים אינן מתכנסות | Qedma, RIKEN, BlueQubit | [D][233] |
| 2026-07-28 | PEC על 56 קיוביטים, מעגלים של עד ~1,000 שערי CZ: ~1.5 h ו-~4 h של זמן QPU בשני עומקים | Algorithmiq et al., ibm_boston | [D][698] |
| 2026-08-31 | אמידת גדלים נצפים עם PEA על מעגלים של 7,500 שערים | IBM Nighthawk r2 | [C][601] |

חישוב קלאסי השתווה בתוך שבועות לדיוק שנטען ב-2023, "מעבר לחישוב קלאסי בכוח גס" [D][308], וערכים מתכנסים חשפו הטיה באקסטרפולציה שעליה נשענה הטענה [D][704]; הטענות של 2026 מבוססות על אי-הסכמה בין היוריסטיקות קלאסיות, לא על קושי מוכח [D][698]. האיבר השולט: P. יריות מהירות יותר — 100,000 המעגלים לשנייה של Nighthawk r2, 25× לעומת Heron — מקצרות את זמן הריצה בפועל, לא את המעריך [C][601].

## ייצור, חומרים ושרשרת האספקה
דבר אינו מיוצר; החשבון הוא זמן QPU וחישוב קלאסי — 3.2 מיליון יריות, ~45 min של זמן QPU לכל נקודה באומדן של Algorithmiq לאחר שינוי קנה המידה [D][698]. האספקה היא סביבת הריצה (runtime) של הספק [C][693], ועוד QESEM של Qedma, הלומד את רעש ההתקן, מתאים את המעגלים ומבצע עיבוד בדיעבד [C][705], ו-TEM של Algorithmiq ב-Qiskit Functions Catalog של IBM [C][706].

## בקרה, קריאה ועומס הקלט-פלט
הדרישה היא מודל רעש מכויל ויציב: PEA ו-PEC לומדים מודל פאולי–לינדבלד דליל לכל שכבה של שערי שזירה תחת סחרור פאולי אקראי [D][308][D][702]; כל מעגל מהודר במופעים אקראיים רבים [S]. TREX מוסיף אקראיות למדידות בעזרת שערי X והיפוכי ביטים קלאסיים, ובכך מלכסן את מטריצת הקריאה לשם היפוכה [C][693]. אופן הכשל הוא סחיפה: מודל שנלמד לפני ריצת PEC בת ארבע שעות שגוי בכל מה שנסחף במהלכה [S]. אין הזנה קדימה, והפלט הוא ערכי תוחלת, לא דגימות [G][693].

## תפקיד במחסנית
משבצת 7 בארכיטקטורה "סריג טרנסמונים עם מצמדים ברי-כוונון", לצד code_surface, code_color, code_qldpc, code_magic ו-code_detect. הוא **דורש** את ct_rt, לשם מודלי רעש מכוילים; הוא אינו **מספק** דבר לשכבות שמעליו — לא קיוביט לוגי ולא סינדרום למפענחים של משבצת 8; הוא **מוחלף** בידי code_surface, וקשת ההתנגשות הפתוחה (2023-06) אינה מציינת שום מענה לתקורה המעריכית שלו. code_detect משליך ריצות מסומנות בעלות של ההופכי של שיעור הקבלה, גם היא מעריכית בגודל המעגל; האפחות שומר כל ריצה ומשקלל אותה מחדש, ומסיר את ההטיה רק בממוצע [S]. הניסוח "כל שלוש טענות היתרון של IBM מיולי 2026" בפנקס הפערים נכון בפועל לשתיים משלוש — QESEM על Heron r3 [D][233] ו-PEC על ibm_boston [D][698]; הטענה של IBM–UChicago נשענת על בחירה בדיעבד בקודי מרחב-זמן, והיא תוצאה של code_detect [C][45]. השיבוץ ביונים שהציע הפנקס לא אומץ, אף ש-Qedma חזרה על המחזורים ב-Quantinuum H2 וב-Helios [D][233]. המרשם: IBM Eagle r1–r3 (ראשית, הוצאה משימוש); Heron r3 ו-Nighthawk r2 (חלופית).

## ראיות — כיצד נמדדו המספרים
PEC חסר הטיה ומספק קווי שגיאה, אם מודל הרעש שלו נכון, ולכן האימות הופך לתיקוף המודל [C][45]. מבין {{N_T_CODE_MITIG_MACHINES}} תאי המרשם, התאים של Heron r3 ושל Nighthawk r2 מאומתים ✅ — הראשון בטרום-הפרסומים על ibm_boston מיולי 2026 [D][233], [698], השני בסעיף של הבלוג על r2 [C][601] — והתא של Eagle אינו מאומת (🔎), אף שהמקור שלו תומך בו [D][308]. Heron r1 ו-Nighthawk r1 אינן נושאות קוד: אין מקור ראשוני המראה שיטת אפחות מוגדרת שהורצה על r1 עצמה, והכתבה העיתונאית על r3 שהתא שלה מצטט אינה נוקבת בשום שיטה כזאת [P][707]. Zuchongzhi 3.0 ו-Tianyan-287 מריצות דגימת מעגלים אקראיים המדורגת לפי נאמנות גולמית; התמציות שלהן אינן מזכירות לא אפחות ולא תיקון [D][35][D][708], ולכן נכון ל-2026-09-26 משבצת הקוד שלהן ריקה, ולא תפוסה בידי אפחות.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| IBM | מפתח | ארה״ב | TREX, ZNE, PEA, PEC ב-Qiskit Runtime; ניסוי ה"תועלת" מ-2023; PEA ב-7,500 שערים | [C][693][D][308][C][601] |
| Qedma | ספק תוכנה | ישראל | QESEM: למידת רעש, אומדים מבוססי PEC ו-ZNE | [D][233] |
| Algorithmiq | ספק תוכנה | איטליה (לשעבר פינלנד) | TEM בקטלוג של IBM; PEC בטענה המבוססת על הד לושמידט | [C][706][D][698] |
| Flatiron Institute | מחקר | ארה״ב | תורם למעקב הפתוח אחר טענות היתרון | [C][486] |

**כספים.**
- 2025-07-03 · Qedma · סבב A בהובלת Glilot Capital Partners, בהשתתפות IBM · USD 26 M · הוכרז [C][705]
- 2026-05-11 · Algorithmiq · סבב בהובלת United Ventures, עם CDP ו-Inventure · EUR 18 M (EUR 36 M בסך הכול) · הוכרז [C][709]

**שוק ושרשרת אספקה.** נמכר כאפשרויות של סביבת הריצה וכפונקציות של צד שלישי בענן של ספק החומרה, כש-IBM מחזיקה במניות של Qedma: שוק קשור אנכית. רק G2 משלם עליו; G3–G4 זקוקים לקוד.

**קניין רוחני ותקנים.** שום תקן אינו מגדיר מדד איכות לאומדנים לאחר אפחות או פורמט לחשיפת מודל הרעש; אין ספירת פטנטים מתוארכת ממאגר נקוב בשמו, נכון ל-2026-09-26.

**מפות דרכים ועמידה בהבטחות.** IBM הבטיחה גרסאות של Nighthawk ב-5,000, 7,500, 10,000 ו-15,000 שערים [R][486]; צעד ה-7,500 שערים, אבן הדרך שלה ל-2026, סופק ב-2026-08-31 עם PEA [C][601].

**פרשנות אסטרטגית.** האפחות הופך את מודל הרעש למוצר ומשאיר את הערך בתוך המחסנית של ספק החומרה. רק למידת הרעש עוברת לסבילות לתקלות; כשקוד רץ, הטכנולוגיה מתרוקנת מתוכן.

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 יופיע אומדן PEC חסר הטיה על ≥5,000 שערים עם קווי שגיאה, או אם טענה מיולי 2026 תשרוד עד 2027-07-31 ללא שחזור קלאסי מתכנס; להוריד בדרגה את הטענות האלה לכדי "תועלת" אם ערכים מתכנסים של רשתות טנזורים או של התפשטות פאולי יתאימו להן, כמו ב-2023.
שאלות פתוחות. (1) עד כמה יציב מודל פאולי–לינדבלד נלמד לאורך ריצה של כמה שעות ב-10³–10⁴ שערים? (2) האם החיסכון הריבועי של TEM שורד את שגיאת המודל בחומרה? (3) מאיזה גודל קוד גילוי בתוספת אפחות גובר על אפחות לבדו במספר היריות? (4) האם אפשר להוכיח שמשימה של ערך תוחלת לאחר אפחות קשה קלאסית? (5) איזה מכפיל יריות הוציאה ריצת ה-PEA של 7,500 השערים על Nighthawk r2?

## מקורות
[35] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[45] A. Kandala, A. Javadi-Abhari, and J. Gambetta, “Researchers demonstrate quantum advantage through trusted quantum computation,” IBM Quantum Computing Blog, Jul. 30, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-advantage [C]
[233] E. Leviatan *et al.*, “Resolving Structure in Prethermal Floquet Dynamics with Precision Quantum Computation,” [arXiv:2607.24937](https://arxiv.org/abs/2607.24937), Jul. 2026. [D]
[308] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[309] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[486] R. Mandelbaum, “Scaling for quantum advantage and beyond,” IBM Quantum Computing Blog, Nov. 12, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/qdc-2025 [C]
[601] H. Haas, D. McKay, and R. Davis, “IBM Quantum Nighthawk r2—more circuits, faster,” IBM Quantum Computing Blog, Aug. 31, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/nighthawk-r2 [C]
[693] IBM, “Error mitigation and suppression techniques.” [Online]. Available: https://quantum.cloud.ibm.com/docs/en/guides/error-mitigation-and-suppression-techniques [C]
[694] K. Temme, S. Bravyi, and J. M. Gambetta, “Error mitigation for short-depth quantum circuits,” *Phys. Rev. Lett.*, vol. 119, Art. no. 180509, 2017, doi: [10.1103/PhysRevLett.119.180509](https://doi.org/10.1103/PhysRevLett.119.180509). [arXiv:1612.02058](https://arxiv.org/abs/1612.02058). [D]
[695] Y. Li and S. C. Benjamin, “Efficient Variational Quantum Simulator Incorporating Active Error Minimization,” *Phys. Rev. X*, vol. 7, no. 2, Art. no. 021050, Jun. 2017, doi: [10.1103/PhysRevX.7.021050](https://doi.org/10.1103/PhysRevX.7.021050). [arXiv:1611.09301](https://arxiv.org/abs/1611.09301). [D]
[696] A. Kandala *et al.*, “Error mitigation extends the computational reach of a noisy quantum processor,” *Nature*, vol. 567, pp. 491–495, Mar. 2019, doi: [10.1038/s41586-019-1040-7](https://doi.org/10.1038/s41586-019-1040-7). [arXiv:1805.04492](https://arxiv.org/abs/1805.04492). [D]
[697] S. Filippov, M. Leahy, M. A. C. Rossi, and G. García-Pérez, “Scalable tensor-network error mitigation for near-term quantum computing,” [arXiv:2307.11740](https://arxiv.org/abs/2307.11740), Jul. 2023. [S]
[698] S. V. Barron *et al.*, “Observable Estimation in the Absence of Classical Verification,” [arXiv:2607.25998](https://arxiv.org/abs/2607.25998), Jul. 2026. [D]
[699] R. Takagi, S. Endo, S. Minagawa, and M. Gu, “Fundamental limits of quantum error mitigation,” *npj Quantum Inf.*, vol. 8, Art. no. 114, 2022, doi: [10.1038/s41534-022-00618-z](https://doi.org/10.1038/s41534-022-00618-z). [arXiv:2109.04457](https://arxiv.org/abs/2109.04457). [D]
[700] R. Takagi, H. Tajima, and M. Gu, “Universal Sampling Lower Bounds for Quantum Error Mitigation,” *Phys. Rev. Lett.*, vol. 131, Art. no. 210602, 2023, doi: [10.1103/PhysRevLett.131.210602](https://doi.org/10.1103/PhysRevLett.131.210602). [arXiv:2208.09178](https://arxiv.org/abs/2208.09178). [D]
[701] Y. Quek, D. S. França, S. Khatri, J. J. Meyer, and J. Eisert, “Exponentially tighter bounds on limitations of quantum error mitigation,” *Nat. Phys.*, vol. 20, p. 1648, 2024, doi: [10.1038/s41567-024-02536-7](https://doi.org/10.1038/s41567-024-02536-7). [arXiv:2210.11505](https://arxiv.org/abs/2210.11505). [D]
[702] E. van den Berg, Z. K. Minev, A. Kandala, and K. Temme, “Probabilistic error cancellation with sparse Pauli–Lindblad models on noisy quantum processors,” *Nat. Phys.*, vol. 19, no. 8, pp. 1116–1121, May 2023, doi: [10.1038/s41567-023-02042-2](https://doi.org/10.1038/s41567-023-02042-2). [arXiv:2201.09866](https://arxiv.org/abs/2201.09866). [D]
[703] T. Begušić and G. K.-L. Chan, “Fast classical simulation of evidence for the utility of quantum computing before fault tolerance,” [arXiv:2306.16372](https://arxiv.org/abs/2306.16372), Jun. 2023. [D]
[704] T. Begušić, J. Gray, and G. K.-L. Chan, “Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance,” *Sci. Adv.*, Art. no. eadk4321, 2024, doi: [10.1126/sciadv.adk4321](https://doi.org/10.1126/sciadv.adk4321). [arXiv:2308.05077](https://arxiv.org/abs/2308.05077). [D]
[705] QEDMA, “QEDMA raises $26M with participation from IBM to tackle quantum computing errors and accelerate pace to quantum advantage,” PR Newswire, Jul. 3, 2025. [Online]. Available: https://www.prnewswire.com/news-releases/qedma-raises-26m-with-participation-from-ibm-to-tackle-quantum-computing-errors-and-accelerate-pace-to-quantum-advantage-302497701.html [C]
[706] Algorithmiq, “Algorithmiq Launches High-Performing Error Mitigation Solution in IBM's Qiskit Functions Catalog,” Sep. 16, 2024. [Online]. Available: https://www.algorithmiq.fi/news/press-release-tem-ibm-qiskit-functions/ [C]
[707] M. Ivezic, “IBM Launches Heron R3 (ibm_pittsburgh): ~350 uS T2 and a Quality Upgrade for Its 156-Qubit Platform,” PostQuantum.com, Aug. 1, 2025. [Online]. Available: https://postquantum.com/industry-news/ibm-heron-r3-pittsburgh/ [P]
[708] T. Q. Group, “Tianyan: Cloud services with quantum advantage,” [arXiv:2512.10504](https://arxiv.org/abs/2512.10504), Dec. 2025. [D]
[709] Algorithmiq, “Algorithmiq Establishes Milan Headquarters and raises €18m to Position Europe as the Future of Quantum Software,” May 11, 2026. [Online]. Available: https://algorithmiq.fi/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software/ [C]

## פריטי אימות פתוחים
- ההפחתה של 100× בתקורת PEC בזכות samplomatic (2025-11-12) היא טענה בבלוג של IBM; לא נמצא מאמר המציין את קו הבסיס שלה או את מחלקת המעגלים (נוסה ב-2026-09-26).
- ריצת ה-PEA של 7,500 השערים על Nighthawk r2: מספר היריות, זמן ה-QPU והגודל הנצפה אינם מופיעים בבלוג (נבדק ב-2026-09-26).
- Zuchongzhi 3.0 ו-Tianyan-287: נקראו רק התמציות ב-arXiv; הטקסטים המלאים לא נבדקו לאיתור שלב אפחות (2026-09-26).
- Heron r1: לא נמצא מקור ראשוני המראה שיטת אפחות נקובה שהורצה על r1 עצמה (2026-09-26).
- הכרך והגיליון של המאמר של Begušić, Gray ו-Chan ב-Science Advances לא אומתו (Crossref הגביל את קצב הבקשות, PubMed Central מאחורי captcha, 2026-09-26); את נתוני הכותרת של מאמר ה-TREX (arXiv:2012.09738) לא ניתן היה לקרוא, ולכן TREX מצוטט מהתיעוד של IBM.
- קנה המידה e^(4P) של מספר היריות וערכי P נגזרו כאן מבניית PEC ומשיעורי שגיאה שפורסמו, ואינם מצוטטים ממקור.
