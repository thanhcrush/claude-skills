---
name: boc-dam-mong
description: Bóc dầm móng, giằng móng và đà kiềng — các tuyến bê tông cốt thép nằm dưới cốt nền nối các móng hoặc cổ cột với nhau. Dùng skill này khi người dùng nói bóc giằng móng, dầm móng, đà kiềng, đà kiềng cốt nền, DKT, DM, GM, ĐK, hoặc kiểm lại khối lượng giằng. Đây là cấu kiện sai nhiều nhất trong toàn bộ phần ngầm — trừ nhầm cột thay vì trừ đài từng làm dư 44 phần trăm chiều dài. Skill nêu rõ khi nào trừ móng, khi nào tính thông thủy cổ cột cộng nút giao, cách xác nhận một tuyến là có thật, cách ghép hình khai triển vào tuyến, và ván khuôn đáy khi nào có. Ghi vào sheet 6.2-05DamMong theo mẫu PL VI TT 13/2021.
---

# Bóc dầm móng, giằng móng, đà kiềng

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp và thứ tự gán phần giao ở mục 5.

Đây là cấu kiện **sai nhiều nhất** của phần ngầm. Bốn lỗi dưới đây đều đã xảy ra thật, và ba trong bốn là lỗi hệ thống chứ không phải sai số.

## 1. Ba câu hỏi phải trả lời riêng cho mỗi tuyến

### Câu 1 — Có ván khuôn đáy không? Theo **cấu tạo đáy** đọc trên mặt cắt.

| Đáy tuyến | Ván khuôn |
|---|---|
| **tựa lên nền, lên lót hoặc lên tường** | chỉ **hai thành** |
| **treo**, đáy không tựa gì | hai thành **+ đáy** |

Ảnh hưởng trực tiếp khối lượng ván khuôn. Ghi rõ "đáy tựa nền" hoặc "đáy treo" trong diễn giải. *(Bộ gốc mã hóa bằng MNG / MN cho phần mềm dtPro — bản này ghi thẳng bằng lời.)*

### Câu 2 — Ranh giới chiều dài? Theo **cấu tạo tuyến**.

| Cấu tạo | Chiều dài tính | Phần giao |
|---|---|---|
| Tuyến **chạy xuyên qua** móng / đài | **mép đài → mép đài** | phần nằm trong đài thuộc **đài** |
| Tuyến **nối giữa các cổ cột**, không xuyên móng | **mép cổ cột → mép cổ cột** (thông thủy) | **nút** = tiết diện cổ cột × chiều cao giằng (phần dưới sàn nền nếu có) → ghi **một dòng nút** trong công tác bê tông giằng, mỗi nút một lần |

Nút giao thuộc giằng theo nguyên tắc PL VI "nút cột–dầm tính vào dầm". Cổ cột phía `boc-co-cot-vach-pit` đã trừ đúng đoạn này — **hai skill phải khớp nhau**.

**Không trừ cả móng lẫn cổ cột tại cùng một vùng giao** — đó là trừ hai lần.
**Đo trực tiếp mép–mép rồi thì phần trừ đã xong**, không trừ lại lần nữa.

### Câu 3 — Chiều cao tính? Theo **quan hệ với sàn nền**.

- Không có sàn nền BTCT đổ liền khối → lấy **đủ H tiết diện**.
- Có sàn nền BTCT đổ liền khối trên giằng → phần trong chiều dày sàn thuộc **sàn**: cao tính = **H − dày sàn nền** (cùng nguyên tắc dầm–sàn).

### Ký hiệu trên bản vẽ không quyết định gì cả

`DM`, `GM`, `ĐK`, `DKT` chỉ là tên của từng hồ sơ. Giữ chúng ở cột Danh mục. **Không dùng ký hiệu để chọn ván khuôn đáy, cũng không dùng để chọn quy tắc trừ.** Phân loại theo hình học, cao độ và quan hệ liên kết đọc được trên mặt cắt.

## 2. Bốn lỗi thật — đọc trước khi đo

**Lỗi 1 — trừ cột thay vì trừ đài (260702).** Tuyến chạy xuyên đài mà lại trừ kích thước cột: ra 21,67 md thay vì 12,06 md, **dư 44 %**, khoảng 12 triệu trên dự toán 722 triệu. Nhà nhịp ngắn mà đài to thì phần giao đài chiếm rất lớn. Đây là lỗi hệ thống, không phải sai số.

**Lỗi 2 — bịa thêm tuyến từ một nét đứt (260702).** Thấy nét đứt ở trục B tưởng là dầm, thực chất là **ranh hạ cốt sàn WC (−0.10)**.

Một tuyến giằng **có thật** phải xác nhận được bằng **ít nhất một** trong ba dấu hiệu mạnh:

