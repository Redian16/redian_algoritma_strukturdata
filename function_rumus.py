def luas_persegi(sisi):

    luas = sisi * sisi

    return luas

#rumus sisi x sisi x sisi
def volume_persegi (sisi):
    volume = luas_persegi (sisi) * sisi
    return volume

sisi = 8
print("luas persegi : ",luas_persegi(sisi))
print("volume kubus : ",volume_persegi(sisi))