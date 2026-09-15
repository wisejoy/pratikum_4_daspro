
def rasio_akar(a: float, b: float, c: float) -> float:
    diskriminan = b ** 2 - 4 * a * c

    if a == 0:
        return -999
    elif diskriminan < 0:
        return -999
    else:
        akar1 = (-b + diskriminan ** 0.5) / (2 * a)
        akar2 = (-b - diskriminan ** 0.5) / (2 * a)
        akar_besar = max(akar1, akar2)
        akar_kecil = min(akar1, akar2)

        if akar_kecil == 0:
            return -999
        else:
            return akar_besar / akar_kecil
            

print(rasio_akar(1, -3, 2))  
print(rasio_akar(1, 2, 5))     
print(rasio_akar(0, 2, 5))   
print(rasio_akar(1, -4, 4))   

