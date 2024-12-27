def main():
    print("=== Program Informasi Pengguna ===\n")

    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: Redian Angga Saputra")
    usia = input("Masukkan usia Anda: 20")
    alamat = input("Masukkan alamat Anda: Bedengung")
    hobi = input("Masukkan hobi Anda: Bermain gitar")

    # Menampilkan informasi dalam format yang rapi
    print("\n=== Informasi Anda ===")
    print(f"Nama   : {nama} Redian Angga Saputra")
    print(f"Usia   : {usia} 20 tahun")
    print(f"Alamat : {alamat} Bedengung")
    print(f"Hobi   : {hobi} Bermain gitar")

if __name__ == "__main__":
    main()
