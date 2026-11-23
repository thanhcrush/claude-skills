# -*- coding: utf-8 -*-
"""
Chuyển bản thảo Markdown đơn giản sang Word, dùng cho THUYẾT MINH BIỆN PHÁP TỔ CHỨC THI CÔNG
và các văn bản dài trong E-HSDT. Khổ A4, Times New Roman 13, lề T20 D20 Tr30 P15 mm,
căn đều hai bên, giãn dòng 1,2, số trang ở chân trang.

Cách chạy:
    python md_sang_docx.py <ban_thao.md> <file_ra.docx> [--kiem-tra]

  --kiem-tra : dùng Word (COM) xuất PDF rồi render PNG từng trang để soát bố cục (cần MS Word).

Markdown hỗ trợ:
  # Tiêu đề văn bản (in hoa, căn giữa)      ## Chương / phần (1.)      ### Mục (1.1.)   #### Tiểu mục
  - gạch đầu dòng     **chữ đậm**     *chữ nghiêng*     bảng dạng | a | b | (dòng |---| bỏ qua)
  Dòng trống = sang đoạn mới.   Dòng chỉ có "---pagebreak---" = sang trang.
"""
import os
import re
import sys
import tempfile

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt

FONT, CO = "Times New Roman", 13
RE_DINH_DANG = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def run(p, text, bold=False, italic=False, size=CO):
    r = p.add_run(text)
    r.bold, r.italic, r.font.size, r.font.name = bold, italic, Pt(size), FONT
    r._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), FONT)
    return r


def ghi(p, text, size=CO, bold=False):
    for part in RE_DINH_DANG.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run(p, part[2:-2], True, False, size)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run(p, part[1:-1], bold, True, size)
        else:
            run(p, part, bold, False, size)


def doan(doc, can=WD_ALIGN_PARAGRAPH.JUSTIFY, thut=True, truoc=0, sau=6, giu_voi_sau=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.alignment, pf.space_before, pf.space_after = can, Pt(truoc), Pt(sau)
    pf.line_spacing = 1.2
    pf.keep_with_next = giu_voi_sau
    if thut:
        pf.first_line_indent = Mm(10)
    return p


def so_trang(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = run(p, "", size=11)
    for loai, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if loai:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), loai)
        else:
            e = OxmlElement("w:instrText")
            e.set(qn("xml:space"), "preserve")
            e.text = txt
        r._element.append(e)


def bang(doc, dong):
    hang = [[c.strip() for c in d.strip().strip("|").split("|")] for d in dong
            if not re.fullmatch(r"\s*\|?[\s:\-|]+\|?\s*", d)]
    so_cot = max(len(h) for h in hang)
    t = doc.add_table(rows=len(hang), cols=so_cot)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    # độ rộng cột theo lượng chữ dài nhất, tối thiểu 12 mm, tổng bằng vùng chữ 165 mm
    dai = [max(max((len(h[j]) if j < len(h) else 0) for h in hang), 3) for j in range(so_cot)]
    rong = [max(12.0, 165.0 * x / sum(dai)) for x in dai]
    rong = [w * 165.0 / sum(rong) for w in rong]
    for j, w in enumerate(rong):
        for o in t.columns[j].cells:
            o.width = Mm(w)
    for i, h in enumerate(hang):
        for j in range(so_cot):
            o = t.cell(i, j)
            p = o.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            ghi(p, h[j] if j < len(h) else "", size=12, bold=(i == 0))
            if i == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if i == 0:  # lặp hàng tiêu đề khi bảng sang trang
            tr = t.rows[0]._tr.get_or_add_trPr()
            e = OxmlElement("w:tblHeader")
            e.set(qn("w:val"), "true")
            tr.append(e)
    doan(doc, thut=False, sau=0)


def chuyen(md, dich):
    doc = Document()
    s = doc.sections[0]
    s.page_width, s.page_height = Mm(210), Mm(297)
    s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = Mm(20), Mm(20), Mm(30), Mm(15)
    st = doc.styles["Normal"]
    st.font.name, st.font.size = FONT, Pt(CO)
    st.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), FONT)
    so_trang(s)

    dong = md.splitlines()
    i = 0
    while i < len(dong):
        d = dong[i].rstrip()
        if not d.strip():
            i += 1
            continue
        if d.strip() == "---pagebreak---":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        elif d.startswith("|"):
            khoi = []
            while i < len(dong) and dong[i].strip().startswith("|"):
                khoi.append(dong[i])
                i += 1
            bang(doc, khoi)
            continue
        elif d.startswith("#### "):
            ghi(doan(doc, thut=False, truoc=4, sau=3, giu_voi_sau=True), f"*{d[5:].strip()}*", bold=True)
        elif d.startswith("### "):
            ghi(doan(doc, thut=False, truoc=6, sau=3, giu_voi_sau=True), d[4:].strip(), bold=True)
        elif d.startswith("## "):
            ghi(doan(doc, can=WD_ALIGN_PARAGRAPH.LEFT, thut=False, truoc=12, sau=6, giu_voi_sau=True),
                d[3:].strip().upper(), size=CO, bold=True)
        elif d.startswith("# "):
            ghi(doan(doc, can=WD_ALIGN_PARAGRAPH.CENTER, thut=False, truoc=0, sau=12),
                d[2:].strip().upper(), size=15, bold=True)
        elif re.match(r"^\s*[-*+] ", d):
            p = doan(doc, thut=False, sau=3)
            p.paragraph_format.left_indent = Mm(10 + 5 * (len(d) - len(d.lstrip())) // 2)
            p.paragraph_format.first_line_indent = Mm(-5)
            ghi(p, "- " + re.sub(r"^\s*[-*+] ", "", d))
        else:
            ghi(doan(doc), d.strip())
        i += 1
    doc.save(dich)


def kiem_tra(docx):
    import pymupdf
    import win32com.client
    ra = os.path.join(tempfile.gettempdir(), "md_sang_docx")
    os.makedirs(ra, exist_ok=True)
    pdf = os.path.join(ra, os.path.splitext(os.path.basename(docx))[0] + ".pdf")
    w = win32com.client.DispatchEx("Word.Application")
    w.Visible = False
    try:
        d = w.Documents.Open(os.path.abspath(docx), ReadOnly=True)
        d.SaveAs2(pdf, FileFormat=17)
        d.Close(False)
    finally:
        w.Quit()
    for i, pg in enumerate(pymupdf.open(pdf), 1):
        f = os.path.join(ra, f"trang{i:02d}.png")
        pg.get_pixmap(dpi=80).save(f)
        print(f"[Ảnh trang {i}] {f}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(arg) != 2:
        print(__doc__)
        sys.exit(1)
    nguon, dich = arg
    if os.path.exists(dich):
        sys.exit(f"LỖI: {dich} đã tồn tại. Không ghi đè, hãy tăng số phiên bản (_v02, _v03...).")
    with open(nguon, encoding="utf-8") as fh:
        chuyen(fh.read(), dich)
    print(f"Đã tạo: {os.path.abspath(dich)}")
    if "--kiem-tra" in sys.argv:
        kiem_tra(dich)


if __name__ == "__main__":
    main()
