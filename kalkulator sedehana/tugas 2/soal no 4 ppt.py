def generate_factorial_series(n):
    for i in range(n, 0, -1):
        result = 1
        for j in range(i, 0, -1):
            result *= j
        print(result, end=' ')  
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  

n = int(input("Masukkan nilai n: "))
generate_factorial_series(n)
