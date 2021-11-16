"""
Домашнее задание к уроку №3.

Задание №9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import cProfile
import profile
import random
MIN_ITEM = -100
MAX_ITEM = 100


def for_cycle_in_range(rows, columns):
    matrix = []
    for i in range(rows):
        r = []
        for j in range(columns):
            r.append(random.randint(MIN_ITEM, MAX_ITEM))
            # print(r[j], end='\t')
        matrix.append(r)
        # print()
    return matrix


def min_in_columns_enum(matrix):
    min_ = [float('inf')] * len(matrix[0])
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col < min_[j]:
                min_[j] = col
    # print(f'Минимальные значения в столбцах: {min_}')
    # return min_


def min_in_columns_range(matrix):
    min_ = [float('inf')] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_[j]:
                min_[j] = matrix[i][j]
    # print(f'Минимальные значения в столбцах: {min_}')
    # return min_


def min_in_columns_while(matrix):
    min_ = []
    j = 0
    while j < len(matrix[0]):
        min_.append(float('inf'))
        i = 0
        while i < len(matrix):
            if matrix[i][j] < min_[j]:
                min_[j] = matrix[i][j]
            i += 1
        j += 1
    # print(f'Минимальные значения в столбцах: {min_}')
    # return min_


def max_number(min_):
    max_ = float('-inf')
    for n in min_:
        if n > max_:
            max_ = n
    print(f'Максимальное значение среди минимальных: {max_}')


# Матрица 100х100
def main_r100_c100():
    m = for_cycle_in_range(100, 100)
    min_in_columns_enum(m)
    min_in_columns_while(m)
    min_in_columns_range(m)
    # max_number(min_in_col_en)


"""
Результат замера для матрицы 100х100:

73276 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
    10000    0.005    0.000    0.007    0.000 random.py:238(_randbelow_with_getrandbits)
    10000    0.006    0.000    0.012    0.000 random.py:291(randrange)
    10000    0.003    0.000    0.015    0.000 random.py:335(randint)
        1    0.004    0.004    0.020    0.020 task_1.py:14(for_cycle_in_range)
        
        1    0.000    0.000    0.000    0.000 task_1.py:26(min_in_columns_enum)  <-- контрольная функция
        1    0.001    0.001    0.001    0.001 task_1.py:36(min_in_columns_range) <-- контрольная функция
        1    0.003    0.003    0.003    0.003 task_1.py:46(min_in_columns_while) <-- контрольная функция
        
        1    0.000    0.000    0.025    0.025 task_1.py:69(main)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
    10304    0.001    0.000    0.001    0.000 {built-in method builtins.len}
    10200    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12764    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


# Матрица 1000х100
def main_r1000_c100():
    m = for_cycle_in_range(1000, 100)
    min_in_columns_enum(m)
    min_in_columns_while(m)
    min_in_columns_range(m)
    # max_number(min_in_col_en)


# Матрица 1000х1000
def main_r1000_c1000():
    m = for_cycle_in_range(1000, 1000)
    min_in_columns_enum(m)
    min_in_columns_while(m)
    min_in_columns_range(m)
    # max_number(min_in_col_en)


# Матрица 10 000х1000
def main_r10000_c1000():
    m = for_cycle_in_range(10000, 1000)
    min_in_columns_enum(m)
    min_in_columns_while(m)
    min_in_columns_range(m)
    # max_number(min_in_col_en)


# Матрица 10 000х10 000
def main_r10000_c10000():
    m = for_cycle_in_range(10_000, 10_000)
    min_in_columns_enum(m)
    min_in_columns_while(m)
    min_in_columns_range(m)
    # max_number(min_in_col_en)


if __name__ == '__main__':
    cProfile.run('main_r100_c100()')
    cProfile.run('main_r1000_c100()')
    cProfile.run('main_r1000_c1000()')
    cProfile.run('main_r10000_c1000()')
    cProfile.run('main_r10000_c10000()')
