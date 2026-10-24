# Claude-audit · WSG-20261024-STYLE10-002 (Astra A fázis, tíz stílus) · célzott, 2026-10-24 este

- **Vizsgált fájl:** `ai-coordination/results/WSG-20261024-STYLE10-002.md` – Astra eredeti, teljes eredménye, SHA-256 `f94acf93b71440837808df2a1f54bab927609e24649c0d29076b34f7fed86189`, `main` @ `abeb68079a8abbf9f70d531047058f3ec7e1c8ef`.
- **Auditor:** Claude (független; a termékadatokat saját forrásból újraellenőrizte). **Jelleg:** célzott, Péter 20:34-es kérése szerint; nem teljes műszaki audit.
- **Módszer:** (1) a repó A-902 méretpróba-motorja (`03_blender/geometry_A811_A812/meretproba/kanape_meretproba_a902.py`, lock v2b, P902_24A étkező = terv −0,30 m) lefuttatva Astra és Kave Home kanapé-jelöltjeivel, két szigorúsággal (minden út 0,90 m; ill. terasz/05.3 mellékút 0,75 m, ahogy Péter a P902_24A-nál elfogadta); (2) termékoldalak újraolvasása 2026-10-24 20:40–20:50 (Westwing HU, IKEA HU keresési API, Kave Home HU – Chrome, csak olvasás); (3) a 7. fejezet összegeinek újraszámolása; (4) a tíz koncepció csontvázának összevetése Claude gesztus-mátrixával (A1 a forráskatalógusban). **Kép nem készült, Astra nem futott.**
- **Összkép:** az A fázis tartalmilag teljes és számszakilag konzisztens; **két kritikus** és három fontos hiba van, mind javítható a V2 Medium-briefben Astra-újrakutatás nélkül. **A tíz látványkoncepciónak nincs valódi akadálya** – feltételekkel (lent).

## 1. Hibák és javítások

