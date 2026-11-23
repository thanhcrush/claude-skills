# -*- coding: utf-8 -*-
# CHANG 8: hoan thien mai + dau hoi WC theo ban ve goc (mat dung truc 1-17, 17-1, MB mai, MB ap mai).
#  - Mai: thay mai 2 mai don gian (chang 6) bang mai 3 mat: mai sau day du, mai truoc cat cheo
#    (duong cheo MB mai: (-710,9650)->(8400,4290) va (55260,9650)->(46450,4290)), 2 mat tam giac
#    o dau nha doc doc nha (mep truoc dang tu +11.111 len +14.800 o dau hoi).
#  - Tuong thu hoi truc 1, 15 va tuong ap mai truc B vat theo mat mai tam giac (MD truc 1-17:
#    tuong vat tu truc 1 toi truc 2, tu truc 14 toi truc 15).
#  - Hanh lang ra WC (truc 15-16): mai bang +10.800, tuong chan mai 220 cao 300 (dinh +11.100),
#    ha cot truc 16 o ap mai xuong 300; lan can tang 1; lam dung truoc bay 14-15 (+3.200 -> +10.300).
# Mat mai tinh theo mat duoi mai (mep dua mai +11.111, tuong truc B/E +11.600, dinh +14.800).
from pyrevit.api import DB
from pyrevit.revit.db.create import create_footprint_roof
from vn_revit import *
from vn_don_vi import diem
import cuaviet_3tang as plan
from System.Collections.Generic import List

TAG = NHAN + "hoanthien"
AM_Z = 10800.0
DOC = 3200.0 / 4650.0                         # mai truoc, mai sau
Z_DUA = AM_Z + 311                            # mep dua mai (mat duoi)
Z_DINH = 14800.0
X0, X1, Y0, Y1, YR = -710, 55260, 4290, 15010, 9650
XD_TRAI, XD_PHAI = 8400, 46450                # chan duong cheo o mep dua truoc
DOC_TRAI = (Z_DINH - Z_DUA) / (XD_TRAI - X0)  # mat tam giac trai (doc theo x)
DOC_PHAI = (Z_DINH - Z_DUA) / (X1 - XD_PHAI)


def z_tg_trai(x):
    return Z_DINH - (x - X0) * DOC_TRAI


def z_tg_phai(x):
    return Z_DINH - (X1 - x) * DOC_PHAI


def tuong_profile(doc, wt, lv, pts, normal):
    """pts: [(x, y, z)] mm theo thu tu vong kin, tren mat phang dung."""
    cs = List[DB.Curve]()
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        cs.Add(DB.Line.CreateBound(xyz(*a), xyz(*b)))
    return DB.Wall.Create(doc, cs, wt.Id, lv.Id, False, normal)


def mai_tam_giac(doc, rt, lv, view, ten_mp, x_cao, x_thap):
    """Mai dun (extrusion) doc theo x: cao Z_DINH o x_cao, thap Z_DUA o x_thap, keo theo y tu Y0 toi YR."""
    for rp in collect(doc, DB.ReferencePlane):
        if rp.Name == ten_mp:
            doc.Delete(rp.Id)
    rp = doc.Create.NewReferencePlane(xyz(min(x_cao, x_thap) - 1000, Y0, 0), xyz(max(x_cao, x_thap) + 1000, Y0, 0),
                                      DB.XYZ(0, 0, 1), view)
    rp.Name = ten_mp
    prof = DB.CurveArray()
    # duong bien dang cua mai dun la MAT TREN: nang 110 de mat duoi trung mat z_tg (dinh tuong)
    prof.Append(DB.Line.CreateBound(xyz(x_cao, Y0, Z_DINH + 110), xyz(x_thap, Y0, Z_DUA + 110)))
    n = rp.Normal
    dai = ft(YR - Y0)
    # keo ve phia +y
    s, e = (0.0, dai) if n.Y > 0 else (-dai, 0.0)
    r = doc.Create.NewExtrusionRoof(prof, rp, lv, rt, s, e)
    return r


