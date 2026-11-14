asisten = []
while True:
    nama = input("Nama asisten (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    asisten.append(nama)
asisten_awal = tuple(asisten)

tambahan = input("Nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

hari = []
while True:
    h = input("Nama hari (ketik 'cukup' untuk berhenti): ")
    if h == "cukup":
        break
    hari.append(h)
hari_tugas = tuple(hari)

ex_nama = input("Nama asisten pengecualian: ")
ex_hari = input("Hari pengecualian: ")

print("\n--- Jadwal Shift ---")
for a in asisten_akhir:
    for h in hari_tugas:
        if a == ex_nama and h == ex_hari:
            continue
        print(f"{a} - {h}")