---
id: fluxq
name: קיוביט שטף rf-SQUID (מחשב הרפיה)
layer: "1 נושא הקיוביט"
status: demonstrated
since: 2011
one_line: לולאה מוליכת-על בעלת בור כפול, המשמשת כספין איזינג ניתן לתכנות במחשבי ההרפיה של D-Wave; אין ערכת שערים, אין קוד.
verdict: נכון ל-4 בספטמבר 2026 אף טענה של D-Wave ליכולת שמעבר לקלאסית לא שרדה הפרכה; הפסק יופרך אם טענה אחת תחזיק מעמד עד 2028, ויאושר — דוגם ולא פותר — אם השחיקה תחזור.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
לולאה מוליכת-על עם צומת ג'וזפסון מורכב: הטיית השטף קובעת את גובה המחסום ואת השיפוע; שני מצבי הזרם המעגלי הם ספין איזינג. קו המוצרים של D-Wave, מ-D-Wave One (2011) ועד Advantage2 (זמינות כללית ב-2025-05-20: 4,400+ קיוביטים, Zephyr מדרגה 20, 12.5 kW) [P][220], נשען עליו. אין ערכת שערים — רק המילטוניאן איזינג ניתן לתכנות בשדה רוחבי, שממנו דוגמים.
נושא מיוצר; זמן אופייני ~3 ns, אין פעולת שזירה דטרמיניסטית; קריאה דיספרסיבית ~1 µs, לא הרסנית, לא באמצע המעגל.
צימוד מדרגה 20; בקרת שטף בתדר נמוך ב-mK; שגיאת פאולי ועוד שגיאה קוהרנטית; ליתוגרפיה של מוליכי-על.

## פיזיקה וגבולות
משרעת המנהור והזרם המתמיד קובעים את הבור. לנדאו–זנר מחייב סריקה איטית ביחס לריבוע הפער המינימלי, שבמופעים קשים נסגר באופן מעריכי עם הגודל: הרצפה הראשונה קומבינטורית, לא חומרית. הרצפה התרמית מגבילה מוקדם יותר: ב-15–20 mK, kT הוא כמה מאות MHz, ולכן מתחת לפער כזה השבב מגיע לשיווי משקל עם האמבט שלו ופולט דגימה כמעט-בולצמנית, לא מצב יסוד. רעש שטף 1/f גורם לדה-פאזה בבסיס העצמי של האנרגיה, ובכך הופך אובדן דיאבטי לבלתי ניתן להבחנה מפער קשה. שלבי קירור קרים יותר, זרם מתמיד גדול יותר או הרפיות חטופות בנות ננו-שניות מזיזים את הרצפה.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2021-09 | טופולוגיית Zephyr, דרגה 20 | D-Wave | [G:DWAVE-ZEPHYR-2021] |
| 2025-03 | טענה ליכולת שמעבר לקלאסית — דינמיקת הרפיה חטופה, לא אופטימיזציה | D-Wave | [D][221] |
| 2025-05-20 | זמינות כללית של Advantage2: 4,400+ קיוביטים, 12.5 kW | D-Wave | [P][220] |
| 2025–26 | נשחקה בידי רשתות טנזורים עם התפשטות אמונה; t-VMC | Tindall et al.; Mauron & Carleo | [D][222]; [D][223] |

השגיאה השולטת: עירור תרמי סמוך לפער המינימלי.

## ייצור, חומרים ושרשרת האספקה
ליתוגרפיה רב-שכבתית של מוליכי-על מסוג Nb/Al, מאותה משפחה של מפעלי הטרנסמונים. דוח ה-10-K לשנת הכספים 2024 מזכיר מפעלי ייצור של צד שלישי עם מקור שני שהודגם; EDGAR מחזיר תשעה אזכורים של SkyWater בדוחות ה-10-K של D-Wave בשנים 2023–26 [G:DWAVE-FAB-10K], ו-SkyWater בבעלות IonQ מאז 2026-07-31 [G:IONQ-SKYWATER-2026] — המקור הזה יושב בתוך מתחרה. הנכס האמיתי הוא הקלט-פלט: DAC-שטף בריבוב על השבב מחזיקים את מספר הקווים מטמפרטורת החדר על O(100) עבור עשרות אלפי קיוביטים ומצמדים, לעומת O(מספר הקיוביטים) במכונות שערים — אם כי D-Wave מצטטת 200 חוטי הטיה (2026-01-06) ו-~300 (מסמך טכני, 2026-01-23), בלי יישוב הסתירה [C][G:DWAVE-FLUXDAC-LINECOUNT-CONFLICT]. הקיר ב-10⁴–10⁶ ספינים הוא תקורת שיכון המינורים (minor embedding) ומתקן הקירור של 12.5 kW, לא החיווט. ECCN 4A906 נשען על שגיאת שער דו-קיוביטי, שאינה מוגדרת כאן; במקומו חלים על המקררים סיווגי 3A904 [G][301].

