# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких
# N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Задание №3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

# Сначала нагенерирую 5 списков 100, 1000, 10000, 100000, 1000000 элементов.
# Для чистоты экспперемента все варианты будут проходиться по 5 одинаковым но сгенерированным спискам

import copy

import timeit

import cProfile

from f_hub import random_list_int_number

list_gen_min = 1
list_gen_max = 20
list_gen_len = 5

test_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

list_gen_min = -100
list_gen_max = 100
list_gen_len = 100

t_1_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)  # 0.0094927
# print(timeit.timeit('random_list_int_number(list_gen_min, list_gen_max, list_gen_len)',
#                     globals=globals(), number=100))

list_gen_len = 1000

t_2_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)  # 0.0956913
# print(timeit.timeit('random_list_int_number(list_gen_min, list_gen_max, list_gen_len)',
#                     globals=globals(), number=100))

list_gen_len = 10000

t_3_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)  # 0.9549424
# print(timeit.timeit('random_list_int_number(list_gen_min, list_gen_max, list_gen_len)',
#                     globals=globals(), number=100))

list_gen_len = 100000

t_4_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)  # 9.572761700000001
# print(timeit.timeit('random_list_int_number(list_gen_min, list_gen_max, list_gen_len)',
#                     globals=globals(), number=100))

list_gen_len = 1000000

t_5_list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)  # 96.8439958
# print(timeit.timeit('random_list_int_number(list_gen_min, list_gen_max, list_gen_len)',
#                     globals=globals(), number=100))

# Вариант № 1 так как решал в домашнем задании
print('Вариант № 1 так как решал в домашнем задании')


def choice_one(list_random_gen):
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

    # print(f'Сгенерирован список - {list_random_gen}')
    # print(f'Минимальное число в нем - {min_number} с индексом {min_index_number}.')
    # print(f'Максимальное число в нем {max_number} с индексом {max_index_number}.')

    list_random_gen[min_index_number] = max_number

    list_random_gen[max_index_number] = min_number

    # print(f'Список с рокировкой макс и мин числа - {list_random_gen}')


print(timeit.timeit('choice_one(t_1_list_random_gen)', globals=globals(), number=1000))  # 0.011028600000000166

print(timeit.timeit('choice_one(t_2_list_random_gen)', globals=globals(), number=1000))  # 0.12315649999999989

print(timeit.timeit('choice_one(t_3_list_random_gen)', globals=globals(), number=1000))  # 1.2950809999999997

print(timeit.timeit('choice_one(t_4_list_random_gen)', globals=globals(), number=1000))  # 13.9948016

print(timeit.timeit('choice_one(t_5_list_random_gen)', globals=globals(), number=1000))  # 145.0667292

