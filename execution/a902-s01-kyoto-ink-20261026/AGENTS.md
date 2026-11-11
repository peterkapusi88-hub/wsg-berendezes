# AGENTS.md – A-902 médiafalak gyártás-előkészítése (S16 + R16)

Bármelyik kódoló ügynök (Claude Code, Codex) ezt olvassa el, mielőtt ebben a mappában bármihez nyúl. A gyökér `GOAL.md` és a saját házirended (`CLAUDE.md`, illetve a gyökér `AGENTS.md`) itt is érvényes; ez a fájl csak a médiafal-gyártásra vonatkozik.

## Állapot a repó szerint (összefoglaló: 2026-11-12 – ha elavult, frissítsd)

- **A friss munka nem a `main`-en van**, hanem a #30-as draft PR ágán (`claude/s16-f2-cad-20261030`): mindkét szekrény F1–F4 lánca és szerelési anyaga (S16 R15C: 129 alkatrész, R16 J: 106 alkatrész). A `main`-en csak az S16 F1 + R15 van.
- A v8 csomagot (S16 + R16, látványtervvel) Péter 2026-10-30 18:23-kor elküldte az asztalosnak. A válasz a repóban még nincs rögzítve – kérdezd meg Pétert, megjött-e.
- 2026-10-31: összeszerelési útmutatók, műhelyi próba-ellenőrzőlista, S16 fiókdoboz-csavarkötések a furattervben. **A v9 DWG még nincs felépítve a Macen** (AcCoreConsole + visszaolvasás hátravan).
- Semmi sincs gyártásra kiadva; minden kimenet TERVI.

Munka előtt: `git fetch origin`, nézd meg a PR #30 és a `main` állapotát, és ott folytasd, ahol a friss munka van.

## Egy igazság-forrás

- Lánc a `S16_GYARTAS/` alatt (az R16-nál ugyanígy az `R16_GYARTAS/` alatt): `10_F1_adatmodell` → `20_F2_cad` → `30_F2b_vasalat` → `40_F3F4_dokumentacio` → `60_szereles`. A két szekrény csomagját a `S16_GYARTAS/50_csomag/csomag.py` állítja össze. A futtatási parancsok a mappák `README.md`-jében vannak.
- Minden kimenet a `parts_v1.json`-ból (+ `vasalat_terv.json`) generálódik. **Sem a `parts_v1.json`-t, sem a DWG/DXF/PDF/XLSX/MPR kimenetet nem szerkesztjük kézzel.** Változás = javító szkript (az `r15_patch.py`, `r15b_patch.py`, `r15c_patch.py` mintájára), indoklással és forrással a változásnaplóban, utána újragenerálás.
- A `forras_*` mappák változatlan bemenetek (SHA-256-tal ellenőrizve) – nem írjuk át őket.
- Az R16 szkriptjei a S16 moduljait importálják: ha S16-modult módosítasz, az R16 láncot is futtasd és ellenőrizd.

## Kapuk – ezek nélkül nincs export és nincs „kész"

- Ha a QA BLOKKOLÓ-t talál (a `qa_parts_v1.py` ilyenkor 2-es kóddal lép ki), nincs export. Kiadást blokkol: negatív vagy nulla méret, modell ↔ lista ↔ rajz ↔ export eltérés, verziókeveredés.
- DWG csak akkor elfogadott, ha az AutoCAD-visszaolvasás minden testre egyezik (S16 129/129, R16 106/106; `S16_GYARTAS/20_F2_cad/f2_readback.py`).
- A dokumentáció-QA-ban a vasalatterv = MPR = Excel = PDF = DXF egyezésnek teljesülnie kell.
- Eredményről a számokat a QA-jelentésből idézd, ne emlékezetből.

## Amit nem találunk ki

- Furatkép és vasalat-koordináta csak gyártói adatból (Blum, Häfele…), forrásmegjelöléssel. Ahol nincs gyártói adat, ott nincs koordináta, csak nyitott tétel (a mappák README-i listázzák, melyik ilyen).
- A műhelyi konvenciók – élkód-sorrend és az `A` jelentése, nullpont és ütköző, élanyag, előmarás, ráhagyás – **FELTEVÉSEK** a `gyartasi_szabalyok_v1.json`-ban, amíg az asztalos nem válaszol. A válasz oda kerül, utána mindent újragenerálunk.
- Az MPR csak TERVEZET, amíg nincs meg a műhely minta-MPR-je és szerszámtáblája, woodWOP-szimuláció és próbadarab.

## Mac-függő lépések

- Az AutoCAD 2027 for Mac Péter gépén fut, ActiveX/COM nélkül: DWG csak AutoLISP + `.scr` úton, AcCoreConsole-lal készül. Buktatók: `S16_GYARTAS/20_F2_cad/README.md` (kb. 4 KB-os sorvágás, külső `.lsp` tiltva, a `-help` beragad, PDF-nyomtatás nem megy).
- Felhőből a DWG nem olvasható (ACIS-testek): DXF-export vagy a Macen futó visszaolvasás kell. Ha nincs elérhető Mac, készítsd elő a lépést, írd le, mit kell futtatni, és ne állítsd, hogy lefutott.
- Az asztalos etalon-DWG/DXF-jei az ő szellemi tulajdona: nem kerülnek a repóba. A csomag-zip sem.

## Döntések és kommunikáció

- Tervezési döntést Péter hoz; a dátumozott döntések a `GOAL.md` 7. pontjában vannak. Amit kifejezetten ránk bízott (pl. az R15B pántolás), azt visszafordíthatóként jelöljük.
- Az asztalosnak szóló üzenet csak tervezet (`S16_GYARTAS/50_csomag/asztalos_uzenet_TERVEZET.md`); Péter küldi el, az ő „mehet"-je után.
- Ha megjön az asztalos válasza: a válasz a szabályfájlba → újragenerálás mindkét szekrényre → QA és AutoCAD-visszaolvasás → eltéréslista Péternek.

## Ki mit csinál itt

- **Claude (Code vagy Desktop):** a lánc gazdája – javító szkriptek, újragenerálás, QA, AutoCAD-futtatás a Macen, PR.
- **Codex:** független ellenőr – olvas, saját teszteket ír, újraszámolja a QA állításait; külön ágon dolgozik, a generált fájlokhoz, a `forras_*` mappákhoz és az AutoCAD-hez nem nyúl.
- Egy ágon egyszerre egy ügynök dolgozik.

## Git

- Ág: `claude/…` vagy `codex/…`, draft PR; a `main`-be csak Péter „mehet"-jével kerül.
- Commit-üzenet magyarul, egy sor.
- `__pycache__/` és ideiglenes kimenet nem kerül commitba (lásd `S16_GYARTAS/10_F1_adatmodell/.gitignore`).
