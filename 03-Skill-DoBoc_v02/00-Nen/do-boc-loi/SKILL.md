---
name: do-boc-loi
description: Lõi quy ước đo bóc khối lượng xây dựng Việt Nam của công ty (kế thừa Phụ lục VI TT 13/2021, phù hợp QĐ 1041/QĐ-BXD năm 2026), ghi ra sổ Excel mẫu Bảng 6.1 và 6.2 có công thức, dùng được với mọi phần mềm dự toán (G8, Eta, Delta, Acitt...) hoặc Excel thuần. BẮT BUỘC đọc trước mọi việc liên quan tới đo bóc, bóc khối lượng, tính khối lượng, đọc bản vẽ để lấy số, lập dự toán, kiểm bản bóc — trước cả khi mở skill của từng cấu kiện. Gồm hai lớp dữ liệu (sổ nội bộ và sổ khối lượng giao), quy tắc bất biến, trạng thái C/S/T/N, chuẩn truy nguồn, bảy bước B1–B7, bảng quy ước cặp liên cấu kiện (cột–dầm–sàn, móng–giằng–cổ cột, tường–cửa–lanh tô, bê tông–ván khuôn–thép–lót–đào đắp), cách ghi sổ bằng script bangkl.py, cấu trúc thư mục, ngưỡng kinh nghiệm và bản đồ các skill con. Dùng cả khi người dùng chỉ nói "bóc công trình này", "làm tiếp", "kiểm lại khối lượng", hoặc đưa bản vẽ và hỏi ra bao nhiêu khối.
---

# Lõi đo bóc — đọc trước mọi hạng mục

Skill này chỉ chứa thứ dùng ở **mọi** hạng mục. Cách đo từng cấu kiện nằm ở skill riêng (mục 9).

Căn cứ đo bóc (cập nhật 09/10/2026):

- **Từ 01/7/2026, TT 13/2021/TT-BXD (gồm Phụ lục VI quy tắc đo bóc) hết hiệu lực**, thay bằng TT 37/2026/TT-BXD — thông tư mới **không có** phụ lục quy tắc đo bóc chi tiết. Bộ Xây dựng công bố **QĐ 1041/QĐ-BXD ngày 26/6/2026** *Hướng dẫn xác định khối lượng công trình*, **mang tính tham khảo**, chỉ nêu nguyên tắc chung: mỗi khối lượng xác định một lần, xác định rõ phạm vi khi các bộ phận giao nhau, được lấy khối lượng từ BIM.
- Công ty **giữ các quy tắc chi tiết của PL VI TT 13/2021 làm quy ước đo bóc nội bộ** (anh Thành đã chốt). Trong bộ skill, cụm "PL VI" nghĩa là **quy ước này**, không còn là văn bản bắt buộc. Bản tóm tắt: `E:\New folder\04-TieuChuan-PhapLy\02-DinhMuc\01-QuyTacDoBocKL_TT13-2021_PLVI_v01.md`.
- Hồ sơ giao cho bên ngoài (BOQ, hồ sơ thanh toán) phải **ghi rõ quy ước đo bóc đang dùng**. Dự án hoặc hợp đồng quy định quy tắc đo khác thì theo dự án.
- Danh mục văn bản chi phí, định mức, giá hiện hành: `E:\New folder\04-TieuChuan-PhapLy\00-DanhMucVanBan-ChiPhiDuToan_2026_v02.md`. **Nhắc anh Thành kiểm tra lại hiệu lực** mỗi khi trích dẫn.

## 0. Đầu mỗi phiên, không có ngoại lệ

