---
id: ct_rt
name: אלקטרוניקה בטמפרטורת החדר + כבל קואקסיאלי/כבל גמיש לכל קיוביט
layer: "5 בקרה"
status: demonstrated
since: 2007
one_line: קו קוהרנטי אחד לכל מבוא של הנעה, שטף וקריאה עובר ממסדים בטמפרטורת החדר, דרך כבל קואקסיאלי מונחת או כבל סרט גמיש (flex), אל תא הערבוב.
verdict: מספר הקווים והחום בתא הערבוב, ולא הפיזיקה של השערים, מגבילים את מספר הקיוביטים למקרר; ניתן להפרכה אם מקרר אחד יפעיל >2,000 קיוביטים בקווים מטמפרטורת החדר.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
ארכיטקטורת הבקרה השלטת כמעט בכל קיוביט מוליך-על במודל השערים: הנעת המיקרוגל, ממתח השטף ואותות הקריאה מסונתזים בטמפרטורת החדר, יורדים לאורך מקרר הדילול בכבל קואקסיאלי או בכבל סרט גמיש, מונחתים בכל שלב ומגיעים לשבב ב-10–20 mK. כל דרגת חופש של בקרה היא מוליך החוצה מפל של 300 K → 10 mK — בעיה תרמית ומכנית, לא קוונטית. בשימוש מאז מערכות הטרנסמון הראשונות (2007). תכונות: e = בקרת מיקרוגל הממוקמת כולה בטמפרטורת החדר, ללא הגברה קריוגנית וללא פירוק ריבוב; f = שגיאה קוהרנטית כפי שהקוד רואה אותה — הפרעה הדדית, רעש פאזה, סחיפת משרעת.

## פיזיקה וגבולות
האילוץ המחייב הוא תקציב הקירור, לא הקוהרנטיות. כל קו נושא עומס הולכה סביל ועוד עומס פעיל מה-~60 dB של הנחתה, המורידים את רעש ג'ונסון של 300 K אל רצפת הפוטונים של 10 mK, ורובו נפרק ב-4 K ובשלב הזיקוק (still). הספק הקירור של כל שלב קבוע — Bluefors XLD400 נותן כ-1 W ב-4 K ומיקרוואטים בתא הערבוב — ולכן הקווים גדלים כ-O(N) מול קבוע. התקציב שמדדו Krinner ועמיתיו תומך ב-50 קיוביטים ב-14 mK במקרר הזה, ולכל היותר בכ-150 [D][522]; כל רווח מאז הוא כבל דק יותר וזיווד צפוף יותר, לא פיזיקה חדשה. הכשל קוהרנטי — הפרעה הדדית וסחיפת פאזה מופיעות כשגיאת בקרה, ולכן המכונות האלה מתדרדרות בכך שהן נזקקות לכיול מחדש, ולא בדה-קוהרנטיות. מה שמזיז את הרצפה: ריבוב של כמה קיוביטים על כל מוליך, או העברת הסינתזה אל תוך המקרר.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2019 | 50 קיוביטים ל-XLD400, נמדד; ~150 כחסם עליון תרמי | ETH Zürich | [D][522] |
| 2023-12 | 1,121 קיוביטים במקרר אחד (Condor), הגדול ביותר שחווט אי-פעם בדרך זו | IBM | [C][292] |
| 2025-11-10 | 8 ערוצים לכבל גמיש, +50% לכל מבוא, 1,536 קווים ל-XLDsl | Delft Circuits | [C][523] |
| 2026-06-16 | KIDE במפרט של >4,000 קווי RF, >1,000 קיוביטים | Bluefors | [C][303] |

החיווט קובע את ה-N שבו כדאי לתקן שגיאות, לא את הרצפה: האיבר השולט עדיין הוא אי-הנאמנות הדו-קיוביטית — Willow, 105 קיוביטים בנאמנות דו-קיוביטית ממוצעת של 99.88%, מחזור של 1.1 µs [D][1].

