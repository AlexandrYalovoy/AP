# Задача 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

import random


# def stooge_rec(data, i=0, j=None):
#     if j is None:
#         j = len(data) - 1
#     if data[j] < data[i]:
#         data[i], data[j] = data[j], data[i]
#     if j - i > 1:
#         t = (j - i + 1) // 3
#         stooge_rec(data, i, j - t)
#         stooge_rec(data, i + t, j)
#         stooge_rec(data, i, j - t)
#     return data


def stooge(data):
    """
    Функция для сортировки марионеточной и шизофреничной
    :param
    data: - массив на вход
    :return:
    Возвращает отсартированный массив
    """

    def stooge_rec(data, i=0, j=None):
        if j is None:
            j = len(data) - 1
        if data[j] < data[i]:
            data[i], data[j] = data[j], data[i]
        if j - i > 1:
            t = (j - i + 1) // 3
            stooge_rec(data, i, j - t)
            stooge_rec(data, i + t, j)
            stooge_rec(data, i, j - t)
        return data

    return stooge_rec(data, 0, len(data) - 1)


MIN_NUMBER = -100
MAX_NUMBER = 100
m = 2

list_for_sort = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2*m + 1)]

print('Массив до сортировки')
print(list_for_sort)
stooge(list_for_sort)
print('Массив после сортировки')
print(list_for_sort)
print(f'Медиана {list_for_sort[len(list_for_sort) // 2]}')
