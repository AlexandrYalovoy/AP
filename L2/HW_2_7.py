# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

# https://drive.google.com/file/d/1TlHmNcm6ELkpap5gX5s3lKAS7DHeJTZD/view?usp=sharing

def r_left(user_number):
    """
    Хитрая подсмотренная рекурсия.
    То ли я слишком тупенький но до рекурсий додумываться мне сложно а как работает понимаю

    Функйия находит сумму последовательности типа 1+2+...+n
    :param
    user_number - n число множества полученная от пользователя:
    :return сумму последовательности:
    """

    if user_number == 1:
        return user_number

    sum_user_number = user_number + r_left(user_number - 1)
    return sum_user_number


print('\nТебя приветсвует ПО для расчета равенства 1+2+...+n = n(n+1)/2, где n — любое натуральное число')

user_number = int(input('\nВведи натуральное n число для получения множества - '))

l_part = r_left(user_number)
r_part = (user_number * (user_number + 1)) / 2

print(f'Сумма левой части {l_part}, вычисление правой части {r_part}, '
      f'части {"равны" if l_part == r_part else "не равны"}')
