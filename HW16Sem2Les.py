# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 чисел -> ввод 1 0 1 1 0
# результат 2

# import random
# n = int(input("Сколько монет на столе: "))
# i_gerb = int(0) #это 1
# i_reshka = int(0) #это 0
# for i in range(n):
#     a = random.randint(0, 1)
#     print(a)
#     if a == 1:
#         i_gerb +=1
#     else:
#         i_reshka += 1
# if i_gerb == 0 or i_reshka ==0:
#     print("Все монеты лежат одной стороной")
#     quit()
# if i_gerb < i_reshka:
#     print(f"Нужно перевернуть гербы, {i_gerb} шт.")
# elif i_gerb > i_reshka:
#     print(f"Нужно перевернуть решки, {i_reshka} шт.")
# else:
#     print(f"Можно перевернуть любые одинаковые монеты, орлов и решек поровну, по {i_reshka} шт.")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# числа больше 0, так как натуральные

# sum = int(input("Введите сумму чисел x+y: "))
# multip = int(input("Введите произведение чисел x*y: "))
# if sum <= 0 or multip <= 0:
#     print("Напишите два натуральных числа")
# else:
#     for i in range(sum):
#         for j in range(multip):
#             if sum == i + j and multip == i * j:  
#                 print(f"x = {i}, y = {j}")
#                 quit()
#             elif i == sum-1 and j == multip-1:
#                 print("Нет значений, при которых их сумма равна их произведению")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

# n = int(input("Введите число: "))

# for i in range(n):
#     new = 2 ** i
#     if new < n:
#         print(new)
#     else:
#         quit()
