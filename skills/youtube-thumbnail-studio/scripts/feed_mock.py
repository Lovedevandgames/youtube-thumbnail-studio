"""Mock YouTube feed with your thumbnails among real competitors (dark + light) and a 168x94 strip.
python3 feed_mock.py --query "video topic" --ours "a.jpg::Title A" --ours "b.jpg::Title B" --out feed
Needs yt-dlp (on PATH or python3 -m yt_dlp). No videos are downloaded - only public thumbnails from i.ytimg.com."""
import argparse, json, os, shutil, subprocess, sys, textwrap, urllib.request
sys.path.insert(0, os.path.dirname(__file__)); from _fonts import font
from PIL import Image, ImageDraw
a=argparse.ArgumentParser(); a.add_argument("--query",required=True); a.add_argument("--ours",action="append",default=[])
a.add_argument("--n",type=int,default=6); a.add_argument("--out",default="feed"); o=a.parse_args(); os.makedirs(o.out,exist_ok=True)
cmd=[shutil.which("yt-dlp")] if shutil.which("yt-dlp") else [sys.executable,"-m","yt_dlp"]
r=subprocess.run(cmd+["--flat-playlist","-J","--extractor-args","youtube:lang=en",f"ytsearch{o.n}:{o.query}"],capture_output=True,text=True)
items=[]
for e in json.loads(r.stdout or "{}").get("entries",[]):
    p=f"{o.out}/{e['id']}.jpg"
    if not os.path.exists(p): urllib.request.urlretrieve(f"https://i.ytimg.com/vi/{e['id']}/mqdefault.jpg",p)
    v=e.get("view_count") or 0; vs=f"{v/1e6:.1f}M views" if v>=1e6 else f"{v//1000}K views"
    items.append((p,e.get("title",""),f"{e.get('channel','')} · {vs}",e.get("duration_string") or "",False))
ours=[(s.split("::")[0],s.split("::")[1],"OUR CHANNEL · new","",True) for s in o.ours]; rows=[]
for i,x in enumerate(items):
    if i%2==0 and ours: rows.append(ours.pop(0))
    rows.append(x)
rows+=ours; fb=font("ui",23); fs=font("ui_regular",18)
for theme,bg,fg,mut in (("dark",(15,15,15),(241,241,241),(170,170,170)),("light",(255,255,255),(15,15,15),(96,96,96))):
    TH,TW=189,336; img=Image.new("RGB",(880,len(rows)*(TH+16)+16),bg); d=ImageDraw.Draw(img)
    for i,(p,t,ch,dur,our) in enumerate(rows):
        y=16+i*(TH+16); img.paste(Image.open(p).convert("RGB").resize((TW,TH),Image.LANCZOS),(16,y))
        if our: d.rectangle((12,y-4,TW+19,y+TH+3),outline=(232,120,80),width=3)
        if dur:
            w=d.textlength(dur,font=fs)+12; d.rounded_rectangle((TW+10-w,y+TH-30,TW+10,y+TH-6),4,fill=(0,0,0)); d.text((TW+16-w,y+TH-29),dur,font=fs,fill="white")
        ty=y+4
        for ln in textwrap.wrap(t,34)[:2]: d.text((372,ty),ln,font=fb,fill=fg); ty+=30
        d.text((372,ty+6),ch,font=fs,fill=mut)
    img.save(f"{o.out}/feed_{theme}.png")
our=[x for x in rows if x[4]]
if our:
    s=Image.new("RGB",(len(our)*184+16,126),(15,15,15))
    for i,x in enumerate(our): s.paste(Image.open(x[0]).convert("RGB").resize((168,94),Image.LANCZOS),(16+i*184,16))
    s.resize((s.width*2,s.height*2),Image.NEAREST).save(f"{o.out}/small_168x94.png")
print("done:",o.out)
