import pypandoc


def input_lines(num):
    even = set()
    odd = set()
    for idx in range(1, num+1):
        name = input()
        data = sum(ord(ch) for ch in name) // idx
        if data % 2 == 0:
            even.add(data)
        else:
            odd.add(data)
    return even, odd


def result(data):
    sum_evens = sum(data[0])
    sum_odds = sum(data[1])
    if sum_evens == sum_odds:
        res = data[0].union(data[1])
        return res
    elif sum_evens < sum_odds:
        res = data[1].difference(data[0])
        return res
    else:
        res = data[0].symmetric_difference(data[1])
        return res


def print_result(res):
    print(f"{', '.join(str(el) for el in res)}")


print_result(result(input_lines(int(input()))))
