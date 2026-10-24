# AGENTS.md – Codex házirend (ChatGPT Codex ezt olvassa először)

1. Olvasd el a `GOAL.md`-t (a projekt memóriája) és az `OPENAI_instructions.md`-t (a Work/Codex szereposztás és a részletes szabályok).
2. A te szereped: **Blender-technikus**. Python-szkripteket írsz és javítasz a `03_blender/` mappában; a tervezési döntéseket (bútor, anyag, keret) nem te hozod – azok a GOAL.md-ben és a `06_koncepcio/` doksiban vannak.
3. Eszköztár: `03_blender/wsg_helpers.py` (box, cyl, sphere, tube, disc, mat, coll, set_style). Koordináták méterben, origó a 05.2 szoba DNy-i sarka, x kelet, y észak, belmagasság 2,90 m. Minta: `03_blender/stil_lakeforest_layer.py`.
4. Új réteg = új `Stil_<Név>` gyűjtemény; alap-objektumot nem törlünk, csak rejtünk. `bpy.ops` csak ott, ahol `bpy.data` nem elég. Eredmény a `result` dict-ben.
5. A szkript futtatása nem a te dolgod: Claude futtatja a Blender MCP-n át, vagy Péter kézzel a Blender Text Editorban. Ne nyiss második vezérlést ugyanarra a jelenetre.
6. Fájlnevek: renderek `04_renderek/blender_stilusok/A902_<Stílus>_blender_<n>_<helyiség>.png`; promptok `05_promptok/`.
7. Commit-üzenet magyarul, egy sor. Személyes adat nem kerül a repóba. Küldés/rendelés/fizetés soha – azt Péter dönti el.


## Kötelező kiegészítő szabály

A `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` a Codex számára is kötelező. Nem csak Zenit/Lake Forest: a felhasználó több mint 10 alternatív stílust is megvizsgálhat. Fő feladatod a Blender-világkoordináták, fix geometria, tényleges bútorméretek, közlekedősávok és az egyedi beépített bútorok fizikai megvalósíthatóságának tesztelhető ellenőrzése. A rendernek a jóváhagyott, méretezett, beárazott termék- és asztalosspecifikációt kell tükröznie; kimutatható eltéréseket jelöld. Az árakat nem te találod ki, hanem Work és Claude függetlenül ellenőrzi. Ne módosítsd Claude élő Blender-jelenetét önállóan.
