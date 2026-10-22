jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km), 0 untuk selesai: "))
    if jarak == 0:   
        break
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
        continue
    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Dapat diskon 50%!")
    print("Tarif: Rp", tarif)

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("=== HASIL ===")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp", total_pendapatan)
print("Jarak terjauh    :", jarak_terjauh, "km")
if jumlah_penumpang > 0:
    print("Rata-rata jarak  :", total_jarak / jumlah_penumpang, "km")
else:
    print("Rata-rata jarak  : 0 km")