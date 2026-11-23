# CLAUDE.md — Không gian làm việc AI của Công ty TNHH Nghĩa Đạt

## Người dùng
- **Thành**: kỹ sư xây dựng, 15 năm kinh nghiệm, Công ty TNHH Nghĩa Đạt.
- Mảng: nhà ở, công trình dân dụng, cầu đường.
- Công việc: thiết kế bản vẽ, thi công, thầu vật tư, bóc tách khối lượng, đấu thầu, hồ sơ thanh toán.

## Cách làm việc
- Luôn trả lời bằng **tiếng Việt**, dùng đúng thuật ngữ ngành xây dựng Việt Nam.
- **Ngắn gọn, đi thẳng vào việc.** Chỉ giải thích khi được hỏi hoặc khi có điểm cần lưu ý.
- Anh Thành rành chuyên môn nhưng không phải lập trình viên. Khi viết script (LISP, Python...) thì nói rõ cách chạy, từng bước.
- Gặp số liệu không rõ hoặc thiếu (kích thước, mác bê tông, loại thép...) thì **hỏi lại, không tự đoán**. Nếu buộc phải giả định thì ghi rõ là giả định.

## Phạm vi công việc
1. **Bóc khối lượng, dự toán**: bóc từ bản vẽ, lập bảng vật tư, dự toán.
2. **Tự động hóa AutoCAD**: AutoLISP, Python, script để vẽ, sửa, thống kê bản vẽ.
3. **Hồ sơ thầu, thanh toán**: hồ sơ dự thầu, biên bản nghiệm thu, hồ sơ thanh quyết toán.
4. **Thiết kế, tính toán kết cấu**: tính toán, thuyết minh, kiểm tra theo tiêu chuẩn.

## Phần mềm đang dùng
AutoCAD, Excel, phần mềm dự toán Việt Nam (G8, Eta, Delta, Acitt...), Revit, Civil 3D, SAP2000, Etabs.

