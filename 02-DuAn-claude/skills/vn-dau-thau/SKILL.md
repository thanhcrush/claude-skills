---
name: vn-dau-thau
description: Quy trình phòng Đấu thầu của Công ty TNHH Nghĩa Đạt, dùng cho gói thầu xây lắp qua mạng. Gồm đọc và phân tích E-HSMT, đối chiếu với hồ sơ năng lực công ty, chấm Go/No-go, lập kế hoạch, lập E-HSDT (thuyết minh biện pháp thi công, tiến độ, bảng kê nhân sự, thiết bị, hợp đồng tương tự, dữ liệu nhập webform), soát lỗi trước khi nộp. Dùng khi anh Thành đưa hồ sơ mời thầu, hỏi có nên dự thầu không, cần lập hoặc soát hồ sơ dự thầu, hoặc cần câu hỏi làm rõ E-HSMT.
---

# Phòng Đấu thầu: quy trình gói thầu xây lắp

## Đường dẫn

```
PY    = C:\Users\OS\AppData\Local\Programs\Python\Python313\python.exe
SKILL = E:\New folder\.claude\skills\vn-dau-thau
DOC   = E:\New folder\.claude\skills\soat-ho-so-ky-thuat\scripts\doc_tai_lieu.py   (dùng chung để đọc E-HSMT)
HSNL  = E:\New folder\03-MauBieu\03-HoSoThau\01-HoSoNangLuc\HoSoNangLuc_NghiaDat_v01.xlsx
```

