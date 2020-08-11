# №5 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

# https://drive.google.com/file/d/109_M7YCkK7xQU52gocBuW9Qo7q-KuAX3/view?usp=sharing

import math

alphabet_tuple = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
                  'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')

print(f'Добрый день мой приятный юзверь!\n'
      f'Тебя приветсвует программа которая выводит сколько цифр в русском алфовите между,\n'
      f'указанными тобой цифрами\n'
      f'английские буквы искать нельзя, они не входят в область применения данного ПО.')

print('')

users_symbol_1 = input('Введите первую букву Русского алфавита - ').upper()

users_symbol_2 = input('Введите первую букву Русского алфавита - ').upper()

print('')

symbol_number_1 = alphabet_tuple.index(users_symbol_1) + 1
symbol_number_2 = alphabet_tuple.index(users_symbol_2) + 1

symbol_q = math.fabs(symbol_number_1 - symbol_number_2) - 1

print(f'При введении букв {users_symbol_1} и {users_symbol_2}, количество букв между символами'
      f'согласно алфавита {symbol_q}')
