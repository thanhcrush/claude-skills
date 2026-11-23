---
name: boc-tuong-cua-lanh-to
description: Bóc tường xây, cửa và lanh tô — tường 100, 200, 300, tường ngăn, tường bao, tường thu hồi, tường rào, lồng thang máy xây gạch, trụ xây, cửa đi, cửa sổ, vách kính, cổng, và lanh tô trên các ô mở. Dùng skill này khi người dùng nói bóc tường, khối lượng tường, xây tường, tường xây, bóc cửa, thống kê cửa, trừ cửa, lanh tô, hoặc kiểm lại khối lượng tường. Đây là hạng mục rủi ro bỏ sót và gán nhầm cao nhất, có quy trình bảy bước đã kiểm chứng trên hồ sơ thật; áp quy tắc trừ lỗ và trừ cấu kiện BTCT trong tường theo PL VI TT 13/2021. Ghi vào sheet 6.2-11Tuong và bảng thống kê cửa TK-Cua.
---

# Bóc tường, cửa và lanh tô

**Đọc `do-boc-loi` trước**, đặc biệt bảng quy ước cặp ở mục 5.

Tường là hạng mục **rủi ro bỏ sót và gán nhầm cao nhất**. Quy trình dưới đây mô phỏng thao tác của kỹ sư làm tay và đã kiểm chứng ở 2625.

## 1. Bốn quy ước cốt lõi

> **Tường mẹ lấy CẢ MẶT PHẲNG qua ô cửa, rồi mới trừ.**
> **Cửa là dòng trừ (số bộ phận âm) đặt ngay dưới đúng tường mẹ.**
> **Trừ cả thể tích lanh tô, giằng tường, bổ trụ, ô văng BTCT nằm trong tường.**
> **Chỉ nhập chiều cao SAU KHI mặt bằng đã phủ kín.**

Mặt bằng cắt ở cao 1,2 m nên chỉ thấy phần đặc. Đo phần đặc là **mất dải tường phía trên ô cửa**.

> *2625: bức tường có ô mở 4,70 m — đo phần đặc ra **0,45 m**, đo cả mặt phẳng rồi trừ ra **5,30 m²**. Sai hẳn một bậc.*
> `5,20 × 3,55 − 4,70 × 2,80 = 5,30 m²`

Quy tắc PL VI TT 13/2021 (mục Xây) áp kèm:

- Phân theo **vật liệu, mác vữa, chiều dày, chiều cao, bộ phận** — tách công tác theo đúng các tiêu chí này (nhóm chiều cao theo cách định mức chia).
- Chiều dày tường **không gồm lớp trát**; tường vát lấy chiều dày trung bình.
- Lỗ, khoảng trống **< 0,25 m² không trừ**.
- Tường độc lập có **dài ≤ 4 lần dày** → tính là **xây cột, trụ**.
- Trụ liền tường, cùng vật liệu, xây cùng lúc → **tính vào tường**.
- Tính cả phần nhô ra.

## 2. Ghép cặp đường trong DXF KHÔNG đủ tin cho tường

Đây là khác biệt lớn so với dầm và ô sàn.

Bản vẽ kiến trúc vẽ tường **không nhất quán**: hai mép của cùng một bức có thể nằm ở hai layer khác nhau (`A-TUONG 0.5` và `A-NETMANH 0.1`); có chỗ **ba đường song song sát nhau** cách 50–150 mm; bề rộng giữa các đường dọc liên tiếp là 50 / 100 / 150 / 200 / 500 **không theo quy luật**.

> *2625: ghép cặp cho ra **0,51 m** cho một bức tường dài **7 m**.*

DXF chỉ dùng để **lấy toạ độ và rà soát**. Danh sách tường phải đọc từ mặt bằng.

## 3. Phân biệt tường xây với thứ khác — làm TRƯỚC khi đo

| Dấu hiệu | Nghiêng về |
|---|---|
| Cặp nét trên layer tường, cách 100 / 200 / 300 | tường xây |
| Cặp nét **hẹp bất thường** trên layer nét mảnh (2625: 40–50) | khung nhôm, vách kính |
| Ô vuông đúng tiết diện cột tại giao trục | cột — loại khỏi chiều dài tường |
| Cặp nét trên layer lan can | lan can, rào |

**Không kết luận chỉ từ một bề rộng.** Bề rộng nét kính khác nhau theo đơn vị thiết kế. Phải xác nhận thêm bằng ít nhất một trong: layer · ký hiệu trên mặt bằng · **bảng cửa** · mặt đứng · tờ chi tiết.

