def reverse_nums(nums):
    result = []

    while nums:
        result.append(nums.pop())
    return ' '.join(result)


print(reverse_nums(input().split(" ")))
