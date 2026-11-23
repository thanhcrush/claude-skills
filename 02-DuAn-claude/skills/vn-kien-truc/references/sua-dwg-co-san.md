# Sửa bản vẽ DWG có sẵn, đổi số tầng

Rút từ lần đổi bộ KT một trường tiểu học 3 tầng thành 2 tầng (11/2026). Các lỗi ghi ở đây là lỗi đã xảy ra thật. Công cụ và cách chạy: `E:/New folder/06-CongCu/03-DoiSoTang-DWG/01-HuongDan.md`.

## Nguyên tắc

- File gốc, hồ sơ đã ký: chỉ đọc. Làm trên bản sao, kết quả lưu thành `_vNN` mới, không ghi đè.
- Thấy file `.dwl`, `.dwl2` cạnh DWG nghĩa là file đang mở: không lưu đè, báo anh Thành đóng hoặc lưu sang tên khác.
- Không tự tính lại kết cấu. Giảm tầng làm đổi tải, nên phải ghi rõ bản KC, móng chưa tính lại `[Cần xác nhận lại]`.
- Trước khi bắt tay, hỏi rõ: bộ môn nào, bỏ tầng nào, mái xử lý ra sao. Công năng riêng của tầng bị bỏ (vd phòng học bộ môn) phải báo anh quyết.

## Gọi AutoCAD Console

| Việc | Cách đúng | Nếu làm sai |
|---|---|---|
| Gọi `accoreconsole.exe` | Qua PowerShell `Start-Process`, ghi nhật ký ra file | Gọi từ Git Bash thì treo, kể cả script chỉ có `_.QUIT` |
| Nạp LISP | Đưa thẳng biểu thức vào file `.scr`, mỗi biểu thức một dòng | `(load "x.lsp")` ngoài thư mục tin cậy treo vì SECURELOAD hỏi xác nhận. Không đổi SECURELOAD |
| File `.scr` | ASCII, CRLF, không có dòng trống, kết thúc `_.QUIT` rồi `Y` | Dòng trống lặp lệnh trước; thiếu QUIT thì treo |
| Chữ có dấu | Viết dạng `\U+1EA6`, trong chuỗi LISP là `\\U+1EA6` | Lỗi mã hóa |
| Chọn bằng `ssget` cửa sổ | `ZOOM` tới vùng đó trước | Không chọn được đối tượng ngoài màn hình |
| `-STYLE` font TTF | Sau tên font: cao, rộng, nghiêng, ngược, lộn (không có câu hỏi "vertical") | Thừa một `N` thành lệnh lạ, script dừng |

## Trình tự bỏ một tầng

1. Đọc cấu trúc: khung tờ, cao độ, block, xclip. Đừng giả định mọi thứ là nét rời.
2. Chọn đường cắt theo cách sau. Dải bỏ có bề cao đúng một tầng, hai đường cắt cách nhau đúng bằng dải. Đếm thực thể bị mỗi đường đi qua, chọn chỗ ít cấu kiện nhất, tránh cắt cửa. Nên cắt dưới đáy dầm của sàn tầng bị bỏ, để dầm sàn phía trên hạ xuống thế chỗ. Sàn sát mái hạ xuống trùng cao độ sàn bị bỏ.
3. Nổ block bị cắt ngang, lặp đến khi hết. Block bị xclip thì tách đôi (xem bảng bẫy).
4. Xử lý theo vị trí so với dải:
   - Nằm trọn trong dải: xóa.
   - Nằm trên dải: hạ xuống, gồm cả chữ, ký hiệu.
   - Cắt ngang: polyline, line thì cắt tại hai đường rồi ghép lại, tuyệt đối không dời đỉnh theo khoảng cố định.
5. Gian cầu thang xử lý riêng, xem dưới.
6. Tờ mặt bằng của tầng bị bỏ: xóa hình, giữ khung tên, ghi chú rõ. Số tờ đánh lại do anh Thành quyết.
7. Đổi chữ cao độ, kể cả trên tờ chi tiết không cắt.
8. Chạy soát.

## Gian cầu thang (chỗ dễ sai nhất)

Khi bỏ tầng trên cùng, tầng còn lại trên cùng phải có dạng của tầng trên cùng bản gốc: thang không đi lên nữa, có lan can chặn đầu thang, thang lên mái chuyển xuống.