| Dấu hiệu | Ghi chú |
|---|---|
| **Nhãn tên dầm** trên tuyến (`GM-2`, `ĐK4`…) | mạnh nhất — hồ sơ lớn thường có |
| **Cặp nét khuất song song** cách nhau đúng bề rộng tuyến | phải đúng bề rộng, không phải hai nét bất kỳ |
| **Polyline khép kín chạy theo chu vi nhà** trên layer nét khuất | *hồ sơ nhà phố nhỏ hay vẽ kiểu này và **không có nhãn nào** — 260702: một LWP 5 đỉnh bbox 4200×5800 chính là bốn tuyến giằng biên* |

**Cảnh giác với nét đứt ĐƠN LẺ nằm giữa nhà**, không nối hai đài, không thuộc chu vi — đó thường là ranh cao độ, mép đài, hoặc ranh vật liệu. Trục B ở 260702 đúng là loại này.

Xác nhận thêm bằng: tuyến có **nối hai đài hoặc hai cổ cột** không · mặt cắt có thể hiện tiết diện tuyến đó không · bảng thống kê thép có cấu kiện tương ứng không.

Không có dấu hiệu mạnh nào và không nối hai gối → báo **N**, không tự tính.

**Lỗi 3 — mỗi hình khai triển là một tuyến (2622).** Tờ KC11 vẽ ĐK4 thành hai hình (C→B' 3900 và B'→A 4100), thực chất là **một tuyến dài 8 m**. Lặp lỗi cho ĐK5, ĐK6 nên thiếu khoảng 16 md.

> Cách đúng: **đọc tên tuyến trên mặt bằng đà kiềng trước** — tuyến nào chạy trục nào, dài bao nhiêu — rồi mới ghép các hình khai triển vào tuyến. **Tổng các nhịp khai triển phải khớp chiều dài tuyến trên mặt bằng.**

**Lỗi 4 — tin nhãn tiết diện trên mặt bằng (2614).** Nhãn ghi `GM-x (BxH)` nhưng **số thứ hai luôn là 150** cho mọi giằng bất kể tiết diện thật. Ban đầu đoán 150 là chiều dày bê tông lót — **sai**. H thật là 1500 mm cho cả 17 giằng, chỉ tờ chi tiết mới cho biết.

Thêm: **2625 — giằng đổi tiết diện giữa các nhịp** (DK3/4/5/6: nhịp A-B là 250×500, nhịp B-C là 500×900 hoặc 400×800). **Đọc tiết diện theo từng nhịp**, không lấy một tiết diện cho cả tuyến.

## 3. Nguồn và vai trò

| Nguồn | Vai trò |
|---|---|
| **Mặt bằng đà kiềng / giằng móng** | **nhận diện tuyến** — tên tuyến, trục, chiều dài tổng. Đọc trước tiên |
| Mặt bằng móng | lấy đường bao **bê tông** các đài để tính phần trừ |
| Hình khai triển từng giằng | tiết diện từng nhịp, thép |
| Mặt cắt | **đáy tựa nền hay treo** → ván khuôn đáy; cao độ; quan hệ với sàn nền |
| Mặt bằng cột / cổ cột | kích thước cổ cột theo phương tuyến (tính thông thủy và nút) |
| **Mặt bằng sàn trệt** | tìm đà kiềng cốt nền không có trên tờ móng |

Đà kiềng cốt nền (DKT) rất hay nằm trên **mặt bằng sàn trệt** chứ không phải tờ móng — 2625 có DKT 200×250 chỉ xuất hiện trên mặt bằng thép sàn trệt, cả bộ gốc lẫn ChatGPT đều sót.

## 4. Quy trình

**B1 — Lập danh sách tuyến từ mặt bằng.** Mỗi tuyến: tên, trục, điểm đầu–cuối, chiều dài tổng trên mặt bằng. Đây là danh sách điều khiển, chưa lấy số.

**B2 — Xác nhận từng tuyến** bằng ít nhất một dấu hiệu mạnh ở mục 2. Nét đứt đơn lẻ giữa nhà, không nối hai gối → **N**.

**B3 — Ghép hình khai triển vào tuyến**, kiểm tổng nhịp khớp chiều dài tuyến.

**B4 — Tách đoạn.** Tách khi đổi tiết diện · đổi cao độ · đổi cấu tạo đáy (tựa nền ↔ treo) · đổi quy tắc trừ. Ghi xong đoạn nào tô dấu ngay đoạn đó.

**B5 — Tính chiều dài và nút** theo mục 1 câu 2.

Có DXF: ưu tiên **đo trực tiếp đoạn thông thủy mép móng (mép cổ cột) → mép móng (mép cổ cột)**, kiểm lại bằng `Dài thô − tổng đoạn tuyến nằm trong polygon móng / cổ cột`. Xác nhận đúng đường bao **bê tông móng**, không phải bê tông lót.

