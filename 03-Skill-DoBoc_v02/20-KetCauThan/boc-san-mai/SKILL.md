---
name: boc-san-mai
description: Bóc sàn bê tông cốt thép và mái — sàn các tầng, sàn nền trên đất, sàn nắp hầm, ban công, sân thượng, sàn hạ cốt, sàn dốc, sàn mái BTCT, sê nô, và mái ngói, mái tôn, mái bê tông dốc dán ngói. Dùng skill này khi người dùng nói bóc sàn, diện tích sàn, bê tông sàn, ván khuôn sàn, bóc mái, lợp mái, sàn mái, sân thượng, mái tum, hoặc kiểm lại diện tích sàn. Quy ước cốt lõi theo PL VI TT 13/2021: sàn tính diện tích phủ bì trừ ô trống, gồm cả phần dầm, cột, vách nằm trong sàn; đi cặp với dầm lấy H trừ dày sàn. Chứa hai bẫy ngược chiều nhau ở biên sân thượng và ở mái. Ghi vào sheet 6.2-08San.
---

# Bóc sàn và mái

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp ở mục 5.

## 1. Quy ước cốt lõi

> **Sàn tính diện tích PHỦ BÌ, trừ ô trống.**
> **Không trừ dầm, không trừ cột** — phần dầm, cột, vách nằm trong chiều dày sàn thuộc **sàn** (PL VI TT 13/2021).

```
Diện tích tính = Diện tích phủ bì − Tổng diện tích ô trống
Thể tích       = Diện tích tính × Chiều dày
```

Quy ước này đi cặp với **dầm lấy H − dày sàn** (`boc-dam`) và **cột tính đến đáy dầm / đáy sàn** (`boc-cot-vach`). Vì vậy tuyệt đối không:

- trừ bề rộng dầm khỏi diện tích sàn;
- chia sàn thành ô thông thuỷ giữa các dầm rồi cộng lại **để giao**;
- thêm dòng trừ "dầm trong sàn" hay "cột trong sàn".

Ô trống trừ khi thể tích ≥ 0,1 m³ (PL VI) — lỗ kỹ thuật nhỏ không trừ.

**Bóc từng ô sàn vẫn phải làm, nhưng để KIỂM.** Làm ở sổ nội bộ (ô thông thủy + phần trên dầm), hai cách phải ra cùng một số. Bảng giao vẫn là phủ bì trừ ô trống.

## 2. Phạm vi

| Thuộc skill này | Không thuộc |
|---|---|
| Sàn BTCT mọi tầng, sàn nền BTCT trên đất, sàn nắp hầm | Dầm → `boc-dam` |
| Ban công, sân thượng, sàn hạ cốt, sàn dốc, sê nô BTCT | Bản thang, chiếu nghỉ → `boc-cau-thang` |
| Sàn mái BTCT | Thép sàn → `thong-ke-thep` |
| **Mái ngói, mái tôn, mái BT dốc dán ngói**: lớp lợp, úp nóc, diềm, máng | Xà gồ, cầu phong, lito, vì kèo thép → `boc-thep-hinh` |
| | Lớp nền dưới sàn nền (cát tôn, đá lót, BT lót nền) → `boc-dao-dap` |
| | Lát gạch mái, chống thấm → `boc-hoan-thien` |
| | Tường thu hồi, lan can, parapet → `boc-tuong-cua-lanh-to` |

## 3. Quy trình

1. Làm **riêng từng tầng**.
2. Xác định **đường bao phủ bì thực tế** của sàn, đối chiếu kết cấu với kiến trúc và mặt cắt.
3. Tách vùng khác **chiều dày · cao độ · loại · trạng thái**.
4. Tính diện tích phủ bì từng vùng.
5. Kiểm kê và trừ ô trống: ô cầu thang · giếng trời · thang máy · thông tầng · lỗ kỹ thuật lớn · vùng không đổ bê tông.
6. Tô dấu toàn bộ vùng sàn và ô trống; rà vùng chưa tô và tô trùng.
7. Bóc từng ô ở sổ nội bộ làm phép kiểm độc lập.

