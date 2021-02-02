from Lab.fibonacci_sequence import *


def locate_fibonacci_numbers():
    while True:
        commands = input()
        if commands == "Stop":
            break

        actions = commands.split(" ")

        if actions[0] == "Create":
            print(" ".join(str(x) for x in create_sequence(int(actions[2]))))
        elif actions[0] == "Locate":
            print(locate(int(actions[1])))


locate_fibonacci_numbers()