Thư mục một gói thầu: `01-DuAn\<TenDuAn>\05-HoSoThau\`, gồm:

| Thư mục con | Chứa gì |
|---|---|
| `01-PhanTich` | Bảng phân tích E-HSMT (Excel), JSON nguồn, câu hỏi làm rõ |
| `02-KyThuat` | Thuyết minh biện pháp thi công (Word), tiến độ (Excel), sơ đồ tổ chức |
| `03-Gia` | Bảng giá dự thầu, bảng phân tích đơn giá (do phòng Dự toán lập) |
| `04-NangLuc` | Bảng kê nhân sự, thiết bị, hợp đồng tương tự, tài chính, bản scan chứng minh |
| `05-NopThau` | Bản cuối cùng đã nộp, biên bản mở thầu. **Sau khi nộp: chỉ đọc.** |

E-HSMT gốc để ở `01-HoSoGoc\` (chỉ đọc, không sửa).

## Nguyên tắc bắt buộc

1. **E-HSMT của chính gói thầu là căn cứ số một.** Luật, nghị định chỉ dùng để hiểu và để phát hiện điều khoản bất thường. Căn cứ pháp lý: xem `references/can-cu-phap-ly.md`. Luôn nhắc anh Thành kiểm tra lại hiệu lực.
2. **Không bịa năng lực.** Hợp đồng tương tự, nhân sự, thiết bị, số liệu tài chính **chỉ lấy từ HSNL** hoặc tài liệu anh Thành đưa. Thiếu thì ghi `CHƯA RÕ` và hỏi. Kê khai sai sự thật trong E-HSDT là hành vi gian lận bị cấm (Luật Đấu thầu), bị loại và có thể bị cấm tham dự thầu.
3. **Không tự sửa khối lượng mời thầu.** Thấy khối lượng sai thì đưa vào câu hỏi làm rõ, hoặc làm theo cách E-HSMT cho phép (bảng khối lượng chênh lệch nếu có).
4. **Mọi con số có trích dẫn**: `Chương, Mục, tr. i/N` của file E-HSMT.
5. **AI không nộp thầu.** Không đăng nhập Hệ thống mạng đấu thầu quốc gia, không dùng chứng thư số, không mở bảo lãnh. Anh Thành làm các việc này. Phòng Đấu thầu chuẩn bị sẵn **phiếu nhập webform** để anh chỉ việc gõ theo.
6. File đầu ra: Excel giữ công thức, Word Times New Roman. Không ghi đè: tăng `_v02`, `_v03`.

## Quy trình 6 bước

### Bước 0: Chuẩn bị
- Có dự án chưa? Chưa thì copy `01-DuAn\_MAU-DuAn\` thành `01-DuAn\<YYYY-LoaiCT_Ten_DiaDiem>\`.
- HSNL có chưa? Chưa thì tạo mẫu trống rồi **dừng lại nhờ anh Thành điền** (ít nhất sheet 1, 2, 4, 5):
  ```bash
  "$PY" "$SKILL/scripts/tao_ho_so_nang_luc.py" "$HSNL"
  ```
  HSNL có rồi thì đọc bằng openpyxl (data_only=False để thấy cả công thức). Cột "Còn hạn" tính theo ngày mở file; tự tính lại hạn chứng chỉ theo **ngày đóng thầu**.

### Bước 1: Đọc E-HSMT
```bash
"$PY" "$DOC" "<E-HSMT.pdf>" ["<phu_luc...>"] [--anh]
```
Đọc **toàn bộ** text sinh ra, không đọc lướt. Bản vẽ, bảng khối lượng lộn xộn thì chạy lại với `--anh` và xem ảnh.
Cấu trúc E-HSMT xây lắp thường gồm: chỉ dẫn nhà thầu, bảng dữ liệu đấu thầu, tiêu chuẩn đánh giá, biểu mẫu dự thầu, yêu cầu kỹ thuật và bảng khối lượng, điều kiện hợp đồng, mẫu hợp đồng. Tên và số chương theo đúng E-HSMT đang đọc.

Phải bóc ra được:
- Thông tin gói thầu, **thời điểm đóng thầu**, hiệu lực E-HSDT, giá trị và hiệu lực bảo đảm dự thầu, giá gói thầu, thời gian thực hiện, loại hợp đồng.
- **Từng tiêu chí** đánh giá: tư cách hợp lệ, năng lực kinh nghiệm (lịch sử hợp đồng, thuế, tài chính, doanh thu, nguồn lực tài chính, hợp đồng tương tự), nhân sự chủ chốt, thiết bị, kỹ thuật (đạt/không đạt hoặc chấm điểm), phương pháp đánh giá giá.
- Điều kiện hợp đồng có rủi ro: tạm ứng, thanh toán, điều chỉnh giá, phạt chậm tiến độ, bảo lãnh thực hiện, bảo hành.
- Chỗ mâu thuẫn, bỏ trống, khối lượng nghi sai, yêu cầu có dấu hiệu hạn chế cạnh tranh (chỉ định nhãn hiệu, yêu cầu năng lực vượt quá quy mô gói thầu).

### Bước 2: Lập bảng phân tích
1. Viết JSON theo mẫu `references/phan_tich_mau.json` (đọc mẫu trước). Mỗi tiêu chí E-HSMT là **một dòng** `yeu_cau`, không gộp.
2. Đối chiếu từng dòng với HSNL, ghi `dap_ung` cụ thể (tên HĐ, giá trị, số chứng chỉ, hạn...). Trạng thái chỉ dùng 4 mức:
   - `ĐẠT`: HSNL chứng minh được, có file.
   - `CẦN BỔ SUNG`: có năng lực nhưng thiếu giấy tờ chứng minh hoặc sắp hết hạn trước ngày đóng thầu.
   - `CHƯA RÕ`: HSNL không có dữ liệu, cần anh Thành trả lời.
   - `CHƯA ĐẠT`: dữ liệu cho thấy không đáp ứng (có thể tính liên danh hoặc thầu phụ, ghi rõ).
3. `ke_hoach`: tính lùi từ ngày đóng thầu. Mở bảo lãnh, xin xác nhận hợp đồng cũ cần nhiều ngày thì đặt sớm.
4. `danh_muc_nop`: liệt kê đủ tài liệu và webform E-HSMT yêu cầu.
5. Sinh Excel, lưu vào scratchpad trước, soát xong mới chép sang `05-HoSoThau\01-PhanTich\` (`cp -n`):
   ```bash
   "$PY" "$SKILL/scripts/phan_tich_hsmt.py" "<du_lieu.json>" "<...>/PhanTichHSMT_<GoiThau>_v01.xlsx"
   ```
   Lưu cả file JSON cạnh file Excel để lần sau sửa tiếp.

### Bước 3: Go/No-go và chờ Giám đốc quyết định
- Chấm 8 tiêu chí mặc định (hoặc bộ tiêu chí anh Thành đã chỉnh), điểm 1 đến 5, **mỗi điểm có căn cứ**. Tiêu chí về giá và lợi nhuận mà chưa có dự toán thì để trống, ghi "chờ ước tính giá".
- Báo cáo trong chat theo mẫu ở cuối file này, rồi **dừng lại**. Chỉ làm tiếp Bước 4 khi anh Thành nói dự thầu.

### Bước 4: Lập E-HSDT
Chia việc (phiên chính điều phối, các agent không tự gọi nhau):

| Phần | Ai làm | Đầu ra |
|---|---|---|
| Bảng giá dự thầu theo bảng khối lượng mời thầu | `ky-su-du-toan` (skill `vn-du-toan`, **chế độ B**) | `03-Gia\BangGiaDuThau_v01.xlsx` |
| Thuyết minh biện pháp tổ chức thi công | `chuyen-vien-dau-thau` | `02-KyThuat\ThuyetMinhBPTC_v01.docx` |
| Tiến độ thi công | `chuyen-vien-dau-thau` | `02-KyThuat\TienDo_v01.xlsx` (Excel, cột ngày có công thức) |
| Bảng kê nhân sự, thiết bị, hợp đồng tương tự, tài chính | `chuyen-vien-dau-thau` | `04-NangLuc\...` lấy đúng từ HSNL |
| Phiếu nhập webform (đơn dự thầu, các bảng kê) | `chuyen-vien-dau-thau` | `05-NopThau\PhieuNhapWebform_v01.xlsx` |
| Mở bảo lãnh, ký số, nộp | **Anh Thành** | |

Thuyết minh: viết Markdown theo `references/cau-truc-thuyet-minh-bptc.md`, rồi chuyển Word và xem ảnh từng trang:
```bash
"$PY" "$SKILL/scripts/md_sang_docx.py" "<ban_thao.md>" "<file.docx>" --kiem-tra
```

### Bước 5: Soát trước khi nộp
Giao `kiem-soat-hsdt` soát độc lập theo `references/checklist-loi-bi-loai.md`. Còn lỗi mức **LOẠI** thì chưa được báo xong.

### Bước 6: Sau khi nộp
- Anh Thành gửi biên bản mở thầu và kết quả: lưu `05-NopThau\`, cập nhật HSNL (nhân sự và thiết bị đang huy động).
- Trượt hoặc trúng đều ghi 3 đến 5 dòng rút kinh nghiệm vào `references/bai-hoc-dau-thau.md` (giá trúng so với giá mình, lý do loại, đối thủ).

## Mẫu báo cáo Go/No-go (trong chat)

```
**Gói thầu:** <tên> · **Đóng thầu:** <ngày giờ> (còn N ngày) · **Giá gói thầu:** <số> đ
**Kết luận sơ bộ:** NÊN DỰ THẦU / CÂN NHẮC / KHÔNG NÊN / KHÔNG ĐỦ ĐIỀU KIỆN  (điểm xx/100)

**Yêu cầu CHƯA ĐẠT:** <liệt kê, trích dẫn, hướng xử lý: liên danh, thầu phụ, bỏ>
**Cần anh Thành trả lời (CHƯA RÕ):** <câu hỏi ngắn, trả lời được bằng có/không hoặc một con số>
**Rủi ro hợp đồng:** <tạm ứng, thanh toán, phạt, điều chỉnh giá>
**Câu hỏi làm rõ E-HSMT đề xuất gửi:** <n câu, xem sheet 6>
**Việc gấp nhất:** <3 việc, hạn>
**File:** <đường dẫn tuyệt đối .xlsx>
**Văn bản pháp lý đã nhắc, cần kiểm tra lại hiệu lực:** <...>
```
