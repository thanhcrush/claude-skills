# -*- coding: utf-8 -*-
"""
Sinh file Excel PHÂN TÍCH HỒ SƠ MỜI THẦU từ dữ liệu JSON (agent đọc E-HSMT rồi ghi JSON).

Cách chạy:
    python phan_tich_hsmt.py <du_lieu.json> <file_ra.xlsx>

Các sheet (đều giữ công thức, sửa tay được):
  1-TongQuan      thông tin gói thầu, mốc thời gian, đếm trạng thái yêu cầu, điểm Go/No-go, kết luận
  2-YeuCau-DapUng từng yêu cầu của E-HSMT, trích dẫn, năng lực công ty đáp ứng, trạng thái, việc cần làm
  3-GoNoGo        chấm điểm có trọng số quyết định có dự thầu hay không
  4-KeHoach       việc cần làm, hạn tính lùi từ thời điểm đóng thầu
  5-DanhMucNop    danh mục tài liệu phải nộp
  6-LamRo         câu hỏi đề nghị làm rõ E-HSMT

Cấu trúc JSON: xem references/phan_tich_mau.json. Script từ chối ghi đè file đã có.
"""
import json
import os
import sys
from datetime import datetime

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

FONT = "Times New Roman"
CONG_TY = "CÔNG TY TNHH NGHĨA ĐẠT"
TRANG_THAI = ["ĐẠT", "CẦN BỔ SUNG", "CHƯA RÕ", "CHƯA ĐẠT"]
TIEN_DO = ["Chưa làm", "Đang làm", "Xong"]
MAU = {"ĐẠT": "C6EFCE", "CẦN BỔ SUNG": "FFEB9C", "CHƯA RÕ": "DDEBF7", "CHƯA ĐẠT": "FFC7CE"}

GO_NO_GO_MAC_DINH = [
    ("Tư cách hợp lệ, chứng chỉ năng lực hoạt động xây dựng đúng loại và hạng", 15),
    ("Hợp đồng tương tự (số lượng, loại, cấp công trình, giá trị)", 20),
    ("Năng lực tài chính: doanh thu bình quân, tình hình tài chính, nguồn lực tài chính", 15),
    ("Nhân sự chủ chốt và thiết bị chủ yếu (có chứng chỉ, không trùng gói khác)", 15),
    ("Khả năng cạnh tranh về giá, biên lợi nhuận dự kiến", 15),
    ("Địa bàn, khả năng huy động tổ đội, vật tư tại chỗ", 10),
    ("Đủ thời gian lập HSDT chất lượng trước khi đóng thầu", 5),
    ("Rủi ro hợp đồng: tạm ứng, thanh toán, phạt, bảo hành, bảo lãnh", 5),
]

mong = Side(style="thin", color="000000")
KHUNG = Border(left=mong, right=mong, top=mong, bottom=mong)
NEN_TD = PatternFill("solid", fgColor="D9E1F2")


def f(bold=False, italic=False, size=12, color=None):
    return Font(name=FONT, bold=bold, italic=italic, size=size, color=color)


def ngay(s):
    if not s:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(s), fmt)
        except ValueError:
            pass
    raise ValueError(f"Ngày sai định dạng (cần YYYY-MM-DD hoặc YYYY-MM-DD HH:MM): {s}")


def tieu_de(ws, d, ten_bang, so_cot):
    """Khối tiêu đề theo CLAUDE.md: đơn vị lập, tên bảng, công trình, hạng mục, địa điểm, ngày lập."""
    cuoi = get_column_letter(so_cot)
    dong = [
        (CONG_TY, f(True, size=12), "left"),
        (ten_bang, f(True, size=14), "center"),
        (f"Công trình: {d.get('cong_trinh', '')}", f(size=12), "left"),
        (f"Gói thầu: {d.get('goi_thau', '')}", f(size=12), "left"),
        (f"Địa điểm: {d.get('dia_diem', '')}", f(size=12), "left"),
        (f"Ngày lập: {ngay(d.get('ngay_lap')).strftime('%d/%m/%Y') if d.get('ngay_lap') else ''}",
         f(italic=True, size=12), "left"),
    ]
    for i, (txt, font, can) in enumerate(dong, 1):
        ws.merge_cells(f"A{i}:{cuoi}{i}")
        c = ws[f"A{i}"]
        c.value, c.font = txt, font
        c.alignment = Alignment(horizontal=can, vertical="center", wrap_text=True)
    return len(dong) + 2  # dòng tiêu đề cột


