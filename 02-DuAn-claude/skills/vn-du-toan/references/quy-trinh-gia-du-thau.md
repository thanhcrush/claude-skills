# Chế độ B: bảng giá dự thầu (đấu thầu xây lắp)

Dùng khi lập phần **giá** của E-HSDT. Khác dự toán thường ở ba điểm:

| | Dự toán (chế độ A) | Giá dự thầu (chế độ B) |
|---|---|---|
| Khối lượng | Bóc từ bản vẽ của mình | **Lấy nguyên từ bảng khối lượng mời thầu**, không sửa |
| Cấu trúc bảng | Theo trình tự thi công | **Theo đúng mẫu E-HSMT**, đủ từng dòng |
| Đơn giá | Theo định mức, giá thị trường | Theo định mức + báo giá thật + **quyết định thương mại** (giảm giá) |
| Ràng buộc | Không | Không vượt giá gói thầu; khớp đơn dự thầu và webform |

Không dùng `don-gia-thi-truong.md` (giá TP.HCM) để chào giá. File đó chỉ để ước sơ bộ cho chủ đầu tư tư nhân.

## Đường dẫn

```
PY    = C:\Users\OS\AppData\Local\Programs\Python\Python313\python.exe
SKILL = E:\New folder\.claude\skills\vn-du-toan
```

