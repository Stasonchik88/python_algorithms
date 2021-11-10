"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_1 = float('inf')  # Самый минимальный
min_2 = float('inf')

for n in array:
    if n < min_1:
        min_1, min_2 = n, min_1
    elif n < min_2:
        min_2 = n
print(f'{min_1} < {min_2}')
