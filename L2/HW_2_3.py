# Задание 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# https://drive.google.com/file/d/1TlHmNcm6ELkpap5gX5s3lKAS7DHeJTZD/view?usp=sharing


def number_reverse(user_number):
    """
    Функция которая математически разворачивает число, откусывет кусочик с конца
    умножает его на 10 потом к этому кусочку прибавляет 2 которое уже первое число с конца
    и так по циклу пока не соберет число к заду на перед
    :param
    user_number - число пользователя целочисленное натуральное :
    :return вертает обратное число:
    """
    MAGIC_NUMBER = 10
    r_number = 0
    o_number = user_number

    while len(str(r_number)) != len(str(user_number)):
        r_number = (r_number * MAGIC_NUMBER) + (o_number % MAGIC_NUMBER)
        o_number //= MAGIC_NUMBER

    return r_number


print('Добрый день юзверь. Это ПО служит для разворота введеного тобой цисла. Приступим.')

user_number = int(input('\nВведите целое положительное число любой длины - '))

reversed_user_number = number_reverse(user_number)

print(f'\nПри введенном числе {user_number} развернутое число будет {reversed_user_number}')