## ייצור, חומרים ושרשרת האספקה
שיעור התקינות כאן מכני (מחברים לכל מבוא, היפרדות שכבות בכבלים הגמישים, עיגון תרמי) ותרמי, לא ליתוגרפי; המסדים הם כמעט מוצרי מדף (COTS). החיווט הקריוגני הוא השכבה הדקה — Delft Circuits היא ספקית הכבלים הגמישים העצמאית המובילה, ומוצריה מסופקים בתוך מערכות Bluefors [C][523]. המקררים מרכזים את הסיכון: Bluefors בלעה ב-2023 את צינורות הפולס ומתקני ההליום של Cryomech, והכניסה אל תוך הבית את השלב שמתחת ליחידת הדילול, בהכנסות משותפות של מעל EUR 160 M [C][524]; Oxford Instruments היא החלופה המסחרית היחידה בהיקף דומה, ו-ULVAC היא מקור שלישי, יפני, מאז 2025 [C][525]. הפיקוח על יצוא חותך באופן לא סימטרי: מקררים מעל סף ה-BIS (≥600 µW ב-0.1 K, 48 h) נופלים תחת ECCN 3A904, ו-3A901.a מפקח על CMOS שתוכנן לפעול ב-≤4.5 K — וכך לוכד את החלופה של CMOS קריוגני — בעוד שהמסדים בטמפרטורת החדר אינם מפוקחים [G][301].

## בקרה, קריאה ועומס הקלט-פלט
שניים עד ארבעה קווים לקיוביט: הנעה, שטף וקווי הזנה לקריאה, שכל אחד מהם מרבב 5–10 קיוביטים. ב-10³ הארכיטקטורה עובדת וממלאת את רוב המקרר הגדול; KIDE מוגדר במפרט עם >4,000 קווים עבור >1,000 קיוביטים, כארבעה לכל קיוביט [C][303]. ב-10⁴ מפת הדרכים של הכבלים הגמישים (40,000+ קווים עד 2029) היא הקרנה ללא הדגמת ביניים [R][523], ועומק הריבוב, ולא מספר הכבלים, הופך למגבלה. ב-10⁶ אין מסלול מטמפרטורת החדר; כל מפת דרכים מעבר ל-~10⁴ מניחה בקרה בתוך המקרר או חלוקה בין כמה מקררים. המסלול הלוך-ושוב לטמפרטורת החדר מוסיף גם השהיית כבל ועיבוד במסד בסקאלה של µs [C][526], מול מחזור של 1.1 µs ב-Willow [D][1].

## תפקיד במחסנית
משרתת את ארכיטקטורות הטרנסמונים, הקיוביטים הבוזוניים (חתול/GKP) והמחיקה במסילה כפולה — את כל העץ של מוליכי-העל — ואינה דורשת שום טכנולוגיה מקדימה, וזה כוחה המסחרי. היא גם הבקרה החלופית בארכיטקטורות הספינים בנקודות קוונטיות בצורן / גרמניום, ספיני התורמים בצורן והספינים במרכזי צבע. כל אחד מתחליפיה (CMOS קריוגני ב-4 K, SFQ בטמפרטורת מיליקלווין, DAC-שטף על השבב) גובה נטל חדש של הסמכה קריוגנית, ואף אחד מהם לא דחק אותה בקנה מידה: מודול ה-SFQ של SEEQC בטמפרטורת מיליקלווין מגיע לנאמנות חד-קיוביטית מעל 99% ועד 99.9% על חמישה קיוביטים [D][304]; הבקר של HRL ב-4 K מפעיל 18 קיוביטי ספין בצורן עם Λ₅/₃ = 4.7 [D][190]; IBM מדווחת על רכיבי ASIC לשטף ב-CMOS קריוגני בשוויון עם אלקטרוניקה בטמפרטורת החדר על Heron R2 בן 156 קיוביטים, אך רק בתמציות של כנס [C][527]. החיווט מטמפרטורת החדר אינו מוסיף זמן שער או קריאה, ולכן הסבב הנגזר נשאר 0.65 µs, בתוך מחזור תיקון השגיאות הנמדד של 1.1 µs [D][1]. משבצת ריקה שכנה: שכבת בקרה קריוגנית מרובבת שהוכחה בקנה מידה של מערך.

