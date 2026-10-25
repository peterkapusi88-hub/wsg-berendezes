# WSG DESIGN CHALLENGE 2026 – közös §0 blokk és célzott javítások a három indítóprompthoz (v1, 2026-10-25 05:00 CET)

**Forrás:** a ChatGPT által összeállított három indítóprompt (A – GPT-6 Astra Medium; B – Claude Fable 5.1 High; C – Claude Opus 5.5 High) és preflight-kérés, Péter csatolmánya 2026-10-25 03:13; Péter döntései 03:32–04:10 (66 prompt marad; ő a döntőbíró; hero-nézetek először; C1/C2 egyszer, Claude; költség-keresztellenőrzés; közös bemenetek a start előtt; C elrendezés + K1 Cam_03 a PR #18-ból).

**Használat:** az alábbi §0 blokk **szó szerint** kerül mindhárom indítóprompt elejére, a repóban megnevezett dokumentum elé. Utána a 2. pont célzott szövegcseréi. A három prompt egyébként változatlan.

---

## 1. §0 – KÖZÖS VERSENYBLOKK (mindhárom versenyzőnek, bemásolható)

```
§0 – KÖZÖS VERSENYBLOKK (WSG Design Challenge 2026, v1, 2026-10-25). Ez a blokk
elsőbbséget élvez az indítóprompt és az r2 brief minden ellentmondó mondatával
szemben.

0.1 Közös bemenetek a repóban (a rögzített forráscommit utáni, mindhárom
versenyzőnek azonos kiegészítések; olvasd el, mielőtt tervezel):
- ELRENDEZÉS: a nappali–étkező alaprajzi alapja a C elrendezés (Péter döntése,
  2026-10-25): hosszanti étkezőasztal 2+2+1+1 ülésrenddel közvetlenül az ML04
  függeszték alatt, a kanapé a termék valós mélységéhez igazítva nyugatabbra;
  fő utak ≥ 0,90 m betolt székkel, székkihúzás ≥ 0,90 m, kanapé–TV-bútor
  ≥ 0,60 m; a W01 előtt legfeljebb 60 cm mély szekrénytest; a TV a falsíkon
  marad. Részletek: ai-coordination/results/WSG-20261025-A902-ELRENDEZES-ALT_r1.md
  (PR #18). Ezen belül szabad a bútor, a forma, a termék; az étkező 160 × 90-es
  asztalbefoglalója és a hat ülőhely kötött. Koordinátát nem találsz ki.
- CAM_03: a konyhaorientált K1 kamera ([9,45; 7,55; 1,50], dél felé, 20 mm;
  konyha a kép ~22 %-a) – a konyha két pultsora, hűtőoszlopa és magas elemfala
  a kép tárgya, elöl az étkező széle és az ML04 függeszték; a terasz és a TV-fal
  nem látszik. A végleges FRAME LAYOUT-ot Claude adja; a kompozíciót a látható
  elemek hierarchiájaként írd le.
- KÖLTSÉG: ai-coordination/inputs/A902_verseny/KOZOS_FIX_ALAP_v1.csv – a
  18,00 M bruttó = 8,40 M közös fix (gépek, mosogató, 05.2 és 05.3 háló,
  előtér, mosó-szárító, terasz, szállítás/szerelés, tervezés) + 9,60 M
  stílusfüggő. Te a 9,60 M-os stílusfüggő keretet tervezed és árazod
  tételesen (konyhabútor, nappali–étkező, master, fürdő-kiegészítők,
  világítás, falak, textil/styling); a 8,40 M-ot egy sorban, változatlanul
  átveszed. A 2,00 M tartalék érintetlen. Fő és gazdaságos változat a
  stílusfüggő részre.
- HUE: ai-coordination/inputs/A902_verseny/HUE_ALAPCSOMAG_v1.md – közös
  rendszerelv és fajlagos árak; minden fényvonalhoz és lámpatesthez hely,
  hossz/db, termék, táp- és kiállás-azonosító, profil, rögzítés, kábelút,
  anyag + szerelés bruttó.

0.2 Kanapé: minden tervben minimum L-alakú, inkább U-alakú; íves/félhold
kanapé csak puffal, amellyel L/U-ként működik (Péter, GOAL §4.7). Ez nem
opcionális.

0.3 Beszerzési források (GOAL §4.4, CLAUDE.md): látszó darabok – kanapé,
asztalok, székek, ágy, fotel, tükrök, lámpák – Kave Home vagy Westwing
(más márka csak ellenőrizhető magyar árral, szállítással és termékoldallal);
vázak – PAX, METOD, BESTÅ – IKEA; forma-darabok (lakásonként 1–3) asztalos,
az anyagszabály szerint (Egger H1180 / H3710 / F274 laminált család,
bordázott vagy hajlított MDF, furnér legfeljebb egy felületen; nincs tömörfa,
kő, festett front; belső fehér). Dekoranyag (kőfurnér, kőhatású panel,
textúrás tapéta, kárpitpanel) őszintén megnevezve. Minden látható termékhez
gyártó, terméknév/cikkszám, méret, bruttó ár, forrás, dátum, státusz
(ellenőrzött / becslés).

0.4 Kalibráció: a C1 Zenit és C2 Lake Forest × Cam_02/Cam_04/Cam_11 hat
promptját NEM te írod; Claude egyszer elkészítette
(05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/), mindhárom versenyző ugyanazt a
mércét kapja. A te kimeneted: 60 prompt (10 stílus × 6 kamera) + a tíz
stílusspecifikáció a §11.12 szerint. A manifestedben a 61–66. sor
„KALIBRACIO_KOZOS – nem a versenyző feladata” státuszt kap, hogy a 66-os
regiszter teljes maradjon. Az S06 Zenit Atelier és az S07 Lake Forest
Couture teljes stílus marad a feladatod.

0.5 Költségkapu és keresztellenőrzés: a saját költségbecslésed tájékoztató.
A 18 M-os beférésről a keresztellenőrzés dönt (A Astra → Claude; B Fable →
GPT-6; C Opus → Astra vagy GPT-6), azonos módszerrel és azonos fix-alappal.
Hiányzó vagy árazatlan szükséges tételt az ellenőrző konzervatív benchmark-
árral pótol és jelöl – ez korrekció, nem kizárás. Alulárazás ezért nem
előny; a kapu a keresztellenőrzött végösszegen van.

0.6 Képek sorrendje (Péter): a kész 66 promptból a képek egyesével,
Claude Chrome-ból, ChatGPT Images-szel készülnek, „koncepció” státuszban,
előbb a hero-nézetek (minden stílus Cam_12, majd Cam_02), utána a többi.
A Blender- és költségkapu utáni végső összehasonlító képek csak a
továbbjutó koncepciókra készülnek újra, azonos kamerával és referenciával.

0.7 Bírálat: a kapukon (geometria/használhatóság, kivitelezhetőség,
keresztellenőrzött ≤ 18 M, renderhűség) megfelelt tervek közül Péter dönt a
látvány alapján; az integrációtól kezdve a csomagok kódnevet (X/Y/Z) kapnak.
Ne értékeld magadat győztesnek, ne írj a másik két versenyzőről.

0.8 Folytatás megszakadásnál: ha a futás (kontextus, keret, GitHub-írás)
megszakad, új munkamenetben a saját 00_CHECKPOINT_NAPLO.md és
01_MANIFEST_66.csv alapján a PENDING/DRAFT tételekkel folytatod, a COMPLETE
tételeket nem írod újra. Ha a GitHub-push nem megy, a kész fájlokat egyetlen
csomagban átadod a chatben, és Claude változtatás nélkül committálja a saját
ágadra.
```

## 2. Célzott szövegcserék a három promptban

| Prompt | Hol | Mostani szöveg | Csere |
|---|---|---|---|
| A, B, C | kalibráció (A §10, B §2/3., C §2/4.) | „6 külön kalibráció: C1/C2 × …” / „plusz C1 Zenit és C2 Lake Forest három-három kalibrációs promptja” | „A hat kalibrációs promptot Claude készítette el közösen (§0.4); a te kimeneted 60 fő prompt + 10 stílusspecifikáció. A manifest 66 soros marad.” |
| A, B, C | Cam_03 (A §7, B §6, C §6) | „A végleges kamera még készül, értéket ne találj ki.” / „végleges kamerakoordináta még nincs” | „Cam_03 = K1 konyhaorientált kamera (§0.1); a FRAME LAYOUT-ot Claude adja.” |
| A, B, C | elrendezés (A §5, B §4, C §4) | „Claude integrátor 2–3 méretezett alternatívát készít …” | „Az elrendezés alapja a C változat (§0.1, PR #18); a méretezett bútorszándékot ezen belül add meg.” |
| A, B, C | költség (A §8, B §7, C §7) | „Stílusonként adj: teljes lakásszintű becsült költségvetést …” | „Stílusonként adj: a 9,60 M-os stílusfüggő keret tételes fő és gazdaságos költségvetését a KOZOS_FIX_ALAP_v1 szerint, a 8,40 M fix sort változatlanul átvéve (§0.1).” |
| A, B, C | költség, „Árazatlan vagy hiányzó … nem tekinthető igazoltnak” | ua. | „Árazatlan szükséges tételt a keresztellenőrző benchmark-árral pótol és jelöl (§0.5); törekedj a teljességre, mert a pótlás konzervatív.” |
| A | §2 | „A heti Work-keretem körülbelül 26%-a maradt.” | marad, kiegészítve: „Ha a keret elfogy, a §0.8 szerint folytatjuk; a kész részek nem vesznek el.” |
| A | §11 ág | `astra/creative-upgrade-v3-1-r1-20261025` | marad, **de** a mappa és a results-fájl neve legyen egységes a brieffel: `05_promptok/KEP004_ASTRA_V3_1_r1/` és `…V3_1_r1.md` (ok); a brief „r2” a brief verziója, a kimenet „r1” az első kimenet – ezt a README első sorában mondd ki. |
| B, C | §1 „Ne olvasd a másik két versenyző … draft PR-jeit” | ua. | kiegészítés: „A draft PR-ek a repóban láthatók; a tilalom önkéntes fegyelem, a bírálat kódneves (§0.7).” |

## 3. Keresztellenőrzés beosztása (Péter, 04:03: „ok”)
| Versenyző | Saját költség | Keresztellenőrző | Módszer |
|---|---|---|---|
| A – Astra | tájékoztató | **Claude** | azonos fix-alap, dátumozott webshop-árak, benchmark-pótlás |
| B – Fable | tájékoztató | **GPT-6 Chat** | ua. |
| C – Opus | tájékoztató | **Astra vagy GPT-6** (nem Claude) | ua. |
A geometriai kaput mindhárom tervnél Claude futtatja (validator + Render Reality Gate), kódnevekkel, szkripttel; az eredmény fájlban, nem véleményként.

## 4. Mi nem változik
A három prompt szerkezete, a 10 stílus, az S01/S02 három TV-fal-koncepciója, a 66-os regiszter, a §11.12 fájlszerkezet és a checkpoint-rend, a tiltások (nincs kép, Blender, merge, rendelés).
