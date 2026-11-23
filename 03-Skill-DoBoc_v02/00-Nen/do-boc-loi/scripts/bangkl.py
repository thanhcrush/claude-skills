# -*- coding: utf-8 -*-
"""
bangkl.py — Sổ khối lượng theo PL VI TT 13/2021/TT-BXD (Bảng 6.1 + 6.2), không phụ thuộc phần mềm dự toán.
Công ty TNHH Nghĩa Đạt — bộ skill đo bóc v02.

Một công trình = MỘT file Excel, gồm các sheet:
  00-ThongTin      thông tin chung, vật liệu, quy ước đo bóc đã chốt
  6.1-TongHop      bảng tổng hợp (công thức SUMIFS lấy từ mọi sheet 6.2-*)
  6.2-<HangMuc>    bảng chi tiết, mỗi hạng mục một sheet (6.2-02Coc, 6.2-03Mong, ...)
  TK-Thep          thống kê cốt thép từng thanh
  TK-Thep-TH       tổng hợp thép theo bộ phận × nhóm đường kính (công thức)
  TK-Cua           thống kê cửa
  CaiTao-Chuoi     chỉ dùng cho công trình cải tạo

CÁCH CHẠY (Windows, cửa sổ cmd hoặc PowerShell):
  1) Tạo file mẫu trống:
       python bangkl.py mau  "E:\\...\\assets\\Mau_BangKL_TT13_v01.xlsx"
  2) Cập nhật lại bảng 6.1 sau khi thêm/sửa sheet 6.2-*:
       python bangkl.py tonghop "E:\\...\\03-KhoiLuong\\<TenDuAn>_BangKL_v01.xlsx"
     (lệnh này GHI ĐÈ đúng file đó -> hãy chạy trên bản _v mới, không chạy trên bản đã chốt)
  3) Xuất sang phần mềm dự toán F1 (bố cục sheet "Công trình" của F1, đổi đơn vị đào/đắp/ván khuôn sang 100 m3/100 m2):
       python bangkl.py f1 "<sổ khối lượng>.xlsx" "<ra>_F1_v01.xlsx"
     (cần Excel trên máy để tính công thức; file ra là file MỚI, sổ gốc không bị sửa)
  4) Dùng trong Python (cho AI):
       import bangkl as B
       wb = B.tao_so({"Tên công trình": "...", "Hạng mục": "...", "Địa điểm": "..."})
       ws = B.them_sheet_62(wb, "03Mong", "MÓNG")
       B.ghi_cong_tac(ws, ma="", ten="Bê tông móng đá 1x2 mác 250", dv="m3", chi_tiet=[
           dict(vi_tri="Móng M1 trục A-1", kh_bv="KC-02", so_bp=4, dai=1.2, rong=1.2, cao=0.4,
                dien_giai="4 móng × 1,2 × 1,2 × 0,4 (MC 1-1 tờ KC-02)", tt="C"),
       ])
       B.cap_nhat_6_1(wb); wb.save(".._v01.xlsx")
"""
import sys, datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.worksheet.datavalidation import DataValidation

FONT = "Times New Roman"
CTY = "CÔNG TY TNHH NGHĨA ĐẠT"
F_N = Font(name=FONT, size=11)
F_B = Font(name=FONT, size=11, bold=True)
F_I = Font(name=FONT, size=10, italic=True, color="555555")
F_T = Font(name=FONT, size=14, bold=True)
F_RED = Font(name=FONT, size=11, color="C00000")
FILL_H = PatternFill("solid", fgColor="D9E1F2")
FILL_CT = PatternFill("solid", fgColor="F2F2F2")
FILL_T = PatternFill("solid", fgColor="FCE4D6")     # dòng tạm tính
FILL_IN = PatternFill("solid", fgColor="FFF2CC")    # ô chờ nhập
THIN = Side(style="thin", color="808080")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CEN = Alignment(horizontal="center", vertical="center", wrap_text=True)
NUM3 = "#,##0.000"
NUM2 = "#,##0.00"

