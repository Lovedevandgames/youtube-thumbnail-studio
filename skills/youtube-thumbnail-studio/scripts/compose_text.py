"""Exact thumbnail text in your brand font + safe-zone check.
python3 compose_text.py in.jpg out.jpg --text "NO|AGENCY" --font serif --size 124 --xy 52,40 --color 34,26,24 [--shadow] [--fontfile path]
Lines are split by "|". Position and size use a 1280x720 grid. A source >= 3840 px also writes out_4k.jpg."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(__file__)); from _fonts import font
from PIL import Image, ImageDraw
a=argparse.ArgumentParser(); a.add_argument("src"); a.add_argument("out"); a.add_argument("--text",required=True)
a.add_argument("--font",default="sans",choices=["serif","sans","impact","ui"]); a.add_argument("--fontfile")
a.add_argument("--size",type=int,default=110); a.add_argument("--xy",default="52,40"); a.add_argument("--color",default="250,246,240")
a.add_argument("--shadow",action="store_true"); a.add_argument("--spacing",type=int,default=6); o=a.parse_args()
src=Image.open(o.src).convert("RGB"); big=src.width>=3840; W,H=(3840,2160) if big else (1280,720); k=W/1280
im=src.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(im); f=font(o.font,int(o.size*k),o.fontfile)
x0,y=[int(v)*k for v in o.xy.split(",")]; col=tuple(int(c) for c in o.color.split(",")); boxes=[]
for line in o.text.split("|"):
    x=x0
    for ch in line:
        if o.shadow: d.text((x+3*k,y+4*k),ch,font=f,fill=(10,8,8))
        d.text((x,y),ch,font=f,fill=col); x+=d.textlength(ch,font=f)+o.spacing*k
    boxes.append((x0,y,x,y+o.size*k)); y+=o.size*k*1.05
if big: im.save(os.path.splitext(o.out)[0]+"_4k.jpg",quality=92)
im.resize((1280,720),Image.LANCZOS).save(o.out,quality=90)
bad=[b for b in boxes if b[2]>W*0.78 and b[3]>H*0.82] + [b for b in boxes if b[0]<W*0.2 and b[3]>H*0.9]
print("WARNING: text overlaps the duration badge / chapter zone" if bad else "OK", o.out)
