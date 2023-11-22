import numpy as np
import matplotlib.pyplot as plt
import calendar

# 1
# def Numpy(arr):
#     np_array = np.array(arr, dtype=float)
#     return np_array
#
#
# arr = [[1, 2, 3], [4, 5, 6]]
# numpy_array = Numpy(arr)
#
# print(numpy_array)
# =================================================================
# 2
# def ShapeSizeCalc(arr):
#     shape = arr.shape
#     size = arr.size
#     return shape, size
#
#
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# shape, size = ShapeSizeCalc(arr)
#
# print("shape =", shape, ",", "size =", size)
# =================================================================
# 3
# def ArrayIndexing(arr, rows, val):
#     transformed_array = arr[rows, ::val]
#     return transformed_array
#
#
# arr = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
# rows = (0, 1)
# val = 2
#
# transformed_array = ArrayIndexing(arr, rows, val)
#
# print(transformed_array)

# =================================================================

# 1
# x = np.linspace(-5, 5, 10)
#
# y = 6 * x - 2
#
# plt.plot(x, y)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Линейная функция: y = 6x - 2')
#
# plt.show()
# =================================================================
# 2
# x = np.linspace(-5, 5, 100)
# y = 6 * x**3 - 2 * x + 8
# y2 = 3 * x + 1
#
# plt.figure(figsize=(8, 6))
#
# plt.plot(x, y, label='F(x, y) = 6x^3 - 2x + 8', color='blue')
# plt.plot(x, y2, label='F(x, y) = 3x + 1', color='red')
#
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
#
# plt.title('Графики функций F(x, y) = 6x^3 - 2x + 8 и F(x, y) = 3x + 1')
#
# plt.grid(True)
# plt.show()
# =================================================================
# 3
# fruits = ["помидоры", "огурцы", "тыква", "свекла", "редис", "картофель"]
# counts = [100, 65, 12, 47, 89, 265]
#
# plt.figure(figsize=(8, 6))
# plt.bar(fruits, counts, color='skyblue')
#
# plt.xlabel('Товары')
# plt.ylabel('Количество')
# plt.title('Количество товаров')
#
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

# =================================================================

# 1
# # Найдите расположение файла модуля calendar и изучите его содержимое
# print(calendar.__file__)
#
# # Получите список доступных атрибутов модуля calendar
# print(dir(calendar))
#
# # С помощью модуля calendar узнайте, является ли 2027 год високосным
# is_leap = calendar.isleap(2027)
# print(f"2027 год високосный: {is_leap}")
#
# # С помощью модуля calendar узнайте, каким днем недели был день 25 июня 1995 года
# weekday = calendar.weekday(1995, 6, 25)
# days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# day_of_week = days[weekday]
# print(f"25 июня 1995 года был {day_of_week}")
#
# # Выведите в консоль календарь на 2023 год
# cal = calendar.TextCalendar(calendar.SUNDAY)
# print(cal.formatyear(2023, 2, 1, 1, 1))
# =================================================================
# 2
# # Изучите модуль для базового сравнения строк fuzz(входит в пакет): импортируйте его и получите список доступных атрибутов.
# from fuzzywuzzy import fuzz
# print(dir(fuzz))
#
# # Определите, какие модули включает пакет fuzzywuzzy:
# # fuzz, process, utils
#
# # Изучите синтаксис метода для базового нечеткого сравнения строк ratio() (входит в состав модуля fuzz). Прим.: Данный метод возвращает индекс схожести 2 срок
# similarity1 = fuzz.ratio("Плохой код на самом деле не плохой.", "Его просто не так поняли.")
# similarity2 = fuzz.ratio("Работает? Не трогай.", "Работает? Не трогай.")
# similarity3 = fuzz.ratio("Работает? Не трогай.", "Работает? Не трогай!")
#
# print("Индекс схожести (1):", similarity1)
# print("Индекс схожести (2):", similarity2)
# print("Индекс схожести (3):", similarity3)