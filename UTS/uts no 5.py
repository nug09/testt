def cek_digit_belakang(a, b, c):

    digit_a = a%10
    digit_b = b%10
    digit_c = c%10

    jumlah_sama = 0

    if digit_a == digit_b:
        jumlah_sama += 1
    if digit_a == digit_c:
        jumlah_sama += 1
    if digit_b == digit_c:
        jumlah_sama += 1

# kembalikan true jika minimal dua digit paling kanan sama 
    return jumlah_sama >= 1

# minta input dari nama pengguna
a = int(input('masukkan nilai a: '))
b = int(input('masukkan nilai b: '))
c = int(input('masukkan nilai c: '))    

# panggil fungsi cek_digit_belakang dan cetak hasil
hasil = cek_digit_belakang(a, b, c)
print('output:',hasil)