Chỉ có PDF, thứ tự ưu tiên: kích thước thông thủy ghi trực tiếp → tim–tim kết hợp khoảng từ tim đến mép → chuỗi kích thước suy ra → đo tỷ lệ sau khi hiệu chuẩn.

Với móng đối xứng và tuyến nối tim:
```
L thông thủy = L tim–tim − ½ kích thước gối trái − ½ kích thước gối phải (theo phương tuyến)
```
**Không chia đôi máy móc** khi móng lệch tâm, móng biên, móng chung, hoặc tuyến đi chéo. Thiếu độ lệch thì ghi **T** hoặc **N**, không tự giả định.

**Nút**: đếm số cổ cột mà tuyến **nối vào** (không đếm cổ cột ở đầu tuyến xuyên đài). Một cổ cột có nhiều giằng giao vào → **chỉ một nút**, gán cho giằng sâu nhất; giằng còn lại tính thông thủy, không thêm nút.

**B6 — Kiểm chéo.** Cộng các đoạn + bề rộng các gối phải bằng tổng chiều dài tuyến trên mặt bằng. Liệt kê các cặp nét khuất theo phương x và y trong view — trục nào không có cặp nét kèm nhãn thì **không có giằng ở đó**. Số nút ở đây = số cổ cột đã trừ nút ở `boc-co-cot-vach-pit`.

## 5. Ván khuôn

- Thành: 2 × chiều cao tính × chiều dài thông thủy. Giằng biên có sàn nền ở một phía: thành ngoài lấy **đủ H**, thành trong lấy **H − dày sàn nền**.
- Đáy: **chỉ khi đáy treo** — bề rộng × chiều dài thông thủy.
- Mặt nút lộ ra (cổ cột rộng hơn giằng) tính vào ván khuôn giằng nếu đáng kể; nhỏ thì bỏ qua và ghi rõ quy ước.

## 6. Ghi sổ khối lượng

Sheet `6.2-05DamMong`. Công tác: bê tông giằng móng / dầm móng · ván khuôn giằng · cốt thép (trỏ `TK-Thep-TH`, bộ phận "Giằng móng, dầm móng").

- Dòng chi tiết giữ ký hiệu gốc kèm trục và nhịp: `ĐK4 trục C(1-2)`, `DKT1 trục B(2-3)`.
- **Cột Dài ghi chiều dài thông thủy.** Diễn giải ghi cách ra số: `Tim trục 5,6 − giao 2 đài 2×1,1 = 3,4` hoặc `đo mép đài → mép đài, không trừ thêm`.
- Dòng nút: `Nút cổ cột C1 trục B-2 × giằng ĐK4` — Dài × Rộng = tiết diện cổ cột, Cao = chiều cao giằng tính.
- Rộng × Cao = tiết diện **của đúng nhịp đó**.

## 7. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã lập danh sách tuyến **từ mặt bằng trước**, không đọc hình khai triển trước.
- [ ] Mỗi tuyến xác nhận được bằng **ít nhất một dấu hiệu mạnh**: nhãn tên dầm · cặp nét khuất đúng bề rộng · polyline khép kín theo chu vi nhà.
- [ ] Nét đứt **đơn lẻ giữa nhà**, không nối hai gối, đã để N — không nhầm ranh hạ cốt thành giằng.
- [ ] **Tổng các nhịp khai triển khớp chiều dài tuyến trên mặt bằng.**
- [ ] Tiết diện đọc **theo từng nhịp**; **không tin nhãn tiết diện trên mặt bằng** khi chưa đối chiếu tờ chi tiết.
- [ ] Tuyến xuyên móng đã trừ **đường bao bê tông móng**, không nhầm bê tông lót.
- [ ] Tuyến nối cổ cột tính **thông thủy + nút**; số nút khớp với phần cổ cột đã trừ.
- [ ] **Không trừ cả móng lẫn cổ cột cùng một vùng giao**; đo mép–mép thì **không trừ lần thứ hai**.
- [ ] Có sàn nền BTCT liền khối thì chiều cao tính = H − dày sàn nền.
- [ ] Tuyến lệch tâm, đi chéo, móng biên đã xử lý hình học thực tế, không chia đôi máy móc.
- [ ] `Dài` **không âm** và không lớn hơn chiều dài tuyến trên mặt bằng.
- [ ] Đã rà **đà kiềng cốt nền trên mặt bằng sàn trệt**, không chỉ đọc tờ móng.
- [ ] Ván khuôn đáy chỉ tính cho tuyến **treo**, đọc từ mặt cắt.
- [ ] Có đủ công tác bê tông · ván khuôn · cốt thép.
- [ ] Bản tô dấu phủ kín; trục nào không có tuyến đã nêu rõ.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
