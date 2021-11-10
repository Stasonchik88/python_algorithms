"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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

sum_ = 0
if i_min < i_max:
    for n in array[i_min + 1:i_max]:
        sum_ += n
else:
    for n in array[i_max + 1:i_min]:
        sum_ += n
print(f'Сумма элементов: {sum_}')
