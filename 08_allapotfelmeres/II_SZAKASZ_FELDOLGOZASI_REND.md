# II. szakasz – feldolgozási rend az állapotcsomag megérkezése után

**Indítás:** csak akkor, ha Péter ténylegesen átadta a csomagot (feltöltés vagy „itt a csomag” üzenet). Nincs automatikus hétfői futtatás. Astra-, Codex- és Gemini-feladatot nem indít, PR #1 inaktív. Élő Blender-fájlt nem ír felül. Külső ajánlatkérés és rendelés nincs.

| # | Lépés | Kimenet (repó) | Elkészült, ha |
|---|---|---|---|
| 1 | **Leltár.** Eredetik változatlanul a Macen (`~/Downloads/WSG_helyszin/2026-10-27/`); kicsinyítés, átnevezés, EXIF (idő, irány) | `08_allapotfelmeres/fotok/LELTAR_2026-10-27.csv` + `fotok/<lakás>/<helyiség>/` | minden fájl soron van, lakás és helyiség szerint; a hiányok a `FOTO_KAMERA_KAPCSOLAT.csv` P1 soraival összevetve |
| 2 | **Látható tények.** Padlódekor, falszín, ablakok, panoráma; ami nem dönthető el, `NEM IGAZOLT` | `ADAT_STATUSZ_3_LAKAS.md` v2 (ELŐZETES → IGAZOLT-M átvezetés) | minden P1 sor státusza frissítve |
| 3 | **Összevetés a Blenderrel** (A-902 v1/v2; A-811/812 terv) | `03_blender/geometry_v2/A902_eltereslista_v2_v3.md` + A-811/812 eltéréslista | tételes eltérés cm-ben, forrással |
| 4 | **Reality Card** minden kulcshelyiséghez (nappali, étkező–konyha, master, terasz; A-811/812 nappali és háló) | `ai-coordination/reality_cards/<lakás>_<kamera>.md` | felületenként: MEGLÉVŐ / ÚJ / ISMERETLEN |
| 5 | **Geometria- és anyagkorrekció** új verzióban. Előtte biztonsági másolat az élő állapotról | `WSG_A902_v3_*.blend`, `geometry_lock_A902_v2.json`, validátor-riport | a validátor lefutott; az élő fájl érintetlen; a lock v2-höz Péter jóváhagyása kell |
| 6 | **Költség- és anyag-megvalósíthatóság** a valós felületekre | `KOLTSEGSTRATEGIA_3_LAKAS.md` v2 | a keret lakásonként +10%-kal; az érintett tételek megjelölve |
| 7 | **Friss Astra-brief.** Valós geometria, parketta, falak, kilátás; csak előkészítve, nem indítva | `ai-coordination/inputs/A902_v2/` (+ A811_v1, A812_v1) | REQUEST_TEMPLATE szerint, „NINCS ELINDÍTVA” jelöléssel |
| 8 | **Döntési jelentés:** mit tudunk biztosan, mi változott, mi hiányzik, mihez kell Péter jóváhagyása | `08_allapotfelmeres/DONTESI_JELENTES_2026-10-27.md` + rövid chat-összefoglaló | max. 1 oldal, döntési kérdések számozva |

**Időkeret:** az 1–4. lépés a csomag után kb. 4–6 óra Claude-munka (fotószámtól függ). Az 5–8. lépés ugyanazon a napon, ha a P1 mérések megvannak.
