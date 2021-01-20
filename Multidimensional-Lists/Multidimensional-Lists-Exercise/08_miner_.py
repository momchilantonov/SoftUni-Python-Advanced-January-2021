def init_matrix(s):
    matrix = [[x for x in input().split()] for _ in range(s)]
    return matrix


def init_steps():
    steps = [x for x in input().split()]
    return steps


def miner_start_position(matrix, s):
    position = []
    for r in range(s):
        for c in range(s):
            if matrix[r][c] == "s":
                position = [r, c]
    return position


def calc_coals(matrix, s):
    coals = 0
    for r in range(s):
        for c in range(s):
            if matrix[r][c] == "c":
                coals += 1
    return coals


def is_valid(matrix, curr_pos):
    return 0 <= curr_pos[0] < len(matrix) and 0 <= curr_pos[1] < len(matrix)


size = int(input())
miner_steps = init_steps()
field = init_matrix(size)
miner_position = miner_start_position(field, size)
coals_sum = calc_coals(field, size)
next_miner_position = []
is_end = False

for step in miner_steps:
    if step == "up":
        next_miner_position = [miner_position[0]-1, miner_position[1]]
    elif step == "down":
        next_miner_position = [miner_position[0]+1, miner_position[1]]
    elif step == "left":
        next_miner_position = [miner_position[0], miner_position[1]-1]
    elif step == "right":
        next_miner_position = [miner_position[0], miner_position[1]+1]

    if is_valid(field, next_miner_position):
        row = next_miner_position[0]
        col = next_miner_position[1]
        if field[row][col] == "*":
            field[miner_position[0]][miner_position[1]] = "*"
            field[row][col] = "s"
            miner_position = next_miner_position
        elif field[row][col] == "e":
            print(f"Game over! {row, col}")
            is_end = True
        elif field[row][col] == "c":
            coals_sum -= 1
            if coals_sum == 0:
                print(f"You collected all coals! {row, col}")
                is_end = True
                break
            field[miner_position[0]][miner_position[1]] = "*"
            field[row][col] = "s"
            miner_position = next_miner_position

if not is_end:
    print(f"{coals_sum} coals left. {miner_position[0], miner_position[1]}")
