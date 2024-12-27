def kategori_usia(usia):
    if usia < 13:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 64:
        return "Dewasa"
    else:
        return "Lansia"

def main():
    # Usia tetap diberikan sebagai 20 tahun
    usia = 20

    # Menentukan kategori usia dan menampilkan hasil
    kategori = kategori_usia(usia)
    print(f"Kategori usia Anda (usia {usia} tahun): {kategori}")

# Memanggil fungsi utama
if __name__ == "__main__":
    main()
