# -*- coding: utf-8 -*-
# CHANG 0: don vi mm + nhan ban cac loai (tuong, san, mai, cot, cua, cau thang, lan can).
# Chay lai duoc: loai da co thi chi dat lai kich thuoc.
from pyrevit.api import DB
from vn_revit import *

OST = DB.BuiltInCategory


def set_layer(t, width_mm):
    cs = t.GetCompoundStructure()
    cs.SetLayerWidth(0, ft(width_mm))
    t.SetCompoundStructure(cs)


def chang0(doc):
    made = []
    # don vi hien thi
    units = doc.GetUnits()
    units.SetFormatOptions(DB.SpecTypeId.Length, DB.FormatOptions(DB.UnitTypeId.Millimeters))
    units.SetFormatOptions(DB.SpecTypeId.Area, DB.FormatOptions(DB.UnitTypeId.SquareMeters))
    units.SetFormatOptions(DB.SpecTypeId.Volume, DB.FormatOptions(DB.UnitTypeId.CubicMeters))
    doc.SetUnits(units)

    t = nhan_ban(doc, DB.WallType, 'Generic - 8"', "VN-Tuong gach 220"); set_layer(t, 220); made.append(ten(t))
    t = nhan_ban(doc, DB.WallType, 'Exterior Glazing', "VN-Vach kinh"); made.append(ten(t))
    t = nhan_ban(doc, DB.FloorType, 'Generic - 12"', "VN-San BTCT 120"); set_layer(t, 120); made.append(ten(t))
    t = nhan_ban(doc, DB.FloorType, 'Generic - 12"', "VN-Nen BT 100"); set_layer(t, 100); made.append(ten(t))
    t = nhan_ban(doc, DB.RoofType, 'Generic - 9"', "VN-Mai ngoi"); set_layer(t, 100); made.append(ten(t))

    for name, b, h in [("VN-C220x220", 220, 220), ("VN-C220x350", 220, 350), ("VN-C350x220", 350, 220),
                       ("VN-BT800x330", 800, 330), ("VN-BT800x400", 800, 400)]:
        t = nhan_ban(doc, DB.FamilySymbol, "12 x 18", name, OST.OST_StructuralColumns, "Concrete-Rectangular-Column")
        dat(t, "b", ft(b)); dat(t, "h", ft(h)); made.append(name)

    for name, goc, fam, w, h in [("VN-D1 1400x2800", '72" x 84"', "Door-Passage-Double-Flush", 1400, 2800),
                                 ("VN-D2 900x2800", '36" x 84"', "Door-Passage-Single-Flush", 900, 2800)]:
        t = nhan_ban(doc, DB.FamilySymbol, goc, name, OST.OST_Doors, fam)
        dat(t, "Width", ft(w)); dat(t, "Height", ft(h)); made.append(name)

    for name, w, h in [("VN-S1 1200x1900", 1200, 1900), ("VN-S2 2100x1900", 2100, 1900),
                       ("VN-S3 1200x500", 1200, 500), ("VN-VK1 3000x2250", 3000, 2250),
                       ("VN-VK2 2400x2250", 2400, 2250), ("VN-VK3 3000x3600", 3000, 3600),
                       ("VN-VK4 2400x3600", 2400, 3600)]:
        t = nhan_ban(doc, DB.FamilySymbol, '36" x 48"', name, OST.OST_Windows, "Window-Fixed")
        dat(t, "Width", ft(w)); dat(t, "Height", ft(h)); made.append(name)

    st = nhan_ban(doc, DB.Architecture.StairsType, "Monolithic Stair", "VN-Thang BTCT")
    st.MaxRiserHeight = ft(150); st.MinTreadDepth = ft(300); st.MinRunWidth = ft(1200)
    made.append(ten(st))
    rl = nhan_ban(doc, DB.Architecture.RailingType, "Guardrail - Rectangular", "VN-Lan can 1100")
    rl.TopRailHeight = ft(1100)
    made.append(ten(rl))

    # kich hoat symbol
    for s in collect(doc, DB.FamilySymbol, types=True):
        if ten(s).startswith("VN-") and not s.IsActive:
            s.Activate()
    return made


def chay(doc):
    tr = DB.Transaction(doc, "vn: chang 0 - loai va don vi")
    tr.Start()
    try:
        made = chang0(doc)
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return {"loai": made}
