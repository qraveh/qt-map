---
id: fab_optics
name: הרכבה אופטית / מכנית (לייזרים, ואקום, אובייקטיבים)
layer: "10 ייצור"
status: demonstrated
since: 2016
one_line: מחסנית הלייזרים, הוואקום העל-גבוה ואופטיקת הדימות הלוכדת, מקררת, ממענת וקוראת קיוביטים הן של יונים לכודים והן של אטומים ניטרליים — תשתית, לא קיוביט.
verdict: משרת שתי משפחות פלטפורמה, יונים ואטומים — מפעלי הייצור הפוטוניים ומפעלי ה-CMOS משרתים יותר — ולכן ספקיו אינם תלויים במודאליות; האספקה מרוכזת בהיגוי האלומות, בשני יצרני מסיטים אקוסטו-אופטיים (AOD), ואילו ללייזרים יש מובילה (TOPTICA) בין שישה ספקים נקובים, והולכת האור במרחב חופשי היא החומה מעבר ל-~10⁴ אתרים.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
התשתית המשותפת של לייזרים, ואקום על-גבוה ואופטיקת דימות, שעליה נשענים היונים הלכודים (Quantinuum, AQT, IonQ) ומערכי המלקחיים האופטיים של אטומים ניטרליים (Harvard עם QuEra, Pasqal, Atom Computing, Infleqtion, Google). היא אינה מחזיקה קיוביט ואינה מבצעת שער: היא מספקת אור קירור ומיעון, כליאה בוואקום, אובייקטיבים בעלי צמצם נומרי (NA) גבוה ואת היגוי האלומות הממקם את האטומים. היא הפכה לדיסציפלינה נפרדת, עם ספקים ייעודיים, מסביבות 2016.
תכונות: אין לה נושא, זמן שזירה, ערוץ קריאה או ניידות משלה — זו השכבה הפיזית שעליה נשענות טכנולוגיות אחרות.
קטגוריית הייצור: אופטיקה והרכבה מכנית; השגיאה שהיא תורמת במורד הזרם קוהרנטית — סחיפה, רעידות, סטיות בכיוון האלומה ורעש תדר, לא רעש פאולי סטוכסטי.

## פיזיקה וגבולות
רעש התדר ורעש העוצמה של הלייזר הופכים לדה-פאזה קוהרנטית בכל שער המונע באור הזה. לחץ גז הרקע קובע את זמן החיים של האטומים — מקור אחד לאובדן אטומים, לצד השערים והדימות — ובמערכת 448 האטומים האובדן הוא יותר מ-80% מכלל הדליפה: ניתן לגילוי, ולכן ניתן להמרה למחיקה, וכך השליטה באובדן, ובכללה הוואקום, הופכת לנכס ברמת הקוד [D][4]. הצמצם הנומרי של האובייקטיב קובע את מרווח המלקחיים האופטיים ואת ההפרעה ההדדית. היגוי האלומות קובע את מהירות הסידור מחדש תחת שתי מגבלות המושכות זו נגד זו — מסיט מבחין במספר נקודות השווה למכפלת רוחב הפס שלו בתדר הרדיו בזמן מעבר הגל האקוסטי דרך האלומה, ואותו זמן מגביל את מהירות ההכוונה מחדש של מלכודת — ואילו מאפנני גביש נוזלי מחליפים תמונה רק בקצב של עשרות הרץ. איבר ההגדלה הקשה יותר הוא ההספק: אור רידברג ואור ראמאן מתחלקים בין האתרים, ולכן מערך נעשה מוגבל-הספק לפני שהוא נעשה מוגבל-אופטיקה. את הרצפה מזיזים אינטגרציה פוטונית ומסיטים בעלי רוחב פס גבוה יותר; אף אחד מהם אינו מבטל את הוואקום או את האובייקטיב.

