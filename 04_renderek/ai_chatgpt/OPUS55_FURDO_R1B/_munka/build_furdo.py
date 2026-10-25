import subprocess,hashlib,json,re,glob,os
REPO='/home/claude/wsg-berendezes'; C='252d924308b55a29284ddfc6345c85378a69daf4'
old=open(glob.glob(REPO+'/04_renderek/ai_chatgpt/OPUS55_V3_1_60_TESZT/uzenetek/06_*Cam_10_A.txt')[0]).read()
hdr=old.split('=== BEGIN PROMPT')[0]
F2="""   e) The tile joints, tile sizes and all sanitaryware stay exactly as in image 1.
   f) NEW in this run (see point 3): the floating vanity spans the far wall from the right-hand shaft-block corner (about 68 %) to the shower kerb line (about 35–37 %); the basin stays exactly in place (about 41–58 %). The glass panel stands on the kerb line, running from the far wall (about 30–37 %) towards the left edge of the frame. The glass is 200 cm high; its top stays below the upper edge of the tiling (2.85 m)."""
EXC=' Exception for this run: the creative brief ADDS three new built elements – a fixed 100 × 200 cm glass panel standing on the shower kerb from the far wall towards the camera (no door, open entry at the near end), a floating vanity on the far wall from the right-hand shaft-block corner to the glass (the existing basin stays exactly in place and is set into the counter, asymmetrically: narrow towel slot left, drawer block right), and a slim wall cabinet in the right-hand corner. Add them; everything already built stays exactly as in image 1.'
assert hdr.count('   e) The tile joints, tile sizes and all sanitaryware stay exactly as in image 1.')==1
hdr=hdr.replace('   e) The tile joints, tile sizes and all sanitaryware stay exactly as in image 1.',F2)
m=re.search(r'(3\. Forbidden:[^\n]*)',hdr); assert m
hdr=hdr.replace(m.group(1),m.group(1)+EXC)
plan=[]
files=sorted(subprocess.check_output(['git','-C',REPO,'ls-tree','-r','--name-only',C,'05_promptok/A902_furdo_r1b_20261025/promptok/']).decode().split())
for i,f in enumerate(files):
    kid=os.path.basename(f).replace('.prompt.md','')
    p=subprocess.check_output(['git','-C',REPO,'show',f'{C}:{f}']).decode()
    body=p[p.index('=== BEGIN PROMPT'):p.index('===',p.index('=== END PROMPT')+5)+3]
    h=hdr.replace('A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A',kid).replace('OPUS55-V3.1 · ','FÜRDŐ-R1B · ')
    h=re.sub(r'CREATIVE BRIEF – .*?:\n',f'CREATIVE BRIEF – Claude Opus 5.5 bathroom r1b prompt, verbatim and unchanged (source: wsg/a902-furdo-r1b-20261025 @ {C}, {f}):\n',h,flags=re.S)
    t=h+body+'\n'
    fn=f'{i+1:02d}_{kid}.txt'; open('/home/claude/furdo/uzenetek/'+fn,'w').write(t)
    plan.append(dict(nr=f'{i+1:02d}',kep_id=kid,kamera='Cam_10',verzio='v1',prompt_forras=f'wsg/a902-furdo-r1b-20261025 @ {C}, {f} (prompt sha256 {hashlib.sha256(p.encode()).hexdigest()})',
      csatolmanyok=['Cam_10_image1_A902_Alap-v2b1_blender_10_furdo-06-2.png','image2_A902_06-2_ME-BAL-064_zuhany_mosdo.jpg','photo_A902_06-2_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg'],
      uzenet=fn,uzenet_sha256=hashlib.sha256(t.encode()).hexdigest(),cel_fajl=kid+'__FURDO_R1B__v1.png'))
json.dump(plan,open('/home/claude/furdo/plan.json','w'),ensure_ascii=False,indent=1)
print(len(plan))
