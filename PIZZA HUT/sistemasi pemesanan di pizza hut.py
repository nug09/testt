#print selamat datang dan berapa jumlah pesanan pizza yang di inginkan 
pesanan_pizza =[]
print("selamat datang di pizza hut")
jumlah_pizza = int(input("ingin berapa pizza"))

for _ in range(jumlah_pizza):
    print("=====================================================")
    print("daftar topping yang tersedia : \n1.frankfurter bbq \n2.meat monsta \n3.super supreme \n4.cheese lover  \n5. american favorite /n6.pepperoni \n7.cheese overload \n8.melting tuna")
    topping= int(input("pilih toping anda (1-8):"))
    print("-----------------------------------------------------")
    print ("Daftar Crust Yang Tersedia : \n1. Pan \n2. StuffedCrust Cheese \n3. StuffedCrust Sausage \n4. Cheesy Bites \n5. Crown Crust")
    crust = int(input("Silahkan Pilih Crust Anda (1-5): "))
    print("------------------------------------------------------")
    print ("Daftar Ukuran Pizza Yang Tersedia : \n1. Personal \n2. Regular \n3. Large")
    ukuran = int(input("Silahkan Pilih Ukuran Pizza Anda (1-3): "))
    print(" apakah mau menambah extra cheese")
    xtracheese = input("apakah anda ingin menambahkan extra cheese ? (y/n)")
    
    #daftar dictionory topping yang ada di pizza hut 
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
    
    #daftar dictionory pada crust pizza
    daftar_crust = {
        1: "Pan", 
        2: "stuffedcrust cheese",
        3: "stuffedcrust sausage",
        4: "cheese bites",
        5: "crown crust"
    }
    
    #daftar dictionory pada ukuran pizza
    daftar_ukuran = {
        1: "singel",
        2: "reguler",
        3: "large"
    }
    
    # mengambil nama sesuai yang di inputkan pada sistem menu 
    nama_topping = daftar_topping[topping]
    nama_crust = daftar_crust[crust]
    nama_ukuran = daftar_ukuran[ukuran]

    #deklarasi harga awal = 0 rupiah 
    harga = 0
    harga_topping = 43637 
    harga_xtracheese = 0
    
    # if untuk harga pizza dengan pinggiran crust pan dan juga harga per ukuranya ukurannya 
    if crust == 1 :
        hargacrust = 43637 # untuk harga pizza dengan pinggiran crust pan
        if ukuran == 1 :
            hargaukuran= 0 # untuk harga pizza dengan ukuran personal 
        elif ukuran == 2 :
            hargaukuran = 57273 # untuk harga pizza  dengan ukuran regural 
        else: 
            hargaukuran = 89091 # untuk harga pizza dengan ukuran large
    
    # if untuk harga pizza dengan pinggiran stuffedcrust cheese dan juga harga per ukurannya 
    elif crust == 2 :
        hargacrust = 55455 # untuk harga pizza dengan pinggiran stuffedcrust cheese 
        if ukuran == 1 :
            hargaukuran = 0 # untuk harga pizza  dengan ukuran personal 
        elif ukuran == 2 :
            hargaukuran = 64455 # untuk harga pizza  dengan ukuran regural 
        else: 
            hargaukuran = 104545 # untuk harga pizza  dengan ukuran large 
    
    # if untuk harga pizza dengan pinggiran stuffedcrust sausage dan juga harga per ukurannya 
    elif crust == 3 :
        hargacrust = 52728 # untuk harga pizza dengan pinggiran stuffedcrust sausage 
        if ukuran == 1 :
            hargaukuran = 0 # untuk harga pizza dengan ukuran personal
        elif ukuran == 2 :
            hargaukuran = 64545 # untuk harga pizza  dengan ukuran reguler 
        else:
            hargaukuran = 102727 # untuk harga pizza  dengan ukuran large
            
    # if untuk harga pizzza dengan pinggiran cheessy bites dan juga harga per ukurannya 
    elif crust == 4 :
        hargacrust = 55455 # untuk harga pizza dengan pinggiran cheessy bites 
        if ukuran == 1 : 
            hargaukuran = 0 # ukuran personal dengan ukuran personal 
        elif ukuran == 2 :
            hargaukuran= 65455 # ukuran personal dengan ukuran reguler 
        else:
            hargaukuran = 104545 # ukuran personal dengan ukuran large 
            
    #fungsi if untuk harga pizza dengan pinggiran crown crust dan juga harga per ukurannya 
    else:
        hargacrust = 55455 #harga crust Crown Crust
        if ukuran == 1:
            hargaukuran= 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargaukuran = 65455 #harga jika ukuran regular
        elif ukuran == 3:
            hargaukuran = 104545 #harga jika ukuran large
        else:
            print("menu anda tidak ada")
    
    
            
    #fungsi if untuk jika pelanggan ingin menambahkan Extra Cheese beserta harga per ukuran pizza
    if xtracheese == "Y":
        xtracheese = "Dengan Tambahan Extra Cheese"
        if ukuran == 1:
                harga += 13636 #harga jika ukuran personal
        elif ukuran == 2:
                harga = 16364 #harga jika ukuran regular
        elif ukuran ==3:
                 harga = 19091 #harga jika ukuran large
    else:
          xtracheese = "Tanpa Tambahan Extra Cheese"

     
    #deklarasi perhitungan total harga
    total_harga = harga + hargacrust + hargaukuran + harga_xtracheese 
    
    pesanan_pizza.append({
        "Topping": nama_topping,
        "Crust": nama_crust,
        "Ukuran": nama_ukuran,
        "Extra Cheese": xtracheese,
        "Total Harga": total_harga
    })
total_harga_semua_pesanan = sum(pesanan["Total Harga"] for pesanan in pesanan_pizza)

#print tampilan bill
print("========================================================")
print("-----------Pesanan Anda----------")
print(f"Topping : {nama_topping}") #menampilkan nama topping yang dipilih
print(f"Crust : {nama_crust}") #menampilkan nama crust yang dipilih
print(f"Ukuran : {nama_ukuran}") #menampilkan nama ukuran yang dipilih
print(xtracheese) #menampilkan hasil apakah user menambahkan Extra Cheese atau tidak
print("_________________________________")
print("Total Harga = Rp. {:,.2f}".format(total_harga_semua_pesanan)) #menampilkan harga total
print("Terima Kasih Atas Kunjungan Anda")

