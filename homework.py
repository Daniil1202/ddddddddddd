# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


# n = int (input('Введите количество элементов массива '))
# x = int (input('Введите искомое число '))
# list = [x for x in range(1,n+1)]
# res = 0 
# for i in list:
#     if x == i:
#         res += 1   #res = res + 1
# print(F" {list}  \n  {res}")        



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.\
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


# n = int( input('Введите количество элементов массива '))
# x = int(input('Введите искомое число '))
# list = [x for x in range(1,x+1)]
# res = 0
# print(list)
# if x < min(list):
#     print(min(list))
# elif x > max(list):
#     print (max(list))
# elif x == min(list):
#     print(list[1])
# elif  x == max(list):
#     print(list[-2])
# else:
#     for i in list:
#         if x == i:
#             print(i+1)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int (input('Введите количество элементов первого набора чисел  '))
# x = int (input('Введите количество элементов второго набора чисел  '))

# def create_array(n, mn, mx):
#     import random
#     array = [random.randint(mn, mx) for _ in range(n)]
#     return array


# n = int(input('Кол-во элементов первого набора? -> '))
# m = int(input('Кол-во элементов второго набора? -> '))
# listing_1 = create_array(n, 2, 13)
# listing_2 = create_array(m, 2, 13)
# print(listing_1)
# print(listing_2)

# set_1 = set(listing_1)
# set_2 = set(listing_2)

# result = set_1 & set_2
# print('Пересечение множеств - ', sorted(result), '\n')




# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
kust = int(input('Введите количество кустов: '))
berryes = list(random.randint(0,10) for i in range(kust))
result = []
i = 0
sum = 0
print(berryes)
while(i<kust):
    if(i == kust - 1):
        sum = berryes[i] + berryes[i-1] + berryes[0]
    else :
        sum = berryes[i] + berryes[i-1] + berryes[i+1]
        result.append(sum)
        result.sort
    i +=1
print(f' Максимальное количесвто число ягод за одну итерацию {result[-1]}')