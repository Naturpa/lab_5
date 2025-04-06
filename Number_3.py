def square_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a * a
        a, b = b, a + b

# Пример использования
for square in square_fibonacci(7):
    print(square)
