# A-902 Cam_03 K1 – a BiBo U-konyha Blender-ellenőrzése · **NEM BEFEJEZETT** (2026-10-25 08:50)

**Mi volt a cél:** megállapítani, megépíthető-e a ChatGPT által generált S02 BiBo konyhakép elrendezése, amelyet Péter 08:19-kor elfogadott (`renders/fable51-v3-1-22-tests`: `A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A__FABLE51_V3_1__v1.png`). Péter döntése (08:26): a hűtő „kb. úgy legyen, ahogy a BiBo-konyhában”, vagyis oszlopként a W03-a előtt.

**Állapot:** a renderek és a validátorfutások elkészültek; a tételes elemzés, az ítélet és a hűtőjavaslat **még nincs meg**. Az ellenőrzést végző munkafolyamatot Péter leállította. Az eredményeket változtatás nélkül mentettem.

## Mi készült el
Blender 5.2.3, háttérfolyamatként, a blend MÁSOLATÁN (`WSG_A902_v2b1k13_MASOLAT_cam12v3_korrekcio.blend`, lock: `geometry_lock_A902_v2b.json`). Az eredeti blend, a lock és az élő Blender-fájl érintetlen.

**Renderek** (`04_renderek/A902_cam03_bibo_u_ellenorzes/`):
- `A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_KORR_semleges.png` – új, olvashatóbb semleges Cam_03 K1 alapkép;
- `A902_S02_Cam03K1_BIBO_U_tombrender.png`, `A902_S02_Cam03K1_BIBO_A_tombrender.png` – két tömbváltozat (U = a BiBo-kép szerinti U-alak; A = a Fable-prompt szerinti alap);
- `A902_S02_konyha_BIBO_{ures,U,A}_felulnezet.png` – felülnézetek.

**Validátor** (`naplok/validator_cam03bibo_*.json`):

| Változat | Eredmény |
|---|---|
| üres | PASS – 0 hiba, 0 figyelmeztetés |
| U (BiBo-kép) | FAIL – 11 hiba, 13 figyelmeztetés |
| A (Fable-alap) | FAIL – 9 hiba, 15 figyelmeztetés |

**Figyelem:** a hibákat még senki nem nézte át egyenként. Az előző, Cam_12-es körben a validátor a fal túloldalán lévő kiállásokat is téves riasztásként jelezte (S08, S02, T04, K20). A FAIL tehát ellenőrizetlen.

**Szkriptek** (`03_blender/geometry_v2/cam03_bibo_ellenorzes/`): `bibo_spec.py` (tömbméretek), `11_render_cam03_bibo.py`, `12_utak_kialllasok_bibo.py`, `utak_kiallasok_bibo.json`. A futási napló: `naplok/bibo.log`, `naplok/cam03_bibo_log.json`.

## Mi hiányzik (következő lépés a folytatáskor)
1. A 11 és 9 validátorhiba tételes szétválogatása: valós vagy téves riasztás.
2. A pultsorok közötti szabad szélesség, a 05.3 ajtó felé maradó út (cél ≥ 0,90 m), a sarokszekrény és a géposzlop–pillér viszonya.
3. Kiállások: K07–K09, D12, FL01, mosogató- és elszívóbekötés, a talált mennyezeti csőcsonk (MODEL SOURCE ERROR, hétfőn mérendő).
4. Ítélet (MEGÉPÍTHETŐ / FELTÉTELESEN / NEM) és a hűtőoszlop megoldása Péter döntése szerint (kapcsolóáthelyezés mérettel vagy keskenyebb oszlop).
5. Összevetés a ChatGPT BiBo-képpel (áttűnés/élkép).

A Mac-másolat: `~/Downloads/WSG_CAM12_V3_KORREKCIO/bibo/`. Semmi nem lett törölve.
