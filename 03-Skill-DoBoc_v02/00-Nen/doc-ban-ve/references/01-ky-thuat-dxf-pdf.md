# KỸ THUẬT ĐỌC BẢN VẼ VIỆT NAM — DXF / DWG / PDF

Tất cả cách làm dưới đây đã kiểm chứng trên hồ sơ thật của các đơn vị thiết kế Việt Nam (ABUSA, AI Design, Thái Ngọc Quốc, Vinaduy…).

---

## 1. Mở file

```python
import ezdxf
doc = ezdxf.readfile("BAN VE.dxf")   # AC1021…AC1032 đều đọc được
msp = doc.modelspace()
```

- `.dwg` **không đọc trực tiếp** — xin khách xuất `.dxf`, hoặc convert bằng ODA/LibreDWG trên máy thật.
- DXF Việt Nam hay có **lỗi binary (hex lẻ)** chặn ezdxf → parse thô section `ENTITIES` lấy `INSERT(2,10,20)` / `TEXT(1,10,20)`.
- File `.xlsx`/`.xls` kết quả bị Excel khoá (đang mở) → ghi ra tên mới `-v02`, đừng cố ghi đè.

## 2. Bung block — bước bắt buộc, bỏ là mất gần hết nét

Nội dung bản vẽ Việt Nam gần như **luôn nằm trong block**. `msp.query('LINE')` chỉ trả về vài chục entity trong khi thực tế có hàng chục nghìn.

```python
def walk(container, depth=0, parent_layer=None):
    for e in container:
        lay = e.dxf.layer
        if lay == "0" and parent_layer:      # ← QUAN TRỌNG
            lay = parent_layer               # entity con layer '0' kế thừa layer của INSERT cha
        if e.dxftype() == "INSERT":
            for a in e.attribs:              # đừng bỏ ATTRIB — chứa số liệu bảng thống kê
                thu_attrib(e.dxf.name, a.dxf.tag, a.dxf.text, e.dxf.insert)
            if depth < 6:
                walk(list(e.virtual_entities()), depth+1, lay)
        else:
            emit(e, lay)
```

Ở 2611, sửa đúng chỗ kế thừa layer làm số segment tăng **35.000 → 315.000**.

## 3. Lập bản đồ view — trước khi đo bất cứ thứ gì

Model space chứa **tất cả các tờ xếp cạnh nhau**. Phải biết đang đọc tờ nào.

Ba cách, dùng kết hợp:

1. **Khung tên là block chèn nhiều lần** (2611: `GHTFYR` 60682×42000). Lấy bbox từng lần chèn = một tờ.
2. **Số hiệu tờ là TEXT cao bất thường** (2625: height 4288, giá trị `'01'`…`'51'`), đặt ở góc trên-trái mỗi tờ. Gom theo cột x → hàng y để dựng lưới tờ.
3. **Tên view là TEXT trên một layer riêng** (2625: layer `A - COT`, height 444) đặt **dưới** hình.

Xong thì gán mỗi entity vào một tờ, và **kiểm lại bằng cách render một tờ** để chắc chắn.

⚠ **Cùng một tên mặt cắt có thể vẽ ở 2 tờ với kích thước khác nhau** (2625: MC 6-6 ở KC-09 H=900 và KC-10 H=1000). Gán theo **tờ chứa hình bằng tương ứng**, không gán theo tên.

## 4. Giải mã text tiếng Việt lỗi font — mã VNI

Text hiện ra dạng `MAËT BAÈNG DAÀM SAØN LAÀU 1 COTE +3.950` là **VNI-Windows**, không phải TCVN3 (tài liệu cũ gọi nhầm tên). Nhận ra qua tên font trong MTEXT: `VNI-Times`, `VNI-Helve-Condense`.

**Giải mã được 100 %.** Dùng `scripts/giai_ma_vni.py`, bảng đầy đủ ở `references/03-bang-ma-vni.md`.

```python
from giai_ma_vni import vn, la_vni
vn("MAËT BAÈNG DAÀM SAØN LAÀU 1")   # -> "MẶT BẰNG DẦM SÀN LẦU 1"
```

Ba cái bẫy đã trả giá, bảng mã cũ sai cả ba:

1. **File lưu UTF-8 nhưng nội dung là VNI.** Phải `open(f,'rb').read().decode('utf-8')`. Decode bằng cp1252 ra `MAÃ‹T BAÃˆNG` — double-encode, không giải mã được.
2. **Quét một lượt duy nhất, không `replace()` nhiều lần.** Thay `OÂ`→`Ô` rồi thay tiếp `Ô`→`Ơ` sẽ biến `COÂNG` thành `CƠNG`; tương tự `COÙ`→`CÓ`→`CĨ`. Dùng một `re.sub` với alternation sắp theo độ dài giảm dần.
3. **Bảng phải có cả chữ thường.** Ghi chú kỹ thuật hay viết thường: `Boá trí theùp ñai þ6a100 ñoaïn L/4 ôû chaân coät`.

