# -*- coding: utf-8 -*-
"""
Sinh PHIẾU YÊU CẦU LÀM RÕ THÔNG TIN (RFI) dạng Word, thể thức văn bản hành chính
theo Nghị định 30/2020/NĐ-CP (A4, Times New Roman, lề T20-D20-Tr30-P15 mm).

Cách chạy:
    python tao_rfi.py <du_lieu.json> <file_ra.docx> [--kiem-tra]

  --kiem-tra : dùng Word (COM) xuất PDF rồi render PNG từng trang để soát bố cục.
               In ra đường dẫn các ảnh. Cần máy có cài MS Word.

Cấu trúc JSON: xem references/rfi_mau.json. Trong mọi chuỗi, **chữ** = in đậm.
"""
import json
import os
import re
import sys
import tempfile

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

FONT = "Times New Roman"
TEXT_W = 16.5  # cm, bề rộng vùng chữ A4 với lề trái 3 cm, phải 1,5 cm
CENTER, LEFT, RIGHT, JUSTIFY = (WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT,
                                WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.JUSTIFY)
LA_MA = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


# ---------------------------------------------------------------- tiện ích định dạng
def run(p, text, bold=False, italic=False, size=None):
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.name = FONT
    r._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), FONT)
    if size:
        r.font.size = Pt(size)
    return r


def md(p, text, size=None, bold=False, italic=False):
    """Ghi chuỗi có đánh dấu **đậm** thành các run."""
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", str(text))):
        if part:
            run(p, part, bold or i % 2 == 1, italic, size)


def para(container, text="", align=JUSTIFY, first=0.0, before=0, after=4, line=1.15,
         size=None, bold=False, italic=False):
    p = container.add_paragraph()
    p.alignment = align
    pf = p.paragraph_format
    pf.first_line_indent = Cm(first)
    pf.space_before, pf.space_after, pf.line_spacing = Pt(before), Pt(after), line
    md(p, text, size, bold, italic)
    return p


def bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    for k, v in (("val", "single"), ("sz", "6"), ("space", "1"), ("color", "000000")):
        b.set(qn(f"w:{k}"), v)
    bdr.append(b)
    pPr.append(bdr)


def gach_ngang(container, rong_o, dai_gach, after=6):
    """Đường kẻ ngắn căn giữa dưới tên cơ quan / tiêu ngữ / trích yếu."""
    p = container.add_paragraph()
    p.alignment = CENTER
    lui = max((rong_o - dai_gach) / 2, 0)
    p.paragraph_format.left_indent = Cm(lui)
    p.paragraph_format.right_indent = Cm(lui)
    p.paragraph_format.space_after = Pt(after)
    bottom_border(p)
    run(p, "", size=4)
    return p


def shade(cell, fill):
    s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(s)


def no_borders(table):
    b = OxmlElement("w:tblBorders")
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        x = OxmlElement(f"w:{e}"); x.set(qn("w:val"), "nil"); b.append(x)
    table._tbl.tblPr.append(b)


def fixed_layout(table, widths):
    table.autofit = False
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed")
    table._tbl.tblPr.append(lay)
    for row in table.rows:
        for c, w in zip(row.cells, widths):
            c.width = Cm(w)


def row_flag(row, tag):
    x = OxmlElement(f"w:{tag}"); x.set(qn("w:val"), "true")
    row._tr.get_or_add_trPr().append(x)


def cell_text(cell, text, align=LEFT, size=11.5, bold=False, italic=False):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    md(p, text, size, bold, italic)


def do_rong(cot, rong):
    if rong and abs(sum(rong) - TEXT_W) < 0.05:
        return rong
    if rong:  # co giãn cho đủ bề rộng vùng chữ
        k = TEXT_W / sum(rong)
        return [w * k for w in rong]
    if cot and cot[0].upper() == "STT":
        con = (TEXT_W - 1.2) / (len(cot) - 1)
        return [1.2] + [con] * (len(cot) - 1)
    return [TEXT_W / len(cot)] * len(cot)


