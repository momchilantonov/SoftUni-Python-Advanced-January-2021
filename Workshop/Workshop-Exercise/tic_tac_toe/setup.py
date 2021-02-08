def setup_players():
    global player_one, player_two
    player_one = input("Player 1 name: ")
    player_two = input("Player 2 name: ")

    player_one_sign = input(f"{player_one}, please select a sign (O or X): ")
    while player_one_sign.lower()  not in ("x", "o"):
        player_one_sign = input(f"{player_one}, please select a sign (O or X)")
    player_two_sign = "O" if player_one_sign.lower() == "x" else "X"
    global turn_signs, turn_names
    turn_signs = {1: player_one_sign, 0: player_two_sign}
    turn_names = {1: player_one, 0: player_two}
    print("This is the numeration of the board")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print("Player one starts first")


def setup_board():
    global board
    board = [["", "", ""] for _ in range(3)]


