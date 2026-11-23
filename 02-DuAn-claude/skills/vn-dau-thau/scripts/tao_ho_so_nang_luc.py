# -*- coding: utf-8 -*-
"""
Tạo file Excel HỒ SƠ NĂNG LỰC CÔNG TY (mẫu trống) để anh Thành điền một lần, dùng cho mọi gói thầu.
Agent đấu thầu đọc file này để đối chiếu với yêu cầu E-HSMT.

Cách chạy:
    python tao_ho_so_nang_luc.py <file_ra.xlsx>

Các sheet: 1-ThongTinChung, 2-NhanSu, 3-ThietBi, 4-HopDong, 5-TaiChinh.
Cột "Còn hạn" và các chỉ tiêu tài chính là công thức. Script từ chối ghi đè file đã có.
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

FONT = "Times New Roman"
mong = Side(style="thin", color="000000")
KHUNG = Border(left=mong, right=mong, top=mong, bottom=mong)
NEN_TD = PatternFill("solid", fgColor="D9E1F2")
DO = PatternFill("solid", fgColor="FFC7CE")
VANG = PatternFill("solid", fgColor="FFEB9C")
SO_DONG = 30


def f(bold=False, size=12, italic=False):
    return Font(name=FONT, bold=bold, size=size, italic=italic)


def tieu_de(ws, ten, so_cot):
    cuoi = get_column_letter(so_cot)
    for i, (txt, font) in enumerate([("CÔNG TY TNHH NGHĨA ĐẠT", f(True)), (ten, f(True, 14)),
                                     ("Cập nhật mỗi khi có chứng chỉ, hợp đồng, báo cáo tài chính mới. "
                                      "Cột có công thức: không gõ đè.", f(italic=True, size=11))], 1):
        ws.merge_cells(f"A{i}:{cuoi}{i}")
        ws[f"A{i}"].value, ws[f"A{i}"].font = txt, font
        ws[f"A{i}"].alignment = Alignment(horizontal="center" if i == 2 else "left")
    return 5


def bang(ws, ten, cot, cong_thuc=None, dinh_dang=None):
    """cot: [(tên, rộng)]; cong_thuc: {chỉ số cột: hàm(r) -> chuỗi}; dinh_dang: {chỉ số cột: fmt}."""
    r0 = tieu_de(ws, ten, len(cot))
    for j, (t, w) in enumerate(cot, 1):
        c = ws.cell(r0, j, t)
        c.font, c.fill, c.border = f(True), NEN_TD, KHUNG
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.row_dimensions[r0].height = 45
    ws.freeze_panes = ws.cell(r0 + 1, 3)
    for i in range(1, SO_DONG + 1):
        r = r0 + i
        for j in range(1, len(cot) + 1):
            c = ws.cell(r, j)
            c.font, c.border = f(), KHUNG
            c.alignment = Alignment(vertical="top", wrap_text=True)
            if j == 1:
                c.value = i
                c.alignment = Alignment(horizontal="center", vertical="top")
            if cong_thuc and j in cong_thuc:
                c.value = cong_thuc[j](r)
            if dinh_dang and j in dinh_dang:
                c.number_format = dinh_dang[j]
    return r0 + 1, r0 + SO_DONG


def canh_bao_het_han(ws, vung, cot_con):
    a = int("".join(ch for ch in vung.split(":")[0] if ch.isdigit()))
    ws.conditional_formatting.add(vung, FormulaRule(formula=[f'${cot_con}{a}="HẾT HẠN"'], fill=DO))
    ws.conditional_formatting.add(vung, FormulaRule(formula=[f'LEFT(${cot_con}{a},4)="Còn "'], fill=VANG))


def con_han(cot_ngay):
    return lambda r: (f'=IF({cot_ngay}{r}="","",IF({cot_ngay}{r}<TODAY(),"HẾT HẠN",'
                      f'IF({cot_ngay}{r}-TODAY()<=90,"Còn "&({cot_ngay}{r}-TODAY())&" ngày","Còn hạn")))')


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    dich = sys.argv[1]
    if os.path.exists(dich):
        sys.exit(f"LỖI: {dich} đã tồn tại. Không ghi đè.")
    wb = Workbook()

    # 1. Thông tin chung
    ws = wb.active
    ws.title = "1-ThongTinChung"
    r0 = tieu_de(ws, "THÔNG TIN CHUNG VÀ GIẤY TỜ PHÁP LÝ", 4)
    for j, (t, w) in enumerate([("Nội dung", 42), ("Giá trị", 45), ("Hết hạn", 13), ("Còn hạn", 16)], 1):
        c = ws.cell(r0, j, t)
        c.font, c.fill, c.border = f(True), NEN_TD, KHUNG
        c.alignment = Alignment(horizontal="center")
        ws.column_dimensions[get_column_letter(j)].width = w
    muc = ["Tên doanh nghiệp", "Mã số doanh nghiệp (MST)", "Địa chỉ trụ sở", "Điện thoại, email",
           "Người đại diện theo pháp luật, chức vụ", "Tài khoản ngân hàng", "Năm thành lập",
           "Chứng chỉ năng lực HĐXD: số, cơ quan cấp", "Chứng chỉ năng lực: lĩnh vực và hạng",
           "Chứng thư số (ký E-HSDT): nhà cung cấp", "Tài khoản nhà thầu trên Hệ thống mạng đấu thầu quốc gia",
           "Tình trạng kê khai, nộp thuế (năm gần nhất)", "Báo cáo tài chính đã nộp lên hệ thống (các năm)",
           "Ngành nghề đăng ký kinh doanh liên quan xây dựng"]
    for i, m in enumerate(muc, 1):
        r = r0 + i
        for j in range(1, 5):
            ws.cell(r, j).border, ws.cell(r, j).font = KHUNG, f(j == 1)
            ws.cell(r, j).alignment = Alignment(vertical="top", wrap_text=True)
        ws.cell(r, 1, m)
        ws.cell(r, 3).number_format = "dd/mm/yyyy"
        ws.cell(r, 4, con_han("C")(r))
    ws.cell(r0 + 1, 2, "Công ty TNHH Nghĩa Đạt")
    canh_bao_het_han(ws, f"A{r0 + 1}:D{r0 + len(muc)}", "D")

    # 2. Nhân sự
    ws = wb.create_sheet("2-NhanSu")
    a, b = bang(ws, "NHÂN SỰ CHỦ CHỐT", [
        ("STT", 5), ("Họ và tên", 22), ("Vị trí có thể đảm nhận (chỉ huy trưởng, cán bộ kỹ thuật, ATLĐ...)", 26),
        ("Trình độ, chuyên ngành", 20), ("Số năm KN", 8), ("Số CCHN", 14), ("Lĩnh vực CCHN", 22),
        ("Hạng", 7), ("CCHN hết hạn", 12), ("Còn hạn", 14), ("Hợp đồng LĐ / BHXH với công ty", 14),
        ("Đang huy động cho gói thầu, công trình", 26), ("File chứng minh (đường dẫn)", 30)],
        cong_thuc={10: con_han("I")}, dinh_dang={9: "dd/mm/yyyy"})
    canh_bao_het_han(ws, f"A{a}:M{b}", "J")

    # 3. Thiết bị
    ws = wb.create_sheet("3-ThietBi")
    a, b = bang(ws, "THIẾT BỊ THI CÔNG CHỦ YẾU", [
        ("STT", 5), ("Tên thiết bị", 26), ("Mã hiệu, công suất", 20), ("Số lượng", 9),
        ("Sở hữu / Đi thuê", 12), ("Đơn vị cho thuê, số HĐ thuê", 24), ("Kiểm định đến ngày", 12),
        ("Còn hạn", 14), ("Đang huy động cho", 22), ("File chứng minh", 30)],
        cong_thuc={8: con_han("G")}, dinh_dang={7: "dd/mm/yyyy"})
    dv = DataValidation(type="list", formula1='"Sở hữu,Đi thuê"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"E{a}:E{b}")
    canh_bao_het_han(ws, f"A{a}:J{b}", "H")

    # 4. Hợp đồng đã và đang thực hiện
    ws = wb.create_sheet("4-HopDong")
    a, b = bang(ws, "HỢP ĐỒNG ĐÃ VÀ ĐANG THỰC HIỆN (dùng chứng minh hợp đồng tương tự)", [
        ("STT", 5), ("Tên hợp đồng / công trình", 32), ("Chủ đầu tư", 22), ("Loại công trình", 16),
        ("Cấp công trình", 9), ("Giá trị HĐ (đồng)", 16), ("Giá trị phần công ty thực hiện (đồng)", 16),
        ("Vai trò (độc lập, liên danh, thầu phụ)", 14), ("Ngày ký", 11), ("Ngày hoàn thành", 11),
        ("Tình trạng", 13), ("Có BB nghiệm thu, thanh lý", 11), ("Địa điểm", 16), ("File chứng minh", 30)],
        dinh_dang={6: "#,##0", 7: "#,##0", 9: "dd/mm/yyyy", 10: "dd/mm/yyyy"})
    dv = DataValidation(type="list", formula1='"Đã hoàn thành,Đang thực hiện"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"K{a}:K{b}")

    # 5. Tài chính
    ws = wb.create_sheet("5-TaiChinh")
    r0 = tieu_de(ws, "SỐ LIỆU TÀI CHÍNH (theo báo cáo tài chính đã kiểm toán hoặc đã nộp thuế)", 6)
    hd = ["Chỉ tiêu (đồng)", "Năm N-3", "Năm N-2", "Năm N-1", "Bình quân", "Ghi chú"]
    for j, t in enumerate(hd, 1):
        c = ws.cell(r0, j, t)
        c.font, c.fill, c.border = f(True), NEN_TD, KHUNG
        c.alignment = Alignment(horizontal="center")
        ws.column_dimensions[get_column_letter(j)].width = [44, 17, 17, 17, 17, 40][j - 1]
    chi_tieu = ["Năm tài chính (ghi số năm)", "Tổng tài sản", "Tổng nợ phải trả", "Tài sản ngắn hạn",
                "Nợ ngắn hạn", "Doanh thu", "Doanh thu từ hoạt động xây dựng", "Lợi nhuận trước thuế",
                "Lợi nhuận sau thuế"]
    for i, ct in enumerate(chi_tieu, 1):
        r = r0 + i
        ws.cell(r, 1, ct)
        for j in range(1, 7):
            ws.cell(r, j).border, ws.cell(r, j).font = KHUNG, f(j == 1)
            if 2 <= j <= 5 and i > 1:
                ws.cell(r, j).number_format = "#,##0"
        if i > 1:
            ws.cell(r, 5, f'=IF(COUNT(B{r}:D{r})=0,"",AVERAGE(B{r}:D{r}))')
    ts, no, tsnh, nnh, dt, dtxd = (r0 + k for k in (2, 3, 4, 5, 6, 7))
    tinh = [
        ("Giá trị tài sản ròng = Tổng tài sản − Tổng nợ", lambda c: f'=IF({c}{ts}="","",{c}{ts}-{c}{no})',
         "#,##0", "Thường E-HSMT yêu cầu > 0 năm gần nhất"),
        ("Hệ số thanh toán hiện hành = TS ngắn hạn / Nợ ngắn hạn",
         lambda c: f'=IF(OR({c}{tsnh}="",{c}{nnh}="",{c}{nnh}=0),"",{c}{tsnh}/{c}{nnh})', "0.00", ""),
        ("Tỷ lệ doanh thu xây dựng / doanh thu",
         lambda c: f'=IF(OR({c}{dt}="",{c}{dt}=0,{c}{dtxd}=""),"",{c}{dtxd}/{c}{dt})', "0.0%", ""),
    ]
    r = r0 + len(chi_tieu)
    for ten, ham, fmt, gc in tinh:
        r += 1
        ws.cell(r, 1, ten).font = f(True)
        for j, c in zip((2, 3, 4), "BCD"):
            x = ws.cell(r, j, ham(c))
            x.number_format, x.font = fmt, f()
        for j in range(1, 7):
            ws.cell(r, j).border = KHUNG
        ws.cell(r, 6, gc).font = f(italic=True, size=11)
    r += 2
    ws.cell(r, 1, "Doanh thu bình quân dùng đối chiếu yêu cầu E-HSMT: xem cột Bình quân, dòng Doanh thu "
                  "(hoặc Doanh thu xây dựng, tùy E-HSMT quy định). Số năm lấy bình quân theo đúng E-HSMT.").font = f(italic=True, size=11)

    for ws in wb.worksheets:
        ws.page_setup.orientation = "landscape"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    os.makedirs(os.path.dirname(os.path.abspath(dich)), exist_ok=True)
    wb.save(dich)
    print(f"Đã tạo: {os.path.abspath(dich)}")


if __name__ == "__main__":
    main()
