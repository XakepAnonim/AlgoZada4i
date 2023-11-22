# stroka = input(
#
# print(stroka[2]) #1
# print(stroka[-2]) #2
# print(stroka[:5]) #3
# print(stroka[:-2]) #4
# print(stroka[1::2]) #5
# print(stroka[2::2]) #6
# print(stroka[::-1]) #7
# print(stroka[::-2]) #8
# print(len(stroka)) #9
# =================================================================================
# stroka = input()
# print(stroka.count(' ') + 1)
# =================================================================================
# stroka = input()
#
# print(stroka[:round(len(stroka)/2)])
# print(stroka[round(len(stroka)/2):])
# print(stroka[round(len(stroka)/2):] + stroka[:round(len(stroka)/2)])
# =================================================================================
# stroka = input()
# count = len(stroka) - len(stroka.replace('f', ''))
# if count == 0:
#     pass
# elif count == 1:
#     print(stroka.find('f'))
# else:
#     print(stroka.find('f'), stroka.rfind('f'))
# =================================================================================
# stroka = input()
# s = stroka.find('h')
# s1 = stroka.rfind('h')
# print(stroka[:s] + stroka[s1+1:])
# =================================================================================
# stroka = input()
# s = stroka.replace('1', 'one')
# print(s)
# =================================================================================
# stroka = input()
# s = stroka.split('@')
# s1 = ''.join(s)
# print(s1)
# =================================================================================
# stroka = input()
# print(stroka.replace('h', 'H', stroka.count('h') - 1).replace('H', 'h', 1))
# =================================================================================
# =================================================================================
# x = int(input())
# y = int(input())
#
# if x and y:
#     print(min(x, y))
# ---------------------------------------------------------------------------------
# if x>y:
#   print(y)
# else:
#   print(x)
# =================================================================================
# x = int(input())
# if x > 0:
#     print(1)
# elif x < 0:
#     print(-1)
# else:
#     print(0)
# =================================================================================
# x = int(input())
# y = int(input())
# x1 = int(input())
# y1 = int(input())
# if 1 < x < 8 and 1 < y < 8 and 1 < x1 < 8 and 1 < y1 < 8:
#     if (x + y + x1 + y1) % 2 == 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('Такой клетки не существует')
# =================================================================================
# s = int(input())
# if s % 4 == 0 and s // 100 == 0 or s % 400 == 0:
#     print('YES')
# else:
#     print('NO')
# =================================================================================
# x = int(input())
# y = int(input())
# z = int(input())
# if x == y == z:
#     print(3)
# elif x == y or x == z or y == z:
#     print(2)
# else:
#     print(0)
# =================================================================================
# x = int(input())
# y = int(input())
# x1 = int(input())
# y1 = int(input())
# if x == x1 and y != y1 or y == x1 and x == y1:
#     print('YES')
# else:
#     print('NO')
# =================================================================================
# n = int(input())
# m = int(input())
# k = int(input())
# if (n*m) > k and (k % m == 0 or k % n == 0):
#     print('YES')
# else:
#     print('NO')
# =================================================================================
# N = int(input()); M = int(input()); x = int(input()); y = int(input())
# long = min(x, N - x)
# short = min(y, M - y)
# min_distance = min(long, short)
# print("Минимальное расстояние до бортика: ", min_distance)
# Сначала пробовал сам решить, потом в интернете смотрел.. так и не понял как это работает..