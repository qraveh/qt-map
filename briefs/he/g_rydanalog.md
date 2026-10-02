---
id: g_rydanalog
name: התפתחות אנלוגית תחת המילטוניאן רידברג
layer: "3 מנגנון השער"
status: demonstrated
since: 2017
one_line: "שדות לייזר גלובליים מניעים המילטוניאן איזינג-רידברג הניתן לתכנות על מערך מלקחיים אופטיים שלם בבת אחת: צורות הגל Ω(t), Δ(t), תבנית קבועה של היסט מקומי והגאומטריה של האטומים הם התוכנית, ואין שער בדיד."
verdict: "הודגם עד 256–289 אטומים ופורה לפיזיקה של רב-גופים, אך מדורג לפי גדלים נצפים, לא לפי שגיאת שער: מדד הייחוס לנאמנות רב-גופית מדווח 0.095 ב-60 אטומים על מכונת Sr אקדמית, המרשם אינו מחזיק נתון נאמנות ל-Aquila או ל-Fresnel נכון ל-2026-09-26, ואופן הפעולה הזה אינו מאפשר תיקון שגיאות."
updated: 2026-09-26
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; MIS = קבוצה בלתי תלויה בגודל מרבי (maximum independent set); SA = הרפיה מדומה (simulated annealing); F_d = אומד נאמנות רב-גופית מסוג אנטרופיה צולבת; MPS = מצב מכפלת מטריצות (χ = ממד הקשר); AHS = סימולציית המילטוניאן אנלוגית, סוג התוכנית של Amazon Braket; G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
המערך מתפתח תחת המילטוניאן אחד, H/ℏ = Σᵢ (Ω(t)/2) σˣᵢ − Σᵢ [Δ(t) + hᵢ Δ_loc(t)] nᵢ + Σ_{i<j} C₆ r_ij⁻⁶ nᵢ nⱼ: צורות גל גלובליות, תבנית אתרים סטטית אחת $h_i$, וצימודים שנקבעים לפי מיקומי האטומים [C][262][C][429]. הטכנולוגיה g_ryd משתמשת באותה חסימה ל-CZ של שני אטומים בתוך מעגל; כאן היא פועלת על כל הזוגות לאורך כל הריצה, והפלט הוא דגימה של מחרוזת ביטים. הטכנולוגיה g_anneal, מחשב ההרפיה על קיוביטי שטף rf-SQUID, קובעת את הצימודים במצמדים הניתנים לתכנות על השבב [D][430]; כאן הגאומטריה היא מטריצת הצימוד, והחסימה מגבילה את הדינמיקה לקבוצות בלתי תלויות של גרף דיסקות-יחידה, הבסיס לקידוד MIS [D][431]. שושלת: 51 אטומים בממד אחד, Harvard/MIT, 2017 [D][384]; הארכיטקטורה של Pasqal מ-2020, הנוקבת ב"רצפי המילטוניאן" אנלוגיים לצד מעגלים [D][385]; Aquila ב-Amazon Braket [C][262].
תכונות: נושא טבעי; אין זמן צעד (התפתחות אחת, ≤4 µs ב-Aquila); קריאה בירושה; אין ניידות במהלך התוכנית; בקרה אופטית בטמפרטורת החדר; שגיאות קוהרנטיות ושגיאות אובדן; ייצור אופטי.

