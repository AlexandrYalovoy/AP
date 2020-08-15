# Задача №2 Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
# заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.

from f_hub import random_list_int_number

list_gen_min = 1
list_gen_max = 20
list_gen_len = 10

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

list_even_number_index = []

for i in range(len(list_random_gen)):
    if list_random_gen[i] % 2 == 0:
        list_even_number_index.append(i)

print(f'\nВ списке {list_random_gen}'
      f'\nЧетные числа находятся на индексах {list_even_number_index}')