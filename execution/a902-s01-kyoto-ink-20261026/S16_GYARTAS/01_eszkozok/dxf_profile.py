#!/usr/bin/env python3
"""DXF profil: verzió, egység, rétegek, entitások, blokkok, méretstílusok, szövegminták, lapok, kiterjedés."""
import sys, re
from collections import Counter
import ezdxf
from ezdxf import bbox

path = sys.argv[1]
doc = ezdxf.readfile(path)
msp = doc.modelspace()
print("FÁJL:", path)
print("DXF verzió:", doc.dxfversion, "| $INSUNITS:", doc.header.get("$INSUNITS"), "| $MEASUREMENT:", doc.header.get("$MEASUREMENT"))
print("$DIMSCALE:", doc.header.get("$DIMSCALE"), "| $LTSCALE:", doc.header.get("$LTSCALE"))

# rétegek
print("\nRÉTEGEK (%d):" % len(doc.layers))
for l in sorted(doc.layers, key=lambda x: x.dxf.name):
    def _lay(e):
        try:
            return e.dxf.layer
        except Exception:
            return "?"
    cnt = sum(1 for e in msp if _lay(e) == l.dxf.name)
    print(f"  {l.dxf.name:<28} szín={l.dxf.color:<4} lt={l.dxf.linetype:<14} lw={l.dxf.lineweight:<4} msp_ent={cnt}")

# entitások
c = Counter(e.dxftype() for e in msp)
print("\nMODELSPACE entitások (%d):" % sum(c.values()))
for k, v in c.most_common():
    print(f"  {k:<16} {v}")

# blokkok
blks = [b for b in doc.blocks if not b.name.startswith("*")]
print("\nBLOKKOK (%d nem névtelen):" % len(blks))
inserts = Counter(e.dxf.name for e in msp if e.dxftype() == "INSERT")
for b in sorted(blks, key=lambda b: -inserts.get(b.name, 0))[:40]:
    ents = Counter(e.dxftype() for e in b)
    print(f"  {b.name:<32} beillesztve={inserts.get(b.name,0):<4} tartalom={dict(ents.most_common(4))}")

# méretek
dims = [e for e in msp if e.dxftype() == "DIMENSION"]
print("\nMÉRETEK:", len(dims), "| stílusok:", Counter(d.dxf.dimstyle for d in dims).most_common(6))
print("DIMSTYLE-ok:", [(s.dxf.name, round(s.dxf.dimtxt,2), round(s.dxf.dimasz,2), s.dxf.dimdec, s.dxf.dimscale) for s in doc.dimstyles][:12])
print("TEXTSTYLE-ok:", [(s.dxf.name, s.dxf.font) for s in doc.styles][:12])

# szövegek
texts = []
for e in msp:
    if e.dxftype() == "TEXT":
        texts.append((e.dxf.layer, round(e.dxf.height, 1), e.dxf.text))
    elif e.dxftype() == "MTEXT":
        texts.append((e.dxf.layer, round(e.dxf.char_height, 1), e.plain_text()[:200]))
for b in blks:
    for e in b:
        if e.dxftype() in ("TEXT", "ATTDEF"):
            texts.append(("BLOCK:" + b.name, round(e.dxf.height, 1), e.dxf.text if e.dxftype()=="TEXT" else f"ATTDEF {e.dxf.tag}={e.dxf.text}"))
print("\nSZÖVEGEK (%d) – magasságok: %s" % (len(texts), Counter(t[1] for t in texts).most_common(8)))
seen = set()
shown = 0
for layer, h, t in texts:
    key = re.sub(r"\d+", "#", t)[:60]
    if key in seen or not t.strip():
        continue
    seen.add(key)
    print(f"  [{layer} h={h}] {t[:110]!r}")
    shown += 1
    if shown >= 70:
        break

# lapok
print("\nLAPOK (layouts):", [l.name for l in doc.layouts])
for lay in doc.layouts:
    if lay.name == "Model":
        continue
    ents = Counter(e.dxftype() for e in lay)
    vps = [e for e in lay if e.dxftype() == "VIEWPORT"]
    ps = lay.dxf_layout.dxf
    print(f"  {lay.name}: ent={dict(ents.most_common(6))} viewports={len(vps)} paper={getattr(ps,'paper_width',None)}x{getattr(ps,'paper_height',None)} {getattr(ps,'paper_units',None)}")
    for vp in vps[:12]:
        try:
            print(f"     VP center={tuple(round(v) for v in vp.dxf.center)} w={vp.dxf.width:.0f} h={vp.dxf.height:.0f} view_h={vp.dxf.view_height:.0f} scale≈1:{vp.dxf.view_height/vp.dxf.height:.1f}" if vp.dxf.height else "")
        except Exception as ex:
            print("     VP ?", ex)

# kiterjedés
try:
    ext = bbox.extents(msp, fast=True)
    print("\nMODELSPACE kiterjedés:", tuple(round(v) for v in ext.extmin), "->", tuple(round(v) for v in ext.extmax), "méret:", tuple(round(v) for v in ext.size))
except Exception as ex:
    print("extents hiba:", ex)