## פיזיקה וגבולות
Aquila: Ω ≤ 15.8 rad/µs, |Δ| ≤ 125 rad/µs, $C_6$ = 5,420,503 µm⁶ rad/µs (70S), מרווח ≥4 µm, תוכנית ≤4 µs, T2* 5.8 µs, T2 תחת הנעה 7.5 µs [C][262]: רדיוס חסימה $(C_6/\Omega)^{1/6}$ ≈ 8.4 µm בהנעה מלאה, ותוכנית באורך ~מחצית ה-T2 תחת הנעה, ~10 מחזורי ראבי [S]. איברי השגיאה הנקובים: רעש משרעת ורעש פאזה של הלייזר; תנועה תרמית (דופלר, פיזור מיקום של 0.200 µm); פיזור דרך המצב המתווך, הנמשך גם כשההנעה כבויה; אי-הומוגניות של ההיסט, 0.37 rad/µs RMS לאורך השדה ו-0.18 rad/µs מריצה לריצה [C][262]. דרך r⁻⁶, פיזור המיקום נותן פיזור של ~30% מריצה לריצה בקשר של 5.5 µm (δV/V = 6δr/r) [S] — בלתי מזיק עמוק בתוך החסימה, מכריע היכן ש-V ≈ Ω, וזה מה שבוחר את הפאזה המסודרת. ההיסט המקומי הוא תבנית קבועה עם צורת גל ≤0, ותוכניות המשתמשות בו מאבדות קוהרנטיות מהר יותר מה-T2 הרשום [C][429]. השגיאות מצטברות באופן קוהרנטי לאורך ריצה שאין בה נקודה למדידת סינדרום, ולכן שום קוד אינו פועל [S]; גילוי מחיקות ב-Sr העלה חסם על נאמנות זוג בל מ-≥0.9971 ל-≥0.9985 על ידי השלכת ריצות מסומנות [D][143] — בחירה בדיעבד, לא תיקון.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2017-11 | 51 אטומים, חד-ממדי; סדר Z₂, תנודות לאחר שינוי פתאומי (quench) | Harvard/MIT | [D][384] |
| 2021-07 | 64–256 אטומים, דו-ממדי; מעבר איזינג ב-(2+1)D | Harvard/MIT | [D][432] |
| 2021-07 | עד 196 אטומים, אנטי-פרומגנטים ריבועיים ומשולשים | Institut d'Optique | [D][433] |
| 2021-12 | 219 אטומים על צלעות סריג קגומה; נוזל ספין טופולוגי | Harvard/MIT | [D][434] |
| 2022-06 | עד 289 אטומים; MIS, האצה על-ליניארית לעומת SA | בהובלת Harvard | [D][435] |
| 2024 | 60 אטומי Sr; F_d = 0.095(11) בשזירה רוויה | Caltech | [D][436] |
| 2025-06-04 | שבירת מיתר ב-(2+1)D על Aquila | QuEra et al. | [D][226] |

מעל ~100 אטומים דבר אינו נבדק במדויק: עבודת 196 האטומים הותאמה לחישוב נומרי רק עד ~100 [D][433]. ההאצה של 2022 לא שרדה: פותרים קלאסיים מגיעים לאופטימום על אותם מופעים דמויי Union Jack, עד אלפי צמתים, בתוך דקות [D][431]. Pasqal מציעה QPU אנלוגי של 100 קיוביטים ב-Google Cloud (2025-05-13) [C][437]; נכון ל-2026-09-26 לא נמצא גיליון נתונים של Fresnel כמו זה של Aquila.

## ייצור, חומרים ושרשרת האספקה
אין פרוסה; ההרכבה האופטית משותפת לארכיטקטורות האטומים הספרתיות. Orion Gamma: 140 קיוביטים, טמפרטורת החדר, 3 kW בממוצע, מרווח מינימלי של 5 µm [C][438]. התוספת הייחודית לפעולה האנלוגית היא שדה היסט ברזולוציה של אתר בודד, שאת החומרה שלו QuEra לא תיארה [C][439]; שום דבר אחר במקורות אינו מבדיל בין רשימת הרכיבים האנלוגית לספרתית [S].

## בקרה, קריאה ועומס הקלט-פלט
הבקרה אינה תלויה ב-N: כמה צורות גל, תבנית אחת וגאומטריה [C][262]. העלות עוברת לקריאה ולחזרות. Aquila קוראת בטעות 8% מהאטומים במצב רידברג ו-1% מהאטומים במצב היסוד, ומשאירה 0.7% מהאתרים ריקים [C][262], ולכן תמונת מצב של 256 אתרים, מחציתם מעוררים, נקראת ללא שגיאה בהסתברות 0.92¹²⁸×0.99¹²⁸ ≈ 6×10⁻⁶, ול-~17% מהריצות יש אוגר נטול פגמים [S]. הריצות מתבצעות בפחות מ-10 Hz ב-Aquila [C][262] וב-≥0.25 Hz אפקטיבי ב-Orion Gamma [C][438]: 10⁴ ריצות אורכות בין ≥17 min ל-~11 h [S].

