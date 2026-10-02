---
id: ct_vio
name: הולכת אותות אנכית (מחוץ למישור) — VIO, קואקסמון, חיווט תלת-ממדי
layer: "5 בקרה"
status: demonstrated
since: 2016
one_line: "קווי בקרה וקריאה מאלקטרוניקה בטמפרטורת החדר מגיעים לכל קיוביט מוליך-על דרך פני השבב — פינים קואקסיאליים, גששי מגע, מעברים (vias) מוליכי-על או פיסת אותות מוערמת — במקום להיות מנותבים במישור השבב אל שוליו."
verdict: "נושאת מעבד של 256 קיוביטים (RIKEN/Fujitsu) ומארז בקנה מידה של פרוסה עם >500 קיוביטים (OQC); היא מסירה את חומת הניתוב לשוליים, אך לא את מספר הקווים, ונכון ל-2026-09-26 פורסמה הפרעה הדדית בין קווים רק להתקן של ארבעה קיוביטים."
updated: 2026-09-30
---

TSV = מעבר דרך הצורן (through-silicon via); MXC = תא הערבוב, השלב הקר ביותר של המקרר; T1, T2e = זמן הרלקסציה וזמן הדה-פאזה בהד; G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
הקווים עדיין מתחילים במסדים בטמפרטורת החדר (ct_rt); רק הסנטימטר האחרון משתנה. במקום קו קו-מישורי המנותב אל משטח חיבור חוטים (wire-bond pad) בשולי הפיסה, האות נכנס דרך פני השבב — פין קפיצי או קואקסיאלי, גשש מגע, מעבר מוליך-על, או פיסת אותות המחוברת בבליטות. ה"שקע הקוונטי" של Waterloo (2016) הצמיד לשבב חוטים קואקסיאליים על קפיצים [D][532]; האלקטרודינמיקה הקוונטית הקואקסיאלית של מעגלים (circuit QED) של Oxford (2017) הציבה את הקיוביט ואת המהוד על פנים מנוגדות, כשכל החיווט ניצב לשבב [D][533] — השורש של הקואקסמון של OQC. RIKEN בחרה במעברים מוליכי-על מגב השבב על פני ממשקי שבב הפוך (flip-chip), שעדיין מביאים את משטחי החיבור לשוליים [C][534], וסקרה את הזיווד שהדבר מחייב [G][535].
תכונות: בקרת מיקרוגל בטמפרטורת החדר; שגיאה קוהרנטית; ייצור בליתוגרפיה של מוליכי-על.

## פיזיקה וגבולות
ניתוב לשוליים. בסריג m × m, כל קו המשרת קיוביט שבתוך טבעת חוצה את הטבעת דרך ~4m המרווחים שבין הקיוביטים שלה; עם k קווים לקיוביט ו-c קווים לכל מרווח, הניתוב נסגר ב-m = 4c/k — עבור k = 2 ו-c = 3–5, N ≈ 36–100 [S]. זו רמת הקיפאון של ~100 קיוביטים ש-QuantWare מצטטת [C][536], כש"כמעט 90% מהשבב" מוקדשים לניתוב [C][537]. פיסת אותות בשבב הפוך מגדילה את c, אך הקווים עדיין יוצאים דרך היקף ∝ √N, בעוד שמספרם גדל ∝ N — גידול פולינומי, לא "הפיצול האקספוננציאלי" של הספק [S]. כניסה אנכית שומרת על מספר קווים קבוע ליחידת שטח, ולכן הסריג ניתן לריצוף.
הקו. חור קואקסיאלי בוואקום הוא 50 Ω ביחס קטרים של 2.3 [S]. הפינים של OQC, 50 ± 2.5 Ω, מסתיימים 0.9 mm (קיוביט) או 0.4 mm (מהוד) מהמעגל, ומצטמדים באופן דועך (evanescent) מתחת לתדר הקטעון של החור: בררנות קו הבקרה −40 עד −60 dB בפסיעה של 2 mm [D][538]. פינים לא-גלווניים אינם מעבירים DC, ולכן קיוביטים ומצמדים המכווננים בשטף זקוקים לגששים, למעברים או לבליטות [S].
אופני התיבה. פיסת צורן של 20 mm יכולה להדהד בתדר נמוך עד ~3 GHz, בתוך תחום התדרים של הקיוביטים [S]; העמוד ההשראי של OQC מעלה את תדר הקטעון של המארז ל-34.3 GHz ומגביל את הצימוד הטפילי ל-|J|/2π < 250 kHz [D][538].
החום נקבע לפי הקו, לא לפי המסלול: המארז של OQC בקנה מידה של פרוסה, מחווט במלואו, מוערך ב-≤~3 µW על ה-MXC, מול 25–30 µW של הספק קירור ב-20 mK [D][311].

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2016-05 | חוטים קואקסיאליים על קפיצים, DC–8 GHz, מגע ~150 mΩ, אי-התאמה ~10 Ω | Univ. of Waterloo | [D][532] |
| 2017-08 | TSV מוליכי-על, התנגדות אפס בין מעבר למעבר מתחת לטמפרטורה הקריטית של אלומיניום | Rigetti | [D][539] |
| 2020 | TSV של 10 × 20 × 200 µm נושאים בקרה וקריאה בערימה המחוברת בבליטות | MIT Lincoln Laboratory | [D][540] |
| 2021-11 | 127 קיוביטים, חיווט על "כמה רמות פיזיות" | IBM Eagle | [C][541] |
| 2022-04 | 2 × 2 קואקסמונים; T1 149(38) µs; נאמנות חד-קיוביטית 99.982(4)% | Oxford / OQC | [D][538] |
| 2023-03 | 64 קיוביטים, שבב של 2 cm, גששי מגע, 96 קווי כניסה + 16 קווי יציאה | קונסורציום RIKEN | [C][542] |
| 2025-04 | 256 קיוביטים; צפיפות ×4 באותו מקרר | RIKEN / Fujitsu | [C][51] |
| 2026-02 | >500 קיוביטים על פיסה של 3 אינץ'; חציון T1 97 µs, T2e 129 µs | OQC | [D][311] |

