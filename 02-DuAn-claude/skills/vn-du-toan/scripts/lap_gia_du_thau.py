# -*- coding: utf-8 -*-
"""Lap BANG GIA DU THAU (E-HSDT xay lap) ra Excel, giu cong thuc.

Hai lenh:
  xuat <du_lieu.json> <BangGiaDuThau_vNN.xlsx>
      Sinh file Excel 6 sheet (00-CauHinh ... 05-PhieuWebform) tu file JSON.
  boq  <BangKhoiLuongMoiThau.xlsx> <boq.json> [--sheet TEN] [--dong-dau N] [--cot stt=A,ma=B,ten=C,dvt=D,kl=E,nguon=F]
      Doc bang khoi luong moi thau dang Excel thanh danh sach "boq" cho file JSON.

Nguyen tac:
  * Khoi luong lay tu E-HSMT, khong sua. Don gia chi nhap khi co nguon; thieu thi de trong (o vang).
  * Ty le chi phi (chi phi chung, thu nhap chiu thue, GTGT...) KHONG co gia tri mac dinh: phai do
    nguoi dung dien kem nguon. Chua dien thi o vang va sheet 04-Soat bao loi.
  * Khong ghi de file da co: tang so phien ban _v02, _v03.
"""
import argparse
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import column_index_from_string, get_column_letter

FONT = "Times New Roman"
THIN = Side(style="thin", color="A6A6A6")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEAD_FILL = PatternFill("solid", fgColor="D9D9D9")
SEC_FILL = PatternFill("solid", fgColor="F2F2F2")
YELLOW = PatternFill("solid", bgColor="FFFF00", fgColor="FFFF00")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")

S_CFG, S_BG, S_PT, S_TH, S_SOAT, S_WEB = (
    "00-CauHinh", "01-BangGiaDuThau", "02-PhanTichDonGia", "03-TongHop", "04-Soat", "05-PhieuWebform")


def q(sheet):
    return "'%s'" % sheet


FIRST = 6  # dong dau tien cua du lieu trong sheet 01, 02, 05

# Hang trong sheet 00-CauHinh
ROW_GIAGOI = 9
CFG = {"chi_phi_chung": 14, "thu_nhap": 15, "khong_xd_kl": 16, "gtgt": 17,
       "nha_tam": 18, "giam_gia": 19, "nguong": 20}
CFG_NHAN = {
    "chi_phi_chung": "Chi phí chung (% chi phí trực tiếp)",
    "thu_nhap": "Thu nhập chịu thuế tính trước (% )",
    "khong_xd_kl": "Công việc không xác định được khối lượng từ thiết kế (% chi phí trực tiếp)",
    "gtgt": "Thuế GTGT (%)",
    "nha_tam": "Chi phí nhà tạm để ở và điều hành thi công (%), chỉ khi E-HSMT cho tách riêng",
    "giam_gia": "Giảm giá (%): Giám đốc quyết định",
    "nguong": "Ngưỡng cảnh báo: đơn giá dự thầu / đơn giá tham chiếu nhỏ hơn (VD 0,85)",
}
CFG_BATBUOC = ("chi_phi_chung", "thu_nhap", "gtgt")


# ---------------------------------------------------------------------------
# Tinh lai bang Python (doc lap voi cong thuc Excel) de doi chieu
# ---------------------------------------------------------------------------
def lam_tron(x, so_le=0):
    """ROUND cua Excel: lam tron nua ra xa so 0."""
    d = Decimal(repr(float(x)))
    muc = Decimal(1).scaleb(-so_le)
    return float(d.quantize(muc, rounding=ROUND_HALF_UP))


def _gt(ty_le, khoa):
    muc = (ty_le or {}).get(khoa)
    if muc is None:
        return None
    return muc.get("gia_tri")


