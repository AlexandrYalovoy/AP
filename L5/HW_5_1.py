# Задание №1 Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections


quantity_reports = 4  # Хранит количество отчетных периудов

quantity_firms = int(input('Введите количество предприятий - '))

count_lucky = 0  # Хранит количество предприятий с выручкой выше средней

list_lucky_firm = []  # Хранит названия предприятий выше средней выручки

profit_firms = collections.Counter()  # Хранит название предприятия (ключ) и выручку (значение)

for num in range(1, quantity_firms + 1):
    name_firm = input(f'Введите название {num} предприятия - ')
    for quarter in range(1, quantity_reports + 1):
        profit_firms[name_firm] = int(input(f'Введите выручку за {quarter} кваратл в рублях - '))

sum_all_profit = sum(profit_firms.values())

average_profit = sum_all_profit / quantity_firms

for key, values in profit_firms.items():
    if values >= average_profit:
        count_lucky += 1
        list_lucky_firm.append(key)

print(f'\nВсего фирм в базе - {quantity_firms}.\n'
      f'Общая выручка составила - {sum_all_profit} рублей.\n'
      f'Средня выручка составила - {average_profit} рублей.\n'
      f'Фирмы выручка которых выше среднего - {", ".join(list_lucky_firm)}')
