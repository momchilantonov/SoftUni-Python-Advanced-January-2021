from collections import deque


def best_list_pureness(*args):
    numbers_list = deque(int(num) for num in args[0])
    rotate_numbers = int(args[1])
    counter = 0
    best_counter = 0
    best_pureness = 0

    for _ in range(rotate_numbers+1):
        curr_pureness = sum(numbers_list[i] * i for i in range(len(numbers_list)))
        if curr_pureness > best_pureness:
            best_pureness = curr_pureness
            best_counter = counter
        numbers_list.appendleft(numbers_list.pop())
        counter += 1

    return f"Best pureness {best_pureness} after {best_counter} rotations"


print(best_list_pureness([7, 9, 2, 5, 3, 4], 3))
