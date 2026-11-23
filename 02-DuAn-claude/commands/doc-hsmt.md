---
description: Đọc, phân tích hồ sơ mời thầu, đối chiếu năng lực công ty, chấm Go/No-go, xuất Excel
argument-hint: <đường dẫn file E-HSMT, hoặc tên dự án trong 01-DuAn>
---

Phân tích hồ sơ mời thầu sau: $ARGUMENTS

Làm theo skill `vn-dau-thau`, Bước 0 đến Bước 3:

1. Chưa có thư mục dự án thì đề xuất tên theo quy tắc `YYYY-<LoaiCT>_<Ten>_<DiaDiem>`, hỏi anh Thành
   xác nhận rồi mới tạo. Chép E-HSMT vào `01-HoSoGoc\` (không sửa file gốc).
2. Chưa có hồ sơ năng lực công ty thì tạo mẫu trống, báo anh Thành điền, vẫn làm tiếp phân tích
   với các dòng năng lực để `CHƯA RÕ`.
3. Giao agent `chuyen-vien-dau-thau` làm Bước 1 đến Bước 3.
4. Trình báo cáo Go/No-go theo mẫu của skill, gửi file Excel bằng SendUserFile, rồi **dừng chờ anh
   Thành quyết định** có dự thầu hay không.
