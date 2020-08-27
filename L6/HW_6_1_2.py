# Задание 3.4 Определить, какое число в массиве встречается чаще всего (Вариант 2)

import collections
from f_hub import random_list_int_number
from f_hub import get_sum_all_variables_size

list_gen_min = 1
list_gen_max = 9
list_gen_len = 20

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

# common_number = collections.Counter(list_random_gen)   # строчка для возможности принта каунтера 1/2

print(f'\nСгенерированный список:\n{list_random_gen}')

# print(f'\nСловарь (число : количество в списке):\n{common_number}')  # строчка для возможности принта каунтера 2/2

most_common_number = collections.Counter(list_random_gen).most_common(1)[0][0]

print(f'\nСамое встречающиеся число - {most_common_number}')

size = get_sum_all_variables_size(list(globals()))

print(f'\nКоличество памяти занятой в RAM перменными {size} байт.')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Вариант №2
#
# Сгенерированный список:
# [5, 1, 1, 7, 2, 8, 7, 5, 9, 6, 6, 2, 3, 3, 1, 8, 1, 6, 9, 6]
#
# Самое встречающиеся число - 1
#
# Количество памяти занятой в RAM перменными 642 байт.
# Python 3.8.3  32 bit
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
