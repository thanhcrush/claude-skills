---
name: boc-cau-thang
description: Bóc cầu thang bê tông cốt thép — bản thang nghiêng, chiếu nghỉ, chiếu tới, dầm chân thang, dầm chiếu nghỉ, dầm limon, bậc tam giác, bậc xây gạch, ram dốc, tam cấp. Dùng skill này khi người dùng nói bóc cầu thang, bóc thang bộ, khối lượng cầu thang, bê tông cầu thang, ván khuôn cầu thang, bản thang, chiếu nghỉ, bậc thang, ram dốc, hoặc kiểm lại khối lượng thang. Tách từng bộ phận để giải trình, ra công tác bê tông, ván khuôn, cốt thép, xây bậc; ghi vào sheet 6.2-09CauThang theo mẫu PL VI TT 13/2021. Không dùng cho đá lát bậc, lan can, tay vịn và trát thang, những thứ đó thuộc hoàn thiện.
---

# Bóc cầu thang

**Đọc `do-boc-loi` trước.**

## 1. Phạm vi

| Thuộc skill này | Không thuộc |
|---|---|
| Bản thang nghiêng, chiếu nghỉ, chiếu tới | Đá lát bậc, ốp cổ bậc → `boc-hoan-thien` |
| Dầm chân thang, dầm chiếu nghỉ, dầm limon | Lan can, tay vịn → `boc-hoan-thien` |
| Bậc tam giác BTCT, **bậc xây gạch** | Trát, sơn thang → `boc-hoan-thien` |
| Ram dốc, tam cấp, bậc tam cấp | Thép thang → `thong-ke-thep` (bộ phận "Cầu thang") |
| Móng và dầm móng cầu thang | *(nằm ở `boc-mong` và `boc-dam-mong`)* |

Định mức thường có công tác bê tông **cầu thang** riêng (khác dầm, sàn). **Dầm thang (dầm chân thang, dầm chiếu nghỉ, dầm limon) tính vào công tác cầu thang** — cả bê tông, ván khuôn, cốt thép (anh Thành chốt 09/10/2026). Vẫn bóc tách từng bộ phận thành dòng chi tiết để giải trình và để kiểm.

Móng cầu thang và dầm móng cầu thang thường **không nằm trên tờ móng** mà nằm trên tờ chi tiết cầu thang. Chúng thuộc skill móng và dầm móng — nhưng chính skill này là nơi phát hiện ra chúng, nên gặp thì báo sang.

## 2. Nguồn

| Nguồn | Vai trò |
|---|---|
| **Mặt cắt cầu thang** | nguồn chính — chiều dài triển khai, số bậc, cao bậc, cao độ chiếu nghỉ |
| Mặt bằng kết cấu bản thang từng tầng | bề rộng vế, vị trí dầm thang, hình dạng chiếu nghỉ |
| Chi tiết cầu thang | cấu tạo bậc, chiều dày bản, thép |
| Mặt bằng kiến trúc | công năng, phân biệt thang chính với thang phụ |
| Mặt cắt nhà | chiều cao tầng để kiểm chéo số bậc |

Nếu bản vẽ cho sẵn **diện tích bản thang** thì dùng số đó, ghi rõ nguồn.

## 3. Tách bộ phận — mỗi thứ một dòng chi tiết

Với **từng cầu thang, từng tầng**, tách các dòng sau:

| Bộ phận | Cách tính |
|---|---|
| **Bản thang nghiêng** | `Dài triển khai × Rộng vế × Dày bản` |
| **Chiếu nghỉ** | `Dài × Rộng × Dày` |
| **Chiếu tới** | thường đã tính vào sàn — **kiểm để không trùng** |
| **Dầm chân thang** | `Dài × Rộng × (H − dày bản gối lên)` theo thứ tự gán phần giao |
| **Dầm chiếu nghỉ** | như dầm thường: H − dày chiếu nghỉ |
| **Dầm limon** (nếu có) | dầm nghiêng dọc hai bên vế |
| **Bậc tam giác BTCT** | `số bậc × (rộng bậc × cao bậc ÷ 2) × rộng vế` |
| **Bậc xây gạch** | cùng công thức, nhưng là **công tác xây**, ghi riêng |

Không gộp toàn bộ cầu thang thành một dòng — dòng gộp không giải trình được và không kiểm được. Công tác (dòng `CT`) tự cộng các dòng chi tiết.

## 4. Ba chỗ hay sai

