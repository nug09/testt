jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

total_nilai = 0
total_bobot = 0

for i in range(jumlah_mata_kuliah):
    print(f"Masukkan data untuk mata kuliah ke-{i + 1}:")
    nilai = input("Nilai (A, B, C, atau D): ").upper()
    bobot = float(input("Bobot (dalam SKS): "))
    
    if nilai == "A":
        nilai_numerik = 4.0
    elif nilai == "B":
        nilai_numerik = 3.0
    elif nilai == "C":
        nilai_numerik = 2.0
    elif nilai == "D":
        nilai_numerik = 1.0
    else:
        print("Input nilai tidak valid.")
        continue
    
    total_nilai += nilai_numerik * bobot
    total_bobot += bobot

ips = total_nilai / total_bobot

print(f"Indeks Prestasi Semester (IPS) Anda adalah: {ips:.2f}")
