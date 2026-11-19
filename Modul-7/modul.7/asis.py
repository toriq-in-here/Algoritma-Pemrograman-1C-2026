tugas = {}

while True:
    print("LIST TUGAS SAYA")
    print("1. Menambah Tugas")
    print("2. Menampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. hapus tugas")
    print("5. Jumlah Tugas Selesai dan Belum")
    print("6. Selesai")
    pilih = input("Pilih Menu: ")

    if pilih == "1":
        nama = input("Nama Tugas: ")
        tugas[nama]= ("Belum Selesai")
        print("tugas ditambahkan")
    elif pilih == "2":
        if not tugas:
            print("belum ada tugas")
        for nama, status in tugas.items():
            print("f- {nama}: {status}")
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