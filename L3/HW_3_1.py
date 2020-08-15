# Задача №1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from f_hub import sequence_list_int_number

base_start = 2
base_stop = 99
base_step = 1

list_base_gen = sequence_list_int_number(base_start, base_stop, base_step)

diversity_start = 2
diversity_stop = 9
diversity_step = 1

list_diversity_gen = sequence_list_int_number(diversity_start, diversity_stop, diversity_step)

print(f'\nЧисла в диапазоне от {base_start} до {base_stop} с шагом {base_step} кратны числам '
      f'в диапазоне от {diversity_start} до {diversity_stop} с шагом {diversity_step}:')

for i_diversity in list_diversity_gen:
    score_diversity = 0
    for i_base in list_base_gen:
        if i_base % i_diversity == 0:
            score_diversity += 1
    print(f'Числу {i_diversity} кратно - {score_diversity} чисел/ла.')