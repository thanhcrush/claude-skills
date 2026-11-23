# BỘ KỸ NĂNG ĐO BÓC — DỰ TOÁN v02 (không phụ thuộc phần mềm)

Công ty TNHH Nghĩa Đạt · lập ngày 08/10/2026

Chuyển thể từ bộ skill gốc `00. SKILL-MOI-Claude` (thư mục `F:\AI\AIDT02 - 260807 - AI đọc bản vẽ tính dự toán…`, bản viết lại 2026-07). **Giữ nguyên cách làm** của bộ gốc: hai lớp dữ liệu, trạng thái C/S/T/N, bảy bước, đếm hai chiều, kiểm ba lượt, các bẫy rút ra từ công trình thật. **Bỏ phụ thuộc phần mềm dtPro MyHouse**: kết quả là sổ khối lượng Excel theo mẫu Bảng 6.1 / 6.2 Phụ lục VI TT 13/2021/TT-BXD, nhập được vào G8, Eta, Delta, Acitt hoặc dùng thẳng trên Excel.

Bộ gốc trên ổ F giữ nguyên, không sửa. Bộ này **chưa cài** vào Claude — anh Thành đọc, kiểm xong mới quyết định cài.

## Danh mục

| # | Skill | Nội dung |
|---|---|---|
| | **00-Nen** | |
| 00 | `do-boc-loi` | Lõi: quy tắc bất biến · C/S/T/N · 7 bước · **quy ước giao cấu kiện theo PL VI** · ván khuôn · cách ghi sổ bằng `bangkl.py` · ngưỡng kinh nghiệm · bản đồ skill. Kèm mẫu Excel và script |
| 01 | `doc-ban-ve` | Kiểm kê hồ sơ, revision, DXF/PDF, danh mục bản vẽ, ma trận cấu kiện × bản vẽ, đối chiếu KT–KC, sheet thông tin chung. Kèm 5 script (đã sửa lỗi `ban_do_view.py`) |
| | **10-KetCauNgam** | |
| 10 | `boc-coc` | Đếm cọc hai nguồn · cọc, ép, nối cọc, đập đầu cọc, khoan nhồi · chiều dài để N nếu không có |
| 11 | `boc-dao-dap` | **Mới.** Đào hố móng, hố gộp, rãnh giằng · lót · đắp hoàn trả · tôn nền · vận chuyển |
| 12 | `boc-mong` | Đài, móng đơn, băng, bè · đếm 3 bước · chiều cao từng đài · ván khuôn móng |
| 13 | `boc-co-cot-vach-pit` | Cổ cột: H thô = cốt nền − mặt móng, trừ đoạn nút giằng và đoạn trong sàn nền · vách pit |
| 14 | `boc-dam-mong` | Xuyên móng thì trừ đài · nối cổ cột thì thông thủy + dòng nút · ván khuôn đáy khi treo · bốn lỗi thật |
| | **20-KetCauThan** | |
| 20 | `boc-cot-vach` | Một dòng một cột một tầng · **cột đến đáy dầm sâu nhất** · vách · cột hàng rào |
| 21 | `boc-dam` | Theo mark tăng dần · **thông thủy mép cột, H − dày sàn, dòng nút** · ván khuôn dầm |
| 22 | `boc-san-mai` | Phủ bì trừ ô trống · hai bẫy sân thượng–mái · ván khuôn sàn · mái ngói/tôn tách lớp lợp, úp nóc |
| 23 | `boc-cau-thang` | Tách bộ phận · dài triển khai · kiểm số bậc × cao bậc · ván khuôn |
| 24 | `thong-ke-thep` | **TK-Thep từng thanh → bộ phận × nhóm Ø** · nối chồng, con kê · hàm lượng chỉ để kiểm / tạm tính |
| 25 | `boc-thep-hinh` | Thép hình, kèo, **xà gồ, cầu phong, lito** · gia công / lắp dựng · sơn theo m² |
| | **30-KienTruc** | |
| 30 | `boc-tuong-cua-lanh-to` | 7 bước · tường mẹ lấy cả ô mở · **trừ lanh tô, giằng trong tường** · cửa theo loại và vật liệu (TK-Cua) |
| 31 | `boc-hoan-thien` | Theo tầng/phòng · mặt đứng riêng · 5 chỗ chống trùng · **bả, sơn lót, sơn dầu, gờ chỉ, dàn giáo** |
| | **40-MEP-CaiTao** | |
| 40 | `boc-dien-nuoc` | Đếm thiết bị **+ bóc dây (theo tiết diện, số sợi, đoạn đứng) và ống (theo tim, ống đứng, phụ kiện)** |
| 41 | `boc-cai-tao` | Chuỗi 8 mắt xích · 4 nhóm hiện trạng · sheet CaiTao-Chuoi chống sót |
| | **50-DuToan-Kiem** | |
| 50 | `lap-du-toan` | **Thay `du-toan-dtpro`.** Căn cứ 2026 (NĐ 206, TT 36/37/38) · sổ khối lượng → **F1** (`bangkl.py f1`) · áp giá Quảng Trị · tổng hợp theo Bảng 3.8 TT 36/2026 · checklist soát file F1 · triage · hợp nhất · BOQ |
| 51 | `kiem-va-giao` | Checklist 8 nhóm (cập nhật quy ước PL VI, đủ công tác đi kèm, mẫu 6.1/6.2) · 4 câu khi giao · 4 nhóm chênh lệch |

