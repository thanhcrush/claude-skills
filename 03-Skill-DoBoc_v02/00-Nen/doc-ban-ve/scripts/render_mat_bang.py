# -*- coding: utf-8 -*-
"""
Render mặt bằng ra PNG, tô màu theo layer, KÈM THƯỚC 1 m và nhãn trục.
Có thước thì đọc được vị trí bằng mắt và đối chiếu ngay với số đo từ vector.

Dùng:
  python3 render_mat_bang.py flat.pkl ra.png --goc 1518634,-12398 \
      --vung=-1200,-1200,15400,15200 --ppm 0.085 \
      --truc-so 1:0,2:5800,3:11600,4:14600 --truc-chu A:0,B:6900,C:13900

--vung là x0,y0,x1,y1 THEO HỆ GỐC (mm). ppm = pixel/mm:
  0,085 (~1500 px) đủ đọc layout cả mặt bằng · 0,45 để soi một dải trục.

LƯU Ý argparse: tham số bắt đầu bằng dấu trừ phải viết liền dấu bằng,
ví dụ --vung=-1200,-1200,15400,15200 (không viết --vung "-1200,...").
"""
import sys, math, pickle, argparse
from PIL import Image, ImageDraw, ImageFont

MAU = {  # layer chứa chuỗi -> (màu, độ dày)
 "TUONG":((0,0,0),3), "COT":((220,0,0),2), "CC":((220,0,0),2),
 "NETMANH":((0,90,220),2), "NET THAY":((0,150,0),2),
 "LAN CAN":((255,140,0),2), "HATCH":((200,200,230),1), "VAT DUNG":((190,190,190),1),
}
def mau_cua(lay):
    u = lay.upper()
    for k,v in MAU.items():
        if k in u: return v
    return ((150,150,150),1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pkl"); ap.add_argument("out")
    ap.add_argument("--goc", required=True)
    ap.add_argument("--vung", required=True)
    ap.add_argument("--ppm", type=float, default=0.085)
    ap.add_argument("--truc-so", default=""); ap.add_argument("--truc-chu", default="")
    a = ap.parse_args()
    X0,Y0 = [float(v) for v in a.goc.split(",")]
    x0,y0,x1,y1 = [float(v) for v in a.vung.split(",")]
    ppm = a.ppm; M = 80
    GEO,_ = pickle.load(open(a.pkl,"rb"))
    W = int((x1-x0)*ppm)+2*M; H = int((y1-y0)*ppm)+2*M
    im = Image.new("RGB",(W,H),(255,255,255)); d = ImageDraw.Draw(im)
    try:
        F  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",22)
        F2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
    except Exception:
        F = F2 = ImageFont.load_default()
    def T(gx,gy): return (M+(gx-x0)*ppm, H-M-(gy-y0)*ppm)

    for spec,horiz in ((a.truc_so,True),(a.truc_chu,False)):
        for item in [s for s in spec.split(",") if s]:
            nm,val = item.split(":"); v = float(val)
            if horiz:
                if x0<=v<=x1:
                    p=T(v,y0); q=T(v,y1); d.line([p,q],fill=(255,170,170))
                    d.text((p[0]-8,H-M+8),nm,fill=(200,0,0),font=F)
            else:
                if y0<=v<=y1:
                    p=T(x0,v); q=T(x1,v); d.line([p,q],fill=(255,170,170))
                    d.text((M-40,p[1]-10),nm,fill=(200,0,0),font=F)
    for gx in range(int(math.ceil(x0/1000))*1000, int(x1)+1, 1000):
        p=T(gx,y0); d.line([(p[0],M-12),(p[0],M-2)],fill=(0,0,255))
        d.text((p[0]-12,M-34),str(gx//1000),fill=(0,0,255),font=F2)
    for gy in range(int(math.ceil(y0/1000))*1000, int(y1)+1, 1000):
        p=T(x0,gy); d.line([(W-M+2,p[1]),(W-M+12,p[1])],fill=(0,0,255))
        d.text((W-M+16,p[1]-8),str(gy//1000),fill=(0,0,255),font=F2)

    for lay,k,P,ex in GEO:
        Q = [(px-X0,py-Y0) for px,py in P]
        if not any(x0-500<=u<=x1+500 and y0-500<=v<=y1+500 for u,v in Q): continue
        col,wd = mau_cua(lay)
        if k in ("L","P"):
            pts=[T(*q) for q in Q]
            if k=="P" and ex is True: pts.append(pts[0])
            if len(pts)>=2: d.line(pts,fill=col,width=wd)
        elif k=="S":
            d.polygon([T(*q) for q in Q],fill=col)
    im.save(a.out); print(a.out, im.size)

if __name__ == "__main__": main()