בין המכונות במרשם הנושאות את הטכנולוגיה, מעבר ל-256 קיוביטים המצומדים בשערים קיימות רק טענות: VIO-40K, 40,000 קווים ל-10,000 קיוביטים במודולים של שבבונים, במשלוח ב-2028 [C][536]. לאף מכונה יפנית אין שגיאה דו-קיוביטית במרשם, והמארז של OQC מדווח על קוהרנטיות ועל קריאה, לא על שערים [D][311].

## ייצור, חומרים ושרשרת האספקה
מעברים: MIT Lincoln Laboratory מייצרת קיוביטים על משטח הנושא TSV [D][540]; הדפנות המשופעות של Rigetti מאפשרות לשכבות מאודות או מרוססות (sputtered) לצפות את המעבר [D][539]. פינים: המארז של OQC מתמודד עם התכווצות תרמית דיפרנציאלית על פני 3 אינץ' באמצעות מרווחים של 0.5 mm בין הפינים [D][311]. ערימות: QuantWare משלבת את "כל רכיבי התניית האותות" [C][537] ופותחת ב-2026 את KiloFab ב-Delft, בקיבולת של 20× מזו שהייתה לה ב-2025 [C][536]. שיעורי התקינות של פינים, מעברים ובליטות ב-10³–10⁴ מגעים לא פורסמו נכון ל-2026-09-26.

## בקרה, קריאה ועומס הקלט-פלט
הולכה אנכית מזיזה קווים; היא אינה מבטלת אותם. 64 הקיוביטים של RIKEN צורכים 112 קווים [C][542], 1.75 לקיוביט [S]; ההתקן של OQC בן ארבעת הקיוביטים — שניים לקיוביט [D][538]; VIO-40K — ארבעה [C][536]. המארז של OQC בקנה מידה של פרוסה משתף כל קו בין תשעה קיוביטים, והבקרה רוכבת על הקריאה [D][311] — ~0.11 לקיוביט [S]; ה-dimon, הקיוביט של GENESIS [C][543], מניע את שני האופנים דרך קו בקרה אחד [D][250]. ב-10³ קיוביטים מדובר ב-10²–4×10³ קווים [S]; ב-10⁴ QuantWare טוענת לקריוסטט אחד [C][537]; ב-10⁶ רק ריבוב קר — ct_cryocmos, ct_sfq — סוגר את הפער [S]. השהיית הלולאה אינה משתנה [S].

