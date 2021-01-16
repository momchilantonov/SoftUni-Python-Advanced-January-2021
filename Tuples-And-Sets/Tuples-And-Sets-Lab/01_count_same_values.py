def input_line(in_line):
    val = tuple(float(el) for el in in_line.split(" "))
    return val


def count_values(val):
    val_count = {}
    for v in val:
        if v not in val_count:
            val_count[v] = 0
        val_count[v] += 1
    return val_count


def print_result(res):
    for k, v in res.items():
        print(f"{k} - {v} times")


values = input_line(input())
result = count_values(values)
print_result(result)
