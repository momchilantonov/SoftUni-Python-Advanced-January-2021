def read_input():
    data = [x for x in input().split("|")]
    data.reverse()
    return data


def flattened_list(data):
    result = [num for i in range(len(data)) for num in data[i].split()]
    return result


def print_result(result):
    print(*result)


input_data = read_input()
print_result(flattened_list(input_data))
