# -*- coding: utf-8 -*-
# TRIEN KHAI 0: chuan ho so - thong tin du an, kieu chu, kieu dim, ky hieu loai cua, luoi truc,
# ti le, ten tren to, khung cat mat bang, mat bang mai, mat cat, view 3D.
# Dung: import tk0_chuan, hoso_xxx as hs; result = tk0_chuan.chay(doc, hs)
from pyrevit.api import DB
from vn_revit import *

KIEU_CHU = [("VN-Arial 2.5", 2.5, False), ("VN-Arial 3.5", 3.5, False), ("VN-Arial 3.5 dam", 3.5, True),
            ("VN-Arial 5 dam", 5.0, True), ("VN-Arial 2.0", 2.0, False)]
KIEU_DIM = "VN-Dim 2.5 gach xien"


def _chu(doc):
    base = collect(doc, DB.TextNoteType, types=True)[0]
    out = {}
    for name, size, bold in KIEU_CHU:
        t = tim_loai(doc, DB.TextNoteType, name) or base.Duplicate(name)
        t.get_Parameter(DB.BuiltInParameter.TEXT_FONT).Set("Arial")
        t.get_Parameter(DB.BuiltInParameter.TEXT_SIZE).Set(ft(size))
        t.get_Parameter(DB.BuiltInParameter.TEXT_STYLE_BOLD).Set(1 if bold else 0)
        t.get_Parameter(DB.BuiltInParameter.TEXT_WIDTH_SCALE).Set(1.0)
        t.get_Parameter(DB.BuiltInParameter.TEXT_BACKGROUND).Set(1)   # trong suot
        p = t.get_Parameter(DB.BuiltInParameter.TEXT_BOX_VISIBILITY)
        if p and not p.IsReadOnly:
            p.Set(0)                                                     # khong ve khung quanh chu
        out[name] = t
    return out


def _dim(doc):
    t = tim_loai(doc, DB.DimensionType, KIEU_DIM)
    if t is None:
        goc = [d for d in collect(doc, DB.DimensionType, types=True)
               if d.StyleType == DB.DimensionStyleType.Linear and ten(d).startswith("Linear")][0]
        t = goc.Duplicate(KIEU_DIM)
    t.get_Parameter(DB.BuiltInParameter.TEXT_FONT).Set("Arial")
    t.get_Parameter(DB.BuiltInParameter.TEXT_SIZE).Set(ft(2.5))
    t.get_Parameter(DB.BuiltInParameter.TEXT_WIDTH_SCALE).Set(1.0)
    # kieu dim cua template co don vi rieng (feet-inch): ep ve mm, khong so le
    fo = DB.FormatOptions(DB.UnitTypeId.Millimeters)
    fo.Accuracy = 1.0
    try:
        t.SetUnitsFormatOptions(fo)
    except Exception:
        pass
    tick = None
    for e in DB.FilteredElementCollector(doc).OfClass(DB.ElementType):
        try:
            if e.FamilyName == "Arrowhead" and ten(e) == 'Diagonal 1/8"':
                tick = e
        except Exception:
            pass
    if tick is not None:
        t.get_Parameter(DB.BuiltInParameter.DIM_LEADER_ARROWHEAD).Set(tick.Id)
    return t


def _ky_hieu_loai(doc):
    n = 0
    for s in collect(doc, DB.FamilySymbol, types=True):
        nm = ten(s)
        if nm.startswith("VN-") and s.Category and s.Category.Id.IntegerValue in (
                int(DB.BuiltInCategory.OST_Doors), int(DB.BuiltInCategory.OST_Windows)):
            kh = nm[3:].split(" ")[0]
            s.get_Parameter(DB.BuiltInParameter.ALL_MODEL_TYPE_MARK).Set(kh)
            n += 1
    return n


def _view(doc, name):
    for v in collect(doc, DB.View):
        if not v.IsTemplate and v.Name == name:
            return v
    return None


def _keo_truc(doc, hs, v):
    n = 0
    so, chu = hs.TRUC_KEO["so"], hs.TRUC_KEO["chu"]
    loi = []
    for g in collect(doc, DB.Grid):
        cs = g.GetCurvesInView(DB.DatumExtentType.Model, v)
        c = cs[0] if cs and cs.Count else g.Curve
        p0, p1 = c.GetEndPoint(0), c.GetEndPoint(1)
        if abs(p0.X - p1.X) < 1e-6:     # truc so (doc theo y)
            new = DB.Line.CreateBound(DB.XYZ(p0.X, ft(so[0]), p0.Z), DB.XYZ(p0.X, ft(so[1]), p0.Z))
        else:
            new = DB.Line.CreateBound(DB.XYZ(ft(chu[0]), p0.Y, p0.Z), DB.XYZ(ft(chu[1]), p0.Y, p0.Z))
        try:
            g.SetCurveInView(DB.DatumExtentType.Model, v, new)
            n += 1
        except Exception as ex:
            loi.append(str(ex)[:120])
    return n if not loi else (n, loi[:2])


