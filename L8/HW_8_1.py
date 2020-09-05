# Задача 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


import hashlib


def count_substring(user_str=None):

    if user_str == None:
        user_str = input('\nВведите строку в которой хотите подсчитать количество подстрок - ')

    set_count_substring = set()

    for start_cut in range(len(user_str)):
        for end_cut in range(start_cut + 1, len(user_str) + 1):
            set_count_substring.add(hashlib.md5(bytes(user_str[start_cut:end_cut].encode('utf-8'))).hexdigest())

    print(f'\nВведена строка "{user_str}"\n'
          f'Количество подстрок в строке - {len(set_count_substring) - 1}')


count_substring('papa')

count_substring('sova')

count_substring()
