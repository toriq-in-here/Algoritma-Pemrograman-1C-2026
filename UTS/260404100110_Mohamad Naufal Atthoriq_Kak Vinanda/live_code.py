#jenis tiket
jenis_tiket = str(input("masukan jenis tiket: ")) 
harga_tiket = int(input("masukan harga tiket:"))

regular = 40000
VIP = 75000
VVIP = 1000000
kategori_minuman = 10000

if regular > 40000:
    print("Kategori Regular")
    if kategori_minuman == "minuman":                  
                biaya = 10000
                minuman = input("Tambahkan minuman? (y/n): ")
                if minuman == "y":
                    biaya = harga_tiket + kategori_minuman
                biaya = 0
elif VIP > 75000:
    print("mendapatkan minuman gratis")
elif VVIP > 1000000:
    print("mendapatkan minuman gratis")
else:
    print("tiket tidak tersedia")

#program diminta membuat sistem pembayaran tiket
#Pertama kita memasukan input jenis tiket dan harga tiket
#ada 3 variabel yaitu jenis-jenis tiket dan satu kategori minuman
#jika pembeli membeli tiket yang regular akan disarankan untuk membeli minuman
#jika pembeli beli tiket VIP dan VVIP akan mendapatkan minuman gratis