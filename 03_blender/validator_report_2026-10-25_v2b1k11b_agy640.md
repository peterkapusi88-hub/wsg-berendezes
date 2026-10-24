# Validator-riport: A-902 v2b-1-k11b JAVASLAT – master 05.1, ágytengely y 6,40 (2026-10-25 00:40)

**Feladat (Péter, 2026-10-25 00:05):**
1. A master ágy tengelye a Blender bútorrétegében legyen y = 6,40 m, a jóváhagyott terv és a dugaljpozíciók szerint.
2. Ellenőrizni kell a fejvég és a kapcsolók hozzáférhetőségét, valamint hogy a Cam_11 nézete helyes marad-e.
3. A PR #15 frissül az aktuális main-ről, a validáció újra lefut.
4. Beolvasztás csak Péter külön jóváhagyásával.

## Eredmény

Validator v2, lock v2b-1-k11b (sha256 `7aa85d70…154b`) + `A902_villamos.json` (terv szerinti kiállások).

| Mód | Előtte (v2b-1-k11) | Utána (v2b-1-k11b) |
|---|---|---|
| üres | PASS 0/0 | PASS 0/0 |
| referencia (beépített szaniterek) | FAIL 6/3 | FAIL 6/3 – ugyanaz a 6 régi szaniter-ütközés (06.2 mosdó 10 cm, zuhanytálca/üveg 2–3 cm, WC-tartály 2 cm, 06.1 törölközőszárító 3 cm); nem e PR tárgya |
| **master bútor** (ágy, éjjeliszekrény, lámpa, szőnyeg) | **FAIL 6/5** | **PASS 0/0** |
| Zenit master (stílusréteg) | FAIL 3/0 | FAIL 2/0 – a két fali olvasólámpa 3 cm-re a falban (régi modellezési hiba, nem az áthelyezésből) |
| Lake Forest master (stílusréteg) | FAIL 2/0 | FAIL 1/0 – a déli éjjeliszekrény márványlapja (48 × 48) a sarkával érinti az ajtó nyitási negyedkörét |

Mindkét fájlnál: LOCK 61 fal / 54 nyílás / 17 padló – 0 eltérés; terasz 43 elem – 0 változás; 11 kamera – a paraméterlap egyezik; villamos: 130 kiállás.

**Az előtte-állapot hibái a master bútor módban** (`geometry_v2/agy640/elotte_v2b1k11/validator_k11_regi_master_butor.json`):
- a fejtámla és a párna/takaró takarta a **K14** kapcsolót;
- a D22/D23 dugalj előtt állt (4 figyelmeztetés);
- mindkét éjjeliszekrény 3 cm-re a keleti falban volt;
- a déli éjjeliszekrény és a lámpája az ajtó nyitási negyedkörében állt.

## Mérések

Források: `04_renderek/A902_agy640_javaslat_v1/render_log_agy640_v2.json`, `geometry_v2/agy640/01_agy640_naplo_r2.json`.

**Ágy** (a bútorréteg referencia-ágya, `Agy_05_1_TALLASEN_180x200`):
- keret x 1,56–3,56; y 5,10–6,90 → **5,50–7,30**, tengely **6,40**;
- fejtámla y 5,50–7,30, magassága 1,05 m.

**A tervrajz ugyanitt van:** Péter 00:30-as képernyőképéről mérve (3,57 m = 465 px) az ágyjel y ≈ 5,48–7,31. Ez 2–3 cm-en belül egyezik a modellel.

**Kiállások a fejvég mellett** (mind x 3,545, z 0,65 m – terv szerint, helyszínen még nem mérve):

| Kiállás | y | Távolság a fejvég szélétől | Takarja a fejvég? |
|---|---|---|---|
| K14 kapcsoló | 5,319 | 0,18 m | nem |
| D22 dugalj | 5,24 | 0,26 m | nem |
| D23 dugalj | 5,159 | 0,34 m | nem |
| K13 kapcsoló | 7,51 | 0,21 m | nem |
| D21 dugalj | 7,589 | 0,29 m | nem |
| D20 dugalj | 7,669 | 0,37 m | nem |