**Dấu hiệu phải nghi ngay:** mặt tiền mà ra "tường 100 dài 3,1 m" — nhiều khả năng là dải kính bị đọc thành tường.

**Thang máy: xác nhận vách BTCT hay tường xây** trước khi tính. Cả hai đều gặp. Nếu là vách BTCT thì thuộc `boc-cot-vach`.

## 4. Quy trình bảy bước

### Bước 0 — Dựng hệ toạ độ
Bung block, lấy layer trục tìm lưới của **từng** mặt bằng, gốc = giao trục 1 × trục A.
⚠ **Nhãn trục trong DXF có thể lệch tim cột 125–150 mm** — không dùng nhãn trục làm mốc đo, đo trực tiếp hình học.

### Bước 1 — Phân biệt tường với kính (mục 3)

### Bước 2 — Quét trục có thứ tự
Trục **SỐ trước** (1→2→3) → **trục phụ** (3a, 3b…) → **trục CHỮ** (A→B→C). Từng tầng, một hướng đọc cố định, **không nhảy qua lại**.

**Mã tường phải duy nhất và có điểm đầu–cuối**: `T1-C(2-3)-200` nghĩa là tầng 1, trục C, nhịp 2-3, dày 200. Chỉ ghi "trục C" là chưa đủ — tại giao trục sẽ gán nhầm đoạn và nhầm cửa. Tường gần hoặc song song trục nhưng không trùng trục đặt mã phụ `1a`, `1b`, `Aa`.

Chiều dài = **mép cột → mép cột** (hoặc mép vách, mép tường vuông góc theo quy ước góc đã chốt), lấy từ toạ độ cột thật trên layer cột. Không lấy "nhịp trục trừ ước lượng" — *2625: hai nhịp khác nhau ra cùng số 5,300 vì trừ theo số giả định*.

**Giao hai tường cùng dày**: phần giao chỉ tính **một lần** — chốt quy ước (tường trục số chạy suốt, tường trục chữ dừng ở mép, hoặc ngược lại) và ghi ở `GhiChu.md`.

Gom dòng **chỉ khi cùng**: tầng + tuyến + bề dày + chiều cao + trạng thái. Tách dòng khi đổi bề dày, **đổi dầm phía trên**, đổi cao độ, hình học phức tạp, hoặc khác trạng thái.

Nhịp có rất ít tường đặc và ít kính so với thông thuỷ → **đưa vào diện rà lại**. Chỉ ghi **NHỊP TRỐNG** sau khi đã soi mặt bằng và nêu được lý do (không gian mở, ô thông tầng, giếng trời). Không bịa ra tường, cũng không im lặng bỏ qua.

### Bước 3 — Đo cả ô mở rồi trừ (mục 1)

### Bước 4 — Gán cửa vào ĐÚNG tường mẹ

- **Rộng** ô mở: lấy từ số ghi hoặc bảng cửa, **và** kiểm lại bằng hình học CAD.
- **Cao** ô mở: lấy từ bảng cửa, mặt đứng hoặc tờ chi tiết. **Không đo cao từ mặt bằng.**
- Hai nguồn lệch nhau: **giữ cả hai**, xét tỷ lệ và quy cách (bề dày khung nhôm, lớp trát, bổ trụ) rồi để **S** hoặc **T**. Không dùng một dung sai cố định cho mọi hồ sơ — *ở 2625 lệch ≤ 120 mm là bề dày khung nhôm, hồ sơ khác có thể khác*.
- **Chỉ trừ khi ký hiệu cửa nằm trên chính tường mẹ.** **Cấm gán cửa theo khoảng cách gần nhất.**
- **Rà riêng tại giao trục** để không kéo cửa của tuyến vuông góc sang tuyến đang bóc.
- Cửa chưa xác định được tường mẹ → **để N, không trừ**.
- **Tổng bề rộng cửa trên một tuyến không được vượt chiều dài tường mẹ.**
- Kích thước trừ là **kích thước lỗ mở trong tường** (thông thủy lỗ), không phải kích thước cánh.

> Khớp rộng đo được với bảng cửa là phép kiểm chéo rất mạnh: ở 2625, 17 ô mở khớp bảng đúng từng mm, nhờ đó **phát hiện hai bản bóc cũ gán ngược hướng nhà**.

### Bước 5 — Rà soát thay bút dạ
Mỗi đoạn nét chỉ dùng **một lần**; cuối cùng **in ra phần chưa dùng**. Ba loại phải liệt kê: nhịp trống kèm lý do · đoạn nét ngoài phạm vi nhà · **đoạn trùng giữa hai cách gom** (ví dụ vách lồng thang máy vừa nằm trên trục 3 → dễ đếm hai lần).