**Không mặc định toàn bộ đường bao kiến trúc là sàn BTCT.** Kiểm riêng: sàn hạ cốt, mái dốc, ban công, sê nô, và **nền trệt**.

## 4. Hai bẫy ngược chiều nhau — cùng ở 2625

Đây là cặp bẫy nguy hiểm vì chúng triệt tiêu nhau khi soi tổng.

**Bẫy 1 — bỏ sót sàn sân thượng.** Thuật toán tách ô sàn báo 159,68 m² trong khi lưới trục là 202,94 m². Nguyên nhân: **biên sân thượng chỉ có tường hoặc lan can 100, không có dầm bao**, nên vùng sàn nối liền vùng ngoài nhà và bị coi là "không có sàn".

> **Sân thượng là sàn đi lại được, luôn có bê tông.** Thiếu dầm bao không có nghĩa là thiếu sàn.

**Bẫy 2 — cho mái phủ kín lưới trục.** Sai theo chiều ngược lại: vùng trục 1–2 ở mái là **khung rỗng có ba lỗ giếng trời** (35,10 m²). Kết quả thật: sân thượng 203,95 m² so với mái 173,15 m².

**Cách nhận biết lỗ trên mái** — đối chiếu hai bản là cách chốt chắc nhất:

| Trên bản vẽ | Dấu hiệu |
|---|---|
| MB kiến trúc mái | vùng lỗ vẽ là **khung rỗng có dải viền**; dải viền **có mũi tên chỉ hướng dốc** nghĩa là chỗ đó **có** bê tông |
| MB dầm sàn mái | lỗ được **hatch ANSI31**, diện tích hatch khớp chính xác kích thước ghi trên bản kiến trúc |
| MB dầm sàn | lỗ còn được ký hiệu bằng **hai đường chéo hình chữ X** — đáng tin hơn suy đoán theo vị trí |

**"Sàn sân thượng ≥ sàn mái" là DẤU HIỆU CẢNH BÁO, không phải luật.** Ra ngược thì phải soi lại: hoặc bỏ sót sàn sân thượng, hoặc mái thật sự đua ra ngoài sân thượng (ô văng, mái đón, sê nô). Cả hai trường hợp đều phải chỉ ra được bằng bản vẽ.

Không mặc định mái phủ kín lưới trục, cũng không mặc định mái nhỏ hơn sân thượng.

## 5. Vài chỗ khác hay sai

- **2611 — nhà giật khối**: sàn phải đo **đường bao thật từng tầng**, tầng trên nhỏ hơn tầng dưới. Đừng lấy footprint đều rồi quên trừ hố thang, thang máy, giếng trời.
- **Không mặc định nền trên đất là sàn BTCT.** Rà mặt bằng sàn trệt tìm đà kiềng cốt nền và cấu kiện cốt nền khác — 2625 có DKT 200×250 chỉ nằm trên MB thép sàn trệt, cả bộ gốc lẫn ChatGPT đều sót.
- **Sàn âm khu ướt** (thường hạ 50 mm) và **sàn dự ứng lực** (kiểm DXF có `EUROCODE` hoặc đối tượng cáp) phải nhận ra sớm, tách dòng.
- Sàn khác chiều dày giữa các tầng là chuyện thường — 2625: trệt 100, tầng trên 120.
- Sàn nền BTCT đổ liền giằng: phần giằng trong chiều dày sàn nền thuộc sàn — `boc-dam-mong` lấy H − dày sàn nền.

## 6. Ván khuôn sàn

```
VK đáy sàn = Diện tích phủ bì − ô trống − hình chiếu đáy dầm (b × L thông thủy) − tiết diện cột, vách
VK thành   = chu vi biên sàn (không có dầm biên) × dày sàn  +  chu vi ô trống × dày sàn
```

- Biên có dầm biên: thành sàn đã nằm trong thành ngoài của dầm (`boc-dam`) — không tính lại.
- Sàn nền đổ trên đất / lót: **không** có ván khuôn đáy.
- Lỗ < 1 m² không trừ (PL VI).

## 7. Mái không phải BTCT

