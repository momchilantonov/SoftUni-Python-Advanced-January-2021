def read_numbers():
    return [int(x) for x in input().split(" ")]


def find_odds_sum(nums):
    return sum([num for num in nums if num % 2 == 0]) * len(nums)


def find_evens_sum(nums):
    return sum([num for num in nums if not num % 2 == 0]) * len(nums)


def check_command_and_numbers_sum(cmd, nums):
    if cmd == "Odd":
        evens_sum = find_evens_sum(nums)
        return evens_sum
    odds_sum = find_odds_sum(nums)
    return odds_sum


def print_result(cmd, nums):
    return check_command_and_numbers_sum(cmd, nums)


command = input()
numbers = read_numbers()
print(print_result(command, numbers))
