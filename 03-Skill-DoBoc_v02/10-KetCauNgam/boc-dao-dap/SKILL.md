---
name: boc-dao-dap
description: Bóc khối lượng đào đắp đất và bê tông lót — đào hố móng, đào rãnh giằng, hố đào gộp, đào mái dốc, đắp đất hoàn trả hố móng, đắp cát hoặc đất tôn nền, vận chuyển đất thừa, bê tông lót móng, lót giằng, lót nền. Dùng skill này khi người dùng nói bóc đào đất, đắp đất, đào móng, lấp móng, tôn nền, san nền trong phạm vi nhà, bê tông lót, vận chuyển đất, hoặc kiểm lại khối lượng đất. Tính theo kích thước thiết kế và Phụ lục VI TT 13/2021, không cộng độ nở rời; các thông số biện pháp (mái dốc, mở rộng đáy hố, tỷ lệ đào máy) phải có nguồn, không tự chọn. Ghi vào sheet 6.2-02DaoDap. Không dùng cho bê tông móng, giằng, cổ cột — những cái đó có skill riêng.
---

# Bóc đào đắp và bê tông lót

**Đọc `do-boc-loi` trước**, đặc biệt mục 5 — cặp "Bê tông ↔ Ván khuôn ↔ Cốt thép ↔ Lót ↔ Đào đắp".

Bộ skill gốc không có skill này vì phần mềm dtPro tự sinh đào đất và lót từ kích thước móng cộng "sâu đào". Bóc trên Excel thì phải làm tay, và đây là hạng mục **nhiều thông số biện pháp nhất** — chỗ dễ tự chế số nhất.

## 1. Thứ tự — làm SAU khi đã chốt móng, giằng, cổ cột

Đào đắp phụ thuộc hình học của móng, giằng, cổ cột, bể ngầm. Chỉ bóc khi `boc-mong`, `boc-dam-mong`, `boc-co-cot-vach-pit` đã xong và đã qua gate. Sửa móng thì **phải bóc lại** phần đất liên quan.

## 2. Nguồn và vai trò

| Nguồn | Cho ra |
|---|---|
| Mặt cắt, chi tiết móng | kích thước và chiều dày **lót**, cao độ đáy lót, mác lót |
| Mặt bằng hiện trạng / khảo sát địa hình, ghi chú chung | **cốt tự nhiên** so với ±0.000 |
| Báo cáo khảo sát địa chất | **cấp đất** từng lớp, mực nước ngầm |
| Thuyết minh / biện pháp thi công / hồ sơ mời thầu | mái dốc hố đào, mở rộng đáy hố, đào máy hay thủ công (tỷ lệ), độ chặt K, cự ly vận chuyển, nơi đổ đất |
| Mặt bằng nền trệt, mặt cắt nhà | phạm vi tôn nền, chiều dày lớp nền, cao độ đáy kết cấu nền |
| Kết quả `boc-mong`, `boc-dam-mong`, `boc-co-cot-vach-pit` | thể tích chiếm chỗ dưới mặt đất |

**Thông số biện pháp — thứ tự ưu tiên** (anh Thành chốt 09/10/2026):

1. Hồ sơ dự án quy định (thuyết minh, biện pháp thi công, hồ sơ mời thầu) → dùng số của dự án.
2. Không có → dùng **thông số mặc định của công ty** trong bảng dưới, diễn giải ghi "mặc định công ty", trạng thái **S**.
3. Trường hợp nằm ngoài phạm vi bảng mặc định (sâu > 5 m, dưới mực nước ngầm không tiêu nước, sát công trình lân cận) → hỏi anh Thành, không tự đặt số.

Bộ mặc định dưới đây được anh Thành duyệt ngày 09/10/2026. Phần lấy từ **TCVN 4447:2012 Công tác đất — Thi công và nghiệm thu** (đọc tại qlda.gxd.vn ngày 09/10/2026, **kiểm tra lại hiệu lực**); phần không có trong TCVN là quy ước của công ty, ghi rõ bên dưới.

