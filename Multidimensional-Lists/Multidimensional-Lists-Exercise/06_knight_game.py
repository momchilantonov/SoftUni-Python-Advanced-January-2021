def creat_board(n):
    # matrix = [[x for x in input()] for _ in range(n)]
    matrix = []
    for _ in range(n):
        matrix.append([x for x in input()])

    return matrix


def is_valid(pos, n):
    row = pos[0]
    col = pos[1]
    return 0 <= row < n and 0 <= col < n


def check_killed_knight(arr, n, row, col):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(len(rows)):
        curr_pos = [row+rows[i], col+cols[i]]
        if is_valid(curr_pos, n) and arr[curr_pos[0]][curr_pos[1]] == "K":
            killed_knights += 1
    return killed_knights


def play_game(arr, n):
    total_kills = 0

    while True:
        most_kills = 0
        kill = []

        for row in range(n):
            for col in range(n):
                if arr[row][col] == "K":
                    killed_knights = check_killed_knight(arr, n, row, col)
                    if killed_knights > most_kills:
                        most_kills = killed_knights
                        kill = [row, col]

        if most_kills == 0:
            break
        kill_row = kill[0]
        kill_col = kill[1]
        arr[kill_row][kill_col] = "0"
        total_kills += 1

    return total_kills


size = int(input())
print(play_game(creat_board(size), size))
