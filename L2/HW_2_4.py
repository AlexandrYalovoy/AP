# Задание 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1TlHmNcm6ELkpap5gX5s3lKAS7DHeJTZD/view?usp=sharing

def sum_half_number_range(user_long_range, start_number=1):
    """
    Функция которая получает сумму элементов длиной user_long_range где каждый элемент с шагом * -0,5
    :param
    user_long_range - длина последовательности:
    :param
    start_number - стартовое число дефолт 1:
    :return вертает сумму последовательности:
    """
    sum_half_number = 0
    MULTIPLIER = -0.5

    for i in range(user_long_range):
        sum_half_number += start_number
        start_number *= MULTIPLIER

    return sum_half_number


print('\nТебя приветствует ПО для получения суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125...')

user_range = int(input('\nВведи длину последовательности - '))

sum_half = sum_half_number_range(user_range)

print(f'\nСумма последовательности равна {sum_half}')