def _mat_cat(doc, hs):
    vft = [t for t in collect(doc, DB.ViewFamilyType, types=True) if t.ViewFamily == DB.ViewFamily.Section
           and ten(t) == "Building Section"][0]
    out = []
    for mc in hs.MAT_CAT:
        old = _view(doc, mc["ten"])
        if old is not None:
            doc.Delete(old.Id)
        # CreateSection: Revit dat mat cat o Min.Z va nhin theo +BasisZ, roi tu lat truc.
        # Muon cat tai x, nhin ve -x (truc A ben trai, E ben phai nhu ban goc):
        t = DB.Transform.Identity
        t.Origin = xyz(mc["x"], 0, 0)
        t.BasisX = DB.XYZ(0, -1, 0)
        t.BasisY = DB.XYZ.BasisZ
        t.BasisZ = DB.XYZ(-1, 0, 0)
        bb = DB.BoundingBoxXYZ()
        bb.Transform = t
        bb.Min = DB.XYZ(-ft(mc["y"][1]), ft(mc["z"][0]), 0)
        bb.Max = DB.XYZ(-ft(mc["y"][0]), ft(mc["z"][1]), ft(mc["sau"]))
        v = DB.ViewSection.CreateSection(doc, vft.Id, bb)
        v.Name = mc["ten"]
        v.Scale = hs.TI_LE
        out.append(v)
    return out


def _crop_chu_thich(v, le_giay_mm=5):
    """Bat khung chu thich, le 5 mm giay (template de 25,4 mm); an chu thich chung cua template
    (mui ten Bac, thuoc ti le nam ngoai khung)."""
    p = v.get_Parameter(DB.BuiltInParameter.VIEWER_ANNOTATION_CROP_ACTIVE)
    if p and not p.IsReadOnly:
        p.Set(1)
    try:
        m = v.GetCropRegionShapeManager()
        d = ft(le_giay_mm * v.Scale)
        m.LeftAnnotationCropOffset = d
        m.RightAnnotationCropOffset = d
        m.TopAnnotationCropOffset = d
        m.BottomAnnotationCropOffset = d
    except Exception:
        pass
    try:
        v.SetCategoryHidden(DB.ElementId(DB.BuiltInCategory.OST_GenericAnnotation), True)
    except Exception:
        pass


def _gon_datum(doc, v, le_mm=1500):
    """Mat dung, mat cat: keo duong cao do (ngang) va truc (dung) vao trong khung cat, bong truc o duoi,
    bong cao do ben phai."""
    cb = v.CropBox
    T = cb.Transform
    p_trai = T.OfPoint(DB.XYZ(cb.Min.X + ft(le_mm), 0, 0))
    p_phai = T.OfPoint(DB.XYZ(cb.Max.X - ft(le_mm), 0, 0))
    z_duoi = T.OfPoint(DB.XYZ(0, cb.Min.Y + ft(800), 0)).Z
    z_tren = T.OfPoint(DB.XYZ(0, cb.Max.Y - ft(300), 0)).Z
    n = 0
    for e in list(collect(doc, DB.Level)) + list(collect(doc, DB.Grid)):
        try:
            cs = e.GetCurvesInView(DB.DatumExtentType.ViewSpecific, v)
            if not cs or cs.Count == 0:
                continue
            c = cs[0]
            a, b = c.GetEndPoint(0), c.GetEndPoint(1)
            for end in (DB.DatumEnds.End0, DB.DatumEnds.End1):
                e.SetDatumExtentType(end, v, DB.DatumExtentType.ViewSpecific)
            if isinstance(e, DB.Level):
                d = (b - a).Normalize()
                s1, s2 = d.DotProduct(p_trai - a), d.DotProduct(p_phai - a)
                na, nb = a + d * min(s1, s2), a + d * max(s1, s2)
                e.SetCurveInView(DB.DatumExtentType.ViewSpecific, v, DB.Line.CreateBound(na, nb))
                # bong ben phai
                ends = (DB.DatumEnds.End0, DB.DatumEnds.End1) if s2 > s1 else (DB.DatumEnds.End1, DB.DatumEnds.End0)
                e.HideBubbleInView(ends[0], v); e.ShowBubbleInView(ends[1], v)
            else:
                na, nb = DB.XYZ(a.X, a.Y, z_duoi), DB.XYZ(a.X, a.Y, z_tren)
                e.SetCurveInView(DB.DatumExtentType.ViewSpecific, v, DB.Line.CreateBound(na, nb))
                e.ShowBubbleInView(DB.DatumEnds.End0, v); e.HideBubbleInView(DB.DatumEnds.End1, v)
            n += 1
        except Exception:
            pass
    return n


def _khung_3d(v3, hop):
    """Cat khung view 3D vua khoi nha (hop = [(x,y,z)] mm)."""
    cb = v3.CropBox
    inv = cb.Transform.Inverse
    pts = [inv.OfPoint(xyz(*p)) for p in hop]
    nb = DB.BoundingBoxXYZ()
    nb.Transform = cb.Transform
    m = ft(1500)
    nb.Min = DB.XYZ(min(p.X for p in pts) - m, min(p.Y for p in pts) - m, cb.Min.Z)
    nb.Max = DB.XYZ(max(p.X for p in pts) + m, max(p.Y for p in pts) + m, cb.Max.Z)
    v3.CropBoxActive = True
    v3.CropBox = nb
    v3.CropBoxVisible = False


