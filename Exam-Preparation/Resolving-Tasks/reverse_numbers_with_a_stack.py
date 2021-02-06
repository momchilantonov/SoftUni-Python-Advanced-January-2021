def read_input():
    numbers_list = [x for x in input().split(" ")]
    return numbers_list


def reverse_with_stack(nums):
    reversed_list = []
    for _ in range(len(nums)):
        reversed_list.append(nums.pop())
    return reversed_list


def print_result(nums):
    print(' '.join(nums))


num_list = read_input()
rev_list = reverse_with_stack(num_list)
print_result(rev_list)