# ---------------------------------------------------------------- 00-ThongTin
THONG_TIN = [
    ("CHUNG", None),
    ("Tên công trình", "[Chờ bổ sung]"), ("Hạng mục", "[Chờ bổ sung]"), ("Địa điểm", "[Chờ bổ sung]"),
    ("Chủ đầu tư", "[Chờ bổ sung]"), ("Đơn vị lập", "Công ty TNHH Nghĩa Đạt"), ("Ngày lập", None),
    ("Người lập", "[Chờ bổ sung]"),
    ("Người chủ trì (CCHN định giá XD số, hạng)", "[Chờ bổ sung]"),
    ("Bộ hồ sơ bản vẽ dùng (tên, revision, ngày)", "[Chờ bổ sung]"),
    ("QUY MÔ", None),
    ("Số tầng nổi (không gồm lửng, tum)", ""), ("Tầng hầm", ""), ("Tầng lửng", ""), ("Tum, mái", ""),
    ("Chiều cao từng tầng (m) — ghi theo mặt cắt", ""), ("Cốt nền ±0.000 so với cốt tự nhiên (m)", ""),
    ("Cốt đang dùng: kiến trúc hay kết cấu", ""), ("Diện tích xây dựng (m²)", ""),
    ("Tổng diện tích sàn (m²) — cách tính theo PL VI mục bóc theo diện tích", ""),
    ("KẾT CẤU", None),
    ("Loại móng", ""), ("Loại cọc, tiết diện, chiều dài thiết kế", ""), ("Hệ chịu lực", ""), ("Kết cấu mái", ""),
    ("VẬT LIỆU (đọc từ ghi chú chung, từng bộ phận)", None),
    ("Mác bê tông lót", ""), ("Mác bê tông móng, đài", ""), ("Mác bê tông cổ cột", ""),
    ("Mác bê tông giằng móng", ""), ("Mác bê tông cột, vách", ""), ("Mác bê tông dầm, sàn", ""),
    ("Mác bê tông cầu thang", ""), ("Mác bê tông lanh tô, ô văng", ""), ("Cỡ đá bê tông", ""),
    ("Loại thép Ø < 10", ""), ("Loại thép Ø ≥ 10", ""), ("Gạch xây (loại, kích thước)", ""),
    ("Mác vữa xây", ""), ("Mác vữa trát", ""),
    ("ĐỊA CHẤT, BIỆN PHÁP", None),
    ("Cấp đất đào (theo báo cáo khảo sát)", ""), ("Mực nước ngầm", ""),
    ("Mái dốc hố đào", "Mặc định: TCVN 4447:2012 Bảng 10 (đào thẳng) và Bảng 11 (hệ số mái) — xem skill boc-dao-dap"),
    ("Mở rộng đáy hố mỗi bên", "Mặc định 0,3 m từ mép ngoài lót; có người làm việc trong khe vách đứng 0,7 m (TCVN 4447:2012 đ.4.2.3)"),
    ("Tỷ lệ đào máy / đào thủ công", "Mặc định: máy đào đến lớp bảo vệ 0,10 m; lớp bảo vệ đào thủ công (TCVN 4447:2012 Bảng 13)"),
    ("Cự ly vận chuyển đất", "Mặc định tạm tính ≤ 1 km (T) khi chưa có bãi đổ"),
    ("Độ chặt đắp K", ""),
    ("QUY ƯỚC ĐO BÓC ĐÃ CHỐT", None),
    ("Căn cứ đo bóc", "Quy ước công ty kế thừa PL VI TT 13/2021 (hết hiệu lực 01/7/2026); tham khảo QĐ 1041/QĐ-BXD ngày 26/6/2026"),
    ("Định mức, giá xây dựng", "TT 38/2026/TT-BXD (định mức); TT 36, 37/2026/TT-BXD; giá Sở Xây dựng Quảng Trị — kiểm tra lại hiệu lực"),
    ("Giao cột – dầm – sàn", "Nút cột–dầm tính vào dầm; dầm, cột, vách nằm trong sàn tính vào sàn"),
    ("Nút giao khác mác bê tông", "Tính vào dầm, theo mác dầm (anh Thành chốt 09/10/2026)"),
    ("Cổ cột", "Áp định mức cột (bê tông, ván khuôn, cốt thép)"),
    ("Cửa", "Mua trọn bộ (gồm lắp đặt, phụ kiện) theo báo giá"),
    ("Dầm thang", "Tính vào công tác cầu thang"),
    ("Phần mềm dự toán", "F1"),
    ("Bộ định mức dùng trong F1", "[Chờ bổ sung] — TT 12/2021 hay TT 38/2026, hỏi anh Thành"),
    ("Giá nhân công", "GIẢ ĐỊNH: tạm dùng QĐ 16/QĐ-SXD ngày 12/01/2026 (vùng …) do chưa có giá theo TT 37/2026 — ghi chú trong thuyết minh"),
    ("Làm tròn", "3 số lẻ"),
]


def _hdr(ws, row, heads, widths=None):
    for j, h in enumerate(heads, 1):
        c = ws.cell(row, j, h); c.font = F_B; c.fill = FILL_H; c.alignment = CEN; c.border = BOX
    if widths:
        for j, w in enumerate(widths, 1):
            ws.column_dimensions[CL(j)].width = w


def _title(ws, tieu_de, ghi_chu, ncol):
    """Đầu bảng: tên công ty + tiêu đề + 4 dòng công trình/hạng mục/địa điểm/ngày lấy từ 00-ThongTin."""
    ws.cell(1, 1, CTY).font = F_B
    c = ws.cell(2, 1, tieu_de); c.font = F_T; c.alignment = Alignment(horizontal="center")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncol)
    ws.cell(3, 1, ghi_chu).font = F_I
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=ncol)
    for k, (nhan, ten) in enumerate([("Công trình: ", "Tên công trình"), ("Hạng mục: ", "Hạng mục"),
                                     ("Địa điểm: ", "Địa điểm"), ("Ngày lập: ", "Ngày lập")]):
        r = _tt_row(ten)
        ws.cell(4 + k, 1, f"=\"{nhan}\"&'00-ThongTin'!C{r}").font = F_N
        ws.merge_cells(start_row=4 + k, start_column=1, end_row=4 + k, end_column=ncol)
    ws.cell(8, 1, "Đơn vị lập: Công ty TNHH Nghĩa Đạt").font = F_N


def _tt_row(ten):
    r = 4
    for k, v in THONG_TIN:
        if k == ten: return r
        r += 1
    raise KeyError(ten)


