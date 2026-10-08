RETR={'bjerstedt2016':'2026-10-08','lahav2007':'2026-10-08','lappe2008':'2026-10-08','guadagnoli2001':'2026-10-08'}
import sys,json,csv,glob,re,html,os,collections
sys.path.insert(0,'/workspace/bl2/work'); sys.path.insert(0,'/workspace/bl2/work/build')
import vq
from sources import S
from evidence import E
_norm=vq.norm
vq.norm=lambda s:_norm(s.replace('⫽','='))
BL='/workspace/bl2'; OUT=BL+'/research'
# record -> page file
rec={}
for f in sorted(glob.glob(BL+'/research/deep-research/*/evidence.jsonl')):
    p=f.split('/')[-2].split('-')[0]; d=f.rsplit('/',1)[0]
    for i,l in enumerate(open(f)):
        r=json.loads(l); rec[f"{p}#{i:02d}"]=(d+'/'+r['source_page_file'],r)
ABS=json.load(open(BL+'/work/abstracts.json'))
EL=list(csv.DictReader(open(BL+'/sources/elicit-sources.csv',encoding='utf-8-sig')))
def text_for(qs):
    t,k=qs
    if t=='page': return open(rec[k][0],errors='replace').read()
    if t=='raw': return open(BL+'/work/raw/'+k+'.txt',errors='replace').read()
    if t=='abs': return html.unescape(ABS[k]['abstract'] or '')
    if t=='elicit': return EL[k]['Summary']
sid={s['source_id'] for s in S}
ecols=['evidence_id','source_id','claim','finding_type','population','instrument','skill_level','n','design','comparator','duration','outcome_and_timing','result_numeric','uncertainty_limits','supporting_quote','location','quote_verified','relevance_to_learner_group','knowledge_tree_branch','notes']
rows=[];bad=[]
for i,ev in enumerate(E,1):
    assert ev['source_id'] in sid, ev['source_id']
    v=vq.check(ev['supporting_quote'],text_for(ev['_qs']))
    if v!='yes': bad.append((i,ev['source_id'],v))
    r={k:ev.get(k,'') for k in ecols}; r['evidence_id']=f'E{i:03d}'; r['quote_verified']=v
    q=ev['_qs']
    prov={'page':f'quote checked against saved page for {q[1]} ({os.path.relpath(rec[q[1]][0],BL)})' if q[0]=='page' else '',
          'raw':f'quote checked against full text/excerpt retrieved {RETR.get(ev["source_id"],"2026-10-07")} (see research/manual-sources/{ev["source_id"]}.md)',
          'abs':f'quote checked against abstract retrieved {RETR.get(ev["source_id"],"2026-10-07")} via {ABS.get(q[1],{}).get("via","")} (saved in research/manual-sources/{ev["source_id"]}.md)',
          'elicit':f'quote checked against Elicit export abstract (sources/elicit-sources.csv row {q[1]})'}[q[0]]
    r['notes']=(r['notes']+' | ' if r['notes'] else '')+prov
    rows.append(r)
print('non-yes quotes:',bad)
# kept sources only for evidence
flag={s['source_id']:s['quality_flag'] for s in S}
for r in rows: assert not flag[r['source_id']].startswith('exclude'), r['source_id']
with open(OUT+'/evidence.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=ecols); w.writeheader(); w.writerows(rows)
scols=['source_id','citation','year','doi','url','source_type','population','instrument','skill_level','design','access','quality_flag','origin','origin_records']
with open(OUT+'/source-register.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=scols); w.writeheader()
    for s in S: w.writerow({k:('' if s.get(k) is None else s.get(k)) for k in scols})
# coverage check: every pass record and elicit row mapped
allrecs=' '.join(s['origin_records'] for s in S)
missing=[k for k in rec if k not in allrecs]
print('unmapped pass records:',missing)
el_mapped=set(int(x) for x in re.findall(r'elicit rows? (\d+)',allrecs))|set(int(x) for x in re.findall(r'rows (\d+) and (\d+)',allrecs) for x in x) if False else set()
for m in re.finditer(r'elicit rows? ([\d ,and]+)',allrecs):
    el_mapped|=set(int(x) for x in re.findall(r'\d+',m.group(1)))
print('unmapped elicit rows:',sorted(set(range(len(EL)))-el_mapped))
# manual-sources texts
md=BL+'/research/manual-sources'; os.makedirs(md,exist_ok=True)
by=collections.defaultdict(list)
for ev in E:
    if ev['_qs'][0] in ('raw','abs'): by[ev['source_id']].append(ev)
smap={s['source_id']:s for s in S}
for k,evs in by.items():
    s=smap[k]; out=[f'# {k}\n',f'Citation: {s["citation"]}\n',f'URL: {s["url"]}\n',f'Retrieved: {RETR.get(k,"2026-10-07")} (Grok Bot, manual search)\n']
    seen=set()
    for ev in evs:
        t,key=ev['_qs']
        if (t,key) in seen: continue
        seen.add((t,key))
        if t=='abs':
            a=ABS[key]; out+= [f'\n## Abstract (via {a.get("via")}; record URL {a.get("url")})\n\n',html.unescape(a['abstract']).strip()+'\n']
    # excerpts for raw full texts
    raws=[ev for ev in evs if ev['_qs'][0]=='raw']
    if raws:
        out.append('\n## Verbatim excerpts around quoted passages (from the full text / page retrieved above; short excerpts for verification only)\n')
        for ev in raws:
            txt=vq.norm(open(BL+'/work/raw/'+ev['_qs'][1]+'.txt',errors='replace').read().replace('⫽','='))
            seg=[x.strip(' .') for x in re.split(r'\s*(?:…|\.\.\.)\s*',vq.norm(ev['supporting_quote'].replace('⫽','='))) if x.strip(' .')][0]
            j=txt.find(seg); 
            if j<0: j=vq.dehyph(txt).find(vq.dehyph(seg)); txt=vq.dehyph(txt) if j>=0 else txt
            ex=txt[max(0,j-250):j+len(seg)+250] if j>=0 else '(not located)'
            out.append(f'\n- [{ev["location"]}] …{ex}…\n')
    open(f'{md}/{k}.md','w').write(''.join(out))
print('manual-source files:',len(by))
c=collections.Counter
print('sources by type:',c(s['source_type'] for s in S))
print('sources by flag:',c(s['quality_flag'].split(' ')[0] for s in S))
print('evidence by branch:',c(r['knowledge_tree_branch'] for r in rows))
print('evidence by relevance:',c(r['relevance_to_learner_group'] for r in rows))
print('evidence by finding type:',c(r['finding_type'] for r in rows))
print('quote_verified:',c(r['quote_verified'] for r in rows))
