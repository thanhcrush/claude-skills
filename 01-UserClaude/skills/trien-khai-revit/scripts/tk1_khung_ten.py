# -*- coding: utf-8 -*-
# TRIEN KHAI 1: family khung ten (title block) theo kho giay trong hoso: vien giay, khung ve
# (le trai 20, cac canh 5), khung ten goc phai duoi voi cac o: cong ty, chu dau tu, cong trinh,
# hang muc, dia diem, ten ban ve, ky hieu, ti le, ngay. Chu co dinh ghi trong family; gia tri
# tung to ghi bang TextNote tren to (API khong tao duoc Label) - toa do o lay tu O_GIA_TRI().
# Can app (agent runtime cap san bien app). Family tao trong bo nho, nap thang vao du an
# (phien agent khong luu duoc .rfa; muon luu: Edit Family -> Save As).
from pyrevit.api import DB
from vn_revit import *
import os

TPL = r"C:\ProgramData\Autodesk\RVT 2025\Family Templates\English\Titleblocks\New Size metric.rft"


def hang(hs):
    """Cac hang khung ten (tu tren xuong): (khoa, nhan, cao mm)."""
    return [("cong_ty", None, 10), ("chu_dau_tu", u"Ch\u1ee7 \u0111\u1ea7u t\u01b0", 7),
            ("cong_trinh", u"C\u00f4ng tr\u00ecnh", 7), ("hang_muc", u"H\u1ea1ng m\u1ee5c", 7),
            ("dia_diem", u"\u0110\u1ecba \u0111i\u1ec3m", 7), ("ten_ban_ve", u"T\u00ean b\u1ea3n v\u1ebd", 10),
            ("cuoi", None, 8)]


def khung(hs):
    W, H = hs.KHO["rong"], hs.KHO["cao"]
    kw, kh = hs.KHUNG_TEN["rong"], hs.KHUNG_TEN["cao"]
    le = hs.KHO["le"]
    x1, x0 = W - le, W - le - kw
    return x0, x1, le, le + kh


def O_GIA_TRI(hs):
    """{khoa: (x, y_tren, kieu_chu)} toa do giay mm de ghi gia tri tung to."""
    x0, x1, y0, y1 = khung(hs)
    out = {}
    y = y1
    for k, nhan, h in hang(hs):
        top = y
        y -= h
        if k in ("chu_dau_tu", "cong_trinh", "hang_muc", "dia_diem"):
            out[k] = (x0 + 32, top - 1.6, "VN-Arial 2.5")
        elif k == "ten_ban_ve":
            out[k] = (x0 + 32, top - 2.6, "VN-Arial 3.5 dam")
        elif k == "cuoi":
            w3 = (x1 - x0) / 3.0
            out["ky_hieu"] = (x0 + 2, top - 3.4, "VN-Arial 3.5 dam")
            out["ti_le"] = (x0 + w3 + 2, top - 3.4, "VN-Arial 3.5")
            out["ngay"] = (x0 + 2 * w3 + 2, top - 3.4, "VN-Arial 3.5")
    return out


def _kieu_chu_family(fd):
    base = list(DB.FilteredElementCollector(fd).OfClass(DB.TextNoteType))[0]
    out = {}
    for name, size, bold in (("VN 2.0", 2.0, 0), ("VN 2.5", 2.5, 0), ("VN 3.5 dam", 3.5, 1)):
        t = base.Duplicate(name)
        t.get_Parameter(DB.BuiltInParameter.TEXT_FONT).Set("Arial")
        t.get_Parameter(DB.BuiltInParameter.TEXT_SIZE).Set(ft(size))
        t.get_Parameter(DB.BuiltInParameter.TEXT_STYLE_BOLD).Set(bold)
        t.get_Parameter(DB.BuiltInParameter.TEXT_WIDTH_SCALE).Set(1.0)
        t.get_Parameter(DB.BuiltInParameter.TEXT_BACKGROUND).Set(1)
        out[name] = t
    return out


def _tao_family(app, hs):
    fd = app.NewFamilyDocument(TPL)
    t = DB.Transaction(fd, "khung ten")
    t.Start()
    try:
        _ve(fd, hs)
        t.Commit()
    except Exception:
        t.RollBack()
        fd.Close(False)
        raise
    return fd


