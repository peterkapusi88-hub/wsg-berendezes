# KEP-004 · ChatGPT Images – csomagépítő és ellenőrző eszközök (Claude, 2026-10-24)

Ezekkel készültek a `../*.prompt.txt` fájlok és a Macen lévő képcsomagok. Átláthatóság és Codex-review a cél; az útvonalak Claude felhős munkakörnyezetére szólnak (`/home/claude/wsg-berendezes/`, `/mnt/user-data/outputs/…`).

| Fájl | Mit csinál |
|---|---|
| `forrasok.py` | A forrásblokkokat szó szerint kinyeri (v3.1 §1/§2/§3, Cam_10-csereblokk, a Cam_11-blokk a PR #15 ágáról `git show`-val, gardrób- és Hue-blokk, Astra V2-stílusblokk, koncepció-cella). Csak olvas. |
| `epito.py` | Összefűzi a promptot: fejléc → közös FIXED → helyiség-FIXED → Hue → gardrób (master) → stílus/kalibráció → RUN NOTES. Összeállítja a csomagokat és a nyilvántartást. |
| `ellenor.py` | Szó szerinti egyezés és csomagteljesség (eredmény: `ellenorzes_promptok_v1.json`, hiba 0). |
| `readme_frissito.py` | A `../README.md` táblái a nyilvántartásból. |
| `kontaktlap.py` | A Cam_02 helyszíni kontaktlapja (ME-BAL-045/046/042/044/053). |
| `kave_kivago.py`, `kave_bizonyitek_kivago.py` | A Kave Home termékképek és a forrás-képernyőképek kivágása Péter képernyőképeiből. A képek nem kerülnek a repóba. |
| `archivalas_elokeszito.py` | A Mac átvételi mappájából előkészíti a GitHub-archívumot. Csak másol. |
| `csomag_nyilvantartas.json` | Képenként: bemenetek, forrásuk és sha256-juk, a prompt sha256-ja. |
