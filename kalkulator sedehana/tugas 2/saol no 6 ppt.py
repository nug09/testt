harga_cpu = 700000
harga_ram = 380000
harga_motherboard = 800000

jumlah_cpu = int(input("Jumlah CPU yang dibeli: "))
jumlah_ram = int(input("Jumlah RAM yang dibeli: "))
jumlah_motherboard = int(input("Jumlah Motherboard yang dibeli: "))

sebelum_diskon = (harga_cpu * jumlah_cpu) + (harga_ram * jumlah_ram) + (harga_motherboard * jumlah_motherboard)

if sebelum_diskon > 1500000:
    diskon = 0.10  
else:
    diskon = 0

harga_diskon = sebelum_diskon * diskon

total = sebelum_diskon - harga_diskon


print("---------------------------------------------------")
print("Total harga: Rp. {:,.2f}".format(sebelum_diskon))
print("Diskon yang didapat sebesar: Rp. {:,.2f}".format(harga_diskon))
print("Total harga yang harus dibayar: Rp. {:,.2f}".format(total))

