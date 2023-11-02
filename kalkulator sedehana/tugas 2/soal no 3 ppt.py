def prima(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prima_terdekat(n):
    closest = None
    for i in range(n - 1, 1, -1):
        if prima(i):
            closest = i
            break
    return closest

n = int(input("Masukkan bilangan n: "))
prima_dekat = prima_terdekat(n)
if prima_dekat:
    print(f"Bilangan prima terdekat yang kurang dari {n} adalah {prima_dekat}.")
else:
    print(f"Tidak ada bilangan prima terdekat yang kurang dari {n}.")

