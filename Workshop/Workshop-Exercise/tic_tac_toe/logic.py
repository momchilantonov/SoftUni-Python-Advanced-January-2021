from tic_tac_toe import setup

board_mapper = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}


def get_row_winner():
    sign = None
    for row in range(len(setup.board)):
        if setup.board[row][0] == setup.board[row][1] == setup.board[row][2] != '':
            sign = setup.board[row][0]
    return sign


def get_column_winner():
    sign = None
    for col in range(len(setup.board)):
        if setup.board[0][col] == setup.board[1][col] == setup.board[2][col] != '':
            sign = setup.board[0][col]
    return sign


def get_diagonal_winner():
    sign = None
    if setup.board[0][0] == setup.board[1][1] == setup.board[2][2] != '':
        sign = setup.board[0][0]
    if setup.board[2][0] == setup.board[1][1] == setup.board[0][2] != '':
        sign = setup.board[0][-3]
    return sign


def get_winner():
    row_winner = get_row_winner()
    column_winner = get_column_winner()
    diagonal_winner = get_diagonal_winner()
    return row_winner or column_winner or diagonal_winner


def has_more_turns(turn):
    if turn >= 9:
        print("No turns left. No winner")
        exit(0)
    return True


def get_spot(c_m):
    if c_m in range(1, 10):
        indexes = board_mapper[c_m]
        if setup.board[indexes[0]][indexes[1]] == "":
            return indexes
    return


def display_board():
    print()
    for row in range(len(setup.board)):
        for col in range(len(setup.board)):
            print(f"| {setup.board[row][col]} ", end="")
        print("|")


def play():
    turn_count = 0
    winner_sign = get_winner()
    while not winner_sign and has_more_turns(turn_count):
        turn_count += 1
        current_move = int(input(f"{setup.turn_names[turn_count%2]}, selects spot: "))
        spot = get_spot(current_move)
        while not spot:
            current_move = int(input(f"Invalid spot! {setup.turn_names[turn_count % 2]}, selects spot: "))
            spot = get_spot(current_move)
        setup.board[spot[0]][spot[1]] = setup.turn_signs[turn_count%2]
        display_board()
        winner_sign = get_winner()


    winner_name = setup.turn_names[{name: number for number, name in setup.turn_signs.items()}[setup.turn_signs[turn_count%2]]]
    print(f"Congrats, {winner_name} you won!")
    exit(0)
