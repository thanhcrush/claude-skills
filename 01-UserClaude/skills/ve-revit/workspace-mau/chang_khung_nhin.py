# -*- coding: utf-8 -*-
# CHANG CUOI: can khung nhin 2D sau khi dung mo hinh (khong dich chuyen mo hinh).
#  - go Scope Box cua template (Scope Box khoa khung cat, dat CropBox khong an)
#  - doi 4 ky hieu mat dung ve tam cong trinh
#  - khung cat mat bang = luoi truc + LE; khung mat dung theo khoi nha
# Dung: import chang_khung_nhin; result = chang_khung_nhin.chay(doc, plan)
# plan can co TRUC_X, TRUC_Y [(ten, toa do mm)] va TANG [(khoa, ten, cao do mm)].
# Rut tu du an Cua Viet (10/11/2026). ASCII only.
from pyrevit.api import DB
from vn_revit import *
from System.Collections.Generic import List

LE = 2000          # le quanh luoi truc (mm)
DOI_TOI_THIEU = 2000  # ky hieu da o quanh tam (lech < 2 m) thi khong doi them


def _khung(plan):
    xs = [v for _, v in plan.TRUC_X]; ys = [v for _, v in plan.TRUC_Y]
    zs = [z for _, _, z in plan.TANG]
    return (min(xs), min(ys), max(xs), max(ys), min(zs), max(zs))


def chay(doc, plan, doi_ten=None):
    x1, y1, x2, y2, z1, z2 = _khung(plan)
    tam = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    # luoi truc trong mau ve-revit keo dai 4000 mm ngoai truc bien
    kx1, ky1, kx2, ky2 = x1 - 4000 - LE, y1 - 4000 - LE, x2 + 4000 + LE, y2 + 4000 + LE
    tr = DB.Transaction(doc, "vn: can khung nhin 2D")
    tr.Start()
    try:
        plans = [v for v in collect(doc, DB.ViewPlan) if not v.IsTemplate and v.ViewType == DB.ViewType.FloorPlan
                 and v.GenLevel is not None]
        plans.sort(key=lambda v: abs(v.GenLevel.Elevation))
        v1 = plans[0]
        cs = []
        for m in collect(doc, DB.ElevationMarker):
            b = m.get_BoundingBox(v1)
            if b:
                cs.append(((b.Min.X + b.Max.X) / 2, (b.Min.Y + b.Max.Y) / 2))
        dich = (0, 0)
        if cs:
            cx = sum(c[0] for c in cs) / len(cs); cy = sum(c[1] for c in cs) / len(cs)
            dv = DB.XYZ(ft(tam[0]) - cx, ft(tam[1]) - cy, 0)
            if abs(mm(dv.X)) > DOI_TOI_THIEU or abs(mm(dv.Y)) > DOI_TOI_THIEU:
                ids = List[DB.ElementId]([m.Id for m in collect(doc, DB.ElevationMarker)])
                DB.ElementTransformUtils.MoveElements(doc, ids, dv)
                doc.Regenerate()
                dich = (round(mm(dv.X)), round(mm(dv.Y)))
        # mat dung: go scope box, khung theo khoi nha, bo gioi han xa
        hop = [(x, y, z) for x in (x1 - 3000, x2 + 3000) for y in (y1 - 3000, y2 + 3000)
               for z in (z1 - 1500, z2 + 1500)]
        n_md = 0
        for v in collect(doc, DB.ViewSection):
            if v.IsTemplate or v.ViewType != DB.ViewType.Elevation:
                continue
            sb = v.get_Parameter(DB.BuiltInParameter.VIEWER_VOLUME_OF_INTEREST_CROP)
            if sb and not sb.IsReadOnly:
                sb.Set(DB.ElementId.InvalidElementId)
            p = v.get_Parameter(DB.BuiltInParameter.VIEWER_BOUND_FAR_CLIPPING)
            if p and not p.IsReadOnly:
                p.Set(0)
            cb = v.CropBox
            inv = cb.Transform.Inverse
            pts = [inv.OfPoint(xyz(*q)) for q in hop]
            nb = DB.BoundingBoxXYZ()
            nb.Transform = cb.Transform
            nb.Min = DB.XYZ(min(q.X for q in pts), min(q.Y for q in pts), cb.Min.Z)
            nb.Max = DB.XYZ(max(q.X for q in pts), max(q.Y for q in pts), cb.Max.Z)
            v.CropBoxActive = True
            v.CropBox = nb
            v.CropBoxVisible = True
            n_md += 1
        # mat bang, mat bang tran, mat bang ket cau
        n_mb = 0
        for v in collect(doc, DB.ViewPlan):
            if v.IsTemplate or v.ViewType not in (DB.ViewType.FloorPlan, DB.ViewType.CeilingPlan,
                                                   DB.ViewType.EngineeringPlan):
                continue
            if v.Name == "Site":
                continue
            sb = v.get_Parameter(DB.BuiltInParameter.VIEWER_VOLUME_OF_INTEREST_CROP)
            if sb and not sb.IsReadOnly:
                sb.Set(DB.ElementId.InvalidElementId)
            bb = DB.BoundingBoxXYZ()
            bb.Min = xyz(kx1, ky1, 0)
            bb.Max = xyz(kx2, ky2, 0)
            v.CropBoxActive = True
            v.CropBox = bb
            v.CropBoxVisible = True
            if doi_ten and v.ViewType == DB.ViewType.FloorPlan and v.Name in doi_ten:
                v.Name = doi_ten[v.Name]
            n_mb += 1
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return {"dich_ky_hieu_mm": dich, "mat_dung": n_md, "mat_bang": n_mb,
            "khung_mb_mm": [kx1, ky1, kx2, ky2]}
