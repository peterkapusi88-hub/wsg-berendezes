# ASTRA-kérés TERVEZET – WSG-A902-STYLE-001

> **2026-10-24 06:30 – frissítés:** a parkettára (Grey Treviso Oak EL2184), a teraszra (többszintű tetőkert) és a kilátásra a `../A902_v1_1/INPUT_CSOMAG_v1_1.md` az irányadó. A Cam_05 terasznézet és az itteni terasz-leírás elavult.

**Státusz: TERVEZET – nincs PR, nincs indítás.** A `REQUEST_TEMPLATE.md` szerint kitöltve; élesítéskor Claude ebből készít `handoff/astra-A902-style-01` ágat és `[ASTRA-REVIEW]` draft PR-t, csak Péter jóváhagyásával. A PR #1 pilot (1 helyiség) sikere az előfeltétel.

- **Task ID:** WSG-A902-STYLE-001
- **Cél AI:** ASTRA_WORK · **Típus:** STYLE_CONCEPT + PRODUCT_RESEARCH (előszűrés)
- **Lakás:** A-902 · **Helyiségek:** nappali–étkező (Cam_02), étkező–konyha (Cam_03), master (Cam_04); terasz csak stíluskártya-szinten
- **Stílus:** ÚJ STÍLUSOK – NINCS MÉG KIVÁLASZTVA (Zenit és Lake Forest csak mérce)
- **Javasolt gondolkodás:** medium – Ultra/Max nem engedélyezett
- **Keret:** 20 M Ft bruttó teljes lakás, ebből 18 M tervezhető + 2 M tartalék; kiindulás: `ai-coordination/inputs/A902_v1/KOLTSEG_KIINDULAS_A902.csv`
- **Bemenet:** `ai-coordination/inputs/A902_v1/INPUT_CSOMAG.md` és az abban felsorolt fájlok

## Kért eredmény
1. **3–4 egymástól karakteresen eltérő stíluskártya** (név, 1 mondatos érzés, 4–6 forma/szín/fény/tér-jegy, kerülendő giccs) – a Zenit/LF-től is különbözzenek.
2. Stílusonként **2–3 WOW-gesztus** a csomag 5. pontjában jelölt helyekre, mindegyikhez: miből készül (anyag, dekor/termék), becsült sáv, melyik költségsorból jön a pénz.
3. Stílusonként **renderprompt** a három semleges Blender-nézethez (Cam_02/03/04), a geometria megtartásával és csak megvalósítható látható anyagokkal.
4. Stílusonként **költségsáv-eltérés** a kiindulási táblához képest (mely sor nő, mely csökken; összeg ≤ 18 M).
5. A fő látható tételekhez **2–3 valós termék-jelölt** (név, link, ár, dátum, méret) – előszűrés, nem végleges lista.
6. **Kérdéslista** Claude felé (hiányzó méret, geometria, kivitelezhetőség).

## Siker
„Ez rohadt drágának néz ki" első benyomás, ízlésesen; semmi nem látszik drágábbnak, mint amiből ténylegesen készül; minden stílus ugyanazon a kereten és geometrián összevethető.

## Nem feladat
Blender-fájlok módosítása, végleges stílusválasztás, rendelés, ajánlatkérés, külső levél, videó.

## Visszaadás
PR-komment `WSG-ASTRA-RESULT: WSG-A902-STYLE-001` fejléccel a `RESULT_TEMPLATE.md` szerint; ha nincs írási jog, a Work eredményében, `handoff blocked` jelzéssel (Claude ilyenkor Chrome-relay-jel veszi át).
