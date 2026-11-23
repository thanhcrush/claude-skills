"""Giai ma text tieng Viet font cu trong DXF -> Unicode.

Bang VNI-Windows (font VNI-Times, VNI-Helve-Condense...). Hieu chuan tren
ho so that 2625 ABUSA: 243 chuoi, con sot 0 ky tu la sau khi giai ma.

Dung:
    from giai_ma_vni import vn, la_vni
    vn("MAËT BAÈNG DAÀM SAØN LAÀU 1")   -> "MẶT BẰNG DẦM SÀN LẦU 1"

LUU Y quan trong:
  * File DXF co the luu UTF-8 nhung noi dung la VNI. Doc bang
    open(f, 'rb').read().decode('utf-8') truoc, dung decode cp1252.
  * Thay theo thu tu DAI TRUOC NGAN SAU. Neu doi 'Ô'->'Ơ' truoc thi
    'COÂNG' se ra 'CƠNG' thay vi 'CÔNG'.
  * Giu chuoi goc khi truy nguon; ban giai ma chi dung de doc va tim kiem.
"""

# --- to hop 2 ky tu: nguyen am co mu/trang + dau ---
_CAP2 = {
    # a + mu (â)
    "AÂ": "Â", "AÁ": "Ấ", "AÀ": "Ầ", "AÅ": "Ẩ", "AÃ": "Ẫ", "AÄ": "Ậ",
    # a + trang (ă)
    "AÊ": "Ă", "AÉ": "Ắ", "AÈ": "Ằ", "AÚ": "Ẳ", "AÜ": "Ẵ", "AË": "Ặ",
    # a tran
    "AØ": "À", "AÙ": "Á", "AÛ": "Ả", "AÕ": "Ã", "AÏ": "Ạ",
    # e + mu (ê)
    "EÂ": "Ê", "EÁ": "Ế", "EÀ": "Ề", "EÅ": "Ể", "EÃ": "Ễ", "EÄ": "Ệ",
    # e tran
    "EØ": "È", "EÙ": "É", "EÛ": "Ẻ", "EÕ": "Ẽ", "EÏ": "Ẹ",
    # o + mu (ô)
    "OÂ": "Ô", "OÁ": "Ố", "OÀ": "Ồ", "OÅ": "Ổ", "OÃ": "Ỗ", "OÄ": "Ộ",
    # o tran
    "OØ": "Ò", "OÙ": "Ó", "OÛ": "Ỏ", "OÕ": "Õ", "OÏ": "Ọ",
    # o + moc (ơ) — 'Ô' don la 'Ơ', xu ly o _CAP1
    "ÔÙ": "Ớ", "ÔØ": "Ờ", "ÔÛ": "Ở", "ÔÕ": "Ỡ", "ÔÏ": "Ợ",
    # u + moc (ư) — 'Ö' don la 'Ư'
    "ÖÙ": "Ứ", "ÖØ": "Ừ", "ÖÛ": "Ử", "ÖÕ": "Ữ", "ÖÏ": "Ự",
    # u tran
    "UØ": "Ù", "UÙ": "Ú", "UÛ": "Ủ", "UÕ": "Ũ", "UÏ": "Ụ",
    # i tran (mot so ban dung to hop)
    "IØ": "Ì", "IÙ": "Í", "IÛ": "Ỉ", "IÕ": "Ĩ", "IÏ": "Ị",
    # y tran
    "YØ": "Ỳ", "YÙ": "Ý", "YÛ": "Ỷ", "YÕ": "Ỹ", "YÏ": "Ỵ",
}

# --- ky tu don ---
_CAP1 = {
    "Ô": "Ơ", "Ö": "Ư", "Ñ": "Đ",
    "Æ": "Ỉ", "Ò": "Ị", "Ó": "Ĩ", "Ì": "Ì", "Í": "Í",
    "þ": "Ø",          # ky hieu duong kinh thep
}

# sinh ban chu thuong
_CAP2.update({k.lower(): v.lower() for k, v in list(_CAP2.items())})
_CAP1.update({k.lower(): v.lower() for k, v in list(_CAP1.items())})
# rieng 'ò' thuong trong VNI la 'ị', 'ó' la 'ĩ' — da sinh o tren
_CAP1["ñ"] = "đ"
_CAP1["ô"] = "ơ"
_CAP1["ö"] = "ư"

# Quet MOT luot duy nhat, uu tien to hop 2 ky tu.
# Khong dung replace() nhieu lan: 'OÂ'->'Ô' roi 'Ô'->'Ơ' se ra 'CƠNG',
# 'OÙ'->'Ó' roi 'Ó'->'Ĩ' se ra 'CĨ'.
import re as _re

_MAP = {**_CAP2, **_CAP1}
_RX = _re.compile("|".join(_re.escape(k) for k in sorted(_MAP, key=len, reverse=True)))


def vn(s: str) -> str:
    """Giai ma mot chuoi VNI sang Unicode. Chuoi khong phai VNI tra ve nguyen ven."""
    if not s:
        return s
    return _RX.sub(lambda m: _MAP[m.group(0)], s)


# ky tu chi xuat hien trong VNI, khong phai chu Viet hop le.
# 'ø'/'Ø' KHONG nam trong day: sau giai ma chung la ky hieu duong kinh thep.
_LA = set("ÛÏÄÅÆÑÖËÜþûïäåæñöëü")


def la_vni(s: str) -> bool:
    """Doan xem chuoi co phai text VNI chua giai ma khong."""
    return any(c in _LA for c in s)


def con_sot(s: str) -> str:
    """Tra ve cac ky tu la con lai sau khi giai ma — dung de kiem bang ma."""
    return "".join(c for c in vn(s) if c in _LA)


if __name__ == "__main__":
    mau = [
        "MAËT BAÈNG DAÀM SAØN LAÀU 1",
        "THOÁNG KEÂ THEÙP MOÙNG",
        "ÑAØ KIEÀNG",
        "TÖÔØNG 20CM XAÂY GAÏCH OÁNG 4 LOÃ",
        "PHAÛI COÙ SÖÏ PHOÁI HÔÏP CHAËT CHEÕ CAÙC BAÛN VEÕ THI COÂNG",
        "(TRÖØ VÒ TRÍ COÙ CHÆ ÑÒNH RIEÂNG)",
        "Boá trí theùp ñai þ6a100 ñoaïn L/4 ôû chaân coät",
    ]
    for m in mau:
        print(f"{m}\n  -> {vn(m)}\n")