## תפקיד במחסנית
משבצת 5 של "סריג טרנסמונים עם מצמדים ברי-כוונון" ושל "קיוביטי מחיקה במסילה כפולה". היא **דורשת** את האלקטרוניקה של ct_rt מאחורי החיווט האנכי, ואת המעברים, הפינים והאינטרפוזרים של fab_sc; היא ו-ct_rt **מחליפות** זו את זו ("הולכת אותות בניתוב לשוליים לעומת הולכה אנכית"); לא נרשמה קשת **מספקת**. מה שהיא משחררת הוא שולי הפיסה, לקישורים משבב לשבב בין קיוביטים שבשוליים [C][537] — תנאי מקדים ל-ic_multidie. {{N_T_CT_VIO_MACH_CAP}} במרשם נושאות אותה ({{N_T_CT_VIO_PRIMARY}} כטכנולוגיה ראשית). RIKEN 64 ו-RIKEN–Fujitsu 256 מסומנות ✅ על סמך נתוני הספק; ה-✅ של Toshiko נשען על מאמר ארבעת הקיוביטים, זה של GENESIS על מאמר המסילה הכפולה, וזה של VIO-40K על ההכרזה עליו. Fujitsu 1,000-qubit machine מסומנת 🔎: המאמר המצוטט נוקב בזיווד בצפיפות גבוהה, לא בחיווט ניצב [P][546]; החיווט של תא 10,000 הקיוביטים לא נחשף. Contralto-A17 ו-Tenor-D64 אינן ביניהן: המקור מציג את Contralto-A כ"מסלול שדרוג חסכוני אל יחידות ה-QPU של QuantWare המבוססות על VIO", לא כאחת מהן [C][544], ודף ה-D-line מציג תמונות של מודולי "VIO 1K" ו-"VIO 40K" בלי לנקוב במעבד [C][545]. הפער G-vio, תשובה: מספר הקווים לקיוביט נע בטווח 0.11–4; מספר שכבות הניתוב אינו נחשף בידי אף מכונה הנושאת את הטכנולוגיה.

## ראיות — כיצד נמדדו המספרים
הפרעה הדדית בין קווים קיימת רק כמטריצת הבררנות של OQC לארבעה קיוביטים [D][538]; RIKEN, Fujitsu ו-QuantWare אינן מפרסמות נתון כזה במקורות שנפתחו, נכון ל-2026-09-26. המארז של OQC הוא מערך הנתונים היחיד עם קיוביטים רבים: חציון T1, T2e ~100 µs על פני ~100 קיוביטים, נאמנות קריאה של 97.5% וטמפרטורת קיוביט של 36 mK על פני 54 [D][311]. חסרים: בחינות ביצועים בו-זמניים על פני >100 קווים; שיעור תקינות המגעים לאורך מחזורי חימום וקירור.

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| RIKEN | מחקר | יפן | מארז עם גששי מגע, 64 קיוביטים | [C][542] |
| Fujitsu | מפתח | יפן | ריצוף תאי יחידה של 256 קיוביטים; 1,000 קיוביטים רשומים ל-2026 | [C][51] |
| Oxford Quantum Circuits | מפתח | בריטניה | קואקסמון ב-Toshiko וב-GENESIS; מארז בקנה מידה של פרוסה | [C][543][D][311] |
| QuantWare | ספק | הולנד | ערימת שבבים VIO; VIO-40K ל-2028 | [C][537] |
| MIT Lincoln Laboratory | מחקר | ארה״ב | TSV בערימות המחוברות בבליטות | [D][540] |
| Rigetti Computing | מפתח | ארה״ב | תהליך TSV מוליך-על | [D][539] |
| IBM | מפתח | ארה״ב | חיווט רב-רמתי (Eagle) | [C][541] |

**כספים.**
- 2026-05-05 · QuantWare · סבב B בהובלת Intel Capital ו-In-Q-Tel, הנוקב ב-VIO-40K וב-KiloFab · USD 178 M · הוכרז [C][547]
- 2026-06-02 · OQC · סבב C בהובלת Bullhound Capital, הקואקסמון אינו מוזכר · GBP 260 M · הוכרז [C][60]

**שוק ושרשרת אספקה.** RIKEN/Fujitsu ו-OQC בונות את המארזים שלהן בעצמן; QuantWare מוכרת את VIO כדי "להגדיל את שבבוני הקיוביטים ואת התכנונים של צדדים שלישיים" [C][547]. משרתת את G2–G4 (טרנסמון) ואת G3–G4 (מסילה כפולה).

**קניין רוחני ותקנים.** OQC מכנה את הקואקסמון "מוגן בפטנט" [C][543], ולא אותר מספר פטנט; QuantWare מציגה את VIO-40K כתקן של ה-Quantum Open Architecture שלה [P][495]. אין גוף תקינה, נכון ל-2026-09-26.

