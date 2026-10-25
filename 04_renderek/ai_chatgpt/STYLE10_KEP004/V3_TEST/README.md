# KEP-004 · V3_TEST – két Cam_02 tesztkép (A-902, nappali–terasz), ChatGPT Images, r2-csomag

**Jóváhagyás (Péter):**
- 2026-10-25 01:55 CEST: V3 azonnali képteszt.
- 02:22 CEST: „1. opció” – ez a munkamenet az egyetlen felelős; **pontosan két generálás, képenként egy**.
- Újragenerálás nem volt, további kép nem készült.

| Kép | Prompt | Generálva | Átvételi név | sha256 | Gate |
|---|---|---|---|---|---|
| `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_TEST.png` (1586×992) | `…_V3_TEST.prompt.txt` (KEP004-CGI-V3TEST-r2, `eb4f1908…`) | 2026-10-25, letöltés 02:35:31 CEST | Modern Nappali Terasszal és Városi Kilátással.png | `2fd2bd787fb7465f82a92d7dd4f858957fe2929559b9035aab94a712aa3b4f8a` | `KONCEPCIÓ – NEM VALIDÁLT`; geometriai kontroll **FAIL** (belmagasság ~+8 %, a falbútorok nagyobbak), javítható |
| `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_TEST.png` (1586×992) | `…_V3_TEST.prompt.txt` (KEP004-CGI-V3TEST-r2, `aea9d602…`) | 2026-10-25, letöltés 02:38:54 CEST | Modern nappali terasszal és városi panorámával.png | `e580f2fda62a44f634b49e75b35fcf653cada18d6d79e20f684381246b82a4f4` | `KONCEPCIÓ – NEM VALIDÁLT`; Gate **`ELŐSZŰRT – FELTÉTELES`**: a héj ±1 %-on belül; a falbútorok magassága és az étkező helye javítandó |

**Futtatás:**
- Chatek: S01 https://chatgpt.com/c/6add4e63-b7c4-83ed-aefc-821359a091f3 · S02 https://chatgpt.com/c/6add4f5c-edf0-83eb-ba22-703be2d0c91b
- Felület: ChatGPT Plus · Chat mód · „Kép létrehozása” · erőfeszítés: Erős (High). Claude in Chrome, Péter böngészője.
- Bemenetek (9 kép képenként, sha256-tal): `archiv_manifest_V3_TEST.json`. Integráció és r1 → r2 változtatások: `05_promptok/KEP004_ChatGPT_Images_V3_TEST/INTEGRACIO_V3_TEST.md`.

**Gate-audit:** `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`. Bizonyítékok: `_gate_V3TEST/`:
- vetítés: `alap_vetitett_ellenorzes.jpg`, `S0x_V3TEST_vetitett_atfedes.jpg`;
- átfedések: `S0x_V3TEST_blend50_alapkep.jpg`, `S0x_V3TEST_elatfedes_alap_piros_tomeg_cian.jpg`;
- összevetések: `S0x_V3TEST_geometriai_osszevetes.jpg`, `V3TEST_kreativ_osszevetes.jpg`;
- részletek: `S0x_V3TEST_reszletek.jpg`;
- kontrollpontok: `kp1`–`kp6`, `kontrollpontok_meres.json`.

**Kapcsolódó képek – nem a 02:22-es tesztpár:**
- A másik munkamenet Péter 02:06-os „mehet”-jére a régi r1-csomaggal két `_V3_r1` képet készített. Helyük: `../CREATIVE_UPGRADE_V3/`, auditjuk: `WSG-20261025-KEP-004_V3teszt_r1.md`.
- Itt A/B-referenciák.
- A V2-es első próbakép (`../A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A.png`) változatlan.
