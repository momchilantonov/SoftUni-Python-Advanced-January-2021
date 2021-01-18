def create_matrix(row):
    matrix = [[0] * int(row) for _ in range(int(row))]
    return matrix


def add_values(matrix):
    for idx in range(len(matrix)):
        line = [x for x in input()]
        matrix[idx] = line
    return matrix


def find_symbol(matrix, symbol):
    for row in matrix:
        for cell in row:
            if cell == symbol:
                return matrix.index(row), row.index(cell)
    return f"{symbol} does not occur in the matrix"


print(find_symbol(add_values(create_matrix(input())), input()))

# size = int(input())
#
# matrix_of_chars = [[] * size for x in range(0, size)]
#
# for x in range(0, size):
#     line = input()
#     for y in range(0, size):
#         matrix_of_chars[x].append(line[y])
#
# symbol = input()
# location = []
# found = False
#
# for row in range(0, size):
#     if found:
#         break
#     for col in range(0, size):
#         if matrix_of_chars[row][col] == symbol:
#             location = [row, col]
#             found = True
#
# if found:
#     print(f"({location[0]}, {location[1]})")
# else:
#     print(f"{symbol} does not occur in the matrix")