Thư mục một gói thầu: `01-DuAn\<TenDuAn>\05-HoSoThau\03-Gia\` (theo skill `vn-dau-thau`).
Gói thầu chưa có thư mục thì tạo theo `vn-dau-thau` Bước 0, không tạo ở chỗ khác.

## Điều kiện vào

1. Anh Thành đã chốt **dự thầu** (`vn-dau-thau` Bước 3). Chưa chốt thì không lập giá.
2. Có E-HSMT gốc ở `01-HoSoGoc\` và bảng khối lượng mời thầu. Thiếu bảng khối lượng thì dừng, hỏi.
3. Đã đọc E-HSMT (`vn-dau-thau` Bước 1) và ghi lại các mục ở bước 1 dưới đây.

## Quy trình

### Bước 1: Rút từ E-HSMT những gì quyết định cách lập giá

Mỗi mục ghi **Chương, Mục, trang**. Mục nào E-HSMT không nói thì ghi `[Tài liệu không đề cập]`, không đoán.

- Giá gói thầu, và đã hay chưa gồm thuế GTGT, dự phòng.
- Loại hợp đồng và hình thức giá: đơn giá cố định, trọn gói, điều chỉnh. Quyết định ai chịu rủi ro trượt giá và khối lượng.
- Mẫu bảng giá dự thầu và cách ghi thuế, giảm giá. Cột sheet 01 mặc định gồm STT, mã, nội dung, ĐVT, khối lượng, đơn giá, thành tiền. **E-HSMT có mẫu khác thì theo E-HSMT**: sửa cột sheet 01 và 05, giữ nguyên công thức.
- E-HSMT có cho tách chi phí nhà tạm, dự phòng thành dòng riêng không.
- Cách áp dụng giảm giá (trên tổng hay từng dòng), hạn nộp thư giảm giá.
- Thời gian thực hiện, tạm ứng, thanh toán, bảo hành, bảo đảm thực hiện hợp đồng (để biết chi phí tài chính).

### Bước 2: Nhập bảng khối lượng mời thầu

Bảng khối lượng dạng Excel:

```bash
"$PY" "$SKILL\scripts\lap_gia_du_thau.py" boq "<BangKL_MoiThau.xlsx>" "<du_lieu.json>" --sheet "<tên sheet>" --dong-dau 2 --cot stt=A,ma=B,ten=C,dvt=D,kl=E
```

Dạng PDF: đọc bằng `doc_tai_lieu.py` (xem `vn-dau-thau` Bước 1), rồi gõ vào JSON, **mỗi dòng ghi `nguon_kl`** (Chương, Mục, tr. i/N). Sau khi nhập, đối chiếu số dòng và tổng từng nhóm với bản gốc.

File JSON mẫu: [du_lieu_mau.json](du_lieu_mau.json). Số trong mẫu là minh họa, thay hết.

### Bước 3: Đối chiếu khối lượng mời thầu với bản vẽ

Bóc nhanh các hạng mục chính từ bản vẽ E-HSMT (giao `ky-su-boc-khoi-luong`, ghi vào file riêng, **không đưa vào bảng giá**). Lệch lớn, thiếu dòng so với bản vẽ, hạng mục có trong bản vẽ mà bảng khối lượng không có:

- **Không sửa khối lượng mời thầu** (checklist D2).
- Đưa vào **câu hỏi làm rõ E-HSMT** trước hạn (`vn-dau-thau` sheet 6).
- Hạng mục thiếu dòng: hỏi xem tính vào dòng nào. Nếu E-HSMT trả lời "đã tính vào dòng khác" thì tính chi phí đó vào đơn giá dòng ấy và ghi vào cột nguồn.

### Bước 4: Đơn giá trực tiếp

Với mỗi dòng, điền **vật liệu, nhân công, máy** trên một đơn vị vào sheet 02. Nguồn đơn giá theo thứ tự ưu tiên:

1. F1 hoặc phần mềm dự toán của công ty: xuất VL, NC, M theo dòng. Bộ định mức, giá nhân công, ca máy, vùng: theo `lap-du-toan` mục 2 và 3. **Hỏi anh Thành chọn bộ định mức** (TT 12/2021 hay TT 38/2026) rồi ghi trong thuyết minh giá.
2. Báo giá nhà cung cấp, thầu phụ (`05-VatTu-NhaCungCap\`): ghi tên, ngày báo giá.
3. Công bố giá vật liệu Sở Xây dựng Quảng Trị kỳ gần nhất: ghi kỳ.

Quy tắc:

- Giá không tách VL/NC/M (báo giá trọn gói) thì **gộp vào cột Vật liệu**.
- **Không có đơn giá thì để trống** (ô vàng, sheet 04 báo LỖI LOẠI). Không điền số đoán, không điền 0.
- Dòng đơn giá bằng 0 chỉ khi E-HSMT cho phép và có ghi chú. Sheet 04 gắn cờ RỦI RO.
- Giá nhân công đang dùng **GIẢ ĐỊNH tạm** (QĐ 16/QĐ-SXD, `lap-du-toan` mục 3) thì ghi vào cột nguồn từng dòng nhân công, và nhắc trong báo cáo.
- Cột "Đơn giá tham chiếu" (tùy chọn): đơn giá tỉnh hoặc đơn giá dự toán chủ đầu tư, để phát hiện dòng bị chào quá thấp.

### Bước 5: Tỷ lệ chi phí

Điền vào `ty_le` của JSON, **mỗi tỷ lệ kèm nguồn**. Không có giá trị mặc định trong script.

| Khoản mục | Lấy ở đâu |
|---|---|
| Chi phí chung, thu nhập chịu thuế tính trước, công việc không xác định KL, nhà tạm | `lap-du-toan` mục 4 (TT 36/2026, đã đối chiếu bản gốc) hoặc theo E-HSMT nếu E-HSMT quy định khác |
| Thuế GTGT | Mức và căn cứ theo E-HSMT và văn bản hiện hành (`lap-du-toan` mục 0) |
| Giảm giá | **Giám đốc quyết định.** Để 0 cho tới khi anh Thành chốt |

Công thức đơn giá dự thầu mỗi dòng (sheet 02), làm tròn đồng:

```
T  = VL + NC + M
C  = T x chi phí chung            TT = T x công việc không xác định KL (nếu có)
TL = (T + C + TT) x thu nhập chịu thuế tính trước
Đơn giá dự thầu = ROUND(T + C + TT + TL, 0)       Thành tiền = ROUND(KL x Đơn giá, 0)
```

Tổng hợp (sheet 03): Σ thành tiền, trừ giảm giá, cộng thuế GTGT, cộng nhà tạm nếu E-HSMT cho tách. Công thức nhà tạm theo `lap-du-toan` mục 4.

Chỗ E-HSMT yêu cầu cấu trúc khác (đơn giá đã gồm thuế, không tách chi phí chung...) thì sửa công thức trong sheet 02 và 03 cho khớp E-HSMT, ghi lại chỗ đã sửa, rồi chạy bước 7.

### Bước 6: Quyết định giá (anh Thành duyệt)

AI **không tự chốt giá dự thầu**. Làm như sau:

1. Điền ba tỷ lệ giảm giá vào `kich_ban_giam_gia` (thấp, giữa, cao do anh Thành cho, hoặc hỏi) rồi xuất.
2. Sheet 03 cho từng kịch bản: giá dự thầu, lợi nhuận trước thuế, % lợi nhuận trên giá thành, tỷ lệ so giá gói thầu.
3. Báo anh Thành theo mẫu cuối file, kèm rủi ro theo loại hợp đồng: trọn gói và đơn giá cố định thì trượt giá do mình chịu; kèm các dòng giá thấp bất thường; kèm các dòng dùng giả định.
4. Lợi nhuận âm: nói thẳng "chào dưới giá thành", không tự điều chỉnh.

### Bước 7: Xuất, soát, giao

```bash
"$PY" "$SKILL\scripts\lap_gia_du_thau.py" xuat "<du_lieu.json>" "<...>\05-HoSoThau\03-Gia\BangGiaDuThau_v01.xlsx"
"$PY" "$SKILL\scripts\kiem_gia_du_thau.py" "<...>\05-HoSoThau\03-Gia\BangGiaDuThau_v01.xlsx"
```

- Lưu file JSON cạnh file Excel để lần sau sửa tiếp. File đã có thì tăng `_v02`, script không ghi đè.
- Lập trong thư mục tạm trước, soát xong mới chép sang `03-Gia\` (`cp -n`).
- `kiem_gia_du_thau.py` mở file bằng Excel, tính lại, đối chiếu với Python, in giá dự thầu **bằng số và bằng chữ** để dán vào đơn dự thầu. Không có Excel thì script nói rõ là chưa kiểm được công thức.
- Sheet 04 phải hết LỖI LOẠI. Còn thì chưa được báo xong.
- Giao `kiem-soat-hsdt` soát độc lập (mục D của `vn-dau-thau/references/checklist-loi-bi-loai.md`).
- Sheet 05 là phiếu nhập webform phần giá: anh Thành gõ theo, số liên kết từ sheet 01. Ghi giá dự thầu ở sheet 03 vào đơn dự thầu, kiểm khớp từng số (checklist A1, D3, E4).
- Việc nộp thầu, ký số do anh Thành làm.

### Bước 8: Sau khi có kết quả

Ghi giá mình chào, giá trúng, tỷ lệ so giá gói thầu vào `vn-dau-thau/references/bai-hoc-dau-thau.md` (3 đến 5 dòng).

## Việc không làm

- Sửa, gộp, tách, bỏ dòng của bảng khối lượng mời thầu.
- Điền đơn giá, tỷ lệ, giá gói thầu không có nguồn.
- Tự chốt tỷ lệ giảm giá hoặc giá dự thầu cuối.
- Dùng đơn giá của dự án khác mà không đối chiếu kỳ giá, vùng, bộ định mức.
- Gửi, nộp, ký số.

## Báo cáo cho anh Thành (trong chat)

```
**Gói thầu:** <tên> · **Đóng thầu:** <ngày giờ> · **Giá gói thầu:** <số> đ (đã/chưa gồm thuế theo E-HSMT)
**Loại hợp đồng:** <...>  → rủi ro: <ai chịu trượt giá, khối lượng>
**Giá dự thầu:** thấp <số> / giữa <số> / cao <số> (đã gồm thuế), so giá gói thầu <%>
**Lợi nhuận trước thuế:** <số> (<% giá thành>) ở mức giữa
**Dòng thiếu đơn giá:** <n, mã dòng>   **Dòng dùng giả định:** <...>   **Dòng giá thấp bất thường:** <...>
**Chênh khối lượng mời thầu so bản vẽ → câu hỏi làm rõ:** <n câu>
**Cần anh quyết:** tỷ lệ giảm giá; bộ định mức; <các chỗ CHƯA RÕ>
**File:** <đường dẫn tuyệt đối> · **Soát 04:** <tình trạng>
**Văn bản đã nhắc, cần kiểm tra lại hiệu lực:** <...>
```
