from collections import deque

cups = deque(int(el) for el in input().split(" "))
bottles = [int(el) for el in input().split(" ")]
wasted_water = 0


def pour(water):
    if spillway["cups"] <= spillway["bottles"]:
        water += spillway["bottles"]-spillway["cups"]
        return water
    else:
        spillway["cups"] -= spillway["bottles"]
        cups.appendleft(spillway["cups"])
        return water


def print_result():
    if len(cups) == 0:
        print(f"Bottles: {' '.join([str(el) for el in bottles])}")
    else:
        print(f"Cups: {' '.join([str(el) for el in cups])}")

    print(f"Wasted litters of water: {wasted_water}")


while cups and bottles:
    spillway = {"cups": cups.popleft(), "bottles": bottles.pop()}
    wasted_water = pour(wasted_water)

print_result()

# from collections import deque
#
# cups = deque(int(el) for el in input().split(" "))
# bottles = [int(el) for el in input().split(" ")]
# wasted_water = 0
#
# while cups and bottles:
#     spillway = {"cups": cups.popleft(), "bottles": bottles.pop()}
#     if spillway["cups"] <= spillway["bottles"]:
#         wasted_water += spillway["bottles"]-spillway["cups"]
#     else:
#         spillway["cups"] -= spillway["bottles"]
#         cups.appendleft(spillway["cups"])
#
# if len(cups) == 0:
#     print(f"Bottles: {' '.join([str(el) for el in bottles])}")
# else:
#     print(f"Cups: {' '.join([str(el) for el in cups])}")
#
# print(f"Wasted litters of water: {wasted_water}")
