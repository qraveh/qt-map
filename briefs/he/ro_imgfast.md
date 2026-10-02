---
id: ro_imgfast
name: קריאה מהירה (≤ 20 µs) של מערכי אטומים
layer: "6 קריאה"
status: emerging
since: 2026
one_line: דימות פלואורסצנציה של קיוביטים במערך אטומים בפחות מ-20 מיקרו-שניות, המחליפה חשיפות של מילישניות ומוציאה את הקריאה מהנתיב הקריטי של מחזור תיקון השגיאות באטומים ניטרליים.
verdict: דימות מהיר מוציא את הקריאה מהנתיב הקריטי, אך משאירה את ההובלה ואת קישור המצלמה, ולכן הסבב משתפר ~2×, לא 30×. להוריד בדרגה אם עד סוף 2027 אף קבוצה לא תציג קריאה של פחות מ-20 µs על מערך מלא תחת טעינה מחדש רציפה.
updated: 2026-09-03
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
דימות פלואורסצנציה תהודתית הקובע את מצבו של כל אתר בעשרות מיקרו-שניות, במקום חשיפה של 0.5–1 ms שמערכי אטומים נזקקו לה מאז ומתמיד [D][4]. שני קדם-פרסומים מאוגוסט 2026, בהפרש של שבוע זה מזה, מגדירים את המצב העדכני: העירור הקוהרנטי של Kyoto ב-¹⁷⁴Yb, 17.6 µs בהבחנה של 99.89(5)% והישרדות של 98.80(44)% [D][261], וההגנה האדפטיבית לכל אתר של USTC עם ספירת פוטונים רציפה, בדיקה של 15 µs בממוצע [D][623].
c = דימות אופטי ב-~17.6 µs (10⁻⁴·⁷⁵ s), לא הרסני, מסוגל לפעול באמצע המעגל [graph].
e = בקרה אופטית בטמפרטורת החדר; g = אופטיקה בלבד — מצלמה ואופטיקת איסוף, ללא שבב [graph].

## פיזיקה וגבולות
הרצפה היא תקציב פוטונים. ההבחנה צריכה די פוטונים מגולים כדי להפריד בהיר מחשוך מעל רעש הקריאה של המצלמה, ומספר הפוטונים המגולים הוא מספר הפוטונים המפוזרים כפול נצילות האיסוף — אובייקטיב בעל NA של 0.6 אוסף כעשירית מ-4π [D][261]. כל פוטון מפוזר נושא שני רתעים, ולכן החימום המשליך את האטום גדל עם אותו מספר פוטונים שקונה את ההבחנה: ההישרדות והנאמנות נסחרות דרך משתנה אחד. שתי התוצאות מ-2026 תוקפות לכן את המספר, לא את החשיפה — Kyoto בעירור קוהרנטי, המקטין את קצב החימום של השיטות הלא-קוהרנטיות למחצית [D][261], ו-USTC בהפסקת הפיזור בכל אתר ברגע שספירת הפוטונים הרציפה הכריעה את מצבו, ומגיעה לאי-נאמנות הבחנה של 4.1×10⁻⁵ באובדן של 2.1×10⁻⁴ [D][623]. מה שמזיז את הרצפה הוא האיסוף: NA גבוה יותר, איסוף במהוד, מערכי ספירת פוטונים במקום EMCCD, קירור במהלך הבדיקה.

## מצב ההנדסה העדכני
| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2025-11 | קריאה לא הרסנית עם 0.46% היפוך ביט, 0.24% אובדן; דימות 0.5–1 ms | Harvard University | [D][4][G:HARVARD-LOSS-QEC-2025] |
| 2026-08-17 | בדיקה של 15 µs בממוצע, אי-נאמנות 4.1×10⁻⁵, 1.7 kHz לאורך 120 סבבים | USTC | [D][623][G:USTC-FASTREADOUT-2026-08] |
| 2026-08-24 | דימות של 17.6 µs, הבחנה 99.89(5)%, הישרדות 98.80(44)% | Kyoto University | [D][261][G:KYOTO-FASTIMG-2026-08] |

האיבר השולט אינו עוד החשיפה: ב-17.6 µs הצעד האופטי הוא אחד חלקי עשרים ושישה מהשרשרת הקלאסית [C][826] וסדר גודל מתחת להובלה [D][4]. מה שנכנס לקוד הוא האובדן במהלך הבדיקה, לא ההבחנה.

