def read_rows_cols():
    return [int(x) for x in input().split()]


def read_lines():
    return [x for x in input().split()]


def check_valid_input(for_check, arr):
    data = for_check.split()
    if len(data) == 5:
        data[1] = int(data[1])
        data[2] = int(data[2])
        data[3] = int(data[3])
        data[4] = int(data[4])
        return data[0] == "swap" and 0 <= data[1] < len(arr) and 0 <= data[3] < len(arr) \
               and 0 <= data[2] < len(arr[0]) and 0 <= data[4] < len(arr[0])
    else:
        return False


def print_result(arr):
    for r in range(len(arr)):
        print(f"{' '.join(arr[r])}")


rows_count, cols_count = read_rows_cols()
matrix = [read_lines() for _ in range(rows_count)]

while True:
    command = input()
    if command == "END":
        break
    if check_valid_input(command, matrix):
        action, row1, col1, row2, col2 = command.split()
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)
        temp = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp
        print_result(matrix)
    else:
        print("Invalid input!")
