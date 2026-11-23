---
name: vn-du-toan
description: >-
  Hai chế độ. A: bóc khối lượng và lập dự toán chi phí xây dựng chuẩn Việt Nam từ hồ sơ bản vẽ vncad,
  xuất Excel 100% phông Times New Roman bằng vncad.estimate, khối lượng LẤY TỪ CHÍNH BẢNG THỐNG KÊ
  TRÊN BẢN VẼ chứ không gõ tay (lập hoặc sửa dự toán, bóc thép, bê tông, ván khuôn, xây tô, ốp lát,
  ước nhanh theo m² sàn, dự toán lệch bản vẽ). B: lập BẢNG GIÁ DỰ THẦU cho gói thầu xây lắp (E-HSDT)
  từ bảng khối lượng mời thầu: phân tích đơn giá, tổng hợp giá, giảm giá, kịch bản giá, so giá gói
  thầu, soát lỗi bị loại phần giá, phiếu nhập webform. Dùng chế độ B khi nhắc giá dự thầu, bảng giá
  dự thầu, đơn giá dự thầu, giảm giá, giá gói thầu, chào giá theo E-HSMT.
---

# Dự toán: gắn với bản vẽ (A) và giá dự thầu (B)

| Việc | Chế độ | Đọc |
|---|---|---|
| Lập dự toán từ bản vẽ vncad, ước nhanh theo m² sàn | **A** | phần dưới đây |
| Lập bảng giá cho E-HSDT, khối lượng do E-HSMT cho sẵn | **B** | [references/quy-trinh-gia-du-thau.md](references/quy-trinh-gia-du-thau.md) |
| Dự toán trên phần mềm F1, soát file F1 | không phải skill này | skill `lap-du-toan` |

Chế độ B dùng **chung nguyên tắc** của A (số có nguồn, thiếu thì để trống, đọc ngược file trước khi giao), khác ở chỗ khối lượng là của E-HSMT nên **không sửa**, và giá phải khớp đơn dự thầu. Đơn giá trực tiếp lấy từ F1 hoặc báo giá thật; tỷ lệ chi phí theo `lap-du-toan` mục 4 và E-HSMT.

## Chế độ B: bảng giá dự thầu

Điều kiện: anh Thành đã chốt dự thầu (`vn-dau-thau` Bước 3), có bảng khối lượng mời thầu. Quy trình 8 bước, công thức, mẫu báo cáo: [references/quy-trinh-gia-du-thau.md](references/quy-trinh-gia-du-thau.md).

