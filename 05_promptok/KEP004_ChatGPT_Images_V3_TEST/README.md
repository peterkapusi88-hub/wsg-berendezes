# KEP-004 · ChatGPT Images · V3_TEST (r2-csomag) – S01 Kyoto Ink és S02 BiBo Nocturne, Cam_02

**Állapot (2026-10-25):** mindkét prompt **lefutott**, képenként egy generálással (Péter, 01:55 és 02:22 CEST).

| Kép | Állapot |
|---|---|
| S01 | `KONCEPCIÓ – NEM VALIDÁLT`; Gate: a geometriai kontroll FAIL (belmagasság ~+8 %) |
| S02 | `KONCEPCIÓ – NEM VALIDÁLT`; Gate: `ELŐSZŰRT – FELTÉTELES` (a héj ±1 %-on belül) |

Audit: `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`. Képek: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/`.

| Fájl | Mi |
|---|---|
| `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_TEST.prompt.txt` | a futtatott S01-prompt (KEP004-CGI-V3TEST-r2), `eb4f1908…` |
| `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_TEST.prompt.txt` | a futtatott S02-prompt, `aea9d602…` |
| `INTEGRACIO_V3_TEST.md` | források; generálás előtti ellenőrzés (V3-méretek, tömbkép, validátor, tükör, pad, fájlazonosság); az r1 → r2 változtatások és okuk |
| `*_r1_r2.diff`, `epites_r2_naplo.json` | a változtatások pontosan, tiltó- és kötelezőlista-ellenőrzéssel |
| `_eszkozok/epito_r2.py` | az r2-csomag építője (az r1-promptból, pontos cserékkel) |
| `_eszkozok/gate_atfedes.py`, `osszevetes_lapok.py`, `reszlet_lap.py`, `kontrollpont_lapok.py` | a Gate-audit vetítési és mérőeszközei |

**Kapcsolódó csomag:** `../KEP004_ChatGPT_Images_V3_teszt/` – a másik munkamenet r1-csomagja, ebből épült az r2. Ezzel 02:18-kor és ≈02:23-kor két `_V3_r1` kép készült. Nem írtuk át.

**A végleges sorozat** az Astra V3.1 (világítás, függöny, összekötő fal) után jön, és külön „mehet” kell hozzá. A V3_TEST tanulságai, a V3.1-promptba javasolt kiegészítésekkel: audit, 8. pont.