**Chiều dài bản thang là chiều dài TRIỂN KHAI, không phải hình chiếu bằng.** Lấy từ mặt cắt. Chỉ có kích thước chiếu bằng thì quy đổi theo độ dốc và **ghi rõ cách quy đổi** trong Diễn giải:

```
L triển khai = √(L chiếu bằng² + H vế²)
```

**Chiếu tới dễ tính trùng với sàn.** Vùng chiếu tới ở mỗi tầng có thể đã nằm trong diện tích sàn phủ bì. Kiểm với sheet sàn: hoặc sàn đã trừ ô thang bao gồm chiếu tới, hoặc chiếu tới nằm trong sàn và không tính lại ở đây. Chọn một cách và ghi rõ.

**Bậc tam giác dễ bị bỏ quên hoặc tính hai lần.** Nếu bản thang đã lấy chiều dày tính từ mặt bậc thì bậc đã nằm trong đó. Nếu bản thang lấy chiều dày bản nghiêng thì bậc phải tính riêng. Đọc mặt cắt để biết đang ở trường hợp nào.

## 5. Ván khuôn cầu thang

- Đáy bản thang: dài triển khai × rộng vế; đáy chiếu nghỉ: dài × rộng.
- Cổ bậc (bậc BTCT): số bậc × cao bậc × rộng vế.
- Thành bản thang biên (phía không áp tường): dài triển khai × (dày bản + phần bậc).
- Dầm thang: cách đo như dầm thường (`boc-dam` mục 5), ghi vào công tác ván khuôn **cầu thang**.
- Bậc xây gạch: không có ván khuôn.

## 6. Phép kiểm bắt buộc

```
Số bậc × Cao bậc = Chiều cao tầng
```

Lệch thì hoặc đọc sai số bậc, hoặc sai cao độ tầng, hoặc thang có chiếu nghỉ lệch cốt. Phải truy ra nguyên nhân, không làm tròn cho khớp.

Kiểm thêm: bề rộng vế thang trên mặt bằng khớp với ô thang đã trừ ở sheet sàn.

## 7. Ghi sổ khối lượng

Sheet `6.2-09CauThang`. Công tác: bê tông cầu thang (gồm dầm thang) · ván khuôn cầu thang (gồm dầm thang) · cốt thép cầu thang (trỏ `TK-Thep-TH`, bộ phận "Cầu thang" — thép dầm thang ghi vào bộ phận này) · xây bậc gạch (nếu có).

- Chia nhóm `HM` theo **cầu thang và tầng**: `Thang bộ chính — trệt → lầu 1`.
- Dòng chi tiết ghi đủ **bộ phận**: `Bản thang vế 1`, `Chiếu nghỉ CN1`, `Bậc tam giác vế 1 (13 bậc)`.
- Cột Cao với bản thang và chiếu nghỉ là **chiều dày**.
- **Số bậc, rộng bậc, cao bậc, chiều dài triển khai và cách quy đổi** ghi trong Diễn giải — đây là dữ liệu để kiểm chéo.
- Bậc tam giác: Dài = rộng bậc, Rộng = cao bậc, Cao = rộng vế, KL một bộ phận = công thức `/2` (ghi `kl1="=0.27*0.17/2*1.1"` hoặc dùng số bộ phận = số bậc × 0,5) — diễn giải nói rõ.

## 8. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã kiểm kê **đủ số cầu thang** trong công trình, kể cả thang phụ, thang lên tum, thang ngoài trời.
- [ ] Mỗi cầu thang tách đủ bộ phận, không gộp một dòng.
- [ ] Chiều dài bản thang là **chiều dài triển khai**; nếu quy đổi thì đã ghi cách quy đổi.
- [ ] **`Số bậc × Cao bậc = Chiều cao tầng`** — lệch đã truy ra nguyên nhân.
- [ ] Bậc tam giác: đã xác định bản thang lấy chiều dày nào, **không tính hai lần**.
- [ ] **Chiếu tới không trùng với sàn** — đã chốt quy ước với sheet sàn.
- [ ] Bề rộng vế khớp ô thang đã trừ ở sheet sàn.
- [ ] Dầm thang lấy H − dày bản theo thứ tự gán phần giao, nằm trong **công tác cầu thang** (không ở sheet dầm).
- [ ] Bậc xây gạch là công tác xây riêng.
- [ ] Có đủ công tác bê tông · ván khuôn · cốt thép.
- [ ] Móng và dầm móng cầu thang (nếu có) đã báo sang `boc-mong` và `boc-dam-mong`.
- [ ] Đá lát bậc, lan can, tay vịn, trát **không** nằm trong sheet này.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
