---
name: boc-cot-vach
description: Bóc cột và vách bê tông cốt thép từ cốt nền trở lên, theo từng tầng. Dùng skill này khi người dùng nói bóc cột, đếm cột, khối lượng cột, bê tông cột, ván khuôn cột, bóc vách, vách BTCT, lõi cứng, lõi thang máy, cột hàng rào, hoặc kiểm lại khối lượng cột. Quy ước cốt lõi theo PL VI TT 13/2021: cột tính từ mặt sàn đến đáy dầm sâu nhất giao vào cột, nút giao cột–dầm tính vào dầm, phần trong sàn tính vào sàn; một dòng một cột một tầng — quy ước này đi cặp với dầm tính thông thủy cộng dòng nút. Ghi vào sheet 6.2-06Cot. Không dùng cho cổ cột dưới cốt nền và vách hố pit, hai thứ đó có skill riêng.
---

# Bóc cột và vách BTCT

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp và thứ tự gán phần giao **sàn → dầm → cột** ở mục 5.

## 1. Quy ước cốt lõi — một cặp, không tách rời

> **Cột tính từ mặt sàn (mặt giằng, cốt nền) đến ĐÁY DẦM SÂU NHẤT giao vào cột.** Cột không có dầm giao (đỡ sàn trực tiếp) thì đến **đáy sàn**.
> **Một dòng = một cột × một tầng.**

```
H tính cột = Cao tầng (mặt sàn → mặt sàn) − H dầm sâu nhất giao vào cột
           = Cao tầng − dày sàn          (cột không có dầm giao)
```

Đoạn cột nằm trong chiều cao dầm là **nút**, thuộc **dầm** (PL VI: nút cột–dầm tính vào dầm); đoạn trong chiều dày sàn thuộc **sàn**. Quy ước này chỉ đúng khi đi **cặp** với file dầm: **dầm tính thông thủy mép cột → mép cột + một dòng nút cho mỗi cột**.

| Làm | Kết quả |
|---|---|
| Cột đến đáy dầm **+** dầm thông thủy **+** dòng nút | ✅ đúng, không trùng không thiếu |
| Cột lấy hết cao tầng **+** dầm có dòng nút | ❌ tính **trùng** nút và phần trong sàn |
| Cột đến đáy dầm **+** dầm thông thủy **không** có nút | ❌ tính **thiếu** nút |

*Bộ gốc dùng quy ước ngược (cột hết cao tầng, dầm trừ giao cột) vì phần mềm dtPro tự trừ phần dầm trong sàn. Bóc theo PL VI trên Excel thì dùng quy ước ở trên — đừng lẫn hai quy ước trong cùng một bộ.*

**Mác cột khác mác dầm sàn** (VD cột M300, dầm sàn M250): nút giao vẫn **tính vào dầm, theo mác dầm** (anh Thành chốt 09/10/2026) — cột vẫn dừng ở đáy dầm sâu nhất.

**2611 — lỗi nặng nhất của cấu kiện này:** gộp cột theo loại rồi lấy full chiều cao nhà 32,3 m → ra **303 m³**, sai gần gấp đôi. Cột phải bóc từng tầng một, mỗi tầng một dòng.

## 2. Phạm vi

| Thuộc skill này | Không thuộc |
|---|---|
| Cột từ **cốt nền** trở lên, mọi tầng kể cả hầm | Cổ cột dưới cốt nền → `boc-co-cot-vach-pit` |
| Vách BTCT, lõi cứng, lõi thang máy phía trên cốt nền | Vách hố pit dưới cốt nền → `boc-co-cot-vach-pit` |
| Cột hàng rào, cột sân, cột trang trí (nhóm riêng) | Thép cột → `thong-ke-thep` |
| | Nút cột–dầm → `boc-dam` |

Ranh giới với cổ cột: **cột tầng trệt bắt đầu từ cốt nền** (mặt sàn nền). Cho cột chạy từ mặt móng lên là tính trùng đúng đoạn cổ cột.

## 3. Kiểm kê — ba bước, làm riêng từng tầng

### Bước 1 — Đếm toàn bộ cột vật lý của tầng

Quét toàn bộ mặt bằng theo trục, đánh mã vị trí tạm, **chưa quan tâm C1 hay C2**.

Rà riêng: cột lệch trục · **cột nằm trong tường** · cột biên và cột góc · cột cầu thang · cột thang máy · cột ban công · cột đỡ mái che · **cột chỉ xuất hiện hoặc dừng ở một tầng**.

