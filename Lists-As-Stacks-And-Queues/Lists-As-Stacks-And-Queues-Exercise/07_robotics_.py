from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque()
products = deque()

for el in data:
    robot_data = el.split("-")
    robot = {}
    robot["name"] = robot_data[0]
    robot["speed"] = int(robot_data[1])
    robot["available"] = time
    robots.append(robot)
    available_robots.append(robot)

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

time += timedelta(seconds=1)

while products:
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available"] = time+timedelta(seconds=current_robot["speed"])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r["available"]:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot["available"] = time+timedelta(seconds=current_robot["speed"])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time += timedelta(seconds=1)
