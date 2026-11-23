---
name: kiem-va-giao
description: Tự kiểm trước khi giao kết quả đo bóc và dự toán, kiểm toán độc lập một hạng mục, đối chiếu hai bản bóc của hai người hoặc hai AI, và bóc lại khi bản cũ sai có tính hệ thống. Dùng skill này khi người dùng nói kiểm trước khi giao, chạy checklist, soát lại, kiểm toán, đối chiếu hai bản, so sánh với bản của ChatGPT, bản cũ sai rồi bóc lại, chốt trạng thái để chuyển phiên, hoặc chuẩn bị gửi khách. Chứa checklist nghiệm thu theo quy ước PL VI TT 13/2021 (giao cấu kiện, đủ công tác đi kèm, mẫu bảng 6.1/6.2), cách phân loại chênh lệch thành bốn nhóm, và mẫu yêu cầu gửi cho người kiểm toán chéo.
---

# Kiểm và giao

**Đọc `do-boc-loi` trước.**

## 1. Bốn tình huống

| Người dùng nói | Việc | Đọc mục |
|---|---|---|
| "chạy checklist trước khi giao" | Tự kiểm toàn bộ | 2, 3 |
| "kiểm toán độc lập hạng mục X" | Lập danh sách từ nguồn trước khi nhìn bảng cũ | 4 |
| "so bản này với bản kia" | Đối chiếu và phân xử | 5 |
| "bản cũ không dùng được, bóc lại" | Bóc lại độc lập | 6 |

## 2. Checklist trước khi giao

Chạy hết. Mục nào không đạt thì **sửa hoặc gắn cờ**, không bỏ qua im lặng.

### A. Nguồn và trạng thái
- [ ] Mọi số có **nguồn đủ trường** — xem `do-boc-loi` mục 3.
- [ ] Mọi số có **cách lấy** ghi kèm.
- [ ] Mọi số có **trạng thái C/S/T/N**; **N không cộng vào tổng**; công tác có T thì bảng 6.1 ghi "Tạm tính".
- [ ] Không có số nào là "theo thông lệ", "ước", "thường là" mà không phải T hoặc N.
- [ ] **Không có nguồn giả** — kiểu ghi "theo ghi chú KC chung B20" khi bản vẽ chỉ ghi mác cọc.
- [ ] **Không có mã hiệu định mức, đơn giá, mác vật liệu tự điền** không nguồn; chỗ trống mang đúng nhãn `[Chờ bổ sung]` / `[Tài liệu không đề cập]` / `[Cần xác nhận lại]`.
- [ ] Mọi dòng T/N có **một mục tương ứng** trong `00-DanhSachCanKiem.md` kèm **biên độ ảnh hưởng** (bao nhiêu m³, bao nhiêu tiền).
- [ ] Mọi giả định đã vào `GiaDinhDaDung.md` kèm lý do và ảnh hưởng.

### B. Hồ sơ và revision
- [ ] Đã kiểm kê đủ PDF, DWG/DXF, ảnh, Excel; ghi trang, view, tầng, **revision**.
- [ ] Đã phát hiện file trùng, bản cũ/mới, bản thay thế. **Không trộn revision** trong cùng cấu kiện.
- [ ] Có **ma trận cấu kiện × bản vẽ**; không tìm cấu kiện chỉ theo tên tờ.
- [ ] Đã nêu **vai trò từng nguồn**: nhận diện · lấy số · kiểm chéo.
- [ ] Cột Ký hiệu bản vẽ trong 6.2 khớp số hiệu tờ đã xác minh ở danh mục bản vẽ.

### C. Phủ kín — gate chặn
- [ ] Mỗi vùng vật lý rơi vào đúng một trong ba: **đã có mã tính** / **loại trừ có lý do** / **N**.
- [ ] Đã rà **ba lượt**: mark → hình học và lưới trục → cấu kiện đặc biệt, lệch trục, thiếu mark.
- [ ] Bản tô dấu đã rà **vùng chưa tô** và **vùng tô hai lần**; mã trên bản tô trùng vị trí trong sổ.
- [ ] Tuyến dài đã kiểm từ đầu đến cuối; không mất đoạn sau cột, sau giao trục, sau chỗ đổi tiết diện.
- [ ] **Không đếm chữ, mark hay hatch thay cho cấu kiện vật lý.**

