---
id: dec_corr
name: פענוח מתואם / מודע-אובדן (טרנסוורסלי, אובדן אטומים)
layer: "8 מפענח"
status: demonstrated
since: 2025
one_line: מפענחים הצורכים את אותות הבישור של אובדן אטומים כמחיקות ממוקמות, ומפענחים על פני שכבות של שערים טרנסוורסליים במקום סבב אחר סבב.
verdict: ממשי על מערך נתונים אחד (1.73(13)× לעומת מפענח עיוור לאובדן, 448 אטומים, ארבעה סבבים); לא הוכח תחת טעינה מחדש, בעומק, או במעבדה שנייה.
updated: 2026-09-03
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
לא חומרה, אלא משמעת של פענוח. פענוח מודע-אובדן צורך את אות הבישור: אטום חסר הוא מחיקה באתר ידוע, ולכן המייצבים הנוגעים באתר הריק מוכפלים זה בזה לאופרטורים של *בדיקת-על* (supercheck) במשקל גבוה יותר, שעדיין מתחלפים עם הקוד ששרד [4]. פענוח מתואם פותר את היסטוריית הסינדרומים המשותפת על פני שכבות טרנסוורסליות (מבלוק לבלוק) במקום בלוק אחר בלוק; Cain et al. (Harvard, 2024-03-05) הראו שמספר הסבבים בין שערי קליפורד צונח O(d)→O(1) [738], והדבר הוכלל כסבילות תקלות אלגוריתמית (Nature 2025) [152].
f = אובדן + מחיקה; a/c/d/e/g = אין — חישוב קלאסי, ללא ייצור וללא מיקום [graph].

## פיזיקה וגבולות
אות הבישור הוא הנכס: יותר מ-80% מהדליפה במערכי רידברג היא אובדן אטומים, והדימות מוצא אותו [4]. מחיקה ממוקמת עולה למפענח רק את מסגרת פאולי, לא את המיקום — ולכן המרה למחיקה מעלה את הספים ברמת המעגל ב-3–4× בפיזיקת שער קבועה [8]. המחיר הוא המרחק: כל בדיקת-על היא מכפלה של שני מייצבים, ולכן כל אתר ריק מדלל את הקוד מקומית. פענוח מתואם משלם אחרת: שערי CNOT טרנסוורסליים מפיצים שגיאות בין בלוקים, ולכן הגרף גדל עם עומק המעגל, לא עם d. דבר אינו מזיז את הרצפה — השארית הלא-מבושרת נותרת כפי שהיא: דליפת m_F של 0.008(1)% לאטום לשער לעומת אובדן אטומים של 0.087(5)% [G:HARVARD-CZ-2026-04].
## מצב ההנדסה העדכני
| תאריך | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2025-11-10 | רווח של 1.73(13)× מדגלי אובדן + למידת מכונה לעומת פענוח רגיל, אותם נתונים של 448 אטומים | Harvard/MIT/QuEra | [D][4][G:HARVARD-LOSS-QEC-2025] |
| 2026-03 | מפענח אובדן מתואם: סף של 4% לעומת 3.2% בהנחת אובדן בלתי תלוי; 144 µs לסבב; סימולציה | QPerfect | [S][739][G:QPERFECT-CORRLOSS-2026-03] |
| 2026-06-12 | [[4,2,2]] ב-¹⁷¹Yb: דעיכה בלתי מותנית איטית 1.9(4)× עם מידע המחיקה (3.6(1)× הוא ההחזקה בבחירה בדיעבד) | Princeton | [D][142][G:PRINCETON-ERASURE-RESOLVED-2026-09] |

אותו מעגל: 2.14(13)×, d=3→5, ארבעה סבבים. האיבר השולט: אובדן אטומים, לא שגיאת פאולי.