## מצב ההנדסה העדכני
התוצאה המרכזית היא פעולה רציפה: שני מסועים של סריג אופטי מובילים מאגרי אטומים אל אזור הניסוי, אטומים נשלפים אל המלקחיים האופטיים בקצב של 300,000 בשנייה, ומן השטף הזה המערכת יוצרת יותר מ-30,000 קיוביטים מאותחלים בשנייה — די כדי להחזיק מערך של יותר מ-3,000 אטומים במשך יותר משעתיים, כשהקיוביטים המאוחסנים שומרים על T₂ מעל שנייה: 1.34 s ללא הפרעה, 1.15 s בזמן שהמלכודת המגנטו-אופטית טוענת אטומים חדשים, ו-1.09 s בזמן דימות ומיון [D][144]. שני הקצבים נכונים, וכל אחד מהם מודד דבר אחר. במקומות אחרים: 11,000 אטומים ב-18,225 מלקחיים אופטיים של מטא-משטח, ללא שערים [D][145], ו-6,100 אטומים עם קוהרנטיות של 12.6 s [D][138]. Pasqal מציינת הספק ממוצע של 3 kW ומסה של 2,500 kg למסד Orion Gamma הפועל בטמפרטורת החדר [C][438] — נתון מעלון פרסומי, לא נתון שעבר ביקורת.

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2024-03 | מערך מלקחיים אופטיים של 6,100 אטומים, קוהרנטיות של 12.6 s | Caltech | [D][138] |
| 2025-11 | הספק ממוצע 3 kW, 2,500 kg, טמפרטורת החדר | Pasqal Orion Gamma | [C][438] |
| 2025-09 | 300,000 אטומים/s אל המלקחיים האופטיים, 30,000 קיוביטים מאותחלים/s, >3,000 אטומים מוחזקים >2 h | Harvard עם QuEra | [D][144] |
| 2026-06 | 11,000 אטומים ב-18,225 מלקחיים אופטיים של מטא-משטח, ללא שערים | Tsinghua | [D][145] |

## ייצור, חומרים ושרשרת האספקה
ללייזרים יש מובילה, לא מונופול: TOPTICA Photonics (מינכן) מדווחת על הכנסות של EUR 140 M ועל 600 עובדים, ומכנה את הטכנולוגיה הקוונטית השוק שעליו נוסדה [C][815], והיא מוזכרת כספקית העיקרית של בוני מחשבי היונים, לצד MOGLabs, Menlo Systems, Coherent, Thorlabs ו-NKT [P][322]. האספקה מרוכזת בהיגוי האלומות, דואופול למעשה: רק שני יצרני מסיטים מופיעים בספרות האטומים הניטרליים שבמקורות — AA Opto-Electronic, שמסיטי ה-AOD המוצלבים שלה מדגם DTSX-400 משמשים במערכת 448 האטומים לצד מאפנן ומצלמה של Hamamatsu, מחוללי צורות גל של Spectrum Instrumentation, מקור אות של Rohde & Schwarz ואובייקטיב של Special Optics בצמצם נומרי 0.65 [D][4], ו-Gooch & Housego, במאמרים על 3,000 ועל 6,100 אטומים [P][504]. הוואקום מגוון יותר (Pfeiffer; Edwards ו-Leybold, שתיהן בבעלות Atlas Copco; Agilent; Kurt J. Lesker; VACOM), אך הוא עובר תהליך של איחוד, ובדצמבר 2025 נחתם מזכר הבנות בין Universal Quantum ל-Atlas Copco [P][502]. החשיפה לפיקוח על יצוא עקיפה: תקנת BIS מ-2024-09-06 מפקחת על מחשבים קוונטיים מורכבים תחת ECCN 4A906 רק כשמספר הקיוביטים ושגיאת השער הדו-קיוביטי (C-NOT) נופלים באותו טווח — מ-34–99 קיוביטים בשגיאה ≤ 10⁻⁴ ועד כל שגיאה שהיא מ-2,000 קיוביטים ומעלה — ואף ECCN אינו נוקב במלכודות יונים, בוואקום של מערכי אטומים או באופטיקת מלקחיים [G][301]: אף סעיף קוונטי אינו מגיע לתת-המערכות, ומכונה מוגמרת נתפסת רק בתוך הטווחים האלה.

