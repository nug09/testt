def hitung_faktorial(angka):
    faktorial = 1
    for i in range(1, angka + 1):
        faktorial *= i
    return faktorial

angka = int(input("Masukkan angka untuk menghitung faktorial: "))
hasil_faktorial = hitung_faktorial(angka)
print(f"{angka}! = {hasil_faktorial}")