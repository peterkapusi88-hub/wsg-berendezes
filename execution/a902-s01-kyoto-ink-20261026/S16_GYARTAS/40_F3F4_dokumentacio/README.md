# S16 R15 médiafal – F3–F4: műhelyi dokumentáció

Készült: 2026-10-30, Claude. Státusz: **TERVI – NEM GYÁRTÁSI KIADÁS.** Egy adatforrásból (`parts_v1.json` + `vasalat_terv.json`) generálva: `python3 f34_dokumentacio.py`.

| Fájl | Tartalom |
|---|---|
| `S16_R15B_szabasjegyzek.xlsx` | Szabásjegyzék (129 sor: kész / élzárás előtti / nyers méret, E1–E4 él, szálirány, A oldal, furatszám, MPR-név, m² és élzáró fm képlettel), Anyag-összesítő (SUMIFS, táblaszám-becslés), Vasalat, Furatok (295), Nyitott és jelmagyarázat. LibreOffice-újraszámolás: 0 képlethiba. |
| `S16_R15B_alkatreszlapok.pdf` | 129 A4 lap: kontúr/kivágás, A-oldali (teli), B-oldali (szaggatott) és élfuratok, élzárás színkóddal, 0,0 ütköző (E1+E4), szálirány, befoglaló méret, furattábla, pecsét. Blokkolós alkatrész piros jelzéssel. |
| `dxf_alkatreszek/` | 129 DXF (KONTUR, KIVAGAS, FURAT_A/B/EL, ELZARAS, MERET, SZOVEG réteg). |
| `S16_R15B_cimkek.pdf` | 129 db 100×50 mm matrica, Code128 = címke-ID (woodScan-hez az MPR-név alapja). |
| `mpr_tervezet/` | 31 woodWOP MPR TERVEZET (`<címke>_A.mpr` / `_B.mpr`), csak furatok (<102 BohrVert>, <103 BohrHoriz>), tiltott kulcs nélkül (az R16 tervezetek `??` hibája itt nincs). |
| `dokumentacio_qa.md` | Visszaolvasó egyezés: vasalatterv = MPR = Excel = PDF = DXF (295 furat, 129 alkatrész) – MINDEN EGYEZIK. |

Gépi konvenció (javaslat, az asztalos minta-MPR-jéig): X = U (hossz), Y = V, A oldal felül, 0,0 = E1+E4 sarok; B program a darab U tengely körüli átfordításával (Y = W − v). Élfurat az A programban, ZA a lap alsó síkjától.

**Nem gépre kész:** kontúrmarás nincs (szerszámtábla kell), a fiók-sín és TIP-ON furatképe a végleges termék után jön, a T-DOOR-L (bal toronyajtó) pántja BLOKKOLÓ – döntés kell. A gépi futtathatóságot csak woodWOP-szimuláció és próbadarab igazolja.

## R15B / v4 (2026-10-30 este)

- Bal toronyajtó pántolható (R15B, `10_F1_adatmodell/r15b_patch.py`): 11 pánt (6+5) Blum 70T3750 + 177H3100E, 0 blokkoló; 325 furat.
- Excel: új oszlop „Élkód (asztalos-sorrend)” és „DWG réteg-azonosító” (#szám a DWG rétegnevéből).
- Paraméterezve: `WSG_GYARTAS=../../R16_GYARTAS python3 f34_dokumentacio.py` → R16 (106 alkatrész, 956 furat, átmenő furat ATMENO jelöléssel).
