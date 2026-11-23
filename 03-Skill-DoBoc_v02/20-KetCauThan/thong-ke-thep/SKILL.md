---
name: thong-ke-thep
description: Thống kê cốt thép BÊ TÔNG CỐT THÉP để lấy số cho dự toán — đọc bảng thống kê thép có sẵn trong hồ sơ ra kilogam và tấn chính xác theo bộ phận và nhóm đường kính, bổ sung thép nối chồng, con kê theo PL VI TT 13/2021, hoặc tạm tính theo hàm lượng kg trên mét khối khi hồ sơ không có số liệu. Dùng skill này khi người dùng nói thống kê thép, bóc thép, cốt thép, hàm lượng thép, bao nhiêu tấn thép, kg trên mét khối, đọc bảng thống kê thép, trích bảng thép từ file CAD, hoặc kiểm lại khối lượng thép. Kèm kỹ thuật trích bảng thống kê thép từ block trong file DXF. Ghi vào sheet TK-Thep, tổng hợp ở TK-Thep-TH, rồi trỏ sang công tác cốt thép trong từng sheet 6.2. Không dùng cho thép hình, khung kèo thép, nhà tiền chế — thứ đó có skill riêng.
---

# Thống kê thép bê tông cốt thép

**Đọc `do-boc-loi` trước.**

## 1. Đầu ra là tấn thép theo BỘ PHẬN × NHÓM ĐƯỜNG KÍNH

PL VI TT 13/2021 (mục Cốt thép): phân theo loại thép (thường / dự ứng lực, trơn / vằn), mác, nhóm, **đường kính**, **bộ phận** (móng, cột, dầm…); trọng lượng theo **đường kính danh nghĩa**; **tính cả** nối chồng, nối ren, ống nối, miếng đệm, con kê, bu lông liên kết, thép biện pháp (chân chống giữa hai lớp).

Dòng chảy dữ liệu trong sổ khối lượng:

```
TK-Thep (mỗi số hiệu thanh một dòng)
   → TK-Thep-TH (bộ phận × nhóm Ø, công thức SUMIFS)
      → dòng công tác cốt thép trong sheet 6.2 của bộ phận đó (kl1 = cong_thuc_thep(bộ phận, nhóm))
```

*Bộ gốc nhập thép vào phần mềm dtPro bằng hàm lượng kg/m³ × thể tích. Bản này lấy thép thực theo đường kính; hàm lượng chỉ còn để kiểm chéo và tạm tính có đánh dấu.*

## 2. Bộ phận và nhóm đường kính

Bộ phận có sẵn trong `TK-Thep` (danh sách chọn): Cọc khoan nhồi · Móng, đài · Cổ cột · Giằng móng, dầm móng · Cột · Vách · Dầm · Sàn · Cầu thang · Lanh tô, ô văng · Bể, hố ga · Khác.

- **Cổ cột** ghi bộ phận riêng để truy nguồn, nhưng **áp định mức cột** (anh Thành chốt 09/10/2026): công tác cốt thép cột lấy tổng hai bộ phận "Cột" và "Cổ cột" theo từng nhóm Ø (`kl1` là tổng hai công thức `cong_thuc_thep`).
- **Nhóm đường kính**: ranh **10 mm và 18 mm** — Ø ≤ 10 · 10 < Ø ≤ 18 · Ø > 18 (anh Thành chốt 09/10/2026). Ô C9, D9 trong `TK-Thep-TH` chỉ sửa khi dự án quy định khác.
- Thép trơn và thép vằn khác mác thì tách bộ phận con hoặc ghi ở cột Ghi chú để tách khi áp giá.

## 3. Ba nguồn để lấy số thực, theo thứ tự ưu tiên

### 3.1. Block bảng thống kê trong DXF — nhanh và chuẩn nhất

Đơn vị thiết kế Việt Nam dùng tool thống kê thép: mỗi thanh là một INSERT block `TK_2`, `TK_3`, `TK_6`, `TK_9`, `TK_14`… có ATTRIB chứa stt, kích thước móc, đường kính, chiều dài một thanh, số lượng mỗi cấu kiện, tổng số lượng, tổng mét dài, kg.

