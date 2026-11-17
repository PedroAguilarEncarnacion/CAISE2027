"""Collect evidence; never assign scientific support labels automatically."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
from engine import assess,canonical,digest
ROOT=Path(__file__).parent

def changes(a,b,path=''):
 if isinstance(a,dict) and isinstance(b,dict):
  out=[]
  for key in sorted(set(a)|set(b)):
   p=path+'/'+key
   if key not in a:out.append({'path':p,'change':'added','value':b[key]})
   elif key not in b:out.append({'path':p,'change':'removed','value':a[key]})
   else:out+=changes(a[key],b[key],p)
  return out
 if a!=b:return [{'path':path,'change':'modified','before':a,'after':b}]
 return []

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',required=True);args=parser.parse_args();out=Path(args.output_dir)
 if out.exists() and any(out.iterdir()):raise SystemExit('Refusing to overwrite a nonempty run directory; select a new directory.')
 frozen=json.loads((ROOT/'baseline/frozen_sha256.json').read_text())
 for name,expected in frozen.items():
  if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=expected:raise SystemExit('Frozen baseline changed: '+name)
 out.mkdir(parents=True,exist_ok=True)
 matrix=json.loads((ROOT/'baseline/evaluation_matrix.json').read_text());runs={};inputs={}
 for row in matrix['rows']:
  id=row['case_id']
  if id in runs:continue
  c=json.loads((ROOT/row['inputs']).read_text());inputs[id]=c;r=assess(c);runs[id]=r
  (out/(id+'.assessment.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 # Fresh interpreter processes examine execution reproducibility, not evaluator agreement.
 repetitions=[]
 for i in range(2):
  target=out/f'REP-01-{i+1}.json'
  subprocess.run([sys.executable,str(ROOT/'engine.py'),str(ROOT/'cases/A-01.json'),'--output',str(target)],check=True,capture_output=True)
  repetitions.append(json.loads(target.read_text()))
 pair_logs=[]
 for row in matrix['rows']:
  if row.get('parent_case'):
   parent=row['parent_case'];child=row['case_id']
   pair_logs.append({'parent':parent,'child':child,'input_delta':changes(inputs[parent],inputs[child]),'assessment_delta':changes(runs[parent],runs[child])})
 log={'baseline_sha256':digest(frozen),'engine_sha256':hashlib.sha256((ROOT/'engine.py').read_bytes()).hexdigest(),'python_version':sys.version,'case_results':{k:{'processing_status':v['processing_status'],'conclusion':v.get('conclusion'),'input_sha256':v.get('input_sha256'),'assessment_sha256':digest(v)} for k,v in runs.items()},'repetition_semantic_equal':canonical(repetitions[0])==canonical(repetitions[1]),'controlled_comparisons':pair_logs,'claim_judgments':'Not assigned automatically. Compare recorded evidence with baseline; diagnose discrepancies and complete independent CL2 review.'}
 (out/'execution_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
 (out/'human_review.json').write_text(json.dumps({'status':'pending','instructions':'An independent evaluator receives assessment snapshots, trace, declared methods and engine procedure, but not expected conclusions. Reconstruct each condition and conclusion. Record undocumented steps and separate software defects, specification gaps and insufficient foundation. Record reviewer identity and actual review; never fabricate agreement.','records':[{'claim':r['claim'],'case_id':r['case_id'],'reviewer':None,'reconstructed_conclusion':None,'missing_steps':None,'discrepancy_type':None,'assessment':'pending'} for r in matrix['rows']]},indent=2)+'\n')
 print('Evidence collected; independent interpretation pending. No CL support labels assigned.')
if __name__=='__main__':main()