1. Kiểm kê **toàn bộ** thư mục công trình kể cả thư mục con, kèm ngày sửa: `find . -type f -printf "%TY-%Tm-%Td %8s %p\n" | sort`. File mới hơn có thể là bản khách vừa gửi.
2. Đọc `GhiChu.md` của công trình. Chưa có thì tạo.
3. **Memory và ghi chú cũ là giả thuyết, không phải trạng thái.** File có thể đã đổi tên, khách đã trả lời câu treo, đã có bản bóc mới.
4. Nhiều bản bóc/dự toán: xác định **bản gần nhất khách đã chỉnh tay** — đó mới là bản tham chiếu, không phải bản mới nhất theo ngày.
5. Thư mục `01-HoSoGoc\` **chỉ đọc**. Không sửa đè file đã có — muốn sửa thì tạo `_v` mới.

## 1. Hai lớp dữ liệu — gốc của phần lớn lỗi cũ

### Lớp sổ nội bộ — tự do
Mã vị trí, nguồn đầy đủ, cách lấy, bản tô dấu, bảng đối chiếu, quan hệ cha–con, các phép kiểm độc lập. Muốn bao nhiêu cột cũng được, cấu trúc nào cũng được. Lưu trong `03-KhoiLuong\01-SoNoiBo\`.

### Lớp sổ khối lượng giao — cứng
File giao cho anh Thành và để nhập phần mềm dự toán là **sổ khối lượng theo mẫu Bảng 6.2 (chi tiết) và Bảng 6.1 (tổng hợp)** của PL VI TT 13/2021, sinh bằng `scripts/bangkl.py` từ mẫu `assets/Mau_BangKL_TT13_v01.xlsx`. Nghĩa là:

- cột (1)–(10) **đúng tên, đúng thứ tự** Bảng 6.2: STT · Ký hiệu bản vẽ · Mã hiệu · Danh mục công tác · Đơn vị · Số bộ phận giống nhau · Diễn giải tính toán · KL một bộ phận · KL toàn bộ · Ghi chú;
- cột (11)–(15) là **số liệu phụ trợ** nằm bên phải: Dài · Rộng · Cao/dày · Loại dòng · Trạng thái. Công thức KL lấy từ đây. **Không chen cột nào khác** vào giữa;
- vùng nhập phần mềm dự toán là bảng 6.1 (Mã hiệu · Danh mục · Đơn vị · Khối lượng) — cách nhập tùy phần mềm, xem `lap-du-toan`;
- số 0 và số âm là dữ liệu hợp lệ, không coi ô 0 như ô trống.

**Đừng trộn hai lớp.** Bản tô dấu, bảng kiểm, ghi chú dài để ở sổ nội bộ; sổ giao chỉ giữ diễn giải cô đọng đủ để kiểm lại.

## 2. Quy tắc bất biến

1. **Tiếng Việt toàn bộ**: tên task, ghi chú, file kết quả. Ghi lập luận đủ chi tiết để anh Thành theo dõi được.
2. **Số không có nguồn = không tồn tại.** Không gán nguồn giả (kiểu ghi "theo ghi chú KC chung B20" khi bản vẽ chỉ ghi mác cọc).
3. **"Chưa đọc" ≠ "không có".** Trước khi kết luận thiếu bản vẽ, quét lại toàn bộ tờ.
4. **Nhìn trước, lấy số sau.** Render/PDF để biết đang đọc cái gì; số chính xác lấy từ vector, không đọc số nhỏ từ ảnh raster khi còn nguồn vector.
5. **Không trộn revision.** Một cấu kiện chỉ lấy từ một revision.
6. **Không vừa đọc, vừa đếm, vừa tính, vừa ghi Excel trong một lượt.** Trộn bước là nguyên nhân gốc của hầu hết lỗi sót và lỗi trùng.
7. **Cách ly nguồn và kết quả cũ.** Bản bóc cũ, dự toán cũ, bản của AI khác chỉ mở ở **bước đối chiếu**. Mở sớm là chép cả lỗi.
8. **Hỏi lại được thì phải hỏi.** Không hỏi được → ghi `GiaDinhDaDung.md` kèm lý do và ảnh hưởng.
9. **Không tự điền mã hiệu định mức, đơn giá, mác vật liệu.** Chỗ chưa có ghi đúng một trong ba nhãn: `[Chờ bổ sung]` (anh sẽ cung cấp) · `[Tài liệu không đề cập]` (đã tìm, hồ sơ không có) · `[Cần xác nhận lại]` (có số nhưng chưa chắc, hoặc là giả định).
10. **Xong việc lớn hoặc phát hiện bài học mới** → cập nhật `GhiChu.md` và memory. Memory chỉ lưu quy trình và bài học, **không lưu số liệu công trình**.

## 3. Trạng thái từng số và chuẩn truy nguồn

| Mã | Nghĩa | Vào tổng? |
|---|---|---|
| **C** | Xác nhận — số ghi trực tiếp trên bản vẽ, hoặc hình học CAD đã kiểm đúng cấu kiện | có |
| **S** | Suy diễn có căn cứ — ghép từ chi tiết liên kết, chuỗi kích thước, trục | có |
| **T** | Tạm tính theo giả định đã nêu | có, **kèm cảnh báo** — bảng 6.1 ghi "Tạm tính" ở cột Cách thức xác định (đúng yêu cầu PL VI) |
| **N** | Chưa đủ cơ sở | **KHÔNG cộng vào tổng** — dòng N trong 6.2 không có số, chữ đỏ |

Truy nguồn tối thiểu:

- **PDF**: file + trang + số hiệu tờ + vị trí trên tờ.
- **DXF**: file + Model/Layout + view/tầng + vị trí hoặc trục/toạ độ (+ layer/block nếu xác định được).
- **Excel**: file + sheet + ô/vùng.

Ghi cả **cách lấy**: số ghi trực tiếp · chi tiết liên kết · chuỗi kích thước · đo tỷ lệ đã hiệu chuẩn · hình học CAD · giả định.

Toạ độ trong diễn giải lấy gốc = **giao trục 1 × trục A**, đơn vị mm, để người khác dò lại được trên CAD. Ký hiệu trong bảng phải **khớp ký hiệu bản vẽ** (PL VI).

Mọi dòng T và N phải có một mục trong `00-DanhSachCanKiem.md` kèm **biên độ ảnh hưởng** (±bao nhiêu m³, bao nhiêu tiền nếu ước được).

## 4. Bảy bước cho mỗi hạng mục — không gộp

`B1 chọn nguồn, phân vai` → `B2 kiểm kê ba lượt` → `B3 phủ kín` → `B4 kích thước` → `B5 phép tính` → `B6 kiểm độc lập` → `B7 ghi sổ`

- **B1 phân vai**: nêu rõ nguồn nào để **nhận diện**, nguồn nào để **lấy số**, nguồn nào để **kiểm chéo**. Không có nguồn nào chính tuyệt đối.
- **B2 ba lượt**: lượt 1 theo mark → lượt 2 theo hình học và lưới trục → lượt 3 tìm cấu kiện đặc biệt, lệch trục, thiếu mark. **Lượt 3 bắt được nhiều lỗi nhất.**
- **B2 đếm hai chiều**: đếm tổng cấu kiện vật lý **trước** khi phân mark, rồi kiểm `Tổng theo mark + cấu kiện không mark = Tổng vật lý`. Chưa khớp thì **chưa được lấy kích thước** — phải tìm đúng vị trí và nguyên nhân, không sửa tổng bằng tay.
- **B3 phủ kín**: mỗi vùng vật lý rơi vào đúng một trong ba — *đã có mã tính* / *loại trừ có lý do* / *N*. Không có loại thứ tư. Bản tô dấu là **bằng chứng phủ kín**; mã trên bản tô phải trùng vị trí ghi ở cột Danh mục của dòng chi tiết.
- **Đếm chữ, mark hay hatch không phải là kiểm kê cấu kiện vật lý.**
- **B5 đủ công tác đi kèm**: với mỗi cấu kiện bê tông đổ tại chỗ, kiểm đủ bê tông · ván khuôn · cốt thép · (lót) · (đào đắp) — xem mục 5, cặp cuối.
- **B7 ghi ngay sau mỗi hạng mục**, kèm cập nhật `GhiChu.md`. Đừng dồn cuối phiên.

**Nguyên tắc dừng:** sai có **tính hệ thống** (mất quan hệ cha–con, mã chồng lấn, bảng vá nhiều lần không truy được nguồn) → **dừng vá, lập lại danh sách từ nguồn**; bảng cũ chỉ dùng đối chiếu.

## 5. Quy ước cặp liên cấu kiện — dùng một vế mà bỏ vế kia là sai

Đây là chỗ tốn tiền nhất và không thuộc skill cấu kiện nào. Đọc cả bảng trước khi bóc bất cứ cấu kiện nào trong cặp.

**Nguyên tắc nền (PL VI TT 13/2021, mục bê tông):** nút giao cột–dầm tính vào **dầm**; dầm, cột, vách nằm trong sàn tính vào **sàn**; cột nối tường cùng mác tính vào **tường**; chỗ giao nhau chỉ tính **một lần**. Nút giao **khác mác bê tông** (VD cột M300, dầm sàn M250) cũng **tính vào dầm**, theo mác dầm (anh Thành chốt 09/10/2026).

Gộp lại thành **một thứ tự gán phần giao**: **sàn → dầm / giằng → cột / cổ cột**. Phần thể tích nằm trong chiều dày sàn thuộc sàn; phần còn lại nằm trong chiều cao dầm (giằng) thuộc dầm (giằng); phần còn lại mới thuộc cột. Gặp giao nhau phức tạp thì cứ áp đúng thứ tự này là không trùng, không sót.

| Cặp | Vế A | Vế B | Sai khi |
|---|---|---|---|
| **Cột ↔ Dầm** | cột tính từ mặt sàn (hoặc mặt giằng, mặt móng) **đến đáy dầm sâu nhất** giao vào cột; cột không có dầm thì đến **đáy sàn**. Một dòng một cột một tầng | dầm tính **thông thủy mép cột → mép cột**; **nút** = tiết diện cột × (H dầm sâu nhất − dày sàn), ghi **một dòng riêng trong công tác bê tông dầm**, mỗi nút một lần | cột lấy hết cao tầng → trùng phần nút. Quên dòng nút → thiếu. *(Bộ gốc làm ngược: cột hết cao tầng, dầm trừ cột — chỉ đúng khi phần mềm dtPro tự xử lý)* |
| **Dầm ↔ Sàn** | sàn tính **diện tích phủ bì trừ ô trống** × dày sàn — đã gồm phần dầm, cột, vách nằm trong sàn | dầm chỉ lấy **phần dưới sàn**: cao tính = H dầm − dày sàn. Dầm bo, dầm biên nhô **lên trên** mặt sàn: phần nhô lên tính vào dầm | dầm nhập đủ H trong khi sàn phủ bì → trùng phần giao. Trừ bề rộng dầm khỏi sàn **và** giảm H dầm → thiếu |
| **Móng ↔ Dầm móng** | móng lấy hết bê tông móng | **dầm móng** (chạy xuyên móng) trừ phần nằm trong móng, mép đài → mép đài | trừ **cột** thay vì trừ **đài** *(260702: 21,67 md thay vì 12,06 — dư 44 %)* |
| **Cổ cột ↔ Giằng móng** | cổ cột từ **mặt trên móng đến cốt nền, trừ đoạn nằm trong chiều cao giằng nối vào** (và trong sàn nền BTCT) — xem `boc-co-cot-vach-pit` mục 2 | **giằng** dài thông thủy mép cổ cột → mép cổ cột + **dòng nút** (tiết diện cổ cột × H giằng) trong công tác bê tông giằng — cùng nguyên tắc nút cột–dầm | trừ cả móng lẫn cổ cột cùng một vùng giao → trừ hai lần. Cổ cột lên tới cốt nền **và** giằng cũng tính nút → trùng |
| **Đài ↔ Cổ cột** | cao đài tính hết bê tông móng, phân biệt bản đáy / bậc / chóp | cổ cột tách riêng | gộp cổ cột vào cao đài *(2622: cao đài gồm 400 mm cổ cột)*. Lấy khoảng từ mặt trên móng đến đầu cọc làm cao móng |
| **Giằng, dầm ↔ Sàn nền BTCT** | sàn nền đổ liền khối tính phủ bì | phần giằng nằm trong chiều dày sàn nền tính vào **sàn** (cùng nguyên tắc dầm–sàn) | tính giằng đủ H mà sàn nền cũng phủ bì |
| **Tường ↔ Cửa ↔ Lanh tô** | tường mẹ lấy **cả mặt phẳng qua ô mở**, chiều dày **không gồm lớp trát** | cửa là **dòng trừ** (số bộ phận âm) ngay dưới đúng tường mẹ; trừ cả **lanh tô, giằng tường, bổ trụ BTCT** nằm trong tường; lỗ < 0,25 m² không trừ (PL VI) | đo phần đặc *(2625: ô mở 4,7 m làm bức tường ra 0,45 m)*. Gán cửa theo khoảng cách gần nhất. Quên trừ thể tích lanh tô |
| **Sàn ↔ Mái** | sân thượng là sàn đi lại được, **luôn có bê tông** | mái **không** mặc định phủ kín lưới trục | suy diện tích mái từ sàn dưới *(2625: ST 203,95 vs mái 173,15 m² — mái có 3 lỗ giếng trời 35,10 m²)* |
| **Bê tông ↔ Ván khuôn ↔ Cốt thép ↔ Lót ↔ Đào đắp** | mỗi cấu kiện bê tông đổ tại chỗ ra **công tác bê tông** | phải có đủ công tác đi kèm: **ván khuôn** (m² mặt bê tông cần chống đỡ) · **cốt thép** (từ `TK-Thep`) · **bê tông lót** và **đào đắp** nếu nằm dưới đất | bộ gốc để phần mềm dtPro tự sinh các công tác này; bóc trên Excel mà quên là **thiếu hàng loạt** |

**Phân biệt dầm móng với giằng móng theo cấu tạo, không theo tên.** Dầm móng chạy xuyên móng/đài → trừ móng. Giằng móng nối giữa các cổ cột → thông thủy mép cổ cột + nút. Ký hiệu `DKT`, `ĐK`, `GM` chỉ là tên trên bản vẽ của từng hồ sơ — giữ ở cột Danh mục, không dùng để quyết định quy tắc trừ.

### Ván khuôn — quy ước chung

PL VI: đo **diện tích mặt bê tông cần chống đỡ tạm** khi đổ; lỗ < 1 m² không trừ; phân theo vật liệu ván khuôn (gỗ, thép, ván phủ phim…) — chưa rõ biện pháp thì ghi `[Chờ bổ sung]` ở tên công tác.

| Cấu kiện | Diện tích ván khuôn |
|---|---|
| Móng, đài | thành xung quanh từng khối (chu vi × cao từng bậc); đáy đổ trên lót → không tính; mặt vát chỉ tính khi bản vẽ/biện pháp có ván khuôn mặt vát `[Cần xác nhận lại]` |
| Cổ cột, cột | chu vi × chiều cao tính bê tông (đến đáy dầm), trừ mặt áp vào cấu kiện đã đổ trước nếu có |
| Dầm, giằng | đáy (bề rộng × dài thông thủy) **chỉ khi đáy treo**; hai thành × (H − dày sàn); dầm biên: thành ngoài lấy đủ H. Giằng đáy tựa nền hoặc tường → chỉ hai thành |
| Sàn | đáy sàn = diện tích phủ bì − ô trống − hình chiếu đáy dầm và tiết diện cột; cộng thành sàn biên (chu vi × dày) |
| Cầu thang | đáy bản thang (dài triển khai × rộng), đáy chiếu nghỉ, cổ bậc, thành bản biên |
| Lanh tô, ô văng | đáy + hai thành |

Quy ước này đi cặp với quy ước bê tông ở bảng trên — tính ván khuôn **theo đúng ranh giới** đã dùng cho bê tông, không theo hình học khác.

## 6. Cách ghi sổ khối lượng

Dùng `scripts/bangkl.py` (đọc docstring đầu file). Mỗi công trình **một file** `<TenDuAn>_BangKL_v01.xlsx`, mỗi hạng mục **một sheet** `6.2-<số><tên>` theo trình tự thi công:

`6.2-01Coc` · `6.2-02DaoDap` · `6.2-03Mong` · `6.2-04CoCot` · `6.2-05DamMong` · `6.2-06Cot` · `6.2-07Dam` · `6.2-08San` · `6.2-09CauThang` · `6.2-10ThepHinh` · `6.2-11Tuong` · `6.2-12HoanThien` · `6.2-13Dien` · `6.2-14Nuoc` · `6.2-15CaiTao`

Trong mỗi sheet: dòng **công tác** (`CT` — mã hiệu, tên, đơn vị, KL = tổng các dòng dưới) → các dòng **chi tiết** (`CTiet`) → các dòng **trừ** (`Tru`, số bộ phận âm). Có thể chia nhóm bằng dòng `HM` (VD "TẦNG 2").

- **Tên công tác** đặt theo đúng cách gọi của định mức để áp mã được (PL VI): công việc + vật liệu + mác + quy cách + chiều dày/chiều cao + biện pháp. VD `Bê tông dầm đổ tại chỗ, đá 1x2, mác 250`. Cùng tên–đơn vị ở nhiều sheet thì bảng 6.1 tự gộp.
- **Mã hiệu định mức**: để `[Chờ bổ sung]` (ô vàng), anh Thành hoặc phần mềm dự toán tra. Chỉ ghi mã khi có nguồn (thư viện mã của công ty, hồ sơ dự án).
- **Kích thước** ghi vào cột Dài/Rộng/Cao (m); `KL một bộ phận = PRODUCT` của các ô có số. **Hình bất quy tắc**: ghi **diện tích vào Dài**, để trống Rộng, ghi Cao/dày; nêu rõ trong diễn giải. Khối lượng đếm (cái, bộ, mối nối) hoặc lấy từ bảng khác: ghi thẳng vào cột KL một bộ phận (`kl1`), có thể là công thức trỏ sang sheet khác (VD thép: `cong_thuc_thep()`).
- **Diễn giải** viết số theo đúng phép nhân, dấu phẩy thập phân, kèm vị trí và nguồn: `2 × 1,2 × 0,22 × 1,5 (bảng cửa KT-10)`. Phải khớp với số ở cột Dài/Rộng/Cao.
- **Mọi ô dẫn xuất là công thức**, không nhập cứng. Sửa một kích thước đầu vào thì tổng phải đổi theo. Làm tròn **3 số lẻ** (PL VI).
- Dòng T tô cam; dòng N chữ đỏ, không có số. Công tác có dòng T thì 6.1 ghi "Tạm tính".
- Sau khi thêm/sửa công tác: chạy `cap_nhat_6_1(wb)` (hoặc `python bangkl.py tonghop <file>` trên bản `_v` mới).
- **Cốt thép không còn là cột "hàm lượng" của từng cấu kiện.** Thép đi qua `TK-Thep` → `TK-Thep-TH` → dòng công tác cốt thép, xem `thong-ke-thep`. Hàm lượng kg/m³ chỉ dùng để **kiểm chéo** hoặc **tạm tính có ghi rõ (T)** khi hồ sơ không có số liệu thép.
  - *Bẫy 260625: điền đại 90 kg/m³ cho đài trong khi tính từ `Ø14a200` thực chỉ ~40–48 → vống gấp đôi.* Ước lượng không có căn cứ nguy hiểm hơn ô trống, vì ô trống thì thấy ngay là thiếu.

## 7. Cấu trúc thư mục kết quả

Theo quy ước thư mục của công ty (`E:\New folder\00-index.md`):

```
01-DuAn\<TenDuAn>\03-KhoiLuong\
  GhiChu.md                         ← nhật ký, đọc đầu mỗi phiên
  00-DanhMucBanVe_v01.xlsx
  00-DanhSachCanKiem.md             ← mọi dòng T/N, kèm biên độ ảnh hưởng
  GiaDinhDaDung.md
  <TenDuAn>_BangKL_v01.xlsx         ← sổ giao: 00-ThongTin, 6.1, các 6.2-*, TK-Thep, TK-Thep-TH, TK-Cua
  01-SoNoiBo\                       ← bản tô dấu, bảng đối chiếu, ảnh render, script riêng