def bang(doc, spec):
    """spec: {cot, dong, rong_cm?, can_giua?, co_chu?, giu_lien?, cao_dong_cm?}"""
    cot, dong = spec["cot"], spec["dong"]
    size = spec.get("co_chu", 11.5)
    giua = set(spec.get("can_giua", [0]))
    t = doc.add_table(rows=1, cols=len(cot))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, h in zip(t.rows[0].cells, cot):
        cell_text(c, h, CENTER, size, bold=True)
        shade(c, "D9D9D9")
    row_flag(t.rows[0], "tblHeader")
    for r in dong:
        cells = t.add_row().cells
        for j, v in enumerate(r):
            cell_text(cells[j], v, CENTER if j in giua else LEFT, size)
    fixed_layout(t, do_rong(cot, spec.get("rong_cm")))
    for r in t.rows:
        row_flag(r, "cantSplit")
        if spec.get("cao_dong_cm") and r is not t.rows[0]:
            r.height = Cm(spec["cao_dong_cm"])
    # giữ tiêu đề bảng đi cùng dòng đầu; bảng ngắn thì giữ liền cả bảng
    for r in (t.rows[:-1] if spec.get("giu_lien") else t.rows[:1]):
        for c in r.cells:
            for p in c.paragraphs:
                p.paragraph_format.keep_with_next = True
    return t