**① Mái dốc hố đào** — TCVN 4447:2012, điều 4.2.5 (Bảng 10) và 4.2.9 (Bảng 11):

| Loại đất | Đào thẳng đứng khi sâu ≤ (Bảng 10) | Sâu ≤ 1,5 m | Sâu ≤ 3,0 m | Sâu ≤ 5,0 m |
|---|---|---|---|---|
| Đất mượn (bãi thải > 6 tháng, không đầm) | — | 1 : 0,67 | 1 : 1,00 | 1 : 1,25 |
| Đất cát, cát cuội ẩm, đất lẫn sỏi sạn | 1,00 m | 1 : 0,50 | 1 : 1,00 | 1 : 1,00 |
| Đất cát pha | 1,25 m | 1 : 0,25 | 1 : 0,67 | 1 : 0,85 |
| Đất thịt | 1,50 m | 1 : 0 | 1 : 0,50 | 1 : 0,75 |
| Đất sét | 1,50 m (sét chắc 2,00 m) | 1 : 0 | 1 : 0,25 | 1 : 0,50 |
| Hoàng thổ khô và tương tự | — | 1 : 0 | 1 : 0,50 | 1 : 0,50 |

- Sâu ≤ giá trị Bảng 10 (đất mềm, trên mực nước ngầm, không có công trình ngầm lân cận) → **đào thẳng đứng**, m = 0. Sâu hơn → hệ số mái theo Bảng 11, lấy **mức chiều sâu kế trên** (VD sâu 2,1 m → cột ≤ 3,0 m).
- Hố qua nhiều lớp đất → lấy loại đất **yếu nhất** (chú thích 1 Bảng 11).
- Loại đất đọc từ báo cáo khảo sát địa chất; cấp đất theo định mức (I–IV) là chuyện khác, dùng để chọn mã đào.
- Bảng 11 áp dụng trên mực nước ngầm, hoặc dưới mực nước ngầm nhưng có tiêu nước. Sâu > 5 m → biện pháp riêng, hỏi.

**② Mở rộng đáy hố** — TCVN 4447:2012, điều 4.2.3:

- Mặc định **0,3 m mỗi bên, tính từ mép ngoài lớp lót** (hố có mái dốc: khoảng cách chân mái dốc đến chân kết cấu ≥ 0,3 m; hố vách đứng: tối thiểu kết cấu + ván khuôn, neo + 0,2 m — công ty lấy chung 0,3 m).
- Có công nhân làm việc trong khe giữa kết cấu và vách đứng (xây móng gạch, chống thấm mặt ngoài) → **0,7 m**.

**③ Tỷ lệ đào máy / thủ công** — quy ước công ty dựa trên TCVN 4447:2012, điều 4.2.18 (Bảng 13):

- **Đào máy** đến cách đáy thiết kế một **lớp bảo vệ**; **lớp bảo vệ đào thủ công** (sửa đáy móng). Khối lượng thủ công = diện tích đáy hố × chiều dày lớp bảo vệ; còn lại là đào máy.
- Chiều dày lớp bảo vệ mặc định **0,10 m** (máy đào gầu sấp 0,25–0,40 m³, Bảng 13). Biện pháp dùng máy khác thì tra lại Bảng 13.
- Hố, rãnh **máy không vào được** (mặt bằng chật, nhà liền kề, cải tạo trong nhà, rãnh hẹp hơn gầu) → **đào thủ công toàn bộ**, ghi lý do trong diễn giải.

**④ Cự ly vận chuyển đất** — quy ước công ty (TCVN không quy định):

- Đất đào giữ lại để lấp hoàn trả và tôn nền; chỉ **đất thừa** mới vận chuyển.
- Chưa có bãi đổ cụ thể → **tạm tính cự ly ≤ 1 km**, trạng thái **T**, ghi vào `00-DanhSachCanKiem.md`. Có bãi đổ thực tế → tính theo cự ly thật (phần ≤ 1 km và phần vượt theo cách chia của định mức).

