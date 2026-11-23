# -*- coding: utf-8 -*-
# TRIEN KHAI 2: ghi chu mat bang - kich thuoc 3 lop (chi tiet o cua -> truc -> tong), tag phong
# (ten + dien tich), tag cua di (Mark) va cua so (Type Mark). Chay lai duoc: xoa dim/tag cu
# trong cac view MB_GHI_CHU truoc khi ve.
from pyrevit.api import DB
from vn_revit import *

KIEU_DIM = "VN-Dim 2.5 gach xien"


def _view(doc, name):
    for v in collect(doc, DB.View):
        if not v.IsTemplate and v.Name == name:
            return v
    return None


def _xoa_cu(doc, v):
    ids = []
    for cls in (DB.Dimension, DB.IndependentTag, DB.SpatialElementTag):
        for e in DB.FilteredElementCollector(doc, v.Id).OfClass(cls):
            ids.append(e.Id)
    for i in ids:
        try:
            doc.Delete(i)
        except Exception:
            pass
    return len(ids)


def _day(doc, v, dt, refs, a, b):
    ra = DB.ReferenceArray()
    for r in refs:
        ra.Append(r)
    return doc.Create.NewDimension(v, DB.Line.CreateBound(a, b), ra, dt)


def chay(doc, hs):
    dt = tim_loai(doc, DB.DimensionType, KIEU_DIM)
    D = hs.DIM
    grids = collect(doc, DB.Grid)
    gx = sorted([g for g in grids if abs(g.Curve.GetEndPoint(0).X - g.Curve.GetEndPoint(1).X) < 1e-6],
                key=lambda g: g.Curve.GetEndPoint(0).X)
    gy = sorted([g for g in grids if g not in gx], key=lambda g: g.Curve.GetEndPoint(0).Y)
    gx_chinh = [g for g in gx if g.Name not in D["bo_truc_phu"]]
    xa, xb = gx[0].Curve.GetEndPoint(0).X - ft(500), gx[-1].Curve.GetEndPoint(0).X + ft(500)
    ya, yb = gy[0].Curve.GetEndPoint(0).Y - ft(500), gy[-1].Curve.GetEndPoint(0).Y + ft(500)
    tag_phong = [s for s in collect(doc, DB.FamilySymbol, DB.BuiltInCategory.OST_RoomTags, types=True)
                 if ten(s) == "Room Tag With Area"][0]
    tag_cua = collect(doc, DB.FamilySymbol, DB.BuiltInCategory.OST_DoorTags, types=True)[0]
    tag_so = collect(doc, DB.FamilySymbol, DB.BuiltInCategory.OST_WindowTags, types=True)[0]
    y_e = max(g.Curve.GetEndPoint(0).Y for g in gy)
    out = {}
    tr = DB.Transaction(doc, "vn: trien khai 2 - ghi chu mat bang")
    tr.Start()
    try:
        for name in hs.MB_GHI_CHU:
            v = _view(doc, name)
            lv = v.GenLevel
            r = {"xoa": _xoa_cu(doc, v), "dim": 0, "tag": 0}
            # truc so: phia duoi (truc + tong), phia tren (chi tiet + truc + tong)
            refs = [DB.Reference(g) for g in gx_chinh]
            _day(doc, v, dt, refs, DB.XYZ(xa, ft(D["duoi_truc"]), 0), DB.XYZ(xb, ft(D["duoi_truc"]), 0))
            _day(doc, v, dt, [refs[0], refs[-1]], DB.XYZ(xa, ft(D["duoi_tong"]), 0), DB.XYZ(xb, ft(D["duoi_tong"]), 0))
            _day(doc, v, dt, refs, DB.XYZ(xa, ft(D["tren_truc"]), 0), DB.XYZ(xb, ft(D["tren_truc"]), 0))
            _day(doc, v, dt, [refs[0], refs[-1]], DB.XYZ(xa, ft(D["tren_tong"]), 0), DB.XYZ(xb, ft(D["tren_tong"]), 0))
            r["dim"] += 4
            # chi tiet: mep cua so tuong truc E cua tang nay + truc
            ct = [(g.Curve.GetEndPoint(0).X, DB.Reference(g)) for g in gx_chinh]
            for fi in collect(doc, DB.FamilyInstance, DB.BuiltInCategory.OST_Windows):
                if fi.LevelId != lv.Id or abs(fi.Location.Point.Y - y_e) > ft(300):
                    continue
                try:
                    for kind in (DB.FamilyInstanceReferenceType.Left, DB.FamilyInstanceReferenceType.Right):
                        for rf in fi.GetReferences(kind):
                            off = fi.Location.Point.X + (-1 if kind == DB.FamilyInstanceReferenceType.Left else 1) * fi.Symbol.LookupParameter("Width").AsDouble() / 2
                            ct.append((off, rf))
                except Exception:
                    pass
            ct.sort(key=lambda t: t[0])
            try:
                _day(doc, v, dt, [t[1] for t in ct], DB.XYZ(xa, ft(D["tren_chi_tiet"]), 0), DB.XYZ(xb, ft(D["tren_chi_tiet"]), 0))
                r["dim"] += 1
            except Exception as ex:
                r["chi_tiet_loi"] = str(ex)[:100]
            # truc chu: ben trai (truc + tong)
            refy = [DB.Reference(g) for g in gy]
            _day(doc, v, dt, refy, DB.XYZ(ft(D["trai_truc"]), ya, 0), DB.XYZ(ft(D["trai_truc"]), yb, 0))
            _day(doc, v, dt, [refy[0], refy[-1]], DB.XYZ(ft(D["trai_tong"]), ya, 0), DB.XYZ(ft(D["trai_tong"]), yb, 0))
            r["dim"] += 2
            # tag phong
            for room in DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Rooms):
                if room.LevelId != lv.Id or room.Area <= 0:
                    continue
                p = room.Location.Point
                t = doc.Create.NewRoomTag(DB.LinkElementId(room.Id), DB.UV(p.X, p.Y), v.Id)
                t.ChangeTypeId(tag_phong.Id)
                r["tag"] += 1
            # tag cua di, cua so
            for cat, sym, dy in ((DB.BuiltInCategory.OST_Doors, tag_cua, -900), (DB.BuiltInCategory.OST_Windows, tag_so, 700)):
                for fi in collect(doc, DB.FamilyInstance, cat):
                    if fi.LevelId != lv.Id:
                        continue
                    p = fi.Location.Point
                    # chi tag cua thuoc tang (bo VK long thang cao tren tang tren)
                    try:
                        tg = DB.IndependentTag.Create(doc, sym.Id, v.Id, DB.Reference(fi), False,
                                                      DB.TagOrientation.Horizontal, DB.XYZ(p.X, p.Y + ft(dy if p.Y > ft(10000) else -dy), 0))
                        r["tag"] += 1
                    except Exception:
                        pass
            out[name.encode("unicode_escape") if hasattr(name, "encode") else name] = r
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return out
