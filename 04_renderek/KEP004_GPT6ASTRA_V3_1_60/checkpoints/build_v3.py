import copy, hashlib, json, shutil, os, sys
sys.path.insert(0,'/home/claude/work/build'); import build as B
OUT=B.OUT; IMG='/home/claude/work/out/img/'
FLOOR3=("real site photo of the EXISTING floor and skirting in this apartment – oak-effect planks in a cool grey-brown, photographed in cool daylight. Material and colour reference ONLY (not a camera, not a layout). "
        "In the result the floor must read as this same cool grey-brown oak with visible grain and knots: under warm evening light it may look slightly warmer, but never honey, orange-brown, reddish, whitened or dark-stained, and never replaced by another floor.")
def floor3(c):
    c['att']=[(p,n,FLOOR3 if '080_parketta' in n else r) for p,n,r in c['att']]; return c
def ident(path,name,cam_from):
    return (path,name,f"an earlier concept image of THIS SAME apartment in THIS SAME style (S01 Kyoto Ink), seen from a DIFFERENT camera ({cam_from}). Use it ONLY to keep the furniture, fronts, worktops, tall units, upholstery, table, chairs, lamps, artwork and materials identical to that view. Do NOT copy its camera, framing, perspective, room shape or layout – image 1 alone defines the geometry and the camera.")
def write(c,tag):
    pf=B.A+'/'+B.PD+c['id']+'.prompt.md'; prompt=open(pf,encoding='utf-8').read().rstrip('\n')
    msg=B.hdr(c)+prompt+"\n"; name=f"{c['nr']}_{c['id']}__ASTRA_V3_1__{tag}.txt"
    open(OUT+'/prompts_sent/'+name,'w',encoding='utf-8').write(msg)
    rd=f"/home/claude/work/upload/{c['cam']}_{tag}"; os.makedirs(rd,exist_ok=True)
    for src,n,r in c['att']: shutil.copyfile(src,rd+'/'+n)
    print(name,len(msg),hashlib.sha256(msg.encode()).hexdigest()); return name,rd
C={c['cam']:c for c in B.CAMS}
# --- Cam_03 v2: floor3 + identity ref Cam_12 v1 (Péter-preferált) ---
c=floor3(copy.deepcopy(C['Cam_03']))
c['att'].append(ident(IMG+'A902_S01_KyotoInk_1_nappali-hero_Cam_12_A__ASTRA_V3_1__v1.png','05_image5_A902_S01_Cam12_v1_butorazonossag_referencia.png','Cam_12, living-room hero'))
c['notes']=c['notes']+["- Image 5 keeps the kitchen fronts, tall units, worktop, dining table, chairs, pendant and W02 artwork identical to the Cam_12 view of this style; where image 5 and the creative brief differ in a design detail, follow image 5 for identity, image 1 for geometry."]
c['lock'][0]=c['lock'][0].replace('Same landscape 16:10 framing as image 1.','Same landscape 16:10 framing as image 1. The eye-level horizon (1.50 m) is at about 37 % from the top.')
w03=write(c,'v2')
json.dump(dict(Cam_03_v2=dict(msg=w03[0],refs=w03[1])),open('/home/claude/work/build/v3_out.json','w'))
