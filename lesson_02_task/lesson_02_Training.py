# employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list[1] + ", " + employee_list[-2])


# def dev_by_three(n):
#     n = int(n)
#     if (n % 3 == 0):
#         print("Yes")
#     else:
#         print("No")

# dev_by_three(n = input("Делится ли число на 3? "))

# def dev2_by_three(number):
#     return "Da" if number % 3 == 0 else "Net"

# num = int(input("Число: "))
# result = dev2_by_three(num)
# print(f"Делится ли на три {num}? - {result}")

# import math
# def min_boxes(items):
#     return math.ceil(items/5)

# num_items = int(input("Количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_items)}")

# n = int(input("Введите число: "))
# def check_devilibity(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print("Делится на 2 и на 4")
#         elif i % 2 == 0:
#             print("Делится на 2, но не на 4")
#         else:
#             print(i)

# check_devilibity(n)


# def quater_of_year(n):
#     if 1 <= n <= 3:
#         return("I qua")
#     if 4 <= n <= 6:
#         return("II qua")
#     if 7 <= n <= 9:
#         return("III qua")
#     if 10 <= n <= 12:
#         return("IV qua")
#     return("No mouth")

# n = int(input("Введите номер месяца от 1 до 12: "))
# print(quater_of_year(n))


# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# for x in lst:
#     if x > 15 and x % 3 == 0:
#         print(x)

# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# result = [x for x in lst if x > 15 and x % 3 == 0]

# print(result)



# for i in range(25, 0, -5):
#     print(i, end=" ")


# lst = list(range(25, 0, -5))
# print(lst)


# var_1 = 50
# var_2 = 5
# var_3 = var_1
# var_1 = var_2
# var_2 = var_3

# print(var_1)
# print(var_2)


# var_1 = 50
# var_2 = 5

# var_1, var_2 = var_2, var_1

# print("var_1 =", var_1)
# print("var_2 =", var_2)


