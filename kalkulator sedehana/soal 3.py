jumlah_awal = 5000000
bunga_tahunan = 0.10
tahun = 3

jumlah_akhir = jumlah_awal * (1 - bunga_tahunan) ** tahun

print(f"jumlah uang di akhir tahun ketiga adalah : Rp . {jumlah_akhir:,.2f}")