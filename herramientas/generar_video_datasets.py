"""Genera el video local con voz española del sistema y gráficos de las tablas.
Requiere macOS (say), Pillow y ffmpeg. --prepare crea los guiones en /tmp;
--render reutiliza las narraciones allí guardadas. Sin opciones hace todo.
"""
from pathlib import Path
import sys,subprocess,json,math,textwrap
from PIL import Image,ImageDraw,ImageFont
from video_datasets import CHAPTERS
ROOT=Path(__file__).resolve().parent.parent
TEMP=Path('/tmp/utfsm-video-datasets');TEMP.mkdir(exist_ok=True)
MEDIA=ROOT/'media';MEDIA.mkdir(exist_ok=True)
for i,c in enumerate(CHAPTERS): (TEMP/f'{i}.txt').write_text(c['narration'])
if '--prepare' in sys.argv: sys.exit()
if '--render' not in sys.argv:
 for i in range(len(CHAPTERS)):
  subprocess.run(['say','-v','Paulina','-r','165','-f',str(TEMP/f'{i}.txt'),'-o',str(TEMP/f'{i}.aiff')],check=True)
font='/System/Library/Fonts/Supplemental/Arial.ttf'
bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def f(size,weight=False):return ImageFont.truetype(bold if weight else font,size)
navy='#1b2a5e';blue='#0160a0';gold='#f8c751'
durations=[];timing=[];start=0
for i,c in enumerate(CHAPTERS):
 raw=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(TEMP/f'{i}.aiff')]))
 duration=math.ceil(raw+2);durations.append(duration);timing.append(dict(start=start,duration=duration));start+=duration

def frame(i,t):
 c=CHAPTERS[i];im=Image.new('RGB',(1280,720),'white');d=ImageDraw.Draw(im)
 d.rectangle((0,0,1280,76),fill=navy);d.rectangle((0,76,1280,81),fill=gold)
 d.text((40,23),'ECONOMETRÍA · TIPOS DE DATASETS',font=f(26,True),fill='white')
 d.text((1050,25),f'{i+1} / 4',font=f(25,True),fill=gold)
 d.text((45,108),c['title'],font=f(43,True),fill=navy)
 d.text((45,164),c['subtitle'],font=f(27),fill=blue)
 widths=[220,145,200,185];left=45;top=230;rh=58
 active=min(3,int(t/max(1,durations[i]-4)*4))
 for r, row in enumerate([c['headers']]+c['rows']):
  y=top+r*rh;x=left
  for j,text in enumerate(row):
   bg=navy if r==0 else ('#fff0bb' if r-1==active else '#edf2f7')
   d.rectangle((x,y,x+widths[j],y+rh),fill=bg,outline='white',width=3)
   d.text((x+14,y+16),text,font=f(25,r==0),fill='white' if r==0 else navy);x+=widths[j]
 d.rounded_rectangle((840,230,1230,520),radius=18,fill='#edf2f7')
 for k,line in enumerate(textwrap.wrap(c['key'],24)):d.text((862,255+k*35),line,font=f(27,True),fill=navy)
 d.text((860,435),'Modelo ilustrativo',font=f(22),fill=blue)
 d.text((860,475),c['formula'],font=f(24),fill=navy)
 d.text((45,548),'Ejemplos ficticios · Las tablas no son nuevas bases empíricas.',font=f(23),fill=blue)
 d.rounded_rectangle((45,595,1230,670),radius=12,fill=navy)
 d.text((67,615),c['key'],font=f(29,True),fill='white')
 d.rectangle((45,694,1230,701),fill='#dce2ea');d.rectangle((45,694,45+int(1185*t/durations[i]),701),fill=gold)
 return im

for i,c in enumerate(CHAPTERS):
 proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','5','-i','pipe:0','-i',str(TEMP/f'{i}.aiff'),'-af','apad','-t',str(durations[i]),'-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-r','25','-c:a','aac','-b:a','96k','-movflags','+faststart',str(TEMP/f'{i}.mp4')],stdin=subprocess.PIPE)
 for tick in range(durations[i]*5):proc.stdin.write(frame(i,tick/5).tobytes())
 proc.stdin.close()
 if proc.wait():raise RuntimeError('Falló ffmpeg')
frame(0,0).save(MEDIA/'tipos-datasets-portada.png')
(TEMP/'concat.txt').write_text('\n'.join(f"file '{TEMP}/{i}.mp4'" for i in range(len(CHAPTERS))))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(TEMP/'concat.txt'),'-c','copy','-movflags','+faststart',str(MEDIA/'tipos-datasets.mp4')],check=True)
(MEDIA/'tipos-datasets-capitulos.json').write_text(json.dumps(timing,indent=2))
def stamp(seconds):
 ms=round(seconds*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}.{ms%1000:03}'
vtt=['WEBVTT','']
for c,entry in zip(CHAPTERS,timing):
 sentences=[s.strip()+'.' for s in c['narration'].split('.') if s.strip()];total=sum(len(s) for s in sentences);position=entry['start']
 for sentence in sentences:
  end=position+(entry['duration']-2)*len(sentence)/total
  vtt += [f'{stamp(position)} --> {stamp(end)}',sentence,''];position=end
(MEDIA/'tipos-datasets-es.vtt').write_text('\n'.join(vtt))
print(f'Video: {start} segundos; {len(CHAPTERS)} capítulos. '+str(MEDIA/'tipos-datasets.mp4'))
