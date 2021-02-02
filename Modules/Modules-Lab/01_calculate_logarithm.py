from math import log


def calc_log(x, base):
    if base == "natural":
        return log(x)
    else:
        return log(x, int(base))


print(calc_log(int(input()), input()))
