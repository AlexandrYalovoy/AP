# Задание №2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections
import timeit
import cProfile


def alignment_positions(first, second):
    """

    Функуия которая принимает два HEX числа срокового типа, преобразует его в collections.deque
    после сверяет длину символов, большее назначается 1 числом, меньшее вторым.
    После меньше число дополняется слева нулями до размера большего числа

    Пример:
    1) на вход переданы строки first = 'A2' и second = 'C4F' они преобразуется
    в first = deque(['A', '2']) и second = deque(['C', '4', 'F'])
    2) сравнивается длина len(first) < len(second) и по условию происходит рокировка
    следовательно first = deque(['C', '4', 'F']) second = deque(['A', '2'])
    3) second = deque(['A', '2']) подгоняется к размеру first = deque(['C', '4', 'F'])
    и преобразуется в second = deque(['0', 'A', '2'])

    :param
    first: - первое HEX число срокового типа на вход
    :param
    second: - второе HEX число срокового типа на вход
    :return:
    возврашает две deque с преобразованиями согласно описания
    """

    first = collections.deque(first)
    second = collections.deque(second)

    if len(first) < len(second):
        first, second = second, first

    quantity_add_left_zero = len(first) - len(second)

    if quantity_add_left_zero != 0:
        for _ in range(quantity_add_left_zero):
            second.appendleft('0')

    return first, second


def sum_hex_number(user_number_first, user_number_second):
    """
    Функция для нахождения суммы двух HEX чисел графическим способом. (Встроенные функции запрешены преподователем)

    Функция принимает на вход два HEX числа срокового типа, отдает их на преобразование функции alignment_positions
    Далее происходи их сложение на основании логически-графического линейного сложения
    по sum_mask = collections.defaultdict(int)
    Пример:
    1) на вход переданы строки first = 'A2' и second = 'C4F' они преобразуется согласно функции alignment_positions
    2) происходит их логически-графическое линейное сложение
    deque(['C', '4', 'F']) + deque(['0', 'A', '2']) = deque(['C', 'F', '1'])
    3) происходит преобразование ответа в строковый тип удобный для вывода пользователю
    :param
    user_number_first: - первое HEX число срокового типа на вход
    :param
    user_number_second: - второе HEX число срокового типа на вход
    :return:
    Возврашает результат сложения двух HEX чисел в строком типе
    """

    a, b = alignment_positions(user_number_first, user_number_second)

    result_f = collections.deque()
    unit_mind = 0

    for index in range(-1, -len(a) - 1, -1):
        spam_sum_up = sum_mask[a[index]]
        spam_sum_down = sum_mask[b[index]]

        spam_res = spam_sum_up + spam_sum_down + unit_mind

        if unit_mind != 0:
            unit_mind = 0

        if spam_res > 15:
            spam_res -= 16
            unit_mind += 1

        for key, value in sum_mask.items():
            if value == spam_res:
                result_f.appendleft(key)

    return ''.join(result_f)


# коллекция которая должна быть инициализирована по умолчанию и храниться в памяти,
# необходима для работы функции sum_hex_number
sum_mask = collections.defaultdict(int)
mask_str = '0123456789ABCDEF'
score = 0
for i in mask_str:
    sum_mask[i] = score
    score += 1

#####################################################################################################################
print(f'\nТестовый пример №1(сложение HEX чисел):')

user_num_first = 'A2'

user_num_second = 'C4F'

result = sum_hex_number(user_num_first, user_num_second)

print(f'Сумма числа {user_num_first} и {user_num_second} будет равна {result}')
#####################################################################################################################
print(f'\nТестовый пример №2(сложение HEX чисел):')

user_num_first = '3A5'

user_num_second = '3E8'

result = sum_hex_number(user_num_first, user_num_second)

print(f'Сумма числа {user_num_first} и {user_num_second} будет равна {result}')
#####################################################################################################################
print(f'\nПользовательский ввод для сложения HEX чисел:')

user_num_first = input('Введите первое HEX число - ').upper()

user_num_second = input('Введите второе HEX число - ').upper()

result = sum_hex_number(user_num_first, user_num_second)

print(f'Сумма числа {user_num_first} и {user_num_second} будет равна {result}')
#####################################################################################################################

# print(timeit.timeit('sum_hex_number("3039", "3039")', number=1000, globals=globals()))  # 0.007008500000000001
#
# print(timeit.timeit('sum_hex_number("1E240", "1E240")', number=1000, globals=globals()))  # 0.008022299999999996
#
# print(timeit.timeit('sum_hex_number("12D687", "12D687")', number=1000, globals=globals()))  # 0.009568300000000002
#
# print(timeit.timeit('sum_hex_number("BC614E", "BC614E")', number=1000, globals=globals()))  # 0.009543700000000002
#
# print(timeit.timeit('sum_hex_number("75BCD15", "75BCD15")', number=1000, globals=globals()))  # 0.014219300000000004
#
# cProfile.run('sum_hex_number("3E8", "3E8")')
# # 1    0.000    0.000    0.000    0.000 HW_5_2.py:50(sum_hex_number)
# cProfile.run('sum_hex_number("2710", "2710")')
# # 1    0.000    0.000    0.000    0.000 HW_5_2.py:50(sum_hex_number)
# cProfile.run('sum_hex_number("186A0", "186A0")')
# # 1    0.000    0.000    0.000    0.000 HW_5_2.py:50(sum_hex_number)
# cProfile.run('sum_hex_number("F4240", "F4240")')
# # 1    0.000    0.000    0.000    0.000 HW_5_2.py:50(sum_hex_number)
# cProfile.run('sum_hex_number("989680", "989680")')
# # 1    0.000    0.000    0.000    0.000 HW_5_2.py:50(sum_hex_number)