### D. Quy ước giao cấu kiện (PL VI) — chỗ tốn tiền nhất
- [ ] **Thứ tự gán phần giao sàn → dầm/giằng → cột** áp thống nhất cho cả bộ.
- [ ] **Cột đến đáy dầm sâu nhất ↔ dầm thông thủy + dòng nút**; số dòng nút mỗi tầng = số cột có dầm giao.
- [ ] **Dầm H − dày sàn ↔ sàn phủ bì** — không trừ dầm khỏi sàn, không để dầm đủ H.
- [ ] **Dầm móng trừ đài ↔ giằng thông thủy cổ cột + nút** — không trừ hai lần cùng vùng giao; số nút giằng khớp phần cổ cột đã trừ.
- [ ] **Cao đài dừng ở mặt trên móng ↔ cổ cột tính riêng ↔ cột trệt từ cốt nền.**
- [ ] **Tường mẹ lấy cả ô mở ↔ cửa trừ đúng tường mẹ ↔ trừ lanh tô, giằng tường trong tường.**
- [ ] Nút giao khác mác bê tông đã tính vào dầm, theo mác dầm.
- [ ] Cổ cột đã đặt tên công tác theo định mức cột; cửa là công tác mua trọn bộ.

### E. Đủ công tác, chống trùng, chống sót
- [ ] **Mỗi cấu kiện bê tông đổ tại chỗ có đủ**: bê tông · ván khuôn · cốt thép · (lót) · (đào đắp).
- [ ] Có đủ nhóm mà phần mềm báo giá nhanh hay tự sinh: **đào đắp, lót, ván khuôn, thép theo đường kính, nối cọc, đập đầu cọc, xà gồ mái, bả, sơn lót, dàn giáo, dây và ống điện nước**.
- [ ] **Chống trùng**: cấu kiện nằm trên nhiều nhóm (vách lồng thang máy trên trục, cổ cột trong đài, chiếu tới trong sàn, hố đào gộp) đã kiểm không đếm hai lần.
- [ ] **Chống sót**: có bảng liệt kê phần **chưa dùng** — nhịp trống kèm lý do, nét ngoài phạm vi nhà.
- [ ] Danh mục công tác đã đối chiếu với **checklist đầy đủ của từng skill**, không chỉ theo yêu cầu viết tay của khách.

### F. Suất kiểm chéo
Bảng ngưỡng ở `do-boc-loi` mục 8. Điền số thực của công trình vào và đối chiếu.

- [ ] Mỗi hạng mục có **hai phép kiểm tổng độc lập**.
- [ ] Ra ngoài dải đã **truy đến cấu kiện cụ thể**, không tự chỉnh tổng.
- [ ] Nhớ: **nằm trong dải không chứng minh là đúng**; ngưỡng đang tạm dùng số nhà phố TP.HCM của bộ gốc.

### G. Excel — sổ khối lượng
- [ ] Sổ đúng mẫu: cột (1)–(10) đúng Bảng 6.2, cột phụ trợ (11)–(15) bên phải; bảng 6.1 đúng 7 cột; **không chen cột lạ**.
- [ ] Không còn `#REF!` `#DIV/0!` `#VALUE!` `#NAME?` `#N/A`.
- [ ] Không có kết quả dẫn xuất **nhập cứng**; sửa một kích thước đầu vào thì tổng đổi theo.
- [ ] **Diễn giải khớp số** ở cột Dài/Rộng/Cao và số bộ phận.
- [ ] Không có số đặt **sai cột**; công thức phân biệt **ô trống với số 0**; dòng trừ có số bộ phận âm.
- [ ] Đã chạy lại `cap_nhat_6_1`; tổng 6.1 = tổng các dòng công tác 6.2.
- [ ] `TK-Thep-TH` ô "Lệch" = 0.
- [ ] Tiêu đề đủ: tên công trình, hạng mục, địa điểm, ngày lập, đơn vị lập; khối lượng làm tròn 3 số lẻ.
- [ ] Mở lại file: đủ sheet, liên kết, vùng in, tiêu đề, độ rộng cột.

