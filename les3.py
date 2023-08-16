# A = int(input('введите число '))
# while A != 0:
#     print(A)
#     A = int(input('введите число '))

# break - останавливает
# continue - продолжает с начала
# Команды относящиеся к циклу или match

# Для точечного выбора мы используем match

# match объект(переменная):
#     case состояние1: - аналог if объект == состояние1
#         [tab]

#     case состояние2:
#         [tab]

#     case _: - все остальные состояния, аналог else
#         [tab]

# flag_exit = 1

# while flag_exit:
#     A = float(input('enter the 1st num: '))
#     B = float(input('enter the 2st num: '))
#     operator = input('choose the operator (-, +, *, /): ')

#     result = None
#     match operator:
#         case '+':
#             result = A + B        
#         case '-':
#             result = A - B
#         case '*':
#             result = A * B
#         case '/':
#             if B == 0:
#                 print('zero error')
#             else:
#                 result = A / B        
#         case _:
#             print('operator error')
    
#     if result is not None:
#         print(result)
    
#     flag_exit = int(input('введите 0 если хотите выйти, введите любое другое число, если хотите продолжить: '))

# range - Итерируемая структура
# range(до) - от 0 до [до] не включительно
# range(от, до) - от [от] включительно до [до] не включительно
# range(от, до, шаг) - от [от] включительно до [до] не включительно с шагом [шаг]

# print(range(10)) 

# for i in range(10):
#     print(i)
# int
# s = 'Hello'
# print(s.upper())
# print(s)
# print(s.find('e'))

# lambda-функции
# f_x = lambda x, все_остальные_аргументы:
# f_x = lambda x: x**3
# A = f_x(2)
# print(A)

# стандартные функции
# def funk(x, y):
#     result = x * y
#     result -= 1
    
#     if result > 35:
#         return True
#     else:
#         return False

# a = 5
# b = 7
# r = funk(a, b)
# print(r)

# def имя_функции(необходимое_кол-во_аргументов_через_запятую):
#     тело функции, всякие вычисления там
#     опционально, если это не процедура, то пишем return - ключевое слово, возвращающее значение (или значения)
#     [return либо переменную, число или выражение]

# obj = range(10)

# print(range(10))
# print(*range(10))

# for i in obj:
#     print(i)

# for i in range(10):
#     print(i)

# result = 0
# for i in range(1, 4):
#     result +=i
# print(result)

# result = 0
# for i in {1, 10, 20}:
#     result += i
# print(result)

# B=1

# while B != 0:
#     B = int(input('введите целое число \n'))
#     if B%2 == 0:
#         print(f'{B} - чётное число')
#     else:
#         print(f'{B} - нечётное число')

# A = int(input('введите целое число \n'))
# for i in range(A):
#     if i%2 != 0:
#         print(i)

# for i in range(A):
#     print(i%6)



# Структуры
# список - упорядоченная структура
# кортеж - упорядоченная, неизменяемая структура - скорость
# множество (математичекое) - неупорядоченная структура состоящая из уникальных элементов
# словарь - неупорядоченная структура, хранящая значения в виде пары {ключ: значение}

# list - cписок
# var = list()
# var = []
# var = [1, 2, 3]
# print(var)
# print(*var)

# var = [1, 'str']

# var = [1, ['str', 12, 3]]
# print(var[1])
# print(*var[1])
# print(var[1][1])

# [] - доступу к элементам упорядоченной структуры по индексу
# к неупорядоченным структурам невозможно обратиться по индексу

# lst = []

# prompt = 'Введите число для добавления в список или 0 для оконяания работы программы: '
# myInput = int(input(prompt))

# while myInput:
#     lst.append(myInput)
#     print(lst)
#     myInput = int(input(prompt))


# # print(len('Hello'))

# result = 0
# for i in lst:
#     result += i
# k = len(lst)

# print(result/k)

# lst = [10, 20, 30]
# for i in range(len(lst)):
#     print(lst[i])
