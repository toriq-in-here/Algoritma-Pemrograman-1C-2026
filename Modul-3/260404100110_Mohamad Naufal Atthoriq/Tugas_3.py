jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 4):
    print("Mahasiswa ke-", i)
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("--- Hasil ---")
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", akhir)
    print("Kategori    :", kategori)

    total_nilai += akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama

    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("=== REKAP KELAS ===")
print("Jumlah A :", jumlah_A)
print("Jumlah B :", jumlah_B)
print("Jumlah C :", jumlah_C)
print("Jumlah D :", jumlah_D)
print("Jumlah E :", jumlah_E)
print("Nilai tertinggi :", tertinggi, "-", nama_tertinggi)
print("Nilai terendah  :", terendah, "-", nama_terendah)
print("Rata-rata nilai :", total_nilai / 10)