def cek_digit_belakang(a, b, c):
    # Mendapatkan digit paling kanan dari masing-masing angka
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10

    # Mengecek apakah setidaknya dua angka memiliki digit paling kanan yang sama
    return (digit_a == digit_b and digit_b != digit_c) or (digit_a == digit_c and digit_b != digit_c) or (digit_b == digit_c and digit_a != digit_c)

# Membaca input dari pengguna
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Memanggil fungsi cek_digit_belakang dan mencetak hasilnya
hasil = cek_digit_belakang(a, b, c)
print("Output yang diharapkan=",hasil)