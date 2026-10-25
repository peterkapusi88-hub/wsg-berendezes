# Verseny-baseline v2 – WSG Design Challenge 2026 (2026-10-25 06:30 CET)

Ez az ág (`competition/baseline-20261025-v2`; a rögzített commit SHA-ja a GOAL §7-ben és a PR #19 leírásában) a három versenyző (A GPT-6 Astra · B Claude Fable 5.1 · C Claude Opus 5.5) **azonos, rögzített forrásállapota**. Tartalma: a `main` friss állapota (Péter 04:39-es döntéseivel, `bc92d44`) + két, a mainbe **nem** beolvasztott ág:

| Beemelt ág | PR | Státusz | Mit ad |
|---|---|---|---|
| `kep004/kameracsomag-C-K1` | #20 (tartalmazza a #17 és #18 tartalmát) | **JAVASLAT** – a kamerákat (Cam_12 v3, Cam_03 K1) Péter 04:39-kor elfogadta, merge nincs; a lock v2b-1-k13 és a .blend csak repóbeli javaslat | végleges C elrendezés, Cam_03 K1, Cam_12 v3, validátor PASS, reality cardok, közös geometriai bemenet (`ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v1.md`) |
| `competition/kozos-bemenetek-20261025` | #19 | **draft** – koncepció elfogadva (Péter 04:27), merge nincs | fix-alap költségtábla, Hue-alap, 6 közös kalibrációs prompt, §0 blokk v2, preflight v2, kerek-asztal méretpróba |

**Szabályok:**
- A versenyzők saját ága **ebből a commitból** indul; a draft PR-ek **célága ez az ág**, nem a `main`.
- A baseline-t a versenyzők nem módosítják; a `main` nem változott; az élő Blender-fájl a Macen érintetlen.
- A javaslati státuszú elemek (Cam_12 v3, Cam_03 K1 FRAME LAYOUT) végleges értékét Claude az integrációnál adja; a versenyzők szöveges kompozíciót írnak, koordinátát nem találnak ki (§0 blokk).
- Közös fájlok: `ai-coordination/requests/WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` (§0 v2), `ai-coordination/inputs/A902_verseny/` (fix-alap, Hue-alap, geometria C), `05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/`, `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md`.
- Az első baseline-ág (`competition/baseline-20261025`, `32ba7bd`: main 29e72cf + #17 + #18 + #19) **ELAVULT** – nem indult belőle versenyző; Péter törölheti.