def tinh(du_lieu):
    """Tinh tong gia du thau tu du lieu JSON. Tra ve dict so lieu chinh."""
    ty = du_lieu.get("ty_le", {})
    cpc = _gt(ty, "chi_phi_chung") or 0.0
    tt = _gt(ty, "khong_xd_kl") or 0.0
    tn = _gt(ty, "thu_nhap") or 0.0
    gtgt = _gt(ty, "gtgt") or 0.0
    nt = _gt(ty, "nha_tam") or 0.0
    gg = _gt(ty, "giam_gia") or 0.0

    tong = gia_thanh = 0.0
    so_dong = thieu_dg = kl_loi = dg_bang_0 = 0
    for it in du_lieu["boq"]:
        if it.get("loai") == "muc":
            continue
        so_dong += 1
        kl = it.get("kl")
        dg = it.get("don_gia") or {}
        tp = [dg.get(k) for k in ("vl", "nc", "m")]
        co_gia = any(v is not None for v in tp)
        T = sum(v for v in tp if v is not None)
        C = T * cpc
        K = T * tt
        L = (T + C + K) * tn
        don_gia = lam_tron(T + C + K + L, 0)
        if not co_gia:
            thieu_dg += 1
        elif don_gia == 0:
            dg_bang_0 += 1
        if not (isinstance(kl, (int, float)) and kl > 0):
            kl_loi += 1
            kl = 0
        tong += lam_tron(kl * don_gia, 0)
        gia_thanh += kl * (T + C + K)
    giam = -lam_tron(tong * gg, 0) or 0.0
    sau_giam = tong + giam
    thue = lam_tron(sau_giam * gtgt, 0)
    nha_tam = lam_tron(sau_giam * nt * (1 + gtgt), 0)
    return {
        "so_dong": so_dong, "thieu_don_gia": thieu_dg, "kl_loi": kl_loi, "don_gia_bang_0": dg_bang_0,
        "cong_truoc_thue": tong, "giam_gia": giam, "sau_giam_truoc_thue": sau_giam,
        "gtgt": thue, "nha_tam": nha_tam, "gia_du_thau": sau_giam + thue + nha_tam,
        "gia_thanh": gia_thanh, "loi_nhuan": sau_giam - gia_thanh,
    }


# ---------------------------------------------------------------------------
# Doc so thanh chu (dung cho don du thau)
# ---------------------------------------------------------------------------
_CHU_SO = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _doc3(n, day_du):
    tram, chuc, dv = n // 100, (n // 10) % 10, n % 10
    p = []
    if tram > 0 or day_du:
        p.append(_CHU_SO[tram] + " trăm")
    if chuc > 1:
        p.append(_CHU_SO[chuc] + " mươi")
        if dv == 1:
            p.append("mốt")
        elif dv == 5:
            p.append("lăm")
        elif dv > 0:
            p.append(_CHU_SO[dv])
    elif chuc == 1:
        p.append("mười")
        if dv == 5:
            p.append("lăm")
        elif dv > 0:
            p.append(_CHU_SO[dv])
    elif dv > 0:
        if tram > 0 or day_du:
            p.append("lẻ")
        p.append(_CHU_SO[dv])
    return " ".join(p)


def so_thanh_chu(n):
    """So nguyen dong -> chu, vd 1005 -> 'Một nghìn không trăm lẻ năm đồng'."""
    n = int(round(n))
    if n == 0:
        return "Không đồng"
    am = n < 0
    n = abs(n)
    nhom = []
    while n:
        nhom.append(n % 1000)
        n //= 1000
    ten = ["", "nghìn", "triệu"]
    out = []
    for i in range(len(nhom) - 1, -1, -1):
        g = nhom[i]
        if g == 0:
            continue
        s = _doc3(g, day_du=(i < len(nhom) - 1))
        suffix = (ten[i % 3] + (" tỷ" if i >= 3 else "")).strip()
        out.append((s + " " + suffix).strip())
    chu = " ".join(out)
    return ("Âm " if am else "") + chu[0].upper() + chu[1:] + " đồng"


# ---------------------------------------------------------------------------
# Xuat Excel
# ---------------------------------------------------------------------------
def _font(bold=False, size=11, italic=False, color=None):
    return Font(name=FONT, size=size, bold=bold, italic=italic, color=color)


def _put(ws, r, c, v, align="left", fmt=None, bold=False, wrap=False, fill=None, border=True, italic=False):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = _font(bold=bold, italic=italic)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    if border:
        cell.border = BOX
    if fmt:
        cell.number_format = fmt
    if fill:
        cell.fill = fill
    return cell


def _head(ws, r, cols):
    for i, (name, w) in enumerate(cols, 1):
        c = ws.cell(row=r, column=i, value=name)
        c.font = _font(bold=True)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.fill = HEAD_FILL
        c.border = BOX
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[r].height = 32


def _title(ws, text, sub, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws["A1"] = text
    ws["A1"].font = _font(bold=True, size=14)
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    ws["A2"] = sub
    ws["A2"].font = _font(italic=True)
    ws["A2"].alignment = Alignment(horizontal="center", wrap_text=True)
    ws.row_dimensions[1].height = 24
    ws.row_dimensions[2].height = 30


def _section(ws, r, text, ncols):
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncols)
    c = ws.cell(row=r, column=1, value=text)
    c.font = _font(bold=True)
    c.fill = SEC_FILL
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    for i in range(1, ncols + 1):
        ws.cell(row=r, column=i).border = BOX


def cfg_ref(khoa):
    return "%s!$B$%d" % (q(S_CFG), CFG[khoa])


