def expressions(nums, curr_sum=0, expression=''):
    if not nums:
        return [(expression, curr_sum)]

    result_plus = expressions(nums[1:], curr_sum+nums[0], f"{expression}+{nums[0]}")
    result_minus = expressions(nums[1:], curr_sum-nums[0], f"{expression}-{nums[0]}")
    return result_plus+result_minus


numbers = [int(el) for el in input().split(", ")]

print(*[f"{el[0]}={el[1]}" for el in expressions(numbers)], sep='\n')
