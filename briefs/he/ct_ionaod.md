---
id: ct_ionaod
name: מיעון לייזר של יונים במרחב חופשי (אלומות AOM/AOD)
layer: "5 בקרה"
status: demonstrated
since: 2016
one_line: "אור השערים משולחן אופטי בטמפרטורת החדר ממותג ומכוון אל יונים בודדים בשרשרת אחת בידי מאפננים אקוסטו-אופטיים רב-ערוציים או מסיטים אקוסטו-אופטיים, וממוקד דרך אופטיקה נפחית מעל המלכודת."
verdict: "בקרת היונים הנפוצה ביותר במרשם, שפורסמה עד 40 יונים ממוענים בשרשרת, עם הפרעה הדדית לשכן של 10⁻³–10⁻²; נכון ל-2026-09-26 לא נמצא מידוד לכל זוג בשרשרת ארוכה יותר הממוענת במרחב חופשי, ומפת הדרכים של IonQ שמעבר ל-Tempo נשענת על שבבים ועל קישורים פוטוניים."
updated: 2026-09-30
---

AOM = מאפנן אקוסטו-אופטי; AOD = מסיט אקוסטו-אופטי; MS = שער מולמר–סורנסן; DRB = מידוד אקראי ישיר; ε = תדירות ראבי של השכן חלקי זו של המטרה; QV = נפח קוונטי; G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
שולחן אופטי שולח את אור השערים דרך חלונות הוואקום ואובייקטיב בעל צמצם גבוה; האקוסטו-אופטיקה קובעת איזה יון מואר, ואת המשרעת, התדר והפאזה של האור. AOM רב-ערוצי נותן ערוץ RF אחד לכל אלומה קבועה — 32 ב-355 nm במכונת חמשת הקיוביטים של Maryland מ-2016, מקור הטכנולוגיה [D][585]; AOD ממפה תדר RF לזווית, כך שאלומה מוסטת מגיעה לכל יון [D][100]. קיוביטים על-דקים דורשים זוג אלומות ראמאן — 355 nm עבור ¹⁷¹Yb⁺ [D][586], 532 nm עבור ¹³³Ba⁺ [D][109]; קיוביטים אופטיים של ⁴⁰Ca⁺ דורשים אלומה אחת של 729 nm [D][253].
תכונות: בקרה אופטית בטמפרטורת החדר; שגיאות קוהרנטיות; אופטיקה נפחית; הרכבה אחת לכל שרשרת.