**מפות דרכים ועמידה בהבטחות.** ביולי 2020 כיוונה RIKEN להתקן של 64 קיוביטים "בתוך שלוש השנים הבאות" [C][534], ופתחה אותו ב-2023-03-27 [C][542] — ההבטחה קוימה. Fujitsu עדיין רושמת 1,000 קיוביטים ל-2026 [C][75], ולא נמצאה השקה נכון ל-2026-09-26. QuantWare: VIO-40K ב-2028 [C][536]; אין נתוני ביניים על VIO, נכון ל-2026-09-26.

**פרשנות אסטרטגית.** מעבר ל-~100 קיוביטים, הכניסה האנכית מכריעה אם פיסה ניתנת לריצוף, לא אם מקרר יכול להזין אותה; הערך עובר לכושר הייצור של מעברים, בליטות ופינים, ולמי שיפרסם ראשון נתוני הפרעה הדדית ושיעור תקינות בקנה מידה.

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 מעבד מחווט אנכית של יותר מ-256 קיוביטים יפרסם שגיאות דו-קיוביטיות יחד עם הפרעה הדדית בפעולה בו-זמנית; להוריד בדרגה אם מכונת 1,000 הקיוביטים של Fujitsu תעבור את 2026-12-31 בלי שנחשפה, או אם VIO-40K יידחה אל מעבר ל-2028. שאלות פתוחות. (1) איזו פסיעה שומרת על בררנות מתחת ל-−40 dB במרווח של 1 mm בין קיוביטים? (2) האם פינים לא-גלווניים יכולים לשרת מצמדים המכווננים בשטף? (3) מהו שיעור התקינות של המגעים לכל מחזור חימום וקירור ב-10⁴ פינים? (4) האם שיתוף קו בין תשעה קיוביטים שורד קיוביטים מצומדים ושערים? (5) באיזה קנה מידה יהפוך החום של הערימה עצמה לאילוץ?

