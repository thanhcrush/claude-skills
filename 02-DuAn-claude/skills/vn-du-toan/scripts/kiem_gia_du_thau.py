# -*- coding: utf-8 -*-
"""Kiem file BangGiaDuThau_vNN.xlsx truoc khi giao.

Chay:  python kiem_gia_du_thau.py <BangGiaDuThau_vNN.xlsx>

Lam 3 viec (khong sua file):
  1. Doc so lieu dau vao trong file (khoi luong, VL, NC, M, ty le), tinh lai bang Python.
  2. Mo file bang Excel (COM), tinh lai cong thuc, doc gia du thau va sheet 04-Soat.
  3. Doi chieu hai ket qua, in ra gia du thau bang so va bang chu de dan vao don du thau.
Khong co Excel thi chi in ket qua tinh bang Python va noi ro la chua kiem duoc cong thuc.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openpyxl import load_workbook  # noqa: E402

import lap_gia_du_thau as g  # noqa: E402


def doc_du_lieu(duong_dan):
    wb = load_workbook(duong_dan)
    cf = wb[g.S_CFG]
    bg = wb[g.S_BG]
    pt = wb[g.S_PT]
    ty = {}
    for khoa, r in g.CFG.items():
        v = cf.cell(row=r, column=2).value
        ty[khoa] = {"gia_tri": v if isinstance(v, (int, float)) else None}
    boq = []
    for r in range(g.FIRST, bg.max_row + 1):
        dvt = bg.cell(row=r, column=4).value
        ten = bg.cell(row=r, column=3).value
        if dvt in (None, ""):
            if bg.cell(row=r, column=1).value not in (None, ""):
                boq.append({"loai": "muc", "ten": str(bg.cell(row=r, column=1).value)})
            continue
        kl = bg.cell(row=r, column=5).value

        def so(c):
            v = pt.cell(row=r, column=c).value
            return v if isinstance(v, (int, float)) else None
        boq.append({"stt": bg.cell(row=r, column=1).value, "ten": ten, "dvt": dvt,
                    "kl": kl if isinstance(kl, (int, float)) else None,
                    "don_gia": {"vl": so(6), "nc": so(7), "m": so(8)}})
    gia_goi = cf.cell(row=g.ROW_GIAGOI, column=2).value
    return {"ty_le": ty, "boq": boq, "gia_goi_thau": gia_goi if isinstance(gia_goi, (int, float)) else None}


def doc_excel(duong_dan):
    """Mo bang Excel, tinh lai, tra ve dict gia tri. Tra None neu khong co Excel."""
    try:
        import win32com.client
    except Exception:
        return None, "Không có pywin32"
    xl = None
    try:
        xl = win32com.client.DispatchEx("Excel.Application")
        xl.Visible = False
        xl.DisplayAlerts = False
        wb = xl.Workbooks.Open(os.path.abspath(duong_dan), 0, True)  # UpdateLinks=0, ReadOnly=True
        xl.CalculateFull()
        th = wb.Worksheets(g.S_TH)
        so = wb.Worksheets(g.S_SOAT)
        kq = {
            "cong_truoc_thue": th.Range("B5").Value, "giam_gia": th.Range("B6").Value,
            "sau_giam_truoc_thue": th.Range("B7").Value, "gtgt": th.Range("B8").Value,
            "nha_tam": th.Range("B9").Value, "gia_du_thau": th.Range("B10").Value,
            "ket_luan_gia_goi": th.Range("B15").Value, "gia_thanh": th.Range("B18").Value,
            "loi_nhuan": th.Range("B19").Value,
        }
        soat = []
        r = 5
        while so.Cells(r, 2).Value not in (None, ""):
            soat.append((so.Cells(r, 1).Value, so.Cells(r, 2).Value, so.Cells(r, 3).Value, so.Cells(r, 4).Value))
            r += 1
        kq["tinh_trang"] = so.Cells(r + 1, 4).Value
        # Quet loi cong thuc tren moi sheet
        loi = []
        for w in wb.Worksheets:
            ur = w.UsedRange
            for row in range(1, ur.Rows.Count + 1):
                for col in range(1, ur.Columns.Count + 1):
                    v = ur.Cells(row, col).Value
                    if isinstance(v, int) and v < 0 and v in (-2146826281, -2146826246, -2146826259, -2146826288,
                                                              -2146826252, -2146826265, -2146826273):
                        loi.append("%s!%s" % (w.Name, ur.Cells(row, col).Address.replace("$", "")))
        kq["o_loi"] = loi
        kq["soat"] = soat
        wb.Close(False)
        return kq, None
    except Exception as e:  # noqa: BLE001
        return None, "Không mở được bằng Excel: %s" % e
    finally:
        if xl is not None:
            try:
                xl.Quit()
            except Exception:
                pass


def dd(x):
    return "{:,.0f}".format(x).replace(",", ".")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    du_lieu = doc_du_lieu(path)
    py = g.tinh(du_lieu)
    print("== Python tính lại từ số liệu đầu vào trong file ==")
    print("Số dòng công việc: %d | thiếu đơn giá: %d | KL lỗi: %d | đơn giá = 0: %d" % (
        py["so_dong"], py["thieu_don_gia"], py["kl_loi"], py["don_gia_bang_0"]))
    print("Cộng trước thuế: %s | Giá dự thầu: %s" % (dd(py["cong_truoc_thue"]), dd(py["gia_du_thau"])))
    xl, loi = doc_excel(path)
    ok = True
    if xl is None:
        print("\n[Chưa kiểm được công thức] %s" % loi)
        ok = False
    else:
        print("\n== Excel tính lại công thức ==")
        for khoa in ("cong_truoc_thue", "giam_gia", "gtgt", "nha_tam", "gia_du_thau"):
            e, p = xl[khoa], py[khoa]
            lech = abs((e or 0) - p)
            print("%-22s Excel %18s | Python %18s | %s" % (
                khoa, dd(e or 0), dd(p), "KHỚP" if lech < 1 else "LỆCH %s" % dd(lech)))
            ok = ok and lech < 1
        print("So với giá gói thầu: %s" % xl["ket_luan_gia_goi"])
        print("Lợi nhuận trước thuế sau giảm giá: %s (giá thành %s)" % (dd(xl["loi_nhuan"] or 0), dd(xl["gia_thanh"] or 0)))
        if xl["o_loi"]:
            ok = False
            print("Ô lỗi công thức (#REF!, #VALUE!...): %s" % ", ".join(xl["o_loi"][:20]))
        else:
            print("Không có ô lỗi công thức.")
        print("\n== Sheet 04-Soat ==")
        for ma, nd, gt, kq in xl["soat"]:
            print("[%s] %s: %s -> %s" % (ma or "-", nd, gt, kq))
        print("TÌNH TRẠNG CHUNG:", xl["tinh_trang"])
    gia = (xl or py)["gia_du_thau"] if xl else py["gia_du_thau"]
    print("\nGiá dự thầu bằng số : %s đồng" % dd(gia))
    print("Giá dự thầu bằng chữ: %s" % g.so_thanh_chu(gia))
    print("\nKẾT LUẬN: %s" % ("Công thức Excel khớp tính lại bằng Python." if ok else "CHƯA XÁC NHẬN ĐƯỢC, xem các dòng trên."))
    if xl is not None and xl.get("tinh_trang") != "ĐẠT":
        print("Nhưng sheet 04-Soat báo: %s. Chưa được báo xong." % xl.get("tinh_trang"))
    elif py["thieu_don_gia"] or py["kl_loi"]:
        print("Còn dòng thiếu đơn giá hoặc khối lượng: chưa được báo xong.")


if __name__ == "__main__":
    main()
