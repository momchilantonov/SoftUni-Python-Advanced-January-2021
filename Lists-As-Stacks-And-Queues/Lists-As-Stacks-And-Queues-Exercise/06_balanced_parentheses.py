parenthesis_input = input()


def print_result(is_true):
    if is_true:
        print("YES")
    else:
        print("NO")


def check(parenthesis):
    my_stack = []
    is_balanced = True
    mapping = {"(": ")", "{": "}", "[": "]"}

    for el in parenthesis:
        if el in "({[":
            my_stack.append(el)
        else:
            if not my_stack or not el == mapping[my_stack.pop()]:
                is_balanced = False
                break

    print_result(is_balanced)


check(parenthesis_input)

# parenthesis = input()
#
# my_stack = []
# is_balanced = True
# mapping = {"(": ")", "{": "}", "[": "]"}
#
# for el in parenthesis:
#     if el in "({[":
#         my_stack.append(el)
#     else:
#         if not my_stack or not el == mapping[my_stack.pop()]:
#             is_balanced = False
#             break
#
# if is_balanced:
#     print("YES")
# else:
#     print("NO")
