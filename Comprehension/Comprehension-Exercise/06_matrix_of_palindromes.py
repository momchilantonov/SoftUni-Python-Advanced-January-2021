def read_matrix_size():
    rows, cols = [int(x) for x in input().split(" ")]
    return rows, cols


def create_ascii_matrix(rows, cols):
    matrix = [[f"{chr(num)}{chr(sec_num)}{chr(num)}" for sec_num in range(num, num+cols)] for num in range(97, 97+rows)]
    return matrix


def print_result(result):
    print(*[' '.join(i) for i in result], sep='\n')


rows_count, cols_count = read_matrix_size()
print_result(create_ascii_matrix(rows_count, cols_count))
