def setup():
    global player_1_name, player_2_name
    global game_counter

    player_1_name = input("Enter player 1 name: ")
    player_2_name = input("Enter player 2 name: ")
    game_counter = {player_1_name: 0, player_2_name: 0}
    player_1_sign = input("Player 1, please select a sign X or O: ")
    while player_1_sign.lower() not in ("x", "o"):
        player_1_sign = input(f"{player_1_name}, please select a sign X or O: ")
    player_1_sign = player_1_sign.upper()
    player_2_sign = "O" if player_1_sign == "X" else "X"
    global player_signs, player_names
    player_signs = {1: player_1_sign, 0: player_2_sign}
    player_names = {1: player_1_name, 0: player_2_name}
    global empty_spots
    empty_spots = input("Please select the empty spots of the board")
    while empty_spots.lower() in ("x", "o"):
        empty_spots = input("Please select the empty spots of the board")
    global board
    board = [[empty_spots, empty_spots, empty_spots] for _ in range(3)]
    print("This is the numeration of the board: ")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print("Player one starts first!")

