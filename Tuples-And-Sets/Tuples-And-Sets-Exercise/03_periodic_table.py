def input_lines(num):
    lines = set()
    for _ in range(num):
        el = input().split(" ")
        for e in el:
            lines.add(e)
    return lines


def print_result(res):
    for r in res:
        print(r)


print_result(input_lines(int(input())))
