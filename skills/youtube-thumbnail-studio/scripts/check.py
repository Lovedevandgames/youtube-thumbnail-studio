"""Thumbnail QA: small-size previews (120, 168x94, 320x180), UI safe-zone overlay, file-size and ratio checks.
python3 check.py thumb.jpg [--vertical] --out check.png"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(__file__)); from _fonts import font
from PIL import Image, ImageDraw
a=argparse.ArgumentParser(); a.add_argument("img"); a.add_argument("--vertical",action="store_true"); a.add_argument("--out",default="check.png"); o=a.parse_args()
im=Image.open(o.img).convert("RGB"); w,h=im.size; kb=os.path.getsize(o.img)//1024
ratio=w/h; want=9/16 if o.vertical else 16/9; notes=[]
if abs(ratio-want)>0.02: notes.append(f"aspect {w}x{h} is not {'9:16' if o.vertical else '16:9'}")
if not o.vertical and w<1280: notes.append("smaller than 1280x720")
if kb>2048: notes.append(f"file {kb} KB > 2 MB")
big=im.resize((960,540) if not o.vertical else (405,720)); ov=big.copy(); d=ImageDraw.Draw(ov,"RGBA"); W,H=big.size
if o.vertical:
    for box in [(0,0,W,H*0.12),(0,H*0.75,W,H),(W*0.85,H*0.35,W,H*0.75)]: d.rectangle(box,fill=(255,0,0,70))
else:
    d.rectangle((W*0.78,H*0.82,W,H),fill=(255,0,0,80)); d.rectangle((0,H*0.92,W*0.2,H),fill=(255,160,0,70)); d.rectangle((W*0.86,0,W,H*0.14),fill=(255,160,0,50))
sizes=[(120,int(120*h/w)),(168,94),(320,180)] if not o.vertical else [(68,120),(108,192)]
canvas=Image.new("RGB",(W+40+max(s[0] for s in sizes)*2+40, max(H, sum(s[1]*2+40 for s in sizes))+60),(15,15,15)); canvas.paste(ov,(20,40))
dd=ImageDraw.Draw(canvas); f=font("ui_regular",20); dd.text((20,10),"UI zones (red = keep key elements out)",font=f,fill="white")
y=40
for sw,sh in sizes:
    t=im.resize((sw,sh),Image.LANCZOS).resize((sw*2,sh*2),Image.NEAREST); canvas.paste(t,(W+60,y)); dd.text((W+60,y-24),f"{sw}×{sh} (×2)",font=f,fill="white"); y+=sh*2+48
canvas.save(o.out); print("OK" if not notes else "; ".join(notes), "→", o.out)
