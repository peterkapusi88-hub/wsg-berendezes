# WSG KÉZJEGY – egyedi AI-művészet mint a lakások védjegye (KÉZJEGY-program, v1)

**Hivatkozás:** „KÉZJEGY” vagy `KÉZJEGY-01` · **Rögzítve:** 2026-10-25 17:34 CET · **Döntés:** Péter („az egész művészire igen”; először Astra-féle művészi irány, utána az alábbi munkafolyamat) · **Lejegyezte:** Claude
**Hatály:** mindhárom lakás (A-811, A-812, A-902), minden stílus. **Státusz:** elfogadott irány; ár, anyag és kivitelező még nincs kiválasztva. Rendelés, ajánlatkérés és külső kommunikáció csak Péter „mehet”-jével.

## 1. Alapgondolat
Ez a legjobb „luxus forintonként” arány a projektben. Egy egyedi, csak oda készült kép vagy minta drágábbnak hat bármelyik bútornál, a kivitelezése pedig többnyire olcsó. Ettől lesz minden lakás „extra grandiózus és exkluzív” (Péter).

## 2. Felépítés
- **Lakásonként egy művészi motívum, 3–4 hordozón.** Például a Kyotónál a tusrajzág megjelenik a TV-fal tapétáján, a zuhanyvégfalon, a fejvégnél egy vásznon és a párnákon. Ettől lesz kurált, nem csak szép a lakás.
- **Olcsó kivitelezési utak** (ár: bruttó Ft, 2026-10-25; „ellenőrzött” = forrással igazolt, „becslés” = ajánlat kell):

| Hordozó | Hol | Ár | Státusz / forrás |
|---|---|---|---|
| Egyedi nyomtatott vlies tapéta (falfestmény-hatás) | száraz fal: TV-fal, fejvég, közlekedő | kész fotótapéta 4 900–7 100 Ft/m²; saját képből 8–15 e Ft/m²; tapétázás 3 500–4 800 Ft/m² → egy 11,6 m²-es TV-fal ≈ 150–230 e Ft | kész tapéta: ellenőrzött (OBI, Komar); egyedi nyomat: becslés |
| Nagy vászonkép | nappali, háló | 200 × 100 cm: 88 320 Ft listaár, akcióban 75 075 Ft | ellenőrzött (kepmania.eu/arlista, 2026-10-25) |
| „Kézzel befejezett nyomat”: a vászonnyomatra képzőművész-hallgató vastag festékréteget, ecsetnyomot vagy aranyfüstöt visz, és aláírja | kiemelt darabok | munkadíj ≈ 20–60 e Ft / kép | becslés |
| Eredeti festmény AI-terv alapján (kezdő festő vagy egyetemista) | kiemelt darabok | ≈ 80–250 e Ft / nagy kép | becslés |
| Falfestmény száraz falra | egy kiemelt fal | ajánlat kell | **eltér a „fehér fal marad” szabálytól → Péter döntése kell** |
| Hátoldalán nyomtatott edzett üveg (Optiwhite) | zuhany, konyhai hátfal | 115 000 Ft/m² + ÁFA = 146 050 Ft/m²; zuhanyvégfal 0,85 × 2,85 m ≈ 420 e Ft, konyhai hátfal ≈ 1,65 m² ≈ 240 e Ft | m²-ár: ellenőrzött (szinesuveg.hu/arak, 2026-10-25); teljes ár: becslés |
| Hátoldalán nyomtatott akril vagy laminált alu-kompozit | zuhany, vizes fal | zuhanyvégfal ≈ 120–180 e Ft | becslés |
| Kompakt HPL nyomott/színes dekorral, CNC-szabással | zuhany, formázott elemek | ≈ 70 e Ft/m² → zuhanyvégfal ≈ 250 e Ft | becslés |
| Egyedi nyomott textil (párna, függöny) | nappali, háló | nincs árazva | becslés kell |

- **Technikai feltétel:**
  - nagy felbontás: egy 85 × 285 cm-es kép 150 dpi-n ≈ 5 000 × 16 800 pixel → nagyítás (upscaling) kell;
  - a mintákhoz ismétlődő, varrat nélküli elem;
  - a promptokba élő művész nevét nem írjuk;
  - a kereskedelmi felhasználás a generáló eszköz feltételei szerint, eszközönként ellenőrizzük.
- **Költség:**
  - a képek a meglévő falfelület- és dekorsorokból (KOZOS_FIX_ALAP 11 és 12) kijönnek, plusz pénz nem kell;
  - egyes asztalos-panelek helyett olcsóbbak;
  - a vizes helyiség üvegfala opció, a stílus keretén belül kell helyet csinálni neki.

## 3. Munkafolyamat
1. **Astra** stílusonként 3–5 művészi irányt generál (motívum, színvilág, a hordozókra bontva). Péter választ.
2. **Claude** elkészíti a nyomdakész specifikációt hordozónként:
   - végméret és kifutó (tapétánál ≥ 5 cm);
   - pixelméret és dpi (≥ 150 dpi a végméreten);
   - színprofil (a nyomda profilja szerint);
   - fájlformátum;
   - a csempefugákhoz és a falélekhez illesztés;
   - fúrási pontok (fogasok).
3. Péter jóváhagyásával **2–3 nyomdától, üvegestől vagy HPL-gyártótól ajánlat** (ajánlatkérés csak az ő „mehet”-jével).
4. A teljes legyártás előtt **A4-es anyagminta**: szín, élesség, anyag.
5. Gyártás, beépítés; a kép a renderen és a valóságban egyezzen (Render Reality Gate).

## 4. Első próba (javaslat)
Egy döntős stílusra: **zuhanyvégfal + TV-fal tapéta + egy kézzel befejezett vászon.** A stílust Péter választja.

## 5. Az első alkalmazás – A-902 fürdő, zuhanyvégfal (r1d)
- **Hely:** a walk-in zuhany vége (a Ny-i fal az ajtótól É-ra), pontosan a zuhany szélességében (≈ 85 cm), a padkától a belső sarokig. Padlótól a csempe tetejéig (2,85 m) ér, egy darabban, a fugákhoz igazítva, élzárva, a csempére ragasztva.
- **Áram nem kell:** a mennyezeti (ML10) spotsín egyik feje világítja.
- **Keretezett nyomat üveg mögött a zuhanyban nem jó:** a pára a keret alá jut, bepenészedik, bepárásodik, és olcsó hatású. Ugyanez az ötlet jól működik keret nélkül: a kép az üveg hátoldalára nyomtatva vagy festve, csiszolt éllel, a csempére ragasztva. Optiwhite (vasmentes) üvegen a minta torzítás és zöld árnyalat nélkül látszik.
- **Fogasok:**
  - üvegnél a furatokat az edzés **előtt** kell kifúrni, a tervben rögzített helyen; a fogas rozettával az üvegen ül, a csavar a falba megy (cső-/vezetékkeresővel);
  - akrilnál a furat utólag is fúrható;
  - alternatíva: külön, keskeny fogasléc a panel ajtó felőli élén.
  - A fogas a motívum része lehet, például a tusrajzág ágvégein.
- **Anyagdöntés:** nyitott (üveg ≈ 420 e / HPL ≈ 250 e / akril vagy alu-kompozit ≈ 120–180 e Ft). A fő keretben nincs benne – Péter dönt.
- **Részletek:** a `wsg/a902-furdo-r1b-20261025` ágon, `05_promptok/A902_furdo_r1b_20261025/` és a stílusspecifikációk 4. pontja.
