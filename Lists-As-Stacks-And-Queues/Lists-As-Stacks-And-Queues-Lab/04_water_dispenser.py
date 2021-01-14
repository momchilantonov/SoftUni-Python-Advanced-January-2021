from collections import deque

START_CMD = "Start"
END_CMD = "End"
REFILL_CMD = "refill"

dispenser = int(input())

people_q = deque()

while True:
    command = input()
    if command == START_CMD:
        break
    people_q.append(command)


while True:
    command = input()
    if command == END_CMD:
        print(f"{dispenser} liters left")
        break
    if command.startswith(REFILL_CMD):
        command_params = command.split(" ")
        refill_litters = int(command_params[1])
        dispenser += refill_litters
    else:
        person = people_q.popleft()
        person_litters = int(command)
        if person_litters <= dispenser:
            print(f"{person} got water")
            dispenser -= person_litters
        else:
            print(f"{person} must wait")
