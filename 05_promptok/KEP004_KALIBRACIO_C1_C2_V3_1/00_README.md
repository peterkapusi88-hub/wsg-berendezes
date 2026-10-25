# KEP-004 · C1 Zenit / C2 Lake Forest – közös kalibrációs promptok, V3.1 (végleges, 2026-10-25)

**Mire:** a WSG Design Challenge 2026 (A GPT-6 Astra · B Claude Fable 5.1 · C Claude Opus 5.5) közös mércéje. Péter döntése (2026-10-25 04:03, 04:27): versenyzőnként **60 saját prompt + e 6 közös kalibráció = 66 képes készlet**. A hat kalibrációt egyszer, Claude írta; a versenyzők nem írnak C1/C2 promptot, a 66 soros manifestjükben a 61–66. sor `KOZOS` státusszal erre a mappára mutat. Azonosítók: a regiszter 61–66. sora (`05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv`), kep_id betű szerint.

**Mit mutat:** a v1 Zenit- és Lake Forest-koncepció (`06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md`) újratervezve a valódi A-902 héjban, V3.1-szinten: minden látható tömör falnak terve van, Hue-fény, C elrendezés, valós termékek. **Szerep:** a kreatív minimum referenciája, nem versenyző. Nem helyettesíti az S06 Zenit Atelier és az S07 Lake Forest Couture teljes stílusát.

**Fény (Péter 04:40/04:49, a versenyblokk VB.3 pontja):** Cam_02 kék óra / kora este, prémium rétegzett Hue, a TV-fal a WOW-elem; Cam_04 este, Hue; Cam_11 nappal – a stílusképekkel azonos.

**Státusz:** `COMPLETE` kreatív prompt, `NEEDS_CLAUDE_VALIDATION` – nem futtatható csomag. A futtatható csomagot Claude a Blender-ellenőrzött FIXED/FRAME LAYOUT blokkokkal és az eredeti helyszíni referenciákkal építi, a stílusképekkel azonos kapukkal.

## Fájlok
| nr | kep_id | kamera | fény | karakter |
|---|---|---|---|---|
| 61 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | Cam_02 | kék óra / kora este, rétegzett Hue, TV-fal = WOW | 7 428 |
| 62 | `A902_C1_Zenit_3_master_Cam_04_A` | Cam_04 | este, Hue | 4 882 |
| 63 | `A902_C1_Zenit_3_master_Cam_11_A` | Cam_11 | nappal | 3 847 |
| 64 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | Cam_02 | kék óra / kora este, rétegzett Hue, TV-fal = WOW | 7 518 |
| 65 | `A902_C2_LakeForest_3_master_Cam_04_A` | Cam_04 | este, Hue | 5 112 |
| 66 | `A902_C2_LakeForest_3_master_Cam_11_A` | Cam_11 | nappal | 3 977 |

Mind a hat `20_PROMPTOK/<kep_id>.prompt.md`, `=== BEGIN PROMPT <kep_id> ===` / `=== END PROMPT <kep_id> ===` jelölőkkel; helykitöltő nincs.

## Közös tények a promptokban (forrás)
- **Kamerák és fény:** `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md` 3. pont; Cam_11 blokk: `05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md`.
- **Elrendezés C:** GEOMETRIA v2 1–2. pont – 160 × 90-es asztalhely az ML04 alatt, 2+2+1+1; a kanapé háttal keletre (háttámla ≤ x 6,67 L / 6,60 U), a hosszú ülés észak–déli, nyitott a TV felé.
- **Termékek:**
  - asztal: Westwing Toni ovális 160 × 90 (259 990 Ft, 2026-10-25), mindkét kalibrációban;
  - C1 kanapé: Kave Home Martina íves moduláris (287 cm; **mélysége termékadat nélkül nem igazolt** – ha 180 cm-nél mélyebb, tartalék a C-ben igazolt Westwing Lennon L 238 × 180);
  - C2 kanapé: Westwing Wolke L 258 × 167 (25WES29958, 1 050 000 Ft, 2026-10-24; az eredeti Lake Forest-kanapé). 2D-méretpróba a C-ben (`03_blender/geometry_v2/elrendezes_alt/wolke_c.py`, Toni 160-nal): háttámla x 6,65, kanapé–TV-bútor 0,91 m (40 cm-es) / 0,71 m (60 cm-es TV-bútorral), minden fő út ≥ 0,90, székkihúzás ≥ 0,90, ML04 0,10 – megfelel; a rövid szár a déli végen (a bal/jobb kivitel a termékoldalon ellenőrizendő); Blender-tömbkép az integrációnál. A mélyebb Gala U 300 × 225 a C-ben nem fér el;
  - a többi Kave Home-tétel (Corvena, Mosi, Eamy, Selven, Sylo, Sheffield, Ciselia, Brisia, Martina ágy) a `ai-coordination/inputs/A902_v2b/KOLTSEG_ELOSZURES_4STILUS_A902.md` 2026-10-24-i webshop-rekordjaiból; ahol a rekord nem ad méretet, a prompt sem ad;
  - a generikus tételek (ív-állólámpa, gyűrűlámpa, gömbcsillár, pouf, éjjelik, pad, Ø300 szőnyeg, gardróbfront) replika/analóg, `becslés` státusszal.
- **Gardróbfal 05.1:** `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md`.
- **Hue:** `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`; fajlagos árak: `ai-coordination/inputs/A902_verseny/HUE_ALAPCSOMAG_v1.md`.
- **Padló, nyílászárók, fürdő, terasz:** Render Reality Gate A. pont és a promptsablon v3.1 §1.

## Változásnapló
- A baseline-commitban (`45632b5`) lévő változathoz képest az előkészítő ágon (`competition/inditas-20261025`) eltávolítva a nem igazolt méretek és kivitelek: a Martina ülésmagassága, a Selven és a Martina ágy keretmérete, a Sylo szélessége, a Sheffield magassága, a „Mosi-style” fém éjjeli, a „Marely-type” Ø300 szőnyeg, a Wolke „bouclé” huzata és északi chaise-e, valamint a krém „FORSAND” front (ilyen IKEA-kivitel nem igazolt). **A képgeneráláskor ezt a tisztított változatot használjuk.**
- A v1 kalibrációs promptok (`05_promptok/KEP004_ChatGPT_Images_v1/`) „semleges borús fény, fehér falak, P902_24A” szabályát a V3.1 és a C elrendezés váltja; a v1 fájlok érintetlenek.

## Nyitott (Claude, integrációkor)
- A Martina íves kanapé mélysége a termékadatlapról.
- A Wolke bal/jobb kivitele és huzatválasztéka a termékoldalról.
- Az olvasólámpák betáplálása (D26/D20) a kiállás-CSV-vel egyeztetendő.
