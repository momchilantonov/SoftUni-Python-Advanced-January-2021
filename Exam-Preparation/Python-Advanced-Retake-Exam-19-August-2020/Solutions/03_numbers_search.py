def numbers_searching(*nums):
    consecutive_nums = []
    duplicate_nums = []
    for num in nums:
        if num not in consecutive_nums:
            consecutive_nums.append(num)
        else:
            if num not in duplicate_nums:
                duplicate_nums.append(num)

    start_num = min(consecutive_nums)
    end_num = max(consecutive_nums)
    list_for_check = list(range(start_num, end_num+1))
    missing_nums = []
    for num in list_for_check:
        if num not in consecutive_nums:
            missing_nums.append(num)

    return [*missing_nums, list(sorted(duplicate_nums))]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
