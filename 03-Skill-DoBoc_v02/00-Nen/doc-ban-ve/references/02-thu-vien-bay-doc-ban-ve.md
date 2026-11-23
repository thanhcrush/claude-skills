# THƯ VIỆN BẪY — hồ sơ, đọc số, hình học

Mỗi bẫy dưới đây **đã xảy ra thật**, cột CT là mã công trình. Đọc khi thấy số bất thường, hoặc khi bị khách bắt lỗi.

---

## A. Bẫy về FILE và HỒ SƠ

| # | Bẫy | Dấu hiệu | Xử lý | CT |
|---|---|---|---|---|
| A1 | Khung tên **lặp số hiệu** cho nhiều tờ khác nhau | "KC-01" xuất hiện ở 10 tờ | Lập danh mục theo **tên bản vẽ + số trang PDF**, không theo số hiệu | 2614 |
| A2 | Khung tên **ghi sai tên** | Tờ ghi "thống kê thép móng" nhưng nội dung là hố ga/vách | Lập danh mục theo **hình**, mở từng tờ xem | 2614, 2624 |
| A3 | **Text rác off-canvas** | Text kết cấu lạc trong file kiến trúc, toạ độ cách bản vẽ hàng triệu đơn vị; layer lạ (`KCS_TEXT`) | Không coi mỗi chuỗi text là một bản vẽ; phải có khung bản vẽ thật ở đó. Cắt theo khung tên thì tự loại | 2611 |
| A4 | **Thiếu tờ** trong file PDF | Bộ 56 tờ nhưng file chỉ có 49 | Ghi vào danh sách cần kiểm và xin bổ sung. **Không suy đoán** phần thiếu | 2622 |
| A5 | Bản vẽ nằm **lệch chỗ** trong PDF | Kết luận "thiếu tờ KC-53" trong khi nó nằm ở trang 38 | "Chưa đọc" ≠ "không có". Quét lại toàn bộ trước khi kết luận thiếu | 2619 |
| A6 | **Hai phương án kiến trúc** trong cùng bộ hồ sơ | Lưới trục không khớp KC | Xác định PA nào khớp KC → dùng PA đó; PA kia chỉ tham khảo. Hỏi khách xác nhận | 2622 |
| A7 | File tham khảo là **dự toán của công trình khác** | Tên file có "tham khao" | Chỉ dùng **cấu trúc đầu việc**, không dùng số | 2623 |
| A8 | **DXF lỗi nhân bản gương** | Ký hiệu bị đẩy ra ngoài phạm vi bản vẽ; block ở vùng x ≈ −4,9 triệu | Đếm ký hiệu tim + kiểm chéo Σ(đài × cọc/đài) | 2625 |
| A9 | **Excel đang mở nên khoá file** | Ghi đè báo lỗi | Ghi ra tên mới `-v02` | 2624 |
| A10 | File zip/xlsx **hỏng** | Không mở được | `zip -FF` phục hồi | 2614 |
| A11 | **mnt không sync khi ghi đè** | bash đọc ra bản cũ/cụt dù file-tools báo đã ghi | Ghi file **tên mới** thì sync ngay | build docx |
| A12 | **Bản mới nhất theo ngày ≠ bản tham chiếu** | Có nhiều .xls | Bản tham chiếu = bản **khách chỉnh tay gần nhất** | 2611 |

---

---

## B. Bẫy về ĐỌC SỐ

