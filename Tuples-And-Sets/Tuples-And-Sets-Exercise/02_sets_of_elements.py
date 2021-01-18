def input_lines(num):
    lines = set()
    for _ in range(num):
        lines.add(input())
    return lines


def intersection(a, b):
    return a.intersection(b)


def print_result(res):
    for r in res:
        print(r)


len1, len2 = input().split(" ")

line1 = input_lines(int(len1))
line2 = input_lines(int(len2))

print_result(intersection(line1, line2))