## ראיות — כיצד נמדדו המספרים
כל מספר קווים מעל 1,536 לקוח מספרות מוצר, לא ממערכת מחווטת: לנתון >4,000 של Bluefors ולנתון 40,000 עד 2029 של Delft Circuits אין התקנה נקובה בשמה, ואף אחת מהן אינה מפרסמת נתוני הפרעה הדדית או יציבות פאזה במספר ערוצים גבוה. נכון ל-4 בספטמבר 2026 אין מדידה בלתי תלויה של הפרעה הדדית מצטברת מעל ~1,000 קווים בו-זמניים — וזה הפער שחשוב, שכן ההפרעה ההדדית היא הדרך שבה הארכיטקטורה הזו נכשלת.

הקיוביט עצמו יכול למדוד את הרעש של שרשרת הבקרה. בקו טרנסמון אחד ב-Jülich עם הנחתה של 56 dB, קצב העירור במודל נשלט בידי רעש קלאסי ממכשיר ההנעה שבטמפרטורת החדר (−146 dBm/Hz מעל 4.6 GHz) ומשלב המנחת ב-1 K, ואילו הרלקסציה נקבעה בידי רעש קוונטי; ספקטרום העירור של הקיוביט שימש ספקטרומטר של אותו רעש בתוך המערך עצמו [P][890]. התוצאה מתארת מערך אחד, לא כל קו.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה בדיוק הם עושים בטכנולוגיה זו | ראיות |
|---|---|---|---|---|
| Bluefors | ספק | פינלנד | מקררים עם רתמות חיווט משולבות; KIDE עם >4,000 קווים | [C][303] |
| Delft Circuits | ספק | הולנד | כבל סרט Cri/oFlex, 8 ערוצים לכבל גמיש, בתוך Bluefors XLDsl | [C][523] |
| Quantum Machines | ספק | ישראל | מסדי בקרה OPX ותוכנת בקר | [C][528] |
| Zurich Instruments | ספק | שווייץ | מסדי ZQCS במערכת 256 הקיוביטים של Fujitsu/RIKEN | [C][526] |
| Qblox | ספק | הולנד | ערכות בקרה מודולריות, ברמת מחיר נמוכה יותר | [C][529] |
| IBM | מפתח | ארה״ב | Condor, 1,121 קיוביטים במקרר אחד; מאתגרת מכיוון ה-CMOS הקריוגני | [C][292] |
| SEEQC | מפתח | ארה״ב | בקרת SFQ בטמפרטורת מיליקלווין, חלופה בתוך המקרר | [D][304] |

**כספים.**
2023-03-28 · Bluefors · מיזוג ורכישה, Cryomech · לא פורסם, הכנסות משותפות > EUR 160 M · נסגר [C][524]
2024-06-20 · Qblox · סבב A · USD 26 M · Quantonation, Invest-NL Deep Tech · נסגר [C][529]
2025-02-25 · Quantum Machines · סבב C · USD 170 M · בהובלת PSG Equity · USD 280 M במצטבר · נסגר [C][528]
2025-12-03 · Delft Circuits · הרחבת סבב A · EUR 8 M · DeepTech XL, HTGF, QuVest · EUR 15 M במצטבר · נסגר [P][530]
2026-06-17 · Quantum Machines · מיזוג ורכישה, PCB Engineering (הונגריה) · לא פורסם · נסגר [C][528]

