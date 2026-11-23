---
name: boc-mong
description: Bóc khối lượng móng và đài cọc trong công trình xây dựng Việt Nam — móng đơn, móng băng, móng bè, đài cọc, móng chung, móng lệch tâm, móng thang máy, móng cầu thang, móng bể. Dùng skill này khi người dùng nói bóc móng, bóc đài, đài cọc, khối lượng móng, bê tông móng, ván khuôn móng, đếm móng, kiểm lại móng, hoặc đưa mặt bằng móng và hỏi ra bao nhiêu khối. Ra công tác bê tông và ván khuôn móng, ghi vào sheet 6.2-03Mong theo mẫu PL VI TT 13/2021. Không dùng cho cọc, cổ cột, giằng móng, đà kiềng, đào đất và bê tông lót — những thứ đó có skill riêng và rất dễ tính trùng với móng.
---

# Bóc móng và đài cọc

**Đọc `do-boc-loi` trước.** Skill này không lặp lại quy tắc bất biến, C/S/T/N, hai lớp dữ liệu.

## 1. Phạm vi — năm thứ dễ tính trùng nằm ngoài skill này

| Không thuộc skill này | Thuộc về |
|---|---|
| Cọc, chiều dài cọc, đập đầu cọc | `boc-coc` |
| **Cổ cột** từ mặt trên móng, **vách** hố pit | `boc-co-cot-vach-pit` |
| Dầm móng, giằng móng, đà kiềng | `boc-dam-mong` |
| Thép móng | `thong-ke-thep` (bộ phận "Móng, đài") |
| **Đào đất và bê tông lót** | `boc-dao-dap` — bóc **sau** khi móng đã chốt |

Ngược lại, **bản đáy hố pit thang máy thuộc skill này** — cùng cụm với móng thang máy. Chỉ phần **vách đứng** của pit mới sang skill cổ cột.

Cả năm cái đều giao với móng về mặt hình học. Đọc bảng quy ước cặp ở `do-boc-loi` mục 5 trước khi lấy bất kỳ chiều cao nào.

## 2. Nguồn và vai trò

| Nguồn | Vai trò |
|---|---|
| Mặt bằng móng / định vị móng | **kiểm kê vị trí và số lượng** |
| Mặt cắt và chi tiết **từng loại** móng | **kích thước, cao độ, cấu tạo bậc/chóp** |
| Mặt bằng cột / vách | kiểm quan hệ móng–cột, phát hiện móng chung |
| Mặt bằng cọc | số cọc mỗi đài, kiểm chéo kích thước đài |
| Ghi chú chung, bảng móng | mác bê tông, cao độ chuẩn |
| Mặt bằng sàn trệt, chi tiết PIT, cầu thang, thang máy, bể | **tìm móng không nằm trên tờ mang tên "móng"** |

Móng thang máy, móng cầu thang, móng bể nước và bể phốt thường **không có trên tờ móng**. Không tìm cấu kiện chỉ theo tên tờ.

## 3. Kiểm kê — ba bước, không được đảo thứ tự

### Bước 1 — Đếm tổng móng vật lý, chưa quan tâm mark

Đi theo một trình tự cố định trên mặt bằng. Mỗi móng vật lý được một mã vị trí tạm. Ở lượt này **không phân biệt M1, M2** và không đếm chữ thay cho cấu kiện.

Rà riêng: móng biên · móng góc · móng lệch trục · **móng chung nhiều cột** · móng thang máy · móng cầu thang · móng bể/PIT · móng không ghi nhãn.

Kết quả: `Tổng số móng vật lý`.

### Bước 2 — Đếm theo từng mark

Sau khi chốt tổng vật lý mới thống kê M1, M2, M3… và lập danh sách vị trí tương ứng. Móng không nhãn mã hoá riêng, **không tự gán vào loại gần nhất**.

### Bước 3 — Đối chiếu bắt buộc

```
Tổng theo các mark  +  móng chưa có mark  =  Tổng móng vật lý
```

