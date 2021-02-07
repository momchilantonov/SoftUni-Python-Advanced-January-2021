from collections import deque
from datetime import datetime, timedelta


def take_start_time(start_time):
    time = datetime.strptime(start_time, "%H:%M:%S")
    return time


def collect_robot_data(robots_info, time):
    robots = robots_info.split(";")
    robots_data = []
    free_robots = deque()
    for robot in robots:
        robot_data = {}
        robot_type, robot_speed = robot.split("-")
        robot_speed = int(robot_speed)
        robot_data["type"] = robot_type
        robot_data["speed"] = robot_speed
        robot_data["time"] = time
        robots_data.append(robot_data)
        free_robots.append(robot_data)
    return robots_data, free_robots


def collect_products_data():
    products = deque()
    while True:
        product = input()
        if product == "End":
            break
        products.append(product)
    return products


def start_process(robots_data, free_robots, products, time):
    t_delta = timedelta(seconds=1)
    time += t_delta
    while products:
        current_product = products.popleft()
        if free_robots:
            current_robot = free_robots.popleft()
            current_robot["time"] = time+timedelta(seconds=current_robot["speed"])
            print(f"{current_robot['type']} - {current_product} [{time.strftime('%H:%M:%S')}]")
        else:
            for robot in robots_data:
                if time >= robot["time"]:
                    free_robots.append(robot)
            if not free_robots:
                products.append(current_product)
            else:
                current_robot = free_robots.popleft()
                current_robot["time"] = time+timedelta(seconds=current_robot["speed"])
                print(f"{current_robot['type']} - {current_product} [{time.strftime('%H:%M:%S')}]")
        time += t_delta


robots_tech_info = input()
start_working_time = input()
working_time = take_start_time(start_working_time)
robots_tech_data, available_robots = collect_robot_data(robots_tech_info, working_time)
products_tech_data = collect_products_data()
start_process(robots_tech_data, available_robots, products_tech_data, working_time)