| # | Bẫy | Dấu hiệu | Xử lý | CT |
|---|---|---|---|---|
| B1 | **Đường gióng kích thước thuộc cấu kiện khác** | Số 850 gióng vào đài, đài thật 750 — số đó là của giằng chạy qua | Đo Δ giữa 2 đường bao bê tông; kiểm hệ số vẽ chi tiết (có thể 4×) | 2625 |
| B2 | **Nhiều bracket cùng gốc đo trên mặt cắt móng** | 1100 / 1500 / 1600 đều đo từ mốc −2.000 | Render mặt cắt và nhìn; hoặc hỏi. Đã sai 2 lần trước khi đúng | 2614 |
| B3 | **Nhãn trên MB có số cố định vô nghĩa** | "GM-x (BxH)" — số thứ 2 luôn là 150 cho mọi giằng | Đừng đoán (từng đoán là dày lót). Xem tờ chi tiết | 2614 |
| B4 | **Nhãn trục lệch tim cột 125–150 mm** | Đo theo nhãn ra số lẻ | Không dùng nhãn trục làm mốc đo; đo hình học | 2625 |
| B5 | **Dim gộp cả lớp lót** | PDF ghi 1250, thực 1150 | Lấy polyline thực (shoelace), không lấy dim gộp | 260702 |
| B6 | **pdftotext -layout trộn cột** | Bảng nhiều cột ra lộn xộn | Bóc bằng toạ độ từ, tự nhận hướng | 2611 |
| B7 | **Bảng xoay 90° + chữ đảo** | pdftotext chỉ ra được khung tên | Render ảnh + rotate rồi đọc mắt | 2611, 2614 |
| B8 | **Bảng thép "lớp dưới / lớp trên" lặp tổng cả sàn** | Hai trang giống nhau | Verify rồi lấy **một** | triage KC |
| B9 | **Bảng ghi "(SL: n)" và cột T.BỘ đã nhân SL** | Tổng hợp khối lượng đã gồm hết | **Không nhân lại** | triage KC |
| B10 | **Cùng tên mặt cắt ở 2 tờ, kích thước khác nhau** | MC 6-6 ở KC-09 H=900, KC-10 H=1000 | Gán theo **tờ chứa hình bằng**, không theo tên | 2625 |
| B11 | **Trùng tên cấu kiện giữa các khu** | `DM-1` móng ≠ `DM-1` mái | Phân biệt bằng vị trí y trong DXF | 2624 |
| B12 | **Cốt KC lệch cốt KT 30–50 mm** | Hai bộ cao độ khác nhau | Ghi rõ đang dùng cốt nào | 2624 |
| B13 | **Ghi chú vật liệu (mác BT) không bung Unicode** | Tiêu đề đọc được nhưng ghi chú thì không | Render ảnh xem, hoặc hỏi | 6016, triage |
| B14 | **Mâu thuẫn nội bộ bản vẽ** | Bảng ghi "PHC D350-A" nhưng đường kính đại trà 400; hai tờ KC ghi 80T và 100T | Không tự chọn. Hỏi TVTK/TMD, ghi vào cần kiểm | 2614, 2619 |
| B15 | **Đếm chú thích lặp trên tờ MEP** | Số máy lạnh đếm theo text ra sai | Đếm ký hiệu thiết bị, không đếm text chú thích | 2623 |

---

---

## C. Bẫy về HÌNH HỌC và THUẬT TOÁN

| # | Bẫy | Dấu hiệu | Xử lý | CT |
|---|---|---|---|---|
| C1 | **Bỏ bước bung block** | `msp.query('LINE')` chỉ ra vài chục entity | Bung đệ quy + cho entity layer `0` kế thừa layer INSERT cha (35k → 315k segment) | 2611 |
| C2 | **polygonize shapely luôn fail** | Nét tường không khép mạch | Dùng raster flood-fill / watershed | 2611 |
| C3 | **Flood-fill không đóng khe trước → rò ra ngoài** | Thiếu ~10 % | `binary_closing` kernel ~14 px (20 mm/px) trước khi label | 2625 |
| C4 | **Ghép cặp đường không đủ tin cho TƯỜNG** | Bức tường 7 m ra 0,51 m | Hai mép ở hai layer khác nhau; có chỗ 3 đường sát nhau; bề rộng 50/100/150/200/500 không quy luật. → Đọc mặt bằng, dùng DXF để lấy toạ độ | 2625 |
| C5 | **Cặp đường 200 mm không phải dầm** | Có thể là tường/gờ/ô văng | Giới hạn phạm vi trong lưới nhà + kiểm mật độ dầm | 2625 |
| C6 | **Biên sân thượng không có dầm → vùng sàn nối ra ngoài** | Sàn ST 159 m² < lưới trục 203 m² | Kiểm bắt buộc: sàn ST ≥ sàn mái | 2625 |
| C7 | **Mặc định mái phủ kín lưới trục** | Mái = sàn ST | Soi MB kiến trúc mái tìm giếng trời (khung rỗng có dải viền); hatch ANSI31 trên MB dầm mái = lỗ | 2625 |
| C8 | **Đếm bằng vision (Hough)** | Sai 13–26 cái | Đếm bằng block/entity trong DXF | 2611 |
| C9 | **Đài đa giác nhân bao chữ nhật** | Diện tích vống | Shoelace từ polyline thực | 260625 |
| C10 | **Đo hatch gộp nhiều hàng view** | Diện tích lát vống gấp đôi | Chỉ đo trong đúng hàng view lát; view trần/vật dụng trùng pattern | 2624 |

---

---

---

## Ngưỡng kinh nghiệm

Không chép lại ở đây. Bảng ngưỡng duy nhất nằm ở skill `do-boc-loi` mục 8. Riêng hai ngưỡng chỉ dùng khi đọc bản vẽ:

| Ngưỡng | Rút từ | Dùng đúng cách |
|---|---|---|
| Cặp nét kính 40–50 mm | 2625 (ABUSA) | Dấu hiệu **nghi** là kính → xác nhận bằng layer + bảng cửa + mặt đứng. Đơn vị thiết kế khác vẽ khác |
| Dung sai rộng cửa ≤ 120 mm | 2625 | Đó là bề dày khung nhôm của **hồ sơ đó**. Hồ sơ khác phải xét tỷ lệ và quy cách; lệch thì giữ cả hai nguồn, để S hoặc T |

Khi một con số kinh nghiệm mâu thuẫn với bản vẽ, **bản vẽ thắng**.
