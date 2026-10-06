"""Side-by-side comparison grid (2x2 or N) with labels. python3 grid.py a.png b.png c.png d.png --out grid.jpg --labels A B C D"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(__file__)); from _fonts import font
from PIL import Image, ImageDraw
a=argparse.ArgumentParser(); a.add_argument("images",nargs="+"); a.add_argument("--out",default="grid.jpg"); a.add_argument("--labels",nargs="*"); o=a.parse_args()
n=len(o.images); cols=2 if n>1 else 1; rows=(n+cols-1)//cols; W,H,g=960,540,24
s=Image.new("RGB",(cols*W+(cols+1)*g,rows*H+(rows+1)*g),(20,20,20)); d=ImageDraw.Draw(s); f=font("ui",44)
for i,p in enumerate(o.images):
    x=g+(i%cols)*(W+g); y=g+(i//cols)*(H+g); s.paste(Image.open(p).convert("RGB").resize((W,H),Image.LANCZOS),(x,y))
    lab=(o.labels[i] if o.labels and i<len(o.labels) else chr(65+i)); d.rectangle((x,y,x+70,y+64),fill=(0,0,0)); d.text((x+18,y+6),lab,font=f,fill="white")
s.save(o.out,quality=90); print(o.out)