## פיזיקה וגבולות
הפרעה הדדית. שדה גאוסי דועך כ-exp(−d²/w²) — ~10⁻¹² במותן של 0.85 µm ובמרווח של 4.43 µm של EURIQA [S] — ובכל זאת השכן רואה עד 2.5% מתדירות ראבי של המטרה [D][254]: אברציות ופיזור קובעים את הרצפה. נתוני השכן שפורסמו, במדדים שונים, יורדים מ-<4% ב-2016 [D][585] ל-<9×10⁻⁴ [D][587]. עבור יחס ראבי ε, יון צופה המסובב ב-εθ מאבד ≈(εθ/2)², כלומר 2.5×10⁻⁴ ב-ε = 10⁻² עבור פולס π [S]; מאחר שהשגיאה קוהרנטית, אפשר לפצות עליה — פולסי הסטת אור התלויים בעוצמה הורידו את נתון השכן של 0.5% במדגים של AQT ל-1.3×10⁻⁴ [D][253].
כיוון ופאזה. ריצוד δx מזיז את קצב ראבי ב-~(δx/w)² [S]; Forte מתכנן את מותן האלומה שלו, 1.5 µm, כנגד רעש הכיוון [D][100]. ב-355 nm, הפרש נתיב של 56 nm בין זרועות המתפשטות זו נגד זו הוא 1 rad של פאזת שער [S]; Forte מגדיר שניים מארבעת הנתיבים שלו לשערים חד-קיוביטיים שאינם רגישים לפאזה [D][100].
ה-AOD. θ = λf/v; הרזולוציה היא זמן הצמצם × רוחב הפס; סחיפה תרמית מחייבת כיול זווית במקום [G][588]. ה-AOD העל-סגול של Duke מסיט 6 mrad על פני פס של 100 MHz [D][587], כלומר v ≈ 5.9 km/s [S]. ה-RF גם מזיז את התדר האופטי בהתאם למיקום; ה-AOD המוצלבים של AQT מבטלים זאת [D][253]. היגוי של ~50 קוטרי אלומה [D][587] משתרע על 25–50 יונים במרווח של 3–4 µm [S]. הזוגות מטופלים בזה אחר זה [D][109]: 15 זוגות זרים, בשער MS חציוני של 672 µs ב-Forte, נמשכים ~10 ms [S]. שדה הראייה והטיפול הסדרתי מחזיקים את השרשרת סביב 30–40 יונים [S].

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2016-08 | 5 ¹⁷¹Yb⁺; AOM על-סגול של 32 ערוצים; הפרעה הדדית <4%; שער XX של 235 µs | Univ. of Maryland | [D][585] |
| 2019-11 | 11 קיוביטים ב-13 יונים; אלומות 355 nm גלובליות + ממוענות; שער דו-קיוביטי 97.5% | IonQ | [D][586] |
| 2021-06 | AOD מוצלבים, 729 nm; הפרעה הדדית לשכן 0.5%; GHZ של 24 יונים 54.4(7)% | Innsbruck / AQT | [D][253] |
| 2021-10 | 32 אלומות, מותן 0.85 µm; 13 קיוביטים ב-15 יונים; שער דו-קיוביטי 98.5–99.3% | EURIQA (Maryland/Duke) | [D][254] |
| 2023-08 | 4 AOD; 30 קיוביטים ב-36 יונים; DRB של שער דו-קיוביטי, חציון 4.64×10⁻³ | IonQ Forte | [D][100] |
| 2026-01 | מודול AOD <1 ft²; הפרעה הדדית <9×10⁻⁴; שרשרת של 30 יונים; מיתוג ב-240 ns | Duke | [D][587] |
| 2026-06 | 40 ¹³³Ba⁺; אלומות ראמאן של 532 nm המכוונות ב-AOD | IonQ | [D][109] |

מעל 40 יונים, מלבד 98 היונים של Helios במלכודת QCCD, קיימות רק טענות: הדף של Tempo מציין 100 קיוביטים כ"יעד" ו-99.9% כ"נאמנות יעד", ללא שיטת מיעון [C][101]. הגביש של Tsinghua, בן 512 יונים, פועל באלומות גלובליות של 411 nm — מרחב חופשי ללא מיעון [D][121].

## ייצור, חומרים ושרשרת האספקה
הרכבה, לא פרוסה: לייזר על-סגול פולסי (EURIQA: Coherent Paladin 355-4000) [D][254], אקוסטו-אופטיקה — סיליקה מותכת בעל-סגול, TeO₂ בתחום הנראה [G][588] — אובייקטיבים וסינתזת RF; המודול של Duke משתמש ב-AOD של Brimrose [D][587]. גם Gooch & Housego ו-AA Opto Electronic נזכרות [P][322]; המסיטים של G&H מכוונים גם מערכי מלקחיים אופטיים של 3,000 ו-6,100 אטומים [C][504], אספקה המשותפת עם cx_aod. AQT מכניסה 12 קיוביטים לשני מסדים של 19 אינץ', 2 m², <2 kW [C][382].

## בקרה, קריאה ועומס הקלט-פלט
AOM רב-ערוצי זקוק לערוץ RF אחד לכל יון במרווח קבוע — EURIQA משאירה שני יונים בקצוות ללא שימוש כדי לשמור על מרווח אחיד [D][254]; ארבעת ה-AOD של Forte, כל אחד מאחורי AOM הקובע משרעת, תדר ופאזה, מתוכננים להגיע לכל אחד מ-40 יונים — מדידת הביצועים השתמשה ב-36 בשל מגבלת ערוצי גילוי הפוטונים — ומשחררים את פוטנציאל הלכידה מאילוץ המרווח הקבוע [D][100]. המיתוג (~240 ns) [D][587] זניח; הטיפול הסדרתי הוא ההשהיה — מחזורי הקוד במצע הניסוי של Ba נמשכים 35–86 ms, וכל היונים מועברים לרמת המדף D₅/₂ בזמן הקריאה באמצע המעגל [D][109]. ב-10³ יונים: ~25 שולחנות אופטיים ועוד קישורים פוטוניים [S].

