# ---------------- kiem tra du lieu (theo skill ve-revit) ----------------
KHOANG_HO_CUA_MM = 152.4
SAI_SO_MM = 1.0


def _len(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def _along(wall, point):
    a, b = wall["tu"], wall["den"]
    length = _len(a, b)
    ux, uy = (b[0] - a[0]) / float(length), (b[1] - a[1]) / float(length)
    dx, dy = point[0] - a[0], point[1] - a[1]
    return dx * ux + dy * uy, abs(dx * uy - dy * ux)


def _diem_noi(wall, walls):
    length = _len(wall["tu"], wall["den"])
    positions = [0.0, length]
    for other in walls:
        if other is wall or other["tang"] != wall["tang"]:
            continue
        for end in (other["tu"], other["den"]):
            s, off = _along(wall, end)
            if off <= SAI_SO_MM and SAI_SO_MM < s < length - SAI_SO_MM:
                positions.append(s)
    return positions


def kiem_tra():
    loi = []
    keys = [k for k, _, _ in TANG]
    elev = [z for _, _, z in TANG]
    if elev != sorted(elev):
        loi.append("TANG: cao do chua tang dan")
    walls = {}
    for w in TUONG:
        if w["ten"] in walls:
            loi.append("TUONG %s: trung ten" % w["ten"])
        walls[w["ten"]] = w
        if _len(w["tu"], w["den"]) <= SAI_SO_MM:
            loi.append("TUONG %s: dai bang 0" % w["ten"])
        if w["tang"] not in keys:
            loi.append("TUONG %s: khong co tang %s" % (w["ten"], w["tang"]))
        if w.get("den_tang"):
            if w["den_tang"] not in keys:
                loi.append("TUONG %s: khong co tang %s" % (w["ten"], w["den_tang"]))
            elif keys.index(w["den_tang"]) <= keys.index(w["tang"]):
                loi.append("TUONG %s: tang tren khong cao hon tang duoi" % w["ten"])
        elif not w.get("cao"):
            loi.append("TUONG %s: thieu den_tang va cao" % w["ten"])
    for c in CUA:
        w = walls.get(c["tuong"])
        if w is None:
            loi.append("CUA %s: khong co tuong %s" % (c["ky_hieu"], c["tuong"]))
            continue
        s, off = _along(w, c["vi_tri"])
        if off > SAI_SO_MM:
            loi.append("CUA %s %s: lech truc tuong %s %.0f mm" % (c["ky_hieu"], c["vi_tri"], w["ten"], off))
            continue
        need = c["rong"] / 2.0 + KHOANG_HO_CUA_MM
        for p in _diem_noi(w, TUONG):
            if abs(s - p) < need:
                loi.append("CUA %s %s: cach diem noi tuong %.0f mm, can >= %.0f" % (c["ky_hieu"], c["vi_tri"], abs(s - p), need))
                break
    # cua chong nhau tren cung tuong (tru cac o cua o cao do khac nhau)
    for i, a in enumerate(CUA):
        for b in CUA[i + 1:]:
            if a["tuong"] != b["tuong"]:
                continue
            wa = walls.get(a["tuong"])
            if wa is None:
                continue
            sa, _ = _along(wa, a["vi_tri"]); sb, _ = _along(wa, b["vi_tri"])
            if abs(sa - sb) < (a["rong"] + b["rong"]) / 2.0:
                za = (a["cao_be"], a["cao_be"] + a["cao"]); zb = (b["cao_be"], b["cao_be"] + b["cao"])
                if za[0] < zb[1] and zb[0] < za[1]:
                    loi.append("CUA %s va %s chong nhau tren tuong %s" % (a["ky_hieu"], b["ky_hieu"], a["tuong"]))
    for f in SAN:
        if f["tang"] not in keys:
            loi.append("SAN %s: khong co tang %s" % (f["ten"], f["tang"]))
    so = set()
    for r in PHONG:
        if r["tang"] not in keys:
            loi.append("PHONG %s: khong co tang %s" % (r["so"], r["tang"]))
        if r["so"] in so:
            loi.append("PHONG %s: trung so" % r["so"])
        so.add(r["so"])
    for c in COT + BO_TRU:
        if c[5] not in keys or (c[6] and c[6] not in keys):
            loi.append("COT %s: tang khong co" % c[0])
    return loi
