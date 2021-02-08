from collections import deque


def read_customers():
    return deque(int(x) for x in input().split(", "))


def read_taxis():
    return [int(x) for x in input().split(", ")]


def is_transport_possible(customer, taxi):
    return customer <= taxi


def driving_customers(customers, taxis):
    total_time = 0
    while customers:
        if not taxis:
            break
        current_customer = customers.popleft()
        current_taxi = taxis.pop()
        if is_transport_possible(current_customer, current_taxi):
            total_time += current_customer
            continue
        else:
            customers.appendleft(current_customer)
    return customers, total_time


def print_result(customers, total_time):
    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
    else:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(str(x) for x in customers)}")


customers_queue = read_customers()
taxis_queue = read_taxis()
customers_left, total_time_driving = driving_customers(customers_queue, taxis_queue)
print_result(customers_left, total_time_driving)
