playlist = {}

while True:
    print("\n PLAYLIST MUSIK ")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada.")
        else:
            playlist[nama] = {}
            print("Playlist dibuat.")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu ditambahkan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        if not playlist:
            print("Belum ada playlist.")
        for nama, lagu in playlist.items():
            print(f"\nPlaylist: {nama}")
            if not lagu:
                print("  (kosong)")
            for judul, penyanyi in lagu.items():
                print(f"  - {judul} oleh {penyanyi}")

    elif pilih == "4":
        cari = input("Judul lagu dicari: ")
        ketemu = False
        for nama, lagu in playlist.items():
            if cari in lagu:
                print(f"Ditemukan di '{nama}' oleh {lagu[cari]}")
                ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu yang dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu dihapus.")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")