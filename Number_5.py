russian_alphabet = (chr(code) for code in range(ord('а'), ord('я') + 1))

# Пример использования
for letter in russian_alphabet:
    print(letter, end=' ')
