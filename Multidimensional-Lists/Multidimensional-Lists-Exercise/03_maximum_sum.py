def read_rows_cols():
    return [int(x) for x in input().split()]


def get_sub_matrix_sum(arr, row, col, size):
    the_sum = 0
    for r in range(row, row+size):
        for c in range(col, col+size):
            the_sum += arr[r][c]
    return the_sum


def print_sum(arr, row, col, size):
    for r in range(row, row+size):
        for c in range(col, col+size):
            print(arr[r][c], end=" ")
        print()


rows_count, cols_count = read_rows_cols()
matrix = [read_rows_cols() for _ in range(rows_count)]
size = 3
best_value = get_sub_matrix_sum(matrix, 0, 0, size)
best_position = (0, 0)

for r in range(len(matrix)-size+1):
    for c in range(len(matrix[r])-size+1):
        current_value = get_sub_matrix_sum(matrix, r, c, size)
        if best_value < current_value:
            best_value = current_value
            best_position = (r, c)

print(f"Sum = {best_value}")
best_row, best_col = best_position
print_sum(matrix, best_row, best_col, size)