Giá trị mặc định chép sang sheet `00-ThongTin` của từng sổ khối lượng.

## 3. Nguyên tắc từ PL VI TT 13/2021 (mục Đào, đắp)

- Đào phân theo **cấp đất đá, độ sâu, bề rộng hố, thủ công hay cơ giới**. Đắp phân theo **vật liệu, cấp đất, chiều dày lớp, độ chặt K**.
- Tính theo **kích thước thiết kế**, **không cộng** độ nở rời, co ngót, hao hụt.
- Lấy đất đào để đắp: `KL đào cần = KL đắp × hệ số chuyển đổi`. Mua đất rời để đắp: `KL đất rời = KL đắp × hệ số tơi xốp`. Hệ số tra theo định mức / thiết kế — `[Cần xác nhận lại]`, không tự chọn.
- **Trừ** công trình ngầm chiếm chỗ (ống, cống) khi tính đắp.
- Đất, đá khác cấp: khối < 1 m³ thì không tách riêng.
- Móng sâu, nền yếu: ghi rõ biện pháp (cừ chống sạt, bơm nước).

## 4. Bê tông lót

- Kích thước lót **đọc từ chi tiết** — thường rộng hơn móng mỗi bên, nhưng **không mặc định 100 mm**. Chi tiết không ghi → T, ghi cần kiểm.
- Tách công tác theo **mác và vị trí**: lót móng · lót giằng · lót đáy bể, hố ga, pit · lót nền.
- `V lót = dài lót × rộng lót × dày lót` từng loại móng × số móng. Giằng: dài lót theo **chiều dài thông thủy giữa các lót móng** — không chồng lên lót móng.
- Lót nền (bê tông gạch vỡ, đá 4x6, bê tông mác thấp dưới sàn nền) là công tác nền, tách dòng.
- Ván khuôn lót: chỉ tính khi bản vẽ hoặc biện pháp có — mặc định không.

## 5. Đào hố móng

**Kích thước đáy hố** = kích thước lót + mở rộng thao tác mỗi bên (theo biện pháp). **Kích thước miệng hố** = đáy + 2 × m × H (m = hệ số mái dốc, H = chiều sâu đào). Chiều sâu đào = **cốt tự nhiên → đáy lót** (không phải cốt nền ±0.000).

Hố hình lăng trụ cụt (đáy a × b, miệng c × d, sâu H):

```
V = H / 6 × [a·b + (a + c)(b + d) + c·d]
```

Ghi vào sổ bằng công thức Excel ở ô KL một bộ phận (trong code Python viết dấu chấm thập phân: `kl1="=1.6/6*(2.1*2.1+(2.1+3.7)*(2.1+3.7)+3.7*3.7)"`) để kiểm được; diễn giải ghi đủ a, b, c, d, H bằng dấu phẩy thập phân và nguồn từng số.

### Hố đào gộp — chỗ tính trùng lớn nhất

Hai hố cạnh nhau mà **miệng hố chồng lên nhau** thì cộng hai lăng trụ là **tính trùng phần giao**. Kiểm từng cặp hố liền kề:

```
khoảng cách mép đáy hai hố  <  m × H₁ + m × H₂   →   miệng chồng nhau → đào gộp
```

Đào gộp: tính **một hố chung** bao các móng (hoặc đào băng theo tuyến), không cộng từng hố. Nhà phố móng sát nhau, đài cọc dày đặc → thường gộp toàn bộ hoặc theo dải. Vẽ phác mặt bằng miệng hố ở sổ nội bộ để chứng minh.

### Rãnh giằng

Đào rãnh giằng dài **thông thủy giữa các hố móng** — phần nằm trong hố móng đã đào rồi, không tính lại. Chiều sâu = cốt tự nhiên → đáy lót giằng.

### Tách theo cấp đất và biện pháp