## ייצור, חומרים ושרשרת האספקה
אין שבב: חיישנים, אובייקטיבים ולייזרים. שלושה ספקי מצלמות מופיעים בכל תוצאה שיש לה מקור — qCMOS של Hamamatsu בקו של Harvard/QuEra [C][G:HAMAMATSU-CAMERA-CONC-2026], EMCCD של Andor (Oxford Instruments) ב-Kyoto [D][261], Teledyne Kinetix במערכת של Quantum Machines [C][826] — ואף חברת מערכי אטומים אינה מייצרת מצלמה, ולכן החיישן הוא נקודת הכשל היחידה הברורה ביותר. החשיפה לפיקוח על יצוא אסימטרית: המכונה נלכדת ב-ECCN 4A906 (BIS, 2024-09-06) [G][301], ואילו המצלמות הן מכשירים דו-שימושיים שמחוץ לסיווגי ה-ECCN הקוונטיים של 2024.

## בקרה, קריאה ועומס הקלט-פלט
דימות מהיר מסיר איבר אחד, לא את המחזור. סבב תיקון שגיאות באטומים הוא דימות (0.5–1 ms) ועוד הובלה (מאות µs) ועוד שערים, 1–4.5 ms בסך הכול [D][4]; הורדת הדימות ל-17.6 µs משאירה את ההובלה ואת השרשרת הקלאסית, ולכן הסבב משתפר בערך פי שניים, ולא ב-30–50× שנתוני הדימות לבדם רומזים עליהם. השרשרת הקלאסית היא האיבר הגדול יותר: 442 µs של העברה מהמצלמה לשרת ועוד 21–85 µs של עיבוד, 460 µs במערך 10×10 [C][826] — פי עשרים ושישה מהחשיפה. ב-10³ אתרים קישור המצלמה הוא החוסם; ב-10⁴–10⁶ רק ספירה לכל אתר עם החלטה על החיישן ניתנת להגדלה.

## תפקיד במחסנית
זו הקריאה החלופית של ארכיטקטורת מערך המלקחיים האופטיים של רידברג באטומים אלקליים-עפרוריים (Yb/Sr). דורשת אטומים אלקליים-עפרוריים (Yb/Sr) לפי הקשת ברשומת הגרף, בהתאמה ל-¹⁷⁴Yb של Kyoto [D][261]. היא מחליפה דימות של מילישניות [graph] ונותנת סבב מהיר יותר רק עם הובלה מהירה יותר: מחזור הפלטפורמה איטי ~10³× ממוליכי-על [D][4], והדימות הוא כמחציתו. תרומה לשעון של ~18 µs קריאה, מול שעון נגזר שעדיין נקבע בידי 800 µs של הובלה (שעון נגזר = סכום סבב הסינדרום: שכבות שערים + הובלה + קריאה + איפוס עבור הארכיטקטורה) — היא מקצצת ~0.5 ms מהסבב של 1.3 ms ומשאירה את ההובלה כאיבר הגדול ביותר. משבצת ריקה סמוכה: קריאה מהירה לא הרסנית על מערך מלא תחת טעינה מחדש.

## ראיות — כיצד נמדדו המספרים
שתיהן קדם-פרסומים ממעבדה יחידה, בהפרש של שבוע זה מזה, ואף אחת מהן לא שוחזרה. 17.6 µs של Kyoto הם דימות בלבד, ללא גודל מערך בתמצית [D][261]. 15 µs של USTC הם זמן בדיקה ממוצע, והריצה של 1.7 kHz ו-120 סבבים הפעילה הגנה אדפטיבית על תת-מערך של 25 אתרים מתוך מערך של 100 קיוביטים [D][623] — לא נבדקה במקום שבו זה חשוב. התקדים הוא קוד הטורוס של Atom Computing: הדיכוי שרד 90 סבבים אך נעלם ברגע שנכללה טעינה מחדש, 0.63% לעומת 0.64% למחזור [D][148]. פעולה רציפה הוכחה בנפרד — >3,000 קיוביטים לאורך שעתיים [D][144] — מעולם לא עם קריאה של מיקרו-שניות.

