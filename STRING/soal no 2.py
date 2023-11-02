def hitung_kemunculan_kata(string,kata):
    string = string.lower()
    kata_kunci = string.split()
    hitungan = 0

    for kata_kunci in kata_kunci:
        if kata_kunci == kata:
            hitungan += 1

    return hitungan 

kalimat = input("masukan kalimat: ")
kata_dicari = input("masukan kata yang dicari: ")

frekuensi = hitung_kemunculan_kata(kalimat, kata_dicari)

print(f"{kata_dicari} ada {frekuensi} buah")