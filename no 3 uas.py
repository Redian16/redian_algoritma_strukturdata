def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    # Konstanta jam kerja normal per hari
    JAM_KERJA_NORMAL = 8
    
    # Inisialisasi total gaji
    total_gaji = 0

    # Perulangan untuk setiap hari kerja
    for hari in range(hari_kerja):
        if jam_kerja_per_hari[hari] <= JAM_KERJA_NORMAL:
            total_gaji += jam_kerja_per_hari[hari] * tarif_per_jam
        else:
            jam_lembur = jam_kerja_per_hari[hari] - JAM_KERJA_NORMAL
            total_gaji += (JAM_KERJA_NORMAL * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)

    return total_gaji

# Input dari pengguna
tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

# Memasukkan jam kerja per hari
jam_kerja_per_hari = []
for i in range(hari_kerja):
    jam = float(input(f"Masukkan jam kerja untuk hari ke-{i + 1}: "))
    jam_kerja_per_hari.append(jam)

# Hitung total gaji
total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)

# Cetak hasil
print(f"Total gaji bulanan adalah: Rp{total_gaji:.2f}")