def _sheet_thong_tin(wb, tt):
    ws = wb.active; ws.title = "00-ThongTin"
    ws.cell(1, 1, CTY).font = F_B
    ws.cell(2, 1, "THÔNG TIN CHUNG CÔNG TRÌNH VÀ QUY ƯỚC ĐO BÓC").font = F_T
    _hdr(ws, 3, ["STT", "Thông tin", "Giá trị", "Nguồn (tờ / trang / văn bản)", "Ghi chú"], [6, 46, 42, 32, 30])
    r, stt = 4, 0
    for k, v in THONG_TIN:
        if v is None and k != "Ngày lập":
            c = ws.cell(r, 2, k); c.font = F_B
            for j in range(1, 6): ws.cell(r, j).fill = FILL_CT; ws.cell(r, j).border = BOX
        else:
            stt += 1
            ws.cell(r, 1, stt).alignment = CEN
            ws.cell(r, 2, k)
            gt = tt.get(k, v)
            if k == "Ngày lập" and not gt:
                gt = datetime.date.today().strftime("%d/%m/%Y")
            c = ws.cell(r, 3, gt)
            if gt in ("", "[Chờ bổ sung]", "[Cần xác nhận lại]"): c.fill = FILL_IN
            for j in range(1, 6):
                ws.cell(r, j).border = BOX; ws.cell(r, j).alignment = WRAP
                if ws.cell(r, j).font != F_B: ws.cell(r, j).font = F_N
        r += 1
    ws.freeze_panes = "A4"
    return ws


# ---------------------------------------------------------------- 6.2 chi tiết
# Cột 1–10 đúng thứ tự Bảng 6.2 TT13; cột 11–15 là số liệu phụ trợ để công thức tự tính
C62 = ["STT", "Ký hiệu bản vẽ", "Mã hiệu định mức", "Danh mục công tác / vị trí", "Đơn vị",
       "Số bộ phận giống nhau", "Diễn giải tính toán", "KL một bộ phận", "KL toàn bộ", "Ghi chú",
       "Dài (m)", "Rộng (m)", "Cao / dày (m)", "Loại dòng", "Trạng thái"]
W62 = [6, 11, 13, 40, 7, 9, 44, 12, 13, 22, 9, 9, 9, 8, 8]
R62 = 11            # dòng dữ liệu đầu tiên
COL = {k: i + 1 for i, k in enumerate(["stt", "kh_bv", "ma", "ten", "dv", "so_bp", "dien_giai", "kl1",
                                       "kl", "ghi_chu", "dai", "rong", "cao", "loai", "tt"])}


def them_sheet_62(wb, ma_hm, ten_hm):
    """Thêm sheet 6.2-<ma_hm>, VD ma_hm='03Mong', ten_hm='MÓNG'."""
    ws = wb.create_sheet(f"6.2-{ma_hm}"[:31], index=len([s for s in wb.sheetnames if s.startswith(("00", "6."))]))
    _title(ws, f"BẢNG CHI TIẾT KHỐI LƯỢNG — {ten_hm}",
           "Mẫu Bảng 6.2 của công ty (theo mẫu PL VI TT 13/2021, bố cục tương thích F1). Cột (11)–(15) là số liệu phụ trợ để công thức tự tính.", 10)
    _hdr(ws, 9, C62, W62)
    for j in range(1, 16):
        c = ws.cell(10, j, f"({j})"); c.font = F_I; c.alignment = CEN; c.border = BOX
    ws.freeze_panes = ws.cell(R62, 5)
    ws.print_title_rows = "9:10"
    ws.page_setup.orientation = "landscape"; ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0; ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.oddFooter.center.text = "Trang &P / &N"
    dv = DataValidation(type="list", formula1='"HM,CT,CTiet,Tru"', allow_blank=True); ws.add_data_validation(dv)
    dv.add(f"N{R62}:N2000")
    dt = DataValidation(type="list", formula1='"C,S,T,N"', allow_blank=True); ws.add_data_validation(dt)
    dt.add(f"O{R62}:O2000")
    return ws


def _next_row(ws):
    r = R62
    while any(ws.cell(r, j).value not in (None, "") for j in (2, 4, 14)):
        r += 1
    return r


def ghi_hang_muc(ws, ten):
    """Dòng tiêu đề hạng mục con trong sheet (VD 'PHẦN BÊ TÔNG', 'TẦNG 2')."""
    r = _next_row(ws)
    ws.cell(r, 4, ten).font = F_B; ws.cell(r, COL["loai"], "HM")
    for j in range(1, 16): ws.cell(r, j).border = BOX; ws.cell(r, j).fill = FILL_H
    return r


