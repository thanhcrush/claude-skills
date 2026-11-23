---
description: Lập hồ sơ dự thầu cho gói thầu đã quyết định tham dự (thuyết minh, tiến độ, năng lực, bảng giá, phiếu webform)
argument-hint: <tên dự án trong 01-DuAn>
---

Lập E-HSDT cho gói thầu: $ARGUMENTS

Làm theo skill `vn-dau-thau`, Bước 4 và Bước 5:

1. Kiểm tra đã có bảng phân tích E-HSMT trong `05-HoSoThau\01-PhanTich\` và anh Thành đã quyết định
   dự thầu. Chưa có thì chạy `/doc-hsmt` trước.
2. Các dòng `CHƯA RÕ`, `CHƯA ĐẠT` còn lại: hỏi anh Thành một lượt, gom thành danh sách ngắn.
3. Giao song song:
   - `ky-su-du-toan`: bảng giá dự thầu theo **đúng bảng khối lượng mời thầu**, đơn giá Quảng Trị.
   - `chuyen-vien-dau-thau`: thuyết minh biện pháp thi công, tiến độ, bảng kê năng lực, phiếu nhập webform.
4. Khi có bảng giá: `chuyen-vien-dau-thau` điền giá vào phiếu webform, soát khớp đơn dự thầu.
5. Giao `kiem-soat-hsdt` soát toàn bộ. Còn lỗi LOẠI thì giao lại người lập sửa, soát lại đến khi hết.
6. Bàn giao: danh sách file (đường dẫn tuyệt đối), việc anh Thành tự làm (mở bảo lãnh, ký số, nộp),
   hạn chót từng việc, các giả định cần duyệt.
