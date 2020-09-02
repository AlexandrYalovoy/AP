# Задача 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sorting(array):
    """
    Функция принимает на вход список после рекурсивно разбирает его на части,
    сортирует элементарные массивы, потом обьеденяет их сортирует повторно
    Принцип основан на сортировке малых элементарных массивов и их слияние
    с последующей сортировкой
    :param array:
    :return:
    возврашает отсортированный список
    """

    # Говорим что если массив из одного числа то ничего не меняем оно  и так упорядочено
    if len(array) <= 1:
        return array

    # говорим что левая часть равна срезу массива от начала до его половины, вызов рекурсивен
    left_part = merge_sorting(array[:len(array) // 2])
    # говорим что правая часть равна срезу массива от его половины до конца, вызов рукурсивен
    right_part = merge_sorting(array[len(array) // 2:])

    i, j = 0, 0

    while len(left_part) > i and len(right_part) > j:
        if left_part[i] < right_part[j]:
            array[i + j] = left_part[i]
            i += 1
        else:
            array[i + j] = right_part[j]
            j += 1

    while len(left_part) > i:
        array[i + j] = left_part[i]
        i += 1
    while len(right_part) > j:
        array[i + j] = right_part[j]
        j += 1

    return array


MIN_NUMBER = 0
MAX_NUMBER = 50
SIZE = 10
list_for_sort = [round(random.uniform(MIN_NUMBER, MAX_NUMBER), 3) for _ in range(SIZE)]

print(list_for_sort)

merge_sorting(list_for_sort)

print(list_for_sort)
