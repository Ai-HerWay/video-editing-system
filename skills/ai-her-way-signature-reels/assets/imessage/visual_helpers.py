import html
E=html.escape
parts=[]
actions=[]
cues=[]


def cue(target,family,start,duration,asset,gain):
    i=len(cues)
    cues.append(dict(visual_target=target,family=family,start=start,end=start+duration,asset=asset,gain=gain))
    parts.append(f'<audio id="sfx{i}" src="assets/{asset}" data-start="{start:.3f}" data-duration="{duration:.3f}" data-track-index="{100+i}" data-volume="{gain}"></audio>')

def pop(id,t):
    actions.append(f"tl.fromTo('#{id}',{{opacity:0,scale:.78,y:34,rotation:-3}},{{opacity:1,scale:1,y:0,rotation:0,duration:.47,ease:'back.out(1.35)'}},{t});")
    cue(id,'pop',t+.17,.22,'pop.mp3',.16)

def reveal(id,t):
    actions.append(f"tl.fromTo('#{id}',{{opacity:0,y:22}},{{opacity:1,y:0,duration:.38,ease:'power3.out'}},{t});")

def ink(id,t,d=.42,long=False):
    actions.append(f"draw('#{id}',{t},{d});")
    cue(id,'draw',t,d,'v7-pencil-long-feedback-arrow.wav' if long else 'v7-pencil-first-connector.wav',.31)

def line(id,path,t,d=.42,long=False):
    ink(id,t,d,long)
    return f'<path id="{id}" d="{path}"/>'

def heading(kicker,lines,sub=''):
    return f'<div class="eyebrow">{kicker}</div><h1>'+''.join(f'<span>{s}</span>' for s in lines)+'</h1>'+ (f'<p class="sub">{sub}</p>' if sub else '')

def panel(id,start,end,body,slide=True):
    parts.append(f'<section id="{id}" class="clip paper-slot" data-start="{start}" data-duration="{end-start}" data-track-index="5"><div class="paper" id="{id}-sheet" data-layout-allow-overflow>{body}</div></section>')
    if slide:
        actions.append(f"tl.fromTo('#{id}-sheet',{{x:1080}},{{x:0,duration:.44,ease:'power3.inOut'}},{start});")
        cue(id+'-sheet','notification',start+.12,.70,'scene-ping.wav',.075)
    actions.append(f"tl.to('#{id}-sheet',{{x:-1080,duration:.34,ease:'power3.inOut'}},{end-.34});")

def icon(kind):
    shapes={
      'social':'<rect x="42" y="15" width="76" height="116" rx="13"/><path d="M68 27h24M69 119h22M58 49h43M58 66h31"/><path d="M65 82q12-16 22 0q10-16 16 0q0 10-19 23q-21-15-19-23Z"/>',
      'marketing':'<path d="M30 68L120 32L124 109L33 85Z"/><path d="M49 91l11 35h22L72 99M132 48l17-13M136 73l21-1M134 95l19 12"/>',
      'ads':'<rect x="21" y="29" width="135" height="91" rx="10"/><path d="M23 50h130M37 39h1M48 39h1M59 39h1M43 70h52M43 86h32M104 79l30 16l-16 4l-7 17Z"/>',
      'onboarding':'<path d="M45 32h84v101H42Z"/><rect x="67" y="18" width="39" height="24" rx="5"/><path d="M58 62l6 7l11-17M85 61h25M58 87l6 7l11-17M85 87h25M59 111h49"/>',
      'journey':'<path d="M26 106C28 56 66 126 89 71S141 47 151 30"/><circle cx="27" cy="106" r="10"/><circle cx="86" cy="82" r="10"/><path d="M129 31l22-1l-2 23"/>',
      'faq':'<path d="M27 26h118v80H90l-29 22l3-23H27Z"/><path d="M69 53q4-19 25-14q21 8 0 26l-8 7v11M85 95h1"/>',
      'person':'<path d="M60 59C38 22 105 11 110 44C118 85 61 90 60 59ZM32 135q0-48 53-48q55 0 56 48"/>',
      'file':'<path d="M43 15h64l29 29v92H42Z M104 17v32h29M61 68h54M61 87h45M61 106h33"/>',
      'hub':'<rect x="26" y="30" width="127" height="90" rx="12"/><path d="M48 52h25v22H48ZM104 78h26v23h-26ZM75 62h29v27M73 101H48V75"/>',
    }
    return '<svg class="doodle" viewBox="0 0 180 155" aria-hidden="true">'+shapes[kind]+'</svg>'

def card(id,label,kind,x,y,color='blue',small='',width=370):
    return f'<div id="{id}" class="sticker {color}" style="left:{x}px;top:{y}px;width:{width}px">{icon(kind)}<div class="card-label">{label}</div>'+ (f'<div class="card-small">{small}</div>' if small else '')+'</div>'

