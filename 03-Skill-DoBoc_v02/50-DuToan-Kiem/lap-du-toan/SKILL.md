---
name: lap-du-toan
description: Lập, kiểm và soát dự toán xây dựng Việt Nam theo NĐ 206/2026/NĐ-CP, TT 36/2026, TT 37/2026 (hiệu lực 01/7/2026), định mức TT 12/2021 hoặc TT 38/2026 theo lựa chọn của anh Thành, giá xây dựng tỉnh Quảng Trị, trên phần mềm Dự toán F1 của công ty (hoặc G8, Eta, Delta, Acitt, Excel). Dùng skill này khi người dùng nhắc tới dự toán, áp giá, đơn giá, áp mã định mức, nhập khối lượng vào F1, tổng hợp chi phí xây dựng, chi phí chung, nhà tạm, thuế GTGT, thuyết minh dự toán, tổng mức đầu tư, hoặc hỏi công trình này bao nhiêu tiền. Dùng cả khi người dùng đưa bản vẽ mới và hỏi có làm đổi dự toán nhiều không (triage), khi cần soát file dự toán xuất từ F1, hợp nhất nhiều bản, hoặc lập BOQ cho tư vấn giám sát. Không bịa mã hiệu, đơn giá, tỷ lệ.
---

# Lập và kiểm dự toán

