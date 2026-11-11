#!/usr/bin/env python3
"""Összeszerelési útmutató (modulonként, lépésenként, ábrával) + egylapos műhelyi ellenőrzőlista – S16 és R16.

Az adatmodellből (parts_v1.json) és a vasalattervből (vasalat_terv.json) generálva: minden lépés felsorolja a beépülő
alkatrészeket (címke-ID, méret), a kötéseket (melyik lap melyikhez, mivel, hány db) és a vasalatot; az ábrán a lépés
alkatrészei színesek, a már beépítettek szürkék. STÁTUSZ: TERVI – a szerelési sorrend javaslat, műhelyi megerősítésre.

Futtatás: python3 szereles.py  → kimenet: <szekrény>_GYARTAS/60_szereles/<TAG>_osszeszerelesi_utmutato.pdf, ../muhelyi_proba_ellenorzolista.pdf
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.backends.backend_pdf import PdfPages  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402
from matplotlib import font_manager  # noqa: E402

HERE = Path(__file__).resolve().parent
EX = HERE.parent.parent
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_manager.fontManager.addfont(FONT)
matplotlib.rcParams["font.family"] = "DejaVu Sans"
TODAY = date.today().isoformat()

MODUL_SORREND = ["HATTER", "ALSO_KERET", "D1", "D2", "D3", "D4", "D5", "D6", "TORONY", "TORONY_KERET", "TV", "EGYEB"]
MODUL_NEV = {"HATTER": "Háttér és falsínek (először a falra)", "ALSO_KERET": "Alsó keret és íves sarokelemek",
             "TORONY": "Bal torony (korpusz, polcok, ajtók)", "TORONY_KERET": "Torony elülső kerete és íves zárói",
             "TV": "TV-mező", "EGYEB": "Fénytakarók, tálcák (LED)"}
LEPES = [  # (lépés neve, típus-szabály a megnevezésre)
    ("Alsó lap és oldalak – a korpusz váza", r"fenék(?!.*fiók)|alsó|oldal(?!.*fiók)|oldallap|korpuszoldal|osztó|középosztó"),
    ("Felső lap / tető", r"tető|fedő|sapka|felső(?!.*hát)"),
    ("Hátfal, szervizfedél", r"\bhát|hátlap|szervizfedél|háttérpanel|kazettahát|hordozó"),
    ("Polcok", r"polc"),
    ("Fiókdobozok (külön összeállítva, majd a sínre)", r"fiók|dobozelő"),
    ("Frontok és ajtók", r"front|ajtó|betét"),
    ("Keret, lécek, íves elemek", r"keret|léc|falsín|távtartó|sarok|záróelem|íves|réteg"),
    ("Fénytakarók, burkolatok", r"fény|tálca|baffle|visor|burkolat|tv-mező|sáv"),
]


def lepes_of(r):
    n = r["megnevezes"].lower()
    if r.get("mozgo_egyseg"):
        return 5 if re.search(r"front|ajtó|betét|textil|szövet", n) else 4
    for i, (_, rx) in enumerate(LEPES):
        if re.search(rx, n):
            return i
    a = r["helyi_rendszer"]["A_normal"]
    return 0 if a in ("+X", "-X") else 3 if a in ("+Z", "-Z") else 5 if a == "+Y" else 2


def box_faces(b):
    x, y, z, dx, dy, dz = b
    y, dy = -(y + dy), dy          # az R14 rendszer balkezes: Y tükrözés, hogy a torony bal oldalt legyen (mint a CAD-ben)
    P = [(x, y, z), (x + dx, y, z), (x + dx, y + dy, z), (x, y + dy, z), (x, y, z + dz), (x + dx, y, z + dz), (x + dx, y + dy, z + dz), (x, y + dy, z + dz)]
    F = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)]
    return [[P[i] for i in f] for f in F]


def draw(ax, parts, kesz, most, title):
    bb = [[b[0], -(b[1] + b[4]), b[2], b[3], b[4], b[5]] for b in (p["befoglalo_globalis"] for p in parts)]
    lo = [min(b[i] for b in bb) for i in range(3)]
    hi = [max(b[i] + b[i + 3] for b in bb) for i in range(3)]
    for p in parts:
        pid = p["id"]
        if pid in most:
            fc, ec, al = "#d9822b", "#5a3b12", 0.95
        elif pid in kesz:
            fc, ec, al = "#cfcac3", "#8a857e", 0.55
        else:
            continue
        ax.add_collection3d(Poly3DCollection(box_faces(p["befoglalo_globalis"]), facecolor=fc, edgecolor=ec, linewidths=0.4, alpha=al))
    span = max(hi[i] - lo[i] for i in range(3))
    c = [(lo[i] + hi[i]) / 2 for i in range(3)]
    ax.set_xlim(c[0] - span / 2, c[0] + span / 2); ax.set_ylim(c[1] - span / 2, c[1] + span / 2); ax.set_zlim(c[2] - span / 2, c[2] + span / 2)
    ax.view_init(elev=18, azim=-62)   # a szoba felől, balról
    ax.set_axis_off()
    ax.set_title(title, fontsize=9)


def build(name, base, tag, cim):
    doc = json.loads((base / "10_F1_adatmodell/parts_v1.json").read_text(encoding="utf-8"))
    vas = json.loads((base / "30_F2b_vasalat/vasalat_terv.json").read_text(encoding="utf-8"))
    P = doc["alkatreszek"]
    R = {r["id"]: r for r in P}
    kot = defaultdict(list)
    for k in vas.get("kotesek", []):
        if k.get("A") in R and k.get("B") in R:
            kot[k["A"]].append(k)
            kot[k["B"]].append(k)
    hw = Counter()
    hw_part = defaultdict(Counter)
    for h in vas["furatok"]:
        hw_part[h["alkatresz"]][h["funkcio"]] += 1
    for w in vas["vasalat"]:
        hw[w["tipus"]] += w.get("db", 1)
    mods = sorted({r["modul"] for r in P}, key=lambda m: MODUL_SORREND.index(m) if m in MODUL_SORREND else 99)
    out = base / "60_szereles"
    out.mkdir(exist_ok=True)
    pdfp = out / f"{tag}_osszeszerelesi_utmutato.pdf"
    kesz = set()
    lepesszam = 0
    with PdfPages(pdfp) as pdf:
        # címlap
        fig = plt.figure(figsize=(11.69, 8.27))
        fig.text(0.05, 0.92, f"{cim} – összeszerelési útmutató", fontsize=20, weight="bold")
        fig.text(0.05, 0.87, f"Rev {doc['modell_revizio']} · {TODAY} · TERVI – a sorrend javaslat, műhelyi megerősítésre", fontsize=10)
        lines = ["Sorrend: " + " → ".join(mods),
                 "Minden lépésnél: a beépülő alkatrészek (címke-ID = matrica = MPR-név), a kötések (melyik lap melyikhez, mivel, hány darab) és a vasalat.",
                 "Az ábrán narancs = ebben a lépésben kerül be, szürke = már kész. Nézet: a szoba felől, balról.",
                 "Kötések: Ø8×35 tipli (lapba 13 / élbe 25 mm), Ø6×30 tipli a keretléceknél, Minifix 15 (Häfele 262.26.174) az íves héjaknál – ragasztás a tipliknél.",
                 "Vasalat összesen: " + ", ".join(f"{k} {v}" for k, v in sorted(hw.items())),
                 "A pontos méretek, furatok és élzárás az alkatrészlapokon és a szabásjegyzékben; ez a füzet csak a sorrendet és a kapcsolatokat mutatja."]
        import textwrap
        yy = 0.80
        for t in lines:
            for ln in textwrap.wrap(t, 120):
                fig.text(0.05, yy, ln, fontsize=9.5); yy -= 0.032
            yy -= 0.012
        ax = fig.add_axes([0.40, 0.0, 0.6, 0.4], projection="3d")
        draw(ax, P, {r["id"] for r in P}, set(), "teljes szekrény")
        pdf.savefig(fig); plt.close(fig)
        for m in mods:
            mp = [r for r in P if r["modul"] == m]
            groups = defaultdict(list)
            for r in mp:
                groups[lepes_of(r)].append(r)
            for li in sorted(groups):
                lepesszam += 1
                most = {r["id"] for r in groups[li]}
                fig = plt.figure(figsize=(11.69, 8.27))
                fig.text(0.04, 0.94, f"{lepesszam}. lépés · {MODUL_NEV.get(m, 'Modul ' + m)} · {LEPES[li][0]}", fontsize=14, weight="bold")
                ax = fig.add_axes([0.52, 0.08, 0.46, 0.8], projection="3d")
                draw(ax, mp, kesz & {r['id'] for r in mp}, most, f"modul {m}")
                y = 0.88
                fig.text(0.04, y, "Alkatrészek:", fontsize=10, weight="bold"); y -= 0.035
                for r in sorted(groups[li], key=lambda r: r["cimke_id"])[:14]:
                    k = r["meret"]["kesz"]
                    fig.text(0.05, y, f"• {r['cimke_id']} – {r['megnevezes'][:38]} · {k['L']:g}×{k['W']:g}×{k['T']:g} · {r['anyag']['kod']}", fontsize=8.5); y -= 0.03
                if len(groups[li]) > 14:
                    fig.text(0.05, y, f"… további {len(groups[li]) - 14} db (szabásjegyzék)", fontsize=8.5); y -= 0.03
                y -= 0.01
                fig.text(0.04, y, "Kötések ebben a lépésben:", fontsize=10, weight="bold"); y -= 0.035
                seen = set()
                n_k = 0
                for pid in sorted(most):
                    for k in kot[pid]:
                        key = (k["A"], k["B"], k.get("el"))
                        if key in seen:
                            continue
                        other = k["B"] if k["A"] == pid else k["A"]
                        if other not in most and other not in kesz:
                            continue
                        seen.add(key)
                        txt = f"• {R[k['A']]['cimke_id']} → {R[k['B']]['cimke_id']}: {k['tipus'].replace('_', ' ').lower()}"
                        if k.get("db"):
                            txt += f", {k['db']} db"
                        if k.get("minifix"):
                            txt += f" + {k['minifix']} Minifix"
                        if n_k < 12:
                            fig.text(0.05, y, txt[:105], fontsize=8.5); y -= 0.03
                        n_k += 1
                if n_k > 12:
                    fig.text(0.05, y, f"… további {n_k - 12} kötés (vasalat_jelentes.md)", fontsize=8.5); y -= 0.03
                if n_k == 0:
                    alap = {3: ("• polc: 4 db Ø5 polctartó csapra fekszik (a furatsor ±32 mm-es állítást ad), rögzítés nélkül", "#333333"),
                            6: ("• léc/távtartó/íves elem: ragasztás + 4×30 mm csavar hátulról, kézi (nincs CNC-furat) – műhelyi megerősítésre", "#333333"),
                            2: ("• bontható hát: 3,5×16 mm csavar kb. 150 mm-enként a korpusz hátsó élébe – szervizhez oldható (kézi, nincs CNC-furat)", "#333333"),
                            5: ("• fiókfront: belülről a dobozelőn át 2–4 db 4×25 csavar + Blum T51.7601 frontrögzítő; ajtó: pánttal (lásd vasalat); hézag 3 mm", "#333333"),
                            7: ("• fénytakaró/burkolat: a LED-profil gyári klipszével / 3M ragasztószalaggal – termék kiválasztása után", "#333333")}
                    t_, col = alap.get(li, ("• nincs tervezett kötőelem ebben a lépésben – ragasztás/csavarozás műhelyi szokás szerint (NYITOTT)", "#b03a2e"))
                    fig.text(0.05, y, t_, fontsize=8.5, color=col); y -= 0.03
                y -= 0.01
                fv = Counter()
                for pid in most:
                    fv.update(hw_part[pid])
                if fv:
                    fig.text(0.04, y, "Furatok / vasalat ezeken a darabokon:", fontsize=10, weight="bold"); y -= 0.035
                    fig.text(0.05, y, ", ".join(f"{k.replace('_', ' ').lower()} {v}" for k, v in sorted(fv.items()))[:150], fontsize=8.5); y -= 0.03
                tip = {
                    0: "Tipp: a tiplit az élfuratba ragaszd, a vázat derékszögben, sík asztalon állítsd össze.",
                    1: "Tipp: a tető előtt ellenőrizd az átlókat (derékszög).",
                    3: "Tipp: polctartó a Ø5 furatsorba; a polc állítható ±32 mm.",
                    4: "Tipp: doboz = oldalon át 4×35 csavar + ragasztás; utána MOVENTO sín a jelölőfuratokra (37/165/261 mm), hátsó horog Ø6×10; zár és TIP-ON sablonnal.",
                    5: "Tipp: pánt Blum CLIP top – kehely Ø35, talp 37 mm-re az elülső éltől; utána hézagállítás (3 mm).",
                    6: "Tipp: a keretléceket Ø6 tiplivel és ragasztással; az íves héjhoz Minifix-szel (bontható).",
                }.get(li)
                if tip:
                    fig.text(0.04, 0.04, tip, fontsize=9, style="italic")
                fig.text(0.98, 0.01, f"{cim} · Rev {doc['modell_revizio']} · TERVI", fontsize=7, ha="right")
                pdf.savefig(fig); plt.close(fig)
                kesz |= most
    return pdfp, lepesszam, len(mods)


def checklist(path, rows):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    pdfmetrics.registerFont(TTFont("DV", FONT))
    pdfmetrics.registerFont(TTFont("DVB", FONT.replace("DejaVuSans.ttf", "DejaVuSans-Bold.ttf")))
    c = canvas.Canvas(str(path), pagesize=A4)
    W, H = A4
    y = H - 20 * mm
    c.setFont("DVB", 15); c.drawString(18 * mm, y, "Műhelyi próba – 10 perces ellenőrzőlista"); y -= 7 * mm
    c.setFont("DV", 9); c.drawString(18 * mm, y, f"WSG A-902 médiafal (S16 + R16) · {TODAY} · egy modul (javaslat: S16 D1 fiókos elem) végignézése"); y -= 10 * mm
    for title, items in rows:
        c.setFont("DVB", 11); c.drawString(18 * mm, y, title); y -= 6 * mm
        c.setFont("DV", 9.5)
        for it in items:
            c.rect(18 * mm, y - 1, 3.2 * mm, 3.2 * mm)
            c.drawString(24 * mm, y, it); y -= 6 * mm
        y -= 3 * mm
    c.setFont("DV", 8.5)
    c.drawString(18 * mm, 15 * mm, "Amit talál: fotó vagy egy mondat elég – egy körben javítjuk minden fájlban (DWG, lapok, Excel, MPR, matrica).")
    c.save()


def main():
    res = []
    for name, base, tag, cim in (("S16", EX / "S16_GYARTAS", "S16_R15C", "WSG A-902 · S16 médiafal"),
                                 ("R16", EX / "R16_GYARTAS", "R16_J", "WSG A-902 · R16 médiafal")):
        res.append((name,) + build(name, base, tag, cim))
    checklist(HERE / "muhelyi_proba_ellenorzolista.pdf", [
        ("1. Megnyitás a saját programjában", [
            "A DWG (01_DWG) megnyílik, a 3D modell és a lapok látszanak",
            "Az alkatrészeket felismeri ($PART_ rétegek) – ad szabásjegyzéket? (képernyőkép)",
            "A furatokat felismeri ($DIFF_OUT testek, CONNOBJ kötőelemek)",
            "Élkód a rétegnévben (pl. V0VV) – jó a sorrend? mit jelent nála az A?"]),
        ("2. Egy modul (S16 D1) végignézése", [
            "D1 korpuszoldal lapja: méret 337×402×18, élzárás, tipli- és Minifix-furatok stimmelnek",
            "Fiók: MOVENTO jelölőfuratok 37/165/261 mm, hátsó horog Ø6×10 – így szokta?",
            "Összeszerelési sorrend (füzet) – így rakná össze? mi hiányzik?",
            "Matrica: amit a gépe olvas (vonalkód = program neve?)"]),
        ("3. Gép és anyag", [
            "Kész minta-MPR + szerszámlista (vagy: a programja generálja a CNC-t a DWG-ből?)",
            "Anyag: Egger U741 korpusz 0,8 ABS, H1399 front 2 mm ABS – rendben? előmarás?",
            "Vasalat: Blum CLIP top 70T3750 + 177H3100E, MOVENTO 760H, Minifix 15, tipli Ø8×35 – ezeket használja?",
            "de_11090 = konfirmát? milyen polctartó?"]),
        ("4. Döntés a végén", [
            "Mit javítsunk elsőként (max. 3 dolog)",
            "Próbadarab: melyik alkatrészt vágja ki elsőnek (javaslat: D1-L oldal)"]),
    ])
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
