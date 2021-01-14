from collections import deque

food_qty = int(input())
orders = deque(int(el) for el in input().split(" "))


def print_result(queue):
    if queue:
        print(f"Orders left: {' '.join([str(el) for el in queue])}")
    else:
        print("Orders complete")


def food_check(food, queue):
    print(max(queue))

    while queue:
        f = queue.popleft()
        if f <= food:
            food -= f
        else:
            queue.appendleft(f)
            break

    print_result(queue)


food_check(food_qty, orders)

# from collections import deque
#
# food = int(input())
# orders = deque(int(el) for el in input().split(" "))
#
# print(max(orders))
#
# while orders:
#     order = orders.popleft()
#     if order <= food:
#         food -= order
#     else:
#         orders.appendleft(order)
#         break
#
#
# if orders:
#     print(f"Orders left: {' '.join([str(el) for el in orders])}")
# else:
#     print("Orders complete")





