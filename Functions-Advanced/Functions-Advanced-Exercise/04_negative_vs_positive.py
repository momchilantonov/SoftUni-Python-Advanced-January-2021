def read_input():
    result = [int(x) for x in input().split(" ")]
    return result


def find_positive_numbers_sum(nums):
    result = sum([num for num in nums if num >= 0])
    return result


def find_negative_numbers_sum(nums):
    result = sum([num for num in nums if num < 0])
    return result


def numbers_sum_fight(positive_sum, negative_sum, is_pos=True):
    if abs(negative_sum) > positive_sum:
        is_pos = False
        return is_pos
    elif positive_sum > abs(negative_sum):
        return is_pos


def print_result(is_pos, nums):
    if is_pos:
        print(find_negative_numbers_sum(nums))
        print(find_positive_numbers_sum(nums))
        print("The positives are stronger than the negatives")
    else:
        print(find_negative_numbers_sum(nums))
        print(find_positive_numbers_sum(nums))
        print("The negatives are stronger than the positives")


numbers = read_input()
positive_numbers_sum = find_positive_numbers_sum(numbers)
negative_numbers_sum = find_negative_numbers_sum(numbers)
battle_result = numbers_sum_fight(positive_numbers_sum, negative_numbers_sum)
print_result(battle_result, numbers)
