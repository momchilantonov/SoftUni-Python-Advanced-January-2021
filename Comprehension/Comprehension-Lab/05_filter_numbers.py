def is_number_valid(number):
    # return len([True for d in range(2, 11) if number % d == 0]) > 0
    return any([number % d == 0 for d in range(2, 11)])


def filter_number(start, stop):
    return [num for num in range(start, stop+1) if is_number_valid(num)]


start_number = int(input())
end_number = int(input())

print(filter_number(start_number, end_number))
