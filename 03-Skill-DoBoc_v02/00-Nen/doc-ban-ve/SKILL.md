---
name: doc-ban-ve
description: Đọc và hiểu toàn bộ hồ sơ bản vẽ xây dựng Việt Nam trước khi đo bóc — DXF, DWG, PDF. Dùng skill này khi nhận một bộ hồ sơ mới, khi cần lập danh mục bản vẽ và kiểm revision, khi đối chiếu kiến trúc với kết cấu tìm sai lệch, khi ghi bảng thông tin chung của công trình, hoặc khi cần lấy số liệu từ file CAD — mở file CAD xem có gì, tìm một tờ hay một mặt bằng, bung block, giải mã chữ tiếng Việt lỗi font trong DXF, đọc kích thước từ dimension, đo chiều dài dầm hay diện tích sàn từ nét vẽ, đếm cọc hoặc cấu kiện, trích bảng thống kê thép, đo diện tích lát bằng hatch, đo chiều dài tuyến ống và dây, render bản vẽ ra ảnh để nhìn, xuất DXF ra PDF. Dùng cả khi người dùng chỉ nói "đọc bộ bản vẽ này", "công trình này có gì đặc biệt", "kiến trúc với kết cấu có khớp không", "lấy giúp kích thước cái này", hoặc than không đọc được chữ trong DXF. Kèm script Python đã chạy trên hồ sơ thật.
---

# Đọc bản vẽ — từ nhận hồ sơ đến bảng thông tin chung

**Đọc `do-boc-loi` trước.** Skill này không lặp lại quy tắc bất biến, C/S/T/N, hai lớp dữ liệu.

Skill này kết thúc khi có đủ bốn thứ: `00-DanhMucBanVe_v01.xlsx` · ma trận cấu kiện × bản vẽ · sheet `00-ThongTin` của sổ khối lượng đã điền · danh sách sai lệch và điểm đặc biệt. **Chưa đủ bốn thứ này thì chưa được bóc bất cứ cấu kiện nào.**

