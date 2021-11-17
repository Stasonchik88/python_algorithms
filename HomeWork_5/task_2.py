"""
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
hex_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_sum(first, second):
    first = first.copy()
    second = second.copy()

    diff_len = len(second) - len(first)
    if diff_len > 0:
        first.extendleft(['0'] * diff_len)
    elif diff_len < 0:
        second.extendleft(['0'] * diff_len)

    overrun = 0
    result = collections.deque([])
    for _ in range(len(first)):
        sum_ = hex_tuple.index(first.pop()) + hex_tuple.index(second.pop()) + overrun
        overrun = sum_ // len(hex_tuple)
        remainder = sum_ % len(hex_tuple)

        result.appendleft(hex_tuple[remainder])
    if overrun:
        result.appendleft(hex_tuple[overrun])
    return result


def hex_mult(first_number, second_number):
    first = first_number.copy()
    res_1 = collections.deque([])  # i-е слагаемое от умножения
    degree = []  # Учет разрядности числа
    for _ in range(len(first)):
        second = second_number.copy()
        res_2 = collections.deque([])  # (i+1)-е слагаемое от умножения
        overrun = 0  # В уме
        n_1 = first.pop()  # i-я цифра первого числа
        for _ in range(len(second)):
            n_2 = second.pop()  # j-я цифра второго числа

            mult_ = hex_tuple.index(n_1) * hex_tuple.index(n_2) + overrun
            overrun = mult_ // len(hex_tuple)
            remainder = mult_ % len(hex_tuple)

            res_2.appendleft(hex_tuple[remainder])
        if overrun:
            res_2.appendleft(hex_tuple[overrun])

        res_2.extend(degree)  # Умножение на 10**i
        res_1 = hex_sum(res_1, res_2)  # Попарное сложение результатов умножения
        degree.append('0')  # Переход к следующему разряду
    return res_1


first_number = input('Введите первое число: ').upper()
second_number = input('Введите второе число: ').upper()
first_number = collections.deque(first_number)
second_number = collections.deque(second_number)

print(hex_sum(first_number, second_number))
print(hex_mult(first_number, second_number))