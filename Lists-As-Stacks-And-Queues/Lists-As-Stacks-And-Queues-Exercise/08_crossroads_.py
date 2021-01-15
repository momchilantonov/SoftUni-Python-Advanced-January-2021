from collections import deque

green_duration = int(input())
free_window = int(input())
cars = deque()
timer = 0
car_counter = 0
is_crashed = False

while True:
    command = input()
    if command == "END" or is_crashed:
        break

    if not command == "green":
        cars.append(command)
    else:
        if cars:
            while timer < green_duration:
                curr_car = cars.popleft()
                timer += len(curr_car)
                if timer <= green_duration:
                    car_counter += 1
                    if cars:
                        curr_car = cars.popleft()
                        left_time = green_duration-timer+free_window
                        while left_time > 0:
                            if len(curr_car) <= left_time and cars:
                                car_counter += 1
                                left_time -= len(curr_car)
                            else:
                                is_crashed = True
                                print(f"A crash happened!")
                                print(f"{curr_car} was hit at {curr_car[left_time]}.")
                                break
                    else:
                        timer = 0
                        break

if not is_crashed:
    print(f"Everyone is safe.")
    print(f"{car_counter} total cars passed the crossroads.")

# from collections import deque
#
# green_light = int(input())
# window = int(input())
#
# cars = deque()
# cars_counter = 0
# crashed = False
#
# command = input()
#
# while command != "END":
#     if command == "green":
#         if cars:
#             current = cars.popleft()
#             seconds_left = green_light-len(current)
#             while seconds_left > 0:
#                 cars_counter += 1
#                 if cars:
#                     current = cars.popleft()
#                     seconds_left -= len(current)
#                 else:
#                     break
#             if seconds_left == 0:
#                 cars_counter += 1
#             if window >= abs(seconds_left):
#                 if seconds_left < 0:
#                     cars_counter += 1
#             else:
#                 idx = window+seconds_left
#                 print("A crash happened!")
#                 print(f"{current} was hit at {current[idx]}.")
#                 crashed = True
#                 break
#     else:
#         cars.append(command)
#     command = input()
#
# if not crashed:
#     print("Everyone is safe.")
#     print(f"{cars_counter} total cars passed the crossroads.")
