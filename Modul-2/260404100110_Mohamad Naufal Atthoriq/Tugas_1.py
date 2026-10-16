kode = int(input("Masukkan kode rahasia (3 digit): "))

d1 = kode // 100
d2 = (kode // 10) % 10
d3 = kode % 10

print("Digit pertama :", d1)
print("Digit kedua   :", d2)
print("Digit ketiga  :", d3)

pelacak = d1 * d3
print("Nilai pelacak awal:", pelacak)

if d2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - d2
print("Nilai pelacak setelah tahap 1:", pelacak)

if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2
print("Nilai pelacak setelah tahap 2 (nilai akhir):", pelacak)

if pelacak > 50:
    print("Status: Kategori A")
elif pelacak > 20:
    print("Status: Kategori B")
else:
    print("Status: Password Ditolak")

if pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")