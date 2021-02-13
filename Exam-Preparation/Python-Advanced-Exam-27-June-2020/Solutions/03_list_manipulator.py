from collections import deque


def list_manipulator(nums_queue, command, position, *args):
    if command == "add" and position == "beginning":
        nums_queue = deque(nums_queue)
        nums_to_add = [*args]
        while nums_to_add:
            nums_queue.appendleft(nums_to_add.pop())
        return list(nums_queue)
    elif command == "add" and position == "end":
        nums_to_add = deque([*args])
        while nums_to_add:
            nums_queue.append(nums_to_add.popleft())
        return nums_queue
    elif command == "remove" and position == "beginning":
        nums_queue = deque(nums_queue)
        if not args:
            nums_queue.popleft()
            return list(nums_queue)
        else:
            remove_counter = int(*args)
            while remove_counter > 0:
                nums_queue.popleft()
                remove_counter -= 1
            return list(nums_queue)
    elif command == "remove" and position == "end":
        if not args:
            nums_queue.pop()
            return nums_queue
        else:
            remove_counter = int(*args)
            while remove_counter > 0:
                nums_queue.pop()
                remove_counter -= 1
            return nums_queue


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
