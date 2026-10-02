---
id: ct_sfq
name: בקרה ספרתית SFQ (מיליקלווין)
layer: "5 בקרה"
status: emerging
since: 2026
one_line: "פולסי שטף מקוונטטים משבב ספרתי מניוביום, המורכב בשיטת השבב ההפוך על פיסת הקיוביטים, מניעים שערים בטמפרטורת מיליקלווין ומחליפים את כבל המיקרוגל הקואקסיאלי לכל קיוביט."
verdict: "ממשי: מודול אחד של חמישה קיוביטים בנאמנות חד-קיוביטית > 99%. לא הוכחו: שערים דו-קיוביטיים, קריאה, ממתח שטף, חסינות לקוואזי-חלקיקים מעבר לחמישה קיוביטים. להוריד בדרגה אם עד 2028 לא יהיה מודול SFQ של >20 קיוביטים."
updated: 2026-09-30
---

Λ = מקדם דיכוי השגיאות לכל צעד במרחק הקוד; QBI = DARPA Quantum Benchmarking Initiative (שלב A — רעיון → B — תוכנית מו״פ → C — אימות ותיקוף (V&V) ממשלתיים); G1–G7 = מחלקות היעדים של הדוח (ראו "שחקנים וכלכלה").

## זהות ומוצא

לוגיקת קוונט שטף בודד (SFQ) מאחסנת ביט כקוונט שטף אחד Φ₀ = h/2e בלולאה מוליכת-על; צומת ג'וזפסון ממתג פולט פולס ששטחו Φ₀, כ-1 mV למשך 2 ps. הצורה המהירה שלה (RSFQ; Likharev ו-Semenov, 1991) נבנתה למחשוב קלאסי ב-4 K. בבקרת קיוביטים, רכבת פולסים הנעולה על המחזור של הקיוביט מצטברת באופן קוהרנטי לסיבוב ראבי [S][565]. בצורת 2026 הבקר מורכב בשיטת השבב ההפוך על הקיוביטים ב-10 mK [D][304]. התחום הרחב של האלקטרוניקה מוליכת-העל נסקר באופן שוטף ב-Superconductor Electronics Monitor [P][56].

תכונות. **זיקת הנושא:** שכבת בקרה מיוצרת לחלוטין. **זמן / שזירה:** לא ישים. **קריאה:** לא הודגמה [C][53]. **ניידות:** אין; מחוברת בבליטות. **אופן הבקרה @ מיקום:** הנעת מיקרוגל המסונתזת ספרתית *בטמפרטורת מיליקלווין*. **מבנה השגיאה כפי שהקוד רואה אותו:** פאולי ועוד פרצי הרעלה מתואמים [D][249]. **ייצור:** ליתוגרפיה רב-שכבתית של ניוביום.

## פיזיקה וגבולות

כל פולס Φ₀ נותן לקיוביט דחיפת פאזה קבועה, ולכן זווית השער נקבעת לפי *מספר* הפולסים, לא לפי משרעת אנלוגית. מיתוג עולה רק ~I_cΦ₀ ≈ 10⁻¹⁹ J לאירוע; בתוך תקציב של עשרות µW בתא הערבוב ב-20 mK, מה שמגביל ראשון הוא הספק הממתח הסטטי של RSFQ וחלוקת הממתח.

הרצפה היא שבירת זוגות: צמתים ממתגים פולטים פוטונים מעל פער האלומיניום (2Δ ≈ 90 GHz), השוברים זוגות קופר בשכבת הקיוביט — הרעלת קוואזי-חלקיקים — וגורמים לרלקסציית T₁ ולפרצים מתואמים. הגבלת רוחב הפס של הפולסים של מעגל ההנעה צפויה לסלק אותה, ולהביא את שגיאת השער לכיוון 0.1% ברצפים תהודתיים [D][249]. מנופים אחרים: מלכודות קוואזי-חלקיקים, הנדסת פער, בולעי גלים מילימטריים.

## מצב ההנדסה העדכני

הטוב ביותר שהודגם (3 בספטמבר 2026): המודול של SEEQC בן חמשת הקיוביטים ב-10 mK, נאמנות חד-קיוביטית מעל 99%, כניסה ספרתית אחת שמפורקת בריבוב לכמה קיוביטים [D][304][C][53]. אף תוצאת SFQ אינה עוברת חמישה קיוביטים או כוללת שער דו-קיוביטי או מחזור תיקון שגיאות.

