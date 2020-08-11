# № 1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/109_M7YCkK7xQU52gocBuW9Qo7q-KuAX3/view?usp=sharing

user_number = input('Введите целое трехзначное число - ')

sum_user_number = int(user_number[0]) + int(user_number[1]) + int(user_number[2])

multi_user_number = int(user_number[0]) * int(user_number[1]) * int(user_number[2])

print(f'Сумма чисел введеного числа {user_number} равна {sum_user_number}')
print(f'Произведение чисел введеного числа {user_number} равна {multi_user_number}')
