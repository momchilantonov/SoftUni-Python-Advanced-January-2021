clothes = [int(el) for el in input().split(" ")]
rack_cap = int(input())


def print_result(data, result):
    if data > 0:
        print(result+1)
    else:
        print(result)


def check(clothes_data, rack_volume):
    sum_clothes = 0
    sum_racks = 0

    while clothes_data:
        clothe_val = clothes_data.pop()
        sum_clothes += clothe_val
        if sum_clothes == rack_volume:
            sum_clothes = 0
            sum_racks += 1
        elif sum_clothes > rack_volume:
            clothes_data.append(clothe_val)
            sum_clothes = 0
            sum_racks += 1

    print_result(sum_clothes, sum_racks)


check(clothes, rack_cap)

# sum_racks = 0
# sum_clothes = 0
#
# while clothes:
#     clothe_val = clothes.pop()
#     sum_clothes += clothe_val
#     if sum_clothes == rack_cap:
#         sum_clothes = 0
#         sum_racks += 1
#     elif sum_clothes > rack_cap:
#         clothes.append(clothe_val)
#         sum_clothes = 0
#         sum_racks += 1
#
# if sum_clothes > 0:
#     print(sum_racks+1)
# else:
#     print(sum_racks)
