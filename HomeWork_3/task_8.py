"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROWS = 5
COLUMNS = 4

matrix = []
for i in range(ROWS):
    r = []
    sum_ = 0
    for j in range(COLUMNS - 1):
        n = int(input(f'Введите {j + 1}-й элемент строки {i + 1}: '))
        r.append(n)
        sum_ += n
    r.append(sum_)
    matrix.append(r)

for row in matrix:
    for col in row:
        print(col, end='\t')
    print()
