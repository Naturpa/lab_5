def sort_points(points):
    # Сортировка по расстоянию от (0, 0), затем по x и y
    sorted_points = sorted(points, key=lambda point: (point[0]**2 + point[1]**2, point[0], point[1]))
    return sorted_points

# Пример использования
points = [(1, 2), (2, 1), (1, -1), (-1, -1), (0, 1)]
sorted_points = sort_points(points)

for point in sorted_points:
    print(point)