cProfile.run('choice_one(t_1_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:67(choice_one)
cProfile.run('choice_one(t_2_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:67(choice_one)
cProfile.run('choice_one(t_3_list_random_gen)')
# 1    0.001    0.001    0.001    0.001 HW_4_1.py:67(choice_one)
cProfile.run('choice_one(t_4_list_random_gen)')
# 1    0.014    0.014    0.014    0.014 HW_4_1.py:67(choice_one)
cProfile.run('choice_one(t_5_list_random_gen)')
# 1    0.144    0.144    0.144    0.144 HW_4_1.py:67(choice_one)

# Вариант № 2 max / min
print('Вариант № 2 max / min')


def choice_two(list_random_gen):

    min_number = min(list_random_gen)
    min_index_number = list_random_gen.index(min_number)

    max_number = max(list_random_gen)
    max_index_number = list_random_gen.index(max_number)

    # print(f'Сгенерирован список - {list_random_gen}')
    # print(f'Минимальное число в нем - {min_number} с индексом {min_index_number}.')
    # print(f'Максимальное число в нем {max_number} с индексом {max_index_number}.')

    list_random_gen[min_index_number] = max_number

    list_random_gen[max_index_number] = min_number

    # print(f'Список с рокировкой макс и мин числа - {list_random_gen}')


print(timeit.timeit('choice_two(t_1_list_random_gen)', globals=globals(), number=1000))  # 0.0064765999999849555

print(timeit.timeit('choice_two(t_2_list_random_gen)', globals=globals(), number=1000))  # 0.0553893999999957

print(timeit.timeit('choice_two(t_3_list_random_gen)', globals=globals(), number=1000))  # 0.5261370999999997

print(timeit.timeit('choice_two(t_4_list_random_gen)', globals=globals(), number=1000))  # 5.1157915

print(timeit.timeit('choice_two(t_5_list_random_gen)', globals=globals(), number=1000))  # 50.901953899999995

cProfile.run('choice_two(t_1_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:119(choice_two)
cProfile.run('choice_two(t_2_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:119(choice_two)
cProfile.run('choice_two(t_3_list_random_gen)')
# 1    0.000    0.000    0.001    0.001 HW_4_1.py:119(choice_two)
cProfile.run('choice_two(t_4_list_random_gen)')
# 1    0.000    0.000    0.005    0.005 HW_4_1.py:119(choice_two)
cProfile.run('choice_two(t_5_list_random_gen)')
# 1    0.000    0.000    0.050    0.050 HW_4_1.py:119(choice_two)

# Вариант № 3 сортировка и взятие 0 и -1 символа
print('Вариант № 3 сортировка и взятие 0 и -1 символа')


def choice_three(list_random_gen):

    sort_list_random_gen = copy.copy(list_random_gen)

    sort_list_random_gen.sort()

    min_index_number = 0
    min_number = sort_list_random_gen[min_index_number]

    max_index_number = -1
    max_number = sort_list_random_gen[max_index_number]

    # print(f'Сгенерирован список - {list_random_gen}')

    min_i = list_random_gen.index(min_number)
    max_i = list_random_gen.index(max_number)

    list_random_gen[max_i] = min_number
    list_random_gen[min_i] = max_number

    # print(f'Минимальное число в нем - {min_number} с индексом {min_i}.')
    # print(f'Максимальное число в нем {max_number} с индексом {max_i}.')
    # print(f'Список с рокировкой макс и мин числа - {list_random_gen}')


print(timeit.timeit('choice_three(t_1_list_random_gen)', globals=globals(), number=1000))  # 0.005065900000005286

print(timeit.timeit('choice_three(t_2_list_random_gen)', globals=globals(), number=1000))  # 0.08948910000000865

print(timeit.timeit('choice_three(t_3_list_random_gen)', globals=globals(), number=1000))  # 1.1123891999999955

print(timeit.timeit('choice_three(t_4_list_random_gen)', globals=globals(), number=1000))  # 11.731289199999992

print(timeit.timeit('choice_three(t_5_list_random_gen)', globals=globals(), number=1000))  # 123.60189689999999

cProfile.run('choice_three(t_1_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:163(choice_three)
cProfile.run('choice_three(t_2_list_random_gen)')
# 1    0.000    0.000    0.000    0.000 HW_4_1.py:163(choice_three)
cProfile.run('choice_three(t_3_list_random_gen)')
# 1    0.000    0.000    0.001    0.001 HW_4_1.py:163(choice_three)
cProfile.run('choice_three(t_4_list_random_gen)')
# 1    0.000    0.000    0.012    0.012 HW_4_1.py:163(choice_three)
cProfile.run('choice_three(t_5_list_random_gen)')
# 1    0.000    0.000    0.119    0.119 HW_4_1.py:163(choice_three)
# --------------------------------------------------------------------------------------------------------------------


# Вывод:
# https://docs.google.com/spreadsheets/d/e/2PACX-1vQWhcPESDj563_wy4lEVvbZ2pFlR_02AAfDC5rK84YSnM6IYuOkL6A5fIIErT1N2WZ3vNqV6riKcfPh/pub?output=pdf
# Ссылка на сравнение времени выполнения приведеных вариантов
# Из сего видно что вариант с применением коробочных функций мин и макс самый быстрый, рост времени на выполнение
# так же самый низкий
# Зависимость во всех вариантах линейная.