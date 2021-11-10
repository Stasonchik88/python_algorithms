"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random
MIN_ITEM = -100
MAX_ITEM = 100

ROWS = 5
COLUMNS = 5

matrix = []
for i in range(ROWS):
    r = []
    for j in range(COLUMNS):
        r.append(random.randint(MIN_ITEM, MAX_ITEM))
        print(r[j], end='\t')
    matrix.append(r)
    print()

min_ = [float('inf')] * len(matrix[0])
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col < min_[j]:
            min_[j] = col
print(f'Минимальные значения в столбцах: {min_}')

max_ = float('-inf')
for n in min_:
    if n > max_:
        max_ = n
print(f'Максимальное значение среди минимальных: {max_}')
