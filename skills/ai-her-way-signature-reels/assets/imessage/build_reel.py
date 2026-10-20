from pathlib import Path
import json,html
from visual_helpers import parts,actions,cues,CSS,cue,pop,reveal,line,heading,panel,card
P=Path(__file__).resolve().parent; D=45.4
parts += [f'<div class="camera"><video id="presenter" class="clip" src="assets/presenter.mp4" data-start="0" data-duration="{D}" data-track-index="0" muted playsinline></video></div>',f'<audio id="voice" src="assets/voice.wav" data-start="0" data-duration="{D}" data-track-index="10" data-volume="1"></audio>']
def banner(id,a,b,text,cls=''):
 parts.append(f'<div class="clip title-slot" data-start="{a}" data-duration="{b-a}" data-track-index="8"><div id="{id}" class="title {cls}">{text}</div></div>');reveal(id,a+.05)
 if a>0:cue(id,'notification',a+.12,.7,'scene-ping.wav',.075)
def proof(id,asset,a,b,x,y,w,h,land=None):
 parts.append(f'<div id="{id}-wrap" class="proof-wrap" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><video id="{id}" class="clip proof" src="assets/{asset}" data-start="{a}" data-duration="{b-a}" data-track-index="7" muted playsinline></video></div>')
 if land is not None:
  actions.append(f"tl.fromTo('#{id}-wrap',{{opacity:0,y:34,scale:.94,rotation:-1.5}},{{opacity:1,y:0,scale:1,rotation:0,duration:{land-a},ease:'back.out(1.15)'}},{a});")
  cue(id,'pop',land,.22,'pop.mp3',.14)
def typed(id,text,t,d,handwritten=False):
 chunks=[]
 for i,word in enumerate(text.split(' ')):
  if i:chunks.append('<span class="typed-char"> </span>')
  chunks.append('<span style="display:inline-block;white-space:nowrap">'+''.join('<span class="typed-char">'+html.escape(c)+'</span>' for c in word)+'</span>')
 chars=''.join(chunks)
 actions.append(f"tl.fromTo('#{id} .typed-char',{{opacity:0}},{{opacity:1,duration:0,stagger:{d/(len(text)-1)},ease:'none'}},{t});")
 cue(id,'draw' if handwritten else 'typewriter',t,d,'v7-pencil-long-feedback-arrow.wav' if handwritten else 'question-typing.wav',.24 if handwritten else .055)
 return f'<div id="{id}" class="typed-message">{chars}</div>'

banner('opening',0,2.92,'Claude can<br>text you.')
proof('example-one','today-redacted.mp4',3.18,7.11,65,180,560,263,3.52)
proof('example-two','lifting-redacted.mp4',4.22,7.11,50,940,450,242,4.56)
banner('workout-buddy',8.45,10.9,typed('buddy-typing','My AI workout buddy.',8.65,1.1),'small-title')

body=heading('01 / CONNECT',['Connect your messages.'])
body+='<div class="hand-note"><span>iPad recording.</span><span>My setup: Mac Mini at home.</span><span>Requires a desktop Mac.</span></div>'
body+='<svg class="connections">'+line('mac-note-arrow','M795 1102 Q916 1060 853 979',11.7,.8,True)+'</svg>'
panel('connect',11.02,16.35,body)
proof('connector','connector-safe.mp4',11.36,16.01,75,452,810,613)

body=heading('02 / SCHEDULE',['Set it once.','<em>A daily nudge.</em>'])
for i,(label,kind,color) in enumerate([('Claude','hub','blue'),('Recurring task','journey','sage'),('iMessage','faq','stone')]):
 id=f'flow-{i}';body+=card(id,label,kind,75+i*280,730,color,width=250);pop(id,16.9+i*.28)
body+='<svg class="connections">'+line('flow-line-a','M326 841 Q342 828 355 841',17.8)+line('flow-line-b','M606 841 Q624 827 635 841',18.3)+'</svg>'
body+=typed('morning-message','Morning! Ready for your workout?',19,1.2)
panel('schedule',16.35,21.4,body)

proof('protein','protein-redacted.mp4',21.79,25.26,65,165,575,380,22.1)

banner('result',26.6,31.65,'<strong>4</strong><span>workouts<br>a week</span>','result-title')
banner('get-texting',32.3,37.6,'Get texting<br>with Claude.')
cta=typed('cta-writing','Comment TEXT',38.7,1.0,handwritten=True)
cta+='<div class="cta-sub">I’ll send you the<br>macOS setup guide.</div>'
banner('comment-guide',38.5,45.4,cta,'cta-title')
parts.append('<svg class="clip connections cta-line" data-start="38.5" data-duration="6.9" data-track-index="9">'+line('text-underline','M400 282 Q530 273 672 282',39.75,.42)+'</svg>')

