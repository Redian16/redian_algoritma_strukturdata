#variabel global

nama = "belajar kode"

versi = "1.0.0"

def help():
    #ini variabel lokal
    nama = "programku"
    versi = "1.0.1"
    #mengakses variabel local
    print("nama: %s" %nama)
    print("versi: %s" %versi)
    
#menfgakses variabel global
print("nama : %s" % nama)
print("versi : %s" % versi)

#memanggil fungsi help
help()