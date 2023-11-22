def positive_or_negative(x):
    x = float(x)
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def even_num(number):
    return number % 2 == 0


def count(num):
    return len(str(abs(num)))


def sum_list(lst):
    return sum(lst)


def sum_numbers(numbers):
    num_list = numbers.split(',')
    num_list = [int(num) for num in num_list]
    return sum(num_list)