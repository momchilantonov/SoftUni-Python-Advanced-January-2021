def create_field(size):
    field = [[el for el in input()] for _ in range(size)]
    return field


def find_player_position(field):
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] == "P":
                return r, c


def is_valid(field, pos):
    return 0 <= pos[0] < len(field) and 0 <= pos[1] < len(field)


def read_commands(num_cmd, player_pos, field, txt):
    next_player_pos = []
    for num in range(num_cmd):
        command = input()
        if command == "up":
            next_player_pos = [player_pos[0]-1, player_pos[1]]
        elif command == "down":
            next_player_pos = [player_pos[0]+1, player_pos[1]]
        elif command == "left":
            next_player_pos = [player_pos[0], player_pos[1]-1]
        elif command == "right":
            next_player_pos = [player_pos[0], player_pos[1]+1]

        if is_valid(field, next_player_pos):
            if field[next_player_pos[0]][next_player_pos[1]] == "-":
                field[next_player_pos[0]][next_player_pos[1]] = "P"
                field[player_pos[0]][player_pos[1]] = "-"
                player_pos = next_player_pos
            else:
                txt = txt+field[next_player_pos[0]][next_player_pos[1]]
                field[player_pos[0]][player_pos[1]] = "-"
                field[next_player_pos[0]][next_player_pos[1]] = "P"
                player_pos = next_player_pos
        else:
            if len(txt) > 0:
                txt = txt[:-1]
    return field, txt


def print_result(field, txt):
    print(txt)
    print(*[''.join(el) for el in field], sep='\n')


text = input()
field_size = int(input())
game_field = create_field(field_size)
player_position = find_player_position(game_field)
number_of_commands = int(input())
end_field, end_text = read_commands(number_of_commands, player_position, game_field, text)
print_result(end_field, end_text)
