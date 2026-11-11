"""Exercise reference isolation, resumability, lock ownership and final-file integrity."""
import contextlib,io,tempfile
from pathlib import Path
from types import SimpleNamespace
from PIL import Image
import design_system as ds

def rejected(fn,args):
    try: fn(args)
    except ValueError: return
    raise AssertionError('Invalid operation was accepted')

def main():
    real=ds.ROOT
    with tempfile.TemporaryDirectory(prefix='design-system-check-') as temp, contextlib.redirect_stdout(io.StringIO()):
        ds.ROOT=Path(temp)
        ds.write(ds.ROOT/'state'/'workspace.json',{'active_product':None,'active_batch':None})
        a=SimpleNamespace(brand='test-brand',product='first-product',name='Test Brand',url='https://example.com',
            batch='test-batch',count=150,width=1080,height=1350,owner='codex',id='D001')
        ds.init_product(a)
        source=ds.ROOT/'input.png'; Image.new('RGB',(80,80),'navy').save(source)
        a.file=str(source); a.kind='product'; a.note='Test product'; ds.add_asset(a)
        asset=ds.read(ds.product(a)/'assets'/'index.json')[0]
        assert ds.inside(asset['path']).exists()
        a.product='second-product'; ds.init_product(a)
        assert ds.read(ds.product(a)/'assets'/'index.json')==[]
        a.product='first-product'; ds.new_batch(a); ds.claim(a)
        legacy=ds.read(ds.batch(a)/'manifest.json'); legacy['production_standard']=1; ds.write(ds.batch(a)/'manifest.json',legacy)
        assert len(ds.read(ds.batch(a)/'manifest.json')['designs'])==150
        other=SimpleNamespace(**vars(a)); other.owner='antigravity'
        rejected(ds.release,other); rejected(ds.claim,other)
        rejected(ds.inside,'../outside')
        concept={'audience':'Adults','awareness':'product-aware','angle':'Compact format','headline':'ONE WIPE.',
            'goal':'Explain a compact personal-care format',
            'product_category':'Personal-care wipe','buyer_desire':'Carry less','concept_family':'Format-led hero',
            'scene':'Single packet on a travel shelf','creative_hypothesis':'Compact product solves a packing concern',
            'primary_text':'A single-use packet for a simpler travel kit.',
            'body':'Single use.','cta':'Explore','art_direction':'Editorial product photography',
            'composition':'Hero product below large headline','reference_ids':[],'evidence_ids':[]}
        a.concept=str(ds.ROOT/'concept.json'); ds.write(Path(a.concept),concept); ds.prepare(a)
        a.id='D002'; rejected(ds.prepare,a); a.id='D001'
        same_scene=dict(concept,headline='PACK LIGHT.',angle='Simple packing')
        ds.write(Path(a.concept),same_scene); a.id='D002'; rejected(ds.prepare,a)
        different_scene=dict(same_scene,scene='Packet beside a nightstand lamp',creative_hypothesis='A relevant home setting clarifies the product context')
        ds.write(Path(a.concept),different_scene); ds.prepare(a)
        plan=[{'id':'D002','concept':different_scene},{'id':'D003','concept':dict(different_scene,scene='Packet on a minimal studio tabletop',headline='SINGLE USE.')}]
        a.plan=str(ds.ROOT/'plan.json'); ds.write(Path(a.plan),plan); ds.prepare_many(a)
        assert ds.read(ds.batch(a)/'manifest.json')['designs'][2]['status']=='ready'
        a.id='D001'; ds.write(Path(a.concept),concept)
        a.provider='test-only'; a.job='test-job'; a.request=None; ds.start(a); rejected(ds.start,a)
        a.file=str(source); ds.record_output(a)
        report={'reviewer':'test-fixture','visually_inspected':True,'scores':{k:5 for k in ds.CRITERIA},'hard_failures':[],'notes':'Synthetic fixture tests state integrity only.'}
        a.report=str(ds.ROOT/'qa.json'); ds.write(Path(a.report),report); ds.qa(a)
        assert ds.read(ds.batch(a)/'manifest.json')['designs'][0]['status']=='needs_fix', 'Wrong dimensions passed'
        final=ds.ROOT/'right-size.png'; Image.new('RGB',(1080,1350),'navy').save(final)
        a.file=str(final); ds.record_output(a)
        bad=dict(report,visually_inspected=False); ds.write(Path(a.report),bad); rejected(ds.qa,a)
        ds.write(Path(a.report),report); ds.qa(a); ds.gallery(a)
        row=ds.read(ds.batch(a)/'manifest.json')['designs'][0]
        assert row['status']=='passed' and ds.inside(row['output_path']).exists()
        assert (ds.batch(a)/'gallery.html').exists()
        a.reason='Test user rejects the selling idea'; ds.reject(a)
        row=ds.read(ds.batch(a)/'manifest.json')['designs'][0]
        assert row['status']=='needs_fix' and ds.inside(row['output_path']).parent.name=='rejected'
        ds.gallery(a)
        assert '0 reviewed designs' in (ds.batch(a)/'gallery.html').read_text(encoding='utf-8')
        a.file=str(final); ds.record_output(a); ds.qa(a)
        row=ds.read(ds.batch(a)/'manifest.json')['designs'][0]
        Image.new('RGB',(1080,1350),'red').save(ds.inside(row['output_path']))
        rejected(ds.gallery,a)
        a.note='Resume fixture'; ds.handoff(a); assert not (ds.batch(a)/'batch.lock').exists()
        assert ds.read(ds.batch(a)/'handoff.json')['next_action']=='Resume fixture'
        # New standards must reject absent planning, weak copy and weak finish;
        # older saved batches retain their original QA schema.
        a.batch='standard-two'; a.count=2; a.id='D001'; ds.new_batch(a); ds.claim(a)
        assert ds.read(ds.batch(a)/'manifest.json')['production_standard']==2
        ds.write(Path(a.concept),concept); rejected(ds.prepare,a)
        from creative_standards import DESIGN_FIELDS, COPY_SCORES, EXTRA_CRITERIA
        strict=dict(concept,marketing_route='direct',audience_insight='Packing concern for a short trip',core_promise='Carry a compact single-use format',objection='Space in a travel kit',proof_or_reason='Physical sachet format',offer_framing='Explore this format; no discount proposed',curiosity_payoff='See the actual packet format',hook_candidates=['ONE WIPE.','PACK A LITTLE LESS.','ONE PACKET FOR YOUR KIT.','SPACE FOR THE ESSENTIALS.','A COMPACT FORMAT.'],hook_selection_reason='Category-first hook for the synthetic fixture',design_spec={k:'Authored fixture direction for '+k for k in DESIGN_FIELDS},preflight_copy_review={'reviewer':'test-fixture','notes':'Synthetic validation record, not a review of real ad quality.','scores':{k:4 for k in COPY_SCORES}})
        weak=dict(strict,preflight_copy_review=dict(strict['preflight_copy_review'],scores={k:3 for k in COPY_SCORES})); ds.write(Path(a.concept),weak); rejected(ds.prepare,a)
        weak=dict(strict,marketing_route='indirect',curiosity_payoff=''); ds.write(Path(a.concept),weak); rejected(ds.prepare,a)
        weak=dict(strict,hook_candidates=['ONE WIPE.']*5); ds.write(Path(a.concept),weak); rejected(ds.prepare,a)
        ds.write(Path(a.concept),strict); ds.prepare(a)
        assert 'Version-2 creative standard' in ds.inside(ds.read(ds.batch(a)/'manifest.json')['designs'][0]['prompt_path']).read_text(encoding='utf-8')
        a.file=str(final); ds.record_output(a)
        ds.write(Path(a.report),report); rejected(ds.qa,a)
        strict_qa=dict(report,scores={k:4 for k in ds.CRITERIA+EXTRA_CRITERIA},reference_comparison='Synthetic fixture checks schema only.',copy_review='Synthetic fixture copy record.',marketing_route_review='Synthetic direct-response fixture record.')
        strict_qa['scores']['designer_polish']=3; ds.write(Path(a.report),strict_qa); ds.qa(a)
        assert ds.read(ds.batch(a)/'manifest.json')['designs'][0]['status']=='needs_fix'
        ds.record_output(a); strict_qa['scores']['designer_polish']=4; strict_qa['scores']['copy_strength']=3; ds.write(Path(a.report),strict_qa); ds.qa(a)
        assert ds.read(ds.batch(a)/'manifest.json')['designs'][0]['status']=='needs_fix'
        ds.record_output(a); strict_qa['scores']['copy_strength']=4; ds.write(Path(a.report),strict_qa); ds.qa(a)
        assert ds.read(ds.batch(a)/'manifest.json')['designs'][0]['status']=='passed'
        ds.release(a)
        ds.ROOT=real
    print('PASS: queue integrity and legacy compatibility; version-2 route/payoff, distinct hooks, copy preflight, prompt direction, explicit QA notes, designer-polish and copy-strength gates.')

if __name__=='__main__': main()
