#!/usr/bin/env python3
"""WSG A-902 médiafal – asztalosi csomag összeállítása (S16 + R16), átadási lappal.

Kimenet: ./kimenet/WSG_A902_mediafal_asztalos_csomag_<dátum>.zip  (a zip NEM kerül a repóba)
Szekrényenként: 01 DWG (3D modell + rajzlapok), 02 alkatrészlapok PDF, 03 szabásjegyzék XLSX, 04 matricák PDF,
05 MPR-tervezetek, 06 alkatrész-DXF, valamint 00_ATADASI_LAP.pdf a közös adatokkal és a nyitott pontokkal.
STÁTUSZ: TERVI – NEM GYÁRTÁSI KIADÁS. Kiküldés csak Péter „mehet”-je után.
"""
from __future__ import annotations

import json
import shutil
import zipfile
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX = HERE.parent.parent
CAB = [("S16", EX / "S16_GYARTAS", "S16_R15B"), ("R16", EX / "R16_GYARTAS", "R16_J")]
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def stats(base, tag):
    doc = json.loads((base / "10_F1_adatmodell/parts_v1.json").read_text(encoding="utf-8"))
    vas = json.loads((base / "30_F2b_vasalat/vasalat_terv.json").read_text(encoding="utf-8"))
    qa = json.loads((base / "10_F1_adatmodell/qa_report.json").read_text(encoding="utf-8"))
    blk = json.loads((base / "20_F2_cad/vasalat_blokkok.json").read_text(encoding="utf-8"))
    rb = (base / "20_F2_cad/mac_futtatas").glob("readback_eredmeny_*v6.txt")
    rbt = next(iter(sorted(rb)), None)
    rbl = rbt.read_text(encoding="utf-8").strip().splitlines()[-1] if rbt else "–"
    dq = (base / "40_F3F4_dokumentacio/dokumentacio_qa.md").read_text(encoding="utf-8")
    sev = {k: v for k, v in (qa.get("osszesites") or {}).items()} if isinstance(qa, dict) else {}
    if not sev:
        sev = {k: v for k, v in qa.items() if isinstance(v, int)}
    return {"rev": doc["modell_revizio"], "db": len(doc["alkatreszek"]), "furat": len(vas["furatok"]),
            "vasalat": sum(blk["blokkok"].values()), "blokkfajta": len(blk["blokkok"]), "lapok": blk["lapok"],
            "qa": sev, "readback": rbl, "dok_ok": "MINDEN EGYEZIK" in dq,
            "mpr": len(list((base / "40_F3F4_dokumentacio/mpr_tervezet").glob("*.mpr")))}


NYITOTT = {
    "S16": ["Pánt: bal toronyajtó keretszár 50/50 mm (R15B) → Blum 70T3750 + 177H3100E, B = 3 mm – Péter megbízásából Claude döntése, visszafordítható.",
            "Fiók: MOVENTO 760H3000S + T51.7601 + TIP-ON T60L7140 – a sínt Blum sablonnal csavarozzuk, gyári furatkép a végleges cikkszám után.",
            "21 él-él illesztés és 11 nem tiplis kötés (vasalat_jelentes.md) – kötőelem műhelyi döntés (etalon: Häfele 637.76.333/351).",
            "BG rejtett visszahajtások (2 db) – helyszíni/Blender ellenőrzés."],
    "R16": ["KI12-TV02CAP-01 fedő 3610 mm nyersen: 2800-as táblából nem jön ki – toldás vagy jumbo tábla (döntés kell).",
            "Mennyezeti rés 20 mm (2900 mm névleges belmagasság, helyszíni felmérés nincs).",
            "M02 dekorpanel élkezelése az R16-ban nincs megadva; falsík-eltolás FELTEVÉS (Y = 418 − Y_R16).",
            "Pánt: R16 saját választása – Blum 70T3550.TL + 173H7100, B = 5,5 mm."],
}
KOZOS = ["DWG-ben két színezés: a modelltérben bal oldalt a gyártási modell valós anyagszínekkel ($PART_ rétegek), jobbra 5,1 m-rel eltolva egy műhelyi másolat alkatrész-típusszínekkel (SZINES_* rétegek, mint a coo1.dwg) – ehhez saját rajzlap (L05_MUHELYI_SZINES). A gyártási adat csak a $PART_ rétegeken van.",
         "Élkód a DWG rétegnevében: hossz-él 1 (látszó) – hossz-él 2 – szél-él 1 – szél-él 2 (coo1.dwg mintájára) – FELTEVÉS.",
         "Vasalat cikkszámos blokként, sematikus burkoló geometriával – gyári 3D-re cserélhető.",
         "MPR: woodWOP 4.0 formátumú TERVEZET, csak furatok; kontúrmarás a szerszámtábla után. Gépi futtathatóság próbadarabbal igazolandó.",
         "Anyag-, élzáró- és táblaméret-feltevések: gyartasi_szabalyok_v1.json – az asztalos válaszai után újragenerálható."]


