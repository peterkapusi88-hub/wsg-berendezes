# Integrátori szövegcsere v1.1 (K-02, K-03) – Opus 5.5 V3.1 négy induló promptja. Claude integrátor, 2026-10-25.
# A versenyzői fájlt NEM módosítja: a bemeneti mappából olvas, a javított példányt a kimeneti mappába írja.
# Minden csere pontos szövegegyezés; ha egy régi szöveg nem pontosan egyszer szerepel, a szkript leáll (így a 7d3c67f-en is ellenőrizhető).
# Futtatás: python3 apply_patch_v1_1.py <Opus 20_PROMPTOK mappa> <kimeneti mappa>
import sys, os, json, hashlib

K02_TILTAS = 'a pendant lamp drawn at the right edge or anywhere above the dining table; '
K03_TILTAS = 'a plant, tree or any object standing in front of W02 or in the mouth of the bedroom corridor; '
ML04_KIVUL = ('The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; '
              'at most a faint warm spill of its light reaches the right edge of the floor and the table.')

PATCH = {
 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A': [
  ('K-02', 'The dining pendant at ML04 – the Kave Home Somar, Ø 76 cm, in pale synthetic fibre with fine steel rods – glows at the right edge.',
           ML04_KIVUL),
  ('K-02', 'Avoid these proven errors: a floor lighter or cooler than the real one;',
           'Avoid these proven errors: ' + K02_TILTAS + 'a floor lighter or cooler than the real one;'),
 ],
 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A': [
  ('K-02', '; at the right edge the dining pendant at ML04, the Kave Home Brisia pendant, one Ø 50 cm frosted glass globe on a brushed-brass rod, glows warm.',
           '. ' + ML04_KIVUL),
  ('K-02', 'Avoid these proven errors: a mirror showing an impossible reflection;',
           'Avoid these proven errors: ' + K02_TILTAS + 'a mirror showing an impossible reflection;'),
 ],
 'A902_S01_KyotoInk_1_nappali-hero_Cam_12_A': [
  ('K-03', ' One tall dark-leafed plant in a matt black pot stands in the south-west corner beside W02, away from the camera position.', ''),
  ('K-03', 'Avoid these proven errors: a floor lighter or cooler than the real one;',
           'Avoid these proven errors: ' + K03_TILTAS + 'a floor lighter or cooler than the real one;'),
 ],
 'A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A': [
  ('K-03', ' A tall olive tree in a matt cream pot stands in the corner beside W02, not in the walkway.', ''),
  ('K-03', 'Avoid these proven errors: a mirror with an impossible reflection;',
           'Avoid these proven errors: ' + K03_TILTAS + 'a mirror with an impossible reflection;'),
 ],
}
VAR_B24BEE7 = {  # a b24bee7-es alap sha256-ja – eltérésnél a csere még futhat, de a napló jelzi
 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A': '7096e13f81621ea7f400c2985fd8ad1ff8b4b9dcba0437f1928f855d993d369c',
 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A': 'dfd6ecf0476030151405018aa851cdc8e42c99884cb97ff1200b6d591f12d29f',
 'A902_S01_KyotoInk_1_nappali-hero_Cam_12_A': '914f0b9e8f0cc620e71cf75b3d225b3dac091ee8b31ce5d57283ee4ce9af46f4',
 'A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A': '5085ab2c7e70b1fe5cb962ad457dd481cdbedaeb4e873ff5b59b44b5c2287d20',
}
sha = lambda b: hashlib.sha256(b).hexdigest()
BE, KI = sys.argv[1], sys.argv[2]; os.makedirs(KI, exist_ok=True); naplo = {}
for kep, csere in PATCH.items():
    raw = open(os.path.join(BE, kep + '.prompt.md'), 'rb').read(); t = raw.decode('utf-8')
    for kod, regi, uj in csere:
        n = t.count(regi)
        if n != 1: sys.exit(f'HIBA {kep} {kod}: a régi szöveg {n}× szerepel (1 kell): {regi[:80]}…')
        t = t.replace(regi, uj)
    for kod, regi, uj in csere:
        if uj and uj not in t: sys.exit(f'HIBA {kep} {kod}: az új szöveg nem került be')
    ki = t.encode('utf-8'); open(os.path.join(KI, kep + '_v1_1.prompt.md'), 'wb').write(ki)
    naplo[kep] = dict(alap_sha256=sha(raw), alap_egyezik_b24bee7=sha(raw) == VAR_B24BEE7[kep], javitott_fajl=kep + '_v1_1.prompt.md',
                      javitott_sha256=sha(ki), karakter_elotte=len(raw.decode('utf-8')), karakter_utana=len(t), cserek=[c[0] for c in csere])
json.dump(naplo, open(os.path.join(KI, 'patch_v1_1_naplo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in naplo.items(): print(k, 'alap=b24bee7' if v['alap_egyezik_b24bee7'] else 'ALAP ELTÉR', v['javitott_sha256'][:16], v['karakter_elotte'], '→', v['karakter_utana'])
