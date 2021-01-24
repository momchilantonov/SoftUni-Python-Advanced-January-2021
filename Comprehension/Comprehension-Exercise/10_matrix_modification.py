def creat_matrix(rows):
    mtrx = [[int(x) for x in input().split()] for _ in range(rows)]

    return mtrx


def read_commands(command):
    action, x, y, value = command.split()
    value = int(value)
    x = int(x)
    y = int(y)

    return action, x, y, value


def add_action(cmd, mtrx):
    x = cmd[1]
    y = cmd[2]
    val = cmd[3]

    mtrx[x][y] += val

    return mtrx


def sub_action(cmd, mtrx):
    x = cmd[1]
    y = cmd[2]
    val = cmd[3]

    mtrx[x][y] -= val

    return mtrx


def is_valid(cmd, mtrx):
    return 0 <= cmd[1] < len(mtrx) and 0 <= cmd[2] < len(mtrx)


def looping(mtrx):
    while True:
        command = input()
        if command == "END":
            break

        if read_commands(command)[0] == "Add" and is_valid(read_commands(command), mtrx):
            mtrx = add_action(read_commands(command), mtrx)
        elif read_commands(command)[0] == "Subtract" and is_valid(read_commands(command), mtrx):
            mtrx = sub_action(read_commands(command), mtrx)
        else:
            print("Invalid coordinates")

    return matrix


def print_result(res):
    print(*[' '.join(str(x) for x in row) for row in res], sep="\n")


matrix_rows = int(input())
matrix = creat_matrix(matrix_rows)
result = looping(matrix)
print_result(result)
