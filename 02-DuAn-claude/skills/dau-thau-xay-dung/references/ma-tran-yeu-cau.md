# Ma trận yêu cầu E-HSMT — trích, phân công, kiểm tra 3 lớp

Dùng khi cần biến E-HSMT thành danh sách việc có người chịu trách nhiệm, hạn và kiểm tra trước khi nộp. Bổ sung cho mục 3 của SKILL.md (đọc nhanh): mục 3 cho kết luận Go/No-go, file này cho bảng theo dõi chi tiết.

## 1. Dữ liệu đầu vào
E-HSMT (chương I–VII), biểu mẫu, tiêu chí đánh giá, mẫu hợp đồng; hồ sơ năng lực công ty. Chỉ dùng dữ liệu trong tệp và thông tin người dùng cung cấp.

## 2. Các bước
1. Trích từng yêu cầu bắt buộc, tiêu chí đạt/không đạt, tài liệu chứng minh.
2. Gắn mỗi yêu cầu với chương/mục E-HSMT, biểu mẫu và trạng thái nguồn (đã có / chưa có / đã hết hạn).
3. Phân công bộ phận chủ trì và hạn nội bộ (sớm hơn hạn đóng thầu; để thời gian cho 3 lớp kiểm tra).
4. Đánh dấu điều kiện cần làm rõ và điều kiện có nguy cơ bị loại.
5. Thêm cột kiểm tra lần 1, lần 2, phê duyệt cuối.

## 3. Định dạng bảng (xuất .xlsx theo quy ước chung)
| Mã | Yêu cầu | Nguồn (chương/mục/trang) | Bằng chứng | Chủ trì | Hạn nội bộ | Trạng thái | Rủi ro / Loại | Kiểm tra lần 1 | Kiểm tra lần 2 | Phê duyệt cuối |

- Mã: `HL-01` (hợp lệ), `NL-01` (năng lực – kinh nghiệm), `KT-01` (kỹ thuật), `TC-01` (tài chính – giá), `HD-01` (điều kiện hợp đồng).
- Cột Rủi ro/Loại ghi rõ: **Loại** (không đạt là bị loại) / **Rủi ro cao** / **Cần làm rõ** / Thường.
- Cột kiểm tra: người kiểm, ngày, kết quả (Đạt / Sửa). Người kiểm lần 2 khác người lập và người kiểm lần 1. Phê duyệt cuối: anh Thành.
- Chủ trì, hạn: nếu người dùng chưa nêu thì ghi `[Chờ bổ sung]`, không tự đặt tên người.

## 4. Quy tắc nhãn (khớp quy tắc global của anh Thành)
| Tình huống | Nhãn |
|---|---|
| Kết luận chưa có bằng chứng trong tệp | `CHƯA ĐỦ DỮ LIỆU` |
| Thông tin anh sẽ cung cấp sau | `[Chờ bổ sung]` |
| Đã tìm hồ sơ mà không có | `[Tài liệu không đề cập]` |
| Có số liệu nhưng chưa chắc / là giả định | `[Cần xác nhận lại]` |
| Căn cứ pháp lý chưa chắc điều khoản hoặc hiệu lực | `CHƯA XÁC MINH` |

Không tự điền số còn thiếu. Giữ nguyên đơn vị, mã công trình, số hợp đồng, số hóa đơn, tên hồ sơ báo cáo đúng như nguồn.

## 5. Tính toán
Nếu có tính (bảo đảm dự thầu, doanh thu bình quân, giá trị hợp đồng tương tự...): ghi công thức, dữ liệu đầu vào (kèm nguồn) và kết quả, để kiểm tra lại. Trong Excel dùng công thức, không dán số.

## 6. Tự kiểm tra trước khi kết thúc
- Cộng lại các số tổng (giá, bảo đảm dự thầu, số hợp đồng tương tự...) và đối chiếu với nguồn.
- Tìm mâu thuẫn giữa các tệp (E-HSMT với bản vẽ, BOQ, mẫu hợp đồng, hồ sơ năng lực): liệt kê vị trí từng bên.
- Nêu **tối đa 5 câu hỏi** còn cần anh Thành trả lời, ưu tiên câu ảnh hưởng đến việc bị loại.