for i,w in enumerate(json.loads((P/'caption-words.json').read_text())):
 if w['end']>w['start']:parts.append(f'<div id="caption-{i}" class="clip caption" data-start="{w["start"]}" data-duration="{w["end"]-w["start"]}" data-track-index="50"><span>{html.escape(w["text"])}</span></div>')
camera=[(0,1.01,0),(2.5,1.045,-12),(5,1.015,0),(7.5,1.055,-15),(10,1.015,0),(21.4,1.01,0),(23.9,1.05,-12),(26.4,1.015,0),(28.9,1.055,-15),(31.4,1.015,0),(33.9,1.05,-12),(36.4,1.015,0),(39,1.045,-12),(41.5,1.01,0),(44,1.045,-12)]
for t,scale,x in camera:actions.append(f"tl.set('.camera',{{scale:{scale},x:{x}}},{t});")
for a,b in [(0,2.5),(5,7.5),(23.9,26.4),(28.9,31.4),(33.9,36.4),(39,41.5),(44,45.4)]:actions.append(f"tl.to('.camera',{{scale:'+=.018',duration:{b-a},ease:'none'}},{a});")
CSS+='''
@font-face{font-family:Hand;src:url('assets/SegoePrint.ttf')}
.camera{transform-origin:65% 46%}.title-slot{inset:0;z-index:8}.title{position:absolute;left:75px;top:160px;width:810px;background:#F2EBDD;border:8px solid #FAF6EF;border-radius:27px;padding:19px 27px 26px;font-family:Advercase;font-size:88px;line-height:1.15}.small-title{font-size:67px}.proof-wrap{position:absolute;z-index:7}.proof{inset:0;width:100%;height:100%;object-fit:contain;border:8px solid #FAF6EF;border-radius:24px;background:#fff;box-shadow:6px 8px 0 #35241F1A}.proof-label{position:absolute;left:80px;font-size:23px;letter-spacing:2px;color:#46513D}.hand-note{position:absolute;left:76px;top:1090px;width:810px;font-family:Hand;font-size:34px;line-height:1.4;color:#35241F}.hand-note span{display:block}.typed-message{position:absolute;left:75px;top:1060px;width:810px;padding:25px 30px;background:#FAF6EF;border:3px solid #C0CACE;border-radius:28px;font-family:Advercase;font-size:54px;line-height:1.25}.privacy-note{position:absolute;left:78px;top:1140px;width:800px;font-size:25px;color:#46513D}.result-title{display:flex;align-items:center;gap:28px;padding:8px 40px}.result-title strong{font-size:160px;font-weight:400;line-height:1.1}.result-title span{font-size:55px;line-height:1.15}.closing-note{left:76px;top:1150px;width:800px;z-index:8}.handwriting{font-family:Hand;font-size:37px;line-height:1.45;background:#F2EBDD;border:6px solid #FAF6EF;border-radius:20px;padding:15px 24px}.card-label{font-size:25px}#connect-sheet h1{font-size:83px}#examples-sheet h1{font-size:96px}
'''
CSS+='''#buddy-typing,#cta-writing{position:static;width:auto;padding:0;border:0;background:none;font:inherit;border-radius:0}.cta-title{font-family:Hand;font-size:65px;line-height:1.4}.cta-sub{font-family:Advercase;font-size:53px;line-height:1.15;margin-top:30px}.cta-line{z-index:9;pointer-events:none}'''
script="const tl=gsap.timeline({paused:true});function draw(sel,t,d){const e=document.querySelector(sel),n=e.getTotalLength();tl.set(e,{opacity:1},t);tl.fromTo(e,{strokeDasharray:n,strokeDashoffset:n},{strokeDashoffset:0,duration:d,ease:'none'},t);}"+'\n'.join(actions)+"window.__timelines['imessage']=tl;"
(P/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><script src="assets/gsap.min.js"></script><style>'+CSS+'</style></head><body>'+f'<div id="root" data-composition-id="imessage" data-width="1080" data-height="1920" data-duration="{D}">'+''.join(parts)+'</div><script>'+script+'</script></body></html>',encoding='utf-8')
(P/'sound-cues.json').write_text(json.dumps(cues,indent=2));(P/'camera-cues.json').write_text(json.dumps(camera,indent=2))
(P/'package.json').write_text(json.dumps({'name':'ai-her-way-imessage','private':True,'scripts':{'check':'npx --yes hyperframes@0.8.90 check --json','render':'npx --yes hyperframes@0.8.90 render --quality delivery --output AI-Her-Way-iMessage-Reel-v2.mp4'}},indent=2))
print(f'Built {D}s reel, message landings at 3.52 and 4.56 seconds.')