## ייצור, חומרים ושרשרת האספקה
ללא מפעל: החישוב הקלאסי כבר נרכש לצורך הזיווג. ההשהיה קובעת את היקף התחולה: 144 µs לסבב נכנסים במחזור אטומים של 1–4.5 ms עם מרווח של 7–30× [739], אך הם ~130× מעל מחזור מוליכי-על של 1.1 µs — ולכן הדבר נשאר ייחודי לאטומים. רוחב הפס של דגלי האובדן הוא ביט אחד לאתר לסבב, ולכן הקיר ב-10³–10⁴ אטומים הוא הדימות של ~0.5–1 ms וחלון פענוח הגדל עם העומק הלוגי, לא הקישור. נקודות כשל יחידות שעברו בירושה: דימות qCMOS של Hamamatsu [G:HAMAMATSU-CAMERA-CONC-2026] ושני ספקי AOD [G:AOD-VENDORS-2026].

## תפקיד במחסנית
המפענח הראשי בשני מערכי המלקחיים האופטיים לאטומי רידברג, האלקליים (Rb/Cs) והאלקליים-עפרוריים (Yb/Sr). דורש קודים משורשרים בקצב גבוה עם שערים טרנסוורסליים; מספק את מחצית הפענוח של סבילות התקלות האלגוריתמית, שטענת מספר הסבבים הקבוע שלה אינה מגובה אחרת בחומרה. שעון נגזר = סכום סבב הסינדרום (שערים 1 µs, הובלה 800 µs, 1Q 10 µs, קריאה 501 µs) ≈ 1.3 ms, ~0.76 kHz; המפענח חייב להשיב בתוכו, לא לקבוע אותו. אימות: 1.73× הוא יחס בין מפענח למפענח על נתוני מעבדה אחת, ללא שחזור; 4% הוא סימולציה [739]. ארבעה סבבים אינם בוחנים סחיפה ולא טעינה מחדש; קוד הטורוס של Atom Computing הוא הביקורת, ובו הדיכוי נעלם עם טעינה מחדש (0.63% לעומת 0.64% למחזור) [148]. הפער בין 1.9(4)× ל-3.6(1)× של Princeton יושב: מאמר אחד, שני גדלים שונים [G:PRINCETON-ERASURE-RESOLVED-2026-09].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק | ראיות |
|---|---|---|---|---|
| Harvard/MIT | מחקר | ארה״ב | פענוח מתואם, בדיקות-על, 1.73(13)× | [D][4], [738] |
| QuEra | מפתח | ארה״ב | שותפה לכתיבה; Libra 2028 מניחה אותו | [D][4][C][153] |
| QPerfect (BTQ) | ספק | צרפת | מפענח אובדן מתואם; התאום הדיגיטלי של aQCess | [S][739][C][740] |
| Atom Computing | משתמש | ארה״ב | Yb עם מחיקה מובנית; דוגמה נגדית של טעינה מחדש | [D][148][C][154] |

**כספים.**
2025-04-09 · BTQ Technologies · €2 M ל-QPerfect לפי שווי של €10 M לפני הכסף (16.67%) · מסמך תנאים (term sheet) [P][741]
2026-07-22 · QPerfect · התאום הדיגיטלי של aQCess, Equipex+ ANR-21-ESRE-0032 · הוכרז [C][740]
2026-06-16 · Atom Computing · $100 M בסבב C (Third Point) + מכתב כוונות CHIPS על $100 M · נסגר + מכתב כוונות [C][154][G:ATOM-300M-2026-06]
2025-11-06 · DARPA QBI שלב B · Atom Computing ו-QuEra בין האחד-עשר · ≤$15 M לכל אחד [G:QBI-STAGEB-2025-11]

**שוק ושרשרת אספקה.** אין שוק רכיבים: מחזורי GPU/FPGA כבר נרכשו לצורך הזיווג; סיכון הריכוזיות יושב במעלה השרשרת, בדימות וב-AOD. משלמים עליו רק G3/G4.