## מקורות
[51] Fujitsu Limited and RIKEN, “Fujitsu and RIKEN develop world-leading 256-qubit superconducting quantum computer,” Fujitsu Global, Apr. 22, 2025. [Online]. Available: https://info.archives.global.fujitsu/global/about/resources/news/press-releases/2025/0422-01.html [C]
[60] A. Curbison, “OQC raises £260m in Europe's largest ever private quantum computing funding round,” OQC, Jun. 2, 2026. [Online]. Available: https://oqc.tech/company/newsroom/series-c [C]
[75] Fujitsu, “Fujitsu Quantum.” [Online]. Available: https://global.fujitsu/en-global/technology/research/quantum [C]
[250] J. Wills, M. T. Haque, and B. Vlastakis, “Error-detected coherence metrology of a dual-rail encoded fixed-frequency multimode superconducting qubit,” [arXiv:2506.15420](https://arxiv.org/abs/2506.15420), Jun. 2025. [D]
[311] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [D]
[495] M. Abdel-Kareem, “QuantWare Debuts VIO-40K™ Architecture to Enable 10,000-Qubit Superconducting Processors,” Quantum Computing Report, Dec. 10, 2025. [Online]. Available: https://quantumcomputingreport.com/quantware-debuts-vio-40k-architecture-to-enable-10000-qubit-superconducting-processors/ [P]
[532] J. H. Béjanin *et al.*, “The Quantum Socket: Three-Dimensional Wiring for Extensible Quantum Computing,” *Phys. Rev. Appl.*, vol. 6, Art. no. 044010, 2016, doi: [10.1103/PhysRevApplied.6.044010](https://doi.org/10.1103/PhysRevApplied.6.044010). [arXiv:1606.00063](https://arxiv.org/abs/1606.00063). [D]
[533] J. Rahamim *et al.*, “Double-sided coaxial circuit QED with out-of-plane wiring,” *Appl. Phys. Lett.*, vol. 110, no. 22, Art. no. 222602, May 2017, doi: [10.1063/1.4984299](https://doi.org/10.1063/1.4984299). [arXiv:1703.05828](https://arxiv.org/abs/1703.05828). [D]
[534] RIKEN, “Wiring a new path to scalable quantum computing,” Jul. 3, 2020. [Online]. Available: https://www.riken.jp/en/news_pubs/research_news/rr/20200703_2/index.html [C]
[535] S. Tamate, Y. Tabuchi, and Y. Nakamura, “Toward Realization of Scalable Packaging and Wiring for Large-Scale Superconducting Quantum Computers,” *IEICE Trans. Electron.*, vol. E105.C, no. 6, pp. 290–295, Jun. 2022, doi: [10.1587/transele.2021SEP0007](https://doi.org/10.1587/transele.2021SEP0007). [G]
[536] QuantWare, “QuantWare announces scaling breakthrough with VIO-40K™, delivering 10,000 qubit Quantum Processors for the first time,” Dec. 8, 2025. [Online]. Available: https://quantware.com/news/quantware-announces-scaling-breakthrough-with-vio-40k [C]
[537] QuantWare, “Technology — VIO™ 3D Scaling Architecture.” [Online]. Available: https://quantware.com/technology [C]
[538] P. A. Spring *et al.*, “High coherence and low cross-talk in a tileable 3D integrated superconducting circuit architecture,” *Sci. Adv.*, vol. 8, no. 16, Art. no. eabl6698, Apr. 2022, doi: [10.1126/sciadv.abl6698](https://doi.org/10.1126/sciadv.abl6698). [arXiv:2107.11140](https://arxiv.org/abs/2107.11140). [D]
[539] M. Vahidpour *et al.*, “Superconducting Through-Silicon Vias for Quantum Integrated Circuits,” [arXiv:1708.02226](https://arxiv.org/abs/1708.02226), Aug. 2017. [D]
[540] D.-R. W. Yost *et al.*, “Solid-state qubits integrated with superconducting through-silicon vias,” *npj Quantum Inf.*, vol. 6, Art. no. 59, 2020, doi: [10.1038/s41534-020-00289-8](https://doi.org/10.1038/s41534-020-00289-8). [arXiv:1912.10942](https://arxiv.org/abs/1912.10942). [D]
[541] J. Chow, O. Dial, and J. Gambetta, “IBM Quantum breaks the 100‑qubit processor barrier,” IBM Quantum Computing Blog, Nov. 16, 2021. [Online]. Available: https://www.ibm.com/quantum/blog/127-qubit-quantum-processor-eagle [C]
[542] NTT (joint release of RIKEN, AIST, NICT, Osaka University, Fujitsu and NTT), “Japanese joint research group launches quantum computing cloud service: Opening access to Japan's first superconducting quantum computer,” Mar. 24, 2023. [Online]. Available: https://group.ntt/en/newsrelease/2023/03/24/230324a.html [C]
[543] Oxford Quantum Circuits, “Devices – OQC,” OQC. [Online]. Available: https://oqc.tech/tech/devices/ [C]
[544] QuantWare, “Introducing Contralto-A: a QPU for quantum error correction,” Feb. 25, 2025. [Online]. Available: https://quantware.com/news/introducing-contralto-a-qpu-for-quantum-error-correction [C]
[545] QuantWare, “D-line QPUs — Build bigger, scale faster.” [Online]. Available: https://quantware.com/product/processors/d-line [C]
[546] M. Swayne, “How Fujitsu Is Tackling a 10,000-Qubit Quantum Computer for Practical Applications,” The Quantum Insider, Dec. 8, 2025. [Online]. Available: https://thequantuminsider.com/2025/12/08/how-fujitsu-is-tackling-a-10000-qubit-quantum-computer-for-practical-applications/ [P]
[547] QuantWare, “QuantWare Raises $178 Million to Build World’s Most Powerful Quantum Processors at an Industrial Scale,” May 5, 2026. [Online]. Available: https://quantware.com/news/quantware-raises-178-million [C]

## פריטי אימות פתוחים
- arXiv:2407.02769, שנקוב בבקשת התקציר כ-Tamate et al. 2024, הוא מאמר לא קשור על סיווג תמונות (נבדק ב-2026-09-26); הסקירה של RIKEN היא של Tamate, Tabuchi ו-Nakamura, IEICE Trans. Electron. E105.C (2022), שהטקסט המלא שלה היה חסום, ולכן אף נתון ממנה אינו בשימוש.
- Crossref, Europe PMC, OpenAlex ו-Semantic Scholar החזירו HTTP 429 ב-2026-09-26; הרשומות של Béjanin ושל Yost נושאות את השנה בלבד.
- הפוסט של IBM שנפתח אינו אומר אם האותות בדור Eagle נכנסים דרך פני השבב, והמרשם אינו מונה אף מכונת IBM הנושאת את הטכנולוגיה; הולכת האותות של Rigetti Ankaa וכל עבודה של imec על הולכה אנכית לא נמצאו (2026-09-26).
- QuantWare אינה מפרסמת נתוני הפרעה הדדית, עכבה, שיעור תקינות או עומס חום עבור VIO, ואינה אומרת איזה מעבד נושא את "VIO 1K" (2026-09-26).
- השיתוף בין תשעה קיוביטים של OQC (56 תאים) לקוח מהטקסט המלא שלו ב-HTML; מספר הקווים הנכנסים למארז, והשאלה אם הקיוביטים בו מצומדים, אינם מצוינים (2026-09-26).
