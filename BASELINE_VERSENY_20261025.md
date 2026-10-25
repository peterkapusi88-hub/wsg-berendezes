# Verseny-baseline – WSG Design Challenge 2026 (2026-10-25)

Ez az ág (`competition/baseline-20261025`, tag `verseny-baseline-20261025`) a három versenyző (A GPT-6 Astra · B Claude Fable 5.1 · C Claude Opus 5.5) **azonos, rögzített forrásállapota**. Tartalma: a `main` `29e72cf` állapota + három, a mainbe **nem** beolvasztott javaslati ág:

| Beemelt ág | PR | Státusz | Mit ad |
|---|---|---|---|
| `kep004/cam12-nappali-hero-javaslat` | #17 | **JAVASLAT** – a Cam_12 kamera a lockban és a .blend-ben; merge nincs jóváhagyva | a Cam_12 hero alapkép és tömbképek (`04_renderek/A902_cam12_hero_javaslat/`) |
| `kep004/elrendezes-alt-cam03-javaslat` | #18 | **MÉRETPRÓBA** – Péter döntése: C elrendezés + K1 Cam_03 (04:08); a kameracsomag validálása folyik; merge nincs | elrendezési alternatívák, méretpróba-motor, Cam_03 jelöltek (`ai-coordination/results/WSG-20261025-A902-ELRENDEZES-ALT_r1.md`) |
| `competition/kozos-bemenetek-20261025` | #19 | **draft** – koncepció elfogadva (Péter 04:27), merge nincs | fix-alap költségtábla, Hue-alap, 6 közös kalibrációs prompt, §0 blokk v2, preflight, kerek-asztal méretpróba |

**Szabályok:**
- A versenyzők saját ága **ebből a tagből** indul; a draft PR-ek **célága ez az ág**, nem a `main`.
- A baseline-t a versenyzők nem módosítják; a `main` nem változott; az élő Blender-fájl a Macen érintetlen (a #17 .blend/lock változása csak repóbeli javaslat).
- A javaslati státuszú elemek (Cam_12, Cam_03 K1 FRAME LAYOUT, kameracsomag) végleges értékét Claude az integrációnál adja; a versenyzők szöveges kompozíciót írnak, koordinátát nem találnak ki (§0 blokk).
- Közös fájlok: `ai-coordination/requests/WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` (§0 v2), `ai-coordination/inputs/A902_verseny/`, `05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/`, `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md`.
