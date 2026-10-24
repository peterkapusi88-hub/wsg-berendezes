# A Péter által 2026-10-24 18:01–18:16 között kért A-811 / A-812 alapelrendezések egy lapon (a terv_elrendezes_a811/a812 ellenőrzőjével).
# Futtatás: python3 elrendezes_dontes_lap.py → elrendezes_dontes_A811_A812.png
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kanape_meretproba_a8 as K, terv_elrendezes_a811 as T1, terv_elrendezes_a812 as T2
from PIL import ImageDraw
panelek = []

def fejlec(im, cim, sor1, sor2):
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, im.size[0], 60], fill=(255, 255, 255))
    dr.text((8, 4), cim, fill=(0, 0, 0), font=K.FB); dr.text((8, 22), sor1, fill=(20, 120, 40), font=K.F); dr.text((8, 41), sor2, fill=(60, 60, 60), font=K.FS)
    return im

A1 = K.lakas_adat('A811')
for e in [x for x in T1.EL if x['kod'] == 'T0SZ60_50']:
    r, akad = T1.ellenoriz(A1, e); cm = r['forgatokonyv']['B']['cel_max_szelesseg_m']
    panelek.append(fejlec(T1.rajz(A1, e, r, akad), 'A-811 · L 2,59 × 2,50 + szekrénysor 60 cm (T0SZ60_50)',
        'Péter döntéseivel MEGFELEL – a konyhába az asztal megkerülésével (elfogadva, 18:01)',
        (f"erkély 1: {cm['egyszárnyú erkélyajtó']:.2f} · erkély 2: {cm['kétszárnyú erkélyajtó']:.2f} (elfogadva, 18:10) · nézőtáv {r['nezotav_m']:.2f} · kanapé–TV {r['kanape_tv_sav_m']:.2f} · mögötte {r['kanape_mogott_m']:.2f} m").replace('.', ',')))
A2 = K.lakas_adat('A812')
for e in [x for x in T2.EL if x['kod'] in ('P812U', 'P812L')]:
    r, akad = T2.ellenoriz(A2, e); cm = r['forgatokonyv']['B']['cel_max_szelesseg_m']
    panelek.append(fejlec(T2.rajz(A2, e, r, akad), ('A-812 · U' if e['kod'] == 'P812U' else 'A-812 · L') + ' + szekrénysor 60 cm a fülkében (' + e['kod'] + ')',
        'Péter döntéseivel MEGFELEL – étkező a terv helyén (18:14)',
        (f"erkély: {cm['kétszárnyú erkélyajtó']:.2f} (mellékút) · konyha {cm['konyha (pult előtti sáv)']:.2f} a székek mellett · nézőtáv {r['nezotav_m']:.2f} · mögötte {r['kanape_mogott_m']:.2f} m").replace('.', ',')))
lab = ['MÉRETPRÓBA – nem stílusterv; terv szerinti geometria (PR #9 v2 lock), helyszínen nem mért. Péter döntései 2026-10-24 18:01–18:16: az étkező a terv helyén (lámpa alatt), a konyhába kerülővel / szűk résen;',
       'a nagy erkélyajtóhoz 0,75 m-es mellékút elfogadva; 60 cm mély szekrénysor a felső falon (A-811: x 0–4,90; A-812: a fülke 3,22 m-es hátfala), a kanapé annyival előrébb, hogy a szekrény éppen megközelíthető (0,50 m).',
       'A-811: a terv L-je 2,59 × 2,50; A-812: U 3,00 széles, rövid szár (1,70) a fix üveg előtt, hosszú (2,25) a másik oldalon – vagy L a hosszú szárral. TV a gyári blokkon. Részletek: MERETPROBA_KANAPE_A811_A812.md.']
K.lap(panelek, 'A-811 és A-812 – alapelrendezés Péter döntései szerint (2026-10-24)', lab).save(os.path.join(K.HERE, 'elrendezes_dontes_A811_A812.png'), optimize=True)
print('kész')