**Chưa khớp thì chưa được lấy kích thước.** Phải tìm đúng vị trí và nguyên nhân: bỏ sót · đếm trùng · móng không nhãn · một móng hai nhãn · **móng chung bị đếm theo số cột** · ký hiệu trong chi tiết bị đếm nhầm · revision không đồng bộ. **Không sửa tổng bằng tay.**

Chỉ sau khi số lượng khớp mới ghép từng mark với mặt cắt và chi tiết — đúng revision, đúng loại móng, đúng số cọc, đúng hướng kích thước. Một mark có nhiều biến thể phải tách loại phụ.

## 4. Kích thước mặt bằng — chỉ lấy bê tông móng

Chi tiết móng thường có **hai hệ kích thước**: bê tông móng, và bê tông lót lớn hơn.

Chỉ lấy đường bao **bê tông móng**. Không lấy kích thước lót, hố đào, khoảng thao tác hay khoảng cách tim cọc — kích thước lót ghi riêng vào sổ nội bộ để `boc-dao-dap` dùng. Kiểm bằng: đầu đường gióng · hatch vật liệu · cao độ · quan hệ với lớp lót.

**Bẫy đường gióng thuộc cấu kiện khác.** 2625 móng M8/M9: số 850 gióng vào đài nhưng thực là của **giằng chạy qua**, đài thật 750. Phải đo Δ giữa hai đường bao bê tông, và kiểm hệ số vẽ của tờ chi tiết — bản vẽ chi tiết có thể phóng 4×.

**Đài đa giác hoặc vát góc**: lấy diện tích đáy **thực** từ polyline DXF bằng shoelace, **không nhân bao chữ nhật** (260625 từng vống vì nhân bao).

## 5. Chiều cao — chỗ sai nhiều nhất

Trên một mặt cắt móng cọc có tới tám kích thước đứng khác nhau. Phải phân biệt:

- chiều dày bản đáy
- chiều cao bậc
- phần chóp / vát
- **chiều cao đài**
- **chiều cao cổ cột** ← không thuộc móng
- chiều dày bê tông lót ← không thuộc móng
- khoảng từ mặt trên móng đến **mặt trên đầu cọc**
- phần đầu cọc cắm vào đài

**Sai phổ biến nhất: lấy khoảng từ mặt trên móng đến mặt trên đầu cọc làm chiều cao móng** — thiếu hẳn phần từ đầu cọc xuống đáy đài. Chiều cao móng phải lấy **giữa đúng hai mặt bê tông của móng**, hoặc bằng chênh cao độ mặt trên và đáy móng.

Ba bài học thật:

- **2611**: giả định mọi đài đỉnh −8.0 → DC-5A sai nặng. Thật là đỉnh −9.5, mặt bằng 4,7×1,1 chứ không phải 4,7×3,18, cao 1,8 chứ không phải 3,3. **Chiều cao đọc từ mặt cắt của TỪNG đài**, không giả định chung một cao độ.
- **2614**: mặt cắt có nhiều bracket cùng gốc đo `−2.000` — các số 1100 / 1500 / 1600 ứng với đầu cọc, đáy đài, đỉnh đài. Đọc sai **hai lần** trước khi đúng. Gặp trường hợp này phải **render mặt cắt và nhìn**, hoặc hỏi.
- **2622**: chiều cao đài ghi gồm cả 400 mm cổ cột. **Tách cổ cột ra**, nếu không sẽ tính trùng với skill cổ cột.

Đài **không có tờ chi tiết** → không có nguồn, để **N** hoặc **T** kèm cờ. Đừng nội suy theo cỡ đài khác.

Móng nhiều bậc hoặc có chóp: **tách từng khối**, không dùng diện tích đáy lớn nhất nhân toàn bộ chiều cao. Chóp cụt: `V = H/6 × [a·b + (a+c)(b+d) + c·d]`.

**Đầu cọc ngàm trong đài**: PL VI chỉ trừ lỗ rỗng trong bê tông khi thể tích ≥ 0,1 m³; phần đầu cọc ngàm mỗi cọc thường nhỏ hơn nhiều → **không trừ** `[Cần xác nhận lại]` — nếu dự án quy định khác thì theo dự án.

