jumlah_hari_bulan = {
    1: 31,  # Januari
    2: 29,  # Februari
    3: 31,  # Maret
    4: 30,  # April
    5: 31,  # Mei
    6: 30,  # Juni
    7: 31,  # Juli
    8: 31,  # Agustus
    9: 30,  # September
    10: 31,  # Oktober
    11: 30,  # November
    12: 31,  # Desember
}

while True:
    try:
        nomor_bulan = int(input("Masukkan nomor bulan (1-12): "))
    
        if 1 <= nomor_bulan <= 12:
            break
        else:
            print("Nomor bulan tidak valid. Masukkan nomor bulan antara 1 hingga 12.")
    except ValueError:
        print("Masukkan nomor bulan yang valid (1-12).")

jumlah_hari = jumlah_hari_bulan[nomor_bulan]
print(f"Jumlah hari dalam bulan {nomor_bulan} di tahun 2020 adalah {jumlah_hari} hari.")
