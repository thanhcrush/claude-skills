---
name: boc-dam
description: Bóc dầm bê tông cốt thép phía trên móng, theo từng tầng — dầm chính, dầm phụ, dầm biên, dầm bo, dầm console, dầm chìm, dầm mái, dầm đỡ thang — kèm dòng nút giao cột–dầm. Dùng skill này khi người dùng nói bóc dầm, khối lượng dầm, bê tông dầm, ván khuôn dầm, dầm sàn, mặt bằng dầm sàn, hoặc kiểm lại khối lượng dầm. Quy ước cốt lõi theo PL VI TT 13/2021: dầm tính thông thủy mép cột → mép cột, chiều cao tính bằng H dầm trừ dày sàn vì phần trong sàn thuộc sàn, nút giao cột–dầm ghi một dòng riêng trong công tác bê tông dầm — đi cặp với cột tính đến đáy dầm và sàn phủ bì. Ghi vào sheet 6.2-07Dam. Không dùng cho dầm móng, giằng móng, đà kiềng và lanh tô, những thứ đó có skill riêng.
---

# Bóc dầm

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp và thứ tự gán phần giao ở mục 5. Dầm dính vào **hai cặp** cùng lúc.

## 1. Hai cặp quy ước — sai một vế là hỏng cả bảng

### Cặp 1 — Dầm ↔ Cột (chiều dài và nút)

> **Dầm tính thông thủy mép cột → mép cột.**
> **Mỗi cột có dầm giao ghi MỘT dòng nút** = tiết diện cột × (H dầm sâu nhất giao vào cột − dày sàn), trong công tác bê tông dầm.
> ↔ **cột tính đến đáy dầm sâu nhất** (`boc-cot-vach`).

PL VI: nút giao cột–dầm tính vào **dầm**. Lấy dầm tim–tim mà cũng ghi nút → trùng. Thông thủy mà quên nút → thiếu. Cột lấy hết cao tầng mà dầm có nút → trùng.

Nút gán vào công tác bê tông của **dầm sâu nhất** giao vào cột. Các dầm khác giao vào cùng cột chỉ tính thông thủy, **không thêm nút**.

### Cặp 2 — Dầm ↔ Sàn (chiều cao)

> **Dầm chỉ lấy phần DƯỚI sàn: cao tính = H dầm − dày sàn.**
> ↔ **sàn tính diện tích phủ bì trừ ô trống** (`boc-san-mai`) — đã gồm phần dầm nằm trong sàn.

PL VI: dầm nằm trong sàn tính vào **sàn**. Vì vậy:

- dầm 450, sàn 120 → cao tính 330;
- **không** trừ bề rộng dầm khỏi diện tích sàn (sàn đã nhận phần đó);
- dầm hai bên sàn khác chiều dày → trừ chiều dày sàn **lớn hơn** phía nào thì ghi rõ, hoặc tách hai nửa tiết diện nếu chênh đáng kể `[Cần xác nhận lại]`;
- **dầm bo, dầm biên nhô lên trên mặt sàn**: phần nhô lên **tính vào dầm** (cao tính = H − dày sàn, nếu dầm chìm một phần thì đo đúng phần nằm ngoài sàn);
- **dầm chìm** nằm trọn trong chiều dày sàn → không có khối lượng dầm riêng, chỉ ghi nhận để kiểm thép.

*Bộ gốc làm ngược ("dầm nhập đủ H") vì phần mềm dtPro tự trừ phần dầm trong sàn. Bóc theo PL VI trên Excel thì không có ai trừ hộ — giữ đủ H là tính trùng.*

## 2. Phạm vi

| Thuộc skill này | Không thuộc |
|---|---|
| Dầm từ **sàn tầng trệt trở lên**, mọi tầng kể cả mái | Dầm móng, giằng móng, đà kiềng → `boc-dam-mong` |
| Dầm chính, phụ, biên, bo, console, chìm | Lanh tô → `boc-tuong-cua-lanh-to` |
| Dầm sàn nắp hầm | Dầm thang, bản thang → `boc-cau-thang` |
| **Dòng nút cột–dầm** của mọi cột có dầm giao | Thép dầm → `thong-ke-thep` |