def ghi_cong_tac(ws, ten, dv, chi_tiet, ma="", kh_bv="", ghi_chu=""):
    """Ghi 1 công tác + các dòng chi tiết. chi_tiet: list dict với các khóa
       vi_tri, kh_bv, so_bp, dai, rong, cao, kl1 (nhập thẳng nếu không có kích thước),
       dien_giai, tt (C/S/T/N), ghi_chu. Dòng trừ: so_bp âm. Dòng N: không có số, không cộng."""
    r0 = _next_row(ws)
    ws.cell(r0, COL["stt"], f'=IF(N{r0}="CT",COUNTIF($N${R62}:N{r0},"CT"),"")')
    ws.cell(r0, COL["kh_bv"], kh_bv)
    ws.cell(r0, COL["ma"], ma if ma else "[Chờ bổ sung]")
    ws.cell(r0, COL["ten"], ten); ws.cell(r0, COL["dv"], dv)
    ws.cell(r0, COL["ghi_chu"], ghi_chu); ws.cell(r0, COL["loai"], "CT")
    for j in range(1, 16):
        c = ws.cell(r0, j); c.font = F_B; c.fill = FILL_CT; c.border = BOX; c.alignment = WRAP
    if not ma: ws.cell(r0, COL["ma"]).fill = FILL_IN; ws.cell(r0, COL["ma"]).font = Font(name=FONT, size=10, italic=True)
    r = r0
    co_T = False
    for d in chi_tiet:
        r += 1
        tt = d.get("tt", "C")
        ws.cell(r, COL["stt"], "-").alignment = CEN
        ws.cell(r, COL["kh_bv"], d.get("kh_bv", ""))
        ws.cell(r, COL["ten"], d.get("vi_tri", ""))
        ws.cell(r, COL["dien_giai"], d.get("dien_giai", ""))
        ws.cell(r, COL["ghi_chu"], d.get("ghi_chu", ""))
        ws.cell(r, COL["loai"], "Tru" if (d.get("so_bp") or 0) < 0 else "CTiet")
        ws.cell(r, COL["tt"], tt)
        if tt != "N":
            ws.cell(r, COL["so_bp"], d.get("so_bp", 1))
            for k in ("dai", "rong", "cao"):
                if d.get(k) not in (None, ""): ws.cell(r, COL[k], d[k])
            if d.get("kl1") not in (None, ""):
                ws.cell(r, COL["kl1"], d["kl1"])
            else:
                ws.cell(r, COL["kl1"], f'=IF(COUNT(K{r}:M{r})=0,"",PRODUCT(K{r}:M{r}))')
            ws.cell(r, COL["kl"], f'=IF(OR(F{r}="",H{r}=""),"",ROUND(F{r}*H{r},3))')
        for j in range(1, 16):
            c = ws.cell(r, j); c.font = F_N; c.border = BOX; c.alignment = WRAP
        if tt == "T":
            co_T = True
            for j in range(1, 16): ws.cell(r, j).fill = FILL_T
        if tt == "N":
            for j in range(1, 16): ws.cell(r, j).font = F_RED
            ws.cell(r, COL["dien_giai"], (d.get("dien_giai", "") + " — CHƯA ĐỦ CƠ SỞ, không cộng").strip(" —"))
        for k in ("so_bp", "dai", "rong", "cao"):
            ws.cell(r, COL[k]).number_format = NUM3
        ws.cell(r, COL["kl1"]).number_format = NUM3; ws.cell(r, COL["kl"]).number_format = NUM3
    if r > r0:
        ws.cell(r0, COL["kl"], f"=ROUND(SUM(I{r0 + 1}:I{r}),3)")
    else:
        ws.cell(r0, COL["kl"], 0)
    ws.cell(r0, COL["kl"]).number_format = NUM3
    if co_T:
        ws.cell(r0, COL["tt"], "T"); ws.cell(r0, COL["ghi_chu"], (ghi_chu + " Có dòng tạm tính.").strip())
    return r0, r


def ghi_ky_ten(ws, r=None):
    r = (r or _next_row(ws)) + 1
    ws.cell(r, 4, "NGƯỜI LẬP").font = F_B; ws.cell(r, 7, "NGƯỜI CHỦ TRÌ").font = F_B
    ws.cell(r + 1, 4, "(Ký, họ tên)").font = F_I
    ws.cell(r + 1, 7, "(Ký, họ tên; CCHN định giá xây dựng số …, hạng …)").font = F_I
    ws.cell(r + 4, 4, "[Chờ bổ sung]").font = F_N; ws.cell(r + 4, 7, "[Chờ bổ sung]").font = F_N


# ---------------------------------------------------------------- 6.1 tổng hợp
C61 = ["STT", "Mã hiệu định mức", "Danh mục công tác", "Đơn vị", "Cách thức xác định", "Khối lượng", "Ghi chú"]


def _sheet_61(wb):
    ws = wb.create_sheet("6.1-TongHop", 1)
    _title(ws, "BẢNG TỔNG HỢP KHỐI LƯỢNG",
           "Mẫu Bảng 6.1 của công ty (theo mẫu PL VI TT 13/2021). Khối lượng là công thức lấy từ các sheet 6.2-*; chạy lại cap_nhat_6_1 khi thêm công tác.", 7)
    _hdr(ws, 9, C61, [6, 16, 52, 8, 22, 14, 30])
    for j in range(1, 8):
        c = ws.cell(10, j, f"({j})"); c.font = F_I; c.alignment = CEN; c.border = BOX
    ws.freeze_panes = "C11"; ws.print_title_rows = "9:10"
    ws.page_setup.orientation = "portrait"; ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0; ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.oddFooter.center.text = "Trang &P / &N"
    return ws