**שוק ושרשרת אספקה.** שוק המסדים תחרותי והופך לסחורה: חמישה ספקים הוסמכו ל-NVQLink [C][531], Quantum Machines היא בעלת ההון הרב ביותר, עם USD 280 M במצטבר [C][528], ו-Qblox קטנה ממנה בסדר גודל [C][529]. המקררים והחיווט שלהם מרוכזים, ו-Delft Circuits, עם EUR 15 M במצטבר [P][530], היא ספקית הכבלים הגמישים העצמאית המשמעותית היחידה — נקודת כשל יחידה. משלמים עליה G2, G3 ו-G7; לא G4.

**קניין רוחני ותקנים.** לא נמצאה במאגר נתונים מזוהה ספירה מתוארכת של משפחות פטנטים לכבילת RF קריוגנית או לבקרה בטמפרטורת החדר — לא נמצאה עובדה מתוארכת. אין תקן רשמי; הקרוב ביותר הוא NVQLink, המגדיר מאז 2025-10-28 ממשק משותף בצד ה-GPU לחמישה ספקי בקרה [C][531], בעוד שתוכנת הפולסים של כל ספק נשארת קניינית.

**מפות דרכים ועמידה בהבטחות.** Delft Circuits (2025-11-10, ל-2029): 40,000+ קווים למקרר, ללא אבן דרך ביניים [R][523]. Bluefors (2026-06-16, ללא תאריך יעד): KIDE עם >4,000 קווים, דף מוצר בלבד [C][303]. Zurich Instruments (2026-03-09, ללא תאריך יעד): "כמה אלפי קיוביטים" [C][526]. שני ספקי הכבלים סיפקו כל מדרגת צפיפות שהכריזו עליה; ואף על פי כן, 2029 היא הקרנה בקו ישר.

**פרשנות אסטרטגית.** אם החיווט מטמפרטורת החדר יגיע ל-10⁴ קיוביטים, ספקי המסדים ו-Bluefors ישמרו על תקציב הבקרה, ובקרת CMOS קריוגני או SFQ תישאר תוכנית מחקר. אם הצפיפות תיעצר סביב 4,000–5,000 קווים, כוח המיקוח יעבור אל תוך המקרר, שם לאף ספק של אלקטרוניקה לטמפרטורת החדר אין קניין רוחני — והתוצאות החזקות ביותר של CMOS קריוגני נמצאות בידי IBM ו-HRL, חברה אחת מאז 2026-08-26 [G:IBM-HRL-CLOSED-2026-08]. הפיקוח על יצוא מיטיב עם הטכנולוגיה השלטת [G][301].

