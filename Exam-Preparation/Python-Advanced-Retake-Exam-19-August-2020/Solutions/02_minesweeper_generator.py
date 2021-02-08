def create_field(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def find_bomb_positions(bombs):
    bomb_x_pos = []
    bomb_y_pos = []
    for bomb in range(bombs):
        bomb_x, bomb_y = input().replace("(", "").replace(")", "").split(", ")
        bomb_x = int(bomb_x)
        bomb_y = int(bomb_y)
        bomb_x_pos.append(bomb_x)
        bomb_y_pos.append(bomb_y)
    return bomb_x_pos, bomb_y_pos


def put_bombs_into_the_field(field, bomb_x, bomb_y):
    for i in range(len(bomb_x)):
        field[bomb_x[i]][bomb_y[i]] = "*"
    return field


def is_valid_position(field, row, col):
    return 0 <= row < len(field) and 0 <= col < len(field[0])


def calc_bombs_for_cell(field, current_row, current_col):
    bombs_counter = 0
    rows = [0, 1, 1, 1, 0, -1, -1, -1]
    cols = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(len(rows)):
        next_row = current_row+rows[i]
        next_col = current_col+cols[i]
        if is_valid_position(field, next_row, next_col) and field[next_row][next_col] == "*":
            bombs_counter += 1
    return bombs_counter


def loop_thru_field(field):
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == "*":
                continue
            else:
                field[row][col] = calc_bombs_for_cell(field, row, col)
    return field


def print_final_game_field(field):
    for row in field:
        print(' '.join(str(x) for x in row))


field_size = int(input())
bombs_number = int(input())

mines_field_template = create_field(field_size)
bomb_x_positions, bomb_y_positions = find_bomb_positions(bombs_number)
mines_field_with_bombs = put_bombs_into_the_field(mines_field_template, bomb_x_positions, bomb_y_positions)
final_mines_field = loop_thru_field(mines_field_with_bombs)
print_final_game_field(final_mines_field)