## תפקיד במחסנית
משבצת 5 של "יונים לכודים — מלכודת פאול ליניארית עם מיעון לייזר פרטני" ושל "יונים לכודים — QCCD (הובלה בין אזורים)". היא **דורשת** את fab_optics (אופטיקה נפחית מעל המלכודת), **מספקת** את השדות במרחב החופשי ש-g_ms דורש, **ומוחלפת** בידי ct_ionlaser (הולכה משולבת) ו-ct_ionmw (שערים אלקטרוניים, שגיאת שער דו-קיוביטי 8.4(7)×10⁻⁵ [D][102]). {{N_T_CT_IONAOD_MACH_CAP}} במרשם נושאות אותה ({{N_T_CT_IONAOD_PRIMARY}} כטכנולוגיה ראשית), וביניהן Aria, Forte ו-Tempo של IonQ ומצע הניסוי של 40 יוני Ba; Helios, H1 ו-H2 של Quantinuum; IBEX Q1 ו-LYNX של AQT; PIAST-Q; QSCOUT (Quantum Scientific Computing Open User Testbed); מכונת היונים בת 70 הקיוביטים של FIAN / Rosatom; Tsinghua; Innsbruck; Maryland/Duke. שבעה תאים הם ✅; התא של Aria הוא 🔎, שכן האופטיקה של האלומות שלה הוצגה רק עבור קודמתה מ-2019 [D][586]; התא של Tsinghua הוא 🔎 ומראה אלומות גלובליות; Tempo, PIAST-Q ומכונת Rosatom הם 🔎. Qudoor AbaQ אינה ביניהן: הבקרה שלה לא נחשפה. AQT ו-Innsbruck מתוארות כקיוביטים אופטיים של ⁴⁰Ca⁺, כמו במאמרים המצוטטים שלהן [D][253][D][255]. הפער G-ionaod נסגר, עם ion_chain במקום ion_elec שהוצע.

## ראיות — כיצד נמדדו המספרים
ההפרעה ההדדית מצוטטת כיחס ראבי, כיחס עוצמות (ε²) או כשגיאת היון הצופה — Duke מכנה יחס ראבי "הפרעה הדדית בעוצמה" [D][587] — ונמדדת בהזזת יון אחד דרך האלומה [D][253], ביוני דגל [D][254] או במידודים בו-זמניים [D][109]. ה-DRB של Forte על 435 זוגות אינו מוצא תלות מובהקת במרחק בין היונים, אך מוצא שגיאות מובהקות שמחוץ למודל [D][100]. מבין דפי הספקים שנפתחו, רק הדף של AQT מציין הפרעה הדדית — לשכן <1.8×10⁻², נכון ל-2026-09-26 [C][382].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| IonQ | מפתח | ארה״ב | מיעון AOD ב-Forte ובמצע הניסוי של 40 יוני Ba | [D][100][D][109] |
| Alpine Quantum Technologies | מפתח | אוסטריה | מיעון ב-729 nm באמצעות AOD מוצלבים, מערכות במסד | [D][253][C][382] |
| University of Innsbruck | מחקר | אוסטריה | אלומות 729 nm ניתנות להיגוי, 16 יונים | [D][255] |
| Univ. of Maryland / Duke | מחקר | ארה״ב | AOM של 32 ערוצים; מודול AOD קומפקטי | [D][254][D][587] |
| Tsinghua University | מחקר | סין | גביש של 512 יונים, אלומות גלובליות | [D][121] |
| Qudoor | מפתח | סין | לייזרים ובקרה בפיתוח עצמי; המיעון לא נחשף | [P][302] |
| Gooch & Housego | ספק | בריטניה | AOD, AOM | [C][504] |

**כספים.**
- 2023-12-05 · AQT · מחשב של 20 קיוביטים בשני מסדים עבור LRZ ו-Munich Quantum Valley, במימון בווארי · ~EUR 9.8 M · נחתם חוזה [C][323]
- 2025-09-17 · IonQ · רכישת Oxford Ionics (מלכודות המיוצרות כשבבים) · לא צוין בהודעה · נסגר [C][18]

