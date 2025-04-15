from random import uniform
a = [uniform(-10, 10) for _ in range(10)]
print([round(i, 3) for i in a])
a = sorted(a, key = abs)
print([round(i, 3) for i in a])