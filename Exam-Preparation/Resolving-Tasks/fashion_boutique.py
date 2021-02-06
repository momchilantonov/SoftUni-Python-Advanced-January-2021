from collections import deque


def take_clothes_vol():
    clothes_vol = [int(x) for x in input().split(" ")]
    return clothes_vol


def has_space(rack_cap, cloth):
    return rack_cap >= cloth


def store_clothes(clothes_vol, rack_cap):
    rack_count = 1
    current_rack_cap = rack_cap
    while clothes_vol:
        next_cloth = clothes_vol.pop()
        if has_space(current_rack_cap, next_cloth):
            current_rack_cap -= next_cloth
        else:
            clothes_vol.append(next_cloth)
            rack_count += 1
            current_rack_cap = rack_cap
    return rack_count


def print_used_racks(res):
    print(res)


clothes = take_clothes_vol()
rack_capacity = int(input())
result = store_clothes(clothes, rack_capacity)
print_used_racks(result)
