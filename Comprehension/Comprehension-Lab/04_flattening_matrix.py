# def read_matrix(r):
#     matrix = [[int(x) for x in input().split(", ")] for _ in range(r)]
#     return matrix
#
#
# def flattening_matrix(matrix):
#     result = []
#     for row in matrix:
#         [result.append(x) for x in row]
#     return result
#
#
# rows = int(input())
#
# print(flattening_matrix(read_matrix(rows)))


def read_matrix(r):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(r)]
    return matrix


def flattening_matrix(matrix):
    result = [x for row in matrix for x in row]
    return result


rows = int(input())

print(flattening_matrix(read_matrix(rows)))
