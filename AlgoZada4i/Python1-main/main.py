# n = int(input())
# a = n+1
# b = a+1
# print(a, b, sep="\n")
# =================================================================================
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# print(n1+n2+n3)
# =================================================================================
# a = int(input())
# V = a**3
# S = 6*a**2
# print(f'Объем куба: {V}')
# print(f'Площадь полной поверхности: {S}')
# =================================================================================
# a = int(input())
# b = int(input())
# print(3*((a+b)**3) + 275*(b**2) - 127*a - 41)
# =================================================================================
# n = int(input())
# print(f'Следующее за числом: {n} число: {n+1}')
# print(f'Следующее за числом: {n} число: {n-1}')
# =================================================================================
# n = int(input("Монитор:"))
# n1 = int(input("Сис. блок:"))
# n2 = int(input("Клавиатура: "))
# n3 = int(input("Мышь: "))
# print((n+n1+n2+n3)*3)
# =================================================================================
# a_1 = int(input("1 член прогрессии: "))
# d = int(input("d: "))
# n = int(input("n: "))
# print(a_1+d*(n-1))
# =================================================================================
# n = int(input("Введите число: "))
# print(n,"--",n*2,"--",n*3,"--",n*4,"--",n*5)
# =================================================================================
# n = int(input())
# k = int(input())
# print(f"Каждому по: {k // n}")
# print(f"Останется яблок: {k % n}")
# =================================================================================
# n = int(input("Введите число населения планеты: "))
# print(round(n/2))
# =================================================================================
# n = int(input())
# h = n // 60
# m = n % 60
# print(n,"мин - это",h,"час",m,"минут.")
# =================================================================================
# a = str(input("Введите число: "))
# print('Сумма цифр =', int(a[0]) + int(a[1]) + int(a[2]))
# print('Произведение цифр =', int(a[0]) * int(a[1]) * int(a[2]))
# =================================================================================
# n = int(input())
# p = '   _~_   '
# p1 = '  (o o)  '
# p2 = '  / V \\ '
# p3 = ' /( _ )\\'
# p4 = '  ^^ ^^  '
#
# print(p*n)
# print(p1*n)
# print(p2*n)
# print(p3*n)
# print(p4*n)
# =================================================================================
# n = int(input("Введите число: "))
# print(n % 100 // 10)
# =================================================================================
# n = int(input())
# hours = n % (60 * 24) // 60
# minutes = n % 60
# print(hours, minutes)
# =================================================================================
# n = int(input("Введите 0 или 1: "))
# if n == 1:
#     print(0)
# elif n == 0:
#     print(1)
# else:
#     print('Error')
# =================================================================================
# n = int(input("Введите число не превышающее 1000: "))
# if n <= 1000:
#     if n % 2 == 0:
#         print(n+2)
#     else:
#         print(n+1)
# else:
#     print("Число превышает 1000!")
# =================================================================================
# v = int(input())
# t = int(input())
# if v*t > 0:
#     print(v*t % 109)
# else:
#     print(v*t)
# =================================================================================
# h = int(input())
# a = int(input())
# b = int(input())
# print((h - a) // (a - b) + 1)
