def jenis_segitiga(a: int, b: int, c: int) -> str:

    if a == b and b == c:
        return "segitiga sama sisi"

    elif a == b or b == c or a == c:
        return "segitiga sama kaki"

    else:
        return "segitiga sembarang"

print(jenis_segitiga(5, 5, 5))
print(jenis_segitiga(5, 5, 8))
print(jenis_segitiga(3, 4, 5))