"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

n_max = float('-inf')
i_max = -1
for i, n in enumerate(array):
    if n_max < n < 0:
        n_max = n
        i_max = i
print(f'Максимальный отрицательный элемент: a[{i_max}] = {n_max}')