Bảng cũ còn sai ba chỗ: thiếu hẳn `AØ`→`À` (sót 92 lần trong một file), map `AÀ`→`À` trong khi đúng là `Ầ`, map `AÁ`→`Ắ` trong khi đúng là `Ấ`.

Giải mã xong mở ra rất nhiều: tên và số hiệu từng tờ từ khung tên, ký hiệu tiết diện `[250x500]`, chiều dài ghi sẵn `L=5900MM`, ghi chú mác bê tông và vữa, cả bảng thống kê cửa — khỏi phải đọc ảnh từng tờ.

Chuẩn hoá để tìm kiếm nhưng **giữ chuỗi gốc khi truy nguồn**.

## 5. Lấy số từ DIMENSION — nhanh hơn đọc ảnh

```python
for e in msp.query('DIMENSION'):
    pt = e.dxf.text_midpoint          # vị trí, để biết dim thuộc hình nào
    m  = e.get_measurement()          # giá trị đo
```

Lọc theo vùng của một view rồi in tập giá trị — thường thấy ngay cao tầng, cao tường, cao lan can, cao cửa. (2625: tập DIM của 2 mặt cắt cho ra `4000, 3600, 3150, 1100, 450, 2800` → chốt được cao tầng, cao tường, cao lan can, cao dầm mà không cần đo hình.)

⚠ **Đường gióng kích thước có thể thuộc cấu kiện khác.** 2625 M8/M9: số 850 là của giằng chạy qua, đài thật 750. Phải đo Δ giữa 2 đường bao bê tông và kiểm hệ số vẽ chi tiết (bản vẽ chi tiết có thể phóng 4×).

⚠ **Mặt cắt móng cọc có 2–3 bracket cùng gốc đo.** 2614: `1100 / 1500 / 1600` đều đo từ mốc `-2.000` nhưng là các mốc khác nhau (đầu cọc, đáy đài, đỉnh đài). Tự đọc dễ nhầm bracket nào là chiều cao chính — phải render mặt cắt và nhìn, hoặc hỏi.

## 6. Đo hình học từ nét vẽ

### 6.1 Ghép cặp đường song song — dùng cho DẦM và Ô SÀN

Lọc LINE theo layer → tách ngang/dọc → gom theo toạ độ cố định → ghép các cặp cách nhau **đúng bề rộng cấu kiện** → lấy đoạn **chồng lấn** làm chiều dài.

Vì nét bị ngắt tại cột nên chiều dài thu được **đã tự động trừ giao cột** — không phải L tim-tim. Khử trùng bằng key `(hướng, bề rộng, tim, đầu, cuối)` làm tròn thô.

**Cảnh báo:** cặp đường 200 mm có thể là tường / gờ / ô văng chứ không phải dầm. Phải giới hạn phạm vi trong lưới nhà và kiểm mật độ (dầm 0,7–0,9 m/m² sàn).

### 6.2 Cách này KHÔNG ĐỦ TIN CHO TƯỜNG

Bản vẽ kiến trúc vẽ tường không nhất quán:
- Hai mép của cùng một bức nằm ở **hai layer khác nhau** (`A-TUONG 0.5` và `A-NETMANH 0.1`), có đoạn ở `A-NET LAN CAN`.
- Có chỗ **3 đường song song sát nhau** (cách 50–150 mm) → ghép cặp ra kết quả vô nghĩa.
- Bề rộng thực tế giữa các đường dọc liên tiếp: 50 / 100 / 150 / 200 / 500 — không có quy luật.

2625 từng ra **0,51 m cho một bức tường dài 7 m**. Cách đúng cho tường: xem skill `boc-tuong-cua-lanh-to`.

### 6.3 Tách ô sàn bằng raster

```
rasterise tuyến dầm (20 mm/px)
→ binary_closing kernel ~14 px          # bịt khe hở tại cột
→ ndimage.label vùng trống
→ loại vùng chạm biên
```
Mỗi vùng còn lại = 1 ô sàn, diện tích = số điểm ảnh (đúng cả với ô không vuông vắn). **Không đóng khe trước khi flood-fill thì rò ra ngoài, thiếu ~10 %.**

`polygonize` của shapely **luôn thất bại** — nét không khép mạch. Đừng thử lại.

### 6.4 Diện tích phòng lọt lòng

Rasterize nét các layer tường/kính/cửa 1 px = 20 mm → `ndimage.label` vùng trống → erosion 17 px làm marker → `watershed_ift` theo distance transform (cắt eo tại khe cửa) → diện tích vùng. Vùng kín = tin; vùng chạm biên = cờ cam. Rò trong/ngoài qua vách kính → vẽ thêm cutline theo mép bao nhà lấy từ dim.

