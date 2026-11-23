# -*- coding: utf-8 -*-
# Ham dung chung cho cac chang dung mo hinh Revit (pyRevit agent runtime).
# ASCII only. Dung voi: from vn_revit import *
from pyrevit.api import DB
from vn_don_vi import ft, mm

NHAN = "vn:"


def ascii_safe(value):
    """Doi chu co dau thanh \\uXXXX truoc khi tra 'result' (IronPython loi serialize chu co dau)."""
    if isinstance(value, dict):
        return dict((ascii_safe(k), ascii_safe(v)) for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return [ascii_safe(v) for v in value]
    try:
        is_text = isinstance(value, basestring)  # noqa: F821
    except NameError:
        is_text = isinstance(value, str)
    if is_text:
        return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in value)
    return value


def collect(doc, cls=None, cat=None, types=False):
    c = DB.FilteredElementCollector(doc)
    if cls is not None:
        c = c.OfClass(cls)
    if cat is not None:
        c = c.OfCategory(cat)
    c = c.WhereElementIsElementType() if types else c.WhereElementIsNotElementType()
    return list(c)


def ten(e):
    p = e.get_Parameter(DB.BuiltInParameter.SYMBOL_NAME_PARAM)
    if p and p.AsString():
        return p.AsString()
    try:
        return DB.Element.Name.GetValue(e)
    except Exception:
        pass
    try:
        return e.Name
    except Exception:
        p = e.get_Parameter(DB.BuiltInParameter.ALL_MODEL_TYPE_NAME)
        return p.AsString() if p else ""


def tim_loai(doc, cls, name, cat=None, family=None):
    for t in collect(doc, cls, cat, types=True):
        if ten(t) == name and (family is None or getattr(t, "FamilyName", None) == family):
            return t
    return None


def nhan_ban(doc, cls, goc, moi, cat=None, family=None):
    """Lay loai 'moi' neu da co, neu chua thi nhan ban tu loai 'goc'."""
    t = tim_loai(doc, cls, moi, cat, family)
    if t is not None:
        return t
    g = tim_loai(doc, cls, goc, cat, family)
    if g is None:
        raise Exception("Khong co loai goc: %s" % goc)
    return g.Duplicate(moi)


def dat(e, name, value):
    p = e.LookupParameter(name)
    if p is None or p.IsReadOnly:
        raise Exception("Khong dat duoc tham so %s cho %s" % (name, ten(e)))
    p.Set(value)


def comments(e, s):
    e.get_Parameter(DB.BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).Set(s)


def xoa_theo_nhan(doc, prefix):
    """Xoa moi phan tu co Comments bat dau bang prefix (de chay lai chang khong bi trung)."""
    ids = []
    for e in DB.FilteredElementCollector(doc).WhereElementIsNotElementType():
        p = e.get_Parameter(DB.BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
        if p is not None:
            s = p.AsString()
            if s and s.startswith(prefix):
                ids.append(e.Id)
    from System.Collections.Generic import List
    if ids:
        doc.Delete(List[DB.ElementId](ids))
    return len(ids)


def dem_theo_nhan(doc, prefix):
    n = 0
    for e in DB.FilteredElementCollector(doc).WhereElementIsNotElementType():
        p = e.get_Parameter(DB.BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
        if p is not None:
            s = p.AsString()
            if s and s.startswith(prefix):
                n += 1
    return n


def levels(doc, plan):
    """{khoa: Level} theo ten tang trong plan.TANG."""
    by_name = dict((l.Name, l) for l in collect(doc, DB.Level))
    out = {}
    for k, name, z in plan.TANG:
        if name in by_name:
            out[k] = by_name[name]
    return out


def xyz(x_mm, y_mm, z_mm=0):
    return DB.XYZ(ft(x_mm), ft(y_mm), ft(z_mm))


def line(a, b, z=0):
    return DB.Line.CreateBound(xyz(a[0], a[1], z), xyz(b[0], b[1], z))


def curve_loop(pts, z=0):
    loop = DB.CurveLoop()
    n = len(pts)
    for i in range(n):
        loop.Append(line(pts[i], pts[(i + 1) % n], z))
    return loop
