# Cam_12 v3 korrekció – szkriptek (Claude, 2026-10-25)
Összefoglaló: `05_promptok/KEP004_FABLE51_V3_1_CAM12_KORREKCIO/README.md`. Validátor-riport: `03_blender/validator_report_2026-10-25_cam12v3_korrekcio.md`.

**Szkriptek** (egyik sem ment blendet):
- `00_probe.py` – csak olvasó felmérés a blend másolatából: kamera, anyagok, gyűjtemények.
- `blokk_spec.py` – az S01/S02 tömbök: méret, hely, állapot (ELL/LEV/BECS/FELT), forrás.
- `01_render_cam12v3.py` – Blender 5.2.3, háttérben, a v2b-1-k13 blend MÁSOLATÁN.
  - Láthatóság a k13 alapkép szerint.
  - EEVEE, északi ablakfény + derítés.
  - Tömbök, validátor v2 négy módban (üres / referencia / S01 / S02).
  - Vetítés, renderek, napló.
  - Futtatás: `Blender -b <MASOLAT.blend> --python 01_render_cam12v3.py -- <KIMENET>`; környezeti változók: `CAM12_FENY` (W, alap 220), `CAM12_EXPO`, `CAM12_ENGINE` (EEVEE/CYCLES).
  - A lockot, a validátort és a villamos JSON-t a blend mappájából vagy a `forras/` mappából várja.
- `02_utak_blokk.py` – 2D közlekedő- és távolságmérés a C elrendezés motorjával és a Fable-konyhával → `utak_blokk_S01_S02.json`.
  - A motor (`elrendezes_alt_a902.py`) a `competition/baseline-20261025-v3` ágon van, útvonala: `WSG_ELRENDEZES_MOTOR`.
- `03_jelolt_kepek.py` – jelölt képek, felülnézetek, régi/új összevetés (`WSG_LOCK`, `WSG_REGI_CAM12`).
- `04_blokk_tabla.py` – a tételtábla (`blokk_tabla.md`) generálása.

**Naplók:** `naplok/` – Blender-napló (sha előtte/utána, kamera, vetítés, bbox-ok), validátor-JSON-ok, probe.