### 6.5 Diện tích lát sàn — cái này AUTO được chính xác

Hatch pattern lát phủ **đúng** vùng lát. Trong DXF kiến trúc, các view lát sàn xếp thành một hàng; mỗi tầng một view. Pattern `NET` = gạch, `DOTS` = đá cubic, `WOOD`/`BOARDW` = gỗ công nghiệp.

Đo area hatch từng pattern **trong đúng hàng view lát** — đừng gộp hàng view trần/vật dụng, trùng pattern sẽ đếm hai lần. Render một view để xác nhận đúng tầng. (2624: 436,4 m², khớp ước 436.)

## 7. Trích bảng thống kê thép từ block

Đơn vị TK dùng tool thống kê thép: mỗi thanh = 1 INSERT block `TK_2/3/6/9/14` có ATTRIB (stt, kích thước móc, Ø, L 1 thanh, SL/CK, tổng SL, tổng md, kg). Cuối mỗi cấu kiện có block `CTK_THKL` / `CTK_THKL2` với attrib dạng `%%c18: 66.8` = **tổng kg theo Ø, đã nhân SL cấu kiện**.

Cách làm: lọc INSERT tên `TK_*`/`CTK_*` → gom nhóm theo cột x → cắt nhóm tại mỗi `CTK` → match nhãn TEXT theo dải y (nhãn có thể **lệch cột** với bảng) → parse `%%c<Ø>: <kg>`.

Kiểm chéo: kg/m² sàn 10–12. Trùng tên cấu kiện giữa các khu (`DM-1` móng ≠ `DM-1` mái) phân biệt bằng vị trí y. Luôn đối chiếu **ngày bản vẽ DXF vs PDF** trước khi tin.

## 8. Đếm cấu kiện (cọc, cột, đài)

**Phải đối chiếu HAI nguồn:** đếm **ký hiệu vẽ** (block/circle) và **số hiệu đánh** (TEXT `C-\d+`). Lệch nhau thì phải truy, đừng vội kết luận theo một phía.

- 2611: block cọc = 84, số hiệu chỉ đánh C-1…C-78. 6 ký hiệu lệch **giống hệt cọc và có đường kích thước dóng tới** → là cọc thật, bên TK sót số. Số đúng = 84.
- 2625: DXF có **lỗi nhân bản gương** — 27/69 vòng tròn ký hiệu cọc bị đẩy sang vùng x dương ngoài bản vẽ, thêm 138 block ở vùng rác x ≈ −4,9 triệu. Đếm circle ra 42 (thiếu) hoặc 86/138 (thừa). **Phải đếm ký hiệu tim cọc rồi kiểm chéo bằng Σ(đài × cọc/đài).**
- Loại ký hiệu **legend** (xếp dọc, lệch khỏi footprint) và ký hiệu ở **mặt cắt**.
- **KHÔNG đếm bằng vision** (Hough nhiễu, 2611 sai 13–26 cái).
- Mẹo: ký hiệu `DC-n` thường có **n = số cọc trong đài** → đối chiếu nhanh tổng cọc (2614 khớp 151).

## 9. Đọc PDF

- Text vector: `pdftotext -layout` — nhưng **không tin** khi bảng xoay hoặc nhiều cột (trộn cột).
- PDF **mã hoá RC4** vẫn trích được bằng `pdftotext`/`pdftoppm`, không cần phá mã.
- Nội dung chính hay bị **xoay 90°** trong khi khung tên không xoay → `pdftotext` chỉ ra được khung tên. Phần nội dung phải render ảnh + `rotate(-90)` rồi đọc bằng mắt.
- Bảng thép Việt Nam trong PDF hay xoay 90° + chữ đảo → bóc bằng **toạ độ từ**, tự nhận hướng, dò scale theo header; rồi kiểm bằng vật lý (kg/m²).
- Text bị nén mất (một số bản export) → chỉ còn cách render.
- Chữ tiếng Việt font SHX có thể thành ô vuông khi render — **số đo vẫn đúng**.
- Text-thành-nét (đã explode) vẫn đo được bằng `page.get_drawings()` + pattern trục + dò scale (2614: 50,74 mm/pt).

## 10. Render để nhìn — cách làm tiết kiệm

Tự viết renderer bằng PIL thay vì dùng backend matplotlib: kiểm soát được layer nào hiện, màu theo layer, và **vẽ thêm thước 1000 mm + nhãn trục** lên ảnh. Có thước thì đọc được vị trí bằng mắt và đối chiếu ngay với số đo từ vector.

Màu quy ước dùng lại được: tường đen dày · cột đỏ · nét mảnh/kính xanh dương · nét thấy xanh lá · lan can cam · trục hồng nhạt · thước xanh dương.

Độ phân giải: mặt bằng nhà 15×14 m ở **0,085 px/mm** (~1500 px) là đủ đọc layout; dải trục cần **0,45 px/mm**.