def _sheet_cauhinh(ws, du_lieu):
    gt = du_lieu["goi_thau"]
    ty = du_lieu.get("ty_le", {})
    _title(ws, "CẤU HÌNH GIÁ DỰ THẦU", "Ô vàng = chưa có số liệu [Chờ bổ sung]. Mọi tỷ lệ phải có nguồn.", 3)
    ws.column_dimensions["A"].width = 62
    ws.column_dimensions["B"].width = 26
    ws.column_dimensions["C"].width = 70
    _section(ws, 3, "THÔNG TIN GÓI THẦU (theo E-HSMT)", 3)
    info = [
        (4, "Tên gói thầu", gt.get("ten")), (5, "Mã TBMT", gt.get("ma_tbmt")),
        (6, "Bên mời thầu", gt.get("ben_moi_thau")), (7, "Địa điểm xây dựng", gt.get("dia_diem")),
        (8, "Loại hợp đồng / hình thức giá", gt.get("hop_dong")),
        (9, "Giá gói thầu (đồng, theo E-HSMT)", gt.get("gia_goi_thau")),
        (10, "Đơn vị lập", du_lieu.get("don_vi_lap", "Công ty TNHH Nghĩa Đạt")),
        (11, "Ngày lập", du_lieu.get("ngay")),
    ]
    for r, nhan, v in info:
        _put(ws, r, 1, nhan)
        c = _put(ws, r, 2, v, align="right" if r == ROW_GIAGOI else "left",
                 fmt="#,##0" if r == ROW_GIAGOI else None, wrap=True)
        _put(ws, r, 3, gt.get("nguon_gia_goi_thau", "") if r == ROW_GIAGOI else gt.get("nguon_%d" % r, ""), wrap=True)
        if v in (None, ""):
            c.fill = YELLOW
    _section(ws, 13, "TỶ LỆ CHI PHÍ (không có giá trị mặc định: điền kèm nguồn, xem lap-du-toan mục 4 và E-HSMT)", 3)
    for khoa, r in CFG.items():
        _put(ws, r, 1, CFG_NHAN[khoa], wrap=True)
        muc = ty.get(khoa)
        if muc is None:
            if khoa in CFG_BATBUOC:
                v, nguon = None, "[Chờ bổ sung]"
            elif khoa == "nguong":
                v, nguon = None, "Không đặt ngưỡng"
            elif khoa == "giam_gia":
                v, nguon = 0, "Chờ Giám đốc quyết định (0 = chưa giảm)"
            else:
                v, nguon = 0, "Không áp dụng"
        else:
            v, nguon = muc.get("gia_tri"), muc.get("nguon", "") or "[Chờ bổ sung]"
        c = _put(ws, r, 2, v, align="right", fmt="0.00%" if khoa != "nguong" else "0.00", fill=None)
        _put(ws, r, 3, nguon, wrap=True)
        if khoa in CFG_BATBUOC:
            ws.conditional_formatting.add("B%d" % r, FormulaRule(formula=["$B$%d=\"\"" % r], fill=YELLOW))
    ws.conditional_formatting.add("B%d" % ROW_GIAGOI, FormulaRule(formula=["$B$%d=\"\"" % ROW_GIAGOI], fill=YELLOW))
    ws.freeze_panes = "A3"


def _sheet_banggia(ws, du_lieu, last):
    boq = du_lieu["boq"]
    gt = du_lieu["goi_thau"]
    _title(ws, "BẢNG GIÁ DỰ THẦU",
           "Gói thầu: %s  |  Mã TBMT: %s  |  Đơn vị lập: %s" % (
               gt.get("ten", ""), gt.get("ma_tbmt", ""), du_lieu.get("don_vi_lap", "Công ty TNHH Nghĩa Đạt")), 8)
    _head(ws, 5, [("STT", 7), ("Mã hiệu", 12), ("Nội dung công việc (theo E-HSMT)", 58), ("ĐVT", 9),
                  ("Khối lượng mời thầu", 14), ("Đơn giá dự thầu (đồng)", 16), ("Thành tiền (đồng)", 19),
                  ("Nguồn khối lượng", 30)])
    r = FIRST
    for it in boq:
        if it.get("loai") == "muc":
            _section(ws, r, it["ten"], 8)
        else:
            _put(ws, r, 1, it.get("stt"), "center")
            _put(ws, r, 2, it.get("ma"), "center")
            _put(ws, r, 3, it.get("ten"), "left", wrap=True)
            _put(ws, r, 4, it.get("dvt"), "center")
            _put(ws, r, 5, it.get("kl"), "right", fmt="#,##0.000")
            _put(ws, r, 6, "=%s!M%d" % (q(S_PT), r), "right", fmt="#,##0")
            _put(ws, r, 7, "=ROUND(E%d*F%d,0)" % (r, r), "right", fmt="#,##0")
            _put(ws, r, 8, it.get("nguon_kl", ""), "left", wrap=True)
        r += 1
    ws.conditional_formatting.add("E%d:E%d" % (FIRST, last), FormulaRule(
        formula=['AND($D%d<>"",NOT(AND(ISNUMBER($E%d),$E%d>0)))' % (FIRST, FIRST, FIRST)], fill=YELLOW))
    ws.freeze_panes = "A6"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1


