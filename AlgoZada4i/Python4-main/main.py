from math import log
from operator import index

# Ряд - 1
# a = int(input())
# b = int(input())
# if a <= b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     print('a меньше b')
# =================================================================
# Ряд - 2
# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)
# =================================================================
# Сумма N чисел
# a = int(input())
# b = int(input())
# i = 0
#
# for i in range(a):
#     i += b
# print(i)
# =================================================================
# Факториал
# n = int(input())
# fact = n
# for i in range(1, n):
#     fact *= i
# print(fact)
# =================================================================
# Лесенка
# n = int(input())
# if n > 9:
#     print('Введите число меньше 9')
# else:
#     for i in range(n):
#         print(end='\n')
#         for i in range(1, i + 2):
#             print(i, end='')

# =================================================================

# Список квадратов
# n = int(input())
# j = 1
#
# for i in range(1, n + 1):
#     if n > j:
#         j = i ** 2
#         i += 1
#         print(j)
# =================================================================
# Степень двойки
# n = int(log(int(input()), 2))
# num = 1
# for i in range(n):
#     num *= 2
#
# print(n, num)
# =================================================================
# Утренняя пробежка
# x = int(input())
# y = int(input())
# l = x
# d = 0
#
# while l <= y:
#     l += 0.1 * l
#     d += 1
# print(d)

# =================================================================
# Длина последовательности
#
# =================================================================
# Количество элементов, которые больше предыдущего
# n = int(input())
# result = 0
# while n != 0:
#     next = int(input())
#     if next != 0 and n < next:
#         result += 1
#     n = next
# print(result)
# =================================================================
# Второй максимум
#
# =================================================================
# Числа Фибоначчи
# n = int(input("Введите номер числа Фибоначчи: "))
#
# def fib(n):
#     if n <= 0:
#         print("Число не может быть меньше 0")
#     elif n == 1:
#         print(0)
#     elif n == 2:
#         print(1)
#     else:
#         c = 0
#         cur = 1
#         for i in range(3, n + 1):
#             next = c + cur
#             c = cur
#             cur = next
#         return cur
#
#
# result = fib(n)
# print(result)
# =================================================================
# Максимальное число идущих подряд равных элементов
# a = int(input())
# b = int(input())
# n = 1
# m = 0
# while a != 0 and b != 0:
#     if a == b:
#         a = b
#         b = int(input())
#         n += 1
#     if a != b != 0:
#         m = max(n, m)
#         n = 1
#         a = b
#         b = int(input())
#
# print(max(n, m))

# =================================================================

# 14
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])
# =================================================================
# 15
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 1
# while i != len(nums):
#     if nums[i] > nums[i - 1]:
#         print(nums[i], end='')
#     i += 1
# =================================================================
# 16
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = max(nums), nums.index(max(nums))
# print(n)
# =================================================================
# 17
# rost = [171, 180, 165, 167, 174, 175, 173, 169]
# x = int(input())
# a = rost.append(x)
# b = sorted(rost)
# print(b)
# =================================================================
# 18
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = nums[:-1:2] + nums[1::2]
# print(n)
# =================================================================
# 19
# nums = list(map(int, input().split()))
# n = list(nums)
# n[nums.index(max(nums))] = min(nums)
# n[nums.index(min(nums))] = max(nums)
#
# print(n)
# =================================================================
# 20
# nums = list(map(int, input().split()))
# n = list(nums)
# k = int(input())
# n = n[:k] + n[k + 1:] + [n[k]]
# n.pop()
# print(*n)
# =================================================================
# 21
# nums = list(map(int, input().split()))
# n = list(nums)
# k = int(input())
# C = int(input())
# n[k] = C
# n.append(C)
# print(*n)
