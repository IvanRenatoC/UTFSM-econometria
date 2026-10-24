"""Genera 45 segundos de puntos animados, sin pista de audio.
Requiere Pillow y ffmpeg. Ejecutar: python3 herramientas/generar_video_datasets.py
"""
from pathlib import Path
import subprocess,json,math,random
from PIL import Image,ImageDraw,ImageFont
from video_datasets import CHAPTERS
ROOT=Path(__file__).resolve().parent.parent
MEDIA=ROOT/'media';MEDIA.mkdir(exist_ok=True)
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def f(size,weight=False):return ImageFont.truetype(BOLD if weight else FONT,size)
NAVY='#1b2a5e';BLUE='#0160a0';GOLD='#f8c751';GREEN='#00875a'
YEARS=list(range(2020,2026))
VALUES=[[4,6,5,8,7,10],[10,9,12,11,14,13],[16,15,18,17,19,20]]
COLORS=[BLUE,GOLD,GREEN]
STARTS=[]
for chapter in range(3):
 rng=random.Random(320+chapter)
 STARTS.append([(rng.uniform(200,1100),rng.uniform(245,505)) for _ in range(18 if chapter==2 else 6)])
def smooth(value):
 value=max(0,min(1,value));return value*value*(3-2*value)
def frame(chapter,time):
 c=CHAPTERS[chapter];im=Image.new('RGB',(1280,720),'white');d=ImageDraw.Draw(im)
 d.text((48,25),'ECONOMETRÍA · TIPOS DE DATASETS',font=f(23,True),fill=NAVY)
 d.text((1070,25),f'{chapter+1} / 3 · 15 s',font=f(23,True),fill=BLUE)
 d.line((48,69,1232,69),fill=GOLD,width=4)
 d.text((48,91),c['title'],font=f(42,True),fill=NAVY)
 d.text((48,146),c['subtitle'],font=f(26),fill=BLUE)
 # Axes are introduced as the cloud orders itself.
 reveal=smooth((time-2)/2)
 axiscolor=tuple(round(255+(v-255)*reveal) for v in (160,175,191))
 d.line((150,530,1180,530),fill=axiscolor,width=2)
 d.line((150,220,150,530),fill=axiscolor,width=2)
 if time>=3:
  d.text((55,205),'Valor',font=f(23),fill=NAVY)
  for value in (0,5,10,15,20):
   y=530-value/22*280
   d.text((106,y-12),str(value),font=f(20),fill=NAVY)
  for j in range(6):
   x=230+j*170
   label=chr(65+j) if chapter==0 else str(YEARS[j])
   d.text((x,547),label,font=f(22),fill=NAVY,anchor='mt')
  d.text((670,580),'Unidad (todas en 2020)' if chapter==0 else 'Tiempo (año)',font=f(22,True),fill=NAVY,anchor='mt')
 positions=[]
 n=18 if chapter==2 else 6
 for index in range(n):
  group=index//6 if chapter==2 else 0;j=index%6
  value=([5,12,8,16,10,19][j] if chapter==0 else VALUES[group][j])
  target=(230+j*170,530-value/22*280)
  progress=smooth((time-2-index*.12)/5)
  start=STARTS[chapter][index]
  positions.append((start[0]+(target[0]-start[0])*progress,start[1]+(target[1]-start[1])*progress))
 if chapter>0 and time>9:
  fraction=smooth((time-9)/3)
  for group in range(3 if chapter==2 else 1):
   for j in range(5):
    a=positions[group*6+j];b=positions[group*6+j+1]
    segment=max(0,min(1,fraction*5-j))
    if segment>0:d.line((a[0],a[1],a[0]+(b[0]-a[0])*segment,a[1]+(b[1]-a[1])*segment),fill=COLORS[group],width=3)
 for index,(x,y) in enumerate(positions):
  group=index//6 if chapter==2 else 0;color=COLORS[group]
  d.ellipse((x-10,y-10,x+10,y+10),fill=color,outline=NAVY,width=2)
  if chapter==0 and time<3:d.text((x+14,y-12),chr(65+index),font=f(21),fill=NAVY)
 if chapter==1:d.text((900,190),'Azul: unidad A',font=f(22,True),fill=BLUE)
 if chapter==2:
  for group in range(3):
   x=755+group*155;d.ellipse((x,193,x+15,208),fill=COLORS[group],outline=NAVY)
   d.text((x+24,186),f'Unidad {chr(65+group)}',font=f(21),fill=NAVY)
 cue=c['cues'][0 if time<4 else 1 if time<10 else 2]
 d.text((640,635),cue,font=f(26,True),fill=NAVY,anchor='mt')
 d.text((48,687),'Ejemplo ficticio · Cada punto representa una observación.',font=f(18),fill=BLUE)
 d.text((1230,687),f'{int(chapter*15+time):02d} / 45 s',font=f(18),fill=BLUE,anchor='rt')
 return im
fps=20
proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r',str(fps),'-i','pipe:0','-an','-t','45','-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',str(MEDIA/'tipos-datasets.mp4')],stdin=subprocess.PIPE)
for tick in range(45*fps):
 chapter=tick//(15*fps);time=(tick%(15*fps))/fps
 proc.stdin.write(frame(chapter,time).tobytes())
proc.stdin.close()
if proc.wait():raise RuntimeError('Falló la generación del video')
frame(0,11).save(MEDIA/'tipos-datasets-portada.png')
for chapter in range(3):frame(chapter,12).save(Path('/tmp')/f'datasets32-{chapter}.png')
(MEDIA/'tipos-datasets-capitulos.json').write_text(json.dumps([dict(start=i*15,duration=15) for i in range(3)],indent=2))
def stamp(seconds):return f'00:00:{seconds:02d}.000'
vtt=['WEBVTT','']
for i,c in enumerate(CHAPTERS):
 for start,end,cue in zip((0,4,10),(4,10,15),c['cues']):vtt += [f'{stamp(i*15+start)} --> {stamp(i*15+end)}',cue,'']
(MEDIA/'tipos-datasets-es.vtt').write_text('\n'.join(vtt))
print('Video silencioso: 45 segundos, 3 capítulos, 900 fotogramas.')