def _sheet_phantich(ws, du_lieu, last):
    boq = du_lieu["boq"]
    _title(ws, "PHÂN TÍCH ĐƠN GIÁ DỰ THẦU",
           "Đơn giá trực tiếp trên 1 đơn vị (VL, NC, M) lấy từ F1 hoặc phân tích nội bộ, có nguồn và kỳ giá. "
           "Ô vàng = chưa có đơn giá [Chờ bổ sung].", 19)
    _head(ws, 5, [("STT", 7), ("Mã hiệu", 12), ("Nội dung công việc", 44), ("ĐVT", 8), ("Khối lượng", 12),
                  ("Vật liệu", 13), ("Nhân công", 13), ("Máy thi công", 13), ("Chi phí trực tiếp T", 14),
                  ("Chi phí chung", 13), ("CV không xác định KL", 13), ("Thu nhập chịu thuế tính trước", 14),
                  ("Đơn giá dự thầu (trước thuế)", 15), ("Đơn giá tham chiếu", 14), ("Tỷ lệ DG/Tham chiếu", 11),
                  ("Thiếu ĐG", 8), ("KL lỗi", 8), ("ĐG = 0", 8), ("Nguồn đơn giá, kỳ giá", 36)])
    r = FIRST
    for it in boq:
        if it.get("loai") == "muc":
            _section(ws, r, it["ten"], 19)
        else:
            dg = it.get("don_gia") or {}
            for col, khoa in ((1, "A"), (2, "B"), (3, "C"), (4, "D")):
                src = "%s!%s%d" % (q(S_BG), khoa, r)
                _put(ws, r, col, '=IF(%s="","",%s)' % (src, src), "center" if col != 3 else "left", wrap=(col == 3))
            _put(ws, r, 5, "=%s!E%d" % (q(S_BG), r), "right", fmt="#,##0.000")
            for col, k in ((6, "vl"), (7, "nc"), (8, "m")):
                _put(ws, r, col, dg.get(k), "right", fmt="#,##0")
            _put(ws, r, 9, "=SUM(F%d:H%d)" % (r, r), "right", fmt="#,##0")
            _put(ws, r, 10, "=I%d*%s" % (r, cfg_ref("chi_phi_chung")), "right", fmt="#,##0")
            _put(ws, r, 11, "=I%d*%s" % (r, cfg_ref("khong_xd_kl")), "right", fmt="#,##0")
            _put(ws, r, 12, "=(I%d+J%d+K%d)*%s" % (r, r, r, cfg_ref("thu_nhap")), "right", fmt="#,##0")
            _put(ws, r, 13, "=ROUND(I%d+J%d+K%d+L%d,0)" % (r, r, r, r), "right", fmt="#,##0", bold=True)
            _put(ws, r, 14, dg.get("tham_chieu"), "right", fmt="#,##0")
            _put(ws, r, 15, '=IF(AND(ISNUMBER(N%d),N%d>0),M%d/N%d,"")' % (r, r, r, r), "right", fmt="0.00")
            _put(ws, r, 16, '=IF(AND(D%d<>"",COUNT(F%d:H%d)=0),1,0)' % (r, r, r), "center")
            _put(ws, r, 17, '=IF(AND(D%d<>"",NOT(AND(ISNUMBER(E%d),E%d>0))),1,0)' % (r, r, r), "center")
            _put(ws, r, 18, '=IF(AND(D%d<>"",P%d=0,M%d=0),1,0)' % (r, r, r), "center")
            nguon = dg.get("nguon") or ""
            if not any(dg.get(k) is not None for k in ("vl", "nc", "m")) and not nguon:
                nguon = "[Chờ bổ sung]"
            _put(ws, r, 19, nguon, "left", wrap=True)
        r += 1
    ws.conditional_formatting.add("F%d:H%d" % (FIRST, last), FormulaRule(
        formula=["$P%d=1" % FIRST], fill=YELLOW))
    ws.freeze_panes = "F6"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1


