def evaluasi(pc):
    if pc[1] == "Normal" and pc[2] >= 8:
        return "Layak"
    return "Tidak Layak"

jumlah = int(input("Jumlah PC: "))
data = []
for i in range(jumlah):
    nama = input(f"Nama PC ke-{i+1}: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("RAM (GB): ")
    try:
        ram = int(ram)
    except ValueError:
        pass  
    data.append([nama, status, ram])

print("\n--- Hasil Evaluasi ---")
for pc in data:
    try:
        hasil = evaluasi(pc)
    except TypeError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')