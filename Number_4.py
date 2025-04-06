def russian_alphabet():
    for code in range(ord('а'), ord('я') + 1):
        yield chr(code)

# Пример использования
for letter in russian_alphabet():
    print(letter, end=' ')
