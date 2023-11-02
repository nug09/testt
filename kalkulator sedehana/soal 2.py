import math 

jumlah_awal = 200_000_000
jumlah_akhir = 400_000_000
bunga_tahunan = 0.10

waktu_tahun = math.log(jumlah_akhir/ jumlah_awal) / math.log(1+bunga_tahunan)
waktu_bulan = waktu_tahun * 12
print(f"waktu yang dibutuhkan mencapai {jumlah_akhir / 1_000_000} juta rupiah adaalah {waktu_tahun:.2f} tahun atau {waktu_bulan:.2f} bulan.")

