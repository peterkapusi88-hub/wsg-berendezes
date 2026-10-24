#!/usr/bin/env python3
# KEP-004 · ChatGPT Images – az átvett képek archiválásának előkészítése a GitHubra (Claude, 2026-10-24).
# Csak MÁSOL: semmit nem töröl, nem nevez át és nem ír felül. Az ATVETELI_NAPLO.csv-t nem módosítja (azt Claude vezeti).
# Futtatás ebben a mappában: python3 archivalas_elokeszito.py probakor1 [--proba]
#   --proba: csak kiírja, mit tenne.
# Kimenet: _github_elokeszites/04_renderek/ai_chatgpt/STYLE10_KEP004/<kép-ID>.<kit> (+ _v2, _v3 … ismétlésnél),
#          mellette <kép-ID>.prompt.txt (a futtatott prompt a csomagból) és archiv_manifest_<kör>.json (sha256).
import os, sys, json, hashlib, shutil, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
KOR = ARGS[0] if ARGS else 'probakor1'
PROBA = '--proba' in sys.argv
CSOMAGOK = os.path.normpath(os.path.join(HERE, '..', '03_chatgpt_images_csomagok'))
CEL = os.path.join(HERE, '_github_elokeszites', '04_renderek', 'ai_chatgpt', 'STYLE10_KEP004')
KEP = ('.png', '.jpg', '.jpeg', '.webp')


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for blokk in iter(lambda: f.read(1 << 20), b''):
            h.update(blokk)
    return h.hexdigest()


def prompt_fajl(mappa_nev, kep_id):
    # a futtatott prompt a csomagból: 03_chatgpt_images_csomagok/<forduló>/<NN_kép-ID>/PROMPT_<kép-ID>.prompt.txt
    if not os.path.isdir(CSOMAGOK):
        return None
    for fordulo in sorted(os.listdir(CSOMAGOK)):
        p = os.path.join(CSOMAGOK, fordulo, mappa_nev, f'PROMPT_{kep_id}.prompt.txt')
        if os.path.exists(p):
            return p
    return None


def szabad_nev(kep_id, kit, forras_sha):
    # első kép: <kép-ID><kit>; további: <kép-ID>_v2<kit>, _v3 … – ha ugyanez a kép már archiválva van, azt adja vissza
    n = 1
    while True:
        nev = kep_id + ('' if n == 1 else f'_v{n}') + kit
        p = os.path.join(CEL, nev)
        if not os.path.exists(p):
            return nev, False
        if sha(p) == forras_sha:
            return nev, True
        n += 1


def main():
    gyoker = os.path.join(HERE, KOR)
    if not os.path.isdir(gyoker):
        print('Nincs ilyen átvételi forduló:', gyoker)
        return
    if not PROBA:
        os.makedirs(CEL, exist_ok=True)
    tetelek, jelentes = [], []
    for mappa_nev in sorted(os.listdir(gyoker)):
        mappa = os.path.join(gyoker, mappa_nev)
        if not os.path.isdir(mappa) or '_' not in mappa_nev:
            continue
        kep_id = mappa_nev.split('_', 1)[1]           # NN_<kép-ID> → <kép-ID>
        kepek = sorted((f for f in os.listdir(mappa) if f.lower().endswith(KEP) and not f.startswith('.')),
                       key=lambda f: os.path.getmtime(os.path.join(mappa, f)))
        if not kepek:
            jelentes.append(f'NINCS KÉP     {mappa_nev}')
            continue
        for f in kepek:
            forras = os.path.join(mappa, f)
            fs = sha(forras)
            kit = os.path.splitext(f)[1].lower()
            nev, mar = szabad_nev(kep_id, kit, fs)
            if mar:
                jelentes.append(f'MÁR ARCHIVÁLVA {mappa_nev}  {f} → {nev}')
            else:
                if not PROBA:
                    shutil.copy2(forras, os.path.join(CEL, nev))
                jelentes.append(f'{"PRÓBA" if PROBA else "MÁSOLVA"}       {mappa_nev}  {f} → {nev}')
            tetelek.append(dict(kep_id=kep_id, atveteli_fajl=f, archiv_nev=nev, sha256=fs, bajt=os.path.getsize(forras),
                                atveteli_mtime=datetime.datetime.fromtimestamp(os.path.getmtime(forras)).isoformat(timespec='seconds')))
        pf = prompt_fajl(mappa_nev, kep_id)
        if pf:
            cel_p = os.path.join(CEL, kep_id + '.prompt.txt')
            if not os.path.exists(cel_p):
                if not PROBA:
                    shutil.copy2(pf, cel_p)
                jelentes.append(f'{"PRÓBA" if PROBA else "MÁSOLVA"}       {mappa_nev}  prompt → {kep_id}.prompt.txt')
            elif sha(cel_p) != sha(pf):
                jelentes.append(f'FIGYELEM      {mappa_nev}  az archivált prompt eltér a csomagétól – nem írom felül, Claude dönt')
        else:
            jelentes.append(f'FIGYELEM      {mappa_nev}  nem találom a csomag promptját')
    if tetelek and not PROBA:
        mf = os.path.join(CEL, f'archiv_manifest_{KOR}.json')
        regi = json.load(open(mf, encoding='utf-8')) if os.path.exists(mf) else []
        ismert = {(t['archiv_nev'], t['sha256']) for t in regi}
        uj = regi + [t for t in tetelek if (t['archiv_nev'], t['sha256']) not in ismert]
        with open(mf, 'w', encoding='utf-8') as f:
            json.dump(uj, f, ensure_ascii=False, indent=1)
    print('\n'.join(jelentes) if jelentes else 'Nincs átvett kép.')


if __name__ == '__main__':
    main()
