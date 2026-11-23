---
name: boc-cai-tao
description: Bóc khối lượng công trình cải tạo, sửa chữa, nâng tầng — bảo vệ hiện trạng, tháo dỡ, phá tường, đục nền, cắt sàn, chống đỡ tạm, vận chuyển phế thải, khoan cấy thép hoá chất, gia cố dầm cột, kết nối kết cấu cũ với mới, hoàn trả và vệ sinh bàn giao. Dùng skill này khi người dùng nói cải tạo, sửa chữa, nâng tầng, thêm tầng, đập phá, tháo dỡ, gia cố, nhà cũ, hoặc đưa hồ sơ cải tạo. Cấu kiện xây mới vẫn bóc bằng skill cấu kiện tương ứng — skill này chỉ lo phần đặc thù của cải tạo, theo chuỗi tám mắt xích và quy tắc phá dỡ của PL VI TT 13/2021. Ghi vào sheet CaiTao-Chuoi (bảng chống sót) và 6.2-15CaiTao.
---

# Bóc cải tạo và sửa chữa

**Đọc `do-boc-loi` trước.**

## 1. Cải tạo khác nhà mới ở đâu

Nhà mới bóc theo **cấu kiện**. Cải tạo bóc theo **chuỗi công việc** — vì giá trị nằm ở trình tự, không ở khối lượng.

```
bảo vệ hiện trạng → tháo dỡ → vận chuyển phế thải → gia cố / kết nối
→ thi công mới → điện nước → hoàn trả → vệ sinh bàn giao
```

**Thiếu một mắt xích là thiếu tiền.** Tháo mà quên hoàn trả, tháo mà quên vận chuyển phế thải, cắt sàn mà quên gia cố — đều là những chỗ khách phát hiện sau khi đã ký giá.

PL VI TT 13/2021 (mục Phá dỡ): phân theo **cấu kiện, vật liệu, biện pháp**; **chống đỡ, vận chuyển phế thải tính riêng**; ghi **tỷ lệ vật liệu tận dụng** nếu có.

## 2. Phạm vi — cấu kiện mới KHÔNG thuộc skill này

| Thuộc skill này | Thuộc skill khác |
|---|---|
| Bảo vệ, che chắn, chống đỡ tạm | Cột, dầm, sàn, tường **xây mới** → skill cấu kiện tương ứng |
| Tháo dỡ, phá, đục, cắt | Móng mới, cọc ép bổ sung → `boc-mong`, `boc-coc` |
| Vận chuyển phế thải | Hoàn thiện phần xây mới → `boc-hoan-thien` |
| **Khoan cấy thép, gia cố, kết nối cũ–mới** | Điện nước mới → `boc-dien-nuoc` |
| Hoàn trả phần bị ảnh hưởng | |
| Vệ sinh bàn giao | |

Nâng tầng thì cột dầm sàn tầng mới bóc y như nhà mới, ghi vào sheet cấu kiện của nó. Skill này chỉ thêm phần **kết nối với nhà cũ** và **ảnh hưởng lên nhà hiện hữu**.

## 3. Bốn nhóm hiện trạng — phân trước khi bóc

Với **từng khu vực**, mỗi phần phải rơi vào đúng một nhóm:

| Nhóm | Nghĩa |
|---|---|
| **GIỮ LẠI** | không động tới — nhưng vẫn có thể cần bảo vệ, che chắn |
| **THÁO DỠ** | phá bỏ — kéo theo vận chuyển phế thải và hoàn trả |
| **XÂY MỚI** | thi công mới — bóc ở skill cấu kiện, nhưng cần kết nối |
| **TẠM TÍNH** | chưa rõ, để **T**, đưa vào danh sách cần kiểm |

Không có nhóm thứ năm. Phần nào chưa phân được thì là **TẠM TÍNH**, không bỏ trống.

## 4. Đầu việc đặc thù hay bị quên

- **Khoan cấy thép hoá chất** — nối thép mới vào kết cấu cũ. Tính theo **số lỗ** hoặc **mét dài neo**, kèm đường kính và chiều sâu khoan.
- **Gia cố dầm, cột** — bọc bê tông, dán sợi carbon, ốp thép hình.
- **Cắt sàn mở ô thang, ô thang máy** — tính theo **mét dài đường cắt** và **m³ (hoặc m²) sàn phá bỏ**.
- **Đục nền cũ**, bóc lớp hoàn thiện cũ, cạo sơn cũ.
- **Phá tường** — phân biệt tường gạch với tường bê tông, phá thủ công hay máy; công tác khác hẳn.
- **Chống đỡ tạm** trong lúc tháo dỡ.
- **Che chắn nhà lân cận**, bạt phủ, giàn giáo bao che.
- **Vận chuyển phế thải** — khối lượng phá dỡ quy đổi theo hệ số của định mức `[Cần xác nhận lại]`, cự ly, có cần cẩu, xe nhỏ trong hẻm hay không.
- **Hoàn trả**: trát vá, sơn vá, lát vá chỗ bị ảnh hưởng.

