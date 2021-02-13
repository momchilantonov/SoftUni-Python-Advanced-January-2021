def create_territory(size):
    return [[x for x in input()] for _ in range(size)]


def find_snake_position(territory):
    for r in range(len(territory)):
        for c in range(len(territory[0])):
            if territory[r][c] == "S":
                return r, c


def is_valid_position(territory, row, col):
    return 0 <= row < len(territory) and 0 <= col < len(territory[0])


def find_next_burrow(territory):
    for r in range(len(territory)):
        for c in range(len(territory[0])):
            if territory[r][c] == "B":
                return r, c


def play_snake_game(territory, current_row_pos, current_col_pos):
    food_qty = 0
    next_row_pos = 0
    next_col_pos = 0
    is_snake_in_territory = True
    while food_qty < 10:
        command = input()
        if command == "up":
            next_row_pos, next_col_pos = [current_row_pos-1, current_col_pos]
        elif command == "down":
            next_row_pos, next_col_pos = [current_row_pos+1, current_col_pos]
        elif command == "left":
            next_row_pos, next_col_pos = [current_row_pos, current_col_pos-1]
        elif command == "right":
            next_row_pos, next_col_pos = [current_row_pos, current_col_pos+1]
        if is_valid_position(territory, next_row_pos, next_col_pos):
            if territory[next_row_pos][next_col_pos] == "-":
                territory[current_row_pos][current_col_pos] = "."
                territory[next_row_pos][next_col_pos] = "S"
                current_row_pos = next_row_pos
                current_col_pos = next_col_pos
            elif territory[next_row_pos][next_col_pos] == "*":
                territory[current_row_pos][current_col_pos] = "."
                territory[next_row_pos][next_col_pos] = "S"
                current_row_pos = next_row_pos
                current_col_pos = next_col_pos
                food_qty += 1
            elif territory[next_row_pos][next_col_pos] == "B":
                territory[current_row_pos][current_col_pos] = "."
                territory[next_row_pos][next_col_pos] = "."
                next_burrow_row, next_burrow_col = find_next_burrow(territory)
                territory[next_burrow_row][next_burrow_col] = "S"
                current_row_pos = next_burrow_row
                current_col_pos = next_burrow_col
        else:
            territory[current_row_pos][current_col_pos] = "."
            is_snake_in_territory = False
            return territory, food_qty, is_snake_in_territory
    return territory, food_qty, is_snake_in_territory


def print_game_result(territory, food_qty, snake_in_territory):
    if snake_in_territory and food_qty >= 10:
        print("You won! You fed the snake.")
    else:
        print("Game over!")
    print(f"Food eaten: {food_qty}")
    for row in territory:
        print(''.join(row))


territory_size = int(input())
snake_territory = create_territory(territory_size)
snake_row_position, snake_col_position = find_snake_position(snake_territory)
territory_after_game, food, in_territory = play_snake_game(snake_territory, snake_row_position, snake_col_position)
print_game_result(territory_after_game, food, in_territory)
