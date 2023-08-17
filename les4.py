# def isEven(num): 
#     return num%2 == 0

# # print(isEven(3))

# a = 9

# if isEven(a):
#     print('Even')
# else:
#     print('Odd')

# можно сделать инверсию возвращаемого значения
# if not isEven(a):
#     print('Odd')
# else:
#     print('Even')

# СТРУКТУРЫ продолжение
# кортеж - упорядоченная, неизменяемая структура - скорость (для хранения и быстрой обработки большого объёма НЕИЗМЕНЯЕМЫХ данных)
# кортеж - tuple

# tpl = tuple()
# tpl = tuple([1, 2, 3])
# tpl = ()
# tpl = (1, 2, 3)
# print(tpl[0])
# tpl[0] = 2

# множество (математичекое) - неупорядоченная структура состоящая из уникальных неизменяемых элементов
# множество - set

# st = set()
# st = set([1, 2, 3])
# st = {1, 2, 3}

# print(st)
# st.add(2)
# print(st)
# st.add('str')
# print(*st)

# st = {(1, 2, 3)}
# print(st)
# st.add((1, 2, 3))
# print(st)

# lst = [1, 4, 'str', 2, 3, 2, 1, 3, 4]
# lst = list(set(lst))
# print(lst)

# st1 = {1, 2, 3, 4}
# st2 = {2, 5, 4, 6}
# print(st1 | st2)
# print(st1 & st2)
# print(st1 - st2)
# print(st2 - st1)
# print(st1 ^ st2)
