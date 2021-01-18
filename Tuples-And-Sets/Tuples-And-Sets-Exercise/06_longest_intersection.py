def input_lines(num):
    data = []
    for _ in range(num):
        first_range, second_range = input().split("-")
        pf1, pf2 = first_range.split(",")
        pf1 = int(pf1)
        pf2 = int(pf2)
        ps1, ps2 = second_range.split(",")
        ps1 = int(ps1)
        ps2 = int(ps2)
        total_range = range(max(pf1, ps1), min(pf2, ps2)+1)
        data.append([el for el in total_range])
    return data


def result(data):
    longest_one = sorted(data, key=lambda x: -len(x))[0]
    return longest_one


def print_result(res):
    print(f"Longest intersection is {res} with length {len(res)}")


print_result(result(input_lines(int(input()))))
