def read_input(separator=" "):
    return [int(x) for x in input().split(separator)]


def calc_primary_diagonal(arr):
    # sum_diagonal = 0
    # for i in range(len(arr)):
    #     sum_diagonal += arr[i][i]
    # return sum_diagonal
    return sum([arr[i][i] for i in range(len(arr))])


def calc_secondary_diagonal(arr):
    # sum_diagonal = 0
    # for i in range(len(arr)):
    #     sum_diagonal += arr[i][-i-1]
    # return sum_diagonal
    return sum([arr[i][-i-1] for i in range(len(arr))])


def calc_below_primary_diagonal(arr):
    the_sum = 0
    for row in range(len(arr)):
        for col in range(row+1):  # if the PD is included row < col (row+1) # if the PD is excluded row == col (row)
            the_sum += arr[row][col]
    return the_sum


def calc_below_secondary_diagonal(arr):
    the_sum = 0
    for row in range(len(arr)):
        for col in range(len(arr)-row-1, len(arr)):  # if the PD is included row < col (row+1) # if the PD is excluded row == col (row)
            the_sum += arr[row][col]
    return the_sum


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(read_input())

print(abs(calc_primary_diagonal(matrix)-calc_secondary_diagonal(matrix)))
