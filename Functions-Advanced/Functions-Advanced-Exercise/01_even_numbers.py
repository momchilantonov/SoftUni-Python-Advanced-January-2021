def read_input():
    nums = [int(x) for x in input().split(" ")]
    return nums


def filter_even_numbers():
    # result = [x for x in read_input() if x % 2 == 0w]
    result = list(filter(lambda x: x % 2 == 0, read_input()))
    return result


print(filter_even_numbers())