def chay(doc, hs):
    out = {}
    tr = DB.Transaction(doc, "vn: trien khai 0 - chuan ho so")
    tr.Start()
    try:
        pi = doc.ProjectInformation
        ti = hs.THONG_TIN
        pi.Name = ti["cong_trinh"]
        pi.get_Parameter(DB.BuiltInParameter.CLIENT_NAME).Set(ti["chu_dau_tu"])
        pi.Address = ti["dia_diem"]
        pi.BuildingName = ti["hang_muc"]
        pi.OrganizationName = ti["cong_ty"]
        pi.IssueDate = ti["ngay"]
        out["kieu_chu"] = len(_chu(doc))
        _dim(doc)
        out["ky_hieu_loai"] = _ky_hieu_loai(doc)
        v1 = _view(doc, hs.MB_GHI_CHU[0])
        out["truc_keo"] = _keo_truc(doc, hs, v1)
        # mat cat
        out["mat_cat"] = [v.Id.IntegerValue for v in _mat_cat(doc, hs)]
        # view 3D phoi canh
        for t in hs.TO:
            if t.get("3d"):
                old = _view(doc, t["3d"])
                if old is not None:
                    doc.Delete(old.Id)
                vft3 = [x for x in collect(doc, DB.ViewFamilyType, types=True) if x.ViewFamily == DB.ViewFamily.ThreeDimensional][0]
                v3 = DB.View3D.CreateIsometric(doc, vft3.Id)
                v3.Name = t["3d"]
                v3.SetOrientation(DB.ViewOrientation3D(DB.XYZ(-1, -1, 1), DB.XYZ(1, 1, 2).Normalize(),
                                                       DB.XYZ(1, 1, -1).Normalize()))
                v3.Scale = hs.TI_LE_3D
                v3.get_Parameter(DB.BuiltInParameter.VIEW_DETAIL_LEVEL).Set(2)
                try:
                    v3.DisplayStyle = DB.DisplayStyle.ShadingWithEdges
                except Exception:
                    pass
                for cat in (DB.BuiltInCategory.OST_Grids, DB.BuiltInCategory.OST_Levels,
                            DB.BuiltInCategory.OST_CLines, DB.BuiltInCategory.OST_SectionBox):
                    try:
                        v3.SetCategoryHidden(DB.ElementId(cat), True)   # an truc, cao do, mat tham chieu
                    except Exception:
                        pass
                doc.Regenerate()
                _khung_3d(v3, hs.HOP_NHA)
        # ti le, ten tren to, khung cat mat bang
        kx1, ky1, kx2, ky2 = hs.KHUNG_MB
        n = 0
        for name, title in hs.TIEU_DE.items():
            v = _view(doc, name)
            if v is None:
                continue
            v.Scale = hs.TI_LE
            v.get_Parameter(DB.BuiltInParameter.VIEW_DESCRIPTION).Set(title)
            v.get_Parameter(DB.BuiltInParameter.VIEW_DETAIL_LEVEL).Set(2)
            if isinstance(v, DB.ViewPlan):
                bb = DB.BoundingBoxXYZ()
                bb.Min = xyz(kx1, ky1, 0); bb.Max = xyz(kx2, ky2, 0)
                v.CropBoxActive = True
                v.CropBox = bb
                v.CropBoxVisible = False
            else:
                v.CropBoxVisible = False
            _crop_chu_thich(v)
            n += 1
        doc.Regenerate()
        nd = 0
        for mc in hs.MAT_CAT:
            v = _view(doc, mc["ten"])
            v.get_Parameter(DB.BuiltInParameter.VIEW_DESCRIPTION).Set(mc["ten"])
            v.CropBoxVisible = False
            _crop_chu_thich(v)
        doc.Regenerate()
        for v in collect(doc, DB.ViewSection):
            if not v.IsTemplate and (v.Name in hs.TIEU_DE or v.Name in [m["ten"] for m in hs.MAT_CAT]):
                nd += _gon_datum(doc, v)
        out["view_chuan"] = n
        out["datum_gon"] = nd
        # mat bang mai: nhin xuong toi tang ap mai
        vm = _view(doc, hs.MB_MAI["view"])
        lv_day = [l for l in collect(doc, DB.Level) if l.Name == hs.MB_MAI["day_toi_tang"]][0]
        vr = vm.GetViewRange()
        vr.SetLevelId(DB.PlanViewPlane.BottomClipPlane, lv_day.Id)
        vr.SetOffset(DB.PlanViewPlane.BottomClipPlane, 0.0)
        vr.SetLevelId(DB.PlanViewPlane.ViewDepthPlane, lv_day.Id)
        vr.SetOffset(DB.PlanViewPlane.ViewDepthPlane, 0.0)
        vr.SetOffset(DB.PlanViewPlane.CutPlane, ft(1200))
        vr.SetOffset(DB.PlanViewPlane.TopClipPlane, ft(2000))
        vm.SetViewRange(vr)
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return ascii_safe(out)