## שחקנים וכלכלה
**מי.**
| ארגון | תפקיד | מדינה | מה הם עושים | ראיות |
|---|---|---|---|---|
| Kyoto University | מחקר | יפן | הדימות הראשון של מערך אטומים ב-≤20 µs, על ¹⁷⁴Yb | [D][261] |
| USTC | מחקר | סין | בדיקה אדפטיבית של 15 µs עם פענוח בהזנה קדימה של פחות מ-µs | [D][623] |
| Quantum Machines | ספק | ישראל | מוכרת את שרשרת הקריאה הקלאסית | [C][826] |
| Hamamatsu Photonics | ספק | יפן | חיישן ה-qCMOS של קו הדימות העיקרי | [C][G:HAMAMATSU-CAMERA-CONC-2026] |

**כספים.** 2025-02-25 · Quantum Machines · סבב C · $170 M · נסגר [C][528][G:QM-SERIESC-2025-02]. 2025-11-06 · DARPA QBI, שלב B · תוכנית · עד $15 M לכל צוות · Atom Computing ו-QuEra בין אחד-עשר [G][65]. 2026-06-16 · Atom Computing · סבב C ועוד מכתב כוונות לא מחייב של CHIPS על $100 M מ-2026-05-21 · $100 M מ-Third Point, >$300 M בסך הכול · נסגר ומכתב כוונות [C][154][G][300]. דבר אינו ממומן כקריאה מהירה: זו הוצאה על מכשור בתוך תקציבי הפלטפורמות, ושתי התוצאות המגדירות הגיעו מאוניברסיטאות, לא מהחברות הזקוקות להן.

**שוק ושרשרת אספקה.** הספקים המאפשרים הם ספקי המצלמות (Hamamatsu, Andor, Teledyne) וספקי הבקרה (Quantum Machines); אין מוצר של קריאה מהירה לאטומים. ריכוזיות החיישנים חמורה: שלושה ספקים, ואף אחד מהם אינו ניתן להחלפה בייצור עצמי. הערך שאפשר ללכוד יושב בשרשרת הקלאסית, ולכן ספק הבקרה הוא שמפרסם את מדדי הביצועים [C][826]. משלם ל-G3 ול-G4, ול-G1 במקום שבו קצב הריצות הוא התפוקה.

**קניין רוחני ותקנים.** אף משפחת פטנטים מתוארכת לקריאה מהירה של מערכי אטומים לא צצה נכון ל-4 בספטמבר 2026; שתי התוצאות הן קדם-פרסומים, והחברה היחידה ברשימת המחברים של אחת מהן היא Yaqumo Inc. [D][261]. אין גוף תקינה השולט בבחירת החיישן. היעדר הקניין הרוחני הוא ממצא בפני עצמו: הטכניקה מפורסמת, לא מגודרת.

**מפות דרכים ועמידה בהבטחות.** Atom Computing עם Microsoft (2025-07 · Magne, 50 לוגיים, €80 M, מפנה 2026/27 · בהתקנה) [R][11]. QuEra (2026-06 · Libra 2028, >256 לוגיים · מפת הדרכים שלה מ-2024 הבטיחה 100 לוגיים ב-2026 — דחייה של שנתיים) [R][162]. איש לא נקב בתאריך להתחייבות לספק קריאה של פחות מ-20 µs; הרשומה של הענף היא דחייה של ~2 שנים.

**פרשנות אסטרטגית.** המנצחת היא חברת האטומים שתוציא את המצלמה מהלולאה, לא זו שתקצר את החשיפה ביותר: צוואר הבקבוק שנמדד הוא העברת פריים של 442 µs, לא בדיקה של 17.6 µs [C][826]. ספקי המצלמות מחזיקים כיום בכוח של ספקים ומאבדים אותו ברגע שיגיע גילוי משולב. הקריאה ברמת הפלטפורמה מפוכחת יותר — סגירת איבר הדימות מזיזה את חיסרון המחזור של האטומים מ-~10³× לאולי ~10²×, וזה אינו מכריע את הוויכוח על הארכיטקטורה [D][4].

