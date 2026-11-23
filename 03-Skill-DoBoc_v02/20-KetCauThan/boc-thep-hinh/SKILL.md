---
name: boc-thep-hinh
description: Thống kê thép hình và kết cấu thép — nhà tiền chế, nhà khung thép, cột thép, vì kèo thép, xà gồ, cầu phong, lito, hệ giằng, sàn deck, mái tôn có khung, bản mã và bulông. Dùng skill này khi người dùng nói thép hình, kết cấu thép, khung thép, nhà tiền chế, nhà thép, vì kèo, xà gồ, thép hộp, thép H, thép I, thép U, thép C, sàn deck, hoặc hỏi công trình khung thép này bao nhiêu tấn thép. Tính theo kilogam từng loại tiết diện theo PL VI TT 13/2021, tách gia công và lắp dựng, sơn tính theo m² bề mặt. Ghi vào sheet 6.2-10ThepHinh. Không dùng cho cốt thép trong bê tông cốt thép — thứ đó có skill riêng.
---

# Thống kê thép hình

**Đọc `do-boc-loi` trước.**

## 1. Hệ tính khác hẳn thép BTCT

| | Thép BTCT | Thép hình |
|---|---|---|
| Cách tính | từng thanh theo Ø, chiều dài, số lượng | `Số lượng × chiều dài × trọng lượng đơn vị kg/m` |
| Đơn vị | tấn theo bộ phận × nhóm Ø | kg / tấn theo nhóm cấu kiện |
| Skill | `thong-ke-thep` | skill này |

Công trình vừa có bê tông cốt thép vừa có khung thép thì **hai hệ tính song song**, không cộng vào nhau, không quy đổi qua lại.

## 2. Khi nào dùng

Nhà tiền chế · nhà xưởng khung thép · nhà phố hoặc biệt thự có tầng tum khung thép · mái che, mái đón, giếng trời khung thép · sàn deck · cầu thang thép · lửng thép · kết cấu thép xen BTCT · **xà gồ, cầu phong, lito đỡ mái ngói, mái tôn**.

*Bộ gốc bỏ qua xà gồ, lito vì đơn giá mái của phần mềm dtPro đã gộp. Bóc theo PL VI (mục Mái: theo bộ phận vì kèo, giằng, xà gồ, cầu phong, lớp lợp) thì **phải bóc** các thứ này ở đây.*

## 3. Nguồn

| Nguồn | Vai trò |
|---|---|
| **Bảng thống kê vật tư thép** trên bản vẽ kết cấu thép | nguồn chính — thường có sẵn kg từng loại |
| Mặt bằng và mặt đứng khung, mặt bằng mái | vị trí, số lượng, khẩu độ, bước khung, bước xà gồ |
| Chi tiết nút liên kết | bản mã, bulông, đường hàn |
| Mặt cắt khung, sơ đồ kèo | chiều dài nghiêng thật của kèo dốc |
| Thuyết minh | mác thép, tiêu chuẩn, lớp sơn |

Có bảng thống kê vật tư thì **luôn ưu tiên số trong bảng**. Bóc tay chỉ khi không có bảng.

## 4. Cách tính

```
Khối lượng (kg) = Số lượng × Chiều dài (m) × Trọng lượng đơn vị (kg/m)
```

**Trọng lượng đơn vị tra theo bảng thép tiêu chuẩn hoặc catalogue của đúng quy cách tiết diện**, ghi nguồn tra. Không ước, không lấy xấp xỉ — cùng ký hiệu `H300` nhưng khác chiều dày bản cánh là khác kg/m. Không tra được → `[Cần xác nhận lại]`.

Với thép tấm và bản mã: `Khối lượng = Diện tích × Chiều dày × 7850 kg/m³`.

**Kèo dốc lấy chiều dài nghiêng thật**, không lấy hình chiếu bằng. Cùng cách xử lý như bản thang nghiêng.