**Skill liên quan** — nếu chưa được cài thành skill thì đọc thẳng file trong bộ v02 (`E:\New folder\06-CongCu\01-Skill-DoBoc_v02\`):

| Tên nhắc trong skill này | File |
|---|---|
| `do-boc-loi` (quy ước đo bóc, sổ khối lượng, ngưỡng kinh nghiệm) | `00-Nen\do-boc-loi\SKILL.md` |
| `bangkl.py` (sổ khối lượng, lệnh xuất F1) | `00-Nen\do-boc-loi\scripts\bangkl.py` |
| `kiem-va-giao` (checklist trước khi giao) | `50-DuToan-Kiem\kiem-va-giao\SKILL.md` |
| `boc-dao-dap` (thông số đào mặc định) | `10-KetCauNgam\boc-dao-dap\SKILL.md` |

Khi việc dự toán cần tới khối lượng hoặc quy ước đo bóc, **đọc `do-boc-loi` trước**.

Skill `vn-du-toan` (đã cài) lập dự toán cho hồ sơ bản vẽ do thư viện vncad tự dựng. Skill này dùng cho dự toán trên **F1** và soát file dự toán. Người dùng nói rõ việc nào thì làm theo skill đó; không rõ thì hỏi.

## 0. Căn cứ — đọc trước mỗi dự toán

Danh mục văn bản hiện hành, tỷ lệ chi phí, mẫu "Căn cứ lập" cho thuyết minh: **`E:\New folder\04-TieuChuan-PhapLy\00-DanhMucVanBan-ChiPhiDuToan_2026_v02.md`**. Mở file đó, kiểm ngày cập nhật; quá 3 tháng hoặc dự án lập vào thời điểm khác thì tra lại văn bản mới trước khi làm. Luôn nhắc anh Thành **kiểm tra lại hiệu lực**.

Tóm tắt (cập nhật 09/10/2026):

| Nội dung | Văn bản áp dụng từ 01/7/2026 | Thay cho |
|---|---|---|
| Quản lý chi phí | **NĐ 206/2026/NĐ-CP** | NĐ 10/2021 |
| Phương pháp xác định chi phí, cấu trúc dự toán | **TT 36/2026/TT-BXD** (+ QĐ 1538/QĐ-BXD đính chính) | TT 11/2021, TT 14/2023 |
| Phương pháp định mức, giá nhân công (nhóm mới), giá ca máy | **TT 37/2026/TT-BXD** | TT 13/2021, TT 01/2025 |
| Định mức xây dựng | **TT 38/2026/TT-BXD** | TT 12/2021, TT 09/2024, TT 08/2025 |
| *Lưu ý định mức* | CLAUDE.md của công ty **giữ ghi TT 12/2021** (anh Thành quyết định 09/10/2026). Mỗi dự toán **hỏi anh Thành chọn bộ định mức trong F1** (TT 12/2021 hay TT 38/2026), ghi rõ bộ đã dùng trong thuyết minh | |
| Xác định khối lượng | **QĐ 1041/QĐ-BXD** (tham khảo) | PL VI TT 13/2021 — công ty giữ làm quy ước đo bóc nội bộ |
| Thuế GTGT | 8 % cho dịch vụ xây dựng đến 31/12/2026 nếu đủ điều kiện (NQ 204/2025/QH15, NĐ 174/2025/NĐ-CP) | |
| Giá nhân công, ca máy Quảng Trị | QĐ 16/QĐ-SXD, QĐ 20/QĐ-SXD (01/2026). Bảng quy đổi theo TT 37/2026 chưa xác minh → giá nhân công dùng **GIẢ ĐỊNH tạm thời**, xem mục 3 | |

Dự án / hợp đồng quy định căn cứ khác thì theo dự án. Dự toán **đã duyệt trước 01/7/2026** không phải duyệt lại; các bước tiếp theo theo văn bản mới (chuyển tiếp NĐ 206/2026 — đối chiếu bản gốc).

## 1. Năm việc khác nhau, đừng lẫn

| Người dùng nói | Việc thật | Đọc mục |
|---|---|---|
| "lập dự toán cho công trình này" | Sổ khối lượng → F1 → áp giá → tổng hợp → thuyết minh | 2, 3, 4, 5 |
| "kiểm giúp file dự toán này" | Soát bản đã có (thường là file xuất từ F1) | 6 |
| "bản vẽ mới có đổi nhiều không" | **Triage** — không bóc lại | 7 |
| "gộp mấy bản dự toán này" | Hợp nhất và phân xử | 8 |
| "làm BOQ cho tư vấn giám sát" | **Bối cảnh khác hẳn** | 9 |

Chưa có khối lượng thì đừng lập dự toán — quay về các skill bóc trước.

## 2. Từ sổ khối lượng sang F1

Phần mềm công ty: **Dự toán F1** (F1 Tech). Mẫu tham chiếu: `E:\New folder\03-MauBieu\02-DuToan\DT HANG RAO NHA VAN HOA.xls` — file xuất từ F1, sheet **"Công trình"** là bảng chi tiết khối lượng kiểu Bảng 6.2: mỗi công tác một dòng (STT · Ký hiệu bản vẽ · Mã hiệu · Tên · Đơn vị · KL toàn bộ = `ROUND(SUM(dòng dưới),3)`), dưới là các dòng diễn giải `vị trí: phép tính = kết quả` có số ở cột KL một bộ phận. Đơn vị theo định mức: **100m3** (đào, đắp), **100m2** (ván khuôn), **tấn** (cốt thép), m3, m2…

Quy trình:

1. **Chốt sổ khối lượng** (`<TenDuAn>_BangKL_vNN.xlsx`), chạy `kiem-va-giao` trước.
2. **Xuất bố cục F1**: `python bangkl.py f1 "<sổ>.xlsx" "<TenDuAn>_F1_v01.xlsx"` (script `E:\New folder\06-CongCu\01-Skill-DoBoc_v02\00-Nen\do-boc-loi\scripts\bangkl.py`; chạy: `cd` vào thư mục `scripts` đó rồi gõ lệnh). Lệnh tự đổi đào/đắp sang 100m3, ván khuôn sang 100m2, bỏ dòng N, liệt kê công tác chưa có mã. Công tác có đơn vị định mức khác (VD lát 100m2, xây trát m2…) truyền `quy_doi={tên: (đơn vị, hệ số)}`.
3. **Nhập vào F1** bằng chức năng nhập Excel của F1 — **thử một hạng mục nhỏ trước**. Thao tác nhập chính xác của phiên bản F1 đang dùng **chưa được kiểm chứng** `[Cần xác nhận lại]`: lần đầu anh Thành làm, ghi lại các bước vào mục này.
4. **Mã hiệu**: tra trong F1 theo tên công tác (tên đã đặt theo cách gọi của định mức). Dùng **bộ định mức anh Thành chọn cho dự toán này** (TT 12/2021 theo CLAUDE.md, hoặc TT 38/2026 — hỏi trước, ghi vào thuyết minh). Mã hai bộ có thể khác nhau — đừng chép mã từ dự toán cũ khi chưa đối chiếu đúng bộ đang dùng. AI **không tự điền mã** khi không có nguồn; gợi ý thì gắn `[Cần xác nhận lại]`.
5. **Đối chiếu sau khi nhập**: số công tác và khối lượng từng công tác trong F1 = bảng 6.1 (sau quy đổi đơn vị). Lệch thì tìm dòng rơi rớt.
6. Ghi mã đã chọn ngược lại vào sổ khối lượng (bản `_v` mới) để lần sau dùng lại.

Phần mềm khác (G8, Eta, Delta, Acitt) hoặc Excel thuần: cùng nguyên tắc, lấy bốn trường Mã · Tên · Đơn vị · Khối lượng từ 6.1, diễn giải từ 6.2.

## 3. Áp giá trong F1 — giá Quảng Trị

Theo hướng dẫn của F1 cho Quảng Trị (dutoanf1.com.vn, áp cho QĐ 16, 20/QĐ-SXD năm 2026):

- **Sheet Nhân công**: chuột phải trong bảng → *Lắp giá nhân công từ cơ sở dữ liệu – tất cả nhân công* → chọn **vùng** của địa bàn công trình → Đồng ý → *Áp giá hiện tại*.
- **Sheet Máy thi công**: chuột phải → *Lắp giá máy từ cơ sở dữ liệu – tất cả máy* → chọn vùng theo QĐ giá ca máy → *Lắp giá máy* → *Bù giá ca máy* → chuột phải nền bảng → *Lắp giá gốc nhiên liệu, thợ điều khiển máy (tất cả máy)* → chọn giá gốc của QĐ ca máy → lắp giá nhiên liệu, điện mới nhất → áp bù giá.
- **Sheet Vật liệu**: nhập giá theo **công bố giá vật liệu Sở Xây dựng Quảng Trị kỳ gần nhất**, ghi rõ tháng/quý ở tiêu đề bảng ("Theo giá thông báo …"). Vật liệu không có trong công bố → báo giá nhà cung cấp (`05-VatTu-NhaCungCap\`), ghi nguồn; không có → `[Chờ bổ sung]`.
- **Vùng**: đơn giá nhân công Quảng Trị chia 3 vùng theo lương tối thiểu vùng (NĐ 293/2025/NĐ-CP) — chọn đúng vùng của xã/phường nơi xây dựng, ghi trong thuyết minh.

Từ 01/7/2026, giá nhân công phải theo **nhóm nhân công mới của TT 37/2026** (bảng quy đổi do Sở Xây dựng công bố).

### Giá nhân công — GIẢ ĐỊNH tạm thời (anh Thành chốt 09/10/2026)

Chưa có bảng giá nhân công quy đổi theo nhóm TT 37/2026 của Sở Xây dựng Quảng Trị (đã xác minh) → **giả định tạm dùng đơn giá nhân công QĐ 16/QĐ-SXD ngày 12/01/2026**, đúng vùng của địa bàn công trình. Mọi chỗ dùng giả định này **bắt buộc ghi chú**:

1. **Thuyết minh, mục căn cứ** — ghi nguyên văn: *"Giá nhân công: GIẢ ĐỊNH tạm áp dụng đơn giá nhân công theo Quyết định số 16/QĐ-SXD ngày 12/01/2026 của Sở Xây dựng tỉnh Quảng Trị (vùng …), do chưa có công bố giá nhân công theo nhóm nhân công của Thông tư 37/2026/TT-BXD; sẽ điều chỉnh khi có công bố."*
2. **F1, sheet Nhân công** — thêm dòng ghi chú `[Giả định]` dưới tiêu đề bảng, nêu văn bản đang tạm dùng.
3. **`GiaDinhDaDung.md`** của dự án — một mục: giả định gì · căn cứ · ảnh hưởng (chênh khi có bảng quy đổi: **chưa ước được**) · việc phải làm khi có công bố.
4. **`00-DanhSachCanKiem.md`** — một dòng nhắc kiểm lại giá nhân công khi Sở công bố.
5. Dự toán gửi ra ngoài: mục **"CẢNH BÁO — đọc trước khi gửi khách"** nêu rõ giá nhân công là giả định.

Khi Sở Xây dựng Quảng Trị công bố bảng quy đổi (đã đối chiếu bản gốc), bỏ giả định, lập bản `_v` mới và ghi chênh lệch.

## 4. Tổng hợp dự toán chi phí xây dựng — TT 36/2026, Phụ lục III *(đã đối chiếu bản gốc + QĐ 1538 đính chính, 09/10/2026)*

Bảng 3.8:

```
I   Chi phí trực tiếp            T   = VL + NC + M
II  Chi phí gián tiếp            GT  = C + TT
    1 Chi phí chung              C   = T × tỷ lệ (Bảng 3.3)   [hoặc NC × tỷ lệ Bảng 3.4 cho một số loại công tác]
    2 Công việc không xác định được khối lượng từ thiết kế
                                 TT  = T × tỷ lệ (Bảng 3.5)
III Thu nhập chịu thuế tính trước TL = (T + GT) × tỷ lệ (Bảng 3.6)
    Chi phí xây dựng trước thuế  GXDTT = T + GT + TL
IV  Thuế GTGT                    GTGT = GXDTT × TGTGT
    Chi phí xây dựng sau thuế    = GXDTT + GTGT
V   Chi phí nhà tạm để ở và điều hành thi công
                                 LT  = GXDTT × tỷ lệ (Bảng 3.7) × (1 + TGTGT)   ← theo QĐ 1538 đính chính
```

| Tỷ lệ (%) | Dân dụng | Giao thông | Hạ tầng kỹ thuật |
|---|---|---|---|
| Chi phí chung — Bảng 3.3 (CPXD trước thuế ≤40 / ≤60 / ≤100 / ≤300 / ≤500 / ≤750 / ≤1000 / >1000 tỷ) | **7,3** / 7,1 / 6,7 / 6,5 / 6,2 / 6,1 / 6,0 / 5,8 | **6,2** / 6,0 / 5,6 / 5,3 / 5,1 / 5,0 / 4,9 / 4,6 | **5,5** / 5,3 / 5,0 / 4,8 / 4,5 / 4,4 / 4,3 / 4,0 |
| Không xác định được khối lượng — Bảng 3.5 | **2,5** | **2,0** (trong hầm 6,5) | **2,0** |
| Thu nhập chịu thuế tính trước — Bảng 3.6 | **5,5** | **6,0** | **5,5** |
| Nhà tạm — Bảng 3.7 (≤15 / ≤100 / ≤500 / ≤1000 / >1000 tỷ) | còn lại: **1,1** / 1,0 / 0,95 / 0,9 / 0,85 | theo tuyến: **2,2** / 2,0 / 1,9 / 1,8 / 1,7 | theo tuyến hoặc còn lại tùy công trình |

- Mức tra Bảng 3.3 và 3.7 theo **chi phí xây dựng trước thuế trong tổng mức đầu tư được duyệt**. Dự án **chỉ lập báo cáo kinh tế – kỹ thuật** → chi phí chung lấy **cột ≤40 tỷ**.
- **Vùng núi, biên giới, trên biển, hải đảo**: chi phí chung **× 1,1**. Một số xã miền núi của Quảng Trị có thể thuộc diện này — kiểm từng dự án `[Cần xác nhận lại]`.
- Chi phí chung trên **NC** (Bảng 3.4) chỉ cho: sửa chữa đường bộ, đường sắt, báo hiệu hàng hải; công trình nông nghiệp – môi trường làm hoàn toàn thủ công; lắp đặt thiết bị công nghệ, đường dây, trạm biến áp, thí nghiệm hiệu chỉnh điện.
- Công trình có **T < 45 tỷ**: tỷ lệ Bảng 3.5 chưa gồm văn phòng phòng thí nghiệm tại hiện trường.
- **Nhà tạm** là khoản mục riêng của chi phí xây dựng (Bảng 3.1: GXD = CPXD công trình + công trình tạm, phụ trợ + nhà tạm + phá dỡ), **không** nằm trong chi phí gián tiếp như TT 11/2021. File F1 mẫu còn cấu trúc cũ — trong F1 chọn **mẫu tổng hợp theo TT 36/2026** khi F1 đã cập nhật; chưa có thì báo anh Thành, không tự sửa tay công thức của F1.
- Hạng mục thiết kế riêng / công nghệ đặc thù, báo giá trọn gói: Bảng 3.9, C, TT, TL **× 50 %**.
- Giá không tách VL / NC / M (báo giá, giá tương tự) → **gộp vào chi phí vật liệu**.
- **Dự phòng** (Điều 6 khoản 7, PL II mục 6): phát sinh khối lượng = dự toán trước dự phòng × **kps ≤ 5 %**; trượt giá theo tiến độ và chỉ số giá xây dựng.
- **Thuế GTGT**: 8 % đến 31/12/2026 nếu dịch vụ xây dựng đủ điều kiện giảm; ghi rõ mức đang dùng và căn cứ.
- Chi tiết, bảng đầy đủ: file danh mục văn bản **v02**, mục 3; bản gốc ở `04-TieuChuan-PhapLy\05-VanBanChiPhi-2026\TT36-2026\`.

## 5. Thuyết minh, bìa, phần chưa gồm

- **Căn cứ lập**: dùng đúng mẫu ở mục 6 file danh mục văn bản; điền số QĐ giá nhân công, ca máy, kỳ công bố giá vật liệu, tên và số hiệu bộ bản vẽ. **Không giữ căn cứ cũ** của file mẫu (NĐ 68/2019, TT 09, 10, 11, 15, 16/2019, NĐ 72/2018, NĐ 141/2017, TT 06/2016 — đều hết hiệu lực).
- **Bìa, tiêu đề**: đơn vị lập **Công ty TNHH Nghĩa Đạt**; xoá thông tin "Công ty CP F1 Tech" của file mẫu. Tên công trình, hạng mục, địa điểm, ngày lập đầy đủ.
- **Giá trị bằng chữ** khớp đúng con số tổng đã làm tròn — kiểm lại sau mỗi lần sửa.
- Sheet không dùng (dự phòng trượt giá năm cũ, gói thầu thiết bị trống…) → ẩn hoặc cập nhật, không để số liệu năm khác.
- Ghi rõ phần **CHƯA GỒM** — thường là: cốt thép chưa thống kê · cọc chưa có chiều dài · san nền ngoài nhà · thiết bị chưa chốt chủng loại · công tác chờ báo giá · công tác tạm tính (dòng T).
- Lưu ở `01-DuAn\<TenDuAn>\04-DuToan\`, tên `<TenDuAn>_DuToan_v01.xls(x)`; sửa thì `_v02`, không ghi đè.

### Khi LẬP — nguyên tắc chung

1. Đơn giá có **nguồn và kỳ công bố**; có nhân hệ số thì ghi rõ hệ số và lý do.
2. Công tác **không có đơn giá** → **ô vàng `[Chờ bổ sung]`**, không bịa giá.
3. Khối lượng lấy từ sổ khối lượng, không gõ lại số.
4. **Không tách công tác chỉ vì khác tầng** — một công tác một dòng giá; chi tiết theo tầng nằm ở diễn giải.
5. Công tác chứa dòng **T** → cảnh báo trong ghi chú dự toán. Dòng **N** không vào dự toán, liệt kê ở phần chưa gồm.
6. **Hiểu thành phần hao phí trước khi kết luận** "đơn giá bất thường" hay "thiếu công tác": đọc thuyết minh định mức (công tác nào đã gồm vật liệu phụ, dàn giáo, vận chuyển trong phạm vi…). *Bài học bộ gốc (2613): tưởng cốp pha bị thổi, thực ra định mức ván khuôn đã gộp vật tư — chiếm ~45 % tổng.*

## 6. Khi KIỂM dự toán (thường là file xuất từ F1)

**Xác định sheet chính**: sheet "Công trình" (khối lượng + đơn giá + thành tiền) và "TH dự toán hạng mục". File xuất từ phần mềm có thể có sheet phụ **chưa tính lại** — chỉ kết luận trên sheet chính; ô hiện `#######` thường chỉ là cột hẹp, mở rộng cột trước khi báo lỗi.

### Checklist soát file F1 — rút từ lần soát file mẫu hàng rào (09/10/2026)

**Khối lượng (sheet "Công trình"):**
- [ ] **Hệ số nhân số lượng** có mặt ở **mọi số hạng** của diễn giải. *Mẫu: `8*(4*0,6*0,15)+(4*0,32*1,05)` — quên nhân 8 cho cổ móng, ván khuôn thiếu ~10 lần.*
- [ ] **Diện tích là hiệu diện tích**, không phải hiệu cạnh. *Mẫu đắp đất: `1,1*0,38*0,38` (0,38 = 0,7 − 0,32) thay vì `1,1*(0,7² − 0,32²)` — đắp thiếu ~một nửa.* Đắp phải = đào − thể tích chiếm chỗ.
- [ ] **Kết quả ghi sau dấu "=" khớp phép tính** trong diễn giải và khớp số ở cột KL. *Mẫu: `1,398/0,15*2` ghi 18,667 (đúng 18,640); dòng ghi ":136,986" nhưng giá trị 166,943.*
- [ ] **Cùng một cấu kiện, cùng kích thước ở mọi công tác**: chiều cao cổ móng ở bê tông và ván khuôn giống nhau; số cột ở bê tông, ván khuôn, sơn giống nhau; số hố đào = số móng.
- [ ] **Đủ bộ công tác cho mỗi cấu kiện**: có ván khuôn thì phải có bê tông (và ngược lại); có gia công thì phải có lắp dựng; có bê tông cột thì có ván khuôn cột.
- [ ] **Mã đúng bộ phận**: thép cột, giằng không dùng mã thép móng; ván khuôn móng không dùng mã ván khuôn cột.
- [ ] Nhãn đoạn, trục không trùng (hai dòng cùng "Đoạn 2-3"); công thức không chép nhầm hàng.
- [ ] Đào: chiều sâu theo **từng đoạn / từng loại móng**, có mở rộng đáy theo quy ước công ty (`boc-dao-dap`).
- [ ] Đơn vị đúng hệ số định mức (100m3, 100m2…), không có đơn vị lạ ("1m2").
- [ ] Làm tròn 3 số lẻ thống nhất.

**Giá và tổng hợp:**
- [ ] Bộ định mức là **TT 38/2026** (với dự toán lập từ 01/7/2026); giá nhân công, ca máy đúng văn bản và **đúng vùng**; giá vật liệu ghi rõ kỳ công bố.
- [ ] Cấu trúc tổng hợp theo **TT 36/2026** (nhà tạm là mục riêng); tỷ lệ C, TT, TL, LT đúng bảng; thuế GTGT đúng mức và căn cứ.
- [ ] Thuyết minh: căn cứ hiện hành; giá trị bằng chữ khớp tổng; tên đơn vị lập đúng.
- [ ] Không còn sheet chứa số liệu năm khác (dự phòng trượt giá 2012–2020…).

### Ba cạm bẫy khi tìm hạng mục

1. Tên công tác hay **gõ thiếu dấu hoặc sai chính tả** — "Thép dự **ưng** lực". **Khớp lỏng, bỏ dấu.**
2. Dòng đặc biệt (dự ứng lực, trọn gói, tạm tính) hay **bỏ trống mã hiệu** → lọc theo mã sẽ bỏ sót. *2611 sót cáp dự ứng lực — một gói 3,5 tỷ — **hai lần**.*
3. **Quét mọi dòng kể cả mã trống.** Xác nhận sự vắng mặt bằng cách đọc mắt đoạn cuối từng phần.

### Dòng KL = 0 có thể là chủ đích

Phần cọc chờ chiều dài · phần sân · bể nước và bể phốt mua sẵn hoặc trọn gói · các dòng phụ thu (0 đ = không áp dụng). **Hỏi xác nhận trước khi gọi là thiếu.**

### Thép

Bản nhập theo **bảng thống kê thực** là **đúng**. Bản tách nhiều dòng theo **hàm lượng giả định** trông gọn nhưng chưa chuẩn.

### Kỷ luật Excel khi kiểm

Quét `#REF!` `#DIV/0!` `#VALUE!` `#NAME?` `#N/A` · công thức thiếu · **kết quả nhập cứng** · số sai cột · **đơn vị lệch hệ số**. Kiểm ngoại lệ: lỗ mở rộng hơn cấu kiện mẹ · chiều dài âm · khối lượng không đổi sau khi sửa kích thước · tổng tuyến khác tổng dòng. **Số 0 là dữ liệu hợp lệ.**

**Báo kết quả soát**: chia ba nhóm — *lỗi làm sai tiền (kèm số ước tính lại)* · *chỗ không khớp cần anh kiểm* · *phần hồ sơ cũ*. Số tính lại phải ghi giả định đã dùng. **Không sửa file gốc**; sửa thì tạo bản `_v` mới.

## 7. Triage — "bản vẽ mới có đổi nhiều không"

Khách hỏi kiểu này thì **không bóc lại từ đầu**. Năm bước:

1. Mở dự toán cũ lấy: tổng · **tỷ trọng phần kết cấu** (móng + thân + cọc) trên tổng · các giả định (diện tích sàn từng tầng, số cọc, chiều dài cọc tạm).
2. Đọc bản vẽ mới chốt **bốn biến lớn**: số tầng · diện tích sàn · **số cọc** · loại móng. Thêm: tiết diện cột, dầm, sàn ở mức bình thường hay bất thường.
3. Phần hoàn thiện + điện nước + xây trát **không đổi** nếu kiến trúc không đổi.
4. Độ nhạy: kết cấu lệch X % → tổng đổi `X % × tỷ trọng KC`. **Ngưỡng "nhiều" = tổng đổi > 5 %** (ngưỡng của bộ gốc — anh Thành chỉnh theo yêu cầu khách).
5. Hình học khớp và tiết diện bình thường → kết luận **đổi ít, không tính lại**. Gắn cờ các mục chưa chốt.

*6016: kết cấu chiếm 38,1 % tổng → kết cấu phải lệch hơn 13 % thì tổng mới đổi hơn 5 %.*

Dự toán cũ lập trước 01/7/2026 mà nay lập lại: chênh còn do **đổi định mức (TT 38/2026), nhóm nhân công (TT 37/2026), cấu trúc tổng hợp (TT 36/2026)** — tách riêng phần chênh do văn bản với phần chênh do bản vẽ.

**Luôn báo cả hai mức chênh**: từng dòng và tổng. Hai bản bóc theo **quy ước giao cấu kiện khác nhau** lệch lớn từng dòng cột / dầm / sàn nhưng tổng bê tông thân gần như không đổi — nói rõ là do quy ước.

## 8. Hợp nhất nhiều bản dự toán

*2616 — ba bản: 702,8 tr · 246,4 tr · hợp nhất 208,3 tr.*

- Lập bảng đối chiếu **từng đầu việc**, phân xử bằng bản vẽ và số của khách.
- Ba lỗi hay gặp: **bịa giá** hạng mục chưa chốt chủng loại · **lấy nhầm đơn giá của hạng mục khác** · **áp hệ số bừa** cho phạm vi chưa chốt.
- Hạng mục chưa chốt → **để trống đơn giá kèm cảnh báo**, không điền tạm.
- Viết mục **"CẢNH BÁO — đọc trước khi gửi khách"** ở đầu ghi chú, liệt kê ô còn trống và lý do.

## 9. BOQ cho tư vấn giám sát — luật khác hẳn

- **Quy định tính khối lượng viết ngay ở cột Mô tả của BOQ**. Hợp đồng không quy định khác thì dùng quy ước đo bóc của công ty (`do-boc-loi`, kế thừa PL VI TT 13/2021, phù hợp QĐ 1041/QĐ-BXD) và **ghi rõ quy ước** trong BOQ — vì từ 01/7/2026 không còn quy tắc đo bóc bắt buộc chung.
- **Mọi ô là công thức**. **Thép vẽ hình thanh**. Dự trù **tối thiểu bốn vòng giải trình**.
- Chênh lệch với BOQ của chủ đầu tư lập bảng **từng dòng**, nêu rõ do **quy ước đo khác** hay **đọc bản vẽ khác**.
- Hợp đồng theo NĐ 210/2026/NĐ-CP; mẫu hợp đồng QĐ 1040/QĐ-BXD. Hợp đồng **trọn gói** thường không đo bóc chi tiết khối lượng hoàn thành — hỏi loại hợp đồng trước khi làm.

## 10. Suất tham chiếu

Xem `do-boc-loi` mục 8. Thêm: **trát ≈ 2 × diện tích tường + trần**. Suất vốn đầu tư dùng số Bộ Xây dựng công bố hiện hành. **Không dùng giá trọn gói ước theo m²** của khu vực khác. Ra ngoài dải phải giải thích được. **Tổng khớp KHÔNG phải xác nhận** — soi danh mục, không soi tổng.

## 11. Gate chốt — chưa đạt thì chưa gửi khách

**Khi lập:**
- [ ] Đã mở danh mục văn bản; căn cứ, định mức, giá đúng thời điểm lập; đã nhắc anh Thành kiểm hiệu lực.
- [ ] Số công tác và khối lượng trong F1 khớp bảng 6.1 (sau quy đổi đơn vị).
- [ ] Mã hiệu có nguồn, theo bộ định mức đang áp dụng; không mã bịa.
- [ ] Giá nhân công, ca máy đúng văn bản và vùng; giá nhân công giả định đã **ghi chú đủ 5 chỗ** (mục 3); giá vật liệu ghi kỳ công bố; công tác chưa có giá để ô vàng.
- [ ] Đã hỏi và ghi rõ bộ định mức dùng trong F1 (TT 12/2021 hay TT 38/2026).
- [ ] Tổng hợp theo Bảng 3.8 TT 36/2026, tỷ lệ đúng, thuế GTGT đúng mức và căn cứ.
- [ ] Đủ công tác đi kèm (đào đắp, lót, ván khuôn, thép, dây ống, bả sơn, dàn giáo).
- [ ] Thuyết minh: căn cứ hiện hành, đơn vị lập, bằng chữ khớp, phần CHƯA GỒM; dòng T có cảnh báo, dòng N không vào dự toán.

**Khi kiểm:**
- [ ] Đã chạy checklist soát file F1 ở mục 6; báo theo ba nhóm, số tính lại kèm giả định.
- [ ] Đã quét **mọi dòng kể cả mã trống**; dòng KL = 0 đã hỏi xác nhận.
- [ ] Không sửa file gốc.

**Khi triage:**
- [ ] Đã lấy tỷ trọng kết cấu; đã chốt bốn biến lớn; kết luận theo độ nhạy; tách chênh do văn bản và chênh do bản vẽ.
