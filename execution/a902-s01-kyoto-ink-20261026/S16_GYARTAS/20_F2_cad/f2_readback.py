#!/usr/bin/env python3
"""S16 F2 – AutoCAD MASSPROP visszaolvasás ↔ cad_terv.json.

Használat: python3 f2_readback.py <mappa a (s16-readback) által írt .mpr fájlokkal> [--smoke]
Minden $PART_ testre: térfogat (≤ 0,5 %) és befoglaló (≤ 0,05 mm) a tervhez képest, CAD-koordinátában (Y_CAD = -Y_helyi).
Kilépési kód 2, ha bármelyik hiányzik vagy eltér.
"""
import json, re, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
NUM = r"(-?[\d.]+(?:E[-+]?\d+)?)"


def parse_mpr(text):
    vol = re.search(r"Volume:\s*" + NUM, text)
    bb = {a: re.search(a + r":\s*" + NUM + r"\s*--\s*" + NUM, text) for a in "XYZ"}
    if not vol or not all(bb.values()):
        return None
    lo = [float(bb[a].group(1)) for a in "XYZ"]
    hi = [float(bb[a].group(2)) for a in "XYZ"]
    return float(vol.group(1)), np.array(lo), np.array(hi)


def expected():
    import f2_cad_export as F
    terv = json.loads((HERE / "cad_terv.json").read_text(encoding="utf-8"))["alkatreszek"]
    out = {}
    for it in terv:
        m = F.rebuild(it)
        lo, hi = m.bounds[0].copy(), m.bounds[1].copy()
        lo[1], hi[1] = -hi[1], -lo[1]
        out[it["reteg"].replace("$", "_").replace("#", "_")] = (abs(m.volume), lo, hi, it["id"])
    return out


ARC_VOL = (200 * 200 - (100 * 100 - 3.141592653589793 * 100 ** 2 / 4)) * 18
SMOKE = {  # várt értékek a (s16-smoketest)-hez, CAD-koordinátában
    "_PART_SMOKE_BOX_0000": (400 * 18 * 600, [0, -300, 0], [400, -282, 600]),
    "_PART_SMOKE_SUB_0000": (400 * 18 * 600 - 200 * 18 * 400, [1000, -300, 0], [1400, -282, 600]),
    # 200×200 profil, jobb alsó sarkán R100 negyedív (100,0)→(200,100); kihúzás 18 mm, tolás (600,-18,0)
    "_PART_SMOKE_ARC_0000": (ARC_VOL, [600, -36, 0], [800, -18, 200]),
}


def main(argv):
    d = Path(argv[0])
    smoke = "--smoke" in argv
    exp = {k: (v[0], np.array(v[1], float), np.array(v[2], float), k) for k, v in SMOKE.items()} if smoke else expected()
    rows, bad = [], 0
    for key, (v, lo, hi, pid) in sorted(exp.items()):
        f = d / f"{key}.mpr"
        if not f.exists():
            rows.append((pid, "HIÁNYZIK", "", "")); bad += 1; continue
        got = parse_mpr(f.read_text(errors="replace"))
        if not got:
            rows.append((pid, "NEM OLVASHATÓ", "", "")); bad += 1; continue
        gv, glo, ghi = got
        dv = (gv - v) / v * 100 if v else 0.0
        db = float(max(np.abs(glo - lo).max(), np.abs(ghi - hi).max()))
        ok = abs(dv) <= 0.5 and db <= 0.05
        bad += not ok
        rows.append((pid, "OK" if ok else "ELTÉR", f"{dv:.3f}%", f"{db:.3f} mm"))
    for r in rows:
        print(" | ".join(map(str, r)))
    print(f"\n{len(rows) - bad}/{len(rows)} egyezik")
    return 2 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
