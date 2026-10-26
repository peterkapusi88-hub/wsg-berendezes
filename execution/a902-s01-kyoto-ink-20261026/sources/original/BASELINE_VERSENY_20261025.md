# Verseny-baseline v3 – WSG Design Challenge 2026 (2026-10-25 05:20 CET)

Ez az ág (`competition/baseline-20261025-v3`; a rögzített commit SHA-ja a GOAL §7-ben és a PR #19 leírásában) a három versenyző (A GPT-6 Astra · B Claude Fable 5.1 · C Claude Opus 5.5) **azonos, rögzített forrásállapota**. Tartalma: a `main` friss állapota (`bdebeb9`, Péter 04:39/04:40/04:49-es döntéseivel) + két, a mainbe **nem** beolvasztott ág:

| Beemelt ág | PR | Végső commit | Státusz | Mit ad |
|---|---|---|---|---|
| `kep004/kameracsomag-C-K1` | #20 r2 (tartalmazza a #17 és #18 tartalmát) | `f190e5f` | **JAVASLAT, lezárt és átadott** (a párhuzamos Claude 04:50) – a kamerákat Péter elfogadta, merge nincs; a lock v2b-1-k13 és a .blend csak repóbeli javaslat | végleges C elrendezés, Cam_03 K1, Cam_12 v3, fénycsere, kerek asztal Blender-méretpróba, keleti teraszszárny 96 eset, validátor-nyilvántartás, **közös geometriai és fénybemenet: `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md`** |
| `competition/kozos-bemenetek-20261025` | #19 | `cf3b523` | **draft** – koncepció elfogadva (Péter 04:27), merge nincs | fix-alap költségtábla, Hue-alap, 6 közös kalibrációs prompt (61/64 kékórás), §0 blokk v3.1, preflight, kerek-asztal 2D-próba (a PR #20-éval egybevág) |

**Szabályok:**
- A versenyzők saját ága **ebből a commitból** indul; a draft PR-ek **célága ez az ág**, nem a `main`.
- A baseline-t a versenyzők nem módosítják; a `main` nem változott; az élő Blender-fájl a Macen érintetlen.
- A javaslati státuszú elemek (Cam_12 v3, Cam_03 K1 FRAME LAYOUT) végleges értékét Claude az integrációnál adja; a versenyzők szöveges kompozíciót írnak, koordinátát nem találnak ki.
- Közös fájlok (mindhárom versenyzőnek szó szerint azonos): `ai-coordination/requests/WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` (§0 v3.1), `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md`, `KOZOS_FIX_ALAP_v1.csv/.md`, `HUE_ALAPCSOMAG_v1.md`, `05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/`, `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md` (a §0 felülírja, ahol eltér).
- Korábbi baseline-ok: `competition/baseline-20261025` (`32ba7bd`) és `-v2` (`a8ab8d3`) **ELAVULTAK**, megőrizve; nem indult belőlük versenyző.
- **Indítás csak Péter külön „mehet”-jével.**

