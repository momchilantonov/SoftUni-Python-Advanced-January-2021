def read_input():
    result = [int(x) for x in input().split(" ")]
    return result


def sort():
    result = sorted(read_input(), key=lambda x: x)
    return result


print(sort())