def _sheet_tonghop(ws, du_lieu, last):
    bg = q(S_BG)
    pt = q(S_PT)
    gg = cfg_ref("giam_gia")
    gtgt = cfg_ref("gtgt")
    nt = cfg_ref("nha_tam")
    _title(ws, "TỔNG HỢP GIÁ DỰ THẦU",
           "Giá dự thầu ở dòng 10 phải bằng giá ghi trong đơn dự thầu và trong webform.", 6)
    for col, w in zip("ABCDEF", (58, 22, 22, 22, 18, 18)):
        ws.column_dimensions[col].width = w
    tong = "SUM(%s!G%d:G%d)" % (bg, FIRST, last)
    E = "%s!E%d:E%d" % (pt, FIRST, last)

    def rng(col):
        return "%s!%s%d:%s%d" % (pt, col, FIRST, col, last)

    lines = [
        (5, "Cộng giá trị các hạng mục (trước thuế)", "=" + tong, "Σ thành tiền sheet 01", False),
        (6, "Giảm giá", "=-ROUND(B5*%s,0)" % gg, "Tỷ lệ ở 00-CauHinh; cách áp dụng theo E-HSMT", False),
        (7, "Giá sau giảm giá, trước thuế", "=B5+B6", "", False),
        (8, "Thuế GTGT", "=ROUND(B7*%s,0)" % gtgt, "Mức và căn cứ ghi ở 00-CauHinh", False),
        (9, "Chi phí nhà tạm (chỉ khi E-HSMT cho tách riêng)",
         "=ROUND(B7*%s*(1+%s),0)" % (nt, gtgt), "Công thức theo lap-du-toan mục 4: GXDTT x tỷ lệ x (1 + GTGT)", False),
        (10, "GIÁ DỰ THẦU (đã gồm thuế)", "=B7+B8+B9", "", True),
        (12, "Giá gói thầu", '=IF(%s!$B$%d="","",%s!$B$%d)' % (q(S_CFG), ROW_GIAGOI, q(S_CFG), ROW_GIAGOI),
         "Cần so cùng cơ sở với E-HSMT (đã/chưa gồm thuế)", False),
        (13, "Giá dự thầu / giá gói thầu", '=IF(B12="","",B10/B12)', "", False),
        (14, "Chênh so với giá gói thầu (đồng)", '=IF(B12="","",B10-B12)', "", False),
        (15, "Kết luận so với giá gói thầu",
         '=IF(B12="","Chưa nhập giá gói thầu [Chờ bổ sung]",IF(B10>B12,"VƯỢT giá gói thầu: có thể bị loại","Không vượt giá gói thầu"))',
         "", True),
        (18, "Giá thành (chi phí trực tiếp + gián tiếp), trước thuế",
         "=SUMPRODUCT(%s,%s)+SUMPRODUCT(%s,%s)+SUMPRODUCT(%s,%s)" % (E, rng("I"), E, rng("J"), E, rng("K")),
         "Σ KL x (T + chi phí chung + CV không xác định KL)", False),
        (19, "Lợi nhuận trước thuế sau giảm giá", "=B7-B18", "Âm = chào dưới giá thành", False),
        (20, "Tỷ suất lợi nhuận / giá thành", '=IF(B18=0,"",B19/B18)', "", False),
    ]
    for r, nhan, ct, ghi, bold in lines:
        _put(ws, r, 1, nhan, bold=bold, wrap=True)
        fmt = "#,##0"
        if r in (13, 20):
            fmt = "0.00%"
        _put(ws, r, 2, ct, "right" if r != 15 else "left", fmt=fmt, bold=bold)
        c = ws.cell(row=r, column=3, value=ghi)
        c.font = _font(italic=True)
    _section(ws, 11, "SO VỚI GIÁ GÓI THẦU", 6)
    _section(ws, 17, "GIÁ THÀNH VÀ LỢI NHUẬN", 6)
    _section(ws, 22, "KỊCH BẢN GIẢM GIÁ (nhập tỷ lệ vào ô vàng cột A; Giám đốc quyết định)", 6)
    for i, t in enumerate(["Tỷ lệ giảm giá", "Giá sau giảm, trước thuế", "Giá dự thầu (gồm thuế)",
                           "Lợi nhuận trước thuế", "% lợi nhuận / giá thành", "Giá dự thầu / giá gói thầu"], 1):
        c = ws.cell(row=23, column=i, value=t)
        c.font = _font(bold=True)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.fill = HEAD_FILL
        c.border = BOX
    ws.row_dimensions[23].height = 32
    kb = list(du_lieu.get("kich_ban_giam_gia") or [])
    kb += [None] * (3 - len(kb))
    for i in range(3):
        r = 24 + i
        _put(ws, r, 1, kb[i], "right", fmt="0.00%", fill=INPUT_FILL)
        _put(ws, r, 2, '=IF(A%d="","",B5-ROUND(B5*A%d,0))' % (r, r), "right", fmt="#,##0")
        _put(ws, r, 3, '=IF(A%d="","",B%d+ROUND(B%d*%s,0)+ROUND(B%d*%s*(1+%s),0))' % (r, r, r, gtgt, r, nt, gtgt),
             "right", fmt="#,##0")
        _put(ws, r, 4, '=IF(A%d="","",B%d-$B$18)' % (r, r), "right", fmt="#,##0")
        _put(ws, r, 5, '=IF(OR(A%d="",$B$18=0),"",D%d/$B$18)' % (r, r), "right", fmt="0.00%")
        _put(ws, r, 6, '=IF(OR(A%d="",$B$12=""),"",C%d/$B$12)' % (r, r), "right", fmt="0.00%")
    ws.cell(row=28, column=1, value="Ghi chú: giá thành chưa gồm chi phí tài chính (bảo lãnh, vốn lưu động) và rủi ro trượt giá. "
            "Hợp đồng trọn gói hoặc đơn giá cố định thì rủi ro này do nhà thầu chịu.").font = _font(italic=True)


