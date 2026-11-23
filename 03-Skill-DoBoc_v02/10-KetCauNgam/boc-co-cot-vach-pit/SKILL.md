---
name: boc-co-cot-vach-pit
description: Bóc cổ cột và vách hố pit thang máy — phần cấu kiện đứng nằm dưới cốt nền, nối móng với cột tầng trệt. Dùng skill này khi người dùng nói bóc cổ cột, cổ móng, cổ vách, đoạn cột dưới nền, vách pit, vách hố thang máy, hoặc hỏi công trình này có cổ cột không. Dùng cả khi kiểm một bản bóc cũ nghi bị tính trùng cổ cột vào chiều cao đài hoặc vào nút giằng, hoặc nghi bỏ sót cổ cột. Đây là cấu kiện bị bỏ quên và bị tính trùng nhiều nhất vì hồ sơ Việt Nam thường không có tờ riêng cho nó. Ra bê tông và ván khuôn cổ cột, vách pit theo quy ước giao cấu kiện PL VI TT 13/2021, ghi vào sheet 6.2-04CoCot.
---

# Bóc cổ cột và vách hố pit

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp và **thứ tự gán phần giao sàn → dầm/giằng → cột** ở mục 5. Cổ cột giao với bốn cấu kiện khác và là chỗ tính trùng nhiều nhất trong cả bộ.

## 1. Cổ cột là gì và tại sao hay bị bỏ quên

**Cổ cột = đoạn cấu kiện đứng từ mặt trên móng đến cốt nền nhà.**

Hồ sơ Việt Nam **thường không có tờ nào tên "cổ cột"**. Nó nằm ẩn trên mặt cắt móng. Không thấy tờ riêng không có nghĩa là không có cổ cột — đó là lý do cấu kiện này hay bị bỏ sót nguyên khối.

Phép kiểm tồn tại là cao độ:

```
H thô = Cốt nền − Cao độ mặt trên móng
```

| Kết quả | Nghĩa |
|---|---|
| **H thô > 0** | **Bắt buộc phải có** cổ cột hoặc cổ vách. Không được bỏ. |
| **H thô = 0** | Có thể không có cổ cột — nhưng phải **ghi rõ số 0 và lý do**, không im lặng bỏ trống. |
| **H thô < 0** | Đọc sai cao độ hoặc sai cấu tạo. Kiểm lại, không tự sửa dấu. |

**Không kết luận "móng cọc thì không có cổ cột".** Một số đài có mặt trên ngay tại cốt nền nên đúng là không có, nhưng kết luận đó chỉ hợp lệ khi **cao độ xác nhận**, không phải vì loại móng.

## 2. Chiều cao tính bê tông — theo thứ tự gán phần giao

Từ H thô, **trừ** những đoạn đã thuộc cấu kiện khác:

```
H tính = H thô − Σ (chiều cao giằng nối vào cổ cột trong đoạn này) − (phần nằm trong chiều dày sàn nền BTCT, nếu có)
```

- Đoạn nằm trong chiều cao **giằng** nối vào cổ cột = **nút**, tính vào công tác bê tông giằng (`boc-dam-mong`).
- Đoạn nằm trong chiều dày **sàn nền BTCT** đổ liền khối = tính vào sàn (`boc-san-mai`).
- Giằng nằm thấp hơn cốt nền (VD giằng −0.500, cốt nền ±0.000, không có sàn BTCT) → cổ cột có **hai đoạn**: mặt móng → đáy giằng, và mặt giằng → cốt nền. Ghi hai dòng chi tiết hoặc một dòng với diễn giải trừ rõ ràng.

Diễn giải bắt buộc ghi đủ: **cốt nền**, **cao độ mặt trên móng**, **cao độ và chiều cao giằng**, chiều dày sàn nền (nếu trừ), kèm tờ nguồn. Đây là cách duy nhất để người khác kiểm lại.

## 3. Quan hệ với bốn cấu kiện xung quanh — đọc trước khi lấy số

| Cấu kiện | Ranh giới | Sai khi |
|---|---|---|
| **Móng / đài** | cao đài tính hết bê tông móng, **dừng ở mặt trên móng** | gộp cổ cột vào cao đài — *2622: cao đài ghi gồm cả 400 mm cổ cột* |
| **Giằng móng** | nút giao cổ cột–giằng **thuộc giằng** (PL VI: nút cột–dầm tính vào dầm) | cổ cột lấy đủ H thô **và** giằng cũng tính nút → trùng. Không ai tính nút → thiếu |
| **Sàn nền BTCT** | phần trong chiều dày sàn thuộc sàn | cổ cột lên tới cốt nền trong khi sàn phủ bì → trùng |
| **Cột tầng trệt** | cột bắt đầu **từ cốt nền** (mặt sàn nền) trở lên | cho cột trệt chạy từ mặt móng lên — tính trùng đúng đoạn cổ cột |

Dầm móng xuyên móng trừ móng; giằng nối cổ cột tính thông thủy + nút — **không trừ cả hai tại cùng một vùng giao**.

## 4. Kiểm kê — đối chiếu ba danh sách

Lập ba danh sách rồi ghép:

1. **Móng / đài** — từ `boc-mong`.
2. **Cột và vách tầng trệt** — từ mặt bằng cột trệt.
3. **Cổ cột / cổ vách** đã tính.

Mỗi vị trí phải có **một kết luận rõ ràng**, không được để trống:

- có cổ cột, H thô = …, H tính = …;
- không có vì mặt trên móng trùng cốt nền (H = 0);
- móng này **không đỡ cột** nào (móng bể, móng thiết bị);
- móng này **đỡ nhiều cột hoặc vách** → nhiều cổ cột trên một móng;
- chưa đủ cơ sở → **N**.

