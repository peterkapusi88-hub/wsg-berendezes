# A-902 – Astra kreatív inputcsomag v1.1 (2026-10-24, rövid delta)

**Státusz: ELŐKÉSZÍTVE – NINCS ELINDÍTVA.** PR #1 inaktív. Ez a v1.1 a v1 (`../A902_v1/`) **mellé** kerül, nem írja felül. Új stílust nem véglegesít, képgenerálást nem rendel. Az állapotcsomag (hétfő) után v2 jön.

## Mi változott a v1-hez képest (TÉNY, nem stílus)
1. **Parketta: Egger Grey Treviso Oak EL2184** (Classic 8/32 4V Aqua+). Dokumentumból IGAZOLT, fotóval még nem. A renderben ez a padló: hideg-semleges szürke tölgy, nem meleg „light oak”. Az A-811/812 parkettája ettől eltér: Grey Soria Oak EL2065.
2. **Belmagasság 2,90 m:** IGAZOLT (Péter).
3. **A terasz nem sík.** Négy zóna (`03_blender/geometry_v2/`, `02_referenciak/A902_helyszin/`):
   - **greslap** a két üvegfal előtt, a belső padló alatt kb. 15 cm-rel (23,62 + 19,34 m²);
   - **emelt WPC-dobogó** +62 cm-rel, középső sávval, harántsávval, 2 × 3 fokkal, északi pihenővel (25,00 m²);
   - **zöldtető** 71,18 m²: szélein sík fű esőztetővel, középen enyhén dombos évelőágyás virágokkal, mulccsal és kavicssávval, **térdmagas betonszegéllyel**;
   - **korlát** (antracit pálcás) és **panorámapontok**.
   **Ezeket nem kell kitalálni vagy megépíteni, már léteznek.** A render ezt a valódi tetőkertet mutassa, ne egy általános luxusteraszt.
4. **Zöldtető:** a terv nem jelöli „nem járható”-nak. Könnyű, szabadon álló bútor mehet rá; koncentrált nagy teher (jakuzzi, nagy dézsa, kőasztal) csak igazolt terhelhetőséggel. A terasz burkolata, a korlát és a teraszfalak a műszaki melléklet szerint **közös részek**, ezért rögzítés és fúrás nélkül tervezünk. Jakuzzi csak a jelölt nyugati greslap-helyre kerülhet, és ott is csak statikai igazolás után.
5. **Kilátás:** csak a helyszíni videókból (`terasz_video_2026-10-21/`, panoráma v0/v0b): Budai hegyek villanegyeddel és városi tetőtáj. Generikus Budapest-panoráma tilos. A daru ideiglenes, elhagyható, de ezt jelölni kell.
6. **Meglévő felületek fotóval** (műszaki ellenőri képek, `08_allapotfelmeres/fotok/A902/`, összefoglaló: `MUSZAKI_ELLENORI_ANYAG_KIVONAT_2026-10-21.md`):
   - hűvös szürke, csomós tölgy parketta (a konyhában is) és fehér fal;
   - világosszürke ajtók fekete kilinccsel;
   - nyílászárók kívül antracit, belül fehér;
   - fürdők világos meleg szürke kőhatású lappal és fekete szerelvényekkel;
   - a teraszajtók sötét antracit téglás kávában, a fő homlokzat világos foltos tégla.
   - Belmagasság: mérve 2,90–2,93 m.
7. **Kültér:** `08_allapotfelmeres/KULTER_KINEZET_3_LAKAS.md` – greslap, WPC, vakolt mellvéd, pálcás korlát, világos és sötét tégla, fekete fali lámpák; teraszbútor csak greslapon és WPC-n, súlyozott, fúrás nélkül.
8. A belső falak a tervhez képest ±15 cm-en belül vannak (`A902_eltereslista_v1_v2.md`). A belső nézetek (Cam_02–04) használhatók; a **Cam_05 terasznézet elavult**.

## Képek
| Fájl | Mire |
|---|---|
| `04_renderek/terasz_v2_geometria/A902_terasz-v2_07/08/09*.jpg` | a terasz geometriai alapja: szintek, zónák (ELŐZETES, nem stíluskép) |
| `02_referenciak/A902_helyszin/terasz_video_2026-10-21/kulcskockak/*` | anyagok, szegélyek, korlát, homlokzat, kilátás – valós |
| `02_referenciak/A902_helyszin/kert_video_IMG2498_2026-10-21/*` | zöldtető: sík fű, domb, ágyás, szegély, öntözés |
| `01_alaprajzok/terv_kivonat_2026-10-24/A902_*` | méretezett alaprajz és megvalósulási terv (kivágat) |
| `04_renderek/semleges/*` (Cam_02–04) | belső geometria-alap, változatlanul |

## Kreatív kérdés Astrának (a v1 kérés-tervezetében a terasz helyett)
**Hogyan lesz a meglévő, többszintű tetőkertből „elképesztően drága” élmény új burkolat és építés nélkül?**
- Ülőzónák a szintek és a panoráma szerint.
- Fény a meglévő szegélyeken és lépcsőkön, rögzítés fúrás és szigetelésáttörés nélkül.
- Bútor csak greslapon és WPC-n.
- Minden javaslathoz anyag, ársáv, és hogy melyik költségsorból (13c–e) jön a pénz.