### H. Giao hàng
- [ ] File lưu bản `_v` mới, đúng thư mục `03-KhoiLuong\`; không ghi đè bản đã giao.
- [ ] Dòng T tô cam, dòng N chữ đỏ; ô chờ nhập tô vàng.
- [ ] Có `00-DanhSachCanKiem.md` với **biên độ ảnh hưởng** từng mục; có `GiaDinhDaDung.md`.
- [ ] `GhiChu.md` đã cập nhật: làm gì, ra số gì, còn treo gì.
- [ ] Memory đã cập nhật nếu có bài học mới.
- [ ] **Nói thẳng con số dùng được ngay và biên độ**, không kết thúc bằng lời khuyên chung chung.

## 3. Bốn câu phải trả lời được khi giao

1. **Con số dùng được ngay là bao nhiêu?**
2. **Biên độ sai bao nhiêu?** — cộng biên độ của mọi dòng T và N.
3. **Còn treo gì?** — danh sách cần kiểm, ai trả lời được.
4. **Nếu khách chốt các mục treo theo hướng xấu nhất thì số đổi bao nhiêu?**

Không trả lời được câu nào thì chưa giao được.

## 4. Kiểm toán độc lập một hạng mục

> **Lập danh sách từ nguồn TRƯỚC khi nhìn bảng hiện tại.**

Mở bảng cũ trước là mất tính độc lập — sẽ đọc theo lối mòn của bảng cũ và bỏ qua đúng chỗ bảng cũ sai.

Trình tự: đọc nguồn → lập danh sách vật lý độc lập → phủ kín → lấy kích thước → **rồi mới** mở bảng cũ đối chiếu.

So đến **cấp cấu kiện, tuyến, ô, mảng, quan hệ cha–con** — không so tổng. Mỗi chênh lệch phải chỉ được **vị trí cụ thể**.

## 5. Đối chiếu hai bản — phân loại chênh lệch thành bốn nhóm

Cách xử lý mỗi nhóm khác nhau, nên phải phân loại trước khi tranh luận:

| Nhóm | Nghĩa | Xử lý |
|---|---|---|
| **Thiếu cấu kiện thật** | một bản bỏ sót vùng vật lý | bổ sung — **lỗi nặng nhất** |
| **Khác quy ước đo hoặc trừ** | cùng nhìn thấy, khác cách tính (VD bản theo phần mềm cũ: cột hết cao tầng; bản PL VI: nút vào dầm) | chốt một quy ước, áp lại **cả hai** bản |
| **Sai ghép nguồn** | lấy số của cấu kiện khác, sai tờ, sai revision | sửa nguồn |
| **Giả định chưa được bản vẽ xác nhận** | không ai đúng | để **N**, hỏi khách |

Nguyên tắc phân xử:

- Mở bản kia **sau** khi đã bóc xong độc lập.
- Phân xử **bằng bản vẽ**, không bằng uy tín và **không theo số đông AI**.
- **Ghi cả trường hợp mình sai** — 2625: ChatGPT đúng, bộ gốc sai ở diện tích đài M5.
- **Giữ hình thức trình bày của bản kia nếu tốt hơn** — tách theo tầng rồi trục rồi đoạn; mục "chưa đủ cơ sở, để 0 kèm lý do"; đánh dấu mức chắc chắn từng dòng.
- Nếu **cả hai bản** không đủ cơ sở → ghi **N** và hỏi đúng vùng cần xác nhận, đừng chọn bừa một bên.

> **Tổng khớp KHÔNG phải xác nhận chéo.** 2625: hai bản chênh 0,015 m³ nhưng cấu thành khác hẳn — hai sai số ngược chiều triệt tiêu nhau. Soi **danh mục cấu kiện**, không soi dòng tổng.

## 6. Khi bóc lại vì bản cũ không dùng được

1. **Đọc bản cũ để biết nó SAI Ở ĐÂU**, không phải để chép số. Ghi ra ba lỗi gốc.
2. **Bóc lại độc lập** thành bản **`_v` mới**. Không mở bản cũ trong lúc bóc. Không ghi đè bản cũ.
3. Đối chiếu theo **danh mục cấu kiện**, không đối chiếu tổng.
4. Viết `SoSanh_vNN_vMM.md`: bản cũ sai gì · bản mới tìm thêm được gì · **chỗ nào bản cũ làm tốt thì giữ** (thường là hình thức bảng).
5. Nếu tổng hai bản gần nhau, **phải giải thích được vì sao** — thường là hai sai số ngược chiều, không phải xác nhận chéo.

**Khi nào bóc lại thay vì vá:** sai có **tính hệ thống** — mất quan hệ cấu kiện cha–lỗ mở, mã chồng lấn, bảng vá nhiều lần không truy được nguồn, **dùng lẫn hai quy ước giao cấu kiện**. Khi đó **dừng vá**, lập lại danh sách từ nguồn; bảng cũ chỉ dùng đối chiếu.

Lỗi **cục bộ** thì sửa dữ liệu gốc và rà ảnh hưởng dây chuyền. Mọi lần sửa tạo **phiên bản mới**, giữ bản đã chốt; trước khi sửa chép bản cũ vào `_backup\<TenDuAn>\`.

## 7. Mẫu yêu cầu gửi người kiểm toán chéo

Gửi cho AI khác hoặc nhân viên. **Chỉ gửi tờ, view, vùng liên quan** cộng bản tô dấu, bảng chi tiết và **câu hỏi cụ thể**. Không gửi cả lịch sử; không yêu cầu viết lại bảng nếu chỉ cần kiểm một rủi ro. Gửi ra ngoài công ty thì **hỏi anh Thành trước**.

**Kiểm toán chung:**
> Đọc độc lập các nguồn đính kèm. Với PDF, kiểm ngữ nghĩa, ký hiệu và phạm vi. Với DXF, kiểm hình học, bảng và block.
> Quy ước đo: PL VI TT 13/2021 — nút cột–dầm tính vào dầm, phần trong sàn tính vào sàn.
> Tập trung tìm: cấu kiện hoặc vùng bỏ sót · đếm trùng · sai loại, tầng, trục · ghép sai nhãn với block · sai kích thước · sai phần trừ · sai tổng nhóm · thiếu công tác đi kèm (ván khuôn, thép, lót, đào đắp).
> Chỉ kết luận khi chỉ được **nguồn và vị trí cụ thể**. Không kết luận từ số tổng.

**Kiểm toán tường:**
> Lập danh sách độc lập theo từng tầng: trục số từ nhỏ đến lớn, sau đó trục chữ. Ghi cả các tuyến phụ gần trục.
> Với mỗi tuyến: xác định tường 100/200/300, điểm đầu–cuối, và những cửa nằm **đúng trên tường đó**.
> So với sổ tường và bản tô dấu đính kèm, chỉ ra: đoạn chưa tính · đoạn tính trùng · sai bề dày · sai chiều cao · cửa gán nhầm tường mẹ · thiếu trừ lanh tô.

**Kiểm toán giằng và đà kiềng:**
> Kiểm **toàn tuyến** từng giằng từ đầu đến cuối, không đếm nhãn.
> Xác nhận mỗi tuyến bằng đủ hai dấu hiệu: **cặp nét khuất đúng bề rộng** và **nhãn tên dầm**. Tuyến chỉ có một dấu hiệu thì báo N.
> Kiểm chiều dài thông thủy giữa mép các đài / cổ cột và số nút. Kiểm tổng tuyến ngang và tổng tuyến dọc so với tổng chi tiết.

## 8. Chốt trạng thái để chuyển phiên hoặc chuyển người

Tóm tắt đủ sáu mục: **nguồn đang dùng** · **kết quả đã chốt** · **dòng T và N** · **mâu thuẫn chưa xử** · **phần còn thiếu** · **bước tiếp theo**.

Ghi vào `GhiChu.md`. Người tiếp theo — hoặc chính mình ở phiên sau — đọc là làm tiếp được ngay, không phải dựng lại bối cảnh.
