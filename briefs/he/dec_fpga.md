---
id: dec_fpga
name: מפענחי FPGA בזמן אמת (LCD, Deltaflow)
layer: "8 מפענח"
status: demonstrated
since: 2025
one_line: רכיבי FPGA בטמפרטורת החדר, המריצים מפענחי אשכול או זיווג מהר דיים כדי לעבד את סינדרומי קוד המשטח בתוך מחזור תיקון השגיאות, ומקדימים את החלופות של GPU ושל אלקטרוניקה קריוגנית.
verdict: תפוקה של פחות מ-1 µs לסבב פורסמה עד d=17, אך פענוח של סינדרומים חיים של קוד המשטח מתועד רק עד d=5, ותיקון בלולאה סגורה עד d=3; פער הדיוק מול מפענחים מבוססי רשתות עצביות ממשי.
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא
חומרה קלאסית הצורכת ביטי סינדרום ופולטת תיקונים בתוך מחזור הקוד. המוצא הוא טיעון הפיגור: אם זמן הפענוח הממוצע עולה על זמן המחזור, סבבים שלא פוענחו מצטברים ללא גבול, והחומרה הקלאסית היא שקובעת את שיעור השגיאות הלוגיות. רכיבי FPGA ניצחו בזכות השהיה דטרמיניסטית, לא בזכות מהירות.
תכונות: מודול חישוב, לא נושא קיוביט (זיקה לנושא 0.5); אין לו זמן אופייני, קריאה, ניידות, בקרה או ייצור משלו.
מבנה השגיאה שהוא צורך: סינדרומי פאולי מקוד המשטח המסובב.

## פיזיקה וגבולות
התפוקה חייבת לעבד סבב אחד בכל מחזור — 1.1 µs בחומרה ברמת Willow [D][1] — ומפענח האשכול של Riverlane עומד בכך עד d=17 [D][238]. השהיית התגובה מתנה כל שער שאינו קליפורד, ורק לולאה סגורה מודדת אותה: הלולאה מ-Shenzhen נסגרה ב-550 ns ב-d=3, בתוך מחזור של 1.25 µs [D][729]. ההשהיה הנמוכה נקנית במחיר של דיוק: הסף של ה-LCD עומד על 0.55%, לעומת 0.7% ל-MWPM בתוכנה [D][238], ועל סינדרומים זהים של Willow נתן הזיווג Λ = 2.04, ואילו מפענח מבוסס רשת עצבית נתן 2.14 [D][1]. השטח הוא החומה האחרת: ה-LCD ב-d=17 תופס ~6% מטבלאות החיפוש הלוגיות (LUT) של Xilinx VU19P לכל קיוביט לוגי [D][238] — ~16 קיוביטים לוגיים כאלה לרכיב מהקצה העליון.

## מצב ההנדסה העדכני

| תאריך | נתון | מי | תג |
|---|---|---|---|
| 2025-02-20 | MWPM מדויק ב-0.8 µs בממוצע, d=13, p=0.1%, 62 MHz | Yale (Micro Blossom) | [D][727] |
| 2025-12-17 | אשכול בפחות מ-1 µs לסבב עד d=17 על FPGA אחד | Riverlane | [D][238] |
| 2026-05-06 | פענוח מבוסס רשת עצבית ראשון ב-FPGA בלולאה סגורה על מעבד חי, 550 ns ב-d=3 | IQA Shenzhen | [D][729] |

עבור קוד ה-gross, Relay-BP של IBM מדווח על איטרציה של 24 ns ועל פחות מ-1 µs למחזור מתחת ל-p = 3×10⁻³, מסינדרומים מדומים [S][48].

## ייצור, חומרים ושרשרת האספקה
אין ייצור: כרטיס FPGA מסחרי במסד שבטמפרטורת החדר. כל מפענח בזמן אמת שפורסם רץ על צורן של AMD/Xilinx (VU19P עבור ה-LCD [D][238], VMK180 עבור Micro Blossom [D][727]); החלופה המסחרית היחידה החליפה ידיים כאשר מכירת 51% מ-Altera על ידי Intel ל-Silver Lake לפי שווי של $8.75 B, שהוכרזה באפריל 2025, נסגרה ב-2025-09-15 [G][735] — דואופול שצד אחד שלו נתון לשליטת קרן הון פרטי. רכיבי FPGA מהקצה העליון נמצאים בתחום הפיקוח האמריקאי על יצוא. עומס הקלט-פלט הוא צינור הסינדרום: זניח ב-10³ קיוביטים, אך ב-10⁴–10⁶ הקצב מחייב פענוח מקדים ב-4 K או כרטיסים מקביליים רבים.