Công cụ (Python 3.13, `openpyxl`, `pywin32` có sẵn; script nằm trong `scripts\` của skill):

```bash
PY="C:\Users\OS\AppData\Local\Programs\Python\Python313\python.exe"; SKILL="E:\New folder\.claude\skills\vn-du-toan"
"$PY" "$SKILL\scripts\lap_gia_du_thau.py" boq  "<BangKL_MoiThau.xlsx>" "<du_lieu.json>"        # đọc bảng khối lượng mời thầu
"$PY" "$SKILL\scripts\lap_gia_du_thau.py" xuat "<du_lieu.json>" "<BangGiaDuThau_v01.xlsx>"      # sinh Excel 6 sheet, giữ công thức
"$PY" "$SKILL\scripts\kiem_gia_du_thau.py" "<BangGiaDuThau_v01.xlsx>"                          # tính lại bằng Excel + Python, in giá bằng chữ
```

File Excel gồm: `00-CauHinh` (giá gói thầu, tỷ lệ kèm nguồn), `01-BangGiaDuThau`, `02-PhanTichDonGia` (VL, NC, M, chi phí chung, thu nhập chịu thuế), `03-TongHop` (giảm giá, thuế, so giá gói thầu, giá thành, lợi nhuận, 3 kịch bản giảm giá), `04-Soat` (checklist D1 đến D6), `05-PhieuWebform`. Mẫu JSON: [references/du_lieu_mau.json](references/du_lieu_mau.json).

Ba điều không thương lượng:

1. **Không sửa khối lượng mời thầu.** Thấy lệch với bản vẽ thì đưa vào câu hỏi làm rõ.
2. **Không bịa số.** Đơn giá, tỷ lệ, giá gói thầu thiếu thì để trống (ô vàng, sheet 04 báo LỖI LOẠI). Script không có giá trị mặc định cho tỷ lệ chi phí.
3. **Giá cuối do anh Thành chốt.** Báo ba kịch bản, kèm lợi nhuận và rủi ro theo loại hợp đồng; không tự chọn mức giảm giá. Nộp thầu, ký số do anh Thành làm.

Không dùng `vncad.estimate.build_estimate` cho giá dự thầu: nó gộp dự phòng và chi phí chung theo tỷ lệ chung, và không giữ bảng khối lượng mời thầu nguyên vẹn.

# Chế độ A: dự toán gắn với bản vẽ

## Nguyên tắc số một: khối lượng không gõ tay

Bộ mẫu từng có dự toán gõ tay 13.700 kg thép khung trong khi bản vẽ chỉ ra 7.217,6 kg; thép móng
3.200 so với 748,9 kg; bê tông móng 38 m³ so với khoảng 12 m³. Dự toán là con số người dùng mang
đi vay vốn và ký hợp đồng, nên:

- Dòng nào có bảng thống kê trên bản vẽ thì **lấy số từ bảng bằng code**, và ghi nguồn ngay trong
  nội dung dòng ("theo bảng thống kê KC-02 x 3 tầng").
- Dòng nào chưa có căn cứ trên bản vẽ thì ghi **"SỐ ƯỚC"** trong nội dung dòng và nêu giả thiết.
- Không bao giờ nối thẳng một con số từ bảng chưa đầy đủ: soát bảng trước (skill `vn-ket-cau`).

## Lấy thép từ bản vẽ

Mẫu `rebar_quantities.py`:

```python
from vncad.struct import bar_weight

SO_TANG_DIEN_HINH = 3      # san tang 2, tang 3, san thuong cung mat bang ket cau
SO_DOAN_THANG = 3
D_RANH_GIOI = 10           # tach hai nhom dinh muc: D <= 10 va D > 10

def theo_duong_kinh(rows, he_so=1):
    nho = lon = 0.0
    for _, _, _, d, dai, sl, so in rows:
        kg = bar_weight(d, dai / 1000.0 * sl * so) * he_so
        nho, lon = (nho + kg, lon) if d <= D_RANH_GIOI else (nho, lon + kg)
    return nho, lon
```

Trong `build_dutoan.py`:

```python
THEP_NHO, THEP_LON = thep_than_nha()
("AF.622", "Cot thep dam cot san CB300-V (D lon hon 10mm), " + NGUON, "kg", round(THEP_LON, 1), 18500),
("AF.623", "Cot thep san va thep dai CB240-T (D tu 10mm tro xuong), " + NGUON, "kg", round(THEP_NHO, 1), 18000),
```

Chú ý nhãn nhóm đường kính: "D nhỏ hơn 10mm" bỏ sót đúng loại Ø10 dùng nhiều nhất; ghi
"D từ 10mm trở xuống".

## Xuất Excel

```python
from vncad.estimate import build_estimate
rows = [("SECTION", "PHAN I: PHAN NGAM VA MONG"),
        ("AB.111", "Ep coc BTCT 250x250, chieu sau ep 25m", "m dai", 750, 280000), ...]
build_estimate("out/DT-01.xlsx", project, rows, vat=0.08, overhead=0.06, contingency=0.05)
```

Module tự lo: phông Times New Roman toàn bộ, định dạng `#,##0`, công thức `=E*F` và `=SUM`, chi phí
chung, dự phòng, thuế GTGT. Không tự viết lại openpyxl; không gõ số vào ô thành tiền.

## Soát trước khi giao

- Đọc ngược file Excel bằng openpyxl: dòng thép bằng đúng số của `rebar_quantities`.
- Hàm lượng: thép khung 20 đến 45 kg/m² sàn; thép móng 50 đến 100 kg/m³ bê tông móng.
- Soát chéo bê tông, ván khuôn với kích thước cấu kiện trên bản vẽ; lệch lớn thì báo người dùng.
- Còn dòng nào gõ tay thì liệt kê trong báo cáo.

## Hai cách ước tính

1. **Bóc chi tiết theo đầu việc** khi đã có bản vẽ: khung đầu việc ở
   [references/danh-muc-cong-tac.md](references/danh-muc-cong-tac.md).
2. **Suất vốn trên m² sàn** khi mới có ý tưởng: hệ số quy đổi và đơn giá ở
   [references/don-gia-thi-truong.md](references/don-gia-thi-truong.md). Nói rõ sai số 10 đến 15%.

## Trung thực về con số

- Báo ba mức: thấp, giữa, cao. Một con số duy nhất luôn sai.
- Ghi mốc thời gian của đơn giá; nhắc hỏi báo giá nhà thầu trước khi ký hợp đồng.
- Khi số mới làm tổng giảm hay tăng mạnh, nói rõ chênh bao nhiêu và vì sao, trước khi người dùng
  tự phát hiện.

Căn cứ pháp lý: Nghị định 10/2021/NĐ-CP và Thông tư 12/2021/TT-BXD (định mức, công ty đang giữ) áp
cho dự toán lập trước 01/7/2026. Từ 01/7/2026, theo `E:\New folder\04-TieuChuan-PhapLy\00-DanhMucVanBan-ChiPhiDuToan_2026_v02.md`:
NĐ 206/2026/NĐ-CP, TT 36/2026/TT-BXD, TT 37/2026/TT-BXD. Kiểm tra văn bản còn hiệu lực tại thời
điểm lập; đấu thầu thì thêm căn cứ ở `vn-dau-thau/references/can-cu-phap-ly.md`.
