jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))
    print(f"\n Pemeriksaan Baris {baris} ")

    for nomor in range(1, jumlah_lampu + 1):
        if nomor % 3 == 0:
            print(f"Lampu {nomor} mengalami gangguan.")
        else:
            print(f"Lampu {nomor} berfungsi normal.")
    print()

print("Pemeriksaan selesai.")
print("Harap periksa sumber listrik utama taman.")

