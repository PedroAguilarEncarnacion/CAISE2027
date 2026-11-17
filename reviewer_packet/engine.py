"""Reference v2: deterministic reconstruction of explicitly curated grounds.
Not an estimator, policy, autonomous argument evaluator or empirical validator.
"""
import argparse,copy,hashlib,json
from pathlib import Path

VERSION='2.0'
DS=('D01','D02','D03','D04','D05','D06')
KINDS={'source','method','need','context','intervention','reference','evidence','warrant','inference','consequence','relevance_warrant','reason','priority','assumption','coverage','review','objection','tension','missing_information','uncertainty','response','constraint','uncertainty_analysis'}
SINGLE_REFS=('method','judgment_method','source','target','addresses','response','priority','precedence_warrant','binding_warrant','exclusion_warrant','uncertainty_analysis')

def canonical(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'))
def digest(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def refs(n):
    out=list(n.get('refs',[]))
    for key in SINGLE_REFS:
        if n.get(key):out.append(n[key])
    return sorted(set(out))

def validate(c):
    errors=[]
    if not isinstance(c,dict):return ['Input must be an object']
    if c.get('schema_version')!='2.0' or c.get('criterion')!='SC1.1':errors.append('Unsupported schema or criterion')
    nodes=c.get('nodes')
    if not isinstance(nodes,list) or not all(isinstance(n,dict) for n in nodes):return errors+['nodes must be a list of objects']
    ids=[n.get('id') for n in nodes]
    if not all(isinstance(i,str) and i for i in ids):return errors+['IDs must be nonempty strings']
    if len(ids)!=len(set(ids)):errors.append('Duplicate node ID')
    idx={n['id']:n for n in nodes}
    for n in nodes:
        if n.get('kind') not in KINDS:errors.append('Unknown kind: '+n['id'])
        if not n.get('content') or not n.get('version'):errors.append('Missing content/version: '+n['id'])
        if not isinstance(n.get('refs',[]),list):errors.append('Invalid refs: '+n['id']);continue
        for ref in refs(n):
            if ref not in idx:errors.append(f"Broken reference {n['id']} -> {ref}")
        if n.get('information_state','available') not in ('available','absent','uncertain','not_measured','incompatible'):errors.append('Invalid information state: '+n['id'])
        if any(d not in DS for d in n.get('affects',[])):errors.append('Unknown affected condition: '+n['id'])
        if n['kind'] in ('inference','warrant','relevance_warrant','response','constraint','uncertainty_analysis') and not n.get('method'):errors.append('Missing judgment method: '+n['id'])
        if n['kind']=='response' and n.get('judgment') not in ('accepted','not_established','rejected'):errors.append('Unknown response judgment: '+n['id'])
        if n['kind']=='constraint':
            for key in ('origin','authority','scope','exceptions','applicability','compliance'):
                if not n.get(key):errors.append('Missing constraint '+key+': '+n['id'])
            if n.get('applicability') not in ('applicable','not_applicable','unknown'):errors.append('Invalid applicability')
            if n.get('compliance') not in ('complied','violated','unknown'):errors.append('Invalid compliance')
        if n['kind']=='uncertainty_analysis':
            alts=n.get('alternatives',[])
            if not n.get('plausibility_basis') or len(alts)<2 or any(not isinstance(a.get('supports_premise'),bool) for a in alts):errors.append('Incomplete plausible-alternatives analysis: '+n['id'])
    claim=c.get('claim',{})
    for key in ('id','version','level','need','candidate','context','reference','horizon','actor','coverage'):
        if not claim.get(key):errors.append('Missing claim '+key)
    for key in ('need','candidate','context','reference'):
        if claim.get(key) not in idx:errors.append('Broken claim '+key)
    if claim.get('level') not in ('individual','contextual'):errors.append('Invalid claim level')
    if claim.get('id') in idx or any(i in DS or i.startswith('GEN:') for i in idx):errors.append('Reserved identifier collision')
    for key in DS:
        if key in c:errors.append('Precomputed condition prohibited: '+key)
    return errors

def assess(case):
    errors=validate(case)
    if errors:return {'processing_status':'invalid','validation_report':errors}
    c=copy.deepcopy(case);idx={n['id']:n for n in c['nodes']};claim=c['claim'];generated=[];conditions=[]
    def kinds(*ks):return sorted([n for n in idx.values() if n['kind'] in ks],key=lambda n:n['id'])
    def closure(ids):
        seen=set();stack=list(ids)
        while stack:
            id=stack.pop()
            if id in seen:continue
            seen.add(id);stack.extend(idx[id].get('refs',[]))
        return seen
    def scoped(n):return not (claim['level']=='individual' and n.get('scope')!='individual')
    def gen(id,kind,text,targets,affects,decisive=True,**kw):
        n={'id':'GEN:'+id,'version':VERSION,'kind':kind,'content':text,'refs':sorted(set(targets)),'affects':list(affects),'status':'open','decisive':decisive,'method_origin':'engine-'+VERSION,**kw};generated.append(n);return n
    # Available-but-uncertain is distinct from absent. Alternatives are curated inputs.
    for n in kinds('evidence','consequence'):
        state=n.get('information_state','available')
        if state in ('absent','not_measured','incompatible'):
            gen('INFO:'+n['id'],'missing_information' if state!='incompatible' else 'uncertainty','Required premise state: '+state,[n['id']],['D06'],information_state=state)
        elif state=='uncertain':
            analysis=idx.get(n.get('uncertainty_analysis'));supported=False
            if analysis and analysis.get('target')==n['id'] and scoped(analysis):supported=all(a['supports_premise'] for a in analysis['alternatives'])
            targets=[n['id']]+([analysis['id']] if analysis else [])
            gen('UNC:'+n['id'],'uncertainty','Uncertainty retained; support stable only over declared curated alternatives.' if supported else 'Uncertainty unresolved over declared alternatives or analysis missing.',targets,['D06'],decisive=not supported,information_state='uncertain',robustness_scope='Only supplied alternatives; no universal robustness')
    def premise_supported(n):
        if n.get('information_state') in ('absent','not_measured','incompatible'):return False
        if n.get('information_state')=='uncertain':
            a=idx.get(n.get('uncertainty_analysis'))
            return bool(a and a.get('target')==n['id'] and scoped(a) and all(v['supports_premise'] for v in a['alternatives']))
        return True
    # Reconstruct practical reasons from consequences plus declared relevance warrant.
    reasons=kinds('reason')
    for w in kinds('relevance_warrant'):
        for con in kinds('consequence'):
            if con['id'] not in w.get('refs',[]):continue
            if not any(w['id'] in r.get('refs',[]) for r in reasons):
                reasons.append({'id':'GEN:REASON:'+w['id'],'version':VERSION,'kind':'reason','content':'Reason reconstructed from supplied consequence and relevance warrant.','refs':[con['id'],w['id']],'direction':w.get('direction','limiting'),'method_origin':'engine-'+VERSION})
    # Priority never resolves tension by itself. An accepted directed response also needs WP.
    priorities=[]
    for p in kinds('priority'):
        wp=idx.get(p.get('precedence_warrant'))
        priorities.append({'id':p['id'],'declared':bool(p.get('declared')),'applicable':bool(p.get('applicable')),'precedence_documented':bool(wp and wp.get('accepted_cost') and wp.get('limits') and scoped(wp)),'precedence_warrant':p.get('precedence_warrant'),'limits':'Document presence does not establish validity; directed response still required.'})
    def resolved(i):
        ans=idx.get(i.get('response'))
        if not ans or ans['kind']!='response' or ans.get('addresses')!=i['id'] or ans.get('judgment')!='accepted' or not scoped(ans):return False
        if not ans.get('refs') or not ans.get('method'):return False
        if i.get('priority'):
            p=next((p for p in priorities if p['id']==i['priority']),None)
            if not p or not p['declared'] or not p['applicable'] or not p['precedence_documented'] or p['precedence_warrant'] not in refs(ans):return False
        return True
    issues=[]
    for n in sorted([n for n in idx.values() if n.get('affects')],key=lambda n:n['id']):
        i=copy.deepcopy(n);i['resolution_supported']=resolved(i);issues.append(i)
    issues+=generated
    def is_blocking(i):return i.get('decisive',False) and i.get('status')=='open' and not i.get('resolution_supported',False)
    def record(d,grounds,requirements,state=None):
        affected=[i for i in issues if d in i.get('affects',[])]
        blockers=sorted(i['id'] for i in affected if is_blocking(i))
        checks=[{'requirement':name,'met':bool(ok),'explanation':why} for name,ok,why in requirements]
        outcome=state or ('supported' if all(v['met'] for v in checks) and not blockers else 'not_established')
        conditions.append({'condition':d,'state':outcome,'grounds':sorted(set(grounds)),'checks':checks,'issue_ids':sorted(i['id'] for i in affected),'blocking_issue_ids':blockers,'method':'CURATED-RELATIONAL-RECONSTRUCTION-2.0'})
    # C1/C2 role-based chains; no special case identifiers.
    for d,role in [('D01','need_support'),('D02','candidate_contribution')]:
        ins=[n for n in kinds('inference') if n.get('role')==role];grounds=[];valid=[]
        for n in ins:
            deps=closure([n['id']]);grounds+=sorted(deps)
            ev=[idx[id] for id in deps if idx[id]['kind']=='evidence']
            warrants=[idx[id] for id in deps if idx[id]['kind'] in ('warrant','relevance_warrant')]
            need_match=claim['need'] in deps
            if role=='candidate_contribution':
                need_match=need_match and claim['candidate'] in deps and any(idx[id]['kind']=='consequence' for id in deps)
            valid.append(scoped(n) and need_match and bool(ev) and bool(warrants) and all(premise_supported(idx[id]) for id in deps))
        record(d,grounds,[('Explicit typed chain within claim scope',any(valid),'Need/candidate links, evidence, warrant, scope and premise information are checked; substantive warrants remain curated judgments.')])
    cons=kinds('consequence');ws=kinds('relevance_warrant');cov=kinds('coverage')
    relevant=all(n.get('actor') and n.get('objective') and n.get('horizon') and n.get('method') and any(n['id'] in w.get('refs',[]) and w.get('direction') in ('supporting','opposing','limiting') for w in ws) for n in cons)
    record('D03',[n['id'] for n in cons+ws+cov],[('Known consequence relevance documented',bool(cons) and relevant,'Actor, objective, horizon and relevance warrant retained.'),('Coverage declared',bool(cov),'No claim of complete consequences.')])
    opposition=kinds('objection','tension');reviews=[n for n in kinds('review') if n.get('role')=='opposition_review']
    response_ids=[n['response'] for n in opposition if n.get('response')]
    record('D04',[n['id'] for n in opposition+reviews]+[r['id'] for r in reasons]+response_ids+[p['id'] for p in priorities],[('Opposition review recorded',bool(reviews),'Open directed decisive issues block support; responses need directed grounds, not a status label.')])
    # Independent contrary pattern: binding/applicable/violated restriction with exclusion warrant.
    constraints=kinds('constraint');contrary=[];violations=[];constraint_open=[]
    for n in constraints:
        if n['applicability']=='not_applicable':continue
        wb=idx.get(n.get('binding_warrant'));wx=idx.get(n.get('exclusion_warrant'))
        bound=bool(wb and scoped(wb) and n['applicability']=='applicable')
        targeted=[i for i in issues if n['id'] in i.get('refs',[]) and is_blocking(i)]
        if not bound or n['compliance']=='unknown' or targeted:constraint_open.append(n['id']);continue
        if n['compliance']=='violated':
            violations.append(n['id'])
            if wx and scoped(wx):contrary.append({'pattern':'EXCLUDING-CONSTRAINT-1','constraint':n['id'],'grounds':sorted(set(refs(n)+[n['id']])),'limitation':'Authority, applicability, compliance and exclusion judgments are supplied, not independently validated.'})
    reviewed=bool(constraints) or any(n.get('constraint_search')=='none_adopted' for n in cov)
    record('D05',[n['id'] for n in constraints+cov],[('Constraint coverage explicit',reviewed,'Empty list alone does not establish absence.'),('Applicable constraints resolved',not constraint_open and not violations,'Unknown binding/applicability/compliance is not established; defended violation contradicts compliance.')],state='contradicted' if violations else None)
    informational=[i for i in issues if i['kind'] in ('missing_information','uncertainty')]
    record('D06',[i['id'] for i in informational]+[n['id'] for n in cov],[('Information limitations reviewed',any(n.get('limitations_review')=='documented' for n in cov),'Declared scope and curated plausible-alternatives analysis retained.')])
    favourable=all(d['state']=='supported' for d in conditions);unfavourable=bool(contrary)
    result='favourably_supported' if favourable and not unfavourable else 'unfavourably_supported' if unfavourable and not favourable else 'undetermined'
    # Snapshot enables reconstruction from output alone. All trace endpoints are typed/versioned.
    allnodes=sorted(list(idx.values())+generated+[r for r in reasons if r['id'].startswith('GEN:')],key=lambda n:n['id'])
    lookup={n['id']:n for n in allnodes};edges=[]
    def edge(a,b,rel):edges.append({'from':a,'to':b,'relation':rel,'target_version':lookup[b]['version'] if b in lookup else VERSION})
    for n in allnodes:
        for target in refs(n):edge(n['id'],target,'depends_on')
    for d in conditions:
        for target in sorted(set(d['grounds']+d['issue_ids'])):edge(d['condition'],target,'examines')
        edge(claim['id'],d['condition'],'condition')
    for x in contrary:
        for target in x['grounds']:edge(claim['id'],target,'contrary_chain')
    output={'processing_status':'completed','engine_version':VERSION,'criterion':c['criterion'],'assessment_id':'ASSESS:'+digest(c)[:16],'input_sha256':digest(c),'claim':claim,'conclusion':result,'chains':{'favourable':favourable,'unfavourable':unfavourable,'contrary_arguments':contrary},'conditions':conditions,'reasons':sorted(reasons,key=lambda n:n['id']),'issues':sorted(issues,key=lambda n:n['id']),'priorities':priorities,'constraints':constraints,'trace':sorted(edges,key=lambda e:(e['from'],e['to'],e['relation'])),'snapshot':{'input':c,'generated_objects':generated,'methods_used':[n for n in kinds('method')]+[{'id':'CURATED-RELATIONAL-RECONSTRUCTION-2.0','version':VERSION,'content':'Implementation design operationalization, not a validated domain inference method.'}]},'limitations':c.get('disclosures',[])+['Substantive warrants, relevance, criticality, accepted responses and plausible-alternative judgments are supplied by the researcher. Structural checks do not validate their adequacy.','No operational action is produced. Independent reconstruction and domain sufficiency remain to be examined.']}
    return output

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--output',required=True);a=p.parse_args()
    result=assess(json.loads(Path(a.case).read_text()));Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(result['processing_status'],result.get('conclusion','no justification emitted'))