## 3. Nguyên tắc tổ chức — theo mark, không theo vị trí

Làm **riêng từng tầng**. Trong mỗi tầng, bóc theo **thứ tự ký hiệu tăng dần**: D1, D2… D9, D10… rồi đến các hệ ký hiệu phụ và dầm không mark.

**Hoàn thành trọn vẹn một mark rồi mới sang mark tiếp theo.** Không bóc xen kẽ nhiều mark theo vị trí — đó là cách chắc chắn nhất để vừa sót vừa trùng.

### Bước 1 — Lập danh mục mark của tầng

Rà mặt bằng, liệt kê toàn bộ mark và tiết diện ghi trực tiếp hoặc từ chi tiết. Danh mục này **điều khiển thứ tự làm việc**, nhưng không thay thế việc kiểm kê từng đoạn vật lý.

### Bước 2 — Bóc từng mark

Với D1: tìm **tất cả** vị trí D1 trong tầng → ghi từng đoạn với điểm đầu–cuối, hướng, chiều dài thông thủy, tiết diện, nguồn → **tô dấu ngay đoạn vừa ghi** → kiểm đủ D1 rồi mới sang D2.

Tách đoạn khi đổi: tiết diện · cao độ · mark · hướng · quy tắc giao · trạng thái.

### Bước 3 — Rà độc lập sau khi hết mark

Đi lại theo **lưới trục, chu vi và vùng đặc biệt** để tìm những thứ không có mark:

dầm không nhãn · **dầm bo** · **dầm chìm** · **dầm console** · đoạn sau cột · dầm quanh ô cầu thang · quanh thang máy · ban công · ô văng · dầm đỡ mái che.

Mỗi đoạn phải rơi vào đúng một trong ba: *đã tính* / *loại trừ có lý do* / *N*.

> **2625 — bài học đắt:** ước chiều dài dầm theo lưới trục làm **thiếu khoảng 30 %**, vì bỏ sót công xôn và dầm phụ. Lưới trục không phải là danh sách dầm.

### Bước 4 — Ghi dòng nút

Sau khi xong mọi mark của tầng: lấy danh sách cột của tầng (từ `boc-cot-vach`), với mỗi cột có dầm giao ghi một dòng nút. **Số dòng nút = số cột có dầm giao** — kiểm khớp với file cột.

## 4. Chiều dài và tiết diện

**Chiều dài**: lấy toạ độ **mép cột thật** từ layer cột khi có DXF; không có thì tim trục trừ hai nửa cột theo phương dầm (đúng tiết diện cột tầng đó), ghi rõ trong Diễn giải và để trạng thái **S** nếu kích thước cột là suy ra. Dầm phụ gác lên dầm chính: tính đến **mép dầm chính** (phần giao thuộc dầm chính).

Ghép cặp đường song song trong DXF cho ra chiều dài **đã tự ngắt tại cột** (vì nét bị ngắt tại cột), nhưng phải xác nhận: cặp 200 mm có thể là tường, gờ hoặc ô văng chứ không phải dầm. Giới hạn phạm vi trong lưới nhà và kiểm mật độ.

**Tiết diện**: đọc từ nhãn `[BxH]` trên mặt bằng hoặc tờ chi tiết dầm, **đúng tầng và đúng đoạn**. Cùng mark nhưng khác tiết diện theo tầng hoặc theo đoạn thì **tách dòng**.

**Không gán một bộ dầm cho nhiều tầng** — mỗi tầng framing khác nhau.

**Trùng tên giữa các khu:** `DM-1` ở móng khác `DM-1` ở mái (2624). Trong DXF phân biệt bằng vị trí y; trong bảng phân biệt bằng tầng ghi trong Danh mục.

Có chi tiết `DS1…DSn` thì phải ra **từng dầm kèm trục**, không gộp một dòng — dòng gộp không giải trình được với khách.

## 5. Ván khuôn dầm

