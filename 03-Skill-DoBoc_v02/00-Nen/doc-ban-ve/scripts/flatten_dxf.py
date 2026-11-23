# -*- coding: utf-8 -*-
"""
Bung block DXF đệ quy, entity con ở layer '0' kế thừa layer của INSERT cha.
Không bung thì mất gần hết nét (2611: 35.000 -> 315.000 segment).

Dùng:  python3 flatten_dxf.py BANVE.dxf [ra.pkl]
Kết quả pickle: (GEO, INS)
  GEO = [(layer, kind, [(x,y)...], extra), ...]   kind: L line · P polyline · S solid · T text · A arc · C circle
  INS = [(ten_block, x, y, [gia tri ATTRIB]), ...]
"""
import sys, pickle, ezdxf

def flatten(path):
    doc = ezdxf.readfile(path); msp = doc.modelspace()
    GEO, INS = [], []

    def emit(e, lay):
        t = e.dxftype()
        try:
            if t == "LINE":
                GEO.append((lay,"L",[(e.dxf.start.x,e.dxf.start.y),(e.dxf.end.x,e.dxf.end.y)],False))
            elif t == "LWPOLYLINE":
                GEO.append((lay,"P",[(a,b) for a,b,*_ in e.get_points()],bool(e.closed)))
            elif t == "POLYLINE":
                GEO.append((lay,"P",[(v.dxf.location.x,v.dxf.location.y) for v in e.vertices],bool(e.is_closed)))
            elif t == "SOLID":
                Q=[]
                for i in range(4):
                    try: v=e[i]; Q.append((v[0],v[1]))
                    except Exception: pass
                GEO.append((lay,"S",Q,True))
            elif t in ("TEXT","MTEXT"):
                s = e.dxf.text if t=="TEXT" else e.text
                h = e.dxf.height if t=="TEXT" else e.dxf.char_height
                GEO.append((lay,"T",[(e.dxf.insert.x,e.dxf.insert.y)],(s,h)))
            elif t == "ARC":
                GEO.append((lay,"A",[(e.dxf.center.x,e.dxf.center.y)],(e.dxf.radius,e.dxf.start_angle,e.dxf.end_angle)))
            elif t == "CIRCLE":
                GEO.append((lay,"C",[(e.dxf.center.x,e.dxf.center.y)],e.dxf.radius))
        except Exception:
            pass

    def walk(container, depth=0, parent_layer=None):
        for e in container:
            lay = e.dxf.layer
            if lay == "0" and parent_layer:      # <-- điểm mấu chốt
                lay = parent_layer
            if e.dxftype() == "INSERT":
                INS.append((e.dxf.name, e.dxf.insert.x, e.dxf.insert.y,
                            [a.dxf.text for a in e.attribs]))
                if depth < 6:
                    try: walk(list(e.virtual_entities()), depth+1, lay)
                    except Exception: pass
            else:
                emit(e, lay)

    walk(msp)
    # Ghi chú: text bảng ghi chú / mác BT có thể nằm trong ĐỊNH NGHĨA block,
    # không được INSERT vào msp -> quét thêm doc.blocks nếu nghi thiếu.
    return GEO, INS

if __name__ == "__main__":
    src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else "flat.pkl"
    GEO, INS = flatten(src)
    pickle.dump((GEO, INS), open(out, "wb"))
    import collections
    c = collections.Counter(g[0] for g in GEO)
    print(f"GEO {len(GEO)} · INS {len(INS)} -> {out}")
    print("Layer nhiều nhất:")
    for k, v in c.most_common(15): print(f"  {v:7d}  {k}")
