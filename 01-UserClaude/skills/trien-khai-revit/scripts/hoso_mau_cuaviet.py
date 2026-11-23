# -*- coding: utf-8 -*-
# CAU HINH HO SO BAN VE (skill trien-khai-revit) - Truong TH Cua Viet, nha lop hoc 3 tang.
# Don vi: mm mo hinh; mm giay cho kho, khung ten. ASCII only (chu co dau viet bang \u).

# Kho giay: A3 dai 840x297 nhu ban ve goc ('A3 dai' 84000x29700 o TL 1:100).
# Nha dai 56 m, o TL 1:100 khong vua A3 thuong (420).
KHO = {"ten": "A3dai", "rong": 840, "cao": 297, "le_trai": 20, "le": 5}
KHUNG_TEN = {"rong": 180, "cao": 56}          # goc phai phia duoi (CLAUDE.md)
TEN_FAMILY_KHUNG = "VN-KhungTen A3dai"

THONG_TIN = {
    # nguon: to bia ban ve goc '2. Kien truc -CUA VIET.dwg'
    "cong_ty": u"CÔNG TY TNHH NGHĨA ĐẠT",
    "chu_dau_tu": u"UBND xã Cửa Việt",
    "cong_trinh": u"Trường Tiểu học Cửa Việt",
    "hang_muc": u"Nhà lớp học 3 tầng",       # [Can xac nhan lai]: to bia ghi '2 tang 10 phong'
    "dia_diem": u"Xã Cửa Việt, tỉnh Quảng Trị",
    "ngay": "11/2026",
}

# Luoi truc: keo lai cho vua kho giay (mm mo hinh)
TRUC_KEO = {"so": (-3000, 17000), "chu": (-3000, 59500)}
# Khung cat mat bang tren to (mm mo hinh): bao bong truc (ban kinh ~400 o TL 1:100)
KHUNG_MB = (-3600, -3600, 60100, 17600)

# Day kich thuoc tren mat bang (mm mo hinh)
DIM = {
    "duoi_truc": -1300, "duoi_tong": -2000,          # truc so, phia truc A
    "tren_chi_tiet": 15100, "tren_truc": 15700, "tren_tong": 16300,   # phia truc E
    "trai_truc": -1700, "trai_tong": -2300,          # truc chu
    "bo_truc_phu": ["4'", "6'"],                     # truc phu khong dua vao day truc chinh
}

# Mat cat (theo vi tri ky hieu tren MB tang 1 ban goc): nhin ve phia truc 1 (-x)
MAT_CAT = [
    {"ten": u"MẶT CẮT A-A", "x": 32000, "y": (-3000, 17500), "z": (-1500, 17500), "sau": 32000},
    {"ten": u"MẶT CẮT B-B", "x": 20190, "y": (-3000, 17500), "z": (-1500, 17500), "sau": 20000},
]

# Ten hien tren to (Title on Sheet) cua cac view co san
TIEU_DE = {
    u"MB Tầng 1": u"MẶT BẰNG TẦNG 1",
    u"MB Tầng 2": u"MẶT BẰNG TẦNG 2",
    u"MB Tầng 3": u"MẶT BẰNG TẦNG 3",
    u"MB Tầng áp mái": u"MẶT BẰNG TẦNG ÁP MÁI",
    u"MB Đỉnh mái": u"MẶT BẰNG MÁI",
    "South - Architectural": u"MẶT ĐỨNG TRỤC 1-16",
    "North - Architectural": u"MẶT ĐỨNG TRỤC 16-1",
    "East - Architectural": u"MẶT ĐỨNG TRỤC A-E",
    "West - Architectural": u"MẶT ĐỨNG TRỤC E-A",
}
# Mat bang mai: view o cao do dinh mai, nhin xuong toi tang ap mai
MB_MAI = {"view": u"MB Đỉnh mái", "day_toi_tang": u"Tầng áp mái"}
# Mat bang can ghi kich thuoc + tag
MB_GHI_CHU = [u"MB Tầng 1", u"MB Tầng 2", u"MB Tầng 3", u"MB Tầng áp mái"]

# Danh muc to. 'view' = ten view; 'bang' = ten bang thong ke; '3d' = view 3D tao moi.
TO = [
    {"so": "KT-01", "ten": u"MẶT BẰNG TẦNG 1", "view": [u"MB Tầng 1"]},
    {"so": "KT-02", "ten": u"MẶT BẰNG TẦNG 2", "view": [u"MB Tầng 2"]},
    {"so": "KT-03", "ten": u"MẶT BẰNG TẦNG 3", "view": [u"MB Tầng 3"]},
    {"so": "KT-04", "ten": u"MẶT BẰNG TẦNG ÁP MÁI", "view": [u"MB Tầng áp mái"]},
    {"so": "KT-05", "ten": u"MẶT BẰNG MÁI", "view": [u"MB Đỉnh mái"]},
    {"so": "KT-06", "ten": u"MẶT ĐỨNG TRỤC 1-16", "view": ["South - Architectural"]},
    {"so": "KT-07", "ten": u"MẶT ĐỨNG TRỤC 16-1", "view": ["North - Architectural"]},
    {"so": "KT-08", "ten": u"MẶT ĐỨNG TRỤC A-E, E-A", "view": ["East - Architectural", "West - Architectural"]},
    {"so": "KT-09", "ten": u"MẶT CẮT A-A, B-B", "view": [u"MẶT CẮT A-A", u"MẶT CẮT B-B"]},
    {"so": "KT-10", "ten": u"BẢNG THỐNG KÊ CỬA, PHÒNG", "bang": True},
    {"so": "KT-11", "ten": u"PHỐI CẢNH 3D", "3d": u"PHỐI CẢNH 3D"},
]
# Hop bao khoi nha (mm) de cat khung view 3D
HOP_NHA = [(x, y, z) for x in (-1200, 56500) for y in (-300, 15100) for z in (-800, 16100)]
TI_LE = 100
TI_LE_3D = 200
BO_TO = "VN-KT Cua Viet"   # bo to de in PDF