# ---------------------------------------------------------------- dựng văn bản
def tao(data, out):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(2), Cm(2)
    sec.left_margin, sec.right_margin = Cm(3), Cm(1.5)
    sec.header_distance = Cm(1)
    sec.different_first_page_header_footer = True  # số trang từ trang 2

    st = doc.styles["Normal"]
    st.font.name, st.font.size = FONT, Pt(13)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.line_spacing = 1.0

    # số trang giữa lề trên
    hp = sec.header.paragraphs[0]
    hp.alignment = CENTER
    for kind, txt in (("begin", None), (None, " PAGE "), ("end", None)):
        r = hp.add_run(); r.font.name = FONT; r.font.size = Pt(13)
        if kind:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), kind); r._r.append(f)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve")
            it.text = txt; r._r.append(it)

    # --- tên cơ quan | quốc hiệu, tiêu ngữ
    W_L, W_R = 6.3, 10.2
    hd = doc.add_table(rows=1, cols=2)
    no_borders(hd); fixed_layout(hd, [W_L, W_R])
    cL, cR = hd.rows[0].cells
    if data.get("co_quan_chu_quan"):
        p = cL.paragraphs[0]; p.alignment = CENTER
        run(p, data["co_quan_chu_quan"].upper(), size=12)
        p = cL.add_paragraph(); p.alignment = CENTER
    else:
        p = cL.paragraphs[0]; p.alignment = CENTER
    run(p, data["don_vi_gui"].upper(), bold=True, size=12)
    gach_ngang(cL, W_L, 2.2)
    p = cL.add_paragraph(); p.alignment = CENTER
    run(p, f"Số: {data.get('so', '……')}", size=13)

    p = cR.paragraphs[0]; p.alignment = CENTER
    run(p, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", bold=True, size=13)
    p = cR.add_paragraph(); p.alignment = CENTER
    run(p, "Độc lập - Tự do - Hạnh phúc", bold=True, size=14)
    gach_ngang(cR, W_R, 6.3)
    p = cR.add_paragraph(); p.alignment = CENTER
    run(p, f"{data.get('dia_danh', '……')}, ngày {data.get('ngay', '….. tháng ….. năm ……')}",
        italic=True, size=14)

    # --- tên loại, trích yếu
    para(doc, data.get("ten_loai", "PHIẾU YÊU CẦU LÀM RÕ THÔNG TIN"), CENTER, before=18, after=0,
         size=14, bold=True)
    para(doc, "(REQUEST FOR INFORMATION — RFI)", CENTER, after=2, size=12, italic=True)
    ty = data["trich_yeu"]
    ty = ty if isinstance(ty, list) else [ty]
    for i, dong in enumerate(ty):
        para(doc, dong, CENTER, after=2 if i == len(ty) - 1 else 0, size=14, bold=True)
    gach_ngang(doc, TEXT_W, 4.0, after=10)

    # --- kính gửi
    kg = data["kinh_gui"]
    t = doc.add_table(rows=len(kg), cols=2); no_borders(t); fixed_layout(t, [2.6, 13.9])
    cell_text(t.cell(0, 0), "Kính gửi:", RIGHT, 14)
    for i, noi in enumerate(kg):
        cell_text(t.cell(i, 1), noi if len(kg) == 1 else f"- {noi}", LEFT, 13)
    para(doc, "", after=4)

    # --- các mục nội dung, đánh số La Mã tự động
    muc = []
    if data.get("thong_tin_chung"):
        muc.append(("THÔNG TIN CHUNG", "ttc"))
    if data.get("can_cu"):
        muc.append(("CĂN CỨ", "cc"))
    if data.get("sai_khac"):
        muc.append((data["sai_khac"].get("tieu_de", "NỘI DUNG SAI KHÁC GIỮA CÁC TÀI LIỆU"), "sk"))
    if data.get("anh_huong"):
        muc.append((data["anh_huong"].get("tieu_de", "ẢNH HƯỞNG ĐẾN NGHIỆM THU, CHI PHÍ VÀ TIẾN ĐỘ"), "ah"))
    if data.get("de_xuat"):
        muc.append((data["de_xuat"].get("tieu_de", "ĐỀ XUẤT"), "dx"))
    if data.get("cau_hoi"):
        muc.append((data["cau_hoi"].get("tieu_de", "NỘI DUNG ĐỀ NGHỊ TRẢ LỜI"), "ch"))
    if data.get("tai_lieu_kem_theo"):
        muc.append(("TÀI LIỆU KÈM THEO", "tl"))

    def heading(text):
        p = para(doc, text, LEFT, before=8, after=4, bold=True)
        p.paragraph_format.keep_with_next = True

    for so, (tieu_de, loai) in enumerate(muc):
        heading(f"{LA_MA[so]}. {tieu_de}")
        if loai == "ttc":
            t = doc.add_table(rows=0, cols=2); t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for k, v in data["thong_tin_chung"]:
                c = t.add_row().cells
                cell_text(c[0], k, size=12, bold=True); shade(c[0], "F2F2F2")
                cell_text(c[1], v, size=12)
            fixed_layout(t, [4.5, 12.0])
            for r in t.rows:
                row_flag(r, "cantSplit")
        elif loai == "cc":
            for i, s in enumerate(data["can_cu"], 1):
                para(doc, f"{i}. {s}", first=1.0)
        elif loai == "sk":
            sk = data["sai_khac"]
            if sk.get("mo_dau"):
                para(doc, sk["mo_dau"], first=1.0)
            bang(doc, sk["bang"])
            if sk.get("ghi_chu"):
                para(doc, sk["ghi_chu"], before=4, size=12, italic=True)
        elif loai == "ah":
            for i, m in enumerate(data["anh_huong"]["muc"], 1):
                para(doc, f"**{i}. {m['tieu_de']}:** {m['noi_dung']}", first=1.0)
                if m.get("bang"):
                    bang(doc, m["bang"])
                if m.get("ghi_chu"):
                    para(doc, m["ghi_chu"], before=4, size=12, italic=True)
        elif loai == "dx":
            dx = data["de_xuat"]
            if dx.get("mo_dau"):
                para(doc, dx["mo_dau"], first=1.0)
            for i, s in enumerate(dx["muc"], 1):
                para(doc, f"{i}. {s}", first=1.0)
        elif loai == "ch":
            ch = data["cau_hoi"]
            bang(doc, {
                "cot": ["STT", "Nội dung cần làm rõ", ch.get("cot_tra_loi", "Trả lời")],
                "dong": [[str(i), q, ""] for i, q in enumerate(ch["muc"], 1)],
                "rong_cm": [1.2, 8.5, 6.8], "cao_dong_cm": 1.3,
            })
        elif loai == "tl":
            for i, s in enumerate(data["tai_lieu_kem_theo"], 1):
                para(doc, f"{i}. {s}", first=1.0)

    if data.get("ket_luan"):
        p = para(doc, data["ket_luan"], first=1.0, before=6)
        p.paragraph_format.keep_with_next = True  # kết luận đi liền khối ký tên

    # --- nơi nhận | chữ ký
    sg = doc.add_table(rows=1, cols=2); no_borders(sg); fixed_layout(sg, [8.0, 8.5])
    cL, cR = sg.rows[0].cells
    p = cL.paragraphs[0]; p.paragraph_format.space_before = Pt(8)
    run(p, "Nơi nhận:", bold=True, italic=True, size=12)
    for s in data.get("noi_nhan", ["Như trên;", "Lưu: VT."]):
        run(cL.add_paragraph(), f"- {s}", size=11)
    ky = data.get("ky", {})
    p = cR.paragraphs[0]; p.alignment = CENTER; p.paragraph_format.space_before = Pt(8)
    dong_ky = ky.get("chuc_danh", ["ĐẠI DIỆN ĐƠN VỊ"])
    run(p, dong_ky[0], bold=True, size=13)
    for s in dong_ky[1:]:
        q = cR.add_paragraph(); q.alignment = CENTER; run(q, s, bold=True, size=13)
    q = cR.add_paragraph(); q.alignment = CENTER
    run(q, "(Ký, ghi rõ họ tên, đóng dấu)", italic=True, size=12)
    for _ in range(4):
        cR.add_paragraph()
    q = cR.add_paragraph(); q.alignment = CENTER
    run(q, ky.get("ho_ten", "……………………………"), bold=True, size=13)
    row_flag(sg.rows[0], "cantSplit")  # không tách Nơi nhận / chữ ký sang 2 trang

    # --- phần xác nhận, phản hồi của các bên nhận
    ben = data.get("phan_hoi", [])
    if ben:
        para(doc, "", after=6)
        p = para(doc, "PHẦN XÁC NHẬN VÀ PHẢN HỒI", CENTER, before=10, after=6, size=13, bold=True)
        p.paragraph_format.keep_with_next = True
        fb = doc.add_table(rows=2, cols=len(ben)); fb.style = "Table Grid"
        fb.alignment = WD_TABLE_ALIGNMENT.CENTER
        for j, h in enumerate(ben):
            cell_text(fb.cell(0, j), h, CENTER, 12, bold=True); shade(fb.cell(0, j), "D9D9D9")
            fb.cell(0, j).paragraphs[0].paragraph_format.keep_with_next = True
            c = fb.cell(1, j)
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            c.paragraphs[0].paragraph_format.space_before = Pt(4)
            run(c.paragraphs[0], "Ý kiến:  ☐ Chấp thuận    ☐ Không chấp thuận", size=11.5)
            for s in ["……………………………………………", "……………………………………………",
                      "Ngày tiếp nhận: ….. /….. /……", "Ngày trả lời: ….. /….. /……"]:
                q = c.add_paragraph(); q.paragraph_format.space_before = Pt(4); run(q, s, size=11.5)
            q = c.add_paragraph(); q.alignment = CENTER; q.paragraph_format.space_before = Pt(6)
            run(q, "(Ký, ghi rõ họ tên, đóng dấu)", italic=True, size=11)
            for _ in range(4):
                c.add_paragraph()
        fixed_layout(fb, [TEXT_W / len(ben)] * len(ben))
        for r in fb.rows:
            row_flag(r, "cantSplit")

    doc.save(out)
    return out


def kiem_tra(docx_path):
    """Word xuất PDF, render PNG từng trang. Trả về danh sách ảnh."""
    import pymupdf
    import win32com.client
    src = os.path.abspath(docx_path)
    thu_muc = os.path.join(tempfile.gettempdir(), "soat_ho_so_rfi")
    os.makedirs(thu_muc, exist_ok=True)
    pdf = os.path.join(thu_muc, os.path.splitext(os.path.basename(src))[0] + ".pdf")
    w = win32com.client.DispatchEx("Word.Application")
    w.Visible = False
    try:
        d = w.Documents.Open(src, ReadOnly=True)
        d.ExportAsFixedFormat(pdf, 17)
        d.Close(False)
    finally:
        w.Quit()
    anh = []
    doc = pymupdf.open(pdf)
    for i, pg in enumerate(doc, 1):
        f = os.path.join(thu_muc, f"trang_{i:02d}.png")
        pg.get_pixmap(dpi=90).save(f)
        anh.append(f)
    return pdf, anh


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    out = sys.argv[2]
    if os.path.exists(out):
        sys.exit(f"LỖI: {out} đã tồn tại. Không ghi đè — hãy tăng số phiên bản (_v02, _v03...).")
    tao(data, out)
    print("Đã tạo:", os.path.abspath(out))
    if "--kiem-tra" in sys.argv:
        pdf, anh = kiem_tra(out)
        print(f"PDF kiểm tra: {pdf} ({len(anh)} trang)")
        for a in anh:
            print("  ", a)
