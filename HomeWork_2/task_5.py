"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

START_NUMBER = 32
FINISH_NUMBER = 127
COLUMNS_IN_ROW = 10

for i in range(START_NUMBER, FINISH_NUMBER + 1):
    if (i - START_NUMBER + 1) % COLUMNS_IN_ROW:
        print(f'{i}:"{chr(i)}"', end=" ")
    else:
        print(f'{i}:"{chr(i)}"')
