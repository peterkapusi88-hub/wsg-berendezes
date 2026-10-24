---
name: "westside-berendezes"
description: "Péter három Westside Grand-lakásának (A-811, A-812, A-902) berendezése: lakásadatok, 10/10/20 M-os bruttó keretek, az „olcsón drága” elv és Péter hitvallása („Mi szeressünk bele. Teremtsünk értéket.”), nyitott stíluslabor (Zenit és Lake Forest csak két példa a 10+ stílusból), render-státuszok, Kave Home + IKEA + asztalos forrásszabály, Hue-világítás, a GitHub-repo mint igazság. Használd, ha a WSG-lakások berendezéséről, bútorlistáról, büdzséről, alaprajzi elrendezésről, Blender-modellről, renderről, stílusokról vagy a lakberendezői ajánlatokról van szó."
---

# Westside Grand – berendezés (A-811, A-812, A-902)

Ez a skill Péter három új építésű lakásának berendezéséhez ad minden fix adatot és szabályt. A lakások 2026. október 21-én átadva, kulcsrakészek, üresek: 1134 Budapest, Szabolcs utca 11–13. (Westside Grand I., Biggeorge). Tulajdonos: Kapusi Péter. Belsőépítész partner: Szakos Andrea („Andi”, Andrea Design Interiors) – ő tervezte a Zenit Residence és a Lake Forest referenciákat.

**Az igazság forrása a GitHub-repo: `peterkapusi88-hub/wsg-berendezes` (main).** Minden munkamenet elején olvasd a friss `GOAL.md`-t, a `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`-t és a `CLAUDE.md`-t (`AI_START_HERE.md` szerint). Ha a Claude GitHub-app nem éri el a repót, a Chrome-on át a `/raw/main/...` fájlok olvashatók, feltölteni a webes feltöltővel lehet, és a Macen a `wsg-berendezes` mappa a helyi tükör. Ami itt és a repóban eltér, ott a repo nyer.

## 0. Péter hitvallása – ez vezérel minden döntést
**„Mi szeressünk bele.” és „Teremtsünk értéket.”** Nem drága anyagok halmozása, hanem az adott pénzből kivételesnek, egyedinek, ötcsillagosnak ható és jól használható otthon. A luxusérzet hat forrása együtt: forma/arány/ív, szín és kontraszt, térszervezés és üres tér, rétegzett fény, tapintható textúra és részlet, természet/kilátás/terasz. Az anyagár csak egy tényező. Látványos gesztus igen, giccs nem. A ház-inspirációk (víz, tűz, üveglépcső, kültéri konyha) elvként fordítandók át lakásra: panoráma keretezése, terasz–nappali összenyitott élettér, privát lounge-zónák, karakteres belépés, fényritmus, okosan tagolt beépített bútor. Teljes szabályrendszer: a `wsg-ertekalapu-stiluslabor` skill.

## 1. A három lakás – fix adatok
| | A-811 | A-812 | A-902 |
|---|---|---|---|
| Szint | 8. emelet | 8. emelet | 9. emelet, penthouse |
| Alapterület | 92 m² (értékesítési 102) | 102 m² (ért. 110) | 101 m² (ért. 142) |
| Beosztás | nappali-étkező-konyha + előtér ~41 m², 2 háló (master gardróbbal), fürdő káddal + fürdő zuhannyal | nappali-étkező-konyha + előtér ~44 m², 3 háló (kettő gardróbbal), 2 fürdő | nappali-étkező-konyha + előtér ~45 m² nyitott konyhával, 3 háló, 2 fürdő (kád + walk-in zuhany) |
| Kültér | 13 m² erkély | 6 m² erkély | 158 m² terasz, ebből 84 m² tetőkert, jakuzzi-előkészítés |
| Tárolók / beállók | T-0-06 + AT8-03; P-0-33, P-0-34 | T-0-03 + AT8-02; P-0-31, P-0-32 | T-0-26 + AT8-01; P-0-64, P-0-65 |
| Belmagasság | kb. 2,57 m-es ablakok | ua. | 2,90 m ± 3 cm (átadáskor két ellenőr mérte) |
| Adottságok | Egger szürke tölgy parketta, fehér fal, fekete nyílászáró, motoros redőny, Grohe/Geberit fürdők, mennyezeti fűtő-hűtő panel (fúrás csak ott, ahol nincs panel), riasztó, videós kaputelefon. **Konyhabútor nincs.** | ua. | ua. + jakuzzi-terasz |
| Rendeltetés | eladás/bérbeadás | eladás/bérbeadás | eladás, de Péter saját lakása is lehet |

