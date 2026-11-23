# -*- coding: utf-8 -*-
"""
Lập bản đồ view: dò lưới trục từng mặt bằng + tiêu đề view + số hiệu tờ.
Model space chứa TẤT CẢ các tờ xếp cạnh nhau -> phải biết đang đọc tờ nào trước khi đo.

Dùng:  python3 ban_do_view.py flat.pkl [ten_layer_truc]
"""
import os, sys, pickle, collections
import numpy as np
# v02: sửa đường dẫn chạy được trên Windows; module đúng tên là giai_ma_vni (bản gốc gọi nhầm giai_ma_tcvn3)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from giai_ma_vni import vn

def cum(vals, gap):
    idx = np.argsort(vals); groups=[]; cur=[idx[0]]
    for a,b in zip(idx, idx[1:]):
        if vals[b]-vals[a] > gap: groups.append(cur); cur=[]
        cur.append(b)
    groups.append(cur); return groups

def main(pkl, layer_truc=None):
    GEO, INS = pickle.load(open(pkl,"rb"))
    lays = collections.Counter(g[0] for g in GEO)
    if not layer_truc:
        cand = [l for l in lays if "TRUC" in l.upper()]
        layer_truc = cand[0] if cand else None
        print("Layer trục đoán:", layer_truc)
    L = [(P[0][0],P[0][1],P[1][0],P[1][1]) for lay,k,P,_ in GEO
         if lay==layer_truc and k=="L" and len(P)==2]
    print(f"{len(L)} nét trục")
    if L:
        cen = np.array([[(a+c)/2,(b+d)/2] for a,b,c,d in L])
        for g in cum(cen[:,0], 20000):
            for h in cum(cen[g,1], 15000):
                ii=[g[k] for k in h]
                V=[L[i] for i in ii if abs(L[i][0]-L[i][2])<1]
                H=[L[i] for i in ii if abs(L[i][1]-L[i][3])<1]
                if not V or not H: continue
                xs=sorted({round(v[0]) for v in V}); ys=sorted({round(h_[1]) for h_ in H})
                print(f"\nMẶT BẰNG  gốc=({xs[0]}, {ys[0]})")
                print("  trục dọc  x:", xs, "-> nhịp", [xs[i+1]-xs[i] for i in range(len(xs)-1)])
                print("  trục ngang y:", ys, "-> nhịp", [ys[i+1]-ys[i] for i in range(len(ys)-1)])
    # tieu de view = TEXT cao bat thuong
    T = [(P[0][0],P[0][1],vn(ex[0]).strip(),ex[1]) for lay,k,P,ex in GEO if k=="T" and ex[1]]
    if T:
        hs = sorted({round(t[3]) for t in T}, reverse=True)[:4]
        print("\nCác cỡ chữ lớn nhất:", hs)
        for x,y,s,h in sorted([t for t in T if round(t[3]) in hs[:2]], key=lambda r:(-r[1],r[0]))[:60]:
            if s: print(f"  h={h:6.0f} ({x:9.0f},{y:9.0f})  {s[:60]}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None)
