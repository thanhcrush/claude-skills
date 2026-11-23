# BẢNG MÃ VNI-WINDOWS → UNICODE

Text tiếng Việt trong DXF Việt Nam hiện ra dạng `MAËT BAÈNG DAÀM SAØN LAÀU 1` là **VNI-Windows**, không phải TCVN3 — tài liệu cũ gọi nhầm tên. Nhận ra qua tên font trong MTEXT: `VNI-Times`, `VNI-Helve-Condense`, `VNI-Univer`.

Dùng `scripts/giai_ma_vni.py`. Bảng dưới đây đã hiệu chuẩn trên hồ sơ thật: **0 ký tự sót** trên 275 chuỗi của 2625 (ABUSA) và 2614.

## Ba bẫy phải tránh khi tự viết lại

1. **File lưu UTF-8 nhưng nội dung là VNI.** Đọc bằng `open(f,'rb').read().decode('utf-8')`. Decode cp1252 sẽ ra `MAÃ‹T BAÃˆNG` — double-encode, không giải mã được nữa.
2. **Quét một lượt duy nhất.** Không dùng `str.replace()` lần lượt: thay `OÂ`→`Ô` rồi thay tiếp `Ô`→`Ơ` biến `COÂNG` thành `CƠNG`; `COÙ`→`CÓ`→`CĨ`. Dùng một `re.sub` với alternation sắp theo độ dài giảm dần.
3. **Phải có cả chữ thường.** Ghi chú kỹ thuật hay viết thường: `Boá trí theùp ñai þ6a100 ñoaïn L/4 ôû chaân coät`.

## Ký tự dấu

| Ký tự | Dấu |
|---|---|
| `Ù` | sắc |
| `Ø` | huyền |
| `Û` | hỏi |
| `Õ` | ngã |
| `Ï` | nặng |

## Nguyên âm có mũ, có móc và ký tự riêng

| VNI | Unicode | VNI | Unicode |
|---|---|---|---|
| `AÂ` | Â | `AÊ` | Ă |
| `EÂ` | Ê | `OÂ` | Ô |
| `Ô` | Ơ | `Ö` | Ư |
| `Ñ` | Đ | `þ` | Ø — ký hiệu đường kính thép, giữ nguyên |

## Bảng đầy đủ — chữ hoa

```
a tròn   AØ→À  AÙ→Á  AÛ→Ả  AÕ→Ã  AÏ→Ạ
â        AÂ→Â  AÁ→Ấ  AÀ→Ầ  AÅ→Ẩ  AÃ→Ẫ  AÄ→Ậ
ă        AÊ→Ă  AÉ→Ắ  AÈ→Ằ  AÚ→Ẳ  AÜ→Ẵ  AË→Ặ
e tròn   EØ→È  EÙ→É  EÛ→Ẻ  EÕ→Ẽ  EÏ→Ẹ
ê        EÂ→Ê  EÁ→Ế  EÀ→Ề  EÅ→Ể  EÃ→Ễ  EÄ→Ệ
o tròn   OØ→Ò  OÙ→Ó  OÛ→Ỏ  OÕ→Õ  OÏ→Ọ
ô        OÂ→Ô  OÁ→Ố  OÀ→Ồ  OÅ→Ổ  OÃ→Ỗ  OÄ→Ộ
ơ        Ô→Ơ   ÔÙ→Ớ  ÔØ→Ờ  ÔÛ→Ở  ÔÕ→Ỡ  ÔÏ→Ợ
u tròn   UØ→Ù  UÙ→Ú  UÛ→Ủ  UÕ→Ũ  UÏ→Ụ
ư        Ö→Ư   ÖÙ→Ứ  ÖØ→Ừ  ÖÛ→Ử  ÖÕ→Ữ  ÖÏ→Ự
i        Ì→Ì   Í→Í   Æ→Ỉ   Ó→Ĩ   Ò→Ị
         IØ→Ì  IÙ→Í  IÛ→Ỉ  IÕ→Ĩ  IÏ→Ị
y        YØ→Ỳ  YÙ→Ý  YÛ→Ỷ  YÕ→Ỹ  YÏ→Ỵ
đ        Ñ→Đ
```

Chữ thường sinh tự động bằng `.lower()` cả khoá lẫn giá trị.

## Ba lỗi của bảng mã cũ

| Sai | Đúng | Hậu quả |
|---|---|---|
| thiếu hẳn `AØ` | `AØ`→À | `SAØN` giữ nguyên `SAØN`, sót **92 lần** trong một file |
| `AÀ`→À | `AÀ`→**Ầ** | `DAÀM`→`DÀM` thay vì `DẦM` |
| `AÁ`→Ắ | `AÁ`→**Ấ** | `KEÁT CAÁU`→`KẾT CẮU` thay vì `KẾT CẤU` |

## Mở ra được gì

Giải mã xong lấy được ngay, khỏi đọc ảnh từng tờ:

- tên và số hiệu từng tờ từ khung tên (anchor `"TÊN BẢN VẼ"`, `"TỜ"`);
- ký hiệu tiết diện `[250x500]`, chiều dài ghi sẵn `L=5900MM`;
- ghi chú chung: mác bê tông từng bộ phận, mác vữa xây và tô, loại thép, chiều dày sàn;
- bảng thống kê cửa, bảng thống kê thép.

Chuẩn hoá để tìm kiếm nhưng **giữ chuỗi gốc khi truy nguồn** — người dò lại trên CAD sẽ thấy chuỗi gốc, không thấy bản đã giải mã.
