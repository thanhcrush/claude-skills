# Cấu trúc thuyết minh biện pháp tổ chức thi công (gói xây lắp dân dụng, giao thông)

## Việc đầu tiên: bảng đối chiếu tiêu chí

Trước khi viết, lập bảng đối chiếu **tiêu chuẩn đánh giá kỹ thuật trong E-HSMT ↔ mục thuyết minh**. Mỗi tiêu chí (đạt/không đạt hoặc có điểm) phải có ít nhất một mục trả lời trực tiếp. Đặt bảng này ở đầu thuyết minh hoặc ở phụ lục, giúp tổ chuyên gia tìm nhanh.

## Khung mục (đổi thứ tự theo tiêu chí E-HSMT nếu cần)

1. **Giới thiệu gói thầu và căn cứ lập**: tên, địa điểm, quy mô, hạng mục chính, khối lượng chủ yếu (lấy từ bảng khối lượng mời thầu), đặc điểm hiện trường.
2. **Tổ chức hiện trường**: sơ đồ tổ chức, chức năng nhiệm vụ từng vị trí (tên nhân sự khớp bảng kê nhân sự), quan hệ với chủ đầu tư, tư vấn giám sát.
3. **Tổng mặt bằng thi công**: lán trại, kho bãi, bãi gia công thép, cốp pha; điện, nước thi công; đường tạm; rào chắn, biển báo; vị trí đổ phế thải.
4. **Biện pháp thi công chi tiết**, theo trình tự thi công: chuẩn bị, định vị, đất, móng (cọc nếu có), cốp pha, cốt thép, bê tông, xây, trát, ốp lát, chống thấm, mái, cửa, sơn, điện nước, hoàn thiện, vệ sinh bàn giao. Công trình giao thông: nền, móng, mặt đường, cống, an toàn giao thông khi thi công.
   - Mỗi công tác: trình tự, máy và nhân lực, yêu cầu kỹ thuật, kiểm tra nghiệm thu. Chỉ viện dẫn tiêu chuẩn **có trong yêu cầu kỹ thuật của E-HSMT** hoặc đã kiểm tra số hiệu và hiệu lực.
5. **Tiến độ**: bảng hoặc sơ đồ ngang (file Excel riêng), tổng thời gian, đường găng, biện pháp bảo đảm tiến độ; biểu đồ huy động nhân lực, thiết bị.
6. **Quản lý chất lượng**: hệ thống quản lý chất lượng của nhà thầu, thí nghiệm vật liệu, nghiệm thu nội bộ, lập hồ sơ quản lý chất lượng.
7. **Vật liệu**: nguồn cung (ưu tiên nhà cung cấp trong `05-VatTu-NhaCungCap\`), chứng chỉ xuất xưởng, đáp ứng yêu cầu kỹ thuật.
8. **An toàn lao động, vệ sinh môi trường, PCCC, an ninh trật tự**.
9. **Biện pháp riêng theo điều kiện**:
   - Mùa mưa bão Quảng Trị (thường từ tháng 9 đến tháng 12): che chắn, thoát nước hố móng, neo giằng giàn giáo, dự trữ vật tư.
   - Công trình đang sử dụng (trường học, trạm y tế...): phân khu, giờ thi công, lối đi an toàn.
10. **Bảo hành, bảo trì**: thời gian, cách xử lý hư hỏng, cam kết.

## Quy tắc viết

- Viết cho **đúng công trình này**. Không để sót tên công trình khác, không viết chung chung kiểu "theo thiết kế" khi có số cụ thể.
- Số nhân sự, thiết bị, thời gian trong thuyết minh **phải khớp** bảng kê năng lực và file tiến độ.
- Câu ngắn, thể chủ động, giọng văn hành chính. Dùng thuật ngữ ngành xây dựng Việt Nam.
- Markdown chuyển Word bằng `scripts/md_sang_docx.py`: `#` tên văn bản, `##` phần, `###` mục, `####` tiểu mục, bảng dùng `|`.
