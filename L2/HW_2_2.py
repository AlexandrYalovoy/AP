# Задание №2 Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

# https://drive.google.com/file/d/1TlHmNcm6ELkpap5gX5s3lKAS7DHeJTZD/view?usp=sharing

def quantity_even_odd_number(user_number):
    iteration = 0
    r_dev = 10
    int_dev = 1
    even_number = 0
    odd_number = 0

    while iteration < len(str(user_number)):
        result = user_number % r_dev // int_dev

        if result % 2 == 0:
            even_number += 1
        else:
            odd_number += 1

        r_dev *= 10
        int_dev *= 10

        iteration += 1

    return even_number, odd_number


print('\nПривет пользователь, данная программа подсчитает количество четных и нечетных цифр\n'
      'в веденном тобой числе, приступим.\n')

user_number = int(input('Введите челое полительное число любой длины - '))

even_number, odd_number = quantity_even_odd_number(user_number)

print(f'\nВ числе {user_number}, четных цифр - {even_number}, нечетных цифр - {odd_number}.')
