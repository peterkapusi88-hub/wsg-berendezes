import subprocess,hashlib,json,re,os
REPO='/home/claude/wsg-berendezes'; C=subprocess.check_output(['git','-C',REPO,'rev-parse','FETCH_HEAD']).decode().strip()
R1B='renders/a902-furdo-r1b-10 @ 7c137b0cf531e89d84b961795140575c1fa06bc2'
files=sorted(subprocess.check_output(['git','-C',REPO,'ls-tree','-r','--name-only',C,'05_promptok/A902_furdo_r1b_20261025/promptok_Cam10W_r1d/']).decode().split())
I1='image1_A902_06-2_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg'; I2='image2_A902_06-2_ME-BAL-064_zuhany_mosdo.jpg'
plan=[]
for i,f in enumerate(files):
    kid=os.path.basename(f).replace('.prompt.md','')
    p=subprocess.check_output(['git','-C',REPO,'show',f'{C}:{f}']).decode()
    i3=re.search(r'\((A902_S\d\d_[^)]*?__FURDO_R1B__v1\.png)\)',p).group(1)
    assert os.path.exists('/home/claude/furdo_d/ref/'+i3), i3
    body=p[p.index('=== BEGIN PROMPT'):p.index('===',p.index('=== END PROMPT')+5)+3]
    h=f"""WSG A-902 · FÜRDŐ-R1D · {kid} · camera Cam_10W (bathroom 06.2, reverse view towards the WC niche, the door and the shower end wall)
STATUS: CONCEPT TEST – NOT VALIDATED (KONCEPCIÓ – NEM VALIDÁLT)

0. METHOD: IMAGE-TO-IMAGE EDIT of image 1. Image 1 is the real site photo and it is the canvas: keep its exact camera position, wide-angle perspective, framing, walls, WC niche, WC, flush plate, ventilation unit, towel radiator, door frame, corridor and every tile joint. Only add or change what the creative brief below adds. Do not re-frame, zoom, crop, rotate or re-draw the room from another angle.

Please generate exactly ONE image – landscape, the same framing and 4:3 aspect as image 1, photorealistic, no text, no labels, no collage, no split view.

ATTACHED IMAGES, IN THIS ORDER
- Image 1 ({I1}): the real site photo ME-BAL-066 – the mandatory camera and geometry.
- Image 2 ({I2}): the real site photo ME-BAL-064 – tiles, hexagonal decor and black fittings only.
- Image 3 ({i3}): the approved render of the same style from the opposite camera – style continuity only (vanity, fronts, colours, materials, light mood); not a camera reference.

CREATIVE BRIEF – Claude Opus 5.5 bathroom r1d prompt, verbatim and unchanged (source: wsg/a902-furdo-r1b-20261025 @ {C}, {f}):

"""
    t=h+body+'\n'
    fn=f'{i+1:02d}_{kid}.txt'; open('/home/claude/furdo_d/uzenetek/'+fn,'w').write(t)
    plan.append(dict(nr=f'{i+1:02d}',kep_id=kid,kamera='Cam_10W',verzio='v1',
      modell='ChatGPT Images – „Kép létrehozása” eszköz; csevegőmodell: GPT-6 (gondolkodás: High); a képmodell külön neve a felületen nem látszik',
      prompt_forras=f'wsg/a902-furdo-r1b-20261025 @ {C}, {f} (prompt sha256 {hashlib.sha256(p.encode()).hexdigest()})',
      csatolmanyok=[I1,I2,i3+f' ({R1B})'],uzenet=fn,uzenet_sha256=hashlib.sha256(t.encode()).hexdigest(),cel_fajl=kid+'__FURDO_R1D__v1.png',i3=i3))
    assert subprocess.check_output(['git','-C',REPO,'show',f'{C}:{f}']).decode().strip().endswith(body.strip())
json.dump(plan,open('/home/claude/furdo_d/plan.json','w'),ensure_ascii=False,indent=1)
print(C,len(plan)); print([x['i3'][:30] for x in plan])
