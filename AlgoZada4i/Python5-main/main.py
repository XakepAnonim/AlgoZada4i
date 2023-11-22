import calendar
from math import sqrt
from datetime import date


# 1
# def distance(x1=0, y1=0, x2=0, y2=0):
#     dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#     return dst
#
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# res = distance(x2=x2, y2=y2, x1=x1, y1=y1)
# print(res)
#
# =================================================================
# 2
# def power(a, n):
#     res = 1
#     if n > 0:
#         for i in range(n):
#             res *= a
#     elif n < 0:
#         for i in range(-n):
#             res /= a
#     return res
#
#
# a = float(input())
# n = int(input())
# print(power(a, n))
#
# =================================================================
# 3
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# n = int(input())
# fib(n)
#
# -----------------------------------------------------------------
#
# 4
# def is_year_leap(year):
#     if calendar.isleap(year):
#         print('Год високосный')
#     else:
#         print('Год не високосный')
#
# is_year_leap(int(input()))
#
# =================================================================
# 5
# def square(a):
#     print(f'Периметр квадрата: {a+a+a+a}')
#     print(f'Площадь квадрата: {a * a}')
#     print(f'Периметр квадрата: {(2*a)**0.5}')
#
# square(int(input('Введите сторону квадрата: ')))
# -----------------------------------------------------------------
# def square(x):
#     return (f'Периметр квадрата: {4 * x},\n'
#             f'Площадь квадрата: {x * x},\n'
#             f'Диагональ квадрата: {x * 2 ** 0.5}')
#
# print(square(int(input('Введите сторону квадрата: '))))
#
# =================================================================
# 6
# def season(i):
#     if i in (12, 1, 2):
#         print('Зима')
#     elif i in (3, 4, 5):
#         print('Весна')
#     elif i in (6, 7, 8):
#         print('Лето')
#     elif i in (9, 10, 11):
#         print('Осень')
#
#
# season(int(input()))
#
# =================================================================
# 7
# def bank(a, years):
#     return a * years * 0.1
#
#
# a = float(input())
# years = int(input())
#
# print(bank(a, years) + a)
# =================================================================
# 8
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# res = int(input())
# print(is_prime(res))
#
# =================================================================
# 9
# def date(year, month, day):
#     try:
#         date(year, month, day)
#         return True
#     except:
#         return False
#
# year = int(input())
# month = int(input())
# day = int(input())
# print(date(day, month, year))
