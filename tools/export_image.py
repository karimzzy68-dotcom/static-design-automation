"""Create an exact-size delivery export with ffmpeg; preserve the raw generation."""
import argparse,json,subprocess
from pathlib import Path
import imageio_ffmpeg
from PIL import Image

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path); p.add_argument('destination',type=Path)
    p.add_argument('--width',type=int,default=1080); p.add_argument('--height',type=int,default=1350)
    p.add_argument('--fit',choices=['cover','contain'],default='cover')
    p.add_argument('--background',default='0xF3F0E9')
    a=p.parse_args()
    if a.destination.exists(): p.error('Destination exists; use a new filename.')
    if a.width<=0 or a.height<=0: p.error('Positive dimensions required.')
    a.destination.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(a.source) as im: original=list(im.size)
    scale=(f'scale={a.width}:{a.height}:force_original_aspect_ratio=increase:flags=lanczos,crop={a.width}:{a.height}' if a.fit=='cover'
        else f'scale={a.width}:{a.height}:force_original_aspect_ratio=decrease:flags=lanczos,pad={a.width}:{a.height}:(ow-iw)/2:(oh-ih)/2:color={a.background}')
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-nostdin','-i',str(a.source),'-vf',scale,'-frames:v','1',str(a.destination)],check=True,capture_output=True)
    with Image.open(a.destination) as im:
        if im.size!=(a.width,a.height): raise RuntimeError('Incorrect exported dimensions')
    a.destination.with_suffix('.export.json').write_text(json.dumps({'source':str(a.source.resolve()),
        'source_dimensions':original,'output_dimensions':[a.width,a.height],
        'transform':'aspect-preserving scale and centered crop; inspect export for clipping' if a.fit=='cover' else 'aspect-preserving contain and background padding; no source pixels cropped'},indent=2),encoding='utf-8')
    print(str(a.destination))

if __name__=='__main__': main()
