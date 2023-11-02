def prima(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
N = int(input("Masukkan nilai N: "))

def print_prima(N):
    for num in range(2, N + 1):
        if prima(num):
            print(num, end=" ")

print("Deret bilangan prima dari 1 sampai", N, "adalah:")
print_prima(N)