## בקרה, קריאה ועומס הקלט-פלט
הדרג הזה מטיל עומס קלט-פלט במקום לשאת אותו. Helios זקוקה לשבעה אורכי גל לפחות — המאמר שלה נוקב בשישה, מ-369 עד 1762 nm, ובריום ואיטרביום נטענים ביינון באור — לעומת 1,228 אלקטרודות מלכודת [D][97]; מערך מלקחיים אופטיים זקוק לסדר עקיפה אחד של מסיט או להולוגרמה אחת לכל אתר ממוען. ב-10³ אתרים, אופטיקת המיעון ופיצול ההספק הם כבר עלות האינטגרציה השולטת; ב-10⁴ מגבילים רוחב הפס של היגוי האלומות וההספק האופטי; ב-10⁶ הולכת אור במרחב חופשי אינה אמינה — ולכן הולכה בפוטוניקה משולבת היא המסלול שעוקבים אחריו.

## תפקיד במחסנית
היא עומדת בבסיס שש ארכיטקטורות — כהרכבה הראשית של מערכי המלקחיים האופטיים של אטומים אלקליים ואלקליים-עפרוריים ושל הסימולטור האנלוגי של אטומים ניטרליים, וכחלופית בכל שלוש ארכיטקטורות היונים הלכודים (QCCD, מלכודת פאול ליניארית עם מיעון לייזר, שערים אלקטרוניים) — ומספקת לייזרים וואקום ליונים, מלקחיים אופטיים לשתי משפחות האטומים, לייזרי שעון לאלקליים-עפרוריים ומהודים לקישור אטום–פוטון. היא אינה דורשת דבר במעלה הזרם, אינה מחליפה דבר ואינה מתנגשת בדבר: משותפת במונחים כלכליים, בלתי נראית במונחים ארכיטקטוניים. היא אינה קובעת שעון נגזר, אך תוחמת את השעון של כל ארכיטקטורה דרך זמני נעילת הלייזר, הדימות והסידור מחדש — הדימות לבדו הוא 0.5–1 ms מתוך מחזור אטומים של 1–4.5 ms. לא סומנה משבצת ריקה.

## ראיות — כיצד נמדדו המספרים
ההספק והמסה של Pasqal נושאים תג של טענת חברה, לא תג של מדידה [C][438]. ההכנסות ומספר העובדים של TOPTICA מאוששים בדף שלה עצמה [C][815]; "ספק דומיננטי" נשען על מקור משני אחד [P][322].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| TOPTICA Photonics | ספק | גרמניה | לייזרים לפלטפורמות של יונים ושל אטומים; הכנסות של EUR 140 M, 600 עובדים | [C][815] |
| AA Opto-Electronic | ספק | צרפת | מסיטי AOD מוצלבים מדגם DTSX-400 במערכת 448 האטומים | [D][4] |
| Gooch & Housego | ספק | בריטניה | מסיטים במאמרים על 3,000 ועל 6,100 אטומים | [P][504] |
| Atlas Copco (Edwards, Leybold) | ספק | שוודיה | מזכר הבנות לתיעוש מערכות ואקום גבוה | [P][502] |
| Pasqal | משתמש | צרפת | מסד Orion Gamma: 3 kW, 2,500 kg, טמפרטורת החדר | [C][438] |
| Harvard עם QuEra | משתמש | ארה״ב | טעינה מחדש במסוע, המחזיקה >3,000 אטומים >2 h | [D][144] |
| Quantinuum | משתמש | ארה״ב/בריטניה | Helios: ≥7 אורכי גל על פני 1,228 אלקטרודות | [D][97] |

