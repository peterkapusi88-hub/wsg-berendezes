# A-902 – közös geometriai és fénybemenet a tervversenyhez (v2, Claude, 2026-10-25 04:50 CET)

**Kinek:** Astra, Fable és Opus – mindhárom versenyzőnek szó szerint azonos.
- Helye: a draft PR #20 (`kep004/kameracsomag-C-K1`).
- A közös versenybaseline-ba a párhuzamos Claude-munkamenet emeli be (Péter, 04:49).

**Forrás:**
- Péter 04:08, 04:39 és 04:40 CET (GOAL 7.);
- kameracsomag C: draft PR #20, `ai-coordination/results/WSG-20261025-A902-KAMERACSOMAG-C_r1.md`;
- kerek asztalos próba: `03_blender/geometry_v2/elrendezes_C/c_kerek*.py` és `cam12_C/05_kerek_meretproba.py` (PR #20).

**Felülírja** a v1-et (`GEOMETRIA_C_KAMERACSOMAG_v1.md`).

**Státusz:** terv szerinti geometria, helyszínen nem mért. A kamerák javaslat státuszúak, amíg a PR #20-at Péter be nem olvasztja.

**Elv (Péter):** maximális kreatív szabadság a valódi lakásban.
- Ami alább kötött, az használati vagy építészeti tény.
- Ami kamerából vagy próbatömbből ered, azt ilyennek jelöljük, és nem korlátozza a tervet.
- A régi Blender-bútortömbök nem korlátok.

## 1. Kötött (használat, építészet)
| Mi | Érték |
|---|---|
| Közlekedés | fő utak ≥ 0,90 m betolt székkel (terasz, konyha, hálók folyosója, 05.3 ajtó); székkihúzás ≥ 0,90 m; kanapé legközelebbi pontja – TV-fal bútora ≥ 0,60 m |
| Kanapé | minimum L, inkább U (íves csak puffal L/U-ként). A háttámla keletre, az étkező felé néz; a hosszú ülés észak–déli irányú, nyitott a TV-fal (nyugat) felé. A háttámla legkeletebbi helye: x 6,67 (L) / 6,60 (U). |
| TV-fal (W01, x 3,67) | zárt szekrénytest legfeljebb 60 cm mély – **lehetőség, nem kötelező mélység**; ≤ 4 cm-es panel mehet a mennyezetig. A TV a falsíkon vagy a fülke hátfalán (képernyő x ≈ 3,77). Ha egy 60 cm-es szekrény elejére kerülne, a nézőtáv 2,0 m alá esne. |
| TV-tengely, szerviz | a TV-csatlakozók (G01–G04, D16, D17, G08) y 6,11–6,44 között; D18 y 4,75. Elöttük kivehető vagy szellőző hátfal, szervizkivágás. |
| Mennyezet | hűtő-fűtő mezőkbe nem fúrunk; fény csak meglévő kiállásról (ML04, ML05, FL01, FL02, D-pontok) |
| Függöny | sín a szemöldök belső síkján vagy a kávában (a mélység hétfőn mérendő) |

## 2. Étkező – jóváhagyott alapváltozat és nyitott formák
- **Alapváltozat (jóváhagyva):** hosszanti asztal, 160 × 90-es befoglaló (x 8,00–8,90; y 5,40–7,00) az ML04 alatt, hat hely 2+2+1+1 (oldalszékek tengelye y 6,10 és 6,70). Mindkét kanapéval és 40–60 cm-es TV-fallal is minden kötelező méret teljesül; a kihúzás behúzott függönnyel is ≥ 0,93 m.
  - **S01-alap:** Westwing Toni ovális 160 × 90 (259 990 Ft, 2026-10-25).
  - **S02:** az Anouk 180 nem elfogadott (a kihúzás függönnyel 0,78 m). 160 × 90-es hatszemélyes asztal kell; jelöltek a PR #20 eredményfájljában.
- **Más forma (kerek, ovális, egyéb):** nem tiltott, de minden eltérő forma és méret külön méretpróbát igényel. Igazolásig a státusza „elrendezésben ellenőrizendő”.
  - A 2026-10-25-i kerek próba: 2D, majd Blender-tömb, validátor PASS; a függönysáv benne van.
  - A párhuzamos munkamenet 2D-eredménye (`ai-coordination/results/WSG-20261025-A902-ELRENDEZES-C-KEREK-ASZTAL_r1.md`, PR #19) ugyanerre jut: Ø120–130 legfeljebb 40 cm-es TV-bútorral; Ø150 csak kompromisszummal.

| Kerek asztal | Feltétel | Fő utak, betolt székkel | ML04 a középtől |
|---|---|---|---|
| Ø150 (pl. Kave Home Nealy, 6 fő) | **csak sík TV-fallal** (≤ 4 cm) és a kanapé legnyugatibb helyén (L: háttámla x 6,11; U: 5,91) | ≥ 0,90 | 0,31 (L) / 0,41 (U) – a függeszték oldalt lóg |
| Ø140 | sík TV-fal, kanapé nyugaton | ≥ 0,90 | 0,31–0,41 |
| Ø130 | 40 cm-es TV-bútor, U-kanapé (háttámla x 6,27) | ≥ 0,90 | 0,21 |
| Ø150 | 40 vagy 60 cm-es TV-bútorral | **nem fér el** (05.3 felé 0,60–0,80) | – |

  **Következmény:**
  - A kerek asztal a TV-fal mélységét és a kanapé helyét is meghatározza, és a függeszték nem kerül középre: az ML04 helye fix, a mennyezetbe nem fúrunk.
  - A nyugatabbra tolt kanapé a Cam_12 előterébe kerül (3. pont).
  - Ezt a kompromisszumot a tervben ki kell mondani.

## 3. Kamerák és fény (Péter 04:40 – mindhárom versenyzőnek kötelező)
A kamerák geometriája és a `kep_id`-k változatlanok, csak a fény cserélődött a Cam_02 és a Cam_12 között.

| Kamera | Hely [x; y; z], irány, optika | Fény | Szerep |
|---|---|---|---|
| **Cam_02** nappali–terasz | [8,30; 4,40; 1,55], északnyugat, 20 mm | **kék óra / kora este, prémium rétegzett Hue** (2200–2700 K, RGB nélkül) | a TV-fal mint fő WOW-elem: a rejtett LED-ek és textúrák itt érvényesülnek; a terasz és a külső látvány felismerhető |
| **Cam_12** nappali hero v3 | [4,40; 7,88; 1,60], θ −48°, vízszintes, 22 mm, shift_y −0,05 | **nappal**, természetes, világos luxusenteriőr-fotó | a nappali–étkező–konyha, a W02/W07, a bútorok és anyagok összehasonlító nézete |
| Cam_03 K1 | [9,45; 7,55; 1,50], dél, 20 mm, shift_y −0,08 | nappal | konyha: a pultsorok, a hűtőoszlop, a magas elemek |
| Cam_04 master | lock szerint | este, Hue | – |
| Cam_11 master panoráma | lock szerint | nappal, panoráma | – |
| Cam_10 fürdő 06.2 | lock szerint | csak műfény | – |

- **Cam_02 esti kép:**
  - ne legyen túl sötét vagy túl kontrasztos: közepes expozíció, nincs bebukó fekete és kiégett fény;
  - a falélek, a nyílások, a padló–fal vonal, a teraszburkolat, a korlát és a zöldtető olvasható marad;
  - a LED profilból, egyenletesen világít (nem pontsoros);
  - fény csak a megnevezett lámpatestekből jön.
- **A Cam_12 v3 nem kreatív korlát.**
  - A kamera x 4,40-en áll, így a TV-fal (x ≤ 4,27) semmilyen eleme nem takarja ki: a fal a kamera mögött, a képen kívül esik.
  - A TV-fal északi vége is szabadon tervezhető, mennyezetig érő szekrénnyel is.
  - Közös összehasonlító kameraként csak a kamera állóhelyét (x 4,30–4,50; y 7,75–8,05) kell szabadon hagyni.
  - Ha egy terv oda vagy a kép előterébe erős, kivitelezhető elemet tesz (például kerek asztal miatt nyugatabbra tolt kanapé, magas elem a sarokban), Claude alternatív hero kamerát vizsgál, és megmutatja a kompromisszumot. Az enteriőrt nem butítjuk le a kép kedvéért.
- **A semleges Blender-alapképek** változatlanok, ezek a geometriai kontroll.

## 4. Feltételes – hétfőn (2026-10-26) a helyszínen ellenőrizendő, addig nem igazolt
**Teraszajtó.** A hat ülőhely és a terasz egyidejű használata nem igazolt, amíg nem tudjuk, melyik szárny nyílik.
- **Ha a középső szárny nyílik:** az alapváltozat rendben (az út 0,95–1,00 m).
- **Ha csak a legkeletibb, 0,93 m-es szárny nyílik:** a vizsgált hatszemélyes változatok közül egyik sem tartja meg egyszerre a terasz elérését és minden fő utat (`c_keleti_szarny.py`, 96 eset).
  - **3+3 asztal (180 × 90):** a terasz 0,95–1,00 m, de a 05.3 felé csak 0,65–0,70 m.
  - **2+2+1+1, az északi végszékkel:** a terasz 0,60–0,75 m.
  - **5+1** (az északi végszék alkalmi pótszék): minden út ≥ 0,90 m.
  - Ez külön jelölt kompromisszum, nem elfogadott végállapot. További lehetőség: bővíthető asztal (például Kave Home Kesia 160 (220) × 90), alaphelyzetben öt hellyel.

Szintén hétfőn mérendő:
- a káva mélysége;
- a TV-csatlakozók helye;
- a parketta dekorja (NEM IGAZOLT).

