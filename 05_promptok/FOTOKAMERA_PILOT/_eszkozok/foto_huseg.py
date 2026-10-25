"""Fotóhűség-ellenőrzés: üres profi fotó vs. AI-val berendezett változat (A szint).

Használat:
  python3 -I foto_huseg.py <ures_foto.jpg> <eredmeny.png> <kimeneti_mappa> [zonak.json]

A zónák a képszélesség/-magasság arányában (0–1): olyan területek, ahol a promptnak
megfelelően NEM kerülhet bútor (mennyezet, üvegfal és kilátás, jobb fal + 05.3 ajtó,
kapcsolók). Ha a zónákba mégis bútor került, az is eltérésnek számít – szándékosan.

Mér: (1) képarány és kivágás (a legjobb illesztés eltolása/nagyítása),
(2) zónánként átlagos színeltolódás (Lab ΔE), (3) élegyezés (Canny-élek F1 2 px tűréssel),
(4) eltéréstérkép és egymás melletti összevetőlap.
"""
import json, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

DEFAULT_ZONES = {  # KZS_3726-506
    "mennyezet": [0.10, 0.00, 0.88, 0.16],
    "uvegfal_kilatas_bal": [0.23, 0.26, 0.40, 0.56],
    "teraszajto_kilatas": [0.42, 0.30, 0.56, 0.56],
    "jobb_fal_05-3_ajto": [0.66, 0.27, 0.88, 0.58],
    "kapcsolosor_jobb_elol": [0.92, 0.37, 0.99, 0.56],
    "bal_fal_szel": [0.00, 0.10, 0.05, 0.70],
}


def lab(a):
    a = a / 255.0
    a = np.where(a > 0.04045, ((a + 0.055) / 1.055) ** 2.4, a / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = a @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def edges(g):
    e = np.asarray(g.filter(ImageFilter.FIND_EDGES), dtype=float)
    return e > np.percentile(e, 92)


def _score(ref, out_l, W, H, s, dx, dy):
    r = ref.resize((round(W * s), round(H * s)), Image.BILINEAR)
    ox = (r.width - W) // 2 + dx
    oy = (r.height - H) // 2 + dy
    if ox < 0 or oy < 0 or ox + W > r.width or oy + H > r.height:
        return None, None
    c = r.crop((ox, oy, ox + W, oy + H))
    d = np.mean(np.abs(np.asarray(c.convert("L"), float)[::3, ::3] - out_l[::3, ::3]))
    return d, c


def best_fit(ref, out):
    """Kivágás/nagyítás keresése két lépésben (durva, majd finom); visszaadja az illesztett üres fotót."""
    W, H = out.size
    out_l = np.asarray(out.convert("L"), float)
    best = (1e9, 1.0, 0, 0)
    for s in np.arange(0.96, 1.081, 0.01):
        for dx in range(-32, 33, 8):
            for dy in range(-32, 33, 8):
                d, _ = _score(ref, out_l, W, H, s, dx, dy)
                if d is not None and d < best[0]:
                    best = (d, s, dx, dy)
    _, s0, dx0, dy0 = best
    for s in np.arange(s0 - 0.01, s0 + 0.0101, 0.0025):
        for dx in range(dx0 - 8, dx0 + 9, 2):
            for dy in range(dy0 - 8, dy0 + 9, 2):
                d, _ = _score(ref, out_l, W, H, s, dx, dy)
                if d is not None and d < best[0]:
                    best = (d, s, dx, dy)
    d, s, dx, dy = best
    _, aligned = _score(ref, out_l, W, H, s, dx, dy)
    return (d, round(float(s), 4), dx, dy), aligned


def main():
    ref_p, out_p, odir = sys.argv[1:4]
    zones = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else DEFAULT_ZONES
    os.makedirs(odir, exist_ok=True)
    out = Image.open(out_p).convert("RGB")
    ref0 = Image.open(ref_p).convert("RGB")
    W, H = out.size
    rep = {"ures_foto": os.path.basename(ref_p), "eredmeny": os.path.basename(out_p),
           "eredmeny_meret": [W, H], "ures_keparany": round(ref0.width / ref0.height, 3),
           "eredmeny_keparany": round(W / H, 3)}
    fit, ref = best_fit(ref0, out)
    rep["illesztes"] = {"atl_elteres": round(fit[0], 2), "nagyitas": fit[1], "dx_px": fit[2], "dy_px": fit[3]}
    A, B = np.asarray(ref, float), np.asarray(out, float)
    LA, LB = lab(A), lab(B)
    dE = np.sqrt(((LA - LB) ** 2).sum(-1))
    EA, EB = edges(ref.convert("L")), edges(out.convert("L"))
    from scipy.ndimage import binary_dilation  # noqa
    EAd, EBd = binary_dilation(EA, iterations=2), binary_dilation(EB, iterations=2)
    zr = {}
    for n, (x0, y0, x1, y1) in zones.items():
        sl = (slice(int(y0 * H), int(y1 * H)), slice(int(x0 * W), int(x1 * W)))
        p = (EB[sl] & EAd[sl]).sum() / max(EB[sl].sum(), 1)
        r = (EA[sl] & EBd[sl]).sum() / max(EA[sl].sum(), 1)
        zr[n] = {"dE_atlag": round(float(dE[sl].mean()), 1), "dE_p90": round(float(np.percentile(dE[sl], 90)), 1),
                 "L_eltolas": round(float((LB[sl][..., 0] - LA[sl][..., 0]).mean()), 1),
                 "el_F1": round(float(2 * p * r / max(p + r, 1e-6)), 2)}
    rep["zonak"] = zr
    hm = np.clip(dE * 6, 0, 255).astype(np.uint8)
    heat = Image.fromarray(np.stack([hm, np.zeros_like(hm), 255 - hm], -1))
    blend = Image.blend(out, heat, 0.45)
    d = ImageDraw.Draw(blend)
    for n, (x0, y0, x1, y1) in zones.items():
        d.rectangle([x0 * W, y0 * H, x1 * W, y1 * H], outline=(255, 255, 0), width=3)
        d.text((x0 * W + 4, y0 * H + 4), n, fill=(255, 255, 0))
    sheet = Image.new("RGB", (W * 3, H), "white")
    sheet.paste(ref, (0, 0)); sheet.paste(out, (W, 0)); sheet.paste(blend, (2 * W, 0))
    sheet.save(os.path.join(odir, "osszeveto_ures_eredmeny_elteres.jpg"), quality=88)
    json.dump(rep, open(os.path.join(odir, "foto_huseg.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps(rep, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
