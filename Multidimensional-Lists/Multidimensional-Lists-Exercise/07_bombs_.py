def create_matrix(s):
    matrix = [[int(x) for x in input().split()] for _ in range(s)]
    return matrix


def is_valid(row, col, s):
    return 0 <= row < s and 0 <= col < s


def explode_bomb(arr, s, bomb_row, bomb_col):
    bomb = arr[bomb_row][bomb_col]
    for row in range(bomb_row-1, bomb_row+2):
        for col in range(bomb_col-1, bomb_col+2):
            if is_valid(row, col, s) and arr[row][col] > 0:
                arr[row][col] -= bomb


def read_bombs(arr, s):
    bombs_data = input().split()

    for bombs in bombs_data:
        bomb = [int(x) for x in bombs.split(",")]
        bomb_row = bomb[0]
        bomb_col = bomb[1]

        if arr[bomb_row][bomb_col] > 0:
            explode_bomb(arr, s, bomb_row, bomb_col)
            # arr[bomb_row][bomb_col] = 0

    alive_cells_count = 0
    alive_cells_sum = 0

    for row in range(s):
        for col in range(s):
            num = arr[row][col]
            if num > 0:
                alive_cells_count += 1
                alive_cells_sum += num

    print(f"Alive cells: {alive_cells_count}")
    print(f"Sum: {alive_cells_sum}")

    for row in arr:
        print(" ".join([str(x) for x in row]))


size = int(input())
read_bombs(create_matrix(size), size)
