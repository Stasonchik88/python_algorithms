"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.

Пример работы функции:
func("papa")
6
func("sova")
9
"""
import hashlib


def num_sub_str(inp_str):
    h_subs = []
    for i in range(1, len(inp_str)):
        for j in range(len(inp_str) - i + 1):
            # print(inp_str[j:j+i])
            h_sub = hashlib.sha1(inp_str[j:j+i].encode('utf-8')).hexdigest()
            if h_sub not in h_subs:
                h_subs.append(h_sub)
    return len(h_subs)


print(f'Количество уникальных подстрок в введенной строке: {num_sub_str("papa")}')
print(f'Количество уникальных подстрок в введенной строке: {num_sub_str("sova")}')
