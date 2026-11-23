---
name: boc-dien-nuoc
description: Bóc khối lượng điện và cấp thoát nước trong nhà — đếm thiết bị (tủ điện, aptomat, đèn các loại, công tắc, ổ cắm, quạt, máy lạnh, bồn cầu, lavabo, vòi sen, bồn tắm, bơm, bồn nước, bình nước nóng, phễu thu) và bóc chiều dài dây điện, cáp, ống luồn, máng cáp, ống cấp nước, ống thoát nước, cùng phụ kiện ống, van. Dùng skill này khi người dùng nói bóc điện nước, bóc MEP, đếm thiết bị điện, đếm đèn, đếm ổ cắm, thiết bị vệ sinh, bóc dây điện, bóc ống nước, hoặc kiểm lại phần điện nước. Đo ống theo tim, tính cả đoạn có phụ kiện, van theo PL VI TT 13/2021. Ghi vào sheet 6.2-13Dien và 6.2-14Nuoc.
---

# Bóc điện và nước

**Đọc `do-boc-loi` trước.**

## 1. Hai việc: ĐẾM thiết bị và ĐO tuyến

*Bộ gốc chỉ đếm thiết bị vì phần mềm dtPro gộp dây, ống vào một dòng tính theo m² xây dựng và theo số phòng. Bóc theo PL VI trên Excel thì phải đo cả tuyến dây, ống.*

| Việc | Rủi ro chính |
|---|---|
| **Đếm thiết bị** | đếm text thay ký hiệu; phân loại sai loại đèn, loại ổ cắm |
| **Đo tuyến** dây, ống | quên đoạn đứng (lên xuống thiết bị, ống đứng giữa tầng); đo trùng tuyến chung |

PL VI (mục Đường ống, Lắp đặt hệ thống kỹ thuật): theo **vật tư, phụ kiện, thông số**; chiều dài ống đo theo **tim ống**, **tính cả đoạn có phụ kiện, van**, tính cả chỗ cong, gấp khúc; ống thoát **trừ đoạn nằm trong hố ga, hố thu**; ghi chiều cao, độ sâu lắp đặt.

## 2. Bốn nguồn phải đối chiếu — thiếu một là sai

1. **Chú giải ký hiệu** — biết ký hiệu nào là thiết bị gì, dây/ống loại gì.
2. **Mặt bằng điện / nước từng tầng** — vị trí, số lượng, tuyến đi.
3. **Sơ đồ nguyên lý** (điện: tủ, aptomat, tiết diện dây từng mạch; nước: sơ đồ không gian, ống đứng, đường kính) — kiểm chéo số lượng, cho số liệu đoạn đứng.
4. **Bảng thống kê thiết bị, vật tư** — nếu hồ sơ có, đây là nguồn đối chiếu mạnh nhất.

**Không đếm text chú thích thay cho ký hiệu thiết bị.** Chú thích lặp nhiều lần trên tờ — *2623: đếm số máy lạnh theo text ra sai*. Đếm ký hiệu block trong DXF, hoặc đếm tay trên ảnh render đã phóng đủ lớn.

## 3. Điện

### Thiết bị — phân loại theo chú giải

| Nhóm | Tách theo |
|---|---|
| Tủ điện, aptomat | tủ tổng, tủ tầng; aptomat theo dòng định mức, số cực (từ sơ đồ nguyên lý) |
| Đèn | **loại đèn theo chú giải**: chùm, áp trần, downlight âm trần, ốp tường, gương, cầu thang, sân vườn, đèn tuýp, đèn hắt… và công suất |
| Công tắc | đơn, đôi, ba; **công tắc 2 chiều (cầu thang) tách riêng** |
| Ổ cắm | ổ đôi, ổ đơn, ổ điện thoại, ổ tivi, ổ mạng, ổ chống nước |
| Thiết bị khác | quạt trần, quạt thông gió (WC, bếp), chuông, máy lạnh (điểm chờ hoặc cả máy — đọc phạm vi) |

**Phân loại đèn theo chú giải ký hiệu, không đoán theo tên phòng.** Đèn trong phòng ngủ chưa chắc là đèn chùm; có thể là áp trần hoặc downlight.

### Tuyến — dây, cáp, ống luồn

- **Chiều dài tuyến ngang**: đo polyline trên mặt bằng theo layer mạch (DXF, xem `doc-ban-ve`), hoặc đo tỷ lệ đã hiệu chuẩn trên PDF. Mặt bằng không vẽ tuyến (chỉ có ký hiệu) → **không tự vạch tuyến**, ghi N hoặc hỏi quy ước ước tính.
- **Đoạn đứng**: mỗi điểm công tắc, ổ cắm, đèn tường cộng đoạn lên/xuống từ trần hoặc sàn đến cao độ lắp đặt — cao độ lấy từ **ghi chú chiều cao lắp đặt** trên bản vẽ. Không có ghi chú → `[Tài liệu không đề cập]`, hỏi.
- **Số sợi**: chiều dài dây = chiều dài tuyến × số sợi cùng loại (pha, trung tính, tiếp địa) đọc từ sơ đồ nguyên lý. Tách theo **tiết diện dây** (1,5 / 2,5 / 4 / 6 mm²…) và loại cáp.
- **Ống luồn, máng cáp**: theo chiều dài tuyến, tách theo đường kính / kích thước.
- **Hộp nối, hộp âm tường**: đếm theo số điểm.
- Đoạn dự phòng đấu nối đầu dây: chỉ cộng khi có quy ước của dự án `[Cần xác nhận lại]`.

