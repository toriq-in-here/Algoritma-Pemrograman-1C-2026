suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    if tekanan > 35:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
    else:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan = "Tekanan Tidak Stabil"
    else:
        pesan = "Operasi Reaktor Normal"
else:
    pesan = "Reaktor Belum Cukup Panas"
    
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print()
print("===== LAPORAN REAKTOR =====")
print("Suhu reaktor   :", suhu, "Celcius")
print("Tekanan gas    :", tekanan, "Bar")
print("Status bahaya  :", pesan)
print("Status pompa   :", status_pompa)