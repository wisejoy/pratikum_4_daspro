
def pembagian_akar(a: float, b: float, c: float) -> float:
    if a == 0:
        return -999
    diskriminan = b ** 2 - 4 * a * c
    if diskriminan < 0:
        return -999
    x1 = (-b + diskriminan ** 0.5) / (2 * a)
    x2 = (-b - diskriminan ** 0.5) / (2 * a)
    x_besar = max(x1, x2)
    x_kecil = min(x1, x2)
    if x_kecil == 0:
        return -999
    else:
        return x_besar / x_kecil

print(pembagian_akar(1, -3, 2))   
print(pembagian_akar(1, 2, 1))    
print(pembagian_akar(1, 0, 1))   
print(pembagian_akar(0, 2, 1))    