## 4. Nước

### Thiết bị

| Nhóm | Gồm |
|---|---|
| Thiết bị vệ sinh | bồn cầu, lavabo, tiểu nam, vòi sen, bồn tắm, gương, bộ phụ kiện WC |
| Cấp nước | bơm, bồn nước mái, bể ngầm (phần thiết bị), bình nước nóng, năng lượng mặt trời, vòi nước, van phao |
| Thoát nước | phễu thu sàn, cầu chắn rác, ga thu |

### Tuyến — ống và phụ kiện

- **Ống cấp, ống thoát** tách theo **vật liệu** (PPR, uPVC, HDPE…) và **đường kính**.
- Chiều dài theo **tim ống**: đoạn ngang đo trên mặt bằng; **ống đứng** và đoạn lên xuống thiết bị đọc từ **sơ đồ không gian / mặt cắt** — mặt bằng không thể hiện được.
- Tính **cả đoạn có phụ kiện, van** (không trừ chiều dài phụ kiện).
- Ống thoát: **trừ đoạn nằm trong hố ga, hố thu**.
- **Phụ kiện** (cút, tê, côn, măng sông, van) đếm **cái theo đường kính** từ sơ đồ không gian; không có sơ đồ → N hoặc hỏi quy ước, không tự cộng %.
- Ống thông hơi, ống thoát nước mưa (từ mái, sê nô) đừng quên — đọc mặt bằng mái và mặt đứng.

**Ranh giới bể nước, bể phốt, hố ga:**

- phần **bê tông, ván khuôn, thép** → `boc-mong` (hoặc sheet riêng nếu nhiều), **đào, lót** → `boc-dao-dap`, **xây, trát** → `boc-tuong-cua-lanh-to` / `boc-hoan-thien`;
- **bơm, bồn, phụ kiện, ống** → skill này.

Bản vẽ chi tiết bể thường **có sẵn bảng khối lượng bê tông và thép** — dùng số đó, ghi nguồn, đừng tự tính lại.

Xác minh khu ướt trước khi đếm: xem `boc-hoan-thien` mục 8. Ô nhỏ có cửa không mặc nhiên là WC.

## 5. Ghi sổ khối lượng

Sheet `6.2-13Dien` và `6.2-14Nuoc`:

- **Công tác** theo loại thiết bị / loại vật tư + quy cách: `Lắp đặt đèn downlight âm trần 9W`, `Kéo rải dây điện Cu/PVC 2,5 mm²`, `Lắp đặt ống PPR D25`, `Lắp đặt cút PPR D25`.
- **Dòng chi tiết** theo **tầng → phòng / khu** để đối chiếu với mặt bằng: `Tầng 2 — P.Ngủ 1 (ký hiệu Đ3)`. Thiết bị: số bộ phận = số cái, KL một bộ phận = 1 (`kl1=1`).
- Dây, ống: dòng chi tiết theo **tuyến / mạch**: `Mạch C2 tầng 2: ngang 18,4 + đứng 6 điểm × 1,2`, ghi rõ đo từ layer nào, tờ nào.
- Cột Ký hiệu bản vẽ ghi số hiệu tờ; ký hiệu thiết bị trên bản vẽ ghi trong Danh mục hoặc Diễn giải để người khác dò lại.

## 6. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã đối chiếu **đủ bốn nguồn**: chú giải · mặt bằng · sơ đồ nguyên lý · bảng thiết bị.
- [ ] **Đếm ký hiệu thiết bị, không đếm text chú thích.**
- [ ] Đếm theo tầng và phòng, dò lại được trên mặt bằng.
- [ ] **Đèn đã phân đúng loại** theo chú giải, không đoán theo tên phòng; công tắc 2 chiều tách riêng; ổ cắm tách đủ loại.
- [ ] Dây đã tách theo **tiết diện**, nhân **số sợi** theo sơ đồ nguyên lý; có **đoạn đứng** theo cao độ lắp đặt.
- [ ] Ống đo **theo tim**, gồm đoạn có phụ kiện, van; có **ống đứng** từ sơ đồ không gian; ống thoát đã trừ đoạn trong hố ga.
- [ ] Phụ kiện ống đếm theo đường kính, không tự cộng %.
- [ ] Không tự vạch tuyến khi bản vẽ không có — đã để N hoặc hỏi quy ước.
- [ ] Bể nước, bể phốt, hố ga: bê tông, thép, đào đã chuyển sang skill tương ứng; chỉ thiết bị và ống ở lại đây.
- [ ] Khu ướt đã xác minh, không nhầm kho hoặc hộp kỹ thuật thành WC.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
