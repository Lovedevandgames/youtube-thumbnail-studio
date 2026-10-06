"""Font lookup for macOS / Linux / Windows with a safe fallback."""
import os
from PIL import ImageFont
CANDS={
 "serif":[("/System/Library/Fonts/Supplemental/Didot.ttc",2),("/System/Library/Fonts/Supplemental/Bodoni 72.ttc",1),("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",0),("C:/Windows/Fonts/georgiab.ttf",0)],
 "sans":[("/System/Library/Fonts/Avenir Next.ttc",2),("/System/Library/Fonts/HelveticaNeue.ttc",1),("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",0),("C:/Windows/Fonts/arialbd.ttf",0)],
 "impact":[("/System/Library/Fonts/Supplemental/Impact.ttf",0),("C:/Windows/Fonts/impact.ttf",0),("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",0)],
 "ui":[("/System/Library/Fonts/HelveticaNeue.ttc",1),("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",0),("C:/Windows/Fonts/arialbd.ttf",0)],
 "ui_regular":[("/System/Library/Fonts/HelveticaNeue.ttc",0),("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",0),("C:/Windows/Fonts/arial.ttf",0)]}
def font(kind,size,path=None):
    if path: return ImageFont.truetype(path,size)
    for p,i in CANDS.get(kind,CANDS["sans"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p,size,index=i)
            except Exception: continue
    return ImageFont.load_default()
