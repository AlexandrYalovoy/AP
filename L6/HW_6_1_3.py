# Задание 3.4 Определить, какое число в массиве встречается чаще всего (Вариант 3)

import collections
from f_hub import random_list_int_number
from f_hub import get_sum_all_variables_size

list_gen_min = 1
list_gen_max = 9
list_gen_len = 20

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

info_list = [-1]

most_c_n = -1

for i_base in range(list_gen_min, list_gen_max + 1):
    if list_random_gen.count(i_base) > most_c_n:
        most_c_n = list_random_gen.count(i_base)
        info_list[0] = i_base

print(f'\nСгенерированный список:\n{list_random_gen}')

# print(f'\nСловарь (число : количество в списке):\n{collections.Counter(list_random_gen)}')  # для проверки

print(f'\nСамое встречающиеся число - {info_list}')

size = get_sum_all_variables_size(list(globals()))

print(f'\nКоличество памяти занятой в RAM перменными {size} байт.')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Вариант №3
# Сгенерированный список:
# [9, 2, 2, 2, 1, 4, 7, 4, 9, 9, 1, 6, 2, 7, 7, 9, 5, 2, 9, 8]
#
# Самое встречающиеся число - [2]
#
# Количество памяти занятой в RAM перменными 697 байт.
# Python 3.8.3  32 bit
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
