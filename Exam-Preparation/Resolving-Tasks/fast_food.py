from collections import deque


def read_orders():
    orders = deque(int(x) for x in input().split(" "))
    find_biggest_order(orders)
    return orders


def find_biggest_order(orders):
    biggest_order = max(orders)
    print(biggest_order)


def is_enough_food(food_qty, order):
    return food_qty >= order


def take_orders(orders, food_qty):
    while orders:
        next_order = orders.popleft()
        if is_enough_food(food_qty, next_order):
            food_qty -= next_order
        else:
            orders.appendleft(next_order)
            return orders
    return orders


def print_orders_result(orders):
    if not orders:
        print(f"Orders complete")
    else:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")


quantity_of_the_food = int(input())
orders_list = read_orders()
orders_result = take_orders(orders_list, quantity_of_the_food)
print_orders_result(orders_result)