### Bước 2 — Đếm theo mark

Thống kê C1, C2… và ghép từng vị trí. Cột không nhãn mã hoá riêng, **không gán theo hình gần nhất**.

### Bước 3 — Đối chiếu

```
Tổng theo mark + cột chưa có mark = Tổng cột vật lý
```

Chưa khớp thì **chưa được lấy kích thước**. Không sửa tổng bằng tay.

### Bước 4 — Kiểm theo phương đứng

Đối chiếu tầng dưới – tầng hiện tại – tầng trên để tìm: cột **phát sinh**, cột **dừng**, cột **lệch**, cột **đổi mark hoặc đổi tiết diện**, cột **chuyển thành vách**.

Số cột đếm trên mặt bằng móng phải khớp mặt bằng dầm sàn từng tầng — lệch thì có cột dừng hoặc phát sinh, phải chỉ ra được vị trí.

## 4. Tiết diện

Ưu tiên **bảng hoặc chi tiết mặt cắt cột của đúng tầng đó**, đúng mark, đúng đoạn cao độ.

- **Cột thu tiết diện theo tầng là chuyện thường** — 2625: C5 đi 400 → 350 → 300. Không lấy một tiết diện cho cả chiều cao nhà.
- **Mặt bằng dầm sàn tầng X thể hiện tiết diện cột của tầng X**, tức cột **phía trên** sàn đó, không phải tầng dưới. Đối chiếu với bảng mặt cắt cột để xác nhận.
- Cột **không có mặt cắt** trong hồ sơ (2625: C6) → cờ cam, hỏi. Không nội suy theo cột khác.

Không có chi tiết cột thì có thể đo tỷ lệ trên mặt bằng, nhưng phải: xác định đúng đường bao **bê tông** (không phải bao tường hay lớp hoàn thiện) · hiệu chuẩn bằng kích thước có sẵn trên cùng view · đo hai phương · kiểm với lưới trục và cấu kiện lân cận · ghi rõ là đo tỷ lệ và để trạng thái **S** hoặc **T**.

Cột tròn, chữ L, chữ T hoặc bất quy tắc: diện tích tiết diện vào cột Dài, để trống Rộng, nêu rõ trong Diễn giải.

## 5. Chiều cao

Cao tầng lấy theo **mặt cắt** và cao độ tầng (mặt sàn → mặt sàn), **không** lấy máy móc từ chi tiết cột nếu chi tiết không phản ánh cao độ tầng thật. Rồi trừ theo mục 1.

**H dầm sâu nhất**: đọc mặt bằng dầm sàn **phía trên** cột, xét mọi dầm giao vào cột đó (cả hai phương). Cột biên, cột góc thường có dầm biên sâu hơn dầm trong — đọc đúng từng cột, không lấy một H dầm chung cho cả tầng.

Phải kiểm riêng: tầng lệch · thông tầng (cột qua hai tầng không có dầm giữa) · mái dốc · tum · sân thượng · cột đỡ mái hoặc bồn nước · khu vực đặc biệt. **Không áp một chiều cao chung cho toàn công trình.**

Cột tầng trệt bắt đầu từ **cốt nền**; phần từ mặt trên móng đến cốt nền là cổ cột, thuộc skill khác.

## 6. Vách BTCT

Vách ghi **cùng sheet này**, công tác riêng nếu định mức tách vách với cột.

- Đơn vị kiểm kê: **từng đoạn vách thẳng**, hoặc một vùng đa giác kiểm được hình học.
- Vách **chữ L, chữ U, lõi thang máy**: tách **từng cánh**, hoặc tính theo đường tim **có kiểm góc**. **Không lấy kích thước lòng** rồi cộng trừ tuỳ ý — cách đó thiếu thể tích ở góc.
- Chiều cao: cùng nguyên tắc — đến **đáy dầm** chạy trên đỉnh vách, hoặc **đáy sàn** nếu không có dầm; phần trong sàn thuộc sàn.
- Kích thước: Dài = chiều dài vách · Rộng = chiều dày · Cao = chiều cao tính.
- Trừ lỗ mở trên vách (cửa thang máy, lỗ kỹ thuật) bằng **dòng trừ** ngay dưới vách mẹ khi thể tích lỗ ≥ 0,1 m³ (PL VI), chỉ trừ khi có nguồn.
- Vách đổi chiều dày hoặc đổi chiều cao giữa các tầng phải tách dòng.
- Đừng nhầm vách BTCT với **tường xây** hoặc **vách kính** — xem dấu hiệu phân biệt ở `boc-tuong-cua-lanh-to`. Thang máy có thể là vách BTCT hoặc tường xây, cả hai đều gặp; **phải xác nhận trước khi tính**.

