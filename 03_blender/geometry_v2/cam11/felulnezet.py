# 05.1 master – felülnézeti ellenőrző rajz: Cam_04 vs Cam_11 látómező, ágy-befoglalók, üvegfal, erkély, kiállások.
import json, math, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Arc, FancyArrowPatch
L = json.load(open('/home/claude/wsg-berendezes/03_blender/geometry_lock_A902_v2b.json'))
V = json.load(open('/home/claude/wsg-berendezes/01_alaprajzok/villamos_kiallasok/A902_villamos.json'))
fig, ax = plt.subplots(figsize=(13, 11), dpi=150)
X0, X1, Y0, Y1 = -2.35, 4.35, 3.0, 9.6
def rect(a, b, **kw): ax.add_patch(Rectangle((a[0], a[1]), b[0] - a[0], b[1] - a[1], **kw))
# erkély
for k, z in L['terrace_zones'].items():
    if k.startswith('erkely_13'):
        r = z['r']; rect((r[0], r[1]), (r[2], r[3]), facecolor='#eef1f4', edgecolor='#9aa5b1', lw=0.6, zorder=1)
ax.text(-1.6, 4.35, '13 ERKÉLY\npadló −0,15 m', ha='center', va='center', fontsize=8, color='#5a6570')
for k, v in L['terrace_v2'].items():
    if k.startswith('v2_Korlat_erkely'):
        rect((v[0], v[1]), (v[3], v[4]), facecolor='#3b3f44', edgecolor='none', zorder=3)
ax.text(-1.95, 7.0, 'pálcás korlát\nteteje +0,95 m\n(a szobapadlóhoz)', ha='left', va='center', fontsize=7.5, color='#3b3f44', rotation=0)
# falak
for k, w in L['walls'].items():
    if k.startswith('Plafon'): continue
    a, b = (w[0], w[1]), (w[3], w[4])
    if b[0] < X0 or a[0] > X1 or b[1] < Y0 or a[1] > Y1: continue
    low = w[5] < 2.5 and w[2] < 0.5
    szem = w[2] > 1.5
    rect(a, b, facecolor='#ffffff' if szem else '#5f6670', edgecolor='#5f6670', lw=0.5, hatch='////' if szem else None, zorder=4)
# üvegfal + profilok
for k, o in L['openings'].items():
    if 'Uvegfal_05_1' in k or 'Erkelyajto_05_2' in k:
        rect((o[0], o[1]), (o[3], o[4]), facecolor='#7cc6e8' if 'uveg' in k else '#ffffff', edgecolor='#2b6f99', lw=0.5, zorder=5)
ax.annotate('nyugati üvegfal 3,64 m (alj +0,05 / teteje +2,54)', xy=(-0.24, 6.1), xytext=(-2.25, 8.95), fontsize=8, color='#2b6f99',
            arrowprops=dict(arrowstyle='-', color='#2b6f99', lw=0.6))
