# 1
# def list_reorder(ref_list):
#     names = ref_list[0] # первый индекс это имена
#     surnames = ref_list[1] # второй индекс это фамилии
#
#     reordered_list = [] # создал список где будет распределение
#     for name, surname in zip(names, surnames):
#         reordered_list.append([name, surname]) # добавляет [имя, фамилия] в список
#
#     return reordered_list # возвращаем распределенный список
#
# # тут пример использование
# ref_list = [['Александр', 'Анастасия', 'Джеймс', 'Эмма'], ['Смирнов', 'Иванова', 'Смит', 'Джонсон']]
# result = list_reorder(ref_list)
# print(result)

# 2
# def del_rep(num):
#     unique_nums = list(set(num)) # удаляем дубликаты через set
#     sorted_nums = sorted(unique_nums)  # сортирует список
#     return sorted_nums  # возвращает список
#
#
# # пример использования
# num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
# result = del_rep(num)
# print(result)

# 3
# def lim_max(nums, limit):
#     max_value = -1 # если кортеж пустой
#     for num in nums:
#         if num < limit and num > max_value: # если число меньше лимита и это не пустой кортеж
#             max_value = num # то в кортеж записывается число
#
#     return max_value # возвращает
#
#
# # Пример использования
# nums = () # исходный кортеж чисел
# limit = 0 # лимит чисел сверху
# result = lim_max(nums, limit)
# print(result)


# 4
# def temp_cat(temp):
#     if temp < -20: # если темература меньше -20
#         return 0 # возвращает 0 #Холодно
#     elif -20 <= temp < 0: # если темература больше или равна -20 и меньше 0
#         return 1 # возвращает 1 #Прохладно
#     elif 0 <= temp < 15: # если темература больше или равна 0 и меньше 15
#         return 2 # возвращает 2 #Зябко
#     elif 15 <= temp < 25: # если темература больше или равна 15 и меньше 25
#         return 3 # возвращает 3 #Тепло
#     else: # тут иначе, т.е если температура больше 25
#         return 4 # возвращает 4 #Жарко
#
#
# # Пример использования
# temp = int(input())
# result = temp_cat(temp)
# print(result)

# 5
# def check_phn(phones):
#     formatted_phones = []  # создаем список где будут форматированные номера
#     for phone in phones:
#         digits = ''.join(filter(str.isdigit, phone)) # удаляет разделители, оставляя цифры
#
#         if len(digits) != 11: # проверяет длину номера
#             formatted_phones.append(-1)
#             continue
#
#         if digits[0] not in ['7', '8']: # проверяет первую цифры
#             formatted_phones.append(-1)
#             continue
#
#         formatted_phone = '+7(' + digits[1:4] + ')' + digits[4:7] + '-' + digits[7:9] + '-' + digits[9:11] # форматирует номер с распределением
#         formatted_phones.append(formatted_phone)
#
#     return formatted_phones
#
#
# # Пример использования
# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
# result = check_phn(phones)
# print(result)