## 7. Cột hàng rào và cột phụ

Tách thành **nhóm riêng ở cuối sheet** (dòng `HM` riêng), không lẫn với cột nhà.

- Chiều cao theo **mặt đứng rào**, không theo chiều cao tầng.
- Đếm số cột nhà ở mặt bằng trệt thì **không đếm cột hàng rào**.
- Hàng rào có thể có mô-đun cao thấp khác nhau, tách dòng theo từng mô-đun.

## 8. Ván khuôn

- Cột: **chu vi × H tính** (đến đáy dầm sâu nhất). Mặt cột áp vào vách hoặc tường BTCT đã đổ trước không tính.
- Vách: hai mặt × chiều dài × chiều cao tính, trừ lỗ ≥ 1 m² (PL VI); cộng thành đầu vách.
- Mặt nút lộ ra giữa các dầm thuộc ván khuôn **dầm** (`boc-dam`), không tính ở đây.

## 9. Ghi sổ khối lượng

Sheet `6.2-06Cot`. Công tác: bê tông cột (theo mác, theo nhóm tiết diện và chiều cao nếu định mức tách) · bê tông vách · ván khuôn cột · ván khuôn vách · cốt thép (trỏ `TK-Thep-TH`, bộ phận "Cột", "Vách").

- Chia nhóm bằng dòng `HM` theo tầng: hầm → trệt/tầng 1 → lửng → tầng 2, 3… → tum.
- Dòng chi tiết chứa **tầng, mark và trục**: `Cột C1 tầng 2 trục B-3`.
- Gộp nhiều cột **cùng tầng, cùng mark, cùng tiết diện, cùng H tính** thành một dòng (số bộ phận = số cột) được, nhưng Diễn giải phải liệt kê đủ trục của từng cột.
- Diễn giải chiều cao ghi đủ: `Cao tầng 3,6 − dầm D2 0,45 = 3,15`.

## 10. Kiểm chéo

- Số cột trên mặt bằng móng khớp mặt bằng dầm sàn từng tầng.
- Số dòng nút ở `boc-dam` cho mỗi tầng = **số cột có dầm giao** của tầng đó.
- Ngưỡng suất bê tông xem `do-boc-loi` mục 8. Ra ngoài dải phải truy đến cột cụ thể, không tự chỉnh tổng.
- So với bản bóc theo quy ước khác (VD bản bóc trên dtPro): bê tông **cột** theo PL VI sẽ **nhỏ hơn** (mất phần nút và phần trong sàn), bê tông **dầm, sàn** lớn hơn tương ứng — **tổng bê tông thân phải gần như không đổi**. Khi báo cáo nêu rõ chênh do quy ước.

## 11. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã đếm **tổng cột vật lý từng tầng** trước khi phân mark.
- [ ] `Tổng theo mark + cột chưa mark = Tổng vật lý` cho **từng tầng**.
- [ ] Đã đối chiếu cột **giữa các tầng**; cột phát sinh, cột dừng, cột đổi tiết diện đã chỉ ra vị trí.
- [ ] **Một dòng một cột một tầng**; không có dòng nào gộp nhiều tầng.
- [ ] **H tính = cao tầng − H dầm sâu nhất giao vào cột** (hoặc − dày sàn), đọc dầm **từng cột**; file dầm có **dòng nút** tương ứng.
- [ ] Cột khác mác dầm sàn: nút vẫn tính vào dầm theo mác dầm.
- [ ] Cột tầng trệt bắt đầu từ **cốt nền**, không tính trùng cổ cột.
- [ ] Tiết diện lấy từ bảng mặt cắt **của đúng tầng**; cột thu tiết diện đã tách dòng.
- [ ] Cột không có mặt cắt đã gắn cờ và hỏi, không nội suy.
- [ ] Đo tỷ lệ (nếu có) đã hiệu chuẩn và ghi trạng thái S hoặc T.
- [ ] Tầng lệch, thông tầng, tum, mái dốc, cột đỡ bồn nước đã rà.
- [ ] Vách L/U và lõi thang máy đã tách cánh hoặc tính tim có kiểm góc; đã xác nhận thang máy là **vách BTCT hay tường xây**.
- [ ] Cột hàng rào tách nhóm riêng, chiều cao theo mặt đứng rào.
- [ ] Có đủ công tác bê tông · ván khuôn · cốt thép.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
