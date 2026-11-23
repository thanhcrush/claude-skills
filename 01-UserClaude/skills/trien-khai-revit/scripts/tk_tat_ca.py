# -*- coding: utf-8 -*-
# Chay tron bo trien khai trong MOT lan run_modify (nguoi dung chi bam Keep mot lan):
#   tk0 chuan ho so -> tk1 khung ten -> tk2 ghi chu mat bang -> tk3 bang thong ke -> tk4 to ban ve.
# Dung: import tk_tat_ca, hoso_xxx as hs; result = tk_tat_ca.chay(doc, app, hs)
import tk0_chuan, tk1_khung_ten, tk2_ghi_chu, tk3_bang, tk4_to
from vn_revit import ascii_safe


def chay(doc, app, hs, file_dich=None, ghi_de_khung=True):
    if file_dich and doc.Title != file_dich:
        raise Exception("File dang mo khong phai %s - dung lai" % file_dich)
    out = {}
    out["tk0"] = tk0_chuan.chay(doc, hs)
    out["tk1"] = tk1_khung_ten.chay(doc, app, hs, ghi_de=ghi_de_khung)
    out["tk2"] = tk2_ghi_chu.chay(doc, hs)
    out["tk3"] = tk3_bang.chay(doc, hs)
    out["tk4"] = tk4_to.chay(doc, hs)
    return ascii_safe(out)
