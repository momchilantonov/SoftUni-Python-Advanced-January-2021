def read_input(data):
    rows, columns = [int(x) for x in data.split(", ")]
    arr = [0 for _ in range(rows)]
    for row in range(rows):
        lines = [int(x) for x in input().split(", ")]
        arr[row] = lines
    return arr


def result(matrix):
    res = sum([sum(el) for el in matrix])
    return res


def print_result(res, matrix):
    print(res)
    print(matrix)


array = read_input(input())
print_result(result(array), array)
