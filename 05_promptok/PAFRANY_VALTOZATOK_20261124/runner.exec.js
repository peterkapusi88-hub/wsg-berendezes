
const rr=await tools.exec_command({cmd:"python3 - <<'PY'\nimport pathlib,json\np=pathlib.Path('05_promptok/PAFRANY_VALTOZATOK_20261124');m=json.loads((p/'MANIFEST.json').read_text());jobs=[j for j in m['jobs'] if j['status']=='PENDING' and not (p/j['output']).exists()][:2]\nfor j in jobs:\n j['prompt_text']=(p/j['prompt']).read_text()\n cam=j['camera'];anchor=None\n if cam in ['Cam_12','Cam_03','Cam_02_DAY','LIVING_WINDOW','KITCHEN_HERO']:anchor='Cam_02' if j['apartment']=='A902' else 'LIVING_HERO'\n if cam=='Cam_03':anchor='Cam_12'\n if cam=='Cam_11c':anchor='Cam_04'\n if cam.endswith('_MEDIA'):anchor=cam.replace('_MEDIA','_HERO')\n if anchor:\n  f=p/'renders'/(j['apartment']+'_'+j['variant']+'_'+anchor+'_v1.png')\n  if f.exists():\n   j['inputs']=j['inputs'][:4];j['inputs'].append(str(f.resolve()));j['prompt_text']+='\\n\\nCONTINUITY INPUT. The last image is this exact new variant already generated in a different camera. Use its precise upholstery, cabinetry material map, artwork and lighting details for continuity, but never replace Image 1 camera with the last image.'\nprint(json.dumps(jobs))\nPY",max_output_tokens:16000});
const jobs=JSON.parse(rr.output);
const results=await Promise.allSettled(jobs.map(async j=>{
 const r=await tools.image_gen__imagegen({prompt:j.prompt_text,referenced_image_paths:j.inputs,transparent_background:false});
 const src=r.output_hint?.match(/as (\/.*?\.png) by default/)?.[1]; if(!src)throw Error("No generated path "+j.id);
 const q=s=>"'"+s.replace(/'/g,"'\\''")+"'";
 const save=await tools.exec_command({cmd:"python3 '05_promptok/PAFRANY_VALTOZATOK_20261124/save_result.py' "+q(j.id)+" "+q(src),max_output_tokens:1000});
 const meta=JSON.stringify({id:j.id,actual_inputs:j.inputs,actual_prompt:j.prompt_text,source:src});
 await tools.apply_patch("*** Begin Patch\n*** Add File: 05_promptok/PAFRANY_VALTOZATOK_20261124/renders/"+j.id+".execution.json\n+"+meta+"\n*** End Patch");
 return {id:j.id,result:r,save:save.output};
}));
for(const r of results){if(r.status==='fulfilled'){generatedImage(r.value.result);text(r.value.save);}else text({error:String(r.reason)});}

