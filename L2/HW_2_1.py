# Задание №1 Написать программу, которая будет складывать, вычитать, умножать или делить два
# числа. Числа и знак операции вводятся пользователем. После выполнения вычисления
# программа не завершается, а запрашивает новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа
# должна сообщать об ошибке и снова запрашивать знак операции. Также она должна
# сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1TlHmNcm6ELkpap5gX5s3lKAS7DHeJTZD/view?usp=sharing

def check_number_s_range(start_number, text):
    while True:
        result = int(input(text))

        if result >= start_number:
            break
        else:
            print('Ошибка, введи число соглано условию!')

    return result


print('Добрый день мой хороший идеальный пользователь!\n'
      'Тебя приветсвует программа типа калькулятор но не полноценный.\n'
      'От тебя прийдется сначало определиться что ты будешь делать и выбрать из приведенных возможностей\n'
      'а после ввести 2 числа с которыми удет происходить магия!\n')

while True:

    while True:
        print('Выбери какой тип операций мы будем выполнять:\n'
              '" + " - операция сложения;\n'
              '" - " - операция вычитания;\n'
              '" * " - операция умножения;\n'
              '" / " -  операция деления;\n'
              '" 0 " -  операция завершения программы.\n')

        iter_operator = input('Введите оператор без ковычек - ')

        if iter_operator == '+' or iter_operator == '-' or iter_operator == '*'\
                or iter_operator == '/' or iter_operator == '0':
            break
        else:
            print('Некорректный вод, прошу быть внимательней!\n')

    if iter_operator == '0':
        break

    arg_1 = check_number_s_range(0, 'Введите 1 число >= 0 - ')
    arg_2 = check_number_s_range(1, 'Введите 2 число >= 1 - ')

    if iter_operator == '+':
        print(f'\nРезультат: {arg_1} {iter_operator} {arg_1} = {arg_1 + arg_2}\n')
    elif iter_operator == '-':
        print(f'\nРезультат: {arg_1} {iter_operator} {arg_1} = {arg_1 - arg_2}\n')
    elif iter_operator == '*':
        print(f'\nРезультат: {arg_1} {iter_operator} {arg_1} = {arg_1 * arg_2}\n')
    else:
        print(f'\nРезультат: {arg_1} {iter_operator} {arg_1} = {arg_1 / arg_2}\n')


