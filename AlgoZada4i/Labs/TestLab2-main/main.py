# Николай написал функцию is_alive(health), которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, то функция возвращает False, в противном случае True.
# К сожалению, функция не работает, так как ученик допустил в ней ряд ошибок.
# Исправьте их и проверьте работоспособность программы (в качестве аргумента всегда передается число).
#
# def is_alive(health):
#     if:
#         health < 0
#         False
#     else:
#         return true
# 1
# def is_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True
#
#
# health = int(input())
# print(is_alive(health))
#
# =================================================================
# Составьте функцию season_events(number_of_month), которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».
#
# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона:
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным».
#
# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента (не попадитесь на этом и предупредите о том, что «Требуется ввести реальный номер месяца»).
# 2
# def season_events(number_of_month):
#     seasons = {
#         1: ("январь", "За окном падал белый снег"),
#         2: ("февраль", "За окном падал белый снег"),
#         3: ("март", "Птицы пели прекрасные песни"),
#         4: ("апрель", "Птицы пели прекрасные песни"),
#         5: ("май", "Птицы пели прекрасные песни"),
#         6: ("июнь", "Солнце светило ярче чем когда-либо"),
#         7: ("июль", "Солнце светило ярче чем когда-либо"),
#         8: ("август", "Солнце светило ярче чем когда-либо"),
#         9: ("сентябрь", "Урожай был невероятным"),
#         10: ("октябрь", "Урожай был невероятным"),
#         11: ("ноябрь", "Урожай был невероятным"),
#         12: ("декабрь", "За окном падал белый снег")
#     }
#
#     if not number_of_month < 1 or number_of_month > 12:
#         print("Введите реальный номер месяца!")
#         return
#
#     month, pattern = seasons[number_of_month]
#     print(f"Вы родились в {month}. {pattern}")
#
#
# season_events(int(input('Введите номер месяца в котором вы родились: ')))
#
# =================================================================
# Анатолию в последний месяц удача улыбалась очень плохо.
# У него 3 раза взломали пароль.
# Вот он и задумался над тем, что неправильно подходит к вопросу составления паролей.
# Чтобы не напрягаться больше и опять не попасть впросак, молодой человек решил написать функцию на Python, которая будет проверять его пароль на надежность.
#
# Требования к паролю у Анатолия следующие (он внимательно изучил рекомендации знатоков):
#
# 1) Длина – 8 символов (если меньше – то проще взломать, а если длиннее – то сложно запомнить)
# 2) В пароле должны быть заглавные буквы, строчные символы, числа и специальные знаки (из перечня «*-#»; другие спецсимволы недопустимы, так как Анатолий их не может запомнить).
#
# Помогите парню составить функцию check_pass (pswd), которая проверит пароль на соответствие требованиям.
# В случае верного пароля выведется на печать «Пароль идеален», а в остальных случаях будут перечислены все ошибки, которые Анатолий допустил (для представления перечня ошибок заведите переменную err в виде словаря).
# 3
# def check_pass(pswd):
#     err = {}
#
#     if len(pswd) < 8:
#         err['Length'] = 'Пароль должен состоять не менее чем из 8 символов'
#
#     if not any(char.isupper() for char in pswd):
#         err['Uppercase'] = 'Пароль должен содержать хотя бы одну заглавную букву'
#
#     if not any(char.islower() for char in pswd):
#         err['Lowercase'] = 'Password should contain at least one lowercase letter'
#
#     if not any(char.isdigit() for char in pswd):
#         err['Numbers'] = 'Пароль должен содержать хотя бы одну строчную букву'
#
#     special_chars = ['*', '-', '#']
#     if not any(char in special_chars for char in pswd):
#         err['Special Characters'] = 'Пароль должен содержать хотя бы один из следующих специальных символов: *, -, #'
#
#     if not err:
#         print('Пароль идеален')
#     else:
#         print('Пароль не соответствует требованиям:')
#         for key, value in err.items():
#             print(f'- {key}: {value}')
#
#
# password = input('Введите пароль: ')
# check_pass(password)
#
# =================================================================
# 4
# def is_divisible_by_6(number):
#     last_digit = number % 10
#     if last_digit % 2 != 0:
#         return f'Число {number} неделимо на 6'
#
#     digit_sum = sum(int(digit) for digit in str(number))
#     if digit_sum % 3 != 0:
#         return f'Число {number} неделимо на 6'
#
#     return f'Число {number} делится на 6'
#
#
# number = int(input())
# result = is_divisible_by_6(number)
# print(result)
#
# =================================================================
# 5
# def search_substr(subst, st):
#     if subst.lower() in st.lower():
#         return 'Есть контакт!'
#     else:
#         return 'Мимо!'
#
#
# substring = input('Введите подстроку: ')
# string = input('Введите строку: ')
# result = search_substr(substring, string)
# print(result)
#
# =================================================================
# 6
# def first_last(letter, st):
#     first_index = st.find(letter)
#     last_index = st.rfind(letter)
#
#     if first_index == -1:
#         return (None, None)
#     else:
#         return (first_index, last_index)
#
#
# letter = input('Введите символ: ')
# string = input("Введите строку: ")
# result = first_last(letter, string)
# print(result)
#
# =================================================================
# 7
# from collections import Counter
#
#
# def top3(st):
#     st = st.replace(" ", "")
#
#     char_counts = Counter(st)
#
#     most_common = char_counts.most_common(3)
#
#     result = ""
#     for char, count in most_common:
#         result += f"{char} - {count} раз, "
#
#     result = result.rstrip(", ")
#
#     return result
#
#
# text = input('Введите любой текст: ')
# result = top3(text)
# print(result)
#
# =================================================================
# 8
# def camel(st):
#     result = ""
#     is_upper = True
#
#     for char in st:
#         if char.isalpha():
#             if is_upper:
#                 result += char.upper()
#             else:
#                 result += char.lower()
#
#             is_upper = not is_upper
#         else:
#             result += char
#
#     return result
#
#
# string = input('Введите любой текст: ')
# result = camel(string)
# print(result)
#
# =================================================================
# 9
# def shortener(st):
#     result = ""
#     stack = []
#
#     for char in st:
#         if char == '(':
#             stack.append('(')
#         elif char == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 result += char
#         elif not stack:
#             result += char
#
#     return result
#
#
# string = input('Введите (любой) текст: ')
# result = shortener(string)
# print
#
# =================================================================
# 10
# def more_than_five(lst):
#     result = [num for num in lst if abs(num) > 5]
#     return result
#
#
# numbers = [3, -7, 8, -2, 6, 0, -10]
# result = more_than_five(numbers)
# print(result)
#
# =================================================================
# 11
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
#
# for letter in letters:
#     if letter.isupper():
#         letters = letters.replace(letter, '')
#
# print(letters)
#
# =================================================================
# 12
# secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
#
# nickname = input("Введите ваш никнейм: ")
#
# if nickname in secret_list:
#     print(f"Ты – свой. Приветствую, любезный {nickname}!")
# else:
#     print("Тут ничего нет. Еще есть вопросы?")
#
# =================================================================
# 13
# def all_divisors(number):
#     div = []
#     i = 1
#
#     while i <= number:
#         if number % i == 0:
#             div.append(i)
#         i += 1
#
#     return div
#
#
# number = 23436
# result = all_divisors(number)
# print(result)
#
# =================================================================
# 14
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#
#     total = 0
#     for num in range(start, end + 1):
#         total += num
#
#     return total
#
#
# start = int(input('Введите число: ')
# end = int(input('Введите число: ')
# result = sum_range(start, end)
# print(result)
#
# =================================================================
# 15
# def three_args(*, var1=None, var2=None, var3=None):
#     args = []
#     if var1 is not None:
#         args.append(f"var1 = {var1}")
#     if var2 is not None:
#         args.append(f"var2 = {var2}")
#     if var3 is not None:
#         args.append(f"var3 = {var3}")
#
#     if args:
#         print("Переданы аргументы: " + ", ".join(args))
#
# =================================================================
# 16
# def inspect_function(func):
#     func_name = func.__name__
#     print(f"Анализируемая функция: {func_name}")
#
#
# def example_function():
#     pass
#
#
# inspect_function(example_function)
#
# =================================================================
# from datetime import datetime
# from time import sleep
#
#
# def time_now(msg, *, dt=None):
#     if dt is None:
#         dt = datetime.now()
#     print(msg, dt)
#
#
# time_now('Сейчас такое время: ')
# sleep(1)
# time_now('Прошла секунда: ')
# sleep(1)
# time_now('Ничего не понимаю... ')
