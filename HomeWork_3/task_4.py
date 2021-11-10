"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

n_max = 0
max_ = 0
dict_ = {}
for n in array:
    if n in dict_:
        dict_[n] += 1
        if dict_[n] > max_:
            max_ = dict_[n]
            n_max = n
    else:
        dict_[n] = 1
print(f'{n_max} встречается {max_} раз')

# Проверка
print(sorted(dict_.items(), key=lambda kv: kv[1], reverse=True))