| שנה | נתון | מי | תג+מפתח |
|---|---|---|---|
| 2014 | 4,544 DAC-שטף על השבב ל-512 קיוביטים דרך 56 חוטים | D-Wave | [D][430] |
| 2019 | שער SFQ ראשון על טרנסמון, ≈ 95% | Wisconsin / Syracuse | [D][566] |
| 2023 | מעגל הנעה על פיסה נפרדת: שגיאה של 1.2(1)% לקליפורד, מתוכה 0.96(2)% מהרעלה | Wisconsin, Syracuse, NIST | [D][249] |
| 2026-03 | חמישה קיוביטים, בקרת SFQ ב-10 mK; חד-קיוביטי > 99%, שיא של 99.9% | SEEQC | [D][304] |
| 2026-03 | קריאה בהשהיית זמן של פלוקסון, ללא דיווח על נאמנות | קדם-פרסום | [S][568] |

איבר השגיאה השולט: הרעלת קוואזי-חלקיקים במודול של 2023 [D][249]; לא נחשף עבור המודול של SEEQC.

## ייצור, חומרים ושרשרת האספקה

פיסת הבקרה היא Nb/AlOx/Nb רב-שכבתית — שמונה שכבות ניוביום מושטחות או יותר, 10⁴–10⁶ צמתים — בשונה מתהליך הקיוביטים מאלומיניום [D][569]. מפעלי הייצור מעטים: MIT Lincoln Laboratory (קו SFQ5ee, מפעל הייצור לקיוביטים SQUILL) [C][570], תהליך הניוביום וספריות התאים של AIST [D][571], ומפעל הייצור המסחרי של SEEQC ב-Elmsford, NY [C][572]. שיעור תקינות סביר דורש פיזור של הזרם הקריטי של אחוזים בודדים על פני אלפי צמתים. החשיפה לפיקוח על יצוא (תקנת BIS מ-2024-09-06): ECCN 3A904, 3B904 ו-4A906; 3A901.a, בקריאה מילולית, חל על CMOS קריוגני בלבד [G][301]. נקודות כשל יחידות: מקררי דילול, חיבור בבליטות אינדיום, וכלי ריסוס (sputter) ו-CMP לניוביום.

## בקרה, קריאה ועומס הקלט-פלט

בקרה מטמפרטורת החדר צריכה בערך כבל קואקסיאלי אחד להנעה וקו שטף אחד לכל טרנסמון, ולכן חתך המקרר ועומס החום קובעים את גבולה; פלטפורמה ברמת KIDE מציעה > 4,000 קווי RF עבור "יותר מ-1000 קיוביטים" [C][G:BLUEFORS-KIDE]. בקרת SFQ צריכה שעון ועוד זרם פקודות בקצב נמוך [D][304]. קריאת SFQ קיימת רק כשיטה בקדם-פרסום [S][568]; SEEQC מונה את ממתח השטף כעבודה עתידית [C][53].

## תפקיד במחסנית

ארכיטקטורה: סריג הטרנסמונים מוליכי-העל. היא דורשת ליתוגרפיה של קיוביטים מוליכי-על ומודולים בשבב הפוך; היא מספקת לוגיקה ספרתית קרה למפענח קריוגני ול-DAC-שטף של D-Wave [D][430]. המסלולים הקרים לבקרה הם CMOS קריוגני או SFQ: ה-CMOS הקריוגני משתמש מחדש במפעלי ייצור ובכלי תכנון מסחריים; SFQ צריכה מערכת אקולוגית של ניוביום, שהכלים המסחריים שלה נעצרים באימות הפיזי. ההתנגשות עם הטרנסמון — פוטוני מיתוג המרעילים את הקיוביט — פתוחה: ההפחתה שלה צפויה בלבד [D][249], והדיווח של SEEQC מ-2026 על היעדר הרעלה ניתנת לגילוי הוא סיקור עיתונאי [C][53]. התרומה לשעון הנגזר: ניטרלית — סבב הסינדרום נשאר על **0.65 µs**, מול מחזור תיקון השגיאות הנמדד של **1.1 µs** [D][1]. משבצות ריקות שכנות: ממתח שטף ב-SFQ, קריאה ב-SFQ.

## ראיות — כיצד נמדדו המספרים

