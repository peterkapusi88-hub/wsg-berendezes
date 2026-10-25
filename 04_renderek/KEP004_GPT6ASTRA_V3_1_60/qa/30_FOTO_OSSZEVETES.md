# Profi fotók (2026-10-25) vs. Astra V3.1 renderek (S01–S05) – visszaellenőrzés

Claude, 2026-10-25 ~20:30. Forrás: GitHub `main` @ 1d59243, `08_allapotfelmeres/fotok_profi_20261025/A902/` (33 kép). A fotók retusáltak, EXIF nélkül → bizonyítékok anyagra, színre, nyílásra és kilátásra, de nem méretforrások.

Pixelpontos kameraegyezés nincs: a fotók nem a Blender-kamerákból készültek. A geometriát elemenként vetettem össze.

## Eredmény röviden
| Szempont | Ítélet | Részlet |
|---|---|---|
| Padló színe/rajzolata | **FAIL – rendszerszintű** | Valóság: világos–középszürke, hűvös, alacsony kontrasztú, egyenes erezetű tölgyhatás (fotók: L* 48–59, C* 3–11, b* −3…−10). Renderek: meleg mézbarna, erős göcsös rajzolat (C* 14–29, b* +10…+25), a nappali fényes Cam_03/Cam_12/Cam_11c képeken is. Legközelebb: S01 Cam_12, S01 Cam_11c (C* ~7). Ok: a ME-080 helyszíni fotó közeli, göcsös részlet, és a meleg fényleírás. |
| Fürdő 06.2 csempe | **eltérés** | Valóság: semleges hűvös szürke nagylap (C* ~0,5). Renderek: bézs/krém (C* 12–17). Részben a 2700–3500 K fény okozza, de így nem a meglévő burkolatot mutatja. |
| Fürdő relief fal | S01, S03 **hibás**; S02, S04, S05 jó | Valóság: hatszöges 3D relief. S01/S03: négyzetrácsos mozaik lett. |
| Nappali teraszüveg alja | **geometriai hiány (Blender + render)** | A fotókon (3659, 3708, 3726) a nappali/étkező üvegfala előtt belül végig egy kb. 10–15 cm magas (becslés), padlóburkolattal borított lépcső/dobogó fut. A Blender-modellben csak vékony fehér küszöb van; a renderekben az üveg a padlóig ér. → mérni kell, majd döntés után a modellbe (nem automatikusan a lockba). |
| Nappali üvegfal kiosztása | megfelel | Emelő-toló (HST) egység + fehér pillér + fix mező; a toló szárny belső éle sötét. A renderek fehér keretezése elfogadható. |
| Master üvegfal (Cam_11c) | **PASS** | Három mező, bal a nyíló szárny, téglafal-visszafordulás jobbra, fekete pálcás korlát, erkély-greslap: mind egyezik. |
| Kilátás | PASS (koncepció) | Pesti tetők, budai hegyek, torony egyezik. A fotón két daru is van (ideiglenes), a renderekből hiányzik – ez rendben van. |
| Terasz (Cam_02) | PASS | Világosszürke nagylap, magasabb WPC-dobogó lépcsőkkel, zöldtető, fekete korlát. A valós WPC-ládák melegebb barnák, a renderek sötétebbek – kis eltérés. |
| Ajtók, kapcsolók | PASS | Középszürke ajtólap, sötétebb tok, fekete kilincs, antracit kapcsolók. |
| Falak, mennyezet | PASS / megjegyzés | A valóságban tiszta fehér sík mennyezet van, spot és kávás LED nélkül. Néhány renderen (S02/S05 Cam_02) mennyezeti fénycsík jelent meg → a lock tiltja, jelölendő. |
| Lábazat | kis eltérés | Valóság: a padlóval egyező szürkésbarna lábazat. A renderek változók. |

## Javaslat (döntés kell)
1. **Padló-referencia csere a 30 hátralévő képhez:** a ME-080 helyett/mellett egy profi fotós padlókivágás (3726/3753), új szerepszöveggel: „light-to-mid cool grey oak effect, low contrast, straight fine grain, few knots; never honey/brown, even in warm evening light”.
2. **A kész S01–S05 képek padlója FAIL.** Három lehetőség:
   - koncepcióként maradnak;
   - célzott újragenerálás csak a padló javításával (kb. 30 kép, ChatGPT-keret);
   - fotókamerás (Cam_F) újrakezdés, amelyet a másik munkamenet holnapra már előkészített.
3. **Üvegfal előtti lépcső:** helyszíni méret (magasság, mélység, hossz), utána Blender v2b-1 javítás + validátor, külön PR-ban.
4. **Fürdő:** a lockba: „hexagonal 3D relief (not square mosaic), existing cool grey large tiles stay grey under warm light”.

Megjegyzés: a holnapi ChatGPT-keretre két feladat vár: a mi hátralévő 30 képünk és a másik munkamenet fotókamerás pilotja (KZS_3726). Ezek ugyanazt a keretet fogyasztják, sorrendet kell dönteni.