## Thay đổi chính so với bộ gốc

| Chủ đề | Bộ gốc (dtPro) | Bộ v02 (quy ước PL VI, Excel, F1) |
|---|---|---|
| Đầu ra | 17 file Excel theo form nhập dtPro, cột Loại mã dtPro (MN, MNG, HH, TT, MD, MB, MC, CBT…) | **Một sổ** `<TenDuAn>_BangKL_v01.xlsx`: 00-ThongTin · 6.1 tổng hợp · các sheet 6.2 chi tiết · TK-Thep · TK-Thep-TH · TK-Cua · (CaiTao-Chuoi). Mọi số là công thức |
| Cột ↔ dầm | Cột hết cao tầng, dầm trừ giao cột | **Cột đến đáy dầm sâu nhất; dầm thông thủy; nút ghi một dòng trong bê tông dầm** |
| Dầm ↔ sàn | Dầm đủ H, sàn phủ bì — dtPro tự trừ | **Dầm H − dày sàn, sàn phủ bì** (phần trong sàn thuộc sàn) |
| Cổ cột ↔ giằng | Cổ cột đến cốt nền, giằng trừ cổ cột | **Cổ cột trừ đoạn nút giằng; giằng thông thủy + dòng nút** |
| Thứ tự gán phần giao | — | **sàn → dầm / giằng → cột** (rút từ PL VI) |
| Đào đất, lót | dtPro tự tính từ "Sâu đào" — cấm bóc | **Bóc riêng** — skill mới `boc-dao-dap` |
| Ván khuôn | dtPro tự tính | **Bóc theo từng cấu kiện**, bảng quy ước chung ở `do-boc-loi` |
| Cốt thép | Hàm lượng kg/m³ × thể tích, bảng mặc định dtPro | **Thống kê từng thanh, tổng hợp theo bộ phận × nhóm Ø**; nối chồng, con kê theo PL VI; bỏ bảng hàm lượng mặc định |
| Cọc | Một dòng "Phần cọc" (m) | Cọc · ép/đóng · nối cọc · đập đầu cọc · thí nghiệm; khoan nhồi tách khoan, bê tông, thép |
| Cửa | 10 mã cố định theo vị trí | Phân theo loại, vật liệu; bảng TK-Cua |
| Tường | Không nói trừ lanh tô | **Trừ lanh tô, giằng tường, bổ trụ BTCT**; lỗ < 0,25 m² không trừ; tường dài ≤ 4 lần dày là trụ |
| Mái ngói/tôn | Chỉ ra m² (đơn giá gộp xà gồ, lito) | Tách lớp lợp, úp nóc, diềm, máng; xà gồ, lito sang thép hình |
| Hoàn thiện | Không bóc nhân công sơn dầu, lắp cửa, cọ ru lô (tính theo m² XD) | Bóc bả, sơn lót, sơn phủ, sơn dầu, gờ chỉ, phào, **dàn giáo theo PL VI** |
| Điện nước | Chỉ đếm thiết bị | Đếm thiết bị **+ dây theo tiết diện, ống theo tim, phụ kiện** |
| Dự toán | `du-toan-dtpro`, file MyHouseMau.xls | `lap-du-toan`, phần mềm bất kỳ, đơn giá Quảng Trị, không bịa mã |
| Ngưỡng kinh nghiệm | Có giá trọn gói 3,5–4,5 tr/m² TP.HCM | Bỏ giá trọn gói; các dải còn lại **tạm dùng** số nhà phố TP.HCM của bộ gốc |
| Thư mục kết quả | `do-boc/02. Coc.xlsx`… | `01-DuAn\<TenDuAn>\03-KhoiLuong\`, tên không dấu, `_v01` |

Mã công trình 26xx, 2607xx, 6016 trong các skill là của bộ gốc, giữ làm dẫn chứng bài học.

## Căn cứ pháp lý — cập nhật 09/10/2026

Từ **01/7/2026**: NĐ 206/2026/NĐ-CP thay NĐ 10/2021; TT 36/2026 thay TT 11/2021; TT 37/2026 thay TT 13/2021; TT 38/2026 (định mức) thay TT 12/2021. Quy tắc đo bóc PL VI TT 13/2021 **không còn bắt buộc** — công ty giữ làm quy ước nội bộ ("PL VI" trong bộ skill hiểu theo nghĩa này); QĐ 1041/QĐ-BXD là hướng dẫn tham khảo. Chi tiết, tỷ lệ chi phí, mẫu căn cứ thuyết minh: `E:\New folder\04-TieuChuan-PhapLy\00-DanhMucVanBan-ChiPhiDuToan_2026_v02.md`.

## Những điểm anh Thành cần chốt trước khi dùng

**Đã chốt (09/10/2026):**

| Điểm | Quyết định |
|---|---|
| Nút giao cột–dầm khác mác bê tông | Tính vào **dầm**, theo mác dầm |
| Ranh nhóm đường kính thép | **≤ 10 / 10–18 / > 18 mm** |
| Cổ cột | Áp định mức **cột** |
| Cửa | **Mua trọn bộ** (gồm phụ kiện, lắp đặt), tính m² hoặc bộ theo báo giá |
| Ngưỡng kinh nghiệm | **Tạm dùng** số nhà phố TP.HCM của bộ gốc, thay khi có số Quảng Trị |
| Dầm thang | Tính vào công tác **cầu thang** |
| Phần mềm dự toán | **F1** |
| Thông số biện pháp đào | **Bộ mặc định** khi dự án không quy định: mái dốc theo TCVN 4447:2012 Bảng 10–11 · mở rộng đáy 0,3 m · lớp bảo vệ 0,10 m đào thủ công, còn lại máy · vận chuyển tạm ≤ 1 km (T) |

**Còn treo:**

1. **Cách nhập Excel của F1**: đã có file dự toán mẫu xuất từ F1 (`03-MauBieu\02-DuToan\DT HANG RAO NHA VAN HOA.xls`); còn cần thử nhập một file nhỏ vào F1 để xác nhận F1 nhận đúng bố cục đó.

## Sổ khối lượng — cách dùng nhanh

```
cd "E:\New folder\06-CongCu\01-Skill-DoBoc_v02\00-Nen\do-boc-loi\scripts"
python bangkl.py mau  "<đường dẫn>\Mau_thu.xlsx"        ← tạo file mẫu có sheet ví dụ
python bangkl.py tonghop "<đường dẫn>\<TenDuAn>_BangKL_v02.xlsx"   ← dựng lại bảng 6.1 (ghi đè đúng file đó)
```

Chi tiết hàm cho AI dùng: docstring đầu `bangkl.py` và `do-boc-loi` mục 6.

## Đóng gói và cài (khi anh Thành cho phép)

Mỗi skill là một thư mục có `SKILL.md`; tên thư mục trùng `name:` trong frontmatter, kebab-case. Giới hạn: `name` ≤ 64 ký tự · `description` ≤ 1024 ký tự · thân `SKILL.md` nên dưới 500 dòng. Thư mục nhóm (`00-Nen`, `10-KetCauNgam`…) chỉ để sắp xếp, không thuộc gói skill.

## Khi thêm bài học mới

Thêm vào **đúng skill của cấu kiện đó**, không nhét vào lõi. Mỗi bài học ghi kèm **mã công trình** rút ra nó, và nói rõ đó là *dấu hiệu đi kiểm* hay *quy ước đã chốt*. Nếu là quy ước thì ghi rõ nó **đi cặp với quy ước nào** — cặp bị tách đôi là nguồn gốc của lỗi tính thiếu và tính trùng.