def _sheet_soat(ws, du_lieu, last):
    pt = q(S_PT)
    bg = q(S_BG)
    th = q(S_TH)
    cf = q(S_CFG)
    _title(ws, "SOÁT GIÁ DỰ THẦU", "Mã D1 đến D6 theo references/checklist-loi-bi-loai.md của skill vn-dau-thau.", 5)
    _head(ws, 4, [("Mã checklist", 12), ("Nội dung kiểm", 62), ("Giá trị", 20), ("Kết quả", 34), ("Ghi chú", 46)])

    def R(col):
        return "%s!%s%d:%s%d" % (pt, col, FIRST, col, last)

    rows = [
        ("D1", "Số dòng công việc trong bảng giá", '=COUNTIF(%s,"?*")' % R("D"), '="Thông tin"', "So với bảng khối lượng mời thầu"),
        ("D1", "Dòng chưa có đơn giá", "=SUM(%s)" % R("P"), '=IF(C6=0,"ĐẠT","LỖI - LOẠI")', "Không được bỏ dòng; thiếu = bị hiệu chỉnh bất lợi hoặc loại"),
        ("D2", "Dòng khối lượng trống hoặc nhỏ hơn hoặc bằng 0", "=SUM(%s)" % R("Q"), '=IF(C7=0,"ĐẠT","LỖI - LOẠI")', "Không tự sửa khối lượng mời thầu; sai thì hỏi làm rõ"),
        ("D4", "Dòng đơn giá bằng 0", "=SUM(%s)" % R("R"), '=IF(C8=0,"ĐẠT","XEM LẠI - RỦI RO")', "Chỉ chấp nhận khi E-HSMT cho phép và có ghi chú"),
        ("D5", "Tỷ lệ bắt buộc chưa điền (chi phí chung, thu nhập chịu thuế, GTGT)",
         '=(%s!B%d="")+(%s!B%d="")+(%s!B%d="")' % (cf, CFG["chi_phi_chung"], cf, CFG["thu_nhap"], cf, CFG["gtgt"]),
         '=IF(C9=0,"ĐẠT","LỖI - LOẠI")', "Theo hướng dẫn trong E-HSMT"),
        ("D3", "Chênh Σ thành tiền (01) và Σ KL x ĐG (02), do làm tròn",
         "=ABS(SUM(%s!G%d:G%d)-SUMPRODUCT(%s,%s))" % (bg, FIRST, last, R("E"), R("M")),
         '=IF(C10<=0.5*C5,"ĐẠT","XEM LẠI - kiểm liên kết")', "Lớn bất thường = liên kết công thức bị hỏng"),
        ("D6", "Giá dự thầu / giá gói thầu", "=%s!B13" % th,
         '=IF(C11="","Chưa nhập giá gói thầu",IF(C11>1,"LỖI - VƯỢT giá gói thầu","ĐẠT"))', "Xác nhận cùng cơ sở thuế với E-HSMT"),
        ("D4", "Dòng có đơn giá dự thầu thấp hơn ngưỡng so với đơn giá tham chiếu",
         '=IF(OR(%s!B%d="",COUNT(%s)=0),"",COUNTIF(%s,"<"&%s!B%d))' % (cf, CFG["nguong"], R("N"), R("O"), cf, CFG["nguong"]),
         '=IF(C12="","Chưa đặt ngưỡng hoặc đơn giá tham chiếu",IF(C12=0,"ĐẠT","XEM LẠI - RỦI RO"))', "Dòng quá thấp dễ bị yêu cầu làm rõ giá bất thường"),
        ("", "Cơ cấu: vật liệu / chi phí trực tiếp", '=IFERROR(SUMPRODUCT(%s,%s)/SUMPRODUCT(%s,%s),"")' % (R("E"), R("F"), R("E"), R("I")), '="Thông tin"', ""),
        ("", "Cơ cấu: nhân công / chi phí trực tiếp", '=IFERROR(SUMPRODUCT(%s,%s)/SUMPRODUCT(%s,%s),"")' % (R("E"), R("G"), R("E"), R("I")), '="Thông tin"', ""),
        ("", "Cơ cấu: máy / chi phí trực tiếp", '=IFERROR(SUMPRODUCT(%s,%s)/SUMPRODUCT(%s,%s),"")' % (R("E"), R("H"), R("E"), R("I")), '="Thông tin"', ""),
        ("", "Lợi nhuận sau giảm giá / giá thành", "=%s!B20" % th,
         '=IF(C16="","",IF(C16<0,"LỖ - chào dưới giá thành","ĐẠT"))', "Giám đốc quyết định mức giảm giá"),
    ]
    for i, (ma, nd, gt_, kq, gc) in enumerate(rows):
        r = 5 + i
        _put(ws, r, 1, ma, "center")
        _put(ws, r, 2, nd, wrap=True)
        fmt = "0.00%" if "Cơ cấu" in nd or "Giá dự thầu /" in nd or "Lợi nhuận" in nd else "#,##0"
        _put(ws, r, 3, gt_, "right", fmt=fmt)
        _put(ws, r, 4, kq, "left", wrap=True)
        _put(ws, r, 5, gc, "left", wrap=True)
    cuoi = 5 + len(rows) - 1
    r = cuoi + 2
    _put(ws, r, 2, "TÌNH TRẠNG CHUNG", bold=True)
    _put(ws, r, 4,
         '=IF(COUNTIF(D5:D%d,"LỖI*")>0,"CÒN LỖI LOẠI",IF(COUNTIF(D5:D%d,"XEM LẠI*")+COUNTIF(D5:D%d,"LỖ*")>0,"CÒN RỦI RO","ĐẠT"))'
         % (cuoi, cuoi, cuoi), bold=True)
    for rr in range(5, cuoi + 1):
        ws.conditional_formatting.add("D%d" % rr, FormulaRule(formula=['LEFT($D%d,3)="LỖI"' % rr], fill=YELLOW))
    ws.freeze_panes = "A5"


