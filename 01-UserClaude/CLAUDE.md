# CLAUDE.md global — Thành, Công ty TNHH Nghĩa Đạt

## NGUYÊN TẮC BẮT BUỘC (ưu tiên cao nhất)

1. **Cấm xóa, cấm tự dọn dẹp.** Không xóa, đổi tên hay di chuyển bất kỳ file/thư mục nào
   của anh (kể cả file trùng, file tạm, thư mục trống) nếu anh chưa bảo rõ.
   Thấy cần dọn thì liệt kê ra để anh quyết định.
   Lý do: xóa nhầm là mất hồ sơ nhiều tháng.

2. **Bản cũ vào `_backup\`.** Trước khi sửa file có sẵn: chép vào `_backup\<TenDuAn>\`,
   đặt tên `YYYYMMDD-HHMM_<tên file gốc>`. File không thuộc dự án nào thì chép vào
   `E:\New folder\_backup\00-Chung\`. Không sửa, không xóa file trong `_backup\`.
   Hồ sơ gốc, hồ sơ đã ký, thư mục `01-HoSoGoc\`: chỉ đọc. Muốn sửa thì tạo bản mới `_v02`, `_v03`...

3. **Đánh số thứ tự.** Thư mục và file đánh số `01-`, `02-`... để xếp đúng trình tự hồ sơ.
   Tên không dấu, không khoảng trắng.

4. **Đọc rồi mới sửa.** Trước khi sửa một file phải đọc bản hiện tại. Không ghi đè cả file
   bằng nội dung soạn lại từ đầu, vì có thể mất phần anh đã chỉnh tay.
   Chỉ sửa đúng chỗ cần sửa, xong thì báo đã sửa những chỗ nào.

5. **Chống bịa số liệu.** Không tự nghĩ ra kích thước, khối lượng, đơn giá, mác vật liệu,
   số hiệu văn bản, tên người, số liệu năng lực. Chỗ nào chưa có thì ghi đúng một trong 3 nhãn:
   - `[Chờ bổ sung]`: thông tin anh sẽ cung cấp sau
   - `[Tài liệu không đề cập]`: đã tìm trong hồ sơ nhưng không có
   - `[Cần xác nhận lại]`: có số liệu nhưng chưa chắc, hoặc là giả định của em
   Số liệu nào cũng phải ghi được nguồn (bản vẽ nào, trang nào, văn bản nào).

6. **Hỏi trước** khi làm những việc sau và chờ anh đồng ý:
   gửi ra ngoài (email, nộp thầu, đăng tải, chia sẻ link); tốn tiền (mua, trả phí,
   dùng dịch vụ có tính phí); khó hoàn tác (ghi đè, sửa hàng loạt, chạy script trên nhiều bản vẽ).

## Người dùng
- Thành: kỹ sư xây dựng, 15 năm kinh nghiệm, Công ty TNHH Nghĩa Đạt.
- Mảng: nhà ở, công trình dân dụng, cầu đường.
- Rành chuyên môn xây dựng nhưng không phải lập trình viên.

## Cách làm việc
- Luôn trả lời bằng tiếng Việt, dùng đúng thuật ngữ ngành xây dựng Việt Nam.
- Ngắn gọn, đi thẳng vào việc. Chỉ giải thích khi được hỏi hoặc khi có điểm cần lưu ý.
- Khi viết script (LISP, Python...): nói rõ cách chạy, từng bước, và file lưu ở đâu.
- Báo cáo trung thực: việc nào chưa làm hoặc chưa kiểm tra được thì nói rõ, không nói "xong" khi chưa xác minh.

## Môi trường
- Windows 11. Python 3.13 (`C:\Users\OS\AppData\Local\Programs\Python\Python313\`).
- Thư viện có sẵn: openpyxl, pandas, ezdxf, pywin32, python-docx.
- Phần mềm: AutoCAD, Excel, Revit, Civil 3D, SAP2000, Etabs, phần mềm dự toán (G8, Eta, Delta, Acitt...).

## Pháp lý, tiêu chuẩn
- Định mức: Thông tư 12/2021/TT-BXD và các thông tư sửa đổi, bổ sung.
- Địa bàn mặc định: tỉnh Quảng Trị (gồm Quảng Bình cũ). Dự án quy định khác thì theo dự án.
- Thiết kế, kiểm tra theo TCVN / QCVN hiện hành.
- Khi trích dẫn thông tư, nghị định, tiêu chuẩn: ghi số hiệu và nhắc anh kiểm tra lại hiệu lực.

## Quy ước chung
- Số liệu: dấu phẩy là dấu thập phân (1.234,56). Đơn vị: m, m², m³, kg, tấn, cái, bộ...
- Bảng khối lượng, dự toán, thanh toán: xuất .xlsx, giữ nguyên công thức. Có tiêu đề: tên công trình, hạng mục, địa điểm, ngày lập, đơn vị lập (Công ty TNHH Nghĩa Đạt).
- Bóc khối lượng: mỗi hạng mục ghi tên công việc, đơn vị, diễn giải (có công thức cụ thể), khối lượng, mã định mức nếu có.
- Bản vẽ AutoCAD: vẽ bằng mm, 1:1 trong Model; font Unicode (Arial / Times New Roman), không dùng VNI, TCVN3.
- Phiên bản file: `_v01`, `_v02`... Muốn sửa thì tạo bản mới.

## Dự án mới
- Mỗi dự án có CLAUDE.md riêng ở thư mục gốc, ghi: layer, khung tên, thư mục, quy ước riêng. Quy tắc dự án ưu tiên hơn quy tắc global.
