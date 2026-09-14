def konversi_suhu(celcius: float, kode: str) -> float:
    if kode == 'R':
        return celcius * 4 / 5
    elif kode == 'F':
        return celcius * 9 / 5 + 32
    elif kode == 'K':
        return celcius + 273.15
    else:
        return -999

print(konversi_suhu(100, 'R'))   
print(konversi_suhu(100, 'F'))   
print(konversi_suhu(0, 'K'))     
print(konversi_suhu(37, 'X'))   