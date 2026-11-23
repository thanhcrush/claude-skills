# -*- coding: utf-8 -*-
"""
Đọc hồ sơ kỹ thuật (PDF, DOCX, XLSX) ra text CÓ ĐÁNH DẤU VỊ TRÍ để trích dẫn chính xác.

Cách chạy:
    python doc_tai_lieu.py <file1> [file2 ...] [--anh] [--ra <thu_muc>]

  --anh      : render thêm ảnh PNG mọi trang PDF (để nhìn bảng biểu, bản vẽ, con dấu).
               Trang không có lớp chữ (bản scan) luôn được render dù không có cờ này.
  --ra <dir> : thư mục ghi kết quả (mặc định: %TEMP%\\soat_ho_so).

Kết quả: <thu_muc>\\<ten_file>.txt, mỗi trang mở đầu bằng
    ===== [<ten_file>] TRANG <i>/<N> =====
Cảnh báo in ra màn hình:
  - trang không có chữ (bản scan: phải xem ảnh, không có OCR);
  - số trang in trên tài liệu ("Trang x / y") khác số trang thực của file => file có thể thiếu trang;
  - số trang nội bộ được viện dẫn trong tài liệu (VD "(Trang 42)") => ghi cả hai khi trích dẫn.
"""
import os
import re
import sys
import tempfile

RE_TRANG_IN = re.compile(r"Trang\s+(\d+)\s*/\s*(\d+)", re.I)
RE_TRANG_NOI_BO = re.compile(r"\([^()]*?Trang\s+(\d+)\)", re.I)


def doc_pdf(path, ra, anh_moi_trang):
    import pymupdf
    ten = os.path.basename(path)
    d = pymupdf.open(path)
    n = len(d)
    khoi, canh_bao = [], []
    for i, pg in enumerate(d, 1):
        txt = pg.get_text().strip()
        khoi.append(f"\n===== [{ten}] TRANG {i}/{n} =====\n{txt}")
        if len(txt) < 20:
            canh_bao.append(f"Trang {i}/{n}: KHÔNG CÓ LỚP CHỮ (có thể là bản scan) -> phải xem ảnh.")
        for a, b in RE_TRANG_IN.findall(txt):
            if int(b) != n:
                canh_bao.append(f"Trang {i}/{n}: tài liệu in 'Trang {a}/{b}' nhưng file chỉ có {n} trang "
                                f"-> CÓ THỂ THIẾU TRANG, phải nêu trong báo cáo.")
        for m in RE_TRANG_NOI_BO.finditer(txt):
            so = m.group(1)
            canh_bao.append(f"Trang {i}/{n}: có viện dẫn số trang nội bộ 'Trang {so}' "
                            f"-> trích dẫn ghi cả trang file và trang nội bộ.")
        if anh_moi_trang or len(txt) < 20:
            f = os.path.join(ra, f"{os.path.splitext(ten)[0]}_trang{i:02d}.png")
            pg.get_pixmap(dpi=110).save(f)
            khoi.append(f"[Ảnh trang: {f}]")
    return khoi, canh_bao, n


def doc_docx(path):
    from docx import Document
    ten = os.path.basename(path)
    d = Document(path)
    khoi = [f"\n===== [{ten}] (Word không có số trang cố định: trích dẫn theo đề mục/điều khoản) ====="]
    for p in d.paragraphs:
        if p.text.strip():
            khoi.append(p.text)
    for k, t in enumerate(d.tables, 1):
        khoi.append(f"\n--- Bảng {k} ---")
        for r in t.rows:
            khoi.append(" | ".join(c.text.strip() for c in r.cells))
    return khoi, [], None


def doc_xlsx(path):
    import openpyxl
    ten = os.path.basename(path)
    wb = openpyxl.load_workbook(path, data_only=True)
    khoi = [f"\n===== [{ten}] (Excel: trích dẫn theo Sheet!Ô) ====="]
    for ws in wb.worksheets:
        khoi.append(f"\n--- Sheet: {ws.title} ---")
        for row in ws.iter_rows():
            o = [f"{c.coordinate}={c.value}" for c in row if c.value not in (None, "")]
            if o:
                khoi.append("  ".join(o))
    return khoi, [], None


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    anh = "--anh" in args
    ra = os.path.join(tempfile.gettempdir(), "soat_ho_so")
    if "--ra" in args:
        ra = args[args.index("--ra") + 1]
    files = [a for i, a in enumerate(args)
             if not a.startswith("--") and (i == 0 or args[i - 1] != "--ra")]
    os.makedirs(ra, exist_ok=True)

    for path in files:
        if not os.path.exists(path):
            print(f"[KHÔNG TÌM THẤY] {path}")
            continue
        ext = os.path.splitext(path)[1].lower()
        if ext == ".pdf":
            khoi, cb, n = doc_pdf(path, ra, anh)
        elif ext == ".docx":
            khoi, cb, n = doc_docx(path)
        elif ext in (".xlsx", ".xlsm"):
            khoi, cb, n = doc_xlsx(path)
        else:
            print(f"[CHƯA HỖ TRỢ] {path} ({ext}). .doc/.xls cũ: mở bằng Word/Excel lưu lại .docx/.xlsx; "
                  f".dwg: xuất PDF hoặc DXF trước.")
            continue
        out = os.path.join(ra, os.path.splitext(os.path.basename(path))[0] + ".txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(khoi))
        so_trang = f"{n} trang" if n else "không phân trang"
        print(f"[OK] {os.path.basename(path)}: {so_trang} -> {out}")
        for c in dict.fromkeys(cb):
            print(f"   ! {c}")


if __name__ == "__main__":
    main()
