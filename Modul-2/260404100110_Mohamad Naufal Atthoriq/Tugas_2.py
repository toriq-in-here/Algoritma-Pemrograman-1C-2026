jumlah_barang = int(input("Masukkan jumlah jenis barang: "))

total_awal = 0

for i in range(jumlah_barang):
    print("Barang ke-", i + 1)
    harga = int(input("  Harga satuan: Rp"))
    jumlah = int(input("  Jumlah beli: "))
    total_awal = total_awal + (harga * jumlah)

if total_awal % 100000 == 0:
    diskon = 100
    keterangan = "Gratis semua belanjaan!"
elif total_awal % 50000 == 0:
    diskon = 50
    keterangan = "Diskon 50%"
elif total_awal % 10000 == 0:
    diskon = 20
    keterangan = "Diskon 20%"
elif total_awal >= 200000:
    diskon = 10
    keterangan = "Diskon 10%"
else:
    diskon = 0
    keterangan = "Tidak ada diskon"

potongan = total_awal * diskon / 100
total_akhir = total_awal - potongan

status_poin = "Poin Bertambah" if total_akhir > 0 else "Tidak Ada Poin"

print()
print("===== STRUK BELANJA =====")
print("Total belanja awal :", total_awal)
print("Promo yang didapat :", keterangan)
print("Total yang dibayar :", int(total_akhir))
print("Status poin        :", status_poin)