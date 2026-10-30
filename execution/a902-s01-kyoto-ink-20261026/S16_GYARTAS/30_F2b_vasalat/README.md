# S16 R15 – 2. fázis (b): vasalat és furatok

Készült: 2026-10-30, Claude (Opus 5.5). Státusz: **TERVI** – típusok, pántoldal, polctartó-magasság műhelyi megerősítésre.

`python3 f2b_vasalat.py` → `vasalat_terv.json` (minden furat globális és alkatrész-helyi koordinátával, iránnyal, átmérővel, mélységgel, kapcsolattal) + `vasalat_jelentes.md`.

| Elem | Szabály | Darab |
|---|---|---|
| Tipli Ø8×35 | minden 18 mm-es korpusz T-kötésnél, a geometriából számolt kötésvonalon; élfurat Ø8×25 (vízszintes), lapfurat Ø8×12; 32 mm a végektől, max. 192 mm köz | 75 pár (25 kötés) |
| Polctartó Ø5×10 | torony 10 polca, elöl/hátul 37 mm, 3 magasság (−32/0/+32) | 120 furat |
| Pánt (Blum CLIP top 110°, sematikus) | kehely Ø35×13, B = 4 mm, 2× Ø8 (45/9,5), talplemez 37 mm/±16 mm; polcütközés-kerülés | jobb ajtó: 5 db |

**BLOKKOLÓ (tervezési döntés kell):** a bal toronyajtón (T-DOOR-L) a textilbetét átmenő kivágása mellett a keret csak **31 mm** – Ø35-ös kehely (B = 3–6 mm) nem fér el; szabványos CLIP top nem építhető be. Lehetőségek: keskeny keretes / csapos (pivot) pánt, vagy a keret szélesítése ~45 mm-re (a betét ~2×12 mm-rel keskenyebb). Ezért a bal ajtón nincs pánt a modellben.

Nem tiplis kapcsolatok (él-él illesztés, íves szerelvényhez kötés, keretlécek) a jelentésben listázva – ezekre külön kötés kell (Häfele kötő, csavar, ragasztás – műhelyi döntés).

Források: Blum fúrási adatlap (Ø35, B 3–6 mm, Ø8 45/9,5): https://static.richelieu.com/documents/docsGr/100/759/9/1007599/1394958.pdf ; etalon (km/coo1): Ø8×25/35 bordás tipli, de_11090 polctartó.