**Éjjeliszekrények és lámpák:**
- Az éjjeliszekrények x 3,16–3,56 között állnak (falhoz igazítva), y 5,02–5,42 és 7,38–7,78 között. A tetejük 0,50 m, így a 0,65 m-es kiállások 15 cm-rel a lap fölött vannak, elérhetők.
- A lámpák a szekrény elejére kerültek (x 3,19–3,33), így 21 cm szabad marad előttük a fal felé.

**Ajtó és átjárók:**
- Az ajtó (Ajto_05_1, x 2,59–3,49, a falsík y 4,05) nyitási negyedköre y 4,95-ig ér. A déli éjjeliszekrény y 5,02-nél kezdődik, tehát 7 cm marad szabadon.
- Északon az ágy és a gardróbfront (pillérsík, y 8,04) között 0,74 m szabad, a minimum 0,60 m.
- Délen 1,45 m szabad az ajtós falig; a nyugati részen 2,05 m a déli fülkéig (y 3,45).

**Cam_11** (változatlan: [3,20; 6,10; 1,20], 20 mm) – **a nézet helyes marad:**
- a kamera az ágy alapterületén van, a tengelytől 0,30 m-re a déli fekvőhely felé, a szem 0,68 m-rel a matrac fölött;
- a 3,64 m-es üvegfal (y 4,28–7,92, közepe 6,10) továbbra is a kép közepén van;
- az ágy lábvége a képszélesség kb. 30–90 %-án látszik, jobbra (észak felé) kifut a képből – mint amikor az ágy bal oldalán ülünk.

Javaslat: a kamera maradjon. Ha y 6,40-re tolnánk, az üvegfal 30 cm-rel elcsúszna a képközéptől, és új Cam_11 alapkép, valamint 4 új prompt kellene.

**Cam_04:** változatlan. Az ágy a két éjjeliszekrény között áll, mindkét kiállás-csoport látszik (`ellenorzes_Cam04_agy640_v2.png`).

**ML06 mennyezeti kiállás** (x 1,834, y 6,049): a terv szerint is a szoba közepére esik, 0,35 m-re az ágy tengelyétől. Mennyezeti lámpának ez rendben van, az ágy fölé szánt függeszték viszont nem lenne tengelyben.

## Hatás a KEP-004-re: nincs

- A Cam_04 és a Cam_11 alapképe üres szoba, bútor nélkül.
- A Cam_04-promptok már eddig is a terv szerinti helyet írták elő („centred between the two bedside socket groups”).
- A 16 csomag és az Astra-promptok változatlanok.

## Mi változott (v2b-1-k11 → v2b-1-k11b)

**`03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`:** sha256 `33bf0af9…7661` → `9875cd57…ed28`. Csak bútor- és stílusréteg-mesh változott, összesen 33 objektum:

| Réteg | Mi mozdult | Eltolás |
|---|---|---|
| `A902_Butor` (9) | ágy (fejtámla, keret, matrac, párna/takaró), szőnyeg | y +0,40 |
| | éjjeliszekrény a/b | y +0,40, x −0,04 |
| | éjjeli lámpa a/b | y +0,40, x −0,14 |
| `Stil_Zenit` (11) | ágy, éjjeliszekrények, olvasólámpák fénysíkkal, szőnyeg | y +0,40 |
| `Stil_LakeForest` (13) | ágy, éjjeliszekrények lappal, olvasólámpák fénysíkkal, szőnyeg, bronzcsík | y +0,40 |

Fal, nyílás, padló, terasz, kamera és render-beállítás nem változott; a validátor 0 eltérést mér.

