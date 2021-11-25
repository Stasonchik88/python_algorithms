"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


def merge_sort(array):
    if len(array) == 1:
        return array

    a = merge_sort(array[:len(array)//2])
    b = merge_sort(array[len(array)//2:])

    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            array[i + j] = a[i]
            i += 1
        else:
            array[i + j] = b[j]
            j += 1
    else:
        while i < len(a):
            array[i + j] = a[i]
            i += 1
        while j < len(b):
            array[i + j] = b[j]
            j += 1
    return array


a = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {a}')

print(f'Отсортированный массив: {merge_sort(a)}')