Bộ gốc chỉ ra diện tích mái vì đơn giá phần mềm dtPro đã gộp xà gồ, lito. Bóc theo PL VI (mục Mái: theo bộ phận — vì kèo, giằng, xà gồ, cầu phong, lớp lợp gồm úp nóc) thì phải tách:

| Công tác | Đơn vị | Ghi chú |
|---|---|---|
| Lợp mái ngói / tôn / dán ngói lên mái BT dốc | m² | diện tích **nghiêng thật**, tách theo loại vật liệu lợp |
| Úp nóc, úp sườn | m | chiều dài theo nóc, sườn |
| Diềm mái, máng xối, ống xối | m | |
| Xà gồ, cầu phong, lito, vì kèo | kg hoặc m³ | **sang `boc-thep-hinh`** (thép) — gỗ thì tính m³ ở đây |
| Lớp chống nóng, lót mái | m² | theo cấu tạo mái |

Diện tích mái dốc = diện tích hình chiếu ÷ cos(góc dốc), hoặc đo trực tiếp mặt nghiêng. Ghi rõ cách quy đổi và góc dốc lấy từ đâu.

Phân biệt cho đúng trước khi tính: **sàn mái BTCT** · **sê nô** · **mái ngói hoặc tôn có khung** · **mái BT dốc dán ngói** · **tường thu hồi** · **lan can hoặc parapet**. Mái tum thường nhỏ hơn sàn dưới.

Hồ sơ **thiếu tờ mái** là chuyện hay gặp — 2622 thiếu 7 tờ KC mái. **Không suy đoán**, ghi vào danh sách cần kiểm và xin bổ sung.

## 8. Ghi sổ khối lượng

Sheet `6.2-08San`. Công tác: bê tông sàn (theo mác, chiều dày nếu định mức tách) · bê tông sàn nền · ván khuôn sàn · cốt thép sàn (trỏ `TK-Thep-TH`) · các công tác mái ở mục 7.

- Chia nhóm `HM` theo tầng.
- Dòng chi tiết ghi tầng và phạm vi: `Sàn tầng 2 — vùng trục 1-4/A-C`; dòng trừ: `Trừ ô thang bộ tầng 2` (số bộ phận âm).
- Cột Cao = **chiều dày sàn**.
- **Vùng bất quy tắc**: diện tích vào cột Dài, để trống Rộng, chiều dày vào Cao; diễn giải nêu rõ.

## 9. Gate chốt — chưa đạt thì chưa giao

- [ ] Đường bao phủ bì xác định theo **từng tầng**, nhà giật khối không dùng chung footprint.
- [ ] Đã rà đầy đủ ô trống: thang bộ, thang máy, giếng trời, thông tầng, lỗ kỹ thuật.
- [ ] Vùng khác chiều dày, khác cao độ đã tách dòng; sàn âm khu ướt đã tách.
- [ ] **Không trừ dầm, cột khỏi sàn**, và file dầm đang lấy **H − dày sàn** — không có cơ chế trùng.
- [ ] **Sàn sân thượng đã kiểm riêng**, không để thuật toán bỏ sót vì thiếu dầm bao.
- [ ] **Mái không mặc định phủ kín lưới trục**; đã soi giếng trời và khoảng hở bằng cả MB kiến trúc lẫn MB dầm sàn.
- [ ] Quan hệ diện tích sân thượng và mái đã giải thích được bằng bản vẽ.
- [ ] **Không mặc định nền trên đất là sàn BTCT**; đã rà cấu kiện cốt nền trên MB sàn trệt.
- [ ] Đã bóc từng ô ở sổ nội bộ làm phép kiểm; hai cách ra cùng số.
- [ ] Ván khuôn đáy sàn đã trừ hình chiếu đáy dầm và tiết diện cột; sàn nền không có ván khuôn đáy.
- [ ] Mái không BTCT đã tách lớp lợp, úp nóc, diềm, máng; xà gồ, kèo đã chuyển `boc-thep-hinh`.
- [ ] Thiếu tờ mái đã ghi vào cần kiểm, không suy đoán.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
