def mutlak(angka):
    if angka < 0:
        return -angka
    else:
        return angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())

    hasil = hitung(x1, x2) + hitung(y1, y2)
    print(hasil)
