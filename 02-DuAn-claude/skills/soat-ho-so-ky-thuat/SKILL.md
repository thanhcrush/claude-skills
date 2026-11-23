---
name: soat-ho-so-ky-thuat
description: Dùng khi cần rà soát chỉ dẫn kỹ thuật, đối chiếu mâu thuẫn giữa bản vẽ và thuyết minh, lập ma trận nghiệm thu vật tư và sinh phiếu RFI.
---

# Rà soát hồ sơ kỹ thuật → Ma trận nghiệm thu → Phiếu RFI

Anh Thành đưa vào một hoặc nhiều hồ sơ (chỉ dẫn kỹ thuật, thuyết minh, bản vẽ, bảng thống kê...). Chạy **trọn quy trình trong một lượt**, không hỏi lại từng bước. Kết quả gồm **5 phần trong chat** và **1 file Word phiếu RFI**.

Chỉ hỏi lại trước khi chạy khi **không đọc được file**, ví dụ file chưa đính kèm, sai đường dẫn, hoặc là file `.dwg`. Mọi chỗ còn thiếu khác thì ghi "Tài liệu không đề cập" rồi đưa vào câu hỏi của phiếu RFI, **không dừng lại để hỏi**.

## Đường dẫn

```
PY    = C:\Users\OS\AppData\Local\Programs\Python\Python313\python.exe
SKILL = E:\New folder\.claude\skills\soat-ho-so-ky-thuat
```

## Quy trình

### Bước 1: Đọc tài liệu và đánh dấu vị trí trích dẫn

```bash
"$PY" "$SKILL/scripts/doc_tai_lieu.py" "<file1>" "<file2>" ...
```

- Kết quả nằm ở `%TEMP%\soat_ho_so\<ten_file>.txt`. Mỗi trang mở đầu bằng dòng `===== [ten_file] TRANG i/N =====`. Đọc **toàn bộ** các file này, không đọc lướt.
- Script tự in ra 3 loại cảnh báo. Mọi cảnh báo phải được đưa vào báo cáo:
  - **Trang không có lớp chữ** (bản scan): dùng Read để xem ảnh PNG mà script đã render. Không có OCR, nên chữ nào đọc không rõ thì ghi "không đọc được".
  - **Số trang in trên tài liệu khác số trang thực của file** (ví dụ tài liệu in "Trang 1/2" nhưng file chỉ có 1 trang): ghi là **file thiếu trang** và đưa thành một câu hỏi trong RFI.
  - **Số trang nội bộ** (ví dụ "(Trang 42)"): khi trích dẫn ghi cả hai loại số trang.
- Bản vẽ hoặc bảng biểu bị trích text lộn xộn: chạy lại với cờ `--anh` rồi xem ảnh để đọc cho đúng hàng, cột.
- File `.doc`, `.xls` đời cũ hoặc `.dwg`: báo anh Thành chuyển sang `.docx`, `.xlsx`, PDF, hoặc để Claude xuất PDF bằng skill `vn-xuat-autocad`.

### Bước 2: Xác định đối tượng rà soát
- Nếu anh Thành chỉ tên hạng mục hoặc ký hiệu (ví dụ "cửa D-08") thì tập trung vào đối tượng đó.
- Nếu không chỉ rõ: rà soát **mọi hạng mục có quy cách vật tư** trong tài liệu. Hạng mục nào có mâu thuẫn giữa các tài liệu thì ưu tiên trình bày trước.
- Tìm **điều khoản ưu tiên pháp lý** (ví dụ "chỉ dẫn kỹ thuật ưu tiên hơn bản vẽ") và **điều khoản chế tài** (ai chịu chi phí khi sai). Hai loại này quyết định mức rủi ro ở Phần 3.

### Bước 3: Viết 5 phần trong chat, đúng mẫu ở mục "Mẫu xuất kết quả"

### Bước 4: Sinh file Word phiếu RFI
1. Viết file JSON theo đúng cấu trúc `references/rfi_mau.json`. Mẫu này là vụ cửa D-08 GreenTech, nên đọc nó trước khi viết. Ghi JSON vào thư mục scratchpad.
2. Chạy, **sinh file vào scratchpad trước**, chưa ghi ra thư mục đích:
   ```bash
   "$PY" "$SKILL/scripts/tao_rfi.py" "<du_lieu.json>" "<scratchpad>/<file_ra.docx>" --kiem-tra
   ```
