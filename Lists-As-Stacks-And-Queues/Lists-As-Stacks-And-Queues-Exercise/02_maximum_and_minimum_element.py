PUSH = "1"
DELETE = "2"
PRINT_MAX = "3"
PRINT_MIN = "4"


def push(num, stack):
    stack.append(num)
    return stack


def delete(stack):
    stack.pop()
    return stack


def print_max(stack):
    max_n = max([int(el) for el in stack])
    return max_n


def print_min(stack):
    min_n = min([int(el) for el in stack])
    return min_n


def main(queries):
    nums = []
    result = []
    for _ in range(queries):
        command = input()
        if command.startswith(PUSH):
            query = command.split(" ")
            nums = push(query[1], nums)
        elif command == DELETE and nums:
            nums = delete(nums)
        elif command == PRINT_MAX and nums:
            print(print_max(nums))
        elif command == PRINT_MIN and nums:
            print(print_min(nums))

    while nums:
        result.append(nums.pop())

    print(f"{', '.join(result)}")


main(int(input()))