## תפקיד במחסנית
משרת את ארכיטקטורת ההרפיה בלבד ואינו מזין אף ארכיטקטורה של מודל השערים: מפת הדרכים של D-Wave לשערים נשענת על חומרת המסילה הכפולה של Quantum Circuits שנרכשה — נושא אחר [C][G:DWAVE-QCI-2026-01]. ההעברה פועלת בכיוון ההפוך: שבב ה-DAC-שטף מניע כעת פלוקסוניום, וחלקים מרכזיים בו יוצרו ב-NASA JPL [C][281]. אין כאן שעון נגזר, אין בחינת ביצועים אקראית ואין נפח קוונטי, ולכן כל כותרת היא זמן-לפתרון מול פותר קלאסי. הטענה ממרץ 2025 נשחקה בתוך שבועות [222], [223]; התשובה של D-Wave (arXiv:2508.15759) הופכת את נטל ההוכחה, ומשתמשת ב-QPU כאמת הבסיס כדי לטעון שהאקסטרפולציות של קנה המידה ברשתות טנזורים אינן אמינות [P][224]. לא הוכרע נכון ל-4 בספטמבר 2026.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| D-Wave Quantum | מפתח | ארה״ב/קנדה | ספקית מחשבי ההרפיה היחידה; Advantage2, Leap | [C][15] |
| US Dept of Commerce | משקיע | ארה״ב | מכתב כוונות של CHIPS בסך $100 M | [G:CHIPS-LOI-2026-05] |
| Anduril Industries | משתמש | ארה״ב | הפותר Stride על Advantage2 | [P][G:DWAVE-FAU-ANDURIL-2026-01] |
| Florida Atlantic University | משתמש | ארה״ב | Advantage2 בקמפוס תמורת $20 M | [P][372] |
| NASA JPL | ספק | ארה״ב | ייצר חלקים לשבב ה-DAC-שטף | [C][281] |

**כספים.** 2026-01-20 · D-Wave · מיזוג ורכישה, Quantum Circuits · $550 M USD · נסגר [C][G:DWAVE-QCI-2026-01]. 2026-01-27 · מכירה ל-FAU · $20 M USD · הוכרז [P][372]. 2026-01-27 · QCaaS, Fortune 100 · $10 M USD · הוכרז [C][373]. 2026-05-21 · LOI של CHIPS · $100 M USD · Commerce · לא מחייב [G:CHIPS-LOI-2026-05]. 2026-08-06 · המחצית הראשונה של 2026 · הכנסות $5.9 M (−67% משנה לשנה), הזמנות $35.5 M (+1,120%), RPO $40.7 M · דווח [C][15].

**שוק ושרשרת אספקה.** ספק אחד, נושא אחד, סוג אחד של מתקן קירור; כושר מפעל הייצור משותף עם קווי מודל השערים. רק G1 וחלקים מ-G5 משלמים עליו; G3/G4 אינם יכולים, בהיעדר שכבת קוד.

**קניין רוחני ותקנים.** הסקירה של PatSnap שפורסמה ב-2026-06-30 מונה 975 משפחות פטנטים קוונטיים של D-Wave [P][G:PATSNAP-2026-06]; לא נמצאו התדיינות משפטית או תקן ייחודיים להרפיה.

**מפות דרכים ועמידה בהבטחות.** (2025-05 · ל-2029/2031 · 20,000 ואחר כך 100,000 קיוביטים · פתוח) [R][15]. אבני הדרך של קנה המידה מגיעות בזמן; הטענות אינן שורדות מול פותרים קלאסיים; ההכנסות קרסו בעוד ההזמנות וה-RPO עלו, ולכן המונטיזציה נדחתה, לא אבדה.