**קניין רוחני ותקנים.** אף משפחת פטנטים מתוארכת אינה נוקבת בפענוח מודע-אובדן או בפענוח מתואם נכון ל-4 בספטמבר 2026; השיטות פתוחות, הקוד אקדמי.

**מפות דרכים ועמידה בהבטחות.** סבבים O(d)→O(1) (2024-03): ב-Nature 2025, הודגם רק במעגל של ארבעה סבבים. QuEra, 100 קיוביטים לוגיים (2024-01, ל-2026): כעת Libra ב-2028 [G:QUERA-LIBRA-2026]. הפיזיקה בזמן, המוצרים מאחרים.

**פרשנות אסטרטגית.** אם הדבר יעמוד, האטומים הופכים את חולשתם הגדולה ביותר לערוץ זול המובא בחשבון, וארכיטקטורות טרנסוורסליות גוברות על ניתוח סריג בעלות מרחב-זמן: QuEra, Atom Computing, Pasqal ו-Infleqtion מרוויחות, וספקי מוליכי-העל מאבדים את השהיית המפענח כמבדיל. איום תחליף: CZ של רידברג מעבר ל-99.95% מכווץ את איבר האובדן. לא-יריבי: אף ספק אינו יכול להשכירו.

## תחזית ושאלות פתוחות
לאשר אם המפענח של QPerfect ירוץ על סינדרומים אמיתיים או אם ספק שני יפרסם רווח מודע-אובדן משלו; להוריד בדרגה אם הרווח ימות תחת טעינה מחדש או מעבר לארבעה סבבים. התרחיש הטוב ביותר ל-2029: ברירת המחדל בכל מחסניות האטומים הניטרליים הסובלות תקלות; התרחיש הגרוע ביותר: ארכיטקטורה של קבוצה אחת, שלעולם אינה עוברת 10³ אטומים. פתוח: האם 1.73× מחזיק ב-10⁴ אטומים, בעומקים שבהם הגרף המתואם גדל מעבר לזיכרון, וביונים [667]?

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[8] Y. Wu, S. Kolkowitz, S. Puri, and J. D. Thompson, “Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays,” *Nat. Commun.*, vol. 13, Art. no. 4657, 2022, doi: [10.1038/s41467-022-32094-6](https://doi.org/10.1038/s41467-022-32094-6). [arXiv:2201.03540](https://arxiv.org/abs/2201.03540). [S]
[142] B. Zhang *et al.*, “Logical qubits with erasure conversion using metastable neutral atoms,” *Nat. Phys.*, vol. 22, no. 6, pp. 910–916, Jun. 2026, doi: [10.1038/s41567-026-03309-0](https://doi.org/10.1038/s41567-026-03309-0). [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). [D]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[152] H. Zhou *et al.*, “Low-Overhead Transversal Fault Tolerance for Universal Quantum Computation,” *Nature*, vol. 646, no. 8084, pp. 303–308, 2025, doi: [10.1038/s41586-025-09543-5](https://doi.org/10.1038/s41586-025-09543-5). [arXiv:2406.17653](https://arxiv.org/abs/2406.17653). [S]
[153] QuEra Computing, “QuEra Expands $230 Million Financing Round Advancing Quantum-Accelerated Supercomputing,” Sep. 9, 2025. [Online]. Available: https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing [C]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[667] A. Paetznick *et al.*, “Improved quantum processor logical error rates via correction and detection,” *Nature*, vol. 654, no. 8118, pp. 349–355, Jun. 2026, doi: [10.1038/s41586-026-10628-y](https://doi.org/10.1038/s41586-026-10628-y). [D]
[738] M. Cain *et al.*, “Correlated decoding of logical algorithms with transversal gates,” [arXiv:2403.03272](https://arxiv.org/abs/2403.03272), Mar. 2024. [D]
[739] H. Perrin, G. Roger, and G. Pupillo, “Correlated Atom Loss as a Resource for Quantum Error Correction,” [arXiv:2603.24237](https://arxiv.org/abs/2603.24237), Mar. 2026. [S]
[740] BTQ Technologies, “BTQ Technologies' QPerfect Subsidiary and the University of Strasbourg Partner to Support France's First Public Neutral-Atom Quantum Computing Platform,” PR Newswire, Jul. 22, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/btq-technologies-qperfect-subsidiary-and-the-university-of-strasbourg-partner-to-support-frances-first-public-neutral-atom-quantum-computing-platform-302831874.html [C]
[741] C. Choucair, “BTQ Technologies to Invest Over $2 Million in QPerfect to Advance Neutral Atom Quantum Computing,” The Quantum Insider, Apr. 9, 2025. [Online]. Available: https://thequantuminsider.com/2025/04/09/btq-technologies-to-invest-over-2-million-in-qperfect-to-advance-neutral-atom-quantum-computing/ [P]
[G] Bluvstein et al. (Harvard/MIT/QuEra), Nature 649, 39 (online 2025-11-10; arXiv:2506.20661, 2025-06-25): surface code on up to 448 atoms, 2.14(13)× below threshold in a four-round c… · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[G] Evered, Xu, Li, Geim, Bonilla Ataides, Kalinowski, Bluvstein, Maskara, Kokail, Greiner, Vuletic, Lukin (Harvard/MIT), "High-fidelity entangling gates and nonlocal circuits with neu… · 2026-04-28 · https://arxiv.org/abs/2604.25987
[G] Perrin, Roger, Pupillo (Univ. Strasbourg/CNRS, QPERFECT SAS), "Correlated Atom Loss as a Resource for Quantum Error Correction", arXiv:2603.24237 (2026-03): fast correlated-loss de… · 2026-03 · https://arxiv.org/html/2603.24237
[G] CONFLICT RESOLVED: the 1.9(4)x and 3.6x figures both appear in arXiv:2506.13724v2 (Princeton [[4,2,2]] metastable 171-Yb) and describe different quantities — the logical decay rate… · 2026-09-04 · https://arxiv.org/html/2506.13724v2
[G] Hamamatsu Photonics ORCA-Quest qCMOS is the named single-photon-sensitivity camera in the Harvard/QuEra 448-atom fluorescence-imaging line and in MIT, NIST/UMD and Osaka neutral-at… · 2026-09 · https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html
[G] Only two acousto-optic deflector suppliers are named across the sourced neutral-atom literature: AA Opto-Electronic (France; DTSX-400 crossed AODs in the Harvard 448-atom system, a… · 2026-09-04 · https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers
[G] QuEra: Libra fault-tolerant system 2028 (>256 logical, 10⁻⁶, on Braket) and gigaquop system 2028–29 — its Jan-2024 roadmap had promised 100 logical qubits in 2026 · 2026-06-15 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[G] Atom Computing: $100 M Series C (Third Point) plus $100 M DoC CHIPS LOI, total > $300 M, 2026-06-16 · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[G] DARPA QBI Stage B (announced 2025-11-06, ~12 months, up to $15 M each): Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon… · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
## פריטי אימות פתוחים
- הרווח של 1.73(13)× לא שוחזר מחוץ למערך הנתונים של 448 האטומים של Harvard/MIT/QuEra, ומפענח הייחוס שלו היה בחירתו של אותו צוות.
- הסף של QPerfect, 4% לעומת 3.2%, הוא סימולציה בלבד; לא נמצאה בדיקה על סינדרומים מחומרה נכון ל-4 בספטמבר 2026.
- האופציה של BTQ לרכוש את QPerfect במלואה מומשה בין 2025-04 ל-2026-07 (ההודעה המאוחרת מכנה את QPerfect חברה בבעלות מלאה); לא נמצאו תאריך סגירה או מחיר.
- לא נמצאה משפחת פטנטים מתוארכת לפענוח מודע-אובדן או לפענוח מתואם.