3. Dùng Read xem **từng ảnh PNG** mà `--kiem-tra` in ra. Kiểm tra các lỗi: chữ trong phần đầu văn bản bị xuống dòng, bảng bị tách một dòng sang trang sau, ô bảng quá hẹp (ví dụ cột STT dưới 1,2 cm sẽ làm tiêu đề "STT" bị ngắt dòng), phần ký tên bị cắt. Có lỗi thì sửa JSON (ví dụ `rong_cm`, `giu_lien`, câu ngắn lại), xóa file nháp trong scratchpad rồi sinh lại. Khi bố cục đạt mới chép file sang thư mục đích (`cp -n`, không ghi đè).
4. **Đặt tên và lưu file:**
   - Tên file: `RFI-<BoMon>-<NNN>_<NoiDungNgan>_v01.docx`, không dấu. Bộ môn ghi là ARC (kiến trúc), STR (kết cấu), MEP (cơ điện) hoặc CIV (giao thông).
   - Có thư mục dự án `01-DuAn\<TenDuAn>\` thì lưu vào `05-HoSoThau\` (giai đoạn đấu thầu) hoặc `06-ThiCong\` (giai đoạn thi công).
   - Chưa có thư mục dự án thì lưu cạnh file nguồn, và báo anh Thành.
   - **Không ghi đè file cũ.** Script tự từ chối nếu file đã tồn tại; khi đó tăng lên `_v02`, `_v03`.
5. Gửi file cho anh Thành bằng SendUserFile.

Thể thức mà script đã làm sẵn, theo NĐ 30/2020/NĐ-CP: khổ A4; font Times New Roman; lề trên và dưới 20 mm, trái 30 mm, phải 15 mm; tên đơn vị kèm số ký hiệu ở bên trái, Quốc hiệu và tiêu ngữ ở bên phải; địa danh, ngày tháng; tên loại văn bản và trích yếu; Kính gửi; nội dung đánh số La Mã; Nơi nhận; chữ ký; khung xác nhận và phản hồi của bên nhận; số trang ở lề trên, bắt đầu từ trang 2.

## Mẫu xuất kết quả (bắt buộc đủ 5 phần, theo đúng thứ tự)

Mở đầu bằng **2–3 dòng kết luận**: số điểm sai lệch, mức rủi ro, chi phí chênh lệch nếu tính được, và đường dẫn file RFI.

### PHẦN 1: TÓM TẮT QUY CÁCH VẬT TƯ & THÔNG SỐ CỐT LÕI
- Nhóm theo cấu phần: phạm vi áp dụng, vật liệu chính, cấu tạo, phụ kiện, hồ sơ, nghiệm thu.
- Bóc **đúng con số và đơn vị** của tài liệu (ví dụ 1,5 mm; ≥ 120 kg/m³; ≥ 04 bản lề/cánh). **Không** viết chung chung kiểu "thép dày theo thiết kế".
- Mỗi dòng có vị trí trích dẫn ngắn, ví dụ `(Đ.5.3 k.2, tr. 2/3)`.
- Cuối phần này liệt kê các chỗ **tài liệu bỏ trống hoặc chưa rõ**: dung sai, cách hiểu chỉ tiêu, tiêu chuẩn còn thiếu, chỉ định nhãn hiệu...

### PHẦN 2: MA TRẬN YÊU CẦU NGHIỆM THU
Bảng **6 cột**, mỗi cấu phần một dòng. Không gộp nhiều chỉ tiêu khác nhau vào một ô.

| STT | Hạng mục / Cấu phần | Quy cách kỹ thuật yêu cầu | Tiêu chuẩn viện dẫn (TCVN / QCVN) | Hồ sơ / Chứng chỉ thí nghiệm nghiệm thu bắt buộc | Vị trí trích dẫn (Tên file, Mục, Số trang) |
|---|---|---|---|---|---|

- **Cột 4:** chỉ ghi tiêu chuẩn **mà tài liệu có viện dẫn**, ghi đủ số hiệu và năm. Tiêu chuẩn nước ngoài (EN, BS, ASTM...) thì ghi rõ là tiêu chuẩn nước ngoài. Tài liệu không viện dẫn thì ghi `Tài liệu không đề cập`.
- **Cột 5:** chỉ ghi hồ sơ **mà tài liệu yêu cầu**: GCN kiểm định, biên bản thí nghiệm, CO/CQ, lấy mẫu tại công trường, v.v. Không có thì ghi `Không quy định riêng`.
- **Cột 6:** ghi `<tên file>, Mục x, Điều y, khoản z, tr. i/N`, kèm số trang nội bộ nếu có. Cho phép ghi tên file đầy đủ một lần ở đầu bảng và viết tắt trong các ô.
- Đưa cả các dòng về **phạm vi áp dụng**, **điều cấm**, **nguyên tắc ưu tiên pháp lý** và **chế tài khi nghiệm thu**, không chỉ các dòng vật tư.

### PHẦN 3: BẢNG ĐỐI CHIẾU MÂU THUẪN

**3.1. Bảng đối chiếu**

| STT | Chỉ tiêu | Tài liệu A: trích + vị trí (file, mục, tr.) | Tài liệu B: trích + vị trí (file, mục, tr.) | Sai lệch (định lượng) | Đánh giá |
|---|---|---|---|---|---|

- **Cột "Sai lệch":** ghi bằng số, ví dụ "−20 kg/m³ (−16,7%)", "thiếu 01 bản lề/cánh", "thấp hơn 30 phút".
- **Cột "Đánh giá":** chỉ dùng 4 mức: ❌ Không đạt, ⚠️ Chưa rõ, ⚠️ Thiếu, ✅ Khớp. Giữ cả các dòng ✅ Khớp để chứng minh đã soát đủ.
- **Khi chỉ có 1 tài liệu:** đối chiếu nội bộ giữa các mục trong tài liệu, và ghi rõ "Chỉ có 1 tài liệu, chưa đối chiếu chéo".
- **Chỗ tài liệu tự mâu thuẫn:** ví dụ một chỉ tiêu ghi "thép mạ điện" ở chỗ này, "mạ kẽm" ở chỗ khác. Đưa vào bảng.

**3.2. Đánh giá rủi ro nghiệm thu**
- Chỉ dùng 3 mức: RẤT CAO, TRUNG BÌNH, THẤP.
- Nêu rõ **bên chịu rủi ro**.
- Căn cứ phải là **điều khoản cụ thể trong tài liệu**: ưu tiên pháp lý, điều cấm, lấy mẫu kiểm tra, chế tài.
- Nếu tài liệu có dấu hiệu cho thấy mâu thuẫn **đã được biết trước** (ví dụ ghi chú QS có cảnh báo) thì nêu ra.
- Kết thúc bằng danh sách **việc cần làm ngay**.

**3.3. Chênh lệch chi phí**
- **Chỉ dùng đơn giá có trong tài liệu.** Bảng gồm các cột: phương án, diễn giải (ví dụ `10 × 1,2 × 2,2 = 26,4`), đơn giá, thành tiền. Thêm dòng chênh lệch tuyệt đối, %, và chênh lệch trên 1 đơn vị.
- Thêm kịch bản **"làm sai rồi phải làm lại"** (chi phí đã bỏ ra + chi phí làm mới), và ghi rõ những khoản chưa tính.
- Muốn ngoại suy cho toàn công trình thì phải ghi **GIẢ ĐỊNH** và nêu rõ giả định là gì.
- Tài liệu không có đơn giá: ghi `Tài liệu không đề cập đơn giá`, rồi đề nghị anh Thành gửi báo giá. **Không tự đưa ra giá thị trường.**
- Phải hỏi lại xem đơn giá **đã gồm những gì**: VAT, lắp đặt, phụ kiện, kiểm định.

### PHẦN 4: DỰ THẢO PHIẾU RFI LÀM RÕ
- Tóm tắt phiếu trong chat: số hiệu, trích yếu, nơi gửi, **các đề xuất**, **danh sách câu hỏi**.
- Ghi đường dẫn file Word đã sinh ở Bước 4.
- Liệt kê **các chỗ còn để trống** (ngày ký, thời hạn trả lời, người ký) và **các giả định trong phiếu** (địa danh, số hiệu, vai trò Nhà thầu, nơi nhận, tên pháp nhân nếu các tài liệu ghi khác nhau).
- **Câu hỏi RFI** lấy từ: mọi dòng ⚠️ ở Phần 3, các chỗ bỏ trống ở Phần 1, file thiếu trang, chỉ định nhãn hiệu, cách hiểu chỉ tiêu mơ hồ, và cách xử lý chi phí.
- **Giọng văn** trung tính, lễ độ, không quy lỗi. Dùng "Nhà thầu kính đề nghị...". Mỗi câu hỏi phải trả lời được bằng "có hoặc không", hoặc bằng một con số.

### PHẦN 5: QUY TẮC CHỐNG BỊA
Liệt kê trong chat để anh Thành kiểm tra nhanh:
1. **Thông tin tài liệu không đề cập:** các mục ghi "Tài liệu không đề cập", đặc biệt những câu anh Thành hỏi mà tài liệu không có.
2. **Số liệu do Claude tự tính:** ghi kèm công thức, ví dụ `50 − 2×1,2 − 2×5 ≈ 37,6 mm`.
3. **Giả định:** những gì đã giả định, và vì sao.
4. **Gợi ý ngoài tài liệu:** ví dụ tiêu chuẩn EN 1935, EN 1125. Ghi rõ "gợi ý, không có trong tài liệu".
5. **Văn bản pháp lý cần anh Thành kiểm tra lại hiệu lực:** thông tư, nghị định, TCVN, QCVN đã nhắc tới.

## Quy tắc chống bịa (bắt buộc, áp dụng cho cả 5 phần và file RFI)
1. **Tài liệu không nói thì ghi đúng câu `Tài liệu không đề cập`.** Không suy từ kinh nghiệm, không lấy thông tin từ tiêu chuẩn khác để lấp chỗ trống. Ví dụ: hỏi mức phạt giao chậm mà tài liệu chỉ có chế tài khi sai chất lượng, thì trả lời "Tài liệu không đề cập", rồi nói rõ điều khoản gần nhất mà tài liệu thực sự có.
2. **Mỗi con số đều kèm vị trí trích dẫn**: tên file, mục hoặc điều, khoản, trang theo dạng `tr. i/N` của file. Có số trang nội bộ thì ghi thêm.
3. **Tách bạch 4 loại thông tin**: trích từ tài liệu, Claude tự tính (có công thức), giả định (ghi chữ **GIẢ ĐỊNH**), gợi ý ngoài tài liệu (ghi chữ **gợi ý**). Loại gợi ý không được đưa vào cột "Tiêu chuẩn viện dẫn" của ma trận.
4. **Không diễn giải nội dung QCVN hay TCVN mà tài liệu không trích.** Ví dụ chỉ được viết "tài liệu dẫn Bảng 4 QCVN 06:2022/BXD", không tự viết Bảng 4 quy định gì.
5. **Tài liệu tự mâu thuẫn hoặc số trang không khớp** thì nêu ra. Không tự chọn một bên cho "hợp lý".
6. **Không chép sai chữ số.** Trước khi trả kết quả, soát lại từng số ở Phần 2 và Phần 3 với text của Bước 1.
7. **Ghi số theo kiểu Việt Nam**: dấu phẩy là dấu thập phân, dấu chấm phân cách hàng nghìn (ví dụ 1.234,56). Đơn vị ghi m, m², m³, kg, kg/m³, mm, đ.
8. **Nhắc anh Thành kiểm tra lại hiệu lực** của mọi thông tư, nghị định, tiêu chuẩn được nhắc tới.

## Sau khi xong
- Cuối câu trả lời, hỏi một câu: anh Thành có cần xuất **ma trận (Phần 2) và bảng chi phí (Phần 3.3) ra Excel** không. Excel phải giữ công thức và có tiêu đề theo quy định trong CLAUDE.md.
- **Không sửa** file nguồn. Không ghi vào `01-HoSoGoc\`.
