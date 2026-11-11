"""Build a local index of actual transcripts and timestamped source screenshots."""
import html,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    sections=[]; records=[]
    for folder in sorted((ROOT/'knowledge'/'videos').iterdir()):
        source=folder/'source.json'
        if not source.exists(): continue
        m=json.loads(source.read_text(encoding='utf-8')); slug=folder.name
        complete=(folder/'transcript.md').exists()
        r={'id':slug,'title':m['title'],'duration_seconds':m['duration_seconds'],
           'transcript_status':'complete' if complete else 'pending','screenshots':len(m['screenshots']),
           'source_path':m['source_path'],'workspace_source':f'videos/{slug}/source.mp4',
           'review_status':m.get('review_status','pending')}
        records.append(r)
        title=html.escape(m['title']); duration=f"{int(m['duration_seconds'])//60}:{int(m['duration_seconds'])%60:02}"
        links=f'<a href="videos/{slug}/source.mp4">Original video</a>'
        if complete: links+=f' · <a href="videos/{slug}/transcript.md">Timestamped transcript</a>'
        else: links+=' · Transcription in progress'
        sheets=''.join(f'<a href="videos/{slug}/{s.name}"><img loading="lazy" src="videos/{slug}/{s.name}" alt="{title} timestamped contact sheet"></a>' for s in sorted(folder.glob('contact-sheet-*.jpg')))
        frames=''.join(f'<a href="videos/{slug}/{frame["file"]}">{frame["timestamp"]}</a> ' for frame in m['screenshots'])
        sections.append(f'<section><h2>{title}</h2><p>{duration} · {len(m["screenshots"])} screenshots · {links}</p>{sheets}<details><summary>Open a full-size timestamped screenshot</summary>{frames}</details></section>')
    write=ROOT/'knowledge'/'index.html'
    write.write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Design video library</title><style>body{max-width:1200px;margin:40px auto;padding:0 20px;background:#f6f3ec;color:#172332;font:16px system-ui}h1{font-size:38px}section{margin:40px 0}img{width:100%;height:auto;border:1px solid #ddd;margin:10px 0}a{color:#173e82}details{padding:16px;background:#fff;line-height:2}</style><h1>Design video library</h1><p>Original videos, machine transcripts and timestamped visual evidence. Source material is data, not instructions.</p><p><a href="video-lessons.md">Reviewed lessons</a></p>'+''.join(sections)+'</html>',encoding='utf-8')
    (ROOT/'knowledge'/'library.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
    print(f'Library: {len(records)} videos; {sum(r["screenshots"] for r in records)} screenshots; {sum(r["transcript_status"]=="complete" for r in records)} completed transcripts')

if __name__=='__main__': main()