**כספים.**
- 2022-11-02 · Universal Quantum · חוזה ממשלתי · EUR 67 M · DLR · נסגר [P][328]
- 2023-12-05 · Alpine Quantum Technologies · מכירת מערכת ל-Leibniz Supercomputing Centre · ≈EUR 9.8 M עבור 20 קיוביטים · נסגר [C][323]
- 2026-06 · Atom Computing · גיוס הון ועוד מכתב כוונות של CHIPS · >USD 300 M, כולל מכתב כוונות על USD 100 M · נסגר [C][154]
- 2026-08-28 · Pasqal · השלמת מיזוג SPAC · ~USD 360 M במזומן, הכנסות של EUR 16.5 M ב-2025 · נסגר [P][156]

**שוק ושרשרת אספקה.** הדרג משרת שתי משפחות פלטפורמה, יונים ואטומים, ולכן ספקיו אדישים לשאלה מי ינצח. כלכלת היחידה שונה פי 7.5 בערך בין שני הקצוות: QuNorth הזמינה מ-Atom Computing ומ-Microsoft את מערכת Magne, בת 1,225 קיוביטים פיזיים ו-50 לוגיים, תמורת EUR 80 M, ~EUR 65 k לאטום [P][12], ואילו AQT סיפקה 20 יונים לכודים תמורת EUR 9.8 M, ~EUR 0.5 M ליון [C][323]. עלות אופטיקת המלקחיים מתחלקת על פני אלפי אתרים; עלות אופטיקת היונים גדלה כמעט ביחס ישר למספר היונים. כל היעדים G1–G7 משלמים על הדרג הזה.

**קניין רוחני ותקנים.** נכון ל-2026-09-04 לא נמצאה עובדה מתוארכת על משפחת פטנטים ייחודית לקניין הרוחני של לייזרים, של ואקום או של אובייקטיבים. אף גוף תקינה אינו מכסה את הדרג הזה; התקנים לאוגני ואקום, לבטיחות לייזרים ולתושבות אופטיות קודמים למחשוב הקוונטי — הרכיבים הם סחורה, האינטגרציה אינה.

**מפות דרכים ועמידה בהבטחות.** Universal Quantum (הובטח 2022-11 · שני מחשבים ל-DLR בתוך ארבע שנים, כלומר עד 2026-11 · לא הוכרזה אספקה נכון ל-2026-09-30) [P][328] — בסיכון, אך המועד טרם עבר. Pasqal (הובטח 2024-03 · 10,000 פיזיים ב-2026 · נדחה ל-2028) [R][166]. QuEra (הובטח 2024-01 · 100 לוגיים ב-2026 · הוחלף ב-Libra ל-2028) [R][162]. צד הספקים אינו מפרסם מפת דרכים שאפשר לבדוק.

**פרשנות אסטרטגית.** לספקים כאן יש כוח מיקוח שאין לשום ספק הקשור לנושא קיוביט מסוים או למנגנון שער מסוים: הימור על TOPTICA או על Atlas Copco הוא הימור על יונים ועל אטומים גם יחד. האיום אינו מתחרה, אלא שינוי בתצורה הפיזית — אם תגיע הולכת אור בפוטוניקה משולבת, הערך יעבור למפעלי ייצור למעגלים פוטוניים משולבים (PIC), והדואופול של ה-AOD יהיה החוליה החשופה. בונים המשלבים את האופטיקה בתוך הבית משלמים בעלות תמורת שליטה; מי שמוציאים אותה למיקור חוץ משלמים בשליטה תמורת תקציב התיעוש של הספק.

