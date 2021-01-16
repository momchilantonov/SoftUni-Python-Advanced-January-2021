def input_line(num):
    in_line = set()
    for _ in range(num):
        in_line.add(input())
    return in_line


def print_result(res):
    for i in res:
        print(i)


names = input_line(int(input()))
print_result(names)
