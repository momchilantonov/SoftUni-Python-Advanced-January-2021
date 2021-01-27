def recursive_power(num, pwr, result=1):
    result *= num
    if pwr == 1:
        return result
    return recursive_power(num, pwr-1, result=result)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