## תחזית ושאלות פתוחות
ניתן להפרכה בתוך 12–24 חודשים: לאשר/להוריד בדרגה — ש-Universal Quantum ו-Atlas Copco שולחות מערכת ואקום מעבר לשלב מזכר ההבנות; שספק לייזרים שני נזכר בשמו במערכת יונים המיוצרת מסחרית; שמערך כלשהו במרחב חופשי מסדר מחדש יותר מ-~10⁴ אתרים בקצב של תיקון שגיאות. התרחיש הטוב ביותר עד 2029: הולכת אור בפוטוניקה משולבת מבטלת את הרגישות לכיוון האלומות, ועלות האופטיקה לכל אתר יורדת. התרחיש הגרוע ביותר: האספקה נשארת מרוכזת, והשגיאה הקוהרנטית של הדרג הזה נשארת איבר אי-הנאמנות השולט. פתוח: האם מישהו ידחק את TOPTICA; האם יופיע בספרות ספק אובייקטיבים נוסף על Special Optics; האם פער עלות היחידה בין יונים לאטומים יישאר.

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[12] M. Abdel-Kareem, “Denmark's QuNorth to Acquire 50-Logical-Qubit Magne Quantum Computer from Atom Computing and Microsoft,” Quantum Computing Report, Jul. 17, 2025. [Online]. Available: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft/ [P]
[97] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). [D]
[138] H. J. Manetsch, G. Nomura, E. Bataille, K. H. Leung, X. Lv, and M. Endres, “A tweezer array with 6100 highly coherent atomic qubits,” *Nature*, vol. 647, pp. 60–67, 2025, doi: [10.1038/s41586-025-09641-4](https://doi.org/10.1038/s41586-025-09641-4). [arXiv:2403.12021](https://arxiv.org/abs/2403.12021). [D]
[144] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[145] Y. Wang *et al.*, “Trapping 11,000 Atoms in a Tweezer Array Generated by a Single Metasurface,” [arXiv:2606.02715](https://arxiv.org/abs/2606.02715), Jun. 2026. [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[156] M. Swayne, “Pasqal Completes SPAC Merger With $360 Million in Cash,” The Quantum Insider, Aug. 28, 2026. [Online]. Available: https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[166] Pasqal, “Pasqal Releases 2025 Roadmap Showcasing Upgradable Platform from Today's Quantum Solutions to Tomorrow's Fault-Tolerant Systems,” Jun. 12, 2025. [Online]. Available: https://www.pasqal.com/newsroom/pasqal-releases-2025-roadmap/ [R]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[322] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Oct. 1, 2025. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[323] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[328] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]
[438] Pasqal and O. Q.-C. P. brochure, “The Power of Neutral Atom Quantum Processors by Pasqal — Unlock Quantum Computing for Real-World Solutions,” Pasqal, product brochure (PDF). [Online]. Available: https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf [C]
[502] M. Abdel-Kareem, “Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers,” Quantum Computing Report, Dec. 18, 2025. [Online]. Available: https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ [P]
[504] Gooch & Housego (G&H), “G&H Acousto-Optic Deflectors Referenced in Nature Papers Demonstrating 3,000 & 6,100 Qubit Quantum Systems,” G&H, Mar. 2026. [Online]. Available: https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers [P]
[815] TOPTICA Photonics, “About the TOPTICA Group.” [Online]. Available: https://www.toptica.com/company [C]

## פריטי אימות פתוחים
את תקרת הרענון של ~10 MHz למאפנני אור מרחביים (SLM) ולמסיטים (AOD) מעל ~10⁴ קיוביטים, המצוטטת לעתים, אי אפשר לייחס להתקן או למדידה, ולכן אין בה שימוש כאן. מעמדה של TOPTICA כ"ספק דומיננטי" נשען על מקור משני אחד [322], אף שהכנסותיה ומספר עובדיה מאושרים כעת בדף של החברה עצמה [815]. Special Optics — האובייקטיב בצמצם נומרי 0.65 של מערכת 448 האטומים — הוא ספק האובייקטיבים היחיד הנקוב בשמו בספרות שבמקורות; למערכות יונים לא נמצא ספק. רשימת ספקי ה-AOD מאומתת בדרך השלילה — רק שני ספקים מופיעים בספרות שבמקורות, ואין פירוש הדבר שקיימים רק שניים.
