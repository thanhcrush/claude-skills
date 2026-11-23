# -*- coding: utf-8 -*-
"""
Quét nét theo từng trục: gom đoạn thẳng theo toạ độ cố định, ghép cặp đúng bề dày,
loại phần trùng cột, in ra bảng đoạn để người đọc kiểm.

CẢNH BÁO: kết quả là ỨNG VIÊN, không phải danh sách xác nhận.
Với TƯỜNG phải đối chiếu mặt bằng render trước khi tin (2625: một bức 7 m ra 0,51 m).

Dùng:
  python3 quet_theo_truc.py flat.pkl --goc 1518634,-12398 \
     --layer "A-TUONG 0.5" --day 100,200,300 --layer-cot COTKC,CC --box=-600,-700,15000,1200

LƯU Ý argparse: tham số bắt đầu bằng dấu trừ phải viết liền dấu bằng,
ví dụ --vung=-1200,-1200,15400,15200 (không viết --vung "-1200,...").
"""
import sys, pickle, argparse, collections

def gom(D, minlen=50):
    keys = sorted(D); out = {}
    for k in keys:
        tgt = next((kk for kk in out if abs(kk-k) <= 3), None)
        (out.setdefault(tgt if tgt is not None else k, [])).extend(D[k])
    for k in out:
        L = sorted(out[k]); m = []
        for a,b in L:
            if m and a <= m[-1][1]+2: m[-1][1] = max(m[-1][1], b)
            else: m.append([a,b])
        out[k] = [(a,b) for a,b in m if b-a >= minlen]
    return out

def tach(GEO, X0, Y0, layers, box):
    V = collections.defaultdict(list); H = collections.defaultdict(list)
    for lay,k,P,ex in GEO:
        if lay not in layers or k not in ("L","P","S"): continue
        Q = [(x-X0,y-Y0) for x,y in P]
        if not all(box[0]<=u<=box[2] and box[1]<=v<=box[3] for u,v in Q): continue
        if k == "S":
            xs=[q[0] for q in Q]; ys=[q[1] for q in Q]
            V[round(min(xs))].append((min(ys),max(ys))); V[round(max(xs))].append((min(ys),max(ys)))
            H[round(min(ys))].append((min(xs),max(xs))); H[round(max(ys))].append((min(xs),max(xs)))
            continue
        loop = Q+[Q[0]] if (k=="P" and ex is True) else Q
        for (ax,ay),(bx,by) in zip(loop, loop[1:]):
            if abs(ax-bx)<3 and abs(ay-by)>3:   V[round((ax+bx)/2)].append((min(ay,by),max(ay,by)))
            elif abs(ay-by)<3 and abs(ax-bx)>3: H[round((ay+by)/2)].append((min(ax,bx),max(ax,bx)))
    return gom(V), gom(H)

def cap(D, days, minlen=150, tol=15):
    ks = sorted(D); res = []
    for i,c1 in enumerate(ks):
        for c2 in ks[i+1:]:
            w = c2-c1
            if w > max(days)+tol: break
            if not any(abs(w-t) <= tol for t in days): continue
            mids = [k for k in ks if c1+20 < k < c2-20]
            for a1,b1 in D[c1]:
                for a2,b2 in D[c2]:
                    a,b = max(a1,a2), min(b1,b2)
                    if b-a < minlen: continue
                    if any(min(b,b3)-max(a,a3) > 0.7*(b-a) for k in mids for a3,b3 in D[k]): continue
                    res.append((c1,c2,round(w),round(a),round(b)))
    return sorted(res)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pkl"); ap.add_argument("--goc", required=True)
    ap.add_argument("--layer", required=True)
    ap.add_argument("--day", default="100,200,300")
    ap.add_argument("--layer-cot", default="")
    ap.add_argument("--box", default="-3500,-3500,18500,17500")
    a = ap.parse_args()
    X0,Y0 = [float(v) for v in a.goc.split(",")]
    box = [float(v) for v in a.box.split(",")]
    days = [int(v) for v in a.day.split(",")]
    GEO,_ = pickle.load(open(a.pkl,"rb"))
    V,H = tach(GEO, X0, Y0, {a.layer}, box)
    print(f"=== TUYẾN DỌC (chạy theo Y, định vị bởi X) — layer {a.layer} ===")
    for c1,c2,w,x,y in cap(V, days): print(f"  x {c1:7}..{c2:7} dày={w:4}  y {x:7}..{y:7}  dài={y-x:7}")
    print(f"=== TUYẾN NGANG (chạy theo X, định vị bởi Y) ===")
    for c1,c2,w,x,y in cap(H, days): print(f"  y {c1:7}..{c2:7} dày={w:4}  x {x:7}..{y:7}  dài={y-x:7}")
    if a.layer_cot:
        Vc,Hc = tach(GEO, X0, Y0, set(a.layer_cot.split(",")), box)
        print("\n=== CỘT (để loại khỏi chiều dài) ===")
        for c in sorted(Vc)[:200]:
            for s,e in Vc[c]:
                if e-s <= 800: print(f"  x={c:7}  y {s:7}..{e:7}")
    print("\n⚠ Đây là ỨNG VIÊN. Phải render mặt bằng và đối chiếu trước khi dùng làm số.")

if __name__ == "__main__": main()