**שוק ושרשרת אספקה.** לייזרים, אקוסטו-אופטיקה, אובייקטיבים ו-RF הם רכיבים מסחריים מהמדף; קווי העל-סגול של האיטרביום דורשים לייזרים יקרים ומוגבלי הספק [P][322]. שתי הארכיטקטורות משרתות את G2, G3, G6 ו-G7.

**קניין רוחני ותקנים.** בקשות פטנט של IonQ על פיצוי שגיאות בגאומטריית אלומות ראמאן (JP 2024, EP 2025) [P][375]; נכון ל-2026-09-26 לא נמצא תקן לדיווח הפרעה הדדית.

**מפות דרכים ועמידה בהבטחות.** IonQ (2025-06-13): Tempo, 100 קיוביטים, 2025; 10,000 על שבב אחד, 2027; >2,000,000 עד 2030, כשהאמצעים הנקובים הם מלכודות דו-ממדיות של Oxford Ionics וקישורים פוטוניים [R][132]. הנתונים של Tempo נשארים יעדים [C][101]; הקישור הפוטוני בין שתי מערכות מ-2026-04-14 לא נתן קצב או נאמנות [C][589]. LYNX של AQT טוענת ל-QV 32,768 ולרגישות נמוכה יותר לרעש הפאזה של הלייזר, ללא מספר קיוביטים [C][128].

**פרשנות אסטרטגית.** הדרך המהירה ביותר למכונה עובדת של 30–40 יונים, ואמת המידה שמולה נמדדות ההולכה המשולבת והבקרה האלקטרונית, אך לא מסלול הגדלה; הערך עובר לשבבי מלכודות ולקישורים.

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 IonQ תפרסם את זמני השער, הנאמנויות ושיטת המיעון של Tempo לכל זוג, או אם שרשרת ממוענת של יותר מ-60 יונים תעבור מידוד; להוריד בדרגה אם המערכות הבאות של IonQ יסופקו עם הולכה אלקטרונית או משולבת. שאלות פתוחות. (1) מה קובע את רצפת השכן מתחת ל-10⁻³ — אברציות, פיזור או אינטרמודולציה של ה-RF? (2) האם AOD רב-תדריים יכולים להריץ שערים מקבילים בלי אלומות תועות? (3) כיצד סחיפת הכיוון גדלה עם מחזור העבודה של ה-RF? (4) האם היגוי דו-צדדי מחזיק ב-100 יונים? (5) מתי קישור פוטוני עדיף על שרשרת ארוכה יותר?