- Hố cắt qua nhiều lớp đất khác cấp → tách khối lượng theo chiều dày từng lớp (khối khác cấp < 1 m³ thì gộp).
- Đào máy / thủ công theo **tỷ lệ của biện pháp hoặc hồ sơ mời thầu** — không có thì `[Chờ bổ sung]`, không tự đặt tỷ lệ.
- Có nước ngầm trong phạm vi đào → ghi công tác bơm nước hố móng `[Chờ bổ sung]`.

## 6. Đắp

**Đắp hoàn trả hố móng:**

```
V đắp = V đào − V chiếm chỗ (lót + móng + cổ cột + giằng + bể ngầm … phần nằm DƯỚI cao độ mặt đắp)
```

Chỉ trừ phần cấu kiện nằm **dưới mặt đắp**. Cổ cột nhô lên trên mặt đắp thì phần nhô không trừ.

**Tôn nền trong nhà:** diện tích nền **thông thủy trong tường/giằng** × chiều dày từ mặt đất sau khi lấp hố → đáy lớp kết cấu nền. Tách theo vật liệu (cát, đất) và độ chặt K. Nền nhiều cao độ (hạ cốt WC, sân, hiên) → tách vùng.

**Vận chuyển đất:** đất thừa = V đào − V đất đào dùng lại để đắp (đã quy đổi hệ số). Cự ly, phương tiện theo biện pháp `[Chờ bổ sung]`. Đất mua về để đắp tính riêng theo hệ số tơi xốp.

## 7. Ghi sổ khối lượng

Sheet `6.2-02DaoDap`. Thứ tự công tác: đào hố móng (máy / thủ công, theo cấp đất) → đào rãnh giằng → bê tông lót móng → lót giằng → (lót nền) → đắp hoàn trả → tôn nền → vận chuyển đất thừa.

- Dòng chi tiết theo **loại móng** (VD `Hố móng M1 — 8 hố`) hoặc theo **hố gộp** (`Hố gộp trục A-B/1-3`).
- Số bộ phận giống nhau = số hố cùng kích thước.
- Đắp hoàn trả: một dòng V đào (công thức trỏ sang dòng công tác đào), các dòng **trừ** từng cấu kiện chiếm chỗ (số bộ phận âm, trỏ thể tích từ sheet móng/giằng hoặc ghi lại kích thước).
- Mọi thông số biện pháp dùng trong diễn giải phải trùng giá trị ở `00-ThongTin`.

## 8. Gate chốt — chưa đạt thì chưa giao

- [ ] Móng, giằng, cổ cột đã chốt trước khi bóc đất; có ghi bản bóc móng làm căn cứ.
- [ ] Chiều sâu đào tính từ **cốt tự nhiên**, không từ cốt ±0.000; cốt tự nhiên có nguồn.
- [ ] Kích thước lót đọc từ chi tiết, không mặc định.
- [ ] Mái dốc, mở rộng đáy, tỷ lệ máy/thủ công, cự ly vận chuyển: **có nguồn** hoặc gắn `[Chờ bổ sung]` / T — không tự chế.
- [ ] Đã kiểm **hố đào gộp** cho từng cặp hố liền kề; không cộng chồng lăng trụ.
- [ ] Rãnh giằng tính thông thủy giữa các hố móng.
- [ ] Đã tách theo cấp đất; cấp đất có nguồn (báo cáo khảo sát).
- [ ] **Không cộng độ nở rời, co ngót, hao hụt** vào khối lượng.
- [ ] Đắp hoàn trả đã trừ đủ cấu kiện chiếm chỗ dưới mặt đắp, không trừ phần nhô lên.
- [ ] Tôn nền tính thông thủy trong tường/giằng, tách vùng khác cao độ.
- [ ] Lót giằng không chồng lót móng.
- [ ] Mọi T/N có mục trong `00-DanhSachCanKiem.md` kèm biên độ ảnh hưởng.
