def is_fibonacci(n):
    a = 1
    b = 1
    while True:
        if a == n:
            return True
        if a > n:
            return False
        a, b = b, a + b

n = int(input("Введите число:\n"))
print(is_fibonacci(n))

