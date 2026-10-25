# Látványterv a profi fotó kamerájából – munkamenet (v1, 2026-10-25)

**Péter kérése (2026-10-25 19:17):** a későbbi látványterveket a profi fotók nézőpontjából kérjük, így a valós kép minősége, színei, méretei, anyagai és geometriája közvetlenül felhasználható.

**Claude értékelése:** ez a legerősebb út a hitelességhez. Az üres fotón minden fix elem (padló, falfehér, ajtó, ablakkeret, fény, kilátás, arány) valós, így a képen csak az **új** elemeket kell létrehozni, a régit nem kell AI-val „kitaláltatni”. Három korlát van, ezeket kezelni kell:
1. **Az AI a fotón is elmozdíthat valamit** (ajtót, ablakosztást, padlótónust, kilátást). Ellenszer: maszk (csak a bútor területe módosulhat) + utólagos összevetés az üres fotóval a maszkon kívül.
2. **A bútor mérete a fotón nem garantált.** Ellenszer: Blender-kameraillesztés a fotóhoz (ismert méretekből: ajtó 0,90×2,10, belmagasság ~2,90, üvegfalak a tervből), majd a Blender bútorréteg ugyanabból a kamerából renderelve **méretvezető** (doboz/clay + mélység/él) az AI-nak.
3. **A fotó retusált és vágott, EXIF nélkül.** A függőlegesek korrigálva vannak (eltolt optikai tengely), a látószöget becsülni kell → a kameraillesztés lens shifttel készül, és a maradék hibát a validátor-riportba írjuk.

## Három szint (a Render Reality Gate státuszaival)
| Szint | Mi készül | Státusz |
|---|---|---|
| A – gyors | üres fotó + valós termékfotók → AI berendezés maszkkal (MeltFlex furniture / Gemini / Astra), a maszkon kívül tilos a változtatás | KONCEPCIÓ |
| B – mérethelyes | Blender-kamera a fotóhoz illesztve, a bútorréteg renderje ugyanabból a nézetből méretvezetőként; AI erre komponál; eltéréskép (fotó vs. eredmény a maszkon kívül) | ELŐSZŰRT |
| C – validált | B + valós cikkszám, méret, bruttó ár, reality card helyiségenként | PASS / FAIL |

## Javasolt kamerák (leltár: `latvanyterv_kamera_prioritas = 1`)
- **A-902:** 3726 étkező → teraszüveg · 3659 nappali → Ny · 3695 nappali → D (TV-irány) · 3708 étkező → 05.3 / konyha · 3599 05.3 → terasz · 3741, 3753 05.1 master · 3789 05.2 · terasz: 3488 greslap, 3498 zöldtető → homlokzat.
- **A-811:** 3449, 4101 nappali → üvegfal · 4122 → TV-blokkos fal · 4148 étkező → bejárat/konyha · 3275 05.1 · 3304 05-23.
- **A-812:** 3065 nappali → üvegfal · 3103 → déli (TV) fal · 3104 → bejárat/konyha · 3132 05.1 · 3141 05.2 · 3206, 3235 05.3.
- A meglévő Blender-kamerák (A-902 Cam_02/03/04) **nem** azonosak ezekkel a nézőpontokkal; a fotókamerák új, `Cam_F_<KZS-szám>` nevű kamerák lesznek, a régieket nem írjuk felül.

## Megfigyelések a fotókról (ellenőrizendő, nem döntés)
- **Parkettatónus:** A-902-ben hűvös szürke (megfelel az Egger Grey Treviso Oak EL2184-nek). Az A-811 és az A-812 fotóin érezhetően melegebb, barnább; a terv szerint mindkettőben Grey Soria Oak EL2065. Ez lehet fehéregyensúly vagy valós dekoreltérés → helyszíni színminta / termékazonosítás kell, mielőtt a fotó színét a rendelés referenciájának vesszük.
- **A-812:** a 06.1 HTH-ról és külön a konyháról nincs kép; a konyha és az előtér csak a nappaliból látszik (3104).
- **A-902 terasz:** a keleti greslapról (10) nincs biztosan azonosítható kép; a 3483 Ny/K besorolása közepes biztonságú.
- **Garázsképek:** harmadik fél rendszámai látszanak – külső publikálásra nem.

## Következő lépés (Péter döntése kell)
1 pilot kép az A szinten (javaslat: A-902 3726, étkező → terasz), ezen kipróbáljuk a maszkos berendezést és az eltérés-ellenőrzést, mielőtt AI-keretet költünk a többire. Utána B szint: kameraillesztés a kiválasztott 1. prioritású nézetekre.
