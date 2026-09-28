jarak_rumah_keluarga = 100
konsumsi_bensin = 40
sisa_bensin = 1.5
harga_per_liter = 10000

jarak_tempuh = 2 * jarak_rumah_keluarga
total_bensin_diperlukan = jarak_tempuh / konsumsi_bensin
bensin_dibeli = max(total_bensin_diperlukan - sisa_bensin, 0)
total_biaya_bensin = bensin_dibeli * harga_per_liter

print("Jarak total yang ditempuh        :", jarak_tempuh, "km")
print("Total bensin untuk seluruh jalan :", total_bensin_diperlukan, "liter")
print("Total bensin yang harus dibeli   :", bensin_dibeli, "liter")
print("Total biaya bensin               : Rp", int(total_biaya_bensin))