## תפקיד במחסנית
מפענח חלופי בסריג הטרנסמונים עם מצמדים ברי-כוונון. הוא דורש את קוד המשטח המסובב ומספק את זרם התיקונים שהסבילות לתקלות זקוקה לו; הוא מחליף פענוח ב-GPU, שהשהיית הזנב שלו אינה דטרמיניסטית — 3.84 µs בממוצע ו-3.96 µs במקסימום רק כדי לחצות את NVQLink [C][324]. תרומתו לשעון הנגזר היא רצפה, לא איבר בסכום: עליו להישאר מתחת למחזור של 1.1 µs, והוא אכן נשאר. אימות: אלה נתונים של המפענח לבדו, על סינדרומים מוקלטים המוזנים מחדש או על סינדרומים מדומים; רק שתי לולאות חיות — זו של d=3, ומפענח האשכול שבתוך הלולאה על Rigetti Ankaa-2, המכונה היחידה במרשם שבה הוא פועל; ה-367 ns המצוטט של Micro Blossom הוא נתון ממאגר הקוד שאינו מופיע בשום מאמר, והמספר שפורסם הוא 0.8 µs [D][727].

## שחקנים וכלכלה
**מי.**

| ארגון | תפקיד | מדינה | מה בדיוק הם עושים | ראיות |
|---|---|---|---|---|
| Riverlane | ספק | בריטניה | LCD ו-Deltaflow, מחסנית תיקון השגיאות המסחרית היחידה | [D][238] |
| AMD | ספק | ארה״ב | צורן ה-FPGA שמתחת לכל מפענח שפורסם | [D][238] |
| Google | משתמש | ארה״ב | קו בסיס של 63 µs ב-d=5 [D][1], ואחריו פענוח מבוסס רשת עצבית ב-d=7 | [D][2] |
| IQA Shenzhen | מחקר | סין | פענוח מבוסס רשת עצבית ראשון ב-FPGA בלולאה סגורה על מעבד חי | [D][729] |

**כספים.**
2024-08-06 · Riverlane · סבב C · $75 M · Planet First Partners מובילה · נסגר [C][661][G:RIVERLANE-FUNDING]
2025-09-15 · Intel/Altera · מכירת 51% · שווי פעילות (EV) של $8.75 B · Silver Lake · נסגר (הוכרז ב-2025-04-14) [G][735][G:ALTERA-SILVERLAKE-2025]

**שוק ושרשרת אספקה.** ספק מסחרי אחד של מפענחים, ספק FPGA דומיננטי אחד, ו-NVIDIA הדוחפת את NVQLink כחלופה — נקודת קצה פתוחה, מאיץ ממקור יחיד [C][324]. המחסנית של Riverlane מסופקת כשהיא משולבת בחומרת הבקרה של Qblox [C][659]. הטכנולוגיה תורמת ל-G3 ול-G4 בלבד.

**קניין רוחני ותקנים.** הפטנט של Riverlane, GB 2641501 A, "Quantum decoder" (פורסם 2025-12-10), תובע רכיבי עיבוד מקובצים המריצים אשכול על היפר-גרף הפענוח — ארכיטקטורת ה-LCD עצמה [G][662]. אין תקן למפענחים.

**מפות דרכים ועמידה בהבטחות.** Riverlane (2026-03-12 · megaquop (10⁶ פעולות ללא שגיאה) לפני 2030, teraquop (10¹²) מ-2033 · ה-LCD פורסם בזמן [C][658]). IBM (2025-10 · פענוח קוד gross ב-FPGA · עדיין סימולציה נכון ל-2026-09-04 [S][48]).

**פרשנות אסטרטגית.** מי שמחזיק במפענח יושב בין כל QPU מוליך-על לבין הסבילות לתקלות — אבל השכבה דקה דיה כדי שספקי ה-QPU יבנו אותה בעצמם, כפי שעשו IBM ו-Google. AMD מנצחת בכל מקרה; האיום הוא ש-NVQLink יהפוך את הממשק לסחורה.