def hang_tieu_de(ws, r, cot, co_dinh=True):
    for j, (ten, rong) in enumerate(cot, 1):
        c = ws.cell(r, j, ten)
        c.font, c.fill, c.border = f(True), NEN_TD, KHUNG
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(j)].width = rong
    if co_dinh:
        ws.freeze_panes = ws.cell(r + 1, 1)


def o(ws, r, c, v, fmt=None, bold=False, can="left"):
    x = ws.cell(r, c, v)
    x.font, x.border = f(bold), KHUNG
    x.alignment = Alignment(horizontal=can, vertical="top", wrap_text=True)
    if fmt:
        x.number_format = fmt
    return x


def ds_chon(ws, vung, gia_tri):
    dv = DataValidation(type="list", formula1='"' + ",".join(gia_tri) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(vung)


def to_mau_trang_thai(ws, vung, cot_tt):
    r0 = int("".join(ch for ch in vung.split(":")[0] if ch.isdigit()))
    for tt, mau in MAU.items():
        ws.conditional_formatting.add(
            vung, FormulaRule(formula=[f'${cot_tt}{r0}="{tt}"'], fill=PatternFill("solid", fgColor=mau)))


# ------------------------------------------------------------------ các sheet
def sheet_yeu_cau(wb, d):
    ws = wb.create_sheet("2-YeuCau-DapUng")
    cot = [("STT", 6), ("Nhóm yêu cầu", 16), ("Yêu cầu của E-HSMT", 45), ("Trích dẫn (mục, tr.)", 18),
           ("Năng lực công ty đáp ứng", 40), ("Trạng thái", 14), ("Việc cần làm", 32),
           ("Phụ trách", 14), ("Hạn", 12)]
    r0 = tieu_de(ws, d, "BẢNG ĐỐI CHIẾU YÊU CẦU E-HSMT VỚI NĂNG LỰC CÔNG TY", len(cot))
    hang_tieu_de(ws, r0, cot)
    r = r0
    for i, y in enumerate(d.get("yeu_cau", []), 1):
        r = r0 + i
        o(ws, r, 1, i, can="center")
        o(ws, r, 2, y.get("nhom", ""))
        o(ws, r, 3, y.get("noi_dung", ""))
        o(ws, r, 4, y.get("trich_dan", ""))
        o(ws, r, 5, y.get("dap_ung", ""))
        o(ws, r, 6, y.get("trang_thai", "CHƯA RÕ"), bold=True, can="center")
        o(ws, r, 7, y.get("viec_can_lam", ""))
        o(ws, r, 8, y.get("phu_trach", ""))
        o(ws, r, 9, ngay(y.get("han")), fmt="dd/mm/yyyy", can="center")
    cuoi = max(r, r0 + 1) + 20  # chừa dòng trống để thêm tay
    for rr in range(r + 1, cuoi + 1):
        for c in range(1, len(cot) + 1):
            o(ws, rr, c, None, fmt="dd/mm/yyyy" if c == 9 else None)
    ds_chon(ws, f"F{r0 + 1}:F{cuoi}", TRANG_THAI)
    to_mau_trang_thai(ws, f"A{r0 + 1}:I{cuoi}", "F")
    return ws, r0 + 1, cuoi


def sheet_go_no_go(wb, d):
    ws = wb.create_sheet("3-GoNoGo")
    cot = [("STT", 6), ("Tiêu chí", 55), ("Trọng số (%)", 12), ("Điểm (1-5)", 11),
           ("Điểm quy đổi", 12), ("Căn cứ chấm", 45)]
    r0 = tieu_de(ws, d, "ĐÁNH GIÁ QUYẾT ĐỊNH DỰ THẦU (GO / NO-GO)", len(cot))
    hang_tieu_de(ws, r0, cot)
    ds = d.get("go_no_go") or [{"tieu_chi": t, "trong_so": w} for t, w in GO_NO_GO_MAC_DINH]
    for i, g in enumerate(ds, 1):
        r = r0 + i
        o(ws, r, 1, i, can="center")
        o(ws, r, 2, g.get("tieu_chi", ""))
        o(ws, r, 3, g.get("trong_so", 0), fmt="0", can="center")
        o(ws, r, 4, g.get("diem"), fmt="0", can="center")
        o(ws, r, 5, f'=IF(D{r}="","",C{r}*D{r}/5)', fmt="0.0", can="center")
        o(ws, r, 6, g.get("ghi_chu", ""))
    a, b = r0 + 1, r0 + len(ds)
    dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"D{a}:D{b}")
    t = b + 1
    o(ws, t, 2, "TỔNG ĐIỂM (thang 100)", bold=True)
    o(ws, t, 3, f"=SUM(C{a}:C{b})", fmt="0", bold=True, can="center")
    o(ws, t, 4, f'=COUNTBLANK(D{a}:D{b})&" chưa chấm"', can="center")
    o(ws, t, 5, f"=SUM(E{a}:E{b})", fmt="0.0", bold=True, can="center")
    o(ws, t, 6, f'=IF(C{t}<>100,"Tổng trọng số phải bằng 100","")')
    ws.cell(t + 2, 2, "Thang điểm: 5 = rất thuận lợi; 3 = đáp ứng vừa đủ; 1 = không đáp ứng hoặc rủi ro cao. "
                      "Ngưỡng: ≥ 70 nên dự thầu; 50 đến dưới 70 cân nhắc; < 50 không nên. "
                      "Có yêu cầu CHƯA ĐẠT ở sheet 2 thì không dự thầu dù điểm cao (trừ khi liên danh, thầu phụ).").font = f(italic=True, size=11)
    ws.cell(t + 2, 2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[t + 2].height = 48
    return f"'3-GoNoGo'!E{t}", f"'3-GoNoGo'!D{a}:D{b}"


def sheet_ke_hoach(wb, d, o_dong_thau):
    ws = wb.create_sheet("4-KeHoach")
    cot = [("STT", 6), ("Việc", 48), ("Phụ trách", 16), ("Trước đóng thầu (ngày)", 12),
           ("Hạn hoàn thành", 14), ("Còn lại (ngày)", 11), ("Tiến độ", 12), ("Ghi chú", 30)]
    r0 = tieu_de(ws, d, "KẾ HOẠCH LẬP HỒ SƠ DỰ THẦU", len(cot))
    hang_tieu_de(ws, r0, cot)
    ds = d.get("ke_hoach", [])
    for i, k in enumerate(ds, 1):
        r = r0 + i
        o(ws, r, 1, i, can="center")
        o(ws, r, 2, k.get("viec", ""))
        o(ws, r, 3, k.get("phu_trach", ""))
        o(ws, r, 4, k.get("truoc_dong_thau_ngay", 0), fmt="0", can="center")
        o(ws, r, 5, f"=INT({o_dong_thau})-D{r}", fmt="dd/mm/yyyy", can="center")
        o(ws, r, 6, f'=IF(G{r}="Xong","",E{r}-TODAY())', fmt="0", can="center")
        o(ws, r, 7, k.get("tien_do", "Chưa làm"), can="center")
        o(ws, r, 8, k.get("ghi_chu", ""))
    if ds:
        a, b = r0 + 1, r0 + len(ds)
        ds_chon(ws, f"G{a}:G{b}", TIEN_DO)
        ws.conditional_formatting.add(f"A{a}:H{b}", FormulaRule(
            formula=[f'AND($G{a}<>"Xong",$F{a}<>"",$F{a}<0)'], fill=PatternFill("solid", fgColor="FFC7CE")))
        ws.conditional_formatting.add(f"A{a}:H{b}", FormulaRule(
            formula=[f'$G{a}="Xong"'], fill=PatternFill("solid", fgColor="C6EFCE")))


def sheet_danh_muc(wb, d):
    ws = wb.create_sheet("5-DanhMucNop")
    cot = [("STT", 6), ("Tài liệu phải nộp", 50), ("Căn cứ E-HSMT", 20), ("Hình thức nộp", 18),
           ("Trạng thái", 14), ("File / ghi chú", 35)]
    r0 = tieu_de(ws, d, "DANH MỤC TÀI LIỆU TRONG E-HSDT", len(cot))
    hang_tieu_de(ws, r0, cot)
    ds = d.get("danh_muc_nop", [])
    for i, k in enumerate(ds, 1):
        r = r0 + i
        o(ws, r, 1, i, can="center")
        o(ws, r, 2, k.get("tai_lieu", ""))
        o(ws, r, 3, k.get("can_cu", ""))
        o(ws, r, 4, k.get("hinh_thuc", ""))
        o(ws, r, 5, k.get("trang_thai", "Chưa làm"), can="center")
        o(ws, r, 6, k.get("ghi_chu", ""))
    if ds:
        a, b = r0 + 1, r0 + len(ds)
        ds_chon(ws, f"E{a}:E{b}", TIEN_DO)
        ws.conditional_formatting.add(f"A{a}:F{b}", FormulaRule(
            formula=[f'$E{a}="Xong"'], fill=PatternFill("solid", fgColor="C6EFCE")))


def sheet_lam_ro(wb, d):
    ws = wb.create_sheet("6-LamRo")
    cot = [("STT", 6), ("Nội dung đề nghị làm rõ", 70), ("Trích dẫn E-HSMT", 22), ("Trả lời của BMT", 40)]
    r0 = tieu_de(ws, d, "CÂU HỎI ĐỀ NGHỊ LÀM RÕ E-HSMT", len(cot))
    hang_tieu_de(ws, r0, cot)
    for i, k in enumerate(d.get("cau_hoi_lam_ro", []), 1):
        r = r0 + i
        o(ws, r, 1, i, can="center")
        o(ws, r, 2, k.get("noi_dung", ""))
        o(ws, r, 3, k.get("trich_dan", ""))
        o(ws, r, 4, "")


def sheet_tong_quan(ws, d, vung_yc, o_diem, vung_diem):
    cot = [("Nội dung", 38), ("Giá trị", 42), ("Ghi chú", 45)]
    r0 = tieu_de(ws, d, "BẢNG PHÂN TÍCH HỒ SƠ MỜI THẦU", len(cot))
    hang_tieu_de(ws, r0, cot, co_dinh=False)
    r = r0
    cell = {}

    def dong(ten, gt, fmt=None, ghi_chu="", khoa=None, bold=False):
        nonlocal r
        r += 1
        o(ws, r, 1, ten, bold=True)
        o(ws, r, 2, gt, fmt=fmt, bold=bold)
        o(ws, r, 3, ghi_chu)
        if khoa:
            cell[khoa] = f"B{r}"

    dong("Số TBMT", d.get("so_tbmt", ""))
    dong("Bên mời thầu", d.get("ben_moi_thau", ""))
    dong("Chủ đầu tư", d.get("chu_dau_tu", ""))
    dong("Nguồn vốn", d.get("nguon_von", ""))
    dong("Hình thức lựa chọn nhà thầu", d.get("hinh_thuc", ""))
    dong("Phương thức", d.get("phuong_thuc", ""))
    dong("Loại hợp đồng", d.get("loai_hop_dong", ""))
    dong("Giá gói thầu (đồng)", d.get("gia_goi_thau"), fmt="#,##0", khoa="gia")
    dong("Thời gian thực hiện hợp đồng (ngày)", d.get("thoi_gian_thuc_hien_ngay"), fmt="0")
    dong("Thời điểm đóng thầu", ngay(d.get("dong_thau")), fmt="dd/mm/yyyy hh:mm", khoa="dong", bold=True)
    dong("Số ngày còn lại đến đóng thầu", f"=INT({cell['dong']})-TODAY()", fmt="0", bold=True)
    dong("Hiệu lực E-HSDT (ngày)", d.get("hieu_luc_hsdt_ngay"), fmt="0", khoa="hl")
    dong("Ngày hết hiệu lực E-HSDT", f"=IF({cell['hl']}=\"\",\"\",INT({cell['dong']})+{cell['hl']})",
         fmt="dd/mm/yyyy")
    dong("Giá trị bảo đảm dự thầu (đồng)", d.get("bao_dam_du_thau"), fmt="#,##0", khoa="bd",
         ghi_chu="Lấy đúng số trong E-HSMT, không làm tròn xuống")
    dong("Tỷ lệ bảo đảm dự thầu / giá gói thầu",
         f"=IF(OR({cell['bd']}=\"\",{cell['gia']}=\"\"),\"\",{cell['bd']}/{cell['gia']})", fmt="0.00%")
    dong("Hiệu lực bảo đảm dự thầu (ngày)", d.get("hieu_luc_bddt_ngay"), fmt="0", khoa="hlbd",
         ghi_chu="Luật Đấu thầu: bằng hiệu lực E-HSDT cộng 30 ngày (kiểm tra lại hiệu lực văn bản)")
    dong("Kiểm tra hiệu lực bảo đảm", f"=IF(OR({cell['hlbd']}=\"\",{cell['hl']}=\"\"),\"Chưa nhập\","
         f"IF({cell['hlbd']}>={cell['hl']}+30,\"Đủ\",\"THIẾU \"&({cell['hl']}+30-{cell['hlbd']})&\" ngày\"))",
         bold=True)
    dong("File E-HSMT đã đọc", d.get("nguon_hsmt", ""))

    r += 2
    o(ws, r, 1, "TÓM TẮT ĐỐI CHIẾU YÊU CẦU", bold=True)
    sh, a, b = "'2-YeuCau-DapUng'", vung_yc[0], vung_yc[1]
    for tt in TRANG_THAI:
        r += 1
        o(ws, r, 1, f"Số yêu cầu {tt}")
        o(ws, r, 2, f'=COUNTIF({sh}!F{a}:F{b},"{tt}")', fmt="0", can="center")
        cell[tt] = f"B{r}"
    r += 1
    o(ws, r, 1, "Điểm Go/No-go (thang 100)", bold=True)
    o(ws, r, 2, f"={o_diem}", fmt="0.0", bold=True, can="center")
    cell["diem"] = f"B{r}"
    r += 1
    o(ws, r, 1, "KẾT LUẬN SƠ BỘ", bold=True)
    kl = (f'=IF({cell["CHƯA ĐẠT"]}>0,"KHÔNG ĐỦ ĐIỀU KIỆN: còn "&{cell["CHƯA ĐẠT"]}&" yêu cầu CHƯA ĐẠT",'
          f'IF(COUNTBLANK({vung_diem})>0,"CHƯA CHẤM ĐỦ GO/NO-GO: còn "&COUNTBLANK({vung_diem})&" tiêu chí",'
          f'IF({cell["diem"]}>=70,"NÊN DỰ THẦU",IF({cell["diem"]}>=50,"CÂN NHẮC","KHÔNG NÊN DỰ THẦU"))))')
    x = o(ws, r, 2, kl, bold=True)
    x.font = f(True, size=13, color="C00000")
    o(ws, r, 3, "Giám đốc quyết định. Kết luận này chỉ để tham khảo.")
    return cell["dong"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    nguon, dich = sys.argv[1], sys.argv[2]
    if os.path.exists(dich):
        sys.exit(f"LỖI: {dich} đã tồn tại. Không ghi đè, hãy tăng số phiên bản (_v02, _v03...).")
    with open(nguon, encoding="utf-8") as fh:
        d = json.load(fh)

    wb = Workbook()
    ws1 = wb.active
    ws1.title = "1-TongQuan"
    _, a, b = sheet_yeu_cau(wb, d)
    o_diem, vung_diem = sheet_go_no_go(wb, d)
    o_dong = sheet_tong_quan(ws1, d, (a, b), o_diem, vung_diem)
    sheet_ke_hoach(wb, d, f"'1-TongQuan'!{o_dong}")
    sheet_danh_muc(wb, d)
    sheet_lam_ro(wb, d)

    for ws in wb.worksheets:
        ws.page_setup.orientation = "landscape"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.print_options.horizontalCentered = True

    os.makedirs(os.path.dirname(os.path.abspath(dich)), exist_ok=True)
    wb.save(dich)
    print(f"Đã tạo: {os.path.abspath(dich)}")
    print(f"  {len(d.get('yeu_cau', []))} yêu cầu, {len(d.get('ke_hoach', []))} việc, "
          f"{len(d.get('danh_muc_nop', []))} tài liệu nộp, {len(d.get('cau_hoi_lam_ro', []))} câu hỏi làm rõ")


if __name__ == "__main__":
    main()
