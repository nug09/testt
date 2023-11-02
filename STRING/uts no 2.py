def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# input dari pengguna
n = int(input('masukan nilai n untuk deret fibonacci:'))

if n <= 0:
    print('nilai n harus lebih dari 0')
else:
    print('deret fibonacci ke-', n, 'adalah:',fibonacci(n))