**Ami nem mozdult:** a teljes falas fejfal-burkolatok (`Z_agyfej_panel_*`, `Z_agyfej_LED`, `L_agyfal_travertin`, `L_agyfal_LED`, y 4,08–7,86). Ezek a falhoz tartoznak, nem az ágyhoz (leltár: `geometry_v2/agy640/06_leltar_r2.json`).
- A Zenit 6 paneles fejfalrácsának fugái y 4,69 / 5,32 / 5,95 / 6,58 / 7,21 m-nél vannak, így az új tengely (6,40) egy panel közepére esik, nem fugára.
- Ha a Zenit döntős lesz, a rácsot az új tengelyhez kell igazítani.

**A módszer:** az eltolás a mesh-adatba került, a location 0 maradt, ahogy a fájl többi bútoránál.
- Az első kísérlet (r1) a location-t írta. Blender 5.2-ben a `matrix_world` futásidejű adat: betöltés után a rejtett, nem kiértékelt objektumoknál egységmátrix. Ezért a validátor a régi helyet látta (`elotte_v2b1k11/04_vizsgal_r1_HIBAS.json`).
- Az r1 fájl nem került a repóba.

**`03_blender/geometry_lock_A902_v2b.json`:** a Cam_11 státuszszövegében az ágy helye frissült, és új bejegyzés került a `javitasok` közé (v2b-1-k11b, `butorreteg` lista). Geometria nem változott. sha256 `9e04ef4d…6645` → `7aa85d70…154b`.

## Megjegyzés a validátorhoz (Blender 5.2)

A `geometry_validator_v2.py` a befoglalókat a `matrix_world`-ből számolja, ami a rejtett, nem kiértékelt objektumoknál egységmátrix.
- A bútorréteg és a stílusrétegek master-elemei 0 location-nel, mesh-be sütve készültek, ezért rájuk a mérés helyes.
- A Zenit-réteg néhány más eleme nem 0 location-nel készült (pl. `Z_lampa_kar_*`, `Z_gyuru_*`, `Z_tukor_iv`). Egy teljes stílusréteg-validálás ezekre hamis hibát adna.
- A javítás (`matrix_basis` vagy depsgraph-kiértékelés) külön feladat, ebben a PR-ben nincs benne.

## Péter kérdése (00:30): 180 vagy 200 cm-es ágy?

**180 (a terv mérete):** kényelmesen elfér. A kapcsolók 18–21 cm-re vannak a fejvégtől, az északi átjáró 0,74 m.

**200: csak feltételesen.**
- A K14 és a K13 kapcsoló tengelytávja 2,19 m.
- A kapcsolólapok (kb. 8,5 cm, becslés) és egy ujjnyi hely miatt közéjük legfeljebb **kb. 2,05 m külső szélességű** keret vagy fejvég fér, y ≈ 6,415-ös tengellyel.
- Ekkor az északi átjáró 0,62 m-re szűkül (a minimum 0,60 m).
- Egy 50 cm-es gardróbajtó kinyitva kb. 12 cm-re áll meg az ágytól.
- A kapcsolók kb. 5 cm-re lennének a fejvégtől. A kiállások terv szerinti helyzetűek, így egy 5 cm-es helyszíni eltérés már takarást okozna.
- Szélesebb ágy csak alacsony (0,60 m alatti) vagy kivágott fejvéggel jöhet szóba.
- Claude javaslata: 180×200. Péter dönt; 200 esetén konkrét termék külső méretével méretezünk.

## Futtatás

- Háttér-Blender 5.2.3 LTS a Macen (`~/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/`), az élő Blender-folyamatból indítva (`subprocess.Popen`).
- Az élő, nem mentett Blender-fájlhoz (`WSG/Blender_aktualis_2026-10-24/…`) nem nyúltam.
- Szkriptek és naplók: `03_blender/geometry_v2/agy640/`.
- Ellenőrzőképek: `04_renderek/A902_agy640_javaslat_v1/`.

**Jóváhagyás:** Péter, 2026-10-25 00:05. A bútorréteg és a lock változása draft PR-be (#15) kerül; a main-be csak külön merge-jóváhagyás után.
