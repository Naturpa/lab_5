def factorials(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f

# Пример использования
for fact in factorials(7):
    print(fact)