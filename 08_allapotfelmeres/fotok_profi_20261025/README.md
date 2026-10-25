# Profi helyszíni fotók – 2026-10-25 (teljes felbontás)

**Forrás:** Péter Macje, `~/Downloads/ADÉL_SZABOLCS_UTCA_ANYAGOK_NEW/` (fotós exportja, `KZS_*` nevek). Feltöltve 2026-10-25, Claude.
**Felbontás:** a fotós teljes felbontású JPG-exportja, változatlanul (kb. 8200×5500 px, 4–21 MB/kép). A fotós által adott 2200 px-es „kis fájlok” nem kerültek fel; a párosításuk a leltárban (`kis_valtozat_neve`).

| Mappa | Darab | Tartalom |
|---|---|---|
| `A811/` | 27 | A-811 lakás |
| `A812/` | 23 | A-812 lakás |
| `A902/` | 33 | A-902 lakás + terasz, zöldtető, panoráma, 9. emeleti közös folyosó, belső kert felülről |
| `KULSO_homlokzat_kozter_garazs/` | 19 | lobby, postaláda-fal, lépcsőház, mélygarázs, belső kert, utcai homlokzatok |
| `_kontaktlapok/` | 4 | áttekintő lapok (bélyegkép + fájlnév) – AI-knak és gyors böngészéshez |
| `LELTAR_profi_20261025.csv` | 102 sor | fájl, pixelméret, képarány, MB, sha256 (16 jegy), kitöltendő: helyiségkód, irány, Blender-kamera |

## Státusz és használati szabály (Render Reality Gate szerint)
- **Bizonyíték, nem méretforrás.** Falak, helyiségméretek: a méretezett megvalósulási alaprajz az elsődleges. A fotóból nyílás, anyag, szín, fény, panoráma, terasz és terveltérés ellenőrizhető.
- **Nincs EXIF** (dátum, gyújtótáv, objektív le van vágva) → a kamerapozíció és látószög csak becsülhető (pl. fPerspective-illesztés a Blender-modellhez).
- **Retusált / vágott export:** eltérő pixelméretek, függőlegesek valószínűleg korrigálva; `-Edit` = külön retusált kép; `…x.jpg` = ugyanannak a felvételnek 16:9-es kivágása. Torzítás és retus miatt ezekből mérni nem szabad.
- Szín: a profi fotó a legjobb elérhető forrás a padló (szürke tölgy hatású parketta), falfehér, ajtó, burkolatok tényleges tónusára, de fehéregyensúly-/expozíció-módosítás lehet rajta → színmintát több képről és lehetőleg helyszíni referenciával vegyünk.
- Garázsképeken harmadik fél autói (rendszám) látszhatnak: belső munkaanyag, külső publikálásra nem.

## Helyiség-hozzárendelés (2026-10-25, Claude, az 1:50-es méretezett alaprajzok alapján)
A `LELTAR_profi_20261025.csv` minden sorában: `helyiseg_kod` (a `FOTO_BEVITEL.md` kódjai; közös terek: `KOZOS_…`, `KULSO_…`), `irany` (mit lát a kamera, tájékozódási ponttal), `bizonyossag` (magas / közepes), `latvanyterv_kamera_prioritas` (1 = elsődleges nézet a későbbi látványtervekhez). A fájlneveket nem írtuk át (a fotós `KZS_` neve a visszakereshető azonosító). Összesen 102 kép, ebből 23 elsődleges látványterv-kamera.

Fotókamerás látványterv-munkamenet: `FOTOKAMERA_LATVANYTERV.md`.

## Következő lépés
1. Blender-kamerák illesztése (`Cam_F_<KZS-szám>`) az 1. prioritású képekhez, padló/fal/ajtó színminták.
2. Összekötés a `FOTO_KAMERA_KAPCSOLAT.csv` tervezett felvételeivel; a hiányzó nézetek listája.
3. Helyiségenkénti reality card a promptokhoz és a rendelési specifikációhoz.