**Không mặc định số cổ cột bằng số móng.** Móng chung đỡ hai ba cột là chuyện thường; ngược lại có móng không đỡ cột nào.

## 5. Tiết diện

**Có thiết kế cổ cột riêng** (mặt bằng, mặt cắt, bảng, chi tiết cổ cột): ưu tiên nguồn đó, đối chiếu với mặt bằng móng và cột trệt.

**Không có thiết kế riêng** — trường hợp phổ biến:

- vị trí và số lượng: từ mặt bằng móng và mặt bằng cột/vách trệt;
- tiết diện: theo mặt cắt hoặc chi tiết **cột tầng trệt**, nhưng phải **kiểm xem có đổi tiết diện tại cốt nền không** — nhiều hồ sơ cổ cột to hơn cột trệt;
- chiều cao: theo mục 1–2.

**Không mặc định mọi cổ cột cùng tiết diện.** Cũng không mặc định cùng chiều cao — móng ở các cao độ khác nhau thì cổ cột cao khác nhau, đây là chuyện thường ở nhà có móng lệch hoặc trên đất dốc.

Tiết diện suy từ cột trệt thì để trạng thái **S**, ghi rõ cách suy trong Diễn giải.

## 6. Vách hố pit thang máy

Vách pit là cấu kiện đứng dưới cốt nền nên thuộc skill này. Nguồn: mặt bằng móng · chi tiết pit · mặt cắt thang máy · cao độ đáy và đỉnh pit · chi tiết lõi.

- Tách **từng cạnh vách** theo điểm đầu–cuối, ghi chiều dài, chiều dày, chiều cao.
- Vách **chữ L hoặc chữ U** phải tách cánh, hoặc tính theo **đường tim có kiểm góc**. **Không lấy kích thước lòng pit** làm tổng chiều dài vách — cách đó thiếu thể tích ở góc.
- Chiều cao vách: từ mặt bản đáy pit đến cốt nền, trừ phần nằm trong sàn hoặc dầm theo thứ tự gán phần giao.
- Trừ lỗ cửa thang máy nếu lỗ nằm trong phạm vi vách pit và thể tích ≥ 0,1 m³ (PL VI), đo khoảng hở trên mặt bằng.

Ranh giới với các skill khác:

- **Bản đáy pit** → `boc-mong`.
- **Vách lõi thang máy phía trên cốt nền** → `boc-cot-vach`.
- **Chống thấm pit** → `boc-hoan-thien`.

## 7. Ván khuôn

- Cổ cột: chu vi × **H tính** (không gồm đoạn nút và đoạn trong sàn). Mặt áp vào cấu kiện đã đổ trước (VD áp vách tầng hầm) không tính.
- Vách pit: hai mặt × chiều dài × chiều cao, trừ lỗ ≥ 1 m² (PL VI); mặt ngoài áp đất / áp cừ thì theo biện pháp — không rõ thì T.

## 8. Ghi sổ khối lượng

Sheet `6.2-04CoCot`. Công tác: bê tông cổ cột · bê tông vách pit (nếu định mức tách vách) · ván khuôn cổ cột · ván khuôn vách · cốt thép (trỏ `TK-Thep-TH`, bộ phận "Cổ cột" và "Vách").

- Dòng chi tiết: `Cổ cột C1 trục B-2` · `Vách pit thang máy cạnh Bắc`.
- Cổ cột chữ nhật: Dài × Rộng = tiết diện, Cao = **H tính**.
- Vách pit: Dài = chiều dài cạnh, Rộng = chiều dày, Cao = chiều cao.
- Tiết diện **bất quy tắc** (tròn, chữ L, chữ T): diện tích tiết diện vào cột Dài, để trống Rộng, nêu rõ trong Diễn giải.
- **Cổ cột áp định mức CỘT** (anh Thành chốt 09/10/2026): đặt tên công tác bê tông, ván khuôn, cốt thép cổ cột **giống hệt** công tác tương ứng của cột (VD `Bê tông cột đá 1x2 mác 250`) để bảng 6.1 tự gộp; trong `TK-Thep` vẫn ghi bộ phận "Cổ cột" riêng để truy nguồn, dòng công tác cốt thép cột cộng cả hai bộ phận.

## 9. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã xác định **cốt nền** và **cao độ mặt trên từng loại móng**.
- [ ] Mọi vị trí móng–cột/vách đều có kết luận về cổ cột; không vị trí nào bỏ trống.
- [ ] Vị trí không có cổ cột đã ghi rõ H = 0 kèm lý do, không phải bỏ im lặng.
- [ ] **Không kết luận "móng cọc nên không có cổ cột"** chỉ theo loại móng.
- [ ] Không mặc định số cổ cột = số móng; đã rà móng chung đỡ nhiều cột và móng không đỡ cột.
- [ ] Thiếu thiết kế riêng thì tiết diện lấy từ cột trệt **đã kiểm có đổi tiết diện tại cốt nền không**, và để trạng thái S.
- [ ] Móng ở các cao độ khác nhau đã cho cổ cột chiều cao khác nhau.
- [ ] **Không tính trùng với cao đài** — cao đài dừng ở mặt trên móng.
- [ ] **Đã trừ đoạn nút giằng và đoạn trong sàn nền BTCT**, và `boc-dam-mong` có dòng nút tương ứng.
- [ ] **Không tính trùng với cột tầng trệt** — cột bắt đầu từ cốt nền.
- [ ] Đã rà và tính vách pit nếu công trình có thang máy; vách L/U đã tách cánh.
- [ ] Bản đáy pit đã chuyển sang `boc-mong`, không bóc ở đây.
- [ ] Có đủ công tác bê tông · ván khuôn · cốt thép.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
