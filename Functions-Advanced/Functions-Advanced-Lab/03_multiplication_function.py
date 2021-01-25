def multiply(*args):
    result = 1
    for x in args:
        result = result * x
    return result


print(multiply(4, 5, 6, 1, 3))
