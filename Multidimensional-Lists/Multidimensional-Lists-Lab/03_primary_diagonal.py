def create_matrix(row):
    matrix = [[0] * int(row) for _ in range(int(row))]
    return matrix


def add_values(matrix):
    for idx in range(len(matrix)):
        line = [int(x) for x in input().split(" ")]
        matrix[idx] = line
    return matrix


def calc_diagonal(matrix):
    diagonal = sum(matrix[len(matrix)-i-1][len(matrix)-i-1] for i in range(len(matrix)))
    return diagonal


print(calc_diagonal(add_values(create_matrix(input()))))

# size = int(input())
# matrix = [[0] * size for row in range(0, size)]
#
# for x in range(0, size):
#     line = list(map(int, input().split()))
#     for y in range(0, size):
#         matrix[x][y] = line[y]
#
# sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
# print(sum_diagonal)
