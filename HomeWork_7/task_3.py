"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.
"""
import random
m = 5
size = 2 * m + 1
MIN_ITEM = -100
MAX_ITEM = 100


def quick_select(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    print(f'{pivot}: {lows} -> {pivots} -> {highs}')

    if k < len(lows):
        return quick_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(f'Исходный массив: {a}')

print(f'Медиана массива: {quick_select(a, len(a) / 2)}')
print(f'Отсортированный массив: {sorted(a)}')