## תפקיד במחסנית
משבצת 3 בארכיטקטורה "סימולטור אנלוגי של אטומים ניטרליים (מערכי רידברג, גזי סריג)" (אטום אלקלי → קיוביט אנלוגי יסוד–רידברג → הטכנולוגיה הזו → הובלה ב-AOD → בקרת לייזר + AOD/SLM → דימות פלואורנות; שכבות 7–9 ריקות; הרכבה אופטית), המשרתת את G1. היא **דורשת** את האטום האלקלי, את קידוד יסוד–רידברג ולייזרי רידברג גלובליים; היא אינה **מספקת** דבר לשכבות שמעליה; היא אינה **מחליפה** דבר, ו-g_ryd מחליף אותה כשמכונה הופכת לספרתית. המרשם: Aquila (QuEra, 256 אתרים) ו-Fresnel/Fresnel 2 (Pasqal, 100 קיוביטים) נושאות אותה כטכנולוגיה ראשית, שתיהן ✅; קו Orion של Pasqal נושא אותה כחלופית בארכיטקטורה "מערך מלקחיים אופטיים רידברג — אלקליים (Rb/Cs)", 🔎. פנקס הפערים הציע את ארכיטקטורות המערכים האלקליים והאלקליים-עפרוריים; הטכנולוגיה קיבלה ארכיטקטורה משלה, ואף מכונה אלקלית-עפרורית במרשם אינה מריצה אותה, אף שמדד הנאמנות שלמעלה השתמש ב-Sr [D][436] — קשת ה"דורש אטום אלקלי" צרה יותר מהפיזיקה.

## ראיות — כיצד נמדדו המספרים
בהיעדר שגיאת שער, הנאמנות נגזרת מגדלים נצפים: פרמטרי סדר מול חישוב נומרי, תקפים עד ~100 אטומים [D][433]; F_d, השוקל מחרוזות ביטים שנמדדו לפי הסתברויות מדומות — 0.095(11) ב-60 אטומים, שם MPS של חרוט אור ב-χ* = 3400 (~110 GB, ~180 ימי ליבה) עומד בקצב [D][436]; ופלט הבעיה, כמו גודל ה-MIS, שזול לתקף אך לא להוכיח את אופטימליותו [D][431]. F_d זקוק להסתברויות קלאסיות, ולכן מה שהוא מאשר ניתן לסימולציה. Λ אינו מוגדר. התא של Orion נשאר 🔎: הדף המצוטט שלו (2026-01-29) מזכיר היסט מקומי לסימולציית חומרים ואת Vela של 2026 עם יותר מ-256 קיוביטים, אך לא אופן פעולה אנלוגי, MIS, Orion או ≤100 קיוביטים [C][390].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| QuEra Computing | מפתח | ארה״ב | Aquila, 256 אתרים, ב-Braket מאז 2022 | [C][162] |
| Pasqal | מפתח | צרפת | QPU אנלוגי של 100 קיוביטים; אופן פעולה אנלוגי ב-Orion | [C][437] |
| Amazon Web Services | ערוץ ענן | ארה״ב | היסט מקומי ב-Aquila לפי בקשה, 2024-04-11 | [C][440] |
| Harvard/MIT | מחקר | ארה״ב | ניסויים של 51 עד 289 אטומים | [D][435] |
| Caltech | מחקר | ארה״ב | מדד F_d, 60 אטומי Sr | [D][436] |

**כספים.**
- 2025-09-09 · QuEra · הרחבת סבב B, NVentures מצטרפת · USD 230 M · הוכרז; מכוון לסבילות לתקלות [C][153]
- 2026-08-28 · Pasqal · מיזוג SPAC, Nasdaq PSQL · ~USD 360 M מזומנים · נסגר [P][156]

**שוק ושרשרת אספקה.** שני ספקים, שני ערוצי ענן. Pasqal מדווחת על שבע יחידות QPU בהפעלה ומשווקת את הפלטפורמה שלה כאנלוגית כיום [P][156]; ההצעה האנלוגית של QuEra היא מכונה אחת. משלמים עליה רק ב-G1.

**קניין רוחני ותקנים.** נכון ל-2026-09-26 אין ספירת פטנטים ייחודית לפעולה האנלוגית; פורמט התוכנית מוגדר בענן (Braket AHS) [C][429]; אין גוף תקינה.

**מפות דרכים ועמידה בהבטחות.** Pasqal הבטיחה 10,000 קיוביטים פיזיים ל-2026 (2024-03-13) [R][167]; ההשקה שלה ב-2026 היא Vela, עם יותר מ-256 קיוביטים [R][390] — ~39× פחות [S] — והחוברת שלה מדברת על אספקה ב-2027, 200+ [C][438]. Libra של QuEra (2028) ספרתית, ללא מפרט אנלוגי [R][162].