Không có bảng này thì không chứng minh được là không sót.

### Bước 6 — Nhập chiều cao sau cùng

| Loại | Cao |
|---|---|
| Tường dưới dầm | cao tầng − chiều cao **của đúng dầm phía trên tuyến đó** (H dầm đủ, vì mặt dưới dầm là đỉnh tường) |
| Vách ngăn trong ô sàn | cao tầng − dày sàn |
| Lan can xây | theo kích thước trên mặt cắt (hay gặp 1100) |
| Tường rào | theo **từng mô-đun / mặt đứng rào**, không áp một chiều cao chung |
| Tường thu hồi | theo mặt đứng / mặt cắt mái, hình tam giác hoặc thang |

**Không áp một chiều cao cho cả tầng khi dầm phía trên thay đổi.** Một tuyến đi dưới nhiều dầm khác nhau thì **tách dòng**, không lấy bình quân. Nếu khách muốn đơn giản hoá (lấy xấp xỉ, hoặc trừ dầm trung bình) thì được, nhưng **phải nói rõ quy ước** và ghi T.

**Tường chữ L/U và lồng thang máy**: tách **từng vách**, hoặc tính theo đường tim **có kiểm góc**. Không lấy tổng kích thước lòng rồi trừ cửa — cách đó **thiếu thể tích ở góc**. Lồng thang máy cộng đủ 4 vách, mỗi vách một dòng, rồi trừ cửa thang máy (đo khoảng hở trên mặt bằng, hay gặp 800×2400).

### Bước 7 — Kiểm chéo

- **Hai phép kiểm tổng độc lập**: `tầng → bề dày → khối lượng` và `bề dày → tầng → khối lượng`. Hai số phải bằng nhau.
- **Mỗi ô mở phải nhỏ hơn bức tường mẹ.** Ô mở rộng hơn tường = gán sai vị trí. *2625: cửa 5,60 trừ lên tường 5,425 → khối lượng âm.*
- Số dòng trừ cửa khớp số cửa trong `TK-Cua` (trừ cửa nằm trong vách BTCT, vách kính).
- Suất tường xem `do-boc-loi` mục 8. Ra ngoài dải phải truy đến tuyến cụ thể.

## 5. Cửa — thống kê theo loại và vật liệu

Ghi **bảng thống kê cửa** `TK-Cua` (sheet có sẵn trong sổ): ký hiệu cửa (giữ mark bản vẽ D1, S2…) · loại (cửa đi / cửa sổ / vách kính / cổng) · vật liệu khung, cánh · B × H · số lượng · vị trí (tầng – trục – nhịp) · nguồn.

**Cửa mua trọn bộ** (anh Thành chốt 09/10/2026): một công tác cho mỗi loại cửa cùng vật liệu, quy cách — giá đã gồm khung, cánh, kính, phụ kiện và lắp đặt. **Không** tách sản xuất / lắp dựng / phụ kiện.

| Công tác | Đơn vị |
|---|---|
| Cung cấp và lắp đặt trọn bộ cửa theo loại, vật liệu, quy cách (VD `Cửa đi nhôm hệ … kính cường lực 8 mm, trọn bộ`) | **m²** (B × H lỗ cửa); dùng **bộ** khi báo giá tính theo bộ |
| Cổng tường rào trọn bộ | m² hoặc bộ theo báo giá |

- Dòng chi tiết lấy từ `TK-Cua`: số bộ phận = số lượng, Dài = B, Rộng = H (hoặc `kl1=1` nếu tính theo bộ).
- Phạm vi trọn bộ khác báo giá (VD báo giá chưa gồm khóa) → ghi rõ ở Ghi chú, thêm dòng phụ kiện riêng chỉ khi báo giá tách.

*Bộ gốc gán cửa về 10 mã cố định theo vị trí của dtPro (cửa đi chính, cửa sổ lầu…) — đã bỏ; giờ phân theo loại và vật liệu thật.*

## 6. Lanh tô

Bóc **sau khi** danh sách cửa đã gán đúng tường mẹ — lanh tô phụ thuộc danh sách ô mở, sai danh sách cửa là sai lanh tô.

Mỗi loại lanh tô (cùng tiết diện, cùng loại cửa) một dòng chi tiết:

```
Dài tính toán = Rộng lỗ mở + Gối trái + Gối phải
```