## תחזית ושאלות פתוחות
לאשר/להוריד בדרגה בתוך 12–24 חודשים: אחת משתי התוצאות משוחזרת בידי קבוצה שנייה; קריאה של פחות מ-20 µs בתוך ריצה חיה של קיוביט לוגי; קריאה הנשמרת תחת טעינה מחדש בגודל מערך מלא. התרחיש הטוב ביותר ל-2029: דימות של מיקרו-שניות הוא הסטנדרט, הסבב מוגבל בידי ההובלה בכמה מאות µs, וגילוי האובדן זול דיו כדי להפוך את ההמרה למחיקה לשגרה. התרחיש הגרוע ביותר: המספרים מחזיקים רק בתת-מערכים קטנים וסטטיים. שאלות פתוחות: באיזה מין השתמשה USTC; האם עצירה אדפטיבית שורדת על מערך מלא, שבו הספירה רצה בכל מקום בבת אחת; מי יבנה את החיישן הראשון עם ההחלטה על הפיסה.

## מקורות
[4] D. Bluvstein *et al.*, “A fault-tolerant neutral-atom architecture for universal quantum computation,” *Nature*, vol. 649, no. 8095, pp. 39–46, Nov. 2025, doi: [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [arXiv:2506.20661](https://arxiv.org/abs/2506.20661). [D]
[11] Novo Nordisk Foundation, “New quantum computer with great potential to boost Nordic research and innovation,” Novo Nordisk Fonden, Jul. 17, 2025. [Online]. Available: https://novonordiskfonden.dk/en/news/new-quantum-computer-with-great-potential-to-boost-nordic-research-and-innovation/ [R]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[144] N.-C. Chiu *et al.*, “Continuous operation of a coherent 3,000-qubit system,” *Nature*, vol. 646, no. 8087, pp. 1075–1080, Sep. 2025, doi: [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [D]
[148] Atom Computing and Collaborators, “Quantum error correction with the toric code,” [arXiv:2606.04079](https://arxiv.org/abs/2606.04079), Jun. 2026. [D]
[154] Atom Computing, “Atom Computing Raises More Than $300 Million to Accelerate Deployment of Fault-Tolerant, Neutral-Atom Quantum Computers,” PR Newswire, Jun. 16, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html [C]
[162] QuEra Computing, “QuEra Announces 2028 Fault-Tolerant Quantum Computer and Expanded Multi-Year Strategic Collaboration with AWS,” Jun. 15, 2026. [Online]. Available: https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws [R]
[261] R. Yokoyama *et al.*, “Minimally Destructive Fast Imaging of Single Atoms in an Optical Tweezer Array with Coherent Excitation,” [arXiv:2605.24175](https://arxiv.org/abs/2605.24175), Jun. 2026. Also https://arxiv.org/abs/2605.24175. [D]
[300] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[528] Quantum Machines, “Quantum Machines Raises $170M as Its Customer Base Exceeds 50% of Companies Developing Quantum Computers,” Feb. 25, 2025. [Online]. Available: https://www.quantum-machines.co/press-release/quantum-machines-raises-170-million-in-series-c-funding/ [C]
[623] Xu-Zhao-Qiu Zeng *et al.*, “Fast Nondestructive Readout for High-Clock-Rate Atom Array Quantum Processor,” [arXiv:2608.17189](https://arxiv.org/abs/2608.17189), Aug. 2026. [D]
[826] U. Akhouri, “Classically Accelerated Readout for Neutral Atoms with CPU/GPU Integration,” Quantum Machines Blog, Jun. 2026. [Online]. Available: https://www.quantum-machines.co/resources/blog/classically-accelerated-readout-neutral-atoms-cpu-gpu-readout/ [C]

## פריטי אימות פתוחים
המין האטומי והמעבר של USTC אינם מצוינים בתמצית הנגישה של arXiv:2608.17189, וכך גם סוג הגלאי ו-NA האיסוף; הנתון 1.7 kHz / 120 סבבים חל על תת-מערך של 25 אתרים מתוך המערך של 100 הקיוביטים [623].
גודל המערך של Kyoto אינו מצוין בתמצית הנגישה; 17.6 µs הם זמן הדימות בלבד, לא מחזור קריאה מלא [261].
לאף אחת משתי תוצאות הקריאה המהירה אין שחזור של צד שלישי, ואף אחת מהן לא הורצה תחת טעינה מחדש רציפה של אטומים נכון ל-4 בספטמבר 2026.
הטענה שמצלמות מדעיות נמצאות מחוץ לסיווגי ה-ECCN הקוונטיים של 2024 נשענת על תחולתם של סיווגים אלה עצמם [301]; קטגוריית הפיקוח הייחודית למצלמות לא אומתה.
נתון השרשרת של 460 µs של Quantum Machines דווח על ידה ולא עבר ביקורת בלתי תלויה [826].