def chay(doc, file_dich="Project1"):
    if doc.Title != file_dich:
        raise Exception("File dang mo khong phai %s" % file_dich)
    lv = levels(doc, plan)
    am = lv["AM"]
    t1 = lv["T1"]
    rt = tim_loai(doc, DB.RoofType, "VN-Mai ngoi")
    wt = tim_loai(doc, DB.WallType, "VN-Tuong gach 220")
    ft_san = tim_loai(doc, DB.FloorType, "VN-San BTCT 120")
    rl = tim_loai(doc, DB.Architecture.RailingType, "VN-Lan can 1100")
    v_am = [v for v in collect(doc, DB.ViewPlan) if not v.IsTemplate and v.GenLevel is not None
            and v.GenLevel.Id == am.Id and v.ViewType == DB.ViewType.FloorPlan][0]
    out = {}
    tr = DB.Transaction(doc, "vn: chang 8 - hoan thien mai, dau hoi WC")
    tr.Start()
    try:
        xoa = xoa_theo_nhan(doc, TAG) + xoa_theo_nhan(doc, NHAN + "mai")
        xoa += xoa_theo_nhan(doc, NHAN + "tuong:AM-B1") + xoa_theo_nhan(doc, NHAN + "tuong:AM-B2")
        out["xoa_cu"] = xoa
        # 1. mai chinh 6 canh: mai sau day du + mai truoc cat cheo
        pts = [(X0, Y1), (X1, Y1), (X1, YR), (XD_PHAI, Y0), (XD_TRAI, Y0), (X0, YR)]
        roof, curves = create_footprint_roof([diem(*p) for p in pts], rt, level=am,
                                             slopes={0: DOC, 3: DOC}, offset=ft(Z_DUA - AM_Z), doc=doc)
        comments(roof, TAG + ":mai-chinh")
        # 2. hai mat tam giac dau nha
        r1 = mai_tam_giac(doc, rt, am, v_am, "vn-mai-tg-trai", X0, XD_TRAI)
        comments(r1, TAG + ":mai-tg-trai")
        r2 = mai_tam_giac(doc, rt, am, v_am, "vn-mai-tg-phai", X1, XD_PHAI)
        comments(r2, TAG + ":mai-tg-phai")
        # 3. tuong thu hoi truc 1 (x=0) va truc 15 (x=54550)
        for x, ztg, name in ((0, z_tg_trai(0), "thu-hoi-1"), (54550, z_tg_phai(54550), "thu-hoi-15")):
            yd = YR - abs(x - (X0 if x < 20000 else X1)) / float(XD_TRAI - X0 if x < 20000 else X1 - XD_PHAI) * (YR - Y0)
            w = tuong_profile(doc, wt, am, [(x, 5000, AM_Z), (x, 14300, AM_Z), (x, 14300, 11600),
                                             (x, YR, Z_DINH), (x, yd, ztg), (x, 5000, ztg)], DB.XYZ(1, 0, 0))
            comments(w, "%s:%s" % (TAG, name))
        # 4. tuong ap mai truc B vat o 2 dau
        w = tuong_profile(doc, wt, am, [(0, 5000, AM_Z), (14840, 5000, AM_Z), (14840, 5000, 11600),
                                         (4200, 5000, 11600), (4200, 5000, z_tg_trai(4200)),
                                         (0, 5000, z_tg_trai(0))], DB.XYZ(0, 1, 0))
        comments(w, TAG + ":AM-B1-vat")
        w = tuong_profile(doc, wt, am, [(22960, 5000, AM_Z), (54550, 5000, AM_Z), (54550, 5000, z_tg_phai(54550)),
                                         (50050, 5000, z_tg_phai(50050)), (50050, 5000, 11600),
                                         (22960, 5000, 11600)], DB.XYZ(0, 1, 0))
        comments(w, TAG + ":AM-B2-vat")
        # 5. hanh lang WC truc 15-16: mai bang + tuong chan mai cao 300
        loops = List[DB.CurveLoop]()
        loops.Add(curve_loop([(54660, 4780), (56460, 4780), (56460, 14410), (54660, 14410)]))
        f = DB.Floor.Create(doc, loops, ft_san.Id, am.Id)
        comments(f, TAG + ":mai-bang-HL-WC")
        for a, b, name in (((54550, 5000), (56350, 5000), "chan-mai-B"), ((56350, 5000), (56350, 14300), "chan-mai-16"),
                           ((56350, 14300), (54550, 14300), "chan-mai-E")):
            w = DB.Wall.Create(doc, line(a, b), wt.Id, am.Id, ft(300), 0.0, False, False)
            comments(w, "%s:%s" % (TAG, name))
        # ha cot truc 16 o tang ap mai xuong 300
        n_cot = 0
        for c in collect(doc, DB.FamilyInstance, DB.BuiltInCategory.OST_StructuralColumns):
            s = c.get_Parameter(DB.BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString() or ""
            if s.startswith(NHAN + "cot:cot:C-AM-56350-"):
                c.get_Parameter(DB.BuiltInParameter.FAMILY_TOP_LEVEL_OFFSET_PARAM).Set(ft(300))
                n_cot += 1
        out["cot_truc16_ha"] = n_cot
        # 6. lan can tang 1 (MD truc 1-17: co lan can tang 1, tru loi bac cap sanh va bay 13-14)
        for duong in ([(-110, 4945), (14790, 4945)], [(23010, 4945), (46050, 4945)],
                      [(50450, 4945), (56350, 4945), (56350, 14300), (54660, 14300)]):
            loop = DB.CurveLoop()
            for i in range(len(duong) - 1):
                loop.Append(line(duong[i], duong[i + 1]))
            r = DB.Architecture.Railing.Create(doc, loop, rl.Id, t1.Id)
            comments(r, TAG + ":lan-can-T1")
        # 7. lam dung truoc bay 14-15
        lam = nhan_ban(doc, DB.WallType, "VN-Vach kinh", "VN-Lam dung")
        try:
            lam.get_Parameter(DB.BuiltInParameter.SPACING_LAYOUT_HORIZ).Set(0)
            lam.get_Parameter(DB.BuiltInParameter.SPACING_LAYOUT_VERT).Set(1)
            lam.get_Parameter(DB.BuiltInParameter.SPACING_LENGTH_VERT).Set(ft(150))
            pnl = [p for p in collect(doc, DB.PanelType, types=True) if "Empty" in ten(p)]
            if pnl:
                lam.get_Parameter(DB.BuiltInParameter.AUTO_PANEL_WALL).Set(pnl[0].Id)
            mul = [m for m in collect(doc, DB.MullionType, types=True) if "ectangular" in (getattr(m, "FamilyName", "") or "")]
            if mul:
                lam.get_Parameter(DB.BuiltInParameter.AUTO_MULLION_INTERIOR_VERT).Set(mul[0].Id)
                out["mullion"] = ten(mul[0])
        except Exception as ex:
            out["lam_loi"] = str(ex)[:150]
        w = DB.Wall.Create(doc, line((50450, 4700), (54150, 4700)), lam.Id, t1.Id, ft(7100), ft(3200), False, False)
        comments(w, TAG + ":lam-14-15")
        doc.Regenerate()
        bb = lambda e: [round(mm(e.get_BoundingBox(None).Min.Z)), round(mm(e.get_BoundingBox(None).Max.Z)),
                        round(mm(e.get_BoundingBox(None).Min.X)), round(mm(e.get_BoundingBox(None).Max.X)),
                        round(mm(e.get_BoundingBox(None).Min.Y)), round(mm(e.get_BoundingBox(None).Max.Y))]
        out["mai_chinh_bb"] = bb(roof)
        out["tg_trai_bb"] = bb(r1)
        out["tg_phai_bb"] = bb(r2)
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return out