## 6. Ván khuôn móng

Theo bảng ván khuôn ở `do-boc-loi` mục 5:

- Thành từng khối: chu vi × chiều cao khối (bản đáy, từng bậc). Đáy đổ trên lót → **không** tính ván khuôn đáy.
- Mặt vát / chóp: chỉ tính khi bản vẽ hoặc biện pháp có ván khuôn mặt vát — không rõ thì T, hỏi.
- Mặt giáp móng đã đổ trước hoặc giáp vách tầng hầm: không tính.
- Móng băng: hai thành dọc tuyến + đầu tuyến; trừ đoạn giao nhau giữa hai tuyến.
- Vật liệu ván khuôn theo biện pháp; chưa có thì `[Chờ bổ sung]` trong tên công tác.

## 7. Móng băng và móng bè

Quy trình đếm từng móng rời ở mục 3 áp dụng cho **móng đơn và đài**.

- **Móng băng**: đơn vị kiểm kê là **tuyến / đoạn** theo điểm đầu–cuối. Tách khi đổi bề rộng, cao độ hoặc hình học. Cẩn thận chỗ giao nhau của hai tuyến — đếm một lần.
- **Móng bè**: đơn vị là **vùng** theo đường bao, chiều dày và cao độ. Vùng bất quy tắc dùng quy ước diện tích ở `do-boc-loi` mục 6.

## 8. Ghi sổ khối lượng

Sheet `6.2-03Mong`. Công tác tối thiểu:

| Công tác | Đơn vị |
|---|---|
| Bê tông móng / đài (tách theo mác, cỡ đá, loại móng nếu định mức tách) | m³ |
| Ván khuôn móng (theo vật liệu ván khuôn) | m² |
| Cốt thép móng | tấn — **trỏ sang `TK-Thep-TH`**, xem `thong-ke-thep` |
| Bê tông đáy pit, móng bể (nếu khác mác hoặc định mức) | m³ |

- Dòng chi tiết **theo mark và vị trí**: `Đài DC-5A trục C-3`, số bộ phận = số móng cùng kích thước. Diễn giải liệt kê đủ trục của các móng gộp.
- Móng bậc: mỗi khối một dòng chi tiết (bản đáy, bậc 1, chóp…).
- **Hình bất quy tắc**: diện tích vào cột Dài, để trống Rộng, chiều cao vào Cao; diễn giải ghi rõ.
- Diễn giải ghi đủ: tờ nguồn, cao độ đỉnh và đáy lấy từ đâu.
- **Không** có công tác đào đất và bê tông lót ở sheet này.

## 9. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã đếm **tổng móng vật lý độc lập** trước khi phân mark.
- [ ] `Tổng theo mark + móng không nhãn = Tổng vật lý`; mọi chênh lệch đã tìm ra vị trí và nguyên nhân.
- [ ] Đã rà móng chung, móng lệch trục, móng thang máy, móng cầu thang, móng bể — kể cả khi chúng không nằm trên tờ móng.
- [ ] Mỗi mark ghép đúng chi tiết, đúng revision.
- [ ] **Không nhầm kích thước lót với kích thước móng**; kích thước lót đã ghi sổ nội bộ cho `boc-dao-dap`.
- [ ] **Không nhầm chiều cao móng với cổ cột hoặc với khoảng đến đầu cọc.** Chiều cao đọc từ mặt cắt của từng đài, không giả định chung.
- [ ] Móng nhiều bậc hoặc có chóp đã tách khối.
- [ ] Đài đa giác dùng shoelace, không nhân bao chữ nhật.
- [ ] Có đủ công tác: bê tông · ván khuôn · cốt thép (trỏ TK-Thep-TH).
- [ ] Ván khuôn không tính đáy móng; mặt vát đã có căn cứ hoặc để T.
- [ ] Số cọc mỗi đài khớp với `boc-coc`; tổng cọc theo đài bằng tổng đếm ở `boc-coc`.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