כל מספר בולט הוא ממוצע על פני פעולות קליפורד בבחינת ביצועים אקראית (RB) [D][566][D][249][D][304]. RB מניח שגיאות מרקוביות שאינן תלויות בשער, ולכן פרצים מתואמים נדירים נבלעים בממוצע כהרעה קלה, ומודול יכול לעבור ב-99.9% ועדיין לפלוט שגיאות מתואמות שהמפענחים אינם ממדלים. ה"היעדר של הרעלת קוואזי-חלקיקים ניתנת לגילוי" של SEEQC מדווח רק בעיתונות [C][53]. לא דווחו: זוגיות המטען תחת תזמון רציף, ו-T₁ כשהשעון פועל וכשהוא כבוי. אין שחזור בלתי תלוי: כל מחברי 2026 הם מ-SEEQC [D][304]. סתירות: "מעל 99%" בתמצית [D][304] לעומת "מעל 99.5%" בעיתונות [C][53]; "ננו-ואטים לקיוביט" [C][53] לעומת ~1.6 µW לקיוביט בהערכה מ-2026 [S][550][G:CRYOCMOS-POWER-CONFLICT].

## שחקנים וכלכלה

**מי.**

| ארגון | תפקיד | מדינה | מה הם עושים בה | ראיות |
|---|---|---|---|---|
| SEEQC | מפתח / מפעל ייצור | ארה״ב | מודול בקרת SFQ ב-mK; מפעל ייצור מסחרי ל-Nb | [D][304][C][572] |
| IBM | אינטגרטור | ארה״ב | שילוב SFQ עם SEEQC (QBI); בקרת CMOS קריוגני משלה | [P][54][C][527] |
| Wisconsin–Madison, Syracuse, NIST Boulder | מחקר | ארה״ב | בקרת SFQ תהודתית; מחקר ההרעלה | [S][565][D][249] |
| MIT Lincoln Laboratory | מפעל ייצור | ארה״ב | תהליך SFQ5ee; מפעל הייצור לקיוביטים SQUILL | [C][570] |
| D-Wave | מפתח (תחום סמוך) | קנדה | DAC-שטף מבוססי SFQ על השבב במחשבי הרפיה | [D][430] |
| AIST, NEC | מחקר / מפעל ייצור | יפן | ספריות תאים ל-Nb; בקר מרובב ב-4.2 K | [D][571][C][567] |

**כספים.**
- 2020-09-16 · SEEQC · סבב A · $22.4 M · EQT Ventures (מובילה) · נסגר [C][572]
- 2025-01-16 · SEEQC · סבב צמיחה · $30 M · SIP Global ואחרים · נסגר [P][573]
- 2025-06-12 · SEEQC + IBM · שילוב SFQ במסגרת DARPA QBI, ו-IBM היא המבצעת [G][65] · לא פורסם · הוכרז [P][54][G:SEEQC-2026]
- 2026-06-29 · SEEQC · S-1 להנפקה ראשונית לציבור (IPO) ב-Nasdaq, לצד הסכם SPAC עם Allegro Merger Corp (שווי פעילות של $1 B) · הוגש [C][556][G:SEEQC-S1-2026-07]
- 2026-08-25 · SEEQC / Allegro · מיזוג ה-SPAC הסתיים בהסדר: Allegro מקבלת מניות בשווי $6 M לפי שווי טרום-כסף (pre-money) של $1.3 B, בעת IPO עתידית, מכירה או גיוס של ≥ $100 M · בוטל [G][574]

**שוק ושרשרת אספקה.** עדיין אין שוק לבקרת SFQ: ספק אחד, הדגמה אחת. SkyWater, מפעל הייצור המסחרי הנקוב בדוחות ה-10-K של D-Wave [G][492], שייך ל-IonQ מאז יולי 2026 [C][19]. G3 ו-G4 משלמים עליה; G7 — במידה משנית.

**קניין רוחני ותקנים.** SEEQC מחזיקה בפטנטים של Hypres על RSFQ ועל תהליך הניוביום, שהועברו אליה עם היפרדותה ב-2019 [C][572]. אין תקנים לבקרת SFQ; בסיסי התכנון המשותפים הם ספריית התאים של AIST [D][571] והערכות של MIT-LL [C][570].

**מפות דרכים ועמידה בהבטחות.** SEEQC: בקרת SFQ בטמפרטורת מיליקלווין (הובטחה ל-2021–22 · סופקה ב-2026-03, על חמישה קיוביטים) [D][304]; בקרת שטף וקריאה על הפיסה (הוכרזו ב-2026-03 · ללא תאריך) [C][53].

**פרשנות אסטרטגית.** יכולת תהליך הניוביום נמצאת בידי SEEQC, ודרך Lincoln Laboratory — בידי ממשלת ארה״ב. מבין המסלולים הקרים, CMOS קריוגני או SFQ, ל-CMOS הקריוגני יש הישגים מתועדים חזקים יותר: הדגמת תיקון שגיאות תחת בקר CMOS קריוגני ב-4 K [D][190] ושוויון עם אלקטרוניקה חמה על מעבד של IBM [C][527]; ל-SFQ יש שערים חד-קיוביטיים על חמישה קיוביטים מקבוצה אחת [D][304].

