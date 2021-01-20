def read_rows_cols(separator=" "):
    return [int(x) for x in input().split(separator)]


def read_lines(separator=" "):
    return [x for x in input().split(separator)]


def check_uniformity(arr, r, c):
    return arr[r][c] == arr[r+1][c] == arr[r][c+1] == arr[r+1][c+1]


rows_count, cols_count = read_rows_cols()
matrix = [read_lines() for _ in range(rows_count)]
cells_counter = 0

for row in range(len(matrix)-1):
    for col in range(len(matrix[row])-1):
        if check_uniformity(matrix, row, col):
            cells_counter += 1

print(cells_counter)