- Đáy: bề rộng × chiều dài thông thủy (dầm thân luôn treo).
- Thành: 2 × (H − dày sàn) × chiều dài thông thủy. **Dầm biên**: thành ngoài lấy **đủ H** (không có sàn che), thành trong H − dày sàn.
- Phần mặt nút lộ ra (cột rộng hơn dầm, giữa các dầm) tính vào ván khuôn dầm nếu đáng kể; quy ước bỏ qua thì ghi rõ.
- Dầm phụ gác dầm chính: trừ phần thành dầm chính bị dầm phụ che nếu ≥ 1 m² (PL VI) — thường nhỏ, không trừ.

## 6. Ghi sổ khối lượng

Sheet `6.2-07Dam`. Công tác: bê tông dầm (theo mác; dầm và sàn có thể chung một công tác "bê tông xà dầm, giằng, sàn mái" tùy định mức — chọn theo cách anh Thành áp mã) · ván khuôn dầm · cốt thép dầm (trỏ `TK-Thep-TH`).

- Chia nhóm bằng dòng `HM` theo tầng; trong tầng theo mark tăng dần, cuối tầng là các dòng nút.
- Dòng chi tiết chứa **tầng, mark và tuyến**: `Dầm D1 tầng 2 trục 1(A-C)`.
- **Cột Dài = chiều dài thông thủy.** Diễn giải: `tim trục 5,4 − 2 nửa cột (0,15 + 0,15) = 5,1`.
- Rộng = b; **Cao = H − dày sàn**, diễn giải ghi `0,45 − 0,12 = 0,33`.
- Dòng nút: `Nút cột C1 tầng 2 trục A-1` — Dài × Rộng = tiết diện cột tầng đó, Cao = H dầm sâu nhất − dày sàn.

## 7. Kiểm cuối tầng

- Tất cả mark đã bóc theo thứ tự tăng dần, không mark nào bỏ dở.
- **Số đoạn trong bảng khớp bản tô dấu**; không còn đoạn chưa tô hoặc tô hai lần.
- Đã rà độc lập theo lưới trục và chu vi để bắt dầm không mark.
- **Số dòng nút = số cột có dầm giao của tầng** (đối chiếu `boc-cot-vach`).
- Kiểm tổng theo phương ngang và phương dọc riêng, so với tổng dòng.
- Mật độ dầm và suất bê tông dầm xem ngưỡng ở `do-boc-loi` mục 8 — **chú ý ngưỡng gốc tính theo quy ước dầm đủ H**, theo PL VI số m³ dầm sẽ thấp hơn; dùng ngưỡng m/m² sàn để kiểm, m³ chỉ tham khảo.

## 8. Gate chốt — chưa đạt thì chưa giao

- [ ] Bóc **riêng từng tầng**, không dòng nào gộp nhiều tầng.
- [ ] Trong mỗi tầng đã đi **hết mark theo thứ tự tăng dần**, xong mark này mới sang mark khác.
- [ ] Đã **tô dấu ngay** sau mỗi đoạn; bản tô phủ kín, không tô trùng.
- [ ] Đã **rà độc lập theo lưới trục và chu vi** sau khi hết mark — bắt được dầm không nhãn, dầm bo, dầm chìm, console, ô văng, dầm quanh thang.
- [ ] **Không ước chiều dài theo lưới trục** (2625 thiếu ~30 %).
- [ ] Chiều dài **thông thủy mép cột**, dầm phụ đến mép dầm chính.
- [ ] **Cao tính = H − dày sàn**; dầm bo, dầm biên nhô lên đã xử lý đúng phần nhô.
- [ ] Có **dòng nút** cho mọi cột có dầm giao, mỗi cột một nút, gán theo dầm sâu nhất; file cột tính đến đáy dầm.
- [ ] File sàn tính **phủ bì**, không trừ bề rộng dầm.
- [ ] Tiết diện đọc đúng tầng, đúng đoạn; cùng mark khác tiết diện đã tách dòng.
- [ ] Có chi tiết từng mã thì ra **từng dầm kèm trục**, không gộp.
- [ ] Đã phân biệt mark trùng tên giữa các khu (dầm móng và dầm mái cùng ký hiệu).
- [ ] Có đủ công tác bê tông · ván khuôn · cốt thép; ván khuôn dầm biên lấy đủ H ở thành ngoài.
- [ ] Tổng theo phương ngang + dọc khớp tổng dòng.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
