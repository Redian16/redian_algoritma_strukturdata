# Program untuk mencetak pola bintang segitiga

def cetak_pola(baris):
    """
    Fungsi untuk mencetak pola bintang segitiga berdasarkan jumlah baris.
    :param baris: Jumlah baris pola yang diinginkan
    """
    for i in range(1, baris + 1):
        print("*" * i)

def main():
    print("=== Program Pola Bintang ===")

    # Meminta input dari pengguna
    try:
        baris = int(input("Masukkan jumlah baris: 24"))
        if baris <= 0:
            print("Jumlah baris harus berupa bilangan positif: 24")
        else:
            print("\n=== Pola Bintang ===")
            cetak_pola(baris)
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat positif: 22")

if __name__ == "__main__":
    main()