```

Bóc lại hoặc sửa thì tạo **`_v02`**, giữ bản cũ, kèm `SoSanh_v01_v02.md`. Không ghi đè bản đã giao. Trước khi sửa file đã có thì chép vào `_backup\<TenDuAn>\YYYYMMDD-HHMM_<tên file>`.

## 8. Ngưỡng kinh nghiệm — nguồn duy nhất của cả bộ

Các skill khác **trỏ về mục này**, không chép lại.

| Chỉ tiêu | Dải hay gặp |
|---|---|
| BT toàn nhà | 0,30–0,45 m³/m² sàn |
| Thép | 90–130 kg/m³ BT · 10–12 kg/m² sàn |
| Dầm | 0,7–0,9 m/m² sàn · 0,06–0,10 m³/m² |
| Tường xây | 0,8–1,3 m² tường/m² sàn |

**Tạm dùng** các dải của bộ skill gốc (rút chủ yếu từ nhà phố khu vực TP.HCM) cho mọi công trình (anh Thành chốt 09/10/2026). Khi công ty có số liệu riêng cho địa bàn Quảng Trị thì thay vào bảng này. Suất vốn đầu tư dùng số do Bộ Xây dựng công bố hiện hành (kiểm tra lại hiệu lực), không dùng giá trọn gói ước.

Cách dùng đúng: **bật đèn đỏ đi kiểm**. Ra ngoài dải → **phải truy đến cấu kiện cụ thể**, không tự chỉnh tổng. **Nằm trong dải không chứng minh là đúng.**

Khi ngưỡng mâu thuẫn bản vẽ, **bản vẽ thắng**. Khi mâu thuẫn quy ước khách đã chốt, **quy ước khách thắng**.

**Tổng khớp KHÔNG phải xác nhận** — hai bản có thể lệch 0,1 % trong khi cấu thành khác hẳn vì hai sai số ngược chiều triệt tiêu nhau. Soi đến cấp tuyến / cấu kiện / quan hệ cha–con, không soi dòng tổng.

## 9. Bản đồ skill

| Việc | Skill |
|---|---|
| Nhận hồ sơ mới: danh mục bản vẽ, revision, đối chiếu KT–KC, thông tin chung, ma trận cấu kiện × nguồn | `doc-ban-ve` |
| Mở file CAD/PDF, lập bản đồ view, bung block, giải mã chữ lỗi font, đo hình học, đếm cấu kiện, render | `doc-ban-ve` |
| Cọc | `boc-coc` |
| Đào đắp đất, bê tông lót, vận chuyển đất | `boc-dao-dap` |
| Đài, móng đơn, băng, bè | `boc-mong` |
| Cổ cột, vách hố pit thang máy | `boc-co-cot-vach-pit` |
| Dầm móng, giằng móng, đà kiềng | `boc-dam-mong` |
| Cột, vách BTCT | `boc-cot-vach` |
| Dầm thân (kể cả dòng nút cột–dầm) | `boc-dam` |
| Sàn, sân thượng, mái | `boc-san-mai` |
| Tường xây, cửa, lanh tô | `boc-tuong-cua-lanh-to` |
| Cầu thang | `boc-cau-thang` |
| Thống kê cốt thép BTCT theo đường kính | `thong-ke-thep` |
| Thép hình, khung kèo, xà gồ, nhà tiền chế | `boc-thep-hinh` |
| Lát, ốp, trần, trát, bả, sơn, chống thấm, đá, mặt tiền, dàn giáo | `boc-hoan-thien` |
| Điện, cấp thoát nước: thiết bị, dây, ống | `boc-dien-nuoc` |
| Cải tạo, sửa chữa, nâng tầng | `boc-cai-tao` |
| Lập/kiểm dự toán, nhập phần mềm dự toán, triage bản vẽ mới, BOQ | `lap-du-toan` |
| Checklist trước khi giao, kiểm toán chéo, so sánh hai bản | `kiem-va-giao` |

## 10. Tệp kèm theo

| File | Việc |
|---|---|
| `assets/Mau_BangKL_TT13_v01.xlsx` | Mẫu sổ khối lượng, có sheet ví dụ `6.2-ViDu` (xóa khi dùng thật) |
| `scripts/bangkl.py` | Tạo sổ, thêm sheet 6.2, ghi công tác + chi tiết có công thức, dựng lại 6.1, công thức trỏ thép. Chạy: `python bangkl.py mau <file>` hoặc `python bangkl.py tonghop <file>` |
