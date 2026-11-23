---
name: boc-coc
description: Đếm và bóc khối lượng cọc trong công trình xây dựng Việt Nam — cọc ép, cọc đóng, cọc khoan nhồi, cọc ly tâm ứng lực trước, cọc bê tông cốt thép đúc sẵn, cọc thử, cọc nén tĩnh. Dùng skill này khi người dùng nói bóc cọc, đếm cọc, công trình này có bao nhiêu cọc, số lượng cọc, chiều dài cọc, ép cọc, nối cọc, đập đầu cọc, phần cọc, hoặc khi cần đọc mặt bằng định vị tim cọc. Dùng cả khi chỉ cần kiểm lại số cọc của một bản bóc cũ. Ghi vào sheet 6.2-01Coc của sổ khối lượng theo mẫu PL VI TT 13/2021, trọng tâm là SỐ LƯỢNG cọc đếm đúng. Không dùng cho đài móng, giằng móng, cổ cột — những cái đó có skill riêng.
---

# Bóc cọc

**Đọc `do-boc-loi` trước.** Skill này không lặp lại quy tắc bất biến, C/S/T/N, hai lớp dữ liệu.

## 1. Việc thật của skill này là ĐẾM ĐÚNG

Mọi công tác cọc đều nhân từ **số lượng cọc**: chiều dài cọc, chiều dài ép/đóng, số mối nối, khối lượng đập đầu cọc. Đếm sai một cọc là sai dây chuyền cả nhóm công tác.

**Chiều dài cọc hầu như không bao giờ chốt trên bản vẽ** — ép theo độ chối, chốt ngoài công trường. Có chiều dài thiết kế thì ghi kèm nguồn, không có thì **để trống, trạng thái N**, ghi `[Tài liệu không đề cập]`, người dùng nhập sau. Tuyệt đối không tự suy, không lấy 20 m cho tiện. Đây là mục treo ở 5 trên 16 công trình của bộ gốc.

Không có chiều dài **không** làm hỏng việc bóc — số lượng cọc mới là cái phải đúng. Công tác nào phụ thuộc chiều dài thì ghi dòng N, các công tác đếm được (số cọc, đập đầu cọc) vẫn ghi số.

## 2. Nguồn và vai trò

| Nguồn | Vai trò |
|---|---|
| Mặt bằng định vị tim cọc | **nhận diện và đếm** — nguồn chính |
| Mặt bằng móng / đài | **kiểm chéo** — cộng số cọc theo từng đài |
| Chi tiết cọc, thuyết minh, ghi chú chung | quy cách, tiết diện, cao độ đầu–mũi, số đoạn, nối cọc, ngàm cọc vào đài, tải thiết kế |
| Bảng thống kê cọc nếu có | kiểm chéo thứ ba |
| Báo cáo khảo sát địa chất | cấp đất (ép, khoan theo cấp đất) |
| DXF | toạ độ tim và đếm bằng entity |
| PDF / render | hiểu ngữ nghĩa, phạm vi, phân biệt legend với cọc thật |

## 3. Đếm cọc — bắt buộc hai nguồn độc lập

Đây là chỗ đã sai nhiều nhất. **Không bao giờ tin một cách đếm.**

**Cách 1 — đếm ký hiệu tim cọc** trên mặt bằng định vị: block hoặc circle trên layer cọc.
**Cách 2 — cộng số cọc theo từng đài** từ mặt bằng móng và chi tiết đài.

```
Σ(cọc theo từng đài)  =  tổng ký hiệu tim cọc
```

Lệch nhau thì **phải truy đến vị trí cụ thể**, không chọn bừa một phía và không sửa tổng bằng tay.

Bốn tình huống thật:

- **2611: block cọc 84, số hiệu chỉ đánh C-1…C-78.** Sáu ký hiệu lệch nhưng **giống hệt cọc và có đường kích thước dóng tới** → là cọc thật, bên thiết kế sót số. Số đúng là **84**. Đếm theo số hiệu sẽ thiếu 6 cọc.
- **2625: DXF lỗi nhân bản gương.** 27 trên 69 vòng tròn ký hiệu bị đẩy sang vùng x dương ngoài bản vẽ, thêm 138 block ở vùng rác x ≈ −4,9 triệu. Đếm circle ra 42 (thiếu) hoặc 86/138 (thừa). Phải đếm ký hiệu tim rồi kiểm chéo bằng Σ(đài × cọc/đài).
- **Ký hiệu legend và ký hiệu trên mặt cắt phải loại.** Legend xếp thành hàng dọc, lệch hẳn khỏi footprint nhà.
- **Mẹo nhanh: ký hiệu `DC-n` thường có n = số cọc trong đài** → cộng nhanh ra tổng để đối chiếu (2614 khớp 151 cọc).

**KHÔNG đếm bằng vision.** Hough transform nhiễu — 2611 sai 13 đến 26 cái. Đếm bằng entity trong DXF, hoặc đếm tay trên ảnh render đã phóng đủ lớn nếu chỉ có PDF.

## 4. Phân loại cọc

| Loại | Nhận biết trên bản vẽ | Ghi chú |
|---|---|---|
| Cọc BTCT đúc sẵn | tiết diện **vuông** — 200×200, 250×250, 300×300; ép hoặc đóng | mua theo cây hoặc đúc tại công trường — **hỏi**, vì công tác khác hẳn |
| Cọc ly tâm ứng lực trước | tiết diện **tròn rỗng** — ký hiệu PHC, PC, D300 / D350 / D400 | mua theo cây, **không bóc thép** |
| Cọc khoan nhồi | tròn đặc, D600 / D800 / D1000, đổ tại chỗ | bóc như bê tông + cốt thép (PL VI); **có bóc thép** → `thong-ke-thep` |