**פרשנות אסטרטגית.** D-Wave מנצחת אם הקונים ימשיכו לשלם על דגימה טובה דיה בקלט-פלט זול, ומפסידה אם מכונות שערים עם הפחתת שגיאות ייקחו את תקציב האופטימיזציה — ולכן קנתה נושא של מודל השערים. כוח תמחור מול לקוחות; אפס כוח מול מפעלי ייצור.

## תחזית ושאלות פתוחות
לאשר אם טענה על מחלקת מופעים שהוצגה מדעית שורדת סבב קלאסי לאורך 2027; להוריד בדרגה אם השחיקה תחזור. התרחיש הטוב ביותר ל-2029: 20,000 קיוביטים וטענה שעמדה במבחן; התרחיש הגרוע ביותר: קו המוצרים קופא ב-Advantage2 בעוד התפנית לשערים בולעת את המזומנים. פתוח: האם מופע כלשהו עמיד בפני התפשטות אמונה ו-t-VMC?

## מקורות
[15] D-Wave Quantum Inc., “D-Wave Reports Second Quarter 2026 Results,” Aug. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/ [C]
[220] M. Swayne, “D-Wave Announces General Availability of Advantage2 Quantum Computer,” The Quantum Insider, May 20, 2025. [Online]. Available: https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/ [P]
[221] A. D. King *et al.*, “Beyond-classical computation in quantum simulation,” *Science*, vol. 388, pp. 199–204, 2025, doi: [10.1126/science.ado6285](https://doi.org/10.1126/science.ado6285). [arXiv:2403.00910](https://arxiv.org/abs/2403.00910). [D]
[222] J. Tindall, A. Mello, M. Fishman, M. Stoudenmire, and D. Sels, “Dynamics of disordered quantum systems with two- and three-dimensional tensor networks,” *Science*, vol. 392, pp. 868–872, 2026, doi: [10.1126/science.adx2728](https://doi.org/10.1126/science.adx2728). [arXiv:2503.05693](https://arxiv.org/abs/2503.05693). [D]
[223] L. Mauron and G. Carleo, “Challenging the Quantum Advantage Frontier with Large-Scale Classical Simulations of Annealing Dynamics,” [arXiv:2503.08247](https://arxiv.org/abs/2503.08247), Mar. 2025. [D]
[224] A. Nocera, J. Raymond, W. Bernoudy, M. H. Amin, and A. D. King, “Evaluating classical simulations with a quantum processor,” [arXiv:2508.15759](https://arxiv.org/abs/2508.15759), Aug. 2025. [P]
[281] D-Wave, “D-Wave Demonstrates First Scalable, On-Chip Cryogenic Control of Gate-Model Qubits,” Jan. 6, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-demonstrates-first-scalable-on-chip-cryogenic-control-of-gate-model-qubits/ [C]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[372] M. Abdel-Kareem, “D-Wave Announces HQ Relocation, $20M System Sale, $10M Fortune 100 Deal, and Dual-Platform Advancements,” Quantum Computing Report, Jan. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/d-wave-announces-hq-relocation-20m-system-sale-and-defense-performance-breakthroughs/ [P]
[373] D-Wave Quantum, “D-Wave Announces $10 Million, Two-Year Enterprise QCaaS Agreement with Fortune 100 Company,” Jan. 27, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-announces-10-million-two-year-enterprise-qcaas-agreement-with-fortune-100-company/ [C]

## פריטי אימות פתוחים
מספר חוטי ההטיה: 200 (הודעה, 2026-01-06) מול ~300 (מסמך טכני 14-1090A-A, 2026-01-23) — לא יושב; נתון המסמך הטכני קשור למערך מתואר. ההיקף המדויק של הקשר עם SkyWater בדוחות ה-10-K של D-Wave (תשעה אזכורים, המשפטים לא חולצו). זהות לקוח ה-QCaaS מ-Fortune-100 וזהות לקוח הקצה הביטחוני שמאחורי המחקר של Anduril/Davidson. האם מחשב הרפיה נופל בגדר ECCN 4A906 כאשר הסף מנוסח בשגיאת שער דו-קיוביטי — לא נמצאה הכרעה.