**פרשנות אסטרטגית.** אופן הפעולה האנלוגי הוא גשר ההכנסות של שני הספקים בזמן ש-g_ryd מבשיל. עם יתרון מאושר מעל ~100 אטומים הוא יישאר מכשיר של G1; בלעדיו, הוא יהפוך לאופן פעולה של מכונות ספרתיות, כמו ב-Orion.

## תחזית ושאלות פתוחות
לאשר אם עד 2027-12-31 מכונה אנלוגית מסחרית תפרסם נאמנות רב-גופית ב-≥60 אטומים, או שתוצאה אנלוגית תשרוד שנה של אתגר קלאסי; להוריד בדרגה אם Vela והמערכות הבאות של QuEra יסופקו ללא מפרטים אנלוגיים. שאלות פתוחות. (1) האם F_d יכול לאשר מעבר לגודל שבו MPS עומד בקצב? (2) מהן שגיאות הכיול של ההיסט המקומי לכל אתר? (3) כיצד מתחלק האובדן ב-T2 תחת הנעה בין רעש פאזה, דופלר ופיזור? (4) האם השמטת מחיקות יכולה לבצע בחירה בדיעבד בריצות רב-גופיות בעלות סבירה במספר הריצות? (5) האם קשת ה"דורש אטום אלקלי" תשרוד מכונות אנלוגיות אלקליות-עפרוריות?