def _sheet_webform(ws, du_lieu, last):
    bg = q(S_BG)
    th = q(S_TH)
    _title(ws, "PHIẾU NHẬP WEBFORM: GIÁ DỰ THẦU",
           "Anh Thành gõ theo phiếu này vào Hệ thống mạng đấu thầu quốc gia. Số ở đây là công thức liên kết sheet 01, không gõ tay.", 6)
    _head(ws, 5, [("STT", 7), ("Nội dung công việc", 60), ("ĐVT", 9), ("Khối lượng", 14),
                  ("Đơn giá dự thầu", 16), ("Thành tiền", 19)])
    r = FIRST
    for it in du_lieu["boq"]:
        if it.get("loai") == "muc":
            _section(ws, r, it["ten"], 6)
        else:
            _put(ws, r, 1, '=IF(%s!A%d="","",%s!A%d)' % (bg, r, bg, r), "center")
            _put(ws, r, 2, '=IF(%s!C%d="","",%s!C%d)' % (bg, r, bg, r), "left", wrap=True)
            _put(ws, r, 3, '=IF(%s!D%d="","",%s!D%d)' % (bg, r, bg, r), "center")
            _put(ws, r, 4, "=%s!E%d" % (bg, r), "right", fmt="#,##0.000")
            _put(ws, r, 5, "=%s!F%d" % (bg, r), "right", fmt="#,##0")
            _put(ws, r, 6, "=%s!G%d" % (bg, r), "right", fmt="#,##0")
        r += 1
    r += 1
    for nhan, ref in (("Cộng giá trị các hạng mục (trước thuế)", "B5"), ("Giảm giá", "B6"),
                      ("Giá sau giảm giá, trước thuế", "B7"), ("Thuế GTGT", "B8"),
                      ("Chi phí nhà tạm", "B9"), ("GIÁ DỰ THẦU (đã gồm thuế)", "B10")):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        c = ws.cell(row=r, column=1, value=nhan)
        c.font = _font(bold=nhan.startswith("GIÁ"))
        c.alignment = Alignment(horizontal="right")
        _put(ws, r, 6, "=%s!%s" % (th, ref), "right", fmt="#,##0", bold=nhan.startswith("GIÁ"))
        r += 1
    ws.freeze_panes = "A6"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1


