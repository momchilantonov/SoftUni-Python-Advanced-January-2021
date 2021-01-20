from collections import deque


def read_size():
    return [int(x) for x in input().split(" ")]


def read_snake():
    snake_list = deque(x for x in input())
    return snake_list


def snake_moves(arr, rows, cols, python):
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                snake_ch = python.popleft()
                arr[i][j] = snake_ch
                python.append(snake_ch)
        else:
            for j in range(cols-1, -1, -1):
                snake_ch = python.popleft()
                arr[i][j] = snake_ch
                python.append(snake_ch)
    return arr


def print_result(arr, row):
    for x in range(row):
        print(f"{''.join(arr[x])}")


rows_count, cols_count = read_size()
matrix = [["a"] * cols_count for _ in range(rows_count)]
snake = read_snake()
snake_moves(matrix, rows_count, cols_count, snake)
print_result(matrix, rows_count)