Cuối mỗi cấu kiện có block **`CTK_THKL`** hoặc `CTK_THKL2` với attrib dạng `%%c18: 66.8` — nghĩa là **tổng kg theo đường kính, đã nhân số lượng cấu kiện**.

Cách làm: lọc INSERT tên `TK_*` và `CTK_*` → gom nhóm theo cột x → cắt nhóm tại mỗi `CTK` → match nhãn TEXT theo dải y (nhãn có thể **lệch cột** so với bảng) → parse `%%c<Ø>: <kg>`.

Chi tiết kỹ thuật và script ở skill `doc-ban-ve`.

### 3.2. Bảng thống kê trên PDF

Render full-res từng trang rồi đọc. Bảng thép Việt Nam trong PDF hay **xoay 90° và chữ đảo** — bóc bằng toạ độ từ, tự nhận hướng, dò scale theo header.

### 3.3. Bóc tay từ chi tiết

Đọc `6Ø18`, `đai Ø6a100-200`, `Ø10a200 hai lớp`… rồi quy ra từng thanh: chiều dài 1 thanh (gồm móc, đoạn neo theo chi tiết), số thanh. Chỉ dùng khi hai nguồn trên không có; trạng thái **S**, ghi rõ sai số có thể khoảng **±15 %**.

## 4. Ghi `TK-Thep`

Mỗi số hiệu thanh một dòng: Bộ phận · Cấu kiện (tên, tầng, trục) · Số hiệu thanh · Ø · Dài 1 thanh · Số thanh / 1 CK · Số cấu kiện · Nguồn. Các cột tổng số thanh, tổng dài, KL đơn vị (π/4 × Ø² × 7850), tổng KL **là công thức có sẵn**.

- Bảng nguồn chỉ cho **kg theo Ø** (block `CTK_THKL`) → ghi một dòng cho mỗi Ø, **nhập thẳng kg vào cột Tổng KL** (đè công thức), ghi rõ ở cột Nguồn.
- Bảng nguồn ghi `(SL: n)` / cột `T.BỘ` là **đã nhân số cấu kiện** → Số cấu kiện = 1.
- So **tổng kg từ công thức** với **tổng kg ghi trên bảng thiết kế** từng cấu kiện; lệch > 1–2 % thì soát lại (KL đơn vị bảng thiết kế có thể làm tròn khác).

### Thép nối chồng, con kê, thép biện pháp

- Kiểm ghi chú bảng thống kê thiết kế: **đã gồm nối chồng chưa**. Chưa gồm → bổ sung dòng `Nối chồng` theo chiều dài nối và vị trí nối ghi trong **ghi chú chung KC** — trạng thái **T**, ghi cách tính `[Cần xác nhận lại]`.
- Con kê, thép chân chống (chân ghế) giữa hai lớp sàn, móng: lấy theo chi tiết nếu có; không có chi tiết → `[Chờ bổ sung]`, hỏi anh Thành có tính không và tính theo cách nào. **Không tự cộng % hao hụt** — hao hụt đã nằm trong định mức.

## 5. Khi hồ sơ không có số liệu thép — tạm tính

Thứ tự đúng: **thép thực → tính từ cấu tạo đọc được (mục 3.3) → suy hàm lượng từ cấu kiện tương tự trong chính công trình này → để trống**. Không bao giờ tự chế một con số ở giữa.

- Tạm tính bằng hàm lượng: ghi dòng công tác cốt thép với `kl1 = thể tích BT × hàm lượng ÷ 1000`, trạng thái **T**, diễn giải ghi rõ hàm lượng lấy từ đâu; nhóm đường kính `[Cần xác nhận lại]`.
- **Không dùng bảng hàm lượng mặc định của phần mềm** (bộ gốc có bảng mặc định của dtPro — đã bỏ).
- Không có căn cứ gì → dòng **N**, `[Tài liệu không đề cập]`, đưa vào `00-DanhSachCanKiem.md`.

> **Cấm điền hàm lượng theo thông lệ khi bản vẽ có đủ căn cứ để tính.**
> *260625: điền đại 90 kg/m³ cho đài trong khi tính từ `Ø14a200` thực chỉ ra 40–48 → vống gấp đôi, thép đài dư 6–7 triệu.*