| # | Súly | Megállapítás | Bizonyíték | Javítás |
|---|---|---|---|---|
| **H1** | **KRITIKUS – kompozíció** | A tíz koncepció csontváza túl közeli: **4 stílus ugyanarra a kanapéra épül** (S01, S04, S06, S10 → Westwing Lennon L 238×180), 2 az IKEA U-ra (S02, S08), 3 a Melva L-re (S03, S05, S09); étkező **2 modellcsalád** (Toni ovál ×4, Anouk üveg ×6); **7/10 L3** elrendezés (nyugati TV), 3 L2; mindenhol 220–240 cm-es alacsony tároló + 250–280 cm-es fejvég. A különbség főként front/textil/relief/tükör – pontosan a „tíz szín, egy elrendezés” kockázat. | eredmény 6. fejezet „Főbútorok” és WOW-táblák; Claude A1 gesztus-mátrix | **Kötelező differenciálási mátrix** (2. pont): minden stílushoz eltérő ülőtömeg-sziluett **vagy** elrendezéscsalád **vagy** étkező-geometria, és csak egy stílus kaphatja ugyanazt a (kanapé, elrendezés, asztal) hármast. Astra dönt a kreatív tartalomról, de a hármasok nem ismétlődhetnek. |
| **H2** | **KRITIKUS – geometria** | **U kanapé + déli TV (L2) nem fér el** a P902_24A étkezővel: a motor szerint JÄTTEBO U 285×160, Gala U 300×225 és a generikus U 300×240 **egyik szigorúsággal sem** fér el déli TV-vel; **nyugati TV-vel (L3) mind elfér** (JÄTTEBO U 0,90-es utakkal, nézőtáv 2,45 m; Gala U 0,90, nézőtáv 3,30 m). Astra S04 és S10 L2-ben kér U-próbát (P05) – ez nem lehetséges. L kanapék (Lennon, Wolke, Melva, JÄTTEBO L) mindkét TV-fallal elférnek. A P902_24A befoglaló (300×240) csak a 0,75 m-es teraszmellékúttal fér (Péter elfogadta); 0,90-nel nem. | `scratch` futás 2026-10-24 20:38: 8 jelölt × 2 TV-fal × 2 szigorúság; részletek a 3. pontban | U-stílus (S02, S08, bármely U-próba) **csak L3**; L2 csak L-kanapéval. A V2-ben és a képfázisban rögzítve. Helyszíni mérés (hétfő) után újrafuttatás. |
| **H3** | FONTOS – termékadat | **P15 Wolke most igazolt** (a 25WES29958 oldal megnyílt): 258×167×65 cm, **1 050 000 Ft**, 12–13 hét, **bal sarok**, 16 variáns (teddy bouclé törtfehér/petrol kék/terrakotta/burgundi, texturált bézs/terrakotta…). **P14 Lennon igazolt:** 800 000 Ft, 238×180×68, 8–9 hét, **20 variáns – köztük sötétkék, olíva, terrakotta, rozsda** → Astra „nem létező kék Lennon” kijelentése téves: a BiBo L-tartalék kékben valós. **P04/P05 JÄTTEBO U 928 000 Ft igazolt** (496.076.48 / 294.713.87); van **karfa nélküli** változat 856 500 Ft (896.076.89 / 894.851.07) és sötétsárga-zöld szín (294.694.93) – Astra nem listázta. P02/P03 Melva árellentmondás nem oldva. | Westwing HU oldalak, IKEA keresési API, 2026-10-24 20:40–20:45 | Sarokirány (Wolke **bal**, Lennon **jobb**) az elrendezéshez igazítandó; a V2 táblája frissítve; P02/P03 kosárban ellenőrizendő. |
| **H4** | FONTOS – forrás | **Kave Home teljesen hiányzik** Astra kosarából (Péter 19:38 és 20:34: egyenrangú). Claude árkönyvtárában 48 Kave Home-sor igazolt (2026-10-24), ma kiegészítve (4. pont): valódi U-k (Gala 300×225, Gala 210 dupla chaise), ívelt Martina, moduláris Neom, Blok/Vera L-ek, kerek asztalok, székek. | `ARKONYVTAR_A902_2026-10-24.csv`; Kave Home HU oldalak 20:47–20:50 | A V2 stílusonként Kave Home **és** Westwing jelöltet kér; a 4. pont táblája kötelező bemenet. HUF: EUR×367 + lehetséges 5 % ÁFA-különbözet + 112,99 € szállítás, **HU végösszeg nem igazolt**. |
| **H5** | FONTOS – kreatív küszöb | A „Zenit/LF WOW = minimum” képi összevetés nélkül nem ítélhető; a meglévő Zenit/LF ChatGPT-képek kamerája, profilja, terasza és aránya eltér (Astra 8. fej. is jelzi). Astra rangsora szerint S03, S09, S10 a leggyengébb; S04–S10 és S01–S06 közeli pár. | eredmény 8. fejezet; `04_renderek/ai_chatgpt/` | A képfázis (**KEP-004**) **kalibrációs párral** indul: Zenit és LF újrarenderelése ugyanarra a Cam_02 alapra, azonos semleges fénnyel – ez a mérhető minimum. Thumbnail-sziluettpróba és „meleg fény nélkül” sorozat kötelező. |
| H6 | MEGJEGYZÉS – költség | A 7. fejezet összegei **újraszámolva: helyesek** (közös 17,90 + stíluseltérés; pl. S02 17,928, S07 17,950, S01/S10 17,650; stressz 26,35−1,40+kanapé+0,50). Kockázat: a WOW-sávok felső értékei több stílusban **a sor plafonján** vannak (S02 tároló+tükör 0,90 = 03a; fejvégek = 04b). Kave Home Gala U (≈1,32 M) a 03b 1,00 M plafon felett → csak PREMIUM-forgatókönyvben vagy tételcserével. | 7. fejezet; 4. pont | PREMIUM (+≈1 M) külön táblában; az U-stílusoknál a 03b-plafon kimondása. |
| H7 | MEGJEGYZÉS – alapkép | A Cam_02 alapképek (`04_renderek/A902_alap_v2b/`, `semleges_v2b/`) a **v2b** modellből készültek; a **v2b-1** (PR #11) a nyugati tetőkert-mellvédet (y 8,50→9,25) és két homlokzati rést javított – a Cam_02 bal széle felé esik. | `validator_report_2026-10-24_v2b1_lockjavitas.md` | A képfázis előtt a Cam_02 alapkép **újrarenderelése vagy eltérés-ellenőrzése a v2b-1 .blend-ből** (Blender-munka, csak Péter „mehet”-jével; most nem futott). |
| H8 | MEGJEGYZÉS | Astra bázisa `cb8080a`: a P902_24A-t (U 3,00×2,40, asztal −0,30 m) nem ismerte; az eredmény „Claude mérje” kitételei ezzel most mérve vannak (3. pont). 05.2 (K2) és konyha (K1) e célzott audit körén kívül. | – | – |

## 2. Differenciálási mátrix – Claude javaslata a V2 briefhez (Astra dönt, de a hármasok nem ismétlődhetnek)

Gesztus-kód: Claude A1 (A textil/színmező · B tükröző/geometrikus objekt · C beépített hatású tömeg · D fényarchitektúra · E panoráma-keretezés · F szobrászati bútor · G anyagritmus · H műtárgy-kuráció · I természet/terasz-folytonosság). Szabály: egy kód legfeljebb 2× elsődleges; ≥7 kód; egy (kanapé-sziluett, elrendezés, étkező) hármas csak egyszer.

| Stílus | Elsődleges gesztus | Ülőtömeg-sziluett (jelölt, igazolt méret) | Elrendezés | Étkező-geometria | Megkülönböztető függőleges / fény |
|---|---|---|---|---|---|
| S01 Kyoto Ink | **A** textilmező | alacsony L: Lennon 238×180 (szürkésbarna szövött) **vagy** Kave Home Vera 232 chaise | L3 | ovál fa (Toni 200×90) | rács + áttetsző mező; opál/textil nagy függeszték |
| S02 BiBo Nocturne | **B** tükröződés | **valódi U**: JÄTTEBO 285×160 sötétkék; prémium: Kave Home Gala 210 dupla chaise / Gala 300×225 (szín igazolandó); L-tartalék Lennon **sötétkék** | **L3 (kötelező)** | üveg tégla (Anouk 180×90) | lekerekített tükörlap + kék matt tömeg |
| S03 Alelí Casa | **F** étkező mint szobor | olíva L: Melva vagy **Kave Home Vera olíva 232** | **L2** | **kerek fa Ø150 (Nealy dió)** – társasági központ | kerámia relief; kerámia függeszték |
| S04 LA Horizon | **E** panoráma | alacsony L: Lennon, **vagy** Kave Home Blok chaise 300 | **L2 (csak L)** | barna üveg tégla (Anouk) | két eltolt horizont-lemez |
| S05 Miami Streamline | **G** bordaritmus | rózsás L: Melva kord | L3 | üveg tégla (Anouk) | lépcsőzött/lekerekített tároló, 2 bordás betét |
| S06 Zenit Atelier | **C** aszimmetrikus tömeg | mély L: Lennon **vagy** Kave Home Blok sarok 290×230 (≈0,96 M) | L3 | barna üveg (Anouk) **vagy** kerek üveg Ø120 (Argo) | eltolt magas elem, koncentrált fény |
| S07 Lake Forest Couture | **F** puha szobor | **Wolke 258×167 (bal)**; íves alternatíva **Kave Home Martina íves 246×112 + Neom puff** | L3 | ovál fa (Toni) **vagy** kerek Ø150 ekrü (Nealy) | valódi relief + fémes asztal |
| S08 Milano Radical | **B** geometrikus testek | **valódi U**: JÄTTEBO 285×160 (sötétkék vagy sötétsárga-zöld) | **L3 (kötelező)** | üveg tégla (Anouk) | „három test” tároló, sárga sík |
| S09 Paris Collector | **H** műtárgy | olíva L + eltérő fotel (Kave Home Corvena/Nema) | L3 | barna üveg | nagy mű + szilvás háttér; állólámpa D18 |
| S10 Desert Modern 70 | **C** lépcsőző tömeg | alacsony L: Lennon terrakotta/rozsda **vagy** Kave Home Blok chaise | **L2 (csak L)** | ovál fa (Toni) **vagy** kerek dió Ø120 (Naanim) | nagy grafikus relief |

Ismétlődés-figyelő: S01/S04/S06/S10 jelenleg azonos kanapé → a V2-ben legalább kettőnél **Kave Home-sziluett** (Vera/Blok/Martina) vagy más Lennon-konfiguráció kötelező; S04–S10 L2-pár → eltérő étkező-geometria és relief-típus kötelező; D (fényarchitektúra) és I (terasz-folytonosság) kód üres → S09 vagy S10 helyén alternatíva mérlegelhető (döntés Péternél, cím-szintű).

## 3. Geometriai méretpróba – P902_24A étkező (terv −0,30 m), lock v2b, 2026-10-24 20:38

Motor: a repó `kanape_meretproba_a902.py` (0,90 m-es utak: bejárat→terasz tolóajtó, konyha, hálók folyosója, 05.3 ajtó; kerülő ≤ 1,5×üres+1; TV-konzol 180×45; nézőtáv 2,0–3,4 m). Két futás: **szigorú** (minden út 0,90) és **mellékút 0,75** (terasz, 05.3 – ahogy a P902_24A-nál elfogadva). Kimenet: `audit_meretproba_astra_kanapek_20261024.json` (e mappában).

| Jelölt (külső méret) | Nyugati TV (L3) – szigorú 0,90 | Déli TV (L2) – szigorú 0,90 | Megjegyzés |
|---|---|---|---|
| IKEA JÄTTEBO U 285×160 (P04/P05) | **ELFÉR** · út ≥1,00 · nézőtáv 2,45 · bbox [5,12; 5,08; 6,72; 7,93] | **NEM** | U-öböl két heverő között ≈95–100 cm → kis asztal |
| Westwing Lennon L 238×180 (P14) | ELFÉR · 1,00 · 2,45 | ELFÉR · 1,00 · 3,33 | jobb sarok |
| Westwing Wolke L 258×167 (P15) | ELFÉR · 1,00 · 2,42 | ELFÉR · 1,00 · 3,32 | bal sarok |
| Westwing Melva L 238×143 (P01–P03) | ELFÉR · 1,00 · 2,38 | ELFÉR · 1,00 · 3,33 | |
| IKEA JÄTTEBO L 190×160 (P06) | ELFÉR · 1,00 · 2,45 | ELFÉR · 1,00 · 2,75 | kompakt tartalék |
| Kave Home Gala U 300×225 | **ELFÉR** · 0,90 · 3,30 · bbox [5,32; 5,05; 7,57; 8,05] | **NEM** | nézőtáv a sáv tetején; üveg előtt szorosan |
| Kave Home Blok sarok L 290×230 | ELFÉR · 1,00 · 3,35 | NEM | |
| P902_24A befoglaló U 300×240 | NEM (0,90) · **ELFÉR 0,75-ös mellékúttal** (0,90/0,95/0,95/0,90 célmaximumok) | NEM | Péter elfogadta a 0,75-ös teraszmellékutat |

Értelmezés: **minden Astra-jelölt elfér L3-ban; U csak L3-ban.** A terv szerinti geometria helyszínen nem mért (±15 cm) – hétfő után újrafuttatás. Ez méretpróba, nem validátor-PASS: a Blender bútorréteg stílusonként még nem épült meg.

## 4. Kave Home-alternatívák (Kave Home HU webshop, EUR; ×367 Ft + lehetséges 5 % ÁFA-korrekció; szállítás 112,99 €/utcaszint; HU végösszeg nem igazolt)

| Kategória | Termék | Méret | Ár (EUR) → ≈ Ft | Forrás/dátum | Stílus-jelölt |
|---|---|---|---|---|---|
| **Valódi U** | Gala 5 személyes sarok + végmodul (jobb v. bal), bézs mikro-bouclé | 300×225, m 87, ülésmélység 70 | 3 605 → ≈1,32 M (chenille 3 910) | Kave HU oldal, 20:47 | S02/S08 prémium U (szín igazolandó: bézs/szürke/fehér/sötétzöld látható, **kék nem igazolt**) |
| Valódi U, kompakt | Gala 3 személyes **dupla chaise** | 210 cm széles | 2 685 (mikro-bouclé) / 2 999 (chenille) → ≈0,99–1,10 M | ua. | S02/S07 kompakt U, prémium sziluett |
| U, nagy | Gala 6 személyes sarok | 300×300 | 4 095–4 399 | ua. | csak PREMIUM, befoglaló-teszt kell |
| L sarok | Blok 3 személyes sarok, bézs chenille | 290×230, m 69 | 2 625 → ≈0,96 M | árkönyvtár + oldal 20:50 | S06 (alternatív mély L), S04 |
| L chaise | Blok 3 személyes chaise (jobb/bal) | 300 cm | 2 195 → ≈0,81 M | oldal 20:50 | S04/S10 alacsony L; színek: bézs chenille, zöld kord, szürke kord |
| L chaise | Vera 3 személyes chaise, **olíva** v. bézs (NEW) | 232 cm | 2 320 → ≈0,85 M | oldal 20:47 | **S03, S09 olíva L**; S01 |
| **Íves** | Martina 3 személyes **íves**, szürke bouclé | 246×112×73 | 2 560 → ≈0,94 M | árkönyvtár (termékoldal) | **S07** Péter félhold-ötlete: Martina íves + Neom végpuff (279 €) |
| L moduláris | Martina 3 személyes + jobb chaise, kő zsenília | 287 | 3 235 → ≈1,19 M | árkönyvtár | PREMIUM |
| Moduláris | Neom 3 személyes + chaise 263 / modulok (sarok 705, chaise 585, 2-üléses 619–985, puff 279) | 263 | 1 570 → ≈0,58 M (+modulok) | árkönyvtár | **S01/S10**: konfigurálható L/U ≈0,7–0,9 M – Astra konfigurálja |
| Étkező | Nealy kerek, sötét dió / ekrü MDF | Ø150 | 1 465 / 1 349 → ≈0,54 / 0,50 M | árkönyvtár | **S03** (társasági központ), S07 (ekrü) |
| Étkező | Naanim kerek dió · Argo kerek üveg fekete · Vedira kerek üveg tópszín | Ø120 / Ø119 / Ø120 | 539 / 379 / 379 | árkönyvtár | S10 / S06 / S04 |
| Szék | Eamy (barna PU v. világosszürke) · Ciselia bézs · Granite bézs-dió | – | 179 · 199 · 419 | árkönyvtár | 6 szék 0,28 M-on belül: Eamy/Ciselia; Granite PREMIUM |
| Fotel | Corvena olíva 509 · Sylo 879 · Nema tópszín bouclé 1 249 · Veliro bársony 1 340 | – | → 0,19–0,49 M | árkönyvtár | S09 fotel (03c ≤0,22 M → Corvena) |
| Dohányzó/kisasztal | Mosi Ø90 695 · Sheffield márvány Ø80 365 · Adularia üveg 85×85 479 · Orlia barna üveg 50×50 219 | – | → 0,08–0,26 M | árkönyvtár | S06 nagy alacsony asztal (Mosi), S07 fémes (Sheffield), S04 barna üveg (Orlia) |

Westwing-oldalon ma igazolt bővülés: Lennon 20 szín (**sötétkék, olíva, terrakotta, rozsda, antracit, törtfehér**; bouclé/kord/vászon változatok), Wolke 16 szín (**petrol kék, terrakotta, burgundi, törtfehér teddy**), JÄTTEBO karfa nélküli U 856 500 Ft és sötétsárga-zöld szín. **Kave Home és Westwing így minden stílushoz ad legalább egy valós, méretezett sziluett-alternatívát.**

## 5. Státusz és következő lépés

- Astra A fázis: **KONCEPCIÓ – NEM VALIDÁLT · költség ELŐSZŰRT – FELTÉTELES · geometria: méretpróbával igazolt befoglalók, validátor-PASS nincs** (bútorréteg nem épült). Ez megfelel az eredeti brief státuszkorlátjának.
- Javítások átvezetve: `ai-coordination/requests/WSG-ASTRA-HIGH-KREATIV-V2.md` (2.0 pont: audit-korrekciók; **mind a tíz** megerősítése, nem három) és új képfázis: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004.md` + `05_promptok/A902_STYLE10_Cam02_prompt_sablon_v2.md` (**NEM INDÍTOTT**, külön jóváhagyásra).
- **Valódi akadály a tíz látványkoncepciónak: nincs.** Feltételek: H2 (U csak L3), H7 (Cam_02 alap v2b-1-ből), kalibrációs pár (H5), helyszíni mérés utáni újrafuttatás (K5/K6 nyitott marad a hétfői fotókig).
- Nem történt: Astra-futás, képgenerálás, Blender-módosítás, rendelés, ajánlatkérés.