def cap_nhat_6_1(wb):
    """Dựng lại bảng 6.1 từ mọi dòng CT trong các sheet 6.2-*. Thứ tự = thứ tự sheet rồi thứ tự dòng.
       Cùng (mã, tên, đơn vị) ở nhiều chỗ thì gộp một dòng, khối lượng = tổng SUMIFS các sheet."""
    ws = wb["6.1-TongHop"]
    for row in ws.iter_rows(min_row=R62, max_row=max(ws.max_row, R62)):
        for c in row: c.value = None; c.fill = PatternFill(); c.border = Border()
    s62 = [s for s in wb.sheetnames if s.startswith("6.2-")]
    keys, info = [], {}
    for sn in s62:
        w = wb[sn]
        for r in range(R62, w.max_row + 1):
            if w.cell(r, COL["loai"]).value == "HM":
                keys.append(("HM", sn, w.cell(r, 4).value)); continue
            if w.cell(r, COL["loai"]).value != "CT": continue
            k = (w.cell(r, 3).value or "", w.cell(r, 4).value or "", w.cell(r, 5).value or "")
            if k not in info:
                keys.append(k); info[k] = {"T": False, "sheets": set()}
            info[k]["sheets"].add(sn)
            if w.cell(r, COL["tt"]).value == "T": info[k]["T"] = True
    r, stt = R62, 0
    for k in keys:
        if k[0] == "HM":
            ws.cell(r, 3, f"{k[2]}  ({k[1]})").font = F_B
            for j in range(1, 8): ws.cell(r, j).fill = FILL_H; ws.cell(r, j).border = BOX
            r += 1; continue
        stt += 1
        ma, ten, dv = k
        parts = [f"SUMIFS('{sn}'!$I:$I,'{sn}'!$C:$C,B{r},'{sn}'!$D:$D,C{r},'{sn}'!$E:$E,D{r},'{sn}'!$N:$N,\"CT\")"
                 for sn in s62 if sn in info[k]["sheets"]]
        vals = [stt, ma, ten, dv, "Tạm tính" if info[k]["T"] else "Bảng chi tiết",
                "=ROUND(" + "+".join(parts) + ",3)", ""]
        for j, v in enumerate(vals, 1):
            c = ws.cell(r, j, v); c.font = F_N; c.border = BOX; c.alignment = WRAP
        ws.cell(r, 6).number_format = NUM3
        if info[k]["T"]:
            for j in range(1, 8): ws.cell(r, j).fill = FILL_T
        r += 1
    ghi_ky_ten(ws, r)
    return ws


# ---------------------------------------------------------------- Thép, cửa, cải tạo
BO_PHAN_THEP = ["Cọc khoan nhồi", "Móng, đài", "Cổ cột", "Giằng móng, dầm móng", "Cột", "Vách", "Dầm",
                "Sàn", "Cầu thang", "Lanh tô, ô văng", "Bể, hố ga", "Khác"]


