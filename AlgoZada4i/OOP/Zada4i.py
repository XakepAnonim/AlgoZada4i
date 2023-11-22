def searchRange(nums, target):
    left = 0
    right = len(nums) - 1 # определяет границы поиска

    while left <= right: # выполняется цикл, пока left не будет больше right
        mid = (left + right) // 2 # вычисляет средний индекс

        if nums[mid] == target:
            start = mid
            end = mid
            # ищет начальный индекс значения
            while start >= 0 and nums[start] == target: # цикл уменьшает значение start,
                                                    # пока оно больше или равно 0 или равно target
                start -= 1

            while end < len(nums) and nums[end] == target:
                end += 1

            return [start+1, end-1]

        elif nums[mid] < target:
            left = mid + 1 # обновляет left для сужения поиска справа от mid
        else:
            right = mid - 1 # обновляет right для сужения поиска справа от mid

    return [-1, -1]

# ------------------------------------------------------------------------------------------------

def spiralOrder(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []

    while top <= bottom and left <= right:
        # Верхний ряд
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Правый столбец
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Проверка других строк и столбцов
        if top <= bottom and left <= right:
            # Нижний ряд
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            # Левый столбец
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# ------------------------------------------------------------------------------------------------

def Sudoku(board):
    rows = [] # текущая строка
    for _ in range(9):
        rows.append(set())

    cols = [] # текущий столбец
    for _ in range(9):
        cols.append(set())

    subgrids = [] # текущая подсетка
    for _ in range(9):
        subgrids.append(set())

    for i in range(9):
        for j in range(9): # проходит по ячейкам
            cell = board[i][j]
            if cell == '.': # проверяет есть ли число в ячейке
                continue # если ячейка пустая, переходит дальше по коду
            num = int(cell) # если число есть, то оно преобразуется в число
            subgrid_index = (i // 3) * 3 + j // 3  # затем вычисляется индекс подсетки

            if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
                # проверяет есть ли число в строке, столбце и подстроке
                return False # если число есть, то возвращает False
            # если число не встречалось, то оно добавляется в множесства
            rows[i].add(num)
            cols[j].add(num)
            subgrids[subgrid_index].add(num)

    return True