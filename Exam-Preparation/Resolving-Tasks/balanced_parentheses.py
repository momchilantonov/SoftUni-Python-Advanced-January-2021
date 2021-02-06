OPEN_BRACKETS = ["(", "[", "{"]
CLOSE_BRACKETS = [")", "]", "}"]


def check_brackets():
    check_stack = []
    for bracket in input():
        if bracket in OPEN_BRACKETS:
            check_stack.append(bracket)
        else:
            bracket_idx = CLOSE_BRACKETS.index(bracket)
            if check_stack and OPEN_BRACKETS[bracket_idx] == check_stack[-1]:
                check_stack.pop()
            else:
                return "NO"
    if not check_stack:
        return "YES"
    else:
        return "NO"


print(check_brackets())
