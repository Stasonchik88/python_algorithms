"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def even_odd(n):
    even = 0
    odd = 0
    if n >= 10:
        even, odd = even_odd(n // 10)
    num = n % 10
    if num % 2:
        return even, odd + 1
    else:
        return even + 1, odd


x = int(input("Введите число: "))
even, odd = even_odd(x)
print(f'Количество четных цифр: {even}, количество нечетных цифр: {odd}')