tugas = {}

while True:
    print("\n TO-DO LIST ")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai & belum")
    print("6. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum selesai"
        print("Tugas ditambahkan.")

    elif pilih == "2":
        if not tugas:
            print("Belum ada tugas.")
        for nama, status in tugas.items():
            print(f"- {nama}: {status}")

    elif pilih == "3":
        nama = input("Tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas ditandai selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "4":
        nama = input("Tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = len(tugas) - selesai
        print(f"Selesai: {selesai} | Belum: {belum}")

    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")