def _sheet_thep(wb):
    ws = wb.create_sheet("TK-Thep")
    _title(ws, "BẢNG THỐNG KÊ CỐT THÉP",
           "Mỗi dòng một số hiệu thanh. KL đơn vị = π/4 × Ø² × 7850 kg/m³ (theo đường kính danh nghĩa). Tính cả thép nối chồng, con kê, thép biện pháp (PL VI TT13).", 14)
    _hdr(ws, 9, ["STT", "Bộ phận", "Cấu kiện (tên, tầng, trục)", "Số hiệu thanh", "Ø (mm)", "Dài 1 thanh (m)",
                 "Số thanh / 1 CK", "Số cấu kiện", "Tổng số thanh", "Tổng dài (m)", "KL đơn vị (kg/m)",
                 "Tổng KL (kg)", "Nguồn (tờ, bảng)", "Ghi chú"], [6, 18, 30, 9, 7, 10, 10, 9, 10, 11, 10, 12, 22, 22])
    dv = DataValidation(type="list", formula1='"' + ",".join(BO_PHAN_THEP) + '"', allow_blank=True)
    ws.add_data_validation(dv); dv.add("B11:B3000")
    for r in range(R62, R62 + 300):
        ws.cell(r, 1, f'=IF(C{r}="","",ROW()-{R62 - 1})')
        ws.cell(r, 9, f'=IF(OR(G{r}="",H{r}=""),"",G{r}*H{r})')
        ws.cell(r, 10, f'=IF(OR(F{r}="",I{r}=""),"",ROUND(F{r}*I{r},2))')
        ws.cell(r, 11, f'=IF(E{r}="","",ROUND(PI()/4*E{r}^2*7850/1000000,3))')
        ws.cell(r, 12, f'=IF(OR(J{r}="",K{r}=""),"",ROUND(J{r}*K{r},2))')
        for j in range(1, 15): ws.cell(r, j).border = BOX; ws.cell(r, j).font = F_N
        for j in (6, 10, 12): ws.cell(r, j).number_format = NUM2
        ws.cell(r, 11).number_format = NUM3
    ws.freeze_panes = "D11"; ws.print_title_rows = "9:9"

    th = wb.create_sheet("TK-Thep-TH")
    _title(th, "TỔNG HỢP CỐT THÉP THEO BỘ PHẬN VÀ NHÓM ĐƯỜNG KÍNH",
           "Ranh nhóm đường kính ở ô C9, D9: 10 và 18 mm (anh Thành chốt 09/10/2026). Sửa ô C9, D9 nếu dự án quy định khác.", 7)
    th.cell(9, 2, "Ranh nhóm Ø (mm):").font = F_B
    th.cell(9, 3, 10).fill = FILL_IN; th.cell(9, 4, 18).fill = FILL_IN
    _hdr_row = 10
    heads = ["STT", "Bộ phận", '="Ø ≤ "&C9&" (kg)"', '=C9&" < Ø ≤ "&D9&" (kg)"', '="Ø > "&D9&" (kg)"', "Tổng (kg)", "Tổng (tấn)"]
    _hdr(th, _hdr_row, heads, [6, 26, 14, 14, 14, 14, 12])
    S = "'TK-Thep'!"
    for i, bp in enumerate(BO_PHAN_THEP):
        r = _hdr_row + 1 + i
        th.cell(r, 1, i + 1); th.cell(r, 2, bp)
        th.cell(r, 3, f'=SUMIFS({S}$L:$L,{S}$B:$B,B{r},{S}$E:$E,"<="&$C$9)')
        th.cell(r, 4, f'=SUMIFS({S}$L:$L,{S}$B:$B,B{r},{S}$E:$E,">"&$C$9,{S}$E:$E,"<="&$D$9)')
        th.cell(r, 5, f'=SUMIFS({S}$L:$L,{S}$B:$B,B{r},{S}$E:$E,">"&$D$9)')
        th.cell(r, 6, f"=SUM(C{r}:E{r})"); th.cell(r, 7, f"=ROUND(F{r}/1000,3)")
        for j in range(1, 8): th.cell(r, j).border = BOX; th.cell(r, j).font = F_N
        for j in range(3, 7): th.cell(r, j).number_format = NUM2
        th.cell(r, 7).number_format = NUM3
    r = _hdr_row + 1 + len(BO_PHAN_THEP)
    th.cell(r, 2, "CỘNG").font = F_B
    for j in range(3, 8):
        th.cell(r, j, f"=SUM({CL(j)}{_hdr_row + 1}:{CL(j)}{r - 1})").font = F_B
        th.cell(r, j).number_format = NUM3 if j == 7 else NUM2
    th.cell(r + 1, 2, "Kiểm: tổng TK-Thep (kg)").font = F_I
    th.cell(r + 1, 6, f"=SUM({S}L:L)").number_format = NUM2
    th.cell(r + 2, 2, "Lệch (phải = 0; khác 0 là có dòng thiếu bộ phận)").font = F_I
    th.cell(r + 2, 6, f"=F{r + 1}-F{r}").number_format = NUM2


def cong_thuc_thep(bo_phan, nhom):
    """Công thức (tấn) trỏ sang TK-Thep-TH, dùng làm kl1 của dòng chi tiết công tác cốt thép.
       nhom: 1 = Ø ≤ ranh 1; 2 = giữa hai ranh; 3 = Ø > ranh 2; 0 = tổng bộ phận."""
    r = 11 + BO_PHAN_THEP.index(bo_phan)
    col = {1: "C", 2: "D", 3: "E", 0: "F"}[nhom]
    return f"=ROUND('TK-Thep-TH'!{col}{r}/1000,3)"


def _sheet_cua(wb):
    ws = wb.create_sheet("TK-Cua")
    _title(ws, "BẢNG THỐNG KÊ CỬA", "Kích thước lỗ mở theo bảng cửa / mặt đứng; vị trí ghi đúng tường mẹ (tầng – trục – nhịp).", 12)
    _hdr(ws, 9, ["STT", "Ký hiệu cửa", "Loại (cửa đi / cửa sổ / vách kính / cổng)", "Vật liệu khung, cánh",
                 "Rộng B (m)", "Cao H (m)", "Số lượng", "Diện tích 1 bộ (m²)", "Tổng diện tích (m²)",
                 "Vị trí (tầng – trục – nhịp)", "Nguồn", "Ghi chú"], [6, 11, 22, 24, 9, 9, 8, 11, 12, 30, 18, 20])
    for r in range(R62, R62 + 150):
        ws.cell(r, 1, f'=IF(B{r}="","",ROW()-{R62 - 1})')
        ws.cell(r, 8, f'=IF(OR(E{r}="",F{r}=""),"",ROUND(E{r}*F{r},3))')
        ws.cell(r, 9, f'=IF(OR(G{r}="",H{r}=""),"",ROUND(G{r}*H{r},3))')
        for j in range(1, 13): ws.cell(r, j).border = BOX; ws.cell(r, j).font = F_N
        for j in (5, 6, 8, 9): ws.cell(r, j).number_format = NUM3
    ws.freeze_panes = "C11"


