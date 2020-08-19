# Сюда буду складывать функции которые будут применяться более чем в 1 файле

import random


def random_list_int_number(min_number, max_number, len_list):
    """
    Функция которая генерирует список из чисел целочисленного типа

    :param
    min_number - минимальное число в списке:
    :param
    max_number - максимальное число в списке :
    :param
    len_list - длина списка:
    :return возврашает сгенерированный список согласно условиям:
    """
    list_gen = [random.randint(min_number, max_number) for _ in range(len_list)]
    return list_gen


def sequence_list_int_number(start_number, end_number, step_gen=1):
    """
    Функция которая генерирует последовательность из чисел целочисленного типа в список

    :param
    start_number - начальное значение последовательности включительно:
    :param
    end_number - конечное значение последовательности включительно:
    :param
    step_gen - шаг последовательности:
    :return возврашает сгенерированный список согласно условиям:
    """
    list_gen = [i for i in range(start_number, end_number + 1, step_gen)]
    return list_gen


if __name__ == '__main__':
    print('Файлик с функциями, тут нечего запускать, от сюда надо брать.')

    print('\nrandom_list_int_number(1, 10, 5)')
    test_random_list_int_number = random_list_int_number(1, 10, 5)
    print(f'{test_random_list_int_number=}')

    print('\nsequence_list_int_number(1, 10, 1)')
    test_sequence_list_int_number = sequence_list_int_number(1, 10, 1)
    print(f'{test_sequence_list_int_number=}')

