kalimat = input("masukan kalimat: ")
kata_kata = kalimat.split()
kata_terpendek = kata_terpanjang = kata_kata[0]

for kata in kata_kata:
    if len(kata) < len(kata_terpanjang):
        kata_terpendek = kata
    if len(kata) > len(kata_terpanjang):
        kata_terpanjang = kata

print("kata terpendek:", kata_terpendek)
print("kata terpanjang:", kata_terpanjang)