Nhà phố liền kề còn có: **thoả thuận và bảo vệ nhà bên cạnh**, chống lún, quan trắc.

## 5. Căn cứ có thể không phải bản vẽ

Cải tạo thường **không có hồ sơ thiết kế đầy đủ**. Căn cứ có thể là:

- bản viết tay hoặc danh sách đầu việc của khách;
- ảnh chụp hiện trạng;
- bản vẽ nhà cũ đã lạc hậu so với thực tế;
- chỉ có bản vẽ phần mới, không có bản vẽ phần cũ.

Khi đó: **bám danh mục đầu việc của khách**, nhưng **đối chiếu với chuỗi tám mắt xích** ở sheet `CaiTao-Chuoi` và danh mục ở mục 4 để không sót nhóm nào.

Khối lượng đo tạm từ PDF theo trục → **trạng thái T toàn bộ**. Có CAD thì đo lại bằng polyline và nâng lên **C** hoặc **S**. Không có gì để đo thì để **N** và hỏi. Khảo sát hiện trạng là việc đầu tiên nên đề xuất với khách.

*2623 (bộ gốc): căn cứ chính là bản viết tay của khách, đã giao danh mục 69 công việc.*

## 6. Công tác chưa có sẵn trong định mức

Một số đầu việc cải tạo (dán carbon, khoan cấy hoá chất theo hãng, cắt bê tông bằng máy chuyên dụng…) có thể **không có mã định mức sẵn** hoặc phải dùng định mức tương tự / định mức dự án. Ghi rõ trong cột Ghi chú: công tác nào **có mã**, công tác nào **cần định mức bổ sung hoặc báo giá** — `[Chờ bổ sung]`. **Không bịa đơn giá** — xem `lap-du-toan`.

## 7. Ghi sổ khối lượng

Sổ tạo bằng `bangkl.tao_so(..., cai_tao=True)` để có sheet `CaiTao-Chuoi`.

**Sheet `CaiTao-Chuoi`** — bảng chống sót theo tầng và khu vực, mỗi cột là một mắt xích:
```
STT | Tầng/Khu vực | Hiện trạng | Bảo vệ/Che chắn | Tháo dỡ | Vận chuyển phế thải | Gia cố/Kết nối | Thi công mới | Điện nước | Hoàn trả | Vệ sinh/Bàn giao | Nguồn | Trạng thái | Ghi chú
```
Nhìn ngang một dòng thấy ngay mắt xích nào còn trống. Ô trống phải có lý do.

**Sheet `6.2-15CaiTao`** — khối lượng từng công tác theo mẫu 6.2. Chia nhóm `HM` theo mắt xích (BẢO VỆ · THÁO DỠ · VẬN CHUYỂN · GIA CỐ, KẾT NỐI · HOÀN TRẢ · VỆ SINH); dòng chi tiết ghi tầng/khu vực và nhóm hiện trạng ở Diễn giải.

- **Đơn vị đúng từng công tác** — m³, m², m, lỗ, cái, trọn gói.
- Phần XÂY MỚI không ghi ở đây — ghi ở sheet cấu kiện, nhưng cột "Thi công mới" của `CaiTao-Chuoi` phải trỏ tên sheet đó.

## 8. Gate chốt — chưa đạt thì chưa giao

- [ ] Mỗi khu vực đã phân vào đúng **một trong bốn nhóm**; không phần nào bỏ trống.
- [ ] **Mỗi công tác tháo dỡ đã kiểm đủ chuỗi**: có vận chuyển phế thải, có gia cố hoặc kết nối, có hoàn trả.
- [ ] Sheet `CaiTao-Chuoi` không còn mắt xích trống chưa giải thích.
- [ ] Đã rà đủ đầu việc đặc thù ở mục 4, đặc biệt **khoan cấy thép**, **cắt sàn**, **chống đỡ tạm**.
- [ ] Phá dỡ đã phân theo cấu kiện, vật liệu, biện pháp; chống đỡ và vận chuyển tính riêng (PL VI).
- [ ] Nâng tầng: cấu kiện mới đã bóc bằng **skill cấu kiện**, không gom vào sheet này.
- [ ] Kết nối cũ–mới và ảnh hưởng lên nhà hiện hữu đã tính.
- [ ] Nhà liền kề: đã xét che chắn, chống lún, thoả thuận nếu có.
- [ ] Căn cứ là bản viết tay thì **đã đối chiếu với chuỗi tám mắt xích**.
- [ ] Khối lượng đo tạm để **T**; đo lại được từ CAD thì đã nâng trạng thái.
- [ ] Công tác chưa có mã định mức đã ghi rõ, không bịa đơn giá.
- [ ] Cột Đơn vị ghi đúng từng dòng, không cộng lẫn.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