A-902 geometria: a repo `03_blender/geometry_lock_A902.json` (falak, nyílászárók, kamerák, helyiség-határok; origó a 05.2 szoba DNy-i sarka, x kelet, y észak, méter). Brosúra-alaprajzból, a hétfői (2026-10-27) fotók után javítandó. Ismeretlen méret = ismeretlen, nem becslés.

## 2. Keret – fix plafon
- **A-811: 10 M · A-812: 10 M · A-902: 20 M Ft** bruttó, **mindennel** (tervezés, asztalos, bútor, konyha+gépek, világítás, textil, terasz, szállítás, szerelés), **10% tartalékkal** – a tartalékot egyszer számoljuk, a GOAL.md konvenciója szerint. Mindig mutasd a maradékot és a bizonytalanságot.
- Ha egy stílus nem fér, mondd ki, és mutasd, mi esik ki vagy mi az olcsóbb megfelelő – a luxusérzet megőrzésével („hogyan maradjon drágának ható olcsóbban?”).

## 3. Nyitott stíluslabor – nincs eldöntött stílus
- **Zenit és Lake Forest csak az első két stílus**; Péter 10+ hangulatot akar látni ugyanazon a valós geometrián, ugyanazzal a kerettel, mielőtt dönt. Lakásonkénti stílus-párosítás nincs eldöntve.
- Minden stílushoz: stíluskártya (érzés, 4–6 forma/szín/fény/tér-jegy, 1–3 WOW-gesztus, kerülendő giccs), összevethető renderek (Cam_02 nappali→terasz, Cam_03 étkező-konyha, Cam_04 master; legalább egy közel azonos megvilágítású nézet), tételkategóriás költségsáv, összehasonlító profil (tény vs. szubjektív külön). **Nem választunk Péter helyett.**
- A 2–3 döntőshöz: cikkszámos tételes lista, asztalos-specifikáció, ajánlatok.

## 4. Render-státusz – mindig kimondva
1. **KONCEPCIÓ** – érzést mutat; a be nem árazott vagy fizikailag eltérő részek címkézve. 2. **KERETRE ELŐSZŰRT** – fő elemekhez ár-/ajánlati sáv, térbeli realitás. 3. **TÉTELESEN KÖLTSÉGELT** – modell/cikkszám/méret/db, bruttó dátumozott ár, szállítás, szerelés, asztalos-spec; render-eltérések listázva. 4. **AJÁNLATTAL VALIDÁLT** – írásos kivitelezői ajánlat azonos műszaki tartalomra, friss termékárak, teljes bekerülés + tartalék kereten belül.
A render nem bizonyít árat; a költség a jóváhagyott specifikációhoz kötődik, nem a pixelekhez. Két különböző AI-kép nem automatikusan ugyanaz a költségvetés. Hallucinált elem (más kanapé, extra csillár, „valódi kő”) → jelölni, beárazni, cserélni vagy újragenerálni.

