# -*- coding: utf-8 -*-
# TRIEN KHAI 3: bang thong ke cua di, cua so, phong (ViewSchedule). Chay lai duoc (xoa theo ten).
from pyrevit.api import DB
from vn_revit import *

BIP = DB.BuiltInParameter
BANG = [
    {"ten": u"BẢNG THỐNG KÊ CỬA ĐI", "cat": DB.BuiltInCategory.OST_Doors, "tung_cai": False,
     "cot": [(BIP.ALL_MODEL_TYPE_MARK, u"Ký hiệu"), (BIP.DOOR_WIDTH, u"Rộng (mm)"),
             (BIP.DOOR_HEIGHT, u"Cao (mm)"), ("COUNT", u"Số lượng")]},
    {"ten": u"BẢNG THỐNG KÊ CỬA SỔ", "cat": DB.BuiltInCategory.OST_Windows, "tung_cai": False,
     "cot": [(BIP.ALL_MODEL_TYPE_MARK, u"Ký hiệu"), (BIP.WINDOW_WIDTH, u"Rộng (mm)"),
             (BIP.WINDOW_HEIGHT, u"Cao (mm)"), ("COUNT", u"Số lượng")]},
    {"ten": u"BẢNG THỐNG KÊ PHÒNG", "cat": DB.BuiltInCategory.OST_Rooms, "tung_cai": True,
     "cot": [(BIP.ROOM_LEVEL_ID, u"Tầng"), (BIP.ROOM_NUMBER, u"Số"), (BIP.ROOM_NAME, u"Tên phòng"),
             (BIP.ROOM_AREA, u"Diện tích (m²)")]},
]


def _field(sd, key):
    for sf in sd.GetSchedulableFields():
        if key == "COUNT" and sf.FieldType == DB.ScheduleFieldType.Count:
            return sf
        if key != "COUNT" and sf.ParameterId == DB.ElementId(key):
            return sf
    return None


def chay(doc, hs=None):
    out = {}
    tr = DB.Transaction(doc, "vn: trien khai 3 - bang thong ke")
    tr.Start()
    try:
        for b in BANG:
            for s in collect(doc, DB.ViewSchedule):
                if s.Name == b["ten"]:
                    doc.Delete(s.Id)
            sch = DB.ViewSchedule.CreateSchedule(doc, DB.ElementId(b["cat"]))
            sch.Name = b["ten"]
            sd = sch.Definition
            fids = []
            thieu = []
            for key, head in b["cot"]:
                sf = _field(sd, key)
                if sf is None:
                    thieu.append(head)
                    continue
                f = sd.AddField(sf)
                f.ColumnHeading = head
                fids.append(f.FieldId)
            sd.IsItemized = b["tung_cai"]
            if fids:
                sd.AddSortGroupField(DB.ScheduleSortGroupField(fids[0]))
                if b["tung_cai"] and len(fids) > 1:
                    sd.AddSortGroupField(DB.ScheduleSortGroupField(fids[1]))
            if b["tung_cai"]:
                sd.ShowGrandTotal = True
            out[b["ten"].encode("unicode_escape")] = {"cot": len(fids), "thieu": [t.encode("unicode_escape") for t in thieu]}
        tr.Commit()
    except Exception:
        tr.RollBack()
        raise
    return out
