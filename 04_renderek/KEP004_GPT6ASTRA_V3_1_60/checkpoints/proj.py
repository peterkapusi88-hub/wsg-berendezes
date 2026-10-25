import json, math, numpy as np
d=json.load(open('/home/claude/astra/03_blender/geometry_lock_A902_v2b.json'))
def R(rx,ry,rz):
    cx,sx=math.cos(rx),math.sin(rx);cy,sy=math.cos(ry),math.sin(ry);cz,sz=math.cos(rz),math.sin(rz)
    Rx=np.array([[1,0,0],[0,cx,-sx],[0,sx,cx]]);Ry=np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]]);Rz=np.array([[cz,-sz,0],[sz,cz,0],[0,0,1]])
    return Rz@Ry@Rx
def proj(cam,P,W=1600,H=1000):
    c=d['cameras'][cam]; M=R(*c['rot']); p=M.T@(np.array(P,float)-np.array(c['loc']))
    if p[2]>=0: return None
    f=c['lens_mm']/36.0
    x=0.5+f*p[0]/(-p[2])-c['shift_x']; y=0.5+(f*p[1]/(-p[2])-c['shift_y'])*W/H
    return (x*W,(1-y)*H,-p[2])
if __name__=='__main__':
    print(proj('Cam_02_Nappali_terasz',(3.67,8.05,0)),proj('Cam_02_Nappali_terasz',(4.44,8.0,2.53)),proj('Cam_02_Nappali_terasz',(3.71,6.27,1.2)))