def _sheet_cai_tao(wb):
    ws = wb.create_sheet("CaiTao-Chuoi")
    _title(ws, "CHUỖI CÔNG VIỆC CẢI TẠO — BẢNG CHỐNG SÓT",
           "Mỗi dòng một tầng / khu vực. Ô trống phải có lý do. Hiện trạng: GIỮ LẠI / THÁO DỠ / XÂY MỚI / TẠM TÍNH.", 14)
    _hdr(ws, 9, ["STT", "Tầng / khu vực", "Hiện trạng", "Bảo vệ, che chắn", "Tháo dỡ", "Vận chuyển phế thải",
                 "Gia cố, kết nối", "Thi công mới", "Điện nước", "Hoàn trả", "Vệ sinh, bàn giao", "Nguồn",
                 "Trạng thái", "Ghi chú"], [6, 22, 12] + [16] * 8 + [16, 9, 22])
    dv = DataValidation(type="list", formula1='"GIỮ LẠI,THÁO DỠ,XÂY MỚI,TẠM TÍNH"', allow_blank=True)
    ws.add_data_validation(dv); dv.add("C11:C500")
    for r in range(R62, R62 + 60):
        ws.cell(r, 1, f'=IF(B{r}="","",ROW()-{R62 - 1})')
        for j in range(1, 15): ws.cell(r, j).border = BOX; ws.cell(r, j).font = F_N; ws.cell(r, j).alignment = WRAP


def tao_so(thong_tin=None, cai_tao=False):
    """Tạo workbook rỗng của một công trình."""
    wb = Workbook()
    _sheet_thong_tin(wb, thong_tin or {})
    _sheet_61(wb)
    _sheet_thep(wb)
    _sheet_cua(wb)
    if cai_tao: _sheet_cai_tao(wb)
    return wb


def tao_mau(path):
    """File mẫu có 1 sheet 6.2 ví dụ (chữ VÍ DỤ — xóa khi dùng thật)."""
    wb = tao_so(cai_tao=True)
    ws = them_sheet_62(wb, "ViDu", "VÍ DỤ CÁCH GHI — XÓA SHEET NÀY KHI DÙNG")
    ghi_hang_muc(ws, "VÍ DỤ — PHẦN THÂN, TẦNG 2")
    ghi_cong_tac(ws, "VÍ DỤ: Xây tường gạch đặc 6,5x10,5x22, dày 220, vữa M75", "m³", [
        dict(vi_tri="Tường trục A(1-2)", kh_bv="KT-03", so_bp=1, dai=4.2, rong=0.22, cao=3.15,
             dien_giai="Mép cột–mép cột 4,2 × dày 0,22 × (cao tầng 3,6 − dầm 0,45)", tt="C"),
        dict(vi_tri="Trừ cửa sổ S1 trục A(1-2)", kh_bv="KT-03", so_bp=-2, dai=1.2, rong=0.22, cao=1.5,
             dien_giai="2 cửa × 1,2 × 0,22 × 1,5 (bảng cửa KT-10)", tt="C"),
        dict(vi_tri="Trừ lanh tô trên S1", kh_bv="KT-11", so_bp=-2, dai=1.6, rong=0.22, cao=0.1,
             dien_giai="2 × (1,2 + 2 gối 0,2) × 0,22 × 0,1 — gối chưa có chi tiết", tt="T"),
    ])
    ghi_cong_tac(ws, "VÍ DỤ: Bê tông dầm đá 1x2 mác 250", "m³", [
        dict(vi_tri="Dầm D1 trục 1(A-C), thông thủy mép cột", kh_bv="KC-05", so_bp=1, dai=7.6, rong=0.22, cao=0.33,
             dien_giai="L thông thủy 7,6 × b 0,22 × (H 0,45 − sàn 0,12)", tt="C"),
        dict(vi_tri="Nút giao cột C1 tại trục A-1 (tính vào dầm)", kh_bv="KC-05", so_bp=1, dai=0.22, rong=0.3, cao=0.33,
             dien_giai="Tiết diện cột 0,22 × 0,3 × (H dầm lớn nhất 0,45 − sàn 0,12)", tt="C"),
        dict(vi_tri="Dầm D7 ban công — chưa có mặt cắt", kh_bv="KC-05", so_bp=1,
             dien_giai="Thiếu tiết diện, đã đưa vào DS cần kiểm", tt="N"),
    ])
    cap_nhat_6_1(wb)
    wb.save(path)
    return path


# ---------------------------------------------------------------- Xuất sang phần mềm dự toán F1
# Bố cục lấy theo sheet "Công trình" của file F1 mẫu (03-MauBieu\02-DuToan\DT HANG RAO NHA VAN HOA.xls):
# dòng công tác (STT, Ký hiệu BV, Mã hiệu, Tên, Đơn vị, KL toàn bộ = ROUND(SUM(dòng dưới),3))
# + dòng diễn giải "vị trí: diễn giải = kết quả" có số ở cột KL một bộ phận.
# Đơn vị quy đổi mặc định theo đơn vị định mức (đào, đắp: 100m3; ván khuôn: 100m2) — KIỂM LẠI trong F1 sau khi nhập.
QUY_DOI_F1 = [(("Đào", "Đắp"), ("m³", "m3"), "100m3", 100),
              (("Ván khuôn",), ("m²", "m2"), "100m2", 100)]


