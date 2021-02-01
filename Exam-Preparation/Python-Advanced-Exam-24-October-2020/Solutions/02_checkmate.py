def create_chess_board(size=8):
    board = [[el for el in input().split(" ")] for _ in range(size)]

    return board


def is_valid(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "Q"


def king_movement(board, queens_list, row, col):
    # Check up
    for i in range(len(board)):
        new_row, new_col = row-i, col
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check down
    for i in range(len(board)):
        new_row, new_col = row+i, col
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check left
    for i in range(len(board)):
        new_row, new_col = row, col-i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check Right
    for i in range(len(board)):
        new_row, new_col = row, col+i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check Left-Up
    for i in range(len(board)):
        new_row, new_col = row-i, col-i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check Left-Down
    for i in range(len(board)):
        new_row, new_col = row+i, col-i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check Right-Up
    for i in range(len(board)):
        new_row, new_col = row-i, col+i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break
    # Check Right-Down
    for i in range(len(board)):
        new_row, new_col = row+i, col+i
        if is_valid(board, new_row, new_col):
            queens_list.append([new_row, new_col])
            break

    return queens_list


def looping_thru_board(board):
    queens = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "K":
                queens = king_movement(board, queens, r, c)
                break

    return queens


def print_result(res):
    if not res:
        print("The king is safe!")
    else:
        for r in res:
            print(r)


chess_board = create_chess_board()
result = looping_thru_board(chess_board)
print_result(result)
