# A = 1
# while A != 0:
#     B = float(input('введите первое число, \n'))
#     C = float(input('введите второе число \n'))
#     D = input('выберите действие \n')

#     if D == '+':
#         E = B + C
#     elif D == '-':
#         E = B - C
#     elif D == '*':
#         E = B * C
#     elif D == '/':
#         if C == 0:
#             E = '0 error'
#         else:
#             E = B / C
#     else:
#         # print('ошибка ввода данных')
#         # continue
#         E = 'ошибка ввода данных'

#     print(E)

#     A = float(input('введите 0 если хотите выйти, введите любое другое число, если хотите продолжить \n'))


flag_exit = 1

while flag_exit:
    A = float(input('enter the 1st num: '))
    B = float(input('enter the 2st num: '))
    operator = input('choose the operator (-, +, *, /): ')

    result = None
    match operator:
        case '+':
            result = A + B        
        case '-':
            result = A - B
        case '*':
            result = A * B
        case '/':
            if B == 0:
                print('zero error')
            else:
                result = A / B        
        case _:
            print('operator error')
    
    if result is not None:
        print(result)
    
    flag_exit = int(input('введите 0 если хотите выйти, введите любое другое число, если хотите продолжить: '))