def _so(x, nd=4):
    s = f"{x:,.{nd}f}".rstrip("0").rstrip(".")
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _doc_gia_tri(path):
    """Đọc sổ với giá trị đã tính. Sổ do openpyxl tạo chưa có giá trị cache → cho Excel tính lại trên bản sao tạm."""
    import os, shutil, tempfile
    wb = load_workbook(path, data_only=True)
    can_tinh = any(ws.cell(r, COL["kl"]).value is None
                   for ws in wb.worksheets if ws.title.startswith("6.2-")
                   for r in range(R62, ws.max_row + 1) if ws.cell(r, COL["loai"]).value == "CT")
    if not can_tinh:
        return wb
    import win32com.client as W
    tmp = os.path.join(tempfile.mkdtemp(), "tam.xlsx"); shutil.copy(path, tmp)
    xl = W.DispatchEx("Excel.Application"); xl.Visible = False; xl.DisplayAlerts = False
    try:
        b = xl.Workbooks.Open(tmp); xl.CalculateFull(); b.Save(); b.Close(False)
    finally:
        xl.Quit()
    return load_workbook(tmp, data_only=True)


def xuat_f1(so_kl, ra, quy_doi=None):
    """Xuất các sheet 6.2-* của sổ khối lượng `so_kl` thành file Excel bố cục F1 (`ra`).
       quy_doi: {tên công tác: (đơn vị F1, hệ số)} để đè quy tắc mặc định.
       Trả về danh sách công tác còn thiếu mã hiệu."""
    v = _doc_gia_tri(so_kl)
    f = load_workbook(so_kl)                       # để lấy diễn giải gốc
    out = Workbook(); ws = out.active; ws.title = "Công trình"
    tt = v["00-ThongTin"]
    ws["A1"] = "BẢNG CHI TIẾT KHỐI LƯỢNG CÔNG TÁC XÂY DỰNG"; ws["A1"].font = F_T
    ws["A3"] = "Công trình: " + str(tt.cell(_tt_row("Tên công trình"), 3).value or "")
    ws["A4"] = "HẠNG MỤC: " + str(tt.cell(_tt_row("Hạng mục"), 3).value or "")
    heads = ["STT", "Ký hiệu bản vẽ", "Mã hiệu công tác", "Danh mục công tác", "Đơn vị",
             "Khối lượng một bộ phận", "Khối lượng toàn bộ"]
    _hdr(ws, 5, heads, [6, 12, 14, 70, 9, 14, 14])
    r, stt, thieu_ma = 7, 0, []
    for sn in [s for s in v.sheetnames if s.startswith("6.2-")]:
        sv, sf = v[sn], f[sn]
        rr = R62
        while rr <= sv.max_row:
            if sv.cell(rr, COL["loai"]).value != "CT":
                rr += 1; continue
            ma = sv.cell(rr, COL["ma"]).value or ""
            ten = sv.cell(rr, COL["ten"]).value or ""; dv = sv.cell(rr, COL["dv"]).value or ""
            dv_f1, hs = dv, 1
            for tien_to, dv_goc, d1, h in QUY_DOI_F1:
                if ten.startswith(tien_to) and dv in dv_goc: dv_f1, hs = d1, h
            if quy_doi and ten in quy_doi: dv_f1, hs = quy_doi[ten]
            dv_f1 = dv_f1.replace("³", "3").replace("²", "2")      # F1 ghi m3, m2, 100m3
            if not ma or ma.startswith("["): thieu_ma.append(ten); ma = ""
            stt += 1; r0 = r
            for j, val in enumerate([stt, sv.cell(rr, COL["kh_bv"]).value, ma, ten, dv_f1], 1):
                ws.cell(r, j, val).font = F_B
            r += 1; rr += 1
            while rr <= sv.max_row and sv.cell(rr, COL["loai"]).value in ("CTiet", "Tru"):
                kl = sv.cell(rr, COL["kl"]).value
                if isinstance(kl, (int, float)):
                    gt = round(kl / hs, 4)
                    dg = sf.cell(rr, COL["dien_giai"]).value or ""
                    txt = f"{sf.cell(rr, COL['ten']).value or ''}: {dg}"
                    if hs != 1: txt += f" — quy đổi ÷{hs}"
                    ws.cell(r, 2, sf.cell(rr, COL["kh_bv"]).value)
                    ws.cell(r, 4, f"{txt} = {_so(gt)}").font = F_N
                    c = ws.cell(r, 6, gt); c.number_format = "#,##0.0000"
                    r += 1
                rr += 1
            c = ws.cell(r0, 7, f"=ROUND(SUM(F{r0 + 1}:F{max(r - 1, r0 + 1)}),3)")
            c.font = F_B; c.number_format = "#,##0.000"
    ws.cell(r, 3, "THM"); ws.cell(r, 4, "TỔNG HẠNG MỤC").font = F_B
    ws.freeze_panes = "A7"
    out.save(ra)
    return thieu_ma


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("mau", "tonghop", "f1"):
        print(__doc__); sys.exit(1)
    if sys.argv[1] == "mau":
        print("Đã tạo:", tao_mau(sys.argv[2]))
    elif sys.argv[1] == "f1":
        thieu = xuat_f1(sys.argv[2], sys.argv[3])
        print("Đã xuất bố cục F1:", sys.argv[3])
        if thieu: print("Công tác chưa có mã hiệu (F1 cần mã để áp giá):", *thieu, sep="\n  - ")
    else:
        wb = load_workbook(sys.argv[2]); cap_nhat_6_1(wb); wb.save(sys.argv[2])
        print("Đã cập nhật 6.1-TongHop:", sys.argv[2])
