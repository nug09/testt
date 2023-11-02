gaji_per_jam = float(input("masukan gaji per jam yang di iginkan"))
jam_kerja_per_minggu = float(input("masukan jumlah jam kerja per minggu"))

pendapatan_sebelum_pajak =  gaji_per_jam * jam_kerja_per_minggu * 5

pajak = 0.14 * pendapatan_sebelum_pajak

pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak 

pengeluaran_pakaian_aksesoris = 0.10 * pendapatan_setelah_pajak

pengeluaran_alat_tulis = 0.01 * pendapatan_setelah_pajak

sedekah = 0.25 * (pendapatan_setelah_pajak  -  pengeluaran_pakaian_aksesoris -pengeluaran_alat_tulis)

uang_anak_yatim = 0.30 * sedekah 

uang_dhuafa = sedekah - uang_anak_yatim

print("pendapatan budi sebelum pajak: Rp. {:,.2f}".format(pendapatan_sebelum_pajak))

print("pendapatan budi setelah pajak: Rp. {:,.2f}" .format(pendapatan_setelah_pajak))

print("pengeluaran pakaian dan aksesoris: Rp. {:,.2f}" .format(pengeluaran_pakaian_aksesoris))

print("pengeluaran untuk alat tulis: Rp.  {:,.2f}" . format(pengeluaran_alat_tulis))

print("jumlah uang yang akan disedekahkan: Rp. {:,.2f}" .format(sedekah))

print("jumlah uang yang  diterima anak yatim: Rp. {:,.2f}" .format(uang_anak_yatim))

print("jumlah uang yang diterima kaum duafa: Rp. {:,.2f}" .format(uang_dhuafa))
    