def xuat(du_lieu, duong_dan):
    if os.path.exists(duong_dan):
        raise SystemExit("File đã có, không ghi đè: %s\nĐổi số phiên bản (_v02, _v03...)." % duong_dan)
    boq = du_lieu.get("boq") or []
    if not boq:
        raise SystemExit("Danh sách boq trống: chưa có bảng khối lượng mời thầu.")
    last = FIRST + len(boq) - 1
    wb = Workbook()
    ws_cfg = wb.active
    ws_cfg.title = S_CFG
    ws = {n: wb.create_sheet(n) for n in (S_BG, S_PT, S_TH, S_SOAT, S_WEB)}
    _sheet_cauhinh(ws_cfg, du_lieu)
    _sheet_banggia(ws[S_BG], du_lieu, last)
    _sheet_phantich(ws[S_PT], du_lieu, last)
    _sheet_tonghop(ws[S_TH], du_lieu, last)
    _sheet_soat(ws[S_SOAT], du_lieu, last)
    _sheet_webform(ws[S_WEB], du_lieu, last)
    for w in wb.worksheets:
        w.sheet_view.zoomScale = 90
    wb.save(duong_dan)
    return duong_dan


# ---------------------------------------------------------------------------
# Doc bang khoi luong moi thau dang Excel
# ---------------------------------------------------------------------------
def boq_tu_excel(duong_dan, sheet=None, dong_dau=2, cot=None):
    """Doc BOQ E-HSMT dang xlsx. Dong co DVT va khoi luong la so -> cong viec; dong con lai co chu -> muc."""
    cot = cot or {"stt": "A", "ma": "B", "ten": "C", "dvt": "D", "kl": "E"}
    wb = load_workbook(duong_dan, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    idx = {k: column_index_from_string(v) for k, v in cot.items()}
    out = []
    for r in range(dong_dau, ws.max_row + 1):
        def g(k):
            if k not in idx:
                return None
            v = ws.cell(row=r, column=idx[k]).value
            return v.strip() if isinstance(v, str) else v
        ten, dvt, kl = g("ten"), g("dvt"), g("kl")
        if ten in (None, "") and dvt in (None, "") and kl in (None, ""):
            continue
        if dvt not in (None, ""):
            it = {"stt": g("stt"), "ma": g("ma"), "ten": ten, "dvt": dvt, "kl": kl if isinstance(kl, (int, float)) else None,
                  "nguon_kl": "E-HSMT, %s, dòng %d" % (os.path.basename(duong_dan), r), "don_gia": None}
            if g("nguon"):
                it["nguon_kl"] = str(g("nguon"))
            out.append(it)
        else:
            out.append({"loai": "muc", "ten": ("%s %s" % (g("stt") or "", ten or "")).strip()})
    return out


def _cli():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="lenh", required=True)
    a = sp.add_parser("xuat")
    a.add_argument("json_vao")
    a.add_argument("xlsx_ra")
    b = sp.add_parser("boq")
    b.add_argument("xlsx_vao")
    b.add_argument("json_ra")
    b.add_argument("--sheet")
    b.add_argument("--dong-dau", type=int, default=2)
    b.add_argument("--cot", default="stt=A,ma=B,ten=C,dvt=D,kl=E")
    args = ap.parse_args()
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if args.lenh == "xuat":
        with open(args.json_vao, encoding="utf-8") as f:
            du_lieu = json.load(f)
        xuat(du_lieu, args.xlsx_ra)
        t = tinh(du_lieu)
        print("Đã xuất:", args.xlsx_ra)
        print("Số dòng: %d | thiếu đơn giá: %d | KL lỗi: %d" % (t["so_dong"], t["thieu_don_gia"], t["kl_loi"]))
        print("Giá dự thầu tính bằng Python: {:,.0f} đồng".format(t["gia_du_thau"]).replace(",", "."))
    else:
        if os.path.exists(args.json_ra):
            raise SystemExit("File đã có, không ghi đè: %s" % args.json_ra)
        cot = dict(p.split("=") for p in args.cot.split(","))
        boq = boq_tu_excel(args.xlsx_vao, args.sheet, args.dong_dau, cot)
        with open(args.json_ra, "w", encoding="utf-8") as f:
            json.dump({"boq": boq}, f, ensure_ascii=False, indent=1)
        n = sum(1 for x in boq if x.get("loai") != "muc")
        print("Đã đọc %d dòng (%d công việc) -> %s" % (len(boq), n, args.json_ra))


if __name__ == "__main__":
    _cli()
