import json,sys
import os
P={p['seq']:p for p in json.load(open('/home/claude/work/v32_plan.json'))+(json.load(open('/home/claude/work/v32_fix_plan.json')) if os.path.exists('/home/claude/work/v32_fix_plan.json') else [])}
T={'1':(2027661463,'ref_449','ref_347'),'2':(2027661477,'ref_372','ref_278')}
acts=[]
for arg in sys.argv[1:]:
    seq,tab,ri,rt=arg.split(':'); p=P[int(seq)]; tid=T[tab][0]; d='/home/claude/work/'+p['dir']
    acts.append({"name":"file_upload","input":{"tabId":tid,"ref":ri,"paths":[d+'/'+c['fajl'] for c in p['csatolmanyok']]}})
    acts.append({"name":"file_upload","input":{"tabId":tid,"ref":rt,"paths":[d+'/_msg.txt']}})
    acts.append({"name":"javascript_tool","input":{"tabId":tid,"action":"javascript_exec","text":f"const r=await wsgFill({len(p['csatolmanyok'])},'=== END PROMPT {p['kep_id']} ===');(JSON.parse(r).ok&&JSON.parse(r).tail)?r+' '+(await wsgSend('V32 {p['nr']}_{p['valtozat']} {p.get('verzio','v1')}')):r"}})
print(json.dumps(acts,ensure_ascii=False))
for arg in sys.argv[1:]:
    p=P[int(arg.split(':')[0])]; print(arg, p['nr'],p['valtozat'],p['kep_fajl'])
