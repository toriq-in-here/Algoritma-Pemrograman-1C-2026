jumlah_penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)
    nama = input("Nama                    : ")
    ipk = float(input("IPK                     : "))
    penghasilan = int(input("Penghasilan orang tua   : "))

    if ipk < 3.00:
        print(nama, "- Tidak memenuhi syarat (IPK < 3.00)")
        continue

    if penghasilan <= 3000000:
        print(nama, "- Mendapat BEASISWA PENUH")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print(nama, "- Mendapat BEASISWA SEBAGIAN")
    else:
        print(nama, "- Tidak mendapat beasiswa")

    if jumlah_penuh == 5:
        print("\nKuota beasiswa penuh (3 mahasiswa) sudah terpenuhi.")
        print("Seleksi dihentikan.")
        break

print("\nSelesai. Jumlah beasiswa penuh:", jumlah_penuh)