def diskriminan(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def akar1(a: float, b: float, c: float) -> float:
    return (-b + diskriminan(a, b, c) ** 0.5) / (2 * a)


def akar2(a: float, b: float, c: float) -> float:
    return (-b - diskriminan(a, b, c) ** 0.5) / (2 * a)


def akar_besar(a: float, b: float, c: float) -> float:
    if akar1(a, b, c) > akar2(a, b, c):
        return akar1(a, b, c)
    else:
        return akar2(a, b, c)


def akar_kecil(a: float, b: float, c: float) -> float:
    if akar1(a, b, c) < akar2(a, b, c):
        return akar1(a, b, c)
    else:
        return akar2(a, b, c)


def pembagian_akar(a: float, b: float, c: float) -> float:
    if a == 0:
        return -999
    elif diskriminan(a, b, c) < 0:
        return -999
    elif akar_kecil(a, b, c) == 0:
        return -999
    else:
        return akar_besar(a, b, c) / akar_kecil(a, b, c)


print(pembagian_akar(1, -3, 2))
print(pembagian_akar(1, 2, 1))
print(pembagian_akar(1, 0, 1))
print(pembagian_akar(0, 2, 1))