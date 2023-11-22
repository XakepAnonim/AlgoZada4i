# 1
def all_divisors(number):
    divisors = []
    i = 1
    while i <= number:
        if number % i == 0:
            divisors.append(i)
        i += 1
    return sorted(divisors)


# =================================================================

# 2
def three_args(*, var1=None, var2=None, var3=None):
    arguments = []
    if var1 is not None:
        arguments.append(f"var1 = {var1}")
    if var2 is not None:
        arguments.append(f"var2 = {var2}")
    if var3 is not None:
        arguments.append(f"var3 = {var3}")
    if arguments:
        print("Переданы аргументы: " + ", ".join(arguments))


# =================================================================

# 3
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]


# =================================================================

# 4
def analyze_text(text):
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)
    longest_word = max(words, key=len)

    return most_common_word, longest_word


# =================================================================
# 5
def create_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1
    row, col = 0, 0
    direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n * m):
        matrix[row][col] = num
        num += 1

        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        if 0 <= next_row < n and 0 <= next_col < m and matrix[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4
            row += directions[direction][0]
            col += directions[direction][1]

    return matrix


# =================================================================

# 6
def is_magic_square(matrix):
    n = len(matrix)
    target_sum = n * (n ** 2 + 1) // 2

    for row in matrix:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    if sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    return True
