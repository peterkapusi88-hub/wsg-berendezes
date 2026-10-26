# A-902 · Philips Hue alapcsomag – közös műszaki és fajlagos költségalap a versenyhez (v1, 2026-10-25 04:40 CET)

**Mire:** mindhárom versenyző ugyanazzal a Hue-rendszerlogikával és fajlagos árakkal számol, hogy a „Hue-kompatibilis” ne általános kijelentés, hanem azonos alapon összevethető tétel legyen (r2 brief §2–4, §11.6, §11.10; GOAL §4.5; `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`).

**Státusz:** `BECSLÉS – KÖZÖS ALAP`. A fajlagos árak 2026. októberi magyar webshop-sávok, **nem dátumozott termékoldalról ellenőrzöttek** (a Claude-munkamenetből a webshopok nem voltak lekérdezhetők 2026-10-25 hajnalban). **A költségkapu előtt Claude Chrome-on ellenőrzi és dátumozza** (alza.hu, emag.hu, philips-hue.com/hu-hu). Eltérés esetén a tábla frissül, a versenyzők promptjai nem.

## 1. Rendszerelv (kötelező, mindhárom versenyzőnél azonos)
- **Minden általános és dekoratív fény Hue-jelenetben működik.** Kivétel: a szekrénybelső tisztán funkcionális fénye (IKEA-szalag ajtóérzékelővel is lehet).
- **Lámpatest:** csak E27 / E14 / GU10 foglalat, amelybe a Hue-izzó fizikailag befér, vagy Hue-gyári lámpatest, vagy Hue-szalag. G9/G4/integrált nem-Hue LED nem.
- **Rejtett vonalfény:** Hue Lightstrip Plus (V4, 2 m alap + 1 m hosszabbítók, max. 10 m egy tápról) vagy Hue Gradient (ahol a színátmenet látványelem). Alumínium profilban, opál fedéllel, a szalag kívülről soha nem látszik.
- **Betáplálás:** a szalag tápja **meglévő dugaljra** megy (D-azonosító a `01_alaprajzok/villamos_kiallasok/A902_villamos.csv`-ből). Függeszték és fali lámpa **csak meglévő ML/FL kiállásra**. Új vezetékért nincs vésés, fúrás, és a mennyezeti hűtő-fűtő mezőbe nem fúrunk.
- **Vezérlés:** egy Hue Bridge a lakásra (már számolva), Hue Tap Dial vagy Smart Button a kapcsolóoszlop mellé, jelenetek 2200–2700 K (este), 3500–4000 K (nappal/munkafény).
- **Fürdő 06.2:** csak nedves zónára alkalmas lámpatest a meglévő pontokon; a tükör mögötti Hue-szalag IP-védett profilban.

## 2. Fajlagos árak (bruttó, becslés – ellenőrzés előtt)
| Tétel | Egység | Ft (sáv) | Megjegyzés |
|---|---|---|---|
| Hue Bridge (v2 vagy Pro) | 1 db / lakás | 25 000–45 000 | egyszer, a 10-es sorban |
| Hue Lightstrip Plus V4 alapkészlet 2 m (szalag + táp + vezérlő) | készlet | 28 000–36 000 | a koncepció-doksi 2026-10-i becslése: 2+1 m ≈ 28–32 e |
| Hue Lightstrip Plus hosszabbító 1 m | db | 10 000–14 000 | |
| Hue Gradient Lightstrip 2 m alap / 1 m hosszabbító | készlet / db | 55 000–70 000 / 20 000–28 000 | csak ahol a színátmenet a koncepció része |
| Hue White Ambiance E27 1100 lm | db | 10 000–14 000 | 2200–6500 K |
| Hue White and Color Ambiance E27 | db | 16 000–22 000 | csak ahol szín kell |
| Hue White Ambiance GU10 | db | 10 000–14 000 | spot-lámpatestbe |
| Hue White Ambiance E14 | db | 9 000–13 000 | |
| Hue Tap Dial Switch / Smart Button | db | 15 000–20 000 / 8 000–11 000 | |
| Hue Smart Plug (táp kapcsolásához) | db | 10 000–13 000 | ha a lámpatest nem Hue, csak izzó |
| Alu LED-profil opál fedéllel, süllyeszthető vagy felületre | fm | 2 500–5 000 | végzárókkal, rögzítőkkel; 2–3 m-es szálak |
| Bútorasztalos horony/ellenfalc a profilnak | fm | 1 500–3 000 | az asztalos ajánlatában; IKEA-vázon utólagos lécezés |
| Villanyszerelő (szalagfektetés, táp elhelyezése, Hue-beüzemelés) | óra | 10 000–15 000 | tipikusan 1–2 nap/lakás; csak meglévő dugaljra |
| Kábelrejtés (kábelcsatorna, bútor mögötti vezetés) | fm | 800–2 000 | |

## 3. Számítási minta (a versenyző ezt a sémát használja)
| Fényvonal / lámpa | Hol (fal/elem-ID) | Hossz vagy db | Táp / kiállás | Profil | Anyag Ft | Szerelés Ft | Összesen Ft |
|---|---|---|---|---|---|---|---|
| pl. W01 TV-fal felső kontúr, felfelé | W01 / TVF-01 | 3,6 m = 2 m alap + 2×1 m | D16 | 3,6 fm opál, süllyesztett | 32 000 + 2×12 000 + 3,6×4 000 = 70 400 | 2 óra = 25 000 | 95 400 |

**Tipikus teljes lakás (tájékoztató, becslés):** 8–12 m rejtett szalag, 6–10 Hue-izzó, 1 Bridge, 2 vezérlő, 1–2 nap villanyszerelő → **0,55–0,90 M Ft**; ez a 10-es sor (cél 1,00, sáv 0,70–1,40) belsejében van, a lámpatestek nélkül. A dekoratív lámpatestek (függeszték, álló-, asztali lámpa) **külön** jönnek hozzá, a 10-es sorból.

## 4. Mit kér a kapu a versenyzőtől Hue-ban
Minden fényvonalhoz és lámpatesthez: hol (fal-/elem-ID), hossz vagy darab, Hue-termék, táp és dugalj-/kiállás-azonosító, profil, rögzítés (asztalos horony vagy felületi), kábelút, anyag + szerelés bruttó. Enélkül a világítás tétele „nem igazolt”, és az ellenőrző a 3. pont tájékoztató sávjának felső értékével pótolja.

