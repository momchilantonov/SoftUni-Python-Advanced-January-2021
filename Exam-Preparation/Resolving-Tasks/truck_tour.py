from collections import deque


def take_pumps_data(pumps_qty):
    pumps_data = deque()
    for _ in range(pumps_qty):
        pumps_data.append([int(x) for x in input().split()])
    return pumps_data


def tank_calc(petrol, distance):
    tank = petrol-distance
    return tank


def is_reachable(tank):
    return tank >= 0


def research_path(pumps_data, pumps_qty):
    for pump in range(pumps_qty):
        is_this_pump = True
        tank = 0
        for p in range(pumps_qty):
            petrol_given = pumps_data[p][0]
            distance_to_next_pump = pumps_data[p][1]
            tank = tank + tank_calc(petrol_given, distance_to_next_pump)
            if is_reachable(tank):
                continue
            else:
                pumps_data.append(pumps_data.popleft())
                is_this_pump = False
                break
        if is_this_pump:
            print(pump)
            break


petrol_stations_qty = int(input())

pump_stations_data = take_pumps_data(petrol_stations_qty)
research_path(pump_stations_data, petrol_stations_qty)