CSS='''
@font-face{font-family:Advercase;src:url('assets/AdvercaseFont-Regular.ttf')}@font-face{font-family:Advercase;src:url('assets/Advercase-Font-Italic.ttf');font-style:italic}@font-face{font-family:Montserrat;src:url('assets/Montserrat.woff2');font-weight:100 900}
*{box-sizing:border-box}body{margin:0;background:#35241F;color:#2B1E19;font-family:Montserrat}#root{position:relative;width:100%;height:100%;overflow:hidden}.clip{position:absolute}.camera{position:absolute;inset:0;transform-origin:50% 42%}.camera video{width:100%;height:100%;object-fit:cover}.paper-slot{inset:0;z-index:5}.paper{position:absolute;inset:0;background:#F2EBDD;background-image:linear-gradient(90deg,#7b5a4909 1px,transparent 1px),linear-gradient(#7b5a4909 1px,transparent 1px);background-size:54px 54px;border-left:18px solid #C4D6DA}.eyebrow{position:absolute;left:75px;top:151px;width:800px;font-size:24px;font-weight:650;letter-spacing:3px;text-transform:uppercase;color:#46513D}h1{position:absolute;left:73px;top:224px;width:810px;margin:0;font-family:Advercase;font-weight:400;font-size:102px;line-height:1.28;letter-spacing:-1px}h1 span{display:block}.sub{position:absolute;left:76px;top:452px;width:770px;font-size:29px;line-height:1.5;margin:0}.folio{position:absolute;left:78px;right:165px;top:1580px;border-top:1px solid #7B5A4960;padding-top:22px;font-size:19px;letter-spacing:3px;color:#46513D}.folio span{float:right;font-size:16px}.sticker{position:absolute;height:228px;background:#C4D6DA;border:10px solid #FAF6EF;border-radius:35px 26px 42px 25px;box-shadow:5px 9px 0 #35241F16;display:flex;flex-direction:column;align-items:center;justify-content:center;transform-origin:center center}.sticker.sage{background:#AAB6A0}.sticker.ivory{background:#FAF6EF;border-color:#C0CACE}.sticker.stone{background:#C0CACE}.doodle{width:145px;height:127px;stroke:#35241F;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;fill:none}.card-label{font-size:28px;font-weight:650;line-height:1.2;text-align:center}.card-small{font-size:22px;margin-top:9px;text-align:center}.connections{position:absolute;inset:0;width:1080px;height:1920px;fill:none;stroke:#7B5A49;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}.caption{z-index:50;left:75px;top:1340px;width:810px;text-align:center;font-family:Advercase;font-size:76px;line-height:1.1;color:#FAF6EF}.caption span{display:inline-block;background:#35241F;padding:6px 20px 13px;border-radius:15px;max-width:810px}.brand{position:absolute;left:78px;top:137px;font-size:21px;font-weight:600;letter-spacing:3px;color:#FAF6EF;background:#35241F;padding:12px 17px;border-radius:5px}.metric{font-family:Advercase;font-size:148px;line-height:1.04}.small-label{font-family:Montserrat;font-size:26px;line-height:1.5;font-weight:600;letter-spacing:1px}.hook-stat{position:absolute;left:77px;top:945px;width:730px;height:196px;background:#F2EBDD;border:8px solid #FAF6EF;border-radius:33px 27px 37px 23px;box-shadow:6px 9px 0 #35241F28;padding:8px 28px}.hook-stat .metric{font-size:118px;display:inline-block}.hook-stat .small-label{display:inline-block;width:175px;margin-left:23px;vertical-align:top;margin-top:30px}.pill{position:absolute;border:7px solid #FAF6EF;background:#C4D6DA;padding:17px 23px;border-radius:22px 30px 20px 27px;font-size:29px;font-weight:650}.numberbox{position:absolute;left:79px;top:595px;width:800px;text-align:center}.numberbox .metric{font-size:152px;line-height:1.2;margin:14px 0}.connections path,.goal-arrow path{opacity:0}#goal-sheet h1{font-size:90px;line-height:1.35}.goal-arrow{position:absolute;left:175px;top:831px;width:630px;height:190px;stroke:#7B5A49;stroke-width:6;fill:none;stroke-linecap:round;stroke-linejoin:round}.screenshot{position:absolute;left:74px;top:598px;width:810px;height:530px;border:12px solid #FAF6EF;border-radius:22px;overflow:hidden;box-shadow:8px 12px 0 #35241F1A;background:#0d1117}.screenshot img{position:absolute;left:0;top:-60px;width:1080px;height:auto}.note{position:absolute;left:80px;top:1160px;width:770px;font-size:27px;line-height:1.45}.tool-label{position:absolute;left:82px;top:986px;background:#F2EBDD;border:7px solid #FAF6EF;border-radius:26px;padding:20px 30px;font-size:36px;font-weight:600}.question{position:absolute;left:75px;top:1000px;width:800px;background:#F2EBDD;border:8px solid #FAF6EF;border-radius:28px;padding:22px 25px;font-family:Advercase;font-size:92px;line-height:1.08}.typed-char{display:inline-block;white-space:pre}.tag{position:absolute;left:84px;top:1160px;width:770px;padding:23px;background:#46513D;color:#FAF6EF;text-align:center;font-size:29px;font-weight:600;border-radius:17px}.badge{position:absolute;left:340px;top:737px;border:7px solid #FAF6EF;border-radius:20px;background:#35241F;color:#FAF6EF;padding:18px 28px;font-size:28px;font-weight:650}.goalbar{position:absolute;left:112px;width:285px;background:#AAB6A0;border:9px solid #FAF6EF;border-radius:20px 20px 0 0;transform-origin:50% 100%}.chart-label{position:absolute;top:1130px;width:340px;text-align:center;font-size:29px;font-weight:650}.chart-value{position:absolute;font-family:Advercase;font-size:96px;width:340px;text-align:center}.goal-note{position:absolute;left:160px;top:1233px;width:650px;text-align:center;font-size:24px;color:#46513D}
'''
