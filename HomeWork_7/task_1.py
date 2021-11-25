"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100 - 1


def bubble_sort(array, reverse=False):
    n = 1
    while n < len(array):
        flag = True
        for i in range(len(array) - n):
            if reverse:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = False
            else:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = False
        # print(f'Шаг {n} из {len(array) - 1}: {array}')
        if flag:
            return array
        n += 1
    return array


a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {a}')

# print(f'Отсортированный массив: {bubble_sort(a)}')
print(f'Отсортированный массив: {bubble_sort(a, reverse=True)}')
