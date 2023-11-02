#print pertama dan input
print ("Selamat Datang di Pizza Hut")
print ("========================================================")
print ("Daftar Topping Yang Tersedia : \n1. Frankfurter BBQ \n2. Meat Monsta \n3. Super Supreme \n4. Cheese Lovers \n5. American Favourite \n6. Pepperoni \n7. Cheese Overload \n8. Tuna Melt")
topping = int(input("Silahkan Pilih Topping Anda (1-8): "))
print ("--------------------------------------------------------")
print ("Daftar Crust Yang Tersedia : \n1. Pan \n2. StuffedCrust Cheese \n3. StuffedCrust Sausage \n4. Cheesy Bites \n5. Crown Crust")
crust = int(input("Silahkan Pilih Crust Anda (1-5): "))
print ("--------------------------------------------------------")
print ("Daftar Ukuran Pizza Yang Tersedia : \n1. Personal \n2. Regular \n3. Large")
ukuran = int(input("Silahkan Pilih Ukuran Pizza Anda (1-3): "))
print ("--------------------------------------------------------")
xtracz = input("Apakah Anda ingin Menambahkan Extra Cheese (Y/N)? ")

#dictionary daftar topping
daftar_topping = {
    1: "Frankfurter BBQ",
    2: "Meat Monsta",
    3: "Super Supreme",
    4: "Cheese Lovers",
    5: "American Favourite",
    6: "Pepperoni",
    7: "Cheese Overload",
    8: "Tuna Melt"
}

#dictionary daftar crust
daftar_crust = {
    1: "Pan",
    2: "StuffedCrust Cheese",
    3: "StuffedCrust Sausage",
    4: "Cheesy Bites",
    5: "Crown Crust"
}

#dictionary daftar ukuran
daftar_ukuran = {
    1: "Personal",
    2: "Regular",
    3: "Large"
}

#mengambil nama berdasarkan nomor yang di inputkan
nama_topping = daftar_topping[topping]
nama_crust = daftar_crust[crust]
nama_ukuran = daftar_ukuran[ukuran]

#deklarasi harga awal = 0 rupiah
harga = 0

#fungsi if untuk harga crust Pan beserta dengan harga per ukuran pizza
if crust == 1:
    harga += 43637 #harga crust Pan
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 57273 #harga jika ukuran regular
    else:
        harga += 89091 #harga jika ukuran large

#fungsi if untuk harga crust StuffedCrust Cheese beserta dengan harga per ukuran pizza
elif crust == 2:
    harga += 55455 #harga crust StuffedCrust Cheese
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 65455 #harga jika ukuran regular
    else:
        harga += 104545 #harga jika ukuran large

#fungsi if untuk harga crust StuffedCrust Sausage beserta dengan harga per ukuran pizza
elif crust == 3:
    harga += 52728 #harga crust StuffedCrust Sausage
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 64545 #harga jika ukuran regular
    else:
        harga += 102727 #harga jika ukuran large

#fungsi if untuk harga crust Cheesy Bites beserta dengan harga per ukuran pizza
elif crust == 4:
    harga += 57273 #harga crust Cheesy Bites
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 66364 #harga jika ukuran regular
    else:
        harga += 107273 #harga jika ukuran large

#fungsi if untuk harga crust Crown Crust beserta dengan harga per ukuran pizza
else:
    harga += 55455 #harga crust Crown Crust
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 65455 #harga jika ukuran regular
    else:
        harga += 104545 #harga jika ukuran large

#fungsi if untuk jika pelanggan ingin menambahkan Extra Cheese beserta harga per ukuran pizza
if xtracz == "Y":
    xtraczif = "Dengan Tambahan Extra Cheese"
    if ukuran == 1:
        harga += 13636 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 16364 #harga jika ukuran regular
    else:
        harga += 19091 #harga jika ukuran large
else:
    xtraczif = "Tanpa Tambahan Extra Cheese"

#print tampilan bill
print("========================================================")
print("-----------Pesanan Anda----------")
print(f"Topping : {nama_topping}") #menampilkan nama topping yang dipilih
print(f"Crust : {nama_crust}") #menampilkan nama crust yang dipilih
print(f"Ukuran : {nama_ukuran}") #menampilkan nama ukuran yang dipilih
print(xtraczif) #menampilkan hasil apakah user menambahkan Extra Cheese atau tidak
print("_________________________________")
print("Total Harga = Rp. {:,.2f}".format(harga)) #menampilkan harga total
print("Terima Kasih Atas Kunjungan Anda")