PL VI (mục Kết cấu thép): tính theo thanh, bản thép, **gồm nối chồng, phần cắt vát, bu lông, đai ốc**; **không tính** bu lông, chi tiết gá lắp tạm; lỗ khoét mỗi lỗ < 0,1 m² không trừ. Thép phục vụ thi công: ghi thời gian dùng, số lần luân chuyển, thu hồi.

Chiều dài lấy theo **tim** hay theo **chiều dài cắt thực** đều được, nhưng phải chốt một quy ước và **ghi rõ đang dùng cái nào** — hai cách lệch nhau ở phần nút liên kết.

## 5. Tách nhóm và tách công tác

| Nhóm | Gồm |
|---|---|
| **Kết cấu chính** | cột thép, kèo, dầm thép, dầm sàn deck |
| **Xà gồ và hệ giằng** | xà gồ C/Z, cầu phong, lito, giằng mái, giằng cột, thanh chống |
| **Bản mã, bulông, neo** | bản mã, bulông neo chân cột, bulông liên kết |
| **Phụ kiện** | máng xối thép, diềm, ke chống bão |

Mỗi nhóm cộng riêng. Định mức thường tách **gia công** và **lắp dựng** theo loại cấu kiện (cột, kèo, xà gồ…) — ghi hai công tác cùng khối lượng nếu cách áp mã của anh Thành tách như vậy `[Cần xác nhận lại]`.

## 6. Sơn kết cấu thép

PL VI: sơn kết cấu thép tính theo **m² bề mặt**; **không tính** diện tích chi tiết bản nối, bu lông; sơn trước khi lắp thì cộng thêm sơn dặm sau lắp. Diện tích bề mặt tra theo bảng tiết diện (m²/m) — không suy từ khối lượng. Sơn ghi ở `boc-hoan-thien` hoặc cuối sheet này, chỉ một chỗ.

## 7. Không thuộc skill này

- **Cốt thép trong bê tông** → `thong-ke-thep`.
- **Tôn lợp mái và tôn vách** → `boc-san-mai` và `boc-hoan-thien`, tính theo m².
- **Móng và bulông neo chôn trong móng**: phần bê tông thuộc `boc-mong`, phần bulông neo thuộc skill này.

## 8. Ghi sổ khối lượng

Sheet `6.2-10ThepHinh`. Mỗi nhóm một (hoặc hai: gia công / lắp dựng) công tác, đơn vị theo định mức (tấn hoặc kg).

- Dòng chi tiết: `Kèo K1 trục 2 — H300×150×6,5×9`, Số bộ phận = số lượng, Dài = chiều dài, **KL một bộ phận** = chiều dài × trọng lượng đơn vị (ghi `kl1` là công thức, VD `"=6.25*36.7"`), diễn giải ghi rõ kg/m tra từ đâu.
- Quy cách ghi đầy đủ: `H300×150×6,5×9`, `C200×75×20×2,3`, `Hộp 100×100×3`, `Tấm 10 mm`.

## 9. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã xác định công trình **có kết cấu thép** những phần nào, kể cả xà gồ, cầu phong, lito đỡ mái.
- [ ] Có bảng thống kê vật tư thì đã dùng số trong bảng.
- [ ] **Trọng lượng đơn vị tra theo đúng quy cách tiết diện**, có ghi nguồn tra, không ước.
- [ ] Kèo dốc lấy **chiều dài nghiêng thật**, không lấy hình chiếu bằng.
- [ ] Đã chốt và ghi rõ quy ước chiều dài: theo tim hay theo chiều dài cắt.
- [ ] Tách đủ bốn nhóm; gia công và lắp dựng đã tách nếu cần.
- [ ] Bản mã và bulông đã tính; bulông gá lắp tạm **không** tính.
- [ ] **Sơn không tính theo kg** — m² bề mặt, không tính bản nối, bu lông.
- [ ] Không cộng lẫn với thép BTCT; hai hệ để riêng.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
