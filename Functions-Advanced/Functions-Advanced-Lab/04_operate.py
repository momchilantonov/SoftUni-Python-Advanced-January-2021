from functools import reduce

mapper = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def operate(operator, *args):
    return reduce(mapper[operator], args)


# if operator == "+":
#     return reduce(lambda x, y: x+y, args)
# elif operator == "-":
#     return reduce(lambda x, y: x-y, args)
# elif operator == "*":
#     return reduce(lambda x, y: x * y, args)
# elif operator == "/":
#     return reduce(lambda x, y: x / y, args)


print(operate("-", 20, 2, 5))
