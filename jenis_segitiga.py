def jenis_segitiga(a: int, b: int, c: int) -> str:

    if a == b and b == c:
        return "sama sisi"

    elif a == b or b == c or a == c:
        return "sama kaki"

    else:
        return "sembarang"

print(jenis_segitiga(5, 5, 5))
print(jenis_segitiga(5, 5, 8))
print(jenis_segitiga(3, 4, 5))