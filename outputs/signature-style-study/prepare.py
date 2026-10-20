from pathlib import Path
import re,json,struct,hashlib,shutil,zipfile
from html.parser import HTMLParser
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent
REF=Path(r'C:\Users\nici\brand-design-system\ref video')
OLD=REF/'batch-2-2026-09-18'
FILES=['1789698582154','1789698621114','1789698663494','1789698690231','1789698702184']
def boxes(data,start,end):
 while start+8<=end:
  size,typ=struct.unpack_from('>I4s',data,start); head=8
  if size==1: size=struct.unpack_from('>Q',data,start+8)[0];head=16
  if size==0:size=end-start
  if size<head:break
  yield typ,start+head,start+size
  start+=size
def probe(path):
 data=path.read_bytes(); info={}
 for typ,s,e in boxes(data,0,len(data)):
  if typ!=b'moov':continue
  for t,a,b in boxes(data,s,e):
   if t==b'mvhd':
    v=data[a];off=a+(20 if v else 12); scale=struct.unpack_from('>I',data,off)[0];dur=struct.unpack_from('>Q' if v else '>I',data,off+4)[0];info['duration']=dur/scale
   if t==b'trak':
    for q,c,d in boxes(data,a,b):
     if q==b'tkhd':
      w,h=struct.unpack_from('>II',data,d-8)
      if w and h:info.update(width=w/65536,height=h/65536)
 return info
manifest=[]
for id,num in zip('ABCDE',FILES):
 path=REF/f'PinGrab_{num}.mp4'; meta=probe(path)
 old=OLD/'analysis'/id
 srt=(old/'transcript.srt').read_text(encoding='utf-8')
 lines=[x.strip() for x in srt.splitlines() if x.strip() and not x.strip().isdigit() and '-->' not in x]
 wc=len(re.findall(r"\b[\w']+\b",' '.join(lines)))
 cuts=[float(x) for x in re.findall(r'pts_time:([\d.]+)',(old/'cuts.txt').read_text())]
 meta.update(id=id,file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),matches_previous_copy=path.read_bytes()==(OLD/path.name).read_bytes(),words_approx=wc,wpm_approx=round(wc/meta['duration']*60),detector_events=cuts)
 manifest.append(meta)
 shutil.copy(old/'transcript.srt',ROOT/'assets'/f'{id}-original-transcript.srt')
 sheets=sorted(old.glob('sheet*.png'))
 for p in sheets:shutil.copy(p,ROOT/'assets'/f'{id}-{p.name}')
 # First frame thumbnail from the prior 5-column, 4-row sheet. No alteration to source video.
 im=Image.open(sheets[0]); im.crop((0,0,im.width//5,im.height//4)).save(ROOT/'assets'/f'{id}-poster.png')
(ROOT/'assets'/'source-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
class Text(HTMLParser):
 def __init__(self):super().__init__();self.hide=0;self.out=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.hide+=1
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.hide=max(0,self.hide-1)
 def handle_data(self,data):
  if not self.hide and data.strip():self.out.append(data.strip())
for n,p in enumerate([Path(r'C:\Users\nici\brand-design-system\AI-Her-Way-Social-Lookbook.html'),Path(r'C:\Users\nici\Downloads\AI-Her-Way-Lookbook.html')],1):
 parser=Text();parser.feed(p.read_text(encoding='utf-8'));(ROOT/'assets'/f'lookbook-{n}-text.txt').write_text('\n'.join(parser.out),encoding='utf-8')
print(json.dumps(manifest,indent=2))
