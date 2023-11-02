def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]

# Contoh penggunaan
jumlah_bilangan = int(input("Masukkan jumlah bilangan Fibonacci yang ingin Anda generasi: "))
hasil_fibonacci = fibonacci(jumlah_bilangan)
print(f"Deret Fibonacci dengan {jumlah_bilangan} bilangan pertama: {hasil_fibonacci}")