## 6. Bốn bẫy khi đọc bảng thống kê

- **Bảng ghi `(SL: n)` và cột `T.BỘ` là ĐÃ NHÂN số cấu kiện** — không nhân lại lần nữa.
- **Bảng "lớp dưới / lớp trên" có thể lặp tổng cả sàn** — hai trang trông giống nhau, verify rồi chỉ lấy một.
- **Trùng tên cấu kiện giữa các khu**: `DM-1` ở móng khác `DM-1` ở mái. Trong DXF phân biệt bằng vị trí y.
- **Bảng trong DXF có thể cũ hơn PDF hoặc ngược lại** — luôn đối chiếu ngày bản vẽ trước khi tin.

## 7. Đưa vào sheet 6.2

Trong sheet 6.2 của mỗi bộ phận (móng, cột, dầm, sàn…), thêm công tác cốt thép theo nhóm đường kính, VD `Cốt thép dầm, Ø ≤ 10` (tấn), dòng chi tiết dùng:

```python
B.ghi_cong_tac(ws, "Cốt thép dầm, đường kính ≤ 10 mm", "tấn", [
    dict(vi_tri="Theo TK-Thep-TH, bộ phận Dầm", kl1=B.cong_thuc_thep("Dầm", 1),
         dien_giai="Tổng thép dầm Ø ≤ 10 từ bảng TK KC-08..KC-12", tt="C")])
```

Nhóm không có thép (= 0) thì không tạo công tác.

## 8. Không thuộc skill này

**Thép hình, khung kèo thép, nhà tiền chế** → `boc-thep-hinh`. Đó là hệ tính hoàn toàn khác: theo kg từng loại tiết diện. Công trình vừa có BTCT vừa có khung thép thì **hai hệ tính song song**, không cộng vào nhau.

## 9. Kiểm chéo

- Ô "Lệch" cuối `TK-Thep-TH` phải = 0 (không có dòng nào thiếu bộ phận).
- Hàm lượng suy ngược (kg thép ÷ m³ bê tông của bộ phận) đối chiếu ngưỡng ở `do-boc-loi` mục 8: thép **90–130 kg/m³ bê tông** và **10–12 kg/m² sàn** (tạm dùng số nhà phố TP.HCM). Ra ngoài dải phải truy đến bộ phận cụ thể.
- **Nằm trong dải không chứng minh là đúng** — hai nhóm sai ngược chiều nhau vẫn cho tổng đẹp.
- Thép đài tính ra thấp bất thường (dưới 60 kg/m³) thường là **đúng** — đài là cấu kiện khối lớn, hàm lượng thấp là bình thường.
- Tổng thép theo đường kính phải khớp tổng theo cấu kiện.

## 10. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã xác định hồ sơ **có bảng thống kê hay không**, đầy đủ hay chỉ một phần.
- [ ] Có bảng thì đã dùng **số thực**; phần thiếu bảng đã tính từ cấu tạo hoặc ghi rõ **T** kèm căn cứ.
- [ ] Mỗi dòng `TK-Thep` có **bộ phận** và **Ø**; ô "Lệch" ở `TK-Thep-TH` = 0.
- [ ] Nhóm đường kính đúng ranh 10 / 18 mm (hoặc theo dự án nếu có quy định khác).
- [ ] Bảng `(SL: n)` và cột `T.BỘ` **không bị nhân lại**; bảng lớp trên và lớp dưới **không cộng trùng**.
- [ ] Mark trùng tên giữa các khu đã phân biệt.
- [ ] Đã xử lý **nối chồng, con kê, thép biện pháp** theo PL VI (có trong bảng, đã bổ sung, hoặc đã hỏi).
- [ ] **Không có hàm lượng bịa**; không dùng bảng hàm lượng mặc định của phần mềm.
- [ ] Mọi bộ phận có thép đều có công tác cốt thép trong sheet 6.2 tương ứng, trỏ công thức sang `TK-Thep-TH`.
- [ ] Thép hình (nếu có) đã chuyển sang `boc-thep-hinh`.
- [ ] Đã kiểm ngưỡng kg/m³ và kg/m² sàn; ra ngoài dải đã truy đến bộ phận.