def atadasi_lap(path, S):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    pdfmetrics.registerFont(TTFont("DV", FONT))
    pdfmetrics.registerFont(TTFont("DVB", FONT_B))
    h1 = ParagraphStyle("h1", fontName="DVB", fontSize=15, leading=19)
    h2 = ParagraphStyle("h2", fontName="DVB", fontSize=10.5, leading=14, spaceBefore=8)
    p = ParagraphStyle("p", fontName="DV", fontSize=8.5, leading=11)
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm, topMargin=14 * mm, bottomMargin=14 * mm)
    E = [Paragraph("WSG A-902 médiafal – asztalosi adatcsomag", h1),
         Paragraph(f"S16 és R16 szekrény · {date.today().isoformat()} · <b>TERVI – NEM GYÁRTÁSI KIADÁS</b> · Kapusi Péter / Claude (AI)", p),
         Spacer(1, 6)]
    rows = [["", "S16", "R16"],
            ["Modell-revízió", S["S16"]["rev"], S["R16"]["rev"]],
            ["Alkatrész (3D test, $PART_ réteg)", S["S16"]["db"], S["R16"]["db"]],
            ["Furat (TECH_ test + MPR)", S["S16"]["furat"], S["R16"]["furat"]],
            ["Vasalat-blokk beillesztés / fajta", f"{S['S16']['vasalat']} / {S['S16']['blokkfajta']}", f"{S['R16']['vasalat']} / {S['R16']['blokkfajta']}"],
            ["Rajzlap (DWG layout, SH_STAMP)", len(S["S16"]["lapok"]), len(S["R16"]["lapok"])],
            ["MPR-tervezet fájl", S["S16"]["mpr"], S["R16"]["mpr"]],
            ["AutoCAD visszaolvasás (térfogat ≤0,5 %, befoglaló ≤0,05 mm)", S["S16"]["readback"], S["R16"]["readback"]],
            ["Adatmodell-QA", ", ".join(f"{k} {v}" for k, v in S["S16"]["qa"].items()), ", ".join(f"{k} {v}" for k, v in S["R16"]["qa"].items())],
            ["Dokumentum-egyezés (MPR=Excel=PDF=DXF)", "egyezik" if S["S16"]["dok_ok"] else "ELTÉR", "egyezik" if S["R16"]["dok_ok"] else "ELTÉR"]]
    t = Table([[Paragraph(str(c), p) for c in r] for r in rows], colWidths=[72 * mm, 52 * mm, 52 * mm])
    t.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, 0), "DVB"), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3B3530")),
                           ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBFBF")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    E += [t, Paragraph("Tartalom szekrényenként", h2)]
    for line in ["01_DWG – 3D szerkezeti modell (AutoCAD 2018): alkatrészenként tömör test a km.dwg rétegrendjében "
                 "($PART_&lt;címke&gt;˙0˙0¨&lt;élkód&gt;˙0¨#0¨&lt;szám&gt;), furatok TECH_* testként, vasalat cikkszámos blokként ($ITEM_REF / $ART_), "
                 "A4 rajzlapok 3 nézettel és SH_STAMP pecséttel.",
                 "02 – alkatrészlapok (PDF, alkatrészenként 1 oldal: kontúr, A/B oldali és élfuratok, élzárás, ütköző, szálirány, furattábla).",
                 "03 – szabásjegyzék (XLSX): kész / élzárás előtti / nyers méret, élek, furatszám, MPR-név, anyag- és vasalat-összesítő, furatlista.",
                 "04 – matricák 100×50 mm, Code128 = címke-ID = MPR-programnév alapja.",
                 "05 – MPR-tervezetek (woodWOP), 06 – alkatrészenkénti DXF (kontúr, furatok, élzárás rétegeken)."]:
        E.append(Paragraph("• " + line, p))
    E.append(Paragraph("Közös feltevések", h2))
    E += [Paragraph("• " + x, p) for x in KOZOS]
    for k in ("S16", "R16"):
        E.append(Paragraph(f"{k} – nyitott / döntés", h2))
        E += [Paragraph("• " + x, p) for x in NYITOTT[k]]
    E.append(Paragraph("Amire a műhelytől szükség van a gépi kiadáshoz", h2))
    E += [Paragraph("• " + x, p) for x in [
        "egy működő minta-MPR és a szerszámtábla (marók, fúrók), a gép ütköző- és nullpont-konvenciója",
        "lapanyag- és élzáró-termékek (vastagság, előmarás), táblaméret, a szokásos vasalat cikkszámai",
        "a rétegnév él-kódjának pontos sorrendje és az „A” jel jelentése, matrica/vonalkód-tartalom, minimális alkatrészméret"]]
    doc.build(E)


def main():
    out = HERE / "kimenet"
    if out.exists():
        shutil.rmtree(out)
    root = out / f"WSG_A902_mediafal_asztalos_csomag_{date.today().strftime('%Y%m%d')}"
    S = {}
    for name, base, tag in CAB:
        S[name] = stats(base, tag)
        d = root / name
        (d / "01_DWG").mkdir(parents=True)
        shutil.copy(base / f"20_F2_cad/{tag}_szerkezet_v6.dwg", d / "01_DWG")
        doc_dir = base / "40_F3F4_dokumentacio"
        shutil.copy(doc_dir / f"{tag}_alkatreszlapok.pdf", d / f"02_{tag}_alkatreszlapok.pdf")
        shutil.copy(doc_dir / f"{tag}_szabasjegyzek.xlsx", d / f"03_{tag}_szabasjegyzek.xlsx")
        shutil.copy(doc_dir / f"{tag}_cimkek.pdf", d / f"04_{tag}_cimkek.pdf")
        shutil.copytree(doc_dir / "mpr_tervezet", d / "05_MPR_tervezet")
        shutil.copytree(doc_dir / "dxf_alkatreszek", d / "06_DXF_alkatreszek")
    atadasi_lap(root / "00_ATADASI_LAP.pdf", S)
    z = out / (root.name + ".zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(root.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(out))
    print(z, round(z.stat().st_size / 1e6, 1), "MB")
    print(json.dumps(S, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