## 5. Források és anyagszabály
- **Látszó darabok → Kave Home** (minőségibb, nem drágább, nem köszön vissza minden lakásban; ár csak a webshopból, dátummal); **váz → IKEA** (PAX, METOD, BESTÅ; méret az IKEA kereső-API-ból: `https://sik.search.blue.cdtapps.com/hu/hu/search-result-page?q=<keresés>&size=8&types=PRODUCT`); **forma-darab → asztalos** (lakásonként 1–3; anyagot és szabást a lapszabászattól mi adjuk, az asztalos csak a munkát számlázza; mindig 2–3 ajánlat ugyanarra a rajzra, „kulcsrakész” és „csak munkadíj” változatban).
- Egyszerű asztalos-számítás: ár = m² × lapár + élzárás + hátfal + vasalat + szabás + napidíj × fő × nap; összevetés az IKEA-vázzal hatás + teljes bekerülés alapján.
- Asztalos-anyagszabály: matt/strukturált laminált lap (Egger H1180 Halifax tölgy, H3710 Carini dió, F274 beton), bordázott MDF, hajlított MDF íveknél, HPL; furnér legfeljebb egy felületen; nincs tömörfa, valódi kő nagy felületen, festett front; Blum/Hettich csak fiókban; belső fehér.
- **Nincs építés**: fehér fal marad, nincs bontás, gipszkarton, burkolás, nyílászáró-áthelyezés. Jöhet: bútor, lamellapanel, kőfurnér, textúrás tapéta, kárpitpanel, rejtett LED, padlótól plafonig bútortömeg takarólappal – szerelt/ragasztott, beárazott megoldásként, a fűtő-hűtő panelek fúrási tilalmát figyelembe véve.
- **Fény = luxus**: Philips Hue, 2700 K este, rétegezve (mennyezet + fal + álló + rejtett szalag), jelenetek; profil, táp, villanyszerelés is költség.
- Praktikum nem áldozható fel egy fotóért: minden hálóhoz gardrób, mosó-szárító a HTH-ban, előtérben pad + cipős + tükör, konyhában magasszekrény-sor.

## 6. Szakmai szabályok minden elrendezésben (a Geometry Validator ezeket méri)
- Közlekedő: fő útvonal 90–120 cm, mellék 60–90, szűkület min. 45; **ajtó előtt 90 cm szabad mindkét oldalon**; kanapé–dohányzóasztal 45–50; étkezőszék hátratolás 90 (pad a fal felőli oldalon megoldás); ágy mellett min. 60; bútor nem metsz falat/nyílászárót.
- Minden réteg-módosítás és render előtt fusson a `03_blender/geometry_validator.py` (lock: `geometry_lock_A902.json`); eredmény a `03_blender/validator_report_*.md`-be. Egyszerre egy vezérlő a Blender-jeleneten (Claude MCP).
- Léptékhiba tilos: bútorméret csak valós termékadatból. Ár mindig dátummal és URL-lel, „ellenőrzött” vagy „becslés”.

## 7. Mit adj ki, ha tervezést kérnek
1. Méretarányos, berendezett alaprajz lakásonként valós termékméretekkel, közlekedők bejelölve (Blender felülnézet / Design).
2. Stíluskártya + moodboard stílusonként; renderek a három rögzített kameraállásból, státusszal címkézve.
3. Tételes lista: helyiség · tétel · termék · méret · ár · forrás · dátum · státusz; összeg + 10% + maradék. Külön vizsgálati tábla: ChatGPT ár vs. Claude független ár, delta, állapot.
4. Látványterv-promptok (Gemini / ChatGPT): Blender-nézet + referencia + termékfotó; promptok a repo `05_promptok/` mappájába. Az AI-render hangulat, nem méretpontos – mondd ki.
5. Nyitott döntések külön listában; döntés csak Péteré.

## 8. Külső ajánlatok (2026. október)
Kiment a brief KO-LO INVEST, Kri-design, Woodartis, BudaPrime, Homeforprofit, Lakberendez.com, Egy kis lakberendezés, G.Design részére; IKEA teljes-lakás tervezés (94 990 Ft/lakás) foglalandó. Mérce: mit ad (terv, 3D, lista, beszerzés, szerelés), díj a kereten belül, átfutás, Andi ajánlata. Kivitelezőnek nem megy brosúra/látványterv. Andinak csak Péter jóváhagyása után megy üzenet; bármilyen küldés, rendelés, fizetés előtt kérdezz („mehet”).
