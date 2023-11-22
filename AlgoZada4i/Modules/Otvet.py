from main import all_divisors, three_args, is_palindrome, analyze_text, create_spiral_matrix, is_magic_square

# 1
print('#1')
divisors1 = all_divisors(23436)
print(divisors1)
print('\n')

# ----------------------------------------------------------------

# 2
print('#2')
three_args(var1=2, var3=10)
print('\n')

# ----------------------------------------------------------------

# 3

print('#3')
text = input("Введите текст палиндром: ")
if is_palindrome(text):
    print(f"{text} - это палиндром")
else:
    print(f"{text} - это не палиндром")
print('\n')

# ----------------------------------------------------------------

# 4

print('#4')
text = input()
most_common, longest = analyze_text(text)
print(f"Наиболее частое слово: {most_common}")
print(f"Самое длинное слово: {longest}")
print('\n')

# ----------------------------------------------------------------

# 5

print('#5')
n = int(input())
m = int(input())

spiral_matrix = create_spiral_matrix(n, m)

for row in spiral_matrix:
    print(row)
print('\n')

# ----------------------------------------------------------------

# 6

print('#6')
matrix = [
    [1, 6, 5],
    [8, 4, 0],
    [3, 2, 7]
]

if is_magic_square(matrix):
    print("Эта матрица - магический квадрат")
else:
    print("Эта матрица - НЕ магический квадрат")
