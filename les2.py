# if условие:
#     pass
# elif условие:
#     pass
# else:

# print(not 125)
# print('c' in 'abs')

# a = 12345678901234567890
# b = 12345678901234567890
# print(a is b)


# a = {1, 2, 3}
# b = {1, 2, 3}
# print(a == b)
# print(a is b)

# c = a
# print(a is c)

# print(0 == None)
# print(sum({0, 0}))
# print(print())

# побитовые 

# или
# 0 1 0 1
# 0 0 1 0
# =======
# 0 1 1 1
# print(122 | True)

# A = int(input('Ваш возраст?  '))
# if A >= 18:
#     print('проходите')
# else:
#     print('уходите')
    
# Решение Вячеслава
# N = input('Как Вас зовут?\n')
# T = int(input('Который час?\n'))

# if 6 <= T and T < 12:
#     print(f'Доброе утро, {N}!')
#     # print('Доброе утро,', N, '!')
#     # print('Доброе утро, ' + N + '!')
# elif 12 <= T and T < 18:
#     print(f'Добрый день, {N}!')
# elif 18 <= T and T < 22:
#     print(f'Добрый вечер, {N}!')
# elif 22 <= T and T <= 24 or 0 <= T and T < 6:
#     print(f'Доброй ночи, {N}!')
# else:
#     print('неправильный формат ввода')

# Еще одно решение
# N = input('Как Вас зовут?\n')
# T = int(input('Который час?\n'))


# if T > 24 or T < 0:
#     print('неправильный формат ввода')
#     exit()


# pattern = None

# if 6 <= T and T < 12:
#     pattern = f'Доброе утро, {N}!'
# elif 12 <= T and T < 18:
#     pattern = f'Добрый день, {N}!'
# elif 18 <= T and T < 22:
#     pattern = f'Добрый вечер, {N}!'
# else:
#     pattern = f'Доброй ночи, {N}!'

# print(pattern) 


# while условие:
#     pass

# for итератор(переменная) in итерируемый объект:
#     pass

# while True:
#     print('Hello!')

# i = 0

# while i < 10:
#     print(i)
#     i += 1

# for i in {1, 20, 3}:
#     print(i)

# for i in 'Hello!':
#     print(i)

# Структура - сложный объект, котоырй чаще всего состоит из простых структур или типов данных

# range - Итерируемая структура
# range(до) - от 0 до [до] не включительно
# range(от, до) - от [от] включительно до [до] не включительно
# range(от, до, шаг) - от [от] включительно до [до] не включительно с шагом [шаг]

# for i in range(1, 11, 2):
#     print(i)

# A = int(input('введите число '))
# while A != 0:
#     print(A)
#     A = int(input('введите число '))