## תחזית ושאלות פתוחות

לאשר אם עד סוף 2027 קבוצה כלשהי תפרסם שער דו-קיוביטי המונע ב-SFQ בשגיאה מתחת ל-1%, התקן בבקרת SFQ של יותר מעשרה קיוביטים, או שעות של נתוני זוגיות מטען ללא פרצים המתואמים עם השעון. להוריד בדרגה אם עד סוף 2028 אף מודול SFQ לא יעבור עשרים קיוביטים, או אם פירוק של תקציב השגיאה יראה הרעלה מעל 0.1% לקליפורד. שאלות פתוחות: האם "היעדר הרעלה ניתנת לגילוי" שורד תזמון רציף במחזורי העבודה של תיקון שגיאות? האם ממתח שטף ב-SFQ יכול להחזיק את יציבות ה-DC שהטרנסמונים צריכים?

## מקורות
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[53] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [C]
[54] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [P]
[56] R. Neeman, “Superconductor Electronics Monitor,” Qodeh, 2026, doi: [10.5281/zenodo.21860767](https://doi.org/10.5281/zenodo.21860767). [Online]. Available: https://qodeh.com/publications/superconductor-electronics-monitor-2026/ [P]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[492] U.S. Securities and Exchange Commission, “EDGAR full-text search: ‘SkyWater’ in D-Wave Quantum Inc. 10-K filings,” SEC EDGAR Full-Text Search, Feb. 26, 2026. [Online]. Available: https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982 [G]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[556] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [C]
[565] R. McDermott and M. G. Vavilov, “Accurate Qubit Control with Single Flux Quantum Pulses,” *Phys. Rev. Appl.*, vol. 2, no. 1, Art. no. 014007, Jul. 2014, doi: [10.1103/PhysRevApplied.2.014007](https://doi.org/10.1103/PhysRevApplied.2.014007). [S]
[566] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[567] AIST; Yokohama National University; Tohoku University; NEC, “Successful demonstration of a superconducting circuit for qubit control within large-scale quantum computer systems,” NEC Press Releases, Jun. 3, 2024. [Online]. Available: https://www.nec.com/en/press/202406/global_20240603_02.html [C]
[568] S. Kamimura, A. Taguchi, M. Tanaka, and T. Yamamoto, “Fluxon Time-Delay Readout of a Superconducting Qubit Protected by a Spectral Gap in a Josephson Transmission Line,” [arXiv:2603.13175](https://arxiv.org/abs/2603.13175), Mar. 2026. [S]
[569] S. K. Tolpygo, “Superconductor Digital Electronics: Scalability and Energy Efficiency Issues,” [arXiv:1602.03546](https://arxiv.org/abs/1602.03546), Feb. 2016. [D]
[570] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[571] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[572] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[573] SIP Global Partners, “SIP Global Partners Participates in $30M Round for SEEQC, Developer of the World's First Full-Stack Processor for Quantum Computers,” PRWeb, Jan. 16, 2025. [Online]. Available: https://www.prweb.com/releases/sip-global-partners-participates-in-30m-round-for-seeqc-developer-of-the-worlds-first-full-stack-processor-for-quantum-computers-302352970.html [P]
[574] Allegro Merger Corp.; SeeQC, Inc., “Settlement, Termination and Release Agreement,” U.S. Securities and Exchange Commission (EDGAR), Aug. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1779977/000121390026095175/ea028847004ex2-2.htm [G]

## פריטי אימות פתוחים

- הטקסט המלא של [304] חסום מאחורי חומת תשלום: חמשת הקיוביטים, 10 mK ו"ננו-ואטים לקיוביט" לקוחים מהעיתונות [53], לא מהתמצית.
- הפרמטרים של SFQ5ee של MIT-LL לא הושגו; [570] עוסק רק במפעל הייצור לקיוביטים.
- לא נמצאה תוצאה סינית מתוארכת מ-2025–26 של בקרת קיוביטים ב-SFQ; אין ספירה של משפחות פטנטים.
- ההכנסות והמזומנים של SEEQC מופיעים בטופסי ה-S-1 שלה — הכנסות של $4.2 M ב-2025, $18.1 M במזומן ב-2026-06-30 [G:SEEQC-S1A-2026-08]; גודל ההנפקה עדיין ריק (תיקון ל-S-1 מ-2026-09-11), ושווי הפעילות לקוח מהעיתונות המקצועית.
- היכולת של SkyWater במוליכי-על הוסקה מאזכורים בדוחות ה-10-K של D-Wave [492].
