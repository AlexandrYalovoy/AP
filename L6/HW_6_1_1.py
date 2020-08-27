# Задание 3.4 Определить, какое число в массиве встречается чаще всего (Вариант 1)


from f_hub import random_list_int_number
from f_hub import sequence_list_int_number
from f_hub import get_sum_all_variables_size

list_gen_min = 1
list_gen_max = 9
list_gen_len = 20

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

base_start = 1
base_stop = 9
base_step = 1

list_base_gen = sequence_list_int_number(base_start, base_stop, base_step)

info_dict = {}

for i_base in list_base_gen:
    count = 0
    for i_gen in list_random_gen:
        if i_base == i_gen:
            count += 1
    info_dict[i_base] = count

print(f'\nСгенерированный список:\n{list_random_gen}')
print(f'\nЧисла которые ищем:\n{list_base_gen}')
print(f'\nСловарь (число : количество в списке):\n{info_dict}')

comparison_number = info_dict[list_base_gen[0]]
most_common_number = None

for k, v in info_dict.items():
    if v >= comparison_number:
        comparison_number = v
        most_common_number = k


print(f'\nСамое встречающиеся число - {most_common_number}')


size = get_sum_all_variables_size(list(globals()))

print(f'\nКоличество памяти занятой в RAM перменными {size} байт.')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Вариант №1
#
# Сгенерированный список:
# [6, 9, 5, 8, 7, 8, 5, 9, 4, 8, 9, 3, 7, 3, 5, 1, 4, 4, 2, 7]
#
# Числа которые ищем:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Словарь (число : количество в списке):
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 1, 7: 3, 8: 3, 9: 3}
#
# Самое встречающиеся число - 9
#
# Количество памяти занятой в RAM перменными 1015 байт.
# Python 3.8.3  32 bit
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
