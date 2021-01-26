def read_input():
    result = [int(x) for x in input().split(" ")]
    return result


def min_value(nums):
    result = min(nums)
    return result


def max_value(nums):
    result = max(nums)
    return  result


def sum_values(nums):
    result = sum(nums)
    return result


def print_result(nums):
    print(f"The minimum number is {min_value(nums)}")
    print(f"The maximum number is {max_value(nums)}")
    print(f"The sum number is: {sum_values(nums)}")


numbers = read_input()
print_result(numbers)
