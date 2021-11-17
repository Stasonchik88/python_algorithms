"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections
data_for_companies = collections.defaultdict(list)
count_companies = int(input('Введите количество предприятий: '))

average_profit = 0
for n in range(count_companies):
    name_company = input('Введите название компании: ')
    for quarter in range(1, 5):
        profit_in_quarter = float(input(f'Введите прибыль компании "{name_company}" в {quarter}-м квартале: '))
        data_for_companies[name_company].append(profit_in_quarter)
        average_profit += profit_in_quarter / count_companies

# Вариант 1
high_companies = [company for company, profit in data_for_companies.items() if sum(profit) > average_profit]
# Вариант 2
low_companies = dict(filter(lambda x: sum(x[1]) < average_profit, data_for_companies.items()))

print('Прибыльные компании:')
print(*high_companies)
print('Убыточные компании:')
print(*low_companies.keys())
