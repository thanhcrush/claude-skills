---
description: Chạy làn A, lập bộ tài liệu sơ bộ trình khách nhà phố (tiếp nhận, công năng, khối lượng thô, kiểm tra chéo)
argument-hint: <đường dẫn phiếu yêu cầu .md; bỏ trống thì dùng 00_yeu-cau-khach-hang.md ở thư mục gốc>
---

Lập hồ sơ sơ bộ trình khách từ phiếu yêu cầu: $ARGUMENTS (bỏ trống thì dùng `00_yeu-cau-khach-hang.md`).

Làm theo `00_phieu-giao-viec.md` (phần Phân công và Quy tắc chung):

1. Kiểm tra có phiếu yêu cầu `.md` và phiếu giao việc. Thiếu thì báo, không tự tạo số liệu.
2. Giao **song song, độc lập** ba agent: `tiep-nhan` (ghi `handoff/01_tiep-nhan.md`), `kien-truc` (ghi
   `handoff/02_kien-truc.md`), `khoi-luong` (ghi `handoff/03_khoi-luong.md`). Mỗi agent chỉ ghi file của mình.
3. Khi cả ba xong, giao `kiem-tra` (ghi `handoff/04_kiem-tra.md`; đã có file thì dùng `_v02`, không ghi đè).
4. Kết luận CẦN SỬA thì giao lại đúng agent bị nêu, tối đa 1 vòng, rồi cho `kiem-tra` soát lại.
5. Báo anh Thành: kết luận ĐẠT hay CẦN SỬA, các nhãn `[Chờ bổ sung]` và `[Cần xác nhận lại]` còn mở, danh
   sách câu hỏi cho khách. **Không gửi gì ra ngoài**; thư gửi khách chỉ là bản nháp để anh Thành duyệt.
