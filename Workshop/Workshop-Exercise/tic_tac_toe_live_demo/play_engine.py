from tic_tac_toe_live_demo import setup

from tic_tac_toe_live_demo.helpers import positions_mapper


def draw_board(board):
    print()
    for row in range(len(board)):
        print(f"| {' | '.join(board[row])} |")


def is_position_valid(pos):
    if pos in [str(el) for el in range(1, 10)]:
        return True
    return False


def position_available(board, selected_pos):
    row_num, col_num = positions_mapper[selected_pos]
    current_element = board[row_num][col_num]
    if not current_element == setup.empty_spots:
        return False
    return True


def play_turn(board, sign, selected_pos):
    if position_available(board, selected_pos):
        row_num, col_num = positions_mapper[selected_pos]
        board[row_num][col_num] = sign
        draw_board(board)
    else:
        current_selected_position = input(f"select a valid available position position [0-9]: ")
        current_selected_position = int(current_selected_position)
        #TODO please debug to see the recursion
        play_turn(board, sign, current_selected_position)


def is_row_winner():
    for row_number in range(len(setup.board)):
        if setup.board[row_number].count("X") == 3 or setup.board[row_number].count("O") == 3:
            return True
    return False


def is_col_winner():
    for col_number in range(len(setup.board)):
        if setup.board[0][col_number] == setup.board[1][col_number] == setup.board[2][col_number] != setup.empty_spots:
            return True
    return False


def is_diagonal_winner():
    diagonals = [setup.board[0][0] == setup.board[1][1] == setup.board[2][2] != setup.empty_spots, setup.board[0][2] == setup.board[1][1] == setup.board[2][0] != setup.empty_spots]
    if any(diagonals):
        return True
    return False


def has_won():
    if is_row_winner() or is_col_winner() or is_diagonal_winner():
        return True
    return False


def has_moves(counter):
    if counter < 10:
        return True
    return False


def check_selected_position_is_valid(pos, counter):
    if not pos.isdigit() or not is_position_valid(pos):
        current_selected_position = input(f"{setup.player_names[counter % 2]}, select a position (number between 0-9): ")
        return check_selected_position_is_valid(current_selected_position, counter)
    return pos


def play():
    turns_counter = 1
    while not has_won() and has_moves(turns_counter):
        current_selected_position = input(f"{setup.player_names[turns_counter%2]}, select a position [0-9]: ")
        current_selected_position = check_selected_position_is_valid(current_selected_position, turns_counter)
        current_selected_position = int(current_selected_position)
        play_turn(setup.board, setup.player_signs[turns_counter % 2], current_selected_position)
        turns_counter += 1
    if not has_moves(turns_counter) and not has_won():
        print("No winner")
        return
    turns_counter -= 1
    print(f"{setup.player_names[turns_counter% 2]} won!")
    setup.game_counter[setup.player_names[turns_counter% 2]] += 1