## מקורות
[18] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[100] J.-S. Chen *et al.*, “Benchmarking a trapped-ion quantum computer with 30 qubits,” *Quantum*, vol. 8, Art. no. 1516, Nov. 2024, doi: [10.22331/q-2024-11-07-1516](https://doi.org/10.22331/q-2024-11-07-1516). [arXiv:2308.05071](https://arxiv.org/abs/2308.05071). [D]
[101] IonQ, “IonQ Tempo: 100-Qubit Quantum Computer (#AQ 64).” [Online]. Available: https://ionq.com/quantum-systems/tempo [C]
[102] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025. [D]
[109] E. Tham *et al.*, “Breakeven demonstration of quantum low-density parity-check codes,” [arXiv:2606.06455](https://arxiv.org/abs/2606.06455), Jun. 2026. [D]
[121] S.-A. Guo *et al.*, “A site-resolved two-dimensional quantum simulator with hundreds of trapped ions,” *Nature*, vol. 630, no. 8017, pp. 613–618, May 2024, doi: [10.1038/s41586-024-07459-0](https://doi.org/10.1038/s41586-024-07459-0). [D]
[128] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[132] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [R]
[253] I. Pogorelov *et al.*, “Compact Ion-Trap Quantum Computing Demonstrator,” *PRX Quantum*, vol. 2, no. 2, Art. no. 020343, Jun. 2021, doi: [10.1103/PRXQuantum.2.020343](https://doi.org/10.1103/PRXQuantum.2.020343). [arXiv:2101.11390](https://arxiv.org/abs/2101.11390). [D]
[254] L. Egan *et al.*, “Fault-tolerant control of an error-corrected qubit,” *Nature*, vol. 598, no. 7880, pp. 281–286, Oct. 2021, doi: [10.1038/s41586-021-03928-y](https://doi.org/10.1038/s41586-021-03928-y). [arXiv:2009.11482](https://arxiv.org/abs/2009.11482). [D]
[255] L. Postler *et al.*, “Demonstration of fault-tolerant universal quantum gate operations,” *Nature*, vol. 605, pp. 675–680, 2022, doi: [10.1038/s41586-022-04721-1](https://doi.org/10.1038/s41586-022-04721-1). [arXiv:2111.12654](https://arxiv.org/abs/2111.12654). [D]
[302] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[375] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[382] Alpine Quantum Technologies, “19-inch rack-mounted quantum computer,” AQT. [Online]. Available: https://www.aqt.eu/products/ibex-q1/ [C]
[504] Gooch & Housego (G&H), “G&H Acousto-Optic Deflectors Referenced in Nature Papers Demonstrating 3,000 & 6,100 Qubit Quantum Systems,” G&H, Mar. 2026. [Online]. Available: https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [C]
[585] S. Debnath, N. M. Linke, C. Figgatt, K. A. Landsman, K. Wright, and C. Monroe, “Demonstration of a small programmable quantum computer with atomic qubits,” *Nature*, vol. 536, no. 7614, pp. 63–66, Aug. 2016, doi: [10.1038/nature18648](https://doi.org/10.1038/nature18648). [arXiv:1603.04512](https://arxiv.org/abs/1603.04512). [D]
[586] K. Wright *et al.*, “Benchmarking an 11-qubit quantum computer,” *Nat. Commun.*, vol. 10, Art. no. 5464, Nov. 2019, doi: [10.1038/s41467-019-13534-2](https://doi.org/10.1038/s41467-019-13534-2). [arXiv:1903.08181](https://arxiv.org/abs/1903.08181). [D]
[587] J. Yu *et al.*, “Design and Characterization of Compact Acousto-Optic-Deflector Individual Addressing System for Trapped-Ion Quantum Computing,” [arXiv:2601.01647](https://arxiv.org/abs/2601.01647), Jan. 2026. [D]
[588] R. Paschotta, “Acousto-optic Deflectors,” RP Photonics Encyclopedia. [Online]. Available: https://www.rp-photonics.com/acousto_optic_deflectors.html [G]
[589] IonQ, “IonQ Achieves Key Photonic Interconnect Milestone, Demonstrating Networked Quantum Systems Using Entanglement,” Apr. 14, 2026. [Online]. Available: https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement [C]

## פריטי אימות פתוחים
- Fang ועמיתיו, PRL 129, 240504 (2022), arXiv:2206.02703, על דיכוי הפרעה הדדית בשערים ממוענים פרטנית: לא נקרא, Crossref ו-PubMed הגבילו את קצב הבקשות (2026-09-26); לא צוטט.
- מיעון AOD דו-צדדי של USTC (arXiv:2306.01307): הפרעה הדדית של ראבי לשכן 1.19(5)×10⁻³ בתמצית הנוכחית, אך 6.32×10⁻⁴ בגרסת ה-HTML מ-2023; רשימת המחברים שפורסמה לא אושרה; לא צוטט (2026-09-26).
- המין, זמן השער ושיטת המיעון של Tempo, הארכיטקטורה של Aria עצמה והבקרה של Qudoor AbaQ אינם נחשפים במקורות שנפתחו (2026-09-26); תאי המרשם האלה הם הסקות.
- פרופילי המרשם מציינים "קיוביט על-דק" עבור IBEX Q1 של AQT ועבור Innsbruck, בעוד שהמאמרים המצוטטים מתארים קיוביטים אופטיים של ⁴⁰Ca⁺ ב-729 nm; הדף של IBEX Q1 מציין 2,000 שערים למעגל, לעומת 1,000 במרשם (2026-09-26).
- לא נפתח מקור כמותי להספק RF לכל תדר, לאינטרמודולציה רב-תדרית או לסחיפת כיוון תרמית של AOD במערכות יונים (2026-09-26).
- תאריך הפרסום ב-Nature של Postler ועמיתיו לא אושר (Crossref הגביל את קצב הבקשות, 2026-09-26); הרשומה נושאת את השנה בלבד.
