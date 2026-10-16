pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

if not (100 <= pin <= 999):
    print("PIN harus 3 digit!")
elif not (0 <= jam <= 23):
    print("Jam harus antara 0-23!")
else:
    digit1 = pin // 100
    digit2 = (pin // 10) % 10
    digit3 = pin % 10

    if pin % 5 == 0:
        if jam < 12:
            pesan = "Garasi Pagi Terbuka"
        else:
            pesan = "Garasi Malam Terbuka, Lampu Dinyalakan"
    elif pin % 2 == 0:
        if digit1 + digit3 == digit2:
            pesan = "Garasi VIP Terbuka Khusus Bos"
        else:
            pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
    else:
        pesan = "Akses Ditolak"

    status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

    print()
    print("===== LAPORAN AKSES =====")
    print("Digit pertama  :", digit1)
    print("Digit kedua    :", digit2)
    print("Digit ketiga   :", digit3)
    print("Status pintu   :", pesan)
    print("Status CCTV    :", status_cctv)