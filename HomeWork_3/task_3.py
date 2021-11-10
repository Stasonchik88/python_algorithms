"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = float('inf')
max_ = float('-inf')
i_min = -1
i_max = -1
for i, n in enumerate(array):
    if n < min_:
        min_ = n
        i_min = i
    elif n > max_:
        max_ = n
        i_max = i
print(f'Минимальный элемент: a[{i_min}] = {min_}')
print(f'Максимальный элемент: a[{i_max}] = {max_}')

array[i_min] = max_
array[i_max] = min_
print(array)
