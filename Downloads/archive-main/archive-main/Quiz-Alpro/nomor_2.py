x = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [12, 34, 56, 78, 90],
    [13, 46, 79, 12, 23],
    [23, 56, 89, 15, 44],
]


def hitung_bilangan_genap(x):
    jumlah_genap = 0
    total_genap = 0

    for a in x:
        for b in a:
            if b % 2 == 0:
                jumlah_genap += 1
                total_genap += b

    return jumlah_genap, total_genap


banyaknya, total = hitung_bilangan_genap(x)

print(f"Banyaknya bilangan genap: {banyaknya}")
print(f"Jumlah semua bilangan genap: {total}")

def bilangan_besar(x): 
    banyak_bilangan = 0
    jumlah_bilangan = 0

    for c in x: 
        for d in c: 
            if d > 50: 
                banyak_bilangan += 1
            jumlah_bilangan += d

    return banyak_bilangan, jumlah_bilangan
banyak, total = bilangan_besar(x)

print(f"Banyaknya bilangan lebih besari dari 50 : {banyak}")
print(f"Jumlah semua bilangan: {total}")

def menghitung(x):
    kolom = len(x[0])
    jumlah = [0] * kolom

    for a in x:
        for i in range(kolom):
            jumlah[i] += a[i]
    return jumlah


total_indeks = menghitung(x)

for idx, total in enumerate(total_indeks):
    print(f"Jumlah untuk indeks ke-{idx}: {total}")