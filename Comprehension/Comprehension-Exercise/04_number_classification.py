def read_input():
    list_of_numbers = [int(x) for x in input(). split(", ")]
    return list_of_numbers


def find_positive_numbers(numbers):
    result = [x for x in numbers if x >= 0]
    return result


def find_negative_numbers(numbers):
    result = [x for x in numbers if x < 0]
    return result


def find_even_numbers(numbers):
    result = [x for x in numbers if x % 2 == 0]
    return result


def find_odd_numbers(numbers):
    result = [x for x in numbers if not x % 2 == 0]
    return result


def print_results(numbers):
    print(f"Positive: {', '.join(str(x) for x in find_positive_numbers(numbers))}")
    print(f"Negative: {', '.join(str(x) for x in find_negative_numbers(numbers))}")
    print(f"Even: {', '.join(str(x) for x in find_even_numbers(numbers))}")
    print(f"Odd: {', '.join(str(x) for x in find_odd_numbers(numbers))}")


print_results(read_input())
