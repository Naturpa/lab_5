# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 18, 19, 20, 9, 27, 36, 45, 90]

# 1. Вывод всех элементов списка, которые меньше 5
less_than_five = list(filter(lambda x: x < 5, numbers))
print(less_than_five)

# 2. Вывод всех элементов списка, разделенные на два
divided_by_two = list(map(lambda x: x / 2, numbers))
print(divided_by_two)

# 3. Вывод результата деления на два всех элементов списка, которые больше 17
greater_than_17_divided = list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers)))
print(greater_than_17_divided)

# 4. Сумма квадратов всех двузначных чисел, делящихся на 9
sum_of_squares = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0 and 10 <= x < 100, numbers)))
print(sum_of_squares)