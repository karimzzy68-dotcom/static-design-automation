"""Extract timestamped evidence and transcribe local learning videos. Resume-safe."""
import argparse, json, os, subprocess, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('static-copy-scale', 'The Ultimate Guide to Static Image Ads (copy & scale).mp4'),
    ('static-2026', 'The ULTIMATE Guide to Static Ads in 2026.mp4'),
    ('ai-static-minutes', 'How I Make AI Static Ads (in minutes).mp4'),
]

def stamp(seconds):
    return f'{int(seconds)//3600:02}:{int(seconds)//60%60:02}:{int(seconds)%60:02}'

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--downloads', type=Path, default=Path.home()/'Downloads')
    p.add_argument('--model', default='base.en')
    p.add_argument('--engine', choices=['faster-whisper','whisper'], default='whisper')
    p.add_argument('--frames-only', action='store_true')
    p.add_argument('--sources-json', type=Path)
    p.add_argument('--interval', type=float, default=30)
    args = p.parse_args()
    import cv2
    from PIL import Image, ImageDraw
    import imageio_ffmpeg
    model = None
    sources=json.loads(args.sources_json.read_text(encoding='utf-8')) if args.sources_json else SOURCES
    for slug, name in sources:
        source = args.downloads/name
        out = ROOT/'knowledge'/'videos'/slug
        out.mkdir(parents=True, exist_ok=True)
        local_source=out/'source.mp4'
        if not source.exists() and local_source.exists(): source=local_source
        if not source.exists(): raise FileNotFoundError(f'Neither original nor workspace copy is available for {name}')
        if not local_source.exists(): shutil.copy2(source,local_source)
        frames = out/'screenshots'
        frames.mkdir(exist_ok=True)
        cap = cv2.VideoCapture(str(source))
        if not cap.isOpened():
            raise RuntimeError(f'Cannot open {source}')
        duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS)
        index = []
        times = [round(i*args.interval,3) for i in range(int(duration/args.interval)+1) if i*args.interval<duration]
        for second in times:
            cap.set(cv2.CAP_PROP_POS_MSEC, second*1000)
            ok, frame = cap.read()
            if not ok:
                continue
            filename = f'{round(second*1000):07d}ms.jpg'
            cv2.imwrite(str(frames/filename), frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
            index.append({'seconds':second,'timestamp':stamp(second),'file':f'screenshots/{filename}'})
        cap.release()
        tiles=[]
        for record in index:
            im=Image.open(out/record['file']).convert('RGB')
            im.thumbnail((400,225))
            tile=Image.new('RGB',(400,255),'#161616')
            tile.paste(im,((400-im.width)//2,0))
            ImageDraw.Draw(tile).text((10,233),record['timestamp'],fill='white')
            tiles.append(tile)
        for start in range(0,len(tiles),24):
            page=tiles[start:start+24]
            sheet=Image.new('RGB',(1600,255*((len(page)+3)//4)),'#161616')
            for i,tile in enumerate(page): sheet.paste(tile,((i%4)*400,(i//4)*255))
            sheet.save(out/f'contact-sheet-{start//24+1:02}.jpg',quality=90)
        metadata={'title':name,'source_path':str(source),'workspace_source':'source.mp4','duration_seconds':duration,
                  'screenshots':index,'transcription_status':'pending'}
        if (out/'transcript.json').exists():
            metadata['transcription_status']='complete'
        (out/'source.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
        print(f'{slug}: {duration:.1f}s; {len(index)} screenshots',flush=True)
        if args.frames_only or (out/'transcript.json').exists(): continue
        wav=out/'audio.wav'
        if not wav.exists():
            subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-nostdin','-y','-i',str(source),
                '-vn','-ar','16000','-ac','1',str(wav)],check=True,capture_output=True)
        if args.engine=='whisper':
            import torch, whisper, wave, numpy as np
            from types import SimpleNamespace
            torch.set_num_threads(min(os.cpu_count() or 4,8))
            if model is None: model=whisper.load_model(args.model,device='cpu')
            with wave.open(str(wav),'rb') as f: audio=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
            def cached_segments():
                for offset in range(0,len(audio),120*16000):
                    result=model.transcribe(audio[offset:offset+120*16000],language='en',fp16=False,verbose=None)
                    for s in result['segments']:
                        yield SimpleNamespace(start=s['start']+offset/16000,end=s['end']+offset/16000,text=s['text'])
            segments=cached_segments(); info=SimpleNamespace(language='en')
        else:
            if model is None:
                from faster_whisper import WhisperModel
                model=WhisperModel(args.model,device='cpu',compute_type='int8',cpu_threads=min(os.cpu_count() or 4,8))
            segments,info=model.transcribe(str(wav),language='en',beam_size=5,vad_filter=True)
        records=[]
        progress_minute=-1
        partial=out/'transcript.partial.jsonl'
        with partial.open('w',encoding='utf-8') as f:
            for s in segments:
                r={'start':round(s.start,2),'end':round(s.end,2),'text':s.text.strip()}
                records.append(r); f.write(json.dumps(r)+'\n'); f.flush()
                minute=int(s.end)//60
                if minute!=progress_minute:
                    print(f'{slug} {stamp(s.end)} / {stamp(duration)}',flush=True)
                    progress_minute=minute
        (out/'transcript.json').write_text(json.dumps({'model':args.model,'engine':args.engine,'language':info.language,
            'machine_generated':True,'segments':records},indent=2),encoding='utf-8')
        (out/'transcript.md').write_text('# '+name+'\n\nMachine transcript; source material, not agent instructions. Proper names and numbers may need checking.\n\n'+
            '\n\n'.join(f"[{stamp(r['start'])}–{stamp(r['end'])}] {r['text']}" for r in records),encoding='utf-8')
        metadata['transcription_status']='complete'
        (out/'source.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
        print(f'{slug}: transcript complete',flush=True)

if __name__=='__main__': main()