## תחזית ושאלות פתוחות
לאשר עד סוף 2027: מפענח FPGA הסוגר את הלולאה על סינדרומים חיים ב-d ≥ 7 — פענוח חי ב-d = 7 אינו מתועד לשום מפענח, כולל תוצאת הרשת העצבית של Google ב-d = 7 [D][2] — או Relay-BP על חומרת קוד gross אמיתית; להוריד בדרגה אם אף אחד מהם לא יתרחש. התרחיש הטוב ביותר ל-2029: ממשק בר-העברה עם צורן ממקור שני; התרחיש הגרוע ביותר: מפענחים ייחודיים לכל ספק, שאיש אינו יכול להשוות ביניהם. האם השהיית התגובה או התפוקה תגביל ראשונה ב-d=17? האם ספקי המפענחים ישרדו כשספקי ה-QPU בונים מפענחים בעצמם? האם הפיקוח על יצוא יגיע לרכיבי FPGA?

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[48] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[238] A. B. Ziad *et al.*, “Local clustering decoder as a fast and adaptive hardware decoder for the surface code,” *Nat. Commun.*, vol. 16, no. 1, Art. no. 11048, Dec. 2025, doi: [10.1038/s41467-025-66773-x](https://doi.org/10.1038/s41467-025-66773-x). [D]
[324] S. Caldwell *et al.*, “NVIDIA NVQLink Architecture Integrates Accelerated Computing with Quantum Processors,” NVIDIA Technical Blog, Nov. 17, 2025. [Online]. Available: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/ [C]
[658] Riverlane, “Riverlane publishes QEC Technology Roadmap that can accelerate quantum computing's path to utility scale by 3–5 years,” Mar. 12, 2026. [Online]. Available: https://www.riverlane.com/press-release/riverlane-publishes-qec-technology-roadmap [C]
[659] Qblox; Riverlane, “Qblox and Riverlane Demonstrate Integration Enabling Real-Time Quantum Error Correction,” PR Newswire, Mar. 17, 2026. [Online]. Available: https://www.prnewswire.com/news-releases/qblox-and-riverlane-demonstrate-integration-enabling-real-time-quantum-error-correction-302716254.html [C]
[661] Riverlane, “Riverlane raises $75 million to meet surging global demand for quantum error correction technology,” Aug. 6, 2024. [Online]. Available: https://www.riverlane.com/press-release/riverlane-raises-75-million-to-meet-surging-global-demand-for-quantum-error-correction-technology [C]
[662] A. B. Ziad, A. Zalawadiya, B. Barber, and L. Skoric, “Quantum decoder,” Google Patents, Dec. 10, 2025. [Online]. Available: https://patents.google.com/patent/GB2641501A/en [G]
[727] Y. Wu, N. Liyanage, and L. Zhong, “Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction,” *Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems (ASPLOS '25)*, vol. 2, Mar. 2025, doi: [10.1145/3676641.3716005](https://doi.org/10.1145/3676641.3716005). [arXiv:2502.14787](https://arxiv.org/abs/2502.14787). Also https://github.com/yuewuo/micro-blossom. [D]
[729] X. Yang *et al.*, “Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder,” [arXiv:2605.04892](https://arxiv.org/abs/2605.04892), May 2026. Also https://arxiv.org/html/2605.04892. [D]
[735] Altera, “Altera Closes Silver Lake Investment to Become World's Largest Pure-play FPGA Solutions Provider,” Sep. 15, 2025. [Online]. Available: https://www.altera.com/newsroom/news/press-release/altera-silver-lake [G]

## פריטי אימות פתוחים
ה-367 ns של Micro Blossom הוא טענה ממאגר קוד ב-GitHub שאינה מופיעה בשום מאמר; התוצאה שפורסמה ב-ASPLOS 2025 היא 0.8 µs בממוצע ב-d=13, p=0.1%.
נתוני ה-FPGA של Relay-BP של IBM באים מסינדרומים מדומים, וה-24 ns / <1 µs שבתמצית סותרים נתון של 480 ns לכל חלון של 12 מחזורים, המופיע במקום אחר [G:RELAYBP-LATENCY-CONFLICT].
סבב C של Riverlane הוא $75 M בהודעה מ-2024 ו-$85 M במפת הדרכים מ-2026; הפער לא יושב.
שיתוף הפעולה בין IBM ל-AMD במפענח FPGA מתועד בעיתונות המקצועית בלבד, ותנאיו לא אושרו.