# nyílások ívei
m = L['openings_meta']['Uvegfal_05_1_erkely']; hz = m['zsaner']
ax.add_patch(Arc((0.0, 4.28), 1.8, 1.8, theta1=0, theta2=90, color='#2b6f99', lw=0.8, ls='--', zorder=6))
ax.plot([0.0, 0.0], [4.28, 5.18], color='#2b6f99', lw=1.2, zorder=6)
ax.add_patch(Arc((3.494, 4.05), 1.8, 1.8, theta1=90, theta2=180, color='#6b7280', lw=0.8, ls='--', zorder=6))
ax.text(3.05, 4.25, 'ajtó 90', fontsize=7, color='#6b7280')
# PAX (modell, déli sáv)
rect((0.0, 3.45), (2.42, 4.02), facecolor='#f3f0e8', edgecolor='#a39e8f', lw=0.6, hatch='xx', zorder=5)
ax.text(1.21, 3.735, 'gardrób 2,42 (modell: PAX)', ha='center', va='center', fontsize=7, color='#6d685c', zorder=6)
# ágyak
rect((1.56, 5.10), (3.56, 6.90), facecolor='none', edgecolor='#555555', lw=1.0, ls=':', zorder=7)
ax.text(1.62, 5.16, 'modell: Agy_05_1_TÄLLÅSEN\n180×200 (tengely y 6,00)', fontsize=6.8, color='#444444', va='bottom', zorder=8)
rect((1.47, 5.10), (3.49, 6.90), facecolor='#ff6b0d22', edgecolor='#ff6b0d', lw=1.6, zorder=8)
ax.text(2.48, 6.55, 'NORDLI 180×202×30\n(IKEA HU, ellenőrzött 2026-10-24)\na modell ágyhelyén – NEM mozdítva', ha='center', va='center', fontsize=7.4, color='#b34700', zorder=9)
rect((3.49, 4.70), (3.57, 7.30), facecolor='#d91ac0', edgecolor='#d91ac0', lw=0.8, zorder=8)
ax.annotate('fejvég-befoglaló\nW260×H100×D8\n(Astra S01 H85 /\nS02 H100 – tervezett)', xy=(3.55, 7.0), xytext=(3.72, 6.35), fontsize=7, color='#a01290',
            arrowprops=dict(arrowstyle='-', color='#a01290', lw=0.6), zorder=9)
rect((1.59, 5.505), (3.57, 7.295), facecolor='none', edgecolor='#1a5cff', lw=1.3, ls='--', zorder=8)
ax.text(1.62, 7.33, 'tervrajz ágyhelye (brosúra + 1:50), tengely ≈ y 6,40', fontsize=7, color='#1a5cff', zorder=9)
for yy in (4.50, 6.90):
    rect((1.47, yy), (3.49, yy + 0.60), facecolor='#19bf4020', edgecolor='#19bf40', lw=0.6, zorder=6)
ax.text(2.55, 4.53, '60 cm szabad sáv', fontsize=6.5, color='#118a2e', zorder=7)
# kiállások 05.1
szin = dict(dugalj='#e07b00', kapcsolo='#1f9d3a', termosztat='#7a3db8', gyengearamu_aljzat='#c99700', mennyezeti_lampakiallas='#d11a1a')
for k in V['kiallasok']:
    if not str(k['helyiseg']).startswith('05.1'): continue
    t = k['tipus']; x = k['doboz_x_m'] or k['x_m']; y = k['doboz_y_m'] or k['y_m']
    if t not in szin: continue
    if t == 'mennyezeti_lampakiallas':
        ax.plot(x, y, marker='x', ms=9, mew=2, color=szin[t], zorder=10); ax.text(x + 0.08, y - 0.18, k['azonosito'].replace('A902-', ''), fontsize=7, color=szin[t], zorder=10)
    else:
        ax.plot(x, y, marker='s', ms=5, color=szin[t], zorder=10)
        if k['azonosito'][-3:] in ('D20', 'D22', 'K13', 'K14', 'D26', 'T02'):
            ax.text(x + (0.08 if x > 3 else 0.06), y + 0.05, k['azonosito'].replace('A902-', '') + (' (0,65 m)' if k['magassag_m'] == 0.65 else ''), fontsize=6.5, color=szin[t], zorder=10)