- **Mặt đứng, mặt cắt:** trong khoảng x của gian thang, dải bỏ thấp hơn một tầng (bỏ dải tầng dưới, giữ dải tầng trên cùng). Các nét liền ngoài gian thang giữ nguyên dải thường.
- **Cửa sổ thang vượt qua sàn:** cửa thang thường nằm lệch tầng theo chiếu nghỉ, nên đường cắt đi qua cửa. Không cắt cửa. Xóa nguyên cụm cửa thuộc dải bỏ, hạ nguyên cụm cửa của tầng trên.
- **Mặt bằng tầng mới trên cùng:** chép hình thang từ mặt bằng tầng trên cùng cũ sang, gồm cả mũi tên, lan can chặn, thang lên mái. Khớp theo trục, không theo khung tờ.
- **Tờ chi tiết thang:** hình "tầng 2-3" có thể đã vẽ dạng tầng trên cùng, chỉ cần đổi tên. Xem hình trước rồi mới sửa.
- **Mặt cắt chi tiết thang trong block xclip:** tách block tại khoảng 600 mm dưới sàn. Phần trên đặt khung xclip tại cao độ cao hơn một tầng rồi hạ xuống, sẽ lấy được dạng tầng trên cùng.

## Bẫy đã gặp

| Bẫy | Hiện tượng | Cách xử lý |
|---|---|---|
| Thanh chia ô cửa là MLINE | Không nằm trong LWPOLYLINE nên không được hạ, nằm chồng trên mái | Xử lý MLINE theo đúng dải của khu vực đó; loại khỏi STRETCH khi đã MOVE |
| Block chèn có điểm chèn thấp | STRETCH chỉ dời block khi điểm chèn lọt cửa sổ, mái trong block đứng yên | Dời theo khung bao bằng handle, không dùng STRETCH cho block |
| Block chỉ có ATTDEF | Không tính được khung bao nên bỏ sót, ký hiệu cửa còn trên tờ bỏ | Lấy điểm chèn khi không có khung bao |
| Hatch cắt ngang | STRETCH không kéo hatch | Sửa đỉnh biên hatch, bỏ liên kết hatch |
| Block xclip bị cắt | Không cắt được bằng nét | Chép thêm một bản, đặt lại xclip cho phần dưới, phần trên, rồi hạ phần trên |
| Kích thước đo qua dải | Giá trị sai (vd 3200 thay vì 400) | Điểm dưới trong dải, điểm trên ngoài dải: xóa. Chỉ giữ kích thước đo vắt qua cả dải hoặc còn trọn dưới |
| Kích thước gắn đỉnh polyline | Sửa polyline thì kích thước nhảy theo số thứ tự đỉnh (400 thành 982, dời 4.000) | `DIMDISASSOCIATE` kích thước đó trước khi cắt |
| Mặt bằng trong block | Mặt bằng cả tầng nằm trong một block | Nổ mới chép được từng phần |
| Cửa sổ cắt quá rộng | Bắt nhầm hình bên cạnh trên cùng tờ | Giới hạn x theo đúng hình |

## Danh sách soát sau khi đổi tầng

Không báo xong khi chưa đi hết danh sách.

- [ ] Cao độ: toàn file không còn cao độ cũ, kể cả tờ chi tiết.
- [ ] Kích thước: so từng kích thước với bản gốc bằng `soat_kich_thuoc.py`, 0 bất thường, tổng cao giảm đúng.
- [ ] Mặt đứng, mặt cắt: **xuất PDF bằng AutoCAD, phóng to từng gian và so với bản gốc**. Nhìn toàn tờ đã bỏ sót nét thừa trên mái.
- [ ] Cầu thang: mặt bằng, mặt cắt, mặt đứng, tờ chi tiết, thang lên mái.
- [ ] Tên hình, tên tờ, ghi chú có nhắc số tầng (vd "cho 02 phòng tầng 2, 3").
- [ ] **Số lượng trên tờ chi tiết**: cửa, vách kính, lavabo, gương, vách ngăn ghi "SL". Đếm lại theo mặt bằng còn lại. Lỗi này từng lọt qua vì không có chữ "tầng 3".
- [ ] Bảng diện tích, chỉ tiêu, thống kê vật tư, nội thất.
- [ ] Công năng của tầng bị bỏ đã được báo.
- [ ] Bộ môn khác (KC, điện nước, PCCC, phối cảnh) và độ khớp: cửa thang có đụng dầm, sàn không.
- [ ] `AUDIT` khi mở lại file đã lưu.
- [ ] File gốc và các bản trước không đổi.

## Giới hạn khi soát bằng ảnh

- ezdxf render không đúng wipeout (thành khối đen), không áp xclip. Soát thật phải xuất PDF bằng AutoCAD.
- Console thiếu font như `vnsimli.shx` thì PDF thiếu chữ hoặc lỗi dấu, chữ vẫn còn trong DWG. Đọc nội dung chữ từ DXF và giải mã TCVN3, VNI.
