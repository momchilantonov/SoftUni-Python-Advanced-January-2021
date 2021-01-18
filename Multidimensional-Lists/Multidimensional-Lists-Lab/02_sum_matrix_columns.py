def rows_columns(data):
    row, column = [int(x) for x in data.split(", ")]
    return row, column


def array(row, column):
    matrix = [[0] * column for _ in range(row)]
    for row in range(row):
        lines = [int(x) for x in input().split(" ")]
        matrix[row] = lines
    return matrix


def result(row, column, matrix):
    summed = [0] * column
    for c in range(column):
        for r in range(row):
            summed[c] += matrix[r][c]
        print(summed[c])


rows, columns = rows_columns(input())
arr = array(rows, columns)
result(rows, columns, arr)

# sizes = list(map(int, input().split(", ")))
# columns = sizes[1]
# rows = sizes[0]
# matrix = [[0] * columns for row in range(rows)]
#
# for row in range(rows):
#     lines = list(map(int, input().split()))
#     for column in range(columns):
#         matrix[row][column] = lines[column]
# summed = [0] * columns
#
# for column in range(columns):
#     for row in range(rows):
#         summed[column] += matrix[row][column]
#     print(summed[column])
