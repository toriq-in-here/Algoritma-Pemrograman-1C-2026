daftar = []
while True:
    nama = input("Masukkan nama (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar.append(nama)

print("\n--- Evaluasi ---")
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(f"{nama} -> nama tidak valid")
    else:
        print(f"{nama} -> valid")

hapus = input("\nMasukkan nama penyusup yang dihapus: ")
try:
    daftar.remove(hapus)
    print(f"{hapus} berhasil dihapus")
except ValueError:
    print(f"{hapus} tidak ada di pendaftaran")

print("Daftar akhir:", daftar)