#harga awal emas per gramnya
harga_awal_emas = 650000  #rupiah 
#emas yang di beli pertama oleh greald
jumlah_emas_pertama = 25 #gram

#harga emas saat ini per gram 
harga_saat_ini = 685000 #rupiah 
#jumlah yang dibeli untuk kedua oleh gerald 
jumlah_emas_kedua = 15 #gram 

#harga emas naik 
harga_naik = 715000 #rupiah 

#menghitung keuntungan pada pembelian pertama 
keuntungan_pertama = (harga_saat_ini -harga_awal_emas) * jumlah_emas_pertama
#menghitung presentase keutungan pertama 
presentase_keuntungan1 = (keuntungan_pertama / (harga_awal_emas * jumlah_emas_pertama)) * 100

#menghitung total keseluruhan emas gerald 
total_emas = jumlah_emas_pertama + jumlah_emas_kedua

#menghitung keuntungan pembelian kedua 
keuntungan_kedua = (harga_naik - harga_saat_ini) *jumlah_emas_kedua

#presentase keuntungan pada pemebelian kedua 
presentase_keuntungan2 = (keuntungan_kedua / (harga_saat_ini * jumlah_emas_kedua)) * 100

#menghitung keuntungan total
keuntungan_total = keuntungan_pertama + keuntungan_kedua

#menghitung keuntungan dalam presentase
presentase_keuntungan3 = (keuntungan_total / (keuntungan_total * total_emas)) * 100

#menampilkan hasil dengan format 3 angka desimal di belakang koma 
print("keuntungan pertama yang di dapat oleh gerald pada pembelian pertama : Rp.", keuntungan_pertama)
print("keuntungan yang di dapat oleh gerald pada pembelian pertama :{:.3f}%".format(presentase_keuntungan1))
print("total emas yang dimiliki gerald sekarang" , total_emas, "gram")
print("keuntungan pertama yang di dapat oleh gerald pada pembelian kedua : Rp.", keuntungan_kedua)
print("keuntungan yang di dapat oleh gerald pada pembelian kedua :{:.3f}%".format(presentase_keuntungan2))
print("keuntungan total yang di dapatkan oleh gerald: Rp.", keuntungan_total)
print("keuntungan total yang di dapat oleh gerald:{:.3f}%".format(presentase_keuntungan3))