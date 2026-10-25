# Integrátori szövegcsere v1.2 (K-02, K-03) – Opus 5.5 V3.1 VÉGLEGES forrás (PR #22 @ 7d3c67f), négy induló prompt.
# Claude integrátor, 2026-10-25. A v1.1 (b24bee7-alapú) tervezet külön mappában marad; ez a végleges forrásra készült.
# A versenyzői fájlt NEM módosítja és régebbi termékválasztást NEM állít vissza: a 7d3c67f git-objektumából olvas,
# a javított példányt a kimeneti mappába írja. Minden csere pontos egyezés; ha egy régi szöveg nem pontosan egyszer szerepel,
# vagy a forrás sha256-ja nem a 7d3c67f-é, a szkript leáll.
# Futtatás: python3 -I apply_patch_v1_2.py <wsg-berendezes repó> <kimeneti mappa>
import sys, os, json, hashlib, subprocess

FORRAS_COMMIT = '7d3c67f823c646d9daef06b294826e89c1c61467'
UTVONAL = '05_promptok/KEP004_OPUS55_V3_1_r1/20_PROMPTOK/'
K02_TILTAS = 'a pendant lamp drawn at the right edge or anywhere above the dining table; '
K03_TILTAS = 'a plant, tree or any object standing in front of W02 or in the mouth of the bedroom corridor; '
ML04_KIVUL = ('The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; '
              'at most a faint warm spill of its light reaches the right edge of the floor and the table.')

PATCH = {
 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A': [
  ('K-02', 'The dining pendant at ML04 – the Kave Home Somar, Ø 76 cm, in pale synthetic fibre with fine steel rods – glows at the right edge.', ML04_KIVUL),
  ('K-02', 'Avoid these proven errors: a floor lighter or cooler than the real one;', 'Avoid these proven errors: ' + K02_TILTAS + 'a floor lighter or cooler than the real one;'),
 ],
 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A': [
  ('K-02', '; at the right edge the dining pendant at ML04, the Kave Home Idela pendant, Ø 26 cm smoked glass with a black marble detail, glows warm.', '. ' + ML04_KIVUL),
  ('K-02', 'Avoid these proven errors: a mirror showing an impossible reflection;', 'Avoid these proven errors: ' + K02_TILTAS + 'a mirror showing an impossible reflection;'),
 ],
 'A902_S01_KyotoInk_1_nappali-hero_Cam_12_A': [
  ('K-03', ' One tall dark-leafed plant in a matt black pot stands in the south-west corner beside W02, away from the camera position.', ''),
  ('K-03', 'Avoid these proven errors: a floor lighter or cooler than the real one;', 'Avoid these proven errors: ' + K03_TILTAS + 'a floor lighter or cooler than the real one;'),
 ],
 'A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A': [
  ('K-03', ' A tall olive tree in a matt cream pot stands in the corner beside W02, not in the walkway.', ''),
  ('K-03', 'Avoid these proven errors: a mirror with an impossible reflection;', 'Avoid these proven errors: ' + K03_TILTAS + 'a mirror with an impossible reflection;'),
 ],
}
sha = lambda b: hashlib.sha256(b).hexdigest()
REPO, KI = sys.argv[1], sys.argv[2]; os.makedirs(KI, exist_ok=True); naplo = dict(forras_commit=FORRAS_COMMIT, kepek={})
for kep, csere in PATCH.items():
    raw = subprocess.run(['git', '-C', REPO, 'show', f'{FORRAS_COMMIT}:{UTVONAL}{kep}.prompt.md'], capture_output=True, check=True).stdout
    t = raw.decode('utf-8')
    for kod, regi, uj in csere:
        n = t.count(regi)
        if n != 1: sys.exit(f'HIBA {kep} {kod}: a régi szöveg {n}× szerepel (1 kell): {regi[:90]}…')
        t = t.replace(regi, uj)
    for kod, regi, uj in csere:
        if uj and uj.strip('. ') not in t: sys.exit(f'HIBA {kep} {kod}: az új szöveg nem került be')
        if regi.strip(' ;.') in t and uj == '': sys.exit(f'HIBA {kep} {kod}: a törlendő mondat bent maradt')
    ki = t.encode('utf-8'); f = kep + '_v1_2.prompt.md'; open(os.path.join(KI, f), 'wb').write(ki)
    naplo['kepek'][kep] = dict(forras=f'{UTVONAL}{kep}.prompt.md @ {FORRAS_COMMIT[:7]}', forras_sha256=sha(raw), javitott_fajl=f, javitott_sha256=sha(ki),
                               karakter_elotte=len(raw.decode('utf-8')), karakter_utana=len(t), cserek=[c[0] for c in csere])
json.dump(naplo, open(os.path.join(KI, 'patch_v1_2_naplo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in naplo['kepek'].items(): print(k, v['forras_sha256'][:16], '→', v['javitott_sha256'][:16], v['karakter_elotte'], '→', v['karakter_utana'])
