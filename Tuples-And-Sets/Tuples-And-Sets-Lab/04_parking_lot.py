def input_line(num):
    res = set()
    for _ in range(num):
        cmd, plate = input().split(", ")
        if cmd == "IN":
            res.add(plate)
        elif cmd == "OUT":
            res.remove(plate)
    return res


def print_result(res):
    if res:
        for r in res:
            print(r)
    else:
        print("Parking Lot is Empty")


print_result(input_line(int(input())))