Tách dòng khi khác bất kỳ cái nào: **loại** · **tiết diện hoặc đường kính** · **chiều dài** · **cọc thử hay đại trà** · **cấp đất** · **trên cạn hay dưới nước**.

**Cọc thử và cọc nén tĩnh**: vẫn là loại cọc của nó, nhưng **tách công tác riêng** (`Cọc thử nén tĩnh PHC D350`). Không cộng chung cọc đại trà: số lượng và đơn giá tính riêng. Cọc neo phục vụ thử tải và công tác thí nghiệm nén tĩnh cũng vậy.

**Mã hiệu cọc có thể mâu thuẫn nội bộ.** 2614: bảng ghi "PHC D350-A" nhưng đường kính đại trà trên mặt bằng ghi 400. Không tự chọn — để **N**, hỏi thiết kế hoặc chủ đầu tư.

Không suy số lượng từ chi tiết một thanh cọc. Không nhầm cọc thể hiện trong legend với cọc thiết kế.

## 5. Danh mục công tác — theo PL VI mục Cọc

| Công tác | Đơn vị | Cách tính |
|---|---|---|
| Cọc (mua hoặc sản xuất) | m | số cọc × chiều dài 1 cọc thiết kế |
| Ép / đóng cọc | m | số cọc × chiều dài vào đất. PL VI: độ sâu đo **dọc trục**, từ điểm chạm mặt đất đến mũi cọc. Đoạn ép âm (cọc dẫn) tách dòng nếu có |
| Nối cọc | mối | số cọc × (số đoạn − 1) — số đoạn đọc từ chi tiết cọc |
| Đập đầu cọc | m³ | số cọc × tiết diện × chiều dài đập (đọc chi tiết ngàm cọc vào đài) |
| Cọc thử, thí nghiệm nén tĩnh | cọc / lần | theo thuyết minh, tách riêng |
| **Khoan nhồi**: khoan tạo lỗ | m | theo đường kính, chiều sâu (đo dọc lỗ, mặt đất → đáy), cấp đất; ghi cách giữ thành (ống vách, bentonite) |
| **Khoan nhồi**: bê tông cọc | m³ | tiết diện × chiều dài thiết kế |
| **Khoan nhồi**: ống vách để lại, siêu âm, khoan lõi kiểm tra | m / ống / cọc | theo thiết kế, ghi rõ |

Tên công tác ghi đủ loại cọc, tiết diện, cấp đất (khi ép/khoan) theo cách gọi của định mức. Mã hiệu để `[Chờ bổ sung]`.

## 6. Ghi sổ khối lượng

Sheet `6.2-01Coc` của sổ `<TenDuAn>_BangKL_v01.xlsx` (tạo bằng `bangkl.py`, xem `do-boc-loi` mục 6).

- Mỗi công tác một dòng `CT`; dưới đó dòng chi tiết **theo nhóm đài hoặc theo loại cọc**, VD `Cọc trong đài DC-4 (6 đài × 4 cọc)` — số bộ phận = 24.
- Số cọc là **số bộ phận giống nhau**; chiều dài 1 cọc ở cột Dài. Chiều dài chưa có → dòng **N**, không số.
- **Diễn giải** ghi: đếm được bao nhiêu bằng cách nào, kiểm chéo ra bao nhiêu, lấy từ tờ nào. VD: `Đếm tim cọc MB định vị KC-02 = 84; Σ(cọc/đài) từ CT đài = 84 → khớp`.
- Ghi số cọc mỗi đài vào sổ nội bộ để `boc-mong` kiểm chéo và để tính đập đầu cọc.

## 7. Những thứ KHÔNG thuộc skill này

- Đài móng → `boc-mong`. Đào đất, bê tông lót đài → `boc-dao-dap`.
- Cổ cột từ mặt trên đài → `boc-co-cot-vach-pit`.
- **Thép cọc**: cọc ly tâm và cọc mua sẵn **không bóc thép**. Cọc khoan nhồi, cọc đúc tại công trường → `thong-ke-thep`, bộ phận "Cọc khoan nhồi".
- Phần đầu cọc ngàm vào đài: **không trừ** khỏi bê tông đài trừ khi thể tích ≥ 0,1 m³ theo PL VI — xem `boc-mong`.

## 8. Gate chốt — chưa đạt thì chưa giao

- [ ] Đã đếm bằng **hai cách độc lập** và hai số khớp nhau; lệch thì đã truy ra vị trí và nguyên nhân.
- [ ] Đã loại ký hiệu legend, ký hiệu trên mặt cắt, và vùng rác ngoài phạm vi bản vẽ.
- [ ] Đã rà cọc biên, cọc lệch tâm, cọc ngoài đài, cọc không có mark.
- [ ] Cọc thử, thí nghiệm nén tĩnh tách riêng, không cộng vào đại trà.
- [ ] Mỗi loại, tiết diện, chiều dài, cấp đất một dòng.
- [ ] Chiều dài: có nguồn thì ghi kèm nguồn; không có thì **dòng N** và có một mục trong `00-DanhSachCanKiem.md` — không điền số ước.
- [ ] Đã có đủ công tác: cọc · ép/đóng (hoặc khoan) · nối cọc · đập đầu cọc · (thí nghiệm).
- [ ] Mã hiệu cọc mâu thuẫn giữa bảng và mặt bằng đã hỏi hoặc để N.
- [ ] Số cọc theo đài đã chuyển sang `boc-mong` để kiểm chéo.