## מקורות
[143] P. Scholl, A. L. Shaw, R. B.-S. Tsai, R. Finkelstein, J. Choi, and M. Endres, “Erasure conversion in a high-fidelity Rydberg quantum simulator,” *Nature*, vol. 622, p. 273, 2023, doi: [10.1038/s41586-023-06516-4](https://doi.org/10.1038/s41586-023-06516-4). [arXiv:2305.03406](https://arxiv.org/abs/2305.03406). [D]
[153] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[156] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [C]
[167] J. Russell, “PASQAL Issues Roadmap to 10,000 Qubits in 2026 and Fault Tolerance in 2028,” HPCwire, Mar. 13, 2024. [Online]. Available: https://www.hpcwire.com/2024/03/13/pasqal-issues-roadmap-to-10000-qubits-in-2026-and-fault-tolerance-in-2028/ [R]
[226] D. González-Cuadra *et al.*, “Observation of string breaking on a (2 + 1)D Rydberg quantum simulator,” *Nature*, vol. 642, no. 8067, pp. 321–326, Jun. 2025, doi: [10.1038/s41586-025-09051-6](https://doi.org/10.1038/s41586-025-09051-6). [D]
[262] J. Wurtz *et al.*, “Aquila: QuEra's 256-qubit neutral-atom quantum computer,” [arXiv:2306.11727](https://arxiv.org/abs/2306.11727), Jun. 2023. [C]
[384] H. Bernien *et al.*, “Probing many-body dynamics on a 51-atom quantum simulator,” *Nature*, vol. 551, pp. 579–584, Nov. 2017, doi: [10.1038/nature24622](https://doi.org/10.1038/nature24622). [arXiv:1707.04344](https://arxiv.org/abs/1707.04344). [D]
[385] L. Henriet *et al.*, “Quantum computing with neutral atoms,” *Quantum*, vol. 4, Art. no. 327, Sep. 2020, doi: [10.22331/q-2020-09-21-327](https://doi.org/10.22331/q-2020-09-21-327). [arXiv:2006.12326](https://arxiv.org/abs/2006.12326). [D]
[390] L. Garbini, “Inside Pasqal's 2026 Vision on Quantum for Industry and Research,” Pasqal, Jan. 29, 2026. [Online]. Available: https://www.pasqal.com/blog/inside-pasqals-2026-vision-on-quantum-for-industry-and-research/ [C]
[429] Amazon Web Services, “Explore Experimental Capabilities - Amazon Braket,” Amazon Braket Developer Guide. [Online]. Available: https://docs.aws.amazon.com/braket/latest/developerguide/braket-access-local-detuning.html [C]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[431] R. S. Andrist *et al.*, “Hardness of the Maximum Independent Set Problem on Unit-Disk Graphs and Prospects for Quantum Speedups,” *Phys. Rev. Research*, vol. 5, no. 4, Art. no. 043277, 2023, doi: [10.1103/PhysRevResearch.5.043277](https://doi.org/10.1103/PhysRevResearch.5.043277). [arXiv:2307.09442](https://arxiv.org/abs/2307.09442). [D]
[432] S. Ebadi *et al.*, “Quantum Phases of Matter on a 256-Atom Programmable Quantum Simulator,” *Nature*, vol. 595, p. 227, Jul. 2021, doi: [10.1038/s41586-021-03582-4](https://doi.org/10.1038/s41586-021-03582-4). [arXiv:2012.12281](https://arxiv.org/abs/2012.12281). [D]
[433] P. Scholl *et al.*, “Programmable quantum simulation of 2D antiferromagnets with hundreds of Rydberg atoms,” *Nature*, vol. 595, p. 233, Jul. 2021, doi: [10.1038/s41586-021-03585-1](https://doi.org/10.1038/s41586-021-03585-1). [arXiv:2012.12268](https://arxiv.org/abs/2012.12268). [D]
[434] G. Semeghini *et al.*, “Probing Topological Spin Liquids on a Programmable Quantum Simulator,” *Science*, vol. 374, p. 1242, Dec. 2021, doi: [10.1126/science.abi8794](https://doi.org/10.1126/science.abi8794). [arXiv:2104.04119](https://arxiv.org/abs/2104.04119). [D]
[435] S. Ebadi *et al.*, “Quantum Optimization of Maximum Independent Set using Rydberg Atom Arrays,” *Science*, vol. 376, p. 1209, Jun. 2022, doi: [10.1126/science.abo6587](https://doi.org/10.1126/science.abo6587). [arXiv:2202.09372](https://arxiv.org/abs/2202.09372). [D]
[436] A. L. Shaw *et al.*, “Benchmarking highly entangled states on a 60-atom analog quantum simulator,” *Nature*, vol. 628, pp. 71–77, 2024, doi: [10.1038/s41586-024-07173-x](https://doi.org/10.1038/s41586-024-07173-x). [arXiv:2308.07914](https://arxiv.org/abs/2308.07914). [D]
[437] Pasqal, “Pasqal's Neutral-Atom Quantum Computer Available on Google Cloud Marketplace,” May 13, 2025. [Online]. Available: https://www.pasqal.com/newsroom/pasqals-neutral-atom-quantum-computer-available-on-google-cloud-marketplace/ [C]
[438] Pasqal and O. Q.-C. P. brochure, “The Power of Neutral Atom Quantum Processors by Pasqal — Unlock Quantum Computing for Real-World Solutions,” Pasqal, product brochure (PDF). [Online]. Available: https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf [C]
[439] QuEra Computing, “Local Qubit Control Brings New Capabilities to QuEra's Quantum Computer,” Apr. 17, 2024. [Online]. Available: https://www.quera.com/press-releases/local-qubit-control-brings-new-capabilities-to-queras-quantum-computer [C]
[440] Amazon Web Services, “Local detuning now available on QuEra's Aquila device with Braket Direct,” AWS What's New, Apr. 11, 2024. [Online]. Available: https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-braket-experimental-capabilities-quera-device-braket-direct/ [C]

## פריטי אימות פתוחים
- מגבלות ההיסט המקומי של Aquila (גודל, רזולוציה, שגיאת כיול לכל אתר) חשופות רק דרך מאפייני ההתקן ב-Braket SDK, ולא נקראו כאן; המנגנון החומרתי (אלומת הסטת אור או אחר) אינו מתואר בהודעה של QuEra (נוסה ב-2026-09-26).
- המסמך הטכני של Aquila אינו נותן זמן חיים של מצב רידברג או קצב אובדן אטומים במהלך ההתפתחות; לא נמצא גיליון נתונים של Fresnel (Ω, Δ, T2, שגיאות גילוי), ודף ה-QPU של Pasqal ב-Scaleway לא נטען (2026-09-26).
- התא של Orion במרשם ("MIS/אופטימיזציה אנלוגיים והמילטוניאנים של חומרים שהוצגו ב-≤100 קיוביטים") אינו נתמך בדף המצוטט שלו; הוא נשאר 🔎 (2026-09-26).
- לגרסת ה-XY הדיפולרית שבתיאור הטכנולוגיה אין מכונה במרשם, והיא לא נבדקה מול מקור ראשוני (2026-09-26).
- המשך השירות של Aquila ב-Braket מוסק מההודעה של QuEra מ-2026-06-15, שאינה אומרת זאת במפורש (2026-09-26).
