def is_kabisat(tahun: int) -> bool:
            if tahun % 400 == 0 :
                    return True

            elif tahun % 100 == 0 :
                    return False

            elif tahun % 4 == 0 :
                     return True

            else:
                    return False

print(is_kabisat(2000))
print(is_kabisat(1900))
print(is_kabisat(2024))
print(is_kabisat(2025))