Hồ sơ gốc nằm trong `01-HoSoGoc\` — **chỉ đọc**. Mọi file trung gian (pickle, ảnh render, bảng tạm) ghi vào `03-KhoiLuong\01-SoNoiBo\`.

## 1. Kiểm kê hồ sơ và revision

Kiểm kê mọi PDF, DWG/DXF, ảnh, Excel, thuyết minh. Ghi: tên file, định dạng, bộ môn, số trang thật, ngày sửa.

Phát hiện **trước khi đo**: file trùng, bản cũ/bản mới, bản thay thế, phần không đọc được.

- **Bản mới nhất theo ngày ≠ bản tham chiếu.** Bản tham chiếu là bản **khách chỉnh tay gần nhất** *(2611)*.
- Hai phương án kiến trúc trong cùng bộ hồ sơ: xác định phương án nào khớp KC → dùng cái đó, cái kia chỉ tham khảo, và hỏi khách *(2622)*.
- File tên có "tham khao" thường là dự toán công trình khác — chỉ dùng **cấu trúc đầu việc**, không dùng số *(2623)*.

*(Các mã 26xx trong bộ skill là mã công trình của bộ gốc, giữ lại làm dẫn chứng bài học.)*

## 2. Làm cho nhìn được — kỹ thuật tối thiểu

DWG thì chuyển sang DXF trước (AutoCAD `SAVEAS` DXF, hoặc skill `vn-xuat-autocad` nếu có). Với DXF, ba việc không được bỏ, chi tiết ở `references/01-ky-thuat-dxf-pdf.md`:

1. **Bung block đệ quy**, cho entity layer `0` kế thừa layer của INSERT cha, gom cả ATTRIB. Bỏ bước này là mất gần hết nét — 2611: 35.000 → 315.000 segment sau khi sửa đúng chỗ kế thừa.
2. **Lập bản đồ view.** Model space chứa tất cả các tờ xếp cạnh nhau. Phải biết đang đọc tờ nào trước khi lấy bất kỳ số nào.
3. **Lấy lưới trục**, gốc toạ độ = giao trục 1 × trục A.

Text hiện dạng `MAËT BAÈNG DAÀM SAØN LAÀU 1` là **VNI-Windows** (font `VNI-Times`, `VNI-Helve-Condense`) — **giải mã được 100 %**, bảng thay ở `references/03-bang-ma-vni.md`. Giải mã xong là có tên và số hiệu từng tờ, ký hiệu tiết diện, chiều dài ghi sẵn, cả bảng thống kê cửa.

Với PDF: phân loại vector / scan / text-đã-thành-nét; phát hiện trang xoay 90°, bảng nhiều cột. Không đọc số nhỏ bằng mắt khi còn nguồn vector.

**Render để nhìn trước khi lấy số.** Renderer tự viết có thước 1 m và nhãn trục thì đọc được vị trí bằng mắt và đối chiếu ngay với số đo từ vector.

## 3. Đọc kỹ một lượt — trình tự

Đọc **hết**, không nhảy cóc, theo thứ tự:

`thuyết minh và ghi chú chung` → `kiến trúc tất cả tầng` → `mặt đứng, mặt cắt, chi tiết` → `móng` → `cột, vách` → `dầm, sàn, mái, thang` → `bảng cửa, bảng vật liệu, bảng thép` → `MEP` → `báo cáo khảo sát địa chất (nếu có)`

Mục tiêu lượt này **không phải lấy số**, mà là hiểu: hình thái, số khối, số tầng, hệ trục, cao độ, hệ móng, hệ chịu lực, hệ mái, vùng lệch/hạ cốt, cấu kiện đặc biệt, cấp đất, và **phần hồ sơ còn thiếu**.

## 4. Danh mục bản vẽ

Ghi ra `00-DanhMucBanVe_v01.xlsx`:

| Cột | Nội dung |
|---|---|
| Bộ | KT / KC / DN / GT |
| File | tên file nguồn |
| Trang PDF / Model-Layout | số trang thật, hoặc view trong Model space |
| Số hiệu | như ghi trên khung tên |
| Tên bản vẽ | **tên thật theo hình, không tin khung tên** |
| Revision / ngày | để không trộn bản cũ với bản mới |
| Nội dung chính | mô tả một dòng |
| Dùng cho | cấu kiện nào sẽ dùng tờ này |
| Trạng thái đọc | đã đọc / chưa / không đọc được |

Ba cảnh báo về khung tên:

- Khung tên hay **lặp số hiệu** — "KC-01" cho 10 tờ khác nhau *(2614)*.
- Khung tên hay **ghi sai tên** — ghi "thống kê thép móng" mà nội dung là hố ga *(2614, 2624)*.
- File CAD Việt Nam hay để **toàn bộ trong Model space**, số hiệu để mặc định.

→ Lập danh mục **theo hình**, mở từng tờ xem, không theo khung tên. Cột Ký hiệu bản vẽ trong sổ khối lượng ghi theo **số hiệu tờ đã xác minh** ở danh mục này.

**Text rác off-canvas không phải là bản vẽ.** Text kết cấu lạc trong file kiến trúc, toạ độ cách bản vẽ hàng triệu đơn vị. Phải có khung bản vẽ thật ở đó mới tính là một tờ — 2611 từng nhầm "MB kết cấu tầng 7" thành bản vẽ thật rồi báo mâu thuẫn giả.

**"Chưa đọc" ≠ "không có".** 2619 từng kết luận thiếu tờ KC-53 trong khi nó nằm ở trang 38. Quét lại toàn bộ trước khi kết luận thiếu.

## 5. Ma trận cấu kiện × bản vẽ

**Không tìm cấu kiện chỉ theo tên tờ.** Sau danh mục, lập bảng thứ hai: mỗi hệ cấu kiện → liệt kê **mọi** tờ có thể chứa nó, kèm vai trò từng tờ (nhận diện / lấy số / kiểm chéo).

Những chỗ hay nằm lệch nhóm tờ:

| Cấu kiện | Có thể nằm ở |
|---|---|
| Đà kiềng cốt nền (DKT) | mặt bằng **sàn trệt**, không phải tờ móng |
| Móng và dầm cầu thang | tờ chi tiết **cầu thang** |
| Pit thang máy, bể nước, bể phốt | tờ MEP hoặc tờ chi tiết riêng |
| Lanh tô | tờ chi tiết cửa hoặc ghi chú chung, thường không có tờ riêng |
| Tường thu hồi, sê nô | tờ mái hoặc mặt cắt |
| Cao độ hoàn thiện | mặt cắt, không phải mặt bằng |
| Cổ cột | mặt cắt móng, không phải tờ riêng |
| Bê tông lót, cao độ đáy hố đào | mặt cắt móng, ghi chú chung móng |
| Ống đứng, chiều cao lắp thiết bị | sơ đồ không gian cấp thoát nước, ghi chú mặt bằng điện |

## 6. Đối chiếu kiến trúc với kết cấu — bốn nhóm bắt buộc

Đây là việc quan trọng nhất của lượt đọc. Mọi sai lệch tìm được ghi vào `00-DanhSachCanKiem.md` kèm **biên độ ảnh hưởng**.

**Nhóm 1 — Lưới trục và kích thước bao.** Nhịp trục hai phương, dài–rộng tổng thể, vị trí trục phụ. Lệch ở đây kéo theo sai toàn bộ, phải xử trước tiên. Kiểm cả trường hợp KT vẽ theo tim tường còn KC theo tim cột.

**Nhóm 2 — Cao độ và số tầng.** Cốt nền, cao từng tầng, tầng lửng, tum, sân thượng, **cốt tự nhiên** (cần cho đào đắp).
⚠ **Cốt kết cấu thường lệch cốt kiến trúc 30–50 mm** *(2624)* — ghi rõ đang dùng cốt nào, và dùng nhất quán.
⚠ Vùng hạ cốt khu ướt (thường −50) và sàn lệch phải nhận ra ở lượt này, không để đến lúc bóc sàn.

**Nhóm 3 — Cột/vách với tường, dầm với ô mở.** Cột và vách KC có nằm đúng trong tường KT không; cửa và lỗ mở có đụng dầm không (đụng thì không có lanh tô riêng); lỗ MEP xuyên kết cấu.

**Nhóm 4 — Thang, thang máy, mái, bể.** Ô thang KT và ô thang KC cùng kích thước; pit thang máy có trên cả hai bộ; phạm vi mái KT và mái KC có bằng nhau không; bể nước và bể phốt có bản vẽ ở bộ nào.

## 7. Xử lý sai lệch

**Nguyên tắc: kết cấu thắng cho phần thô.** Kích thước cấu kiện, cao độ, lưới trục lấy theo KC vì đó là cái thi công thật. Kiến trúc dùng cho hoàn thiện, công năng phòng, cửa, vật liệu.

Nhưng "KC thắng" không có nghĩa là im lặng bỏ qua:

1. **Lệch nhỏ trong dung sai thi công** (cỡ vài chục mm, không đổi khối lượng đáng kể) → lấy KC, ghi một dòng trong `GiaDinhDaDung.md`, không cần hỏi.
2. **Lệch làm đổi khối lượng** → lấy KC làm phương án tạm, trạng thái **T**, ghi vào `00-DanhSachCanKiem.md` kèm biên độ, **và hỏi khách nếu hỏi được**.
3. **Mâu thuẫn nội bộ trong chính một bộ** (không phải KT–KC) → **không tự chọn**. 2614: bảng ghi cọc "PHC D350-A" nhưng đường kính đại trà ghi 400; 2619: hai tờ KC ghi 80T và 100T. Hỏi TVTK hoặc chủ đầu tư, để **N** trong lúc chờ.
4. **Thiếu tờ** → không suy đoán. 2622 thiếu 7 tờ KC mái — ghi vào cần kiểm và xin bổ sung.

Không hỏi lại được khách thì mọi thiếu và mâu thuẫn chuyển thành `GiaDinhDaDung.md`, ghi đủ: giả định là gì · căn cứ · hạng mục nào phụ thuộc · ảnh hưởng bao nhiêu · phải làm gì khi có câu trả lời.

## 8. Điểm đặc biệt cần lưu ý

Rà và ghi ra danh sách riêng. Đây là những thứ nếu phát hiện muộn thì phải bóc lại:

- Móng lệch tâm, móng chung nhiều cột, móng thiếu mark, móng ở cao độ khác nhau.
- Cột chuyển, dầm chuyển, cột dừng hoặc phát sinh giữa chừng, cột thu tiết diện theo tầng.
- Sàn lệch cốt, sàn dự ứng lực (kiểm DXF có `EUROCODE` hoặc đối tượng cáp), sàn không dầm.
- Mái nhiều lớp, mái dốc, sê nô, tường thu hồi.
- Thang máy, pit, bể nước, bể phốt — vách BTCT hay tường xây.
- Tường cong, tường chữ L/U, lồng thang máy.
- Mặt tiền nhiều vật liệu, lam, vách kính lớn.
- Nhà giật khối, nhà chéo, nhà trên đất dốc, nền đất yếu, nước ngầm cao (ảnh hưởng biện pháp đào).
  *2622: hồ sơ ghi "2 hầm" nhưng thực là khoét núi hở — áp định mức thi công hầm sẽ sai. Phải đọc mặt cắt địa hình.*
- Cải tạo, nâng tầng, kết cấu thép xen BTCT.
- Cấu kiện chỉ xuất hiện ở mặt đứng hoặc mặt cắt, không có trên mặt bằng.
- **Mác bê tông khác nhau giữa cột và dầm sàn** — ảnh hưởng cách gán nút giao (`do-boc-loi` mục 5).

## 9. Thông tin chung — sheet `00-ThongTin`

Điền sheet `00-ThongTin` của sổ khối lượng (tạo bằng `bangkl.tao_so()`, xem `do-boc-loi`). Danh mục dòng có sẵn trong mẫu: chung · quy mô · kết cấu · vật liệu · địa chất và biện pháp · quy ước đo bóc đã chốt. Mỗi dòng ghi **nguồn** (tờ, trang, văn bản) ở cột Nguồn.

Những dòng dễ sai nhất:

- **Số tầng** — tầng lửng, tum ghi riêng, không gộp vào số tầng nổi.
- **Chiều cao từng tầng** — đọc từ **mặt cắt**, mặt sàn → mặt sàn. Không áp một chiều cao chung cho cả nhà.
- **Tổng diện tích sàn** — tính theo PL VI TT 13 (mục bóc theo diện tích): mọi tầng kể cả hầm, lửng, tum; mỗi tầng tính cả tường bao, lôgia, ban công, cầu thang, giếng thang, hộp kỹ thuật.
- **Cốt đang dùng** — cốt kiến trúc hay cốt kết cấu, và **cốt tự nhiên** so với ±0.000.

Vật liệu phải đọc **từng bộ phận**, không lấy một mác cho cả nhà: mác bê tông lót, móng, cổ cột, giằng, cột, dầm sàn, cầu thang, lanh tô; cỡ đá; **loại thép theo đường kính** (Ø < 10 và Ø ≥ 10 thường khác nhóm, VD CB240-T / CB400-V hoặc tương đương — ghi theo ghi chú chung KC); loại gạch; **mác vữa xây** và **mác vữa trát** (thường khác nhau). Ghi chú mác bê tông trong DXF hay nằm trong **định nghĩa block**, duyệt modelspace không thấy — phải quét cả `doc.blocks`, hoặc render ảnh xem *(6016)*.

**Cấp đất** lấy từ báo cáo khảo sát địa chất. Không có báo cáo → `[Tài liệu không đề cập]`, hỏi anh Thành; không tự gán cấp đất. Tỷ lệ đào máy/thủ công, mái dốc hố đào là thông tin biện pháp → `[Chờ bổ sung]` nếu hồ sơ không có.

Chưa xác định được thì để nhãn tương ứng và đưa vào cần kiểm, **không điền số mặc định**.

## 10. Gate — chưa đạt thì chưa bóc

- [ ] Đã kiểm kê đủ file, xác định revision có hiệu lực, không còn file nghi trùng chưa phân xử.
- [ ] Danh mục bản vẽ lập theo **hình**, mỗi tờ có tên thật và trạng thái đọc.
- [ ] Đã bung block; số entity ở mức hàng chục nghìn (vài trăm là chưa bung).
- [ ] Có bản đồ view; mỗi phép đo sau này gán được vào một view cụ thể.
- [ ] Có ma trận cấu kiện × bản vẽ, không cấu kiện nào chưa biết đọc ở đâu.
- [ ] Đã đối chiếu đủ bốn nhóm KT–KC; mọi sai lệch có mục trong cần kiểm kèm biên độ.
- [ ] Đã ghi cốt đang dùng là cốt KT hay cốt KC, và cốt tự nhiên.
- [ ] Có danh sách điểm đặc biệt.
- [ ] Sheet `00-ThongTin` đã điền; dòng nào trống đều có nhãn và lý do.
- [ ] Phần hồ sơ thiếu đã liệt kê và đã xin bổ sung.

## 11. Tệp kèm theo

| File | Khi nào đọc |
|---|---|
| `references/01-ky-thuat-dxf-pdf.md` | Thao tác cụ thể: bung block, bản đồ view, dimension, đo hình học, trích thép, đếm cấu kiện, đọc PDF, render |
| `references/02-thu-vien-bay-doc-ban-ve.md` | Số bất thường, hoặc nghi bản vẽ có lỗi |
| `references/03-bang-ma-vni.md` | Giải mã text tiếng Việt lỗi font trong DXF |

| Script | Việc |
|---|---|
| `scripts/flatten_dxf.py` | Bung block đệ quy, kế thừa layer, gom ATTRIB → pickle dùng lại |
| `scripts/ban_do_view.py` | Dò lưới trục, số hiệu tờ, tên view → bản đồ tờ *(v02: đã sửa lỗi import module và đường dẫn Windows của bản gốc)* |
| `scripts/render_mat_bang.py` | Render mặt bằng ra PNG, màu theo layer, có thước 1 m và nhãn trục |
| `scripts/quet_theo_truc.py` | Quét nét theo trục, ghép cặp đúng bề dày, loại cột, in bảng đoạn |
| `scripts/giai_ma_vni.py` | Hàm `vn()` giải mã text VNI → Unicode. Đã kiểm 0 ký tự sót trên hồ sơ 2625 và 2614 |

Cách chạy trên máy công ty (Windows, Python 3.13): mở cmd tại thư mục `scripts`, chạy `python flatten_dxf.py <file.dxf> <ra.pkl>` rồi các script khác nhận file `.pkl` (xem dòng "Dùng:" đầu mỗi script). Thư viện cần: `ezdxf` (có sẵn), `pillow`, `numpy`; thêm `scipy` nếu dùng kỹ thuật tách ô bằng watershed trong `references/01`. Thiếu thì hỏi anh Thành trước khi cài (`python -m pip install <tên>`).

**Máy chậm thì đừng grind render.** Viết script độc lập cho anh Thành chạy trên máy thật, kèm hướng dẫn *(2611)*. Ghép nhiều trang thành ảnh montage (6 trang/ảnh, resize 1000 px) đủ đọc tiêu đề; số nhỏ như bảng thép phải render riêng full-res.
