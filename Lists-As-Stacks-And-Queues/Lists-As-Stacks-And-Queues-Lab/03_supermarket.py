from collections import deque

names_q = deque()

END_CMD = "End"
PAID_CMD = "Paid"


while True:
    command = input()
    if command == END_CMD:
        print(f'{len(names_q)} people remaining.')
        break
    elif command == PAID_CMD:
        while names_q:
            print(names_q.popleft())
    else:
        names_q.append(command)