def _ve(fd, hs):
    v = [x for x in DB.FilteredElementCollector(fd).OfClass(DB.View) if not x.IsTemplate][0]
    # xoa khung A4 297x210 co san cua template: cac net bi kich thuoc rang buoc -> xoa kich thuoc truoc
    for d in list(DB.FilteredElementCollector(fd).OfClass(DB.Dimension)):
        try:
            fd.Delete(d.Id)
        except Exception:
            pass
    con = []
    for c in list(DB.FilteredElementCollector(fd).OfClass(DB.CurveElement)):
        try:
            fd.Delete(c.Id)
        except Exception:
            con.append(c)
    # 4 net he thong cua template khong xoa duoc: doi thanh mep giay
    W0, H0 = hs.KHO["rong"], hs.KHO["cao"]
    canh = [((0, 0), (W0, 0)), ((W0, 0), (W0, H0)), ((W0, H0), (0, H0)), ((0, H0), (0, 0))]
    for c, (a, b) in zip(con, canh):
        try:
            c.SetGeometryCurve(DB.Line.CreateBound(DB.XYZ(ft(a[0]), ft(a[1]), 0), DB.XYZ(ft(b[0]), ft(b[1]), 0)), True)
        except Exception:
            pass
    cat = fd.OwnerFamily.FamilyCategory
    sub = dict((s.Name, s.GetGraphicsStyle(DB.GraphicsStyleType.Projection)) for s in cat.SubCategories)
    day, mong = sub.get("Wide Lines"), sub.get("Fine Lines") or sub.get("Medium Lines")

    def ln(a, b, gs):
        c = fd.FamilyCreate.NewDetailCurve(v, DB.Line.CreateBound(DB.XYZ(ft(a[0]), ft(a[1]), 0), DB.XYZ(ft(b[0]), ft(b[1]), 0)))
        if gs is not None:
            c.LineStyle = gs

    def rect(xa, ya, xb, yb, gs):
        ln((xa, ya), (xb, ya), gs); ln((xb, ya), (xb, yb), gs); ln((xb, yb), (xa, yb), gs); ln((xa, yb), (xa, ya), gs)

    W, H = hs.KHO["rong"], hs.KHO["cao"]
    le, lt = hs.KHO["le"], hs.KHO["le_trai"]
    rect(0, 0, W, H, mong)                       # mep giay
    rect(lt, le, W - le, H - le, day)            # khung ve
    x0, x1, y0, y1 = khung(hs)
    rect(x0, y0, x1, y1, day)
    tts = _kieu_chu_family(fd)
    y = y1
    for k, nhan, h in hang(hs):
        top = y
        y -= h
        if y > y0 + 0.01:
            ln((x0, y), (x1, y), mong)
        if k == "cong_ty":
            DB.TextNote.Create(fd, v.Id, DB.XYZ(ft(x0 + 3), ft(top - 2.8), 0), hs.THONG_TIN["cong_ty"], tts["VN 3.5 dam"].Id)
        elif k == "cuoi":
            w3 = (x1 - x0) / 3.0
            ln((x0 + w3, y), (x0 + w3, top), mong)
            ln((x0 + 2 * w3, y), (x0 + 2 * w3, top), mong)
            for i, s in enumerate((u"K\u00fd hi\u1ec7u", u"T\u1ec9 l\u1ec7", u"Ng\u00e0y")):
                DB.TextNote.Create(fd, v.Id, DB.XYZ(ft(x0 + i * w3 + 1), ft(top - 0.6), 0), s, tts["VN 2.0"].Id)
        else:
            ln((x0 + 30, y), (x0 + 30, top), mong)
            DB.TextNote.Create(fd, v.Id, DB.XYZ(ft(x0 + 1.5), ft(top - 1.6), 0), nhan, tts["VN 2.5"].Id)


def chay(doc, app, hs, ghi_de=False):
    f = None
    for x in collect(doc, DB.Family):
        if x.Name == hs.TEN_FAMILY_KHUNG:
            f = x
    if f is not None and not ghi_de:
        return {"khung_ten": "da co", "family": f.Name}
    if f is not None:
        # family tao trong bo nho mang ten "FamilyN" nen nap de khong an: xoa family cu do skill
        # tao (cac to dung no se duoc tk4 tao lai)
        t0 = DB.Transaction(doc, "vn: xoa khung ten cu")
        t0.Start()
        doc.Delete(f.Id)
        t0.Commit()
    fd = _tao_family(app, hs)
    try:
        fam = fd.LoadFamily(doc)
    finally:
        fd.Close(False)
    tr = DB.Transaction(doc, "vn: trien khai 1 - ten khung ten")
    tr.Start()
    try:
        fam.Name = hs.TEN_FAMILY_KHUNG
        sid = list(fam.GetFamilySymbolIds())[0]
        sym = doc.GetElement(sid)
        sym.Name = hs.KHO["ten"]
        if not sym.IsActive:
            sym.Activate()
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return {"khung_ten": "tao moi", "family": fam.Name}
