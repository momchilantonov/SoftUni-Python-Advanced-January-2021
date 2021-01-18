def input_lines(in_line):
    line = tuple(ch for ch in in_line)
    return line


def count_chars(val):
    val_count = {}
    for v in val:
        if v not in val_count:
            val_count[v] = 0
        val_count[v] += 1
    ord_val = sorted(val_count.items(), key=lambda x: x[0])
    return ord_val


def print_result(res):
    for r in res:
        print(f"{r[0]}: {r[1]} time/s")


print_result(count_chars(input_lines(input())))