- **Gối** mỗi bên hay gặp 200–250 mm, nhưng **phải đọc từ chi tiết**, không mặc định. Không có chi tiết thì để **T** và đưa vào cần kiểm.
- **Rà trùng với dầm**: ô mở nằm ngay dưới dầm thì **không có lanh tô riêng**. Ô mở trong vách BTCT cũng không có.
- Phân biệt ba loại, công tác khác nhau: **đổ tại chỗ** · **cấu kiện đúc sẵn** (sản xuất + lắp đặt) · **gạch cốt thép**.
- **Mác bê tông lanh tô thường thấp hơn kết cấu chính** — *2625: kết cấu M300, lanh tô M200* → tách công tác.
- Công tác đi kèm: **ván khuôn lanh tô** (đáy + hai thành) · **cốt thép lanh tô** (`TK-Thep`, bộ phận "Lanh tô, ô văng").
- Thể tích lanh tô (và ô văng liền lanh tô) **trừ khỏi tường** bằng dòng trừ ngay dưới tường mẹ.

## 7. Ghi sổ khối lượng

Sheet `6.2-11Tuong`:

- Công tác xây **tách theo** vật liệu gạch · chiều dày · mác vữa · nhóm chiều cao · bộ phận (tường, trụ, tường rào, tường thu hồi). VD `Xây tường gạch đặc 6,5×10,5×22, dày ≤ 30 cm, chiều cao ≤ … m, vữa XM M75`.
- Dòng chi tiết **tường**: `Tường T1-C(2-3)-200`, Số bộ phận 1, Dài = chiều dài đã trừ cột, Rộng = bề dày, Cao = chiều cao.
- Dòng **trừ cửa** ngay dưới tường mẹ: `Trừ cửa D2 — T1-C(2-3)`, số bộ phận âm = số cửa, Dài = rộng lỗ, Rộng = bề dày tường mẹ, Cao = cao lỗ.
- Dòng **trừ lanh tô / giằng tường / bổ trụ BTCT** tương tự.
- Chia nhóm `HM` theo tầng, từ dưới lên: hầm → trệt → lửng → lầu 1, 2…
- Tường ra **m³ khối xây**.
- Sau tường: công tác lanh tô (bê tông, ván khuôn, cốt thép), rồi công tác cửa.

Mã tường, nguồn, bản tô dấu giữ ở **sổ nội bộ**; trên sổ giao, diễn giải ghi mã tường và tờ nguồn.

## 8. Gate chốt tường — chưa đạt thì chưa tính khối lượng

- [ ] Không còn tường vật lý nào chưa có mã; không có mã nào bao phủ chồng nhau.
- [ ] Đã phân biệt tường xây với kính, khung nhôm, lan can, cột, vách BTCT bằng **nhiều dấu hiệu**, không chỉ một bề rộng.
- [ ] Thang máy đã xác nhận là tường xây hay vách BTCT.
- [ ] Mã tường **duy nhất và có điểm đầu–cuối**; giao hai tường chỉ tính một lần theo quy ước đã chốt.
- [ ] Dòng tường mẹ lấy **cả mặt phẳng qua ô mở**, không đo phần đặc; chiều dày không gồm trát.
- [ ] Mỗi cửa có **đúng tường mẹ**; cửa chưa rõ đã để N và **chưa trừ**; lỗ < 0,25 m² không trừ.
- [ ] Đã rà tại **giao trục** để không kéo cửa của tuyến vuông góc sang.
- [ ] **Tổng bề rộng cửa không vượt chiều dài tường mẹ**; mỗi ô mở nhỏ hơn tường mẹ.
- [ ] Rộng ô mở đã đối chiếu bảng cửa với CAD; **cao lấy từ bảng cửa hoặc mặt đứng, không đo từ mặt bằng**.
- [ ] **Đã trừ thể tích lanh tô, giằng tường, bổ trụ BTCT** nằm trong tường.
- [ ] Tường độc lập dài ≤ 4 lần dày đã chuyển thành xây cột, trụ.
- [ ] Có **bảng rà soát phần chưa dùng**: nhịp trống kèm lý do, nét ngoài phạm vi nhà, đoạn trùng giữa hai cách gom.
- [ ] Chiều cao nhập **sau khi phủ kín**, theo đúng dầm phía trên; tuyến đi dưới nhiều dầm đã tách dòng.
- [ ] Tường L/U và lồng thang máy đã tách vách hoặc tính tim có kiểm góc.
- [ ] **Hai phép kiểm tổng khớp nhau.**
- [ ] `TK-Cua` đủ cửa; số dòng trừ cửa khớp; cửa là công tác **trọn bộ** theo loại, vật liệu, quy cách.
- [ ] Lanh tô bóc **sau** khi chốt danh sách cửa; đã rà ô mở nằm dưới dầm; có đủ bê tông · ván khuôn · cốt thép.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
