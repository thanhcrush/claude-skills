---
name: trien-khai-revit
description: Triển khai mô hình Revit đã dựng xong thành bộ tờ bản vẽ kiến trúc theo quy ước Công ty TNHH Nghĩa Đạt qua MCP của pyRevit - khung tên công ty (khổ A3 / A3 dài), chữ Arial, dim 3 lớp mm gạch xiên, tag phòng + diện tích, tag cửa, mặt cắt, bảng thống kê cửa và phòng, tờ KT-01…, bộ tờ để in PDF. Dùng sau skill ve-revit, khi người dùng nói "ra bản vẽ từ Revit", "lập tờ, khung tên", "dim, tag mặt bằng", "xuất hồ sơ Revit".
---

# Triển khai mô hình Revit ra bộ tờ bản vẽ

Làm sau skill `ve-revit` (mô hình đã dựng, đã chạy chặng 7 căn khung nhìn). Dùng MCP pyRevit
(`run_modify`, `run_query`, `capture_view`). Trả lời tiếng Việt, ngắn.

Script nằm ở `scripts/` của skill này. Mẫu đã chạy thật: Trường TH Cửa Việt, 11 tờ
(`E:\New folder\01-DuAn\Cua Viet\02-BanVe\01-Revit\revit-workspace\`, 10/11/2026).

## 1. Chuẩn bị

1. Đọc mục "Chuẩn bị phiên" và "Bẫy đã gặp" của skill `ve-revit` (chọn pid, lưu file trước,
   một phiên Claude một mô hình, kết quả có dấu phải `ascii_safe`).
2. Chép `scripts/tk*.py`, `vn_revit.py`, `vn_don_vi.py` vào workspace dự án (cùng chỗ module dữ liệu
   của ve-revit). Chép `hoso_mau_cuaviet.py` thành `hoso_<duan>.py` rồi sửa:
   - `KHO`: khổ giấy. Nhà dài ≤ 35 m dùng A3 (420×297) TL 1:100; dài hơn dùng **A3 dài 840×297**
     (như hồ sơ gốc Cửa Việt) hoặc A3 TL 1:200. Hỏi người dùng nếu chưa rõ.
   - `THONG_TIN`: chủ đầu tư, công trình, hạng mục, địa điểm lấy từ tờ bìa bản vẽ gốc, có nguồn.
     Không tự điền; thiếu ghi `[Chờ bổ sung]`.
   - `TRUC_KEO`, `KHUNG_MB`, `DIM`: theo lưới trục để mặt bằng (kể cả bóng trục, dim) vừa khổ,
     nằm phía trên khung tên.
   - `MAT_CAT`: vị trí ký hiệu mặt cắt lấy từ mặt bằng tầng 1 bản gốc.
   - `TO`: danh mục tờ, ký hiệu `KT-01`… theo CLAUDE.md.
3. Kiểm khổ trước khi chạy: chiều rộng khung cắt / tỉ lệ + 2×5 mm ≤ khổ − 25 mm; chiều cao mặt bằng
   phải chừa khung tên (cao 56 mm) ở góc phải dưới.

## 2. Các chặng (mỗi file một hàm `chay`, chạy lại được)

| File | Làm gì |
|---|---|
| `tk0_chuan.py` | Thông tin dự án; kiểu chữ `VN-Arial 2.0/2.5/3.5/3.5 đậm/5 đậm` (không khung, nền trong); kiểu dim `VN-Dim 2.5 gạch xiên` **đơn vị mm**; Type Mark cửa = ký hiệu Đ1, S1…; kéo lưới trục gọn; tạo mặt cắt; view 3D (ẩn trục, cao độ, mặt tham chiếu); tỉ lệ, tên trên tờ (Title on Sheet), khung cắt, **khung chú thích 5 mm**, ẩn chú thích chung của template; gọn cao độ + trục trên mặt đứng/mặt cắt; view range mặt bằng mái |
| `tk1_khung_ten.py` | Family khung tên tạo trong bộ nhớ từ `New Size metric.rft`, nạp thẳng vào dự án: viền giấy, khung vẽ (lề trái 20, còn lại 5), khung tên 180×56 góc phải dưới |
| `tk2_ghi_chu.py` | Mặt bằng: dim trục + tổng (dưới, trái), chi tiết ô cửa + trục + tổng (trên); tag phòng có diện tích; tag cửa đi, cửa sổ |
| `tk3_bang.py` | Bảng thống kê cửa đi, cửa sổ (gộp theo ký hiệu), phòng (từng phòng, có tổng) |
| `tk4_to.py` | Tạo tờ theo `hs.TO`, đặt viewport canh trên, giữa khổ, tránh khung tên; ghi giá trị khung tên; tạo bộ tờ in PDF |
| `tk_tat_ca.py` | Gọi tk0 → tk4 trong **một** `run_modify`: người dùng chỉ bấm Keep một lần |

Gọi: `import tk_tat_ca, hoso_<duan> as hs; result = tk_tat_ca.chay(doc, app, hs, file_dich="<Title file>")`.
Luôn chạy thử (`dry_run=true`) trước, đọc `to[].canh_bao` ("chong khung ten", "tran le phai") rồi mới
chạy thật. Gói lớn chạy thật mất 1–3 phút cộng thời gian người dùng bấm Keep: báo trước để người dùng
bấm ngay (MCP hết hạn 600 s).

## 3. Bẫy đã gặp (Cửa Việt, 10/11/2026)

| Bẫy | Cách xử lý (đã có trong script) |
|---|---|
| Kiểu dim template hiện feet-inch dù dự án đã mm | `DimensionType.SetUnitsFormatOptions(FormatOptions(Millimeters))` |
| Kiểu chữ nhân bản từ template có khung quanh chữ | `TEXT_BOX_VISIBILITY = 0` |
| Template family khung tên có sẵn khung A4 297×210, 4 nét này không xóa được (kể cả sau khi xóa kích thước ràng buộc) | Dời chính 4 nét đó thành mép giấy (`SetGeometryCurve`) |
| Nạp đè family khung tên không ăn (family tạo trong bộ nhớ mang tên "FamilyN") | Xóa family khung tên cũ do skill tạo rồi nạp mới; tk4 tạo lại các tờ |
| Không xóa được tờ đang là view hiện hành | Chuyển view hiện hành về {3D} (`uidoc.RequestViewChange`) trước khi chạy |
| Khung chú thích template lệch 25,4 mm; mũi tên Bắc, thước tỉ lệ của template nằm ngoài khung làm viewport phình | Đặt offset 5 mm giấy, ẩn `OST_GenericAnnotation` |
| `Viewport.GetBoxOutline()` gồm cả ký hiệu mặt đứng, phần tử ngoài khung → xếp tờ sai | Xếp theo khung cắt: tọa độ tờ = `GetProjectionToSheetTransform().Origin` + tọa độ cục bộ khung cắt / tỉ lệ |
| `ViewSection.CreateSection`: Revit đặt mặt cắt ở `Min.Z`, nhìn theo `+BasisZ` rồi tự lật trục | Muốn cắt tại x nhìn về −x: `BasisX=(0,−1,0)`, `BasisZ=(−1,0,0)`, `Min.Z=0`, `Max.Z=sâu`; đọc lại `ViewDirection`, `RightDirection` |
| View đã nằm trên tờ mẫu của template (A101, A201…) → không đặt được lên tờ mới | Gỡ viewport khỏi tờ mẫu (giữ tờ), báo người dùng |
| Mặt bằng mái trống | View range: đáy và độ sâu nhìn tới tầng áp mái |
| Label (ô chữ tham số) trong family: API không tạo được | Chữ cố định ghi trong family; giá trị từng tờ ghi bằng TextNote theo `tk1.O_GIA_TRI()` |
| Phiên agent không lưu được .rfa, không xuất PDF/DWG | Nhờ người dùng: Edit Family → Save As; in PDF bằng bộ tờ đã tạo |

## 4. Soát trước khi báo xong

- [ ] `capture_view` từng tờ (truyền id tờ). Soát: chữ dim là mm, không chồng chữ, viewport không
      đè khung tên, không có khung thừa, giá trị khung tên đúng.
- [ ] Đếm lại: số tờ, số bảng, số tag phòng = số phòng, tag cửa = số cửa từng tầng.
- [ ] Đối chiếu bảng thống kê với `vn-revit-mcp` (`thong_ke_cua`, `thong_ke_phong`).
- [ ] Báo người dùng: chưa có ô chữ ký (thiết kế, chủ trì, kiểm tra), ghi chú vật liệu, ký hiệu vật
      liệu mặt cắt, cao độ trên mặt bằng; xuất PDF: File → Export → PDF, chọn bộ tờ trong `hs.BO_TO`.
- [ ] Nhắc lưu file. Bản vẽ dựng từ mô hình phải được kiến trúc sư kiểm trước khi phát hành.
