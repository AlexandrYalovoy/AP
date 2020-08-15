# Задание №3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from f_hub import random_list_int_number

list_gen_min = 1
list_gen_max = 20
list_gen_len = 5

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

min_number = list_random_gen[0]
min_index_number = None

max_number = list_random_gen[0]
max_index_number = None

for i in range(len(list_random_gen)):
    if min_number >= list_random_gen[i]:
        min_number = list_random_gen[i]
        min_index_number = i

    if max_number <= list_random_gen[i]:
        max_number = list_random_gen[i]
        max_index_number = i

print(f'Сгенерирован список - {list_random_gen}')
print(f'Минимальное число в нем - {min_number} с индексом {min_index_number}.')
print(f'Максимальное число в нем {max_number} с индексом {max_index_number}.')

list_random_gen[min_index_number] = max_number

list_random_gen[max_index_number] = min_number

print(f'Список с рокировкой макс и мин числа - {list_random_gen}')