## תחזית ושאלות פתוחות
לאשר עד סוף 2027 אם מקרר אחד יפעיל >2,000 קיוביטים בקווים מטמפרטורת החדר, עם נאמנות שפורסמה בצפיפות הזו; להוריד בדרגה אחרי שנה נוספת של מפרטי מספר קווים ללא מערכת מחווטת. התרחיש הטוב ביותר עד 2029: צפיפות הכבלים הגמישים יחד עם ריבוב עמוק יותר מגיעות ל-10⁴ קיוביטים, והמחסנית אינה משתנה. התרחיש הגרוע ביותר: הצפיפות נעצרת סביב 4,000–5,000 קווים, בעוד שמפות הדרכים שמעבר לכך מניחות CMOS קריוגני או SFQ שלא סופקו. שאלות פתוחות: האם ההפרעה ההדדית גדלה מהר יותר מליניארית מעבר ל-~1,000 קווים; האם צפיפות הכבלים הגמישים והריבוב מצטברים זה על זה או נתקלים בחומות בלתי תלויות; האם ספק כלשהו יתחייב לבקרה בתוך המקרר לפני שהחיווט מטמפרטורת החדר ייכשל באופן גלוי; האם חלוקה בין כמה מקררים הופכת את התקרה של מקרר יחיד ללא רלוונטית.

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[292] J. Gambetta, “The hardware and software for the era of quantum utility is here,” IBM Quantum Computing Blog, Dec. 4, 2023. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-roadmap-2033 [C]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[303] Bluefors, “KIDE Cryogenic Platform — For Large-Scale Quantum Computing,” Jun. 16, 2026. [Online]. Available: https://bluefors.com/products/kide-cryogenic-platform/ [C]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[522] S. Krinner *et al.*, “Engineering cryogenic setups for 100-qubit scale superconducting circuit systems,” *EPJ Quantum Technology*, vol. 6, no. 1, Art. no. 2, Dec. 2019, doi: [10.1140/epjqt/s40507-019-0072-0](https://doi.org/10.1140/epjqt/s40507-019-0072-0). [arXiv:1806.07862](https://arxiv.org/abs/1806.07862). [D]
[523] Physics World (IOP Publishing), “Delft Circuits, Bluefors: the engine-room driving joined-up quantum innovation,” Nov. 10, 2025. [Online]. Available: https://physicsworld.com/a/delft-circuits-bluefors-the-engine-room-driving-joined-up-quantum-innovation/ [C]
[524] Bluefors, “Bluefors closes the acquisition of Cryomech,” Mar. 28, 2023. [Online]. Available: https://bluefors.com/press-releases/bluefors-closes-the-acquisition-of-cryomech/ [C]
[525] ULVAC, “ULVAC Developing Next-Generation Dilution Refrigerator for Quantum Computing by 2026,” Nasdaq (JCN Newswire), Mar. 20, 2025. [Online]. Available: https://www.nasdaq.com/press-release/ulvac-developing-next-generation-dilution-refrigerator-quantum-computing-2026-2025-03 [C]
[526] Zurich Instruments, “Zurich Instruments Launches the ZQCS Quantum Control System to Master the Long-Lived Logical Qubit Challenge,” Mar. 9, 2026. [Online]. Available: https://www.zhinst.com/americas/en/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/ [C]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[528] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[529] E. Flipse, “Qblox secures series A funding to accelerate quantum control stack development,” Qblox Newsroom, Jun. 20, 2024. [Online]. Available: https://qblox.com/newsroom/qblox-secures-series-a-funding-quantum-control-stack-development [C]
[530] M. U. Rehman, “Delft Circuits Names Martin Danoesastro CEO and Extends Funding Round,” The Quantum Insider, Dec. 3, 2025. [Online]. Available: https://thequantuminsider.com/2025/12/03/delft-circuits-new-ceo-financing/ [P]
[531] NVIDIA, “NVIDIA Introduces NVQLink — Connecting Quantum and GPU Computing for 17 Quantum Builders and Nine Scientific Labs,” Oct. 28, 2025. [Online]. Available: https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing [C]
[890] J. R. Guimarães *et al.*, “Quantum environment afterglow from broadband excitation spectroscopy in superconducting qubits,” [arXiv:2609.31280](https://arxiv.org/abs/2609.31280), Sep. 2026. [P]

## פריטי אימות פתוחים
אף ספק אינו מפרסם עלות לקו או לרתמת חיווט; אין כלכלת יחידה לחיווט קריוגני שניתן לצטט. אין תקציב חום נמדד או נתוני הפרעה הדדית לרתמת כבלים גמישים של >1,000 קווים — הנתונים של Bluefors (>4,000 קווים) ושל Delft Circuits (40,000 עד 2029) אינם מאומתים ברמת המערכת. ההכנסות ומספרי הלקוחות של Delft Circuits ושל Zurich Instruments לא פורסמו. תוצאת השוויון של IBM לממתח שטף ב-CMOS קריוגני קיימת רק כתמציות של כנס APS, ללא קדם-פרסום או מאמר נכון ל-2026-09-04. לא נמצאה קביעת ECCN מתוארכת ספציפית למסדי בקרה בטמפרטורת החדר; היותם לא מפוקחים נקראת מתוך היעדרה של רשומה תואמת בתקנה של 2024, לא מתוך הצהרה מפורשת של BIS.
