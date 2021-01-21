def init_matrix_rows_cols():
    return [int(x) for x in input().split()]


def init_matrix(rows):
    matrix = []
    for r in range(rows):
        matrix.append([x for x in input()])
    return matrix


def init_commands():
    return [x for x in input()]


def find_player_position(matrix, rows, cols):
    position = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "P":
                position = [r, c]
    return position


def find_bunnies_positions(matrix, rows, cols):
    position = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "B":
                position.append([r, c])
    return position


def is_valid(matrix, next_pos):
    return 0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix[0])


def spread_bunnies():
    b_rows = [-1, 0, 1, 0]
    b_cols = [0, 1, 0, -1]
    for bunny in range(len(bunnies_positions)):
        for i in range(len(b_rows)):
            new_bunny = [bunnies_positions[bunny][0]+b_rows[i], bunnies_positions[bunny][1]+b_cols[i]]
            if is_valid(lair, new_bunny):
                if lair[new_bunny[0]][new_bunny[1]] == "B":
                    continue
                elif lair[new_bunny[0]][new_bunny[1]] == ".":
                    lair[new_bunny[0]][new_bunny[1]] = "B"
                    bunnies_positions.append([new_bunny[0], new_bunny[1]])
                else:
                    lair[new_bunny[0]][new_bunny[1]] = "B"
                    player_position.clear()


rows_count, cols_count = init_matrix_rows_cols()
lair = init_matrix(rows_count)
commands = init_commands()
player_position = find_player_position(lair, rows_count, cols_count)
bunnies_positions = find_bunnies_positions(lair, rows_count, cols_count)

for command in commands:
    next_player_position = []
    if command == "U":
        next_player_position = [player_position[0]-1, player_position[1]]
    elif command == "D":
        next_player_position = [player_position[0]+1, player_position[1]]
    elif command == "L":
        next_player_position = [player_position[0], player_position[1]-1]
    elif command == "R":
        next_player_position = [player_position[0], player_position[1]+1]

    row = next_player_position[0]
    col = next_player_position[1]

    if is_valid(lair, next_player_position):
        if lair[row][col] == ".":
            lair[player_position[0]][player_position[1]] = "."
            lair[row][col] = "P"
            player_position = next_player_position
            spread_bunnies()
            if not player_position:
                for line in lair:
                    print("".join(line))
                print(f"dead: {row} {col}")
                break
        else:
            lair[player_position[0]][player_position[1]] = "."
            spread_bunnies()
            for line in lair:
                print("".join(line))
            print(f"dead: {row} {col}")
            break
    else:
        lair[player_position[0]][player_position[1]] = "."
        spread_bunnies()
        for line in lair:
            print("".join(line))
        print(f"won: {player_position[0]} {player_position[1]}")
        break

