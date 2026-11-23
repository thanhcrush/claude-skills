# Kiểm soát hồ sơ năng lực — ghép bằng chứng, hiệu lực, xung đột huy động, mục lục nộp

Dùng sau khi có ma trận yêu cầu (`ma-tran-yeu-cau.md`) và trước khi nộp. Bổ sung cho checklist mục B của `quy-trinh-nha-thau.md`: checklist hỏi "có hay không", file này kiểm "bằng chứng nào, trang nào, còn hiệu lực không, có bị trùng lịch không".

## 1. Dữ liệu đầu vào
Ma trận E-HSMT, CV đã phê duyệt, chứng chỉ, hợp đồng lao động, đăng ký và kiểm định thiết bị. Chỉ dùng dữ liệu trong tệp và thông tin người dùng cung cấp.

## 2. Các bước
1. **Ghép tiêu chí với bằng chứng**: mỗi tiêu chí ghép với một hoặc nhiều bằng chứng cụ thể (tên file, trang). Tiêu chí không có bằng chứng thì ghi `CHƯA ĐỦ DỮ LIỆU`.
2. **Kiểm hiệu lực và năng lực**:
   - Chứng chỉ (hành nghề, an toàn lao động...): ngày cấp, ngày hết hạn, còn hiệu lực tại **thời điểm đóng thầu** và trong thời gian thực hiện hợp đồng?
   - Kinh nghiệm: số năm tính từ ngày nào đến ngày nào, theo CV đã phê duyệt; đối chiếu yêu cầu E-HSMT.
   - Thiết bị: đăng ký, kiểm định còn hạn; sở hữu hay thuê (có hợp đồng thuê không).
   - Khả năng huy động: có đủ người, đủ thiết bị cho thời gian thi công không.
3. **Phát hiện xung đột huy động**: một nhân sự hoặc một thiết bị bị cam kết cho nhiều gói/công trình trùng thời gian. Lập danh sách xung đột (mục 4).
4. **Đánh dấu dữ liệu cá nhân** cần che trước khi đưa vào công cụ AI (mục 5).
5. **Tạo mục lục và tên file nộp** theo quy tắc thống nhất (mục 6).

## 3. Bảng kết quả
| Tiêu chí | Bằng chứng | Tên file | Trang | Ngày hiệu lực / hết hạn | Trạng thái |
|---|---|---|---|---|---|

- Trạng thái: Đạt / Không đạt / Hết hạn trước thời điểm đóng thầu / `CHƯA ĐỦ DỮ LIỆU`.
- Tính toán (số năm kinh nghiệm, số ngày còn hiệu lực): ghi công thức, ngày đầu vào và kết quả. Trong Excel dùng công thức ngày, không gõ số.
- Nhãn khác (`[Chờ bổ sung]`, `[Cần xác nhận lại]`, `CHƯA XÁC MINH`...) xem `ma-tran-yeu-cau.md` mục 4.

## 4. Danh sách xung đột huy động
| Nhân sự / thiết bị | Gói / công trình A (từ - đến) | Gói / công trình B (từ - đến) | Thời gian trùng | Cách xử lý |
|---|---|---|---|---|

- Chỉ kết luận trùng khi có ngày bắt đầu và kết thúc của cả hai bên. Thiếu ngày thì ghi `CHƯA ĐỦ DỮ LIỆU`.
- Cách xử lý đề xuất: thay người/thiết bị, thuê thêm, hoặc làm rõ. Để anh Thành quyết định.

## 5. Dữ liệu cá nhân cần che trước khi dùng AI
Đánh dấu file và trang có: số CCCD/CMND, ngày sinh, địa chỉ cư trú, số điện thoại, số tài khoản ngân hàng, số bảo hiểm xã hội, mức lương trong hợp đồng lao động, ảnh chân dung.
- Chỉ liệt kê file/trang cần che, **không chép lại dữ liệu cá nhân** vào bảng kết quả.
- Việc che thực hiện trên bản sao; hồ sơ gốc giữ nguyên, không sửa.
- Bản nộp thầu theo E-HSMT thường cần đầy đủ giấy tờ; che chỉ áp dụng cho bản đưa vào AI, không áp dụng cho bản nộp. `[Cần xác nhận lại]` với E-HSMT từng gói.

## 6. Mục lục và tên file nộp
- Mục lục theo thứ tự chương/mục của E-HSMT, đánh số `01-`, `02-`..., khớp mã trong ma trận.
- Tên file: không dấu, không khoảng trắng, mẫu `<MaGoiThau>_<Ma>_<TenTaiLieu>_v01.pdf`, VD: `GoiXL01_NL-03_ChungChiCHT-ChiHuyTruong_v01.pdf`.
- Mỗi file một nội dung, ghi đúng dung lượng và định dạng E-HSMT cho phép `[Cần xác nhận lại]` theo từng gói.
- Mục lục ghi: số thứ tự, tên tài liệu, tên file, số trang, mã tiêu chí liên quan.

## 7. Tự kiểm tra trước khi kết thúc
Cộng lại các số tổng; so mâu thuẫn giữa các tệp (CV với chứng chỉ, hợp đồng lao động với bảng kê nhân sự, đăng ký thiết bị với bảng kê thiết bị); liệt kê tối đa 5 câu hỏi cần người trả lời.
