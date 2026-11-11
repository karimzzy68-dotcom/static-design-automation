"""Report coverage and repetition from actual authored concepts, without inventing performance."""
import argparse,json
from collections import Counter
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('manifest',type=Path); a=p.parse_args()
    manifest=json.loads(a.manifest.read_text(encoding='utf-8')); designs=manifest['designs']
    authored=[d for d in designs if d.get('concept')]
    fields=['goal','audience','awareness','angle','buyer_desire','concept_family','scene']
    if manifest.get('production_standard',1)>=2: fields+=['marketing_route','audience_insight','core_promise','objection','curiosity_payoff']
    coverage={key:dict(Counter(d['concept'].get(key,'UNSPECIFIED') for d in authored)) for key in fields}
    repeated_scenes={scene:count for scene,count in coverage['scene'].items() if count>1}
    report={'authored':len(authored),'requested':manifest['requested_concepts'],'coverage':coverage,
        'repeated_scenes':repeated_scenes,'missing_strategy_ids':[d['id'] for d in authored if any(not d['concept'].get(key) for key in fields)],
        'review_notes':['Text coverage is a planning aid, not proof of visual diversity.',
            'Compare actual images and narrative; differently worded descriptions can still produce the same scene.',
            'Deliberate same-scene copy tests need a variation rationale; do not call them a diverse visual set.',
            'Public impression ranks or run duration cannot establish profitable performance.']}
    path=a.manifest.parent/'plan-audit.json'; path.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'{len(authored)}/{manifest["requested_concepts"]} authored; {len(coverage["scene"])} scene descriptions; {len(repeated_scenes)} repeated scenes; {len(report["missing_strategy_ids"])} missing strategy records.')
    print(path)

if __name__=='__main__': main()