**Python 3.13** (`C:\Users\OS\AppData\Local\Programs\Python\Python313\`), đã cài sẵn các thư viện:
`openpyxl` (Excel), `pandas` (xử lý bảng), `ezdxf` (đọc/ghi DXF), `pywin32` (điều khiển AutoCAD, Excel qua COM), `python-docx` (Word).
Script dùng chung lưu trong `06-CongCu\`.

## Định mức, đơn giá, tiêu chuẩn
- Định mức: **Thông tư 12/2021/TT-BXD** và các thông tư sửa đổi, bổ sung.
- Địa bàn: **tỉnh Quảng Trị** (gồm địa bàn tỉnh Quảng Bình cũ, đã sáp nhập). Dùng đơn giá và công bố giá vật liệu của tỉnh Quảng Trị, trừ khi dự án quy định khác.
- Thiết kế, kiểm tra: theo **TCVN / QCVN** hiện hành.
- Văn bản pháp lý có thể đã thay đổi. Khi trích dẫn thông tư, nghị định, tiêu chuẩn thì ghi số hiệu và nhắc anh Thành kiểm tra lại hiệu lực.

## Quy tắc bóc khối lượng và lập bảng
- Mỗi hạng mục ghi rõ: **tên công việc, đơn vị, diễn giải cách tính, khối lượng**.
- Phần diễn giải phải ghi công thức cụ thể (VD: `2 x 0,22 x 0,3 x 4,5`) để dễ kiểm tra và đối chiếu.
- Sắp xếp theo trình tự thi công: móng → thân → hoàn thiện (hoặc theo hạng mục của hồ sơ mời thầu).
- Ghi mã hiệu định mức khi có thể, để nhập thẳng vào phần mềm dự toán.
- Số liệu: dấu phẩy là dấu thập phân (1.234,56). Đơn vị: m, m², m³, kg, tấn, cái, bộ...

## Đầu ra
- Bảng khối lượng, dự toán, thanh toán: xuất ra **file Excel (.xlsx)**, giữ nguyên **công thức** (không chỉ ghi số) để anh Thành sửa được.
- Tiêu đề bảng ghi: tên công trình, hạng mục, địa điểm, ngày lập, đơn vị lập (Công ty TNHH Nghĩa Đạt).

## Sắp xếp thư mục
Sơ đồ đầy đủ và mục đích từng thư mục xem trong **[00-index.md](00-index.md)**. Khi thêm hoặc đổi thư mục thì cập nhật file đó luôn.

```
E:\New folder\
├── 00-index.md  CLAUDE.md
├── _backup\                 ← bản sao an toàn
├── 01-DuAn\<TenDuAn>\       ← copy từ 01-DuAn\_MAU-DuAn\
│      01-HoSoGoc  02-BanVe  03-KhoiLuong  04-DuToan
│      05-HoSoThau  06-ThiCong  07-ThanhToan  08-KetCau
├── 02-ThuVien-CAD\          ← LISP, block, khung tên, .dwt, .ctb
├── 03-MauBieu\              ← mẫu Excel/Word
├── 04-TieuChuan-PhapLy\     ← TCVN, định mức, đơn giá Quảng Trị, công bố giá
├── 05-VatTu-NhaCungCap\     ← báo giá, hợp đồng vật tư
├── 06-CongCu\               ← script Python, macro
└── 99-LuuTru\               ← dự án đã quyết toán
```
- Tên dự án: `YYYY-<LoaiCT>_<Ten>_<DiaDiem>`, VD: `2026-NhaO_OngA_DongHoi`
- Tên thư mục và file: không dấu, không khoảng trắng, đánh số `01-`, `02-`...

## Quy tắc thiết kế bản vẽ AutoCAD

### Tiêu chuẩn tham chiếu (kiểm tra lại hiệu lực khi dùng)
- TCVN 7285:2003: khổ giấy và cách trình bày tờ vẽ
- TCVN 7286:2003: tỉ lệ
- TCVN 8-20:2002: nét vẽ
- TCVN 7284: chữ viết trên bản vẽ
- TCVN 5570:2012: ký hiệu đường nét và đường trục trong bản vẽ xây dựng
- TCVN 5571:2012: khung tên bản vẽ xây dựng
- TCVN 5572:2012: bản vẽ kết cấu bê tông và bê tông cốt thép

### File và phiên bản
- Lưu theo phiên bản AutoCAD đang dùng, không hạ phiên bản.
- Trước khi gửi file: chạy `PURGE` và `AUDIT`, dùng `ETRANSMIT` nếu có Xref hoặc ảnh chèn.
- Tên file: `<TenDuAn>_<BoMon>-<SoBV>_<TenBanVe>_v01.dwg`, VD: `NhaO_OngA_KC-03_MatBangDam_v01.dwg`

### Đơn vị
- Vẽ bằng **mm**: 1 đơn vị CAD = 1 mm. Vẽ **1:1** trong Model.
- Kích thước (dim) ghi bằng mm, không có số lẻ. Cao độ ghi bằng m, 3 số lẻ (VD: ±0.000, +3.600).

### Font chữ
- Dùng **Unicode**, font **Arial** (hoặc Times New Roman). Không dùng VNI hay TCVN3.
- Text style chuẩn:

| Style | Font | Chiều cao khi in | Dùng cho |
|---|---|---|---|
| CHU_2.5 | Arial | 2,5 mm | ghi chú, chữ trong dim |
| CHU_3.5 | Arial | 3,5 mm | tên chi tiết, tên mặt cắt |
| CHU_5 | Arial (đậm) | 5 mm | tên bản vẽ, tiêu đề |

- Chữ và dim đặt **Annotative** để tự đổi cỡ theo tỉ lệ viewport.

### Layer (bộ layer đề xuất cho công ty)
Quy tắc: `<BỘ MÔN>_<ĐỐI TƯỢNG>`, viết không dấu, chữ in hoa. Không vẽ trên layer `0` (chỉ dùng layer 0 khi tạo block).

| Layer | Màu | Nét | Dùng cho |
|---|---|---|---|
| KT_TRUC | 1 | CENTER | trục định vị |
| KT_TUONG | 4 | liền | tường bị cắt |
| KT_TUONG_NHIN | 8 | liền | tường, cạnh nhìn thấy |
| KT_CUA | 3 | liền | cửa đi, cửa sổ |
| KT_THIETBI | 8 | liền | thiết bị, nội thất |
| KT_HATCH | 8 | liền | mặt cắt vật liệu |
| KT_KHUAT | 2 | HIDDEN | nét khuất |
| KC_COT, KC_DAM, KC_SAN, KC_MONG | 4 | liền | cấu kiện kết cấu bị cắt |
| KC_THEP | 5 | liền | thép chủ (nét đậm) |
| KC_THEPDAI | 3 | liền | thép đai, thép phân bố |
| CD_TIMTUYEN | 1 | CENTER | tim tuyến đường, cầu |
| CD_MEPDUONG | 4 | liền | mép đường, mép cầu |
| DIM | 1 | liền | kích thước |
| CHU | 2 | liền | chữ, ghi chú |
| KYHIEU | 2 | liền | cao độ, mặt cắt, chỉ dẫn |
| KHUNG | 7 | liền | khung tên (ở Layout) |
| VIEWPORT | 8 | liền | khung viewport (đặt **No Plot**) |

Nếu một đối tượng không có trong bảng thì tạo layer mới theo đúng quy tắc tên, rồi báo lại để bổ sung vào đây.

### Nét in: theo màu, file `.ctb`
Bảng màu → độ dày nét in (đề xuất cho khổ A3, anh chỉnh theo file ctb của công ty):

| Màu | 1 đỏ | 2 vàng | 3 xanh lá | 4 xanh lơ | 5 xanh dương | 6 tím | 7 trắng | 8 xám | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Nét (mm) | 0,13 | 0,18 | 0,25 | 0,35 | 0,50 | 0,25 | 0,25 | 0,13 | 0,09 |

- Tất cả in ra **màu đen** (monochrome), trừ khi có yêu cầu in màu.
- Đặt màu cho đối tượng theo **ByLayer**, không gán màu trực tiếp cho từng đối tượng.

### Kích thước (dim)
- Dim style **Annotative**, chữ 2,5 mm (khi in), font Arial.
- Kiến trúc: đầu dim là **gạch xiên** (Architectural tick). Kết cấu, cầu đường: gạch xiên hoặc mũi tên đặc, thống nhất trong cùng một bộ hồ sơ.
- Ghi kích thước theo 3 lớp: chi tiết → trục → tổng.

### Trình bày: Model và Layout
- Vẽ 1:1 trong **Model**. Khung tên và trình bày in đặt ở **Layout**, mỗi tờ bản vẽ là một Layout.
- Viewport đặt đúng tỉ lệ và **khóa** (Display Locked = Yes).
- Tỉ lệ thường dùng:
  - Mặt bằng, mặt đứng, mặt cắt nhà ở: 1:100 (hoặc 1:50)
  - Mặt bằng tổng thể: 1:200 – 1:500
  - Chi tiết: 1:10, 1:20, 1:25
  - Cầu đường: bình đồ 1:500 – 1:1000; trắc dọc 1:1000 (ngang) / 1:100 (đứng); trắc ngang 1:100 – 1:200

### Khổ giấy
- Chủ yếu **A3** (420 × 297); **A4** (297 × 210) dùng cho chi tiết nhỏ, phụ lục, bảng biểu.
- Lề khung: trái 20 mm (để đóng gáy), các cạnh còn lại 5 mm.

### Khung tên (ở góc phải phía dưới)
Có các ô: **tên công ty (Công ty TNHH Nghĩa Đạt), chủ đầu tư, công trình, hạng mục, địa điểm, tên bản vẽ, ký hiệu bản vẽ, tỉ lệ, ngày**.
- Ký hiệu bản vẽ theo bộ môn: `KT-01` (kiến trúc), `KC-01` (kết cấu), `DN-01` (điện nước), `GT-01` (giao thông, cầu đường).
- Khung tên làm thành **block có Attribute** để điền nhanh và sửa hàng loạt. Lưu block mẫu trong `02-ThuVien-CAD\03-KhungTen\`.

## Đội agent (điều phối bởi phiên chính)
Phiên chính là người điều phối: giao việc, chuyển file giữa các agent, hỏi anh Thành khi thiếu số liệu. Agent không gọi được agent khác. Mỗi làn kết thúc bằng một agent **soát độc lập** (chỉ đọc, báo lỗi), không tự soát bài của mình. Sơ đồ: `.claude\doi-agent.html`.

| Làn | Việc | Agent theo thứ tự | Lệnh |
|---|---|---|---|
| A | Trình khách sơ bộ (chỉ chữ, chưa có bản vẽ) | `tiep-nhan` + `kien-truc` + `khoi-luong` (song song) → `kiem-tra` | `/trinh-khach` |
| B | Hồ sơ thiết kế thi công | `kien-truc-su` → `ky-su-ket-cau` + `ky-su-co-dien` → `kiem-soat-ban-ve`; tính toán: `ky-su-tinh-ket-cau` | `/ho-so-moi`, `/soat-ban-ve`, `/xuat-dwg` |
| C | Khối lượng, dự toán | `ky-su-boc-khoi-luong` → `kiem-tra-khoi-luong` → `ky-su-du-toan` | |
| D | Đấu thầu | `chuyen-vien-dau-thau` + `ky-su-du-toan` (song song) → `kiem-soat-hsdt` | `/doc-hsmt`, `/lap-hsdt`, `/soat-hsdt` |
| E | Thi công, thanh toán | `ky-su-thanh-toan` | |
| F | Công cụ AutoCAD | `ky-su-lisp-cad` | |
| G | Media (hình ảnh, video) | `giam-doc-media` (quản lý dự án media, tư vấn, soạn subagent từng mảng) → subagent mảng (chưa tạo, chờ anh Thành duyệt cơ cấu) | |

- Chọn đúng làn: `kien-truc`, `khoi-luong` thuộc làn A (ước tính bằng chữ, chỉ ghi file handoff); `kien-truc-su`, `ky-su-boc-khoi-luong` thuộc làn B, C (làm việc trên bản vẽ thật).
- Mỗi agent chỉ ghi vào phạm vi của mình, không sửa file của agent khác. Soát ra CẦN SỬA thì giao lại đúng agent bị nêu, tối đa 1 vòng.
- Việc gửi ra ngoài (nộp thầu, gửi khách, ký số, nộp hồ sơ thanh toán) luôn do anh Thành làm.

## Lưu ý an toàn
- **Không sửa đè hay xóa** file gốc (bản vẽ, hồ sơ đã ký). Muốn sửa thì tạo bản mới, VD: `..._v02.xlsx`.
- Thư mục `01-HoSoGoc\` của mỗi dự án: **chỉ đọc**, không sửa.
- **Trước khi sửa** file quan trọng, chép một bản vào `_backup\` (chia thư mục con theo dự án), tên bản sao: `YYYYMMDD-HHMM_<tên file gốc>`.
- **Không xóa, không sửa** file trong `_backup\`, trừ khi anh Thành cho phép.
- Trước khi chạy script sửa hàng loạt bản vẽ: sao lưu toàn bộ file liên quan vào `_backup\` trước.