ax.text(3.62, 5.0, 'D22/D23 + K14\na modell ágyhelyén a fejvég\nmögé kerülnek', fontsize=6.6, color='#b00020', zorder=10)
# kamerák
def fov(nev, x, y, yaw_deg, hfov, szin_, hossz, cimke):
    import numpy as np
    angs = np.linspace(math.radians(yaw_deg - hfov / 2), math.radians(yaw_deg + hfov / 2), 40)
    pts = [(x, y)] + [(x + hossz * math.cos(a), y + hossz * math.sin(a)) for a in angs]
    ax.add_patch(Polygon(pts, closed=True, facecolor=szin_ + '22', edgecolor=szin_, lw=1.0, zorder=11))
    ax.add_patch(FancyArrowPatch((x, y), (x + 0.75 * math.cos(math.radians(yaw_deg)), y + 0.75 * math.sin(math.radians(yaw_deg))), arrowstyle='-|>', mutation_scale=14, color=szin_, lw=2, zorder=12))
    ax.plot(x, y, 'o', ms=8, color=szin_, zorder=12); ax.text(x, y - 0.22, cimke, ha='center', va='top', fontsize=8, color=szin_, fontweight='bold', zorder=12)
# Cam_04: yaw (x-tengelytől, CCW) = rz + 90°
fov('Cam_04', 0.35, 4.30, math.degrees(-0.7448) + 90, 84.0, '#7a7a7a', 3.3, '')
ax.text(0.80, 4.72, 'Cam_04 (meglévő)\n[0,35; 4,30; 1,50] 20 mm\nüvegfal a képen: 0 %', fontsize=7.6, color='#555555', fontweight='bold', zorder=12)
fov('Cam_11', 3.20, 6.10, math.degrees(math.pi / 2) + 90, 84.0, '#0b7a75', 3.75, '')
ax.text(2.05, 5.62, 'Cam_11 JAVASLAT\n[3,20; 6,10; 1,20] 20 mm\nüvegfal a képen: 38 %', fontsize=7.6, color='#0b7a75', fontweight='bold', zorder=12)
ax.text(-0.15, 9.45, 'É', fontsize=12, fontweight='bold', ha='center'); ax.annotate('', xy=(-0.15, 9.42), xytext=(-0.15, 9.0), arrowprops=dict(arrowstyle='-|>', lw=1.5))
ax.plot([2.35, 3.35], [9.45, 9.45], color='k', lw=2); ax.text(2.85, 9.5, '1 m', ha='center', fontsize=8)
rect((0.01, 8.05), (3.01, 8.95), facecolor='#1a5cff14', edgecolor='#1a5cff', lw=1.2, ls='-.', zorder=7)
ax.text(1.51, 8.62, 'GARDRÓBFAL-JAVASLAT az északi fülkében (Péter 22:37)\n≈3,00 × 0,90 × 2,90 m – front a pillér síkjában (y 8,05)\nnincs alatta hűtő-fűtő mező; D26/G05 hátfal-kivágással', ha='center', va='center', fontsize=7, color='#1a3fb3', zorder=9)
ax.set_xlim(X0, X1); ax.set_ylim(Y0, Y1); ax.set_aspect('equal'); ax.grid(True, lw=0.3, alpha=0.4)
ax.set_xlabel('x [m] (kelet →)'); ax.set_ylabel('y [m] (észak →)')
ax.set_title('A-902 · 05.1 master · Cam_04 vs Cam_11_Master_Panorama (JAVASLAT) · felülnézet, lock v2b-1-k10 · 2026-10-24', fontsize=10.5)
ax.text(-2.25, 3.08, 'Látóvonal az ágyból (ülve, szem ≈1,20 m – becslés): a korlát teteje −3,3°-kal a vízszintes alatt →\n'
        'a távoli panoráma (budai hegyek, tetőtáj; ME-BAL-077) a korlát fölött látszik. Fekve-félig ülve (≈0,90 m): a korlát\n'
        'szemmagasságban (+0,7°) – a közeli városkép a pálcák között. A modell égboltja egyszínű; a valós kilátást a fotó adja.',
        fontsize=7.3, color='#0b4f4c', va='bottom', ha='left', zorder=13, bbox=dict(facecolor='white', edgecolor='#0b7a75', lw=0.6, alpha=0.92))
plt.tight_layout(); plt.savefig('ellenorzes_05_1_felulnezet_Cam04_Cam11_v1.png', dpi=150)
print('ok')
