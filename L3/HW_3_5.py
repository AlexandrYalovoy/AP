# Задание №5 В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте
# «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

from f_hub import random_list_int_number

list_gen_min = -9
list_gen_max = 9
list_gen_len = 10

list_random_gen = random_list_int_number(list_gen_min, list_gen_max, list_gen_len)

print(f'\nСгенерированный список:\n{list_random_gen}')

min_number = list_gen_min
min_number_index = None

for i in range(len(list_random_gen)):
    if list_random_gen[i] < 0 and list_random_gen[i] > min_number:
        min_number = list_random_gen[i]
        min_number_index = i

print(f'\nМаксимальное из минимальных чисел в списке {min_number} с индексом {min_number_index}.')
