# -*- coding: utf-8 -*-
# TRIEN KHAI 4: tao to ban ve theo hs.TO - dat khung ten, viewport dung ti le (canh tren, tranh khung
# ten), bang thong ke, ghi gia tri khung ten tung to, tao bo to de in PDF.
# Chay lai duoc: xoa cac to co so hieu trong hs.TO roi tao lai.
from pyrevit.api import DB
from vn_revit import *
import tk1_khung_ten as kt


def _view(doc, name):
    for v in collect(doc, DB.View):
        if not v.IsTemplate and v.Name == name and not isinstance(v, DB.ViewSheet):
            return v
    return None


def _outline(vp):
    """Khung cat cua view chieu len to (toa do to). View 3D / khong co khung: dung box outline."""
    doc = vp.Document
    v = doc.GetElement(vp.ViewId)
    try:
        if isinstance(v, DB.View3D) or not v.CropBoxActive:
            raise Exception("dung outline")
        # Do thuc te (Revit 2025): to = P.Origin + toa do cuc bo cua khung cat / ti le
        cb = v.CropBox
        P = vp.GetProjectionToSheetTransform()
        s = float(v.Scale)
        pts = [P.OfPoint(DB.XYZ(x / s, y / s, 0)) for x in (cb.Min.X, cb.Max.X) for y in (cb.Min.Y, cb.Max.Y)]
        return (DB.XYZ(min(p.X for p in pts), min(p.Y for p in pts), 0),
                DB.XYZ(max(p.X for p in pts), max(p.Y for p in pts), 0))
    except Exception:
        o = vp.GetBoxOutline()
        return o.MinimumPoint, o.MaximumPoint


def _dat(doc, vps, hs):
    """Xep cac viewport tren mot to: canh tren, nam ngang, giua kho; tranh khung ten."""
    W = hs.KHO["rong"]
    lt, le = hs.KHO["le_trai"], hs.KHO["le"]
    x0k, x1k, y0k, y1k = kt.khung(hs)
    gap = ft(20)
    sizes = []
    for vp in vps:
        mn, mx = _outline(vp)
        sizes.append((mx.X - mn.X, mx.Y - mn.Y))
    tong = sum(s[0] for s in sizes) + gap * (len(sizes) - 1)
    trai = max(ft(lt + 5), ft((lt + W - le) / 2.0) - tong / 2)
    tren = ft(hs.KHO["cao"] - le - 12)      # chua 5 mm le chu thich + bong truc phia tren
    canh = []
    for vp, (w, h) in zip(vps, sizes):
        mn, mx = _outline(vp)
        tam_moi = DB.XYZ(trai + w / 2, tren - h / 2, 0)
        tam_cu = DB.XYZ((mn.X + mx.X) / 2, (mn.Y + mx.Y) / 2, 0)
        DB.ElementTransformUtils.MoveElement(doc, vp.Id, tam_moi - tam_cu)
        day = tren - h
        if trai + w > ft(x0k) and day < ft(y1k + 3):
            canh.append("chong khung ten")
        if trai + w > ft(W - le):
            canh.append("tran le phai")
        trai += w + gap
    return [round(mm(s[0])) for s in sizes], [round(mm(s[1])) for s in sizes], canh


def _ghi(doc, sheet, hs, so, ten_to, ti_le, tts):
    o = kt.O_GIA_TRI(hs)
    gt = dict(hs.THONG_TIN)
    gt.update({"ten_ban_ve": ten_to, "ky_hieu": so, "ti_le": ti_le})
    for k, (x, y, kieu) in o.items():
        if k in gt:
            DB.TextNote.Create(doc, sheet.Id, DB.XYZ(ft(x), ft(y), 0), gt[k], tts[kieu].Id)


def chay(doc, hs):
    tb = None
    for s in collect(doc, DB.FamilySymbol, DB.BuiltInCategory.OST_TitleBlocks, types=True):
        if s.FamilyName == hs.TEN_FAMILY_KHUNG:
            tb = s
    if tb is None:
        raise Exception("Chua co khung ten %s - chay tk1_khung_ten truoc" % hs.TEN_FAMILY_KHUNG)
    tts = dict((ten(t), t) for t in collect(doc, DB.TextNoteType, types=True) if ten(t).startswith("VN-"))
    vpt = [t for t in collect(doc, DB.ElementType, types=True) if getattr(t, "FamilyName", "") == "Viewport" and ten(t) == "Title w Line"]
    so_list = [t["so"] for t in hs.TO]
    out = {"to": []}
    tr = DB.Transaction(doc, "vn: trien khai 4 - to ban ve")
    tr.Start()
    try:
        for s in collect(doc, DB.ViewSheet):
            if s.SheetNumber in so_list:
                doc.Delete(s.Id)
        doc.Regenerate()
        sheets = []
        for t in hs.TO:
            sh = DB.ViewSheet.Create(doc, tb.Id)
            sh.SheetNumber = t["so"]
            sh.Name = t["ten"]
            sheets.append(sh)
            ghi = {"so": t["so"]}
            tam = DB.XYZ(ft(400), ft(150), 0)
            if t.get("bang"):
                x = 30
                for sch in collect(doc, DB.ViewSchedule):
                    if sch.Name.startswith(u"BẢNG THỐNG KÊ"):
                        DB.ScheduleSheetInstance.Create(doc, sh.Id, sch.Id, DB.XYZ(ft(x), ft(285), 0))
                        x += 200
                ti_le = "-"
            else:
                names = t.get("view") or [t.get("3d")]
                vps = []
                for n in names:
                    v = _view(doc, n)
                    if v is None:
                        ghi.setdefault("thieu_view", []).append(n.encode("unicode_escape"))
                        continue
                    if not DB.Viewport.CanAddViewToSheet(doc, sh.Id, v.Id):
                        # view dang nam tren to mau cua template (A101, A201...): go viewport cu, giu to
                        for ovp in collect(doc, DB.Viewport):
                            if ovp.ViewId == v.Id:
                                osh = doc.GetElement(ovp.SheetId)
                                out.setdefault("go_khoi_to_mau", []).append(osh.SheetNumber)
                                doc.Delete(ovp.Id)
                    vp = DB.Viewport.Create(doc, sh.Id, v.Id, tam)
                    if vpt:
                        vp.ChangeTypeId(vpt[0].Id)
                    vps.append(vp)
                doc.Regenerate()
                if vps:
                    ghi["rong"], ghi["cao"], ghi["canh_bao"] = _dat(doc, vps, hs)
                ti_le = "1:%d" % (hs.TI_LE_3D if t.get("3d") else hs.TI_LE)
            _ghi(doc, sh, hs, t["so"], t["ten"], ti_le, tts)
            out["to"].append(ghi)
        # bo to de in PDF
        try:
            pm = doc.PrintManager
            pm.PrintRange = DB.PrintRange.Select
            vss = pm.ViewSheetSetting
            vs = DB.ViewSet()
            for sh in sheets:
                vs.Insert(sh)
            for old in collect(doc, DB.ViewSheetSet):
                if old.Name == hs.BO_TO:
                    vss.CurrentViewSheetSet = old
                    vss.Delete()
            vss.CurrentViewSheetSet.Views = vs
            vss.SaveAs(hs.BO_TO)
            out["bo_to"] = hs.BO_TO
        except Exception as ex:
            out["bo_to_loi"] = str(ex)[:150]
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return out
