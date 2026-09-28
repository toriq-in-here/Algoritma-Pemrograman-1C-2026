def hitung_volume_kerucut(tinggi, jari_jari):
    volume = (1/3) * 3.14 * (jari_jari ** 2) * tinggi
    return volume

jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))
volume = hitung_volume_kerucut(tinggi, jari_jari)
print(f"Volume kerucut adalah: {volume}")
