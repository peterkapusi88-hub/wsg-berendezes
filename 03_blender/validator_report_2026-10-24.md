# Geometry Validator – jelentés, 2026-10-24 (A-902, mindkét stílusréteg)

Mérés: `03_blender/geometry_validator.py` a `WSG_A902_stilusok.blend`-en, lock: `geometry_lock_A902.json` (54 fal, 52 nyílászáró, 19 padló, 6 kamera). Ez mérés, nem vélemény.

## Eredmény

| Ellenőrzés | Zenit | Lake Forest |
|---|---|---|
| LOCK (falak, nyílászárók, padlók, kamerák a jóváhagyott helyen, tűrés 1 cm) | ✅ 0 eltérés | ✅ 0 eltérés |
| Bútor a lakás/terasz területén belül, z 0–2,90 | ✅ | ✅ |
| Bútor ↔ fal / nyílászáró ütközés | ✅ 0 (javítás után) | ✅ 0 (javítás után) |
| Ajtó-előtér (90 cm) szabad | ❌ 3 helyen | ❌ 3 helyen |
| Kanapé–dohányzóasztal 45–50 cm | ⚠ 14 cm | ⚠ mérés pontosítandó (modul-átfedés) |
| Kanapé–TV-fal közlekedő ≥ 90 | ✅ 109 | ✅ 90 |
| Ágy mellett ≥ 60 (master, nyugat) | ✅ 156 | ✅ 156 |
| Étkezőszék hátratolás ≥ 60 (cél 90) | ✅ > 90 | ✅ > 90 |

## Amit a validátor talált és már javítva lett (2026-10-24 éjjel, mentve a .blend-ben)
- **Étkező mindkét rétegben**: a székek a keleti falba / a 05.3 ajtóba / a gépészeti aknába lógtak (Zenit 3–30 cm, LF 2–6 cm), a tálaló a 05.3 ajtó előterét zárta. Újraépítve: 160×90 asztal x-irányban (x 8,15–9,72, y 5,65–6,55), **pad északon** (hátratolás nem kell), 3 szék délen, tálaló törölve, lámpák az asztal fölé. A kerek asztal a 2,7 m-es sávban ajtó-előtér nélkül nem fér el – ez tervezési döntés, Péter visszavonhatja.
- **LF kanapé** egy modullal rövidebb (4,55–7,25), hogy az átjáró (x 7,40–8,45) felől 90 cm közlekedő maradjon az asztalig; kisasztal áthelyezve.
- **Zenit fotel + kisasztal** kikerült az átjáró vonalából (DNy-i sarok, TV-fal mellett).

## Nyitott hibák – NEM javítva, Péter döntésére vár
1. **Master (05.1) déli éjjeliszekrény az ajtó előterében** (38 cm) – javaslat: az ágycsoport +35 cm északra (ágy y 5,45–7,25); az északi éjjeli 7 cm-re kerül a pillértől.
2. **05.2 háló: a 160×200 ágy és az északi éjjeli a szobaajtó előterében** (22–30 cm). A 3,62×2,55-ös szobában a 90 cm-es ajtó-előtér ÉS az erkélyajtó-előtér mellett **nem fér el 160-as ágy két éjjelivel**. Opciók: (a) ágy 40 cm-rel délre (y 0,05–1,65), éjjelik helyett fali olvasólámpa + lebegő polc; (b) 140×200 ágy; (c) elfogadjuk, hogy az ajtó csak ~60 cm-re nyílik.
3. **05.3 háló: PAX 200 gardrób közvetlenül a szobaajtó mögött** (60 cm az előtérben) – javaslat: a déli falra (x 11,0–11,6 → y 4,04–6,04 a nyugati falon, vagy x 11,1–13,1 a déli falon), ágy ennek megfelelően.
4. **Előtér: cipősszekrény a WC-ajtó előterében** (17 cm) – javaslat: 96 cm-es elem (STÄLL-méret) y 0,08–1,04 között, vagy a déli falra a bejárati ajtótól nyugatra.
5. **Zenit dohányzóasztal 14 cm-re a kanapétól** – javaslat: 30 cm délre (középpont 5,95 / 5,25).
6. **LF dohányzóasztal a rövidített chaise alá lóg** – javaslat: kanapé +35 cm északra (hát 7,10), asztal (5,90 / 5,20).

## Tanulság a munkarendhez
- A validátort **minden réteg-módosítás és minden render előtt** le kell futtatni; a kimenet ide (vagy a PR-be) kerül.
- A kezdő IKEA-alaprajz (A902_Butor) is tartalmaz ajtó-előtér hibákat → a hétfői fotók utáni geometria-javítással együtt az alap elrendezést is újra kell validálni.
- Codex feladata lehet a tesztek bővítése: fűtő-hűtő mennyezeti panelek zónái (fúrási tilalom) a lock-ba; közlekedő-útvonalak gráfként; ajtószárny-nyitásirány.
